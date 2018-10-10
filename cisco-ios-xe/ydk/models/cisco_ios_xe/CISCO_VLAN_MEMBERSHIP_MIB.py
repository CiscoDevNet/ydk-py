""" CISCO_VLAN_MEMBERSHIP_MIB 

The MIB module for the management of the VLAN
Membership within the frame  work of Cisco
VLAN Architecture, v 2.0 by Keith McCloghrie. The MIB
provides information on VLAN Membership Policy Servers
used by a device and VLAN membership assignments of
non\-trunk bridge ports of the device.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOVLANMEMBERSHIPMIB(Entity):
    """
    
    
    .. attribute:: vmvmps
    
    	
    	**type**\:  :py:class:`VmVmps <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CISCOVLANMEMBERSHIPMIB.VmVmps>`
    
    .. attribute:: vmmembership
    
    	
    	**type**\:  :py:class:`VmMembership <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CISCOVLANMEMBERSHIPMIB.VmMembership>`
    
    .. attribute:: vmstatistics
    
    	
    	**type**\:  :py:class:`VmStatistics <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CISCOVLANMEMBERSHIPMIB.VmStatistics>`
    
    .. attribute:: vmstatus
    
    	
    	**type**\:  :py:class:`VmStatus <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CISCOVLANMEMBERSHIPMIB.VmStatus>`
    
    .. attribute:: vmvmpstable
    
    	A table of VMPS to use. The device will use the the primary VMPS by default. If the device is unable to reach the primary server after vmVmpsRetries retries, it uses the first secondary server in the table until it runs out of secondary servers, in which case it will return to using the primary server. Entries in this table may be created and deleted via this MIB or the management console on a device
    	**type**\:  :py:class:`VmVmpsTable <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CISCOVLANMEMBERSHIPMIB.VmVmpsTable>`
    
    .. attribute:: vmmembershipsummarytable
    
    	A summary of VLAN membership of non\-trunk bridge ports. This is a convenience table for retrieving VLAN membership information.  A row is created for a VLAN if\: a) the VLAN exists, or b) a port is assigned to a non\-existent VLAN.  VLAN membership can only be modified via the vmMembershipTable
    	**type**\:  :py:class:`VmMembershipSummaryTable <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryTable>`
    
    .. attribute:: vmmembershiptable
    
    	A table for configuring VLAN port membership. There is one row for each bridge port that is assigned to a static or dynamic access port. Trunk ports are not  represented in this table.  An entry may be created and deleted when ports are created or deleted via SNMP or the management console on a  device
    	**type**\:  :py:class:`VmMembershipTable <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CISCOVLANMEMBERSHIPMIB.VmMembershipTable>`
    
    .. attribute:: vmmembershipsummaryexttable
    
    	A summary of VLAN membership of non\-trunk bridge ports. This table is used for  retrieving VLAN membership information for the device which supports dot1dBasePort  with value greater than 2048.  A row is created for a VLAN and a particular bridge port range, where at least one port  in the range is assigned to this VLAN.  VLAN membership can only be modified via the vmMembershipTable
    	**type**\:  :py:class:`VmMembershipSummaryExtTable <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryExtTable>`
    
    .. attribute:: vmvoicevlantable
    
    	A table for configuring the Voice VLAN\-ID for the ports. An entry will exist for each interface which supports Voice Vlan feature
    	**type**\:  :py:class:`VmVoiceVlanTable <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CISCOVLANMEMBERSHIPMIB.VmVoiceVlanTable>`
    
    

    """

    _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
    _revision = '2007-12-14'

    def __init__(self):
        super(CISCOVLANMEMBERSHIPMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-VLAN-MEMBERSHIP-MIB"
        self.yang_parent_name = "CISCO-VLAN-MEMBERSHIP-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vmVmps", ("vmvmps", CISCOVLANMEMBERSHIPMIB.VmVmps)), ("vmMembership", ("vmmembership", CISCOVLANMEMBERSHIPMIB.VmMembership)), ("vmStatistics", ("vmstatistics", CISCOVLANMEMBERSHIPMIB.VmStatistics)), ("vmStatus", ("vmstatus", CISCOVLANMEMBERSHIPMIB.VmStatus)), ("vmVmpsTable", ("vmvmpstable", CISCOVLANMEMBERSHIPMIB.VmVmpsTable)), ("vmMembershipSummaryTable", ("vmmembershipsummarytable", CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryTable)), ("vmMembershipTable", ("vmmembershiptable", CISCOVLANMEMBERSHIPMIB.VmMembershipTable)), ("vmMembershipSummaryExtTable", ("vmmembershipsummaryexttable", CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryExtTable)), ("vmVoiceVlanTable", ("vmvoicevlantable", CISCOVLANMEMBERSHIPMIB.VmVoiceVlanTable))])
        self._leafs = OrderedDict()

        self.vmvmps = CISCOVLANMEMBERSHIPMIB.VmVmps()
        self.vmvmps.parent = self
        self._children_name_map["vmvmps"] = "vmVmps"

        self.vmmembership = CISCOVLANMEMBERSHIPMIB.VmMembership()
        self.vmmembership.parent = self
        self._children_name_map["vmmembership"] = "vmMembership"

        self.vmstatistics = CISCOVLANMEMBERSHIPMIB.VmStatistics()
        self.vmstatistics.parent = self
        self._children_name_map["vmstatistics"] = "vmStatistics"

        self.vmstatus = CISCOVLANMEMBERSHIPMIB.VmStatus()
        self.vmstatus.parent = self
        self._children_name_map["vmstatus"] = "vmStatus"

        self.vmvmpstable = CISCOVLANMEMBERSHIPMIB.VmVmpsTable()
        self.vmvmpstable.parent = self
        self._children_name_map["vmvmpstable"] = "vmVmpsTable"

        self.vmmembershipsummarytable = CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryTable()
        self.vmmembershipsummarytable.parent = self
        self._children_name_map["vmmembershipsummarytable"] = "vmMembershipSummaryTable"

        self.vmmembershiptable = CISCOVLANMEMBERSHIPMIB.VmMembershipTable()
        self.vmmembershiptable.parent = self
        self._children_name_map["vmmembershiptable"] = "vmMembershipTable"

        self.vmmembershipsummaryexttable = CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryExtTable()
        self.vmmembershipsummaryexttable.parent = self
        self._children_name_map["vmmembershipsummaryexttable"] = "vmMembershipSummaryExtTable"

        self.vmvoicevlantable = CISCOVLANMEMBERSHIPMIB.VmVoiceVlanTable()
        self.vmvoicevlantable.parent = self
        self._children_name_map["vmvoicevlantable"] = "vmVoiceVlanTable"
        self._segment_path = lambda: "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOVLANMEMBERSHIPMIB, [], name, value)


    class VmVmps(Entity):
        """
        
        
        .. attribute:: vmvmpsvqpversion
        
        	The VLAN Query Protocol (VQP) version supported on the device. VQP is the protocol used to query VLAN Membership Policy Server (VMPS) for VLAN membership assignments of dynamic VLAN ports. A VMPS provides VLAN membership policy assignments based on the content of the packets received on a port
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: vmvmpsretries
        
        	The number of retries for VQP requests to a VMPS before using the next available VMPS
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: vmvmpsreconfirminterval
        
        	The switch will reconfirm membership of addresses on each port with VMPS periodically. This object specifies the interval to perform reconfirmation. If the value is set to 0, the switch does not reconfirm membership with VMPS
        	**type**\: int
        
        	**range:** 0..120
        
        	**units**\: Minutes
        
        .. attribute:: vmvmpsreconfirm
        
        	Setting this object to execute(2) causes the switch to reconfirm membership of every dynamic port. Reading this object always return ready(1)
        	**type**\:  :py:class:`VmVmpsReconfirm <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CISCOVLANMEMBERSHIPMIB.VmVmps.VmVmpsReconfirm>`
        
        .. attribute:: vmvmpsreconfirmresult
        
        	This object returns the result of the last request that sets vmVmpsReconfirm to execute(2). The semantics of the possible results are as follows\:       other(1)           \- none of following      inProgress(2)      \- reconfirm in progress      success(3)         \- reconfirm completed successfully      noResponse(4)      \- reconfirm failed because no                           VMPS responded      noVmps(5)          \- No VMPS configured      noDynamicPort(6)   \- No dynamic ports configured      noHostConnected(7) \- No hosts on dynamic ports
        	**type**\:  :py:class:`VmVmpsReconfirmResult <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CISCOVLANMEMBERSHIPMIB.VmVmps.VmVmpsReconfirmResult>`
        
        .. attribute:: vmvmpscurrent
        
        	This is the IpAddress of the current VMPS used
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        

        """

        _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
        _revision = '2007-12-14'

        def __init__(self):
            super(CISCOVLANMEMBERSHIPMIB.VmVmps, self).__init__()

            self.yang_name = "vmVmps"
            self.yang_parent_name = "CISCO-VLAN-MEMBERSHIP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('vmvmpsvqpversion', (YLeaf(YType.int32, 'vmVmpsVQPVersion'), ['int'])),
                ('vmvmpsretries', (YLeaf(YType.int32, 'vmVmpsRetries'), ['int'])),
                ('vmvmpsreconfirminterval', (YLeaf(YType.int32, 'vmVmpsReconfirmInterval'), ['int'])),
                ('vmvmpsreconfirm', (YLeaf(YType.enumeration, 'vmVmpsReconfirm'), [('ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB', 'VmVmps.VmVmpsReconfirm')])),
                ('vmvmpsreconfirmresult', (YLeaf(YType.enumeration, 'vmVmpsReconfirmResult'), [('ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB', 'VmVmps.VmVmpsReconfirmResult')])),
                ('vmvmpscurrent', (YLeaf(YType.str, 'vmVmpsCurrent'), ['str'])),
            ])
            self.vmvmpsvqpversion = None
            self.vmvmpsretries = None
            self.vmvmpsreconfirminterval = None
            self.vmvmpsreconfirm = None
            self.vmvmpsreconfirmresult = None
            self.vmvmpscurrent = None
            self._segment_path = lambda: "vmVmps"
            self._absolute_path = lambda: "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVLANMEMBERSHIPMIB.VmVmps, ['vmvmpsvqpversion', 'vmvmpsretries', 'vmvmpsreconfirminterval', 'vmvmpsreconfirm', 'vmvmpsreconfirmresult', 'vmvmpscurrent'], name, value)

        class VmVmpsReconfirm(Enum):
            """
            VmVmpsReconfirm (Enum Class)

            Setting this object to execute(2) causes the switch

            to reconfirm membership of every dynamic port.

            Reading this object always return ready(1).

            .. data:: ready = 1

            .. data:: execute = 2

            """

            ready = Enum.YLeaf(1, "ready")

            execute = Enum.YLeaf(2, "execute")


        class VmVmpsReconfirmResult(Enum):
            """
            VmVmpsReconfirmResult (Enum Class)

            This object returns the result of the last request

            that sets vmVmpsReconfirm to execute(2). The

            semantics of the possible results are as follows\:

                 other(1)           \- none of following

                 inProgress(2)      \- reconfirm in progress

                 success(3)         \- reconfirm completed successfully

                 noResponse(4)      \- reconfirm failed because no

                                      VMPS responded

                 noVmps(5)          \- No VMPS configured

                 noDynamicPort(6)   \- No dynamic ports configured

                 noHostConnected(7) \- No hosts on dynamic ports

            .. data:: other = 1

            .. data:: inProgress = 2

            .. data:: success = 3

            .. data:: noResponse = 4

            .. data:: noVmps = 5

            .. data:: noDynamicPort = 6

            .. data:: noHostConnected = 7

            """

            other = Enum.YLeaf(1, "other")

            inProgress = Enum.YLeaf(2, "inProgress")

            success = Enum.YLeaf(3, "success")

            noResponse = Enum.YLeaf(4, "noResponse")

            noVmps = Enum.YLeaf(5, "noVmps")

            noDynamicPort = Enum.YLeaf(6, "noDynamicPort")

            noHostConnected = Enum.YLeaf(7, "noHostConnected")



    class VmMembership(Entity):
        """
        
        
        .. attribute:: vmvlancreationmode
        
        	This object is used to determine whether or not a non\-existing VLAN will be created automatically by the system after assigned to a port.  automatic(1)\:  a non\-existing VLAN will be created                automatically by the system after                assigned to a port.  manual(2)\:     a non\-existing VLAN will not be created                automatically by the system and need to be                manually created by the users after assigned                to a port
        	**type**\:  :py:class:`VmVlanCreationMode <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CISCOVLANMEMBERSHIPMIB.VmMembership.VmVlanCreationMode>`
        
        

        """

        _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
        _revision = '2007-12-14'

        def __init__(self):
            super(CISCOVLANMEMBERSHIPMIB.VmMembership, self).__init__()

            self.yang_name = "vmMembership"
            self.yang_parent_name = "CISCO-VLAN-MEMBERSHIP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('vmvlancreationmode', (YLeaf(YType.enumeration, 'vmVlanCreationMode'), [('ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB', 'VmMembership.VmVlanCreationMode')])),
            ])
            self.vmvlancreationmode = None
            self._segment_path = lambda: "vmMembership"
            self._absolute_path = lambda: "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVLANMEMBERSHIPMIB.VmMembership, ['vmvlancreationmode'], name, value)

        class VmVlanCreationMode(Enum):
            """
            VmVlanCreationMode (Enum Class)

            This object is used to determine whether or not

            a non\-existing VLAN will be created automatically

            by the system after assigned to a port.

            automatic(1)\:  a non\-existing VLAN will be created

                           automatically by the system after

                           assigned to a port.

            manual(2)\:     a non\-existing VLAN will not be created

                           automatically by the system and need to be

                           manually created by the users after assigned

                           to a port.

            .. data:: automatic = 1

            .. data:: manual = 2

            """

            automatic = Enum.YLeaf(1, "automatic")

            manual = Enum.YLeaf(2, "manual")



    class VmStatistics(Entity):
        """
        
        
        .. attribute:: vmvqpqueries
        
        	The total number of VQP requests sent by this device to all VMPS since last system re\-initialization
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vmvqpresponses
        
        	The number of VQP responses received by this device from all VMPS since last system re\-initialization
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vmvmpschanges
        
        	The number of times, since last system re\-initialization, the current VMPS was changed. The current VMPS is changed whenever the VMPS fails to  response after vmVmpsRetries of a VQP request
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vmvqpshutdown
        
        	The number of times, since last system re\-initialization, a VQP response indicates  'shutdown'. A 'shutdown' response is a result of  the membership policy configured at a VMPS by the administrator
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vmvqpdenied
        
        	The number of times, since last system re\-initialization, a VQP response indicates  'denied'. A 'denied' response is a result of  the membership policy configured at a VMPS by the administrator
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vmvqpwrongdomain
        
        	The number of times, since last system re\-initialization, a VQP response indicates wrong  management domain. A wrong management domain  response indicates that the VMPS used serves a  management domain that is different from the device's management domain
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vmvqpwrongversion
        
        	The number of times, since last system re\-initialization, a VQP response indicates wrong  VQP version. A wrong VQP version response  indicates that the VMPS used supports a VQP  version that is different from the device's  VQP version
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vminsufficientresources
        
        	The number of times, since last system re\-initialization, a VQP response indicates  insufficient resources. An insufficient resources  response indicates that the VMPS used does not  have the required resources to verify the membership assignment requested
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
        _revision = '2007-12-14'

        def __init__(self):
            super(CISCOVLANMEMBERSHIPMIB.VmStatistics, self).__init__()

            self.yang_name = "vmStatistics"
            self.yang_parent_name = "CISCO-VLAN-MEMBERSHIP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('vmvqpqueries', (YLeaf(YType.uint32, 'vmVQPQueries'), ['int'])),
                ('vmvqpresponses', (YLeaf(YType.uint32, 'vmVQPResponses'), ['int'])),
                ('vmvmpschanges', (YLeaf(YType.uint32, 'vmVmpsChanges'), ['int'])),
                ('vmvqpshutdown', (YLeaf(YType.uint32, 'vmVQPShutdown'), ['int'])),
                ('vmvqpdenied', (YLeaf(YType.uint32, 'vmVQPDenied'), ['int'])),
                ('vmvqpwrongdomain', (YLeaf(YType.uint32, 'vmVQPWrongDomain'), ['int'])),
                ('vmvqpwrongversion', (YLeaf(YType.uint32, 'vmVQPWrongVersion'), ['int'])),
                ('vminsufficientresources', (YLeaf(YType.uint32, 'vmInsufficientResources'), ['int'])),
            ])
            self.vmvqpqueries = None
            self.vmvqpresponses = None
            self.vmvmpschanges = None
            self.vmvqpshutdown = None
            self.vmvqpdenied = None
            self.vmvqpwrongdomain = None
            self.vmvqpwrongversion = None
            self.vminsufficientresources = None
            self._segment_path = lambda: "vmStatistics"
            self._absolute_path = lambda: "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVLANMEMBERSHIPMIB.VmStatistics, ['vmvqpqueries', 'vmvqpresponses', 'vmvmpschanges', 'vmvqpshutdown', 'vmvqpdenied', 'vmvqpwrongdomain', 'vmvqpwrongversion', 'vminsufficientresources'], name, value)


    class VmStatus(Entity):
        """
        
        
        .. attribute:: vmnotificationsenabled
        
        	An indication of whether the notifications/traps defined in this MIB are enabled
        	**type**\: bool
        
        

        """

        _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
        _revision = '2007-12-14'

        def __init__(self):
            super(CISCOVLANMEMBERSHIPMIB.VmStatus, self).__init__()

            self.yang_name = "vmStatus"
            self.yang_parent_name = "CISCO-VLAN-MEMBERSHIP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('vmnotificationsenabled', (YLeaf(YType.boolean, 'vmNotificationsEnabled'), ['bool'])),
            ])
            self.vmnotificationsenabled = None
            self._segment_path = lambda: "vmStatus"
            self._absolute_path = lambda: "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVLANMEMBERSHIPMIB.VmStatus, ['vmnotificationsenabled'], name, value)


    class VmVmpsTable(Entity):
        """
        A table of VMPS to use. The device will use
        the the primary VMPS by default. If the
        device is unable to reach the primary server
        after vmVmpsRetries retries, it uses the first
        secondary server in the table until it runs out
        of secondary servers, in which case it will return
        to using the primary server. Entries in this table
        may be created and deleted via this MIB or
        the management console on a device.
        
        .. attribute:: vmvmpsentry
        
        	An entry (conceptual row) in the vmVmpsTable
        	**type**\: list of  		 :py:class:`VmVmpsEntry <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CISCOVLANMEMBERSHIPMIB.VmVmpsTable.VmVmpsEntry>`
        
        

        """

        _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
        _revision = '2007-12-14'

        def __init__(self):
            super(CISCOVLANMEMBERSHIPMIB.VmVmpsTable, self).__init__()

            self.yang_name = "vmVmpsTable"
            self.yang_parent_name = "CISCO-VLAN-MEMBERSHIP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vmVmpsEntry", ("vmvmpsentry", CISCOVLANMEMBERSHIPMIB.VmVmpsTable.VmVmpsEntry))])
            self._leafs = OrderedDict()

            self.vmvmpsentry = YList(self)
            self._segment_path = lambda: "vmVmpsTable"
            self._absolute_path = lambda: "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVLANMEMBERSHIPMIB.VmVmpsTable, [], name, value)


        class VmVmpsEntry(Entity):
            """
            An entry (conceptual row) in the vmVmpsTable.
            
            .. attribute:: vmvmpsipaddress  (key)
            
            	The Ip Address of the VMPS
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: vmvmpsprimary
            
            	The status of the VMPS. Setting this value to true will make this VMPS the primary server and make the switch use this as the current server. Setting this entry to true causes other rows to transition to false. Attempting to write a value of false after creation will result in a return of bad value. Deleting an entry whose value is true will result in the first entry in the table being set to true
            	**type**\: bool
            
            .. attribute:: vmvmpsrowstatus
            
            	The status of this conceptual row
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
            _revision = '2007-12-14'

            def __init__(self):
                super(CISCOVLANMEMBERSHIPMIB.VmVmpsTable.VmVmpsEntry, self).__init__()

                self.yang_name = "vmVmpsEntry"
                self.yang_parent_name = "vmVmpsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vmvmpsipaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('vmvmpsipaddress', (YLeaf(YType.str, 'vmVmpsIpAddress'), ['str'])),
                    ('vmvmpsprimary', (YLeaf(YType.boolean, 'vmVmpsPrimary'), ['bool'])),
                    ('vmvmpsrowstatus', (YLeaf(YType.enumeration, 'vmVmpsRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.vmvmpsipaddress = None
                self.vmvmpsprimary = None
                self.vmvmpsrowstatus = None
                self._segment_path = lambda: "vmVmpsEntry" + "[vmVmpsIpAddress='" + str(self.vmvmpsipaddress) + "']"
                self._absolute_path = lambda: "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/vmVmpsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVLANMEMBERSHIPMIB.VmVmpsTable.VmVmpsEntry, ['vmvmpsipaddress', 'vmvmpsprimary', 'vmvmpsrowstatus'], name, value)


    class VmMembershipSummaryTable(Entity):
        """
        A summary of VLAN membership of non\-trunk
        bridge ports. This is a convenience table
        for retrieving VLAN membership information.
        
        A row is created for a VLAN if\:
        a) the VLAN exists, or
        b) a port is assigned to a non\-existent VLAN.
        
        VLAN membership can only be modified via the
        vmMembershipTable.
        
        .. attribute:: vmmembershipsummaryentry
        
        	An entry (conceptual row) in the vmMembershipSummaryTable
        	**type**\: list of  		 :py:class:`VmMembershipSummaryEntry <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryTable.VmMembershipSummaryEntry>`
        
        

        """

        _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
        _revision = '2007-12-14'

        def __init__(self):
            super(CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryTable, self).__init__()

            self.yang_name = "vmMembershipSummaryTable"
            self.yang_parent_name = "CISCO-VLAN-MEMBERSHIP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vmMembershipSummaryEntry", ("vmmembershipsummaryentry", CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryTable.VmMembershipSummaryEntry))])
            self._leafs = OrderedDict()

            self.vmmembershipsummaryentry = YList(self)
            self._segment_path = lambda: "vmMembershipSummaryTable"
            self._absolute_path = lambda: "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryTable, [], name, value)


        class VmMembershipSummaryEntry(Entity):
            """
            An entry (conceptual row) in the
            vmMembershipSummaryTable.
            
            .. attribute:: vmmembershipsummaryvlanindex  (key)
            
            	The VLAN id of the VLAN
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vmmembershipsummarymemberports
            
            	The set of the device's member ports that belong to the VLAN.  Each octet within the value of this object specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc.   Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port.  Thus, each port of the VLAN is represented by a single bit within the value of this object.  If that bit has a value of '1' then that port is included in the set of ports; the port is not included if its bit has a value of '0'.  A port number is the value of dot1dBasePort for the port in the BRIDGE\-MIB (RFC 1493)
            	**type**\: str
            
            	**length:** 0..128
            
            	**status**\: deprecated
            
            .. attribute:: vmmembershipsummarymember2kports
            
            	The set of the device's member ports that belong to the VLAN. It has the VLAN membership information of up to 2048 ports with the port number from 1 to  2048.  Each octet within the value of this object specifies a set of eight ports, with the first octet specifying  ports 1 through 8, the second octet specifying ports 9 through 16, etc.   Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port.  Thus, each port of the VLAN is represented by a single bit within the value of this object.  If that bit has a value of '1' then that port is included in the set of ports; the port is not included if its bit has a value of '0'.  A port number is the value of dot1dBasePort for the port in the BRIDGE\-MIB (RFC 1493)
            	**type**\: str
            
            	**length:** 0..256
            
            

            """

            _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
            _revision = '2007-12-14'

            def __init__(self):
                super(CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryTable.VmMembershipSummaryEntry, self).__init__()

                self.yang_name = "vmMembershipSummaryEntry"
                self.yang_parent_name = "vmMembershipSummaryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vmmembershipsummaryvlanindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('vmmembershipsummaryvlanindex', (YLeaf(YType.int32, 'vmMembershipSummaryVlanIndex'), ['int'])),
                    ('vmmembershipsummarymemberports', (YLeaf(YType.str, 'vmMembershipSummaryMemberPorts'), ['str'])),
                    ('vmmembershipsummarymember2kports', (YLeaf(YType.str, 'vmMembershipSummaryMember2kPorts'), ['str'])),
                ])
                self.vmmembershipsummaryvlanindex = None
                self.vmmembershipsummarymemberports = None
                self.vmmembershipsummarymember2kports = None
                self._segment_path = lambda: "vmMembershipSummaryEntry" + "[vmMembershipSummaryVlanIndex='" + str(self.vmmembershipsummaryvlanindex) + "']"
                self._absolute_path = lambda: "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/vmMembershipSummaryTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryTable.VmMembershipSummaryEntry, ['vmmembershipsummaryvlanindex', 'vmmembershipsummarymemberports', 'vmmembershipsummarymember2kports'], name, value)


    class VmMembershipTable(Entity):
        """
        A table for configuring VLAN port membership.
        There is one row for each bridge port that is
        assigned to a static or dynamic access port. Trunk
        ports are not  represented in this table.  An entry
        may be created and deleted when ports are created or
        deleted via SNMP or the management console on a 
        device.
        
        .. attribute:: vmmembershipentry
        
        	An entry (conceptual row) in the vmMembershipTable
        	**type**\: list of  		 :py:class:`VmMembershipEntry <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CISCOVLANMEMBERSHIPMIB.VmMembershipTable.VmMembershipEntry>`
        
        

        """

        _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
        _revision = '2007-12-14'

        def __init__(self):
            super(CISCOVLANMEMBERSHIPMIB.VmMembershipTable, self).__init__()

            self.yang_name = "vmMembershipTable"
            self.yang_parent_name = "CISCO-VLAN-MEMBERSHIP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vmMembershipEntry", ("vmmembershipentry", CISCOVLANMEMBERSHIPMIB.VmMembershipTable.VmMembershipEntry))])
            self._leafs = OrderedDict()

            self.vmmembershipentry = YList(self)
            self._segment_path = lambda: "vmMembershipTable"
            self._absolute_path = lambda: "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVLANMEMBERSHIPMIB.VmMembershipTable, [], name, value)


        class VmMembershipEntry(Entity):
            """
            An entry (conceptual row) in the vmMembershipTable.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: vmvlantype
            
            	The type of VLAN membership assigned to this port. A port with static vlan membership is assigned to a single VLAN directly. A port with dynamic membership is assigned a single VLAN based on content of packets received on the port and via VQP queries to VMPS. A port with multiVlan membership may be assigned to one or more VLANs directly.  A static or dynamic port membership is specified by the value of vmVlan. A multiVlan port membership is specified by the value of vmVlans
            	**type**\:  :py:class:`VmVlanType <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CISCOVLANMEMBERSHIPMIB.VmMembershipTable.VmMembershipEntry.VmVlanType>`
            
            .. attribute:: vmvlan
            
            	The VLAN id of the VLAN the port is assigned to when vmVlanType is set to static or dynamic. This object is not instantiated if not applicable.  The value may be 0 if the port is not assigned to a VLAN.  If vmVlanType is static, the port is always assigned to a VLAN and the object may not be set to 0.  If vmVlanType is dynamic the object's value is 0 if the port is currently not assigned to a VLAN. In addition, the object may be set to 0 only
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vmportstatus
            
            	An indication of the current VLAN status of the port. A status of inactive(1) indicates that a dynamic port does not yet have a VLAN assigned, or a port is  assigned to a VLAN that is currently not active. A  status of active(2) indicates that the currently  assigned VLAN is active. A status of shutdown(3)  indicates that the port has been disabled as a result of VQP shutdown response
            	**type**\:  :py:class:`VmPortStatus <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CISCOVLANMEMBERSHIPMIB.VmMembershipTable.VmMembershipEntry.VmPortStatus>`
            
            .. attribute:: vmvlans
            
            	The VLAN(s) the port is assigned to when the port's vmVlanType is set to multiVlan. This object is not instantiated if not applicable.  The port is always assigned to one or more VLANs and the object may not be set so that there are no vlans assigned.  Each octet within the value of this object specifies a set of eight VLANs, with the first octet specifying VLAN id 1 through 8, the second octet specifying VLAN ids 9 through 16, etc.   Within each octet, the most significant bit represents the lowest numbered VLAN id, and the least significant bit represents the highest numbered VLAN id.  Thus, each VLAN of the port is represented by a single bit within the value of this object.  If that bit has a value of '1' then that VLAN is included in the set of VLANs; the VLAN is not included if its bit has a value of '0'
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: vmvlans2k
            
            	The VLAN(s) the port is assigned to when the port's vmVlanType is set to multiVlan. This object is not instantiated if not applicable.  The port is always assigned to one or more VLANs and the object may not be set so that there are no vlans assigned.  Each octet within the value of this object specifies a set of eight VLANs, with the first octet specifying VLAN id 1024 through 1031, the second octet specifying  VLAN ids 1032 through 1039, etc.  Within each octet,  the most significant bit represents the lowest  numbered VLAN id, and the least significant bit  represents the highest numbered VLAN id.  Thus, each  VLAN of the port is represented by a single bit within the value of this object.  If that bit has a value of '1' then that VLAN is included in the set of VLANs; the VLAN is not included if its bit has a value of '0'
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: vmvlans3k
            
            	The VLAN(s) the port is assigned to when the port's vmVlanType is set to multiVlan. This object is not instantiated if not applicable.  The port is always assigned to one or more VLANs and the object may not be set so that there are no vlans assigned.  Each octet within the value of this object specifies a set of eight VLANs, with the first octet specifying VLAN id 2048 through 2055, the second octet specifying  VLAN ids 2056 through 2063, etc.   Within each octet,  the most significant bit represents the lowest  numbered VLAN id, and the least significant bit  represents the highest numbered VLAN id.  Thus, each VLAN of the port is represented by a single bit within the value of this object.  If that bit has a value of '1' then that VLAN is included in the set of VLANs; the VLAN is not included if its bit has a value of '0'
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: vmvlans4k
            
            	The VLAN(s) the port is assigned to when the port's vmVlanType is set to multiVlan. This object is not instantiated if not applicable.  The port is always assigned to one or more VLANs and the object may not be set so that there are no vlans assigned.  Each octet within the value of this object specifies a set of eight VLANs, with the first octet specifying VLAN id 3072 through 3079, the second octet specifying  VLAN ids 3040 through 3047, etc.   Within each octet,  the most significant bit represents the lowest  numbered VLAN id, and the least significant bit  represents the highest numbered VLAN id.  Thus, each VLAN of the port is represented by a single bit within the value of this object.  If that bit has a value of '1' then that VLAN is included in the set of VLANs; the VLAN is not included if its bit has a value of '0'
            	**type**\: str
            
            	**length:** 0..128
            
            

            """

            _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
            _revision = '2007-12-14'

            def __init__(self):
                super(CISCOVLANMEMBERSHIPMIB.VmMembershipTable.VmMembershipEntry, self).__init__()

                self.yang_name = "vmMembershipEntry"
                self.yang_parent_name = "vmMembershipTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('vmvlantype', (YLeaf(YType.enumeration, 'vmVlanType'), [('ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB', 'VmMembershipTable.VmMembershipEntry.VmVlanType')])),
                    ('vmvlan', (YLeaf(YType.int32, 'vmVlan'), ['int'])),
                    ('vmportstatus', (YLeaf(YType.enumeration, 'vmPortStatus'), [('ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB', 'CISCOVLANMEMBERSHIPMIB', 'VmMembershipTable.VmMembershipEntry.VmPortStatus')])),
                    ('vmvlans', (YLeaf(YType.str, 'vmVlans'), ['str'])),
                    ('vmvlans2k', (YLeaf(YType.str, 'vmVlans2k'), ['str'])),
                    ('vmvlans3k', (YLeaf(YType.str, 'vmVlans3k'), ['str'])),
                    ('vmvlans4k', (YLeaf(YType.str, 'vmVlans4k'), ['str'])),
                ])
                self.ifindex = None
                self.vmvlantype = None
                self.vmvlan = None
                self.vmportstatus = None
                self.vmvlans = None
                self.vmvlans2k = None
                self.vmvlans3k = None
                self.vmvlans4k = None
                self._segment_path = lambda: "vmMembershipEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/vmMembershipTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVLANMEMBERSHIPMIB.VmMembershipTable.VmMembershipEntry, ['ifindex', 'vmvlantype', 'vmvlan', 'vmportstatus', 'vmvlans', 'vmvlans2k', 'vmvlans3k', 'vmvlans4k'], name, value)

            class VmPortStatus(Enum):
                """
                VmPortStatus (Enum Class)

                An indication of the current VLAN status of the port.

                A status of inactive(1) indicates that a dynamic port

                does not yet have a VLAN assigned, or a port is 

                assigned to a VLAN that is currently not active. A 

                status of active(2) indicates that the currently 

                assigned VLAN is active. A status of shutdown(3) 

                indicates that the port has been disabled as a result

                of VQP shutdown response.

                .. data:: inactive = 1

                .. data:: active = 2

                .. data:: shutdown = 3

                """

                inactive = Enum.YLeaf(1, "inactive")

                active = Enum.YLeaf(2, "active")

                shutdown = Enum.YLeaf(3, "shutdown")


            class VmVlanType(Enum):
                """
                VmVlanType (Enum Class)

                The type of VLAN membership assigned to this port.

                A port with static vlan membership is assigned to a

                single VLAN directly. A port with dynamic membership

                is assigned a single VLAN based on content of packets

                received on the port and via VQP queries to VMPS.

                A port with multiVlan membership may be assigned to

                one or more VLANs directly.

                A static or dynamic port membership is specified

                by the value of vmVlan. A multiVlan port membership is

                specified by the value of vmVlans.

                .. data:: static = 1

                .. data:: dynamic = 2

                .. data:: multiVlan = 3

                """

                static = Enum.YLeaf(1, "static")

                dynamic = Enum.YLeaf(2, "dynamic")

                multiVlan = Enum.YLeaf(3, "multiVlan")



    class VmMembershipSummaryExtTable(Entity):
        """
        A summary of VLAN membership of non\-trunk
        bridge ports. This table is used for 
        retrieving VLAN membership information
        for the device which supports dot1dBasePort 
        with value greater than 2048.
        
        A row is created for a VLAN and a particular
        bridge port range, where at least one port 
        in the range is assigned to this VLAN.
        
        VLAN membership can only be modified via the
        vmMembershipTable.
        
        .. attribute:: vmmembershipsummaryextentry
        
        	An entry (conceptual row) in the vmMembershipSummaryExtTable
        	**type**\: list of  		 :py:class:`VmMembershipSummaryExtEntry <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryExtTable.VmMembershipSummaryExtEntry>`
        
        

        """

        _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
        _revision = '2007-12-14'

        def __init__(self):
            super(CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryExtTable, self).__init__()

            self.yang_name = "vmMembershipSummaryExtTable"
            self.yang_parent_name = "CISCO-VLAN-MEMBERSHIP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vmMembershipSummaryExtEntry", ("vmmembershipsummaryextentry", CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryExtTable.VmMembershipSummaryExtEntry))])
            self._leafs = OrderedDict()

            self.vmmembershipsummaryextentry = YList(self)
            self._segment_path = lambda: "vmMembershipSummaryExtTable"
            self._absolute_path = lambda: "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryExtTable, [], name, value)


        class VmMembershipSummaryExtEntry(Entity):
            """
            An entry (conceptual row) in the
            vmMembershipSummaryExtTable.
            
            .. attribute:: vmmembershipsummaryvlanindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`vmmembershipsummaryvlanindex <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryTable.VmMembershipSummaryEntry>`
            
            .. attribute:: vmmembershipportrangeindex  (key)
            
            	The bridge port range index of this row
            	**type**\:  :py:class:`CiscoPortListRange <ydk.models.cisco_ios_xe.CISCO_TC.CiscoPortListRange>`
            
            .. attribute:: vmmembershipsummaryextports
            
            	The set of the device's member ports that belong to the VLAN. It has the VLAN membership information of up to 2k ports with the port number starting from the information indicated in vmMembershipPortRangeIndex object of the same row. For example, if the value of vmMembershipPortRangeIndex is 'twoKto4K', the port number indicated in this object starting from 2049 and ending to 4096.   A port number is the value of dot1dBasePort for the port in the BRIDGE\-MIB (RFC 1493)
            	**type**\: str
            
            	**length:** 0..256
            
            

            """

            _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
            _revision = '2007-12-14'

            def __init__(self):
                super(CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryExtTable.VmMembershipSummaryExtEntry, self).__init__()

                self.yang_name = "vmMembershipSummaryExtEntry"
                self.yang_parent_name = "vmMembershipSummaryExtTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vmmembershipsummaryvlanindex','vmmembershipportrangeindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('vmmembershipsummaryvlanindex', (YLeaf(YType.str, 'vmMembershipSummaryVlanIndex'), ['int'])),
                    ('vmmembershipportrangeindex', (YLeaf(YType.enumeration, 'vmMembershipPortRangeIndex'), [('ydk.models.cisco_ios_xe.CISCO_TC', 'CiscoPortListRange', '')])),
                    ('vmmembershipsummaryextports', (YLeaf(YType.str, 'vmMembershipSummaryExtPorts'), ['str'])),
                ])
                self.vmmembershipsummaryvlanindex = None
                self.vmmembershipportrangeindex = None
                self.vmmembershipsummaryextports = None
                self._segment_path = lambda: "vmMembershipSummaryExtEntry" + "[vmMembershipSummaryVlanIndex='" + str(self.vmmembershipsummaryvlanindex) + "']" + "[vmMembershipPortRangeIndex='" + str(self.vmmembershipportrangeindex) + "']"
                self._absolute_path = lambda: "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/vmMembershipSummaryExtTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVLANMEMBERSHIPMIB.VmMembershipSummaryExtTable.VmMembershipSummaryExtEntry, ['vmmembershipsummaryvlanindex', 'vmmembershipportrangeindex', 'vmmembershipsummaryextports'], name, value)


    class VmVoiceVlanTable(Entity):
        """
        A table for configuring the Voice VLAN\-ID
        for the ports. An entry will exist for each
        interface which supports Voice Vlan feature.
        
        .. attribute:: vmvoicevlanentry
        
        	An entry (conceptual row) in the vmVoiceVlanTable. Only interfaces which support Voice Vlan feature are shown
        	**type**\: list of  		 :py:class:`VmVoiceVlanEntry <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CISCOVLANMEMBERSHIPMIB.VmVoiceVlanTable.VmVoiceVlanEntry>`
        
        

        """

        _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
        _revision = '2007-12-14'

        def __init__(self):
            super(CISCOVLANMEMBERSHIPMIB.VmVoiceVlanTable, self).__init__()

            self.yang_name = "vmVoiceVlanTable"
            self.yang_parent_name = "CISCO-VLAN-MEMBERSHIP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vmVoiceVlanEntry", ("vmvoicevlanentry", CISCOVLANMEMBERSHIPMIB.VmVoiceVlanTable.VmVoiceVlanEntry))])
            self._leafs = OrderedDict()

            self.vmvoicevlanentry = YList(self)
            self._segment_path = lambda: "vmVoiceVlanTable"
            self._absolute_path = lambda: "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVLANMEMBERSHIPMIB.VmVoiceVlanTable, [], name, value)


        class VmVoiceVlanEntry(Entity):
            """
            An entry (conceptual row) in the vmVoiceVlanTable.
            Only interfaces which support Voice Vlan feature
            are shown.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: vmvoicevlanid
            
            	The Voice Vlan ID (VVID) to which this port belongs to.  0    \-    The CDP packets transmitting            through this port would contain           Appliance VLAN\-ID TLV with value            of 0. VoIP and related packets            are expected to be sent and            received with VLAN\-id=0 and an            802.1p priority.   1..4094 \- The CDP packets transmitting           through this port would contain           Appliance VLAN\-ID TLV with N.           VoIP and related packets are           expected to be sent and received           with VLAN\-id=N and an 802.1p           priority.  4095  \-   The CDP packets transmitting           through this port would contain           Appliance VLAN\-ID TLV with value           of 4095. VoIP and related packets           are expected to be sent and            received untagged without an            802.1p priority.  4096  \-   The CDP packets transmitting            through this port would not            include Appliance VLAN\-ID TLV;            or, if the VVID is not supported            on the port, this MIB object will           not be configurable and will            return 4096
            	**type**\: int
            
            	**range:** 0..4096
            
            .. attribute:: vmvoicevlancdpverifyenable
            
            	Enable or Disable the feature of CDP message verification of voice VLANs.  true   \- The voice VLAN vmVoiceVlan is enabled           only after CDP messages are received           from the IP phone.  false \-  The voice VLAN vmVoiceVlan is enabled          as soon as the IP phone interface is          up. There is no verification needed           from CDP messages from the IP phone
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
            _revision = '2007-12-14'

            def __init__(self):
                super(CISCOVLANMEMBERSHIPMIB.VmVoiceVlanTable.VmVoiceVlanEntry, self).__init__()

                self.yang_name = "vmVoiceVlanEntry"
                self.yang_parent_name = "vmVoiceVlanTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('vmvoicevlanid', (YLeaf(YType.int32, 'vmVoiceVlanId'), ['int'])),
                    ('vmvoicevlancdpverifyenable', (YLeaf(YType.boolean, 'vmVoiceVlanCdpVerifyEnable'), ['bool'])),
                ])
                self.ifindex = None
                self.vmvoicevlanid = None
                self.vmvoicevlancdpverifyenable = None
                self._segment_path = lambda: "vmVoiceVlanEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/vmVoiceVlanTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVLANMEMBERSHIPMIB.VmVoiceVlanTable.VmVoiceVlanEntry, ['ifindex', 'vmvoicevlanid', 'vmvoicevlancdpverifyenable'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOVLANMEMBERSHIPMIB()
        return self._top_entity


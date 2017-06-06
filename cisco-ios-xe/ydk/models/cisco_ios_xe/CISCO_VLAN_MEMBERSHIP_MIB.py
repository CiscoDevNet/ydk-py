""" CISCO_VLAN_MEMBERSHIP_MIB 

The MIB module for the management of the VLAN
Membership within the frame  work of Cisco
VLAN Architecture, v 2.0 by Keith McCloghrie. The MIB
provides information on VLAN Membership Policy Servers
used by a device and VLAN membership assignments of
non\-trunk bridge ports of the device.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoVlanMembershipMib(object):
    """
    
    
    .. attribute:: vmmembership
    
    	
    	**type**\:   :py:class:`Vmmembership <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmmembership>`
    
    .. attribute:: vmmembershipsummaryexttable
    
    	A summary of VLAN membership of non\-trunk bridge ports. This table is used for  retrieving VLAN membership information for the device which supports dot1dBasePort  with value greater than 2048.  A row is created for a VLAN and a particular bridge port range, where at least one port  in the range is assigned to this VLAN.  VLAN membership can only be modified via the vmMembershipTable
    	**type**\:   :py:class:`Vmmembershipsummaryexttable <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmmembershipsummaryexttable>`
    
    .. attribute:: vmmembershipsummarytable
    
    	A summary of VLAN membership of non\-trunk bridge ports. This is a convenience table for retrieving VLAN membership information.  A row is created for a VLAN if\: a) the VLAN exists, or b) a port is assigned to a non\-existent VLAN.  VLAN membership can only be modified via the vmMembershipTable
    	**type**\:   :py:class:`Vmmembershipsummarytable <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmmembershipsummarytable>`
    
    .. attribute:: vmmembershiptable
    
    	A table for configuring VLAN port membership. There is one row for each bridge port that is assigned to a static or dynamic access port. Trunk ports are not  represented in this table.  An entry may be created and deleted when ports are created or deleted via SNMP or the management console on a  device
    	**type**\:   :py:class:`Vmmembershiptable <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmmembershiptable>`
    
    .. attribute:: vmstatistics
    
    	
    	**type**\:   :py:class:`Vmstatistics <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmstatistics>`
    
    .. attribute:: vmstatus
    
    	
    	**type**\:   :py:class:`Vmstatus <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmstatus>`
    
    .. attribute:: vmvmps
    
    	
    	**type**\:   :py:class:`Vmvmps <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmvmps>`
    
    .. attribute:: vmvmpstable
    
    	A table of VMPS to use. The device will use the the primary VMPS by default. If the device is unable to reach the primary server after vmVmpsRetries retries, it uses the first secondary server in the table until it runs out of secondary servers, in which case it will return to using the primary server. Entries in this table may be created and deleted via this MIB or the management console on a device
    	**type**\:   :py:class:`Vmvmpstable <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmvmpstable>`
    
    .. attribute:: vmvoicevlantable
    
    	A table for configuring the Voice VLAN\-ID for the ports. An entry will exist for each interface which supports Voice Vlan feature
    	**type**\:   :py:class:`Vmvoicevlantable <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmvoicevlantable>`
    
    

    """

    _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
    _revision = '2007-12-14'

    def __init__(self):
        self.vmmembership = CiscoVlanMembershipMib.Vmmembership()
        self.vmmembership.parent = self
        self.vmmembershipsummaryexttable = CiscoVlanMembershipMib.Vmmembershipsummaryexttable()
        self.vmmembershipsummaryexttable.parent = self
        self.vmmembershipsummarytable = CiscoVlanMembershipMib.Vmmembershipsummarytable()
        self.vmmembershipsummarytable.parent = self
        self.vmmembershiptable = CiscoVlanMembershipMib.Vmmembershiptable()
        self.vmmembershiptable.parent = self
        self.vmstatistics = CiscoVlanMembershipMib.Vmstatistics()
        self.vmstatistics.parent = self
        self.vmstatus = CiscoVlanMembershipMib.Vmstatus()
        self.vmstatus.parent = self
        self.vmvmps = CiscoVlanMembershipMib.Vmvmps()
        self.vmvmps.parent = self
        self.vmvmpstable = CiscoVlanMembershipMib.Vmvmpstable()
        self.vmvmpstable.parent = self
        self.vmvoicevlantable = CiscoVlanMembershipMib.Vmvoicevlantable()
        self.vmvoicevlantable.parent = self


    class Vmvmps(object):
        """
        
        
        .. attribute:: vmvmpscurrent
        
        	This is the IpAddress of the current VMPS used
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: vmvmpsreconfirm
        
        	Setting this object to execute(2) causes the switch to reconfirm membership of every dynamic port. Reading this object always return ready(1)
        	**type**\:   :py:class:`VmvmpsreconfirmEnum <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmvmps.VmvmpsreconfirmEnum>`
        
        .. attribute:: vmvmpsreconfirminterval
        
        	The switch will reconfirm membership of addresses on each port with VMPS periodically. This object specifies the interval to perform reconfirmation. If the value is set to 0, the switch does not reconfirm membership with VMPS
        	**type**\:  int
        
        	**range:** 0..120
        
        	**units**\: Minutes
        
        .. attribute:: vmvmpsreconfirmresult
        
        	This object returns the result of the last request that sets vmVmpsReconfirm to execute(2). The semantics of the possible results are as follows\:       other(1)           \- none of following      inProgress(2)      \- reconfirm in progress      success(3)         \- reconfirm completed successfully      noResponse(4)      \- reconfirm failed because no                           VMPS responded      noVmps(5)          \- No VMPS configured      noDynamicPort(6)   \- No dynamic ports configured      noHostConnected(7) \- No hosts on dynamic ports
        	**type**\:   :py:class:`VmvmpsreconfirmresultEnum <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmvmps.VmvmpsreconfirmresultEnum>`
        
        .. attribute:: vmvmpsretries
        
        	The number of retries for VQP requests to a VMPS before using the next available VMPS
        	**type**\:  int
        
        	**range:** 1..10
        
        .. attribute:: vmvmpsvqpversion
        
        	The VLAN Query Protocol (VQP) version supported on the device. VQP is the protocol used to query VLAN Membership Policy Server (VMPS) for VLAN membership assignments of dynamic VLAN ports. A VMPS provides VLAN membership policy assignments based on the content of the packets received on a port
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
        _revision = '2007-12-14'

        def __init__(self):
            self.parent = None
            self.vmvmpscurrent = None
            self.vmvmpsreconfirm = None
            self.vmvmpsreconfirminterval = None
            self.vmvmpsreconfirmresult = None
            self.vmvmpsretries = None
            self.vmvmpsvqpversion = None

        class VmvmpsreconfirmEnum(Enum):
            """
            VmvmpsreconfirmEnum

            Setting this object to execute(2) causes the switch

            to reconfirm membership of every dynamic port.

            Reading this object always return ready(1).

            .. data:: ready = 1

            .. data:: execute = 2

            """

            ready = 1

            execute = 2


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_VLAN_MEMBERSHIP_MIB as meta
                return meta._meta_table['CiscoVlanMembershipMib.Vmvmps.VmvmpsreconfirmEnum']


        class VmvmpsreconfirmresultEnum(Enum):
            """
            VmvmpsreconfirmresultEnum

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

            other = 1

            inProgress = 2

            success = 3

            noResponse = 4

            noVmps = 5

            noDynamicPort = 6

            noHostConnected = 7


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_VLAN_MEMBERSHIP_MIB as meta
                return meta._meta_table['CiscoVlanMembershipMib.Vmvmps.VmvmpsreconfirmresultEnum']


        @property
        def _common_path(self):

            return '/CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/CISCO-VLAN-MEMBERSHIP-MIB:vmVmps'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.vmvmpscurrent is not None:
                return True

            if self.vmvmpsreconfirm is not None:
                return True

            if self.vmvmpsreconfirminterval is not None:
                return True

            if self.vmvmpsreconfirmresult is not None:
                return True

            if self.vmvmpsretries is not None:
                return True

            if self.vmvmpsvqpversion is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_VLAN_MEMBERSHIP_MIB as meta
            return meta._meta_table['CiscoVlanMembershipMib.Vmvmps']['meta_info']


    class Vmmembership(object):
        """
        
        
        .. attribute:: vmvlancreationmode
        
        	This object is used to determine whether or not a non\-existing VLAN will be created automatically by the system after assigned to a port.  automatic(1)\:  a non\-existing VLAN will be created                automatically by the system after                assigned to a port.  manual(2)\:     a non\-existing VLAN will not be created                automatically by the system and need to be                manually created by the users after assigned                to a port
        	**type**\:   :py:class:`VmvlancreationmodeEnum <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmmembership.VmvlancreationmodeEnum>`
        
        

        """

        _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
        _revision = '2007-12-14'

        def __init__(self):
            self.parent = None
            self.vmvlancreationmode = None

        class VmvlancreationmodeEnum(Enum):
            """
            VmvlancreationmodeEnum

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

            automatic = 1

            manual = 2


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_VLAN_MEMBERSHIP_MIB as meta
                return meta._meta_table['CiscoVlanMembershipMib.Vmmembership.VmvlancreationmodeEnum']


        @property
        def _common_path(self):

            return '/CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/CISCO-VLAN-MEMBERSHIP-MIB:vmMembership'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.vmvlancreationmode is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_VLAN_MEMBERSHIP_MIB as meta
            return meta._meta_table['CiscoVlanMembershipMib.Vmmembership']['meta_info']


    class Vmstatistics(object):
        """
        
        
        .. attribute:: vminsufficientresources
        
        	The number of times, since last system re\-initialization, a VQP response indicates  insufficient resources. An insufficient resources  response indicates that the VMPS used does not  have the required resources to verify the membership assignment requested
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: vmvmpschanges
        
        	The number of times, since last system re\-initialization, the current VMPS was changed. The current VMPS is changed whenever the VMPS fails to  response after vmVmpsRetries of a VQP request
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: vmvqpdenied
        
        	The number of times, since last system re\-initialization, a VQP response indicates  'denied'. A 'denied' response is a result of  the membership policy configured at a VMPS by the administrator
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: vmvqpqueries
        
        	The total number of VQP requests sent by this device to all VMPS since last system re\-initialization
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: vmvqpresponses
        
        	The number of VQP responses received by this device from all VMPS since last system re\-initialization
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: vmvqpshutdown
        
        	The number of times, since last system re\-initialization, a VQP response indicates  'shutdown'. A 'shutdown' response is a result of  the membership policy configured at a VMPS by the administrator
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: vmvqpwrongdomain
        
        	The number of times, since last system re\-initialization, a VQP response indicates wrong  management domain. A wrong management domain  response indicates that the VMPS used serves a  management domain that is different from the device's management domain
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: vmvqpwrongversion
        
        	The number of times, since last system re\-initialization, a VQP response indicates wrong  VQP version. A wrong VQP version response  indicates that the VMPS used supports a VQP  version that is different from the device's  VQP version
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
        _revision = '2007-12-14'

        def __init__(self):
            self.parent = None
            self.vminsufficientresources = None
            self.vmvmpschanges = None
            self.vmvqpdenied = None
            self.vmvqpqueries = None
            self.vmvqpresponses = None
            self.vmvqpshutdown = None
            self.vmvqpwrongdomain = None
            self.vmvqpwrongversion = None

        @property
        def _common_path(self):

            return '/CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/CISCO-VLAN-MEMBERSHIP-MIB:vmStatistics'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.vminsufficientresources is not None:
                return True

            if self.vmvmpschanges is not None:
                return True

            if self.vmvqpdenied is not None:
                return True

            if self.vmvqpqueries is not None:
                return True

            if self.vmvqpresponses is not None:
                return True

            if self.vmvqpshutdown is not None:
                return True

            if self.vmvqpwrongdomain is not None:
                return True

            if self.vmvqpwrongversion is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_VLAN_MEMBERSHIP_MIB as meta
            return meta._meta_table['CiscoVlanMembershipMib.Vmstatistics']['meta_info']


    class Vmstatus(object):
        """
        
        
        .. attribute:: vmnotificationsenabled
        
        	An indication of whether the notifications/traps defined in this MIB are enabled
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
        _revision = '2007-12-14'

        def __init__(self):
            self.parent = None
            self.vmnotificationsenabled = None

        @property
        def _common_path(self):

            return '/CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/CISCO-VLAN-MEMBERSHIP-MIB:vmStatus'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.vmnotificationsenabled is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_VLAN_MEMBERSHIP_MIB as meta
            return meta._meta_table['CiscoVlanMembershipMib.Vmstatus']['meta_info']


    class Vmvmpstable(object):
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
        	**type**\: list of    :py:class:`Vmvmpsentry <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmvmpstable.Vmvmpsentry>`
        
        

        """

        _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
        _revision = '2007-12-14'

        def __init__(self):
            self.parent = None
            self.vmvmpsentry = YList()
            self.vmvmpsentry.parent = self
            self.vmvmpsentry.name = 'vmvmpsentry'


        class Vmvmpsentry(object):
            """
            An entry (conceptual row) in the vmVmpsTable.
            
            .. attribute:: vmvmpsipaddress  <key>
            
            	The Ip Address of the VMPS
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: vmvmpsprimary
            
            	The status of the VMPS. Setting this value to true will make this VMPS the primary server and make the switch use this as the current server. Setting this entry to true causes other rows to transition to false. Attempting to write a value of false after creation will result in a return of bad value. Deleting an entry whose value is true will result in the first entry in the table being set to true
            	**type**\:  bool
            
            .. attribute:: vmvmpsrowstatus
            
            	The status of this conceptual row
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            

            """

            _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
            _revision = '2007-12-14'

            def __init__(self):
                self.parent = None
                self.vmvmpsipaddress = None
                self.vmvmpsprimary = None
                self.vmvmpsrowstatus = None

            @property
            def _common_path(self):
                if self.vmvmpsipaddress is None:
                    raise YPYModelError('Key property vmvmpsipaddress is None')

                return '/CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/CISCO-VLAN-MEMBERSHIP-MIB:vmVmpsTable/CISCO-VLAN-MEMBERSHIP-MIB:vmVmpsEntry[CISCO-VLAN-MEMBERSHIP-MIB:vmVmpsIpAddress = ' + str(self.vmvmpsipaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.vmvmpsipaddress is not None:
                    return True

                if self.vmvmpsprimary is not None:
                    return True

                if self.vmvmpsrowstatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_VLAN_MEMBERSHIP_MIB as meta
                return meta._meta_table['CiscoVlanMembershipMib.Vmvmpstable.Vmvmpsentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/CISCO-VLAN-MEMBERSHIP-MIB:vmVmpsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.vmvmpsentry is not None:
                for child_ref in self.vmvmpsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_VLAN_MEMBERSHIP_MIB as meta
            return meta._meta_table['CiscoVlanMembershipMib.Vmvmpstable']['meta_info']


    class Vmmembershipsummarytable(object):
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
        	**type**\: list of    :py:class:`Vmmembershipsummaryentry <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmmembershipsummarytable.Vmmembershipsummaryentry>`
        
        

        """

        _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
        _revision = '2007-12-14'

        def __init__(self):
            self.parent = None
            self.vmmembershipsummaryentry = YList()
            self.vmmembershipsummaryentry.parent = self
            self.vmmembershipsummaryentry.name = 'vmmembershipsummaryentry'


        class Vmmembershipsummaryentry(object):
            """
            An entry (conceptual row) in the
            vmMembershipSummaryTable.
            
            .. attribute:: vmmembershipsummaryvlanindex  <key>
            
            	The VLAN id of the VLAN
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: vmmembershipsummarymember2kports
            
            	The set of the device's member ports that belong to the VLAN. It has the VLAN membership information of up to 2048 ports with the port number from 1 to  2048.  Each octet within the value of this object specifies a set of eight ports, with the first octet specifying  ports 1 through 8, the second octet specifying ports 9 through 16, etc.   Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port.  Thus, each port of the VLAN is represented by a single bit within the value of this object.  If that bit has a value of '1' then that port is included in the set of ports; the port is not included if its bit has a value of '0'.  A port number is the value of dot1dBasePort for the port in the BRIDGE\-MIB (RFC 1493)
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: vmmembershipsummarymemberports
            
            	The set of the device's member ports that belong to the VLAN.  Each octet within the value of this object specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc.   Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port.  Thus, each port of the VLAN is represented by a single bit within the value of this object.  If that bit has a value of '1' then that port is included in the set of ports; the port is not included if its bit has a value of '0'.  A port number is the value of dot1dBasePort for the port in the BRIDGE\-MIB (RFC 1493)
            	**type**\:  str
            
            	**length:** 0..128
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
            _revision = '2007-12-14'

            def __init__(self):
                self.parent = None
                self.vmmembershipsummaryvlanindex = None
                self.vmmembershipsummarymember2kports = None
                self.vmmembershipsummarymemberports = None

            @property
            def _common_path(self):
                if self.vmmembershipsummaryvlanindex is None:
                    raise YPYModelError('Key property vmmembershipsummaryvlanindex is None')

                return '/CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/CISCO-VLAN-MEMBERSHIP-MIB:vmMembershipSummaryTable/CISCO-VLAN-MEMBERSHIP-MIB:vmMembershipSummaryEntry[CISCO-VLAN-MEMBERSHIP-MIB:vmMembershipSummaryVlanIndex = ' + str(self.vmmembershipsummaryvlanindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.vmmembershipsummaryvlanindex is not None:
                    return True

                if self.vmmembershipsummarymember2kports is not None:
                    return True

                if self.vmmembershipsummarymemberports is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_VLAN_MEMBERSHIP_MIB as meta
                return meta._meta_table['CiscoVlanMembershipMib.Vmmembershipsummarytable.Vmmembershipsummaryentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/CISCO-VLAN-MEMBERSHIP-MIB:vmMembershipSummaryTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.vmmembershipsummaryentry is not None:
                for child_ref in self.vmmembershipsummaryentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_VLAN_MEMBERSHIP_MIB as meta
            return meta._meta_table['CiscoVlanMembershipMib.Vmmembershipsummarytable']['meta_info']


    class Vmmembershiptable(object):
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
        	**type**\: list of    :py:class:`Vmmembershipentry <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmmembershiptable.Vmmembershipentry>`
        
        

        """

        _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
        _revision = '2007-12-14'

        def __init__(self):
            self.parent = None
            self.vmmembershipentry = YList()
            self.vmmembershipentry.parent = self
            self.vmmembershipentry.name = 'vmmembershipentry'


        class Vmmembershipentry(object):
            """
            An entry (conceptual row) in the vmMembershipTable.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: vmportstatus
            
            	An indication of the current VLAN status of the port. A status of inactive(1) indicates that a dynamic port does not yet have a VLAN assigned, or a port is  assigned to a VLAN that is currently not active. A  status of active(2) indicates that the currently  assigned VLAN is active. A status of shutdown(3)  indicates that the port has been disabled as a result of VQP shutdown response
            	**type**\:   :py:class:`VmportstatusEnum <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmmembershiptable.Vmmembershipentry.VmportstatusEnum>`
            
            .. attribute:: vmvlan
            
            	The VLAN id of the VLAN the port is assigned to when vmVlanType is set to static or dynamic. This object is not instantiated if not applicable.  The value may be 0 if the port is not assigned to a VLAN.  If vmVlanType is static, the port is always assigned to a VLAN and the object may not be set to 0.  If vmVlanType is dynamic the object's value is 0 if the port is currently not assigned to a VLAN. In addition, the object may be set to 0 only
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: vmvlans
            
            	The VLAN(s) the port is assigned to when the port's vmVlanType is set to multiVlan. This object is not instantiated if not applicable.  The port is always assigned to one or more VLANs and the object may not be set so that there are no vlans assigned.  Each octet within the value of this object specifies a set of eight VLANs, with the first octet specifying VLAN id 1 through 8, the second octet specifying VLAN ids 9 through 16, etc.   Within each octet, the most significant bit represents the lowest numbered VLAN id, and the least significant bit represents the highest numbered VLAN id.  Thus, each VLAN of the port is represented by a single bit within the value of this object.  If that bit has a value of '1' then that VLAN is included in the set of VLANs; the VLAN is not included if its bit has a value of '0'
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: vmvlans2k
            
            	The VLAN(s) the port is assigned to when the port's vmVlanType is set to multiVlan. This object is not instantiated if not applicable.  The port is always assigned to one or more VLANs and the object may not be set so that there are no vlans assigned.  Each octet within the value of this object specifies a set of eight VLANs, with the first octet specifying VLAN id 1024 through 1031, the second octet specifying  VLAN ids 1032 through 1039, etc.  Within each octet,  the most significant bit represents the lowest  numbered VLAN id, and the least significant bit  represents the highest numbered VLAN id.  Thus, each  VLAN of the port is represented by a single bit within the value of this object.  If that bit has a value of '1' then that VLAN is included in the set of VLANs; the VLAN is not included if its bit has a value of '0'
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: vmvlans3k
            
            	The VLAN(s) the port is assigned to when the port's vmVlanType is set to multiVlan. This object is not instantiated if not applicable.  The port is always assigned to one or more VLANs and the object may not be set so that there are no vlans assigned.  Each octet within the value of this object specifies a set of eight VLANs, with the first octet specifying VLAN id 2048 through 2055, the second octet specifying  VLAN ids 2056 through 2063, etc.   Within each octet,  the most significant bit represents the lowest  numbered VLAN id, and the least significant bit  represents the highest numbered VLAN id.  Thus, each VLAN of the port is represented by a single bit within the value of this object.  If that bit has a value of '1' then that VLAN is included in the set of VLANs; the VLAN is not included if its bit has a value of '0'
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: vmvlans4k
            
            	The VLAN(s) the port is assigned to when the port's vmVlanType is set to multiVlan. This object is not instantiated if not applicable.  The port is always assigned to one or more VLANs and the object may not be set so that there are no vlans assigned.  Each octet within the value of this object specifies a set of eight VLANs, with the first octet specifying VLAN id 3072 through 3079, the second octet specifying  VLAN ids 3040 through 3047, etc.   Within each octet,  the most significant bit represents the lowest  numbered VLAN id, and the least significant bit  represents the highest numbered VLAN id.  Thus, each VLAN of the port is represented by a single bit within the value of this object.  If that bit has a value of '1' then that VLAN is included in the set of VLANs; the VLAN is not included if its bit has a value of '0'
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: vmvlantype
            
            	The type of VLAN membership assigned to this port. A port with static vlan membership is assigned to a single VLAN directly. A port with dynamic membership is assigned a single VLAN based on content of packets received on the port and via VQP queries to VMPS. A port with multiVlan membership may be assigned to one or more VLANs directly.  A static or dynamic port membership is specified by the value of vmVlan. A multiVlan port membership is specified by the value of vmVlans
            	**type**\:   :py:class:`VmvlantypeEnum <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmmembershiptable.Vmmembershipentry.VmvlantypeEnum>`
            
            

            """

            _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
            _revision = '2007-12-14'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.vmportstatus = None
                self.vmvlan = None
                self.vmvlans = None
                self.vmvlans2k = None
                self.vmvlans3k = None
                self.vmvlans4k = None
                self.vmvlantype = None

            class VmportstatusEnum(Enum):
                """
                VmportstatusEnum

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

                inactive = 1

                active = 2

                shutdown = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_VLAN_MEMBERSHIP_MIB as meta
                    return meta._meta_table['CiscoVlanMembershipMib.Vmmembershiptable.Vmmembershipentry.VmportstatusEnum']


            class VmvlantypeEnum(Enum):
                """
                VmvlantypeEnum

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

                static = 1

                dynamic = 2

                multiVlan = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_VLAN_MEMBERSHIP_MIB as meta
                    return meta._meta_table['CiscoVlanMembershipMib.Vmmembershiptable.Vmmembershipentry.VmvlantypeEnum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/CISCO-VLAN-MEMBERSHIP-MIB:vmMembershipTable/CISCO-VLAN-MEMBERSHIP-MIB:vmMembershipEntry[CISCO-VLAN-MEMBERSHIP-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.vmportstatus is not None:
                    return True

                if self.vmvlan is not None:
                    return True

                if self.vmvlans is not None:
                    return True

                if self.vmvlans2k is not None:
                    return True

                if self.vmvlans3k is not None:
                    return True

                if self.vmvlans4k is not None:
                    return True

                if self.vmvlantype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_VLAN_MEMBERSHIP_MIB as meta
                return meta._meta_table['CiscoVlanMembershipMib.Vmmembershiptable.Vmmembershipentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/CISCO-VLAN-MEMBERSHIP-MIB:vmMembershipTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.vmmembershipentry is not None:
                for child_ref in self.vmmembershipentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_VLAN_MEMBERSHIP_MIB as meta
            return meta._meta_table['CiscoVlanMembershipMib.Vmmembershiptable']['meta_info']


    class Vmmembershipsummaryexttable(object):
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
        	**type**\: list of    :py:class:`Vmmembershipsummaryextentry <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmmembershipsummaryexttable.Vmmembershipsummaryextentry>`
        
        

        """

        _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
        _revision = '2007-12-14'

        def __init__(self):
            self.parent = None
            self.vmmembershipsummaryextentry = YList()
            self.vmmembershipsummaryextentry.parent = self
            self.vmmembershipsummaryextentry.name = 'vmmembershipsummaryextentry'


        class Vmmembershipsummaryextentry(object):
            """
            An entry (conceptual row) in the
            vmMembershipSummaryExtTable.
            
            .. attribute:: vmmembershipsummaryvlanindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`vmmembershipsummaryvlanindex <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmmembershipsummarytable.Vmmembershipsummaryentry>`
            
            .. attribute:: vmmembershipportrangeindex  <key>
            
            	The bridge port range index of this row
            	**type**\:   :py:class:`CiscoportlistrangeEnum <ydk.models.cisco_ios_xe.CISCO_TC.CiscoportlistrangeEnum>`
            
            .. attribute:: vmmembershipsummaryextports
            
            	The set of the device's member ports that belong to the VLAN. It has the VLAN membership information of up to 2k ports with the port number starting from the information indicated in vmMembershipPortRangeIndex object of the same row. For example, if the value of vmMembershipPortRangeIndex is 'twoKto4K', the port number indicated in this object starting from 2049 and ending to 4096.   A port number is the value of dot1dBasePort for the port in the BRIDGE\-MIB (RFC 1493)
            	**type**\:  str
            
            	**length:** 0..256
            
            

            """

            _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
            _revision = '2007-12-14'

            def __init__(self):
                self.parent = None
                self.vmmembershipsummaryvlanindex = None
                self.vmmembershipportrangeindex = None
                self.vmmembershipsummaryextports = None

            @property
            def _common_path(self):
                if self.vmmembershipsummaryvlanindex is None:
                    raise YPYModelError('Key property vmmembershipsummaryvlanindex is None')
                if self.vmmembershipportrangeindex is None:
                    raise YPYModelError('Key property vmmembershipportrangeindex is None')

                return '/CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/CISCO-VLAN-MEMBERSHIP-MIB:vmMembershipSummaryExtTable/CISCO-VLAN-MEMBERSHIP-MIB:vmMembershipSummaryExtEntry[CISCO-VLAN-MEMBERSHIP-MIB:vmMembershipSummaryVlanIndex = ' + str(self.vmmembershipsummaryvlanindex) + '][CISCO-VLAN-MEMBERSHIP-MIB:vmMembershipPortRangeIndex = ' + str(self.vmmembershipportrangeindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.vmmembershipsummaryvlanindex is not None:
                    return True

                if self.vmmembershipportrangeindex is not None:
                    return True

                if self.vmmembershipsummaryextports is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_VLAN_MEMBERSHIP_MIB as meta
                return meta._meta_table['CiscoVlanMembershipMib.Vmmembershipsummaryexttable.Vmmembershipsummaryextentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/CISCO-VLAN-MEMBERSHIP-MIB:vmMembershipSummaryExtTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.vmmembershipsummaryextentry is not None:
                for child_ref in self.vmmembershipsummaryextentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_VLAN_MEMBERSHIP_MIB as meta
            return meta._meta_table['CiscoVlanMembershipMib.Vmmembershipsummaryexttable']['meta_info']


    class Vmvoicevlantable(object):
        """
        A table for configuring the Voice VLAN\-ID
        for the ports. An entry will exist for each
        interface which supports Voice Vlan feature.
        
        .. attribute:: vmvoicevlanentry
        
        	An entry (conceptual row) in the vmVoiceVlanTable. Only interfaces which support Voice Vlan feature are shown
        	**type**\: list of    :py:class:`Vmvoicevlanentry <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmvoicevlantable.Vmvoicevlanentry>`
        
        

        """

        _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
        _revision = '2007-12-14'

        def __init__(self):
            self.parent = None
            self.vmvoicevlanentry = YList()
            self.vmvoicevlanentry.parent = self
            self.vmvoicevlanentry.name = 'vmvoicevlanentry'


        class Vmvoicevlanentry(object):
            """
            An entry (conceptual row) in the vmVoiceVlanTable.
            Only interfaces which support Voice Vlan feature
            are shown.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: vmvoicevlancdpverifyenable
            
            	Enable or Disable the feature of CDP message verification of voice VLANs.  true   \- The voice VLAN vmVoiceVlan is enabled           only after CDP messages are received           from the IP phone.  false \-  The voice VLAN vmVoiceVlan is enabled          as soon as the IP phone interface is          up. There is no verification needed           from CDP messages from the IP phone
            	**type**\:  bool
            
            .. attribute:: vmvoicevlanid
            
            	The Voice Vlan ID (VVID) to which this port belongs to.  0    \-    The CDP packets transmitting            through this port would contain           Appliance VLAN\-ID TLV with value            of 0. VoIP and related packets            are expected to be sent and            received with VLAN\-id=0 and an            802.1p priority.   1..4094 \- The CDP packets transmitting           through this port would contain           Appliance VLAN\-ID TLV with N.           VoIP and related packets are           expected to be sent and received           with VLAN\-id=N and an 802.1p           priority.  4095  \-   The CDP packets transmitting           through this port would contain           Appliance VLAN\-ID TLV with value           of 4095. VoIP and related packets           are expected to be sent and            received untagged without an            802.1p priority.  4096  \-   The CDP packets transmitting            through this port would not            include Appliance VLAN\-ID TLV;            or, if the VVID is not supported            on the port, this MIB object will           not be configurable and will            return 4096
            	**type**\:  int
            
            	**range:** 0..4096
            
            

            """

            _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
            _revision = '2007-12-14'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.vmvoicevlancdpverifyenable = None
                self.vmvoicevlanid = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/CISCO-VLAN-MEMBERSHIP-MIB:vmVoiceVlanTable/CISCO-VLAN-MEMBERSHIP-MIB:vmVoiceVlanEntry[CISCO-VLAN-MEMBERSHIP-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.vmvoicevlancdpverifyenable is not None:
                    return True

                if self.vmvoicevlanid is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_VLAN_MEMBERSHIP_MIB as meta
                return meta._meta_table['CiscoVlanMembershipMib.Vmvoicevlantable.Vmvoicevlanentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/CISCO-VLAN-MEMBERSHIP-MIB:vmVoiceVlanTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.vmvoicevlanentry is not None:
                for child_ref in self.vmvoicevlanentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_VLAN_MEMBERSHIP_MIB as meta
            return meta._meta_table['CiscoVlanMembershipMib.Vmvoicevlantable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.vmmembership is not None and self.vmmembership._has_data():
            return True

        if self.vmmembershipsummaryexttable is not None and self.vmmembershipsummaryexttable._has_data():
            return True

        if self.vmmembershipsummarytable is not None and self.vmmembershipsummarytable._has_data():
            return True

        if self.vmmembershiptable is not None and self.vmmembershiptable._has_data():
            return True

        if self.vmstatistics is not None and self.vmstatistics._has_data():
            return True

        if self.vmstatus is not None and self.vmstatus._has_data():
            return True

        if self.vmvmps is not None and self.vmvmps._has_data():
            return True

        if self.vmvmpstable is not None and self.vmvmpstable._has_data():
            return True

        if self.vmvoicevlantable is not None and self.vmvoicevlantable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_VLAN_MEMBERSHIP_MIB as meta
        return meta._meta_table['CiscoVlanMembershipMib']['meta_info']



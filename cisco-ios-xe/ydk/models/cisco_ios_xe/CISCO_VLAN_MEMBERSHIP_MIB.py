""" CISCO_VLAN_MEMBERSHIP_MIB 

The MIB module for the management of the VLAN
Membership within the frame  work of Cisco
VLAN Architecture, v 2.0 by Keith McCloghrie. The MIB
provides information on VLAN Membership Policy Servers
used by a device and VLAN membership assignments of
non\-trunk bridge ports of the device.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoVlanMembershipMib(Entity):
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
        super(CiscoVlanMembershipMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-VLAN-MEMBERSHIP-MIB"
        self.yang_parent_name = "CISCO-VLAN-MEMBERSHIP-MIB"

        self.vmmembership = CiscoVlanMembershipMib.Vmmembership()
        self.vmmembership.parent = self
        self._children_name_map["vmmembership"] = "vmMembership"
        self._children_yang_names.add("vmMembership")

        self.vmmembershipsummaryexttable = CiscoVlanMembershipMib.Vmmembershipsummaryexttable()
        self.vmmembershipsummaryexttable.parent = self
        self._children_name_map["vmmembershipsummaryexttable"] = "vmMembershipSummaryExtTable"
        self._children_yang_names.add("vmMembershipSummaryExtTable")

        self.vmmembershipsummarytable = CiscoVlanMembershipMib.Vmmembershipsummarytable()
        self.vmmembershipsummarytable.parent = self
        self._children_name_map["vmmembershipsummarytable"] = "vmMembershipSummaryTable"
        self._children_yang_names.add("vmMembershipSummaryTable")

        self.vmmembershiptable = CiscoVlanMembershipMib.Vmmembershiptable()
        self.vmmembershiptable.parent = self
        self._children_name_map["vmmembershiptable"] = "vmMembershipTable"
        self._children_yang_names.add("vmMembershipTable")

        self.vmstatistics = CiscoVlanMembershipMib.Vmstatistics()
        self.vmstatistics.parent = self
        self._children_name_map["vmstatistics"] = "vmStatistics"
        self._children_yang_names.add("vmStatistics")

        self.vmstatus = CiscoVlanMembershipMib.Vmstatus()
        self.vmstatus.parent = self
        self._children_name_map["vmstatus"] = "vmStatus"
        self._children_yang_names.add("vmStatus")

        self.vmvmps = CiscoVlanMembershipMib.Vmvmps()
        self.vmvmps.parent = self
        self._children_name_map["vmvmps"] = "vmVmps"
        self._children_yang_names.add("vmVmps")

        self.vmvmpstable = CiscoVlanMembershipMib.Vmvmpstable()
        self.vmvmpstable.parent = self
        self._children_name_map["vmvmpstable"] = "vmVmpsTable"
        self._children_yang_names.add("vmVmpsTable")

        self.vmvoicevlantable = CiscoVlanMembershipMib.Vmvoicevlantable()
        self.vmvoicevlantable.parent = self
        self._children_name_map["vmvoicevlantable"] = "vmVoiceVlanTable"
        self._children_yang_names.add("vmVoiceVlanTable")


    class Vmvmps(Entity):
        """
        
        
        .. attribute:: vmvmpscurrent
        
        	This is the IpAddress of the current VMPS used
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: vmvmpsreconfirm
        
        	Setting this object to execute(2) causes the switch to reconfirm membership of every dynamic port. Reading this object always return ready(1)
        	**type**\:   :py:class:`Vmvmpsreconfirm <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmvmps.Vmvmpsreconfirm>`
        
        .. attribute:: vmvmpsreconfirminterval
        
        	The switch will reconfirm membership of addresses on each port with VMPS periodically. This object specifies the interval to perform reconfirmation. If the value is set to 0, the switch does not reconfirm membership with VMPS
        	**type**\:  int
        
        	**range:** 0..120
        
        	**units**\: Minutes
        
        .. attribute:: vmvmpsreconfirmresult
        
        	This object returns the result of the last request that sets vmVmpsReconfirm to execute(2). The semantics of the possible results are as follows\:       other(1)           \- none of following      inProgress(2)      \- reconfirm in progress      success(3)         \- reconfirm completed successfully      noResponse(4)      \- reconfirm failed because no                           VMPS responded      noVmps(5)          \- No VMPS configured      noDynamicPort(6)   \- No dynamic ports configured      noHostConnected(7) \- No hosts on dynamic ports
        	**type**\:   :py:class:`Vmvmpsreconfirmresult <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmvmps.Vmvmpsreconfirmresult>`
        
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
            super(CiscoVlanMembershipMib.Vmvmps, self).__init__()

            self.yang_name = "vmVmps"
            self.yang_parent_name = "CISCO-VLAN-MEMBERSHIP-MIB"

            self.vmvmpscurrent = YLeaf(YType.str, "vmVmpsCurrent")

            self.vmvmpsreconfirm = YLeaf(YType.enumeration, "vmVmpsReconfirm")

            self.vmvmpsreconfirminterval = YLeaf(YType.int32, "vmVmpsReconfirmInterval")

            self.vmvmpsreconfirmresult = YLeaf(YType.enumeration, "vmVmpsReconfirmResult")

            self.vmvmpsretries = YLeaf(YType.int32, "vmVmpsRetries")

            self.vmvmpsvqpversion = YLeaf(YType.int32, "vmVmpsVQPVersion")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("vmvmpscurrent",
                            "vmvmpsreconfirm",
                            "vmvmpsreconfirminterval",
                            "vmvmpsreconfirmresult",
                            "vmvmpsretries",
                            "vmvmpsvqpversion") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoVlanMembershipMib.Vmvmps, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVlanMembershipMib.Vmvmps, self).__setattr__(name, value)

        class Vmvmpsreconfirm(Enum):
            """
            Vmvmpsreconfirm

            Setting this object to execute(2) causes the switch

            to reconfirm membership of every dynamic port.

            Reading this object always return ready(1).

            .. data:: ready = 1

            .. data:: execute = 2

            """

            ready = Enum.YLeaf(1, "ready")

            execute = Enum.YLeaf(2, "execute")


        class Vmvmpsreconfirmresult(Enum):
            """
            Vmvmpsreconfirmresult

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


        def has_data(self):
            return (
                self.vmvmpscurrent.is_set or
                self.vmvmpsreconfirm.is_set or
                self.vmvmpsreconfirminterval.is_set or
                self.vmvmpsreconfirmresult.is_set or
                self.vmvmpsretries.is_set or
                self.vmvmpsvqpversion.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.vmvmpscurrent.yfilter != YFilter.not_set or
                self.vmvmpsreconfirm.yfilter != YFilter.not_set or
                self.vmvmpsreconfirminterval.yfilter != YFilter.not_set or
                self.vmvmpsreconfirmresult.yfilter != YFilter.not_set or
                self.vmvmpsretries.yfilter != YFilter.not_set or
                self.vmvmpsvqpversion.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vmVmps" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.vmvmpscurrent.is_set or self.vmvmpscurrent.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vmvmpscurrent.get_name_leafdata())
            if (self.vmvmpsreconfirm.is_set or self.vmvmpsreconfirm.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vmvmpsreconfirm.get_name_leafdata())
            if (self.vmvmpsreconfirminterval.is_set or self.vmvmpsreconfirminterval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vmvmpsreconfirminterval.get_name_leafdata())
            if (self.vmvmpsreconfirmresult.is_set or self.vmvmpsreconfirmresult.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vmvmpsreconfirmresult.get_name_leafdata())
            if (self.vmvmpsretries.is_set or self.vmvmpsretries.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vmvmpsretries.get_name_leafdata())
            if (self.vmvmpsvqpversion.is_set or self.vmvmpsvqpversion.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vmvmpsvqpversion.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vmVmpsCurrent" or name == "vmVmpsReconfirm" or name == "vmVmpsReconfirmInterval" or name == "vmVmpsReconfirmResult" or name == "vmVmpsRetries" or name == "vmVmpsVQPVersion"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "vmVmpsCurrent"):
                self.vmvmpscurrent = value
                self.vmvmpscurrent.value_namespace = name_space
                self.vmvmpscurrent.value_namespace_prefix = name_space_prefix
            if(value_path == "vmVmpsReconfirm"):
                self.vmvmpsreconfirm = value
                self.vmvmpsreconfirm.value_namespace = name_space
                self.vmvmpsreconfirm.value_namespace_prefix = name_space_prefix
            if(value_path == "vmVmpsReconfirmInterval"):
                self.vmvmpsreconfirminterval = value
                self.vmvmpsreconfirminterval.value_namespace = name_space
                self.vmvmpsreconfirminterval.value_namespace_prefix = name_space_prefix
            if(value_path == "vmVmpsReconfirmResult"):
                self.vmvmpsreconfirmresult = value
                self.vmvmpsreconfirmresult.value_namespace = name_space
                self.vmvmpsreconfirmresult.value_namespace_prefix = name_space_prefix
            if(value_path == "vmVmpsRetries"):
                self.vmvmpsretries = value
                self.vmvmpsretries.value_namespace = name_space
                self.vmvmpsretries.value_namespace_prefix = name_space_prefix
            if(value_path == "vmVmpsVQPVersion"):
                self.vmvmpsvqpversion = value
                self.vmvmpsvqpversion.value_namespace = name_space
                self.vmvmpsvqpversion.value_namespace_prefix = name_space_prefix


    class Vmmembership(Entity):
        """
        
        
        .. attribute:: vmvlancreationmode
        
        	This object is used to determine whether or not a non\-existing VLAN will be created automatically by the system after assigned to a port.  automatic(1)\:  a non\-existing VLAN will be created                automatically by the system after                assigned to a port.  manual(2)\:     a non\-existing VLAN will not be created                automatically by the system and need to be                manually created by the users after assigned                to a port
        	**type**\:   :py:class:`Vmvlancreationmode <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmmembership.Vmvlancreationmode>`
        
        

        """

        _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
        _revision = '2007-12-14'

        def __init__(self):
            super(CiscoVlanMembershipMib.Vmmembership, self).__init__()

            self.yang_name = "vmMembership"
            self.yang_parent_name = "CISCO-VLAN-MEMBERSHIP-MIB"

            self.vmvlancreationmode = YLeaf(YType.enumeration, "vmVlanCreationMode")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("vmvlancreationmode") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoVlanMembershipMib.Vmmembership, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVlanMembershipMib.Vmmembership, self).__setattr__(name, value)

        class Vmvlancreationmode(Enum):
            """
            Vmvlancreationmode

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


        def has_data(self):
            return self.vmvlancreationmode.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.vmvlancreationmode.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vmMembership" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.vmvlancreationmode.is_set or self.vmvlancreationmode.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vmvlancreationmode.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vmVlanCreationMode"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "vmVlanCreationMode"):
                self.vmvlancreationmode = value
                self.vmvlancreationmode.value_namespace = name_space
                self.vmvlancreationmode.value_namespace_prefix = name_space_prefix


    class Vmstatistics(Entity):
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
            super(CiscoVlanMembershipMib.Vmstatistics, self).__init__()

            self.yang_name = "vmStatistics"
            self.yang_parent_name = "CISCO-VLAN-MEMBERSHIP-MIB"

            self.vminsufficientresources = YLeaf(YType.uint32, "vmInsufficientResources")

            self.vmvmpschanges = YLeaf(YType.uint32, "vmVmpsChanges")

            self.vmvqpdenied = YLeaf(YType.uint32, "vmVQPDenied")

            self.vmvqpqueries = YLeaf(YType.uint32, "vmVQPQueries")

            self.vmvqpresponses = YLeaf(YType.uint32, "vmVQPResponses")

            self.vmvqpshutdown = YLeaf(YType.uint32, "vmVQPShutdown")

            self.vmvqpwrongdomain = YLeaf(YType.uint32, "vmVQPWrongDomain")

            self.vmvqpwrongversion = YLeaf(YType.uint32, "vmVQPWrongVersion")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("vminsufficientresources",
                            "vmvmpschanges",
                            "vmvqpdenied",
                            "vmvqpqueries",
                            "vmvqpresponses",
                            "vmvqpshutdown",
                            "vmvqpwrongdomain",
                            "vmvqpwrongversion") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoVlanMembershipMib.Vmstatistics, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVlanMembershipMib.Vmstatistics, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.vminsufficientresources.is_set or
                self.vmvmpschanges.is_set or
                self.vmvqpdenied.is_set or
                self.vmvqpqueries.is_set or
                self.vmvqpresponses.is_set or
                self.vmvqpshutdown.is_set or
                self.vmvqpwrongdomain.is_set or
                self.vmvqpwrongversion.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.vminsufficientresources.yfilter != YFilter.not_set or
                self.vmvmpschanges.yfilter != YFilter.not_set or
                self.vmvqpdenied.yfilter != YFilter.not_set or
                self.vmvqpqueries.yfilter != YFilter.not_set or
                self.vmvqpresponses.yfilter != YFilter.not_set or
                self.vmvqpshutdown.yfilter != YFilter.not_set or
                self.vmvqpwrongdomain.yfilter != YFilter.not_set or
                self.vmvqpwrongversion.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vmStatistics" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.vminsufficientresources.is_set or self.vminsufficientresources.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vminsufficientresources.get_name_leafdata())
            if (self.vmvmpschanges.is_set or self.vmvmpschanges.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vmvmpschanges.get_name_leafdata())
            if (self.vmvqpdenied.is_set or self.vmvqpdenied.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vmvqpdenied.get_name_leafdata())
            if (self.vmvqpqueries.is_set or self.vmvqpqueries.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vmvqpqueries.get_name_leafdata())
            if (self.vmvqpresponses.is_set or self.vmvqpresponses.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vmvqpresponses.get_name_leafdata())
            if (self.vmvqpshutdown.is_set or self.vmvqpshutdown.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vmvqpshutdown.get_name_leafdata())
            if (self.vmvqpwrongdomain.is_set or self.vmvqpwrongdomain.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vmvqpwrongdomain.get_name_leafdata())
            if (self.vmvqpwrongversion.is_set or self.vmvqpwrongversion.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vmvqpwrongversion.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vmInsufficientResources" or name == "vmVmpsChanges" or name == "vmVQPDenied" or name == "vmVQPQueries" or name == "vmVQPResponses" or name == "vmVQPShutdown" or name == "vmVQPWrongDomain" or name == "vmVQPWrongVersion"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "vmInsufficientResources"):
                self.vminsufficientresources = value
                self.vminsufficientresources.value_namespace = name_space
                self.vminsufficientresources.value_namespace_prefix = name_space_prefix
            if(value_path == "vmVmpsChanges"):
                self.vmvmpschanges = value
                self.vmvmpschanges.value_namespace = name_space
                self.vmvmpschanges.value_namespace_prefix = name_space_prefix
            if(value_path == "vmVQPDenied"):
                self.vmvqpdenied = value
                self.vmvqpdenied.value_namespace = name_space
                self.vmvqpdenied.value_namespace_prefix = name_space_prefix
            if(value_path == "vmVQPQueries"):
                self.vmvqpqueries = value
                self.vmvqpqueries.value_namespace = name_space
                self.vmvqpqueries.value_namespace_prefix = name_space_prefix
            if(value_path == "vmVQPResponses"):
                self.vmvqpresponses = value
                self.vmvqpresponses.value_namespace = name_space
                self.vmvqpresponses.value_namespace_prefix = name_space_prefix
            if(value_path == "vmVQPShutdown"):
                self.vmvqpshutdown = value
                self.vmvqpshutdown.value_namespace = name_space
                self.vmvqpshutdown.value_namespace_prefix = name_space_prefix
            if(value_path == "vmVQPWrongDomain"):
                self.vmvqpwrongdomain = value
                self.vmvqpwrongdomain.value_namespace = name_space
                self.vmvqpwrongdomain.value_namespace_prefix = name_space_prefix
            if(value_path == "vmVQPWrongVersion"):
                self.vmvqpwrongversion = value
                self.vmvqpwrongversion.value_namespace = name_space
                self.vmvqpwrongversion.value_namespace_prefix = name_space_prefix


    class Vmstatus(Entity):
        """
        
        
        .. attribute:: vmnotificationsenabled
        
        	An indication of whether the notifications/traps defined in this MIB are enabled
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
        _revision = '2007-12-14'

        def __init__(self):
            super(CiscoVlanMembershipMib.Vmstatus, self).__init__()

            self.yang_name = "vmStatus"
            self.yang_parent_name = "CISCO-VLAN-MEMBERSHIP-MIB"

            self.vmnotificationsenabled = YLeaf(YType.boolean, "vmNotificationsEnabled")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("vmnotificationsenabled") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoVlanMembershipMib.Vmstatus, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVlanMembershipMib.Vmstatus, self).__setattr__(name, value)

        def has_data(self):
            return self.vmnotificationsenabled.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.vmnotificationsenabled.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vmStatus" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.vmnotificationsenabled.is_set or self.vmnotificationsenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vmnotificationsenabled.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vmNotificationsEnabled"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "vmNotificationsEnabled"):
                self.vmnotificationsenabled = value
                self.vmnotificationsenabled.value_namespace = name_space
                self.vmnotificationsenabled.value_namespace_prefix = name_space_prefix


    class Vmvmpstable(Entity):
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
            super(CiscoVlanMembershipMib.Vmvmpstable, self).__init__()

            self.yang_name = "vmVmpsTable"
            self.yang_parent_name = "CISCO-VLAN-MEMBERSHIP-MIB"

            self.vmvmpsentry = YList(self)

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
                        super(CiscoVlanMembershipMib.Vmvmpstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVlanMembershipMib.Vmvmpstable, self).__setattr__(name, value)


        class Vmvmpsentry(Entity):
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
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
            _revision = '2007-12-14'

            def __init__(self):
                super(CiscoVlanMembershipMib.Vmvmpstable.Vmvmpsentry, self).__init__()

                self.yang_name = "vmVmpsEntry"
                self.yang_parent_name = "vmVmpsTable"

                self.vmvmpsipaddress = YLeaf(YType.str, "vmVmpsIpAddress")

                self.vmvmpsprimary = YLeaf(YType.boolean, "vmVmpsPrimary")

                self.vmvmpsrowstatus = YLeaf(YType.enumeration, "vmVmpsRowStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vmvmpsipaddress",
                                "vmvmpsprimary",
                                "vmvmpsrowstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVlanMembershipMib.Vmvmpstable.Vmvmpsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVlanMembershipMib.Vmvmpstable.Vmvmpsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.vmvmpsipaddress.is_set or
                    self.vmvmpsprimary.is_set or
                    self.vmvmpsrowstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vmvmpsipaddress.yfilter != YFilter.not_set or
                    self.vmvmpsprimary.yfilter != YFilter.not_set or
                    self.vmvmpsrowstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vmVmpsEntry" + "[vmVmpsIpAddress='" + self.vmvmpsipaddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/vmVmpsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vmvmpsipaddress.is_set or self.vmvmpsipaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vmvmpsipaddress.get_name_leafdata())
                if (self.vmvmpsprimary.is_set or self.vmvmpsprimary.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vmvmpsprimary.get_name_leafdata())
                if (self.vmvmpsrowstatus.is_set or self.vmvmpsrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vmvmpsrowstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "vmVmpsIpAddress" or name == "vmVmpsPrimary" or name == "vmVmpsRowStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vmVmpsIpAddress"):
                    self.vmvmpsipaddress = value
                    self.vmvmpsipaddress.value_namespace = name_space
                    self.vmvmpsipaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "vmVmpsPrimary"):
                    self.vmvmpsprimary = value
                    self.vmvmpsprimary.value_namespace = name_space
                    self.vmvmpsprimary.value_namespace_prefix = name_space_prefix
                if(value_path == "vmVmpsRowStatus"):
                    self.vmvmpsrowstatus = value
                    self.vmvmpsrowstatus.value_namespace = name_space
                    self.vmvmpsrowstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vmvmpsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vmvmpsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vmVmpsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vmVmpsEntry"):
                for c in self.vmvmpsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVlanMembershipMib.Vmvmpstable.Vmvmpsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vmvmpsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vmVmpsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Vmmembershipsummarytable(Entity):
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
            super(CiscoVlanMembershipMib.Vmmembershipsummarytable, self).__init__()

            self.yang_name = "vmMembershipSummaryTable"
            self.yang_parent_name = "CISCO-VLAN-MEMBERSHIP-MIB"

            self.vmmembershipsummaryentry = YList(self)

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
                        super(CiscoVlanMembershipMib.Vmmembershipsummarytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVlanMembershipMib.Vmmembershipsummarytable, self).__setattr__(name, value)


        class Vmmembershipsummaryentry(Entity):
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
                super(CiscoVlanMembershipMib.Vmmembershipsummarytable.Vmmembershipsummaryentry, self).__init__()

                self.yang_name = "vmMembershipSummaryEntry"
                self.yang_parent_name = "vmMembershipSummaryTable"

                self.vmmembershipsummaryvlanindex = YLeaf(YType.int32, "vmMembershipSummaryVlanIndex")

                self.vmmembershipsummarymember2kports = YLeaf(YType.str, "vmMembershipSummaryMember2kPorts")

                self.vmmembershipsummarymemberports = YLeaf(YType.str, "vmMembershipSummaryMemberPorts")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vmmembershipsummaryvlanindex",
                                "vmmembershipsummarymember2kports",
                                "vmmembershipsummarymemberports") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVlanMembershipMib.Vmmembershipsummarytable.Vmmembershipsummaryentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVlanMembershipMib.Vmmembershipsummarytable.Vmmembershipsummaryentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.vmmembershipsummaryvlanindex.is_set or
                    self.vmmembershipsummarymember2kports.is_set or
                    self.vmmembershipsummarymemberports.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vmmembershipsummaryvlanindex.yfilter != YFilter.not_set or
                    self.vmmembershipsummarymember2kports.yfilter != YFilter.not_set or
                    self.vmmembershipsummarymemberports.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vmMembershipSummaryEntry" + "[vmMembershipSummaryVlanIndex='" + self.vmmembershipsummaryvlanindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/vmMembershipSummaryTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vmmembershipsummaryvlanindex.is_set or self.vmmembershipsummaryvlanindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vmmembershipsummaryvlanindex.get_name_leafdata())
                if (self.vmmembershipsummarymember2kports.is_set or self.vmmembershipsummarymember2kports.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vmmembershipsummarymember2kports.get_name_leafdata())
                if (self.vmmembershipsummarymemberports.is_set or self.vmmembershipsummarymemberports.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vmmembershipsummarymemberports.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "vmMembershipSummaryVlanIndex" or name == "vmMembershipSummaryMember2kPorts" or name == "vmMembershipSummaryMemberPorts"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vmMembershipSummaryVlanIndex"):
                    self.vmmembershipsummaryvlanindex = value
                    self.vmmembershipsummaryvlanindex.value_namespace = name_space
                    self.vmmembershipsummaryvlanindex.value_namespace_prefix = name_space_prefix
                if(value_path == "vmMembershipSummaryMember2kPorts"):
                    self.vmmembershipsummarymember2kports = value
                    self.vmmembershipsummarymember2kports.value_namespace = name_space
                    self.vmmembershipsummarymember2kports.value_namespace_prefix = name_space_prefix
                if(value_path == "vmMembershipSummaryMemberPorts"):
                    self.vmmembershipsummarymemberports = value
                    self.vmmembershipsummarymemberports.value_namespace = name_space
                    self.vmmembershipsummarymemberports.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vmmembershipsummaryentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vmmembershipsummaryentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vmMembershipSummaryTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vmMembershipSummaryEntry"):
                for c in self.vmmembershipsummaryentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVlanMembershipMib.Vmmembershipsummarytable.Vmmembershipsummaryentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vmmembershipsummaryentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vmMembershipSummaryEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Vmmembershiptable(Entity):
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
            super(CiscoVlanMembershipMib.Vmmembershiptable, self).__init__()

            self.yang_name = "vmMembershipTable"
            self.yang_parent_name = "CISCO-VLAN-MEMBERSHIP-MIB"

            self.vmmembershipentry = YList(self)

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
                        super(CiscoVlanMembershipMib.Vmmembershiptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVlanMembershipMib.Vmmembershiptable, self).__setattr__(name, value)


        class Vmmembershipentry(Entity):
            """
            An entry (conceptual row) in the vmMembershipTable.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: vmportstatus
            
            	An indication of the current VLAN status of the port. A status of inactive(1) indicates that a dynamic port does not yet have a VLAN assigned, or a port is  assigned to a VLAN that is currently not active. A  status of active(2) indicates that the currently  assigned VLAN is active. A status of shutdown(3)  indicates that the port has been disabled as a result of VQP shutdown response
            	**type**\:   :py:class:`Vmportstatus <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmmembershiptable.Vmmembershipentry.Vmportstatus>`
            
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
            	**type**\:   :py:class:`Vmvlantype <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmmembershiptable.Vmmembershipentry.Vmvlantype>`
            
            

            """

            _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
            _revision = '2007-12-14'

            def __init__(self):
                super(CiscoVlanMembershipMib.Vmmembershiptable.Vmmembershipentry, self).__init__()

                self.yang_name = "vmMembershipEntry"
                self.yang_parent_name = "vmMembershipTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.vmportstatus = YLeaf(YType.enumeration, "vmPortStatus")

                self.vmvlan = YLeaf(YType.int32, "vmVlan")

                self.vmvlans = YLeaf(YType.str, "vmVlans")

                self.vmvlans2k = YLeaf(YType.str, "vmVlans2k")

                self.vmvlans3k = YLeaf(YType.str, "vmVlans3k")

                self.vmvlans4k = YLeaf(YType.str, "vmVlans4k")

                self.vmvlantype = YLeaf(YType.enumeration, "vmVlanType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "vmportstatus",
                                "vmvlan",
                                "vmvlans",
                                "vmvlans2k",
                                "vmvlans3k",
                                "vmvlans4k",
                                "vmvlantype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVlanMembershipMib.Vmmembershiptable.Vmmembershipentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVlanMembershipMib.Vmmembershiptable.Vmmembershipentry, self).__setattr__(name, value)

            class Vmportstatus(Enum):
                """
                Vmportstatus

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


            class Vmvlantype(Enum):
                """
                Vmvlantype

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


            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.vmportstatus.is_set or
                    self.vmvlan.is_set or
                    self.vmvlans.is_set or
                    self.vmvlans2k.is_set or
                    self.vmvlans3k.is_set or
                    self.vmvlans4k.is_set or
                    self.vmvlantype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.vmportstatus.yfilter != YFilter.not_set or
                    self.vmvlan.yfilter != YFilter.not_set or
                    self.vmvlans.yfilter != YFilter.not_set or
                    self.vmvlans2k.yfilter != YFilter.not_set or
                    self.vmvlans3k.yfilter != YFilter.not_set or
                    self.vmvlans4k.yfilter != YFilter.not_set or
                    self.vmvlantype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vmMembershipEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/vmMembershipTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.vmportstatus.is_set or self.vmportstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vmportstatus.get_name_leafdata())
                if (self.vmvlan.is_set or self.vmvlan.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vmvlan.get_name_leafdata())
                if (self.vmvlans.is_set or self.vmvlans.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vmvlans.get_name_leafdata())
                if (self.vmvlans2k.is_set or self.vmvlans2k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vmvlans2k.get_name_leafdata())
                if (self.vmvlans3k.is_set or self.vmvlans3k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vmvlans3k.get_name_leafdata())
                if (self.vmvlans4k.is_set or self.vmvlans4k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vmvlans4k.get_name_leafdata())
                if (self.vmvlantype.is_set or self.vmvlantype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vmvlantype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "vmPortStatus" or name == "vmVlan" or name == "vmVlans" or name == "vmVlans2k" or name == "vmVlans3k" or name == "vmVlans4k" or name == "vmVlanType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "vmPortStatus"):
                    self.vmportstatus = value
                    self.vmportstatus.value_namespace = name_space
                    self.vmportstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "vmVlan"):
                    self.vmvlan = value
                    self.vmvlan.value_namespace = name_space
                    self.vmvlan.value_namespace_prefix = name_space_prefix
                if(value_path == "vmVlans"):
                    self.vmvlans = value
                    self.vmvlans.value_namespace = name_space
                    self.vmvlans.value_namespace_prefix = name_space_prefix
                if(value_path == "vmVlans2k"):
                    self.vmvlans2k = value
                    self.vmvlans2k.value_namespace = name_space
                    self.vmvlans2k.value_namespace_prefix = name_space_prefix
                if(value_path == "vmVlans3k"):
                    self.vmvlans3k = value
                    self.vmvlans3k.value_namespace = name_space
                    self.vmvlans3k.value_namespace_prefix = name_space_prefix
                if(value_path == "vmVlans4k"):
                    self.vmvlans4k = value
                    self.vmvlans4k.value_namespace = name_space
                    self.vmvlans4k.value_namespace_prefix = name_space_prefix
                if(value_path == "vmVlanType"):
                    self.vmvlantype = value
                    self.vmvlantype.value_namespace = name_space
                    self.vmvlantype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vmmembershipentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vmmembershipentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vmMembershipTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vmMembershipEntry"):
                for c in self.vmmembershipentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVlanMembershipMib.Vmmembershiptable.Vmmembershipentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vmmembershipentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vmMembershipEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Vmmembershipsummaryexttable(Entity):
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
            super(CiscoVlanMembershipMib.Vmmembershipsummaryexttable, self).__init__()

            self.yang_name = "vmMembershipSummaryExtTable"
            self.yang_parent_name = "CISCO-VLAN-MEMBERSHIP-MIB"

            self.vmmembershipsummaryextentry = YList(self)

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
                        super(CiscoVlanMembershipMib.Vmmembershipsummaryexttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVlanMembershipMib.Vmmembershipsummaryexttable, self).__setattr__(name, value)


        class Vmmembershipsummaryextentry(Entity):
            """
            An entry (conceptual row) in the
            vmMembershipSummaryExtTable.
            
            .. attribute:: vmmembershipsummaryvlanindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`vmmembershipsummaryvlanindex <ydk.models.cisco_ios_xe.CISCO_VLAN_MEMBERSHIP_MIB.CiscoVlanMembershipMib.Vmmembershipsummarytable.Vmmembershipsummaryentry>`
            
            .. attribute:: vmmembershipportrangeindex  <key>
            
            	The bridge port range index of this row
            	**type**\:   :py:class:`Ciscoportlistrange <ydk.models.cisco_ios_xe.CISCO_TC.Ciscoportlistrange>`
            
            .. attribute:: vmmembershipsummaryextports
            
            	The set of the device's member ports that belong to the VLAN. It has the VLAN membership information of up to 2k ports with the port number starting from the information indicated in vmMembershipPortRangeIndex object of the same row. For example, if the value of vmMembershipPortRangeIndex is 'twoKto4K', the port number indicated in this object starting from 2049 and ending to 4096.   A port number is the value of dot1dBasePort for the port in the BRIDGE\-MIB (RFC 1493)
            	**type**\:  str
            
            	**length:** 0..256
            
            

            """

            _prefix = 'CISCO-VLAN-MEMBERSHIP-MIB'
            _revision = '2007-12-14'

            def __init__(self):
                super(CiscoVlanMembershipMib.Vmmembershipsummaryexttable.Vmmembershipsummaryextentry, self).__init__()

                self.yang_name = "vmMembershipSummaryExtEntry"
                self.yang_parent_name = "vmMembershipSummaryExtTable"

                self.vmmembershipsummaryvlanindex = YLeaf(YType.str, "vmMembershipSummaryVlanIndex")

                self.vmmembershipportrangeindex = YLeaf(YType.enumeration, "vmMembershipPortRangeIndex")

                self.vmmembershipsummaryextports = YLeaf(YType.str, "vmMembershipSummaryExtPorts")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vmmembershipsummaryvlanindex",
                                "vmmembershipportrangeindex",
                                "vmmembershipsummaryextports") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVlanMembershipMib.Vmmembershipsummaryexttable.Vmmembershipsummaryextentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVlanMembershipMib.Vmmembershipsummaryexttable.Vmmembershipsummaryextentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.vmmembershipsummaryvlanindex.is_set or
                    self.vmmembershipportrangeindex.is_set or
                    self.vmmembershipsummaryextports.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vmmembershipsummaryvlanindex.yfilter != YFilter.not_set or
                    self.vmmembershipportrangeindex.yfilter != YFilter.not_set or
                    self.vmmembershipsummaryextports.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vmMembershipSummaryExtEntry" + "[vmMembershipSummaryVlanIndex='" + self.vmmembershipsummaryvlanindex.get() + "']" + "[vmMembershipPortRangeIndex='" + self.vmmembershipportrangeindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/vmMembershipSummaryExtTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vmmembershipsummaryvlanindex.is_set or self.vmmembershipsummaryvlanindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vmmembershipsummaryvlanindex.get_name_leafdata())
                if (self.vmmembershipportrangeindex.is_set or self.vmmembershipportrangeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vmmembershipportrangeindex.get_name_leafdata())
                if (self.vmmembershipsummaryextports.is_set or self.vmmembershipsummaryextports.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vmmembershipsummaryextports.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "vmMembershipSummaryVlanIndex" or name == "vmMembershipPortRangeIndex" or name == "vmMembershipSummaryExtPorts"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vmMembershipSummaryVlanIndex"):
                    self.vmmembershipsummaryvlanindex = value
                    self.vmmembershipsummaryvlanindex.value_namespace = name_space
                    self.vmmembershipsummaryvlanindex.value_namespace_prefix = name_space_prefix
                if(value_path == "vmMembershipPortRangeIndex"):
                    self.vmmembershipportrangeindex = value
                    self.vmmembershipportrangeindex.value_namespace = name_space
                    self.vmmembershipportrangeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "vmMembershipSummaryExtPorts"):
                    self.vmmembershipsummaryextports = value
                    self.vmmembershipsummaryextports.value_namespace = name_space
                    self.vmmembershipsummaryextports.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vmmembershipsummaryextentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vmmembershipsummaryextentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vmMembershipSummaryExtTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vmMembershipSummaryExtEntry"):
                for c in self.vmmembershipsummaryextentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVlanMembershipMib.Vmmembershipsummaryexttable.Vmmembershipsummaryextentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vmmembershipsummaryextentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vmMembershipSummaryExtEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Vmvoicevlantable(Entity):
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
            super(CiscoVlanMembershipMib.Vmvoicevlantable, self).__init__()

            self.yang_name = "vmVoiceVlanTable"
            self.yang_parent_name = "CISCO-VLAN-MEMBERSHIP-MIB"

            self.vmvoicevlanentry = YList(self)

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
                        super(CiscoVlanMembershipMib.Vmvoicevlantable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVlanMembershipMib.Vmvoicevlantable, self).__setattr__(name, value)


        class Vmvoicevlanentry(Entity):
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
                super(CiscoVlanMembershipMib.Vmvoicevlantable.Vmvoicevlanentry, self).__init__()

                self.yang_name = "vmVoiceVlanEntry"
                self.yang_parent_name = "vmVoiceVlanTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.vmvoicevlancdpverifyenable = YLeaf(YType.boolean, "vmVoiceVlanCdpVerifyEnable")

                self.vmvoicevlanid = YLeaf(YType.int32, "vmVoiceVlanId")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "vmvoicevlancdpverifyenable",
                                "vmvoicevlanid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVlanMembershipMib.Vmvoicevlantable.Vmvoicevlanentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVlanMembershipMib.Vmvoicevlantable.Vmvoicevlanentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.vmvoicevlancdpverifyenable.is_set or
                    self.vmvoicevlanid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.vmvoicevlancdpverifyenable.yfilter != YFilter.not_set or
                    self.vmvoicevlanid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vmVoiceVlanEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/vmVoiceVlanTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.vmvoicevlancdpverifyenable.is_set or self.vmvoicevlancdpverifyenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vmvoicevlancdpverifyenable.get_name_leafdata())
                if (self.vmvoicevlanid.is_set or self.vmvoicevlanid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vmvoicevlanid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "vmVoiceVlanCdpVerifyEnable" or name == "vmVoiceVlanId"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "vmVoiceVlanCdpVerifyEnable"):
                    self.vmvoicevlancdpverifyenable = value
                    self.vmvoicevlancdpverifyenable.value_namespace = name_space
                    self.vmvoicevlancdpverifyenable.value_namespace_prefix = name_space_prefix
                if(value_path == "vmVoiceVlanId"):
                    self.vmvoicevlanid = value
                    self.vmvoicevlanid.value_namespace = name_space
                    self.vmvoicevlanid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vmvoicevlanentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vmvoicevlanentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vmVoiceVlanTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vmVoiceVlanEntry"):
                for c in self.vmvoicevlanentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVlanMembershipMib.Vmvoicevlantable.Vmvoicevlanentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vmvoicevlanentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vmVoiceVlanEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.vmmembership is not None and self.vmmembership.has_data()) or
            (self.vmmembershipsummaryexttable is not None and self.vmmembershipsummaryexttable.has_data()) or
            (self.vmmembershipsummarytable is not None and self.vmmembershipsummarytable.has_data()) or
            (self.vmmembershiptable is not None and self.vmmembershiptable.has_data()) or
            (self.vmstatistics is not None and self.vmstatistics.has_data()) or
            (self.vmstatus is not None and self.vmstatus.has_data()) or
            (self.vmvmps is not None and self.vmvmps.has_data()) or
            (self.vmvmpstable is not None and self.vmvmpstable.has_data()) or
            (self.vmvoicevlantable is not None and self.vmvoicevlantable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.vmmembership is not None and self.vmmembership.has_operation()) or
            (self.vmmembershipsummaryexttable is not None and self.vmmembershipsummaryexttable.has_operation()) or
            (self.vmmembershipsummarytable is not None and self.vmmembershipsummarytable.has_operation()) or
            (self.vmmembershiptable is not None and self.vmmembershiptable.has_operation()) or
            (self.vmstatistics is not None and self.vmstatistics.has_operation()) or
            (self.vmstatus is not None and self.vmstatus.has_operation()) or
            (self.vmvmps is not None and self.vmvmps.has_operation()) or
            (self.vmvmpstable is not None and self.vmvmpstable.has_operation()) or
            (self.vmvoicevlantable is not None and self.vmvoicevlantable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-VLAN-MEMBERSHIP-MIB:CISCO-VLAN-MEMBERSHIP-MIB" + path_buffer

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

        if (child_yang_name == "vmMembership"):
            if (self.vmmembership is None):
                self.vmmembership = CiscoVlanMembershipMib.Vmmembership()
                self.vmmembership.parent = self
                self._children_name_map["vmmembership"] = "vmMembership"
            return self.vmmembership

        if (child_yang_name == "vmMembershipSummaryExtTable"):
            if (self.vmmembershipsummaryexttable is None):
                self.vmmembershipsummaryexttable = CiscoVlanMembershipMib.Vmmembershipsummaryexttable()
                self.vmmembershipsummaryexttable.parent = self
                self._children_name_map["vmmembershipsummaryexttable"] = "vmMembershipSummaryExtTable"
            return self.vmmembershipsummaryexttable

        if (child_yang_name == "vmMembershipSummaryTable"):
            if (self.vmmembershipsummarytable is None):
                self.vmmembershipsummarytable = CiscoVlanMembershipMib.Vmmembershipsummarytable()
                self.vmmembershipsummarytable.parent = self
                self._children_name_map["vmmembershipsummarytable"] = "vmMembershipSummaryTable"
            return self.vmmembershipsummarytable

        if (child_yang_name == "vmMembershipTable"):
            if (self.vmmembershiptable is None):
                self.vmmembershiptable = CiscoVlanMembershipMib.Vmmembershiptable()
                self.vmmembershiptable.parent = self
                self._children_name_map["vmmembershiptable"] = "vmMembershipTable"
            return self.vmmembershiptable

        if (child_yang_name == "vmStatistics"):
            if (self.vmstatistics is None):
                self.vmstatistics = CiscoVlanMembershipMib.Vmstatistics()
                self.vmstatistics.parent = self
                self._children_name_map["vmstatistics"] = "vmStatistics"
            return self.vmstatistics

        if (child_yang_name == "vmStatus"):
            if (self.vmstatus is None):
                self.vmstatus = CiscoVlanMembershipMib.Vmstatus()
                self.vmstatus.parent = self
                self._children_name_map["vmstatus"] = "vmStatus"
            return self.vmstatus

        if (child_yang_name == "vmVmps"):
            if (self.vmvmps is None):
                self.vmvmps = CiscoVlanMembershipMib.Vmvmps()
                self.vmvmps.parent = self
                self._children_name_map["vmvmps"] = "vmVmps"
            return self.vmvmps

        if (child_yang_name == "vmVmpsTable"):
            if (self.vmvmpstable is None):
                self.vmvmpstable = CiscoVlanMembershipMib.Vmvmpstable()
                self.vmvmpstable.parent = self
                self._children_name_map["vmvmpstable"] = "vmVmpsTable"
            return self.vmvmpstable

        if (child_yang_name == "vmVoiceVlanTable"):
            if (self.vmvoicevlantable is None):
                self.vmvoicevlantable = CiscoVlanMembershipMib.Vmvoicevlantable()
                self.vmvoicevlantable.parent = self
                self._children_name_map["vmvoicevlantable"] = "vmVoiceVlanTable"
            return self.vmvoicevlantable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "vmMembership" or name == "vmMembershipSummaryExtTable" or name == "vmMembershipSummaryTable" or name == "vmMembershipTable" or name == "vmStatistics" or name == "vmStatus" or name == "vmVmps" or name == "vmVmpsTable" or name == "vmVoiceVlanTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoVlanMembershipMib()
        return self._top_entity


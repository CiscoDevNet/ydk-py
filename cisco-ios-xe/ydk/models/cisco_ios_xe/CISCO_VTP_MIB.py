""" CISCO_VTP_MIB 

The MIB module for entities implementing the VTP
protocol and Vlan management.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Vlantype(Enum):
    """
    Vlantype

    The type of a VLAN.

    Note that the 'ethernet' type, is used for any ethernet or

    802.3 VLAN, including an ATM Ethernet ELAN; and the

    'tokenRing' ('trCrf') type is used for each VLAN

    representing a single logical 802.5 ring including an ATM

    Token\-Ring ELAN.

    The 'trCrf' type is used for token ring VLANs made up of

    (at most) one transparently bridged LAN segment.

    The 'trBrf' type is used for VLANs which represent the

    scope of many 'trCrf' VLANs all connected together via

    source route bridging.  The token ring 'trBrf' can be said

    to represent the bridged broadcast domain.

    .. data:: ethernet = 1

    .. data:: fddi = 2

    .. data:: tokenRing = 3

    .. data:: fddiNet = 4

    .. data:: trNet = 5

    .. data:: deprecated = 6

    """

    ethernet = Enum.YLeaf(1, "ethernet")

    fddi = Enum.YLeaf(2, "fddi")

    tokenRing = Enum.YLeaf(3, "tokenRing")

    fddiNet = Enum.YLeaf(4, "fddiNet")

    trNet = Enum.YLeaf(5, "trNet")

    deprecated = Enum.YLeaf(6, "deprecated")


class Vlantypeext(Bits):
    """
    Vlantypeext

    The additional type information of VLAN.
    vtpmanageable(0)    An user defined VLAN which is 
                        manageable through VTP protocol.
                        The value of this bit cannot be 
                        changed.
    internal(1)         An internal VLAN created by the device.
                        Internal VLANs cannot be created or
                        deleted. The value of this bit cannot
                        be changed.
    reserved(2)         A VLAN reserved by the device.
                        Reserved VLANs cannot be created or
                        deleted. The value of this bit cannot
                        be changed.
    rspan(3)            A VLAN created to exclusively carry
                        the traffic for a Remote Switched
                        Port Analyzer (RSPAN). This bit can
                        only be set or cleared during the
                        VLAN creation. Once the VLAN is
                        created, the value of this bit cannot
                        be modified.
    dynamicGvrp(4)      A VLAN dynamically created by GVRP
                        (GARP VLAN Registration Protocol)
                        propagation. The value of this bit 
                        cannot be changed.
    Keys are:- vtpmanageable , rspan , internal , dynamicGvrp , reserved

    """

    def __init__(self):
        super(Vlantypeext, self).__init__()


class CiscoVtpMib(Entity):
    """
    
    
    .. attribute:: internalvlaninfo
    
    	
    	**type**\:   :py:class:`Internalvlaninfo <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Internalvlaninfo>`
    
    .. attribute:: managementdomaintable
    
    	The table containing information on the management domains in which the local system is participating.  Devices which support only one management domain will support just one row in this table, and will not let it be deleted nor let other rows be created.  Devices which support multiple management domains will allow rows to be created and deleted, but will not allow the last row to be deleted. If the device does  not support VTP, the table is read\-only
    	**type**\:   :py:class:`Managementdomaintable <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Managementdomaintable>`
    
    .. attribute:: vlanstatistics
    
    	
    	**type**\:   :py:class:`Vlanstatistics <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vlanstatistics>`
    
    .. attribute:: vlantrunkports
    
    	
    	**type**\:   :py:class:`Vlantrunkports <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vlantrunkports>`
    
    .. attribute:: vlantrunkporttable
    
    	The table containing information on the local system's VLAN trunk ports
    	**type**\:   :py:class:`Vlantrunkporttable <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vlantrunkporttable>`
    
    .. attribute:: vtpauthenticationtable
    
    	The table contains the authentication information of VTP in which the local system participates.  The security mechanism of VTP relies on a secret key that is used to alter the MD5 digest of the packets transmitted on the wire.  The secret value is created from a password that may be saved in plain text in the configuration or hidden from the configuration.  The device creating or modifying the VTP configuration signs it using the MD5 digest generated from the secret key before advertising it. Other devices in the domain receive this configuration use the same secret key to accept it if correctly signed or drop it otherwise.  The user has the option to hide the password from the configuration. Once the password is hidden, the secret key generated from the password is shown in the  configuration instead, and there is no other way to  show the password in plain text again but clearing  it or resetting it.   In an un\-trusted area, the password on a device can  be configured without being unveiled. After that, it has to be provided again by setting the same  value to vtpDatabaseTakeOverPassword if the user  wants to take over the whole VTP management domain of the database type.  When managementDomainVersionInUse is version3(4), the  authentication mechanism is common to all VTP database type
    	**type**\:   :py:class:`Vtpauthenticationtable <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpauthenticationtable>`
    
    .. attribute:: vtpdatabasetable
    
    	This table contains information of the VTP databases. It is not instantiated when managementDomainVersionInUse is version1(1),  version2(3) or none(3)
    	**type**\:   :py:class:`Vtpdatabasetable <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpdatabasetable>`
    
    .. attribute:: vtpdiscoverresulttable
    
    	The table containing information of discovered VTP members in the management domain in which the local system is participating. This table is not instantiated when  managementDomainVersionInUse is version1(1), version2(2) or none(3)
    	**type**\:   :py:class:`Vtpdiscoverresulttable <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpdiscoverresulttable>`
    
    .. attribute:: vtpdiscovertable
    
    	This table contains information related to the discovery of the VTP members in the designated management domain. This table is not instantiated when  managementDomainVersionInUse is version1(1), version2(3) or none(3)
    	**type**\:   :py:class:`Vtpdiscovertable <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpdiscovertable>`
    
    .. attribute:: vtpinternalvlantable
    
    	A vtpInternalVlanTable entry contains information on an existing internal VLAN. It is internally created by the device for a specific application program  and hence owned by the application.   It cannot be modified or deleted by (local  or network) management
    	**type**\:   :py:class:`Vtpinternalvlantable <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpinternalvlantable>`
    
    .. attribute:: vtpstatus
    
    	
    	**type**\:   :py:class:`Vtpstatus <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpstatus>`
    
    .. attribute:: vtpvlanedittable
    
    	The table which contains the information in the Edit Buffers, one Edit Buffer per management domain.  The information for a particular management domain is initialized, by a 'copy' operation, to be the current global VLAN information for that management domain.  After initialization, editing can be performed to add VLANs, delete VLANs, or modify their global parameters.  The information as modified through editing is local to this Edit Buffer.  An apply operation using the vtpVlanEditOperation object is necessary to instanciate the modified information as the new global VLAN information for that management domain.  To use the Edit Buffer, a manager acts as follows\:  1. ensures the Edit Buffer for a management domain is empty, i.e., there are no rows in this table for this management domain.  2. issues a SNMP set operation which sets vtpVlanEditOperation to 'copy', and vtpVlanEditBufferOwner to its own identifier (e.g., its own IP address).  3. if this set operation is successful, proceeds to edit the information in the vtpVlanEditTable.  4. if and when the edited information is to be instantiated, issues a SNMP set operation which sets vtpVlanEditOperation to 'apply'.  5. issues retrieval requests to obtain the value of vtpVlanApplyStatus, until the result of the apply is determined.  6. releases the Edit Buffer by issuing a SNMP set operation which sets vtpVlanEditOperation to 'release'.  Note that the information contained in this table is not saved across agent reboots
    	**type**\:   :py:class:`Vtpvlanedittable <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpvlanedittable>`
    
    .. attribute:: vtpvlanlocalshutdowntable
    
    	Ths table contains the VLAN local shutdown information within management domain
    	**type**\:   :py:class:`Vtpvlanlocalshutdowntable <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpvlanlocalshutdowntable>`
    
    .. attribute:: vtpvlantable
    
    	This table contains information on the VLANs which currently exist
    	**type**\:   :py:class:`Vtpvlantable <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpvlantable>`
    
    

    """

    _prefix = 'CISCO-VTP-MIB'
    _revision = '2013-10-14'

    def __init__(self):
        super(CiscoVtpMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-VTP-MIB"
        self.yang_parent_name = "CISCO-VTP-MIB"

        self.internalvlaninfo = CiscoVtpMib.Internalvlaninfo()
        self.internalvlaninfo.parent = self
        self._children_name_map["internalvlaninfo"] = "internalVlanInfo"
        self._children_yang_names.add("internalVlanInfo")

        self.managementdomaintable = CiscoVtpMib.Managementdomaintable()
        self.managementdomaintable.parent = self
        self._children_name_map["managementdomaintable"] = "managementDomainTable"
        self._children_yang_names.add("managementDomainTable")

        self.vlanstatistics = CiscoVtpMib.Vlanstatistics()
        self.vlanstatistics.parent = self
        self._children_name_map["vlanstatistics"] = "vlanStatistics"
        self._children_yang_names.add("vlanStatistics")

        self.vlantrunkports = CiscoVtpMib.Vlantrunkports()
        self.vlantrunkports.parent = self
        self._children_name_map["vlantrunkports"] = "vlanTrunkPorts"
        self._children_yang_names.add("vlanTrunkPorts")

        self.vlantrunkporttable = CiscoVtpMib.Vlantrunkporttable()
        self.vlantrunkporttable.parent = self
        self._children_name_map["vlantrunkporttable"] = "vlanTrunkPortTable"
        self._children_yang_names.add("vlanTrunkPortTable")

        self.vtpauthenticationtable = CiscoVtpMib.Vtpauthenticationtable()
        self.vtpauthenticationtable.parent = self
        self._children_name_map["vtpauthenticationtable"] = "vtpAuthenticationTable"
        self._children_yang_names.add("vtpAuthenticationTable")

        self.vtpdatabasetable = CiscoVtpMib.Vtpdatabasetable()
        self.vtpdatabasetable.parent = self
        self._children_name_map["vtpdatabasetable"] = "vtpDatabaseTable"
        self._children_yang_names.add("vtpDatabaseTable")

        self.vtpdiscoverresulttable = CiscoVtpMib.Vtpdiscoverresulttable()
        self.vtpdiscoverresulttable.parent = self
        self._children_name_map["vtpdiscoverresulttable"] = "vtpDiscoverResultTable"
        self._children_yang_names.add("vtpDiscoverResultTable")

        self.vtpdiscovertable = CiscoVtpMib.Vtpdiscovertable()
        self.vtpdiscovertable.parent = self
        self._children_name_map["vtpdiscovertable"] = "vtpDiscoverTable"
        self._children_yang_names.add("vtpDiscoverTable")

        self.vtpinternalvlantable = CiscoVtpMib.Vtpinternalvlantable()
        self.vtpinternalvlantable.parent = self
        self._children_name_map["vtpinternalvlantable"] = "vtpInternalVlanTable"
        self._children_yang_names.add("vtpInternalVlanTable")

        self.vtpstatus = CiscoVtpMib.Vtpstatus()
        self.vtpstatus.parent = self
        self._children_name_map["vtpstatus"] = "vtpStatus"
        self._children_yang_names.add("vtpStatus")

        self.vtpvlanedittable = CiscoVtpMib.Vtpvlanedittable()
        self.vtpvlanedittable.parent = self
        self._children_name_map["vtpvlanedittable"] = "vtpVlanEditTable"
        self._children_yang_names.add("vtpVlanEditTable")

        self.vtpvlanlocalshutdowntable = CiscoVtpMib.Vtpvlanlocalshutdowntable()
        self.vtpvlanlocalshutdowntable.parent = self
        self._children_name_map["vtpvlanlocalshutdowntable"] = "vtpVlanLocalShutdownTable"
        self._children_yang_names.add("vtpVlanLocalShutdownTable")

        self.vtpvlantable = CiscoVtpMib.Vtpvlantable()
        self.vtpvlantable.parent = self
        self._children_name_map["vtpvlantable"] = "vtpVlanTable"
        self._children_yang_names.add("vtpVlanTable")


    class Vtpstatus(Entity):
        """
        
        
        .. attribute:: vtpmaxvlanstorage
        
        	An estimate of the maximum number of VLANs about which the local system can recover complete VTP information after a reboot.  If the number of defined VLANs is greater than this value, then the system can not act as a VTP Server. For a device which has no means to calculate the estimated number, this value is \-1
        	**type**\:  int
        
        	**range:** \-1..1023
        
        .. attribute:: vtpnotificationsenabled
        
        	An indication of whether the notifications/traps defined by the vtpConfigNotificationsGroup, vtpConfigNotificationsGroup2, and vtpConfigNotificationsGroup8 are enabled
        	**type**\:  bool
        
        .. attribute:: vtpversion
        
        	The version of VTP in use on the local system.  A device will report its version capability and not any particular version in use on the device. If the device does not support vtp, the version is none(3)
        	**type**\:   :py:class:`Vtpversion <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpstatus.Vtpversion>`
        
        .. attribute:: vtpvlancreatednotifenabled
        
        	An indication of whether the notification should be generated when a VLAN is created.   If the value of this object is 'true' then the vtpVlanCreated notification will be generated.  If the value of this object is 'false' then the vtpVlanCreated notification will not be generated
        	**type**\:  bool
        
        .. attribute:: vtpvlandeletednotifenabled
        
        	An indication of whether the notification should be generated when a VLAN is deleted.    If the value of this object is 'true' then the vtpVlanDeleted notification will be generated.  If the value of this object is 'false' then the vtpVlanDeleted notification will not be generated
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CiscoVtpMib.Vtpstatus, self).__init__()

            self.yang_name = "vtpStatus"
            self.yang_parent_name = "CISCO-VTP-MIB"

            self.vtpmaxvlanstorage = YLeaf(YType.int32, "vtpMaxVlanStorage")

            self.vtpnotificationsenabled = YLeaf(YType.boolean, "vtpNotificationsEnabled")

            self.vtpversion = YLeaf(YType.enumeration, "vtpVersion")

            self.vtpvlancreatednotifenabled = YLeaf(YType.boolean, "vtpVlanCreatedNotifEnabled")

            self.vtpvlandeletednotifenabled = YLeaf(YType.boolean, "vtpVlanDeletedNotifEnabled")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("vtpmaxvlanstorage",
                            "vtpnotificationsenabled",
                            "vtpversion",
                            "vtpvlancreatednotifenabled",
                            "vtpvlandeletednotifenabled") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoVtpMib.Vtpstatus, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVtpMib.Vtpstatus, self).__setattr__(name, value)

        class Vtpversion(Enum):
            """
            Vtpversion

            The version of VTP in use on the local system.  A device

            will report its version capability and not any particular

            version in use on the device. If the device does not support

            vtp, the version is none(3).

            .. data:: one = 1

            .. data:: two = 2

            .. data:: none = 3

            .. data:: three = 4

            """

            one = Enum.YLeaf(1, "one")

            two = Enum.YLeaf(2, "two")

            none = Enum.YLeaf(3, "none")

            three = Enum.YLeaf(4, "three")


        def has_data(self):
            return (
                self.vtpmaxvlanstorage.is_set or
                self.vtpnotificationsenabled.is_set or
                self.vtpversion.is_set or
                self.vtpvlancreatednotifenabled.is_set or
                self.vtpvlandeletednotifenabled.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.vtpmaxvlanstorage.yfilter != YFilter.not_set or
                self.vtpnotificationsenabled.yfilter != YFilter.not_set or
                self.vtpversion.yfilter != YFilter.not_set or
                self.vtpvlancreatednotifenabled.yfilter != YFilter.not_set or
                self.vtpvlandeletednotifenabled.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vtpStatus" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.vtpmaxvlanstorage.is_set or self.vtpmaxvlanstorage.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vtpmaxvlanstorage.get_name_leafdata())
            if (self.vtpnotificationsenabled.is_set or self.vtpnotificationsenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vtpnotificationsenabled.get_name_leafdata())
            if (self.vtpversion.is_set or self.vtpversion.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vtpversion.get_name_leafdata())
            if (self.vtpvlancreatednotifenabled.is_set or self.vtpvlancreatednotifenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vtpvlancreatednotifenabled.get_name_leafdata())
            if (self.vtpvlandeletednotifenabled.is_set or self.vtpvlandeletednotifenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vtpvlandeletednotifenabled.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vtpMaxVlanStorage" or name == "vtpNotificationsEnabled" or name == "vtpVersion" or name == "vtpVlanCreatedNotifEnabled" or name == "vtpVlanDeletedNotifEnabled"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "vtpMaxVlanStorage"):
                self.vtpmaxvlanstorage = value
                self.vtpmaxvlanstorage.value_namespace = name_space
                self.vtpmaxvlanstorage.value_namespace_prefix = name_space_prefix
            if(value_path == "vtpNotificationsEnabled"):
                self.vtpnotificationsenabled = value
                self.vtpnotificationsenabled.value_namespace = name_space
                self.vtpnotificationsenabled.value_namespace_prefix = name_space_prefix
            if(value_path == "vtpVersion"):
                self.vtpversion = value
                self.vtpversion.value_namespace = name_space
                self.vtpversion.value_namespace_prefix = name_space_prefix
            if(value_path == "vtpVlanCreatedNotifEnabled"):
                self.vtpvlancreatednotifenabled = value
                self.vtpvlancreatednotifenabled.value_namespace = name_space
                self.vtpvlancreatednotifenabled.value_namespace_prefix = name_space_prefix
            if(value_path == "vtpVlanDeletedNotifEnabled"):
                self.vtpvlandeletednotifenabled = value
                self.vtpvlandeletednotifenabled.value_namespace = name_space
                self.vtpvlandeletednotifenabled.value_namespace_prefix = name_space_prefix


    class Internalvlaninfo(Entity):
        """
        
        
        .. attribute:: vtpinternalvlanallocpolicy
        
        	The internal VLAN allocation policy.  'ascending'  \- internal VLANs are allocated                starting from a lowwer VLAN ID and                 upwards. 'descending' \- internal VLANs are allocated                starting from a higher VLAN ID and                downwards
        	**type**\:   :py:class:`Vtpinternalvlanallocpolicy <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Internalvlaninfo.Vtpinternalvlanallocpolicy>`
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CiscoVtpMib.Internalvlaninfo, self).__init__()

            self.yang_name = "internalVlanInfo"
            self.yang_parent_name = "CISCO-VTP-MIB"

            self.vtpinternalvlanallocpolicy = YLeaf(YType.enumeration, "vtpInternalVlanAllocPolicy")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("vtpinternalvlanallocpolicy") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoVtpMib.Internalvlaninfo, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVtpMib.Internalvlaninfo, self).__setattr__(name, value)

        class Vtpinternalvlanallocpolicy(Enum):
            """
            Vtpinternalvlanallocpolicy

            The internal VLAN allocation policy.

            'ascending'  \- internal VLANs are allocated

                           starting from a lowwer VLAN ID and 

                           upwards.

            'descending' \- internal VLANs are allocated

                           starting from a higher VLAN ID and

                           downwards.

            .. data:: ascending = 1

            .. data:: descending = 2

            """

            ascending = Enum.YLeaf(1, "ascending")

            descending = Enum.YLeaf(2, "descending")


        def has_data(self):
            return self.vtpinternalvlanallocpolicy.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.vtpinternalvlanallocpolicy.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "internalVlanInfo" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.vtpinternalvlanallocpolicy.is_set or self.vtpinternalvlanallocpolicy.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vtpinternalvlanallocpolicy.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vtpInternalVlanAllocPolicy"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "vtpInternalVlanAllocPolicy"):
                self.vtpinternalvlanallocpolicy = value
                self.vtpinternalvlanallocpolicy.value_namespace = name_space
                self.vtpinternalvlanallocpolicy.value_namespace_prefix = name_space_prefix


    class Vlantrunkports(Entity):
        """
        
        
        .. attribute:: vlantrunkportsdot1qtag
        
        	An indication of whether the tagging on all VLANs including native VLAN for all 802.1q trunks is enabled.  If this object has a value of true(1) then all VLANs including native VLAN are tagged.  If the value is false(2) then all VLANs excluding native VLAN are tagged.  This object has been deprecated and is replaced by the object 'cltcDot1qAllTaggedEnabled' in the CISCO\-L2\-TUNNEL\-CONFIG\-MIB
        	**type**\:  bool
        
        	**status**\: deprecated
        
        .. attribute:: vlantrunkportsetserialno
        
        	An advisory lock used to allow several cooperating SNMPv2 managers to coordinate their use of the SNMPv2 set operation acting upon any instance of vlanTrunkPortVlansEnabled
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CiscoVtpMib.Vlantrunkports, self).__init__()

            self.yang_name = "vlanTrunkPorts"
            self.yang_parent_name = "CISCO-VTP-MIB"

            self.vlantrunkportsdot1qtag = YLeaf(YType.boolean, "vlanTrunkPortsDot1qTag")

            self.vlantrunkportsetserialno = YLeaf(YType.int32, "vlanTrunkPortSetSerialNo")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("vlantrunkportsdot1qtag",
                            "vlantrunkportsetserialno") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoVtpMib.Vlantrunkports, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVtpMib.Vlantrunkports, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.vlantrunkportsdot1qtag.is_set or
                self.vlantrunkportsetserialno.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.vlantrunkportsdot1qtag.yfilter != YFilter.not_set or
                self.vlantrunkportsetserialno.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vlanTrunkPorts" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.vlantrunkportsdot1qtag.is_set or self.vlantrunkportsdot1qtag.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vlantrunkportsdot1qtag.get_name_leafdata())
            if (self.vlantrunkportsetserialno.is_set or self.vlantrunkportsetserialno.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vlantrunkportsetserialno.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vlanTrunkPortsDot1qTag" or name == "vlanTrunkPortSetSerialNo"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "vlanTrunkPortsDot1qTag"):
                self.vlantrunkportsdot1qtag = value
                self.vlantrunkportsdot1qtag.value_namespace = name_space
                self.vlantrunkportsdot1qtag.value_namespace_prefix = name_space_prefix
            if(value_path == "vlanTrunkPortSetSerialNo"):
                self.vlantrunkportsetserialno = value
                self.vlantrunkportsetserialno.value_namespace = name_space
                self.vlantrunkportsetserialno.value_namespace_prefix = name_space_prefix


    class Vlanstatistics(Entity):
        """
        
        
        .. attribute:: vlanstatsextendedvlans
        
        	This object indicates the number of the existing manageable VLANs with VLAN indices greater than 1024 in the system
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: vlanstatsfreevlans
        
        	This object indicates the number of the free or unused VLANs in the system
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: vlanstatsinternalvlans
        
        	This object indicates the number of the internal VLANs existing in the system
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: vlanstatsvlans
        
        	This object indicates the number of the existing manageable VLANs with VLAN indices from 1 to 1024 in the system
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CiscoVtpMib.Vlanstatistics, self).__init__()

            self.yang_name = "vlanStatistics"
            self.yang_parent_name = "CISCO-VTP-MIB"

            self.vlanstatsextendedvlans = YLeaf(YType.uint32, "vlanStatsExtendedVlans")

            self.vlanstatsfreevlans = YLeaf(YType.uint32, "vlanStatsFreeVlans")

            self.vlanstatsinternalvlans = YLeaf(YType.uint32, "vlanStatsInternalVlans")

            self.vlanstatsvlans = YLeaf(YType.uint32, "vlanStatsVlans")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("vlanstatsextendedvlans",
                            "vlanstatsfreevlans",
                            "vlanstatsinternalvlans",
                            "vlanstatsvlans") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoVtpMib.Vlanstatistics, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVtpMib.Vlanstatistics, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.vlanstatsextendedvlans.is_set or
                self.vlanstatsfreevlans.is_set or
                self.vlanstatsinternalvlans.is_set or
                self.vlanstatsvlans.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.vlanstatsextendedvlans.yfilter != YFilter.not_set or
                self.vlanstatsfreevlans.yfilter != YFilter.not_set or
                self.vlanstatsinternalvlans.yfilter != YFilter.not_set or
                self.vlanstatsvlans.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vlanStatistics" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.vlanstatsextendedvlans.is_set or self.vlanstatsextendedvlans.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vlanstatsextendedvlans.get_name_leafdata())
            if (self.vlanstatsfreevlans.is_set or self.vlanstatsfreevlans.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vlanstatsfreevlans.get_name_leafdata())
            if (self.vlanstatsinternalvlans.is_set or self.vlanstatsinternalvlans.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vlanstatsinternalvlans.get_name_leafdata())
            if (self.vlanstatsvlans.is_set or self.vlanstatsvlans.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vlanstatsvlans.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vlanStatsExtendedVlans" or name == "vlanStatsFreeVlans" or name == "vlanStatsInternalVlans" or name == "vlanStatsVlans"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "vlanStatsExtendedVlans"):
                self.vlanstatsextendedvlans = value
                self.vlanstatsextendedvlans.value_namespace = name_space
                self.vlanstatsextendedvlans.value_namespace_prefix = name_space_prefix
            if(value_path == "vlanStatsFreeVlans"):
                self.vlanstatsfreevlans = value
                self.vlanstatsfreevlans.value_namespace = name_space
                self.vlanstatsfreevlans.value_namespace_prefix = name_space_prefix
            if(value_path == "vlanStatsInternalVlans"):
                self.vlanstatsinternalvlans = value
                self.vlanstatsinternalvlans.value_namespace = name_space
                self.vlanstatsinternalvlans.value_namespace_prefix = name_space_prefix
            if(value_path == "vlanStatsVlans"):
                self.vlanstatsvlans = value
                self.vlanstatsvlans.value_namespace = name_space
                self.vlanstatsvlans.value_namespace_prefix = name_space_prefix


    class Managementdomaintable(Entity):
        """
        The table containing information on the management domains
        in which the local system is participating.  Devices which
        support only one management domain will support just one row
        in this table, and will not let it be deleted nor let other
        rows be created.  Devices which support multiple management
        domains will allow rows to be created and deleted, but will
        not allow the last row to be deleted. If the device does 
        not support VTP, the table is read\-only.
        
        .. attribute:: managementdomainentry
        
        	Information about the status of one management domain
        	**type**\: list of    :py:class:`Managementdomainentry <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Managementdomaintable.Managementdomainentry>`
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CiscoVtpMib.Managementdomaintable, self).__init__()

            self.yang_name = "managementDomainTable"
            self.yang_parent_name = "CISCO-VTP-MIB"

            self.managementdomainentry = YList(self)

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
                        super(CiscoVtpMib.Managementdomaintable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVtpMib.Managementdomaintable, self).__setattr__(name, value)


        class Managementdomainentry(Entity):
            """
            Information about the status of one management domain.
            
            .. attribute:: managementdomainindex  <key>
            
            	An arbitrary value to uniquely identify the management domain on the local system
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: managementdomainadminsrcif
            
            	The object specifies the interface to be used as the preferred source interface for the VTP IP updater address.  A zero length value indicates that a source interface is not specified
            	**type**\:  str
            
            .. attribute:: managementdomainconfigfile
            
            	The object specifies the file name where VTP configuration is stored in the format of <filename> or <devices>\:[<filename>].  <device> can be (but not limited to)\: flash, bootflash, slot0, slot1, disk0
            	**type**\:  str
            
            .. attribute:: managementdomainconfigrevnumber
            
            	The current Configuration Revision Number as known by the local device for this management domain when  managementDomainVersionInUse is version1(1) or  version2(2).  If managementDomainVersionInUse is version3(4), this  object has the same value with vtpDatabaseRevisionNumber  of VLAN database type.  This value is updated (if necessary) whenever a VTP advertisement is received or generated. When in the 'no management\-domain' state, this value is 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: managementdomaindeviceid
            
            	The object indicates a value that uniquely identifies this device within a VTP Domain.  The value of this object is zero length string if managementDomainVersionInUse is not 'version3'
            	**type**\:  str
            
            .. attribute:: managementdomainlastchange
            
            	The time at which the Configuration Revision Number was (last) increased to its current value, as indicated in the most recently received VTP advertisement for this management domain when managementDomainVersionInUse is not version3(4) or in the most recently received VTP VLAN database  advertisement for this management domain when  managementDomainVersionInUse is version3(4).  The value 0x0000010100000000 indicates that the device which last increased the Configuration Revision Number had no idea of the date/time, or that no advertisement has been received
            	**type**\:  str
            
            .. attribute:: managementdomainlastupdater
            
            	The IP\-address (or one of them) of the VTP Server which last updated the Configuration Revision Number, as indicated in the most recently received VTP advertisement for this management domain, when managementDomainVersionInUse is version1(1) or version2(2).   If managementDomainVersionInUse is version3(4), this object has the value of 0.0.0.0.  Before an advertisement has been received, this value is 0.0.0.0
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: managementdomainlocalmode
            
            	The local VTP mode in this management domain when managementDomainVersionInUse is version1(1) or version2(2).  If managementDomainVersionInUse is version3(4), this  object has the same value with vtpDatabaseLocalMode  of VLAN database type.  \- 'client' indicates that the local system is acting   as a VTP client.  \- 'server' indicates that the local system is acting   as a VTP server.  \- 'transparent' indicates that the local system does   not generate or listen to VTP messages, but forwards   messages. This mode can also be set by the device   itself when the amount of VLAN information is too   large for it to hold in DRAM.  \- 'off' indicates that the local system does not   generate, listen to or forward any VTP messages
            	**type**\:   :py:class:`Managementdomainlocalmode <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Managementdomaintable.Managementdomainentry.Managementdomainlocalmode>`
            
            .. attribute:: managementdomainlocalupdater
            
            	The object indicates the Internet address of the preferred source interface for the VTP IP updater
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: managementdomainlocalupdatertype
            
            	The object indicates the type of the Internet address of the preferred source interface for the VTP IP updater.  The value of this object is 'unknown' if managementDomainVersionInUse is 'version3' or managementDomainLocalMode is not 'server'
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: managementdomainname
            
            	The management name of a domain in which the local system is participating.  The zero\-length name corresponds to the 'no management\-domain' state which is the initial value at installation\-time if not configured otherwise.  Note that the zero\-length name does not correspond to an operational management domain, and a device does not send VTP advertisements while in the 'no management\-domain' state.  A device leaves the 'no management\-domain' state when it obtains a management\-domain name, either through configuration or through inheriting the management\-domain name from a received VTP advertisement.  When the value of an existing instance of this object is modified by network management, the local system should re\- initialize its VLAN information (for the given management domain) as if it had just been configured with a management domain name at installation time
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: managementdomainopersrcif
            
            	The object indicates the interface used as the preferred source interface for the VTP IP updater address.  A zero length string indicates that a source interface is not available
            	**type**\:  str
            
            .. attribute:: managementdomainpruningstate
            
            	An indication of whether VTP pruning is enabled or disabled in this managament domain.   This object can only be modified, either when the  corresponding instance value of managementDomainVersionInUse  is 'version1' or 'version2' and the corresponding instance  value of managementDomainLocalMode is 'server', or when the  corresponding instance value of managementDomainVersionInUse  is 'version3' and the corresponding instance value of  managementDomainLocalMode is 'server' or 'client'
            	**type**\:   :py:class:`Managementdomainpruningstate <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Managementdomaintable.Managementdomainentry.Managementdomainpruningstate>`
            
            .. attribute:: managementdomainpruningstateoper
            
            	Indicates whether VTP pruning is operationally enabled or disabled in this managament domain
            	**type**\:   :py:class:`Managementdomainpruningstateoper <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Managementdomaintable.Managementdomainentry.Managementdomainpruningstateoper>`
            
            .. attribute:: managementdomainrowstatus
            
            	The status of this conceptual row
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: managementdomainsourceonlymode
            
            	The object specifies whether to use only the IP address of managementDomainAdminSrcIf as the VTP IP updater address.   'true' indicates to only use the IP address of         managementDomainAdminSrcIf as the VTP IP         updater address.   'false' indicates to use the IP address of          managementDomainAdminSrcIf as the VTP IP          updater address if managementDomainAdminSrcIf          is configured with an IP address.  Otherwise, the          first available IP address of the system will         be used
            	**type**\:  bool
            
            .. attribute:: managementdomaintftppathname
            
            	The complete pathname of the file at the TFTP Server identified by the value of managementDomainTftpServer in/from which VTP VLAN information for this management domain is to be stored/retrieved.  If the value of corresponding instance of managementDomainTftpServer is 0.0.0.0, the value of this object is ignored
            	**type**\:  str
            
            .. attribute:: managementdomaintftpserver
            
            	The IP address of a TFTP Server in/from which VTP VLAN information for this management domain is to be stored/retrieved.  If the information is being locally stored in NVRAM, this object should take the value 0.0.0.0
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: managementdomainversioninuse
            
            	The current version of the VTP that is in use by the designated management domain.   This object can be set to none(3) only when  vtpVersion is none(3)
            	**type**\:   :py:class:`Managementdomainversioninuse <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Managementdomaintable.Managementdomainentry.Managementdomainversioninuse>`
            
            .. attribute:: vtpconfigdigesterrors
            
            	The number of occurrences of configuration digest errors for this management domain.  A configuration digest error occurs when a device receives a VTP advertisement for which\:  \- the advertisement's Configuration Revision Number is   greater than the current locally\-held value, and  \-  the advertisement's digest value computed by the  receiving device does not match the checksum in the  summary advertisement that was received earlier. This  can happen, for example, if there is a mismatch in VTP  passwords between the VTP devices
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpconfigrevnumbererrors
            
            	The number of occurrences of configuration revision number errors for this management domain.  A configuration revision number error occurs when a device receives a VTP advertisement for which\:  \- the advertisement's Configuration Revision Number is the   same as the current locally\-held value, and  \- the advertisement's digest value is different from the   current locally\-held value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpinadvertrequests
            
            	The total number of VTP Advert Requests received for this management domain
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpinsubsetadverts
            
            	The total number of VTP Subset Adverts received for this management domain
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpinsummaryadverts
            
            	The total number of VTP Summary Adverts received for this management domain
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpoutadvertrequests
            
            	The total number of VTP Advert Requests sent for this management domain
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpoutsubsetadverts
            
            	The total number of VTP Subset Adverts sent for this management domain
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpoutsummaryadverts
            
            	The total number of VTP Summary Adverts sent for this management domain
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpvlanapplystatus
            
            	The current status of an 'apply' operation to instanciate the Edit Buffer as the new global VLAN information (for this management domain).  If no apply is currently active, the status represented is that of the most recently completed apply.  The possible values are\:     inProgress \- 'apply' operation in progress;     succeeded \- the 'apply' was successful (this value is           also used when no apply has been invoked since the           last time the local system restarted);     configNumberError \- the apply failed because the value of           vtpVlanEditConfigRevNumber was less or equal to           the value of current value of            managementDomainConfigRevNumber;     inconsistentEdit \- the apply failed because the modified           information was not self\-consistent;     tooBig \- the apply failed because the modified           information was too large to fit in this VTP           Server's non\-volatile storage location;     localNVStoreFail \- the apply failed in trying to store           the new information in a local non\-volatile           storage location;     remoteNVStoreFail \- the apply failed in trying to store           the new information in a remote non\-volatile           storage location;     editBufferEmpty \- the apply failed because the Edit           Buffer was empty (for this management domain).     someOtherError \- the apply failed for some other reason           (e.g., insufficient memory).     notPrimaryServer \- the apply failed because the local            device is not a VTP primary server for VLAN            database type when managementDomainVersionInUse           is version3(4)
            	**type**\:   :py:class:`Vtpvlanapplystatus <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Managementdomaintable.Managementdomainentry.Vtpvlanapplystatus>`
            
            .. attribute:: vtpvlaneditbufferowner
            
            	The management station which is currently using the Edit Buffer for this management domain.  When the Edit Buffer for a management domain is not currently in use, the value of this object is the zero\-length string.  Note that it is also the zero\-length string if a manager fails to set this object when invoking a copy operation
            	**type**\:  str
            
            	**length:** 0..127
            
            .. attribute:: vtpvlaneditconfigrevnumber
            
            	The Configuration Revision Number to be used for the next apply operation.  This value is initialized (by the agent) on a copy operation to be one greater than the value of managementDomainConfigRevNumber. On an apply, if the  number is less or equal to the value of  managementDomainConfigRevNumber, then the apply fails. The value can be modified (increased) by network management before an apply to ensure that an apply does not fail for  this reason.  This object is used to allow management control over whether a configuration revision received via a VTP advertisement after a copy operation but before the succeeding apply operation is lost by being overwritten by the (local) edit operation.  By default, the apply operation will fail in this situation.  By increasing this object's value after the copy but before the apply, management can control whether the apply is to succeed (with the update via VTP advertisement being lost)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpvlaneditmodifiedvlan
            
            	The VLAN\-id of the modified VLAN in the Edit Buffer. If the object has the value of zero, any VLAN can  be edited. If the value of the object is not zero, only this VLAN can be edited.  The object's value is reset to zero after a successful 'apply' operation or a 'release' operation.   This object is only supported for devices which allow  only one VLAN editing for each 'apply' operation. For devices which allow multiple VLAN editing for each 'apply' operation, this object is not supported
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlaneditoperation
            
            	This object always has the value 'none' when read.  When written, each value causes the appropriate action\:   'copy' \- causes the creation of rows in the vtpVlanEditTable exactly corresponding to the current global VLAN information for this management domain.  If the Edit Buffer (for this management domain) is not currently empty, a copy operation fails.  A successful copy operation starts the deadman\-timer.   'apply' \- first performs a consistent check on the the modified information contained in the Edit Buffer, and if consistent, then tries to instanciate the modified information as the new global VLAN information.  Note that an empty Edit Buffer (for the management domain) would always result in an inconsistency since the default VLANs are required to be present.   'release' \- flushes the Edit Buffer (for this management domain), clears the Owner information, and aborts the deadman\-timer.  A release is generated automatically if the deadman\-timer ever expires.   'restartTimer' \- restarts the deadman\-timer.   'none' \- no operation is performed
            	**type**\:   :py:class:`Vtpvlaneditoperation <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Managementdomaintable.Managementdomainentry.Vtpvlaneditoperation>`
            
            

            """

            _prefix = 'CISCO-VTP-MIB'
            _revision = '2013-10-14'

            def __init__(self):
                super(CiscoVtpMib.Managementdomaintable.Managementdomainentry, self).__init__()

                self.yang_name = "managementDomainEntry"
                self.yang_parent_name = "managementDomainTable"

                self.managementdomainindex = YLeaf(YType.int32, "managementDomainIndex")

                self.managementdomainadminsrcif = YLeaf(YType.str, "managementDomainAdminSrcIf")

                self.managementdomainconfigfile = YLeaf(YType.str, "managementDomainConfigFile")

                self.managementdomainconfigrevnumber = YLeaf(YType.uint32, "managementDomainConfigRevNumber")

                self.managementdomaindeviceid = YLeaf(YType.str, "managementDomainDeviceID")

                self.managementdomainlastchange = YLeaf(YType.str, "managementDomainLastChange")

                self.managementdomainlastupdater = YLeaf(YType.str, "managementDomainLastUpdater")

                self.managementdomainlocalmode = YLeaf(YType.enumeration, "managementDomainLocalMode")

                self.managementdomainlocalupdater = YLeaf(YType.str, "managementDomainLocalUpdater")

                self.managementdomainlocalupdatertype = YLeaf(YType.enumeration, "managementDomainLocalUpdaterType")

                self.managementdomainname = YLeaf(YType.str, "managementDomainName")

                self.managementdomainopersrcif = YLeaf(YType.str, "managementDomainOperSrcIf")

                self.managementdomainpruningstate = YLeaf(YType.enumeration, "managementDomainPruningState")

                self.managementdomainpruningstateoper = YLeaf(YType.enumeration, "managementDomainPruningStateOper")

                self.managementdomainrowstatus = YLeaf(YType.enumeration, "managementDomainRowStatus")

                self.managementdomainsourceonlymode = YLeaf(YType.boolean, "managementDomainSourceOnlyMode")

                self.managementdomaintftppathname = YLeaf(YType.str, "managementDomainTftpPathname")

                self.managementdomaintftpserver = YLeaf(YType.str, "managementDomainTftpServer")

                self.managementdomainversioninuse = YLeaf(YType.enumeration, "managementDomainVersionInUse")

                self.vtpconfigdigesterrors = YLeaf(YType.uint32, "vtpConfigDigestErrors")

                self.vtpconfigrevnumbererrors = YLeaf(YType.uint32, "vtpConfigRevNumberErrors")

                self.vtpinadvertrequests = YLeaf(YType.uint32, "vtpInAdvertRequests")

                self.vtpinsubsetadverts = YLeaf(YType.uint32, "vtpInSubsetAdverts")

                self.vtpinsummaryadverts = YLeaf(YType.uint32, "vtpInSummaryAdverts")

                self.vtpoutadvertrequests = YLeaf(YType.uint32, "vtpOutAdvertRequests")

                self.vtpoutsubsetadverts = YLeaf(YType.uint32, "vtpOutSubsetAdverts")

                self.vtpoutsummaryadverts = YLeaf(YType.uint32, "vtpOutSummaryAdverts")

                self.vtpvlanapplystatus = YLeaf(YType.enumeration, "vtpVlanApplyStatus")

                self.vtpvlaneditbufferowner = YLeaf(YType.str, "vtpVlanEditBufferOwner")

                self.vtpvlaneditconfigrevnumber = YLeaf(YType.uint32, "vtpVlanEditConfigRevNumber")

                self.vtpvlaneditmodifiedvlan = YLeaf(YType.int32, "vtpVlanEditModifiedVlan")

                self.vtpvlaneditoperation = YLeaf(YType.enumeration, "vtpVlanEditOperation")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("managementdomainindex",
                                "managementdomainadminsrcif",
                                "managementdomainconfigfile",
                                "managementdomainconfigrevnumber",
                                "managementdomaindeviceid",
                                "managementdomainlastchange",
                                "managementdomainlastupdater",
                                "managementdomainlocalmode",
                                "managementdomainlocalupdater",
                                "managementdomainlocalupdatertype",
                                "managementdomainname",
                                "managementdomainopersrcif",
                                "managementdomainpruningstate",
                                "managementdomainpruningstateoper",
                                "managementdomainrowstatus",
                                "managementdomainsourceonlymode",
                                "managementdomaintftppathname",
                                "managementdomaintftpserver",
                                "managementdomainversioninuse",
                                "vtpconfigdigesterrors",
                                "vtpconfigrevnumbererrors",
                                "vtpinadvertrequests",
                                "vtpinsubsetadverts",
                                "vtpinsummaryadverts",
                                "vtpoutadvertrequests",
                                "vtpoutsubsetadverts",
                                "vtpoutsummaryadverts",
                                "vtpvlanapplystatus",
                                "vtpvlaneditbufferowner",
                                "vtpvlaneditconfigrevnumber",
                                "vtpvlaneditmodifiedvlan",
                                "vtpvlaneditoperation") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVtpMib.Managementdomaintable.Managementdomainentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVtpMib.Managementdomaintable.Managementdomainentry, self).__setattr__(name, value)

            class Managementdomainlocalmode(Enum):
                """
                Managementdomainlocalmode

                The local VTP mode in this management domain when

                managementDomainVersionInUse is version1(1) or

                version2(2).

                If managementDomainVersionInUse is version3(4), this 

                object has the same value with vtpDatabaseLocalMode 

                of VLAN database type.

                \- 'client' indicates that the local system is acting

                  as a VTP client.

                \- 'server' indicates that the local system is acting

                  as a VTP server.

                \- 'transparent' indicates that the local system does

                  not generate or listen to VTP messages, but forwards

                  messages. This mode can also be set by the device

                  itself when the amount of VLAN information is too

                  large for it to hold in DRAM.

                \- 'off' indicates that the local system does not

                  generate, listen to or forward any VTP messages.

                .. data:: client = 1

                .. data:: server = 2

                .. data:: transparent = 3

                .. data:: off = 4

                """

                client = Enum.YLeaf(1, "client")

                server = Enum.YLeaf(2, "server")

                transparent = Enum.YLeaf(3, "transparent")

                off = Enum.YLeaf(4, "off")


            class Managementdomainpruningstate(Enum):
                """
                Managementdomainpruningstate

                An indication of whether VTP pruning is enabled or disabled

                in this managament domain. 

                This object can only be modified, either when the 

                corresponding instance value of managementDomainVersionInUse 

                is 'version1' or 'version2' and the corresponding instance 

                value of managementDomainLocalMode is 'server', or when the 

                corresponding instance value of managementDomainVersionInUse 

                is 'version3' and the corresponding instance value of 

                managementDomainLocalMode is 'server' or 'client'.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = Enum.YLeaf(1, "enabled")

                disabled = Enum.YLeaf(2, "disabled")


            class Managementdomainpruningstateoper(Enum):
                """
                Managementdomainpruningstateoper

                Indicates whether VTP pruning is operationally enabled or

                disabled in this managament domain.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = Enum.YLeaf(1, "enabled")

                disabled = Enum.YLeaf(2, "disabled")


            class Managementdomainversioninuse(Enum):
                """
                Managementdomainversioninuse

                The current version of the VTP that is in use by the

                designated management domain. 

                This object can be set to none(3) only when 

                vtpVersion is none(3).

                .. data:: version1 = 1

                .. data:: version2 = 2

                .. data:: none = 3

                .. data:: version3 = 4

                """

                version1 = Enum.YLeaf(1, "version1")

                version2 = Enum.YLeaf(2, "version2")

                none = Enum.YLeaf(3, "none")

                version3 = Enum.YLeaf(4, "version3")


            class Vtpvlanapplystatus(Enum):
                """
                Vtpvlanapplystatus

                The current status of an 'apply' operation to instanciate

                the Edit Buffer as the new global VLAN information (for this

                management domain).  If no apply is currently active, the

                status represented is that of the most recently completed

                apply.  The possible values are\:

                   inProgress \- 'apply' operation in progress;

                   succeeded \- the 'apply' was successful (this value is

                          also used when no apply has been invoked since the

                          last time the local system restarted);

                   configNumberError \- the apply failed because the value of

                          vtpVlanEditConfigRevNumber was less or equal to

                          the value of current value of 

                          managementDomainConfigRevNumber;

                   inconsistentEdit \- the apply failed because the modified

                          information was not self\-consistent;

                   tooBig \- the apply failed because the modified

                          information was too large to fit in this VTP

                          Server's non\-volatile storage location;

                   localNVStoreFail \- the apply failed in trying to store

                          the new information in a local non\-volatile

                          storage location;

                   remoteNVStoreFail \- the apply failed in trying to store

                          the new information in a remote non\-volatile

                          storage location;

                   editBufferEmpty \- the apply failed because the Edit

                          Buffer was empty (for this management domain).

                   someOtherError \- the apply failed for some other reason

                          (e.g., insufficient memory).

                   notPrimaryServer \- the apply failed because the local 

                          device is not a VTP primary server for VLAN 

                          database type when managementDomainVersionInUse

                          is version3(4).

                .. data:: inProgress = 1

                .. data:: succeeded = 2

                .. data:: configNumberError = 3

                .. data:: inconsistentEdit = 4

                .. data:: tooBig = 5

                .. data:: localNVStoreFail = 6

                .. data:: remoteNVStoreFail = 7

                .. data:: editBufferEmpty = 8

                .. data:: someOtherError = 9

                .. data:: notPrimaryServer = 10

                """

                inProgress = Enum.YLeaf(1, "inProgress")

                succeeded = Enum.YLeaf(2, "succeeded")

                configNumberError = Enum.YLeaf(3, "configNumberError")

                inconsistentEdit = Enum.YLeaf(4, "inconsistentEdit")

                tooBig = Enum.YLeaf(5, "tooBig")

                localNVStoreFail = Enum.YLeaf(6, "localNVStoreFail")

                remoteNVStoreFail = Enum.YLeaf(7, "remoteNVStoreFail")

                editBufferEmpty = Enum.YLeaf(8, "editBufferEmpty")

                someOtherError = Enum.YLeaf(9, "someOtherError")

                notPrimaryServer = Enum.YLeaf(10, "notPrimaryServer")


            class Vtpvlaneditoperation(Enum):
                """
                Vtpvlaneditoperation

                This object always has the value 'none' when read.  When

                written, each value causes the appropriate action\:

                 'copy' \- causes the creation of rows in the

                vtpVlanEditTable exactly corresponding to the current global

                VLAN information for this management domain.  If the Edit

                Buffer (for this management domain) is not currently empty,

                a copy operation fails.  A successful copy operation starts

                the deadman\-timer.

                 'apply' \- first performs a consistent check on the the

                modified information contained in the Edit Buffer, and if

                consistent, then tries to instanciate the modified

                information as the new global VLAN information.  Note that

                an empty Edit Buffer (for the management domain) would

                always result in an inconsistency since the default VLANs

                are required to be present.

                 'release' \- flushes the Edit Buffer (for this management

                domain), clears the Owner information, and aborts the

                deadman\-timer.  A release is generated automatically if the

                deadman\-timer ever expires.

                 'restartTimer' \- restarts the deadman\-timer.

                 'none' \- no operation is performed.

                .. data:: none = 1

                .. data:: copy = 2

                .. data:: apply = 3

                .. data:: release = 4

                .. data:: restartTimer = 5

                """

                none = Enum.YLeaf(1, "none")

                copy = Enum.YLeaf(2, "copy")

                apply = Enum.YLeaf(3, "apply")

                release = Enum.YLeaf(4, "release")

                restartTimer = Enum.YLeaf(5, "restartTimer")


            def has_data(self):
                return (
                    self.managementdomainindex.is_set or
                    self.managementdomainadminsrcif.is_set or
                    self.managementdomainconfigfile.is_set or
                    self.managementdomainconfigrevnumber.is_set or
                    self.managementdomaindeviceid.is_set or
                    self.managementdomainlastchange.is_set or
                    self.managementdomainlastupdater.is_set or
                    self.managementdomainlocalmode.is_set or
                    self.managementdomainlocalupdater.is_set or
                    self.managementdomainlocalupdatertype.is_set or
                    self.managementdomainname.is_set or
                    self.managementdomainopersrcif.is_set or
                    self.managementdomainpruningstate.is_set or
                    self.managementdomainpruningstateoper.is_set or
                    self.managementdomainrowstatus.is_set or
                    self.managementdomainsourceonlymode.is_set or
                    self.managementdomaintftppathname.is_set or
                    self.managementdomaintftpserver.is_set or
                    self.managementdomainversioninuse.is_set or
                    self.vtpconfigdigesterrors.is_set or
                    self.vtpconfigrevnumbererrors.is_set or
                    self.vtpinadvertrequests.is_set or
                    self.vtpinsubsetadverts.is_set or
                    self.vtpinsummaryadverts.is_set or
                    self.vtpoutadvertrequests.is_set or
                    self.vtpoutsubsetadverts.is_set or
                    self.vtpoutsummaryadverts.is_set or
                    self.vtpvlanapplystatus.is_set or
                    self.vtpvlaneditbufferowner.is_set or
                    self.vtpvlaneditconfigrevnumber.is_set or
                    self.vtpvlaneditmodifiedvlan.is_set or
                    self.vtpvlaneditoperation.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.managementdomainindex.yfilter != YFilter.not_set or
                    self.managementdomainadminsrcif.yfilter != YFilter.not_set or
                    self.managementdomainconfigfile.yfilter != YFilter.not_set or
                    self.managementdomainconfigrevnumber.yfilter != YFilter.not_set or
                    self.managementdomaindeviceid.yfilter != YFilter.not_set or
                    self.managementdomainlastchange.yfilter != YFilter.not_set or
                    self.managementdomainlastupdater.yfilter != YFilter.not_set or
                    self.managementdomainlocalmode.yfilter != YFilter.not_set or
                    self.managementdomainlocalupdater.yfilter != YFilter.not_set or
                    self.managementdomainlocalupdatertype.yfilter != YFilter.not_set or
                    self.managementdomainname.yfilter != YFilter.not_set or
                    self.managementdomainopersrcif.yfilter != YFilter.not_set or
                    self.managementdomainpruningstate.yfilter != YFilter.not_set or
                    self.managementdomainpruningstateoper.yfilter != YFilter.not_set or
                    self.managementdomainrowstatus.yfilter != YFilter.not_set or
                    self.managementdomainsourceonlymode.yfilter != YFilter.not_set or
                    self.managementdomaintftppathname.yfilter != YFilter.not_set or
                    self.managementdomaintftpserver.yfilter != YFilter.not_set or
                    self.managementdomainversioninuse.yfilter != YFilter.not_set or
                    self.vtpconfigdigesterrors.yfilter != YFilter.not_set or
                    self.vtpconfigrevnumbererrors.yfilter != YFilter.not_set or
                    self.vtpinadvertrequests.yfilter != YFilter.not_set or
                    self.vtpinsubsetadverts.yfilter != YFilter.not_set or
                    self.vtpinsummaryadverts.yfilter != YFilter.not_set or
                    self.vtpoutadvertrequests.yfilter != YFilter.not_set or
                    self.vtpoutsubsetadverts.yfilter != YFilter.not_set or
                    self.vtpoutsummaryadverts.yfilter != YFilter.not_set or
                    self.vtpvlanapplystatus.yfilter != YFilter.not_set or
                    self.vtpvlaneditbufferowner.yfilter != YFilter.not_set or
                    self.vtpvlaneditconfigrevnumber.yfilter != YFilter.not_set or
                    self.vtpvlaneditmodifiedvlan.yfilter != YFilter.not_set or
                    self.vtpvlaneditoperation.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "managementDomainEntry" + "[managementDomainIndex='" + self.managementdomainindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/managementDomainTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.managementdomainindex.is_set or self.managementdomainindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainindex.get_name_leafdata())
                if (self.managementdomainadminsrcif.is_set or self.managementdomainadminsrcif.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainadminsrcif.get_name_leafdata())
                if (self.managementdomainconfigfile.is_set or self.managementdomainconfigfile.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainconfigfile.get_name_leafdata())
                if (self.managementdomainconfigrevnumber.is_set or self.managementdomainconfigrevnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainconfigrevnumber.get_name_leafdata())
                if (self.managementdomaindeviceid.is_set or self.managementdomaindeviceid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomaindeviceid.get_name_leafdata())
                if (self.managementdomainlastchange.is_set or self.managementdomainlastchange.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainlastchange.get_name_leafdata())
                if (self.managementdomainlastupdater.is_set or self.managementdomainlastupdater.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainlastupdater.get_name_leafdata())
                if (self.managementdomainlocalmode.is_set or self.managementdomainlocalmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainlocalmode.get_name_leafdata())
                if (self.managementdomainlocalupdater.is_set or self.managementdomainlocalupdater.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainlocalupdater.get_name_leafdata())
                if (self.managementdomainlocalupdatertype.is_set or self.managementdomainlocalupdatertype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainlocalupdatertype.get_name_leafdata())
                if (self.managementdomainname.is_set or self.managementdomainname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainname.get_name_leafdata())
                if (self.managementdomainopersrcif.is_set or self.managementdomainopersrcif.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainopersrcif.get_name_leafdata())
                if (self.managementdomainpruningstate.is_set or self.managementdomainpruningstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainpruningstate.get_name_leafdata())
                if (self.managementdomainpruningstateoper.is_set or self.managementdomainpruningstateoper.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainpruningstateoper.get_name_leafdata())
                if (self.managementdomainrowstatus.is_set or self.managementdomainrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainrowstatus.get_name_leafdata())
                if (self.managementdomainsourceonlymode.is_set or self.managementdomainsourceonlymode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainsourceonlymode.get_name_leafdata())
                if (self.managementdomaintftppathname.is_set or self.managementdomaintftppathname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomaintftppathname.get_name_leafdata())
                if (self.managementdomaintftpserver.is_set or self.managementdomaintftpserver.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomaintftpserver.get_name_leafdata())
                if (self.managementdomainversioninuse.is_set or self.managementdomainversioninuse.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainversioninuse.get_name_leafdata())
                if (self.vtpconfigdigesterrors.is_set or self.vtpconfigdigesterrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpconfigdigesterrors.get_name_leafdata())
                if (self.vtpconfigrevnumbererrors.is_set or self.vtpconfigrevnumbererrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpconfigrevnumbererrors.get_name_leafdata())
                if (self.vtpinadvertrequests.is_set or self.vtpinadvertrequests.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpinadvertrequests.get_name_leafdata())
                if (self.vtpinsubsetadverts.is_set or self.vtpinsubsetadverts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpinsubsetadverts.get_name_leafdata())
                if (self.vtpinsummaryadverts.is_set or self.vtpinsummaryadverts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpinsummaryadverts.get_name_leafdata())
                if (self.vtpoutadvertrequests.is_set or self.vtpoutadvertrequests.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpoutadvertrequests.get_name_leafdata())
                if (self.vtpoutsubsetadverts.is_set or self.vtpoutsubsetadverts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpoutsubsetadverts.get_name_leafdata())
                if (self.vtpoutsummaryadverts.is_set or self.vtpoutsummaryadverts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpoutsummaryadverts.get_name_leafdata())
                if (self.vtpvlanapplystatus.is_set or self.vtpvlanapplystatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanapplystatus.get_name_leafdata())
                if (self.vtpvlaneditbufferowner.is_set or self.vtpvlaneditbufferowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlaneditbufferowner.get_name_leafdata())
                if (self.vtpvlaneditconfigrevnumber.is_set or self.vtpvlaneditconfigrevnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlaneditconfigrevnumber.get_name_leafdata())
                if (self.vtpvlaneditmodifiedvlan.is_set or self.vtpvlaneditmodifiedvlan.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlaneditmodifiedvlan.get_name_leafdata())
                if (self.vtpvlaneditoperation.is_set or self.vtpvlaneditoperation.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlaneditoperation.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "managementDomainIndex" or name == "managementDomainAdminSrcIf" or name == "managementDomainConfigFile" or name == "managementDomainConfigRevNumber" or name == "managementDomainDeviceID" or name == "managementDomainLastChange" or name == "managementDomainLastUpdater" or name == "managementDomainLocalMode" or name == "managementDomainLocalUpdater" or name == "managementDomainLocalUpdaterType" or name == "managementDomainName" or name == "managementDomainOperSrcIf" or name == "managementDomainPruningState" or name == "managementDomainPruningStateOper" or name == "managementDomainRowStatus" or name == "managementDomainSourceOnlyMode" or name == "managementDomainTftpPathname" or name == "managementDomainTftpServer" or name == "managementDomainVersionInUse" or name == "vtpConfigDigestErrors" or name == "vtpConfigRevNumberErrors" or name == "vtpInAdvertRequests" or name == "vtpInSubsetAdverts" or name == "vtpInSummaryAdverts" or name == "vtpOutAdvertRequests" or name == "vtpOutSubsetAdverts" or name == "vtpOutSummaryAdverts" or name == "vtpVlanApplyStatus" or name == "vtpVlanEditBufferOwner" or name == "vtpVlanEditConfigRevNumber" or name == "vtpVlanEditModifiedVlan" or name == "vtpVlanEditOperation"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "managementDomainIndex"):
                    self.managementdomainindex = value
                    self.managementdomainindex.value_namespace = name_space
                    self.managementdomainindex.value_namespace_prefix = name_space_prefix
                if(value_path == "managementDomainAdminSrcIf"):
                    self.managementdomainadminsrcif = value
                    self.managementdomainadminsrcif.value_namespace = name_space
                    self.managementdomainadminsrcif.value_namespace_prefix = name_space_prefix
                if(value_path == "managementDomainConfigFile"):
                    self.managementdomainconfigfile = value
                    self.managementdomainconfigfile.value_namespace = name_space
                    self.managementdomainconfigfile.value_namespace_prefix = name_space_prefix
                if(value_path == "managementDomainConfigRevNumber"):
                    self.managementdomainconfigrevnumber = value
                    self.managementdomainconfigrevnumber.value_namespace = name_space
                    self.managementdomainconfigrevnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "managementDomainDeviceID"):
                    self.managementdomaindeviceid = value
                    self.managementdomaindeviceid.value_namespace = name_space
                    self.managementdomaindeviceid.value_namespace_prefix = name_space_prefix
                if(value_path == "managementDomainLastChange"):
                    self.managementdomainlastchange = value
                    self.managementdomainlastchange.value_namespace = name_space
                    self.managementdomainlastchange.value_namespace_prefix = name_space_prefix
                if(value_path == "managementDomainLastUpdater"):
                    self.managementdomainlastupdater = value
                    self.managementdomainlastupdater.value_namespace = name_space
                    self.managementdomainlastupdater.value_namespace_prefix = name_space_prefix
                if(value_path == "managementDomainLocalMode"):
                    self.managementdomainlocalmode = value
                    self.managementdomainlocalmode.value_namespace = name_space
                    self.managementdomainlocalmode.value_namespace_prefix = name_space_prefix
                if(value_path == "managementDomainLocalUpdater"):
                    self.managementdomainlocalupdater = value
                    self.managementdomainlocalupdater.value_namespace = name_space
                    self.managementdomainlocalupdater.value_namespace_prefix = name_space_prefix
                if(value_path == "managementDomainLocalUpdaterType"):
                    self.managementdomainlocalupdatertype = value
                    self.managementdomainlocalupdatertype.value_namespace = name_space
                    self.managementdomainlocalupdatertype.value_namespace_prefix = name_space_prefix
                if(value_path == "managementDomainName"):
                    self.managementdomainname = value
                    self.managementdomainname.value_namespace = name_space
                    self.managementdomainname.value_namespace_prefix = name_space_prefix
                if(value_path == "managementDomainOperSrcIf"):
                    self.managementdomainopersrcif = value
                    self.managementdomainopersrcif.value_namespace = name_space
                    self.managementdomainopersrcif.value_namespace_prefix = name_space_prefix
                if(value_path == "managementDomainPruningState"):
                    self.managementdomainpruningstate = value
                    self.managementdomainpruningstate.value_namespace = name_space
                    self.managementdomainpruningstate.value_namespace_prefix = name_space_prefix
                if(value_path == "managementDomainPruningStateOper"):
                    self.managementdomainpruningstateoper = value
                    self.managementdomainpruningstateoper.value_namespace = name_space
                    self.managementdomainpruningstateoper.value_namespace_prefix = name_space_prefix
                if(value_path == "managementDomainRowStatus"):
                    self.managementdomainrowstatus = value
                    self.managementdomainrowstatus.value_namespace = name_space
                    self.managementdomainrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "managementDomainSourceOnlyMode"):
                    self.managementdomainsourceonlymode = value
                    self.managementdomainsourceonlymode.value_namespace = name_space
                    self.managementdomainsourceonlymode.value_namespace_prefix = name_space_prefix
                if(value_path == "managementDomainTftpPathname"):
                    self.managementdomaintftppathname = value
                    self.managementdomaintftppathname.value_namespace = name_space
                    self.managementdomaintftppathname.value_namespace_prefix = name_space_prefix
                if(value_path == "managementDomainTftpServer"):
                    self.managementdomaintftpserver = value
                    self.managementdomaintftpserver.value_namespace = name_space
                    self.managementdomaintftpserver.value_namespace_prefix = name_space_prefix
                if(value_path == "managementDomainVersionInUse"):
                    self.managementdomainversioninuse = value
                    self.managementdomainversioninuse.value_namespace = name_space
                    self.managementdomainversioninuse.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpConfigDigestErrors"):
                    self.vtpconfigdigesterrors = value
                    self.vtpconfigdigesterrors.value_namespace = name_space
                    self.vtpconfigdigesterrors.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpConfigRevNumberErrors"):
                    self.vtpconfigrevnumbererrors = value
                    self.vtpconfigrevnumbererrors.value_namespace = name_space
                    self.vtpconfigrevnumbererrors.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpInAdvertRequests"):
                    self.vtpinadvertrequests = value
                    self.vtpinadvertrequests.value_namespace = name_space
                    self.vtpinadvertrequests.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpInSubsetAdverts"):
                    self.vtpinsubsetadverts = value
                    self.vtpinsubsetadverts.value_namespace = name_space
                    self.vtpinsubsetadverts.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpInSummaryAdverts"):
                    self.vtpinsummaryadverts = value
                    self.vtpinsummaryadverts.value_namespace = name_space
                    self.vtpinsummaryadverts.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpOutAdvertRequests"):
                    self.vtpoutadvertrequests = value
                    self.vtpoutadvertrequests.value_namespace = name_space
                    self.vtpoutadvertrequests.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpOutSubsetAdverts"):
                    self.vtpoutsubsetadverts = value
                    self.vtpoutsubsetadverts.value_namespace = name_space
                    self.vtpoutsubsetadverts.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpOutSummaryAdverts"):
                    self.vtpoutsummaryadverts = value
                    self.vtpoutsummaryadverts.value_namespace = name_space
                    self.vtpoutsummaryadverts.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanApplyStatus"):
                    self.vtpvlanapplystatus = value
                    self.vtpvlanapplystatus.value_namespace = name_space
                    self.vtpvlanapplystatus.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanEditBufferOwner"):
                    self.vtpvlaneditbufferowner = value
                    self.vtpvlaneditbufferowner.value_namespace = name_space
                    self.vtpvlaneditbufferowner.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanEditConfigRevNumber"):
                    self.vtpvlaneditconfigrevnumber = value
                    self.vtpvlaneditconfigrevnumber.value_namespace = name_space
                    self.vtpvlaneditconfigrevnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanEditModifiedVlan"):
                    self.vtpvlaneditmodifiedvlan = value
                    self.vtpvlaneditmodifiedvlan.value_namespace = name_space
                    self.vtpvlaneditmodifiedvlan.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanEditOperation"):
                    self.vtpvlaneditoperation = value
                    self.vtpvlaneditoperation.value_namespace = name_space
                    self.vtpvlaneditoperation.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.managementdomainentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.managementdomainentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "managementDomainTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "managementDomainEntry"):
                for c in self.managementdomainentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVtpMib.Managementdomaintable.Managementdomainentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.managementdomainentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "managementDomainEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Vtpvlantable(Entity):
        """
        This table contains information on the VLANs which
        currently exist.
        
        .. attribute:: vtpvlanentry
        
        	Information about one current VLAN.  The managementDomainIndex value in the INDEX clause indicates which management domain the VLAN is in
        	**type**\: list of    :py:class:`Vtpvlanentry <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpvlantable.Vtpvlanentry>`
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CiscoVtpMib.Vtpvlantable, self).__init__()

            self.yang_name = "vtpVlanTable"
            self.yang_parent_name = "CISCO-VTP-MIB"

            self.vtpvlanentry = YList(self)

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
                        super(CiscoVtpMib.Vtpvlantable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVtpMib.Vtpvlantable, self).__setattr__(name, value)


        class Vtpvlanentry(Entity):
            """
            Information about one current VLAN.  The
            managementDomainIndex value in the INDEX clause indicates
            which management domain the VLAN is in.
            
            .. attribute:: managementdomainindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..255
            
            	**refers to**\:  :py:class:`managementdomainindex <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Managementdomaintable.Managementdomainentry>`
            
            .. attribute:: vtpvlanindex  <key>
            
            	The VLAN\-id of this VLAN on ISL or 802.1q trunks
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: stpxvlanmistpinstmapinstindex
            
            	The MISTP instance, to which the corresponding vlan is mapped. If this value of this mib object is 0,  the corresponding vlan  is not configured to be mapped to any MISTP instance and all the ports under this VLAN remain in blocking state
            	**type**\:  int
            
            	**range:** 0..256
            
            .. attribute:: vtpvlanarehopcount
            
            	The maximum number of bridge hops allowed in All Routes Explorer frames on this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanType has a value of fddi(2) or tokenRing(3) and Source Routing is in use on this VLAN
            	**type**\:  int
            
            	**range:** 1..13
            
            .. attribute:: vtpvlanbridgenumber
            
            	The bridge number of the VTP\-capable switches for this VLAN.  This object is only instantiated for VLANs that are involved with emulating token ring segments
            	**type**\:  int
            
            	**range:** 0..15
            
            .. attribute:: vtpvlanbridgetype
            
            	The type of the Source Route bridging mode in use on this VLAN.  This object is only instantiated when the value of  the corresponding instance of vtpVlanType has a value of  fddi(2) or tokenRing(3) and Source Routing is in use on this VLAN
            	**type**\:   :py:class:`Vtpvlanbridgetype <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpvlantable.Vtpvlanentry.Vtpvlanbridgetype>`
            
            .. attribute:: vtpvlandot10said
            
            	The value of the 802.10 SAID field for this VLAN
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: vtpvlanifindex
            
            	The value of the ifIndex corresponding to this VLAN ID. If the VLAN ID does not have its corresponding interface,  this object has the value of zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: vtpvlaniscrfbackup
            
            	True if this VLAN is of type trCrf and also is acting as a backup trCrf for the ISL distributed BRF
            	**type**\:  bool
            
            .. attribute:: vtpvlanmtu
            
            	The MTU size on this VLAN, defined as the size of largest MAC\-layer (information field portion of the) data frame which can be transmitted on the VLAN
            	**type**\:  int
            
            	**range:** 1500..18190
            
            .. attribute:: vtpvlanname
            
            	The name of this VLAN.  This name is used as the ELAN\-name for an ATM LAN\-Emulation segment of this VLAN
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: vtpvlanparentvlan
            
            	The parent VLAN for this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanType has a value of 'fddi' or 'tokenRing' and Source Routing is in use on this VLAN.  The parent VLAN must have  a vtpVlanType value of fddiNet(4) or trNet(5),  respectively
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlanringnumber
            
            	The ring number of this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanType has a value of 'fddi' or 'tokenRing' and Source Routing is in use on this VLAN
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlanstate
            
            	The state of this VLAN.  The state 'mtuTooBigForDevice' indicates that this device cannot participate in this VLAN because the VLAN's MTU is larger than the device can support.  The state 'mtuTooBigForTrunk' indicates that while this VLAN's MTU is supported by this device, it is too large for one or more of the device's trunk ports
            	**type**\:   :py:class:`Vtpvlanstate <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpvlantable.Vtpvlanentry.Vtpvlanstate>`
            
            .. attribute:: vtpvlanstehopcount
            
            	The maximum number of bridge hops allowed in Spanning Tree Explorer frames on this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanType has a value of fddi(2) or tokenRing(3) and Source Routing is in use on this VLAN
            	**type**\:  int
            
            	**range:** 1..13
            
            .. attribute:: vtpvlanstptype
            
            	The type of the Spanning Tree Protocol (STP) running on this VLAN.  This object is only instanciated when the value of the corresponding instance of vtpVlanType has a value of 'fddiNet' or 'trNet'.  The value returned by this object depends upon the value of the corresponding instance of vtpVlanEditStpType.  \- 'ieee' indicates IEEE STP is running exclusively.  \- 'ibm' indicates IBM STP is running exclusively.  \- 'hybrid' indicates a STP that allows a combination of   IEEE and IBM is running.  The 'hybrid' STP type results from tokenRing/fddi VLANs that are children of this trNet/fddiNet parent VLAN being configured in a combination of SRT and SRB vtpVlanBridgeTypes while the instance of vtpVlanEditStpType that corresponds to this object is set to 'auto'
            	**type**\:   :py:class:`Vtpvlanstptype <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpvlantable.Vtpvlanentry.Vtpvlanstptype>`
            
            .. attribute:: vtpvlantranslationalvlan1
            
            	A VLAN to which this VLAN is being translational\-bridged. If this value and the corresponding instance of vtpVlanTranslationalVlan2 are both zero, then this VLAN is not being translational\-bridged
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlantranslationalvlan2
            
            	Another VLAN, i.e., other than that indicated by vtpVlanTranslationalVlan1, to which this VLAN is being translational\-bridged.  If this value and the corresponding instance of vtpVlanTranslationalVlan1 are both zero, then this VLAN is not being translational\-bridged
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlantype
            
            	The type of this VLAN
            	**type**\:   :py:class:`Vlantype <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.Vlantype>`
            
            .. attribute:: vtpvlantypeext
            
            	The additional type information of this VLAN
            	**type**\:   :py:class:`Vlantypeext <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.Vlantypeext>`
            
            

            """

            _prefix = 'CISCO-VTP-MIB'
            _revision = '2013-10-14'

            def __init__(self):
                super(CiscoVtpMib.Vtpvlantable.Vtpvlanentry, self).__init__()

                self.yang_name = "vtpVlanEntry"
                self.yang_parent_name = "vtpVlanTable"

                self.managementdomainindex = YLeaf(YType.str, "managementDomainIndex")

                self.vtpvlanindex = YLeaf(YType.int32, "vtpVlanIndex")

                self.stpxvlanmistpinstmapinstindex = YLeaf(YType.int32, "CISCO-STP-EXTENSIONS-MIB:stpxVlanMISTPInstMapInstIndex")

                self.vtpvlanarehopcount = YLeaf(YType.int32, "vtpVlanAreHopCount")

                self.vtpvlanbridgenumber = YLeaf(YType.int32, "vtpVlanBridgeNumber")

                self.vtpvlanbridgetype = YLeaf(YType.enumeration, "vtpVlanBridgeType")

                self.vtpvlandot10said = YLeaf(YType.str, "vtpVlanDot10Said")

                self.vtpvlanifindex = YLeaf(YType.int32, "vtpVlanIfIndex")

                self.vtpvlaniscrfbackup = YLeaf(YType.boolean, "vtpVlanIsCRFBackup")

                self.vtpvlanmtu = YLeaf(YType.int32, "vtpVlanMtu")

                self.vtpvlanname = YLeaf(YType.str, "vtpVlanName")

                self.vtpvlanparentvlan = YLeaf(YType.int32, "vtpVlanParentVlan")

                self.vtpvlanringnumber = YLeaf(YType.int32, "vtpVlanRingNumber")

                self.vtpvlanstate = YLeaf(YType.enumeration, "vtpVlanState")

                self.vtpvlanstehopcount = YLeaf(YType.int32, "vtpVlanSteHopCount")

                self.vtpvlanstptype = YLeaf(YType.enumeration, "vtpVlanStpType")

                self.vtpvlantranslationalvlan1 = YLeaf(YType.int32, "vtpVlanTranslationalVlan1")

                self.vtpvlantranslationalvlan2 = YLeaf(YType.int32, "vtpVlanTranslationalVlan2")

                self.vtpvlantype = YLeaf(YType.enumeration, "vtpVlanType")

                self.vtpvlantypeext = YLeaf(YType.bits, "vtpVlanTypeExt")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("managementdomainindex",
                                "vtpvlanindex",
                                "stpxvlanmistpinstmapinstindex",
                                "vtpvlanarehopcount",
                                "vtpvlanbridgenumber",
                                "vtpvlanbridgetype",
                                "vtpvlandot10said",
                                "vtpvlanifindex",
                                "vtpvlaniscrfbackup",
                                "vtpvlanmtu",
                                "vtpvlanname",
                                "vtpvlanparentvlan",
                                "vtpvlanringnumber",
                                "vtpvlanstate",
                                "vtpvlanstehopcount",
                                "vtpvlanstptype",
                                "vtpvlantranslationalvlan1",
                                "vtpvlantranslationalvlan2",
                                "vtpvlantype",
                                "vtpvlantypeext") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVtpMib.Vtpvlantable.Vtpvlanentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVtpMib.Vtpvlantable.Vtpvlanentry, self).__setattr__(name, value)

            class Vtpvlanbridgetype(Enum):
                """
                Vtpvlanbridgetype

                The type of the Source Route bridging mode in use on this

                VLAN.  This object is only instantiated when the value of 

                the corresponding instance of vtpVlanType has a value of 

                fddi(2) or tokenRing(3) and Source Routing is in use on

                this VLAN.

                .. data:: none = 0

                .. data:: srt = 1

                .. data:: srb = 2

                """

                none = Enum.YLeaf(0, "none")

                srt = Enum.YLeaf(1, "srt")

                srb = Enum.YLeaf(2, "srb")


            class Vtpvlanstate(Enum):
                """
                Vtpvlanstate

                The state of this VLAN.

                The state 'mtuTooBigForDevice' indicates that this device

                cannot participate in this VLAN because the VLAN's MTU is

                larger than the device can support.

                The state 'mtuTooBigForTrunk' indicates that while this

                VLAN's MTU is supported by this device, it is too large for

                one or more of the device's trunk ports.

                .. data:: operational = 1

                .. data:: suspended = 2

                .. data:: mtuTooBigForDevice = 3

                .. data:: mtuTooBigForTrunk = 4

                """

                operational = Enum.YLeaf(1, "operational")

                suspended = Enum.YLeaf(2, "suspended")

                mtuTooBigForDevice = Enum.YLeaf(3, "mtuTooBigForDevice")

                mtuTooBigForTrunk = Enum.YLeaf(4, "mtuTooBigForTrunk")


            class Vtpvlanstptype(Enum):
                """
                Vtpvlanstptype

                The type of the Spanning Tree Protocol (STP) running on

                this VLAN.  This object is only instanciated when the

                value of the corresponding instance of vtpVlanType has a

                value of 'fddiNet' or 'trNet'.

                The value returned by this object depends upon the value

                of the corresponding instance of vtpVlanEditStpType.

                \- 'ieee' indicates IEEE STP is running exclusively.

                \- 'ibm' indicates IBM STP is running exclusively.

                \- 'hybrid' indicates a STP that allows a combination of

                  IEEE and IBM is running.

                The 'hybrid' STP type results from tokenRing/fddi VLANs

                that are children of this trNet/fddiNet parent VLAN being

                configured in a combination of SRT and SRB

                vtpVlanBridgeTypes while the instance of

                vtpVlanEditStpType that corresponds to this object is set

                to 'auto'.

                .. data:: ieee = 1

                .. data:: ibm = 2

                .. data:: hybrid = 3

                """

                ieee = Enum.YLeaf(1, "ieee")

                ibm = Enum.YLeaf(2, "ibm")

                hybrid = Enum.YLeaf(3, "hybrid")


            def has_data(self):
                return (
                    self.managementdomainindex.is_set or
                    self.vtpvlanindex.is_set or
                    self.stpxvlanmistpinstmapinstindex.is_set or
                    self.vtpvlanarehopcount.is_set or
                    self.vtpvlanbridgenumber.is_set or
                    self.vtpvlanbridgetype.is_set or
                    self.vtpvlandot10said.is_set or
                    self.vtpvlanifindex.is_set or
                    self.vtpvlaniscrfbackup.is_set or
                    self.vtpvlanmtu.is_set or
                    self.vtpvlanname.is_set or
                    self.vtpvlanparentvlan.is_set or
                    self.vtpvlanringnumber.is_set or
                    self.vtpvlanstate.is_set or
                    self.vtpvlanstehopcount.is_set or
                    self.vtpvlanstptype.is_set or
                    self.vtpvlantranslationalvlan1.is_set or
                    self.vtpvlantranslationalvlan2.is_set or
                    self.vtpvlantype.is_set or
                    self.vtpvlantypeext.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.managementdomainindex.yfilter != YFilter.not_set or
                    self.vtpvlanindex.yfilter != YFilter.not_set or
                    self.stpxvlanmistpinstmapinstindex.yfilter != YFilter.not_set or
                    self.vtpvlanarehopcount.yfilter != YFilter.not_set or
                    self.vtpvlanbridgenumber.yfilter != YFilter.not_set or
                    self.vtpvlanbridgetype.yfilter != YFilter.not_set or
                    self.vtpvlandot10said.yfilter != YFilter.not_set or
                    self.vtpvlanifindex.yfilter != YFilter.not_set or
                    self.vtpvlaniscrfbackup.yfilter != YFilter.not_set or
                    self.vtpvlanmtu.yfilter != YFilter.not_set or
                    self.vtpvlanname.yfilter != YFilter.not_set or
                    self.vtpvlanparentvlan.yfilter != YFilter.not_set or
                    self.vtpvlanringnumber.yfilter != YFilter.not_set or
                    self.vtpvlanstate.yfilter != YFilter.not_set or
                    self.vtpvlanstehopcount.yfilter != YFilter.not_set or
                    self.vtpvlanstptype.yfilter != YFilter.not_set or
                    self.vtpvlantranslationalvlan1.yfilter != YFilter.not_set or
                    self.vtpvlantranslationalvlan2.yfilter != YFilter.not_set or
                    self.vtpvlantype.yfilter != YFilter.not_set or
                    self.vtpvlantypeext.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vtpVlanEntry" + "[managementDomainIndex='" + self.managementdomainindex.get() + "']" + "[vtpVlanIndex='" + self.vtpvlanindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/vtpVlanTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.managementdomainindex.is_set or self.managementdomainindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainindex.get_name_leafdata())
                if (self.vtpvlanindex.is_set or self.vtpvlanindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanindex.get_name_leafdata())
                if (self.stpxvlanmistpinstmapinstindex.is_set or self.stpxvlanmistpinstmapinstindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxvlanmistpinstmapinstindex.get_name_leafdata())
                if (self.vtpvlanarehopcount.is_set or self.vtpvlanarehopcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanarehopcount.get_name_leafdata())
                if (self.vtpvlanbridgenumber.is_set or self.vtpvlanbridgenumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanbridgenumber.get_name_leafdata())
                if (self.vtpvlanbridgetype.is_set or self.vtpvlanbridgetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanbridgetype.get_name_leafdata())
                if (self.vtpvlandot10said.is_set or self.vtpvlandot10said.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlandot10said.get_name_leafdata())
                if (self.vtpvlanifindex.is_set or self.vtpvlanifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanifindex.get_name_leafdata())
                if (self.vtpvlaniscrfbackup.is_set or self.vtpvlaniscrfbackup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlaniscrfbackup.get_name_leafdata())
                if (self.vtpvlanmtu.is_set or self.vtpvlanmtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanmtu.get_name_leafdata())
                if (self.vtpvlanname.is_set or self.vtpvlanname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanname.get_name_leafdata())
                if (self.vtpvlanparentvlan.is_set or self.vtpvlanparentvlan.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanparentvlan.get_name_leafdata())
                if (self.vtpvlanringnumber.is_set or self.vtpvlanringnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanringnumber.get_name_leafdata())
                if (self.vtpvlanstate.is_set or self.vtpvlanstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanstate.get_name_leafdata())
                if (self.vtpvlanstehopcount.is_set or self.vtpvlanstehopcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanstehopcount.get_name_leafdata())
                if (self.vtpvlanstptype.is_set or self.vtpvlanstptype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanstptype.get_name_leafdata())
                if (self.vtpvlantranslationalvlan1.is_set or self.vtpvlantranslationalvlan1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlantranslationalvlan1.get_name_leafdata())
                if (self.vtpvlantranslationalvlan2.is_set or self.vtpvlantranslationalvlan2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlantranslationalvlan2.get_name_leafdata())
                if (self.vtpvlantype.is_set or self.vtpvlantype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlantype.get_name_leafdata())
                if (self.vtpvlantypeext.is_set or self.vtpvlantypeext.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlantypeext.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "managementDomainIndex" or name == "vtpVlanIndex" or name == "stpxVlanMISTPInstMapInstIndex" or name == "vtpVlanAreHopCount" or name == "vtpVlanBridgeNumber" or name == "vtpVlanBridgeType" or name == "vtpVlanDot10Said" or name == "vtpVlanIfIndex" or name == "vtpVlanIsCRFBackup" or name == "vtpVlanMtu" or name == "vtpVlanName" or name == "vtpVlanParentVlan" or name == "vtpVlanRingNumber" or name == "vtpVlanState" or name == "vtpVlanSteHopCount" or name == "vtpVlanStpType" or name == "vtpVlanTranslationalVlan1" or name == "vtpVlanTranslationalVlan2" or name == "vtpVlanType" or name == "vtpVlanTypeExt"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "managementDomainIndex"):
                    self.managementdomainindex = value
                    self.managementdomainindex.value_namespace = name_space
                    self.managementdomainindex.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanIndex"):
                    self.vtpvlanindex = value
                    self.vtpvlanindex.value_namespace = name_space
                    self.vtpvlanindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxVlanMISTPInstMapInstIndex"):
                    self.stpxvlanmistpinstmapinstindex = value
                    self.stpxvlanmistpinstmapinstindex.value_namespace = name_space
                    self.stpxvlanmistpinstmapinstindex.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanAreHopCount"):
                    self.vtpvlanarehopcount = value
                    self.vtpvlanarehopcount.value_namespace = name_space
                    self.vtpvlanarehopcount.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanBridgeNumber"):
                    self.vtpvlanbridgenumber = value
                    self.vtpvlanbridgenumber.value_namespace = name_space
                    self.vtpvlanbridgenumber.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanBridgeType"):
                    self.vtpvlanbridgetype = value
                    self.vtpvlanbridgetype.value_namespace = name_space
                    self.vtpvlanbridgetype.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanDot10Said"):
                    self.vtpvlandot10said = value
                    self.vtpvlandot10said.value_namespace = name_space
                    self.vtpvlandot10said.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanIfIndex"):
                    self.vtpvlanifindex = value
                    self.vtpvlanifindex.value_namespace = name_space
                    self.vtpvlanifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanIsCRFBackup"):
                    self.vtpvlaniscrfbackup = value
                    self.vtpvlaniscrfbackup.value_namespace = name_space
                    self.vtpvlaniscrfbackup.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanMtu"):
                    self.vtpvlanmtu = value
                    self.vtpvlanmtu.value_namespace = name_space
                    self.vtpvlanmtu.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanName"):
                    self.vtpvlanname = value
                    self.vtpvlanname.value_namespace = name_space
                    self.vtpvlanname.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanParentVlan"):
                    self.vtpvlanparentvlan = value
                    self.vtpvlanparentvlan.value_namespace = name_space
                    self.vtpvlanparentvlan.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanRingNumber"):
                    self.vtpvlanringnumber = value
                    self.vtpvlanringnumber.value_namespace = name_space
                    self.vtpvlanringnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanState"):
                    self.vtpvlanstate = value
                    self.vtpvlanstate.value_namespace = name_space
                    self.vtpvlanstate.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanSteHopCount"):
                    self.vtpvlanstehopcount = value
                    self.vtpvlanstehopcount.value_namespace = name_space
                    self.vtpvlanstehopcount.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanStpType"):
                    self.vtpvlanstptype = value
                    self.vtpvlanstptype.value_namespace = name_space
                    self.vtpvlanstptype.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanTranslationalVlan1"):
                    self.vtpvlantranslationalvlan1 = value
                    self.vtpvlantranslationalvlan1.value_namespace = name_space
                    self.vtpvlantranslationalvlan1.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanTranslationalVlan2"):
                    self.vtpvlantranslationalvlan2 = value
                    self.vtpvlantranslationalvlan2.value_namespace = name_space
                    self.vtpvlantranslationalvlan2.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanType"):
                    self.vtpvlantype = value
                    self.vtpvlantype.value_namespace = name_space
                    self.vtpvlantype.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanTypeExt"):
                    self.vtpvlantypeext[value] = True

        def has_data(self):
            for c in self.vtpvlanentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vtpvlanentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vtpVlanTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vtpVlanEntry"):
                for c in self.vtpvlanentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVtpMib.Vtpvlantable.Vtpvlanentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vtpvlanentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vtpVlanEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Vtpinternalvlantable(Entity):
        """
        A vtpInternalVlanTable entry contains
        information on an existing internal
        VLAN. It is internally created by the
        device for a specific application program 
        and hence owned by the application.  
        It cannot be modified or deleted by (local 
        or network) management.
        
        .. attribute:: vtpinternalvlanentry
        
        	Information about one current internal VLAN
        	**type**\: list of    :py:class:`Vtpinternalvlanentry <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpinternalvlantable.Vtpinternalvlanentry>`
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CiscoVtpMib.Vtpinternalvlantable, self).__init__()

            self.yang_name = "vtpInternalVlanTable"
            self.yang_parent_name = "CISCO-VTP-MIB"

            self.vtpinternalvlanentry = YList(self)

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
                        super(CiscoVtpMib.Vtpinternalvlantable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVtpMib.Vtpinternalvlantable, self).__setattr__(name, value)


        class Vtpinternalvlanentry(Entity):
            """
            Information about one current internal
            VLAN.
            
            .. attribute:: managementdomainindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..255
            
            	**refers to**\:  :py:class:`managementdomainindex <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Managementdomaintable.Managementdomainentry>`
            
            .. attribute:: vtpvlanindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`vtpvlanindex <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpvlantable.Vtpvlanentry>`
            
            .. attribute:: vtpinternalvlanowner
            
            	The program name of the internal VLAN's owner application. This internal VLAN is allocated by the device specifically for this application and no one else could create, modify or delete this  VLAN
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-VTP-MIB'
            _revision = '2013-10-14'

            def __init__(self):
                super(CiscoVtpMib.Vtpinternalvlantable.Vtpinternalvlanentry, self).__init__()

                self.yang_name = "vtpInternalVlanEntry"
                self.yang_parent_name = "vtpInternalVlanTable"

                self.managementdomainindex = YLeaf(YType.str, "managementDomainIndex")

                self.vtpvlanindex = YLeaf(YType.str, "vtpVlanIndex")

                self.vtpinternalvlanowner = YLeaf(YType.str, "vtpInternalVlanOwner")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("managementdomainindex",
                                "vtpvlanindex",
                                "vtpinternalvlanowner") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVtpMib.Vtpinternalvlantable.Vtpinternalvlanentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVtpMib.Vtpinternalvlantable.Vtpinternalvlanentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.managementdomainindex.is_set or
                    self.vtpvlanindex.is_set or
                    self.vtpinternalvlanowner.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.managementdomainindex.yfilter != YFilter.not_set or
                    self.vtpvlanindex.yfilter != YFilter.not_set or
                    self.vtpinternalvlanowner.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vtpInternalVlanEntry" + "[managementDomainIndex='" + self.managementdomainindex.get() + "']" + "[vtpVlanIndex='" + self.vtpvlanindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/vtpInternalVlanTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.managementdomainindex.is_set or self.managementdomainindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainindex.get_name_leafdata())
                if (self.vtpvlanindex.is_set or self.vtpvlanindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanindex.get_name_leafdata())
                if (self.vtpinternalvlanowner.is_set or self.vtpinternalvlanowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpinternalvlanowner.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "managementDomainIndex" or name == "vtpVlanIndex" or name == "vtpInternalVlanOwner"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "managementDomainIndex"):
                    self.managementdomainindex = value
                    self.managementdomainindex.value_namespace = name_space
                    self.managementdomainindex.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanIndex"):
                    self.vtpvlanindex = value
                    self.vtpvlanindex.value_namespace = name_space
                    self.vtpvlanindex.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpInternalVlanOwner"):
                    self.vtpinternalvlanowner = value
                    self.vtpinternalvlanowner.value_namespace = name_space
                    self.vtpinternalvlanowner.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vtpinternalvlanentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vtpinternalvlanentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vtpInternalVlanTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vtpInternalVlanEntry"):
                for c in self.vtpinternalvlanentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVtpMib.Vtpinternalvlantable.Vtpinternalvlanentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vtpinternalvlanentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vtpInternalVlanEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Vtpvlanedittable(Entity):
        """
        The table which contains the information in the Edit
        Buffers, one Edit Buffer per management domain.  The
        information for a particular management domain is
        initialized, by a 'copy' operation, to be the current global
        VLAN information for that management domain.  After
        initialization, editing can be performed to add VLANs,
        delete VLANs, or modify their global parameters.  The
        information as modified through editing is local to this
        Edit Buffer.  An apply operation using the
        vtpVlanEditOperation object is necessary to instanciate the
        modified information as the new global VLAN information for
        that management domain.
        
        To use the Edit Buffer, a manager acts as follows\:
        
        1. ensures the Edit Buffer for a management domain is empty,
        i.e., there are no rows in this table for this management
        domain.
        
        2. issues a SNMP set operation which sets
        vtpVlanEditOperation to 'copy', and vtpVlanEditBufferOwner
        to its own identifier (e.g., its own IP address).
        
        3. if this set operation is successful, proceeds to edit the
        information in the vtpVlanEditTable.
        
        4. if and when the edited information is to be instantiated,
        issues a SNMP set operation which sets vtpVlanEditOperation
        to 'apply'.
        
        5. issues retrieval requests to obtain the value of
        vtpVlanApplyStatus, until the result of the apply is
        determined.
        
        6. releases the Edit Buffer by issuing a SNMP set operation
        which sets vtpVlanEditOperation to 'release'.
        
        Note that the information contained in this table is not
        saved across agent reboots.
        
        .. attribute:: vtpvlaneditentry
        
        	Information about one VLAN in the Edit Buffer for a particular management domain
        	**type**\: list of    :py:class:`Vtpvlaneditentry <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpvlanedittable.Vtpvlaneditentry>`
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CiscoVtpMib.Vtpvlanedittable, self).__init__()

            self.yang_name = "vtpVlanEditTable"
            self.yang_parent_name = "CISCO-VTP-MIB"

            self.vtpvlaneditentry = YList(self)

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
                        super(CiscoVtpMib.Vtpvlanedittable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVtpMib.Vtpvlanedittable, self).__setattr__(name, value)


        class Vtpvlaneditentry(Entity):
            """
            Information about one VLAN in the Edit Buffer for a
            particular management domain.
            
            .. attribute:: managementdomainindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..255
            
            	**refers to**\:  :py:class:`managementdomainindex <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Managementdomaintable.Managementdomainentry>`
            
            .. attribute:: vtpvlaneditindex  <key>
            
            	The VLAN\-id which this VLAN would have on ISL or 802.1q trunks
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: stpxvlanmistpinstmapeditinstindex
            
            	The MISTP instance, to which the corresponding vlan would be  mapped. The value of this mib object is from 0 to the value of stpxMISTPInstanceNumber. If setting the value of this object to 0, the corresponding vlan will not be mapped to a MISTP  instance and all the ports under this VLAN will be moved into the blocking state
            	**type**\:  int
            
            	**range:** 0..256
            
            .. attribute:: vtpvlaneditarehopcount
            
            	The maximum number of bridge hops allowed in All Routes Explorer frames on this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanType has a value of fddi(2) or tokenRing(3) and Source Routing is in use on this VLAN
            	**type**\:  int
            
            	**range:** 1..13
            
            .. attribute:: vtpvlaneditbridgenumber
            
            	The bridge number of the VTP\-capable switches which would be used for this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanEditType has a value of fddiNet(4) or trNet(5)
            	**type**\:  int
            
            	**range:** 0..15
            
            .. attribute:: vtpvlaneditbridgetype
            
            	The type of Source Route bridging mode which would be in use on this VLAN.  This object is only instantiated when  the value of  the corresponding instance of vtpVlanEditType has a value of fddi(2) or tokenRing(3) and Source Routing  is in use on this VLAN
            	**type**\:   :py:class:`Vtpvlaneditbridgetype <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpvlanedittable.Vtpvlaneditentry.Vtpvlaneditbridgetype>`
            
            .. attribute:: vtpvlaneditdot10said
            
            	The value of the 802.10 SAID field which would be used for this VLAN.  An implementation may restrict access to this object
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: vtpvlaneditiscrfbackup
            
            	True if this VLAN is of type trCrf and also is acting as a backup trCrf for the ISL distributed BRF.  This object is only instantiated when the value of the corresponding instance of vtpVlanEditType has a value of tokenRing(3)
            	**type**\:  bool
            
            .. attribute:: vtpvlaneditmtu
            
            	The MTU size which this VLAN would have, defined as the size of largest MAC\-layer (information field portion of the) data frame which can be transmitted on the VLAN.  An implementation may restrict access to this object
            	**type**\:  int
            
            	**range:** 1500..18190
            
            .. attribute:: vtpvlaneditname
            
            	The name which this VLAN would have.  This name would be used as the ELAN\-name for an ATM LAN\-Emulation segment of this VLAN.  An implementation may restrict access to this object
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: vtpvlaneditparentvlan
            
            	The VLAN index of the VLAN which would be the parent for this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanEditType has a value of 'fddi' or 'tokenRing' and Source Routing is in use on this VLAN.  The parent VLAN must have a vtpVlanEditType  value of fddiNet(4) or trNet(5), respectively
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlaneditringnumber
            
            	The ring number which would be used for this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanEditType has a value of 'fddi' or 'tokenRing' and Source Routing is in use on  this VLAN
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlaneditrowstatus
            
            	The status of this row.  Any and all columnar objects in an existing row can be modified irrespective of the status of the row.  A row is not qualified for activation until instances of at least its vtpVlanEditType, vtpVlanEditName and vtpVlanEditDot10Said columns have appropriate values.  The management station should endeavor to make all rows consistent in the table before 'apply'ing the buffer.  An inconsistent entry in the table will cause the entire buffer to be rejected with the vtpVlanApplyStatus object set to the appropriate error value
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: vtpvlaneditstate
            
            	The state which this VLAN would have
            	**type**\:   :py:class:`Vtpvlaneditstate <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpvlanedittable.Vtpvlaneditentry.Vtpvlaneditstate>`
            
            .. attribute:: vtpvlaneditstehopcount
            
            	The maximum number of bridge hops allowed in Spanning Tree Explorer frames on this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanType has a value of fddi(2) or tokenRing(3) and Source Routing is in use on this VLAN
            	**type**\:  int
            
            	**range:** 1..13
            
            .. attribute:: vtpvlaneditstptype
            
            	The type of the Spanning Tree Protocol which would be running on this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanEditType has a value of fddiNet(4) or trNet(5).  If 'ieee' is selected, the STP that runs will be IEEE.  If 'ibm' is selected, the STP that runs will be IBM.  If 'auto' is selected, the STP that runs will be dependant on the values of vtpVlanEditBridgeType for all children tokenRing/fddi type VLANs.  This will result in a 'hybrid' STP (see vtpVlanStpType)
            	**type**\:   :py:class:`Vtpvlaneditstptype <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpvlanedittable.Vtpvlaneditentry.Vtpvlaneditstptype>`
            
            .. attribute:: vtpvlanedittranslationalvlan1
            
            	A VLAN to which this VLAN would be translational\-bridged. If this value and the corresponding instance of vtpVlanTranslationalVlan2 are both zero, then this VLAN would not be translational\-bridged.  An implementation may restrict access to this object
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlanedittranslationalvlan2
            
            	Another VLAN, i.e., other than that indicated by vtpVlanEditTranslationalVlan1, to which this VLAN would be translational\-bridged.  If this value and the corresponding instance of vtpVlanTranslationalVlan1 are both zero, then this VLAN would not be translational\-bridged.  An implementation may restrict access to this object
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlanedittype
            
            	The type which this VLAN would have. An implementation may restrict access to this object
            	**type**\:   :py:class:`Vlantype <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.Vlantype>`
            
            .. attribute:: vtpvlanedittypeext
            
            	The additional type information of this VLAN. vtpVlanEditTypeExt object is superseded by vtpVlanEditTypeExt2
            	**type**\:   :py:class:`Vlantypeext <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.Vlantypeext>`
            
            	**status**\: deprecated
            
            .. attribute:: vtpvlanedittypeext2
            
            	The additional type information of this VLAN. The VlanTypeExt TC specifies which bits may be written by a management application. The agent should provide a default value
            	**type**\:   :py:class:`Vlantypeext <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.Vlantypeext>`
            
            

            """

            _prefix = 'CISCO-VTP-MIB'
            _revision = '2013-10-14'

            def __init__(self):
                super(CiscoVtpMib.Vtpvlanedittable.Vtpvlaneditentry, self).__init__()

                self.yang_name = "vtpVlanEditEntry"
                self.yang_parent_name = "vtpVlanEditTable"

                self.managementdomainindex = YLeaf(YType.str, "managementDomainIndex")

                self.vtpvlaneditindex = YLeaf(YType.int32, "vtpVlanEditIndex")

                self.stpxvlanmistpinstmapeditinstindex = YLeaf(YType.int32, "CISCO-STP-EXTENSIONS-MIB:stpxVlanMISTPInstMapEditInstIndex")

                self.vtpvlaneditarehopcount = YLeaf(YType.int32, "vtpVlanEditAreHopCount")

                self.vtpvlaneditbridgenumber = YLeaf(YType.int32, "vtpVlanEditBridgeNumber")

                self.vtpvlaneditbridgetype = YLeaf(YType.enumeration, "vtpVlanEditBridgeType")

                self.vtpvlaneditdot10said = YLeaf(YType.str, "vtpVlanEditDot10Said")

                self.vtpvlaneditiscrfbackup = YLeaf(YType.boolean, "vtpVlanEditIsCRFBackup")

                self.vtpvlaneditmtu = YLeaf(YType.int32, "vtpVlanEditMtu")

                self.vtpvlaneditname = YLeaf(YType.str, "vtpVlanEditName")

                self.vtpvlaneditparentvlan = YLeaf(YType.int32, "vtpVlanEditParentVlan")

                self.vtpvlaneditringnumber = YLeaf(YType.int32, "vtpVlanEditRingNumber")

                self.vtpvlaneditrowstatus = YLeaf(YType.enumeration, "vtpVlanEditRowStatus")

                self.vtpvlaneditstate = YLeaf(YType.enumeration, "vtpVlanEditState")

                self.vtpvlaneditstehopcount = YLeaf(YType.int32, "vtpVlanEditSteHopCount")

                self.vtpvlaneditstptype = YLeaf(YType.enumeration, "vtpVlanEditStpType")

                self.vtpvlanedittranslationalvlan1 = YLeaf(YType.int32, "vtpVlanEditTranslationalVlan1")

                self.vtpvlanedittranslationalvlan2 = YLeaf(YType.int32, "vtpVlanEditTranslationalVlan2")

                self.vtpvlanedittype = YLeaf(YType.enumeration, "vtpVlanEditType")

                self.vtpvlanedittypeext = YLeaf(YType.bits, "vtpVlanEditTypeExt")

                self.vtpvlanedittypeext2 = YLeaf(YType.bits, "vtpVlanEditTypeExt2")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("managementdomainindex",
                                "vtpvlaneditindex",
                                "stpxvlanmistpinstmapeditinstindex",
                                "vtpvlaneditarehopcount",
                                "vtpvlaneditbridgenumber",
                                "vtpvlaneditbridgetype",
                                "vtpvlaneditdot10said",
                                "vtpvlaneditiscrfbackup",
                                "vtpvlaneditmtu",
                                "vtpvlaneditname",
                                "vtpvlaneditparentvlan",
                                "vtpvlaneditringnumber",
                                "vtpvlaneditrowstatus",
                                "vtpvlaneditstate",
                                "vtpvlaneditstehopcount",
                                "vtpvlaneditstptype",
                                "vtpvlanedittranslationalvlan1",
                                "vtpvlanedittranslationalvlan2",
                                "vtpvlanedittype",
                                "vtpvlanedittypeext",
                                "vtpvlanedittypeext2") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVtpMib.Vtpvlanedittable.Vtpvlaneditentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVtpMib.Vtpvlanedittable.Vtpvlaneditentry, self).__setattr__(name, value)

            class Vtpvlaneditbridgetype(Enum):
                """
                Vtpvlaneditbridgetype

                The type of Source Route bridging mode which would be in

                use on this VLAN.  This object is only instantiated when 

                the value of  the corresponding instance of vtpVlanEditType

                has a value of fddi(2) or tokenRing(3) and Source Routing 

                is in use on this VLAN.

                .. data:: srt = 1

                .. data:: srb = 2

                """

                srt = Enum.YLeaf(1, "srt")

                srb = Enum.YLeaf(2, "srb")


            class Vtpvlaneditstate(Enum):
                """
                Vtpvlaneditstate

                The state which this VLAN would have.

                .. data:: operational = 1

                .. data:: suspended = 2

                """

                operational = Enum.YLeaf(1, "operational")

                suspended = Enum.YLeaf(2, "suspended")


            class Vtpvlaneditstptype(Enum):
                """
                Vtpvlaneditstptype

                The type of the Spanning Tree Protocol which would be

                running on this VLAN.  This object is only instantiated

                when the value of the corresponding instance of

                vtpVlanEditType has a value of fddiNet(4) or trNet(5).

                If 'ieee' is selected, the STP that runs will be IEEE.

                If 'ibm' is selected, the STP that runs will be IBM.

                If 'auto' is selected, the STP that runs will be

                dependant on the values of vtpVlanEditBridgeType for all

                children tokenRing/fddi type VLANs.  This will result in

                a 'hybrid' STP (see vtpVlanStpType).

                .. data:: ieee = 1

                .. data:: ibm = 2

                .. data:: auto = 3

                """

                ieee = Enum.YLeaf(1, "ieee")

                ibm = Enum.YLeaf(2, "ibm")

                auto = Enum.YLeaf(3, "auto")


            def has_data(self):
                return (
                    self.managementdomainindex.is_set or
                    self.vtpvlaneditindex.is_set or
                    self.stpxvlanmistpinstmapeditinstindex.is_set or
                    self.vtpvlaneditarehopcount.is_set or
                    self.vtpvlaneditbridgenumber.is_set or
                    self.vtpvlaneditbridgetype.is_set or
                    self.vtpvlaneditdot10said.is_set or
                    self.vtpvlaneditiscrfbackup.is_set or
                    self.vtpvlaneditmtu.is_set or
                    self.vtpvlaneditname.is_set or
                    self.vtpvlaneditparentvlan.is_set or
                    self.vtpvlaneditringnumber.is_set or
                    self.vtpvlaneditrowstatus.is_set or
                    self.vtpvlaneditstate.is_set or
                    self.vtpvlaneditstehopcount.is_set or
                    self.vtpvlaneditstptype.is_set or
                    self.vtpvlanedittranslationalvlan1.is_set or
                    self.vtpvlanedittranslationalvlan2.is_set or
                    self.vtpvlanedittype.is_set or
                    self.vtpvlanedittypeext.is_set or
                    self.vtpvlanedittypeext2.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.managementdomainindex.yfilter != YFilter.not_set or
                    self.vtpvlaneditindex.yfilter != YFilter.not_set or
                    self.stpxvlanmistpinstmapeditinstindex.yfilter != YFilter.not_set or
                    self.vtpvlaneditarehopcount.yfilter != YFilter.not_set or
                    self.vtpvlaneditbridgenumber.yfilter != YFilter.not_set or
                    self.vtpvlaneditbridgetype.yfilter != YFilter.not_set or
                    self.vtpvlaneditdot10said.yfilter != YFilter.not_set or
                    self.vtpvlaneditiscrfbackup.yfilter != YFilter.not_set or
                    self.vtpvlaneditmtu.yfilter != YFilter.not_set or
                    self.vtpvlaneditname.yfilter != YFilter.not_set or
                    self.vtpvlaneditparentvlan.yfilter != YFilter.not_set or
                    self.vtpvlaneditringnumber.yfilter != YFilter.not_set or
                    self.vtpvlaneditrowstatus.yfilter != YFilter.not_set or
                    self.vtpvlaneditstate.yfilter != YFilter.not_set or
                    self.vtpvlaneditstehopcount.yfilter != YFilter.not_set or
                    self.vtpvlaneditstptype.yfilter != YFilter.not_set or
                    self.vtpvlanedittranslationalvlan1.yfilter != YFilter.not_set or
                    self.vtpvlanedittranslationalvlan2.yfilter != YFilter.not_set or
                    self.vtpvlanedittype.yfilter != YFilter.not_set or
                    self.vtpvlanedittypeext.yfilter != YFilter.not_set or
                    self.vtpvlanedittypeext2.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vtpVlanEditEntry" + "[managementDomainIndex='" + self.managementdomainindex.get() + "']" + "[vtpVlanEditIndex='" + self.vtpvlaneditindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/vtpVlanEditTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.managementdomainindex.is_set or self.managementdomainindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainindex.get_name_leafdata())
                if (self.vtpvlaneditindex.is_set or self.vtpvlaneditindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlaneditindex.get_name_leafdata())
                if (self.stpxvlanmistpinstmapeditinstindex.is_set or self.stpxvlanmistpinstmapeditinstindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxvlanmistpinstmapeditinstindex.get_name_leafdata())
                if (self.vtpvlaneditarehopcount.is_set or self.vtpvlaneditarehopcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlaneditarehopcount.get_name_leafdata())
                if (self.vtpvlaneditbridgenumber.is_set or self.vtpvlaneditbridgenumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlaneditbridgenumber.get_name_leafdata())
                if (self.vtpvlaneditbridgetype.is_set or self.vtpvlaneditbridgetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlaneditbridgetype.get_name_leafdata())
                if (self.vtpvlaneditdot10said.is_set or self.vtpvlaneditdot10said.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlaneditdot10said.get_name_leafdata())
                if (self.vtpvlaneditiscrfbackup.is_set or self.vtpvlaneditiscrfbackup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlaneditiscrfbackup.get_name_leafdata())
                if (self.vtpvlaneditmtu.is_set or self.vtpvlaneditmtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlaneditmtu.get_name_leafdata())
                if (self.vtpvlaneditname.is_set or self.vtpvlaneditname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlaneditname.get_name_leafdata())
                if (self.vtpvlaneditparentvlan.is_set or self.vtpvlaneditparentvlan.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlaneditparentvlan.get_name_leafdata())
                if (self.vtpvlaneditringnumber.is_set or self.vtpvlaneditringnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlaneditringnumber.get_name_leafdata())
                if (self.vtpvlaneditrowstatus.is_set or self.vtpvlaneditrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlaneditrowstatus.get_name_leafdata())
                if (self.vtpvlaneditstate.is_set or self.vtpvlaneditstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlaneditstate.get_name_leafdata())
                if (self.vtpvlaneditstehopcount.is_set or self.vtpvlaneditstehopcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlaneditstehopcount.get_name_leafdata())
                if (self.vtpvlaneditstptype.is_set or self.vtpvlaneditstptype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlaneditstptype.get_name_leafdata())
                if (self.vtpvlanedittranslationalvlan1.is_set or self.vtpvlanedittranslationalvlan1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanedittranslationalvlan1.get_name_leafdata())
                if (self.vtpvlanedittranslationalvlan2.is_set or self.vtpvlanedittranslationalvlan2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanedittranslationalvlan2.get_name_leafdata())
                if (self.vtpvlanedittype.is_set or self.vtpvlanedittype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanedittype.get_name_leafdata())
                if (self.vtpvlanedittypeext.is_set or self.vtpvlanedittypeext.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanedittypeext.get_name_leafdata())
                if (self.vtpvlanedittypeext2.is_set or self.vtpvlanedittypeext2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanedittypeext2.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "managementDomainIndex" or name == "vtpVlanEditIndex" or name == "stpxVlanMISTPInstMapEditInstIndex" or name == "vtpVlanEditAreHopCount" or name == "vtpVlanEditBridgeNumber" or name == "vtpVlanEditBridgeType" or name == "vtpVlanEditDot10Said" or name == "vtpVlanEditIsCRFBackup" or name == "vtpVlanEditMtu" or name == "vtpVlanEditName" or name == "vtpVlanEditParentVlan" or name == "vtpVlanEditRingNumber" or name == "vtpVlanEditRowStatus" or name == "vtpVlanEditState" or name == "vtpVlanEditSteHopCount" or name == "vtpVlanEditStpType" or name == "vtpVlanEditTranslationalVlan1" or name == "vtpVlanEditTranslationalVlan2" or name == "vtpVlanEditType" or name == "vtpVlanEditTypeExt" or name == "vtpVlanEditTypeExt2"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "managementDomainIndex"):
                    self.managementdomainindex = value
                    self.managementdomainindex.value_namespace = name_space
                    self.managementdomainindex.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanEditIndex"):
                    self.vtpvlaneditindex = value
                    self.vtpvlaneditindex.value_namespace = name_space
                    self.vtpvlaneditindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxVlanMISTPInstMapEditInstIndex"):
                    self.stpxvlanmistpinstmapeditinstindex = value
                    self.stpxvlanmistpinstmapeditinstindex.value_namespace = name_space
                    self.stpxvlanmistpinstmapeditinstindex.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanEditAreHopCount"):
                    self.vtpvlaneditarehopcount = value
                    self.vtpvlaneditarehopcount.value_namespace = name_space
                    self.vtpvlaneditarehopcount.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanEditBridgeNumber"):
                    self.vtpvlaneditbridgenumber = value
                    self.vtpvlaneditbridgenumber.value_namespace = name_space
                    self.vtpvlaneditbridgenumber.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanEditBridgeType"):
                    self.vtpvlaneditbridgetype = value
                    self.vtpvlaneditbridgetype.value_namespace = name_space
                    self.vtpvlaneditbridgetype.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanEditDot10Said"):
                    self.vtpvlaneditdot10said = value
                    self.vtpvlaneditdot10said.value_namespace = name_space
                    self.vtpvlaneditdot10said.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanEditIsCRFBackup"):
                    self.vtpvlaneditiscrfbackup = value
                    self.vtpvlaneditiscrfbackup.value_namespace = name_space
                    self.vtpvlaneditiscrfbackup.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanEditMtu"):
                    self.vtpvlaneditmtu = value
                    self.vtpvlaneditmtu.value_namespace = name_space
                    self.vtpvlaneditmtu.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanEditName"):
                    self.vtpvlaneditname = value
                    self.vtpvlaneditname.value_namespace = name_space
                    self.vtpvlaneditname.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanEditParentVlan"):
                    self.vtpvlaneditparentvlan = value
                    self.vtpvlaneditparentvlan.value_namespace = name_space
                    self.vtpvlaneditparentvlan.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanEditRingNumber"):
                    self.vtpvlaneditringnumber = value
                    self.vtpvlaneditringnumber.value_namespace = name_space
                    self.vtpvlaneditringnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanEditRowStatus"):
                    self.vtpvlaneditrowstatus = value
                    self.vtpvlaneditrowstatus.value_namespace = name_space
                    self.vtpvlaneditrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanEditState"):
                    self.vtpvlaneditstate = value
                    self.vtpvlaneditstate.value_namespace = name_space
                    self.vtpvlaneditstate.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanEditSteHopCount"):
                    self.vtpvlaneditstehopcount = value
                    self.vtpvlaneditstehopcount.value_namespace = name_space
                    self.vtpvlaneditstehopcount.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanEditStpType"):
                    self.vtpvlaneditstptype = value
                    self.vtpvlaneditstptype.value_namespace = name_space
                    self.vtpvlaneditstptype.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanEditTranslationalVlan1"):
                    self.vtpvlanedittranslationalvlan1 = value
                    self.vtpvlanedittranslationalvlan1.value_namespace = name_space
                    self.vtpvlanedittranslationalvlan1.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanEditTranslationalVlan2"):
                    self.vtpvlanedittranslationalvlan2 = value
                    self.vtpvlanedittranslationalvlan2.value_namespace = name_space
                    self.vtpvlanedittranslationalvlan2.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanEditType"):
                    self.vtpvlanedittype = value
                    self.vtpvlanedittype.value_namespace = name_space
                    self.vtpvlanedittype.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanEditTypeExt"):
                    self.vtpvlanedittypeext[value] = True
                if(value_path == "vtpVlanEditTypeExt2"):
                    self.vtpvlanedittypeext2[value] = True

        def has_data(self):
            for c in self.vtpvlaneditentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vtpvlaneditentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vtpVlanEditTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vtpVlanEditEntry"):
                for c in self.vtpvlaneditentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVtpMib.Vtpvlanedittable.Vtpvlaneditentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vtpvlaneditentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vtpVlanEditEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Vtpvlanlocalshutdowntable(Entity):
        """
        Ths table contains the VLAN local shutdown
        information within management domain.
        
        .. attribute:: vtpvlanlocalshutdownentry
        
        	An entry containing VLAN local shutdown information for a particular VLAN in the management domain.  An entry is created if a VLAN which supports local shutdown has been created.  An entry is deleted if a VLAN which supports local shutdown has been removed
        	**type**\: list of    :py:class:`Vtpvlanlocalshutdownentry <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpvlanlocalshutdowntable.Vtpvlanlocalshutdownentry>`
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CiscoVtpMib.Vtpvlanlocalshutdowntable, self).__init__()

            self.yang_name = "vtpVlanLocalShutdownTable"
            self.yang_parent_name = "CISCO-VTP-MIB"

            self.vtpvlanlocalshutdownentry = YList(self)

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
                        super(CiscoVtpMib.Vtpvlanlocalshutdowntable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVtpMib.Vtpvlanlocalshutdowntable, self).__setattr__(name, value)


        class Vtpvlanlocalshutdownentry(Entity):
            """
            An entry containing VLAN local shutdown information for a
            particular VLAN in the management domain.
            
            An entry is created if a VLAN which supports local shutdown
            has been created.
            
            An entry is deleted if a VLAN which supports local shutdown
            has been removed.
            
            .. attribute:: managementdomainindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..255
            
            	**refers to**\:  :py:class:`managementdomainindex <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Managementdomaintable.Managementdomainentry>`
            
            .. attribute:: vtpvlanindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`vtpvlanindex <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpvlantable.Vtpvlanentry>`
            
            .. attribute:: vtpvlanlocalshutdown
            
            	The object specifies the VLAN local shutdown state
            	**type**\:   :py:class:`Vtpvlanlocalshutdown <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpvlanlocalshutdowntable.Vtpvlanlocalshutdownentry.Vtpvlanlocalshutdown>`
            
            

            """

            _prefix = 'CISCO-VTP-MIB'
            _revision = '2013-10-14'

            def __init__(self):
                super(CiscoVtpMib.Vtpvlanlocalshutdowntable.Vtpvlanlocalshutdownentry, self).__init__()

                self.yang_name = "vtpVlanLocalShutdownEntry"
                self.yang_parent_name = "vtpVlanLocalShutdownTable"

                self.managementdomainindex = YLeaf(YType.str, "managementDomainIndex")

                self.vtpvlanindex = YLeaf(YType.str, "vtpVlanIndex")

                self.vtpvlanlocalshutdown = YLeaf(YType.enumeration, "vtpVlanLocalShutdown")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("managementdomainindex",
                                "vtpvlanindex",
                                "vtpvlanlocalshutdown") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVtpMib.Vtpvlanlocalshutdowntable.Vtpvlanlocalshutdownentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVtpMib.Vtpvlanlocalshutdowntable.Vtpvlanlocalshutdownentry, self).__setattr__(name, value)

            class Vtpvlanlocalshutdown(Enum):
                """
                Vtpvlanlocalshutdown

                The object specifies the VLAN local shutdown state.

                .. data:: up = 1

                .. data:: down = 2

                """

                up = Enum.YLeaf(1, "up")

                down = Enum.YLeaf(2, "down")


            def has_data(self):
                return (
                    self.managementdomainindex.is_set or
                    self.vtpvlanindex.is_set or
                    self.vtpvlanlocalshutdown.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.managementdomainindex.yfilter != YFilter.not_set or
                    self.vtpvlanindex.yfilter != YFilter.not_set or
                    self.vtpvlanlocalshutdown.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vtpVlanLocalShutdownEntry" + "[managementDomainIndex='" + self.managementdomainindex.get() + "']" + "[vtpVlanIndex='" + self.vtpvlanindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/vtpVlanLocalShutdownTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.managementdomainindex.is_set or self.managementdomainindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainindex.get_name_leafdata())
                if (self.vtpvlanindex.is_set or self.vtpvlanindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanindex.get_name_leafdata())
                if (self.vtpvlanlocalshutdown.is_set or self.vtpvlanlocalshutdown.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanlocalshutdown.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "managementDomainIndex" or name == "vtpVlanIndex" or name == "vtpVlanLocalShutdown"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "managementDomainIndex"):
                    self.managementdomainindex = value
                    self.managementdomainindex.value_namespace = name_space
                    self.managementdomainindex.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanIndex"):
                    self.vtpvlanindex = value
                    self.vtpvlanindex.value_namespace = name_space
                    self.vtpvlanindex.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlanLocalShutdown"):
                    self.vtpvlanlocalshutdown = value
                    self.vtpvlanlocalshutdown.value_namespace = name_space
                    self.vtpvlanlocalshutdown.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vtpvlanlocalshutdownentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vtpvlanlocalshutdownentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vtpVlanLocalShutdownTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vtpVlanLocalShutdownEntry"):
                for c in self.vtpvlanlocalshutdownentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVtpMib.Vtpvlanlocalshutdowntable.Vtpvlanlocalshutdownentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vtpvlanlocalshutdownentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vtpVlanLocalShutdownEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Vlantrunkporttable(Entity):
        """
        The table containing information on the local system's VLAN
        trunk ports.
        
        .. attribute:: vlantrunkportentry
        
        	Information about one trunk port
        	**type**\: list of    :py:class:`Vlantrunkportentry <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry>`
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CiscoVtpMib.Vlantrunkporttable, self).__init__()

            self.yang_name = "vlanTrunkPortTable"
            self.yang_parent_name = "CISCO-VTP-MIB"

            self.vlantrunkportentry = YList(self)

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
                        super(CiscoVtpMib.Vlantrunkporttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVtpMib.Vlantrunkporttable, self).__setattr__(name, value)


        class Vlantrunkportentry(Entity):
            """
            Information about one trunk port.
            
            .. attribute:: vlantrunkportifindex  <key>
            
            	The value of ifIndex for the interface corresponding to this trunk port
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: stpxpreferredmistpinstancesmap
            
            	A string of octets containing one bit per MISTP instances  in the management domain on this trunk port. The first octet corresponds to MISTP instances with InstIndex values of 1  through 8; the second octet to MISTP instances 9 through 16; etc. The most significant bit of each octet corresponds to  the lowest value instanceIndex in that octet. The number of  bits for this mib object will be determined by the value of  stpxMISTPInstanceNumber.  For each instance, if it is preferred on this trunk port, then the bit corresponding to that instance is set to '1'.   To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single instance on the trunk port), any SNMP Set operation  accessing an instance of this object should also write the  value of vlanTrunkPortSetSerialNo
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: stpxpreferredmstinstancesmap
            
            	A string of octets containing one bit per MST instances  on this trunk port.  The first octet corresponds to MST  instances of 0 through 7; the second octet to MST instances  8 through 15; etc. The most significant bit of each octet  corresponds to the lowest MST instance value in that octet.  The number of bits for this mib object will be determined  by the value of stpxMSTMaxInstanceNumber.  For each instance, if it is preferred on this trunk port,  then the bit corresponding to that instance is set to '1'
            	**type**\:  str
            
            	**length:** 1..32
            
            	**status**\: deprecated
            
            .. attribute:: stpxpreferredvlansmap
            
            	A string of octets containing one bit per VLAN in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is preferred on this trunk port, then the bit corresponding to that VLAN is set to '1'. The default value is 128 bytes of zeros.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\:  str
            
            	**length:** 128
            
            .. attribute:: stpxpreferredvlansmap2k
            
            	A string of octets containing one bit per VLAN for VLANS  with VlanIndex values of 1024 through 2047 in the management domain on this trunk port.  The first octet corresponds to  VLANs with VlanIndex values of 1024 through 1031;  the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the  lowest value VlanIndex in that octet.   For each VLAN, if it is preferred on this trunk port, then  the bit corresponding to that VLAN is set to '1'.  The default value is 128 bytes of zeros.   To avoid conflicts between overlapping partial updates by  multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of  vlanTrunkPortSetSerialNo
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: stpxpreferredvlansmap3k
            
            	A string of octets containing one bit per VLAN for VLANS  with VlanIndex values of 2048 through 3071 in the management domain on this trunk port.  The first octet corresponds to  VLANs with VlanIndex values of 2048 through 2055;  the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the  lowest value VlanIndex in that octet.   For each VLAN, if it is preferred on this trunk port, then  the bit corresponding to that VLAN is set to '1'.  The default value is 128 bytes of zeros.   To avoid conflicts between overlapping partial updates by  multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of  vlanTrunkPortSetSerialNo
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: stpxpreferredvlansmap4k
            
            	A string of octets containing one bit per VLAN for VLANS  with VlanIndex values of 3072 through 4095 in the management domain on this trunk port.  The first octet corresponds to  VLANs with VlanIndex values of 3072 through 3079;  the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the  lowest value VlanIndex in that octet.   For each VLAN, if it is preferred on this trunk port, then  the bit corresponding to that VLAN is set to '1'.  The default value is 128 bytes of zeros.   To avoid conflicts between overlapping partial updates by  multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of  vlanTrunkPortSetSerialNo
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: vlantrunkportdot1qtunnel
            
            	Indicates dot1qtunnel mode of the port.  If the portDot1qTunnel  is set to 'trunk' mode, the port's vlanTrunkPortDynamicState will be changed to 'onNoNegotiate' and the vlanTrunkPortEncapsulationType will be set to 'dot1Q'. These values cannot be changed unless dot1q tunnel is disabled on this port.  If the portDot1qTunnel mode is set to 'access' mode, the port's vlanTrunkPortDynamicState will be set to 'off'.And the value of vlanTrunkPortDynamicState cannot be changed unless dot1q tunnel is disabled on this port. 1Q packets received on this access port will remain.  Setting the port to dot1q tunnel 'disabled' mode causes the dot1q tunnel feature to be disabled on this port.  This object can't be set to 'trunk' or 'access' mode, when vlanTrunkPortsDot1qTag  object is set to 'false'.  This object has been deprecated and is replaced by the object 'cltcDot1qTunnelMode' in the CISCO\-L2\-TUNNEL\-CONFIG\-MIB
            	**type**\:   :py:class:`Vlantrunkportdot1Qtunnel <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry.Vlantrunkportdot1Qtunnel>`
            
            	**status**\: deprecated
            
            .. attribute:: vlantrunkportdynamicstate
            
            	For devices that allows dynamic determination of whether a link between two switches should be a trunk or not, this object allows the operator to mandate the behavior of that dynamic mechanism.  on(1) dictates that the interface will always be a trunk. This is the value for static entries (those that show no dynamic behavior). If the negotiation is supported on this port, negotiation will take place with the far end to attempt to bring the far end into trunking state.  off(2) allows an operator to specify that the specified interface is never to be trunk, regardless of any dynamic mechanisms to the contrary.  This value is useful for overriding the default behavior of some switches. If the negotiation is supported on this port, negotiation will take place with the far end to attempt on the link to bring the far end into non\-trunking state.  desirable(3) is used to indicate that it is desirable for the interface to become a trunk.  The device will initiate any negotiation necessary to become a trunk but will not become a trunk unless it receives confirmation from the far end on the link.  auto(4) is used to indicate that the interface is capable and willing to become a trunk but will not initiate trunking negotiations.  The far end on the link are required to either start negotiations or start sending encapsulated packets, on which event the specified interface will become a trunk.  onNoNegotiate(5) is used to indicate that the interface is permanently set to be a trunk, and no negotiation takes place with the far end on the link to ensure consistent operation. This is similar to on(1) except no negotiation takes place with the far end.  If the port does not support negotiation or its vlanTrunkPortEncapsulationType is set to negotiate(5), onNoNegotiate(5) is not allowed.  Devices that do no support dynamic determination (for just a particular interface, encapsulation or for the whole device) need only support the 'on', and 'off' values
            	**type**\:   :py:class:`Vlantrunkportdynamicstate <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry.Vlantrunkportdynamicstate>`
            
            .. attribute:: vlantrunkportdynamicstatus
            
            	Indicates whether the specified interface is either acting as a trunk or not. This is a result of the vlanTrunkPortDynamicState and the ifOperStatus of the trunk port itself
            	**type**\:   :py:class:`Vlantrunkportdynamicstatus <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry.Vlantrunkportdynamicstatus>`
            
            .. attribute:: vlantrunkportencapsulationopertype
            
            	The type of VLAN encapsulation in use on this trunk port. For intefaces with vlanTrunkPortDynamicStatus of notTrunking(2) the vlanTrunkPortEncapsulationOperType shall be notApplicable(6)
            	**type**\:   :py:class:`Vlantrunkportencapsulationopertype <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry.Vlantrunkportencapsulationopertype>`
            
            .. attribute:: vlantrunkportencapsulationtype
            
            	The type of VLAN encapsulation desired to be used on this trunk port. It is either a particular type, or 'negotiate' meaning whatever type results from the negotiation. negotiate(5) is not allowed if the port does not support negotiation or if its vlanTrunkPortDynamicState is set to on(1) or onNoNegotiate(5). Whether writing to this object in order to modify the encapsulation is supported is both device and interface specific
            	**type**\:   :py:class:`Vlantrunkportencapsulationtype <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry.Vlantrunkportencapsulationtype>`
            
            .. attribute:: vlantrunkportinjoins
            
            	The number of VTP Join messages received on this trunk port
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vlantrunkportmanagementdomain
            
            	The value of managementDomainIndex for the management domain on this trunk port.  Devices which support only one management domain will support this object read\-only
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: vlantrunkportnativevlan
            
            	The VlanIndex of the VLAN which is represented by native frames on this trunk port.  For trunk ports not supporting the sending and receiving of native frames, this value should be set to zero
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: vlantrunkportoldadverts
            
            	The number of VTP Advertisement messages which indicated the sender does not support VLAN\-pruning received on this trunk port
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vlantrunkportoutjoins
            
            	The number of VTP Join messages sent on this trunk port
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vlantrunkportrowstatus
            
            	The status of this row.  In some circumstances, the creation of a row in this table is needed to enable the appropriate trunking/tagging protocol on the port, to enable the use of VTP on the port, and to assign the port to the appropriate management domain.  In other circumstances, rows in this table will be created as a by\-product of other operations
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: vlantrunkportvlansactivefirst2k
            
            	A string of octets containing one bit per VLAN with VlanIndex values of 0 through 2047.  If the bit corresponding to a VLAN is set to 1, it indicates that vlan is allowed and active in management domain.  If the bit corresponding to a VLAN is set to 0, it indicates that vlan is not allowed or not active in management domain
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: vlantrunkportvlansactivesecond2k
            
            	A string of octets containing one bit per VLAN with VlanIndex values of 2048 through 4095.  If the bit corresponding to a VLAN is set to 1, it indicates that vlan is allowed and active in management domain.  If the bit corresponding to a VLAN is set to 0, it indicates that vlan is not allowed or not active in management domain
            	**type**\:  str
            
            	**length:** 0..256
            
            .. attribute:: vlantrunkportvlansenabled
            
            	A string of octets containing one bit per VLAN in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local system is enabled for sending and receiving frames on that VLAN; if the bit is set to '0', then the system is disabled from sending and receiving frames on that VLAN.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\:  str
            
            	**length:** 128
            
            .. attribute:: vlantrunkportvlansenabled2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 1024 through 2047 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 1024 through 1031; the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet. If the bit corresponding to a VLAN is set to '1', then the local system is enabled for sending and receiving frames on that VLAN; if the bit is set to '0', then the system is disabled from sending and receiving frames on that VLAN. The default value is zero length string.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: vlantrunkportvlansenabled3k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 3071 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet. If the bit corresponding to a VLAN is set to '1', then the local system is enabled for sending and receiving frames on that VLAN; if the bit is set to '0', then the system is disabled from sending and receiving frames on that VLAN. The default value is zero length string.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: vlantrunkportvlansenabled4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 3072 through 4095 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 3072 through 3079; the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet. If the bit corresponding to a VLAN is set to '1', then the local system is enabled for sending and receiving frames on that VLAN; if the bit is set to '0', then the system is disabled from sending and receiving frames on that VLAN. The default value is zero length string.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: vlantrunkportvlanspruningeligible
            
            	A string of octets containing one bit per VLAN in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local system is permitted to prune that VLAN on this trunk port; if the bit is set to '0', then the system must not prune that VLAN on this trunk port.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\:  str
            
            	**length:** 128
            
            .. attribute:: vlantrunkportvlansrcvjoined
            
            	A string of octets containing one bit per VLAN in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local switch is currently sending joins for this VLAN on this trunk port, i.e., it is asking to receive frames for this VLAN; if the bit is set to '0', then the local switch is not currently sending joins for this VLAN on this trunk port
            	**type**\:  str
            
            	**length:** 128
            
            .. attribute:: vlantrunkportvlansrcvjoined2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 1024 through 2047 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 1024 through 1031; the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local switch is currently sending joins for this VLAN on this trunk port, i.e., it is asking to receive frames for this VLAN; if the bit is set to '0', then the local switch is not currently sending joins for this VLAN on this trunk port
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: vlantrunkportvlansrcvjoined3k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 3071 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local switch is currently sending joins for this VLAN on this trunk port, i.e., it is asking to receive frames for this VLAN; if the bit is set to '0', then the local switch is not currently sending joins for this VLAN on this trunk port
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: vlantrunkportvlansrcvjoined4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 3072 through 4095 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 3072 through 3079; the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local switch is currently sending joins for this VLAN on this trunk port, i.e., it is asking to receive frames for this VLAN; if the bit is set to '0', then the local switch is not currently sending joins for this VLAN on this trunk port
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: vlantrunkportvlansxmitjoined
            
            	A string of octets containing one bit per VLAN in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then this VLAN is presently being forwarded on this trunk port, i.e., it is not pruned; if the bit is set to '0', then this VLAN is presently not being forwarded on this trunk port, either because it is pruned or for some other reason
            	**type**\:  str
            
            	**length:** 128
            
            .. attribute:: vlantrunkportvlansxmitjoined2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 1024 through 2047 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 1024 through 1031; the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then this VLAN is presently being forwarded on this trunk port, i.e., it is not pruned; if the bit is set to '0', then this VLAN is presently not being forwarded on this trunk port, either because it is pruned or for some other reason
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: vlantrunkportvlansxmitjoined3k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 3071 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then this VLAN is presently being forwarded on this trunk port, i.e., it is not pruned; if the bit is set to '0', then this VLAN is presently not being forwarded on this trunk port, either because it is pruned or for some other reason
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: vlantrunkportvlansxmitjoined4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 3072 through 4095 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 3072 through 3079; the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then this VLAN is presently being forwarded on this trunk port, i.e., it is not pruned; if the bit is set to '0', then this VLAN is presently not being forwarded on this trunk port, either because it is pruned or for some other reason
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: vlantrunkportvtpenabled
            
            	Some trunk interface modules allow VTP to be enabled/disabled seperately from that of the central device.  In such a case this object provides management a way to remotely enable VTP on that module.  If a module does not support a seperate VTP enabled state then this object shall always return 'true' and will accept no other value during a SET operation
            	**type**\:  bool
            
            .. attribute:: vtpvlanspruningeligible2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 1024 through 2047 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 1024 through 1031; the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local system is permitted to prune that VLAN on this trunk port; if the bit is set to '0', then the system must not prune that VLAN on this trunk port. The default value is zero length string.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: vtpvlanspruningeligible3k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 3071 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local system is permitted to prune that VLAN on this trunk port; if the bit is set to '0', then the system must not prune that VLAN on this trunk port. The default value is zero length string.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: vtpvlanspruningeligible4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 3072 through 4095 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 3072 through 3079; the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local system is permitted to prune that VLAN on this trunk port; if the bit is set to '0', then the system must not prune that VLAN on this trunk port. The default value is zero length string.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\:  str
            
            	**length:** 0..128
            
            

            """

            _prefix = 'CISCO-VTP-MIB'
            _revision = '2013-10-14'

            def __init__(self):
                super(CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry, self).__init__()

                self.yang_name = "vlanTrunkPortEntry"
                self.yang_parent_name = "vlanTrunkPortTable"

                self.vlantrunkportifindex = YLeaf(YType.int32, "vlanTrunkPortIfIndex")

                self.stpxpreferredmistpinstancesmap = YLeaf(YType.str, "CISCO-STP-EXTENSIONS-MIB:stpxPreferredMISTPInstancesMap")

                self.stpxpreferredmstinstancesmap = YLeaf(YType.str, "CISCO-STP-EXTENSIONS-MIB:stpxPreferredMSTInstancesMap")

                self.stpxpreferredvlansmap = YLeaf(YType.str, "CISCO-STP-EXTENSIONS-MIB:stpxPreferredVlansMap")

                self.stpxpreferredvlansmap2k = YLeaf(YType.str, "CISCO-STP-EXTENSIONS-MIB:stpxPreferredVlansMap2k")

                self.stpxpreferredvlansmap3k = YLeaf(YType.str, "CISCO-STP-EXTENSIONS-MIB:stpxPreferredVlansMap3k")

                self.stpxpreferredvlansmap4k = YLeaf(YType.str, "CISCO-STP-EXTENSIONS-MIB:stpxPreferredVlansMap4k")

                self.vlantrunkportdot1qtunnel = YLeaf(YType.enumeration, "vlanTrunkPortDot1qTunnel")

                self.vlantrunkportdynamicstate = YLeaf(YType.enumeration, "vlanTrunkPortDynamicState")

                self.vlantrunkportdynamicstatus = YLeaf(YType.enumeration, "vlanTrunkPortDynamicStatus")

                self.vlantrunkportencapsulationopertype = YLeaf(YType.enumeration, "vlanTrunkPortEncapsulationOperType")

                self.vlantrunkportencapsulationtype = YLeaf(YType.enumeration, "vlanTrunkPortEncapsulationType")

                self.vlantrunkportinjoins = YLeaf(YType.uint32, "vlanTrunkPortInJoins")

                self.vlantrunkportmanagementdomain = YLeaf(YType.int32, "vlanTrunkPortManagementDomain")

                self.vlantrunkportnativevlan = YLeaf(YType.int32, "vlanTrunkPortNativeVlan")

                self.vlantrunkportoldadverts = YLeaf(YType.uint32, "vlanTrunkPortOldAdverts")

                self.vlantrunkportoutjoins = YLeaf(YType.uint32, "vlanTrunkPortOutJoins")

                self.vlantrunkportrowstatus = YLeaf(YType.enumeration, "vlanTrunkPortRowStatus")

                self.vlantrunkportvlansactivefirst2k = YLeaf(YType.str, "vlanTrunkPortVlansActiveFirst2k")

                self.vlantrunkportvlansactivesecond2k = YLeaf(YType.str, "vlanTrunkPortVlansActiveSecond2k")

                self.vlantrunkportvlansenabled = YLeaf(YType.str, "vlanTrunkPortVlansEnabled")

                self.vlantrunkportvlansenabled2k = YLeaf(YType.str, "vlanTrunkPortVlansEnabled2k")

                self.vlantrunkportvlansenabled3k = YLeaf(YType.str, "vlanTrunkPortVlansEnabled3k")

                self.vlantrunkportvlansenabled4k = YLeaf(YType.str, "vlanTrunkPortVlansEnabled4k")

                self.vlantrunkportvlanspruningeligible = YLeaf(YType.str, "vlanTrunkPortVlansPruningEligible")

                self.vlantrunkportvlansrcvjoined = YLeaf(YType.str, "vlanTrunkPortVlansRcvJoined")

                self.vlantrunkportvlansrcvjoined2k = YLeaf(YType.str, "vlanTrunkPortVlansRcvJoined2k")

                self.vlantrunkportvlansrcvjoined3k = YLeaf(YType.str, "vlanTrunkPortVlansRcvJoined3k")

                self.vlantrunkportvlansrcvjoined4k = YLeaf(YType.str, "vlanTrunkPortVlansRcvJoined4k")

                self.vlantrunkportvlansxmitjoined = YLeaf(YType.str, "vlanTrunkPortVlansXmitJoined")

                self.vlantrunkportvlansxmitjoined2k = YLeaf(YType.str, "vlanTrunkPortVlansXmitJoined2k")

                self.vlantrunkportvlansxmitjoined3k = YLeaf(YType.str, "vlanTrunkPortVlansXmitJoined3k")

                self.vlantrunkportvlansxmitjoined4k = YLeaf(YType.str, "vlanTrunkPortVlansXmitJoined4k")

                self.vlantrunkportvtpenabled = YLeaf(YType.boolean, "vlanTrunkPortVtpEnabled")

                self.vtpvlanspruningeligible2k = YLeaf(YType.str, "vtpVlansPruningEligible2k")

                self.vtpvlanspruningeligible3k = YLeaf(YType.str, "vtpVlansPruningEligible3k")

                self.vtpvlanspruningeligible4k = YLeaf(YType.str, "vtpVlansPruningEligible4k")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vlantrunkportifindex",
                                "stpxpreferredmistpinstancesmap",
                                "stpxpreferredmstinstancesmap",
                                "stpxpreferredvlansmap",
                                "stpxpreferredvlansmap2k",
                                "stpxpreferredvlansmap3k",
                                "stpxpreferredvlansmap4k",
                                "vlantrunkportdot1qtunnel",
                                "vlantrunkportdynamicstate",
                                "vlantrunkportdynamicstatus",
                                "vlantrunkportencapsulationopertype",
                                "vlantrunkportencapsulationtype",
                                "vlantrunkportinjoins",
                                "vlantrunkportmanagementdomain",
                                "vlantrunkportnativevlan",
                                "vlantrunkportoldadverts",
                                "vlantrunkportoutjoins",
                                "vlantrunkportrowstatus",
                                "vlantrunkportvlansactivefirst2k",
                                "vlantrunkportvlansactivesecond2k",
                                "vlantrunkportvlansenabled",
                                "vlantrunkportvlansenabled2k",
                                "vlantrunkportvlansenabled3k",
                                "vlantrunkportvlansenabled4k",
                                "vlantrunkportvlanspruningeligible",
                                "vlantrunkportvlansrcvjoined",
                                "vlantrunkportvlansrcvjoined2k",
                                "vlantrunkportvlansrcvjoined3k",
                                "vlantrunkportvlansrcvjoined4k",
                                "vlantrunkportvlansxmitjoined",
                                "vlantrunkportvlansxmitjoined2k",
                                "vlantrunkportvlansxmitjoined3k",
                                "vlantrunkportvlansxmitjoined4k",
                                "vlantrunkportvtpenabled",
                                "vtpvlanspruningeligible2k",
                                "vtpvlanspruningeligible3k",
                                "vtpvlanspruningeligible4k") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry, self).__setattr__(name, value)

            class Vlantrunkportdot1Qtunnel(Enum):
                """
                Vlantrunkportdot1Qtunnel

                Indicates dot1qtunnel mode of the port.

                If the portDot1qTunnel  is set to 'trunk' mode, the port's

                vlanTrunkPortDynamicState will be changed to 'onNoNegotiate'

                and the vlanTrunkPortEncapsulationType will be set to

                'dot1Q'. These values cannot be changed unless dot1q tunnel

                is disabled on this port.

                If the portDot1qTunnel mode is set to 'access' mode, the

                port's vlanTrunkPortDynamicState will be set to 'off'.And

                the value of vlanTrunkPortDynamicState cannot be changed

                unless dot1q tunnel is disabled on this port. 1Q packets

                received on this access port will remain.

                Setting the port to dot1q tunnel 'disabled' mode causes the

                dot1q tunnel feature to be disabled on this port.  This

                object can't be set to 'trunk' or 'access' mode, when

                vlanTrunkPortsDot1qTag  object is set to 'false'.

                This object has been deprecated and is replaced by the

                object 'cltcDot1qTunnelMode' in the

                CISCO\-L2\-TUNNEL\-CONFIG\-MIB

                .. data:: trunk = 1

                .. data:: access = 2

                .. data:: disabled = 3

                """

                trunk = Enum.YLeaf(1, "trunk")

                access = Enum.YLeaf(2, "access")

                disabled = Enum.YLeaf(3, "disabled")


            class Vlantrunkportdynamicstate(Enum):
                """
                Vlantrunkportdynamicstate

                For devices that allows dynamic determination of whether

                a link between two switches should be a trunk or not, this

                object allows the operator to mandate the behavior of that

                dynamic mechanism.

                on(1) dictates that the interface will always be a

                trunk. This is the value for static entries (those that

                show no dynamic behavior). If the negotiation is supported

                on this port, negotiation will take place with the far end

                to attempt to bring the far end into trunking state.

                off(2) allows an operator to specify that the specified

                interface is never to be trunk, regardless of any dynamic

                mechanisms to the contrary.  This value is useful for

                overriding the default behavior of some switches. If the

                negotiation is supported on this port, negotiation will take

                place with the far end to attempt on the link to bring the

                far end into non\-trunking state.

                desirable(3) is used to indicate that it is desirable for

                the interface to become a trunk.  The device will initiate

                any negotiation necessary to become a trunk but will not

                become a trunk unless it receives confirmation from the far

                end on the link.

                auto(4) is used to indicate that the interface is capable

                and willing to become a trunk but will not initiate

                trunking negotiations.  The far end on the link are

                required to either start negotiations or start sending

                encapsulated packets, on which event the specified

                interface will become a trunk.

                onNoNegotiate(5) is used to indicate that the interface is

                permanently set to be a trunk, and no negotiation takes

                place with the far end on the link to ensure consistent

                operation. This is similar to on(1) except no negotiation

                takes place with the far end.

                If the port does not support negotiation or its

                vlanTrunkPortEncapsulationType is set to negotiate(5),

                onNoNegotiate(5) is not allowed.

                Devices that do no support dynamic determination (for just

                a particular interface, encapsulation or for the whole

                device) need only support the 'on', and 'off' values.

                .. data:: on = 1

                .. data:: off = 2

                .. data:: desirable = 3

                .. data:: auto = 4

                .. data:: onNoNegotiate = 5

                """

                on = Enum.YLeaf(1, "on")

                off = Enum.YLeaf(2, "off")

                desirable = Enum.YLeaf(3, "desirable")

                auto = Enum.YLeaf(4, "auto")

                onNoNegotiate = Enum.YLeaf(5, "onNoNegotiate")


            class Vlantrunkportdynamicstatus(Enum):
                """
                Vlantrunkportdynamicstatus

                Indicates whether the specified interface is either

                acting as a trunk or not. This is a result of the

                vlanTrunkPortDynamicState and the ifOperStatus of the

                trunk port itself.

                .. data:: trunking = 1

                .. data:: notTrunking = 2

                """

                trunking = Enum.YLeaf(1, "trunking")

                notTrunking = Enum.YLeaf(2, "notTrunking")


            class Vlantrunkportencapsulationopertype(Enum):
                """
                Vlantrunkportencapsulationopertype

                The type of VLAN encapsulation in use on this trunk port.

                For intefaces with vlanTrunkPortDynamicStatus of

                notTrunking(2) the vlanTrunkPortEncapsulationOperType shall

                be notApplicable(6).

                .. data:: isl = 1

                .. data:: dot10 = 2

                .. data:: lane = 3

                .. data:: dot1Q = 4

                .. data:: negotiating = 5

                .. data:: notApplicable = 6

                """

                isl = Enum.YLeaf(1, "isl")

                dot10 = Enum.YLeaf(2, "dot10")

                lane = Enum.YLeaf(3, "lane")

                dot1Q = Enum.YLeaf(4, "dot1Q")

                negotiating = Enum.YLeaf(5, "negotiating")

                notApplicable = Enum.YLeaf(6, "notApplicable")


            class Vlantrunkportencapsulationtype(Enum):
                """
                Vlantrunkportencapsulationtype

                The type of VLAN encapsulation desired to be used on this

                trunk port. It is either a particular type, or 'negotiate'

                meaning whatever type results from the negotiation.

                negotiate(5) is not allowed if the port does not support

                negotiation or if its vlanTrunkPortDynamicState is set to

                on(1) or onNoNegotiate(5). Whether writing to this object

                in order to modify the encapsulation is supported is both

                device and interface specific.

                .. data:: isl = 1

                .. data:: dot10 = 2

                .. data:: lane = 3

                .. data:: dot1Q = 4

                .. data:: negotiate = 5

                """

                isl = Enum.YLeaf(1, "isl")

                dot10 = Enum.YLeaf(2, "dot10")

                lane = Enum.YLeaf(3, "lane")

                dot1Q = Enum.YLeaf(4, "dot1Q")

                negotiate = Enum.YLeaf(5, "negotiate")


            def has_data(self):
                return (
                    self.vlantrunkportifindex.is_set or
                    self.stpxpreferredmistpinstancesmap.is_set or
                    self.stpxpreferredmstinstancesmap.is_set or
                    self.stpxpreferredvlansmap.is_set or
                    self.stpxpreferredvlansmap2k.is_set or
                    self.stpxpreferredvlansmap3k.is_set or
                    self.stpxpreferredvlansmap4k.is_set or
                    self.vlantrunkportdot1qtunnel.is_set or
                    self.vlantrunkportdynamicstate.is_set or
                    self.vlantrunkportdynamicstatus.is_set or
                    self.vlantrunkportencapsulationopertype.is_set or
                    self.vlantrunkportencapsulationtype.is_set or
                    self.vlantrunkportinjoins.is_set or
                    self.vlantrunkportmanagementdomain.is_set or
                    self.vlantrunkportnativevlan.is_set or
                    self.vlantrunkportoldadverts.is_set or
                    self.vlantrunkportoutjoins.is_set or
                    self.vlantrunkportrowstatus.is_set or
                    self.vlantrunkportvlansactivefirst2k.is_set or
                    self.vlantrunkportvlansactivesecond2k.is_set or
                    self.vlantrunkportvlansenabled.is_set or
                    self.vlantrunkportvlansenabled2k.is_set or
                    self.vlantrunkportvlansenabled3k.is_set or
                    self.vlantrunkportvlansenabled4k.is_set or
                    self.vlantrunkportvlanspruningeligible.is_set or
                    self.vlantrunkportvlansrcvjoined.is_set or
                    self.vlantrunkportvlansrcvjoined2k.is_set or
                    self.vlantrunkportvlansrcvjoined3k.is_set or
                    self.vlantrunkportvlansrcvjoined4k.is_set or
                    self.vlantrunkportvlansxmitjoined.is_set or
                    self.vlantrunkportvlansxmitjoined2k.is_set or
                    self.vlantrunkportvlansxmitjoined3k.is_set or
                    self.vlantrunkportvlansxmitjoined4k.is_set or
                    self.vlantrunkportvtpenabled.is_set or
                    self.vtpvlanspruningeligible2k.is_set or
                    self.vtpvlanspruningeligible3k.is_set or
                    self.vtpvlanspruningeligible4k.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vlantrunkportifindex.yfilter != YFilter.not_set or
                    self.stpxpreferredmistpinstancesmap.yfilter != YFilter.not_set or
                    self.stpxpreferredmstinstancesmap.yfilter != YFilter.not_set or
                    self.stpxpreferredvlansmap.yfilter != YFilter.not_set or
                    self.stpxpreferredvlansmap2k.yfilter != YFilter.not_set or
                    self.stpxpreferredvlansmap3k.yfilter != YFilter.not_set or
                    self.stpxpreferredvlansmap4k.yfilter != YFilter.not_set or
                    self.vlantrunkportdot1qtunnel.yfilter != YFilter.not_set or
                    self.vlantrunkportdynamicstate.yfilter != YFilter.not_set or
                    self.vlantrunkportdynamicstatus.yfilter != YFilter.not_set or
                    self.vlantrunkportencapsulationopertype.yfilter != YFilter.not_set or
                    self.vlantrunkportencapsulationtype.yfilter != YFilter.not_set or
                    self.vlantrunkportinjoins.yfilter != YFilter.not_set or
                    self.vlantrunkportmanagementdomain.yfilter != YFilter.not_set or
                    self.vlantrunkportnativevlan.yfilter != YFilter.not_set or
                    self.vlantrunkportoldadverts.yfilter != YFilter.not_set or
                    self.vlantrunkportoutjoins.yfilter != YFilter.not_set or
                    self.vlantrunkportrowstatus.yfilter != YFilter.not_set or
                    self.vlantrunkportvlansactivefirst2k.yfilter != YFilter.not_set or
                    self.vlantrunkportvlansactivesecond2k.yfilter != YFilter.not_set or
                    self.vlantrunkportvlansenabled.yfilter != YFilter.not_set or
                    self.vlantrunkportvlansenabled2k.yfilter != YFilter.not_set or
                    self.vlantrunkportvlansenabled3k.yfilter != YFilter.not_set or
                    self.vlantrunkportvlansenabled4k.yfilter != YFilter.not_set or
                    self.vlantrunkportvlanspruningeligible.yfilter != YFilter.not_set or
                    self.vlantrunkportvlansrcvjoined.yfilter != YFilter.not_set or
                    self.vlantrunkportvlansrcvjoined2k.yfilter != YFilter.not_set or
                    self.vlantrunkportvlansrcvjoined3k.yfilter != YFilter.not_set or
                    self.vlantrunkportvlansrcvjoined4k.yfilter != YFilter.not_set or
                    self.vlantrunkportvlansxmitjoined.yfilter != YFilter.not_set or
                    self.vlantrunkportvlansxmitjoined2k.yfilter != YFilter.not_set or
                    self.vlantrunkportvlansxmitjoined3k.yfilter != YFilter.not_set or
                    self.vlantrunkportvlansxmitjoined4k.yfilter != YFilter.not_set or
                    self.vlantrunkportvtpenabled.yfilter != YFilter.not_set or
                    self.vtpvlanspruningeligible2k.yfilter != YFilter.not_set or
                    self.vtpvlanspruningeligible3k.yfilter != YFilter.not_set or
                    self.vtpvlanspruningeligible4k.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vlanTrunkPortEntry" + "[vlanTrunkPortIfIndex='" + self.vlantrunkportifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/vlanTrunkPortTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vlantrunkportifindex.is_set or self.vlantrunkportifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportifindex.get_name_leafdata())
                if (self.stpxpreferredmistpinstancesmap.is_set or self.stpxpreferredmistpinstancesmap.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxpreferredmistpinstancesmap.get_name_leafdata())
                if (self.stpxpreferredmstinstancesmap.is_set or self.stpxpreferredmstinstancesmap.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxpreferredmstinstancesmap.get_name_leafdata())
                if (self.stpxpreferredvlansmap.is_set or self.stpxpreferredvlansmap.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxpreferredvlansmap.get_name_leafdata())
                if (self.stpxpreferredvlansmap2k.is_set or self.stpxpreferredvlansmap2k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxpreferredvlansmap2k.get_name_leafdata())
                if (self.stpxpreferredvlansmap3k.is_set or self.stpxpreferredvlansmap3k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxpreferredvlansmap3k.get_name_leafdata())
                if (self.stpxpreferredvlansmap4k.is_set or self.stpxpreferredvlansmap4k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stpxpreferredvlansmap4k.get_name_leafdata())
                if (self.vlantrunkportdot1qtunnel.is_set or self.vlantrunkportdot1qtunnel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportdot1qtunnel.get_name_leafdata())
                if (self.vlantrunkportdynamicstate.is_set or self.vlantrunkportdynamicstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportdynamicstate.get_name_leafdata())
                if (self.vlantrunkportdynamicstatus.is_set or self.vlantrunkportdynamicstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportdynamicstatus.get_name_leafdata())
                if (self.vlantrunkportencapsulationopertype.is_set or self.vlantrunkportencapsulationopertype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportencapsulationopertype.get_name_leafdata())
                if (self.vlantrunkportencapsulationtype.is_set or self.vlantrunkportencapsulationtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportencapsulationtype.get_name_leafdata())
                if (self.vlantrunkportinjoins.is_set or self.vlantrunkportinjoins.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportinjoins.get_name_leafdata())
                if (self.vlantrunkportmanagementdomain.is_set or self.vlantrunkportmanagementdomain.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportmanagementdomain.get_name_leafdata())
                if (self.vlantrunkportnativevlan.is_set or self.vlantrunkportnativevlan.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportnativevlan.get_name_leafdata())
                if (self.vlantrunkportoldadverts.is_set or self.vlantrunkportoldadverts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportoldadverts.get_name_leafdata())
                if (self.vlantrunkportoutjoins.is_set or self.vlantrunkportoutjoins.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportoutjoins.get_name_leafdata())
                if (self.vlantrunkportrowstatus.is_set or self.vlantrunkportrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportrowstatus.get_name_leafdata())
                if (self.vlantrunkportvlansactivefirst2k.is_set or self.vlantrunkportvlansactivefirst2k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportvlansactivefirst2k.get_name_leafdata())
                if (self.vlantrunkportvlansactivesecond2k.is_set or self.vlantrunkportvlansactivesecond2k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportvlansactivesecond2k.get_name_leafdata())
                if (self.vlantrunkportvlansenabled.is_set or self.vlantrunkportvlansenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportvlansenabled.get_name_leafdata())
                if (self.vlantrunkportvlansenabled2k.is_set or self.vlantrunkportvlansenabled2k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportvlansenabled2k.get_name_leafdata())
                if (self.vlantrunkportvlansenabled3k.is_set or self.vlantrunkportvlansenabled3k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportvlansenabled3k.get_name_leafdata())
                if (self.vlantrunkportvlansenabled4k.is_set or self.vlantrunkportvlansenabled4k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportvlansenabled4k.get_name_leafdata())
                if (self.vlantrunkportvlanspruningeligible.is_set or self.vlantrunkportvlanspruningeligible.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportvlanspruningeligible.get_name_leafdata())
                if (self.vlantrunkportvlansrcvjoined.is_set or self.vlantrunkportvlansrcvjoined.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportvlansrcvjoined.get_name_leafdata())
                if (self.vlantrunkportvlansrcvjoined2k.is_set or self.vlantrunkportvlansrcvjoined2k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportvlansrcvjoined2k.get_name_leafdata())
                if (self.vlantrunkportvlansrcvjoined3k.is_set or self.vlantrunkportvlansrcvjoined3k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportvlansrcvjoined3k.get_name_leafdata())
                if (self.vlantrunkportvlansrcvjoined4k.is_set or self.vlantrunkportvlansrcvjoined4k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportvlansrcvjoined4k.get_name_leafdata())
                if (self.vlantrunkportvlansxmitjoined.is_set or self.vlantrunkportvlansxmitjoined.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportvlansxmitjoined.get_name_leafdata())
                if (self.vlantrunkportvlansxmitjoined2k.is_set or self.vlantrunkportvlansxmitjoined2k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportvlansxmitjoined2k.get_name_leafdata())
                if (self.vlantrunkportvlansxmitjoined3k.is_set or self.vlantrunkportvlansxmitjoined3k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportvlansxmitjoined3k.get_name_leafdata())
                if (self.vlantrunkportvlansxmitjoined4k.is_set or self.vlantrunkportvlansxmitjoined4k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportvlansxmitjoined4k.get_name_leafdata())
                if (self.vlantrunkportvtpenabled.is_set or self.vlantrunkportvtpenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vlantrunkportvtpenabled.get_name_leafdata())
                if (self.vtpvlanspruningeligible2k.is_set or self.vtpvlanspruningeligible2k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanspruningeligible2k.get_name_leafdata())
                if (self.vtpvlanspruningeligible3k.is_set or self.vtpvlanspruningeligible3k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanspruningeligible3k.get_name_leafdata())
                if (self.vtpvlanspruningeligible4k.is_set or self.vtpvlanspruningeligible4k.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpvlanspruningeligible4k.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "vlanTrunkPortIfIndex" or name == "stpxPreferredMISTPInstancesMap" or name == "stpxPreferredMSTInstancesMap" or name == "stpxPreferredVlansMap" or name == "stpxPreferredVlansMap2k" or name == "stpxPreferredVlansMap3k" or name == "stpxPreferredVlansMap4k" or name == "vlanTrunkPortDot1qTunnel" or name == "vlanTrunkPortDynamicState" or name == "vlanTrunkPortDynamicStatus" or name == "vlanTrunkPortEncapsulationOperType" or name == "vlanTrunkPortEncapsulationType" or name == "vlanTrunkPortInJoins" or name == "vlanTrunkPortManagementDomain" or name == "vlanTrunkPortNativeVlan" or name == "vlanTrunkPortOldAdverts" or name == "vlanTrunkPortOutJoins" or name == "vlanTrunkPortRowStatus" or name == "vlanTrunkPortVlansActiveFirst2k" or name == "vlanTrunkPortVlansActiveSecond2k" or name == "vlanTrunkPortVlansEnabled" or name == "vlanTrunkPortVlansEnabled2k" or name == "vlanTrunkPortVlansEnabled3k" or name == "vlanTrunkPortVlansEnabled4k" or name == "vlanTrunkPortVlansPruningEligible" or name == "vlanTrunkPortVlansRcvJoined" or name == "vlanTrunkPortVlansRcvJoined2k" or name == "vlanTrunkPortVlansRcvJoined3k" or name == "vlanTrunkPortVlansRcvJoined4k" or name == "vlanTrunkPortVlansXmitJoined" or name == "vlanTrunkPortVlansXmitJoined2k" or name == "vlanTrunkPortVlansXmitJoined3k" or name == "vlanTrunkPortVlansXmitJoined4k" or name == "vlanTrunkPortVtpEnabled" or name == "vtpVlansPruningEligible2k" or name == "vtpVlansPruningEligible3k" or name == "vtpVlansPruningEligible4k"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vlanTrunkPortIfIndex"):
                    self.vlantrunkportifindex = value
                    self.vlantrunkportifindex.value_namespace = name_space
                    self.vlantrunkportifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxPreferredMISTPInstancesMap"):
                    self.stpxpreferredmistpinstancesmap = value
                    self.stpxpreferredmistpinstancesmap.value_namespace = name_space
                    self.stpxpreferredmistpinstancesmap.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxPreferredMSTInstancesMap"):
                    self.stpxpreferredmstinstancesmap = value
                    self.stpxpreferredmstinstancesmap.value_namespace = name_space
                    self.stpxpreferredmstinstancesmap.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxPreferredVlansMap"):
                    self.stpxpreferredvlansmap = value
                    self.stpxpreferredvlansmap.value_namespace = name_space
                    self.stpxpreferredvlansmap.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxPreferredVlansMap2k"):
                    self.stpxpreferredvlansmap2k = value
                    self.stpxpreferredvlansmap2k.value_namespace = name_space
                    self.stpxpreferredvlansmap2k.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxPreferredVlansMap3k"):
                    self.stpxpreferredvlansmap3k = value
                    self.stpxpreferredvlansmap3k.value_namespace = name_space
                    self.stpxpreferredvlansmap3k.value_namespace_prefix = name_space_prefix
                if(value_path == "stpxPreferredVlansMap4k"):
                    self.stpxpreferredvlansmap4k = value
                    self.stpxpreferredvlansmap4k.value_namespace = name_space
                    self.stpxpreferredvlansmap4k.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortDot1qTunnel"):
                    self.vlantrunkportdot1qtunnel = value
                    self.vlantrunkportdot1qtunnel.value_namespace = name_space
                    self.vlantrunkportdot1qtunnel.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortDynamicState"):
                    self.vlantrunkportdynamicstate = value
                    self.vlantrunkportdynamicstate.value_namespace = name_space
                    self.vlantrunkportdynamicstate.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortDynamicStatus"):
                    self.vlantrunkportdynamicstatus = value
                    self.vlantrunkportdynamicstatus.value_namespace = name_space
                    self.vlantrunkportdynamicstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortEncapsulationOperType"):
                    self.vlantrunkportencapsulationopertype = value
                    self.vlantrunkportencapsulationopertype.value_namespace = name_space
                    self.vlantrunkportencapsulationopertype.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortEncapsulationType"):
                    self.vlantrunkportencapsulationtype = value
                    self.vlantrunkportencapsulationtype.value_namespace = name_space
                    self.vlantrunkportencapsulationtype.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortInJoins"):
                    self.vlantrunkportinjoins = value
                    self.vlantrunkportinjoins.value_namespace = name_space
                    self.vlantrunkportinjoins.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortManagementDomain"):
                    self.vlantrunkportmanagementdomain = value
                    self.vlantrunkportmanagementdomain.value_namespace = name_space
                    self.vlantrunkportmanagementdomain.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortNativeVlan"):
                    self.vlantrunkportnativevlan = value
                    self.vlantrunkportnativevlan.value_namespace = name_space
                    self.vlantrunkportnativevlan.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortOldAdverts"):
                    self.vlantrunkportoldadverts = value
                    self.vlantrunkportoldadverts.value_namespace = name_space
                    self.vlantrunkportoldadverts.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortOutJoins"):
                    self.vlantrunkportoutjoins = value
                    self.vlantrunkportoutjoins.value_namespace = name_space
                    self.vlantrunkportoutjoins.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortRowStatus"):
                    self.vlantrunkportrowstatus = value
                    self.vlantrunkportrowstatus.value_namespace = name_space
                    self.vlantrunkportrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortVlansActiveFirst2k"):
                    self.vlantrunkportvlansactivefirst2k = value
                    self.vlantrunkportvlansactivefirst2k.value_namespace = name_space
                    self.vlantrunkportvlansactivefirst2k.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortVlansActiveSecond2k"):
                    self.vlantrunkportvlansactivesecond2k = value
                    self.vlantrunkportvlansactivesecond2k.value_namespace = name_space
                    self.vlantrunkportvlansactivesecond2k.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortVlansEnabled"):
                    self.vlantrunkportvlansenabled = value
                    self.vlantrunkportvlansenabled.value_namespace = name_space
                    self.vlantrunkportvlansenabled.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortVlansEnabled2k"):
                    self.vlantrunkportvlansenabled2k = value
                    self.vlantrunkportvlansenabled2k.value_namespace = name_space
                    self.vlantrunkportvlansenabled2k.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortVlansEnabled3k"):
                    self.vlantrunkportvlansenabled3k = value
                    self.vlantrunkportvlansenabled3k.value_namespace = name_space
                    self.vlantrunkportvlansenabled3k.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortVlansEnabled4k"):
                    self.vlantrunkportvlansenabled4k = value
                    self.vlantrunkportvlansenabled4k.value_namespace = name_space
                    self.vlantrunkportvlansenabled4k.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortVlansPruningEligible"):
                    self.vlantrunkportvlanspruningeligible = value
                    self.vlantrunkportvlanspruningeligible.value_namespace = name_space
                    self.vlantrunkportvlanspruningeligible.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortVlansRcvJoined"):
                    self.vlantrunkportvlansrcvjoined = value
                    self.vlantrunkportvlansrcvjoined.value_namespace = name_space
                    self.vlantrunkportvlansrcvjoined.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortVlansRcvJoined2k"):
                    self.vlantrunkportvlansrcvjoined2k = value
                    self.vlantrunkportvlansrcvjoined2k.value_namespace = name_space
                    self.vlantrunkportvlansrcvjoined2k.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortVlansRcvJoined3k"):
                    self.vlantrunkportvlansrcvjoined3k = value
                    self.vlantrunkportvlansrcvjoined3k.value_namespace = name_space
                    self.vlantrunkportvlansrcvjoined3k.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortVlansRcvJoined4k"):
                    self.vlantrunkportvlansrcvjoined4k = value
                    self.vlantrunkportvlansrcvjoined4k.value_namespace = name_space
                    self.vlantrunkportvlansrcvjoined4k.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortVlansXmitJoined"):
                    self.vlantrunkportvlansxmitjoined = value
                    self.vlantrunkportvlansxmitjoined.value_namespace = name_space
                    self.vlantrunkportvlansxmitjoined.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortVlansXmitJoined2k"):
                    self.vlantrunkportvlansxmitjoined2k = value
                    self.vlantrunkportvlansxmitjoined2k.value_namespace = name_space
                    self.vlantrunkportvlansxmitjoined2k.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortVlansXmitJoined3k"):
                    self.vlantrunkportvlansxmitjoined3k = value
                    self.vlantrunkportvlansxmitjoined3k.value_namespace = name_space
                    self.vlantrunkportvlansxmitjoined3k.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortVlansXmitJoined4k"):
                    self.vlantrunkportvlansxmitjoined4k = value
                    self.vlantrunkportvlansxmitjoined4k.value_namespace = name_space
                    self.vlantrunkportvlansxmitjoined4k.value_namespace_prefix = name_space_prefix
                if(value_path == "vlanTrunkPortVtpEnabled"):
                    self.vlantrunkportvtpenabled = value
                    self.vlantrunkportvtpenabled.value_namespace = name_space
                    self.vlantrunkportvtpenabled.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlansPruningEligible2k"):
                    self.vtpvlanspruningeligible2k = value
                    self.vtpvlanspruningeligible2k.value_namespace = name_space
                    self.vtpvlanspruningeligible2k.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlansPruningEligible3k"):
                    self.vtpvlanspruningeligible3k = value
                    self.vtpvlanspruningeligible3k.value_namespace = name_space
                    self.vtpvlanspruningeligible3k.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpVlansPruningEligible4k"):
                    self.vtpvlanspruningeligible4k = value
                    self.vtpvlanspruningeligible4k.value_namespace = name_space
                    self.vtpvlanspruningeligible4k.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vlantrunkportentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vlantrunkportentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vlanTrunkPortTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vlanTrunkPortEntry"):
                for c in self.vlantrunkportentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVtpMib.Vlantrunkporttable.Vlantrunkportentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vlantrunkportentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vlanTrunkPortEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Vtpdiscovertable(Entity):
        """
        This table contains information related to the discovery
        of the VTP members in the designated management
        domain. This table is not instantiated when 
        managementDomainVersionInUse is version1(1), version2(3)
        or none(3).
        
        .. attribute:: vtpdiscoverentry
        
        	Information related to the discovery of the VTP members in one management domain
        	**type**\: list of    :py:class:`Vtpdiscoverentry <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpdiscovertable.Vtpdiscoverentry>`
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CiscoVtpMib.Vtpdiscovertable, self).__init__()

            self.yang_name = "vtpDiscoverTable"
            self.yang_parent_name = "CISCO-VTP-MIB"

            self.vtpdiscoverentry = YList(self)

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
                        super(CiscoVtpMib.Vtpdiscovertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVtpMib.Vtpdiscovertable, self).__setattr__(name, value)


        class Vtpdiscoverentry(Entity):
            """
            Information related to the discovery of the
            VTP members in one management domain.
            
            .. attribute:: managementdomainindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..255
            
            	**refers to**\:  :py:class:`managementdomainindex <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Managementdomaintable.Managementdomainentry>`
            
            .. attribute:: vtpdiscoveraction
            
            	When this object is set to discover(1), all the entries in vtpDiscoverResultTable for the corresponding management domain will be removed  and the local device will begin to discover all VTP members in the management domain. Upon the successful completion of discovery, the discovered result will be stored in the vtpDiscoverResultTable.  If vtpDiscoverStatus is inProgress(1), setting  vtpDiscoverAction to discover(1) will fail.   When this object is set to purgeResult(3),  all the entries of vtpDiscoverResultTable for  the corresponding management domain will be removed from vtpDiscoverResultTable.  When this object is set to noOperation(2), no action will be taken. When read, this object always returns noOperation(2)
            	**type**\:   :py:class:`Vtpdiscoveraction <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpdiscovertable.Vtpdiscoverentry.Vtpdiscoveraction>`
            
            .. attribute:: vtpdiscoverstatus
            
            	The current status of VTP discovery.  inProgress \- a discovery is in progress;  succeeded \- the discovery was completed successfully             (this value is also used when              no discover has been invoked since the             last time the local system restarted);  resourceUnavailable \- the discovery failed because             the required allocation of a resource is             presently unavailable.  someOtherError \- 'the discovery failed due to a             reason no listed
            	**type**\:   :py:class:`Vtpdiscoverstatus <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpdiscovertable.Vtpdiscoverentry.Vtpdiscoverstatus>`
            
            .. attribute:: vtplastdiscovertime
            
            	The value of sysUpTime at which the last discovery was completed.  A value of zero indicates that no discovery has been invoked since last time the local system restarted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-VTP-MIB'
            _revision = '2013-10-14'

            def __init__(self):
                super(CiscoVtpMib.Vtpdiscovertable.Vtpdiscoverentry, self).__init__()

                self.yang_name = "vtpDiscoverEntry"
                self.yang_parent_name = "vtpDiscoverTable"

                self.managementdomainindex = YLeaf(YType.str, "managementDomainIndex")

                self.vtpdiscoveraction = YLeaf(YType.enumeration, "vtpDiscoverAction")

                self.vtpdiscoverstatus = YLeaf(YType.enumeration, "vtpDiscoverStatus")

                self.vtplastdiscovertime = YLeaf(YType.uint32, "vtpLastDiscoverTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("managementdomainindex",
                                "vtpdiscoveraction",
                                "vtpdiscoverstatus",
                                "vtplastdiscovertime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVtpMib.Vtpdiscovertable.Vtpdiscoverentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVtpMib.Vtpdiscovertable.Vtpdiscoverentry, self).__setattr__(name, value)

            class Vtpdiscoveraction(Enum):
                """
                Vtpdiscoveraction

                When this object is set to discover(1), all the

                entries in vtpDiscoverResultTable for the

                corresponding management domain will be removed 

                and the local device will begin to discover all

                VTP members in the management domain. Upon the

                successful completion of discovery, the discovered

                result will be stored in the vtpDiscoverResultTable.

                If vtpDiscoverStatus is inProgress(1), setting 

                vtpDiscoverAction to discover(1) will fail. 

                When this object is set to purgeResult(3), 

                all the entries of vtpDiscoverResultTable for 

                the corresponding management domain will be

                removed from vtpDiscoverResultTable.

                When this object is set to noOperation(2), no

                action will be taken. When read, this object

                always returns noOperation(2).

                .. data:: discover = 1

                .. data:: noOperation = 2

                .. data:: purgeResult = 3

                """

                discover = Enum.YLeaf(1, "discover")

                noOperation = Enum.YLeaf(2, "noOperation")

                purgeResult = Enum.YLeaf(3, "purgeResult")


            class Vtpdiscoverstatus(Enum):
                """
                Vtpdiscoverstatus

                The current status of VTP discovery.

                inProgress \- a discovery is in progress;

                succeeded \- the discovery was completed successfully

                            (this value is also used when 

                            no discover has been invoked since the

                            last time the local system restarted);

                resourceUnavailable \- the discovery failed because

                            the required allocation of a resource is

                            presently unavailable.

                someOtherError \- 'the discovery failed due to a

                            reason no listed.

                .. data:: inProgress = 1

                .. data:: succeeded = 2

                .. data:: resourceUnavailable = 3

                .. data:: someOtherError = 4

                """

                inProgress = Enum.YLeaf(1, "inProgress")

                succeeded = Enum.YLeaf(2, "succeeded")

                resourceUnavailable = Enum.YLeaf(3, "resourceUnavailable")

                someOtherError = Enum.YLeaf(4, "someOtherError")


            def has_data(self):
                return (
                    self.managementdomainindex.is_set or
                    self.vtpdiscoveraction.is_set or
                    self.vtpdiscoverstatus.is_set or
                    self.vtplastdiscovertime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.managementdomainindex.yfilter != YFilter.not_set or
                    self.vtpdiscoveraction.yfilter != YFilter.not_set or
                    self.vtpdiscoverstatus.yfilter != YFilter.not_set or
                    self.vtplastdiscovertime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vtpDiscoverEntry" + "[managementDomainIndex='" + self.managementdomainindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/vtpDiscoverTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.managementdomainindex.is_set or self.managementdomainindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainindex.get_name_leafdata())
                if (self.vtpdiscoveraction.is_set or self.vtpdiscoveraction.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpdiscoveraction.get_name_leafdata())
                if (self.vtpdiscoverstatus.is_set or self.vtpdiscoverstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpdiscoverstatus.get_name_leafdata())
                if (self.vtplastdiscovertime.is_set or self.vtplastdiscovertime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtplastdiscovertime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "managementDomainIndex" or name == "vtpDiscoverAction" or name == "vtpDiscoverStatus" or name == "vtpLastDiscoverTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "managementDomainIndex"):
                    self.managementdomainindex = value
                    self.managementdomainindex.value_namespace = name_space
                    self.managementdomainindex.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpDiscoverAction"):
                    self.vtpdiscoveraction = value
                    self.vtpdiscoveraction.value_namespace = name_space
                    self.vtpdiscoveraction.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpDiscoverStatus"):
                    self.vtpdiscoverstatus = value
                    self.vtpdiscoverstatus.value_namespace = name_space
                    self.vtpdiscoverstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpLastDiscoverTime"):
                    self.vtplastdiscovertime = value
                    self.vtplastdiscovertime.value_namespace = name_space
                    self.vtplastdiscovertime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vtpdiscoverentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vtpdiscoverentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vtpDiscoverTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vtpDiscoverEntry"):
                for c in self.vtpdiscoverentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVtpMib.Vtpdiscovertable.Vtpdiscoverentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vtpdiscoverentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vtpDiscoverEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Vtpdiscoverresulttable(Entity):
        """
        The table containing information of discovered VTP members
        in the management domain in which the local system is
        participating. This table is not instantiated when 
        managementDomainVersionInUse is version1(1), version2(2) or
        none(3).
        
        .. attribute:: vtpdiscoverresultentry
        
        	A conceptual row is created for each VTP member which is found through successful discovery
        	**type**\: list of    :py:class:`Vtpdiscoverresultentry <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpdiscoverresulttable.Vtpdiscoverresultentry>`
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CiscoVtpMib.Vtpdiscoverresulttable, self).__init__()

            self.yang_name = "vtpDiscoverResultTable"
            self.yang_parent_name = "CISCO-VTP-MIB"

            self.vtpdiscoverresultentry = YList(self)

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
                        super(CiscoVtpMib.Vtpdiscoverresulttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVtpMib.Vtpdiscoverresulttable, self).__setattr__(name, value)


        class Vtpdiscoverresultentry(Entity):
            """
            A conceptual row is created for each VTP member which
            is found through successful discovery.
            
            .. attribute:: managementdomainindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..255
            
            	**refers to**\:  :py:class:`managementdomainindex <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Managementdomaintable.Managementdomainentry>`
            
            .. attribute:: vtpdiscoverresultindex  <key>
            
            	A value assigned by the system which identifies a VTP member and the associated database in the  management domain
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpdiscoverresultconflicting
            
            	Indicates whether this VTP member contains conflicting information.  true(1) indicates that this member has conflicting  information of the database type in the management domain.  false(2) indicates that there is no conflicting information of the database type in the management domain
            	**type**\:  bool
            
            .. attribute:: vtpdiscoverresultdatabasename
            
            	The database name associated with the discovered VTP member
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: vtpdiscoverresultdeviceid
            
            	The unique identifier of the device for this VTP member
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: vtpdiscoverresultprimaryserver
            
            	The unique identifier of the primary server for this VTP member and the associated database type.  There are two different VTP servers, the primary server and the secondary server.  When a local device is configured as a server for a certain database type, it becomes secondary server by default.  Primary server is an operational role under which a server can initiate or change the VTP configuration of the database type.  If this VTP member itself is the primary server, the    value of this object is the same as the value of  vtpDiscoverResultDeviceId of the instance
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: vtpdiscoverresultrevnumber
            
            	The current configuration revision number as known by the VTP member. When the database type is unknown for the VTP member, this value is 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpdiscoverresultsystemname
            
            	sysName of the VTP member
            	**type**\:  str
            
            	**length:** 0..64
            
            

            """

            _prefix = 'CISCO-VTP-MIB'
            _revision = '2013-10-14'

            def __init__(self):
                super(CiscoVtpMib.Vtpdiscoverresulttable.Vtpdiscoverresultentry, self).__init__()

                self.yang_name = "vtpDiscoverResultEntry"
                self.yang_parent_name = "vtpDiscoverResultTable"

                self.managementdomainindex = YLeaf(YType.str, "managementDomainIndex")

                self.vtpdiscoverresultindex = YLeaf(YType.uint32, "vtpDiscoverResultIndex")

                self.vtpdiscoverresultconflicting = YLeaf(YType.boolean, "vtpDiscoverResultConflicting")

                self.vtpdiscoverresultdatabasename = YLeaf(YType.str, "vtpDiscoverResultDatabaseName")

                self.vtpdiscoverresultdeviceid = YLeaf(YType.str, "vtpDiscoverResultDeviceId")

                self.vtpdiscoverresultprimaryserver = YLeaf(YType.str, "vtpDiscoverResultPrimaryServer")

                self.vtpdiscoverresultrevnumber = YLeaf(YType.uint32, "vtpDiscoverResultRevNumber")

                self.vtpdiscoverresultsystemname = YLeaf(YType.str, "vtpDiscoverResultSystemName")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("managementdomainindex",
                                "vtpdiscoverresultindex",
                                "vtpdiscoverresultconflicting",
                                "vtpdiscoverresultdatabasename",
                                "vtpdiscoverresultdeviceid",
                                "vtpdiscoverresultprimaryserver",
                                "vtpdiscoverresultrevnumber",
                                "vtpdiscoverresultsystemname") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVtpMib.Vtpdiscoverresulttable.Vtpdiscoverresultentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVtpMib.Vtpdiscoverresulttable.Vtpdiscoverresultentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.managementdomainindex.is_set or
                    self.vtpdiscoverresultindex.is_set or
                    self.vtpdiscoverresultconflicting.is_set or
                    self.vtpdiscoverresultdatabasename.is_set or
                    self.vtpdiscoverresultdeviceid.is_set or
                    self.vtpdiscoverresultprimaryserver.is_set or
                    self.vtpdiscoverresultrevnumber.is_set or
                    self.vtpdiscoverresultsystemname.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.managementdomainindex.yfilter != YFilter.not_set or
                    self.vtpdiscoverresultindex.yfilter != YFilter.not_set or
                    self.vtpdiscoverresultconflicting.yfilter != YFilter.not_set or
                    self.vtpdiscoverresultdatabasename.yfilter != YFilter.not_set or
                    self.vtpdiscoverresultdeviceid.yfilter != YFilter.not_set or
                    self.vtpdiscoverresultprimaryserver.yfilter != YFilter.not_set or
                    self.vtpdiscoverresultrevnumber.yfilter != YFilter.not_set or
                    self.vtpdiscoverresultsystemname.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vtpDiscoverResultEntry" + "[managementDomainIndex='" + self.managementdomainindex.get() + "']" + "[vtpDiscoverResultIndex='" + self.vtpdiscoverresultindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/vtpDiscoverResultTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.managementdomainindex.is_set or self.managementdomainindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainindex.get_name_leafdata())
                if (self.vtpdiscoverresultindex.is_set or self.vtpdiscoverresultindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpdiscoverresultindex.get_name_leafdata())
                if (self.vtpdiscoverresultconflicting.is_set or self.vtpdiscoverresultconflicting.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpdiscoverresultconflicting.get_name_leafdata())
                if (self.vtpdiscoverresultdatabasename.is_set or self.vtpdiscoverresultdatabasename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpdiscoverresultdatabasename.get_name_leafdata())
                if (self.vtpdiscoverresultdeviceid.is_set or self.vtpdiscoverresultdeviceid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpdiscoverresultdeviceid.get_name_leafdata())
                if (self.vtpdiscoverresultprimaryserver.is_set or self.vtpdiscoverresultprimaryserver.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpdiscoverresultprimaryserver.get_name_leafdata())
                if (self.vtpdiscoverresultrevnumber.is_set or self.vtpdiscoverresultrevnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpdiscoverresultrevnumber.get_name_leafdata())
                if (self.vtpdiscoverresultsystemname.is_set or self.vtpdiscoverresultsystemname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpdiscoverresultsystemname.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "managementDomainIndex" or name == "vtpDiscoverResultIndex" or name == "vtpDiscoverResultConflicting" or name == "vtpDiscoverResultDatabaseName" or name == "vtpDiscoverResultDeviceId" or name == "vtpDiscoverResultPrimaryServer" or name == "vtpDiscoverResultRevNumber" or name == "vtpDiscoverResultSystemName"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "managementDomainIndex"):
                    self.managementdomainindex = value
                    self.managementdomainindex.value_namespace = name_space
                    self.managementdomainindex.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpDiscoverResultIndex"):
                    self.vtpdiscoverresultindex = value
                    self.vtpdiscoverresultindex.value_namespace = name_space
                    self.vtpdiscoverresultindex.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpDiscoverResultConflicting"):
                    self.vtpdiscoverresultconflicting = value
                    self.vtpdiscoverresultconflicting.value_namespace = name_space
                    self.vtpdiscoverresultconflicting.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpDiscoverResultDatabaseName"):
                    self.vtpdiscoverresultdatabasename = value
                    self.vtpdiscoverresultdatabasename.value_namespace = name_space
                    self.vtpdiscoverresultdatabasename.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpDiscoverResultDeviceId"):
                    self.vtpdiscoverresultdeviceid = value
                    self.vtpdiscoverresultdeviceid.value_namespace = name_space
                    self.vtpdiscoverresultdeviceid.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpDiscoverResultPrimaryServer"):
                    self.vtpdiscoverresultprimaryserver = value
                    self.vtpdiscoverresultprimaryserver.value_namespace = name_space
                    self.vtpdiscoverresultprimaryserver.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpDiscoverResultRevNumber"):
                    self.vtpdiscoverresultrevnumber = value
                    self.vtpdiscoverresultrevnumber.value_namespace = name_space
                    self.vtpdiscoverresultrevnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpDiscoverResultSystemName"):
                    self.vtpdiscoverresultsystemname = value
                    self.vtpdiscoverresultsystemname.value_namespace = name_space
                    self.vtpdiscoverresultsystemname.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vtpdiscoverresultentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vtpdiscoverresultentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vtpDiscoverResultTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vtpDiscoverResultEntry"):
                for c in self.vtpdiscoverresultentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVtpMib.Vtpdiscoverresulttable.Vtpdiscoverresultentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vtpdiscoverresultentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vtpDiscoverResultEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Vtpdatabasetable(Entity):
        """
        This table contains information of the VTP
        databases. It is not instantiated when
        managementDomainVersionInUse is version1(1), 
        version2(3) or none(3).
        
        .. attribute:: vtpdatabaseentry
        
        	Information about the status of the VTP database in the domain.  Each VTP database type known to the local device type has an entry in this table. An entry is also created for unknown database which is notified through VTP advertisements from other VTP servers
        	**type**\: list of    :py:class:`Vtpdatabaseentry <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpdatabasetable.Vtpdatabaseentry>`
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CiscoVtpMib.Vtpdatabasetable, self).__init__()

            self.yang_name = "vtpDatabaseTable"
            self.yang_parent_name = "CISCO-VTP-MIB"

            self.vtpdatabaseentry = YList(self)

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
                        super(CiscoVtpMib.Vtpdatabasetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVtpMib.Vtpdatabasetable, self).__setattr__(name, value)


        class Vtpdatabaseentry(Entity):
            """
            Information about the status of the VTP database
            in the domain.  Each VTP database type known to the
            local device type has an entry in this table.
            An entry is also created for unknown database which is
            notified through VTP advertisements from other VTP
            servers.
            
            .. attribute:: managementdomainindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..255
            
            	**refers to**\:  :py:class:`managementdomainindex <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Managementdomaintable.Managementdomainentry>`
            
            .. attribute:: vtpdatabaseindex  <key>
            
            	A value assigned by the system which uniquely identifies a VTP database in the local system
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpdatabaselocalmode
            
            	The local VTP mode for a particular database type in this administrative domain.  \- 'client' indicates that the local system is acting   as a VTP client of the database type.  \- 'server' indicates that the local system is acting   as a VTP server of the database type.  \- 'transparent' indicates that the local system does   not generate or listen to VTP messages of this    database type, but forwards   messages. This mode can also be set by the device   itself when the size of database is too large for it   to hold in DRAM.  \- 'off' indicates that the local system does not   generate, listen to or forward any VTP messages   of this database type.  The default mode is 'client' for the database type  known to the local device and 'transparent' for the unknown database type
            	**type**\:   :py:class:`Vtpdatabaselocalmode <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpdatabasetable.Vtpdatabaseentry.Vtpdatabaselocalmode>`
            
            .. attribute:: vtpdatabasename
            
            	The name of the database
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: vtpdatabaseprimaryserver
            
            	There are two kinds of VTP version 3 servers for a certain database type \- the primary server and the secondary server. When a local device is configured as a server for a certain database type, it becomes secondary server by default. Primary server is an operational role under which a server can initiate or change the VTP configuration of the database type.  A true(1) value indicates that the local device is the  primary server of the database type in the management domain. A false(2) value indicates that the local device is not the primary server, or the database type is unknown to the local device
            	**type**\:  bool
            
            .. attribute:: vtpdatabaseprimaryserverid
            
            	The unique identifier of the primary server in the management domain for the database type.   If no primary server is discovered for the database type, the object has a value of zero length string
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: vtpdatabaserevnumber
            
            	The current configuration revision number as known by the local device for this VTP 3 database type in the management domain.  This value is updated (if necessary) whenever a  VTP advertisement for the database type is received  or generated. When the database type is unknown to the  local device or no VTP advertisement for the database type is received or generated, its value is 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpdatabasetakeoverpassword
            
            	When read, this object always returns the value of a zero\-length octet string.  In the case that the VTP password is hidden from the  configuration and the local device intends to take over the whole domain, this object must be  set to the matching password with the secret key  (vtpAuthSecretKey) in the same data packet as which  the vtpDatabaseTakeOverPrimary is in. In all the  other situations, setting a valid value to this object  has no impact on the system
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: vtpdatabasetakeoverprimary
            
            	There are two kinds of VTP version 3 servers for a certain database type \- the primary server and the secondary server. When a local device is configured as a server for a certain database type, it becomes secondary server by default. Primary server is an operational role under which a server can initiate or change the VTP configuration of the database type.  Setting this object to a true(1) value will advertise the configuration of this database type to the whole domain.  In order to successfully setting this object to true(1), the value of vtpDatabaseLocalMode must be server(2). Besides that, when the VTP password is hidden from the configuration file, the password (vtpDatabaseTakeOverPassword) which  matches  the secret key (vtpAuthSecretKey) must be provided in the same data packet.   When read, the object always returns false(2)
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-VTP-MIB'
            _revision = '2013-10-14'

            def __init__(self):
                super(CiscoVtpMib.Vtpdatabasetable.Vtpdatabaseentry, self).__init__()

                self.yang_name = "vtpDatabaseEntry"
                self.yang_parent_name = "vtpDatabaseTable"

                self.managementdomainindex = YLeaf(YType.str, "managementDomainIndex")

                self.vtpdatabaseindex = YLeaf(YType.uint32, "vtpDatabaseIndex")

                self.vtpdatabaselocalmode = YLeaf(YType.enumeration, "vtpDatabaseLocalMode")

                self.vtpdatabasename = YLeaf(YType.str, "vtpDatabaseName")

                self.vtpdatabaseprimaryserver = YLeaf(YType.boolean, "vtpDatabasePrimaryServer")

                self.vtpdatabaseprimaryserverid = YLeaf(YType.str, "vtpDatabasePrimaryServerId")

                self.vtpdatabaserevnumber = YLeaf(YType.uint32, "vtpDatabaseRevNumber")

                self.vtpdatabasetakeoverpassword = YLeaf(YType.str, "vtpDatabaseTakeOverPassword")

                self.vtpdatabasetakeoverprimary = YLeaf(YType.boolean, "vtpDatabaseTakeOverPrimary")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("managementdomainindex",
                                "vtpdatabaseindex",
                                "vtpdatabaselocalmode",
                                "vtpdatabasename",
                                "vtpdatabaseprimaryserver",
                                "vtpdatabaseprimaryserverid",
                                "vtpdatabaserevnumber",
                                "vtpdatabasetakeoverpassword",
                                "vtpdatabasetakeoverprimary") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVtpMib.Vtpdatabasetable.Vtpdatabaseentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVtpMib.Vtpdatabasetable.Vtpdatabaseentry, self).__setattr__(name, value)

            class Vtpdatabaselocalmode(Enum):
                """
                Vtpdatabaselocalmode

                The local VTP mode for a particular database type

                in this administrative domain.

                \- 'client' indicates that the local system is acting

                  as a VTP client of the database type.

                \- 'server' indicates that the local system is acting

                  as a VTP server of the database type.

                \- 'transparent' indicates that the local system does

                  not generate or listen to VTP messages of this 

                  database type, but forwards

                  messages. This mode can also be set by the device

                  itself when the size of database is too large for it

                  to hold in DRAM.

                \- 'off' indicates that the local system does not

                  generate, listen to or forward any VTP messages

                  of this database type.

                The default mode is 'client' for the database type 

                known to the local device and 'transparent' for the

                unknown database type.

                .. data:: client = 1

                .. data:: server = 2

                .. data:: transparent = 3

                .. data:: off = 4

                """

                client = Enum.YLeaf(1, "client")

                server = Enum.YLeaf(2, "server")

                transparent = Enum.YLeaf(3, "transparent")

                off = Enum.YLeaf(4, "off")


            def has_data(self):
                return (
                    self.managementdomainindex.is_set or
                    self.vtpdatabaseindex.is_set or
                    self.vtpdatabaselocalmode.is_set or
                    self.vtpdatabasename.is_set or
                    self.vtpdatabaseprimaryserver.is_set or
                    self.vtpdatabaseprimaryserverid.is_set or
                    self.vtpdatabaserevnumber.is_set or
                    self.vtpdatabasetakeoverpassword.is_set or
                    self.vtpdatabasetakeoverprimary.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.managementdomainindex.yfilter != YFilter.not_set or
                    self.vtpdatabaseindex.yfilter != YFilter.not_set or
                    self.vtpdatabaselocalmode.yfilter != YFilter.not_set or
                    self.vtpdatabasename.yfilter != YFilter.not_set or
                    self.vtpdatabaseprimaryserver.yfilter != YFilter.not_set or
                    self.vtpdatabaseprimaryserverid.yfilter != YFilter.not_set or
                    self.vtpdatabaserevnumber.yfilter != YFilter.not_set or
                    self.vtpdatabasetakeoverpassword.yfilter != YFilter.not_set or
                    self.vtpdatabasetakeoverprimary.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vtpDatabaseEntry" + "[managementDomainIndex='" + self.managementdomainindex.get() + "']" + "[vtpDatabaseIndex='" + self.vtpdatabaseindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/vtpDatabaseTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.managementdomainindex.is_set or self.managementdomainindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainindex.get_name_leafdata())
                if (self.vtpdatabaseindex.is_set or self.vtpdatabaseindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpdatabaseindex.get_name_leafdata())
                if (self.vtpdatabaselocalmode.is_set or self.vtpdatabaselocalmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpdatabaselocalmode.get_name_leafdata())
                if (self.vtpdatabasename.is_set or self.vtpdatabasename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpdatabasename.get_name_leafdata())
                if (self.vtpdatabaseprimaryserver.is_set or self.vtpdatabaseprimaryserver.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpdatabaseprimaryserver.get_name_leafdata())
                if (self.vtpdatabaseprimaryserverid.is_set or self.vtpdatabaseprimaryserverid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpdatabaseprimaryserverid.get_name_leafdata())
                if (self.vtpdatabaserevnumber.is_set or self.vtpdatabaserevnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpdatabaserevnumber.get_name_leafdata())
                if (self.vtpdatabasetakeoverpassword.is_set or self.vtpdatabasetakeoverpassword.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpdatabasetakeoverpassword.get_name_leafdata())
                if (self.vtpdatabasetakeoverprimary.is_set or self.vtpdatabasetakeoverprimary.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpdatabasetakeoverprimary.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "managementDomainIndex" or name == "vtpDatabaseIndex" or name == "vtpDatabaseLocalMode" or name == "vtpDatabaseName" or name == "vtpDatabasePrimaryServer" or name == "vtpDatabasePrimaryServerId" or name == "vtpDatabaseRevNumber" or name == "vtpDatabaseTakeOverPassword" or name == "vtpDatabaseTakeOverPrimary"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "managementDomainIndex"):
                    self.managementdomainindex = value
                    self.managementdomainindex.value_namespace = name_space
                    self.managementdomainindex.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpDatabaseIndex"):
                    self.vtpdatabaseindex = value
                    self.vtpdatabaseindex.value_namespace = name_space
                    self.vtpdatabaseindex.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpDatabaseLocalMode"):
                    self.vtpdatabaselocalmode = value
                    self.vtpdatabaselocalmode.value_namespace = name_space
                    self.vtpdatabaselocalmode.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpDatabaseName"):
                    self.vtpdatabasename = value
                    self.vtpdatabasename.value_namespace = name_space
                    self.vtpdatabasename.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpDatabasePrimaryServer"):
                    self.vtpdatabaseprimaryserver = value
                    self.vtpdatabaseprimaryserver.value_namespace = name_space
                    self.vtpdatabaseprimaryserver.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpDatabasePrimaryServerId"):
                    self.vtpdatabaseprimaryserverid = value
                    self.vtpdatabaseprimaryserverid.value_namespace = name_space
                    self.vtpdatabaseprimaryserverid.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpDatabaseRevNumber"):
                    self.vtpdatabaserevnumber = value
                    self.vtpdatabaserevnumber.value_namespace = name_space
                    self.vtpdatabaserevnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpDatabaseTakeOverPassword"):
                    self.vtpdatabasetakeoverpassword = value
                    self.vtpdatabasetakeoverpassword.value_namespace = name_space
                    self.vtpdatabasetakeoverpassword.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpDatabaseTakeOverPrimary"):
                    self.vtpdatabasetakeoverprimary = value
                    self.vtpdatabasetakeoverprimary.value_namespace = name_space
                    self.vtpdatabasetakeoverprimary.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vtpdatabaseentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vtpdatabaseentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vtpDatabaseTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vtpDatabaseEntry"):
                for c in self.vtpdatabaseentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVtpMib.Vtpdatabasetable.Vtpdatabaseentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vtpdatabaseentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vtpDatabaseEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Vtpauthenticationtable(Entity):
        """
        The table contains the authentication information of VTP
        in which the local system participates.
        
        The security mechanism of VTP relies on a secret key
        that is used to alter the MD5 digest of the packets
        transmitted on the wire.  The secret value is
        created from a password that may be saved in plain text
        in the configuration or hidden from the configuration.
        
        The device creating or modifying the VTP configuration
        signs it using the MD5 digest generated from the secret
        key before advertising it. Other devices in the domain
        receive this configuration use the same secret key
        to accept it if correctly signed or drop it otherwise.
        
        The user has the option to hide the password from the
        configuration. Once the password is hidden, the secret
        key generated from the password is shown in the 
        configuration instead, and there is no other way to 
        show the password in plain text again but clearing 
        it or resetting it. 
        
        In an un\-trusted area, the password on a device can 
        be configured without being unveiled. After that,
        it has to be provided again by setting the same 
        value to vtpDatabaseTakeOverPassword if the user 
        wants to take over the whole VTP management domain
        of the database type.
        
        When managementDomainVersionInUse is version3(4), the 
        authentication mechanism is common to all VTP
        database type.
        
        .. attribute:: vtpauthentry
        
        	Information about the status of the VTP authentication information in one domain
        	**type**\: list of    :py:class:`Vtpauthentry <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpauthenticationtable.Vtpauthentry>`
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CiscoVtpMib.Vtpauthenticationtable, self).__init__()

            self.yang_name = "vtpAuthenticationTable"
            self.yang_parent_name = "CISCO-VTP-MIB"

            self.vtpauthentry = YList(self)

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
                        super(CiscoVtpMib.Vtpauthenticationtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVtpMib.Vtpauthenticationtable, self).__setattr__(name, value)


        class Vtpauthentry(Entity):
            """
            Information about the status of the VTP
            authentication information in one domain.
            
            .. attribute:: managementdomainindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..255
            
            	**refers to**\:  :py:class:`managementdomainindex <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Managementdomaintable.Managementdomainentry>`
            
            .. attribute:: vtpauthpassword
            
            	By default, this object has a value of a zero\-length character string and is considered to be not configured.  The device uses the password to generate the  secret key. It can be stored in the configuration in  plain text or hidden from the configuration. If a VTP  server intends to modify the database's configuration in the domain but the password was hidden from the configuration, the same password (vtpDatabaseTakeOverPassword) as the hidden one has to be provided.  When this object is set alone, vtpAuthPasswordType is set to plaintext(1) automatically by the system. Setting this object to a zero length character string resets the password to its default value and the password is considered as not configured.  This object is not allowed to be set at the same time when  vtpAuthSecretKey is set.  When the vtpAuthPasswordType is hidden(2), this object  will return a zero\-length character string when read
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: vtpauthpasswordtype
            
            	By default this object has the value as plaintext(1) and the VTP password is stored in the configuration file in plain text.  Setting this object to hidden(2) will hide the password from the configuration.  Once this object is set to hidden(2), it cannot be set to plaintext(1) alone. However, it may be set to plaintext(1) at the same time the password is set
            	**type**\:   :py:class:`Vtpauthpasswordtype <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CiscoVtpMib.Vtpauthenticationtable.Vtpauthentry.Vtpauthpasswordtype>`
            
            .. attribute:: vtpauthsecretkey
            
            	The device creating or modifying the VTP configuration signs it using the MD5 digest generated from the secret key before advertising it. Other devices in the domain receiving this configuration use the same secret key to accept it if it was correctly signed or drop it  otherwise.  By default, the object has the value as a zero\-length string and this value is read only. It is set  to this value automatically when the password  (vtpAuthPassword) is set to a zero\-length octet string.  The secret key can be either generated using the password or configured by the user. Once the secret key is configured by the user, it is stored as a hexadecimal string in the device's configuration and the password is considered to be the secret key's matching password and hidden from the configuration automatically.  This object is not allowed to be set at the same time when vtpAuthPassword is set.  The secret key is overwritten by a newly generated secret key when the password is re\-configured
            	**type**\:  str
            
            	**length:** 0 \| 16
            
            

            """

            _prefix = 'CISCO-VTP-MIB'
            _revision = '2013-10-14'

            def __init__(self):
                super(CiscoVtpMib.Vtpauthenticationtable.Vtpauthentry, self).__init__()

                self.yang_name = "vtpAuthEntry"
                self.yang_parent_name = "vtpAuthenticationTable"

                self.managementdomainindex = YLeaf(YType.str, "managementDomainIndex")

                self.vtpauthpassword = YLeaf(YType.str, "vtpAuthPassword")

                self.vtpauthpasswordtype = YLeaf(YType.enumeration, "vtpAuthPasswordType")

                self.vtpauthsecretkey = YLeaf(YType.str, "vtpAuthSecretKey")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("managementdomainindex",
                                "vtpauthpassword",
                                "vtpauthpasswordtype",
                                "vtpauthsecretkey") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVtpMib.Vtpauthenticationtable.Vtpauthentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVtpMib.Vtpauthenticationtable.Vtpauthentry, self).__setattr__(name, value)

            class Vtpauthpasswordtype(Enum):
                """
                Vtpauthpasswordtype

                By default this object has the value as plaintext(1)

                and the VTP password is stored in the configuration

                file in plain text.

                Setting this object to hidden(2) will hide the

                password from the configuration.

                Once this object is set to hidden(2), it cannot

                be set to plaintext(1) alone. However, it may

                be set to plaintext(1) at the same time the

                password is set.

                .. data:: plaintext = 1

                .. data:: hidden = 2

                """

                plaintext = Enum.YLeaf(1, "plaintext")

                hidden = Enum.YLeaf(2, "hidden")


            def has_data(self):
                return (
                    self.managementdomainindex.is_set or
                    self.vtpauthpassword.is_set or
                    self.vtpauthpasswordtype.is_set or
                    self.vtpauthsecretkey.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.managementdomainindex.yfilter != YFilter.not_set or
                    self.vtpauthpassword.yfilter != YFilter.not_set or
                    self.vtpauthpasswordtype.yfilter != YFilter.not_set or
                    self.vtpauthsecretkey.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vtpAuthEntry" + "[managementDomainIndex='" + self.managementdomainindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/vtpAuthenticationTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.managementdomainindex.is_set or self.managementdomainindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.managementdomainindex.get_name_leafdata())
                if (self.vtpauthpassword.is_set or self.vtpauthpassword.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpauthpassword.get_name_leafdata())
                if (self.vtpauthpasswordtype.is_set or self.vtpauthpasswordtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpauthpasswordtype.get_name_leafdata())
                if (self.vtpauthsecretkey.is_set or self.vtpauthsecretkey.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vtpauthsecretkey.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "managementDomainIndex" or name == "vtpAuthPassword" or name == "vtpAuthPasswordType" or name == "vtpAuthSecretKey"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "managementDomainIndex"):
                    self.managementdomainindex = value
                    self.managementdomainindex.value_namespace = name_space
                    self.managementdomainindex.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpAuthPassword"):
                    self.vtpauthpassword = value
                    self.vtpauthpassword.value_namespace = name_space
                    self.vtpauthpassword.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpAuthPasswordType"):
                    self.vtpauthpasswordtype = value
                    self.vtpauthpasswordtype.value_namespace = name_space
                    self.vtpauthpasswordtype.value_namespace_prefix = name_space_prefix
                if(value_path == "vtpAuthSecretKey"):
                    self.vtpauthsecretkey = value
                    self.vtpauthsecretkey.value_namespace = name_space
                    self.vtpauthsecretkey.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vtpauthentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vtpauthentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vtpAuthenticationTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vtpAuthEntry"):
                for c in self.vtpauthentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVtpMib.Vtpauthenticationtable.Vtpauthentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vtpauthentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vtpAuthEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.internalvlaninfo is not None and self.internalvlaninfo.has_data()) or
            (self.managementdomaintable is not None and self.managementdomaintable.has_data()) or
            (self.vlanstatistics is not None and self.vlanstatistics.has_data()) or
            (self.vlantrunkports is not None and self.vlantrunkports.has_data()) or
            (self.vlantrunkporttable is not None and self.vlantrunkporttable.has_data()) or
            (self.vtpauthenticationtable is not None and self.vtpauthenticationtable.has_data()) or
            (self.vtpdatabasetable is not None and self.vtpdatabasetable.has_data()) or
            (self.vtpdiscoverresulttable is not None and self.vtpdiscoverresulttable.has_data()) or
            (self.vtpdiscovertable is not None and self.vtpdiscovertable.has_data()) or
            (self.vtpinternalvlantable is not None and self.vtpinternalvlantable.has_data()) or
            (self.vtpstatus is not None and self.vtpstatus.has_data()) or
            (self.vtpvlanedittable is not None and self.vtpvlanedittable.has_data()) or
            (self.vtpvlanlocalshutdowntable is not None and self.vtpvlanlocalshutdowntable.has_data()) or
            (self.vtpvlantable is not None and self.vtpvlantable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.internalvlaninfo is not None and self.internalvlaninfo.has_operation()) or
            (self.managementdomaintable is not None and self.managementdomaintable.has_operation()) or
            (self.vlanstatistics is not None and self.vlanstatistics.has_operation()) or
            (self.vlantrunkports is not None and self.vlantrunkports.has_operation()) or
            (self.vlantrunkporttable is not None and self.vlantrunkporttable.has_operation()) or
            (self.vtpauthenticationtable is not None and self.vtpauthenticationtable.has_operation()) or
            (self.vtpdatabasetable is not None and self.vtpdatabasetable.has_operation()) or
            (self.vtpdiscoverresulttable is not None and self.vtpdiscoverresulttable.has_operation()) or
            (self.vtpdiscovertable is not None and self.vtpdiscovertable.has_operation()) or
            (self.vtpinternalvlantable is not None and self.vtpinternalvlantable.has_operation()) or
            (self.vtpstatus is not None and self.vtpstatus.has_operation()) or
            (self.vtpvlanedittable is not None and self.vtpvlanedittable.has_operation()) or
            (self.vtpvlanlocalshutdowntable is not None and self.vtpvlanlocalshutdowntable.has_operation()) or
            (self.vtpvlantable is not None and self.vtpvlantable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-VTP-MIB:CISCO-VTP-MIB" + path_buffer

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

        if (child_yang_name == "internalVlanInfo"):
            if (self.internalvlaninfo is None):
                self.internalvlaninfo = CiscoVtpMib.Internalvlaninfo()
                self.internalvlaninfo.parent = self
                self._children_name_map["internalvlaninfo"] = "internalVlanInfo"
            return self.internalvlaninfo

        if (child_yang_name == "managementDomainTable"):
            if (self.managementdomaintable is None):
                self.managementdomaintable = CiscoVtpMib.Managementdomaintable()
                self.managementdomaintable.parent = self
                self._children_name_map["managementdomaintable"] = "managementDomainTable"
            return self.managementdomaintable

        if (child_yang_name == "vlanStatistics"):
            if (self.vlanstatistics is None):
                self.vlanstatistics = CiscoVtpMib.Vlanstatistics()
                self.vlanstatistics.parent = self
                self._children_name_map["vlanstatistics"] = "vlanStatistics"
            return self.vlanstatistics

        if (child_yang_name == "vlanTrunkPorts"):
            if (self.vlantrunkports is None):
                self.vlantrunkports = CiscoVtpMib.Vlantrunkports()
                self.vlantrunkports.parent = self
                self._children_name_map["vlantrunkports"] = "vlanTrunkPorts"
            return self.vlantrunkports

        if (child_yang_name == "vlanTrunkPortTable"):
            if (self.vlantrunkporttable is None):
                self.vlantrunkporttable = CiscoVtpMib.Vlantrunkporttable()
                self.vlantrunkporttable.parent = self
                self._children_name_map["vlantrunkporttable"] = "vlanTrunkPortTable"
            return self.vlantrunkporttable

        if (child_yang_name == "vtpAuthenticationTable"):
            if (self.vtpauthenticationtable is None):
                self.vtpauthenticationtable = CiscoVtpMib.Vtpauthenticationtable()
                self.vtpauthenticationtable.parent = self
                self._children_name_map["vtpauthenticationtable"] = "vtpAuthenticationTable"
            return self.vtpauthenticationtable

        if (child_yang_name == "vtpDatabaseTable"):
            if (self.vtpdatabasetable is None):
                self.vtpdatabasetable = CiscoVtpMib.Vtpdatabasetable()
                self.vtpdatabasetable.parent = self
                self._children_name_map["vtpdatabasetable"] = "vtpDatabaseTable"
            return self.vtpdatabasetable

        if (child_yang_name == "vtpDiscoverResultTable"):
            if (self.vtpdiscoverresulttable is None):
                self.vtpdiscoverresulttable = CiscoVtpMib.Vtpdiscoverresulttable()
                self.vtpdiscoverresulttable.parent = self
                self._children_name_map["vtpdiscoverresulttable"] = "vtpDiscoverResultTable"
            return self.vtpdiscoverresulttable

        if (child_yang_name == "vtpDiscoverTable"):
            if (self.vtpdiscovertable is None):
                self.vtpdiscovertable = CiscoVtpMib.Vtpdiscovertable()
                self.vtpdiscovertable.parent = self
                self._children_name_map["vtpdiscovertable"] = "vtpDiscoverTable"
            return self.vtpdiscovertable

        if (child_yang_name == "vtpInternalVlanTable"):
            if (self.vtpinternalvlantable is None):
                self.vtpinternalvlantable = CiscoVtpMib.Vtpinternalvlantable()
                self.vtpinternalvlantable.parent = self
                self._children_name_map["vtpinternalvlantable"] = "vtpInternalVlanTable"
            return self.vtpinternalvlantable

        if (child_yang_name == "vtpStatus"):
            if (self.vtpstatus is None):
                self.vtpstatus = CiscoVtpMib.Vtpstatus()
                self.vtpstatus.parent = self
                self._children_name_map["vtpstatus"] = "vtpStatus"
            return self.vtpstatus

        if (child_yang_name == "vtpVlanEditTable"):
            if (self.vtpvlanedittable is None):
                self.vtpvlanedittable = CiscoVtpMib.Vtpvlanedittable()
                self.vtpvlanedittable.parent = self
                self._children_name_map["vtpvlanedittable"] = "vtpVlanEditTable"
            return self.vtpvlanedittable

        if (child_yang_name == "vtpVlanLocalShutdownTable"):
            if (self.vtpvlanlocalshutdowntable is None):
                self.vtpvlanlocalshutdowntable = CiscoVtpMib.Vtpvlanlocalshutdowntable()
                self.vtpvlanlocalshutdowntable.parent = self
                self._children_name_map["vtpvlanlocalshutdowntable"] = "vtpVlanLocalShutdownTable"
            return self.vtpvlanlocalshutdowntable

        if (child_yang_name == "vtpVlanTable"):
            if (self.vtpvlantable is None):
                self.vtpvlantable = CiscoVtpMib.Vtpvlantable()
                self.vtpvlantable.parent = self
                self._children_name_map["vtpvlantable"] = "vtpVlanTable"
            return self.vtpvlantable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "internalVlanInfo" or name == "managementDomainTable" or name == "vlanStatistics" or name == "vlanTrunkPorts" or name == "vlanTrunkPortTable" or name == "vtpAuthenticationTable" or name == "vtpDatabaseTable" or name == "vtpDiscoverResultTable" or name == "vtpDiscoverTable" or name == "vtpInternalVlanTable" or name == "vtpStatus" or name == "vtpVlanEditTable" or name == "vtpVlanLocalShutdownTable" or name == "vtpVlanTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoVtpMib()
        return self._top_entity


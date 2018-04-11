""" CISCO_VTP_MIB 

The MIB module for entities implementing the VTP
protocol and Vlan management.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class VlanType(Enum):
    """
    VlanType (Enum Class)

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



class CISCOVTPMIB(Entity):
    """
    
    
    .. attribute:: vtpstatus
    
    	
    	**type**\:  :py:class:`Vtpstatus <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpstatus>`
    
    .. attribute:: internalvlaninfo
    
    	
    	**type**\:  :py:class:`Internalvlaninfo <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Internalvlaninfo>`
    
    .. attribute:: vlantrunkports
    
    	
    	**type**\:  :py:class:`Vlantrunkports <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vlantrunkports>`
    
    .. attribute:: vlanstatistics
    
    	
    	**type**\:  :py:class:`Vlanstatistics <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vlanstatistics>`
    
    .. attribute:: managementdomaintable
    
    	The table containing information on the management domains in which the local system is participating.  Devices which support only one management domain will support just one row in this table, and will not let it be deleted nor let other rows be created.  Devices which support multiple management domains will allow rows to be created and deleted, but will not allow the last row to be deleted. If the device does  not support VTP, the table is read\-only
    	**type**\:  :py:class:`Managementdomaintable <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Managementdomaintable>`
    
    .. attribute:: vtpvlantable
    
    	This table contains information on the VLANs which currently exist
    	**type**\:  :py:class:`Vtpvlantable <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpvlantable>`
    
    .. attribute:: vtpinternalvlantable
    
    	A vtpInternalVlanTable entry contains information on an existing internal VLAN. It is internally created by the device for a specific application program  and hence owned by the application.   It cannot be modified or deleted by (local  or network) management
    	**type**\:  :py:class:`Vtpinternalvlantable <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpinternalvlantable>`
    
    .. attribute:: vtpvlanedittable
    
    	The table which contains the information in the Edit Buffers, one Edit Buffer per management domain.  The information for a particular management domain is initialized, by a 'copy' operation, to be the current global VLAN information for that management domain.  After initialization, editing can be performed to add VLANs, delete VLANs, or modify their global parameters.  The information as modified through editing is local to this Edit Buffer.  An apply operation using the vtpVlanEditOperation object is necessary to instanciate the modified information as the new global VLAN information for that management domain.  To use the Edit Buffer, a manager acts as follows\:  1. ensures the Edit Buffer for a management domain is empty, i.e., there are no rows in this table for this management domain.  2. issues a SNMP set operation which sets vtpVlanEditOperation to 'copy', and vtpVlanEditBufferOwner to its own identifier (e.g., its own IP address).  3. if this set operation is successful, proceeds to edit the information in the vtpVlanEditTable.  4. if and when the edited information is to be instantiated, issues a SNMP set operation which sets vtpVlanEditOperation to 'apply'.  5. issues retrieval requests to obtain the value of vtpVlanApplyStatus, until the result of the apply is determined.  6. releases the Edit Buffer by issuing a SNMP set operation which sets vtpVlanEditOperation to 'release'.  Note that the information contained in this table is not saved across agent reboots
    	**type**\:  :py:class:`Vtpvlanedittable <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpvlanedittable>`
    
    .. attribute:: vtpvlanlocalshutdowntable
    
    	Ths table contains the VLAN local shutdown information within management domain
    	**type**\:  :py:class:`Vtpvlanlocalshutdowntable <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpvlanlocalshutdowntable>`
    
    .. attribute:: vlantrunkporttable
    
    	The table containing information on the local system's VLAN trunk ports
    	**type**\:  :py:class:`Vlantrunkporttable <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vlantrunkporttable>`
    
    .. attribute:: vtpdiscovertable
    
    	This table contains information related to the discovery of the VTP members in the designated management domain. This table is not instantiated when  managementDomainVersionInUse is version1(1), version2(3) or none(3)
    	**type**\:  :py:class:`Vtpdiscovertable <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpdiscovertable>`
    
    .. attribute:: vtpdiscoverresulttable
    
    	The table containing information of discovered VTP members in the management domain in which the local system is participating. This table is not instantiated when  managementDomainVersionInUse is version1(1), version2(2) or none(3)
    	**type**\:  :py:class:`Vtpdiscoverresulttable <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpdiscoverresulttable>`
    
    .. attribute:: vtpdatabasetable
    
    	This table contains information of the VTP databases. It is not instantiated when managementDomainVersionInUse is version1(1),  version2(3) or none(3)
    	**type**\:  :py:class:`Vtpdatabasetable <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpdatabasetable>`
    
    .. attribute:: vtpauthenticationtable
    
    	The table contains the authentication information of VTP in which the local system participates.  The security mechanism of VTP relies on a secret key that is used to alter the MD5 digest of the packets transmitted on the wire.  The secret value is created from a password that may be saved in plain text in the configuration or hidden from the configuration.  The device creating or modifying the VTP configuration signs it using the MD5 digest generated from the secret key before advertising it. Other devices in the domain receive this configuration use the same secret key to accept it if correctly signed or drop it otherwise.  The user has the option to hide the password from the configuration. Once the password is hidden, the secret key generated from the password is shown in the  configuration instead, and there is no other way to  show the password in plain text again but clearing  it or resetting it.   In an un\-trusted area, the password on a device can  be configured without being unveiled. After that, it has to be provided again by setting the same  value to vtpDatabaseTakeOverPassword if the user  wants to take over the whole VTP management domain of the database type.  When managementDomainVersionInUse is version3(4), the  authentication mechanism is common to all VTP database type
    	**type**\:  :py:class:`Vtpauthenticationtable <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpauthenticationtable>`
    
    

    """

    _prefix = 'CISCO-VTP-MIB'
    _revision = '2013-10-14'

    def __init__(self):
        super(CISCOVTPMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-VTP-MIB"
        self.yang_parent_name = "CISCO-VTP-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("vtpStatus", ("vtpstatus", CISCOVTPMIB.Vtpstatus)), ("internalVlanInfo", ("internalvlaninfo", CISCOVTPMIB.Internalvlaninfo)), ("vlanTrunkPorts", ("vlantrunkports", CISCOVTPMIB.Vlantrunkports)), ("vlanStatistics", ("vlanstatistics", CISCOVTPMIB.Vlanstatistics)), ("managementDomainTable", ("managementdomaintable", CISCOVTPMIB.Managementdomaintable)), ("vtpVlanTable", ("vtpvlantable", CISCOVTPMIB.Vtpvlantable)), ("vtpInternalVlanTable", ("vtpinternalvlantable", CISCOVTPMIB.Vtpinternalvlantable)), ("vtpVlanEditTable", ("vtpvlanedittable", CISCOVTPMIB.Vtpvlanedittable)), ("vtpVlanLocalShutdownTable", ("vtpvlanlocalshutdowntable", CISCOVTPMIB.Vtpvlanlocalshutdowntable)), ("vlanTrunkPortTable", ("vlantrunkporttable", CISCOVTPMIB.Vlantrunkporttable)), ("vtpDiscoverTable", ("vtpdiscovertable", CISCOVTPMIB.Vtpdiscovertable)), ("vtpDiscoverResultTable", ("vtpdiscoverresulttable", CISCOVTPMIB.Vtpdiscoverresulttable)), ("vtpDatabaseTable", ("vtpdatabasetable", CISCOVTPMIB.Vtpdatabasetable)), ("vtpAuthenticationTable", ("vtpauthenticationtable", CISCOVTPMIB.Vtpauthenticationtable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.vtpstatus = CISCOVTPMIB.Vtpstatus()
        self.vtpstatus.parent = self
        self._children_name_map["vtpstatus"] = "vtpStatus"
        self._children_yang_names.add("vtpStatus")

        self.internalvlaninfo = CISCOVTPMIB.Internalvlaninfo()
        self.internalvlaninfo.parent = self
        self._children_name_map["internalvlaninfo"] = "internalVlanInfo"
        self._children_yang_names.add("internalVlanInfo")

        self.vlantrunkports = CISCOVTPMIB.Vlantrunkports()
        self.vlantrunkports.parent = self
        self._children_name_map["vlantrunkports"] = "vlanTrunkPorts"
        self._children_yang_names.add("vlanTrunkPorts")

        self.vlanstatistics = CISCOVTPMIB.Vlanstatistics()
        self.vlanstatistics.parent = self
        self._children_name_map["vlanstatistics"] = "vlanStatistics"
        self._children_yang_names.add("vlanStatistics")

        self.managementdomaintable = CISCOVTPMIB.Managementdomaintable()
        self.managementdomaintable.parent = self
        self._children_name_map["managementdomaintable"] = "managementDomainTable"
        self._children_yang_names.add("managementDomainTable")

        self.vtpvlantable = CISCOVTPMIB.Vtpvlantable()
        self.vtpvlantable.parent = self
        self._children_name_map["vtpvlantable"] = "vtpVlanTable"
        self._children_yang_names.add("vtpVlanTable")

        self.vtpinternalvlantable = CISCOVTPMIB.Vtpinternalvlantable()
        self.vtpinternalvlantable.parent = self
        self._children_name_map["vtpinternalvlantable"] = "vtpInternalVlanTable"
        self._children_yang_names.add("vtpInternalVlanTable")

        self.vtpvlanedittable = CISCOVTPMIB.Vtpvlanedittable()
        self.vtpvlanedittable.parent = self
        self._children_name_map["vtpvlanedittable"] = "vtpVlanEditTable"
        self._children_yang_names.add("vtpVlanEditTable")

        self.vtpvlanlocalshutdowntable = CISCOVTPMIB.Vtpvlanlocalshutdowntable()
        self.vtpvlanlocalshutdowntable.parent = self
        self._children_name_map["vtpvlanlocalshutdowntable"] = "vtpVlanLocalShutdownTable"
        self._children_yang_names.add("vtpVlanLocalShutdownTable")

        self.vlantrunkporttable = CISCOVTPMIB.Vlantrunkporttable()
        self.vlantrunkporttable.parent = self
        self._children_name_map["vlantrunkporttable"] = "vlanTrunkPortTable"
        self._children_yang_names.add("vlanTrunkPortTable")

        self.vtpdiscovertable = CISCOVTPMIB.Vtpdiscovertable()
        self.vtpdiscovertable.parent = self
        self._children_name_map["vtpdiscovertable"] = "vtpDiscoverTable"
        self._children_yang_names.add("vtpDiscoverTable")

        self.vtpdiscoverresulttable = CISCOVTPMIB.Vtpdiscoverresulttable()
        self.vtpdiscoverresulttable.parent = self
        self._children_name_map["vtpdiscoverresulttable"] = "vtpDiscoverResultTable"
        self._children_yang_names.add("vtpDiscoverResultTable")

        self.vtpdatabasetable = CISCOVTPMIB.Vtpdatabasetable()
        self.vtpdatabasetable.parent = self
        self._children_name_map["vtpdatabasetable"] = "vtpDatabaseTable"
        self._children_yang_names.add("vtpDatabaseTable")

        self.vtpauthenticationtable = CISCOVTPMIB.Vtpauthenticationtable()
        self.vtpauthenticationtable.parent = self
        self._children_name_map["vtpauthenticationtable"] = "vtpAuthenticationTable"
        self._children_yang_names.add("vtpAuthenticationTable")
        self._segment_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB"


    class Vtpstatus(Entity):
        """
        
        
        .. attribute:: vtpversion
        
        	The version of VTP in use on the local system.  A device will report its version capability and not any particular version in use on the device. If the device does not support vtp, the version is none(3)
        	**type**\:  :py:class:`Vtpversion <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpstatus.Vtpversion>`
        
        .. attribute:: vtpmaxvlanstorage
        
        	An estimate of the maximum number of VLANs about which the local system can recover complete VTP information after a reboot.  If the number of defined VLANs is greater than this value, then the system can not act as a VTP Server. For a device which has no means to calculate the estimated number, this value is \-1
        	**type**\: int
        
        	**range:** \-1..1023
        
        .. attribute:: vtpnotificationsenabled
        
        	An indication of whether the notifications/traps defined by the vtpConfigNotificationsGroup, vtpConfigNotificationsGroup2, and vtpConfigNotificationsGroup8 are enabled
        	**type**\: bool
        
        .. attribute:: vtpvlancreatednotifenabled
        
        	An indication of whether the notification should be generated when a VLAN is created.   If the value of this object is 'true' then the vtpVlanCreated notification will be generated.  If the value of this object is 'false' then the vtpVlanCreated notification will not be generated
        	**type**\: bool
        
        .. attribute:: vtpvlandeletednotifenabled
        
        	An indication of whether the notification should be generated when a VLAN is deleted.    If the value of this object is 'true' then the vtpVlanDeleted notification will be generated.  If the value of this object is 'false' then the vtpVlanDeleted notification will not be generated
        	**type**\: bool
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CISCOVTPMIB.Vtpstatus, self).__init__()

            self.yang_name = "vtpStatus"
            self.yang_parent_name = "CISCO-VTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('vtpversion', YLeaf(YType.enumeration, 'vtpVersion')),
                ('vtpmaxvlanstorage', YLeaf(YType.int32, 'vtpMaxVlanStorage')),
                ('vtpnotificationsenabled', YLeaf(YType.boolean, 'vtpNotificationsEnabled')),
                ('vtpvlancreatednotifenabled', YLeaf(YType.boolean, 'vtpVlanCreatedNotifEnabled')),
                ('vtpvlandeletednotifenabled', YLeaf(YType.boolean, 'vtpVlanDeletedNotifEnabled')),
            ])
            self.vtpversion = None
            self.vtpmaxvlanstorage = None
            self.vtpnotificationsenabled = None
            self.vtpvlancreatednotifenabled = None
            self.vtpvlandeletednotifenabled = None
            self._segment_path = lambda: "vtpStatus"
            self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVTPMIB.Vtpstatus, ['vtpversion', 'vtpmaxvlanstorage', 'vtpnotificationsenabled', 'vtpvlancreatednotifenabled', 'vtpvlandeletednotifenabled'], name, value)

        class Vtpversion(Enum):
            """
            Vtpversion (Enum Class)

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



    class Internalvlaninfo(Entity):
        """
        
        
        .. attribute:: vtpinternalvlanallocpolicy
        
        	The internal VLAN allocation policy.  'ascending'  \- internal VLANs are allocated                starting from a lowwer VLAN ID and                 upwards. 'descending' \- internal VLANs are allocated                starting from a higher VLAN ID and                downwards
        	**type**\:  :py:class:`Vtpinternalvlanallocpolicy <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Internalvlaninfo.Vtpinternalvlanallocpolicy>`
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CISCOVTPMIB.Internalvlaninfo, self).__init__()

            self.yang_name = "internalVlanInfo"
            self.yang_parent_name = "CISCO-VTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('vtpinternalvlanallocpolicy', YLeaf(YType.enumeration, 'vtpInternalVlanAllocPolicy')),
            ])
            self.vtpinternalvlanallocpolicy = None
            self._segment_path = lambda: "internalVlanInfo"
            self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVTPMIB.Internalvlaninfo, ['vtpinternalvlanallocpolicy'], name, value)

        class Vtpinternalvlanallocpolicy(Enum):
            """
            Vtpinternalvlanallocpolicy (Enum Class)

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



    class Vlantrunkports(Entity):
        """
        
        
        .. attribute:: vlantrunkportsetserialno
        
        	An advisory lock used to allow several cooperating SNMPv2 managers to coordinate their use of the SNMPv2 set operation acting upon any instance of vlanTrunkPortVlansEnabled
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: vlantrunkportsdot1qtag
        
        	An indication of whether the tagging on all VLANs including native VLAN for all 802.1q trunks is enabled.  If this object has a value of true(1) then all VLANs including native VLAN are tagged.  If the value is false(2) then all VLANs excluding native VLAN are tagged.  This object has been deprecated and is replaced by the object 'cltcDot1qAllTaggedEnabled' in the CISCO\-L2\-TUNNEL\-CONFIG\-MIB
        	**type**\: bool
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CISCOVTPMIB.Vlantrunkports, self).__init__()

            self.yang_name = "vlanTrunkPorts"
            self.yang_parent_name = "CISCO-VTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('vlantrunkportsetserialno', YLeaf(YType.int32, 'vlanTrunkPortSetSerialNo')),
                ('vlantrunkportsdot1qtag', YLeaf(YType.boolean, 'vlanTrunkPortsDot1qTag')),
            ])
            self.vlantrunkportsetserialno = None
            self.vlantrunkportsdot1qtag = None
            self._segment_path = lambda: "vlanTrunkPorts"
            self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVTPMIB.Vlantrunkports, ['vlantrunkportsetserialno', 'vlantrunkportsdot1qtag'], name, value)


    class Vlanstatistics(Entity):
        """
        
        
        .. attribute:: vlanstatsvlans
        
        	This object indicates the number of the existing manageable VLANs with VLAN indices from 1 to 1024 in the system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vlanstatsextendedvlans
        
        	This object indicates the number of the existing manageable VLANs with VLAN indices greater than 1024 in the system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vlanstatsinternalvlans
        
        	This object indicates the number of the internal VLANs existing in the system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vlanstatsfreevlans
        
        	This object indicates the number of the free or unused VLANs in the system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CISCOVTPMIB.Vlanstatistics, self).__init__()

            self.yang_name = "vlanStatistics"
            self.yang_parent_name = "CISCO-VTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('vlanstatsvlans', YLeaf(YType.uint32, 'vlanStatsVlans')),
                ('vlanstatsextendedvlans', YLeaf(YType.uint32, 'vlanStatsExtendedVlans')),
                ('vlanstatsinternalvlans', YLeaf(YType.uint32, 'vlanStatsInternalVlans')),
                ('vlanstatsfreevlans', YLeaf(YType.uint32, 'vlanStatsFreeVlans')),
            ])
            self.vlanstatsvlans = None
            self.vlanstatsextendedvlans = None
            self.vlanstatsinternalvlans = None
            self.vlanstatsfreevlans = None
            self._segment_path = lambda: "vlanStatistics"
            self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVTPMIB.Vlanstatistics, ['vlanstatsvlans', 'vlanstatsextendedvlans', 'vlanstatsinternalvlans', 'vlanstatsfreevlans'], name, value)


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
        	**type**\: list of  		 :py:class:`Managementdomainentry <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Managementdomaintable.Managementdomainentry>`
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CISCOVTPMIB.Managementdomaintable, self).__init__()

            self.yang_name = "managementDomainTable"
            self.yang_parent_name = "CISCO-VTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("managementDomainEntry", ("managementdomainentry", CISCOVTPMIB.Managementdomaintable.Managementdomainentry))])
            self._leafs = OrderedDict()

            self.managementdomainentry = YList(self)
            self._segment_path = lambda: "managementDomainTable"
            self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVTPMIB.Managementdomaintable, [], name, value)


        class Managementdomainentry(Entity):
            """
            Information about the status of one management domain.
            
            .. attribute:: managementdomainindex  (key)
            
            	An arbitrary value to uniquely identify the management domain on the local system
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: managementdomainname
            
            	The management name of a domain in which the local system is participating.  The zero\-length name corresponds to the 'no management\-domain' state which is the initial value at installation\-time if not configured otherwise.  Note that the zero\-length name does not correspond to an operational management domain, and a device does not send VTP advertisements while in the 'no management\-domain' state.  A device leaves the 'no management\-domain' state when it obtains a management\-domain name, either through configuration or through inheriting the management\-domain name from a received VTP advertisement.  When the value of an existing instance of this object is modified by network management, the local system should re\- initialize its VLAN information (for the given management domain) as if it had just been configured with a management domain name at installation time
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: managementdomainlocalmode
            
            	The local VTP mode in this management domain when managementDomainVersionInUse is version1(1) or version2(2).  If managementDomainVersionInUse is version3(4), this  object has the same value with vtpDatabaseLocalMode  of VLAN database type.  \- 'client' indicates that the local system is acting   as a VTP client.  \- 'server' indicates that the local system is acting   as a VTP server.  \- 'transparent' indicates that the local system does   not generate or listen to VTP messages, but forwards   messages. This mode can also be set by the device   itself when the amount of VLAN information is too   large for it to hold in DRAM.  \- 'off' indicates that the local system does not   generate, listen to or forward any VTP messages
            	**type**\:  :py:class:`Managementdomainlocalmode <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Managementdomaintable.Managementdomainentry.Managementdomainlocalmode>`
            
            .. attribute:: managementdomainconfigrevnumber
            
            	The current Configuration Revision Number as known by the local device for this management domain when  managementDomainVersionInUse is version1(1) or  version2(2).  If managementDomainVersionInUse is version3(4), this  object has the same value with vtpDatabaseRevisionNumber  of VLAN database type.  This value is updated (if necessary) whenever a VTP advertisement is received or generated. When in the 'no management\-domain' state, this value is 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: managementdomainlastupdater
            
            	The IP\-address (or one of them) of the VTP Server which last updated the Configuration Revision Number, as indicated in the most recently received VTP advertisement for this management domain, when managementDomainVersionInUse is version1(1) or version2(2).   If managementDomainVersionInUse is version3(4), this object has the value of 0.0.0.0.  Before an advertisement has been received, this value is 0.0.0.0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: managementdomainlastchange
            
            	The time at which the Configuration Revision Number was (last) increased to its current value, as indicated in the most recently received VTP advertisement for this management domain when managementDomainVersionInUse is not version3(4) or in the most recently received VTP VLAN database  advertisement for this management domain when  managementDomainVersionInUse is version3(4).  The value 0x0000010100000000 indicates that the device which last increased the Configuration Revision Number had no idea of the date/time, or that no advertisement has been received
            	**type**\: str
            
            .. attribute:: managementdomainrowstatus
            
            	The status of this conceptual row
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: managementdomaintftpserver
            
            	The IP address of a TFTP Server in/from which VTP VLAN information for this management domain is to be stored/retrieved.  If the information is being locally stored in NVRAM, this object should take the value 0.0.0.0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: managementdomaintftppathname
            
            	The complete pathname of the file at the TFTP Server identified by the value of managementDomainTftpServer in/from which VTP VLAN information for this management domain is to be stored/retrieved.  If the value of corresponding instance of managementDomainTftpServer is 0.0.0.0, the value of this object is ignored
            	**type**\: str
            
            .. attribute:: managementdomainpruningstate
            
            	An indication of whether VTP pruning is enabled or disabled in this managament domain.   This object can only be modified, either when the  corresponding instance value of managementDomainVersionInUse  is 'version1' or 'version2' and the corresponding instance  value of managementDomainLocalMode is 'server', or when the  corresponding instance value of managementDomainVersionInUse  is 'version3' and the corresponding instance value of  managementDomainLocalMode is 'server' or 'client'
            	**type**\:  :py:class:`Managementdomainpruningstate <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Managementdomaintable.Managementdomainentry.Managementdomainpruningstate>`
            
            .. attribute:: managementdomainversioninuse
            
            	The current version of the VTP that is in use by the designated management domain.   This object can be set to none(3) only when  vtpVersion is none(3)
            	**type**\:  :py:class:`Managementdomainversioninuse <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Managementdomaintable.Managementdomainentry.Managementdomainversioninuse>`
            
            .. attribute:: managementdomainpruningstateoper
            
            	Indicates whether VTP pruning is operationally enabled or disabled in this managament domain
            	**type**\:  :py:class:`Managementdomainpruningstateoper <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Managementdomaintable.Managementdomainentry.Managementdomainpruningstateoper>`
            
            .. attribute:: managementdomainadminsrcif
            
            	The object specifies the interface to be used as the preferred source interface for the VTP IP updater address.  A zero length value indicates that a source interface is not specified
            	**type**\: str
            
            .. attribute:: managementdomainsourceonlymode
            
            	The object specifies whether to use only the IP address of managementDomainAdminSrcIf as the VTP IP updater address.   'true' indicates to only use the IP address of         managementDomainAdminSrcIf as the VTP IP         updater address.   'false' indicates to use the IP address of          managementDomainAdminSrcIf as the VTP IP          updater address if managementDomainAdminSrcIf          is configured with an IP address.  Otherwise, the          first available IP address of the system will         be used
            	**type**\: bool
            
            .. attribute:: managementdomainopersrcif
            
            	The object indicates the interface used as the preferred source interface for the VTP IP updater address.  A zero length string indicates that a source interface is not available
            	**type**\: str
            
            .. attribute:: managementdomainconfigfile
            
            	The object specifies the file name where VTP configuration is stored in the format of <filename> or <devices>\:[<filename>].  <device> can be (but not limited to)\: flash, bootflash, slot0, slot1, disk0
            	**type**\: str
            
            .. attribute:: managementdomainlocalupdatertype
            
            	The object indicates the type of the Internet address of the preferred source interface for the VTP IP updater.  The value of this object is 'unknown' if managementDomainVersionInUse is 'version3' or managementDomainLocalMode is not 'server'
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: managementdomainlocalupdater
            
            	The object indicates the Internet address of the preferred source interface for the VTP IP updater
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: managementdomaindeviceid
            
            	The object indicates a value that uniquely identifies this device within a VTP Domain.  The value of this object is zero length string if managementDomainVersionInUse is not 'version3'
            	**type**\: str
            
            .. attribute:: vtpvlaneditoperation
            
            	This object always has the value 'none' when read.  When written, each value causes the appropriate action\:   'copy' \- causes the creation of rows in the vtpVlanEditTable exactly corresponding to the current global VLAN information for this management domain.  If the Edit Buffer (for this management domain) is not currently empty, a copy operation fails.  A successful copy operation starts the deadman\-timer.   'apply' \- first performs a consistent check on the the modified information contained in the Edit Buffer, and if consistent, then tries to instanciate the modified information as the new global VLAN information.  Note that an empty Edit Buffer (for the management domain) would always result in an inconsistency since the default VLANs are required to be present.   'release' \- flushes the Edit Buffer (for this management domain), clears the Owner information, and aborts the deadman\-timer.  A release is generated automatically if the deadman\-timer ever expires.   'restartTimer' \- restarts the deadman\-timer.   'none' \- no operation is performed
            	**type**\:  :py:class:`Vtpvlaneditoperation <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Managementdomaintable.Managementdomainentry.Vtpvlaneditoperation>`
            
            .. attribute:: vtpvlanapplystatus
            
            	The current status of an 'apply' operation to instanciate the Edit Buffer as the new global VLAN information (for this management domain).  If no apply is currently active, the status represented is that of the most recently completed apply.  The possible values are\:     inProgress \- 'apply' operation in progress;     succeeded \- the 'apply' was successful (this value is           also used when no apply has been invoked since the           last time the local system restarted);     configNumberError \- the apply failed because the value of           vtpVlanEditConfigRevNumber was less or equal to           the value of current value of            managementDomainConfigRevNumber;     inconsistentEdit \- the apply failed because the modified           information was not self\-consistent;     tooBig \- the apply failed because the modified           information was too large to fit in this VTP           Server's non\-volatile storage location;     localNVStoreFail \- the apply failed in trying to store           the new information in a local non\-volatile           storage location;     remoteNVStoreFail \- the apply failed in trying to store           the new information in a remote non\-volatile           storage location;     editBufferEmpty \- the apply failed because the Edit           Buffer was empty (for this management domain).     someOtherError \- the apply failed for some other reason           (e.g., insufficient memory).     notPrimaryServer \- the apply failed because the local            device is not a VTP primary server for VLAN            database type when managementDomainVersionInUse           is version3(4)
            	**type**\:  :py:class:`Vtpvlanapplystatus <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Managementdomaintable.Managementdomainentry.Vtpvlanapplystatus>`
            
            .. attribute:: vtpvlaneditbufferowner
            
            	The management station which is currently using the Edit Buffer for this management domain.  When the Edit Buffer for a management domain is not currently in use, the value of this object is the zero\-length string.  Note that it is also the zero\-length string if a manager fails to set this object when invoking a copy operation
            	**type**\: str
            
            	**length:** 0..127
            
            .. attribute:: vtpvlaneditconfigrevnumber
            
            	The Configuration Revision Number to be used for the next apply operation.  This value is initialized (by the agent) on a copy operation to be one greater than the value of managementDomainConfigRevNumber. On an apply, if the  number is less or equal to the value of  managementDomainConfigRevNumber, then the apply fails. The value can be modified (increased) by network management before an apply to ensure that an apply does not fail for  this reason.  This object is used to allow management control over whether a configuration revision received via a VTP advertisement after a copy operation but before the succeeding apply operation is lost by being overwritten by the (local) edit operation.  By default, the apply operation will fail in this situation.  By increasing this object's value after the copy but before the apply, management can control whether the apply is to succeed (with the update via VTP advertisement being lost)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpvlaneditmodifiedvlan
            
            	The VLAN\-id of the modified VLAN in the Edit Buffer. If the object has the value of zero, any VLAN can  be edited. If the value of the object is not zero, only this VLAN can be edited.  The object's value is reset to zero after a successful 'apply' operation or a 'release' operation.   This object is only supported for devices which allow  only one VLAN editing for each 'apply' operation. For devices which allow multiple VLAN editing for each 'apply' operation, this object is not supported
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vtpinsummaryadverts
            
            	The total number of VTP Summary Adverts received for this management domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpinsubsetadverts
            
            	The total number of VTP Subset Adverts received for this management domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpinadvertrequests
            
            	The total number of VTP Advert Requests received for this management domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpoutsummaryadverts
            
            	The total number of VTP Summary Adverts sent for this management domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpoutsubsetadverts
            
            	The total number of VTP Subset Adverts sent for this management domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpoutadvertrequests
            
            	The total number of VTP Advert Requests sent for this management domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpconfigrevnumbererrors
            
            	The number of occurrences of configuration revision number errors for this management domain.  A configuration revision number error occurs when a device receives a VTP advertisement for which\:  \- the advertisement's Configuration Revision Number is the   same as the current locally\-held value, and  \- the advertisement's digest value is different from the   current locally\-held value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpconfigdigesterrors
            
            	The number of occurrences of configuration digest errors for this management domain.  A configuration digest error occurs when a device receives a VTP advertisement for which\:  \- the advertisement's Configuration Revision Number is   greater than the current locally\-held value, and  \-  the advertisement's digest value computed by the  receiving device does not match the checksum in the  summary advertisement that was received earlier. This  can happen, for example, if there is a mismatch in VTP  passwords between the VTP devices
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-VTP-MIB'
            _revision = '2013-10-14'

            def __init__(self):
                super(CISCOVTPMIB.Managementdomaintable.Managementdomainentry, self).__init__()

                self.yang_name = "managementDomainEntry"
                self.yang_parent_name = "managementDomainTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['managementdomainindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('managementdomainindex', YLeaf(YType.int32, 'managementDomainIndex')),
                    ('managementdomainname', YLeaf(YType.str, 'managementDomainName')),
                    ('managementdomainlocalmode', YLeaf(YType.enumeration, 'managementDomainLocalMode')),
                    ('managementdomainconfigrevnumber', YLeaf(YType.uint32, 'managementDomainConfigRevNumber')),
                    ('managementdomainlastupdater', YLeaf(YType.str, 'managementDomainLastUpdater')),
                    ('managementdomainlastchange', YLeaf(YType.str, 'managementDomainLastChange')),
                    ('managementdomainrowstatus', YLeaf(YType.enumeration, 'managementDomainRowStatus')),
                    ('managementdomaintftpserver', YLeaf(YType.str, 'managementDomainTftpServer')),
                    ('managementdomaintftppathname', YLeaf(YType.str, 'managementDomainTftpPathname')),
                    ('managementdomainpruningstate', YLeaf(YType.enumeration, 'managementDomainPruningState')),
                    ('managementdomainversioninuse', YLeaf(YType.enumeration, 'managementDomainVersionInUse')),
                    ('managementdomainpruningstateoper', YLeaf(YType.enumeration, 'managementDomainPruningStateOper')),
                    ('managementdomainadminsrcif', YLeaf(YType.str, 'managementDomainAdminSrcIf')),
                    ('managementdomainsourceonlymode', YLeaf(YType.boolean, 'managementDomainSourceOnlyMode')),
                    ('managementdomainopersrcif', YLeaf(YType.str, 'managementDomainOperSrcIf')),
                    ('managementdomainconfigfile', YLeaf(YType.str, 'managementDomainConfigFile')),
                    ('managementdomainlocalupdatertype', YLeaf(YType.enumeration, 'managementDomainLocalUpdaterType')),
                    ('managementdomainlocalupdater', YLeaf(YType.str, 'managementDomainLocalUpdater')),
                    ('managementdomaindeviceid', YLeaf(YType.str, 'managementDomainDeviceID')),
                    ('vtpvlaneditoperation', YLeaf(YType.enumeration, 'vtpVlanEditOperation')),
                    ('vtpvlanapplystatus', YLeaf(YType.enumeration, 'vtpVlanApplyStatus')),
                    ('vtpvlaneditbufferowner', YLeaf(YType.str, 'vtpVlanEditBufferOwner')),
                    ('vtpvlaneditconfigrevnumber', YLeaf(YType.uint32, 'vtpVlanEditConfigRevNumber')),
                    ('vtpvlaneditmodifiedvlan', YLeaf(YType.int32, 'vtpVlanEditModifiedVlan')),
                    ('vtpinsummaryadverts', YLeaf(YType.uint32, 'vtpInSummaryAdverts')),
                    ('vtpinsubsetadverts', YLeaf(YType.uint32, 'vtpInSubsetAdverts')),
                    ('vtpinadvertrequests', YLeaf(YType.uint32, 'vtpInAdvertRequests')),
                    ('vtpoutsummaryadverts', YLeaf(YType.uint32, 'vtpOutSummaryAdverts')),
                    ('vtpoutsubsetadverts', YLeaf(YType.uint32, 'vtpOutSubsetAdverts')),
                    ('vtpoutadvertrequests', YLeaf(YType.uint32, 'vtpOutAdvertRequests')),
                    ('vtpconfigrevnumbererrors', YLeaf(YType.uint32, 'vtpConfigRevNumberErrors')),
                    ('vtpconfigdigesterrors', YLeaf(YType.uint32, 'vtpConfigDigestErrors')),
                ])
                self.managementdomainindex = None
                self.managementdomainname = None
                self.managementdomainlocalmode = None
                self.managementdomainconfigrevnumber = None
                self.managementdomainlastupdater = None
                self.managementdomainlastchange = None
                self.managementdomainrowstatus = None
                self.managementdomaintftpserver = None
                self.managementdomaintftppathname = None
                self.managementdomainpruningstate = None
                self.managementdomainversioninuse = None
                self.managementdomainpruningstateoper = None
                self.managementdomainadminsrcif = None
                self.managementdomainsourceonlymode = None
                self.managementdomainopersrcif = None
                self.managementdomainconfigfile = None
                self.managementdomainlocalupdatertype = None
                self.managementdomainlocalupdater = None
                self.managementdomaindeviceid = None
                self.vtpvlaneditoperation = None
                self.vtpvlanapplystatus = None
                self.vtpvlaneditbufferowner = None
                self.vtpvlaneditconfigrevnumber = None
                self.vtpvlaneditmodifiedvlan = None
                self.vtpinsummaryadverts = None
                self.vtpinsubsetadverts = None
                self.vtpinadvertrequests = None
                self.vtpoutsummaryadverts = None
                self.vtpoutsubsetadverts = None
                self.vtpoutadvertrequests = None
                self.vtpconfigrevnumbererrors = None
                self.vtpconfigdigesterrors = None
                self._segment_path = lambda: "managementDomainEntry" + "[managementDomainIndex='" + str(self.managementdomainindex) + "']"
                self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/managementDomainTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVTPMIB.Managementdomaintable.Managementdomainentry, ['managementdomainindex', 'managementdomainname', 'managementdomainlocalmode', 'managementdomainconfigrevnumber', 'managementdomainlastupdater', 'managementdomainlastchange', 'managementdomainrowstatus', 'managementdomaintftpserver', 'managementdomaintftppathname', 'managementdomainpruningstate', 'managementdomainversioninuse', 'managementdomainpruningstateoper', 'managementdomainadminsrcif', 'managementdomainsourceonlymode', 'managementdomainopersrcif', 'managementdomainconfigfile', 'managementdomainlocalupdatertype', 'managementdomainlocalupdater', 'managementdomaindeviceid', 'vtpvlaneditoperation', 'vtpvlanapplystatus', 'vtpvlaneditbufferowner', 'vtpvlaneditconfigrevnumber', 'vtpvlaneditmodifiedvlan', 'vtpinsummaryadverts', 'vtpinsubsetadverts', 'vtpinadvertrequests', 'vtpoutsummaryadverts', 'vtpoutsubsetadverts', 'vtpoutadvertrequests', 'vtpconfigrevnumbererrors', 'vtpconfigdigesterrors'], name, value)

            class Managementdomainlocalmode(Enum):
                """
                Managementdomainlocalmode (Enum Class)

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
                Managementdomainpruningstate (Enum Class)

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
                Managementdomainpruningstateoper (Enum Class)

                Indicates whether VTP pruning is operationally enabled or

                disabled in this managament domain.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = Enum.YLeaf(1, "enabled")

                disabled = Enum.YLeaf(2, "disabled")


            class Managementdomainversioninuse(Enum):
                """
                Managementdomainversioninuse (Enum Class)

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
                Vtpvlanapplystatus (Enum Class)

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
                Vtpvlaneditoperation (Enum Class)

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



    class Vtpvlantable(Entity):
        """
        This table contains information on the VLANs which
        currently exist.
        
        .. attribute:: vtpvlanentry
        
        	Information about one current VLAN.  The managementDomainIndex value in the INDEX clause indicates which management domain the VLAN is in
        	**type**\: list of  		 :py:class:`Vtpvlanentry <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpvlantable.Vtpvlanentry>`
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CISCOVTPMIB.Vtpvlantable, self).__init__()

            self.yang_name = "vtpVlanTable"
            self.yang_parent_name = "CISCO-VTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("vtpVlanEntry", ("vtpvlanentry", CISCOVTPMIB.Vtpvlantable.Vtpvlanentry))])
            self._leafs = OrderedDict()

            self.vtpvlanentry = YList(self)
            self._segment_path = lambda: "vtpVlanTable"
            self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVTPMIB.Vtpvlantable, [], name, value)


        class Vtpvlanentry(Entity):
            """
            Information about one current VLAN.  The
            managementDomainIndex value in the INDEX clause indicates
            which management domain the VLAN is in.
            
            .. attribute:: managementdomainindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..255
            
            	**refers to**\:  :py:class:`managementdomainindex <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Managementdomaintable.Managementdomainentry>`
            
            .. attribute:: vtpvlanindex  (key)
            
            	The VLAN\-id of this VLAN on ISL or 802.1q trunks
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlanstate
            
            	The state of this VLAN.  The state 'mtuTooBigForDevice' indicates that this device cannot participate in this VLAN because the VLAN's MTU is larger than the device can support.  The state 'mtuTooBigForTrunk' indicates that while this VLAN's MTU is supported by this device, it is too large for one or more of the device's trunk ports
            	**type**\:  :py:class:`Vtpvlanstate <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpvlantable.Vtpvlanentry.Vtpvlanstate>`
            
            .. attribute:: vtpvlantype
            
            	The type of this VLAN
            	**type**\:  :py:class:`VlanType <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.VlanType>`
            
            .. attribute:: vtpvlanname
            
            	The name of this VLAN.  This name is used as the ELAN\-name for an ATM LAN\-Emulation segment of this VLAN
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: vtpvlanmtu
            
            	The MTU size on this VLAN, defined as the size of largest MAC\-layer (information field portion of the) data frame which can be transmitted on the VLAN
            	**type**\: int
            
            	**range:** 1500..18190
            
            .. attribute:: vtpvlandot10said
            
            	The value of the 802.10 SAID field for this VLAN
            	**type**\: str
            
            	**length:** 4
            
            .. attribute:: vtpvlanringnumber
            
            	The ring number of this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanType has a value of 'fddi' or 'tokenRing' and Source Routing is in use on this VLAN
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlanbridgenumber
            
            	The bridge number of the VTP\-capable switches for this VLAN.  This object is only instantiated for VLANs that are involved with emulating token ring segments
            	**type**\: int
            
            	**range:** 0..15
            
            .. attribute:: vtpvlanstptype
            
            	The type of the Spanning Tree Protocol (STP) running on this VLAN.  This object is only instanciated when the value of the corresponding instance of vtpVlanType has a value of 'fddiNet' or 'trNet'.  The value returned by this object depends upon the value of the corresponding instance of vtpVlanEditStpType.  \- 'ieee' indicates IEEE STP is running exclusively.  \- 'ibm' indicates IBM STP is running exclusively.  \- 'hybrid' indicates a STP that allows a combination of   IEEE and IBM is running.  The 'hybrid' STP type results from tokenRing/fddi VLANs that are children of this trNet/fddiNet parent VLAN being configured in a combination of SRT and SRB vtpVlanBridgeTypes while the instance of vtpVlanEditStpType that corresponds to this object is set to 'auto'
            	**type**\:  :py:class:`Vtpvlanstptype <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpvlantable.Vtpvlanentry.Vtpvlanstptype>`
            
            .. attribute:: vtpvlanparentvlan
            
            	The parent VLAN for this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanType has a value of 'fddi' or 'tokenRing' and Source Routing is in use on this VLAN.  The parent VLAN must have  a vtpVlanType value of fddiNet(4) or trNet(5),  respectively
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlantranslationalvlan1
            
            	A VLAN to which this VLAN is being translational\-bridged. If this value and the corresponding instance of vtpVlanTranslationalVlan2 are both zero, then this VLAN is not being translational\-bridged
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlantranslationalvlan2
            
            	Another VLAN, i.e., other than that indicated by vtpVlanTranslationalVlan1, to which this VLAN is being translational\-bridged.  If this value and the corresponding instance of vtpVlanTranslationalVlan1 are both zero, then this VLAN is not being translational\-bridged
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlanbridgetype
            
            	The type of the Source Route bridging mode in use on this VLAN.  This object is only instantiated when the value of  the corresponding instance of vtpVlanType has a value of  fddi(2) or tokenRing(3) and Source Routing is in use on this VLAN
            	**type**\:  :py:class:`Vtpvlanbridgetype <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpvlantable.Vtpvlanentry.Vtpvlanbridgetype>`
            
            .. attribute:: vtpvlanarehopcount
            
            	The maximum number of bridge hops allowed in All Routes Explorer frames on this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanType has a value of fddi(2) or tokenRing(3) and Source Routing is in use on this VLAN
            	**type**\: int
            
            	**range:** 1..13
            
            .. attribute:: vtpvlanstehopcount
            
            	The maximum number of bridge hops allowed in Spanning Tree Explorer frames on this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanType has a value of fddi(2) or tokenRing(3) and Source Routing is in use on this VLAN
            	**type**\: int
            
            	**range:** 1..13
            
            .. attribute:: vtpvlaniscrfbackup
            
            	True if this VLAN is of type trCrf and also is acting as a backup trCrf for the ISL distributed BRF
            	**type**\: bool
            
            .. attribute:: vtpvlantypeext
            
            	The additional type information of this VLAN
            	**type**\:  :py:class:`VlanTypeExt <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.VlanTypeExt>`
            
            .. attribute:: vtpvlanifindex
            
            	The value of the ifIndex corresponding to this VLAN ID. If the VLAN ID does not have its corresponding interface,  this object has the value of zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: stpxvlanmistpinstmapinstindex
            
            	The MISTP instance, to which the corresponding vlan is mapped. If this value of this mib object is 0,  the corresponding vlan  is not configured to be mapped to any MISTP instance and all the ports under this VLAN remain in blocking state
            	**type**\: int
            
            	**range:** 0..256
            
            

            """

            _prefix = 'CISCO-VTP-MIB'
            _revision = '2013-10-14'

            def __init__(self):
                super(CISCOVTPMIB.Vtpvlantable.Vtpvlanentry, self).__init__()

                self.yang_name = "vtpVlanEntry"
                self.yang_parent_name = "vtpVlanTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['managementdomainindex','vtpvlanindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('managementdomainindex', YLeaf(YType.str, 'managementDomainIndex')),
                    ('vtpvlanindex', YLeaf(YType.int32, 'vtpVlanIndex')),
                    ('vtpvlanstate', YLeaf(YType.enumeration, 'vtpVlanState')),
                    ('vtpvlantype', YLeaf(YType.enumeration, 'vtpVlanType')),
                    ('vtpvlanname', YLeaf(YType.str, 'vtpVlanName')),
                    ('vtpvlanmtu', YLeaf(YType.int32, 'vtpVlanMtu')),
                    ('vtpvlandot10said', YLeaf(YType.str, 'vtpVlanDot10Said')),
                    ('vtpvlanringnumber', YLeaf(YType.int32, 'vtpVlanRingNumber')),
                    ('vtpvlanbridgenumber', YLeaf(YType.int32, 'vtpVlanBridgeNumber')),
                    ('vtpvlanstptype', YLeaf(YType.enumeration, 'vtpVlanStpType')),
                    ('vtpvlanparentvlan', YLeaf(YType.int32, 'vtpVlanParentVlan')),
                    ('vtpvlantranslationalvlan1', YLeaf(YType.int32, 'vtpVlanTranslationalVlan1')),
                    ('vtpvlantranslationalvlan2', YLeaf(YType.int32, 'vtpVlanTranslationalVlan2')),
                    ('vtpvlanbridgetype', YLeaf(YType.enumeration, 'vtpVlanBridgeType')),
                    ('vtpvlanarehopcount', YLeaf(YType.int32, 'vtpVlanAreHopCount')),
                    ('vtpvlanstehopcount', YLeaf(YType.int32, 'vtpVlanSteHopCount')),
                    ('vtpvlaniscrfbackup', YLeaf(YType.boolean, 'vtpVlanIsCRFBackup')),
                    ('vtpvlantypeext', YLeaf(YType.bits, 'vtpVlanTypeExt')),
                    ('vtpvlanifindex', YLeaf(YType.int32, 'vtpVlanIfIndex')),
                    ('stpxvlanmistpinstmapinstindex', YLeaf(YType.int32, 'CISCO-STP-EXTENSIONS-MIB:stpxVlanMISTPInstMapInstIndex')),
                ])
                self.managementdomainindex = None
                self.vtpvlanindex = None
                self.vtpvlanstate = None
                self.vtpvlantype = None
                self.vtpvlanname = None
                self.vtpvlanmtu = None
                self.vtpvlandot10said = None
                self.vtpvlanringnumber = None
                self.vtpvlanbridgenumber = None
                self.vtpvlanstptype = None
                self.vtpvlanparentvlan = None
                self.vtpvlantranslationalvlan1 = None
                self.vtpvlantranslationalvlan2 = None
                self.vtpvlanbridgetype = None
                self.vtpvlanarehopcount = None
                self.vtpvlanstehopcount = None
                self.vtpvlaniscrfbackup = None
                self.vtpvlantypeext = Bits()
                self.vtpvlanifindex = None
                self.stpxvlanmistpinstmapinstindex = None
                self._segment_path = lambda: "vtpVlanEntry" + "[managementDomainIndex='" + str(self.managementdomainindex) + "']" + "[vtpVlanIndex='" + str(self.vtpvlanindex) + "']"
                self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/vtpVlanTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVTPMIB.Vtpvlantable.Vtpvlanentry, ['managementdomainindex', 'vtpvlanindex', 'vtpvlanstate', 'vtpvlantype', 'vtpvlanname', 'vtpvlanmtu', 'vtpvlandot10said', 'vtpvlanringnumber', 'vtpvlanbridgenumber', 'vtpvlanstptype', 'vtpvlanparentvlan', 'vtpvlantranslationalvlan1', 'vtpvlantranslationalvlan2', 'vtpvlanbridgetype', 'vtpvlanarehopcount', 'vtpvlanstehopcount', 'vtpvlaniscrfbackup', 'vtpvlantypeext', 'vtpvlanifindex', 'stpxvlanmistpinstmapinstindex'], name, value)

            class Vtpvlanbridgetype(Enum):
                """
                Vtpvlanbridgetype (Enum Class)

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
                Vtpvlanstate (Enum Class)

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
                Vtpvlanstptype (Enum Class)

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
        	**type**\: list of  		 :py:class:`Vtpinternalvlanentry <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpinternalvlantable.Vtpinternalvlanentry>`
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CISCOVTPMIB.Vtpinternalvlantable, self).__init__()

            self.yang_name = "vtpInternalVlanTable"
            self.yang_parent_name = "CISCO-VTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("vtpInternalVlanEntry", ("vtpinternalvlanentry", CISCOVTPMIB.Vtpinternalvlantable.Vtpinternalvlanentry))])
            self._leafs = OrderedDict()

            self.vtpinternalvlanentry = YList(self)
            self._segment_path = lambda: "vtpInternalVlanTable"
            self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVTPMIB.Vtpinternalvlantable, [], name, value)


        class Vtpinternalvlanentry(Entity):
            """
            Information about one current internal
            VLAN.
            
            .. attribute:: managementdomainindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..255
            
            	**refers to**\:  :py:class:`managementdomainindex <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Managementdomaintable.Managementdomainentry>`
            
            .. attribute:: vtpvlanindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`vtpvlanindex <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpvlantable.Vtpvlanentry>`
            
            .. attribute:: vtpinternalvlanowner
            
            	The program name of the internal VLAN's owner application. This internal VLAN is allocated by the device specifically for this application and no one else could create, modify or delete this  VLAN
            	**type**\: str
            
            

            """

            _prefix = 'CISCO-VTP-MIB'
            _revision = '2013-10-14'

            def __init__(self):
                super(CISCOVTPMIB.Vtpinternalvlantable.Vtpinternalvlanentry, self).__init__()

                self.yang_name = "vtpInternalVlanEntry"
                self.yang_parent_name = "vtpInternalVlanTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['managementdomainindex','vtpvlanindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('managementdomainindex', YLeaf(YType.str, 'managementDomainIndex')),
                    ('vtpvlanindex', YLeaf(YType.str, 'vtpVlanIndex')),
                    ('vtpinternalvlanowner', YLeaf(YType.str, 'vtpInternalVlanOwner')),
                ])
                self.managementdomainindex = None
                self.vtpvlanindex = None
                self.vtpinternalvlanowner = None
                self._segment_path = lambda: "vtpInternalVlanEntry" + "[managementDomainIndex='" + str(self.managementdomainindex) + "']" + "[vtpVlanIndex='" + str(self.vtpvlanindex) + "']"
                self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/vtpInternalVlanTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVTPMIB.Vtpinternalvlantable.Vtpinternalvlanentry, ['managementdomainindex', 'vtpvlanindex', 'vtpinternalvlanowner'], name, value)


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
        	**type**\: list of  		 :py:class:`Vtpvlaneditentry <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpvlanedittable.Vtpvlaneditentry>`
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CISCOVTPMIB.Vtpvlanedittable, self).__init__()

            self.yang_name = "vtpVlanEditTable"
            self.yang_parent_name = "CISCO-VTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("vtpVlanEditEntry", ("vtpvlaneditentry", CISCOVTPMIB.Vtpvlanedittable.Vtpvlaneditentry))])
            self._leafs = OrderedDict()

            self.vtpvlaneditentry = YList(self)
            self._segment_path = lambda: "vtpVlanEditTable"
            self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVTPMIB.Vtpvlanedittable, [], name, value)


        class Vtpvlaneditentry(Entity):
            """
            Information about one VLAN in the Edit Buffer for a
            particular management domain.
            
            .. attribute:: managementdomainindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..255
            
            	**refers to**\:  :py:class:`managementdomainindex <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Managementdomaintable.Managementdomainentry>`
            
            .. attribute:: vtpvlaneditindex  (key)
            
            	The VLAN\-id which this VLAN would have on ISL or 802.1q trunks
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlaneditstate
            
            	The state which this VLAN would have
            	**type**\:  :py:class:`Vtpvlaneditstate <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpvlanedittable.Vtpvlaneditentry.Vtpvlaneditstate>`
            
            .. attribute:: vtpvlanedittype
            
            	The type which this VLAN would have. An implementation may restrict access to this object
            	**type**\:  :py:class:`VlanType <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.VlanType>`
            
            .. attribute:: vtpvlaneditname
            
            	The name which this VLAN would have.  This name would be used as the ELAN\-name for an ATM LAN\-Emulation segment of this VLAN.  An implementation may restrict access to this object
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: vtpvlaneditmtu
            
            	The MTU size which this VLAN would have, defined as the size of largest MAC\-layer (information field portion of the) data frame which can be transmitted on the VLAN.  An implementation may restrict access to this object
            	**type**\: int
            
            	**range:** 1500..18190
            
            .. attribute:: vtpvlaneditdot10said
            
            	The value of the 802.10 SAID field which would be used for this VLAN.  An implementation may restrict access to this object
            	**type**\: str
            
            	**length:** 4
            
            .. attribute:: vtpvlaneditringnumber
            
            	The ring number which would be used for this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanEditType has a value of 'fddi' or 'tokenRing' and Source Routing is in use on  this VLAN
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlaneditbridgenumber
            
            	The bridge number of the VTP\-capable switches which would be used for this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanEditType has a value of fddiNet(4) or trNet(5)
            	**type**\: int
            
            	**range:** 0..15
            
            .. attribute:: vtpvlaneditstptype
            
            	The type of the Spanning Tree Protocol which would be running on this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanEditType has a value of fddiNet(4) or trNet(5).  If 'ieee' is selected, the STP that runs will be IEEE.  If 'ibm' is selected, the STP that runs will be IBM.  If 'auto' is selected, the STP that runs will be dependant on the values of vtpVlanEditBridgeType for all children tokenRing/fddi type VLANs.  This will result in a 'hybrid' STP (see vtpVlanStpType)
            	**type**\:  :py:class:`Vtpvlaneditstptype <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpvlanedittable.Vtpvlaneditentry.Vtpvlaneditstptype>`
            
            .. attribute:: vtpvlaneditparentvlan
            
            	The VLAN index of the VLAN which would be the parent for this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanEditType has a value of 'fddi' or 'tokenRing' and Source Routing is in use on this VLAN.  The parent VLAN must have a vtpVlanEditType  value of fddiNet(4) or trNet(5), respectively
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlaneditrowstatus
            
            	The status of this row.  Any and all columnar objects in an existing row can be modified irrespective of the status of the row.  A row is not qualified for activation until instances of at least its vtpVlanEditType, vtpVlanEditName and vtpVlanEditDot10Said columns have appropriate values.  The management station should endeavor to make all rows consistent in the table before 'apply'ing the buffer.  An inconsistent entry in the table will cause the entire buffer to be rejected with the vtpVlanApplyStatus object set to the appropriate error value
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: vtpvlanedittranslationalvlan1
            
            	A VLAN to which this VLAN would be translational\-bridged. If this value and the corresponding instance of vtpVlanTranslationalVlan2 are both zero, then this VLAN would not be translational\-bridged.  An implementation may restrict access to this object
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlanedittranslationalvlan2
            
            	Another VLAN, i.e., other than that indicated by vtpVlanEditTranslationalVlan1, to which this VLAN would be translational\-bridged.  If this value and the corresponding instance of vtpVlanTranslationalVlan1 are both zero, then this VLAN would not be translational\-bridged.  An implementation may restrict access to this object
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vtpvlaneditbridgetype
            
            	The type of Source Route bridging mode which would be in use on this VLAN.  This object is only instantiated when  the value of  the corresponding instance of vtpVlanEditType has a value of fddi(2) or tokenRing(3) and Source Routing  is in use on this VLAN
            	**type**\:  :py:class:`Vtpvlaneditbridgetype <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpvlanedittable.Vtpvlaneditentry.Vtpvlaneditbridgetype>`
            
            .. attribute:: vtpvlaneditarehopcount
            
            	The maximum number of bridge hops allowed in All Routes Explorer frames on this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanType has a value of fddi(2) or tokenRing(3) and Source Routing is in use on this VLAN
            	**type**\: int
            
            	**range:** 1..13
            
            .. attribute:: vtpvlaneditstehopcount
            
            	The maximum number of bridge hops allowed in Spanning Tree Explorer frames on this VLAN.  This object is only instantiated when the value of the corresponding instance of vtpVlanType has a value of fddi(2) or tokenRing(3) and Source Routing is in use on this VLAN
            	**type**\: int
            
            	**range:** 1..13
            
            .. attribute:: vtpvlaneditiscrfbackup
            
            	True if this VLAN is of type trCrf and also is acting as a backup trCrf for the ISL distributed BRF.  This object is only instantiated when the value of the corresponding instance of vtpVlanEditType has a value of tokenRing(3)
            	**type**\: bool
            
            .. attribute:: vtpvlanedittypeext
            
            	The additional type information of this VLAN. vtpVlanEditTypeExt object is superseded by vtpVlanEditTypeExt2
            	**type**\:  :py:class:`VlanTypeExt <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.VlanTypeExt>`
            
            	**status**\: deprecated
            
            .. attribute:: vtpvlanedittypeext2
            
            	The additional type information of this VLAN. The VlanTypeExt TC specifies which bits may be written by a management application. The agent should provide a default value
            	**type**\:  :py:class:`VlanTypeExt <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.VlanTypeExt>`
            
            .. attribute:: stpxvlanmistpinstmapeditinstindex
            
            	The MISTP instance, to which the corresponding vlan would be  mapped. The value of this mib object is from 0 to the value of stpxMISTPInstanceNumber. If setting the value of this object to 0, the corresponding vlan will not be mapped to a MISTP  instance and all the ports under this VLAN will be moved into the blocking state
            	**type**\: int
            
            	**range:** 0..256
            
            

            """

            _prefix = 'CISCO-VTP-MIB'
            _revision = '2013-10-14'

            def __init__(self):
                super(CISCOVTPMIB.Vtpvlanedittable.Vtpvlaneditentry, self).__init__()

                self.yang_name = "vtpVlanEditEntry"
                self.yang_parent_name = "vtpVlanEditTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['managementdomainindex','vtpvlaneditindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('managementdomainindex', YLeaf(YType.str, 'managementDomainIndex')),
                    ('vtpvlaneditindex', YLeaf(YType.int32, 'vtpVlanEditIndex')),
                    ('vtpvlaneditstate', YLeaf(YType.enumeration, 'vtpVlanEditState')),
                    ('vtpvlanedittype', YLeaf(YType.enumeration, 'vtpVlanEditType')),
                    ('vtpvlaneditname', YLeaf(YType.str, 'vtpVlanEditName')),
                    ('vtpvlaneditmtu', YLeaf(YType.int32, 'vtpVlanEditMtu')),
                    ('vtpvlaneditdot10said', YLeaf(YType.str, 'vtpVlanEditDot10Said')),
                    ('vtpvlaneditringnumber', YLeaf(YType.int32, 'vtpVlanEditRingNumber')),
                    ('vtpvlaneditbridgenumber', YLeaf(YType.int32, 'vtpVlanEditBridgeNumber')),
                    ('vtpvlaneditstptype', YLeaf(YType.enumeration, 'vtpVlanEditStpType')),
                    ('vtpvlaneditparentvlan', YLeaf(YType.int32, 'vtpVlanEditParentVlan')),
                    ('vtpvlaneditrowstatus', YLeaf(YType.enumeration, 'vtpVlanEditRowStatus')),
                    ('vtpvlanedittranslationalvlan1', YLeaf(YType.int32, 'vtpVlanEditTranslationalVlan1')),
                    ('vtpvlanedittranslationalvlan2', YLeaf(YType.int32, 'vtpVlanEditTranslationalVlan2')),
                    ('vtpvlaneditbridgetype', YLeaf(YType.enumeration, 'vtpVlanEditBridgeType')),
                    ('vtpvlaneditarehopcount', YLeaf(YType.int32, 'vtpVlanEditAreHopCount')),
                    ('vtpvlaneditstehopcount', YLeaf(YType.int32, 'vtpVlanEditSteHopCount')),
                    ('vtpvlaneditiscrfbackup', YLeaf(YType.boolean, 'vtpVlanEditIsCRFBackup')),
                    ('vtpvlanedittypeext', YLeaf(YType.bits, 'vtpVlanEditTypeExt')),
                    ('vtpvlanedittypeext2', YLeaf(YType.bits, 'vtpVlanEditTypeExt2')),
                    ('stpxvlanmistpinstmapeditinstindex', YLeaf(YType.int32, 'CISCO-STP-EXTENSIONS-MIB:stpxVlanMISTPInstMapEditInstIndex')),
                ])
                self.managementdomainindex = None
                self.vtpvlaneditindex = None
                self.vtpvlaneditstate = None
                self.vtpvlanedittype = None
                self.vtpvlaneditname = None
                self.vtpvlaneditmtu = None
                self.vtpvlaneditdot10said = None
                self.vtpvlaneditringnumber = None
                self.vtpvlaneditbridgenumber = None
                self.vtpvlaneditstptype = None
                self.vtpvlaneditparentvlan = None
                self.vtpvlaneditrowstatus = None
                self.vtpvlanedittranslationalvlan1 = None
                self.vtpvlanedittranslationalvlan2 = None
                self.vtpvlaneditbridgetype = None
                self.vtpvlaneditarehopcount = None
                self.vtpvlaneditstehopcount = None
                self.vtpvlaneditiscrfbackup = None
                self.vtpvlanedittypeext = Bits()
                self.vtpvlanedittypeext2 = Bits()
                self.stpxvlanmistpinstmapeditinstindex = None
                self._segment_path = lambda: "vtpVlanEditEntry" + "[managementDomainIndex='" + str(self.managementdomainindex) + "']" + "[vtpVlanEditIndex='" + str(self.vtpvlaneditindex) + "']"
                self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/vtpVlanEditTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVTPMIB.Vtpvlanedittable.Vtpvlaneditentry, ['managementdomainindex', 'vtpvlaneditindex', 'vtpvlaneditstate', 'vtpvlanedittype', 'vtpvlaneditname', 'vtpvlaneditmtu', 'vtpvlaneditdot10said', 'vtpvlaneditringnumber', 'vtpvlaneditbridgenumber', 'vtpvlaneditstptype', 'vtpvlaneditparentvlan', 'vtpvlaneditrowstatus', 'vtpvlanedittranslationalvlan1', 'vtpvlanedittranslationalvlan2', 'vtpvlaneditbridgetype', 'vtpvlaneditarehopcount', 'vtpvlaneditstehopcount', 'vtpvlaneditiscrfbackup', 'vtpvlanedittypeext', 'vtpvlanedittypeext2', 'stpxvlanmistpinstmapeditinstindex'], name, value)

            class Vtpvlaneditbridgetype(Enum):
                """
                Vtpvlaneditbridgetype (Enum Class)

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
                Vtpvlaneditstate (Enum Class)

                The state which this VLAN would have.

                .. data:: operational = 1

                .. data:: suspended = 2

                """

                operational = Enum.YLeaf(1, "operational")

                suspended = Enum.YLeaf(2, "suspended")


            class Vtpvlaneditstptype(Enum):
                """
                Vtpvlaneditstptype (Enum Class)

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



    class Vtpvlanlocalshutdowntable(Entity):
        """
        Ths table contains the VLAN local shutdown
        information within management domain.
        
        .. attribute:: vtpvlanlocalshutdownentry
        
        	An entry containing VLAN local shutdown information for a particular VLAN in the management domain.  An entry is created if a VLAN which supports local shutdown has been created.  An entry is deleted if a VLAN which supports local shutdown has been removed
        	**type**\: list of  		 :py:class:`Vtpvlanlocalshutdownentry <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpvlanlocalshutdowntable.Vtpvlanlocalshutdownentry>`
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CISCOVTPMIB.Vtpvlanlocalshutdowntable, self).__init__()

            self.yang_name = "vtpVlanLocalShutdownTable"
            self.yang_parent_name = "CISCO-VTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("vtpVlanLocalShutdownEntry", ("vtpvlanlocalshutdownentry", CISCOVTPMIB.Vtpvlanlocalshutdowntable.Vtpvlanlocalshutdownentry))])
            self._leafs = OrderedDict()

            self.vtpvlanlocalshutdownentry = YList(self)
            self._segment_path = lambda: "vtpVlanLocalShutdownTable"
            self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVTPMIB.Vtpvlanlocalshutdowntable, [], name, value)


        class Vtpvlanlocalshutdownentry(Entity):
            """
            An entry containing VLAN local shutdown information for a
            particular VLAN in the management domain.
            
            An entry is created if a VLAN which supports local shutdown
            has been created.
            
            An entry is deleted if a VLAN which supports local shutdown
            has been removed.
            
            .. attribute:: managementdomainindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..255
            
            	**refers to**\:  :py:class:`managementdomainindex <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Managementdomaintable.Managementdomainentry>`
            
            .. attribute:: vtpvlanindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`vtpvlanindex <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpvlantable.Vtpvlanentry>`
            
            .. attribute:: vtpvlanlocalshutdown
            
            	The object specifies the VLAN local shutdown state
            	**type**\:  :py:class:`Vtpvlanlocalshutdown <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpvlanlocalshutdowntable.Vtpvlanlocalshutdownentry.Vtpvlanlocalshutdown>`
            
            

            """

            _prefix = 'CISCO-VTP-MIB'
            _revision = '2013-10-14'

            def __init__(self):
                super(CISCOVTPMIB.Vtpvlanlocalshutdowntable.Vtpvlanlocalshutdownentry, self).__init__()

                self.yang_name = "vtpVlanLocalShutdownEntry"
                self.yang_parent_name = "vtpVlanLocalShutdownTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['managementdomainindex','vtpvlanindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('managementdomainindex', YLeaf(YType.str, 'managementDomainIndex')),
                    ('vtpvlanindex', YLeaf(YType.str, 'vtpVlanIndex')),
                    ('vtpvlanlocalshutdown', YLeaf(YType.enumeration, 'vtpVlanLocalShutdown')),
                ])
                self.managementdomainindex = None
                self.vtpvlanindex = None
                self.vtpvlanlocalshutdown = None
                self._segment_path = lambda: "vtpVlanLocalShutdownEntry" + "[managementDomainIndex='" + str(self.managementdomainindex) + "']" + "[vtpVlanIndex='" + str(self.vtpvlanindex) + "']"
                self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/vtpVlanLocalShutdownTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVTPMIB.Vtpvlanlocalshutdowntable.Vtpvlanlocalshutdownentry, ['managementdomainindex', 'vtpvlanindex', 'vtpvlanlocalshutdown'], name, value)

            class Vtpvlanlocalshutdown(Enum):
                """
                Vtpvlanlocalshutdown (Enum Class)

                The object specifies the VLAN local shutdown state.

                .. data:: up = 1

                .. data:: down = 2

                """

                up = Enum.YLeaf(1, "up")

                down = Enum.YLeaf(2, "down")



    class Vlantrunkporttable(Entity):
        """
        The table containing information on the local system's VLAN
        trunk ports.
        
        .. attribute:: vlantrunkportentry
        
        	Information about one trunk port
        	**type**\: list of  		 :py:class:`Vlantrunkportentry <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vlantrunkporttable.Vlantrunkportentry>`
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CISCOVTPMIB.Vlantrunkporttable, self).__init__()

            self.yang_name = "vlanTrunkPortTable"
            self.yang_parent_name = "CISCO-VTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("vlanTrunkPortEntry", ("vlantrunkportentry", CISCOVTPMIB.Vlantrunkporttable.Vlantrunkportentry))])
            self._leafs = OrderedDict()

            self.vlantrunkportentry = YList(self)
            self._segment_path = lambda: "vlanTrunkPortTable"
            self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVTPMIB.Vlantrunkporttable, [], name, value)


        class Vlantrunkportentry(Entity):
            """
            Information about one trunk port.
            
            .. attribute:: vlantrunkportifindex  (key)
            
            	The value of ifIndex for the interface corresponding to this trunk port
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: vlantrunkportmanagementdomain
            
            	The value of managementDomainIndex for the management domain on this trunk port.  Devices which support only one management domain will support this object read\-only
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: vlantrunkportencapsulationtype
            
            	The type of VLAN encapsulation desired to be used on this trunk port. It is either a particular type, or 'negotiate' meaning whatever type results from the negotiation. negotiate(5) is not allowed if the port does not support negotiation or if its vlanTrunkPortDynamicState is set to on(1) or onNoNegotiate(5). Whether writing to this object in order to modify the encapsulation is supported is both device and interface specific
            	**type**\:  :py:class:`Vlantrunkportencapsulationtype <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vlantrunkporttable.Vlantrunkportentry.Vlantrunkportencapsulationtype>`
            
            .. attribute:: vlantrunkportvlansenabled
            
            	A string of octets containing one bit per VLAN in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local system is enabled for sending and receiving frames on that VLAN; if the bit is set to '0', then the system is disabled from sending and receiving frames on that VLAN.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**length:** 128
            
            .. attribute:: vlantrunkportnativevlan
            
            	The VlanIndex of the VLAN which is represented by native frames on this trunk port.  For trunk ports not supporting the sending and receiving of native frames, this value should be set to zero
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: vlantrunkportrowstatus
            
            	The status of this row.  In some circumstances, the creation of a row in this table is needed to enable the appropriate trunking/tagging protocol on the port, to enable the use of VTP on the port, and to assign the port to the appropriate management domain.  In other circumstances, rows in this table will be created as a by\-product of other operations
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: vlantrunkportinjoins
            
            	The number of VTP Join messages received on this trunk port
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vlantrunkportoutjoins
            
            	The number of VTP Join messages sent on this trunk port
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vlantrunkportoldadverts
            
            	The number of VTP Advertisement messages which indicated the sender does not support VLAN\-pruning received on this trunk port
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vlantrunkportvlanspruningeligible
            
            	A string of octets containing one bit per VLAN in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local system is permitted to prune that VLAN on this trunk port; if the bit is set to '0', then the system must not prune that VLAN on this trunk port.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**length:** 128
            
            .. attribute:: vlantrunkportvlansxmitjoined
            
            	A string of octets containing one bit per VLAN in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then this VLAN is presently being forwarded on this trunk port, i.e., it is not pruned; if the bit is set to '0', then this VLAN is presently not being forwarded on this trunk port, either because it is pruned or for some other reason
            	**type**\: str
            
            	**length:** 128
            
            .. attribute:: vlantrunkportvlansrcvjoined
            
            	A string of octets containing one bit per VLAN in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local switch is currently sending joins for this VLAN on this trunk port, i.e., it is asking to receive frames for this VLAN; if the bit is set to '0', then the local switch is not currently sending joins for this VLAN on this trunk port
            	**type**\: str
            
            	**length:** 128
            
            .. attribute:: vlantrunkportdynamicstate
            
            	For devices that allows dynamic determination of whether a link between two switches should be a trunk or not, this object allows the operator to mandate the behavior of that dynamic mechanism.  on(1) dictates that the interface will always be a trunk. This is the value for static entries (those that show no dynamic behavior). If the negotiation is supported on this port, negotiation will take place with the far end to attempt to bring the far end into trunking state.  off(2) allows an operator to specify that the specified interface is never to be trunk, regardless of any dynamic mechanisms to the contrary.  This value is useful for overriding the default behavior of some switches. If the negotiation is supported on this port, negotiation will take place with the far end to attempt on the link to bring the far end into non\-trunking state.  desirable(3) is used to indicate that it is desirable for the interface to become a trunk.  The device will initiate any negotiation necessary to become a trunk but will not become a trunk unless it receives confirmation from the far end on the link.  auto(4) is used to indicate that the interface is capable and willing to become a trunk but will not initiate trunking negotiations.  The far end on the link are required to either start negotiations or start sending encapsulated packets, on which event the specified interface will become a trunk.  onNoNegotiate(5) is used to indicate that the interface is permanently set to be a trunk, and no negotiation takes place with the far end on the link to ensure consistent operation. This is similar to on(1) except no negotiation takes place with the far end.  If the port does not support negotiation or its vlanTrunkPortEncapsulationType is set to negotiate(5), onNoNegotiate(5) is not allowed.  Devices that do no support dynamic determination (for just a particular interface, encapsulation or for the whole device) need only support the 'on', and 'off' values
            	**type**\:  :py:class:`Vlantrunkportdynamicstate <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vlantrunkporttable.Vlantrunkportentry.Vlantrunkportdynamicstate>`
            
            .. attribute:: vlantrunkportdynamicstatus
            
            	Indicates whether the specified interface is either acting as a trunk or not. This is a result of the vlanTrunkPortDynamicState and the ifOperStatus of the trunk port itself
            	**type**\:  :py:class:`Vlantrunkportdynamicstatus <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vlantrunkporttable.Vlantrunkportentry.Vlantrunkportdynamicstatus>`
            
            .. attribute:: vlantrunkportvtpenabled
            
            	Some trunk interface modules allow VTP to be enabled/disabled seperately from that of the central device.  In such a case this object provides management a way to remotely enable VTP on that module.  If a module does not support a seperate VTP enabled state then this object shall always return 'true' and will accept no other value during a SET operation
            	**type**\: bool
            
            .. attribute:: vlantrunkportencapsulationopertype
            
            	The type of VLAN encapsulation in use on this trunk port. For intefaces with vlanTrunkPortDynamicStatus of notTrunking(2) the vlanTrunkPortEncapsulationOperType shall be notApplicable(6)
            	**type**\:  :py:class:`Vlantrunkportencapsulationopertype <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vlantrunkporttable.Vlantrunkportentry.Vlantrunkportencapsulationopertype>`
            
            .. attribute:: vlantrunkportvlansenabled2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 1024 through 2047 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 1024 through 1031; the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet. If the bit corresponding to a VLAN is set to '1', then the local system is enabled for sending and receiving frames on that VLAN; if the bit is set to '0', then the system is disabled from sending and receiving frames on that VLAN. The default value is zero length string.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: vlantrunkportvlansenabled3k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 3071 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet. If the bit corresponding to a VLAN is set to '1', then the local system is enabled for sending and receiving frames on that VLAN; if the bit is set to '0', then the system is disabled from sending and receiving frames on that VLAN. The default value is zero length string.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: vlantrunkportvlansenabled4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 3072 through 4095 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 3072 through 3079; the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet. If the bit corresponding to a VLAN is set to '1', then the local system is enabled for sending and receiving frames on that VLAN; if the bit is set to '0', then the system is disabled from sending and receiving frames on that VLAN. The default value is zero length string.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: vtpvlanspruningeligible2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 1024 through 2047 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 1024 through 1031; the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local system is permitted to prune that VLAN on this trunk port; if the bit is set to '0', then the system must not prune that VLAN on this trunk port. The default value is zero length string.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: vtpvlanspruningeligible3k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 3071 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local system is permitted to prune that VLAN on this trunk port; if the bit is set to '0', then the system must not prune that VLAN on this trunk port. The default value is zero length string.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: vtpvlanspruningeligible4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 3072 through 4095 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 3072 through 3079; the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local system is permitted to prune that VLAN on this trunk port; if the bit is set to '0', then the system must not prune that VLAN on this trunk port. The default value is zero length string.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: vlantrunkportvlansxmitjoined2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 1024 through 2047 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 1024 through 1031; the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then this VLAN is presently being forwarded on this trunk port, i.e., it is not pruned; if the bit is set to '0', then this VLAN is presently not being forwarded on this trunk port, either because it is pruned or for some other reason
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: vlantrunkportvlansxmitjoined3k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 3071 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then this VLAN is presently being forwarded on this trunk port, i.e., it is not pruned; if the bit is set to '0', then this VLAN is presently not being forwarded on this trunk port, either because it is pruned or for some other reason
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: vlantrunkportvlansxmitjoined4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 3072 through 4095 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 3072 through 3079; the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then this VLAN is presently being forwarded on this trunk port, i.e., it is not pruned; if the bit is set to '0', then this VLAN is presently not being forwarded on this trunk port, either because it is pruned or for some other reason
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: vlantrunkportvlansrcvjoined2k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 1024 through 2047 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 1024 through 1031; the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local switch is currently sending joins for this VLAN on this trunk port, i.e., it is asking to receive frames for this VLAN; if the bit is set to '0', then the local switch is not currently sending joins for this VLAN on this trunk port
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: vlantrunkportvlansrcvjoined3k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 2048 through 3071 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 2048 through 2055; the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local switch is currently sending joins for this VLAN on this trunk port, i.e., it is asking to receive frames for this VLAN; if the bit is set to '0', then the local switch is not currently sending joins for this VLAN on this trunk port
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: vlantrunkportvlansrcvjoined4k
            
            	A string of octets containing one bit per VLAN for VLANS with VlanIndex values of 3072 through 4095 in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 3072 through 3079; the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  If the bit corresponding to a VLAN is set to '1', then the local switch is currently sending joins for this VLAN on this trunk port, i.e., it is asking to receive frames for this VLAN; if the bit is set to '0', then the local switch is not currently sending joins for this VLAN on this trunk port
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: vlantrunkportdot1qtunnel
            
            	Indicates dot1qtunnel mode of the port.  If the portDot1qTunnel  is set to 'trunk' mode, the port's vlanTrunkPortDynamicState will be changed to 'onNoNegotiate' and the vlanTrunkPortEncapsulationType will be set to 'dot1Q'. These values cannot be changed unless dot1q tunnel is disabled on this port.  If the portDot1qTunnel mode is set to 'access' mode, the port's vlanTrunkPortDynamicState will be set to 'off'.And the value of vlanTrunkPortDynamicState cannot be changed unless dot1q tunnel is disabled on this port. 1Q packets received on this access port will remain.  Setting the port to dot1q tunnel 'disabled' mode causes the dot1q tunnel feature to be disabled on this port.  This object can't be set to 'trunk' or 'access' mode, when vlanTrunkPortsDot1qTag  object is set to 'false'.  This object has been deprecated and is replaced by the object 'cltcDot1qTunnelMode' in the CISCO\-L2\-TUNNEL\-CONFIG\-MIB
            	**type**\:  :py:class:`Vlantrunkportdot1Qtunnel <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vlantrunkporttable.Vlantrunkportentry.Vlantrunkportdot1Qtunnel>`
            
            	**status**\: deprecated
            
            .. attribute:: vlantrunkportvlansactivefirst2k
            
            	A string of octets containing one bit per VLAN with VlanIndex values of 0 through 2047.  If the bit corresponding to a VLAN is set to 1, it indicates that vlan is allowed and active in management domain.  If the bit corresponding to a VLAN is set to 0, it indicates that vlan is not allowed or not active in management domain
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: vlantrunkportvlansactivesecond2k
            
            	A string of octets containing one bit per VLAN with VlanIndex values of 2048 through 4095.  If the bit corresponding to a VLAN is set to 1, it indicates that vlan is allowed and active in management domain.  If the bit corresponding to a VLAN is set to 0, it indicates that vlan is not allowed or not active in management domain
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: stpxpreferredvlansmap
            
            	A string of octets containing one bit per VLAN in the management domain on this trunk port.  The first octet corresponds to VLANs with VlanIndex values of 0 through 7; the second octet to VLANs 8 through 15; etc.  The most significant bit of each octet corresponds to the lowest value VlanIndex in that octet.  For each VLAN, if it is preferred on this trunk port, then the bit corresponding to that VLAN is set to '1'. The default value is 128 bytes of zeros.  To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**length:** 128
            
            .. attribute:: stpxpreferredvlansmap2k
            
            	A string of octets containing one bit per VLAN for VLANS  with VlanIndex values of 1024 through 2047 in the management domain on this trunk port.  The first octet corresponds to  VLANs with VlanIndex values of 1024 through 1031;  the second octet to VLANs 1032 through 1039; etc.  The most significant bit of each octet corresponds to the  lowest value VlanIndex in that octet.   For each VLAN, if it is preferred on this trunk port, then  the bit corresponding to that VLAN is set to '1'.  The default value is 128 bytes of zeros.   To avoid conflicts between overlapping partial updates by  multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of  vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: stpxpreferredvlansmap3k
            
            	A string of octets containing one bit per VLAN for VLANS  with VlanIndex values of 2048 through 3071 in the management domain on this trunk port.  The first octet corresponds to  VLANs with VlanIndex values of 2048 through 2055;  the second octet to VLANs 2056 through 2063; etc.  The most significant bit of each octet corresponds to the  lowest value VlanIndex in that octet.   For each VLAN, if it is preferred on this trunk port, then  the bit corresponding to that VLAN is set to '1'.  The default value is 128 bytes of zeros.   To avoid conflicts between overlapping partial updates by  multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of  vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: stpxpreferredvlansmap4k
            
            	A string of octets containing one bit per VLAN for VLANS  with VlanIndex values of 3072 through 4095 in the management domain on this trunk port.  The first octet corresponds to  VLANs with VlanIndex values of 3072 through 3079;  the second octet to VLANs 3080 through 3087; etc.  The most significant bit of each octet corresponds to the  lowest value VlanIndex in that octet.   For each VLAN, if it is preferred on this trunk port, then  the bit corresponding to that VLAN is set to '1'.  The default value is 128 bytes of zeros.   To avoid conflicts between overlapping partial updates by  multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single VLAN on the trunk port), any SNMP Set operation accessing an instance of this object should also write the value of  vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**length:** 0..128
            
            .. attribute:: stpxpreferredmistpinstancesmap
            
            	A string of octets containing one bit per MISTP instances  in the management domain on this trunk port. The first octet corresponds to MISTP instances with InstIndex values of 1  through 8; the second octet to MISTP instances 9 through 16; etc. The most significant bit of each octet corresponds to  the lowest value instanceIndex in that octet. The number of  bits for this mib object will be determined by the value of  stpxMISTPInstanceNumber.  For each instance, if it is preferred on this trunk port, then the bit corresponding to that instance is set to '1'.   To avoid conflicts between overlapping partial updates by multiple managers, i.e., updates which modify only a portion of an instance of this object (e.g., enable/disable a single instance on the trunk port), any SNMP Set operation  accessing an instance of this object should also write the  value of vlanTrunkPortSetSerialNo
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: stpxpreferredmstinstancesmap
            
            	A string of octets containing one bit per MST instances  on this trunk port.  The first octet corresponds to MST  instances of 0 through 7; the second octet to MST instances  8 through 15; etc. The most significant bit of each octet  corresponds to the lowest MST instance value in that octet.  The number of bits for this mib object will be determined  by the value of stpxMSTMaxInstanceNumber.  For each instance, if it is preferred on this trunk port,  then the bit corresponding to that instance is set to '1'
            	**type**\: str
            
            	**length:** 1..32
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-VTP-MIB'
            _revision = '2013-10-14'

            def __init__(self):
                super(CISCOVTPMIB.Vlantrunkporttable.Vlantrunkportentry, self).__init__()

                self.yang_name = "vlanTrunkPortEntry"
                self.yang_parent_name = "vlanTrunkPortTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vlantrunkportifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('vlantrunkportifindex', YLeaf(YType.int32, 'vlanTrunkPortIfIndex')),
                    ('vlantrunkportmanagementdomain', YLeaf(YType.int32, 'vlanTrunkPortManagementDomain')),
                    ('vlantrunkportencapsulationtype', YLeaf(YType.enumeration, 'vlanTrunkPortEncapsulationType')),
                    ('vlantrunkportvlansenabled', YLeaf(YType.str, 'vlanTrunkPortVlansEnabled')),
                    ('vlantrunkportnativevlan', YLeaf(YType.int32, 'vlanTrunkPortNativeVlan')),
                    ('vlantrunkportrowstatus', YLeaf(YType.enumeration, 'vlanTrunkPortRowStatus')),
                    ('vlantrunkportinjoins', YLeaf(YType.uint32, 'vlanTrunkPortInJoins')),
                    ('vlantrunkportoutjoins', YLeaf(YType.uint32, 'vlanTrunkPortOutJoins')),
                    ('vlantrunkportoldadverts', YLeaf(YType.uint32, 'vlanTrunkPortOldAdverts')),
                    ('vlantrunkportvlanspruningeligible', YLeaf(YType.str, 'vlanTrunkPortVlansPruningEligible')),
                    ('vlantrunkportvlansxmitjoined', YLeaf(YType.str, 'vlanTrunkPortVlansXmitJoined')),
                    ('vlantrunkportvlansrcvjoined', YLeaf(YType.str, 'vlanTrunkPortVlansRcvJoined')),
                    ('vlantrunkportdynamicstate', YLeaf(YType.enumeration, 'vlanTrunkPortDynamicState')),
                    ('vlantrunkportdynamicstatus', YLeaf(YType.enumeration, 'vlanTrunkPortDynamicStatus')),
                    ('vlantrunkportvtpenabled', YLeaf(YType.boolean, 'vlanTrunkPortVtpEnabled')),
                    ('vlantrunkportencapsulationopertype', YLeaf(YType.enumeration, 'vlanTrunkPortEncapsulationOperType')),
                    ('vlantrunkportvlansenabled2k', YLeaf(YType.str, 'vlanTrunkPortVlansEnabled2k')),
                    ('vlantrunkportvlansenabled3k', YLeaf(YType.str, 'vlanTrunkPortVlansEnabled3k')),
                    ('vlantrunkportvlansenabled4k', YLeaf(YType.str, 'vlanTrunkPortVlansEnabled4k')),
                    ('vtpvlanspruningeligible2k', YLeaf(YType.str, 'vtpVlansPruningEligible2k')),
                    ('vtpvlanspruningeligible3k', YLeaf(YType.str, 'vtpVlansPruningEligible3k')),
                    ('vtpvlanspruningeligible4k', YLeaf(YType.str, 'vtpVlansPruningEligible4k')),
                    ('vlantrunkportvlansxmitjoined2k', YLeaf(YType.str, 'vlanTrunkPortVlansXmitJoined2k')),
                    ('vlantrunkportvlansxmitjoined3k', YLeaf(YType.str, 'vlanTrunkPortVlansXmitJoined3k')),
                    ('vlantrunkportvlansxmitjoined4k', YLeaf(YType.str, 'vlanTrunkPortVlansXmitJoined4k')),
                    ('vlantrunkportvlansrcvjoined2k', YLeaf(YType.str, 'vlanTrunkPortVlansRcvJoined2k')),
                    ('vlantrunkportvlansrcvjoined3k', YLeaf(YType.str, 'vlanTrunkPortVlansRcvJoined3k')),
                    ('vlantrunkportvlansrcvjoined4k', YLeaf(YType.str, 'vlanTrunkPortVlansRcvJoined4k')),
                    ('vlantrunkportdot1qtunnel', YLeaf(YType.enumeration, 'vlanTrunkPortDot1qTunnel')),
                    ('vlantrunkportvlansactivefirst2k', YLeaf(YType.str, 'vlanTrunkPortVlansActiveFirst2k')),
                    ('vlantrunkportvlansactivesecond2k', YLeaf(YType.str, 'vlanTrunkPortVlansActiveSecond2k')),
                    ('stpxpreferredvlansmap', YLeaf(YType.str, 'CISCO-STP-EXTENSIONS-MIB:stpxPreferredVlansMap')),
                    ('stpxpreferredvlansmap2k', YLeaf(YType.str, 'CISCO-STP-EXTENSIONS-MIB:stpxPreferredVlansMap2k')),
                    ('stpxpreferredvlansmap3k', YLeaf(YType.str, 'CISCO-STP-EXTENSIONS-MIB:stpxPreferredVlansMap3k')),
                    ('stpxpreferredvlansmap4k', YLeaf(YType.str, 'CISCO-STP-EXTENSIONS-MIB:stpxPreferredVlansMap4k')),
                    ('stpxpreferredmistpinstancesmap', YLeaf(YType.str, 'CISCO-STP-EXTENSIONS-MIB:stpxPreferredMISTPInstancesMap')),
                    ('stpxpreferredmstinstancesmap', YLeaf(YType.str, 'CISCO-STP-EXTENSIONS-MIB:stpxPreferredMSTInstancesMap')),
                ])
                self.vlantrunkportifindex = None
                self.vlantrunkportmanagementdomain = None
                self.vlantrunkportencapsulationtype = None
                self.vlantrunkportvlansenabled = None
                self.vlantrunkportnativevlan = None
                self.vlantrunkportrowstatus = None
                self.vlantrunkportinjoins = None
                self.vlantrunkportoutjoins = None
                self.vlantrunkportoldadverts = None
                self.vlantrunkportvlanspruningeligible = None
                self.vlantrunkportvlansxmitjoined = None
                self.vlantrunkportvlansrcvjoined = None
                self.vlantrunkportdynamicstate = None
                self.vlantrunkportdynamicstatus = None
                self.vlantrunkportvtpenabled = None
                self.vlantrunkportencapsulationopertype = None
                self.vlantrunkportvlansenabled2k = None
                self.vlantrunkportvlansenabled3k = None
                self.vlantrunkportvlansenabled4k = None
                self.vtpvlanspruningeligible2k = None
                self.vtpvlanspruningeligible3k = None
                self.vtpvlanspruningeligible4k = None
                self.vlantrunkportvlansxmitjoined2k = None
                self.vlantrunkportvlansxmitjoined3k = None
                self.vlantrunkportvlansxmitjoined4k = None
                self.vlantrunkportvlansrcvjoined2k = None
                self.vlantrunkportvlansrcvjoined3k = None
                self.vlantrunkportvlansrcvjoined4k = None
                self.vlantrunkportdot1qtunnel = None
                self.vlantrunkportvlansactivefirst2k = None
                self.vlantrunkportvlansactivesecond2k = None
                self.stpxpreferredvlansmap = None
                self.stpxpreferredvlansmap2k = None
                self.stpxpreferredvlansmap3k = None
                self.stpxpreferredvlansmap4k = None
                self.stpxpreferredmistpinstancesmap = None
                self.stpxpreferredmstinstancesmap = None
                self._segment_path = lambda: "vlanTrunkPortEntry" + "[vlanTrunkPortIfIndex='" + str(self.vlantrunkportifindex) + "']"
                self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/vlanTrunkPortTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVTPMIB.Vlantrunkporttable.Vlantrunkportentry, ['vlantrunkportifindex', 'vlantrunkportmanagementdomain', 'vlantrunkportencapsulationtype', 'vlantrunkportvlansenabled', 'vlantrunkportnativevlan', 'vlantrunkportrowstatus', 'vlantrunkportinjoins', 'vlantrunkportoutjoins', 'vlantrunkportoldadverts', 'vlantrunkportvlanspruningeligible', 'vlantrunkportvlansxmitjoined', 'vlantrunkportvlansrcvjoined', 'vlantrunkportdynamicstate', 'vlantrunkportdynamicstatus', 'vlantrunkportvtpenabled', 'vlantrunkportencapsulationopertype', 'vlantrunkportvlansenabled2k', 'vlantrunkportvlansenabled3k', 'vlantrunkportvlansenabled4k', 'vtpvlanspruningeligible2k', 'vtpvlanspruningeligible3k', 'vtpvlanspruningeligible4k', 'vlantrunkportvlansxmitjoined2k', 'vlantrunkportvlansxmitjoined3k', 'vlantrunkportvlansxmitjoined4k', 'vlantrunkportvlansrcvjoined2k', 'vlantrunkportvlansrcvjoined3k', 'vlantrunkportvlansrcvjoined4k', 'vlantrunkportdot1qtunnel', 'vlantrunkportvlansactivefirst2k', 'vlantrunkportvlansactivesecond2k', 'stpxpreferredvlansmap', 'stpxpreferredvlansmap2k', 'stpxpreferredvlansmap3k', 'stpxpreferredvlansmap4k', 'stpxpreferredmistpinstancesmap', 'stpxpreferredmstinstancesmap'], name, value)

            class Vlantrunkportdot1Qtunnel(Enum):
                """
                Vlantrunkportdot1Qtunnel (Enum Class)

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
                Vlantrunkportdynamicstate (Enum Class)

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
                Vlantrunkportdynamicstatus (Enum Class)

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
                Vlantrunkportencapsulationopertype (Enum Class)

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
                Vlantrunkportencapsulationtype (Enum Class)

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



    class Vtpdiscovertable(Entity):
        """
        This table contains information related to the discovery
        of the VTP members in the designated management
        domain. This table is not instantiated when 
        managementDomainVersionInUse is version1(1), version2(3)
        or none(3).
        
        .. attribute:: vtpdiscoverentry
        
        	Information related to the discovery of the VTP members in one management domain
        	**type**\: list of  		 :py:class:`Vtpdiscoverentry <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpdiscovertable.Vtpdiscoverentry>`
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CISCOVTPMIB.Vtpdiscovertable, self).__init__()

            self.yang_name = "vtpDiscoverTable"
            self.yang_parent_name = "CISCO-VTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("vtpDiscoverEntry", ("vtpdiscoverentry", CISCOVTPMIB.Vtpdiscovertable.Vtpdiscoverentry))])
            self._leafs = OrderedDict()

            self.vtpdiscoverentry = YList(self)
            self._segment_path = lambda: "vtpDiscoverTable"
            self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVTPMIB.Vtpdiscovertable, [], name, value)


        class Vtpdiscoverentry(Entity):
            """
            Information related to the discovery of the
            VTP members in one management domain.
            
            .. attribute:: managementdomainindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..255
            
            	**refers to**\:  :py:class:`managementdomainindex <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Managementdomaintable.Managementdomainentry>`
            
            .. attribute:: vtpdiscoveraction
            
            	When this object is set to discover(1), all the entries in vtpDiscoverResultTable for the corresponding management domain will be removed  and the local device will begin to discover all VTP members in the management domain. Upon the successful completion of discovery, the discovered result will be stored in the vtpDiscoverResultTable.  If vtpDiscoverStatus is inProgress(1), setting  vtpDiscoverAction to discover(1) will fail.   When this object is set to purgeResult(3),  all the entries of vtpDiscoverResultTable for  the corresponding management domain will be removed from vtpDiscoverResultTable.  When this object is set to noOperation(2), no action will be taken. When read, this object always returns noOperation(2)
            	**type**\:  :py:class:`Vtpdiscoveraction <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpdiscovertable.Vtpdiscoverentry.Vtpdiscoveraction>`
            
            .. attribute:: vtpdiscoverstatus
            
            	The current status of VTP discovery.  inProgress \- a discovery is in progress;  succeeded \- the discovery was completed successfully             (this value is also used when              no discover has been invoked since the             last time the local system restarted);  resourceUnavailable \- the discovery failed because             the required allocation of a resource is             presently unavailable.  someOtherError \- 'the discovery failed due to a             reason no listed
            	**type**\:  :py:class:`Vtpdiscoverstatus <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpdiscovertable.Vtpdiscoverentry.Vtpdiscoverstatus>`
            
            .. attribute:: vtplastdiscovertime
            
            	The value of sysUpTime at which the last discovery was completed.  A value of zero indicates that no discovery has been invoked since last time the local system restarted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-VTP-MIB'
            _revision = '2013-10-14'

            def __init__(self):
                super(CISCOVTPMIB.Vtpdiscovertable.Vtpdiscoverentry, self).__init__()

                self.yang_name = "vtpDiscoverEntry"
                self.yang_parent_name = "vtpDiscoverTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['managementdomainindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('managementdomainindex', YLeaf(YType.str, 'managementDomainIndex')),
                    ('vtpdiscoveraction', YLeaf(YType.enumeration, 'vtpDiscoverAction')),
                    ('vtpdiscoverstatus', YLeaf(YType.enumeration, 'vtpDiscoverStatus')),
                    ('vtplastdiscovertime', YLeaf(YType.uint32, 'vtpLastDiscoverTime')),
                ])
                self.managementdomainindex = None
                self.vtpdiscoveraction = None
                self.vtpdiscoverstatus = None
                self.vtplastdiscovertime = None
                self._segment_path = lambda: "vtpDiscoverEntry" + "[managementDomainIndex='" + str(self.managementdomainindex) + "']"
                self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/vtpDiscoverTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVTPMIB.Vtpdiscovertable.Vtpdiscoverentry, ['managementdomainindex', 'vtpdiscoveraction', 'vtpdiscoverstatus', 'vtplastdiscovertime'], name, value)

            class Vtpdiscoveraction(Enum):
                """
                Vtpdiscoveraction (Enum Class)

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
                Vtpdiscoverstatus (Enum Class)

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



    class Vtpdiscoverresulttable(Entity):
        """
        The table containing information of discovered VTP members
        in the management domain in which the local system is
        participating. This table is not instantiated when 
        managementDomainVersionInUse is version1(1), version2(2) or
        none(3).
        
        .. attribute:: vtpdiscoverresultentry
        
        	A conceptual row is created for each VTP member which is found through successful discovery
        	**type**\: list of  		 :py:class:`Vtpdiscoverresultentry <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpdiscoverresulttable.Vtpdiscoverresultentry>`
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CISCOVTPMIB.Vtpdiscoverresulttable, self).__init__()

            self.yang_name = "vtpDiscoverResultTable"
            self.yang_parent_name = "CISCO-VTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("vtpDiscoverResultEntry", ("vtpdiscoverresultentry", CISCOVTPMIB.Vtpdiscoverresulttable.Vtpdiscoverresultentry))])
            self._leafs = OrderedDict()

            self.vtpdiscoverresultentry = YList(self)
            self._segment_path = lambda: "vtpDiscoverResultTable"
            self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVTPMIB.Vtpdiscoverresulttable, [], name, value)


        class Vtpdiscoverresultentry(Entity):
            """
            A conceptual row is created for each VTP member which
            is found through successful discovery.
            
            .. attribute:: managementdomainindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..255
            
            	**refers to**\:  :py:class:`managementdomainindex <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Managementdomaintable.Managementdomainentry>`
            
            .. attribute:: vtpdiscoverresultindex  (key)
            
            	A value assigned by the system which identifies a VTP member and the associated database in the  management domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpdiscoverresultdatabasename
            
            	The database name associated with the discovered VTP member
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: vtpdiscoverresultconflicting
            
            	Indicates whether this VTP member contains conflicting information.  true(1) indicates that this member has conflicting  information of the database type in the management domain.  false(2) indicates that there is no conflicting information of the database type in the management domain
            	**type**\: bool
            
            .. attribute:: vtpdiscoverresultdeviceid
            
            	The unique identifier of the device for this VTP member
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: vtpdiscoverresultprimaryserver
            
            	The unique identifier of the primary server for this VTP member and the associated database type.  There are two different VTP servers, the primary server and the secondary server.  When a local device is configured as a server for a certain database type, it becomes secondary server by default.  Primary server is an operational role under which a server can initiate or change the VTP configuration of the database type.  If this VTP member itself is the primary server, the    value of this object is the same as the value of  vtpDiscoverResultDeviceId of the instance
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: vtpdiscoverresultrevnumber
            
            	The current configuration revision number as known by the VTP member. When the database type is unknown for the VTP member, this value is 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpdiscoverresultsystemname
            
            	sysName of the VTP member
            	**type**\: str
            
            	**length:** 0..64
            
            

            """

            _prefix = 'CISCO-VTP-MIB'
            _revision = '2013-10-14'

            def __init__(self):
                super(CISCOVTPMIB.Vtpdiscoverresulttable.Vtpdiscoverresultentry, self).__init__()

                self.yang_name = "vtpDiscoverResultEntry"
                self.yang_parent_name = "vtpDiscoverResultTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['managementdomainindex','vtpdiscoverresultindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('managementdomainindex', YLeaf(YType.str, 'managementDomainIndex')),
                    ('vtpdiscoverresultindex', YLeaf(YType.uint32, 'vtpDiscoverResultIndex')),
                    ('vtpdiscoverresultdatabasename', YLeaf(YType.str, 'vtpDiscoverResultDatabaseName')),
                    ('vtpdiscoverresultconflicting', YLeaf(YType.boolean, 'vtpDiscoverResultConflicting')),
                    ('vtpdiscoverresultdeviceid', YLeaf(YType.str, 'vtpDiscoverResultDeviceId')),
                    ('vtpdiscoverresultprimaryserver', YLeaf(YType.str, 'vtpDiscoverResultPrimaryServer')),
                    ('vtpdiscoverresultrevnumber', YLeaf(YType.uint32, 'vtpDiscoverResultRevNumber')),
                    ('vtpdiscoverresultsystemname', YLeaf(YType.str, 'vtpDiscoverResultSystemName')),
                ])
                self.managementdomainindex = None
                self.vtpdiscoverresultindex = None
                self.vtpdiscoverresultdatabasename = None
                self.vtpdiscoverresultconflicting = None
                self.vtpdiscoverresultdeviceid = None
                self.vtpdiscoverresultprimaryserver = None
                self.vtpdiscoverresultrevnumber = None
                self.vtpdiscoverresultsystemname = None
                self._segment_path = lambda: "vtpDiscoverResultEntry" + "[managementDomainIndex='" + str(self.managementdomainindex) + "']" + "[vtpDiscoverResultIndex='" + str(self.vtpdiscoverresultindex) + "']"
                self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/vtpDiscoverResultTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVTPMIB.Vtpdiscoverresulttable.Vtpdiscoverresultentry, ['managementdomainindex', 'vtpdiscoverresultindex', 'vtpdiscoverresultdatabasename', 'vtpdiscoverresultconflicting', 'vtpdiscoverresultdeviceid', 'vtpdiscoverresultprimaryserver', 'vtpdiscoverresultrevnumber', 'vtpdiscoverresultsystemname'], name, value)


    class Vtpdatabasetable(Entity):
        """
        This table contains information of the VTP
        databases. It is not instantiated when
        managementDomainVersionInUse is version1(1), 
        version2(3) or none(3).
        
        .. attribute:: vtpdatabaseentry
        
        	Information about the status of the VTP database in the domain.  Each VTP database type known to the local device type has an entry in this table. An entry is also created for unknown database which is notified through VTP advertisements from other VTP servers
        	**type**\: list of  		 :py:class:`Vtpdatabaseentry <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpdatabasetable.Vtpdatabaseentry>`
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CISCOVTPMIB.Vtpdatabasetable, self).__init__()

            self.yang_name = "vtpDatabaseTable"
            self.yang_parent_name = "CISCO-VTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("vtpDatabaseEntry", ("vtpdatabaseentry", CISCOVTPMIB.Vtpdatabasetable.Vtpdatabaseentry))])
            self._leafs = OrderedDict()

            self.vtpdatabaseentry = YList(self)
            self._segment_path = lambda: "vtpDatabaseTable"
            self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVTPMIB.Vtpdatabasetable, [], name, value)


        class Vtpdatabaseentry(Entity):
            """
            Information about the status of the VTP database
            in the domain.  Each VTP database type known to the
            local device type has an entry in this table.
            An entry is also created for unknown database which is
            notified through VTP advertisements from other VTP
            servers.
            
            .. attribute:: managementdomainindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..255
            
            	**refers to**\:  :py:class:`managementdomainindex <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Managementdomaintable.Managementdomainentry>`
            
            .. attribute:: vtpdatabaseindex  (key)
            
            	A value assigned by the system which uniquely identifies a VTP database in the local system
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpdatabasename
            
            	The name of the database
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: vtpdatabaselocalmode
            
            	The local VTP mode for a particular database type in this administrative domain.  \- 'client' indicates that the local system is acting   as a VTP client of the database type.  \- 'server' indicates that the local system is acting   as a VTP server of the database type.  \- 'transparent' indicates that the local system does   not generate or listen to VTP messages of this    database type, but forwards   messages. This mode can also be set by the device   itself when the size of database is too large for it   to hold in DRAM.  \- 'off' indicates that the local system does not   generate, listen to or forward any VTP messages   of this database type.  The default mode is 'client' for the database type  known to the local device and 'transparent' for the unknown database type
            	**type**\:  :py:class:`Vtpdatabaselocalmode <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpdatabasetable.Vtpdatabaseentry.Vtpdatabaselocalmode>`
            
            .. attribute:: vtpdatabaserevnumber
            
            	The current configuration revision number as known by the local device for this VTP 3 database type in the management domain.  This value is updated (if necessary) whenever a  VTP advertisement for the database type is received  or generated. When the database type is unknown to the  local device or no VTP advertisement for the database type is received or generated, its value is 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vtpdatabaseprimaryserver
            
            	There are two kinds of VTP version 3 servers for a certain database type \- the primary server and the secondary server. When a local device is configured as a server for a certain database type, it becomes secondary server by default. Primary server is an operational role under which a server can initiate or change the VTP configuration of the database type.  A true(1) value indicates that the local device is the  primary server of the database type in the management domain. A false(2) value indicates that the local device is not the primary server, or the database type is unknown to the local device
            	**type**\: bool
            
            .. attribute:: vtpdatabaseprimaryserverid
            
            	The unique identifier of the primary server in the management domain for the database type.   If no primary server is discovered for the database type, the object has a value of zero length string
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: vtpdatabasetakeoverprimary
            
            	There are two kinds of VTP version 3 servers for a certain database type \- the primary server and the secondary server. When a local device is configured as a server for a certain database type, it becomes secondary server by default. Primary server is an operational role under which a server can initiate or change the VTP configuration of the database type.  Setting this object to a true(1) value will advertise the configuration of this database type to the whole domain.  In order to successfully setting this object to true(1), the value of vtpDatabaseLocalMode must be server(2). Besides that, when the VTP password is hidden from the configuration file, the password (vtpDatabaseTakeOverPassword) which  matches  the secret key (vtpAuthSecretKey) must be provided in the same data packet.   When read, the object always returns false(2)
            	**type**\: bool
            
            .. attribute:: vtpdatabasetakeoverpassword
            
            	When read, this object always returns the value of a zero\-length octet string.  In the case that the VTP password is hidden from the  configuration and the local device intends to take over the whole domain, this object must be  set to the matching password with the secret key  (vtpAuthSecretKey) in the same data packet as which  the vtpDatabaseTakeOverPrimary is in. In all the  other situations, setting a valid value to this object  has no impact on the system
            	**type**\: str
            
            	**length:** 0..64
            
            

            """

            _prefix = 'CISCO-VTP-MIB'
            _revision = '2013-10-14'

            def __init__(self):
                super(CISCOVTPMIB.Vtpdatabasetable.Vtpdatabaseentry, self).__init__()

                self.yang_name = "vtpDatabaseEntry"
                self.yang_parent_name = "vtpDatabaseTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['managementdomainindex','vtpdatabaseindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('managementdomainindex', YLeaf(YType.str, 'managementDomainIndex')),
                    ('vtpdatabaseindex', YLeaf(YType.uint32, 'vtpDatabaseIndex')),
                    ('vtpdatabasename', YLeaf(YType.str, 'vtpDatabaseName')),
                    ('vtpdatabaselocalmode', YLeaf(YType.enumeration, 'vtpDatabaseLocalMode')),
                    ('vtpdatabaserevnumber', YLeaf(YType.uint32, 'vtpDatabaseRevNumber')),
                    ('vtpdatabaseprimaryserver', YLeaf(YType.boolean, 'vtpDatabasePrimaryServer')),
                    ('vtpdatabaseprimaryserverid', YLeaf(YType.str, 'vtpDatabasePrimaryServerId')),
                    ('vtpdatabasetakeoverprimary', YLeaf(YType.boolean, 'vtpDatabaseTakeOverPrimary')),
                    ('vtpdatabasetakeoverpassword', YLeaf(YType.str, 'vtpDatabaseTakeOverPassword')),
                ])
                self.managementdomainindex = None
                self.vtpdatabaseindex = None
                self.vtpdatabasename = None
                self.vtpdatabaselocalmode = None
                self.vtpdatabaserevnumber = None
                self.vtpdatabaseprimaryserver = None
                self.vtpdatabaseprimaryserverid = None
                self.vtpdatabasetakeoverprimary = None
                self.vtpdatabasetakeoverpassword = None
                self._segment_path = lambda: "vtpDatabaseEntry" + "[managementDomainIndex='" + str(self.managementdomainindex) + "']" + "[vtpDatabaseIndex='" + str(self.vtpdatabaseindex) + "']"
                self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/vtpDatabaseTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVTPMIB.Vtpdatabasetable.Vtpdatabaseentry, ['managementdomainindex', 'vtpdatabaseindex', 'vtpdatabasename', 'vtpdatabaselocalmode', 'vtpdatabaserevnumber', 'vtpdatabaseprimaryserver', 'vtpdatabaseprimaryserverid', 'vtpdatabasetakeoverprimary', 'vtpdatabasetakeoverpassword'], name, value)

            class Vtpdatabaselocalmode(Enum):
                """
                Vtpdatabaselocalmode (Enum Class)

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
        	**type**\: list of  		 :py:class:`Vtpauthentry <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpauthenticationtable.Vtpauthentry>`
        
        

        """

        _prefix = 'CISCO-VTP-MIB'
        _revision = '2013-10-14'

        def __init__(self):
            super(CISCOVTPMIB.Vtpauthenticationtable, self).__init__()

            self.yang_name = "vtpAuthenticationTable"
            self.yang_parent_name = "CISCO-VTP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("vtpAuthEntry", ("vtpauthentry", CISCOVTPMIB.Vtpauthenticationtable.Vtpauthentry))])
            self._leafs = OrderedDict()

            self.vtpauthentry = YList(self)
            self._segment_path = lambda: "vtpAuthenticationTable"
            self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVTPMIB.Vtpauthenticationtable, [], name, value)


        class Vtpauthentry(Entity):
            """
            Information about the status of the VTP
            authentication information in one domain.
            
            .. attribute:: managementdomainindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..255
            
            	**refers to**\:  :py:class:`managementdomainindex <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Managementdomaintable.Managementdomainentry>`
            
            .. attribute:: vtpauthpassword
            
            	By default, this object has a value of a zero\-length character string and is considered to be not configured.  The device uses the password to generate the  secret key. It can be stored in the configuration in  plain text or hidden from the configuration. If a VTP  server intends to modify the database's configuration in the domain but the password was hidden from the configuration, the same password (vtpDatabaseTakeOverPassword) as the hidden one has to be provided.  When this object is set alone, vtpAuthPasswordType is set to plaintext(1) automatically by the system. Setting this object to a zero length character string resets the password to its default value and the password is considered as not configured.  This object is not allowed to be set at the same time when  vtpAuthSecretKey is set.  When the vtpAuthPasswordType is hidden(2), this object  will return a zero\-length character string when read
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: vtpauthpasswordtype
            
            	By default this object has the value as plaintext(1) and the VTP password is stored in the configuration file in plain text.  Setting this object to hidden(2) will hide the password from the configuration.  Once this object is set to hidden(2), it cannot be set to plaintext(1) alone. However, it may be set to plaintext(1) at the same time the password is set
            	**type**\:  :py:class:`Vtpauthpasswordtype <ydk.models.cisco_ios_xe.CISCO_VTP_MIB.CISCOVTPMIB.Vtpauthenticationtable.Vtpauthentry.Vtpauthpasswordtype>`
            
            .. attribute:: vtpauthsecretkey
            
            	The device creating or modifying the VTP configuration signs it using the MD5 digest generated from the secret key before advertising it. Other devices in the domain receiving this configuration use the same secret key to accept it if it was correctly signed or drop it  otherwise.  By default, the object has the value as a zero\-length string and this value is read only. It is set  to this value automatically when the password  (vtpAuthPassword) is set to a zero\-length octet string.  The secret key can be either generated using the password or configured by the user. Once the secret key is configured by the user, it is stored as a hexadecimal string in the device's configuration and the password is considered to be the secret key's matching password and hidden from the configuration automatically.  This object is not allowed to be set at the same time when vtpAuthPassword is set.  The secret key is overwritten by a newly generated secret key when the password is re\-configured
            	**type**\: str
            
            	**length:** 0 \| 16
            
            

            """

            _prefix = 'CISCO-VTP-MIB'
            _revision = '2013-10-14'

            def __init__(self):
                super(CISCOVTPMIB.Vtpauthenticationtable.Vtpauthentry, self).__init__()

                self.yang_name = "vtpAuthEntry"
                self.yang_parent_name = "vtpAuthenticationTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['managementdomainindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('managementdomainindex', YLeaf(YType.str, 'managementDomainIndex')),
                    ('vtpauthpassword', YLeaf(YType.str, 'vtpAuthPassword')),
                    ('vtpauthpasswordtype', YLeaf(YType.enumeration, 'vtpAuthPasswordType')),
                    ('vtpauthsecretkey', YLeaf(YType.str, 'vtpAuthSecretKey')),
                ])
                self.managementdomainindex = None
                self.vtpauthpassword = None
                self.vtpauthpasswordtype = None
                self.vtpauthsecretkey = None
                self._segment_path = lambda: "vtpAuthEntry" + "[managementDomainIndex='" + str(self.managementdomainindex) + "']"
                self._absolute_path = lambda: "CISCO-VTP-MIB:CISCO-VTP-MIB/vtpAuthenticationTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVTPMIB.Vtpauthenticationtable.Vtpauthentry, ['managementdomainindex', 'vtpauthpassword', 'vtpauthpasswordtype', 'vtpauthsecretkey'], name, value)

            class Vtpauthpasswordtype(Enum):
                """
                Vtpauthpasswordtype (Enum Class)

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


    def clone_ptr(self):
        self._top_entity = CISCOVTPMIB()
        return self._top_entity


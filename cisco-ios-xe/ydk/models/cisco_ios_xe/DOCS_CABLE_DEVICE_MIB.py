""" DOCS_CABLE_DEVICE_MIB 

This is the MIB Module for DOCSIS\-compliant cable modems
and cable\-modem termination systems.

Copyright (C) The IETF Trust (2006).  This version
of this MIB module was published in RFC 4639; for full
legal notices see the RFC itself.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class DOCSCABLEDEVICEMIB(Entity):
    """
    
    
    .. attribute:: docsdevbase
    
    	
    	**type**\:  :py:class:`DocsDevBase <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevBase>`
    
    .. attribute:: docsdevsoftware
    
    	
    	**type**\:  :py:class:`DocsDevSoftware <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevSoftware>`
    
    .. attribute:: docsdevserver
    
    	
    	**type**\:  :py:class:`DocsDevServer <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevServer>`
    
    .. attribute:: docsdevevent
    
    	
    	**type**\:  :py:class:`DocsDevEvent <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevEvent>`
    
    .. attribute:: docsdevfilter
    
    	
    	**type**\:  :py:class:`DocsDevFilter <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevFilter>`
    
    .. attribute:: docsdevcpe
    
    	
    	**type**\:  :py:class:`DocsDevCpe <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevCpe>`
    
    .. attribute:: docsdevnmaccesstable
    
    	This table controls access to SNMP objects by network management stations.  If the table is empty, access to SNMP objects is unrestricted.  The objects in this table MUST NOT persist across reboots.  The objects in this table are only accessible from cable devices that are not capable of operating in SNMP Coexistence mode (RFC 3584) or in SNMPv3 mode (RFC 3410). See the conformance section for details.  Note that some devices are required by other specifications (e.g., the DOCSIS OSSIv1.1 specification) to support the legacy SNMPv1/v2c docsDevNmAccess mode for backward compatibility.  This table is deprecated.  Instead, use the SNMP coexistence MIBs from RFC 3584, the TARGET and NOTIFICATION MIBs from RFC 3413, and the View\-Based Access Control Model (VACM) MIBs for all SNMP protocol versions from RFC 3415
    	**type**\:  :py:class:`DocsDevNmAccessTable <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevNmAccessTable>`
    
    	**status**\: deprecated
    
    .. attribute:: docsdevevcontroltable
    
    	This table allows control of the reporting of event classes.  For each event priority, a combination of logging and reporting mechanisms may be chosen.  The mapping of event types to priorities is vendor dependent.  Vendors may also choose to allow the user to control that mapping through proprietary means.  Table entries MUST persist across reboots for CMTS devices and MUST NOT persist across reboots for CM devices
    	**type**\:  :py:class:`DocsDevEvControlTable <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevEvControlTable>`
    
    .. attribute:: docsdeveventtable
    
    	Contains a log of network and device events that may be of interest in fault isolation and troubleshooting. If the local(0) bit is set in docsDevEvReporting, entries in this table MUST persist across reboots
    	**type**\:  :py:class:`DocsDevEventTable <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevEventTable>`
    
    .. attribute:: docsdevfilterllctable
    
    	A list of filters to apply to (bridged) LLC traffic. The filters in this table are applied to incoming traffic on the appropriate interface(s)  prior to any further processing (e.g., before the packet is handed off for level 3 processing, or for bridging). The specific action taken when no filter is matched is controlled by docsDevFilterLLCUnmatchedAction.  Table entries MUST NOT persist across reboots for any device
    	**type**\:  :py:class:`DocsDevFilterLLCTable <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevFilterLLCTable>`
    
    .. attribute:: docsdevfilteriptable
    
    	An ordered list of filters or classifiers to apply to IP traffic. Filter application is ordered by the filter index, rather than by a best match algorithm (Note that this implies that the filter table may have gaps in the index values).  Packets that match no filters will have policy 0 in the docsDevFilterPolicyTable applied to them, if it exists.  Otherwise, Packets that match no filters are discarded or forwarded according to the setting of docsDevFilterIpDefault.  Any IP packet can theoretically match multiple rows of this table.  When considering a packet, the table is scanned in row index order (e.g., filter 10 is checked before filter 20).  If the packet matches that filter (which means that it matches ALL criteria for that row), actions appropriate to docsDevFilterIpControl and docsDevFilterPolicyId are taken.  If the packet was discarded processing is complete.  If docsDevFilterIpContinue is set to true, the filter comparison continues with the next row in the table, looking for additional matches.  If the packet matches no filter in the table, the packet is accepted or dropped for further processing according to the setting of docsDevFilterIpDefault. If the packet is accepted, the actions specified by policy group 0 (e.g., the rows in docsDevFilterPolicyTable that have a value of 0 for docsDevFilterPolicyId) are taken, if that policy group exists.  Logically, this table is consulted twice during the processing of any IP packet\: once upon its acceptance from the L2 entity, and once upon its transmission to the L2 entity.  In actuality, for cable modems, IP filtering is generally the only IP processing done for transit traffic.  This means that inbound and outbound filtering can generally be done at the same time with one pass through the filter table.  The objects in this table are only accessible from cable devices that are not operating in DiffServ MIB mode (RFC 3289).  See the conformance section for details.  Note that some devices are required by other specifications (e.g., the DOCSIS OSSIv1.1 specification) to support the legacy SNMPv1/v2c docsDevFilter mode for backward compatibility.  Table entries MUST NOT persist across reboots for any device.  This table is deprecated.  Instead, use the DiffServ MIB from RFC3289
    	**type**\:  :py:class:`DocsDevFilterIpTable <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevFilterIpTable>`
    
    	**status**\: deprecated
    
    .. attribute:: docsdevfilterpolicytable
    
    	A Table that maps between a policy group ID and a set of pointers to policies to be applied.  All rows with the same docsDevFilterPolicyId are part of the same group of policy pointers and are applied in the order in this table.  docsDevFilterPolicyTable exists to allow multiple policy actions (referenced by policy pointers) to be applied to any given classified packet. The policy actions are applied in index order. For example\:  Index   ID    Type    Action  1      1      TOS     1  9      5      TOS     1  12     1      IPSEC   3  This says that a packet that matches a filter with policy id 1 first has TOS policy 1 applied (which might set the TOS bits to enable a higher priority) and next has the IPSEC policy 3 applied (which may result in the packets being dumped into a secure VPN to a remote encryptor).  Policy ID 0 is reserved for default actions and is applied only to packets that match no filters in docsDevFilterIpTable.  Table entries MUST NOT persist across reboots for any device.  This table is deprecated.  Instead, use the DiffServ MIB from RFC3289
    	**type**\:  :py:class:`DocsDevFilterPolicyTable <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevFilterPolicyTable>`
    
    	**status**\: deprecated
    
    .. attribute:: docsdevfiltertostable
    
    	Table used to describe Type of Service (TOS) bits processing.  This table is an adjunct to the docsDevFilterIpTable and the docsDevFilterPolicy table.  Entries in the latter table can point to specific rows in this (and other) tables and cause specific actions to be taken. This table permits the manipulation of the value of the Type of Service bits in the IP header of the matched packet as follows\:  Set the tosBits of the packet to    (tosBits & docsDevFilterTosAndMask) \|    docsDevFilterTosOrMask  This construct allows you to do a clear and set of all the TOS bits in a flexible manner.  Table entries MUST NOT persist across reboots for any device.  This table is deprecated.  Instead, use the DiffServ MIB from RFC3289
    	**type**\:  :py:class:`DocsDevFilterTosTable <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevFilterTosTable>`
    
    	**status**\: deprecated
    
    .. attribute:: docsdevcpetable
    
    	This table lists the IPv4 addresses seen (or permitted) as source addresses in packets originating from the customer interface on this device.  In addition, this table can be provisioned with the specific addresses permitted for the CPEs via the normal row creation mechanisms.  Table entries MUST NOT persist across reboots for any device.  N.B.  Management action can add entries in this table and in docsDevCpeIpTable past the value of docsDevCpeIpMax.  docsDevCpeIpMax ONLY restricts the ability of the CM to add learned addresses automatically.  This table is deprecated and is replaced by docsDevCpeInetTable
    	**type**\:  :py:class:`DocsDevCpeTable <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevCpeTable>`
    
    	**status**\: deprecated
    
    .. attribute:: docsdevcpeinettable
    
    	This table lists the IP addresses seen (or permitted) as source addresses in packets originating from the customer interface on this device.  In addition, this table can be provisioned with the specific addresses permitted for the CPEs via the normal row creation mechanisms.  N.B.  Management action can add entries in this table and in docsDevCpeIpTable past the value of docsDevCpeIpMax.  docsDevCpeIpMax ONLY restricts the ability of the CM to add learned addresses automatically.  Table entries MUST NOT persist across reboots for any device.  This table exactly mirrors docsDevCpeTable and applies to IPv4 and IPv6 addresses
    	**type**\:  :py:class:`DocsDevCpeInetTable <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevCpeInetTable>`
    
    

    """

    _prefix = 'DOCS-CABLE-DEVICE-MIB'
    _revision = '2006-12-20'

    def __init__(self):
        super(DOCSCABLEDEVICEMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "DOCS-CABLE-DEVICE-MIB"
        self.yang_parent_name = "DOCS-CABLE-DEVICE-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("docsDevBase", ("docsdevbase", DOCSCABLEDEVICEMIB.DocsDevBase)), ("docsDevSoftware", ("docsdevsoftware", DOCSCABLEDEVICEMIB.DocsDevSoftware)), ("docsDevServer", ("docsdevserver", DOCSCABLEDEVICEMIB.DocsDevServer)), ("docsDevEvent", ("docsdevevent", DOCSCABLEDEVICEMIB.DocsDevEvent)), ("docsDevFilter", ("docsdevfilter", DOCSCABLEDEVICEMIB.DocsDevFilter)), ("docsDevCpe", ("docsdevcpe", DOCSCABLEDEVICEMIB.DocsDevCpe)), ("docsDevNmAccessTable", ("docsdevnmaccesstable", DOCSCABLEDEVICEMIB.DocsDevNmAccessTable)), ("docsDevEvControlTable", ("docsdevevcontroltable", DOCSCABLEDEVICEMIB.DocsDevEvControlTable)), ("docsDevEventTable", ("docsdeveventtable", DOCSCABLEDEVICEMIB.DocsDevEventTable)), ("docsDevFilterLLCTable", ("docsdevfilterllctable", DOCSCABLEDEVICEMIB.DocsDevFilterLLCTable)), ("docsDevFilterIpTable", ("docsdevfilteriptable", DOCSCABLEDEVICEMIB.DocsDevFilterIpTable)), ("docsDevFilterPolicyTable", ("docsdevfilterpolicytable", DOCSCABLEDEVICEMIB.DocsDevFilterPolicyTable)), ("docsDevFilterTosTable", ("docsdevfiltertostable", DOCSCABLEDEVICEMIB.DocsDevFilterTosTable)), ("docsDevCpeTable", ("docsdevcpetable", DOCSCABLEDEVICEMIB.DocsDevCpeTable)), ("docsDevCpeInetTable", ("docsdevcpeinettable", DOCSCABLEDEVICEMIB.DocsDevCpeInetTable))])
        self._leafs = OrderedDict()

        self.docsdevbase = DOCSCABLEDEVICEMIB.DocsDevBase()
        self.docsdevbase.parent = self
        self._children_name_map["docsdevbase"] = "docsDevBase"

        self.docsdevsoftware = DOCSCABLEDEVICEMIB.DocsDevSoftware()
        self.docsdevsoftware.parent = self
        self._children_name_map["docsdevsoftware"] = "docsDevSoftware"

        self.docsdevserver = DOCSCABLEDEVICEMIB.DocsDevServer()
        self.docsdevserver.parent = self
        self._children_name_map["docsdevserver"] = "docsDevServer"

        self.docsdevevent = DOCSCABLEDEVICEMIB.DocsDevEvent()
        self.docsdevevent.parent = self
        self._children_name_map["docsdevevent"] = "docsDevEvent"

        self.docsdevfilter = DOCSCABLEDEVICEMIB.DocsDevFilter()
        self.docsdevfilter.parent = self
        self._children_name_map["docsdevfilter"] = "docsDevFilter"

        self.docsdevcpe = DOCSCABLEDEVICEMIB.DocsDevCpe()
        self.docsdevcpe.parent = self
        self._children_name_map["docsdevcpe"] = "docsDevCpe"

        self.docsdevnmaccesstable = DOCSCABLEDEVICEMIB.DocsDevNmAccessTable()
        self.docsdevnmaccesstable.parent = self
        self._children_name_map["docsdevnmaccesstable"] = "docsDevNmAccessTable"

        self.docsdevevcontroltable = DOCSCABLEDEVICEMIB.DocsDevEvControlTable()
        self.docsdevevcontroltable.parent = self
        self._children_name_map["docsdevevcontroltable"] = "docsDevEvControlTable"

        self.docsdeveventtable = DOCSCABLEDEVICEMIB.DocsDevEventTable()
        self.docsdeveventtable.parent = self
        self._children_name_map["docsdeveventtable"] = "docsDevEventTable"

        self.docsdevfilterllctable = DOCSCABLEDEVICEMIB.DocsDevFilterLLCTable()
        self.docsdevfilterllctable.parent = self
        self._children_name_map["docsdevfilterllctable"] = "docsDevFilterLLCTable"

        self.docsdevfilteriptable = DOCSCABLEDEVICEMIB.DocsDevFilterIpTable()
        self.docsdevfilteriptable.parent = self
        self._children_name_map["docsdevfilteriptable"] = "docsDevFilterIpTable"

        self.docsdevfilterpolicytable = DOCSCABLEDEVICEMIB.DocsDevFilterPolicyTable()
        self.docsdevfilterpolicytable.parent = self
        self._children_name_map["docsdevfilterpolicytable"] = "docsDevFilterPolicyTable"

        self.docsdevfiltertostable = DOCSCABLEDEVICEMIB.DocsDevFilterTosTable()
        self.docsdevfiltertostable.parent = self
        self._children_name_map["docsdevfiltertostable"] = "docsDevFilterTosTable"

        self.docsdevcpetable = DOCSCABLEDEVICEMIB.DocsDevCpeTable()
        self.docsdevcpetable.parent = self
        self._children_name_map["docsdevcpetable"] = "docsDevCpeTable"

        self.docsdevcpeinettable = DOCSCABLEDEVICEMIB.DocsDevCpeInetTable()
        self.docsdevcpeinettable.parent = self
        self._children_name_map["docsdevcpeinettable"] = "docsDevCpeInetTable"
        self._segment_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(DOCSCABLEDEVICEMIB, [], name, value)


    class DocsDevBase(Entity):
        """
        
        
        .. attribute:: docsdevrole
        
        	Defines the current role of this device.  cm(1) is a Cable Modem, cmtsActive(2) is a Cable Modem Termination System that is controlling the system of cable modems, and cmtsBackup(3) is a CMTS that is currently connected but is not controlling the system (not currently used).  In general, if this device is a 'cm', its role will not change during operation or between reboots.  If the device is a 'cmts' it may change between cmtsActive and cmtsBackup and back again during normal operation.  NB\: At this time, the DOCSIS standards do not support the concept of a backup CMTS, but cmtsBackup is included for completeness
        	**type**\:  :py:class:`DocsDevRole <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevBase.DocsDevRole>`
        
        .. attribute:: docsdevdatetime
        
        	The current date and time, with time zone information (if known).  If the real data and time cannot be determined, this shall represent elapsed time from boot relative to the standard epoch '1970\-1\-1,0\:0\:0.0'.  In other words, if this agent has been up for 3 minutes and not been able to determine what the actual date and time are, this object will return the value '1970\-1\-1,0\:03\:0.0'
        	**type**\: str
        
        .. attribute:: docsdevresetnow
        
        	Setting this object to true(1) causes the device to reset.  Reading this object always returns false(2)
        	**type**\: bool
        
        .. attribute:: docsdevserialnumber
        
        	The manufacturer's serial number for this device
        	**type**\: str
        
        .. attribute:: docsdevstpcontrol
        
        	This object controls operation of the spanning tree protocol (as distinguished from transparent bridging).  If set to stEnabled(1), then the spanning tree protocol is enabled, subject to bridging constraints. If noStFilterBpdu(2), then spanning tree is not active, and Bridge PDUs received are discarded.  If noStPassBpdu(3), then spanning tree is not active, and Bridge PDUs are transparently forwarded.  Note that a device need not implement all of these options, but that noStFilterBpdu(2) is required
        	**type**\:  :py:class:`DocsDevSTPControl <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevBase.DocsDevSTPControl>`
        
        .. attribute:: docsdevigmpmodecontrol
        
        	This object controls the IGMP mode of operation for the CM or CMTS.  In passive mode, the device forwards IGMP between interfaces as based on knowledge of Multicast Session activity on the subscriber side interface and the rules defined in the DOCSIS RFI specification.  In active mode, the device terminates at and initiates IGMP through its interfaces as based on the knowledge of Multicast Session activity on the subscriber side interface
        	**type**\:  :py:class:`DocsDevIgmpModeControl <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevBase.DocsDevIgmpModeControl>`
        
        .. attribute:: docsdevmaxcpe
        
        	The maximum number of CPEs that can be granted access through a CM during a CM epoch.  This value can be obtained from the CM configuration file; however, it may be adjusted by the CM according to hardware or software limitations that have been imposed on the implementation
        	**type**\: int
        
        	**range:** 0..255
        
        	**units**\: CPEs
        
        

        """

        _prefix = 'DOCS-CABLE-DEVICE-MIB'
        _revision = '2006-12-20'

        def __init__(self):
            super(DOCSCABLEDEVICEMIB.DocsDevBase, self).__init__()

            self.yang_name = "docsDevBase"
            self.yang_parent_name = "DOCS-CABLE-DEVICE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('docsdevrole', (YLeaf(YType.enumeration, 'docsDevRole'), [('ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB', 'DOCSCABLEDEVICEMIB', 'DocsDevBase.DocsDevRole')])),
                ('docsdevdatetime', (YLeaf(YType.str, 'docsDevDateTime'), ['str'])),
                ('docsdevresetnow', (YLeaf(YType.boolean, 'docsDevResetNow'), ['bool'])),
                ('docsdevserialnumber', (YLeaf(YType.str, 'docsDevSerialNumber'), ['str'])),
                ('docsdevstpcontrol', (YLeaf(YType.enumeration, 'docsDevSTPControl'), [('ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB', 'DOCSCABLEDEVICEMIB', 'DocsDevBase.DocsDevSTPControl')])),
                ('docsdevigmpmodecontrol', (YLeaf(YType.enumeration, 'docsDevIgmpModeControl'), [('ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB', 'DOCSCABLEDEVICEMIB', 'DocsDevBase.DocsDevIgmpModeControl')])),
                ('docsdevmaxcpe', (YLeaf(YType.uint32, 'docsDevMaxCpe'), ['int'])),
            ])
            self.docsdevrole = None
            self.docsdevdatetime = None
            self.docsdevresetnow = None
            self.docsdevserialnumber = None
            self.docsdevstpcontrol = None
            self.docsdevigmpmodecontrol = None
            self.docsdevmaxcpe = None
            self._segment_path = lambda: "docsDevBase"
            self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevBase, [u'docsdevrole', u'docsdevdatetime', u'docsdevresetnow', u'docsdevserialnumber', u'docsdevstpcontrol', u'docsdevigmpmodecontrol', u'docsdevmaxcpe'], name, value)

        class DocsDevIgmpModeControl(Enum):
            """
            DocsDevIgmpModeControl (Enum Class)

            This object controls the IGMP mode of operation for

            the CM or CMTS.  In passive mode, the device forwards

            IGMP between interfaces as based on knowledge of

            Multicast Session activity on the subscriber side

            interface and the rules defined in the DOCSIS RFI

            specification.  In active mode, the device terminates

            at and initiates IGMP through its interfaces as based

            on the knowledge of Multicast Session activity on the

            subscriber side interface.

            .. data:: passive = 1

            .. data:: active = 2

            """

            passive = Enum.YLeaf(1, "passive")

            active = Enum.YLeaf(2, "active")


        class DocsDevRole(Enum):
            """
            DocsDevRole (Enum Class)

            Defines the current role of this device.  cm(1) is a

            Cable Modem, cmtsActive(2) is a Cable Modem Termination

            System that is controlling the system of cable modems,

            and cmtsBackup(3) is a CMTS that is currently connected

            but is not controlling the system (not currently used).

            In general, if this device is a 'cm', its role will not

            change during operation or between reboots.  If the

            device is a 'cmts' it may change between cmtsActive and

            cmtsBackup and back again during normal operation.  NB\:

            At this time, the DOCSIS standards do not support the

            concept of a backup CMTS, but cmtsBackup is included for

            completeness.

            .. data:: cm = 1

            .. data:: cmtsActive = 2

            .. data:: cmtsBackup = 3

            """

            cm = Enum.YLeaf(1, "cm")

            cmtsActive = Enum.YLeaf(2, "cmtsActive")

            cmtsBackup = Enum.YLeaf(3, "cmtsBackup")


        class DocsDevSTPControl(Enum):
            """
            DocsDevSTPControl (Enum Class)

            This object controls operation of the spanning tree

            protocol (as distinguished from transparent bridging).

            If set to stEnabled(1), then the spanning tree protocol

            is enabled, subject to bridging constraints.

            If noStFilterBpdu(2), then spanning tree is not active,

            and Bridge PDUs received are discarded.

            If noStPassBpdu(3), then spanning tree is not active,

            and Bridge PDUs are transparently forwarded.

            Note that a device need not implement all of these

            options, but that noStFilterBpdu(2) is required.

            .. data:: stEnabled = 1

            .. data:: noStFilterBpdu = 2

            .. data:: noStPassBpdu = 3

            """

            stEnabled = Enum.YLeaf(1, "stEnabled")

            noStFilterBpdu = Enum.YLeaf(2, "noStFilterBpdu")

            noStPassBpdu = Enum.YLeaf(3, "noStPassBpdu")



    class DocsDevSoftware(Entity):
        """
        
        
        .. attribute:: docsdevswserver
        
        	The address of the TFTP server used for software upgrades.  If the TFTP server is unknown or is a non\-IPv4 address, return 0.0.0.0.  This object is deprecated.  See docsDevSwServerAddress for its replacement.  This object will have its value modified, given a valid SET to docsDevSwServerAddress
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**status**\: deprecated
        
        .. attribute:: docsdevswfilename
        
        	The filename of the software image to be downloaded via TFTP, or the abs\_path (as defined in RFC2616) of the software image to be downloaded via HTTP.  Unless set via SNMP, this is the filename or abs\_path specified by the provisioning server during the boot process  that corresponds to the software version that is desired for this device.  If unknown, the value of this object is the zero\-length string
        	**type**\: str
        
        	**length:** 0..64
        
        .. attribute:: docsdevswadminstatus
        
        	If set to upgradeFromMgt(1), the device will initiate a TFTP or HTTP software image download.  After successfully receiving an image, the device will set its state to ignoreProvisioningUpgrade(3) and reboot. If the download process is interrupted (e.g., by a reset or power failure), the device will load the previous image and, after re\-initialization, continue to attempt loading the image specified in docsDevSwFilename.  If set to allowProvisioningUpgrade(2), the device will use the software version information supplied by the provisioning server when next rebooting (this does not cause a reboot).  When set to ignoreProvisioningUpgrade(3), the device will disregard software image upgrade information from the provisioning server.  Note that reading this object can return upgradeFromMgt(1).  This indicates that a software download is currently in progress, and that the device will reboot after successfully receiving an image
        	**type**\:  :py:class:`DocsDevSwAdminStatus <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevSoftware.DocsDevSwAdminStatus>`
        
        .. attribute:: docsdevswoperstatus
        
        	InProgress(1) indicates that a TFTP or HTTP download is underway, either as a result of a version mismatch at provisioning or as a result of a upgradeFromMgt request. No other docsDevSw\* objects can be modified in this state.  CompleteFromProvisioning(2) indicates that the last software upgrade was a result of version mismatch at provisioning.  CompleteFromMgt(3) indicates that the last software upgrade was a result of setting docsDevSwAdminStatus to upgradeFromMgt.  Failed(4) indicates that the last attempted download failed, ordinarily due to TFTP or HTTP timeout
        	**type**\:  :py:class:`DocsDevSwOperStatus <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevSoftware.DocsDevSwOperStatus>`
        
        .. attribute:: docsdevswcurrentvers
        
        	The software version currently operating in this device. This string's syntax is that used by the individual vendor to identify software versions. For a CM, this string will describe the current software load.  For a CMTS, this object SHOULD contain a human\-readable representation either of the vendor specific designation of the software for the chassis, or of the software for the control processor.  If neither of these is applicable, the value MUST be a zero\-length string
        	**type**\: str
        
        .. attribute:: docsdevswserveraddresstype
        
        	The type of address of the TFTP or HTTP server used for software upgrades.  If docsDevSwServerTransportProtocol is currently set to tftp(1), attempting to set this object to dns(16) MUST result in an error
        	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
        
        .. attribute:: docsdevswserveraddress
        
        	The address of the TFTP or HTTP server used for software upgrades.  If the TFTP/HTTP server is unknown, return the zero\- length address string (see the TextualConvention).  If docsDevSwServer is also implemented in this agent, this object is tied to it.  A set of this object to an IPv4 address will result in also setting the value of docsDevSwServer to that address.  If this object is set to an IPv6 address, docsDevSwServer is set to 0.0.0.0. If docsDevSwServer is set, this object is also set to that value.  Note that if both are set in the same action, the order of which one sets the other is undefined
        	**type**\: str
        
        	**length:** 0..255
        
        .. attribute:: docsdevswservertransportprotocol
        
        	This object specifies the transport protocol (TFTP or HTTP) to be used for software upgrades.  If the value of this object is tftp(1), then the cable device uses TFTP (RFC1350) read request packets to download the docsDevSwFilename from the docsDevSwServerAddress in octet mode.  If the value of this object is http(2), then the cable device uses HTTP 1.0 (RFC1945) or HTTP 1.1 (RFC2616) GET requests sent to host docsDevSwServerAddress to download the software image from path docsDevSwFilename.  If docsDevSwServerAddressType is currently set to dns(16), attempting to set this object to tftp(1) MUST result in an error
        	**type**\:  :py:class:`DocsDevSwServerTransportProtocol <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevSoftware.DocsDevSwServerTransportProtocol>`
        
        

        """

        _prefix = 'DOCS-CABLE-DEVICE-MIB'
        _revision = '2006-12-20'

        def __init__(self):
            super(DOCSCABLEDEVICEMIB.DocsDevSoftware, self).__init__()

            self.yang_name = "docsDevSoftware"
            self.yang_parent_name = "DOCS-CABLE-DEVICE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('docsdevswserver', (YLeaf(YType.str, 'docsDevSwServer'), ['str'])),
                ('docsdevswfilename', (YLeaf(YType.str, 'docsDevSwFilename'), ['str'])),
                ('docsdevswadminstatus', (YLeaf(YType.enumeration, 'docsDevSwAdminStatus'), [('ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB', 'DOCSCABLEDEVICEMIB', 'DocsDevSoftware.DocsDevSwAdminStatus')])),
                ('docsdevswoperstatus', (YLeaf(YType.enumeration, 'docsDevSwOperStatus'), [('ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB', 'DOCSCABLEDEVICEMIB', 'DocsDevSoftware.DocsDevSwOperStatus')])),
                ('docsdevswcurrentvers', (YLeaf(YType.str, 'docsDevSwCurrentVers'), ['str'])),
                ('docsdevswserveraddresstype', (YLeaf(YType.enumeration, 'docsDevSwServerAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                ('docsdevswserveraddress', (YLeaf(YType.str, 'docsDevSwServerAddress'), ['str'])),
                ('docsdevswservertransportprotocol', (YLeaf(YType.enumeration, 'docsDevSwServerTransportProtocol'), [('ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB', 'DOCSCABLEDEVICEMIB', 'DocsDevSoftware.DocsDevSwServerTransportProtocol')])),
            ])
            self.docsdevswserver = None
            self.docsdevswfilename = None
            self.docsdevswadminstatus = None
            self.docsdevswoperstatus = None
            self.docsdevswcurrentvers = None
            self.docsdevswserveraddresstype = None
            self.docsdevswserveraddress = None
            self.docsdevswservertransportprotocol = None
            self._segment_path = lambda: "docsDevSoftware"
            self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevSoftware, [u'docsdevswserver', u'docsdevswfilename', u'docsdevswadminstatus', u'docsdevswoperstatus', u'docsdevswcurrentvers', u'docsdevswserveraddresstype', u'docsdevswserveraddress', u'docsdevswservertransportprotocol'], name, value)

        class DocsDevSwAdminStatus(Enum):
            """
            DocsDevSwAdminStatus (Enum Class)

            If set to upgradeFromMgt(1), the device will initiate a

            TFTP or HTTP software image download.  After

            successfully receiving an image, the device will set

            its state to ignoreProvisioningUpgrade(3) and reboot.

            If the download process is interrupted (e.g., by a reset

            or power failure), the device will load the previous

            image and, after re\-initialization, continue to attempt

            loading the image specified in docsDevSwFilename.

            If set to allowProvisioningUpgrade(2), the device will

            use the software version information supplied by the

            provisioning server when next rebooting (this does not

            cause a reboot).

            When set to ignoreProvisioningUpgrade(3), the device

            will disregard software image upgrade information

            from the provisioning server.

            Note that reading this object can return

            upgradeFromMgt(1).  This indicates that a software

            download is currently in progress, and that the device

            will reboot after successfully receiving an image.

            .. data:: upgradeFromMgt = 1

            .. data:: allowProvisioningUpgrade = 2

            .. data:: ignoreProvisioningUpgrade = 3

            """

            upgradeFromMgt = Enum.YLeaf(1, "upgradeFromMgt")

            allowProvisioningUpgrade = Enum.YLeaf(2, "allowProvisioningUpgrade")

            ignoreProvisioningUpgrade = Enum.YLeaf(3, "ignoreProvisioningUpgrade")


        class DocsDevSwOperStatus(Enum):
            """
            DocsDevSwOperStatus (Enum Class)

            InProgress(1) indicates that a TFTP or HTTP download is

            underway, either as a result of a version mismatch at

            provisioning or as a result of a upgradeFromMgt request.

            No other docsDevSw\* objects can be modified in

            this state.

            CompleteFromProvisioning(2) indicates that the last

            software upgrade was a result of version mismatch at

            provisioning.

            CompleteFromMgt(3) indicates that the last software

            upgrade was a result of setting docsDevSwAdminStatus to

            upgradeFromMgt.

            Failed(4) indicates that the last attempted download

            failed, ordinarily due to TFTP or HTTP timeout.

            .. data:: inProgress = 1

            .. data:: completeFromProvisioning = 2

            .. data:: completeFromMgt = 3

            .. data:: failed = 4

            .. data:: other = 5

            """

            inProgress = Enum.YLeaf(1, "inProgress")

            completeFromProvisioning = Enum.YLeaf(2, "completeFromProvisioning")

            completeFromMgt = Enum.YLeaf(3, "completeFromMgt")

            failed = Enum.YLeaf(4, "failed")

            other = Enum.YLeaf(5, "other")


        class DocsDevSwServerTransportProtocol(Enum):
            """
            DocsDevSwServerTransportProtocol (Enum Class)

            This object specifies the transport protocol (TFTP or

            HTTP) to be used for software upgrades.

            If the value of this object is tftp(1), then the cable

            device uses TFTP (RFC1350) read request packets to

            download the docsDevSwFilename from the

            docsDevSwServerAddress in octet mode.

            If the value of this object is http(2), then the cable

            device uses HTTP 1.0 (RFC1945) or HTTP 1.1 (RFC2616)

            GET requests sent to host docsDevSwServerAddress to

            download the software image from path docsDevSwFilename.

            If docsDevSwServerAddressType is currently set to

            dns(16), attempting to set this object to tftp(1) MUST

            result in an error.

            .. data:: tftp = 1

            .. data:: http = 2

            """

            tftp = Enum.YLeaf(1, "tftp")

            http = Enum.YLeaf(2, "http")



    class DocsDevServer(Entity):
        """
        
        
        .. attribute:: docsdevserverbootstate
        
        	If operational(1), the device has completed loading and processing of configuration parameters, and the CMTS has completed the Registration exchange.  If disabled(2), then the device was administratively disabled, possibly by being refused network access in the configuration file.  If waitingForDhcpOffer(3), then a Dynamic Host Configuration Protocol (DHCP) Discover has been transmitted, and no offer has yet been received.  If waitingForDhcpResponse(4), then a DHCP Request has been transmitted, and no response has yet been received.  If waitingForTimeServer(5), then a Time Request has been transmitted, and no response has yet been received. If waitingForTftp(6), then a request to the TFTP parameter server has been made, and no response received.  If refusedByCmts(7), then the Registration Request/Response exchange with the CMTS failed.  If forwardingDenied(8), then the registration process was completed, but the network access option in the received configuration file prohibits forwarding.  If other(9), then the registration process reached a point that does not fall into one of the above categories.  If unknown(10), then the device has not yet begun the registration process or is in some other indeterminate state
        	**type**\:  :py:class:`DocsDevServerBootState <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevServer.DocsDevServerBootState>`
        
        .. attribute:: docsdevserverdhcp
        
        	The IP address of the DHCP server that assigned an IP address to this device. Returns 0.0.0.0 if DHCP is not used for IP address assignment, or if this agent is not assigned an IPv4 address.  This object is deprecated and is replaced by docsDevServerDhcpAddress
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**status**\: deprecated
        
        .. attribute:: docsdevservertime
        
        	The IP address of the Time server (RFC 0868).  Returns 0.0.0.0 if the time server IP address is unknown, or if the time server is not an IPv4 server.  This object is deprecated and is replaced by docsDevServerTimeAddress
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**status**\: deprecated
        
        .. attribute:: docsdevservertftp
        
        	The IP address of the TFTP server responsible for downloading provisioning and configuration parameters to this device. Returns 0.0.0.0 if the TFTP server address is unknown or is not an IPv4 address.  This object is deprecated and is replaced by docsDevServerConfigTftpAddress
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**status**\: deprecated
        
        .. attribute:: docsdevserverconfigfile
        
        	The name of the device configuration file read from the TFTP server.  Returns a zero\-length string if the configuration file name is unknown
        	**type**\: str
        
        .. attribute:: docsdevserverdhcpaddresstype
        
        	The type of address of docsDevServerDhcpAddress.  If DHCP was not used, this value should return unknown(0)
        	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
        
        .. attribute:: docsdevserverdhcpaddress
        
        	The internet address of the DHCP server that assigned an IP address to this device. Returns the zero length octet string if DHCP was not used for IP address assignment
        	**type**\: str
        
        	**length:** 0..255
        
        .. attribute:: docsdevservertimeaddresstype
        
        	The type of address of docsDevServerTimeAddress.  If no time server exists, this value should return unknown(0)
        	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
        
        .. attribute:: docsdevservertimeaddress
        
        	The Internet address of the RFC 868 Time server, as provided by DHCP option 4.  Note that if multiple values are provided to the CM in DHCP option 4, the value of this MIB object MUST be the Time server address from which the Time of Day reference was acquired as based on the DOCSIS RFI specification.  During the period of time where the Time of Day have not been acquired, the Time server address reported by the CM may report the first address value in the DHCP option value or the last server address the CM attempted to get the Time of day value.  Returns the zero\-length octet string if the time server IP address is not provisioned
        	**type**\: str
        
        	**length:** 0..255
        
        .. attribute:: docsdevserverconfigtftpaddresstype
        
        	The type of address of docsDevServerConfigTftpAddress. If no TFTP server exists, this value should return unknown(0)
        	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
        
        .. attribute:: docsdevserverconfigtftpaddress
        
        	The internet address of the TFTP server responsible for downloading provisioning and configuration parameters to this device.  Returns the zero\-length octet string if the config server address is unknown.  There are certain security risks that are involved with using TFTP
        	**type**\: str
        
        	**length:** 0..255
        
        

        """

        _prefix = 'DOCS-CABLE-DEVICE-MIB'
        _revision = '2006-12-20'

        def __init__(self):
            super(DOCSCABLEDEVICEMIB.DocsDevServer, self).__init__()

            self.yang_name = "docsDevServer"
            self.yang_parent_name = "DOCS-CABLE-DEVICE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('docsdevserverbootstate', (YLeaf(YType.enumeration, 'docsDevServerBootState'), [('ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB', 'DOCSCABLEDEVICEMIB', 'DocsDevServer.DocsDevServerBootState')])),
                ('docsdevserverdhcp', (YLeaf(YType.str, 'docsDevServerDhcp'), ['str'])),
                ('docsdevservertime', (YLeaf(YType.str, 'docsDevServerTime'), ['str'])),
                ('docsdevservertftp', (YLeaf(YType.str, 'docsDevServerTftp'), ['str'])),
                ('docsdevserverconfigfile', (YLeaf(YType.str, 'docsDevServerConfigFile'), ['str'])),
                ('docsdevserverdhcpaddresstype', (YLeaf(YType.enumeration, 'docsDevServerDhcpAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                ('docsdevserverdhcpaddress', (YLeaf(YType.str, 'docsDevServerDhcpAddress'), ['str'])),
                ('docsdevservertimeaddresstype', (YLeaf(YType.enumeration, 'docsDevServerTimeAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                ('docsdevservertimeaddress', (YLeaf(YType.str, 'docsDevServerTimeAddress'), ['str'])),
                ('docsdevserverconfigtftpaddresstype', (YLeaf(YType.enumeration, 'docsDevServerConfigTftpAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                ('docsdevserverconfigtftpaddress', (YLeaf(YType.str, 'docsDevServerConfigTftpAddress'), ['str'])),
            ])
            self.docsdevserverbootstate = None
            self.docsdevserverdhcp = None
            self.docsdevservertime = None
            self.docsdevservertftp = None
            self.docsdevserverconfigfile = None
            self.docsdevserverdhcpaddresstype = None
            self.docsdevserverdhcpaddress = None
            self.docsdevservertimeaddresstype = None
            self.docsdevservertimeaddress = None
            self.docsdevserverconfigtftpaddresstype = None
            self.docsdevserverconfigtftpaddress = None
            self._segment_path = lambda: "docsDevServer"
            self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevServer, [u'docsdevserverbootstate', u'docsdevserverdhcp', u'docsdevservertime', u'docsdevservertftp', u'docsdevserverconfigfile', u'docsdevserverdhcpaddresstype', u'docsdevserverdhcpaddress', u'docsdevservertimeaddresstype', u'docsdevservertimeaddress', u'docsdevserverconfigtftpaddresstype', u'docsdevserverconfigtftpaddress'], name, value)

        class DocsDevServerBootState(Enum):
            """
            DocsDevServerBootState (Enum Class)

            If operational(1), the device has completed loading and

            processing of configuration parameters, and the CMTS has

            completed the Registration exchange.

            If disabled(2), then the device was administratively

            disabled, possibly by being refused network access in

            the configuration file.

            If waitingForDhcpOffer(3), then a Dynamic Host

            Configuration Protocol (DHCP) Discover has been

            transmitted, and no offer has yet been received.

            If waitingForDhcpResponse(4), then a DHCP Request has

            been transmitted, and no response has yet been received.

            If waitingForTimeServer(5), then a Time Request has been

            transmitted, and no response has yet been received.

            If waitingForTftp(6), then a request to the TFTP

            parameter server has been made, and no response

            received.

            If refusedByCmts(7), then the Registration

            Request/Response exchange with the CMTS failed.

            If forwardingDenied(8), then the registration process

            was completed, but the network access option in the

            received configuration file prohibits forwarding.

            If other(9), then the registration process reached a

            point that does not fall into one of the above

            categories.

            If unknown(10), then the device has not yet begun the

            registration process or is in some other indeterminate

            state.

            .. data:: operational = 1

            .. data:: disabled = 2

            .. data:: waitingForDhcpOffer = 3

            .. data:: waitingForDhcpResponse = 4

            .. data:: waitingForTimeServer = 5

            .. data:: waitingForTftp = 6

            .. data:: refusedByCmts = 7

            .. data:: forwardingDenied = 8

            .. data:: other = 9

            .. data:: unknown = 10

            """

            operational = Enum.YLeaf(1, "operational")

            disabled = Enum.YLeaf(2, "disabled")

            waitingForDhcpOffer = Enum.YLeaf(3, "waitingForDhcpOffer")

            waitingForDhcpResponse = Enum.YLeaf(4, "waitingForDhcpResponse")

            waitingForTimeServer = Enum.YLeaf(5, "waitingForTimeServer")

            waitingForTftp = Enum.YLeaf(6, "waitingForTftp")

            refusedByCmts = Enum.YLeaf(7, "refusedByCmts")

            forwardingDenied = Enum.YLeaf(8, "forwardingDenied")

            other = Enum.YLeaf(9, "other")

            unknown = Enum.YLeaf(10, "unknown")



    class DocsDevEvent(Entity):
        """
        
        
        .. attribute:: docsdevevcontrol
        
        	Setting this object to resetLog(1) empties the event log.  All data is deleted.  Setting it to useDefaultReporting(2) returns all event priorities to their factory\-default reporting.  Reading this object always returns useDefaultReporting(2)
        	**type**\:  :py:class:`DocsDevEvControl <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevEvent.DocsDevEvControl>`
        
        .. attribute:: docsdevevsyslog
        
        	The IP address of the Syslog server. If 0.0.0.0, either syslog transmission is inhibited, or the Syslog server address is not an IPv4 address.  This object is deprecated and is replaced by docsDevEvSyslogAddress
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        	**status**\: deprecated
        
        .. attribute:: docsdevevthrottleadminstatus
        
        	Controls the transmission of traps and syslog messages with respect to the trap pacing threshold.  unconstrained(1) causes traps and syslog messages to be transmitted without regard to the threshold settings.  maintainBelowThreshold(2) causes trap transmission and syslog messages to be suppressed if the number of traps would otherwise exceed the threshold.  stopAtThreshold(3) causes trap transmission to cease at the threshold and not to resume until directed to do so.  inhibited(4) causes all trap transmission and syslog messages to be suppressed.  A single event is always treated as a single event for threshold counting.  That is, an event causing both a trap and a syslog message is still treated as a single event.  Writing to this object resets the thresholding state
        	**type**\:  :py:class:`DocsDevEvThrottleAdminStatus <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevEvent.DocsDevEvThrottleAdminStatus>`
        
        .. attribute:: docsdevevthrottleinhibited
        
        	If true(1), trap and syslog transmission is currently inhibited due to thresholds and/or the current setting of docsDevEvThrottleAdminStatus.  In addition, this is true(1) when transmission is inhibited because no syslog (docsDevEvSyslog) or trap (docsDevNmAccessEntry) destinations have been set.  This object is deprecated and is replaced by docsDevEvThrottleThresholdExceeded
        	**type**\: bool
        
        	**status**\: deprecated
        
        .. attribute:: docsdevevthrottlethreshold
        
        	Number of events per docsDevEvThrottleInterval permitted before throttling is to occur.  A single event, whether the notification could result in messages transmitted using syslog, SNMP, or both protocols, and regardless of the number of destinations, (including zero) is always treated as a single event for threshold counting.  For example, an event causing both a trap and a syslog message is still treated as a single event.  All system notifications that occur within the device should be taken into consideration when calculating and monitoring the threshold
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: events
        
        .. attribute:: docsdevevthrottleinterval
        
        	The interval over which docsDevEvThrottleThreshold applies
        	**type**\: int
        
        	**range:** 1..2147483647
        
        	**units**\: seconds
        
        .. attribute:: docsdevevsyslogaddresstype
        
        	The type of address of docsDevEvSyslogAddress.  If no syslog server exists, this value should return unknown(0)
        	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
        
        .. attribute:: docsdevevsyslogaddress
        
        	The Internet address of the Syslog server, as provided by DHCP option 7 or set via SNMP management.  If the address of the server is set to the zero\-length string, the 0.0.0.0 IPv4 address, or the 0\: IPv6 address, Syslog transmission is inhibited.  Note that if multiple values are provided to the CM in DHCP option 7, the value of this MIB object MUST be the first Syslog server address received.  By default at agent boot, this object returns the zero length string
        	**type**\: str
        
        	**length:** 0..255
        
        .. attribute:: docsdevevthrottlethresholdexceeded
        
        	If true(1), trap and syslog transmission is currently inhibited due to exceeding the trap/syslog event threshold in the current interval
        	**type**\: bool
        
        

        """

        _prefix = 'DOCS-CABLE-DEVICE-MIB'
        _revision = '2006-12-20'

        def __init__(self):
            super(DOCSCABLEDEVICEMIB.DocsDevEvent, self).__init__()

            self.yang_name = "docsDevEvent"
            self.yang_parent_name = "DOCS-CABLE-DEVICE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('docsdevevcontrol', (YLeaf(YType.enumeration, 'docsDevEvControl'), [('ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB', 'DOCSCABLEDEVICEMIB', 'DocsDevEvent.DocsDevEvControl')])),
                ('docsdevevsyslog', (YLeaf(YType.str, 'docsDevEvSyslog'), ['str'])),
                ('docsdevevthrottleadminstatus', (YLeaf(YType.enumeration, 'docsDevEvThrottleAdminStatus'), [('ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB', 'DOCSCABLEDEVICEMIB', 'DocsDevEvent.DocsDevEvThrottleAdminStatus')])),
                ('docsdevevthrottleinhibited', (YLeaf(YType.boolean, 'docsDevEvThrottleInhibited'), ['bool'])),
                ('docsdevevthrottlethreshold', (YLeaf(YType.uint32, 'docsDevEvThrottleThreshold'), ['int'])),
                ('docsdevevthrottleinterval', (YLeaf(YType.int32, 'docsDevEvThrottleInterval'), ['int'])),
                ('docsdevevsyslogaddresstype', (YLeaf(YType.enumeration, 'docsDevEvSyslogAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                ('docsdevevsyslogaddress', (YLeaf(YType.str, 'docsDevEvSyslogAddress'), ['str'])),
                ('docsdevevthrottlethresholdexceeded', (YLeaf(YType.boolean, 'docsDevEvThrottleThresholdExceeded'), ['bool'])),
            ])
            self.docsdevevcontrol = None
            self.docsdevevsyslog = None
            self.docsdevevthrottleadminstatus = None
            self.docsdevevthrottleinhibited = None
            self.docsdevevthrottlethreshold = None
            self.docsdevevthrottleinterval = None
            self.docsdevevsyslogaddresstype = None
            self.docsdevevsyslogaddress = None
            self.docsdevevthrottlethresholdexceeded = None
            self._segment_path = lambda: "docsDevEvent"
            self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevEvent, [u'docsdevevcontrol', u'docsdevevsyslog', u'docsdevevthrottleadminstatus', u'docsdevevthrottleinhibited', u'docsdevevthrottlethreshold', u'docsdevevthrottleinterval', u'docsdevevsyslogaddresstype', u'docsdevevsyslogaddress', u'docsdevevthrottlethresholdexceeded'], name, value)

        class DocsDevEvControl(Enum):
            """
            DocsDevEvControl (Enum Class)

            Setting this object to resetLog(1) empties the event

            log.  All data is deleted.  Setting it to

            useDefaultReporting(2) returns all event priorities to

            their factory\-default reporting.  Reading this object

            always returns useDefaultReporting(2).

            .. data:: resetLog = 1

            .. data:: useDefaultReporting = 2

            """

            resetLog = Enum.YLeaf(1, "resetLog")

            useDefaultReporting = Enum.YLeaf(2, "useDefaultReporting")


        class DocsDevEvThrottleAdminStatus(Enum):
            """
            DocsDevEvThrottleAdminStatus (Enum Class)

            Controls the transmission of traps and syslog messages

            with respect to the trap pacing threshold.

            unconstrained(1) causes traps and syslog messages to be

            transmitted without regard to the threshold settings.

            maintainBelowThreshold(2) causes trap transmission and

            syslog messages to be suppressed if the number of traps

            would otherwise exceed the threshold.

            stopAtThreshold(3) causes trap transmission to cease at

            the threshold and not to resume until directed to do so.

            inhibited(4) causes all trap transmission and syslog

            messages to be suppressed.

            A single event is always treated as a single event for

            threshold counting.  That is, an event causing both a

            trap and a syslog message is still treated as a single

            event.

            Writing to this object resets the thresholding state.

            .. data:: unconstrained = 1

            .. data:: maintainBelowThreshold = 2

            .. data:: stopAtThreshold = 3

            .. data:: inhibited = 4

            """

            unconstrained = Enum.YLeaf(1, "unconstrained")

            maintainBelowThreshold = Enum.YLeaf(2, "maintainBelowThreshold")

            stopAtThreshold = Enum.YLeaf(3, "stopAtThreshold")

            inhibited = Enum.YLeaf(4, "inhibited")



    class DocsDevFilter(Entity):
        """
        
        
        .. attribute:: docsdevfilterllcunmatchedaction
        
        	LLC (Link Level Control) filters can be defined on an inclusive or exclusive basis\: CMs can be configured to forward only packets matching a set of layer three protocols, or to drop packets matching a set of layer three protocols.  Typical use of these filters is to filter out possibly harmful (given the context of a large metropolitan LAN) protocols.  If set to discard(1), any L2 packet that does not match at least one filter in the docsDevFilterLLCTable will be discarded.  If set to accept(2), any L2 packet that does not match at least one filter in the docsDevFilterLLCTable will be accepted for further processing (e.g., bridging).  In other words, if the packet does not match an entry in the table, it takes this action; if it does match an entry in the table, it takes the opposite of this action
        	**type**\:  :py:class:`DocsDevFilterLLCUnmatchedAction <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevFilter.DocsDevFilterLLCUnmatchedAction>`
        
        .. attribute:: docsdevfilteripdefault
        
        	The default behavior for (bridged) packets that do not match IP filters (or Internet filters, if implemented) is defined by docsDevFilterIpDefault.  If set to discard(1), all packets not matching an IP filter in docsDevFilterIpTable will be discarded.  If set to accept(2), all packets not matching an IP filter or an Internet filter will be accepted for further processing (e.g., bridging)
        	**type**\:  :py:class:`DocsDevFilterIpDefault <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevFilter.DocsDevFilterIpDefault>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'DOCS-CABLE-DEVICE-MIB'
        _revision = '2006-12-20'

        def __init__(self):
            super(DOCSCABLEDEVICEMIB.DocsDevFilter, self).__init__()

            self.yang_name = "docsDevFilter"
            self.yang_parent_name = "DOCS-CABLE-DEVICE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('docsdevfilterllcunmatchedaction', (YLeaf(YType.enumeration, 'docsDevFilterLLCUnmatchedAction'), [('ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB', 'DOCSCABLEDEVICEMIB', 'DocsDevFilter.DocsDevFilterLLCUnmatchedAction')])),
                ('docsdevfilteripdefault', (YLeaf(YType.enumeration, 'docsDevFilterIpDefault'), [('ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB', 'DOCSCABLEDEVICEMIB', 'DocsDevFilter.DocsDevFilterIpDefault')])),
            ])
            self.docsdevfilterllcunmatchedaction = None
            self.docsdevfilteripdefault = None
            self._segment_path = lambda: "docsDevFilter"
            self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevFilter, [u'docsdevfilterllcunmatchedaction', u'docsdevfilteripdefault'], name, value)

        class DocsDevFilterIpDefault(Enum):
            """
            DocsDevFilterIpDefault (Enum Class)

            The default behavior for (bridged) packets that do not

            match IP filters (or Internet filters, if implemented)

            is defined by docsDevFilterIpDefault.

            If set to discard(1), all packets not matching an IP

            filter in docsDevFilterIpTable will be discarded.  If

            set to accept(2), all packets not matching an IP filter

            or an Internet filter will be accepted for further

            processing (e.g., bridging).

            .. data:: discard = 1

            .. data:: accept = 2

            """

            discard = Enum.YLeaf(1, "discard")

            accept = Enum.YLeaf(2, "accept")


        class DocsDevFilterLLCUnmatchedAction(Enum):
            """
            DocsDevFilterLLCUnmatchedAction (Enum Class)

            LLC (Link Level Control) filters can be defined on an

            inclusive or exclusive basis\: CMs can be configured to

            forward only packets matching a set of layer three

            protocols, or to drop packets matching a set of layer

            three protocols.  Typical use of these filters is to

            filter out possibly harmful (given the context of a

            large metropolitan LAN) protocols.

            If set to discard(1), any L2 packet that does not match

            at least one filter in the docsDevFilterLLCTable will be

            discarded.  If set to accept(2), any L2 packet that

            does not match at least one filter in the

            docsDevFilterLLCTable will be accepted for further

            processing (e.g., bridging).  In other words, if the

            packet does not match an entry in the table, it takes

            this action; if it does match an entry in the table, it

            takes the opposite of this action.

            .. data:: discard = 1

            .. data:: accept = 2

            """

            discard = Enum.YLeaf(1, "discard")

            accept = Enum.YLeaf(2, "accept")



    class DocsDevCpe(Entity):
        """
        
        
        .. attribute:: docsdevcpeenroll
        
        	This object controls the population of docsDevFilterCpeTable. If set to none, the filters must be set manually by a network management action (either configuration or SNMP set). If set to any, the CM wiretaps the packets originating from the ethernet and enrolls up to docsDevCpeIpMax addresses as based on the source IPv4 or v6 addresses of those packets
        	**type**\:  :py:class:`DocsDevCpeEnroll <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevCpe.DocsDevCpeEnroll>`
        
        .. attribute:: docsdevcpeipmax
        
        	This object controls the maximum number of CPEs allowed to be learned behind this device. If set to zero, any number of CPEs may connect up to the maximum permitted for the device. If set to \-1, no filtering is done on CPE source addresses, and no entries are made in the docsDevFilterCpeTable via learning.  If an attempt is made to set this to a number greater than that permitted for the device, it is set to that maximum
        	**type**\: int
        
        	**range:** \-1..2147483647
        
        

        """

        _prefix = 'DOCS-CABLE-DEVICE-MIB'
        _revision = '2006-12-20'

        def __init__(self):
            super(DOCSCABLEDEVICEMIB.DocsDevCpe, self).__init__()

            self.yang_name = "docsDevCpe"
            self.yang_parent_name = "DOCS-CABLE-DEVICE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('docsdevcpeenroll', (YLeaf(YType.enumeration, 'docsDevCpeEnroll'), [('ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB', 'DOCSCABLEDEVICEMIB', 'DocsDevCpe.DocsDevCpeEnroll')])),
                ('docsdevcpeipmax', (YLeaf(YType.int32, 'docsDevCpeIpMax'), ['int'])),
            ])
            self.docsdevcpeenroll = None
            self.docsdevcpeipmax = None
            self._segment_path = lambda: "docsDevCpe"
            self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevCpe, [u'docsdevcpeenroll', u'docsdevcpeipmax'], name, value)

        class DocsDevCpeEnroll(Enum):
            """
            DocsDevCpeEnroll (Enum Class)

            This object controls the population of

            docsDevFilterCpeTable.

            If set to none, the filters must be set manually

            by a network management action (either configuration

            or SNMP set).

            If set to any, the CM wiretaps the packets originating

            from the ethernet and enrolls up to docsDevCpeIpMax

            addresses as based on the source IPv4 or v6 addresses of

            those packets.

            .. data:: none = 1

            .. data:: any = 2

            """

            none = Enum.YLeaf(1, "none")

            any = Enum.YLeaf(2, "any")



    class DocsDevNmAccessTable(Entity):
        """
        This table controls access to SNMP objects by network
        management stations.  If the table is empty, access to
        SNMP objects is unrestricted.  The objects in this table
        MUST NOT persist across reboots.  The objects in this
        table are only accessible from cable devices that are
        not capable of operating in SNMP Coexistence mode
        (RFC 3584) or in SNMPv3 mode (RFC 3410).
        See the conformance section for
        details.  Note that some devices are required by other
        specifications (e.g., the DOCSIS OSSIv1.1 specification)
        to support the legacy SNMPv1/v2c docsDevNmAccess mode
        for backward compatibility.
        
        This table is deprecated.  Instead, use the SNMP
        coexistence MIBs from RFC 3584, the TARGET and
        NOTIFICATION MIBs from RFC 3413, and
        the View\-Based Access Control Model (VACM) MIBs for
        all SNMP protocol versions from RFC 3415.
        
        .. attribute:: docsdevnmaccessentry
        
        	An entry describing access to SNMP objects by a particular network management station. An entry in this table is not readable unless the management station has read\-write permission (either implicit if the table is empty, or explicit through an entry in this table). Entries are ordered by docsDevNmAccessIndex.  The first matching entry (e.g., matching IP address and community string) is used to derive access
        	**type**\: list of  		 :py:class:`DocsDevNmAccessEntry <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevNmAccessTable.DocsDevNmAccessEntry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'DOCS-CABLE-DEVICE-MIB'
        _revision = '2006-12-20'

        def __init__(self):
            super(DOCSCABLEDEVICEMIB.DocsDevNmAccessTable, self).__init__()

            self.yang_name = "docsDevNmAccessTable"
            self.yang_parent_name = "DOCS-CABLE-DEVICE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsDevNmAccessEntry", ("docsdevnmaccessentry", DOCSCABLEDEVICEMIB.DocsDevNmAccessTable.DocsDevNmAccessEntry))])
            self._leafs = OrderedDict()

            self.docsdevnmaccessentry = YList(self)
            self._segment_path = lambda: "docsDevNmAccessTable"
            self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevNmAccessTable, [], name, value)


        class DocsDevNmAccessEntry(Entity):
            """
            An entry describing access to SNMP objects by a
            particular network management station. An entry in
            this table is not readable unless the management station
            has read\-write permission (either implicit if the table
            is empty, or explicit through an entry in this table).
            Entries are ordered by docsDevNmAccessIndex.  The first
            matching entry (e.g., matching IP address and community
            string) is used to derive access.
            
            .. attribute:: docsdevnmaccessindex  (key)
            
            	Index used to order the application of access entries
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: docsdevnmaccessip
            
            	The IP address (or subnet) of the network management station. The address 0.0.0.0 is defined to mean any Network Management Station (NMS).  If traps are enabled for this entry, then the value must be the address of a specific device.  Implementations MAY recognize 255.255.255.255 as equivalent to 0.0.0.0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: docsdevnmaccessipmask
            
            	The IP subnet mask of the network management stations. If traps are enabled for this entry, then the value must be 0.0.0.0.  Implementations MAY recognize 255.255.255.255 as equivalent to 0.0.0.0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: docsdevnmaccesscommunity
            
            	The community string to be matched for access by this entry.  If set to a zero\-length string, then any community string will match.  When read, this object SHOULD return a zero\-length string
            	**type**\: str
            
            	**status**\: deprecated
            
            .. attribute:: docsdevnmaccesscontrol
            
            	Specifies the type of access allowed to this NMS. Setting this object to none(1) causes the table entry to be destroyed.  Read(2) allows access by 'get' and 'get\-next' PDUs.  ReadWrite(3) allows access by 'set' as well.  RoWithtraps(4), rwWithTraps(5), and trapsOnly(6) control distribution of Trap PDUs transmitted by this device
            	**type**\:  :py:class:`DocsDevNmAccessControl <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevNmAccessTable.DocsDevNmAccessEntry.DocsDevNmAccessControl>`
            
            	**status**\: deprecated
            
            .. attribute:: docsdevnmaccessinterfaces
            
            	Specifies the set of interfaces from which requests from this NMS will be accepted.  Each octet within the value of this object specifies a set of eight interfaces, the first octet specifying ports 1 through 8, the second octet specifying interfaces 9 through 16, etc.  Within each octet, the most significant bit represents the lowest numbered interface, and the least significant bit represents the highest numbered interface.  Thus, each interface is represented by a single bit within the value of this object.  If that bit has a value of '1' then that interface is included in the set.  Note that entries in this table apply only to link\-layer interfaces (e.g., Ethernet and CATV MAC).  Bits representing upstream and downstream channel interfaces MUST NOT be set to '1'. Note that if bits corresponding to non\-existing interfaces are set, the result is implementation specific.  Note that according to the DOCSIS OSSIv1.1 specification, when ifIndex '1' is included in the set, then this row applies to all CPE (customer\-facing) interfaces.  The size of this object is the minimum required to represent all configured interfaces for this device
            	**type**\: str
            
            	**length:** 1..32
            
            	**status**\: deprecated
            
            .. attribute:: docsdevnmaccessstatus
            
            	Controls and reflects the status of rows in this table. Rows in this table may be created by either the create\-and\-go or create\-and\-wait paradigm.   There is no restriction on changing values in a row of this table while the row is active.  The following objects MUST have valid values before this object can be set to active\: docsDevNmAccessIp, docsDevNmAccessStatus, docsDevNmAccessIpMask, docsDevNmAccessCommunity, docsDevNmAccessControl, and docsDevNmAccessInterfaces
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**status**\: deprecated
            
            .. attribute:: docsdevnmaccesstrapversion
            
            	Specifies the TRAP version that is sent to this NMS. Setting this object to disableSNMPv2trap (1) causes the trap in SNMPv1 format to be sent to a particular NMS. Setting this object to enableSNMPv2trap (2) causes the trap in SNMPv2 format be sent to a particular NMS
            	**type**\:  :py:class:`DocsDevNmAccessTrapVersion <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevNmAccessTable.DocsDevNmAccessEntry.DocsDevNmAccessTrapVersion>`
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'DOCS-CABLE-DEVICE-MIB'
            _revision = '2006-12-20'

            def __init__(self):
                super(DOCSCABLEDEVICEMIB.DocsDevNmAccessTable.DocsDevNmAccessEntry, self).__init__()

                self.yang_name = "docsDevNmAccessEntry"
                self.yang_parent_name = "docsDevNmAccessTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsdevnmaccessindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsdevnmaccessindex', (YLeaf(YType.int32, 'docsDevNmAccessIndex'), ['int'])),
                    ('docsdevnmaccessip', (YLeaf(YType.str, 'docsDevNmAccessIp'), ['str'])),
                    ('docsdevnmaccessipmask', (YLeaf(YType.str, 'docsDevNmAccessIpMask'), ['str'])),
                    ('docsdevnmaccesscommunity', (YLeaf(YType.str, 'docsDevNmAccessCommunity'), ['str'])),
                    ('docsdevnmaccesscontrol', (YLeaf(YType.enumeration, 'docsDevNmAccessControl'), [('ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB', 'DOCSCABLEDEVICEMIB', 'DocsDevNmAccessTable.DocsDevNmAccessEntry.DocsDevNmAccessControl')])),
                    ('docsdevnmaccessinterfaces', (YLeaf(YType.str, 'docsDevNmAccessInterfaces'), ['str'])),
                    ('docsdevnmaccessstatus', (YLeaf(YType.enumeration, 'docsDevNmAccessStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('docsdevnmaccesstrapversion', (YLeaf(YType.enumeration, 'docsDevNmAccessTrapVersion'), [('ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB', 'DOCSCABLEDEVICEMIB', 'DocsDevNmAccessTable.DocsDevNmAccessEntry.DocsDevNmAccessTrapVersion')])),
                ])
                self.docsdevnmaccessindex = None
                self.docsdevnmaccessip = None
                self.docsdevnmaccessipmask = None
                self.docsdevnmaccesscommunity = None
                self.docsdevnmaccesscontrol = None
                self.docsdevnmaccessinterfaces = None
                self.docsdevnmaccessstatus = None
                self.docsdevnmaccesstrapversion = None
                self._segment_path = lambda: "docsDevNmAccessEntry" + "[docsDevNmAccessIndex='" + str(self.docsdevnmaccessindex) + "']"
                self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/docsDevNmAccessTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevNmAccessTable.DocsDevNmAccessEntry, [u'docsdevnmaccessindex', u'docsdevnmaccessip', u'docsdevnmaccessipmask', u'docsdevnmaccesscommunity', u'docsdevnmaccesscontrol', u'docsdevnmaccessinterfaces', u'docsdevnmaccessstatus', u'docsdevnmaccesstrapversion'], name, value)

            class DocsDevNmAccessControl(Enum):
                """
                DocsDevNmAccessControl (Enum Class)

                Specifies the type of access allowed to this NMS.

                Setting this object to none(1) causes the table entry

                to be destroyed.  Read(2) allows access by 'get' and

                'get\-next' PDUs.  ReadWrite(3) allows access by 'set' as

                well.  RoWithtraps(4), rwWithTraps(5), and trapsOnly(6)

                control distribution of Trap PDUs transmitted by this

                device.

                .. data:: none = 1

                .. data:: read = 2

                .. data:: readWrite = 3

                .. data:: roWithTraps = 4

                .. data:: rwWithTraps = 5

                .. data:: trapsOnly = 6

                """

                none = Enum.YLeaf(1, "none")

                read = Enum.YLeaf(2, "read")

                readWrite = Enum.YLeaf(3, "readWrite")

                roWithTraps = Enum.YLeaf(4, "roWithTraps")

                rwWithTraps = Enum.YLeaf(5, "rwWithTraps")

                trapsOnly = Enum.YLeaf(6, "trapsOnly")


            class DocsDevNmAccessTrapVersion(Enum):
                """
                DocsDevNmAccessTrapVersion (Enum Class)

                Specifies the TRAP version that is sent to this NMS.

                Setting this object to disableSNMPv2trap (1) causes the

                trap in SNMPv1 format to be sent to a particular NMS.

                Setting this object to enableSNMPv2trap (2) causes the

                trap in SNMPv2 format be sent to a particular NMS.

                .. data:: disableSNMPv2trap = 1

                .. data:: enableSNMPv2trap = 2

                """

                disableSNMPv2trap = Enum.YLeaf(1, "disableSNMPv2trap")

                enableSNMPv2trap = Enum.YLeaf(2, "enableSNMPv2trap")



    class DocsDevEvControlTable(Entity):
        """
        This table allows control of the reporting of event
        classes.  For each event priority, a combination of
        logging and reporting mechanisms may be chosen.  The
        mapping of event types to priorities is
        vendor dependent.  Vendors may also choose to allow
        the user to control that mapping through proprietary
        means.  Table entries MUST persist across reboots for
        CMTS devices and MUST NOT persist across reboots for CM
        devices.
        
        .. attribute:: docsdevevcontrolentry
        
        	Allows configuration of the reporting mechanisms for a particular event priority
        	**type**\: list of  		 :py:class:`DocsDevEvControlEntry <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevEvControlTable.DocsDevEvControlEntry>`
        
        

        """

        _prefix = 'DOCS-CABLE-DEVICE-MIB'
        _revision = '2006-12-20'

        def __init__(self):
            super(DOCSCABLEDEVICEMIB.DocsDevEvControlTable, self).__init__()

            self.yang_name = "docsDevEvControlTable"
            self.yang_parent_name = "DOCS-CABLE-DEVICE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsDevEvControlEntry", ("docsdevevcontrolentry", DOCSCABLEDEVICEMIB.DocsDevEvControlTable.DocsDevEvControlEntry))])
            self._leafs = OrderedDict()

            self.docsdevevcontrolentry = YList(self)
            self._segment_path = lambda: "docsDevEvControlTable"
            self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevEvControlTable, [], name, value)


        class DocsDevEvControlEntry(Entity):
            """
            Allows configuration of the reporting mechanisms for a
            particular event priority.
            
            .. attribute:: docsdevevpriority  (key)
            
            	The priority level that is controlled by this entry. These are ordered from most (emergency) to least (debug) critical.  Each event with a CM or CMTS has a particular priority level associated with it (as defined by the vendor).  emergency(1) events indicate vendor\-specific fatal hardware or software errors that prevent normal system operation.  alert(2) events indicate a serious failure that causes the reporting system to reboot but is not caused by hardware or software malfunctioning.  critical(3) events indicate a serious failure that requires attention and prevents the device from transmitting data but that could be recovered without rebooting the system.  error(4) and warning(5) events indicate that a failure occurred that could interrupt the normal data flow but that does not cause the device to re\-register.  notice(6) and information(7) events indicate a milestone or checkpoint in normal operation that could be of particular importance for troubleshooting.  debug(8) events are reserved for vendor\-specific events.  During normal operation, no event more critical than notice(6) should be generated.  Events between warning and emergency should be generated at appropriate levels of problems (e.g., emergency when the box is about to crash)
            	**type**\:  :py:class:`DocsDevEvPriority <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevEvControlTable.DocsDevEvControlEntry.DocsDevEvPriority>`
            
            .. attribute:: docsdevevreporting
            
            	Defines the action to be taken on occurrence of this event class.  Implementations may not necessarily support all options for all event classes but at minimum must allow traps and syslogging to be disabled.  If the local(0) bit is set, then log to the internal log and update non\-volatile store, for backward compatibility with the original RFC 2669 definition. If the traps(1) bit is set, then generate an SNMP trap; if the syslog(2) bit is set, then send a syslog message (assuming that the syslog address is set).  If the localVolatile(8) bit is set, then log to the internal log without updating non\-volatile store.  If the stdInterface(9) bit is set, then the agent ignores all other bits except the local(0), syslog(2), and localVolatile(8) bits.  Setting the stdInterface(9) bit indicates that RFC3413 and RFC3014 are being used to control event reporting mechanisms
            	**type**\: str
            
            

            """

            _prefix = 'DOCS-CABLE-DEVICE-MIB'
            _revision = '2006-12-20'

            def __init__(self):
                super(DOCSCABLEDEVICEMIB.DocsDevEvControlTable.DocsDevEvControlEntry, self).__init__()

                self.yang_name = "docsDevEvControlEntry"
                self.yang_parent_name = "docsDevEvControlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsdevevpriority']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsdevevpriority', (YLeaf(YType.enumeration, 'docsDevEvPriority'), [('ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB', 'DOCSCABLEDEVICEMIB', 'DocsDevEvControlTable.DocsDevEvControlEntry.DocsDevEvPriority')])),
                    ('docsdevevreporting', (YLeaf(YType.str, 'docsDevEvReporting'), ['str'])),
                ])
                self.docsdevevpriority = None
                self.docsdevevreporting = None
                self._segment_path = lambda: "docsDevEvControlEntry" + "[docsDevEvPriority='" + str(self.docsdevevpriority) + "']"
                self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/docsDevEvControlTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevEvControlTable.DocsDevEvControlEntry, [u'docsdevevpriority', u'docsdevevreporting'], name, value)

            class DocsDevEvPriority(Enum):
                """
                DocsDevEvPriority (Enum Class)

                The priority level that is controlled by this

                entry. These are ordered from most (emergency) to least

                (debug) critical.  Each event with a CM or CMTS has a

                particular priority level associated with it (as defined

                by the vendor).

                emergency(1) events indicate vendor\-specific fatal

                hardware or software errors that prevent normal system

                operation.

                alert(2) events indicate a serious failure that causes

                the reporting system to reboot but is not caused by

                hardware or software malfunctioning.

                critical(3) events indicate a serious failure that

                requires attention and prevents the device from

                transmitting data but that could be recovered without

                rebooting the system.

                error(4) and warning(5) events indicate that a failure

                occurred that could interrupt the normal data flow but

                that does not cause the device to re\-register.

                notice(6) and information(7) events indicate a

                milestone or checkpoint in normal operation that could

                be of particular importance for troubleshooting.

                debug(8) events are reserved for vendor\-specific

                events.

                During normal operation, no event more

                critical than notice(6) should be generated.  Events

                between warning and emergency should be generated at

                appropriate levels of problems (e.g., emergency when the

                box is about to crash).

                .. data:: emergency = 1

                .. data:: alert = 2

                .. data:: critical = 3

                .. data:: error = 4

                .. data:: warning = 5

                .. data:: notice = 6

                .. data:: information = 7

                .. data:: debug = 8

                """

                emergency = Enum.YLeaf(1, "emergency")

                alert = Enum.YLeaf(2, "alert")

                critical = Enum.YLeaf(3, "critical")

                error = Enum.YLeaf(4, "error")

                warning = Enum.YLeaf(5, "warning")

                notice = Enum.YLeaf(6, "notice")

                information = Enum.YLeaf(7, "information")

                debug = Enum.YLeaf(8, "debug")



    class DocsDevEventTable(Entity):
        """
        Contains a log of network and device events that may be
        of interest in fault isolation and troubleshooting.
        If the local(0) bit is set in docsDevEvReporting,
        entries in this table MUST persist across reboots.
        
        .. attribute:: docsdevevententry
        
        	Describes a network or device event that may be of interest in fault isolation and troubleshooting. Multiple sequential identical events are represented by incrementing docsDevEvCounts and setting docsDevEvLastTime to the current time rather than creating multiple rows.  Entries are created with the first occurrence of an event.  docsDevEvControl can be used to clear the table.  Individual events cannot be deleted
        	**type**\: list of  		 :py:class:`DocsDevEventEntry <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevEventTable.DocsDevEventEntry>`
        
        

        """

        _prefix = 'DOCS-CABLE-DEVICE-MIB'
        _revision = '2006-12-20'

        def __init__(self):
            super(DOCSCABLEDEVICEMIB.DocsDevEventTable, self).__init__()

            self.yang_name = "docsDevEventTable"
            self.yang_parent_name = "DOCS-CABLE-DEVICE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsDevEventEntry", ("docsdevevententry", DOCSCABLEDEVICEMIB.DocsDevEventTable.DocsDevEventEntry))])
            self._leafs = OrderedDict()

            self.docsdevevententry = YList(self)
            self._segment_path = lambda: "docsDevEventTable"
            self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevEventTable, [], name, value)


        class DocsDevEventEntry(Entity):
            """
            Describes a network or device event that may be of
            interest in fault isolation and troubleshooting.
            Multiple sequential identical events are represented by
            incrementing docsDevEvCounts and setting
            docsDevEvLastTime to the current time rather than
            creating multiple rows.
            
            Entries are created with the first occurrence of an
            event.  docsDevEvControl can be used to clear the
            table.  Individual events cannot be deleted.
            
            .. attribute:: docsdevevindex  (key)
            
            	Provides relative ordering of the objects in the event log. This object will always increase except when (a) the log is reset via docsDevEvControl, (b) the device reboots and does not implement non\-volatile storage for this log, or (c) it reaches the value 2^31.  The next entry for all the above cases is 1
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: docsdevevfirsttime
            
            	The value of docsDevDateTime at the time this entry was created
            	**type**\: str
            
            .. attribute:: docsdevevlasttime
            
            	When an entry reports only one event, this object will have the same value as the corresponding instance of docsDevEvFirstTime.  When an entry reports multiple events, this object will record the value that docsDevDateTime had when the most recent event for this entry occurred
            	**type**\: str
            
            .. attribute:: docsdevevcounts
            
            	The number of consecutive event instances reported by this entry.  This starts at 1 with the creation of this row and increments by 1 for each subsequent duplicate event
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: events
            
            .. attribute:: docsdevevlevel
            
            	The priority level of this event, as defined by the vendor.  These are ordered from most serious (emergency) to least serious (debug).  emergency(1) events indicate vendor\-specific fatal hardware or software errors that prevent normal system operation.  alert(2) events indicate a serious failure that causes the reporting system to reboot but that is not caused by hardware or software malfunctioning.  critical(3) events indicate a serious failure that requires attention and prevents the device from transmitting data but that could be recovered without rebooting the system.  error(4) and warning(5) events indicate that a failure occurred that could interrupt the normal data flow but that does not cause the device to re\-register.  notice(6) and information(7) events indicate a milestone or checkpoint in normal operation that could be of particular importance for troubleshooting.  debug(8) events are reserved for vendor\-specific events.  During normal operation, no event more critical than notice(6) should be generated.  Events between warning and emergency should be generated at appropriate levels of problems (e.g., emergency when the box is about to crash)
            	**type**\:  :py:class:`DocsDevEvLevel <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevEventTable.DocsDevEventEntry.DocsDevEvLevel>`
            
            .. attribute:: docsdevevid
            
            	For this product, uniquely identifies the type of event that is reported by this entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: docsdevevtext
            
            	Provides a human\-readable description of the event, including all relevant context (interface numbers, etc.)
            	**type**\: str
            
            

            """

            _prefix = 'DOCS-CABLE-DEVICE-MIB'
            _revision = '2006-12-20'

            def __init__(self):
                super(DOCSCABLEDEVICEMIB.DocsDevEventTable.DocsDevEventEntry, self).__init__()

                self.yang_name = "docsDevEventEntry"
                self.yang_parent_name = "docsDevEventTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsdevevindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsdevevindex', (YLeaf(YType.int32, 'docsDevEvIndex'), ['int'])),
                    ('docsdevevfirsttime', (YLeaf(YType.str, 'docsDevEvFirstTime'), ['str'])),
                    ('docsdevevlasttime', (YLeaf(YType.str, 'docsDevEvLastTime'), ['str'])),
                    ('docsdevevcounts', (YLeaf(YType.uint32, 'docsDevEvCounts'), ['int'])),
                    ('docsdevevlevel', (YLeaf(YType.enumeration, 'docsDevEvLevel'), [('ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB', 'DOCSCABLEDEVICEMIB', 'DocsDevEventTable.DocsDevEventEntry.DocsDevEvLevel')])),
                    ('docsdevevid', (YLeaf(YType.uint32, 'docsDevEvId'), ['int'])),
                    ('docsdevevtext', (YLeaf(YType.str, 'docsDevEvText'), ['str'])),
                ])
                self.docsdevevindex = None
                self.docsdevevfirsttime = None
                self.docsdevevlasttime = None
                self.docsdevevcounts = None
                self.docsdevevlevel = None
                self.docsdevevid = None
                self.docsdevevtext = None
                self._segment_path = lambda: "docsDevEventEntry" + "[docsDevEvIndex='" + str(self.docsdevevindex) + "']"
                self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/docsDevEventTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevEventTable.DocsDevEventEntry, [u'docsdevevindex', u'docsdevevfirsttime', u'docsdevevlasttime', u'docsdevevcounts', u'docsdevevlevel', u'docsdevevid', u'docsdevevtext'], name, value)

            class DocsDevEvLevel(Enum):
                """
                DocsDevEvLevel (Enum Class)

                The priority level of this event, as defined by the

                vendor.  These are ordered from most serious (emergency)

                to least serious (debug).

                emergency(1) events indicate vendor\-specific fatal

                hardware or software errors that prevent normal system

                operation.

                alert(2) events indicate a serious failure that causes

                the reporting system to reboot but that is not caused by

                hardware or software malfunctioning.

                critical(3) events indicate a serious failure that

                requires attention and prevents the device from

                transmitting data but that could be recovered without

                rebooting the system.

                error(4) and warning(5) events indicate that a failure

                occurred that could interrupt the normal data flow but

                that does not cause the device to re\-register.

                notice(6) and information(7) events indicate a

                milestone or checkpoint in normal operation that could

                be of particular importance for troubleshooting.

                debug(8) events are reserved for vendor\-specific

                events.

                During normal operation, no event more

                critical than notice(6) should be generated.  Events

                between warning and emergency should be generated at

                appropriate levels of problems (e.g., emergency when the

                box is about to crash).

                .. data:: emergency = 1

                .. data:: alert = 2

                .. data:: critical = 3

                .. data:: error = 4

                .. data:: warning = 5

                .. data:: notice = 6

                .. data:: information = 7

                .. data:: debug = 8

                """

                emergency = Enum.YLeaf(1, "emergency")

                alert = Enum.YLeaf(2, "alert")

                critical = Enum.YLeaf(3, "critical")

                error = Enum.YLeaf(4, "error")

                warning = Enum.YLeaf(5, "warning")

                notice = Enum.YLeaf(6, "notice")

                information = Enum.YLeaf(7, "information")

                debug = Enum.YLeaf(8, "debug")



    class DocsDevFilterLLCTable(Entity):
        """
        A list of filters to apply to (bridged) LLC
        traffic. The filters in this table are applied to
        incoming traffic on the appropriate interface(s)  prior
        to any further processing (e.g., before the packet
        is handed off for level 3 processing, or for bridging).
        The specific action taken when no filter is matched is
        controlled by docsDevFilterLLCUnmatchedAction.  Table
        entries MUST NOT persist across reboots for any device.
        
        .. attribute:: docsdevfilterllcentry
        
        	Describes a single filter to apply to (bridged) LLC traffic received on a specified interface. 
        	**type**\: list of  		 :py:class:`DocsDevFilterLLCEntry <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevFilterLLCTable.DocsDevFilterLLCEntry>`
        
        

        """

        _prefix = 'DOCS-CABLE-DEVICE-MIB'
        _revision = '2006-12-20'

        def __init__(self):
            super(DOCSCABLEDEVICEMIB.DocsDevFilterLLCTable, self).__init__()

            self.yang_name = "docsDevFilterLLCTable"
            self.yang_parent_name = "DOCS-CABLE-DEVICE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsDevFilterLLCEntry", ("docsdevfilterllcentry", DOCSCABLEDEVICEMIB.DocsDevFilterLLCTable.DocsDevFilterLLCEntry))])
            self._leafs = OrderedDict()

            self.docsdevfilterllcentry = YList(self)
            self._segment_path = lambda: "docsDevFilterLLCTable"
            self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevFilterLLCTable, [], name, value)


        class DocsDevFilterLLCEntry(Entity):
            """
            Describes a single filter to apply to (bridged) LLC
            traffic received on a specified interface. 
            
            .. attribute:: docsdevfilterllcindex  (key)
            
            	Index used for the identification of filters (note that LLC filter order is irrelevant)
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: docsdevfilterllcstatus
            
            	Controls and reflects the status of rows in this table. There is no restriction on changing any of the associated columns for this row while this object is set to active.  Specifying only this object (with the appropriate index) on a CM is sufficient to create a filter row that matches all inbound packets on the ethernet interface and results in the packets being discarded.  docsDevFilterLLCIfIndex (at least) must be specified on a CMTS to create a row
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: docsdevfilterllcifindex
            
            	The entry interface to which this filter applies.  The value corresponds to ifIndex for either a CATV MAC or another network interface.  If the value is zero, the filter applies to all interfaces.  In Cable Modems, the default value is the customer side interface(s).  In CMTSs, this object has to be specified to create a row in this table.  Note that according to the DOCSIS OSSIv1.1 specification, ifIndex '1' in the CM means that this row applies to all Cable Modem\-to\-CPE Interfaces (CMCI)
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: docsdevfilterllcprotocoltype
            
            	The format of the value in docsDevFilterLLCProtocol\: either a two\-byte Ethernet Ethertype, or a one\-byte 802.2 Service Access Point (SAP) value.  ethertype(1) also applies to Standard Network Access Protocol (SNAP) encapsulated frames
            	**type**\:  :py:class:`DocsDevFilterLLCProtocolType <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevFilterLLCTable.DocsDevFilterLLCEntry.DocsDevFilterLLCProtocolType>`
            
            .. attribute:: docsdevfilterllcprotocol
            
            	The layer\-three protocol for which this filter applies. The protocol value format depends on docsDevFilterLLCProtocolType.  Note that for SNAP frames, ethertype filtering is performed rather than Destination Service Access Point (DSAP) =0xAA
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: docsdevfilterllcmatches
            
            	Counts the number of times this filter was matched
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: matches
            
            

            """

            _prefix = 'DOCS-CABLE-DEVICE-MIB'
            _revision = '2006-12-20'

            def __init__(self):
                super(DOCSCABLEDEVICEMIB.DocsDevFilterLLCTable.DocsDevFilterLLCEntry, self).__init__()

                self.yang_name = "docsDevFilterLLCEntry"
                self.yang_parent_name = "docsDevFilterLLCTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsdevfilterllcindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsdevfilterllcindex', (YLeaf(YType.int32, 'docsDevFilterLLCIndex'), ['int'])),
                    ('docsdevfilterllcstatus', (YLeaf(YType.enumeration, 'docsDevFilterLLCStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('docsdevfilterllcifindex', (YLeaf(YType.int32, 'docsDevFilterLLCIfIndex'), ['int'])),
                    ('docsdevfilterllcprotocoltype', (YLeaf(YType.enumeration, 'docsDevFilterLLCProtocolType'), [('ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB', 'DOCSCABLEDEVICEMIB', 'DocsDevFilterLLCTable.DocsDevFilterLLCEntry.DocsDevFilterLLCProtocolType')])),
                    ('docsdevfilterllcprotocol', (YLeaf(YType.int32, 'docsDevFilterLLCProtocol'), ['int'])),
                    ('docsdevfilterllcmatches', (YLeaf(YType.uint32, 'docsDevFilterLLCMatches'), ['int'])),
                ])
                self.docsdevfilterllcindex = None
                self.docsdevfilterllcstatus = None
                self.docsdevfilterllcifindex = None
                self.docsdevfilterllcprotocoltype = None
                self.docsdevfilterllcprotocol = None
                self.docsdevfilterllcmatches = None
                self._segment_path = lambda: "docsDevFilterLLCEntry" + "[docsDevFilterLLCIndex='" + str(self.docsdevfilterllcindex) + "']"
                self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/docsDevFilterLLCTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevFilterLLCTable.DocsDevFilterLLCEntry, [u'docsdevfilterllcindex', u'docsdevfilterllcstatus', u'docsdevfilterllcifindex', u'docsdevfilterllcprotocoltype', u'docsdevfilterllcprotocol', u'docsdevfilterllcmatches'], name, value)

            class DocsDevFilterLLCProtocolType(Enum):
                """
                DocsDevFilterLLCProtocolType (Enum Class)

                The format of the value in docsDevFilterLLCProtocol\:

                either a two\-byte Ethernet Ethertype, or a one\-byte

                802.2 Service Access Point (SAP) value.  ethertype(1)

                also applies to Standard Network Access Protocol

                (SNAP) encapsulated frames.

                .. data:: ethertype = 1

                .. data:: dsap = 2

                """

                ethertype = Enum.YLeaf(1, "ethertype")

                dsap = Enum.YLeaf(2, "dsap")



    class DocsDevFilterIpTable(Entity):
        """
        An ordered list of filters or classifiers to apply to
        IP traffic. Filter application is ordered by the filter
        index, rather than by a best match algorithm (Note that
        this implies that the filter table may have gaps in the
        index values).  Packets that match no filters will have
        policy 0 in the docsDevFilterPolicyTable applied to
        them, if it exists.  Otherwise, Packets that match no
        filters are discarded or forwarded according to the
        setting of docsDevFilterIpDefault.
        
        Any IP packet can theoretically match multiple rows of
        this table.  When considering a packet, the table is
        scanned in row index order (e.g., filter 10 is checked
        before filter 20).  If the packet matches that filter
        (which means that it matches ALL criteria for that row),
        actions appropriate to docsDevFilterIpControl and
        docsDevFilterPolicyId are taken.  If the packet was
        discarded processing is complete.  If
        docsDevFilterIpContinue is set to true, the filter
        comparison continues with the next row in the table,
        looking for additional matches.
        
        If the packet matches no filter in the table, the packet
        is accepted or dropped for further processing
        according to the setting of docsDevFilterIpDefault.
        If the packet is accepted, the actions specified by
        policy group 0 (e.g., the rows in
        docsDevFilterPolicyTable that have a value of 0 for
        docsDevFilterPolicyId) are taken, if that policy
        group exists.
        
        Logically, this table is consulted twice during the
        processing of any IP packet\: once upon its acceptance
        from the L2 entity, and once upon its transmission to
        the L2 entity.  In actuality, for cable modems, IP
        filtering is generally the only IP processing done for
        transit traffic.  This means that inbound and outbound
        filtering can generally be done at the same time with
        one pass through the filter table.
        
        The objects in this table are only accessible from cable
        devices that are not operating in DiffServ MIB mode
        (RFC 3289).  See the conformance section for details.
        
        Note that some devices are required by other
        specifications (e.g., the DOCSIS OSSIv1.1 specification)
        to support the legacy SNMPv1/v2c docsDevFilter mode
        for backward compatibility.
        
        Table entries MUST NOT persist across reboots for any
        device.
        
        This table is deprecated.  Instead, use the DiffServ MIB
        from RFC3289.
        
        .. attribute:: docsdevfilteripentry
        
        	Describes a filter to apply to IP traffic received on a specified interface.  All identity objects in this table (e.g., source and destination address/mask, protocol, source/dest port, TOS/mask, interface and direction) must match their respective fields in the packet for any given filter to match.  To create an entry in this table, docsDevFilterIpIfIndex must be specified
        	**type**\: list of  		 :py:class:`DocsDevFilterIpEntry <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevFilterIpTable.DocsDevFilterIpEntry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'DOCS-CABLE-DEVICE-MIB'
        _revision = '2006-12-20'

        def __init__(self):
            super(DOCSCABLEDEVICEMIB.DocsDevFilterIpTable, self).__init__()

            self.yang_name = "docsDevFilterIpTable"
            self.yang_parent_name = "DOCS-CABLE-DEVICE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsDevFilterIpEntry", ("docsdevfilteripentry", DOCSCABLEDEVICEMIB.DocsDevFilterIpTable.DocsDevFilterIpEntry))])
            self._leafs = OrderedDict()

            self.docsdevfilteripentry = YList(self)
            self._segment_path = lambda: "docsDevFilterIpTable"
            self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevFilterIpTable, [], name, value)


        class DocsDevFilterIpEntry(Entity):
            """
            Describes a filter to apply to IP traffic received on a
            specified interface.  All identity objects in this table
            (e.g., source and destination address/mask, protocol,
            source/dest port, TOS/mask, interface and direction)
            must match their respective fields in the packet for
            any given filter to match.
            
            To create an entry in this table, docsDevFilterIpIfIndex
            must be specified.
            
            .. attribute:: docsdevfilteripindex  (key)
            
            	Index used to order the application of filters. The filter with the lowest index is always applied first
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfilteripstatus
            
            	Controls and reflects the status of rows in this table.  Specifying only this object (with the appropriate index) on a CM is sufficient to create a filter row that matches all inbound packets on the ethernet interface and results in the packets being discarded. docsDevFilterIpIfIndex (at least) must be specified on a CMTS to create a row.  Creation of the rows may be done via either create\-and\-wait or create\-and\-go, but the filter is not applied until this object is set to (or changes to) active. There is no restriction in changing any object in a row while this object is set to active
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfilteripcontrol
            
            	If set to discard(1), all packets matching this filter will be discarded, and scanning of the remainder of the filter list will be aborted. If set to accept(2), all packets matching this filter will be accepted for further processing (e.g., bridging).  If docsDevFilterIpContinue is set to true, see if there are other matches; otherwise, done.  If set to policy (3), execute the policy entries matched by docsDevFilterIpPolicyId in docsDevFilterPolicyTable.  If docsDevFilterIpContinue is set to true, continue scanning the table for other matches; otherwise, done
            	**type**\:  :py:class:`DocsDevFilterIpControl <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevFilterIpTable.DocsDevFilterIpEntry.DocsDevFilterIpControl>`
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfilteripifindex
            
            	The entry interface to which this filter applies. The value corresponds to ifIndex for either a CATV MAC or another interface. If the value is zero, the filter applies to all interfaces.  Default value in CMs is the index of the customer\-side (e.g., ethernet) interface(s).  In CMTSes, this object MUST be specified to create a row in this table.  Note that according to the DOCSIS OSSIv1.1 specification, ifIndex '1' in the Cable Modem means that this row applies to all CMCI (customer\-facing) interfaces
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfilteripdirection
            
            	Determines whether the filter is applied to inbound(1) traffic, outbound(2) traffic, or traffic in both(3) directions
            	**type**\:  :py:class:`DocsDevFilterIpDirection <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevFilterIpTable.DocsDevFilterIpEntry.DocsDevFilterIpDirection>`
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfilteripbroadcast
            
            	If set to true(1), the filter only applies to multicast and broadcast traffic. If set to false(2), the filter applies to all traffic
            	**type**\: bool
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfilteripsaddr
            
            	The source IP address, or portion thereof, that is to be matched for this filter.  The source address is first masked (ANDed) against docsDevFilterIpSmask before being compared to this value.  A value of 0 for this object and 0 for the mask matches all IP addresses
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfilteripsmask
            
            	A bit mask that is to be applied to the source address prior to matching.  This mask is not necessarily the same as a subnet mask, but 1s bits must be leftmost and contiguous
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfilteripdaddr
            
            	The destination IP address, or portion thereof, that is to be matched for this filter.  The destination address is first masked (ANDed) against docsDevFilterIpDmask before being compared to this value.  A value of 00000000 for this object and 00000000 for the mask matches all IP addresses
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfilteripdmask
            
            	A bit mask that is to be applied to the destination address prior to matching. This mask is not necessarily the same as a subnet mask, but 1s bits MUST be leftmost and contiguous
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfilteripprotocol
            
            	The IP protocol value that is to be matched.  For example, icmp is 1, tcp is 6, and udp is 17.  A value of 256 matches ANY protocol
            	**type**\: int
            
            	**range:** 0..256
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfilteripsourceportlow
            
            	This is the inclusive lower bound of the transport\-layer source port range that is to be matched.  If the IP protocol of the packet is neither UDP nor TCP, this object is ignored during matching
            	**type**\: int
            
            	**range:** 0..65535
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfilteripsourceporthigh
            
            	This is the inclusive upper bound of the transport\-layer source port range that is to be matched.  If the IP protocol of the packet is neither UDP nor TCP, this object is ignored during matching
            	**type**\: int
            
            	**range:** 0..65535
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfilteripdestportlow
            
            	This is the inclusive lower bound of the transport\-layer destination port range that is to be matched. If the IP protocol of the packet is neither UDP nor TCP, this object is ignored during matching
            	**type**\: int
            
            	**range:** 0..65535
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfilteripdestporthigh
            
            	This is the inclusive upper bound of the transport\-layer destination port range that is to be matched. If the IP protocol of the packet is neither UDP nor TCP, this object is ignored during matching
            	**type**\: int
            
            	**range:** 0..65535
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfilteripmatches
            
            	Counts the number of times this filter was matched. This object is initialized to 0 at boot, or at row creation, and is reset only upon reboot
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: matches
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfilteriptos
            
            	This is the value to be matched to the packet's TOS (Type of Service) value (after the TOS value is ANDed with docsDevFilterIpTosMask).  A value for this object of 0 and a mask of 0 matches all TOS values
            	**type**\: str
            
            	**length:** 1
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfilteriptosmask
            
            	The mask to be applied to the packet's TOS value before matching
            	**type**\: str
            
            	**length:** 1
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfilteripcontinue
            
            	If this value is set to true and docsDevFilterIpControl is anything but discard (1), continue scanning and applying policies.  See Section 3.3.3 for more details
            	**type**\: bool
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfilterippolicyid
            
            	This object points to an entry in docsDevFilterPolicyTable.  If docsDevFilterIpControl is set to policy (3), execute all matching policies in docsDevFilterPolicyTable.  If no matching policy exists, treat as if docsDevFilterIpControl were set to accept (1).  If this object is set to the value of 0, there is no matching policy, and docsDevFilterPolicyTable MUST NOT be consulted
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'DOCS-CABLE-DEVICE-MIB'
            _revision = '2006-12-20'

            def __init__(self):
                super(DOCSCABLEDEVICEMIB.DocsDevFilterIpTable.DocsDevFilterIpEntry, self).__init__()

                self.yang_name = "docsDevFilterIpEntry"
                self.yang_parent_name = "docsDevFilterIpTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsdevfilteripindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsdevfilteripindex', (YLeaf(YType.int32, 'docsDevFilterIpIndex'), ['int'])),
                    ('docsdevfilteripstatus', (YLeaf(YType.enumeration, 'docsDevFilterIpStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('docsdevfilteripcontrol', (YLeaf(YType.enumeration, 'docsDevFilterIpControl'), [('ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB', 'DOCSCABLEDEVICEMIB', 'DocsDevFilterIpTable.DocsDevFilterIpEntry.DocsDevFilterIpControl')])),
                    ('docsdevfilteripifindex', (YLeaf(YType.int32, 'docsDevFilterIpIfIndex'), ['int'])),
                    ('docsdevfilteripdirection', (YLeaf(YType.enumeration, 'docsDevFilterIpDirection'), [('ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB', 'DOCSCABLEDEVICEMIB', 'DocsDevFilterIpTable.DocsDevFilterIpEntry.DocsDevFilterIpDirection')])),
                    ('docsdevfilteripbroadcast', (YLeaf(YType.boolean, 'docsDevFilterIpBroadcast'), ['bool'])),
                    ('docsdevfilteripsaddr', (YLeaf(YType.str, 'docsDevFilterIpSaddr'), ['str'])),
                    ('docsdevfilteripsmask', (YLeaf(YType.str, 'docsDevFilterIpSmask'), ['str'])),
                    ('docsdevfilteripdaddr', (YLeaf(YType.str, 'docsDevFilterIpDaddr'), ['str'])),
                    ('docsdevfilteripdmask', (YLeaf(YType.str, 'docsDevFilterIpDmask'), ['str'])),
                    ('docsdevfilteripprotocol', (YLeaf(YType.int32, 'docsDevFilterIpProtocol'), ['int'])),
                    ('docsdevfilteripsourceportlow', (YLeaf(YType.int32, 'docsDevFilterIpSourcePortLow'), ['int'])),
                    ('docsdevfilteripsourceporthigh', (YLeaf(YType.int32, 'docsDevFilterIpSourcePortHigh'), ['int'])),
                    ('docsdevfilteripdestportlow', (YLeaf(YType.int32, 'docsDevFilterIpDestPortLow'), ['int'])),
                    ('docsdevfilteripdestporthigh', (YLeaf(YType.int32, 'docsDevFilterIpDestPortHigh'), ['int'])),
                    ('docsdevfilteripmatches', (YLeaf(YType.uint32, 'docsDevFilterIpMatches'), ['int'])),
                    ('docsdevfilteriptos', (YLeaf(YType.str, 'docsDevFilterIpTos'), ['str'])),
                    ('docsdevfilteriptosmask', (YLeaf(YType.str, 'docsDevFilterIpTosMask'), ['str'])),
                    ('docsdevfilteripcontinue', (YLeaf(YType.boolean, 'docsDevFilterIpContinue'), ['bool'])),
                    ('docsdevfilterippolicyid', (YLeaf(YType.int32, 'docsDevFilterIpPolicyId'), ['int'])),
                ])
                self.docsdevfilteripindex = None
                self.docsdevfilteripstatus = None
                self.docsdevfilteripcontrol = None
                self.docsdevfilteripifindex = None
                self.docsdevfilteripdirection = None
                self.docsdevfilteripbroadcast = None
                self.docsdevfilteripsaddr = None
                self.docsdevfilteripsmask = None
                self.docsdevfilteripdaddr = None
                self.docsdevfilteripdmask = None
                self.docsdevfilteripprotocol = None
                self.docsdevfilteripsourceportlow = None
                self.docsdevfilteripsourceporthigh = None
                self.docsdevfilteripdestportlow = None
                self.docsdevfilteripdestporthigh = None
                self.docsdevfilteripmatches = None
                self.docsdevfilteriptos = None
                self.docsdevfilteriptosmask = None
                self.docsdevfilteripcontinue = None
                self.docsdevfilterippolicyid = None
                self._segment_path = lambda: "docsDevFilterIpEntry" + "[docsDevFilterIpIndex='" + str(self.docsdevfilteripindex) + "']"
                self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/docsDevFilterIpTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevFilterIpTable.DocsDevFilterIpEntry, [u'docsdevfilteripindex', u'docsdevfilteripstatus', u'docsdevfilteripcontrol', u'docsdevfilteripifindex', u'docsdevfilteripdirection', u'docsdevfilteripbroadcast', u'docsdevfilteripsaddr', u'docsdevfilteripsmask', u'docsdevfilteripdaddr', u'docsdevfilteripdmask', u'docsdevfilteripprotocol', u'docsdevfilteripsourceportlow', u'docsdevfilteripsourceporthigh', u'docsdevfilteripdestportlow', u'docsdevfilteripdestporthigh', u'docsdevfilteripmatches', u'docsdevfilteriptos', u'docsdevfilteriptosmask', u'docsdevfilteripcontinue', u'docsdevfilterippolicyid'], name, value)

            class DocsDevFilterIpControl(Enum):
                """
                DocsDevFilterIpControl (Enum Class)

                If set to discard(1), all packets matching this filter

                will be discarded, and scanning of the remainder of the

                filter list will be aborted. If set to accept(2), all

                packets matching this filter will be accepted for

                further processing (e.g., bridging).  If

                docsDevFilterIpContinue is set to true, see if there

                are other matches; otherwise, done.  If set to

                policy (3), execute the policy entries

                matched by docsDevFilterIpPolicyId in

                docsDevFilterPolicyTable.

                If docsDevFilterIpContinue is set to true, continue

                scanning the table for other matches; otherwise, done.

                .. data:: discard = 1

                .. data:: accept = 2

                .. data:: policy = 3

                """

                discard = Enum.YLeaf(1, "discard")

                accept = Enum.YLeaf(2, "accept")

                policy = Enum.YLeaf(3, "policy")


            class DocsDevFilterIpDirection(Enum):
                """
                DocsDevFilterIpDirection (Enum Class)

                Determines whether the filter is applied to inbound(1)

                traffic, outbound(2) traffic, or traffic in both(3)

                directions.

                .. data:: inbound = 1

                .. data:: outbound = 2

                .. data:: both = 3

                """

                inbound = Enum.YLeaf(1, "inbound")

                outbound = Enum.YLeaf(2, "outbound")

                both = Enum.YLeaf(3, "both")



    class DocsDevFilterPolicyTable(Entity):
        """
        A Table that maps between a policy group ID and a set
        of pointers to policies to be applied.  All rows with
        the same docsDevFilterPolicyId are part of the same
        group of policy pointers and are applied in the order
        in this table.  docsDevFilterPolicyTable exists to
        allow multiple policy actions (referenced by policy
        pointers) to be applied to any given classified packet.
        The policy actions are applied in index order.
        For example\:
        
        Index   ID    Type    Action
         1      1      TOS     1
         9      5      TOS     1
         12     1      IPSEC   3
        
        This says that a packet that matches a filter with
        policy id 1 first has TOS policy 1 applied (which might
        set the TOS bits to enable a higher priority) and next
        has the IPSEC policy 3 applied (which may result in the
        packets being dumped into a secure VPN to a remote
        encryptor).
        
        Policy ID 0 is reserved for default actions and is
        applied only to packets that match no filters in
        docsDevFilterIpTable.
        
        Table entries MUST NOT persist across reboots for any
        device.
        
        This table is deprecated.  Instead, use the DiffServ MIB
        from RFC3289.
        
        .. attribute:: docsdevfilterpolicyentry
        
        	An entry in the docsDevFilterPolicyTable. Entries are created by Network Management. To create an entry, docsDevFilterPolicyId MUST be specified
        	**type**\: list of  		 :py:class:`DocsDevFilterPolicyEntry <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevFilterPolicyTable.DocsDevFilterPolicyEntry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'DOCS-CABLE-DEVICE-MIB'
        _revision = '2006-12-20'

        def __init__(self):
            super(DOCSCABLEDEVICEMIB.DocsDevFilterPolicyTable, self).__init__()

            self.yang_name = "docsDevFilterPolicyTable"
            self.yang_parent_name = "DOCS-CABLE-DEVICE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsDevFilterPolicyEntry", ("docsdevfilterpolicyentry", DOCSCABLEDEVICEMIB.DocsDevFilterPolicyTable.DocsDevFilterPolicyEntry))])
            self._leafs = OrderedDict()

            self.docsdevfilterpolicyentry = YList(self)
            self._segment_path = lambda: "docsDevFilterPolicyTable"
            self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevFilterPolicyTable, [], name, value)


        class DocsDevFilterPolicyEntry(Entity):
            """
            An entry in the docsDevFilterPolicyTable. Entries are
            created by Network Management. To create an entry,
            docsDevFilterPolicyId MUST be specified.
            
            .. attribute:: docsdevfilterpolicyindex  (key)
            
            	Index value for the table
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfilterpolicyid
            
            	Policy ID for this entry.  If a policy ID can apply to multiple rows of this table, all relevant policies are executed. Policy 0 (if populated) is applied to all packets that do not match any of the filters.  N.B. If docsDevFilterIpPolicyId is set to 0, it DOES NOT match policy 0 of this table
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfilterpolicystatus
            
            	Object used to create an entry in this table.  There is no restriction in changing any object in a row while this object is set to active. The following object MUST have a valid value before this object can be set to active\:  docsDevFilterPolicyPtr
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfilterpolicyptr
            
            	This object points to a row in an applicable filter policy table.  Currently, the only standard policy table is docsDevFilterTosTable.  Per the textual convention, this object points to the first accessible object in the row; e.g., to point to a row in docsDevFilterTosTable with an index of 21, the value of this object would be the object identifier docsDevTosStatus.21.  Vendors are recommended to adhere to the same convention when adding vendor\-specific policy table extensions.  If this pointer references an empty or non\-existent row, then no policy action is taken.  The default upon row creation is a null pointer that results in no policy action being taken
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'DOCS-CABLE-DEVICE-MIB'
            _revision = '2006-12-20'

            def __init__(self):
                super(DOCSCABLEDEVICEMIB.DocsDevFilterPolicyTable.DocsDevFilterPolicyEntry, self).__init__()

                self.yang_name = "docsDevFilterPolicyEntry"
                self.yang_parent_name = "docsDevFilterPolicyTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsdevfilterpolicyindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsdevfilterpolicyindex', (YLeaf(YType.int32, 'docsDevFilterPolicyIndex'), ['int'])),
                    ('docsdevfilterpolicyid', (YLeaf(YType.int32, 'docsDevFilterPolicyId'), ['int'])),
                    ('docsdevfilterpolicystatus', (YLeaf(YType.enumeration, 'docsDevFilterPolicyStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('docsdevfilterpolicyptr', (YLeaf(YType.str, 'docsDevFilterPolicyPtr'), ['str'])),
                ])
                self.docsdevfilterpolicyindex = None
                self.docsdevfilterpolicyid = None
                self.docsdevfilterpolicystatus = None
                self.docsdevfilterpolicyptr = None
                self._segment_path = lambda: "docsDevFilterPolicyEntry" + "[docsDevFilterPolicyIndex='" + str(self.docsdevfilterpolicyindex) + "']"
                self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/docsDevFilterPolicyTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevFilterPolicyTable.DocsDevFilterPolicyEntry, [u'docsdevfilterpolicyindex', u'docsdevfilterpolicyid', u'docsdevfilterpolicystatus', u'docsdevfilterpolicyptr'], name, value)


    class DocsDevFilterTosTable(Entity):
        """
        Table used to describe Type of Service (TOS) bits
        processing.
        
        This table is an adjunct to the docsDevFilterIpTable
        and the docsDevFilterPolicy table.  Entries in the
        latter table can point to specific rows in this (and
        other) tables and cause specific actions to be taken.
        This table permits the manipulation of the value of the
        Type of Service bits in the IP header of the matched
        packet as follows\:
        
        Set the tosBits of the packet to
           (tosBits & docsDevFilterTosAndMask) \|
           docsDevFilterTosOrMask
        
        This construct allows you to do a clear and set of all
        the TOS bits in a flexible manner.
        
        Table entries MUST NOT persist across reboots for any
        device.
        
        This table is deprecated.  Instead, use the DiffServ MIB
        from RFC3289.
        
        .. attribute:: docsdevfiltertosentry
        
        	A TOS policy entry
        	**type**\: list of  		 :py:class:`DocsDevFilterTosEntry <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevFilterTosTable.DocsDevFilterTosEntry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'DOCS-CABLE-DEVICE-MIB'
        _revision = '2006-12-20'

        def __init__(self):
            super(DOCSCABLEDEVICEMIB.DocsDevFilterTosTable, self).__init__()

            self.yang_name = "docsDevFilterTosTable"
            self.yang_parent_name = "DOCS-CABLE-DEVICE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsDevFilterTosEntry", ("docsdevfiltertosentry", DOCSCABLEDEVICEMIB.DocsDevFilterTosTable.DocsDevFilterTosEntry))])
            self._leafs = OrderedDict()

            self.docsdevfiltertosentry = YList(self)
            self._segment_path = lambda: "docsDevFilterTosTable"
            self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevFilterTosTable, [], name, value)


        class DocsDevFilterTosEntry(Entity):
            """
            A TOS policy entry.
            
            .. attribute:: docsdevfiltertosindex  (key)
            
            	The unique index for this row.  There are no ordering requirements for this table, and any valid index may be specified
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfiltertosstatus
            
            	The object used to create and delete entries in this table. A row created by specifying just this object results in a row that specifies no change to the TOS bits.  A row may be created using either the create\-and\-go or create\-and\-wait paradigms.  There is no restriction on the ability to change values in this row while the row is active
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfiltertosandmask
            
            	This value is bitwise ANDed with the matched packet's TOS bits
            	**type**\: str
            
            	**length:** 1
            
            	**status**\: deprecated
            
            .. attribute:: docsdevfiltertosormask
            
            	This value is bitwise ORed with the result from the AND procedure (tosBits & docsDevFilterTosAndMask). The result then replaces the packet's TOS bits
            	**type**\: str
            
            	**length:** 1
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'DOCS-CABLE-DEVICE-MIB'
            _revision = '2006-12-20'

            def __init__(self):
                super(DOCSCABLEDEVICEMIB.DocsDevFilterTosTable.DocsDevFilterTosEntry, self).__init__()

                self.yang_name = "docsDevFilterTosEntry"
                self.yang_parent_name = "docsDevFilterTosTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsdevfiltertosindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsdevfiltertosindex', (YLeaf(YType.int32, 'docsDevFilterTosIndex'), ['int'])),
                    ('docsdevfiltertosstatus', (YLeaf(YType.enumeration, 'docsDevFilterTosStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('docsdevfiltertosandmask', (YLeaf(YType.str, 'docsDevFilterTosAndMask'), ['str'])),
                    ('docsdevfiltertosormask', (YLeaf(YType.str, 'docsDevFilterTosOrMask'), ['str'])),
                ])
                self.docsdevfiltertosindex = None
                self.docsdevfiltertosstatus = None
                self.docsdevfiltertosandmask = None
                self.docsdevfiltertosormask = None
                self._segment_path = lambda: "docsDevFilterTosEntry" + "[docsDevFilterTosIndex='" + str(self.docsdevfiltertosindex) + "']"
                self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/docsDevFilterTosTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevFilterTosTable.DocsDevFilterTosEntry, [u'docsdevfiltertosindex', u'docsdevfiltertosstatus', u'docsdevfiltertosandmask', u'docsdevfiltertosormask'], name, value)


    class DocsDevCpeTable(Entity):
        """
        This table lists the IPv4 addresses seen (or permitted)
        as source addresses in packets originating from the
        customer interface on this device.  In addition, this
        table can be provisioned with the specific addresses
        permitted for the CPEs via the normal row creation
        mechanisms.  Table entries MUST NOT persist across
        reboots for any device.
        
        N.B.  Management action can add entries in this table
        and in docsDevCpeIpTable past the value of
        docsDevCpeIpMax.  docsDevCpeIpMax ONLY restricts the
        ability of the CM to add learned addresses
        automatically.
        
        This table is deprecated and is replaced by
        docsDevCpeInetTable.
        
        .. attribute:: docsdevcpeentry
        
        	An entry in the docsDevFilterCpeTable.  There is one entry for each IPv4 CPE seen or provisioned.  If docsDevCpeIpMax is set to \-1, this table is ignored; otherwise, upon receipt of an IP packet from the customer interface of the CM, the source IP address is checked against this table.  If the address is in the table, packet processing continues.  If the address is not in the table but docsDevCpeEnroll is set to any and the sum of the table sizes of docsDevCpeTable and docsDevCpeInetTable is less than docsDevCpeIpMax, the address is added to the table, and packet processing continues.  Otherwise, the packet is dropped.  The filtering actions specified by this table occur after any LLC filtering (docsDevFilterLLCTable), but prior to any IP filtering (docsDevFilterIpTable, docsDevNmAccessTable)
        	**type**\: list of  		 :py:class:`DocsDevCpeEntry <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevCpeTable.DocsDevCpeEntry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'DOCS-CABLE-DEVICE-MIB'
        _revision = '2006-12-20'

        def __init__(self):
            super(DOCSCABLEDEVICEMIB.DocsDevCpeTable, self).__init__()

            self.yang_name = "docsDevCpeTable"
            self.yang_parent_name = "DOCS-CABLE-DEVICE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsDevCpeEntry", ("docsdevcpeentry", DOCSCABLEDEVICEMIB.DocsDevCpeTable.DocsDevCpeEntry))])
            self._leafs = OrderedDict()

            self.docsdevcpeentry = YList(self)
            self._segment_path = lambda: "docsDevCpeTable"
            self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevCpeTable, [], name, value)


        class DocsDevCpeEntry(Entity):
            """
            An entry in the docsDevFilterCpeTable.  There is one
            entry for each IPv4 CPE seen or provisioned.  If
            docsDevCpeIpMax is set to \-1, this table is ignored;
            otherwise, upon receipt of an IP packet from the
            customer interface of the CM, the source IP address is
            checked against this table.  If the address is in the
            table, packet processing continues.  If the address is
            not in the table but docsDevCpeEnroll is set to any
            and the sum of the table sizes of docsDevCpeTable and
            docsDevCpeInetTable is less than docsDevCpeIpMax, the
            address is added to the table, and packet processing
            continues.  Otherwise, the packet is dropped.
            
            The filtering actions specified by this table occur
            after any LLC filtering (docsDevFilterLLCTable), but
            prior to any IP filtering (docsDevFilterIpTable,
            docsDevNmAccessTable).
            
            .. attribute:: docsdevcpeip  (key)
            
            	The IPv4 address to which this entry applies.  N.B.  Attempts to set all zeros or all ones address values MUST be rejected
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: docsdevcpesource
            
            	This object describes how this entry was created.  If the value is manual(2), this row was created by a network management action (either configuration or SNMP set).  If set to learned(3), then it was found via looking at the source IPv4 address of a received packet. The value other(1) is used for any entries that do not meet manual(2) or learned(3) criteria
            	**type**\:  :py:class:`DocsDevCpeSource <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevCpeTable.DocsDevCpeEntry.DocsDevCpeSource>`
            
            	**status**\: deprecated
            
            .. attribute:: docsdevcpestatus
            
            	Standard object to manipulate rows.  To create a row in this table, one only needs to specify this object. Management stations SHOULD use the create\-and\-go mechanism for creating rows in this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'DOCS-CABLE-DEVICE-MIB'
            _revision = '2006-12-20'

            def __init__(self):
                super(DOCSCABLEDEVICEMIB.DocsDevCpeTable.DocsDevCpeEntry, self).__init__()

                self.yang_name = "docsDevCpeEntry"
                self.yang_parent_name = "docsDevCpeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsdevcpeip']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsdevcpeip', (YLeaf(YType.str, 'docsDevCpeIp'), ['str'])),
                    ('docsdevcpesource', (YLeaf(YType.enumeration, 'docsDevCpeSource'), [('ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB', 'DOCSCABLEDEVICEMIB', 'DocsDevCpeTable.DocsDevCpeEntry.DocsDevCpeSource')])),
                    ('docsdevcpestatus', (YLeaf(YType.enumeration, 'docsDevCpeStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.docsdevcpeip = None
                self.docsdevcpesource = None
                self.docsdevcpestatus = None
                self._segment_path = lambda: "docsDevCpeEntry" + "[docsDevCpeIp='" + str(self.docsdevcpeip) + "']"
                self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/docsDevCpeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevCpeTable.DocsDevCpeEntry, [u'docsdevcpeip', u'docsdevcpesource', u'docsdevcpestatus'], name, value)

            class DocsDevCpeSource(Enum):
                """
                DocsDevCpeSource (Enum Class)

                This object describes how this entry was created.  If

                the value is manual(2), this row was created by a

                network management action (either configuration or

                SNMP set).  If set to learned(3), then it was found via

                looking at the source IPv4 address of a received packet.

                The value other(1) is used for any entries that do not

                meet manual(2) or learned(3) criteria.

                .. data:: other = 1

                .. data:: manual = 2

                .. data:: learned = 3

                """

                other = Enum.YLeaf(1, "other")

                manual = Enum.YLeaf(2, "manual")

                learned = Enum.YLeaf(3, "learned")



    class DocsDevCpeInetTable(Entity):
        """
        This table lists the IP addresses seen (or permitted) as
        source addresses in packets originating from the
        customer interface on this device.  In addition, this
        table can be provisioned with the specific addresses
        permitted for the CPEs via the normal row creation
        mechanisms.
        
        N.B.  Management action can add entries in this table
        and in docsDevCpeIpTable past the value of
        docsDevCpeIpMax.  docsDevCpeIpMax ONLY restricts the
        ability of the CM to add learned addresses
        automatically.
        
        Table entries MUST NOT persist across reboots for any
        device.
        
        This table exactly mirrors docsDevCpeTable and applies
        to IPv4 and IPv6 addresses.
        
        .. attribute:: docsdevcpeinetentry
        
        	An entry in the docsDevFilterCpeInetTable. There is one entry for each IP CPE seen or provisioned. If docsDevCpeIpMax is set to \-1, this table is ignored; otherwise, upon receipt of an IP packet from the customer interface of the CM, the source IP address is checked against this table.  If the address is in the table, packet processing continues.  If the address is not in the table but docsDevCpeEnroll is set to any and the sum of the table sizes for docsDevCpeTable and docsDevCpeInetTable is less than docsDevCpeIpMax, the address is added to the table, and packet processing continues.  Otherwise, the packet is dropped.  The filtering actions specified by this table occur after any LLC filtering (docsDevFilterLLCTable), but prior to any IP filtering (docsDevFilterIpTable, docsDevNmAccessTable).  When an agent (cable modem) restarts, then all dynamically created rows are lost
        	**type**\: list of  		 :py:class:`DocsDevCpeInetEntry <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevCpeInetTable.DocsDevCpeInetEntry>`
        
        

        """

        _prefix = 'DOCS-CABLE-DEVICE-MIB'
        _revision = '2006-12-20'

        def __init__(self):
            super(DOCSCABLEDEVICEMIB.DocsDevCpeInetTable, self).__init__()

            self.yang_name = "docsDevCpeInetTable"
            self.yang_parent_name = "DOCS-CABLE-DEVICE-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsDevCpeInetEntry", ("docsdevcpeinetentry", DOCSCABLEDEVICEMIB.DocsDevCpeInetTable.DocsDevCpeInetEntry))])
            self._leafs = OrderedDict()

            self.docsdevcpeinetentry = YList(self)
            self._segment_path = lambda: "docsDevCpeInetTable"
            self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevCpeInetTable, [], name, value)


        class DocsDevCpeInetEntry(Entity):
            """
            An entry in the docsDevFilterCpeInetTable. There is one
            entry for each IP CPE seen or provisioned. If
            docsDevCpeIpMax is set to \-1, this table is ignored;
            otherwise, upon receipt of an IP packet from the
            customer interface of the CM, the source IP address is
            checked against this table.  If the address is in the
            table, packet processing continues.  If the address is
            not in the table but docsDevCpeEnroll is set to any and
            the sum of the table sizes for docsDevCpeTable and
            docsDevCpeInetTable is less than docsDevCpeIpMax, the
            address is added to the table, and packet processing
            continues.  Otherwise, the packet is dropped.
            
            The filtering actions specified by this table occur
            after any LLC filtering (docsDevFilterLLCTable), but
            prior to any IP filtering (docsDevFilterIpTable,
            docsDevNmAccessTable).
            
            When an agent (cable modem) restarts, then all
            dynamically created rows are lost.
            
            .. attribute:: docsdevcpeinettype  (key)
            
            	The type of internet address of docsDevCpeInetAddr
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: docsdevcpeinetaddr  (key)
            
            	The Internet address to which this entry applies.  Implementors need to be aware that if the size of docsDevCpeInetAddr exceeds 114 octets OIDs of instances of columns in this row will have more than 128 sub\-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3.  Only unicast address are allowed for this object
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: docsdevcpeinetsource
            
            	This object describes how this entry was created.  If the value is manual(2), this row was created by a network management action (either configuration or SNMP set).  If set to learned(3), then it was found via looking at the source IP address of a received packet
            	**type**\:  :py:class:`DocsDevCpeInetSource <ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB.DOCSCABLEDEVICEMIB.DocsDevCpeInetTable.DocsDevCpeInetEntry.DocsDevCpeInetSource>`
            
            .. attribute:: docsdevcpeinetrowstatus
            
            	Standard object to manipulate rows.  To create a row in this table, one only needs to specify this object. Management stations SHOULD use the create\-and\-go mechanism for creating rows in this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DOCS-CABLE-DEVICE-MIB'
            _revision = '2006-12-20'

            def __init__(self):
                super(DOCSCABLEDEVICEMIB.DocsDevCpeInetTable.DocsDevCpeInetEntry, self).__init__()

                self.yang_name = "docsDevCpeInetEntry"
                self.yang_parent_name = "docsDevCpeInetTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsdevcpeinettype','docsdevcpeinetaddr']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsdevcpeinettype', (YLeaf(YType.enumeration, 'docsDevCpeInetType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('docsdevcpeinetaddr', (YLeaf(YType.str, 'docsDevCpeInetAddr'), ['str'])),
                    ('docsdevcpeinetsource', (YLeaf(YType.enumeration, 'docsDevCpeInetSource'), [('ydk.models.cisco_ios_xe.DOCS_CABLE_DEVICE_MIB', 'DOCSCABLEDEVICEMIB', 'DocsDevCpeInetTable.DocsDevCpeInetEntry.DocsDevCpeInetSource')])),
                    ('docsdevcpeinetrowstatus', (YLeaf(YType.enumeration, 'docsDevCpeInetRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.docsdevcpeinettype = None
                self.docsdevcpeinetaddr = None
                self.docsdevcpeinetsource = None
                self.docsdevcpeinetrowstatus = None
                self._segment_path = lambda: "docsDevCpeInetEntry" + "[docsDevCpeInetType='" + str(self.docsdevcpeinettype) + "']" + "[docsDevCpeInetAddr='" + str(self.docsdevcpeinetaddr) + "']"
                self._absolute_path = lambda: "DOCS-CABLE-DEVICE-MIB:DOCS-CABLE-DEVICE-MIB/docsDevCpeInetTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSCABLEDEVICEMIB.DocsDevCpeInetTable.DocsDevCpeInetEntry, [u'docsdevcpeinettype', u'docsdevcpeinetaddr', u'docsdevcpeinetsource', u'docsdevcpeinetrowstatus'], name, value)

            class DocsDevCpeInetSource(Enum):
                """
                DocsDevCpeInetSource (Enum Class)

                This object describes how this entry was created.  If

                the value is manual(2), this row was created by a

                network management action (either configuration or

                SNMP set).  If set to learned(3), then it was found

                via looking at the source IP address of a received

                packet.

                .. data:: manual = 2

                .. data:: learned = 3

                """

                manual = Enum.YLeaf(2, "manual")

                learned = Enum.YLeaf(3, "learned")


    def clone_ptr(self):
        self._top_entity = DOCSCABLEDEVICEMIB()
        return self._top_entity


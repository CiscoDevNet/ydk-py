""" CISCO_CDP_MIB 

The MIB module for management of the Cisco Discovery
Protocol in Cisco devices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOCDPMIB(Entity):
    """
    
    
    .. attribute:: cdpglobal
    
    	
    	**type**\:  :py:class:`Cdpglobal <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CISCOCDPMIB.Cdpglobal>`
    
    .. attribute:: cdpinterfacetable
    
    	The (conceptual) table containing the status of CDP on the device's interfaces
    	**type**\:  :py:class:`Cdpinterfacetable <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CISCOCDPMIB.Cdpinterfacetable>`
    
    .. attribute:: cdpinterfaceexttable
    
    	This table contains the additional CDP configuration on the device's interfaces
    	**type**\:  :py:class:`Cdpinterfaceexttable <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CISCOCDPMIB.Cdpinterfaceexttable>`
    
    .. attribute:: cdpcachetable
    
    	The (conceptual) table containing the cached information obtained via receiving CDP messages
    	**type**\:  :py:class:`Cdpcachetable <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CISCOCDPMIB.Cdpcachetable>`
    
    .. attribute:: cdpctaddresstable
    
    	The (conceptual) table containing the list of  network\-layer addresses of a neighbor interface, as reported in the Address TLV of the most recently received CDP message. The first address included in the Address TLV is saved in cdpCacheAddress.  This table contains the remainder of the addresses in the Address TLV
    	**type**\:  :py:class:`Cdpctaddresstable <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CISCOCDPMIB.Cdpctaddresstable>`
    
    

    """

    _prefix = 'CISCO-CDP-MIB'
    _revision = '2005-03-21'

    def __init__(self):
        super(CISCOCDPMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-CDP-MIB"
        self.yang_parent_name = "CISCO-CDP-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("cdpGlobal", ("cdpglobal", CISCOCDPMIB.Cdpglobal)), ("cdpInterfaceTable", ("cdpinterfacetable", CISCOCDPMIB.Cdpinterfacetable)), ("cdpInterfaceExtTable", ("cdpinterfaceexttable", CISCOCDPMIB.Cdpinterfaceexttable)), ("cdpCacheTable", ("cdpcachetable", CISCOCDPMIB.Cdpcachetable)), ("cdpCtAddressTable", ("cdpctaddresstable", CISCOCDPMIB.Cdpctaddresstable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cdpglobal = CISCOCDPMIB.Cdpglobal()
        self.cdpglobal.parent = self
        self._children_name_map["cdpglobal"] = "cdpGlobal"
        self._children_yang_names.add("cdpGlobal")

        self.cdpinterfacetable = CISCOCDPMIB.Cdpinterfacetable()
        self.cdpinterfacetable.parent = self
        self._children_name_map["cdpinterfacetable"] = "cdpInterfaceTable"
        self._children_yang_names.add("cdpInterfaceTable")

        self.cdpinterfaceexttable = CISCOCDPMIB.Cdpinterfaceexttable()
        self.cdpinterfaceexttable.parent = self
        self._children_name_map["cdpinterfaceexttable"] = "cdpInterfaceExtTable"
        self._children_yang_names.add("cdpInterfaceExtTable")

        self.cdpcachetable = CISCOCDPMIB.Cdpcachetable()
        self.cdpcachetable.parent = self
        self._children_name_map["cdpcachetable"] = "cdpCacheTable"
        self._children_yang_names.add("cdpCacheTable")

        self.cdpctaddresstable = CISCOCDPMIB.Cdpctaddresstable()
        self.cdpctaddresstable.parent = self
        self._children_name_map["cdpctaddresstable"] = "cdpCtAddressTable"
        self._children_yang_names.add("cdpCtAddressTable")
        self._segment_path = lambda: "CISCO-CDP-MIB:CISCO-CDP-MIB"


    class Cdpglobal(Entity):
        """
        
        
        .. attribute:: cdpglobalrun
        
        	An indication of whether the Cisco Discovery Protocol is currently running.  Entries in cdpCacheTable are deleted when CDP is disabled
        	**type**\: bool
        
        .. attribute:: cdpglobalmessageinterval
        
        	The interval at which CDP messages are to be generated. The default value is 60 seconds
        	**type**\: int
        
        	**range:** 5..254
        
        	**units**\: seconds
        
        .. attribute:: cdpglobalholdtime
        
        	The time for the receiving device holds CDP message. The default value is 180 seconds
        	**type**\: int
        
        	**range:** 10..255
        
        	**units**\: seconds
        
        .. attribute:: cdpglobaldeviceid
        
        	The device ID advertised by this device. The format of this device id is characterized by the value of  cdpGlobalDeviceIdFormat object
        	**type**\: str
        
        .. attribute:: cdpgloballastchange
        
        	Indicates the time when the cache table was last changed. It is the most recent time at which any row was last created, modified or deleted
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cdpglobaldeviceidformatcpb
        
        	Indicate the Device\-Id format capability of the device.  serialNumber(0) indicates that the device supports using serial number as the format for its DeviceId.  macAddress(1) indicates that the device supports using layer 2 MAC address as the format for its DeviceId.  other(2) indicates that the device supports using its platform specific format as the format for its DeviceId
        	**type**\:  :py:class:`Cdpglobaldeviceidformatcpb <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CISCOCDPMIB.Cdpglobal.Cdpglobaldeviceidformatcpb>`
        
        .. attribute:: cdpglobaldeviceidformat
        
        	An indication of the format of Device\-Id contained in the corresponding instance of cdpGlobalDeviceId. User can only specify the formats that the device is capable of as denoted in cdpGlobalDeviceIdFormatCpb object.  serialNumber(1) indicates that the value of cdpGlobalDeviceId  object is in the form of an ASCII string contain the device serial number.   macAddress(2) indicates that the value of cdpGlobalDeviceId  object is in the form of Layer 2 MAC address.  other(3) indicates that the value of cdpGlobalDeviceId object is in the form of a platform specific ASCII string contain info that identifies the device. For example\: ASCII string contains serialNumber appended/prepened with system name
        	**type**\:  :py:class:`Cdpglobaldeviceidformat <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CISCOCDPMIB.Cdpglobal.Cdpglobaldeviceidformat>`
        
        

        """

        _prefix = 'CISCO-CDP-MIB'
        _revision = '2005-03-21'

        def __init__(self):
            super(CISCOCDPMIB.Cdpglobal, self).__init__()

            self.yang_name = "cdpGlobal"
            self.yang_parent_name = "CISCO-CDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cdpglobalrun', YLeaf(YType.boolean, 'cdpGlobalRun')),
                ('cdpglobalmessageinterval', YLeaf(YType.int32, 'cdpGlobalMessageInterval')),
                ('cdpglobalholdtime', YLeaf(YType.int32, 'cdpGlobalHoldTime')),
                ('cdpglobaldeviceid', YLeaf(YType.str, 'cdpGlobalDeviceId')),
                ('cdpgloballastchange', YLeaf(YType.uint32, 'cdpGlobalLastChange')),
                ('cdpglobaldeviceidformatcpb', YLeaf(YType.bits, 'cdpGlobalDeviceIdFormatCpb')),
                ('cdpglobaldeviceidformat', YLeaf(YType.enumeration, 'cdpGlobalDeviceIdFormat')),
            ])
            self.cdpglobalrun = None
            self.cdpglobalmessageinterval = None
            self.cdpglobalholdtime = None
            self.cdpglobaldeviceid = None
            self.cdpgloballastchange = None
            self.cdpglobaldeviceidformatcpb = Bits()
            self.cdpglobaldeviceidformat = None
            self._segment_path = lambda: "cdpGlobal"
            self._absolute_path = lambda: "CISCO-CDP-MIB:CISCO-CDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCDPMIB.Cdpglobal, ['cdpglobalrun', 'cdpglobalmessageinterval', 'cdpglobalholdtime', 'cdpglobaldeviceid', 'cdpgloballastchange', 'cdpglobaldeviceidformatcpb', 'cdpglobaldeviceidformat'], name, value)

        class Cdpglobaldeviceidformat(Enum):
            """
            Cdpglobaldeviceidformat (Enum Class)

            An indication of the format of Device\-Id contained in the

            corresponding instance of cdpGlobalDeviceId. User can only

            specify the formats that the device is capable of as

            denoted in cdpGlobalDeviceIdFormatCpb object.

            serialNumber(1) indicates that the value of cdpGlobalDeviceId 

            object is in the form of an ASCII string contain the device

            serial number. 

            macAddress(2) indicates that the value of cdpGlobalDeviceId 

            object is in the form of Layer 2 MAC address.

            other(3) indicates that the value of cdpGlobalDeviceId object

            is in the form of a platform specific ASCII string contain

            info that identifies the device. For example\: ASCII string

            contains serialNumber appended/prepened with system name.

            .. data:: serialNumber = 1

            .. data:: macAddress = 2

            .. data:: other = 3

            """

            serialNumber = Enum.YLeaf(1, "serialNumber")

            macAddress = Enum.YLeaf(2, "macAddress")

            other = Enum.YLeaf(3, "other")



    class Cdpinterfacetable(Entity):
        """
        The (conceptual) table containing the status of CDP on
        the device's interfaces.
        
        .. attribute:: cdpinterfaceentry
        
        	An entry (conceptual row) in the cdpInterfaceTable, containing the status of CDP on an interface
        	**type**\: list of  		 :py:class:`Cdpinterfaceentry <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CISCOCDPMIB.Cdpinterfacetable.Cdpinterfaceentry>`
        
        

        """

        _prefix = 'CISCO-CDP-MIB'
        _revision = '2005-03-21'

        def __init__(self):
            super(CISCOCDPMIB.Cdpinterfacetable, self).__init__()

            self.yang_name = "cdpInterfaceTable"
            self.yang_parent_name = "CISCO-CDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cdpInterfaceEntry", ("cdpinterfaceentry", CISCOCDPMIB.Cdpinterfacetable.Cdpinterfaceentry))])
            self._leafs = OrderedDict()

            self.cdpinterfaceentry = YList(self)
            self._segment_path = lambda: "cdpInterfaceTable"
            self._absolute_path = lambda: "CISCO-CDP-MIB:CISCO-CDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCDPMIB.Cdpinterfacetable, [], name, value)


        class Cdpinterfaceentry(Entity):
            """
            An entry (conceptual row) in the cdpInterfaceTable,
            containing the status of CDP on an interface.
            
            .. attribute:: cdpinterfaceifindex  (key)
            
            	The ifIndex value of the local interface.  For 802.3 Repeaters on which the repeater ports do not have ifIndex values assigned, this value is a unique value for the port, and greater than any ifIndex value supported by the repeater; in this case, the specific port is indicated by corresponding values of cdpInterfaceGroup and cdpInterfacePort, where these values correspond to the group number and port number values of RFC 1516
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cdpinterfaceenable
            
            	An indication of whether the Cisco Discovery Protocol is currently running on this interface.  This variable has no effect when CDP is disabled (cdpGlobalRun = FALSE)
            	**type**\: bool
            
            .. attribute:: cdpinterfacemessageinterval
            
            	The interval at which CDP messages are to be generated on this interface.  The default value is 60 seconds
            	**type**\: int
            
            	**range:** 0..254
            
            	**units**\: seconds
            
            	**status**\: obsolete
            
            .. attribute:: cdpinterfacegroup
            
            	This object is only relevant to interfaces which are repeater ports on 802.3 repeaters.  In this situation, it indicates the RFC1516 group number of the repeater port which corresponds to this interface
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cdpinterfaceport
            
            	This object is only relevant to interfaces which are repeater ports on 802.3 repeaters.  In this situation, it indicates the RFC1516 port number of the repeater port which corresponds to this interface
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cdpinterfacename
            
            	The name of the local interface as advertised by CDP in the Port\-ID TLV
            	**type**\: str
            
            

            """

            _prefix = 'CISCO-CDP-MIB'
            _revision = '2005-03-21'

            def __init__(self):
                super(CISCOCDPMIB.Cdpinterfacetable.Cdpinterfaceentry, self).__init__()

                self.yang_name = "cdpInterfaceEntry"
                self.yang_parent_name = "cdpInterfaceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdpinterfaceifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdpinterfaceifindex', YLeaf(YType.int32, 'cdpInterfaceIfIndex')),
                    ('cdpinterfaceenable', YLeaf(YType.boolean, 'cdpInterfaceEnable')),
                    ('cdpinterfacemessageinterval', YLeaf(YType.int32, 'cdpInterfaceMessageInterval')),
                    ('cdpinterfacegroup', YLeaf(YType.int32, 'cdpInterfaceGroup')),
                    ('cdpinterfaceport', YLeaf(YType.int32, 'cdpInterfacePort')),
                    ('cdpinterfacename', YLeaf(YType.str, 'cdpInterfaceName')),
                ])
                self.cdpinterfaceifindex = None
                self.cdpinterfaceenable = None
                self.cdpinterfacemessageinterval = None
                self.cdpinterfacegroup = None
                self.cdpinterfaceport = None
                self.cdpinterfacename = None
                self._segment_path = lambda: "cdpInterfaceEntry" + "[cdpInterfaceIfIndex='" + str(self.cdpinterfaceifindex) + "']"
                self._absolute_path = lambda: "CISCO-CDP-MIB:CISCO-CDP-MIB/cdpInterfaceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCDPMIB.Cdpinterfacetable.Cdpinterfaceentry, ['cdpinterfaceifindex', 'cdpinterfaceenable', 'cdpinterfacemessageinterval', 'cdpinterfacegroup', 'cdpinterfaceport', 'cdpinterfacename'], name, value)


    class Cdpinterfaceexttable(Entity):
        """
        This table contains the additional CDP configuration on
        the device's interfaces.
        
        .. attribute:: cdpinterfaceextentry
        
        	An entry in the cdpInterfaceExtTable contains the values configured for Extented Trust TLV and COS (Class of Service) for Untrusted Ports TLV on an interface which supports the sending of these TLVs
        	**type**\: list of  		 :py:class:`Cdpinterfaceextentry <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CISCOCDPMIB.Cdpinterfaceexttable.Cdpinterfaceextentry>`
        
        

        """

        _prefix = 'CISCO-CDP-MIB'
        _revision = '2005-03-21'

        def __init__(self):
            super(CISCOCDPMIB.Cdpinterfaceexttable, self).__init__()

            self.yang_name = "cdpInterfaceExtTable"
            self.yang_parent_name = "CISCO-CDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cdpInterfaceExtEntry", ("cdpinterfaceextentry", CISCOCDPMIB.Cdpinterfaceexttable.Cdpinterfaceextentry))])
            self._leafs = OrderedDict()

            self.cdpinterfaceextentry = YList(self)
            self._segment_path = lambda: "cdpInterfaceExtTable"
            self._absolute_path = lambda: "CISCO-CDP-MIB:CISCO-CDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCDPMIB.Cdpinterfaceexttable, [], name, value)


        class Cdpinterfaceextentry(Entity):
            """
            An entry in the cdpInterfaceExtTable contains the values
            configured for Extented Trust TLV and COS (Class of Service)
            for Untrusted Ports TLV on an interface which supports the
            sending of these TLVs.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: cdpinterfaceextendedtrust
            
            	Indicates the value to be sent by Extended Trust TLV.  If trusted(1) is configured, the value of Extended Trust TLV is one byte in length with its least significant bit equal to 1 to indicate extended trust. All other bits are 0.  If noTrust(2) is configured, the value of Extended Trust TLV is one byte in length with its least significant bit equal to 0 to indicate no extended trust. All other bits are 0
            	**type**\:  :py:class:`Cdpinterfaceextendedtrust <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CISCOCDPMIB.Cdpinterfaceexttable.Cdpinterfaceextentry.Cdpinterfaceextendedtrust>`
            
            .. attribute:: cdpinterfacecosforuntrustedport
            
            	Indicates the value to be sent by COS for Untrusted Ports TLV
            	**type**\: int
            
            	**range:** 0..7
            
            

            """

            _prefix = 'CISCO-CDP-MIB'
            _revision = '2005-03-21'

            def __init__(self):
                super(CISCOCDPMIB.Cdpinterfaceexttable.Cdpinterfaceextentry, self).__init__()

                self.yang_name = "cdpInterfaceExtEntry"
                self.yang_parent_name = "cdpInterfaceExtTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('cdpinterfaceextendedtrust', YLeaf(YType.enumeration, 'cdpInterfaceExtendedTrust')),
                    ('cdpinterfacecosforuntrustedport', YLeaf(YType.uint32, 'cdpInterfaceCosForUntrustedPort')),
                ])
                self.ifindex = None
                self.cdpinterfaceextendedtrust = None
                self.cdpinterfacecosforuntrustedport = None
                self._segment_path = lambda: "cdpInterfaceExtEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-CDP-MIB:CISCO-CDP-MIB/cdpInterfaceExtTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCDPMIB.Cdpinterfaceexttable.Cdpinterfaceextentry, ['ifindex', 'cdpinterfaceextendedtrust', 'cdpinterfacecosforuntrustedport'], name, value)

            class Cdpinterfaceextendedtrust(Enum):
                """
                Cdpinterfaceextendedtrust (Enum Class)

                Indicates the value to be sent by Extended Trust TLV.

                If trusted(1) is configured, the value of Extended Trust TLV

                is one byte in length with its least significant bit equal to

                1 to indicate extended trust. All other bits are 0.

                If noTrust(2) is configured, the value of Extended Trust TLV

                is one byte in length with its least significant bit equal to

                0 to indicate no extended trust. All other bits are 0.

                .. data:: trusted = 1

                .. data:: noTrust = 2

                """

                trusted = Enum.YLeaf(1, "trusted")

                noTrust = Enum.YLeaf(2, "noTrust")



    class Cdpcachetable(Entity):
        """
        The (conceptual) table containing the cached
        information obtained via receiving CDP messages.
        
        .. attribute:: cdpcacheentry
        
        	An entry (conceptual row) in the cdpCacheTable, containing the information received via CDP on one interface from one device.  Entries appear when a CDP advertisement is received from a neighbor device.  Entries disappear when CDP is disabled on the interface, or globally
        	**type**\: list of  		 :py:class:`Cdpcacheentry <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CISCOCDPMIB.Cdpcachetable.Cdpcacheentry>`
        
        

        """

        _prefix = 'CISCO-CDP-MIB'
        _revision = '2005-03-21'

        def __init__(self):
            super(CISCOCDPMIB.Cdpcachetable, self).__init__()

            self.yang_name = "cdpCacheTable"
            self.yang_parent_name = "CISCO-CDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cdpCacheEntry", ("cdpcacheentry", CISCOCDPMIB.Cdpcachetable.Cdpcacheentry))])
            self._leafs = OrderedDict()

            self.cdpcacheentry = YList(self)
            self._segment_path = lambda: "cdpCacheTable"
            self._absolute_path = lambda: "CISCO-CDP-MIB:CISCO-CDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCDPMIB.Cdpcachetable, [], name, value)


        class Cdpcacheentry(Entity):
            """
            An entry (conceptual row) in the cdpCacheTable,
            containing the information received via CDP on one
            interface from one device.  Entries appear when
            a CDP advertisement is received from a neighbor
            device.  Entries disappear when CDP is disabled
            on the interface, or globally.
            
            .. attribute:: cdpcacheifindex  (key)
            
            	Normally, the ifIndex value of the local interface. For 802.3 Repeaters for which the repeater ports do not have ifIndex values assigned, this value is a unique value for the port, and greater than any ifIndex value supported by the repeater; the specific port number in this case, is given by the corresponding value of cdpInterfacePort
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cdpcachedeviceindex  (key)
            
            	A unique value for each device from which CDP messages are being received
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cdpcacheaddresstype
            
            	An indication of the type of address contained in the corresponding instance of cdpCacheAddress
            	**type**\:  :py:class:`CiscoNetworkProtocol <ydk.models.cisco_ios_xe.CISCO_TC.CiscoNetworkProtocol>`
            
            .. attribute:: cdpcacheaddress
            
            	The (first) network\-layer address of the device as reported in the Address TLV of the most recently received CDP message.  For example, if the corresponding instance of cacheAddressType had the value 'ip(1)', then this object  would be an IPv4\-address.  If the neighbor device is  SNMP\-manageable, it is supposed to generate its CDP messages such that this address is one at which it will receive SNMP messages. Use cdpCtAddressTable to extract the remaining addresses from the Address TLV received most recently
            	**type**\: str
            
            .. attribute:: cdpcacheversion
            
            	The Version string as reported in the most recent CDP message.  The zero\-length string indicates no Version field (TLV) was reported in the most recent CDP message
            	**type**\: str
            
            .. attribute:: cdpcachedeviceid
            
            	The Device\-ID string as reported in the most recent CDP message.  The zero\-length string indicates no Device\-ID field (TLV) was reported in the most recent CDP message
            	**type**\: str
            
            .. attribute:: cdpcachedeviceport
            
            	The Port\-ID string as reported in the most recent CDP message.  This will typically be the value of the ifName object (e.g., 'Ethernet0').  The zero\-length string indicates no Port\-ID field (TLV) was reported in the most recent CDP message
            	**type**\: str
            
            .. attribute:: cdpcacheplatform
            
            	The Device's Hardware Platform as reported in the most recent CDP message.  The zero\-length string indicates that no Platform field (TLV) was reported in the most recent CDP message
            	**type**\: str
            
            .. attribute:: cdpcachecapabilities
            
            	The Device's Functional Capabilities as reported in the most recent CDP message.  For latest set of specific values, see the latest version of the CDP specification. The zero\-length string indicates no Capabilities field (TLV) was reported in the most recent CDP message
            	**type**\: str
            
            	**length:** 0..4
            
            .. attribute:: cdpcachevtpmgmtdomain
            
            	The VTP Management Domain for the remote device's interface,  as reported in the most recently received CDP message. This object is not instantiated if no VTP Management Domain field (TLV) was reported in the most recently received CDP message
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: cdpcachenativevlan
            
            	The remote device's interface's native VLAN, as reported in the  most recent CDP message.  The value 0 indicates no native VLAN field (TLV) was reported in the most recent CDP message
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: cdpcacheduplex
            
            	The remote device's interface's duplex mode, as reported in the  most recent CDP message.  The value unknown(1) indicates no duplex mode field (TLV) was reported in the most recent CDP message
            	**type**\:  :py:class:`Cdpcacheduplex <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CISCOCDPMIB.Cdpcachetable.Cdpcacheentry.Cdpcacheduplex>`
            
            .. attribute:: cdpcacheapplianceid
            
            	The remote device's Appliance ID, as reported in the  most recent CDP message. This object is not instantiated if no Appliance VLAN\-ID field (TLV) was reported in the most recently received CDP message
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cdpcachevlanid
            
            	The remote device's VoIP VLAN ID, as reported in the  most recent CDP message. This object is not instantiated if no Appliance VLAN\-ID field (TLV) was reported in the most recently received CDP message
            	**type**\: int
            
            	**range:** 0..4095
            
            .. attribute:: cdpcachepowerconsumption
            
            	The amount of power consumed by remote device, as reported in the most recent CDP message. This object is not instantiated if no Power Consumption field (TLV) was reported in the most recently received CDP message
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliwatts
            
            .. attribute:: cdpcachemtu
            
            	Indicates the size of the largest datagram that can be sent/received by remote device, as reported in the most recent CDP message. This object is not instantiated if no MTU field (TLV) was reported in the most recently received CDP message
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cdpcachesysname
            
            	Indicates the value of the remote device's sysName MIB object. By convention, it is the device's fully qualified domain name. This object is not instantiated if no sysName field (TLV) was reported in the most recently received CDP message
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cdpcachesysobjectid
            
            	Indicates the value of the remote device's sysObjectID MIB object. This object is not instantiated if no sysObjectID field (TLV) was reported in the most recently received CDP message
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: cdpcacheprimarymgmtaddrtype
            
            	An indication of the type of address contained in the corresponding instance of cdpCachePrimaryMgmtAddress
            	**type**\:  :py:class:`CiscoNetworkProtocol <ydk.models.cisco_ios_xe.CISCO_TC.CiscoNetworkProtocol>`
            
            .. attribute:: cdpcacheprimarymgmtaddr
            
            	This object indicates the (first) network layer address at which the device will accept SNMP messages as reported in the first address in the  Management\-Address TLV of the most recently received CDP message.  If the corresponding instance of  cdpCachePrimaryMgmtAddrType has the value 'ip(1)', then this object would be an IP\-address. If the  remote device is not currently manageable via any  network protocol, then it reports the special value  of the IPv4 address 0.0.0.0, and that address is  recorded in this object.  If the most recently received CDP message did not contain the Management\-Address TLV, then this object is not instanstiated
            	**type**\: str
            
            .. attribute:: cdpcachesecondarymgmtaddrtype
            
            	An indication of the type of address contained in the corresponding instance of cdpCacheSecondaryMgmtAddress
            	**type**\:  :py:class:`CiscoNetworkProtocol <ydk.models.cisco_ios_xe.CISCO_TC.CiscoNetworkProtocol>`
            
            .. attribute:: cdpcachesecondarymgmtaddr
            
            	This object indicates the alternate network layer address at which the device will accept SNMP messages as reported in the second address in the  Management\-Address TLV of the most recently received CDP message.  If the corresponding instance of cdpCacheSecondaryMgmtAddrType has the value 'ip(1)', then this object would be an IP\-address. If the  remote device reports the special value of the  IPv4 address 0.0.0.0, that address is recorded in  this object.  If the most recently received CDP message did not contain the Management\-Address TLV, or if that TLV contained only one address, then this object is not instanstiated
            	**type**\: str
            
            .. attribute:: cdpcachephyslocation
            
            	Indicates the physical location, as reported by the most recent CDP message, of a connector which is on, or physically connected to, the remote device's interface over which the CDP packet is sent. This object is not instantiated if no Physical Location field (TLV) was reported by the most recently received CDP message
            	**type**\: str
            
            .. attribute:: cdpcachelastchange
            
            	Indicates the time when this cache entry was last changed. This object is initialised to the current time when the entry gets created and updated to the current time whenever the value of any (other) object instance in the corresponding row is modified
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-CDP-MIB'
            _revision = '2005-03-21'

            def __init__(self):
                super(CISCOCDPMIB.Cdpcachetable.Cdpcacheentry, self).__init__()

                self.yang_name = "cdpCacheEntry"
                self.yang_parent_name = "cdpCacheTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdpcacheifindex','cdpcachedeviceindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdpcacheifindex', YLeaf(YType.int32, 'cdpCacheIfIndex')),
                    ('cdpcachedeviceindex', YLeaf(YType.int32, 'cdpCacheDeviceIndex')),
                    ('cdpcacheaddresstype', YLeaf(YType.enumeration, 'cdpCacheAddressType')),
                    ('cdpcacheaddress', YLeaf(YType.str, 'cdpCacheAddress')),
                    ('cdpcacheversion', YLeaf(YType.str, 'cdpCacheVersion')),
                    ('cdpcachedeviceid', YLeaf(YType.str, 'cdpCacheDeviceId')),
                    ('cdpcachedeviceport', YLeaf(YType.str, 'cdpCacheDevicePort')),
                    ('cdpcacheplatform', YLeaf(YType.str, 'cdpCachePlatform')),
                    ('cdpcachecapabilities', YLeaf(YType.str, 'cdpCacheCapabilities')),
                    ('cdpcachevtpmgmtdomain', YLeaf(YType.str, 'cdpCacheVTPMgmtDomain')),
                    ('cdpcachenativevlan', YLeaf(YType.int32, 'cdpCacheNativeVLAN')),
                    ('cdpcacheduplex', YLeaf(YType.enumeration, 'cdpCacheDuplex')),
                    ('cdpcacheapplianceid', YLeaf(YType.uint32, 'cdpCacheApplianceID')),
                    ('cdpcachevlanid', YLeaf(YType.uint32, 'cdpCacheVlanID')),
                    ('cdpcachepowerconsumption', YLeaf(YType.uint32, 'cdpCachePowerConsumption')),
                    ('cdpcachemtu', YLeaf(YType.uint32, 'cdpCacheMTU')),
                    ('cdpcachesysname', YLeaf(YType.str, 'cdpCacheSysName')),
                    ('cdpcachesysobjectid', YLeaf(YType.str, 'cdpCacheSysObjectID')),
                    ('cdpcacheprimarymgmtaddrtype', YLeaf(YType.enumeration, 'cdpCachePrimaryMgmtAddrType')),
                    ('cdpcacheprimarymgmtaddr', YLeaf(YType.str, 'cdpCachePrimaryMgmtAddr')),
                    ('cdpcachesecondarymgmtaddrtype', YLeaf(YType.enumeration, 'cdpCacheSecondaryMgmtAddrType')),
                    ('cdpcachesecondarymgmtaddr', YLeaf(YType.str, 'cdpCacheSecondaryMgmtAddr')),
                    ('cdpcachephyslocation', YLeaf(YType.str, 'cdpCachePhysLocation')),
                    ('cdpcachelastchange', YLeaf(YType.uint32, 'cdpCacheLastChange')),
                ])
                self.cdpcacheifindex = None
                self.cdpcachedeviceindex = None
                self.cdpcacheaddresstype = None
                self.cdpcacheaddress = None
                self.cdpcacheversion = None
                self.cdpcachedeviceid = None
                self.cdpcachedeviceport = None
                self.cdpcacheplatform = None
                self.cdpcachecapabilities = None
                self.cdpcachevtpmgmtdomain = None
                self.cdpcachenativevlan = None
                self.cdpcacheduplex = None
                self.cdpcacheapplianceid = None
                self.cdpcachevlanid = None
                self.cdpcachepowerconsumption = None
                self.cdpcachemtu = None
                self.cdpcachesysname = None
                self.cdpcachesysobjectid = None
                self.cdpcacheprimarymgmtaddrtype = None
                self.cdpcacheprimarymgmtaddr = None
                self.cdpcachesecondarymgmtaddrtype = None
                self.cdpcachesecondarymgmtaddr = None
                self.cdpcachephyslocation = None
                self.cdpcachelastchange = None
                self._segment_path = lambda: "cdpCacheEntry" + "[cdpCacheIfIndex='" + str(self.cdpcacheifindex) + "']" + "[cdpCacheDeviceIndex='" + str(self.cdpcachedeviceindex) + "']"
                self._absolute_path = lambda: "CISCO-CDP-MIB:CISCO-CDP-MIB/cdpCacheTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCDPMIB.Cdpcachetable.Cdpcacheentry, ['cdpcacheifindex', 'cdpcachedeviceindex', 'cdpcacheaddresstype', 'cdpcacheaddress', 'cdpcacheversion', 'cdpcachedeviceid', 'cdpcachedeviceport', 'cdpcacheplatform', 'cdpcachecapabilities', 'cdpcachevtpmgmtdomain', 'cdpcachenativevlan', 'cdpcacheduplex', 'cdpcacheapplianceid', 'cdpcachevlanid', 'cdpcachepowerconsumption', 'cdpcachemtu', 'cdpcachesysname', 'cdpcachesysobjectid', 'cdpcacheprimarymgmtaddrtype', 'cdpcacheprimarymgmtaddr', 'cdpcachesecondarymgmtaddrtype', 'cdpcachesecondarymgmtaddr', 'cdpcachephyslocation', 'cdpcachelastchange'], name, value)

            class Cdpcacheduplex(Enum):
                """
                Cdpcacheduplex (Enum Class)

                The remote device's interface's duplex mode, as reported in the 

                most recent CDP message.  The value unknown(1) indicates

                no duplex mode field (TLV) was reported in the most

                recent CDP message.

                .. data:: unknown = 1

                .. data:: halfduplex = 2

                .. data:: fullduplex = 3

                """

                unknown = Enum.YLeaf(1, "unknown")

                halfduplex = Enum.YLeaf(2, "halfduplex")

                fullduplex = Enum.YLeaf(3, "fullduplex")



    class Cdpctaddresstable(Entity):
        """
        The (conceptual) table containing the list of 
        network\-layer addresses of a neighbor interface,
        as reported in the Address TLV of the most recently
        received CDP message. The first address included in
        the Address TLV is saved in cdpCacheAddress.  This
        table contains the remainder of the addresses in the
        Address TLV.
        
        .. attribute:: cdpctaddressentry
        
        	An entry (conceptual row) in the cdpCtAddressTable, containing the information on one address received via CDP  on one interface from one device.  Entries appear  when a CDP advertisement is received from a neighbor device, with an Address TLV.  Entries disappear when CDP is disabled on the interface, or globally. An entry  or entries would also disappear if the most recently received CDP packet contain fewer address entries in the Address TLV, than are currently present in the CDP cache
        	**type**\: list of  		 :py:class:`Cdpctaddressentry <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CISCOCDPMIB.Cdpctaddresstable.Cdpctaddressentry>`
        
        

        """

        _prefix = 'CISCO-CDP-MIB'
        _revision = '2005-03-21'

        def __init__(self):
            super(CISCOCDPMIB.Cdpctaddresstable, self).__init__()

            self.yang_name = "cdpCtAddressTable"
            self.yang_parent_name = "CISCO-CDP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cdpCtAddressEntry", ("cdpctaddressentry", CISCOCDPMIB.Cdpctaddresstable.Cdpctaddressentry))])
            self._leafs = OrderedDict()

            self.cdpctaddressentry = YList(self)
            self._segment_path = lambda: "cdpCtAddressTable"
            self._absolute_path = lambda: "CISCO-CDP-MIB:CISCO-CDP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCDPMIB.Cdpctaddresstable, [], name, value)


        class Cdpctaddressentry(Entity):
            """
            An entry (conceptual row) in the cdpCtAddressTable,
            containing the information on one address received via CDP 
            on one interface from one device.  Entries appear 
            when a CDP advertisement is received from a neighbor
            device, with an Address TLV.  Entries disappear when
            CDP is disabled on the interface, or globally. An entry 
            or entries would also disappear if the most recently
            received CDP packet contain fewer address entries in the
            Address TLV, than are currently present in the CDP cache.
            
            .. attribute:: cdpcacheifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`cdpcacheifindex <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CISCOCDPMIB.Cdpcachetable.Cdpcacheentry>`
            
            .. attribute:: cdpcachedeviceindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`cdpcachedeviceindex <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CISCOCDPMIB.Cdpcachetable.Cdpcacheentry>`
            
            .. attribute:: cdpctaddressindex  (key)
            
            	The index of the address entry for a given  cdpCacheIfIndex,cdpCacheDeviceIndex pair. It has the value N\-1 for the N\-th address in the Address TLV
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cdpctaddresstype
            
            	An indication of the type of address contained in the corresponding instance of cdpCtAddress
            	**type**\:  :py:class:`CiscoNetworkProtocol <ydk.models.cisco_ios_xe.CISCO_TC.CiscoNetworkProtocol>`
            
            .. attribute:: cdpctaddress
            
            	The N\-th network\-layer address of the device as reported in the most recent CDP message's Address TLV, where N\-1 is given by the value of cdpCtAddressIndex. For example, if the the corresponding instance of cdpCtAddressType had the value 'ip(1)', then this object would be an IPv4\-address. NOTE \- The 1st address received in the Address TLV is        available using cdpCacheAddress
            	**type**\: str
            
            

            """

            _prefix = 'CISCO-CDP-MIB'
            _revision = '2005-03-21'

            def __init__(self):
                super(CISCOCDPMIB.Cdpctaddresstable.Cdpctaddressentry, self).__init__()

                self.yang_name = "cdpCtAddressEntry"
                self.yang_parent_name = "cdpCtAddressTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cdpcacheifindex','cdpcachedeviceindex','cdpctaddressindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cdpcacheifindex', YLeaf(YType.str, 'cdpCacheIfIndex')),
                    ('cdpcachedeviceindex', YLeaf(YType.str, 'cdpCacheDeviceIndex')),
                    ('cdpctaddressindex', YLeaf(YType.int32, 'cdpCtAddressIndex')),
                    ('cdpctaddresstype', YLeaf(YType.enumeration, 'cdpCtAddressType')),
                    ('cdpctaddress', YLeaf(YType.str, 'cdpCtAddress')),
                ])
                self.cdpcacheifindex = None
                self.cdpcachedeviceindex = None
                self.cdpctaddressindex = None
                self.cdpctaddresstype = None
                self.cdpctaddress = None
                self._segment_path = lambda: "cdpCtAddressEntry" + "[cdpCacheIfIndex='" + str(self.cdpcacheifindex) + "']" + "[cdpCacheDeviceIndex='" + str(self.cdpcachedeviceindex) + "']" + "[cdpCtAddressIndex='" + str(self.cdpctaddressindex) + "']"
                self._absolute_path = lambda: "CISCO-CDP-MIB:CISCO-CDP-MIB/cdpCtAddressTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCDPMIB.Cdpctaddresstable.Cdpctaddressentry, ['cdpcacheifindex', 'cdpcachedeviceindex', 'cdpctaddressindex', 'cdpctaddresstype', 'cdpctaddress'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOCDPMIB()
        return self._top_entity


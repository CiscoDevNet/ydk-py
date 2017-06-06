""" CISCO_CDP_MIB 

The MIB module for management of the Cisco Discovery
Protocol in Cisco devices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoCdpMib(object):
    """
    
    
    .. attribute:: cdpcachetable
    
    	The (conceptual) table containing the cached information obtained via receiving CDP messages
    	**type**\:   :py:class:`Cdpcachetable <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpcachetable>`
    
    .. attribute:: cdpctaddresstable
    
    	The (conceptual) table containing the list of  network\-layer addresses of a neighbor interface, as reported in the Address TLV of the most recently received CDP message. The first address included in the Address TLV is saved in cdpCacheAddress.  This table contains the remainder of the addresses in the Address TLV
    	**type**\:   :py:class:`Cdpctaddresstable <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpctaddresstable>`
    
    .. attribute:: cdpglobal
    
    	
    	**type**\:   :py:class:`Cdpglobal <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpglobal>`
    
    .. attribute:: cdpinterfaceexttable
    
    	This table contains the additional CDP configuration on the device's interfaces
    	**type**\:   :py:class:`Cdpinterfaceexttable <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpinterfaceexttable>`
    
    .. attribute:: cdpinterfacetable
    
    	The (conceptual) table containing the status of CDP on the device's interfaces
    	**type**\:   :py:class:`Cdpinterfacetable <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpinterfacetable>`
    
    

    """

    _prefix = 'CISCO-CDP-MIB'
    _revision = '2005-03-21'

    def __init__(self):
        self.cdpcachetable = CiscoCdpMib.Cdpcachetable()
        self.cdpcachetable.parent = self
        self.cdpctaddresstable = CiscoCdpMib.Cdpctaddresstable()
        self.cdpctaddresstable.parent = self
        self.cdpglobal = CiscoCdpMib.Cdpglobal()
        self.cdpglobal.parent = self
        self.cdpinterfaceexttable = CiscoCdpMib.Cdpinterfaceexttable()
        self.cdpinterfaceexttable.parent = self
        self.cdpinterfacetable = CiscoCdpMib.Cdpinterfacetable()
        self.cdpinterfacetable.parent = self


    class Cdpglobal(object):
        """
        
        
        .. attribute:: cdpglobaldeviceid
        
        	The device ID advertised by this device. The format of this device id is characterized by the value of  cdpGlobalDeviceIdFormat object
        	**type**\:  str
        
        .. attribute:: cdpglobaldeviceidformat
        
        	An indication of the format of Device\-Id contained in the corresponding instance of cdpGlobalDeviceId. User can only specify the formats that the device is capable of as denoted in cdpGlobalDeviceIdFormatCpb object.  serialNumber(1) indicates that the value of cdpGlobalDeviceId  object is in the form of an ASCII string contain the device serial number.   macAddress(2) indicates that the value of cdpGlobalDeviceId  object is in the form of Layer 2 MAC address.  other(3) indicates that the value of cdpGlobalDeviceId object is in the form of a platform specific ASCII string contain info that identifies the device. For example\: ASCII string contains serialNumber appended/prepened with system name
        	**type**\:   :py:class:`CdpglobaldeviceidformatEnum <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpglobal.CdpglobaldeviceidformatEnum>`
        
        .. attribute:: cdpglobaldeviceidformatcpb
        
        	Indicate the Device\-Id format capability of the device.  serialNumber(0) indicates that the device supports using serial number as the format for its DeviceId.  macAddress(1) indicates that the device supports using layer 2 MAC address as the format for its DeviceId.  other(2) indicates that the device supports using its platform specific format as the format for its DeviceId
        	**type**\:   :py:class:`Cdpglobaldeviceidformatcpb <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpglobal.Cdpglobaldeviceidformatcpb>`
        
        .. attribute:: cdpglobalholdtime
        
        	The time for the receiving device holds CDP message. The default value is 180 seconds
        	**type**\:  int
        
        	**range:** 10..255
        
        	**units**\: seconds
        
        .. attribute:: cdpgloballastchange
        
        	Indicates the time when the cache table was last changed. It is the most recent time at which any row was last created, modified or deleted
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cdpglobalmessageinterval
        
        	The interval at which CDP messages are to be generated. The default value is 60 seconds
        	**type**\:  int
        
        	**range:** 5..254
        
        	**units**\: seconds
        
        .. attribute:: cdpglobalrun
        
        	An indication of whether the Cisco Discovery Protocol is currently running.  Entries in cdpCacheTable are deleted when CDP is disabled
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-CDP-MIB'
        _revision = '2005-03-21'

        def __init__(self):
            self.parent = None
            self.cdpglobaldeviceid = None
            self.cdpglobaldeviceidformat = None
            self.cdpglobaldeviceidformatcpb = CiscoCdpMib.Cdpglobal.Cdpglobaldeviceidformatcpb()
            self.cdpglobalholdtime = None
            self.cdpgloballastchange = None
            self.cdpglobalmessageinterval = None
            self.cdpglobalrun = None

        class CdpglobaldeviceidformatEnum(Enum):
            """
            CdpglobaldeviceidformatEnum

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

            serialNumber = 1

            macAddress = 2

            other = 3


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_CDP_MIB as meta
                return meta._meta_table['CiscoCdpMib.Cdpglobal.CdpglobaldeviceidformatEnum']


        class Cdpglobaldeviceidformatcpb(FixedBitsDict):
            """
            Cdpglobaldeviceidformatcpb

            Indicate the Device\-Id format capability of the device.
            
            serialNumber(0) indicates that the device supports using
            serial number as the format for its DeviceId.
            
            macAddress(1) indicates that the device supports using
            layer 2 MAC address as the format for its DeviceId.
            
            other(2) indicates that the device supports using its
            platform specific format as the format for its DeviceId.
            Keys are:- serialNumber , macAddress , other

            """

            def __init__(self):
                self._dictionary = { 
                    'serialNumber':False,
                    'macAddress':False,
                    'other':False,
                }
                self._pos_map = { 
                    'serialNumber':0,
                    'macAddress':1,
                    'other':2,
                }

        @property
        def _common_path(self):

            return '/CISCO-CDP-MIB:CISCO-CDP-MIB/CISCO-CDP-MIB:cdpGlobal'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cdpglobaldeviceid is not None:
                return True

            if self.cdpglobaldeviceidformat is not None:
                return True

            if self.cdpglobaldeviceidformatcpb is not None:
                if self.cdpglobaldeviceidformatcpb._has_data():
                    return True

            if self.cdpglobalholdtime is not None:
                return True

            if self.cdpgloballastchange is not None:
                return True

            if self.cdpglobalmessageinterval is not None:
                return True

            if self.cdpglobalrun is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_CDP_MIB as meta
            return meta._meta_table['CiscoCdpMib.Cdpglobal']['meta_info']


    class Cdpinterfacetable(object):
        """
        The (conceptual) table containing the status of CDP on
        the device's interfaces.
        
        .. attribute:: cdpinterfaceentry
        
        	An entry (conceptual row) in the cdpInterfaceTable, containing the status of CDP on an interface
        	**type**\: list of    :py:class:`Cdpinterfaceentry <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpinterfacetable.Cdpinterfaceentry>`
        
        

        """

        _prefix = 'CISCO-CDP-MIB'
        _revision = '2005-03-21'

        def __init__(self):
            self.parent = None
            self.cdpinterfaceentry = YList()
            self.cdpinterfaceentry.parent = self
            self.cdpinterfaceentry.name = 'cdpinterfaceentry'


        class Cdpinterfaceentry(object):
            """
            An entry (conceptual row) in the cdpInterfaceTable,
            containing the status of CDP on an interface.
            
            .. attribute:: cdpinterfaceifindex  <key>
            
            	The ifIndex value of the local interface.  For 802.3 Repeaters on which the repeater ports do not have ifIndex values assigned, this value is a unique value for the port, and greater than any ifIndex value supported by the repeater; in this case, the specific port is indicated by corresponding values of cdpInterfaceGroup and cdpInterfacePort, where these values correspond to the group number and port number values of RFC 1516
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cdpinterfaceenable
            
            	An indication of whether the Cisco Discovery Protocol is currently running on this interface.  This variable has no effect when CDP is disabled (cdpGlobalRun = FALSE)
            	**type**\:  bool
            
            .. attribute:: cdpinterfacegroup
            
            	This object is only relevant to interfaces which are repeater ports on 802.3 repeaters.  In this situation, it indicates the RFC1516 group number of the repeater port which corresponds to this interface
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cdpinterfacemessageinterval
            
            	The interval at which CDP messages are to be generated on this interface.  The default value is 60 seconds
            	**type**\:  int
            
            	**range:** 0..254
            
            	**units**\: seconds
            
            	**status**\: obsolete
            
            .. attribute:: cdpinterfacename
            
            	The name of the local interface as advertised by CDP in the Port\-ID TLV
            	**type**\:  str
            
            .. attribute:: cdpinterfaceport
            
            	This object is only relevant to interfaces which are repeater ports on 802.3 repeaters.  In this situation, it indicates the RFC1516 port number of the repeater port which corresponds to this interface
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'CISCO-CDP-MIB'
            _revision = '2005-03-21'

            def __init__(self):
                self.parent = None
                self.cdpinterfaceifindex = None
                self.cdpinterfaceenable = None
                self.cdpinterfacegroup = None
                self.cdpinterfacemessageinterval = None
                self.cdpinterfacename = None
                self.cdpinterfaceport = None

            @property
            def _common_path(self):
                if self.cdpinterfaceifindex is None:
                    raise YPYModelError('Key property cdpinterfaceifindex is None')

                return '/CISCO-CDP-MIB:CISCO-CDP-MIB/CISCO-CDP-MIB:cdpInterfaceTable/CISCO-CDP-MIB:cdpInterfaceEntry[CISCO-CDP-MIB:cdpInterfaceIfIndex = ' + str(self.cdpinterfaceifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cdpinterfaceifindex is not None:
                    return True

                if self.cdpinterfaceenable is not None:
                    return True

                if self.cdpinterfacegroup is not None:
                    return True

                if self.cdpinterfacemessageinterval is not None:
                    return True

                if self.cdpinterfacename is not None:
                    return True

                if self.cdpinterfaceport is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_CDP_MIB as meta
                return meta._meta_table['CiscoCdpMib.Cdpinterfacetable.Cdpinterfaceentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CDP-MIB:CISCO-CDP-MIB/CISCO-CDP-MIB:cdpInterfaceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cdpinterfaceentry is not None:
                for child_ref in self.cdpinterfaceentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_CDP_MIB as meta
            return meta._meta_table['CiscoCdpMib.Cdpinterfacetable']['meta_info']


    class Cdpinterfaceexttable(object):
        """
        This table contains the additional CDP configuration on
        the device's interfaces.
        
        .. attribute:: cdpinterfaceextentry
        
        	An entry in the cdpInterfaceExtTable contains the values configured for Extented Trust TLV and COS (Class of Service) for Untrusted Ports TLV on an interface which supports the sending of these TLVs
        	**type**\: list of    :py:class:`Cdpinterfaceextentry <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpinterfaceexttable.Cdpinterfaceextentry>`
        
        

        """

        _prefix = 'CISCO-CDP-MIB'
        _revision = '2005-03-21'

        def __init__(self):
            self.parent = None
            self.cdpinterfaceextentry = YList()
            self.cdpinterfaceextentry.parent = self
            self.cdpinterfaceextentry.name = 'cdpinterfaceextentry'


        class Cdpinterfaceextentry(object):
            """
            An entry in the cdpInterfaceExtTable contains the values
            configured for Extented Trust TLV and COS (Class of Service)
            for Untrusted Ports TLV on an interface which supports the
            sending of these TLVs.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cdpinterfacecosforuntrustedport
            
            	Indicates the value to be sent by COS for Untrusted Ports TLV
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: cdpinterfaceextendedtrust
            
            	Indicates the value to be sent by Extended Trust TLV.  If trusted(1) is configured, the value of Extended Trust TLV is one byte in length with its least significant bit equal to 1 to indicate extended trust. All other bits are 0.  If noTrust(2) is configured, the value of Extended Trust TLV is one byte in length with its least significant bit equal to 0 to indicate no extended trust. All other bits are 0
            	**type**\:   :py:class:`CdpinterfaceextendedtrustEnum <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpinterfaceexttable.Cdpinterfaceextentry.CdpinterfaceextendedtrustEnum>`
            
            

            """

            _prefix = 'CISCO-CDP-MIB'
            _revision = '2005-03-21'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cdpinterfacecosforuntrustedport = None
                self.cdpinterfaceextendedtrust = None

            class CdpinterfaceextendedtrustEnum(Enum):
                """
                CdpinterfaceextendedtrustEnum

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

                trusted = 1

                noTrust = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_CDP_MIB as meta
                    return meta._meta_table['CiscoCdpMib.Cdpinterfaceexttable.Cdpinterfaceextentry.CdpinterfaceextendedtrustEnum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYModelError('Key property ifindex is None')

                return '/CISCO-CDP-MIB:CISCO-CDP-MIB/CISCO-CDP-MIB:cdpInterfaceExtTable/CISCO-CDP-MIB:cdpInterfaceExtEntry[CISCO-CDP-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ifindex is not None:
                    return True

                if self.cdpinterfacecosforuntrustedport is not None:
                    return True

                if self.cdpinterfaceextendedtrust is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_CDP_MIB as meta
                return meta._meta_table['CiscoCdpMib.Cdpinterfaceexttable.Cdpinterfaceextentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CDP-MIB:CISCO-CDP-MIB/CISCO-CDP-MIB:cdpInterfaceExtTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cdpinterfaceextentry is not None:
                for child_ref in self.cdpinterfaceextentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_CDP_MIB as meta
            return meta._meta_table['CiscoCdpMib.Cdpinterfaceexttable']['meta_info']


    class Cdpcachetable(object):
        """
        The (conceptual) table containing the cached
        information obtained via receiving CDP messages.
        
        .. attribute:: cdpcacheentry
        
        	An entry (conceptual row) in the cdpCacheTable, containing the information received via CDP on one interface from one device.  Entries appear when a CDP advertisement is received from a neighbor device.  Entries disappear when CDP is disabled on the interface, or globally
        	**type**\: list of    :py:class:`Cdpcacheentry <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpcachetable.Cdpcacheentry>`
        
        

        """

        _prefix = 'CISCO-CDP-MIB'
        _revision = '2005-03-21'

        def __init__(self):
            self.parent = None
            self.cdpcacheentry = YList()
            self.cdpcacheentry.parent = self
            self.cdpcacheentry.name = 'cdpcacheentry'


        class Cdpcacheentry(object):
            """
            An entry (conceptual row) in the cdpCacheTable,
            containing the information received via CDP on one
            interface from one device.  Entries appear when
            a CDP advertisement is received from a neighbor
            device.  Entries disappear when CDP is disabled
            on the interface, or globally.
            
            .. attribute:: cdpcacheifindex  <key>
            
            	Normally, the ifIndex value of the local interface. For 802.3 Repeaters for which the repeater ports do not have ifIndex values assigned, this value is a unique value for the port, and greater than any ifIndex value supported by the repeater; the specific port number in this case, is given by the corresponding value of cdpInterfacePort
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cdpcachedeviceindex  <key>
            
            	A unique value for each device from which CDP messages are being received
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cdpcacheaddress
            
            	The (first) network\-layer address of the device as reported in the Address TLV of the most recently received CDP message.  For example, if the corresponding instance of cacheAddressType had the value 'ip(1)', then this object  would be an IPv4\-address.  If the neighbor device is  SNMP\-manageable, it is supposed to generate its CDP messages such that this address is one at which it will receive SNMP messages. Use cdpCtAddressTable to extract the remaining addresses from the Address TLV received most recently
            	**type**\:  str
            
            .. attribute:: cdpcacheaddresstype
            
            	An indication of the type of address contained in the corresponding instance of cdpCacheAddress
            	**type**\:   :py:class:`CisconetworkprotocolEnum <ydk.models.cisco_ios_xe.CISCO_TC.CisconetworkprotocolEnum>`
            
            .. attribute:: cdpcacheapplianceid
            
            	The remote device's Appliance ID, as reported in the  most recent CDP message. This object is not instantiated if no Appliance VLAN\-ID field (TLV) was reported in the most recently received CDP message
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cdpcachecapabilities
            
            	The Device's Functional Capabilities as reported in the most recent CDP message.  For latest set of specific values, see the latest version of the CDP specification. The zero\-length string indicates no Capabilities field (TLV) was reported in the most recent CDP message
            	**type**\:  str
            
            	**length:** 0..4
            
            .. attribute:: cdpcachedeviceid
            
            	The Device\-ID string as reported in the most recent CDP message.  The zero\-length string indicates no Device\-ID field (TLV) was reported in the most recent CDP message
            	**type**\:  str
            
            .. attribute:: cdpcachedeviceport
            
            	The Port\-ID string as reported in the most recent CDP message.  This will typically be the value of the ifName object (e.g., 'Ethernet0').  The zero\-length string indicates no Port\-ID field (TLV) was reported in the most recent CDP message
            	**type**\:  str
            
            .. attribute:: cdpcacheduplex
            
            	The remote device's interface's duplex mode, as reported in the  most recent CDP message.  The value unknown(1) indicates no duplex mode field (TLV) was reported in the most recent CDP message
            	**type**\:   :py:class:`CdpcacheduplexEnum <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpcachetable.Cdpcacheentry.CdpcacheduplexEnum>`
            
            .. attribute:: cdpcachelastchange
            
            	Indicates the time when this cache entry was last changed. This object is initialised to the current time when the entry gets created and updated to the current time whenever the value of any (other) object instance in the corresponding row is modified
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cdpcachemtu
            
            	Indicates the size of the largest datagram that can be sent/received by remote device, as reported in the most recent CDP message. This object is not instantiated if no MTU field (TLV) was reported in the most recently received CDP message
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cdpcachenativevlan
            
            	The remote device's interface's native VLAN, as reported in the  most recent CDP message.  The value 0 indicates no native VLAN field (TLV) was reported in the most recent CDP message
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: cdpcachephyslocation
            
            	Indicates the physical location, as reported by the most recent CDP message, of a connector which is on, or physically connected to, the remote device's interface over which the CDP packet is sent. This object is not instantiated if no Physical Location field (TLV) was reported by the most recently received CDP message
            	**type**\:  str
            
            .. attribute:: cdpcacheplatform
            
            	The Device's Hardware Platform as reported in the most recent CDP message.  The zero\-length string indicates that no Platform field (TLV) was reported in the most recent CDP message
            	**type**\:  str
            
            .. attribute:: cdpcachepowerconsumption
            
            	The amount of power consumed by remote device, as reported in the most recent CDP message. This object is not instantiated if no Power Consumption field (TLV) was reported in the most recently received CDP message
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliwatts
            
            .. attribute:: cdpcacheprimarymgmtaddr
            
            	This object indicates the (first) network layer address at which the device will accept SNMP messages as reported in the first address in the  Management\-Address TLV of the most recently received CDP message.  If the corresponding instance of  cdpCachePrimaryMgmtAddrType has the value 'ip(1)', then this object would be an IP\-address. If the  remote device is not currently manageable via any  network protocol, then it reports the special value  of the IPv4 address 0.0.0.0, and that address is  recorded in this object.  If the most recently received CDP message did not contain the Management\-Address TLV, then this object is not instanstiated
            	**type**\:  str
            
            .. attribute:: cdpcacheprimarymgmtaddrtype
            
            	An indication of the type of address contained in the corresponding instance of cdpCachePrimaryMgmtAddress
            	**type**\:   :py:class:`CisconetworkprotocolEnum <ydk.models.cisco_ios_xe.CISCO_TC.CisconetworkprotocolEnum>`
            
            .. attribute:: cdpcachesecondarymgmtaddr
            
            	This object indicates the alternate network layer address at which the device will accept SNMP messages as reported in the second address in the  Management\-Address TLV of the most recently received CDP message.  If the corresponding instance of cdpCacheSecondaryMgmtAddrType has the value 'ip(1)', then this object would be an IP\-address. If the  remote device reports the special value of the  IPv4 address 0.0.0.0, that address is recorded in  this object.  If the most recently received CDP message did not contain the Management\-Address TLV, or if that TLV contained only one address, then this object is not instanstiated
            	**type**\:  str
            
            .. attribute:: cdpcachesecondarymgmtaddrtype
            
            	An indication of the type of address contained in the corresponding instance of cdpCacheSecondaryMgmtAddress
            	**type**\:   :py:class:`CisconetworkprotocolEnum <ydk.models.cisco_ios_xe.CISCO_TC.CisconetworkprotocolEnum>`
            
            .. attribute:: cdpcachesysname
            
            	Indicates the value of the remote device's sysName MIB object. By convention, it is the device's fully qualified domain name. This object is not instantiated if no sysName field (TLV) was reported in the most recently received CDP message
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cdpcachesysobjectid
            
            	Indicates the value of the remote device's sysObjectID MIB object. This object is not instantiated if no sysObjectID field (TLV) was reported in the most recently received CDP message
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: cdpcacheversion
            
            	The Version string as reported in the most recent CDP message.  The zero\-length string indicates no Version field (TLV) was reported in the most recent CDP message
            	**type**\:  str
            
            .. attribute:: cdpcachevlanid
            
            	The remote device's VoIP VLAN ID, as reported in the  most recent CDP message. This object is not instantiated if no Appliance VLAN\-ID field (TLV) was reported in the most recently received CDP message
            	**type**\:  int
            
            	**range:** 0..4095
            
            .. attribute:: cdpcachevtpmgmtdomain
            
            	The VTP Management Domain for the remote device's interface,  as reported in the most recently received CDP message. This object is not instantiated if no VTP Management Domain field (TLV) was reported in the most recently received CDP message
            	**type**\:  str
            
            	**length:** 0..32
            
            

            """

            _prefix = 'CISCO-CDP-MIB'
            _revision = '2005-03-21'

            def __init__(self):
                self.parent = None
                self.cdpcacheifindex = None
                self.cdpcachedeviceindex = None
                self.cdpcacheaddress = None
                self.cdpcacheaddresstype = None
                self.cdpcacheapplianceid = None
                self.cdpcachecapabilities = None
                self.cdpcachedeviceid = None
                self.cdpcachedeviceport = None
                self.cdpcacheduplex = None
                self.cdpcachelastchange = None
                self.cdpcachemtu = None
                self.cdpcachenativevlan = None
                self.cdpcachephyslocation = None
                self.cdpcacheplatform = None
                self.cdpcachepowerconsumption = None
                self.cdpcacheprimarymgmtaddr = None
                self.cdpcacheprimarymgmtaddrtype = None
                self.cdpcachesecondarymgmtaddr = None
                self.cdpcachesecondarymgmtaddrtype = None
                self.cdpcachesysname = None
                self.cdpcachesysobjectid = None
                self.cdpcacheversion = None
                self.cdpcachevlanid = None
                self.cdpcachevtpmgmtdomain = None

            class CdpcacheduplexEnum(Enum):
                """
                CdpcacheduplexEnum

                The remote device's interface's duplex mode, as reported in the 

                most recent CDP message.  The value unknown(1) indicates

                no duplex mode field (TLV) was reported in the most

                recent CDP message.

                .. data:: unknown = 1

                .. data:: halfduplex = 2

                .. data:: fullduplex = 3

                """

                unknown = 1

                halfduplex = 2

                fullduplex = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_CDP_MIB as meta
                    return meta._meta_table['CiscoCdpMib.Cdpcachetable.Cdpcacheentry.CdpcacheduplexEnum']


            @property
            def _common_path(self):
                if self.cdpcacheifindex is None:
                    raise YPYModelError('Key property cdpcacheifindex is None')
                if self.cdpcachedeviceindex is None:
                    raise YPYModelError('Key property cdpcachedeviceindex is None')

                return '/CISCO-CDP-MIB:CISCO-CDP-MIB/CISCO-CDP-MIB:cdpCacheTable/CISCO-CDP-MIB:cdpCacheEntry[CISCO-CDP-MIB:cdpCacheIfIndex = ' + str(self.cdpcacheifindex) + '][CISCO-CDP-MIB:cdpCacheDeviceIndex = ' + str(self.cdpcachedeviceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cdpcacheifindex is not None:
                    return True

                if self.cdpcachedeviceindex is not None:
                    return True

                if self.cdpcacheaddress is not None:
                    return True

                if self.cdpcacheaddresstype is not None:
                    return True

                if self.cdpcacheapplianceid is not None:
                    return True

                if self.cdpcachecapabilities is not None:
                    return True

                if self.cdpcachedeviceid is not None:
                    return True

                if self.cdpcachedeviceport is not None:
                    return True

                if self.cdpcacheduplex is not None:
                    return True

                if self.cdpcachelastchange is not None:
                    return True

                if self.cdpcachemtu is not None:
                    return True

                if self.cdpcachenativevlan is not None:
                    return True

                if self.cdpcachephyslocation is not None:
                    return True

                if self.cdpcacheplatform is not None:
                    return True

                if self.cdpcachepowerconsumption is not None:
                    return True

                if self.cdpcacheprimarymgmtaddr is not None:
                    return True

                if self.cdpcacheprimarymgmtaddrtype is not None:
                    return True

                if self.cdpcachesecondarymgmtaddr is not None:
                    return True

                if self.cdpcachesecondarymgmtaddrtype is not None:
                    return True

                if self.cdpcachesysname is not None:
                    return True

                if self.cdpcachesysobjectid is not None:
                    return True

                if self.cdpcacheversion is not None:
                    return True

                if self.cdpcachevlanid is not None:
                    return True

                if self.cdpcachevtpmgmtdomain is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_CDP_MIB as meta
                return meta._meta_table['CiscoCdpMib.Cdpcachetable.Cdpcacheentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CDP-MIB:CISCO-CDP-MIB/CISCO-CDP-MIB:cdpCacheTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cdpcacheentry is not None:
                for child_ref in self.cdpcacheentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_CDP_MIB as meta
            return meta._meta_table['CiscoCdpMib.Cdpcachetable']['meta_info']


    class Cdpctaddresstable(object):
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
        	**type**\: list of    :py:class:`Cdpctaddressentry <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpctaddresstable.Cdpctaddressentry>`
        
        

        """

        _prefix = 'CISCO-CDP-MIB'
        _revision = '2005-03-21'

        def __init__(self):
            self.parent = None
            self.cdpctaddressentry = YList()
            self.cdpctaddressentry.parent = self
            self.cdpctaddressentry.name = 'cdpctaddressentry'


        class Cdpctaddressentry(object):
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
            
            .. attribute:: cdpcacheifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`cdpcacheifindex <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpcachetable.Cdpcacheentry>`
            
            .. attribute:: cdpcachedeviceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`cdpcachedeviceindex <ydk.models.cisco_ios_xe.CISCO_CDP_MIB.CiscoCdpMib.Cdpcachetable.Cdpcacheentry>`
            
            .. attribute:: cdpctaddressindex  <key>
            
            	The index of the address entry for a given  cdpCacheIfIndex,cdpCacheDeviceIndex pair. It has the value N\-1 for the N\-th address in the Address TLV
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cdpctaddress
            
            	The N\-th network\-layer address of the device as reported in the most recent CDP message's Address TLV, where N\-1 is given by the value of cdpCtAddressIndex. For example, if the the corresponding instance of cdpCtAddressType had the value 'ip(1)', then this object would be an IPv4\-address. NOTE \- The 1st address received in the Address TLV is        available using cdpCacheAddress
            	**type**\:  str
            
            .. attribute:: cdpctaddresstype
            
            	An indication of the type of address contained in the corresponding instance of cdpCtAddress
            	**type**\:   :py:class:`CisconetworkprotocolEnum <ydk.models.cisco_ios_xe.CISCO_TC.CisconetworkprotocolEnum>`
            
            

            """

            _prefix = 'CISCO-CDP-MIB'
            _revision = '2005-03-21'

            def __init__(self):
                self.parent = None
                self.cdpcacheifindex = None
                self.cdpcachedeviceindex = None
                self.cdpctaddressindex = None
                self.cdpctaddress = None
                self.cdpctaddresstype = None

            @property
            def _common_path(self):
                if self.cdpcacheifindex is None:
                    raise YPYModelError('Key property cdpcacheifindex is None')
                if self.cdpcachedeviceindex is None:
                    raise YPYModelError('Key property cdpcachedeviceindex is None')
                if self.cdpctaddressindex is None:
                    raise YPYModelError('Key property cdpctaddressindex is None')

                return '/CISCO-CDP-MIB:CISCO-CDP-MIB/CISCO-CDP-MIB:cdpCtAddressTable/CISCO-CDP-MIB:cdpCtAddressEntry[CISCO-CDP-MIB:cdpCacheIfIndex = ' + str(self.cdpcacheifindex) + '][CISCO-CDP-MIB:cdpCacheDeviceIndex = ' + str(self.cdpcachedeviceindex) + '][CISCO-CDP-MIB:cdpCtAddressIndex = ' + str(self.cdpctaddressindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cdpcacheifindex is not None:
                    return True

                if self.cdpcachedeviceindex is not None:
                    return True

                if self.cdpctaddressindex is not None:
                    return True

                if self.cdpctaddress is not None:
                    return True

                if self.cdpctaddresstype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_CDP_MIB as meta
                return meta._meta_table['CiscoCdpMib.Cdpctaddresstable.Cdpctaddressentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CDP-MIB:CISCO-CDP-MIB/CISCO-CDP-MIB:cdpCtAddressTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cdpctaddressentry is not None:
                for child_ref in self.cdpctaddressentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_CDP_MIB as meta
            return meta._meta_table['CiscoCdpMib.Cdpctaddresstable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-CDP-MIB:CISCO-CDP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cdpcachetable is not None and self.cdpcachetable._has_data():
            return True

        if self.cdpctaddresstable is not None and self.cdpctaddresstable._has_data():
            return True

        if self.cdpglobal is not None and self.cdpglobal._has_data():
            return True

        if self.cdpinterfaceexttable is not None and self.cdpinterfaceexttable._has_data():
            return True

        if self.cdpinterfacetable is not None and self.cdpinterfacetable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_CDP_MIB as meta
        return meta._meta_table['CiscoCdpMib']['meta_info']



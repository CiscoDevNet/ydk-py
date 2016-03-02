""" LLDP_MIB 

Management Information Base module for LLDP configuration,
statistics, local system data and remote systems data
components.

Copyright (C) IEEE (2005).  This version of this MIB module
is published as subclause 12.1 of IEEE Std 802.1AB\-2005;
see the standard itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.iana.IANA_ADDRESS_FAMILY_NUMBERS_MIB import AddressFamilyNumbers_Enum

class LldpChassisIdSubtype_Enum(Enum):
    """
    LldpChassisIdSubtype_Enum

    This TC describes the source of a chassis identifier.
    
    The enumeration 'chassisComponent(1)' represents a chassis
    identifier based on the value of entPhysicalAlias object
    (defined in IETF RFC 2737) for a chassis component (i.e.,
    an entPhysicalClass value of 'chassis(3)').
    
    The enumeration 'interfaceAlias(2)' represents a chassis
    identifier based on the value of ifAlias object (defined in
    IETF RFC 2863) for an interface on the containing chassis.
    
    The enumeration 'portComponent(3)' represents a chassis
    identifier based on the value of entPhysicalAlias object
    (defined in IETF RFC 2737) for a port or backplane
    component (i.e., entPhysicalClass value of 'port(10)' or
    'backplane(4)'), within the containing chassis.
    
    The enumeration 'macAddress(4)' represents a chassis
    identifier based on the value of a unicast source address
    (encoded in network byte order and IEEE 802.3 canonical bit
    order), of a port on the containing chassis as defined in
    IEEE Std 802\-2001.
    
    The enumeration 'networkAddress(5)' represents a chassis
    identifier based on a network address, associated with
    a particular chassis.  The encoded address is actually
    composed of two fields.  The first field is a single octet,
    representing the IANA AddressFamilyNumbers value for the
    specific address type, and the second field is the network
    address value.
    
    The enumeration 'interfaceName(6)' represents a chassis
    identifier based on the value of ifName object (defined in
    IETF RFC 2863) for an interface on the containing chassis.
    
    The enumeration 'local(7)' represents a chassis identifier
    based on a locally defined value.

    """

    CHASSISCOMPONENT = 1

    INTERFACEALIAS = 2

    PORTCOMPONENT = 3

    MACADDRESS = 4

    NETWORKADDRESS = 5

    INTERFACENAME = 6

    LOCAL = 7


    @staticmethod
    def _meta_info():
        from ydk.models.lldp._meta import _LLDP_MIB as meta
        return meta._meta_table['LldpChassisIdSubtype_Enum']


class LldpManAddrIfSubtype_Enum(Enum):
    """
    LldpManAddrIfSubtype_Enum

    This TC describes the basis of a particular type of
    interface associated with the management address.
    
    The enumeration 'unknown(1)' represents the case where the
    interface is not known.
    
    The enumeration 'ifIndex(2)' represents interface identifier
    based on the ifIndex MIB object.
    
    The enumeration 'systemPortNumber(3)' represents interface
    identifier based on the system port numbering convention.

    """

    UNKNOWN = 1

    IFINDEX = 2

    SYSTEMPORTNUMBER = 3


    @staticmethod
    def _meta_info():
        from ydk.models.lldp._meta import _LLDP_MIB as meta
        return meta._meta_table['LldpManAddrIfSubtype_Enum']


class LldpPortIdSubtype_Enum(Enum):
    """
    LldpPortIdSubtype_Enum

    This TC describes the source of a particular type of port
    identifier used in the LLDP MIB.
    
    The enumeration 'interfaceAlias(1)' represents a port
    identifier based on the ifAlias MIB object, defined in IETF
    RFC 2863.
    
    The enumeration 'portComponent(2)' represents a port
    identifier based on the value of entPhysicalAlias (defined in
    IETF RFC 2737) for a port component (i.e., entPhysicalClass
    value of 'port(10)'), within the containing chassis.
    
    The enumeration 'macAddress(3)' represents a port identifier
    based on a unicast source address (encoded in network
    byte order and IEEE 802.3 canonical bit order), which has
    been detected by the agent and associated with a particular
    port (IEEE Std 802\-2001).
    
    The enumeration 'networkAddress(4)' represents a port
    identifier based on a network address, detected by the agent
    and associated with a particular port.
    
    The enumeration 'interfaceName(5)' represents a port
    identifier based on the ifName MIB object, defined in IETF
    RFC 2863.
    
    The enumeration 'agentCircuitId(6)' represents a port
    identifier based on the agent\-local identifier of the circuit
    (defined in RFC 3046), detected by the agent and associated
    with a particular port.
    
    The enumeration 'local(7)' represents a port identifier
    based on a value locally assigned.

    """

    INTERFACEALIAS = 1

    PORTCOMPONENT = 2

    MACADDRESS = 3

    NETWORKADDRESS = 4

    INTERFACENAME = 5

    AGENTCIRCUITID = 6

    LOCAL = 7


    @staticmethod
    def _meta_info():
        from ydk.models.lldp._meta import _LLDP_MIB as meta
        return meta._meta_table['LldpPortIdSubtype_Enum']


class LldpSystemCapabilitiesMap_Bits(FixedBitsDict):
    """
    LldpSystemCapabilitiesMap_Bits

    This TC describes the system capabilities.
    
    The bit 'other(0)' indicates that the system has capabilities
    other than those listed below.
    
    The bit 'repeater(1)' indicates that the system has repeater
    capability.
    
    The bit 'bridge(2)' indicates that the system has bridge
    capability.
    
    The bit 'wlanAccessPoint(3)' indicates that the system has 
    WLAN access point capability.
    
    The bit 'router(4)' indicates that the system has router
    capability.
    
    The bit 'telephone(5)' indicates that the system has telephone
    capability.
    
    The bit 'docsisCableDevice(6)' indicates that the system has
    DOCSIS Cable Device capability (IETF RFC 2669 & 2670).
    
    The bit 'stationOnly(7)' indicates that the system has only
    station capability and nothing else.
    Keys are:- bridge , wlanAccessPoint , repeater , stationOnly , telephone , docsisCableDevice , other , router

    """

    def __init__(self):
        self._dictionary = { 
            'bridge':False,
            'wlanAccessPoint':False,
            'repeater':False,
            'stationOnly':False,
            'telephone':False,
            'docsisCableDevice':False,
            'other':False,
            'router':False,
        }
        self._pos_map = { 
            'bridge':2,
            'wlanAccessPoint':3,
            'repeater':1,
            'stationOnly':7,
            'telephone':5,
            'docsisCableDevice':6,
            'other':0,
            'router':4,
        }


class LLDPMIB(object):
    """
    
    
    .. attribute:: lldpconfiguration
    
    	
    	**type**\: :py:class:`LldpConfiguration <ydk.models.lldp.LLDP_MIB.LLDPMIB.LldpConfiguration>`
    
    .. attribute:: lldplocalsystemdata
    
    	
    	**type**\: :py:class:`LldpLocalSystemData <ydk.models.lldp.LLDP_MIB.LLDPMIB.LldpLocalSystemData>`
    
    .. attribute:: lldplocmanaddrtable
    
    	This table contains management address information on the local system known to this agent
    	**type**\: :py:class:`LldpLocManAddrTable <ydk.models.lldp.LLDP_MIB.LLDPMIB.LldpLocManAddrTable>`
    
    .. attribute:: lldplocporttable
    
    	This table contains one or more rows per port information associated with the local system known to this agent
    	**type**\: :py:class:`LldpLocPortTable <ydk.models.lldp.LLDP_MIB.LLDPMIB.LldpLocPortTable>`
    
    .. attribute:: lldpportconfigtable
    
    	The table that controls LLDP frame transmission on individual ports
    	**type**\: :py:class:`LldpPortConfigTable <ydk.models.lldp.LLDP_MIB.LLDPMIB.LldpPortConfigTable>`
    
    .. attribute:: lldpremmanaddrtable
    
    	This table contains one or more rows per management address information on the remote system learned on a particular port contained in the local chassis known to this agent
    	**type**\: :py:class:`LldpRemManAddrTable <ydk.models.lldp.LLDP_MIB.LLDPMIB.LldpRemManAddrTable>`
    
    .. attribute:: lldpremorgdefinfotable
    
    	This table contains one or more rows per physical network connection which advertises the organizationally defined information.  Note that this table contains one or more rows of organizationally defined information that is not recognized by the local agent.  If the local system is capable of recognizing any organizationally defined information, appropriate extension MIBs from the organization should be used for information retrieval
    	**type**\: :py:class:`LldpRemOrgDefInfoTable <ydk.models.lldp.LLDP_MIB.LLDPMIB.LldpRemOrgDefInfoTable>`
    
    .. attribute:: lldpremtable
    
    	This table contains one or more rows per physical network connection known to this agent.  The agent may wish to ensure that only one lldpRemEntry is present for each local port, or it may choose to maintain multiple lldpRemEntries for the same local port.  The following procedure may be used to retrieve remote systems information updates from an LLDP agent\:     1. NMS polls all tables associated with remote systems       and keeps a local copy of the information retrieved.       NMS polls periodically the values of the following       objects\:          a. lldpStatsRemTablesInserts          b. lldpStatsRemTablesDeletes          c. lldpStatsRemTablesDrops          d. lldpStatsRemTablesAgeouts          e. lldpStatsRxPortAgeoutsTotal for all ports.     2. LLDP agent updates remote systems MIB objects, and       sends out notifications to a list of notification       destinations.     3. NMS receives the notifications and compares the new       values of objects listed in step 1.          Periodically, NMS should poll the object       lldpStatsRemTablesLastChangeTime to find out if anything       has changed since the last poll.  if something has       changed, NMS will poll the objects listed in step 1 to       figure out what kind of changes occurred in the tables.        if value of lldpStatsRemTablesInserts has changed,       then NMS will walk all tables by employing TimeFilter       with the last\-polled time value.  This request will       return new objects or objects whose values are updated       since the last poll.        if value of lldpStatsRemTablesAgeouts has changed,       then NMS will walk the lldpStatsRxPortAgeoutsTotal and       compare the new values with previously recorded ones.       For ports whose lldpStatsRxPortAgeoutsTotal value is       greater than the recorded value, NMS will have to       retrieve objects associated with those ports from       table(s) without employing a TimeFilter (which is       performed by specifying 0 for the TimeFilter.)        lldpStatsRemTablesDeletes and lldpStatsRemTablesDrops       objects are provided for informational purposes
    	**type**\: :py:class:`LldpRemTable <ydk.models.lldp.LLDP_MIB.LLDPMIB.LldpRemTable>`
    
    .. attribute:: lldpremunknowntlvtable
    
    	This table contains information about an incoming TLV which is not recognized by the receiving LLDP agent.  The TLV may be from a later version of the basic management set.  This table should only contain TLVs that are found in a single LLDP frame.  Entries in this table, associated with an MAC service access point (MSAP, the access point for MAC services provided to the LCC sublayer, defined in IEEE 100, which is also identified with a particular lldpRemLocalPortNum, lldpRemIndex pair) are overwritten with most recently received unrecognized TLV from the same MSAP, or they will naturally age out when the rxInfoTTL timer (associated with the MSAP) expires
    	**type**\: :py:class:`LldpRemUnknownTLVTable <ydk.models.lldp.LLDP_MIB.LLDPMIB.LldpRemUnknownTLVTable>`
    
    .. attribute:: lldpstatistics
    
    	
    	**type**\: :py:class:`LldpStatistics <ydk.models.lldp.LLDP_MIB.LLDPMIB.LldpStatistics>`
    
    .. attribute:: lldpstatsrxporttable
    
    	A table containing LLDP reception statistics for individual ports.  Entries are not required to exist in this table while the lldpPortConfigEntry object is equal to 'disabled(4)'
    	**type**\: :py:class:`LldpStatsRxPortTable <ydk.models.lldp.LLDP_MIB.LLDPMIB.LldpStatsRxPortTable>`
    
    .. attribute:: lldpstatstxporttable
    
    	A table containing LLDP transmission statistics for individual ports.  Entries are not required to exist in this table while the lldpPortConfigEntry object is equal to 'disabled(4)'
    	**type**\: :py:class:`LldpStatsTxPortTable <ydk.models.lldp.LLDP_MIB.LLDPMIB.LldpStatsTxPortTable>`
    
    

    """

    _prefix = 'lldp-mib'
    _revision = '2005-05-06'

    def __init__(self):
        self.lldpconfiguration = LLDPMIB.LldpConfiguration()
        self.lldpconfiguration.parent = self
        self.lldplocalsystemdata = LLDPMIB.LldpLocalSystemData()
        self.lldplocalsystemdata.parent = self
        self.lldplocmanaddrtable = LLDPMIB.LldpLocManAddrTable()
        self.lldplocmanaddrtable.parent = self
        self.lldplocporttable = LLDPMIB.LldpLocPortTable()
        self.lldplocporttable.parent = self
        self.lldpportconfigtable = LLDPMIB.LldpPortConfigTable()
        self.lldpportconfigtable.parent = self
        self.lldpremmanaddrtable = LLDPMIB.LldpRemManAddrTable()
        self.lldpremmanaddrtable.parent = self
        self.lldpremorgdefinfotable = LLDPMIB.LldpRemOrgDefInfoTable()
        self.lldpremorgdefinfotable.parent = self
        self.lldpremtable = LLDPMIB.LldpRemTable()
        self.lldpremtable.parent = self
        self.lldpremunknowntlvtable = LLDPMIB.LldpRemUnknownTLVTable()
        self.lldpremunknowntlvtable.parent = self
        self.lldpstatistics = LLDPMIB.LldpStatistics()
        self.lldpstatistics.parent = self
        self.lldpstatsrxporttable = LLDPMIB.LldpStatsRxPortTable()
        self.lldpstatsrxporttable.parent = self
        self.lldpstatstxporttable = LLDPMIB.LldpStatsTxPortTable()
        self.lldpstatstxporttable.parent = self


    class LldpConfiguration(object):
        """
        
        
        .. attribute:: lldpmessagetxholdmultiplier
        
        	The time\-to\-live value expressed as a multiple of the lldpMessageTxInterval object.  The actual time\-to\-live value used in LLDP frames, transmitted on behalf of this LLDP agent, can be expressed by the following formula\: TTL = min(65535, (lldpMessageTxInterval \* lldpMessageTxHoldMultiplier)) For example, if the value of lldpMessageTxInterval is '30', and the value of lldpMessageTxHoldMultiplier is '4', then the value '120' is encoded in the TTL field in the LLDP header.  The default value for lldpMessageTxHoldMultiplier object is 4.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
        	**type**\: int
        
        	**range:** 2..10
        
        .. attribute:: lldpmessagetxinterval
        
        	The interval at which LLDP frames are transmitted on behalf of this LLDP agent.  The default value for lldpMessageTxInterval object is 30 seconds.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
        	**type**\: int
        
        	**range:** 5..32768
        
        .. attribute:: lldpnotificationinterval
        
        	This object controls the transmission of LLDP notifications.  the agent must not generate more than one lldpRemTablesChange notification\-event in the indicated period, where a 'notification\-event' is the transmission of a single notification PDU type to a list of notification destinations. If additional changes in lldpRemoteSystemsData object groups occur within the indicated throttling period, then these trap\- events must be suppressed by the agent. An NMS should periodically check the value of lldpStatsRemTableLastChangeTime to detect any missed lldpRemTablesChange notification\-events, e.g. due to throttling or transmission loss.  If notification transmission is enabled for particular ports, the suggested default throttling period is 5 seconds.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
        	**type**\: int
        
        	**range:** 5..3600
        
        .. attribute:: lldpreinitdelay
        
        	The lldpReinitDelay indicates the delay (in units of seconds) from when lldpPortConfigAdminStatus object of a particular port becomes 'disabled' until re\-initialization will be attempted.  The default value for lldpReintDelay object is two seconds.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
        	**type**\: int
        
        	**range:** 1..10
        
        .. attribute:: lldptxdelay
        
        	The lldpTxDelay indicates the delay (in units of seconds) between successive LLDP frame transmissions  initiated by value/status changes in the LLDP local systems MIB.  The recommended value for the lldpTxDelay is set by the following  formula\:     1 <= lldpTxDelay <= (0.25 \* lldpMessageTxInterval)  The default value for lldpTxDelay object is two seconds.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
        	**type**\: int
        
        	**range:** 1..8192
        
        

        """

        _prefix = 'lldp-mib'
        _revision = '2005-05-06'

        def __init__(self):
            self.parent = None
            self.lldpmessagetxholdmultiplier = None
            self.lldpmessagetxinterval = None
            self.lldpnotificationinterval = None
            self.lldpreinitdelay = None
            self.lldptxdelay = None

        @property
        def _common_path(self):

            return '/LLDP-MIB:LLDP-MIB/LLDP-MIB:lldpConfiguration'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.lldpmessagetxholdmultiplier is not None:
                return True

            if self.lldpmessagetxinterval is not None:
                return True

            if self.lldpnotificationinterval is not None:
                return True

            if self.lldpreinitdelay is not None:
                return True

            if self.lldptxdelay is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.lldp._meta import _LLDP_MIB as meta
            return meta._meta_table['LLDPMIB.LldpConfiguration']['meta_info']


    class LldpLocManAddrTable(object):
        """
        This table contains management address information on the
        local system known to this agent.
        
        .. attribute:: lldplocmanaddrentry
        
        	Management address information about a particular chassis component.  There may be multiple management addresses configured on the system identified by a particular lldpLocChassisId.  Each management address should have distinct 'management address type' (lldpLocManAddrSubtype) and 'management address' (lldpLocManAddr.)  Entries may be created and deleted in this table by the agent
        	**type**\: list of :py:class:`LldpLocManAddrEntry <ydk.models.lldp.LLDP_MIB.LLDPMIB.LldpLocManAddrTable.LldpLocManAddrEntry>`
        
        

        """

        _prefix = 'lldp-mib'
        _revision = '2005-05-06'

        def __init__(self):
            self.parent = None
            self.lldplocmanaddrentry = YList()
            self.lldplocmanaddrentry.parent = self
            self.lldplocmanaddrentry.name = 'lldplocmanaddrentry'


        class LldpLocManAddrEntry(object):
            """
            Management address information about a particular chassis
            component.  There may be multiple management addresses
            configured on the system identified by a particular
            lldpLocChassisId.  Each management address should have
            distinct 'management address type' (lldpLocManAddrSubtype) and
            'management address' (lldpLocManAddr.)
            
            Entries may be created and deleted in this table by the
            agent.
            
            .. attribute:: lldplocmanaddr
            
            	The string value used to identify the management address component associated with the local system.  The purpose of this address is to contact the management entity
            	**type**\: str
            
            	**range:** 1..31
            
            .. attribute:: lldplocmanaddrsubtype
            
            	The type of management address identifier encoding used in the associated 'lldpLocManagmentAddr' object
            	**type**\: :py:class:`AddressFamilyNumbers_Enum <ydk.models.iana.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers_Enum>`
            
            .. attribute:: lldpconfigmanaddrportstxenable
            
            	A set of ports that are identified by a PortList, in which each port is represented as a bit.  The corresponding local system management address instance will be transmitted on the member ports of the lldpManAddrPortsTxEnable.    The default value for lldpConfigManAddrPortsTxEnable object is empty binary string, which means no ports are specified for advertising indicated management address instance
            	**type**\: str
            
            	**range:** 0..512
            
            .. attribute:: lldplocmanaddrifid
            
            	The integer value used to identify the interface number regarding the management address component associated with the local system
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: lldplocmanaddrifsubtype
            
            	The enumeration value that identifies the interface numbering method used for defining the interface number, associated with the local system
            	**type**\: :py:class:`LldpManAddrIfSubtype_Enum <ydk.models.lldp.LLDP_MIB.LldpManAddrIfSubtype_Enum>`
            
            .. attribute:: lldplocmanaddrlen
            
            	The total length of the management address subtype and the management address fields in LLDPDUs transmitted by the local LLDP agent.  The management address length field is needed so that the receiving systems that do not implement SNMP will not be required to implement an iana family numbers/address length equivalency table in order to decode the management adress
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: lldplocmanaddroid
            
            	The OID value used to identify the type of hardware component or protocol entity associated with the management address advertised by the local system agent
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'lldp-mib'
            _revision = '2005-05-06'

            def __init__(self):
                self.parent = None
                self.lldplocmanaddr = None
                self.lldplocmanaddrsubtype = None
                self.lldpconfigmanaddrportstxenable = None
                self.lldplocmanaddrifid = None
                self.lldplocmanaddrifsubtype = None
                self.lldplocmanaddrlen = None
                self.lldplocmanaddroid = None

            @property
            def _common_path(self):
                if self.lldplocmanaddr is None:
                    raise YPYDataValidationError('Key property lldplocmanaddr is None')
                if self.lldplocmanaddrsubtype is None:
                    raise YPYDataValidationError('Key property lldplocmanaddrsubtype is None')

                return '/LLDP-MIB:LLDP-MIB/LLDP-MIB:lldpLocManAddrTable/LLDP-MIB:lldpLocManAddrEntry[LLDP-MIB:lldpLocManAddr = ' + str(self.lldplocmanaddr) + '][LLDP-MIB:lldpLocManAddrSubtype = ' + str(self.lldplocmanaddrsubtype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.lldplocmanaddr is not None:
                    return True

                if self.lldplocmanaddrsubtype is not None:
                    return True

                if self.lldpconfigmanaddrportstxenable is not None:
                    return True

                if self.lldplocmanaddrifid is not None:
                    return True

                if self.lldplocmanaddrifsubtype is not None:
                    return True

                if self.lldplocmanaddrlen is not None:
                    return True

                if self.lldplocmanaddroid is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.lldp._meta import _LLDP_MIB as meta
                return meta._meta_table['LLDPMIB.LldpLocManAddrTable.LldpLocManAddrEntry']['meta_info']

        @property
        def _common_path(self):

            return '/LLDP-MIB:LLDP-MIB/LLDP-MIB:lldpLocManAddrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.lldplocmanaddrentry is not None:
                for child_ref in self.lldplocmanaddrentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.lldp._meta import _LLDP_MIB as meta
            return meta._meta_table['LLDPMIB.LldpLocManAddrTable']['meta_info']


    class LldpLocPortTable(object):
        """
        This table contains one or more rows per port information
        associated with the local system known to this agent.
        
        .. attribute:: lldplocportentry
        
        	Information about a particular port component.  Entries may be created and deleted in this table by the agent
        	**type**\: list of :py:class:`LldpLocPortEntry <ydk.models.lldp.LLDP_MIB.LLDPMIB.LldpLocPortTable.LldpLocPortEntry>`
        
        

        """

        _prefix = 'lldp-mib'
        _revision = '2005-05-06'

        def __init__(self):
            self.parent = None
            self.lldplocportentry = YList()
            self.lldplocportentry.parent = self
            self.lldplocportentry.name = 'lldplocportentry'


        class LldpLocPortEntry(object):
            """
            Information about a particular port component.
            
            Entries may be created and deleted in this table by the
            agent.
            
            .. attribute:: lldplocportnum
            
            	The index value used to identify the port component (contained in the local chassis with the LLDP agent) associated with this entry.  The value of this object is used as a port index to the lldpLocPortTable
            	**type**\: int
            
            	**range:** 1..4096
            
            .. attribute:: lldplocportdesc
            
            	The string value used to identify the 802 LAN station's port description associated with the local system.  If the local agent supports IETF RFC 2863, lldpLocPortDesc object should have the same value of ifDescr object
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: lldplocportid
            
            	The string value used to identify the port component associated with a given port in the local system
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: lldplocportidsubtype
            
            	The type of port identifier encoding used in the associated 'lldpLocPortId' object
            	**type**\: :py:class:`LldpPortIdSubtype_Enum <ydk.models.lldp.LLDP_MIB.LldpPortIdSubtype_Enum>`
            
            

            """

            _prefix = 'lldp-mib'
            _revision = '2005-05-06'

            def __init__(self):
                self.parent = None
                self.lldplocportnum = None
                self.lldplocportdesc = None
                self.lldplocportid = None
                self.lldplocportidsubtype = None

            @property
            def _common_path(self):
                if self.lldplocportnum is None:
                    raise YPYDataValidationError('Key property lldplocportnum is None')

                return '/LLDP-MIB:LLDP-MIB/LLDP-MIB:lldpLocPortTable/LLDP-MIB:lldpLocPortEntry[LLDP-MIB:lldpLocPortNum = ' + str(self.lldplocportnum) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.lldplocportnum is not None:
                    return True

                if self.lldplocportdesc is not None:
                    return True

                if self.lldplocportid is not None:
                    return True

                if self.lldplocportidsubtype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.lldp._meta import _LLDP_MIB as meta
                return meta._meta_table['LLDPMIB.LldpLocPortTable.LldpLocPortEntry']['meta_info']

        @property
        def _common_path(self):

            return '/LLDP-MIB:LLDP-MIB/LLDP-MIB:lldpLocPortTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.lldplocportentry is not None:
                for child_ref in self.lldplocportentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.lldp._meta import _LLDP_MIB as meta
            return meta._meta_table['LLDPMIB.LldpLocPortTable']['meta_info']


    class LldpLocalSystemData(object):
        """
        
        
        .. attribute:: lldplocchassisid
        
        	The string value used to identify the chassis component associated with the local system
        	**type**\: str
        
        	**range:** 1..255
        
        .. attribute:: lldplocchassisidsubtype
        
        	The type of encoding used to identify the chassis associated with the local system
        	**type**\: :py:class:`LldpChassisIdSubtype_Enum <ydk.models.lldp.LLDP_MIB.LldpChassisIdSubtype_Enum>`
        
        .. attribute:: lldplocsyscapenabled
        
        	The bitmap value used to identify which system capabilities are enabled on the local system
        	**type**\: :py:class:`LldpSystemCapabilitiesMap_Bits <ydk.models.lldp.LLDP_MIB.LldpSystemCapabilitiesMap_Bits>`
        
        .. attribute:: lldplocsyscapsupported
        
        	The bitmap value used to identify which system capabilities are supported on the local system
        	**type**\: :py:class:`LldpSystemCapabilitiesMap_Bits <ydk.models.lldp.LLDP_MIB.LldpSystemCapabilitiesMap_Bits>`
        
        .. attribute:: lldplocsysdesc
        
        	The string value used to identify the system description of the local system.  If the local agent supports IETF RFC 3418, lldpLocSysDesc object should have the same value of sysDesc object
        	**type**\: str
        
        	**range:** 0..255
        
        .. attribute:: lldplocsysname
        
        	The string value used to identify the system name of the local system.  If the local agent supports IETF RFC 3418, lldpLocSysName object should have the same value of sysName object
        	**type**\: str
        
        	**range:** 0..255
        
        

        """

        _prefix = 'lldp-mib'
        _revision = '2005-05-06'

        def __init__(self):
            self.parent = None
            self.lldplocchassisid = None
            self.lldplocchassisidsubtype = None
            self.lldplocsyscapenabled = LldpSystemCapabilitiesMap_Bits()
            self.lldplocsyscapsupported = LldpSystemCapabilitiesMap_Bits()
            self.lldplocsysdesc = None
            self.lldplocsysname = None

        @property
        def _common_path(self):

            return '/LLDP-MIB:LLDP-MIB/LLDP-MIB:lldpLocalSystemData'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.lldplocchassisid is not None:
                return True

            if self.lldplocchassisidsubtype is not None:
                return True

            if self.lldplocsyscapenabled is not None:
                if self.lldplocsyscapenabled._has_data():
                    return True

            if self.lldplocsyscapsupported is not None:
                if self.lldplocsyscapsupported._has_data():
                    return True

            if self.lldplocsysdesc is not None:
                return True

            if self.lldplocsysname is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.lldp._meta import _LLDP_MIB as meta
            return meta._meta_table['LLDPMIB.LldpLocalSystemData']['meta_info']


    class LldpPortConfigTable(object):
        """
        The table that controls LLDP frame transmission on individual
        ports.
        
        .. attribute:: lldpportconfigentry
        
        	LLDP configuration information for a particular port. This configuration parameter controls the transmission and the reception of LLDP frames on those ports whose rows are created in this table
        	**type**\: list of :py:class:`LldpPortConfigEntry <ydk.models.lldp.LLDP_MIB.LLDPMIB.LldpPortConfigTable.LldpPortConfigEntry>`
        
        

        """

        _prefix = 'lldp-mib'
        _revision = '2005-05-06'

        def __init__(self):
            self.parent = None
            self.lldpportconfigentry = YList()
            self.lldpportconfigentry.parent = self
            self.lldpportconfigentry.name = 'lldpportconfigentry'


        class LldpPortConfigEntry(object):
            """
            LLDP configuration information for a particular port.
            This configuration parameter controls the transmission and
            the reception of LLDP frames on those ports whose rows are
            created in this table.
            
            .. attribute:: lldpportconfigportnum
            
            	The index value used to identify the port component (contained in the local chassis with the LLDP agent) associated with this entry.  The value of this object is used as a port index to the lldpPortConfigTable
            	**type**\: int
            
            	**range:** 1..4096
            
            .. attribute:: lldpportconfigadminstatus
            
            	The administratively desired status of the local LLDP agent.  If the associated lldpPortConfigAdminStatus object has a value of 'txOnly(1)', then LLDP agent will transmit LLDP frames on this port and it will not store any information about the remote systems connected.  If the associated lldpPortConfigAdminStatus object has a value of 'rxOnly(2)', then the LLDP agent will receive, but it will not transmit LLDP frames on this port.  If the associated lldpPortConfigAdminStatus object has a value of 'txAndRx(3)', then the LLDP agent will transmit and receive LLDP frames on this port.  If the associated lldpPortConfigAdminStatus object has a value of 'disabled(4)', then LLDP agent will not transmit or receive LLDP frames on this port.  If there is remote systems information which is received on this port and stored in other tables, before the port's lldpPortConfigAdminStatus becomes disabled, then the information will naturally age out
            	**type**\: :py:class:`LldpPortConfigAdminStatus_Enum <ydk.models.lldp.LLDP_MIB.LLDPMIB.LldpPortConfigTable.LldpPortConfigEntry.LldpPortConfigAdminStatus_Enum>`
            
            .. attribute:: lldpportconfignotificationenable
            
            	The lldpPortConfigNotificationEnable controls, on a per port basis,  whether or not notifications from the agent are enabled. The value true(1) means that notifications are enabled; the value false(2) means that they are not
            	**type**\: bool
            
            .. attribute:: lldpportconfigtlvstxenable
            
            	The lldpPortConfigTLVsTxEnable, defined as a bitmap, includes the basic set of LLDP TLVs whose transmission is allowed on the local LLDP agent by the network management. Each bit in the bitmap corresponds to a TLV type associated with a specific optional TLV.  It should be noted that the organizationally\-specific TLVs are excluded from the lldpTLVsTxEnable bitmap.  LLDP Organization Specific Information Extension MIBs should have similar configuration object to control transmission of their organizationally defined TLVs.  The bit 'portDesc(0)' indicates that LLDP agent should transmit 'Port Description TLV'.  The bit 'sysName(1)' indicates that LLDP agent should transmit 'System Name TLV'.  The bit 'sysDesc(2)' indicates that LLDP agent should transmit 'System Description TLV'.  The bit 'sysCap(3)' indicates that LLDP agent should transmit 'System Capabilities TLV'.  There is no bit reserved for the management address TLV type since transmission of management address TLVs are controlled by another object, lldpConfigManAddrTable.  The default value for lldpPortConfigTLVsTxEnable object is empty set, which means no enumerated values are set.  The value of this object must be restored from non\-volatile storage after a re\-initialization of the management system
            	**type**\: :py:class:`LldpPortConfigTLVsTxEnable_Bits <ydk.models.lldp.LLDP_MIB.LLDPMIB.LldpPortConfigTable.LldpPortConfigEntry.LldpPortConfigTLVsTxEnable_Bits>`
            
            

            """

            _prefix = 'lldp-mib'
            _revision = '2005-05-06'

            def __init__(self):
                self.parent = None
                self.lldpportconfigportnum = None
                self.lldpportconfigadminstatus = None
                self.lldpportconfignotificationenable = None
                self.lldpportconfigtlvstxenable = LLDPMIB.LldpPortConfigTable.LldpPortConfigEntry.LldpPortConfigTLVsTxEnable_Bits()

            class LldpPortConfigAdminStatus_Enum(Enum):
                """
                LldpPortConfigAdminStatus_Enum

                The administratively desired status of the local LLDP agent.
                
                If the associated lldpPortConfigAdminStatus object has a
                value of 'txOnly(1)', then LLDP agent will transmit LLDP
                frames on this port and it will not store any information
                about the remote systems connected.
                
                If the associated lldpPortConfigAdminStatus object has a
                value of 'rxOnly(2)', then the LLDP agent will receive,
                but it will not transmit LLDP frames on this port.
                
                If the associated lldpPortConfigAdminStatus object has a
                value of 'txAndRx(3)', then the LLDP agent will transmit
                and receive LLDP frames on this port.
                
                If the associated lldpPortConfigAdminStatus object has a
                value of 'disabled(4)', then LLDP agent will not transmit or
                receive LLDP frames on this port.  If there is remote systems
                information which is received on this port and stored in
                other tables, before the port's lldpPortConfigAdminStatus
                becomes disabled, then the information will naturally age out.

                """

                TXONLY = 1

                RXONLY = 2

                TXANDRX = 3

                DISABLED = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.lldp._meta import _LLDP_MIB as meta
                    return meta._meta_table['LLDPMIB.LldpPortConfigTable.LldpPortConfigEntry.LldpPortConfigAdminStatus_Enum']


            class LldpPortConfigTLVsTxEnable_Bits(FixedBitsDict):
                """
                LldpPortConfigTLVsTxEnable_Bits

                The lldpPortConfigTLVsTxEnable, defined as a bitmap,
                includes the basic set of LLDP TLVs whose transmission is
                allowed on the local LLDP agent by the network management.
                Each bit in the bitmap corresponds to a TLV type associated
                with a specific optional TLV.
                
                It should be noted that the organizationally\-specific TLVs
                are excluded from the lldpTLVsTxEnable bitmap.
                
                LLDP Organization Specific Information Extension MIBs should
                have similar configuration object to control transmission
                of their organizationally defined TLVs.
                
                The bit 'portDesc(0)' indicates that LLDP agent should
                transmit 'Port Description TLV'.
                
                The bit 'sysName(1)' indicates that LLDP agent should transmit
                'System Name TLV'.
                
                The bit 'sysDesc(2)' indicates that LLDP agent should transmit
                'System Description TLV'.
                
                The bit 'sysCap(3)' indicates that LLDP agent should transmit
                'System Capabilities TLV'.
                
                There is no bit reserved for the management address TLV type
                since transmission of management address TLVs are controlled
                by another object, lldpConfigManAddrTable.
                
                The default value for lldpPortConfigTLVsTxEnable object is
                empty set, which means no enumerated values are set.
                
                The value of this object must be restored from non\-volatile
                storage after a re\-initialization of the management system.
                Keys are:- sysCap , sysName , portDesc , sysDesc

                """

                def __init__(self):
                    self._dictionary = { 
                        'sysCap':False,
                        'sysName':False,
                        'portDesc':False,
                        'sysDesc':False,
                    }
                    self._pos_map = { 
                        'sysCap':3,
                        'sysName':1,
                        'portDesc':0,
                        'sysDesc':2,
                    }

            @property
            def _common_path(self):
                if self.lldpportconfigportnum is None:
                    raise YPYDataValidationError('Key property lldpportconfigportnum is None')

                return '/LLDP-MIB:LLDP-MIB/LLDP-MIB:lldpPortConfigTable/LLDP-MIB:lldpPortConfigEntry[LLDP-MIB:lldpPortConfigPortNum = ' + str(self.lldpportconfigportnum) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.lldpportconfigportnum is not None:
                    return True

                if self.lldpportconfigadminstatus is not None:
                    return True

                if self.lldpportconfignotificationenable is not None:
                    return True

                if self.lldpportconfigtlvstxenable is not None:
                    if self.lldpportconfigtlvstxenable._has_data():
                        return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.lldp._meta import _LLDP_MIB as meta
                return meta._meta_table['LLDPMIB.LldpPortConfigTable.LldpPortConfigEntry']['meta_info']

        @property
        def _common_path(self):

            return '/LLDP-MIB:LLDP-MIB/LLDP-MIB:lldpPortConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.lldpportconfigentry is not None:
                for child_ref in self.lldpportconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.lldp._meta import _LLDP_MIB as meta
            return meta._meta_table['LLDPMIB.LldpPortConfigTable']['meta_info']


    class LldpRemManAddrTable(object):
        """
        This table contains one or more rows per management address
        information on the remote system learned on a particular port
        contained in the local chassis known to this agent.
        
        .. attribute:: lldpremmanaddrentry
        
        	Management address information about a particular chassis component.  There may be multiple management addresses configured on the remote system identified by a particular lldpRemIndex whose information is received on lldpRemLocalPortNum of the local system.  Each management address should have distinct 'management address type' (lldpRemManAddrSubtype) and 'management address' (lldpRemManAddr.)  Entries may be created and deleted in this table by the agent
        	**type**\: list of :py:class:`LldpRemManAddrEntry <ydk.models.lldp.LLDP_MIB.LLDPMIB.LldpRemManAddrTable.LldpRemManAddrEntry>`
        
        

        """

        _prefix = 'lldp-mib'
        _revision = '2005-05-06'

        def __init__(self):
            self.parent = None
            self.lldpremmanaddrentry = YList()
            self.lldpremmanaddrentry.parent = self
            self.lldpremmanaddrentry.name = 'lldpremmanaddrentry'


        class LldpRemManAddrEntry(object):
            """
            Management address information about a particular chassis
            component.  There may be multiple management addresses
            configured on the remote system identified by a particular
            lldpRemIndex whose information is received on
            lldpRemLocalPortNum of the local system.  Each management
            address should have distinct 'management address
            type' (lldpRemManAddrSubtype) and 'management address'
            (lldpRemManAddr.)
            
            Entries may be created and deleted in this table by the
            agent.
            
            .. attribute:: lldpremindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: lldpremlocalportnum
            
            	
            	**type**\: int
            
            	**range:** 1..4096
            
            .. attribute:: lldpremmanaddr
            
            	The string value used to identify the management address component associated with the remote system.  The purpose of this address is to contact the management entity
            	**type**\: str
            
            	**range:** 1..31
            
            .. attribute:: lldpremmanaddrsubtype
            
            	The type of management address identifier encoding used in the associated 'lldpRemManagmentAddr' object
            	**type**\: :py:class:`AddressFamilyNumbers_Enum <ydk.models.iana.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers_Enum>`
            
            .. attribute:: lldpremtimemark
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: lldpremmanaddrifid
            
            	The integer value used to identify the interface number regarding the management address component associated with the remote system
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: lldpremmanaddrifsubtype
            
            	The enumeration value that identifies the interface numbering method used for defining the interface number, associated with the remote system
            	**type**\: :py:class:`LldpManAddrIfSubtype_Enum <ydk.models.lldp.LLDP_MIB.LldpManAddrIfSubtype_Enum>`
            
            .. attribute:: lldpremmanaddroid
            
            	The OID value used to identify the type of hardware component or protocol entity associated with the management address advertised by the remote system agent
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'lldp-mib'
            _revision = '2005-05-06'

            def __init__(self):
                self.parent = None
                self.lldpremindex = None
                self.lldpremlocalportnum = None
                self.lldpremmanaddr = None
                self.lldpremmanaddrsubtype = None
                self.lldpremtimemark = None
                self.lldpremmanaddrifid = None
                self.lldpremmanaddrifsubtype = None
                self.lldpremmanaddroid = None

            @property
            def _common_path(self):
                if self.lldpremindex is None:
                    raise YPYDataValidationError('Key property lldpremindex is None')
                if self.lldpremlocalportnum is None:
                    raise YPYDataValidationError('Key property lldpremlocalportnum is None')
                if self.lldpremmanaddr is None:
                    raise YPYDataValidationError('Key property lldpremmanaddr is None')
                if self.lldpremmanaddrsubtype is None:
                    raise YPYDataValidationError('Key property lldpremmanaddrsubtype is None')
                if self.lldpremtimemark is None:
                    raise YPYDataValidationError('Key property lldpremtimemark is None')

                return '/LLDP-MIB:LLDP-MIB/LLDP-MIB:lldpRemManAddrTable/LLDP-MIB:lldpRemManAddrEntry[LLDP-MIB:lldpRemIndex = ' + str(self.lldpremindex) + '][LLDP-MIB:lldpRemLocalPortNum = ' + str(self.lldpremlocalportnum) + '][LLDP-MIB:lldpRemManAddr = ' + str(self.lldpremmanaddr) + '][LLDP-MIB:lldpRemManAddrSubtype = ' + str(self.lldpremmanaddrsubtype) + '][LLDP-MIB:lldpRemTimeMark = ' + str(self.lldpremtimemark) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.lldpremindex is not None:
                    return True

                if self.lldpremlocalportnum is not None:
                    return True

                if self.lldpremmanaddr is not None:
                    return True

                if self.lldpremmanaddrsubtype is not None:
                    return True

                if self.lldpremtimemark is not None:
                    return True

                if self.lldpremmanaddrifid is not None:
                    return True

                if self.lldpremmanaddrifsubtype is not None:
                    return True

                if self.lldpremmanaddroid is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.lldp._meta import _LLDP_MIB as meta
                return meta._meta_table['LLDPMIB.LldpRemManAddrTable.LldpRemManAddrEntry']['meta_info']

        @property
        def _common_path(self):

            return '/LLDP-MIB:LLDP-MIB/LLDP-MIB:lldpRemManAddrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.lldpremmanaddrentry is not None:
                for child_ref in self.lldpremmanaddrentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.lldp._meta import _LLDP_MIB as meta
            return meta._meta_table['LLDPMIB.LldpRemManAddrTable']['meta_info']


    class LldpRemOrgDefInfoTable(object):
        """
        This table contains one or more rows per physical network
        connection which advertises the organizationally defined
        information.
        
        Note that this table contains one or more rows of
        organizationally defined information that is not recognized
        by the local agent.
        
        If the local system is capable of recognizing any
        organizationally defined information, appropriate extension
        MIBs from the organization should be used for information
        retrieval.
        
        .. attribute:: lldpremorgdefinfoentry
        
        	Information about the unrecognized organizationally defined information advertised by the remote system. The lldpRemTimeMark, lldpRemLocalPortNum, lldpRemIndex, lldpRemOrgDefInfoOUI, lldpRemOrgDefInfoSubtype, and lldpRemOrgDefInfoIndex are indexes to this table.  If there is an lldpRemOrgDefInfoEntry associated with a particular remote system identified by the lldpRemLocalPortNum and lldpRemIndex, there must be an lldpRemEntry associated with the same instance (i.e, using same indexes.)  When the lldpRemEntry for the same index is removed from the lldpRemTable, the associated lldpRemOrgDefInfoEntry should be removed from the lldpRemOrgDefInfoTable.  Entries may be created and deleted in this table by the agent
        	**type**\: list of :py:class:`LldpRemOrgDefInfoEntry <ydk.models.lldp.LLDP_MIB.LLDPMIB.LldpRemOrgDefInfoTable.LldpRemOrgDefInfoEntry>`
        
        

        """

        _prefix = 'lldp-mib'
        _revision = '2005-05-06'

        def __init__(self):
            self.parent = None
            self.lldpremorgdefinfoentry = YList()
            self.lldpremorgdefinfoentry.parent = self
            self.lldpremorgdefinfoentry.name = 'lldpremorgdefinfoentry'


        class LldpRemOrgDefInfoEntry(object):
            """
            Information about the unrecognized organizationally
            defined information advertised by the remote system.
            The lldpRemTimeMark, lldpRemLocalPortNum, lldpRemIndex,
            lldpRemOrgDefInfoOUI, lldpRemOrgDefInfoSubtype, and
            lldpRemOrgDefInfoIndex are indexes to this table.  If there is
            an lldpRemOrgDefInfoEntry associated with a particular remote
            system identified by the lldpRemLocalPortNum and lldpRemIndex,
            there must be an lldpRemEntry associated with the same
            instance (i.e, using same indexes.)  When the lldpRemEntry
            for the same index is removed from the lldpRemTable, the
            associated lldpRemOrgDefInfoEntry should be removed from
            the lldpRemOrgDefInfoTable.
            
            Entries may be created and deleted in this table by the
            agent.
            
            .. attribute:: lldpremindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: lldpremlocalportnum
            
            	
            	**type**\: int
            
            	**range:** 1..4096
            
            .. attribute:: lldpremorgdefinfoindex
            
            	This object represents an arbitrary local integer value used by this agent to identify a particular unrecognized organizationally defined information instance, unique only for the lldpRemOrgDefInfoOUI and lldpRemOrgDefInfoSubtype from the same remote system.  An agent is encouraged to assign monotonically increasing index values to new entries, starting with one, after each reboot.  It is considered unlikely that the lldpRemOrgDefInfoIndex will wrap between reboots
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: lldpremorgdefinfooui
            
            	The Organizationally Unique Identifier (OUI), as defined in IEEE std 802\-2001, is a 24 bit (three octets) globally unique assigned number referenced by various standards, of the information received from the remote system
            	**type**\: str
            
            	**range:** 3
            
            .. attribute:: lldpremorgdefinfosubtype
            
            	The integer value used to identify the subtype of the organizationally defined information received from the remote system.  The subtype value is required to identify different instances of organizationally defined information that could not be retrieved without a unique identifier that indicates the particular type of information contained in the information string
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: lldpremtimemark
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: lldpremorgdefinfo
            
            	The string value used to identify the organizationally defined information of the remote system.  The encoding for this object should be as defined for SnmpAdminString TC
            	**type**\: str
            
            	**range:** 0..507
            
            

            """

            _prefix = 'lldp-mib'
            _revision = '2005-05-06'

            def __init__(self):
                self.parent = None
                self.lldpremindex = None
                self.lldpremlocalportnum = None
                self.lldpremorgdefinfoindex = None
                self.lldpremorgdefinfooui = None
                self.lldpremorgdefinfosubtype = None
                self.lldpremtimemark = None
                self.lldpremorgdefinfo = None

            @property
            def _common_path(self):
                if self.lldpremindex is None:
                    raise YPYDataValidationError('Key property lldpremindex is None')
                if self.lldpremlocalportnum is None:
                    raise YPYDataValidationError('Key property lldpremlocalportnum is None')
                if self.lldpremorgdefinfoindex is None:
                    raise YPYDataValidationError('Key property lldpremorgdefinfoindex is None')
                if self.lldpremorgdefinfooui is None:
                    raise YPYDataValidationError('Key property lldpremorgdefinfooui is None')
                if self.lldpremorgdefinfosubtype is None:
                    raise YPYDataValidationError('Key property lldpremorgdefinfosubtype is None')
                if self.lldpremtimemark is None:
                    raise YPYDataValidationError('Key property lldpremtimemark is None')

                return '/LLDP-MIB:LLDP-MIB/LLDP-MIB:lldpRemOrgDefInfoTable/LLDP-MIB:lldpRemOrgDefInfoEntry[LLDP-MIB:lldpRemIndex = ' + str(self.lldpremindex) + '][LLDP-MIB:lldpRemLocalPortNum = ' + str(self.lldpremlocalportnum) + '][LLDP-MIB:lldpRemOrgDefInfoIndex = ' + str(self.lldpremorgdefinfoindex) + '][LLDP-MIB:lldpRemOrgDefInfoOUI = ' + str(self.lldpremorgdefinfooui) + '][LLDP-MIB:lldpRemOrgDefInfoSubtype = ' + str(self.lldpremorgdefinfosubtype) + '][LLDP-MIB:lldpRemTimeMark = ' + str(self.lldpremtimemark) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.lldpremindex is not None:
                    return True

                if self.lldpremlocalportnum is not None:
                    return True

                if self.lldpremorgdefinfoindex is not None:
                    return True

                if self.lldpremorgdefinfooui is not None:
                    return True

                if self.lldpremorgdefinfosubtype is not None:
                    return True

                if self.lldpremtimemark is not None:
                    return True

                if self.lldpremorgdefinfo is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.lldp._meta import _LLDP_MIB as meta
                return meta._meta_table['LLDPMIB.LldpRemOrgDefInfoTable.LldpRemOrgDefInfoEntry']['meta_info']

        @property
        def _common_path(self):

            return '/LLDP-MIB:LLDP-MIB/LLDP-MIB:lldpRemOrgDefInfoTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.lldpremorgdefinfoentry is not None:
                for child_ref in self.lldpremorgdefinfoentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.lldp._meta import _LLDP_MIB as meta
            return meta._meta_table['LLDPMIB.LldpRemOrgDefInfoTable']['meta_info']


    class LldpRemTable(object):
        """
        This table contains one or more rows per physical network
        connection known to this agent.  The agent may wish to ensure
        that only one lldpRemEntry is present for each local port,
        or it may choose to maintain multiple lldpRemEntries for
        the same local port.
        
        The following procedure may be used to retrieve remote
        systems information updates from an LLDP agent\:
        
           1. NMS polls all tables associated with remote systems
              and keeps a local copy of the information retrieved.
              NMS polls periodically the values of the following
              objects\:
                 a. lldpStatsRemTablesInserts
                 b. lldpStatsRemTablesDeletes
                 c. lldpStatsRemTablesDrops
                 d. lldpStatsRemTablesAgeouts
                 e. lldpStatsRxPortAgeoutsTotal for all ports.
        
           2. LLDP agent updates remote systems MIB objects, and
              sends out notifications to a list of notification
              destinations.
        
           3. NMS receives the notifications and compares the new
              values of objects listed in step 1.  
        
              Periodically, NMS should poll the object
              lldpStatsRemTablesLastChangeTime to find out if anything
              has changed since the last poll.  if something has
              changed, NMS will poll the objects listed in step 1 to
              figure out what kind of changes occurred in the tables.
        
              if value of lldpStatsRemTablesInserts has changed,
              then NMS will walk all tables by employing TimeFilter
              with the last\-polled time value.  This request will
              return new objects or objects whose values are updated
              since the last poll.
        
              if value of lldpStatsRemTablesAgeouts has changed,
              then NMS will walk the lldpStatsRxPortAgeoutsTotal and
              compare the new values with previously recorded ones.
              For ports whose lldpStatsRxPortAgeoutsTotal value is
              greater than the recorded value, NMS will have to
              retrieve objects associated with those ports from
              table(s) without employing a TimeFilter (which is
              performed by specifying 0 for the TimeFilter.)
        
              lldpStatsRemTablesDeletes and lldpStatsRemTablesDrops
              objects are provided for informational purposes.
        
        .. attribute:: lldprementry
        
        	Information about a particular physical network connection. Entries may be created and deleted in this table by the agent, if a physical topology discovery process is active
        	**type**\: list of :py:class:`LldpRemEntry <ydk.models.lldp.LLDP_MIB.LLDPMIB.LldpRemTable.LldpRemEntry>`
        
        

        """

        _prefix = 'lldp-mib'
        _revision = '2005-05-06'

        def __init__(self):
            self.parent = None
            self.lldprementry = YList()
            self.lldprementry.parent = self
            self.lldprementry.name = 'lldprementry'


        class LldpRemEntry(object):
            """
            Information about a particular physical network connection.
            Entries may be created and deleted in this table by the agent,
            if a physical topology discovery process is active.
            
            .. attribute:: lldpremindex
            
            	This object represents an arbitrary local integer value used by this agent to identify a particular connection instance, unique only for the indicated remote system.  An agent is encouraged to assign monotonically increasing index values to new entries, starting with one, after each reboot.  It is considered unlikely that the lldpRemIndex will wrap between reboots
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: lldpremlocalportnum
            
            	The index value used to identify the port component (contained in the local chassis with the LLDP agent) associated with this entry.  The lldpRemLocalPortNum identifies the port on which the remote system information is received.  The value of this object is used as a port index to the lldpRemTable
            	**type**\: int
            
            	**range:** 1..4096
            
            .. attribute:: lldpremtimemark
            
            	A TimeFilter for this entry.  See the TimeFilter textual convention in IETF RFC 2021 and  http\://www.ietf.org/IESG/Implementations/RFC2021\-Implementation.txt to see how TimeFilter works
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: lldpremchassisid
            
            	The string value used to identify the chassis component associated with the remote system
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: lldpremchassisidsubtype
            
            	The type of encoding used to identify the chassis associated with the remote system
            	**type**\: :py:class:`LldpChassisIdSubtype_Enum <ydk.models.lldp.LLDP_MIB.LldpChassisIdSubtype_Enum>`
            
            .. attribute:: lldpremportdesc
            
            	The string value used to identify the description of the given port associated with the remote system
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: lldpremportid
            
            	The string value used to identify the port component associated with the remote system
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: lldpremportidsubtype
            
            	The type of port identifier encoding used in the associated 'lldpRemPortId' object
            	**type**\: :py:class:`LldpPortIdSubtype_Enum <ydk.models.lldp.LLDP_MIB.LldpPortIdSubtype_Enum>`
            
            .. attribute:: lldpremsyscapenabled
            
            	The bitmap value used to identify which system capabilities are enabled on the remote system
            	**type**\: :py:class:`LldpSystemCapabilitiesMap_Bits <ydk.models.lldp.LLDP_MIB.LldpSystemCapabilitiesMap_Bits>`
            
            .. attribute:: lldpremsyscapsupported
            
            	The bitmap value used to identify which system capabilities are supported on the remote system
            	**type**\: :py:class:`LldpSystemCapabilitiesMap_Bits <ydk.models.lldp.LLDP_MIB.LldpSystemCapabilitiesMap_Bits>`
            
            .. attribute:: lldpremsysdesc
            
            	The string value used to identify the system description of the remote system
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: lldpremsysname
            
            	The string value used to identify the system name of the remote system
            	**type**\: str
            
            	**range:** 0..255
            
            

            """

            _prefix = 'lldp-mib'
            _revision = '2005-05-06'

            def __init__(self):
                self.parent = None
                self.lldpremindex = None
                self.lldpremlocalportnum = None
                self.lldpremtimemark = None
                self.lldpremchassisid = None
                self.lldpremchassisidsubtype = None
                self.lldpremportdesc = None
                self.lldpremportid = None
                self.lldpremportidsubtype = None
                self.lldpremsyscapenabled = LldpSystemCapabilitiesMap_Bits()
                self.lldpremsyscapsupported = LldpSystemCapabilitiesMap_Bits()
                self.lldpremsysdesc = None
                self.lldpremsysname = None

            @property
            def _common_path(self):
                if self.lldpremindex is None:
                    raise YPYDataValidationError('Key property lldpremindex is None')
                if self.lldpremlocalportnum is None:
                    raise YPYDataValidationError('Key property lldpremlocalportnum is None')
                if self.lldpremtimemark is None:
                    raise YPYDataValidationError('Key property lldpremtimemark is None')

                return '/LLDP-MIB:LLDP-MIB/LLDP-MIB:lldpRemTable/LLDP-MIB:lldpRemEntry[LLDP-MIB:lldpRemIndex = ' + str(self.lldpremindex) + '][LLDP-MIB:lldpRemLocalPortNum = ' + str(self.lldpremlocalportnum) + '][LLDP-MIB:lldpRemTimeMark = ' + str(self.lldpremtimemark) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.lldpremindex is not None:
                    return True

                if self.lldpremlocalportnum is not None:
                    return True

                if self.lldpremtimemark is not None:
                    return True

                if self.lldpremchassisid is not None:
                    return True

                if self.lldpremchassisidsubtype is not None:
                    return True

                if self.lldpremportdesc is not None:
                    return True

                if self.lldpremportid is not None:
                    return True

                if self.lldpremportidsubtype is not None:
                    return True

                if self.lldpremsyscapenabled is not None:
                    if self.lldpremsyscapenabled._has_data():
                        return True

                if self.lldpremsyscapsupported is not None:
                    if self.lldpremsyscapsupported._has_data():
                        return True

                if self.lldpremsysdesc is not None:
                    return True

                if self.lldpremsysname is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.lldp._meta import _LLDP_MIB as meta
                return meta._meta_table['LLDPMIB.LldpRemTable.LldpRemEntry']['meta_info']

        @property
        def _common_path(self):

            return '/LLDP-MIB:LLDP-MIB/LLDP-MIB:lldpRemTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.lldprementry is not None:
                for child_ref in self.lldprementry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.lldp._meta import _LLDP_MIB as meta
            return meta._meta_table['LLDPMIB.LldpRemTable']['meta_info']


    class LldpRemUnknownTLVTable(object):
        """
        This table contains information about an incoming TLV which
        is not recognized by the receiving LLDP agent.  The TLV may
        be from a later version of the basic management set.
        
        This table should only contain TLVs that are found in
        a single LLDP frame.  Entries in this table, associated
        with an MAC service access point (MSAP, the access point
        for MAC services provided to the LCC sublayer, defined
        in IEEE 100, which is also identified with a particular
        lldpRemLocalPortNum, lldpRemIndex pair) are overwritten with
        most recently received unrecognized TLV from the same MSAP,
        or they will naturally age out when the rxInfoTTL timer
        (associated with the MSAP) expires.
        
        .. attribute:: lldpremunknowntlventry
        
        	Information about an unrecognized TLV received from a physical network connection.  Entries may be created and deleted in this table by the agent, if a physical topology discovery process is active
        	**type**\: list of :py:class:`LldpRemUnknownTLVEntry <ydk.models.lldp.LLDP_MIB.LLDPMIB.LldpRemUnknownTLVTable.LldpRemUnknownTLVEntry>`
        
        

        """

        _prefix = 'lldp-mib'
        _revision = '2005-05-06'

        def __init__(self):
            self.parent = None
            self.lldpremunknowntlventry = YList()
            self.lldpremunknowntlventry.parent = self
            self.lldpremunknowntlventry.name = 'lldpremunknowntlventry'


        class LldpRemUnknownTLVEntry(object):
            """
            Information about an unrecognized TLV received from a
            physical network connection.  Entries may be created and
            deleted in this table by the agent, if a physical topology
            discovery process is active.
            
            .. attribute:: lldpremindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: lldpremlocalportnum
            
            	
            	**type**\: int
            
            	**range:** 1..4096
            
            .. attribute:: lldpremtimemark
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: lldpremunknowntlvtype
            
            	This object represents the value extracted from the type field of the TLV
            	**type**\: int
            
            	**range:** 9..126
            
            .. attribute:: lldpremunknowntlvinfo
            
            	This object represents the value extracted from the value field of the TLV
            	**type**\: str
            
            	**range:** 0..511
            
            

            """

            _prefix = 'lldp-mib'
            _revision = '2005-05-06'

            def __init__(self):
                self.parent = None
                self.lldpremindex = None
                self.lldpremlocalportnum = None
                self.lldpremtimemark = None
                self.lldpremunknowntlvtype = None
                self.lldpremunknowntlvinfo = None

            @property
            def _common_path(self):
                if self.lldpremindex is None:
                    raise YPYDataValidationError('Key property lldpremindex is None')
                if self.lldpremlocalportnum is None:
                    raise YPYDataValidationError('Key property lldpremlocalportnum is None')
                if self.lldpremtimemark is None:
                    raise YPYDataValidationError('Key property lldpremtimemark is None')
                if self.lldpremunknowntlvtype is None:
                    raise YPYDataValidationError('Key property lldpremunknowntlvtype is None')

                return '/LLDP-MIB:LLDP-MIB/LLDP-MIB:lldpRemUnknownTLVTable/LLDP-MIB:lldpRemUnknownTLVEntry[LLDP-MIB:lldpRemIndex = ' + str(self.lldpremindex) + '][LLDP-MIB:lldpRemLocalPortNum = ' + str(self.lldpremlocalportnum) + '][LLDP-MIB:lldpRemTimeMark = ' + str(self.lldpremtimemark) + '][LLDP-MIB:lldpRemUnknownTLVType = ' + str(self.lldpremunknowntlvtype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.lldpremindex is not None:
                    return True

                if self.lldpremlocalportnum is not None:
                    return True

                if self.lldpremtimemark is not None:
                    return True

                if self.lldpremunknowntlvtype is not None:
                    return True

                if self.lldpremunknowntlvinfo is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.lldp._meta import _LLDP_MIB as meta
                return meta._meta_table['LLDPMIB.LldpRemUnknownTLVTable.LldpRemUnknownTLVEntry']['meta_info']

        @property
        def _common_path(self):

            return '/LLDP-MIB:LLDP-MIB/LLDP-MIB:lldpRemUnknownTLVTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.lldpremunknowntlventry is not None:
                for child_ref in self.lldpremunknowntlventry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.lldp._meta import _LLDP_MIB as meta
            return meta._meta_table['LLDPMIB.LldpRemUnknownTLVTable']['meta_info']


    class LldpStatistics(object):
        """
        
        
        .. attribute:: lldpstatsremtablesageouts
        
        	The number of times the complete set of information advertised by a particular MSAP has been deleted from tables contained in lldpRemoteSystemsData and lldpExtensions objects because the information timeliness interval has expired.  This counter should be incremented only once when the complete set of information is completely invalidated (aged out) from all related tables.  Partial aging, similar to deletion case, is not allowed, and thus, should not change the value of this counter
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: lldpstatsremtablesdeletes
        
        	The number of times the complete set of information advertised by a particular MSAP has been deleted from tables contained in lldpRemoteSystemsData and lldpExtensions objects.  This counter should be incremented only once when the complete set of information is completely deleted from all related tables.  Partial deletions, such as deletion of rows associated with a particular MSAP from some tables, but not from all tables are not allowed, thus should not change the value of this counter
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: lldpstatsremtablesdrops
        
        	The number of times the complete set of information advertised by a particular MSAP could not be entered into tables contained in lldpRemoteSystemsData and lldpExtensions objects because of insufficient resources
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: lldpstatsremtablesinserts
        
        	The number of times the complete set of information advertised by a particular MSAP has been inserted into tables contained in lldpRemoteSystemsData and lldpExtensions objects.  The complete set of information received from a particular MSAP should be inserted into related tables.  If partial information cannot be inserted for a reason such as lack of resources, all of the complete set of information should be removed.  This counter should be incremented only once after the complete set of information is successfully recorded in all related tables.  Any failures during inserting information set which result in deletion of previously inserted information should not trigger any changes in lldpStatsRemTablesInserts since the insert is not completed yet or or in lldpStatsRemTablesDeletes, since the deletion would only be a partial deletion. If the failure was the result of lack of resources, the lldpStatsRemTablesDrops counter should be incremented once
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: lldpstatsremtableslastchangetime
        
        	The value of sysUpTime object (defined in IETF RFC 3418) at the time an entry is created, modified, or deleted in the in tables associated with the lldpRemoteSystemsData objects and all LLDP extension objects associated with remote systems.  An NMS can use this object to reduce polling of the lldpRemoteSystemsData objects
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'lldp-mib'
        _revision = '2005-05-06'

        def __init__(self):
            self.parent = None
            self.lldpstatsremtablesageouts = None
            self.lldpstatsremtablesdeletes = None
            self.lldpstatsremtablesdrops = None
            self.lldpstatsremtablesinserts = None
            self.lldpstatsremtableslastchangetime = None

        @property
        def _common_path(self):

            return '/LLDP-MIB:LLDP-MIB/LLDP-MIB:lldpStatistics'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.lldpstatsremtablesageouts is not None:
                return True

            if self.lldpstatsremtablesdeletes is not None:
                return True

            if self.lldpstatsremtablesdrops is not None:
                return True

            if self.lldpstatsremtablesinserts is not None:
                return True

            if self.lldpstatsremtableslastchangetime is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.lldp._meta import _LLDP_MIB as meta
            return meta._meta_table['LLDPMIB.LldpStatistics']['meta_info']


    class LldpStatsRxPortTable(object):
        """
        A table containing LLDP reception statistics for individual
        ports.  Entries are not required to exist in this table while
        the lldpPortConfigEntry object is equal to 'disabled(4)'.
        
        .. attribute:: lldpstatsrxportentry
        
        	LLDP frame reception statistics for a particular port. The port must be contained in the same chassis as the LLDP agent.  All counter values in a particular entry shall be maintained on a continuing basis and shall not be deleted upon expiration of rxInfoTTL timing counters in the LLDP remote systems MIB of the receipt of a shutdown frame from a remote LLDP agent.  All statistical counters associated with a particular port on the local LLDP agent become frozen whenever the adminStatus is disabled for the same port
        	**type**\: list of :py:class:`LldpStatsRxPortEntry <ydk.models.lldp.LLDP_MIB.LLDPMIB.LldpStatsRxPortTable.LldpStatsRxPortEntry>`
        
        

        """

        _prefix = 'lldp-mib'
        _revision = '2005-05-06'

        def __init__(self):
            self.parent = None
            self.lldpstatsrxportentry = YList()
            self.lldpstatsrxportentry.parent = self
            self.lldpstatsrxportentry.name = 'lldpstatsrxportentry'


        class LldpStatsRxPortEntry(object):
            """
            LLDP frame reception statistics for a particular port.
            The port must be contained in the same chassis as the
            LLDP agent.
            
            All counter values in a particular entry shall be
            maintained on a continuing basis and shall not be deleted
            upon expiration of rxInfoTTL timing counters in the LLDP
            remote systems MIB of the receipt of a shutdown frame from
            a remote LLDP agent.
            
            All statistical counters associated with a particular
            port on the local LLDP agent become frozen whenever the
            adminStatus is disabled for the same port.
            
            .. attribute:: lldpstatsrxportnum
            
            	The index value used to identify the port component (contained in the local chassis with the LLDP agent) associated with this entry.  The value of this object is used as a port index to the lldpStatsTable
            	**type**\: int
            
            	**range:** 1..4096
            
            .. attribute:: lldpstatsrxportageoutstotal
            
            	The counter that represents the number of age\-outs that occurred on a given port.  An age\-out is the number of times the complete set of information advertised by a particular MSAP has been deleted from tables contained in lldpRemoteSystemsData and lldpExtensions objects because the information timeliness interval has expired.  This counter is similar to lldpStatsRemTablesAgeouts, except that the counter is on a per port basis.  This enables NMS to poll tables associated with the lldpRemoteSystemsData objects and all LLDP extension objects associated with remote systems on the indicated port only.  This counter should be set to zero during agent initialization and its value should not be saved in non\-volatile storage. When a port's admin status changes from 'disabled' to 'rxOnly', 'txOnly' or 'txAndRx', the counter associated with the same port should reset to 0.  The agent should also flush all remote system information associated with the same port.  This counter should be incremented only once when the complete set of information is invalidated (aged out) from all related tables on a particular port.  Partial aging is not allowed, and thus, should not change the value of this counter
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: lldpstatsrxportframesdiscardedtotal
            
            	The number of LLDP frames received by this LLDP agent on the indicated port, and then discarded for any reason. This counter can provide an indication that LLDP header formating problems may exist with the local LLDP agent in the sending system or that LLDPDU validation problems may exist with the local LLDP agent in the receiving system
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: lldpstatsrxportframeserrors
            
            	The number of invalid LLDP frames received by this LLDP agent on the indicated port, while this LLDP agent is enabled
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: lldpstatsrxportframestotal
            
            	The number of valid LLDP frames received by this LLDP agent on the indicated port, while this LLDP agent is enabled
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: lldpstatsrxporttlvsdiscardedtotal
            
            	The number of LLDP TLVs discarded for any reason by this LLDP agent on the indicated port
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: lldpstatsrxporttlvsunrecognizedtotal
            
            	The number of LLDP TLVs received on the given port that are not recognized by this LLDP agent on the indicated port.  An unrecognized TLV is referred to as the TLV whose type value is in the range of reserved TLV types (000 1001 \- 111 1110) in Table 9.1 of IEEE Std 802.1AB\-2005.  An unrecognized TLV may be a basic management TLV from a later LLDP version
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'lldp-mib'
            _revision = '2005-05-06'

            def __init__(self):
                self.parent = None
                self.lldpstatsrxportnum = None
                self.lldpstatsrxportageoutstotal = None
                self.lldpstatsrxportframesdiscardedtotal = None
                self.lldpstatsrxportframeserrors = None
                self.lldpstatsrxportframestotal = None
                self.lldpstatsrxporttlvsdiscardedtotal = None
                self.lldpstatsrxporttlvsunrecognizedtotal = None

            @property
            def _common_path(self):
                if self.lldpstatsrxportnum is None:
                    raise YPYDataValidationError('Key property lldpstatsrxportnum is None')

                return '/LLDP-MIB:LLDP-MIB/LLDP-MIB:lldpStatsRxPortTable/LLDP-MIB:lldpStatsRxPortEntry[LLDP-MIB:lldpStatsRxPortNum = ' + str(self.lldpstatsrxportnum) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.lldpstatsrxportnum is not None:
                    return True

                if self.lldpstatsrxportageoutstotal is not None:
                    return True

                if self.lldpstatsrxportframesdiscardedtotal is not None:
                    return True

                if self.lldpstatsrxportframeserrors is not None:
                    return True

                if self.lldpstatsrxportframestotal is not None:
                    return True

                if self.lldpstatsrxporttlvsdiscardedtotal is not None:
                    return True

                if self.lldpstatsrxporttlvsunrecognizedtotal is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.lldp._meta import _LLDP_MIB as meta
                return meta._meta_table['LLDPMIB.LldpStatsRxPortTable.LldpStatsRxPortEntry']['meta_info']

        @property
        def _common_path(self):

            return '/LLDP-MIB:LLDP-MIB/LLDP-MIB:lldpStatsRxPortTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.lldpstatsrxportentry is not None:
                for child_ref in self.lldpstatsrxportentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.lldp._meta import _LLDP_MIB as meta
            return meta._meta_table['LLDPMIB.LldpStatsRxPortTable']['meta_info']


    class LldpStatsTxPortTable(object):
        """
        A table containing LLDP transmission statistics for
        individual ports.  Entries are not required to exist in
        this table while the lldpPortConfigEntry object is equal to
        'disabled(4)'.
        
        .. attribute:: lldpstatstxportentry
        
        	LLDP frame transmission statistics for a particular port. The port must be contained in the same chassis as the LLDP agent.  All counter values in a particular entry shall be maintained on a continuing basis and shall not be deleted upon expiration of rxInfoTTL timing counters in the LLDP remote systems MIB of the receipt of a shutdown frame from a remote LLDP agent.  All statistical counters associated with a particular port on the local LLDP agent become frozen whenever the adminStatus is disabled for the same port
        	**type**\: list of :py:class:`LldpStatsTxPortEntry <ydk.models.lldp.LLDP_MIB.LLDPMIB.LldpStatsTxPortTable.LldpStatsTxPortEntry>`
        
        

        """

        _prefix = 'lldp-mib'
        _revision = '2005-05-06'

        def __init__(self):
            self.parent = None
            self.lldpstatstxportentry = YList()
            self.lldpstatstxportentry.parent = self
            self.lldpstatstxportentry.name = 'lldpstatstxportentry'


        class LldpStatsTxPortEntry(object):
            """
            LLDP frame transmission statistics for a particular port.
            The port must be contained in the same chassis as the
            LLDP agent.
            
            All counter values in a particular entry shall be
            maintained on a continuing basis and shall not be deleted
            upon expiration of rxInfoTTL timing counters in the LLDP
            remote systems MIB of the receipt of a shutdown frame from
            a remote LLDP agent.
            
            All statistical counters associated with a particular
            port on the local LLDP agent become frozen whenever the
            adminStatus is disabled for the same port.
            
            .. attribute:: lldpstatstxportnum
            
            	The index value used to identify the port component (contained in the local chassis with the LLDP agent) associated with this entry.  The value of this object is used as a port index to the lldpStatsTable
            	**type**\: int
            
            	**range:** 1..4096
            
            .. attribute:: lldpstatstxportframestotal
            
            	The number of LLDP frames transmitted by this LLDP agent on the indicated port
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'lldp-mib'
            _revision = '2005-05-06'

            def __init__(self):
                self.parent = None
                self.lldpstatstxportnum = None
                self.lldpstatstxportframestotal = None

            @property
            def _common_path(self):
                if self.lldpstatstxportnum is None:
                    raise YPYDataValidationError('Key property lldpstatstxportnum is None')

                return '/LLDP-MIB:LLDP-MIB/LLDP-MIB:lldpStatsTxPortTable/LLDP-MIB:lldpStatsTxPortEntry[LLDP-MIB:lldpStatsTxPortNum = ' + str(self.lldpstatstxportnum) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.lldpstatstxportnum is not None:
                    return True

                if self.lldpstatstxportframestotal is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.lldp._meta import _LLDP_MIB as meta
                return meta._meta_table['LLDPMIB.LldpStatsTxPortTable.LldpStatsTxPortEntry']['meta_info']

        @property
        def _common_path(self):

            return '/LLDP-MIB:LLDP-MIB/LLDP-MIB:lldpStatsTxPortTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.lldpstatstxportentry is not None:
                for child_ref in self.lldpstatstxportentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.lldp._meta import _LLDP_MIB as meta
            return meta._meta_table['LLDPMIB.LldpStatsTxPortTable']['meta_info']

    @property
    def _common_path(self):

        return '/LLDP-MIB:LLDP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.lldpconfiguration is not None and self.lldpconfiguration._has_data():
            return True

        if self.lldpconfiguration is not None and self.lldpconfiguration.is_presence():
            return True

        if self.lldplocalsystemdata is not None and self.lldplocalsystemdata._has_data():
            return True

        if self.lldplocalsystemdata is not None and self.lldplocalsystemdata.is_presence():
            return True

        if self.lldplocmanaddrtable is not None and self.lldplocmanaddrtable._has_data():
            return True

        if self.lldplocmanaddrtable is not None and self.lldplocmanaddrtable.is_presence():
            return True

        if self.lldplocporttable is not None and self.lldplocporttable._has_data():
            return True

        if self.lldplocporttable is not None and self.lldplocporttable.is_presence():
            return True

        if self.lldpportconfigtable is not None and self.lldpportconfigtable._has_data():
            return True

        if self.lldpportconfigtable is not None and self.lldpportconfigtable.is_presence():
            return True

        if self.lldpremmanaddrtable is not None and self.lldpremmanaddrtable._has_data():
            return True

        if self.lldpremmanaddrtable is not None and self.lldpremmanaddrtable.is_presence():
            return True

        if self.lldpremorgdefinfotable is not None and self.lldpremorgdefinfotable._has_data():
            return True

        if self.lldpremorgdefinfotable is not None and self.lldpremorgdefinfotable.is_presence():
            return True

        if self.lldpremtable is not None and self.lldpremtable._has_data():
            return True

        if self.lldpremtable is not None and self.lldpremtable.is_presence():
            return True

        if self.lldpremunknowntlvtable is not None and self.lldpremunknowntlvtable._has_data():
            return True

        if self.lldpremunknowntlvtable is not None and self.lldpremunknowntlvtable.is_presence():
            return True

        if self.lldpstatistics is not None and self.lldpstatistics._has_data():
            return True

        if self.lldpstatistics is not None and self.lldpstatistics.is_presence():
            return True

        if self.lldpstatsrxporttable is not None and self.lldpstatsrxporttable._has_data():
            return True

        if self.lldpstatsrxporttable is not None and self.lldpstatsrxporttable.is_presence():
            return True

        if self.lldpstatstxporttable is not None and self.lldpstatstxporttable._has_data():
            return True

        if self.lldpstatstxporttable is not None and self.lldpstatstxporttable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.lldp._meta import _LLDP_MIB as meta
        return meta._meta_table['LLDPMIB']['meta_info']



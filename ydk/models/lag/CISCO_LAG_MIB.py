""" CISCO_LAG_MIB 

Cisco Link Aggregation module for managing IEEE Std
802.3ad.

This MIB provides Link Aggregation information that are
either excluded by IEEE Std 802.3ad (IEEE8023\-LAG\-MIB)
or specific to Cisco products.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class ClagAggregationProtocol_Enum(Enum):
    """
    ClagAggregationProtocol_Enum

    An enumerated type for all the supported aggregation
    protocols.
    
    lacp(1)     Link Aggregation Control Protocol(LACP),
                IEEE 802.3ad
    pagp(2)     Port Aggregation Protocol

    """

    LACP = 1

    PAGP = 2


    @staticmethod
    def _meta_info():
        from ydk.models.lag._meta import _CISCO_LAG_MIB as meta
        return meta._meta_table['ClagAggregationProtocol_Enum']


class ClagDistributionAddressMode_Enum(Enum):
    """
    ClagDistributionAddressMode_Enum

    An enumerated type for all the supported load
    balancing address modes to distribute traffic
    across multiple links.  The address mode can be 
    source, destination, or both used on this port 
    channel interface to distribute outgoing data frames 
    among its component interfaces. 
    
    source(1)         Source address.
    destination(2)    Destination address.
    both(3)           both, Source and Destination.

    """

    SOURCE = 1

    DESTINATION = 2

    BOTH = 3


    @staticmethod
    def _meta_info():
        from ydk.models.lag._meta import _CISCO_LAG_MIB as meta
        return meta._meta_table['ClagDistributionAddressMode_Enum']


class ClagDistributionMplsProtocol_Enum(Enum):
    """
    ClagDistributionMplsProtocol_Enum

    An enumerated type for all the supported load balancing
    algorithms used on the port channel interface to distribute 
    outgoing MPLS (Multi\-Protocol Label Switching) data 
    frames among its component interfaces, such as 
    MPLS label.
    
    label(1)            MPLS label
    labelIp(2)          MPLS label or IP address

    """

    LABEL = 1

    LABELIP = 2


    @staticmethod
    def _meta_info():
        from ydk.models.lag._meta import _CISCO_LAG_MIB as meta
        return meta._meta_table['ClagDistributionMplsProtocol_Enum']


class ClagDistributionProtocol_Enum(Enum):
    """
    ClagDistributionProtocol_Enum

    An enumerated type for all the supported load balancing
    algorithms used on the port channel interface to distribute 
    outgoing data frames among its component interaces, such 
    as IP address.  
    
    ip(1)               IP address
    mac(2)              MAC address 
    port(3)             port number
    vlanIpPort(4)       vlan number, IP address and
                        port number
    vlanIp(5)           VLAN number and IP address
    ipPort(6)           IP address and port number

    """

    IP = 1

    MAC = 2

    PORT = 3

    VLANIPPORT = 4

    VLANIP = 5

    IPPORT = 6


    @staticmethod
    def _meta_info():
        from ydk.models.lag._meta import _CISCO_LAG_MIB as meta
        return meta._meta_table['ClagDistributionProtocol_Enum']


class ClagPortAdminStatus_Enum(Enum):
    """
    ClagPortAdminStatus_Enum

    An enumerated type for all the LACP administrative states on
    a particular aggregation port.
    
    off(1)          No LACP involved on the aggregation port.
    
    on(2)           The aggregation port always join link
                    aggregation whithout any LACP protocol
                    involved.
    
    active(3)       Active LACP indicates the port's preference
                    to participate in the protocol regardless of
                    Partner's control value.
    
    passive(4)      Passive indicates the port's preference for
                    not transmitting LACP PDU unless its Partner's
                    control value is Active LACP.

    """

    OFF = 1

    ON = 2

    ACTIVE = 3

    PASSIVE = 4


    @staticmethod
    def _meta_info():
        from ydk.models.lag._meta import _CISCO_LAG_MIB as meta
        return meta._meta_table['ClagPortAdminStatus_Enum']



class CISCOLAGMIB(object):
    """
    
    
    .. attribute:: clagaggchanneliftable
    
    	A table providing port channel configuration information for port channel interfaces identified by ifIndex
    	**type**\: :py:class:`ClagAggChannelIfTable <ydk.models.lag.CISCO_LAG_MIB.CISCOLAGMIB.ClagAggChannelIfTable>`
    
    .. attribute:: clagaggprotocoltable
    
    	A table that contains protocol information about every interface which supports link aggregation
    	**type**\: :py:class:`ClagAggProtocolTable <ydk.models.lag.CISCO_LAG_MIB.CISCOLAGMIB.ClagAggProtocolTable>`
    
    .. attribute:: clagglobalconfigobjects
    
    	
    	**type**\: :py:class:`ClagGlobalConfigObjects <ydk.models.lag.CISCO_LAG_MIB.CISCOLAGMIB.ClagGlobalConfigObjects>`
    
    

    """

    _prefix = 'cisco-lag'
    _revision = '2010-10-20'

    def __init__(self):
        self.clagaggchanneliftable = CISCOLAGMIB.ClagAggChannelIfTable()
        self.clagaggchanneliftable.parent = self
        self.clagaggprotocoltable = CISCOLAGMIB.ClagAggProtocolTable()
        self.clagaggprotocoltable.parent = self
        self.clagglobalconfigobjects = CISCOLAGMIB.ClagGlobalConfigObjects()
        self.clagglobalconfigobjects.parent = self


    class ClagAggChannelIfTable(object):
        """
        A table providing port channel
        configuration information for port channel
        interfaces identified by ifIndex.
        
        .. attribute:: clagaggchannelifentry
        
        	An entry containing port channel configuration information for port  channel interfaces
        	**type**\: list of :py:class:`ClagAggChannelIfEntry <ydk.models.lag.CISCO_LAG_MIB.CISCOLAGMIB.ClagAggChannelIfTable.ClagAggChannelIfEntry>`
        
        

        """

        _prefix = 'cisco-lag'
        _revision = '2010-10-20'

        def __init__(self):
            self.parent = None
            self.clagaggchannelifentry = YList()
            self.clagaggchannelifentry.parent = self
            self.clagaggchannelifentry.name = 'clagaggchannelifentry'


        class ClagAggChannelIfEntry(object):
            """
            An entry containing port channel
            configuration information for port 
            channel interfaces.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: clagaggchanneliffastswitchover
            
            	Specifies whether LACP protocol fast switchover mode is enabled on this port channel interface or not
            	**type**\: bool
            
            .. attribute:: clagaggchannelifhashdistadminmethod
            
            	Specifies the hash distribution method that is administratively configured on this port channel interface upon its channel  membership transition event.   none(1)      \:  Hash distribution algorithm on this                  port channel interface is not specifically                  configured and global configuration of                  clagAggHashDistMethodGlobalConfig will                 be applied on this port channel interface. adaptive(2)  \:  Adaptive hash distribution for this port                  channel interface among its channel members. fixed(3)     \:  Fixed hash distribution for this port channel                 interface among its channel members
            	**type**\: :py:class:`ClagAggChannelIfHashDistAdminMethod_Enum <ydk.models.lag.CISCO_LAG_MIB.CISCOLAGMIB.ClagAggChannelIfTable.ClagAggChannelIfEntry.ClagAggChannelIfHashDistAdminMethod_Enum>`
            
            .. attribute:: clagaggchannelifhashdistopermethod
            
            	Specifies the operational hash distribution method for this port channel interface among the port channel members.  other(1)        \: None of the following.  adaptive(2)     \: Adaptive hash distribution for the                    port channel interface among its                    channel members. fixed(3)        \: Fixed hash distribution for the port                   channel among channel members
            	**type**\: :py:class:`ClagAggChannelIfHashDistOperMethod_Enum <ydk.models.lag.CISCO_LAG_MIB.CISCOLAGMIB.ClagAggChannelIfTable.ClagAggChannelIfEntry.ClagAggChannelIfHashDistOperMethod_Enum>`
            
            .. attribute:: clagaggchannelifmaxbundle
            
            	Specifies the maximum number of member ports that can be bundled on this port channel interface for LACP protocol
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: clagaggchannelifminlink
            
            	Specifies the minimum number of bundled member ports that are needed in order for this port channel interface to be operational. A value of zero for this object indicates that no minimum number of bundled member ports are required for this port channel interface to be operational
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-lag'
            _revision = '2010-10-20'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.clagaggchanneliffastswitchover = None
                self.clagaggchannelifhashdistadminmethod = None
                self.clagaggchannelifhashdistopermethod = None
                self.clagaggchannelifmaxbundle = None
                self.clagaggchannelifminlink = None

            class ClagAggChannelIfHashDistAdminMethod_Enum(Enum):
                """
                ClagAggChannelIfHashDistAdminMethod_Enum

                Specifies the hash distribution method that is administratively
                configured on this port channel interface upon its channel 
                membership transition event. 
                
                none(1)      \:  Hash distribution algorithm on this 
                                port channel interface is not specifically 
                                configured and global configuration of 
                                clagAggHashDistMethodGlobalConfig will
                                be applied on this port channel interface.
                adaptive(2)  \:  Adaptive hash distribution for this port 
                                channel interface among its channel members.
                fixed(3)     \:  Fixed hash distribution for this port channel
                                interface among its channel members.

                """

                NONE = 1

                ADAPTIVE = 2

                FIXED = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.lag._meta import _CISCO_LAG_MIB as meta
                    return meta._meta_table['CISCOLAGMIB.ClagAggChannelIfTable.ClagAggChannelIfEntry.ClagAggChannelIfHashDistAdminMethod_Enum']


            class ClagAggChannelIfHashDistOperMethod_Enum(Enum):
                """
                ClagAggChannelIfHashDistOperMethod_Enum

                Specifies the operational hash distribution method
                for this port channel interface among the port channel members.
                
                other(1)        \: None of the following. 
                adaptive(2)     \: Adaptive hash distribution for the 
                                  port channel interface among its 
                                  channel members.
                fixed(3)        \: Fixed hash distribution for the port
                                  channel among channel members.

                """

                OTHER = 1

                ADAPTIVE = 2

                FIXED = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.lag._meta import _CISCO_LAG_MIB as meta
                    return meta._meta_table['CISCOLAGMIB.ClagAggChannelIfTable.ClagAggChannelIfEntry.ClagAggChannelIfHashDistOperMethod_Enum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-LAG-MIB:CISCO-LAG-MIB/CISCO-LAG-MIB:clagAggChannelIfTable/CISCO-LAG-MIB:clagAggChannelIfEntry[CISCO-LAG-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.clagaggchanneliffastswitchover is not None:
                    return True

                if self.clagaggchannelifhashdistadminmethod is not None:
                    return True

                if self.clagaggchannelifhashdistopermethod is not None:
                    return True

                if self.clagaggchannelifmaxbundle is not None:
                    return True

                if self.clagaggchannelifminlink is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.lag._meta import _CISCO_LAG_MIB as meta
                return meta._meta_table['CISCOLAGMIB.ClagAggChannelIfTable.ClagAggChannelIfEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-LAG-MIB:CISCO-LAG-MIB/CISCO-LAG-MIB:clagAggChannelIfTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.clagaggchannelifentry is not None:
                for child_ref in self.clagaggchannelifentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.lag._meta import _CISCO_LAG_MIB as meta
            return meta._meta_table['CISCOLAGMIB.ClagAggChannelIfTable']['meta_info']


    class ClagAggProtocolTable(object):
        """
        A table that contains protocol information about every
        interface which supports link aggregation.
        
        .. attribute:: clagaggprotocolentry
        
        	Entry containing aggregation protocol type for a particular interface.  An entry is created in this table when its associated ifEntry is created and that  interface supports link aggregation.  The entry of this table is deleted when the associated ifEntry is removed
        	**type**\: list of :py:class:`ClagAggProtocolEntry <ydk.models.lag.CISCO_LAG_MIB.CISCOLAGMIB.ClagAggProtocolTable.ClagAggProtocolEntry>`
        
        

        """

        _prefix = 'cisco-lag'
        _revision = '2010-10-20'

        def __init__(self):
            self.parent = None
            self.clagaggprotocolentry = YList()
            self.clagaggprotocolentry.parent = self
            self.clagaggprotocolentry.name = 'clagaggprotocolentry'


        class ClagAggProtocolEntry(object):
            """
            Entry containing aggregation protocol type for a
            particular interface.  An entry is created in this
            table when its associated ifEntry is created and that 
            interface supports link aggregation.  The entry of this
            table is deleted when the associated ifEntry is removed.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: clagaggprotocoltype
            
            	The aggregation protocol type for the interface.  On some platforms, aggregation protocol may be assigned per group.  The group can be a collection of the ports which belong to a module or system.  If the aggregation protocol is assigned to any of the ports in such group then the aggregation protocol will apply to all ports in the same group.  On some platforms, aggregation protocol type  can be assigned per aggregator.  If multiple ports belong to a aggregator, the aggregation protocol assigned to any of the ports in such aggregator will apply to all ports in the same
            	**type**\: :py:class:`ClagAggregationProtocol_Enum <ydk.models.lag.CISCO_LAG_MIB.ClagAggregationProtocol_Enum>`
            
            

            """

            _prefix = 'cisco-lag'
            _revision = '2010-10-20'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.clagaggprotocoltype = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-LAG-MIB:CISCO-LAG-MIB/CISCO-LAG-MIB:clagAggProtocolTable/CISCO-LAG-MIB:clagAggProtocolEntry[CISCO-LAG-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.clagaggprotocoltype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.lag._meta import _CISCO_LAG_MIB as meta
                return meta._meta_table['CISCOLAGMIB.ClagAggProtocolTable.ClagAggProtocolEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-LAG-MIB:CISCO-LAG-MIB/CISCO-LAG-MIB:clagAggProtocolTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.clagaggprotocolentry is not None:
                for child_ref in self.clagaggprotocolentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.lag._meta import _CISCO_LAG_MIB as meta
            return meta._meta_table['CISCOLAGMIB.ClagAggProtocolTable']['meta_info']


    class ClagGlobalConfigObjects(object):
        """
        
        
        .. attribute:: clagaggdistributionaddressmode
        
        	The load balancing address mode for the device
        	**type**\: :py:class:`ClagDistributionAddressMode_Enum <ydk.models.lag.CISCO_LAG_MIB.ClagDistributionAddressMode_Enum>`
        
        .. attribute:: clagaggdistributionmplsprotocol
        
        	This object controls the load balancing algorithms used on this port channel interface to distribute  outgoing MPLS data frames among its component interfaces.  This object is only instantiated on platforms which  support aggregation load balancing for MPLS packets
        	**type**\: :py:class:`ClagDistributionMplsProtocol_Enum <ydk.models.lag.CISCO_LAG_MIB.ClagDistributionMplsProtocol_Enum>`
        
        .. attribute:: clagaggdistributionprotocol
        
        	This object controls the load balancing algorithms used on this port channel interface to distribute outgoing  data frames among its component interfaces
        	**type**\: :py:class:`ClagDistributionProtocol_Enum <ydk.models.lag.CISCO_LAG_MIB.ClagDistributionProtocol_Enum>`
        
        .. attribute:: clagagghashdistmethodglobalconfig
        
        	Specifies the global configuration for hash distribution method applied on a port channel  interface among its channel members.  adaptive(1)  \:  Adaptive hash distribution for the bundle                 among port channel members. fixed(2)     \:  Fixed hash distribution for the bundle                 among port channel members
        	**type**\: :py:class:`ClagAggHashDistMethodGlobalConfig_Enum <ydk.models.lag.CISCO_LAG_MIB.CISCOLAGMIB.ClagGlobalConfigObjects.ClagAggHashDistMethodGlobalConfig_Enum>`
        
        .. attribute:: clagaggmaxaggregators
        
        	This object indicates the maximum number of aggregators supported by the device
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-lag'
        _revision = '2010-10-20'

        def __init__(self):
            self.parent = None
            self.clagaggdistributionaddressmode = None
            self.clagaggdistributionmplsprotocol = None
            self.clagaggdistributionprotocol = None
            self.clagagghashdistmethodglobalconfig = None
            self.clagaggmaxaggregators = None

        class ClagAggHashDistMethodGlobalConfig_Enum(Enum):
            """
            ClagAggHashDistMethodGlobalConfig_Enum

            Specifies the global configuration for hash
            distribution method applied on a port channel 
            interface among its channel members.
            
            adaptive(1)  \:  Adaptive hash distribution for the bundle
                            among port channel members.
            fixed(2)     \:  Fixed hash distribution for the bundle
                            among port channel members.

            """

            ADAPTIVE = 1

            FIXED = 2


            @staticmethod
            def _meta_info():
                from ydk.models.lag._meta import _CISCO_LAG_MIB as meta
                return meta._meta_table['CISCOLAGMIB.ClagGlobalConfigObjects.ClagAggHashDistMethodGlobalConfig_Enum']


        @property
        def _common_path(self):

            return '/CISCO-LAG-MIB:CISCO-LAG-MIB/CISCO-LAG-MIB:clagGlobalConfigObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.clagaggdistributionaddressmode is not None:
                return True

            if self.clagaggdistributionmplsprotocol is not None:
                return True

            if self.clagaggdistributionprotocol is not None:
                return True

            if self.clagagghashdistmethodglobalconfig is not None:
                return True

            if self.clagaggmaxaggregators is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.lag._meta import _CISCO_LAG_MIB as meta
            return meta._meta_table['CISCOLAGMIB.ClagGlobalConfigObjects']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-LAG-MIB:CISCO-LAG-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.clagaggchanneliftable is not None and self.clagaggchanneliftable._has_data():
            return True

        if self.clagaggchanneliftable is not None and self.clagaggchanneliftable.is_presence():
            return True

        if self.clagaggprotocoltable is not None and self.clagaggprotocoltable._has_data():
            return True

        if self.clagaggprotocoltable is not None and self.clagaggprotocoltable.is_presence():
            return True

        if self.clagglobalconfigobjects is not None and self.clagglobalconfigobjects._has_data():
            return True

        if self.clagglobalconfigobjects is not None and self.clagglobalconfigobjects.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.lag._meta import _CISCO_LAG_MIB as meta
        return meta._meta_table['CISCOLAGMIB']['meta_info']



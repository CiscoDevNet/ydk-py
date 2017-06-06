""" P_BRIDGE_MIB 

The Bridge MIB Extension module for managing Priority
and Multicast Filtering, defined by IEEE 802.1D\-1998,
including Restricted Group Registration defined by
IEEE 802.1t\-2001.

Copyright (C) The Internet Society (2006).  This version of
this MIB module is part of RFC 4363; See the RFC itself for
full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class EnabledstatusEnum(Enum):
    """
    EnabledstatusEnum

    A simple status value for the object.

    .. data:: enabled = 1

    .. data:: disabled = 2

    """

    enabled = 1

    disabled = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _P_BRIDGE_MIB as meta
        return meta._meta_table['EnabledstatusEnum']



class PBridgeMib(object):
    """
    
    
    .. attribute:: dot1dextbase
    
    	
    	**type**\:   :py:class:`Dot1Dextbase <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Dextbase>`
    
    .. attribute:: dot1dportoutboundaccessprioritytable
    
    	A table mapping Regenerated User Priority to Outbound Access Priority.  This is a fixed mapping for all port types, with two options for 802.5 Token Ring
    	**type**\:   :py:class:`Dot1Dportoutboundaccessprioritytable <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Dportoutboundaccessprioritytable>`
    
    .. attribute:: dot1dtphcporttable
    
    	A table that contains information about every high\- capacity port that is associated with this transparent bridge
    	**type**\:   :py:class:`Dot1Dtphcporttable <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Dtphcporttable>`
    
    .. attribute:: dot1dtpportoverflowtable
    
    	A table that contains the most\-significant bits of statistics counters for ports that are associated with this transparent bridge that are on high\-capacity interfaces, as defined in the conformance clauses for this table.  This table is provided as a way to read 64\-bit counters for agents that support only SNMPv1.  Note that the reporting of most\-significant and least\-significant counter bits separately runs the risk of missing an overflow of the lower bits in the interval between sampling.  The manager must be aware of this possibility, even within the same varbindlist, when interpreting the results of a request or asynchronous notification
    	**type**\:   :py:class:`Dot1Dtpportoverflowtable <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Dtpportoverflowtable>`
    
    .. attribute:: dot1dtrafficclasstable
    
    	A table mapping evaluated User Priority to Traffic Class, for forwarding by the bridge.  Traffic class is a number in the range (0..(dot1dPortNumTrafficClasses\-1))
    	**type**\:   :py:class:`Dot1Dtrafficclasstable <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Dtrafficclasstable>`
    
    .. attribute:: dot1duserpriorityregentable
    
    	A list of Regenerated User Priorities for each received User Priority on each port of a bridge.  The Regenerated User Priority value may be used to index the Traffic Class Table for each input port.  This only has effect on media that support native User Priority.  The default values for Regenerated User Priorities are the same as the User Priorities
    	**type**\:   :py:class:`Dot1Duserpriorityregentable <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Duserpriorityregentable>`
    
    

    """

    _prefix = 'P-BRIDGE-MIB'
    _revision = '2006-01-09'

    def __init__(self):
        self.dot1dextbase = PBridgeMib.Dot1Dextbase()
        self.dot1dextbase.parent = self
        self.dot1dportoutboundaccessprioritytable = PBridgeMib.Dot1Dportoutboundaccessprioritytable()
        self.dot1dportoutboundaccessprioritytable.parent = self
        self.dot1dtphcporttable = PBridgeMib.Dot1Dtphcporttable()
        self.dot1dtphcporttable.parent = self
        self.dot1dtpportoverflowtable = PBridgeMib.Dot1Dtpportoverflowtable()
        self.dot1dtpportoverflowtable.parent = self
        self.dot1dtrafficclasstable = PBridgeMib.Dot1Dtrafficclasstable()
        self.dot1dtrafficclasstable.parent = self
        self.dot1duserpriorityregentable = PBridgeMib.Dot1Duserpriorityregentable()
        self.dot1duserpriorityregentable.parent = self


    class Dot1Dextbase(object):
        """
        
        
        .. attribute:: dot1ddevicecapabilities
        
        	Indicates the optional parts of IEEE 802.1D and 802.1Q that are implemented by this device and are manageable through this MIB.  Capabilities that are allowed on a per\-port basis are indicated in dot1dPortCapabilities.  dot1dExtendedFilteringServices(0),                       \-\- can perform filtering of                       \-\- individual multicast addresses                       \-\- controlled by GMRP. dot1dTrafficClasses(1),                       \-\- can map user priority to                       \-\- multiple traffic classes. dot1qStaticEntryIndividualPort(2),                       \-\- dot1qStaticUnicastReceivePort &                       \-\- dot1qStaticMulticastReceivePort                       \-\- can represent non\-zero entries. dot1qIVLCapable(3),   \-\- Independent VLAN Learning (IVL). dot1qSVLCapable(4),   \-\- Shared VLAN Learning (SVL). dot1qHybridCapable(5),                       \-\- both IVL & SVL simultaneously. dot1qConfigurablePvidTagging(6),                       \-\- whether the implementation                       \-\- supports the ability to                       \-\- override the default PVID                       \-\- setting and its egress status                       \-\- (VLAN\-Tagged or Untagged) on                       \-\- each port. dot1dLocalVlanCapable(7)                       \-\- can support multiple local                       \-\- bridges, outside of the scope                       \-\- of 802.1Q defined VLANs
        	**type**\:   :py:class:`Dot1Ddevicecapabilities <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Dextbase.Dot1Ddevicecapabilities>`
        
        .. attribute:: dot1dgmrpstatus
        
        	The administrative status requested by management for GMRP.  The value enabled(1) indicates that GMRP should be enabled on this device, in all VLANs, on all ports for which it has not been specifically disabled.  When disabled(2), GMRP is disabled, in all VLANs and on all ports, and all GMRP packets will be forwarded transparently.  This object affects both Applicant and Registrar state machines.  A transition from disabled(2) to enabled(1) will cause a reset of all GMRP state machines on all ports.  The value of this object MUST be retained across reinitializations of the management system
        	**type**\:   :py:class:`EnabledstatusEnum <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.EnabledstatusEnum>`
        
        .. attribute:: dot1dtrafficclassesenabled
        
        	The value true(1) indicates that Traffic Classes are enabled on this bridge.  When false(2), the bridge operates with a single priority level for all traffic.  The value of this object MUST be retained across reinitializations of the management system
        	**type**\:  bool
        
        

        """

        _prefix = 'P-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            self.parent = None
            self.dot1ddevicecapabilities = PBridgeMib.Dot1Dextbase.Dot1Ddevicecapabilities()
            self.dot1dgmrpstatus = None
            self.dot1dtrafficclassesenabled = None

        class Dot1Ddevicecapabilities(FixedBitsDict):
            """
            Dot1Ddevicecapabilities

            Indicates the optional parts of IEEE 802.1D and 802.1Q
            that are implemented by this device and are manageable
            through this MIB.  Capabilities that are allowed on a
            per\-port basis are indicated in dot1dPortCapabilities.
            
            dot1dExtendedFilteringServices(0),
                                  \-\- can perform filtering of
                                  \-\- individual multicast addresses
                                  \-\- controlled by GMRP.
            dot1dTrafficClasses(1),
                                  \-\- can map user priority to
                                  \-\- multiple traffic classes.
            dot1qStaticEntryIndividualPort(2),
                                  \-\- dot1qStaticUnicastReceivePort &
                                  \-\- dot1qStaticMulticastReceivePort
                                  \-\- can represent non\-zero entries.
            dot1qIVLCapable(3),   \-\- Independent VLAN Learning (IVL).
            dot1qSVLCapable(4),   \-\- Shared VLAN Learning (SVL).
            dot1qHybridCapable(5),
                                  \-\- both IVL & SVL simultaneously.
            dot1qConfigurablePvidTagging(6),
                                  \-\- whether the implementation
                                  \-\- supports the ability to
                                  \-\- override the default PVID
                                  \-\- setting and its egress status
                                  \-\- (VLAN\-Tagged or Untagged) on
                                  \-\- each port.
            dot1dLocalVlanCapable(7)
                                  \-\- can support multiple local
                                  \-\- bridges, outside of the scope
                                  \-\- of 802.1Q defined VLANs.
            Keys are:- dot1dTrafficClasses , dot1qStaticEntryIndividualPort , dot1qConfigurablePvidTagging , dot1qHybridCapable , dot1qIVLCapable , dot1dLocalVlanCapable , dot1dExtendedFilteringServices , dot1qSVLCapable

            """

            def __init__(self):
                self._dictionary = { 
                    'dot1dTrafficClasses':False,
                    'dot1qStaticEntryIndividualPort':False,
                    'dot1qConfigurablePvidTagging':False,
                    'dot1qHybridCapable':False,
                    'dot1qIVLCapable':False,
                    'dot1dLocalVlanCapable':False,
                    'dot1dExtendedFilteringServices':False,
                    'dot1qSVLCapable':False,
                }
                self._pos_map = { 
                    'dot1dTrafficClasses':1,
                    'dot1qStaticEntryIndividualPort':2,
                    'dot1qConfigurablePvidTagging':6,
                    'dot1qHybridCapable':5,
                    'dot1qIVLCapable':3,
                    'dot1dLocalVlanCapable':7,
                    'dot1dExtendedFilteringServices':0,
                    'dot1qSVLCapable':4,
                }

        @property
        def _common_path(self):

            return '/P-BRIDGE-MIB:P-BRIDGE-MIB/P-BRIDGE-MIB:dot1dExtBase'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dot1ddevicecapabilities is not None:
                if self.dot1ddevicecapabilities._has_data():
                    return True

            if self.dot1dgmrpstatus is not None:
                return True

            if self.dot1dtrafficclassesenabled is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _P_BRIDGE_MIB as meta
            return meta._meta_table['PBridgeMib.Dot1Dextbase']['meta_info']


    class Dot1Dtphcporttable(object):
        """
        A table that contains information about every high\-
        capacity port that is associated with this transparent
        bridge.
        
        .. attribute:: dot1dtphcportentry
        
        	Statistics information for each high\-capacity port of a transparent bridge
        	**type**\: list of    :py:class:`Dot1Dtphcportentry <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Dtphcporttable.Dot1Dtphcportentry>`
        
        

        """

        _prefix = 'P-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            self.parent = None
            self.dot1dtphcportentry = YList()
            self.dot1dtphcportentry.parent = self
            self.dot1dtphcportentry.name = 'dot1dtphcportentry'


        class Dot1Dtphcportentry(object):
            """
            Statistics information for each high\-capacity port of a
            transparent bridge.
            
            .. attribute:: dot1dtpport  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`dot1dtpport <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dtpporttable.Dot1Dtpportentry>`
            
            .. attribute:: dot1dtphcportindiscards
            
            	Count of valid frames that have been received by this port from its segment that were discarded (i.e., filtered) by the Forwarding Process
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dot1dtphcportinframes
            
            	The number of frames that have been received by this port from its segment.  Note that a frame received on the interface corresponding to this port is only counted by this object if and only if it is for a protocol being processed by the local bridging function, including bridge management frames
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: dot1dtphcportoutframes
            
            	The number of frames that have been transmitted by this port to its segment.  Note that a frame transmitted on the interface corresponding to this port is only counted by this object if and only if it is for a protocol being processed by the local bridging function, including bridge management frames
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'P-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                self.parent = None
                self.dot1dtpport = None
                self.dot1dtphcportindiscards = None
                self.dot1dtphcportinframes = None
                self.dot1dtphcportoutframes = None

            @property
            def _common_path(self):
                if self.dot1dtpport is None:
                    raise YPYModelError('Key property dot1dtpport is None')

                return '/P-BRIDGE-MIB:P-BRIDGE-MIB/P-BRIDGE-MIB:dot1dTpHCPortTable/P-BRIDGE-MIB:dot1dTpHCPortEntry[P-BRIDGE-MIB:dot1dTpPort = ' + str(self.dot1dtpport) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dot1dtpport is not None:
                    return True

                if self.dot1dtphcportindiscards is not None:
                    return True

                if self.dot1dtphcportinframes is not None:
                    return True

                if self.dot1dtphcportoutframes is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _P_BRIDGE_MIB as meta
                return meta._meta_table['PBridgeMib.Dot1Dtphcporttable.Dot1Dtphcportentry']['meta_info']

        @property
        def _common_path(self):

            return '/P-BRIDGE-MIB:P-BRIDGE-MIB/P-BRIDGE-MIB:dot1dTpHCPortTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dot1dtphcportentry is not None:
                for child_ref in self.dot1dtphcportentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _P_BRIDGE_MIB as meta
            return meta._meta_table['PBridgeMib.Dot1Dtphcporttable']['meta_info']


    class Dot1Dtpportoverflowtable(object):
        """
        A table that contains the most\-significant bits of
        statistics counters for ports that are associated with this
        transparent bridge that are on high\-capacity interfaces, as
        defined in the conformance clauses for this table.  This table
        is provided as a way to read 64\-bit counters for agents that
        support only SNMPv1.
        
        Note that the reporting of most\-significant and
        least\-significant counter bits separately runs the risk of
        missing an overflow of the lower bits in the interval between
        sampling.  The manager must be aware of this possibility, even
        within the same varbindlist, when interpreting the results of
        a request or asynchronous notification.
        
        .. attribute:: dot1dtpportoverflowentry
        
        	The most significant bits of statistics counters for a high\- capacity interface of a transparent bridge.  Each object is associated with a corresponding object in dot1dTpPortTable that indicates the least significant bits of the counter
        	**type**\: list of    :py:class:`Dot1Dtpportoverflowentry <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Dtpportoverflowtable.Dot1Dtpportoverflowentry>`
        
        

        """

        _prefix = 'P-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            self.parent = None
            self.dot1dtpportoverflowentry = YList()
            self.dot1dtpportoverflowentry.parent = self
            self.dot1dtpportoverflowentry.name = 'dot1dtpportoverflowentry'


        class Dot1Dtpportoverflowentry(object):
            """
            The most significant bits of statistics counters for a high\-
            capacity interface of a transparent bridge.  Each object is
            associated with a corresponding object in dot1dTpPortTable
            that indicates the least significant bits of the counter.
            
            .. attribute:: dot1dtpport  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`dot1dtpport <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dtpporttable.Dot1Dtpportentry>`
            
            .. attribute:: dot1dtpportinoverflowdiscards
            
            	The number of times the associated dot1dTpPortInDiscards counter has overflowed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1dtpportinoverflowframes
            
            	The number of times the associated dot1dTpPortInFrames counter has overflowed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1dtpportoutoverflowframes
            
            	The number of times the associated dot1dTpPortOutFrames counter has overflowed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'P-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                self.parent = None
                self.dot1dtpport = None
                self.dot1dtpportinoverflowdiscards = None
                self.dot1dtpportinoverflowframes = None
                self.dot1dtpportoutoverflowframes = None

            @property
            def _common_path(self):
                if self.dot1dtpport is None:
                    raise YPYModelError('Key property dot1dtpport is None')

                return '/P-BRIDGE-MIB:P-BRIDGE-MIB/P-BRIDGE-MIB:dot1dTpPortOverflowTable/P-BRIDGE-MIB:dot1dTpPortOverflowEntry[P-BRIDGE-MIB:dot1dTpPort = ' + str(self.dot1dtpport) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dot1dtpport is not None:
                    return True

                if self.dot1dtpportinoverflowdiscards is not None:
                    return True

                if self.dot1dtpportinoverflowframes is not None:
                    return True

                if self.dot1dtpportoutoverflowframes is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _P_BRIDGE_MIB as meta
                return meta._meta_table['PBridgeMib.Dot1Dtpportoverflowtable.Dot1Dtpportoverflowentry']['meta_info']

        @property
        def _common_path(self):

            return '/P-BRIDGE-MIB:P-BRIDGE-MIB/P-BRIDGE-MIB:dot1dTpPortOverflowTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dot1dtpportoverflowentry is not None:
                for child_ref in self.dot1dtpportoverflowentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _P_BRIDGE_MIB as meta
            return meta._meta_table['PBridgeMib.Dot1Dtpportoverflowtable']['meta_info']


    class Dot1Duserpriorityregentable(object):
        """
        A list of Regenerated User Priorities for each received
        User Priority on each port of a bridge.  The Regenerated
        User Priority value may be used to index the Traffic
        Class Table for each input port.  This only has effect
        on media that support native User Priority.  The default
        values for Regenerated User Priorities are the same as
        the User Priorities.
        
        .. attribute:: dot1duserpriorityregenentry
        
        	A mapping of incoming User Priority to a Regenerated User Priority
        	**type**\: list of    :py:class:`Dot1Duserpriorityregenentry <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Duserpriorityregentable.Dot1Duserpriorityregenentry>`
        
        

        """

        _prefix = 'P-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            self.parent = None
            self.dot1duserpriorityregenentry = YList()
            self.dot1duserpriorityregenentry.parent = self
            self.dot1duserpriorityregenentry.name = 'dot1duserpriorityregenentry'


        class Dot1Duserpriorityregenentry(object):
            """
            A mapping of incoming User Priority to a Regenerated
            User Priority.
            
            .. attribute:: dot1dbaseport  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`dot1dbaseport <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry>`
            
            .. attribute:: dot1duserpriority  <key>
            
            	The User Priority for a frame received on this port
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: dot1dregenuserpriority
            
            	The Regenerated User Priority that the incoming User  Priority is mapped to for this port.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  int
            
            	**range:** 0..7
            
            

            """

            _prefix = 'P-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                self.parent = None
                self.dot1dbaseport = None
                self.dot1duserpriority = None
                self.dot1dregenuserpriority = None

            @property
            def _common_path(self):
                if self.dot1dbaseport is None:
                    raise YPYModelError('Key property dot1dbaseport is None')
                if self.dot1duserpriority is None:
                    raise YPYModelError('Key property dot1duserpriority is None')

                return '/P-BRIDGE-MIB:P-BRIDGE-MIB/P-BRIDGE-MIB:dot1dUserPriorityRegenTable/P-BRIDGE-MIB:dot1dUserPriorityRegenEntry[P-BRIDGE-MIB:dot1dBasePort = ' + str(self.dot1dbaseport) + '][P-BRIDGE-MIB:dot1dUserPriority = ' + str(self.dot1duserpriority) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dot1dbaseport is not None:
                    return True

                if self.dot1duserpriority is not None:
                    return True

                if self.dot1dregenuserpriority is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _P_BRIDGE_MIB as meta
                return meta._meta_table['PBridgeMib.Dot1Duserpriorityregentable.Dot1Duserpriorityregenentry']['meta_info']

        @property
        def _common_path(self):

            return '/P-BRIDGE-MIB:P-BRIDGE-MIB/P-BRIDGE-MIB:dot1dUserPriorityRegenTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dot1duserpriorityregenentry is not None:
                for child_ref in self.dot1duserpriorityregenentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _P_BRIDGE_MIB as meta
            return meta._meta_table['PBridgeMib.Dot1Duserpriorityregentable']['meta_info']


    class Dot1Dtrafficclasstable(object):
        """
        A table mapping evaluated User Priority to Traffic
        Class, for forwarding by the bridge.  Traffic class is a
        number in the range (0..(dot1dPortNumTrafficClasses\-1)).
        
        .. attribute:: dot1dtrafficclassentry
        
        	User Priority to Traffic Class mapping
        	**type**\: list of    :py:class:`Dot1Dtrafficclassentry <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Dtrafficclasstable.Dot1Dtrafficclassentry>`
        
        

        """

        _prefix = 'P-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            self.parent = None
            self.dot1dtrafficclassentry = YList()
            self.dot1dtrafficclassentry.parent = self
            self.dot1dtrafficclassentry.name = 'dot1dtrafficclassentry'


        class Dot1Dtrafficclassentry(object):
            """
            User Priority to Traffic Class mapping.
            
            .. attribute:: dot1dbaseport  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`dot1dbaseport <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry>`
            
            .. attribute:: dot1dtrafficclasspriority  <key>
            
            	The Priority value determined for the received frame. This value is equivalent to the priority indicated in the tagged frame received, or one of the evaluated priorities, determined according to the media\-type.  For untagged frames received from Ethernet media, this value is equal to the dot1dPortDefaultUserPriority value for the ingress port.  For untagged frames received from non\-Ethernet media, this value is equal to the dot1dRegenUserPriority value for the ingress port and media\-specific user priority
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: dot1dtrafficclass
            
            	The Traffic Class the received frame is mapped to.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  int
            
            	**range:** 0..7
            
            

            """

            _prefix = 'P-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                self.parent = None
                self.dot1dbaseport = None
                self.dot1dtrafficclasspriority = None
                self.dot1dtrafficclass = None

            @property
            def _common_path(self):
                if self.dot1dbaseport is None:
                    raise YPYModelError('Key property dot1dbaseport is None')
                if self.dot1dtrafficclasspriority is None:
                    raise YPYModelError('Key property dot1dtrafficclasspriority is None')

                return '/P-BRIDGE-MIB:P-BRIDGE-MIB/P-BRIDGE-MIB:dot1dTrafficClassTable/P-BRIDGE-MIB:dot1dTrafficClassEntry[P-BRIDGE-MIB:dot1dBasePort = ' + str(self.dot1dbaseport) + '][P-BRIDGE-MIB:dot1dTrafficClassPriority = ' + str(self.dot1dtrafficclasspriority) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dot1dbaseport is not None:
                    return True

                if self.dot1dtrafficclasspriority is not None:
                    return True

                if self.dot1dtrafficclass is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _P_BRIDGE_MIB as meta
                return meta._meta_table['PBridgeMib.Dot1Dtrafficclasstable.Dot1Dtrafficclassentry']['meta_info']

        @property
        def _common_path(self):

            return '/P-BRIDGE-MIB:P-BRIDGE-MIB/P-BRIDGE-MIB:dot1dTrafficClassTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dot1dtrafficclassentry is not None:
                for child_ref in self.dot1dtrafficclassentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _P_BRIDGE_MIB as meta
            return meta._meta_table['PBridgeMib.Dot1Dtrafficclasstable']['meta_info']


    class Dot1Dportoutboundaccessprioritytable(object):
        """
        A table mapping Regenerated User Priority to Outbound
        Access Priority.  This is a fixed mapping for all port
        types, with two options for 802.5 Token Ring.
        
        .. attribute:: dot1dportoutboundaccesspriorityentry
        
        	Regenerated User Priority to Outbound Access Priority mapping
        	**type**\: list of    :py:class:`Dot1Dportoutboundaccesspriorityentry <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Dportoutboundaccessprioritytable.Dot1Dportoutboundaccesspriorityentry>`
        
        

        """

        _prefix = 'P-BRIDGE-MIB'
        _revision = '2006-01-09'

        def __init__(self):
            self.parent = None
            self.dot1dportoutboundaccesspriorityentry = YList()
            self.dot1dportoutboundaccesspriorityentry.parent = self
            self.dot1dportoutboundaccesspriorityentry.name = 'dot1dportoutboundaccesspriorityentry'


        class Dot1Dportoutboundaccesspriorityentry(object):
            """
            Regenerated User Priority to Outbound Access Priority
            mapping.
            
            .. attribute:: dot1dbaseport  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`dot1dbaseport <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry>`
            
            .. attribute:: dot1dregenuserpriority  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..7
            
            	**refers to**\:  :py:class:`dot1dregenuserpriority <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.PBridgeMib.Dot1Duserpriorityregentable.Dot1Duserpriorityregenentry>`
            
            .. attribute:: dot1dportoutboundaccesspriority
            
            	The Outbound Access Priority the received frame is mapped to
            	**type**\:  int
            
            	**range:** 0..7
            
            

            """

            _prefix = 'P-BRIDGE-MIB'
            _revision = '2006-01-09'

            def __init__(self):
                self.parent = None
                self.dot1dbaseport = None
                self.dot1dregenuserpriority = None
                self.dot1dportoutboundaccesspriority = None

            @property
            def _common_path(self):
                if self.dot1dbaseport is None:
                    raise YPYModelError('Key property dot1dbaseport is None')
                if self.dot1dregenuserpriority is None:
                    raise YPYModelError('Key property dot1dregenuserpriority is None')

                return '/P-BRIDGE-MIB:P-BRIDGE-MIB/P-BRIDGE-MIB:dot1dPortOutboundAccessPriorityTable/P-BRIDGE-MIB:dot1dPortOutboundAccessPriorityEntry[P-BRIDGE-MIB:dot1dBasePort = ' + str(self.dot1dbaseport) + '][P-BRIDGE-MIB:dot1dRegenUserPriority = ' + str(self.dot1dregenuserpriority) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dot1dbaseport is not None:
                    return True

                if self.dot1dregenuserpriority is not None:
                    return True

                if self.dot1dportoutboundaccesspriority is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _P_BRIDGE_MIB as meta
                return meta._meta_table['PBridgeMib.Dot1Dportoutboundaccessprioritytable.Dot1Dportoutboundaccesspriorityentry']['meta_info']

        @property
        def _common_path(self):

            return '/P-BRIDGE-MIB:P-BRIDGE-MIB/P-BRIDGE-MIB:dot1dPortOutboundAccessPriorityTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dot1dportoutboundaccesspriorityentry is not None:
                for child_ref in self.dot1dportoutboundaccesspriorityentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _P_BRIDGE_MIB as meta
            return meta._meta_table['PBridgeMib.Dot1Dportoutboundaccessprioritytable']['meta_info']

    @property
    def _common_path(self):

        return '/P-BRIDGE-MIB:P-BRIDGE-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.dot1dextbase is not None and self.dot1dextbase._has_data():
            return True

        if self.dot1dportoutboundaccessprioritytable is not None and self.dot1dportoutboundaccessprioritytable._has_data():
            return True

        if self.dot1dtphcporttable is not None and self.dot1dtphcporttable._has_data():
            return True

        if self.dot1dtpportoverflowtable is not None and self.dot1dtpportoverflowtable._has_data():
            return True

        if self.dot1dtrafficclasstable is not None and self.dot1dtrafficclasstable._has_data():
            return True

        if self.dot1duserpriorityregentable is not None and self.dot1duserpriorityregentable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _P_BRIDGE_MIB as meta
        return meta._meta_table['PBridgeMib']['meta_info']



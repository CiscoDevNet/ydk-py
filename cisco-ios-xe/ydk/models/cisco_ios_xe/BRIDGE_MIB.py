""" BRIDGE_MIB 

The Bridge MIB module for managing devices that support
IEEE 802.1D.

Copyright (C) The Internet Society (2005).  This version of
this MIB module is part of RFC 4188; see the RFC itself for
full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class BridgeMib(object):
    """
    
    
    .. attribute:: dot1dbase
    
    	
    	**type**\:   :py:class:`Dot1Dbase <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dbase>`
    
    .. attribute:: dot1dbaseporttable
    
    	A table that contains generic information about every port that is associated with this bridge.  Transparent, source\-route, and srt ports are included
    	**type**\:   :py:class:`Dot1Dbaseporttable <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dbaseporttable>`
    
    .. attribute:: dot1dstatictable
    
    	A table containing filtering information configured into the bridge by (local or network) management specifying the set of ports to which frames received from specific ports and containing specific destination addresses are allowed to be forwarded.  The value of zero in this table, as the port number from which frames with a specific destination address are received, is used to specify all ports for which there is no specific entry in this table for that particular destination address.  Entries are valid for unicast and for group/broadcast addresses
    	**type**\:   :py:class:`Dot1Dstatictable <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dstatictable>`
    
    .. attribute:: dot1dstp
    
    	
    	**type**\:   :py:class:`Dot1Dstp <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dstp>`
    
    .. attribute:: dot1dstpporttable
    
    	A table that contains port\-specific information for the Spanning Tree Protocol
    	**type**\:   :py:class:`Dot1Dstpporttable <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dstpporttable>`
    
    .. attribute:: dot1dtp
    
    	
    	**type**\:   :py:class:`Dot1Dtp <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dtp>`
    
    .. attribute:: dot1dtpfdbtable
    
    	A table that contains information about unicast entries for which the bridge has forwarding and/or filtering information.  This information is used by the transparent bridging function in determining how to propagate a received frame
    	**type**\:   :py:class:`Dot1Dtpfdbtable <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dtpfdbtable>`
    
    .. attribute:: dot1dtpporttable
    
    	A table that contains information about every port that is associated with this transparent bridge
    	**type**\:   :py:class:`Dot1Dtpporttable <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dtpporttable>`
    
    

    """

    _prefix = 'BRIDGE-MIB'
    _revision = '2005-09-19'

    def __init__(self):
        self.dot1dbase = BridgeMib.Dot1Dbase()
        self.dot1dbase.parent = self
        self.dot1dbaseporttable = BridgeMib.Dot1Dbaseporttable()
        self.dot1dbaseporttable.parent = self
        self.dot1dstatictable = BridgeMib.Dot1Dstatictable()
        self.dot1dstatictable.parent = self
        self.dot1dstp = BridgeMib.Dot1Dstp()
        self.dot1dstp.parent = self
        self.dot1dstpporttable = BridgeMib.Dot1Dstpporttable()
        self.dot1dstpporttable.parent = self
        self.dot1dtp = BridgeMib.Dot1Dtp()
        self.dot1dtp.parent = self
        self.dot1dtpfdbtable = BridgeMib.Dot1Dtpfdbtable()
        self.dot1dtpfdbtable.parent = self
        self.dot1dtpporttable = BridgeMib.Dot1Dtpporttable()
        self.dot1dtpporttable.parent = self


    class Dot1Dbase(object):
        """
        
        
        .. attribute:: dot1dbasebridgeaddress
        
        	The MAC address used by this bridge when it must be referred to in a unique fashion.  It is recommended that this be the numerically smallest MAC address of all ports that belong to this bridge.  However, it is only  required to be unique.  When concatenated with dot1dStpPriority, a unique BridgeIdentifier is formed, which is used in the Spanning Tree Protocol
        	**type**\:  str
        
        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
        
        .. attribute:: dot1dbasenumports
        
        	The number of ports controlled by this bridging entity
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        	**units**\: ports
        
        .. attribute:: dot1dbasetype
        
        	Indicates what type of bridging this bridge can perform.  If a bridge is actually performing a certain type of bridging, this will be indicated by entries in the port table for the given type
        	**type**\:   :py:class:`Dot1DbasetypeEnum <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dbase.Dot1DbasetypeEnum>`
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            self.parent = None
            self.dot1dbasebridgeaddress = None
            self.dot1dbasenumports = None
            self.dot1dbasetype = None

        class Dot1DbasetypeEnum(Enum):
            """
            Dot1DbasetypeEnum

            Indicates what type of bridging this bridge can

            perform.  If a bridge is actually performing a

            certain type of bridging, this will be indicated by

            entries in the port table for the given type.

            .. data:: unknown = 1

            .. data:: transparent_only = 2

            .. data:: sourceroute_only = 3

            .. data:: srt = 4

            """

            unknown = 1

            transparent_only = 2

            sourceroute_only = 3

            srt = 4


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _BRIDGE_MIB as meta
                return meta._meta_table['BridgeMib.Dot1Dbase.Dot1DbasetypeEnum']


        @property
        def _common_path(self):

            return '/BRIDGE-MIB:BRIDGE-MIB/BRIDGE-MIB:dot1dBase'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dot1dbasebridgeaddress is not None:
                return True

            if self.dot1dbasenumports is not None:
                return True

            if self.dot1dbasetype is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _BRIDGE_MIB as meta
            return meta._meta_table['BridgeMib.Dot1Dbase']['meta_info']


    class Dot1Dstp(object):
        """
        
        
        .. attribute:: dot1dstpbridgeforwarddelay
        
        	The value that all bridges use for ForwardDelay when this bridge is acting as the root.  Note that 802.1D\-1998 specifies that the range for this parameter is related to the value of dot1dStpBridgeMaxAge.  The granularity of this timer is specified by 802.1D\-1998 to be 1 second.  An agent may return a badValue error if a set is attempted to a value that is not a whole number of seconds
        	**type**\:  int
        
        	**range:** 400..3000
        
        	**units**\: centi-seconds
        
        .. attribute:: dot1dstpbridgehellotime
        
        	The value that all bridges use for HelloTime when this bridge is acting as the root.  The granularity of this timer is specified by 802.1D\-1998 to be 1 second.  An agent may return a badValue error if a set is attempted  to a value that is not a whole number of seconds
        	**type**\:  int
        
        	**range:** 100..1000
        
        	**units**\: centi-seconds
        
        .. attribute:: dot1dstpbridgemaxage
        
        	The value that all bridges use for MaxAge when this bridge is acting as the root.  Note that 802.1D\-1998 specifies that the range for this parameter is related to the value of dot1dStpBridgeHelloTime.  The granularity of this timer is specified by 802.1D\-1998 to be 1 second.  An agent may return a badValue error if a set is attempted to a value that is not a whole number of seconds
        	**type**\:  int
        
        	**range:** 600..4000
        
        	**units**\: centi-seconds
        
        .. attribute:: dot1dstpdesignatedroot
        
        	The bridge identifier of the root of the spanning tree, as determined by the Spanning Tree Protocol, as executed by this node.  This value is used as the Root Identifier parameter in all Configuration Bridge PDUs originated by this node
        	**type**\:  str
        
        	**length:** 8
        
        .. attribute:: dot1dstpforwarddelay
        
        	This time value, measured in units of hundredths of a second, controls how fast a port changes its spanning state when moving towards the Forwarding state.  The value determines how long the port stays in each of the Listening and Learning states, which precede the Forwarding state.  This value is also used when a topology change has been detected and is underway, to age all dynamic entries in the Forwarding Database. [Note that this value is the one that this bridge is currently using, in contrast to dot1dStpBridgeForwardDelay, which is the value that this bridge and all others would start using if/when this bridge were to become the root.]
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        	**units**\: centi-seconds
        
        .. attribute:: dot1dstphellotime
        
        	The amount of time between the transmission of Configuration bridge PDUs by this node on any port when it is the root of the spanning tree, or trying to become so, in units of hundredths of a second.  This is the actual value that this bridge is currently using
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        	**units**\: centi-seconds
        
        .. attribute:: dot1dstpholdtime
        
        	This time value determines the interval length during which no more than two Configuration bridge PDUs shall be transmitted by this node, in units of hundredths of a second
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        	**units**\: centi-seconds
        
        .. attribute:: dot1dstpmaxage
        
        	The maximum age of Spanning Tree Protocol information learned from the network on any port before it is discarded, in units of hundredths of a second.  This is the actual value that this bridge is currently using
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        	**units**\: centi-seconds
        
        .. attribute:: dot1dstppriority
        
        	The value of the write\-able portion of the Bridge ID (i.e., the first two octets of the (8 octet long) Bridge ID).  The other (last) 6 octets of the Bridge ID are given by the value of dot1dBaseBridgeAddress. On bridges supporting IEEE 802.1t or IEEE 802.1w, permissible values are 0\-61440, in steps of 4096
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: dot1dstpprotocolspecification
        
        	An indication of what version of the Spanning Tree Protocol is being run.  The value 'decLb100(2)' indicates the DEC LANbridge 100 Spanning Tree protocol. IEEE 802.1D implementations will return 'ieee8021d(3)'. If future versions of the IEEE Spanning Tree Protocol that are incompatible with the current version are released a new value will be defined
        	**type**\:   :py:class:`Dot1DstpprotocolspecificationEnum <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dstp.Dot1DstpprotocolspecificationEnum>`
        
        .. attribute:: dot1dstprootcost
        
        	The cost of the path to the root as seen from this bridge
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: dot1dstprootport
        
        	The port number of the port that offers the lowest cost path from this bridge to the root bridge
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: dot1dstptimesincetopologychange
        
        	The time (in hundredths of a second) since the last time a topology change was detected by the bridge entity. For RSTP, this reports the time since the tcWhile timer for any port on this Bridge was nonzero
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: centi-seconds
        
        .. attribute:: dot1dstptopchanges
        
        	The total number of topology changes detected by this bridge since the management entity was last reset or initialized
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            self.parent = None
            self.dot1dstpbridgeforwarddelay = None
            self.dot1dstpbridgehellotime = None
            self.dot1dstpbridgemaxage = None
            self.dot1dstpdesignatedroot = None
            self.dot1dstpforwarddelay = None
            self.dot1dstphellotime = None
            self.dot1dstpholdtime = None
            self.dot1dstpmaxage = None
            self.dot1dstppriority = None
            self.dot1dstpprotocolspecification = None
            self.dot1dstprootcost = None
            self.dot1dstprootport = None
            self.dot1dstptimesincetopologychange = None
            self.dot1dstptopchanges = None

        class Dot1DstpprotocolspecificationEnum(Enum):
            """
            Dot1DstpprotocolspecificationEnum

            An indication of what version of the Spanning Tree

            Protocol is being run.  The value 'decLb100(2)'

            indicates the DEC LANbridge 100 Spanning Tree protocol.

            IEEE 802.1D implementations will return 'ieee8021d(3)'.

            If future versions of the IEEE Spanning Tree Protocol

            that are incompatible with the current version

            are released a new value will be defined.

            .. data:: unknown = 1

            .. data:: decLb100 = 2

            .. data:: ieee8021d = 3

            """

            unknown = 1

            decLb100 = 2

            ieee8021d = 3


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _BRIDGE_MIB as meta
                return meta._meta_table['BridgeMib.Dot1Dstp.Dot1DstpprotocolspecificationEnum']


        @property
        def _common_path(self):

            return '/BRIDGE-MIB:BRIDGE-MIB/BRIDGE-MIB:dot1dStp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dot1dstpbridgeforwarddelay is not None:
                return True

            if self.dot1dstpbridgehellotime is not None:
                return True

            if self.dot1dstpbridgemaxage is not None:
                return True

            if self.dot1dstpdesignatedroot is not None:
                return True

            if self.dot1dstpforwarddelay is not None:
                return True

            if self.dot1dstphellotime is not None:
                return True

            if self.dot1dstpholdtime is not None:
                return True

            if self.dot1dstpmaxage is not None:
                return True

            if self.dot1dstppriority is not None:
                return True

            if self.dot1dstpprotocolspecification is not None:
                return True

            if self.dot1dstprootcost is not None:
                return True

            if self.dot1dstprootport is not None:
                return True

            if self.dot1dstptimesincetopologychange is not None:
                return True

            if self.dot1dstptopchanges is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _BRIDGE_MIB as meta
            return meta._meta_table['BridgeMib.Dot1Dstp']['meta_info']


    class Dot1Dtp(object):
        """
        
        
        .. attribute:: dot1dtpagingtime
        
        	The timeout period in seconds for aging out dynamically\-learned forwarding information. 802.1D\-1998 recommends a default of 300 seconds
        	**type**\:  int
        
        	**range:** 10..1000000
        
        	**units**\: seconds
        
        .. attribute:: dot1dtplearnedentrydiscards
        
        	The total number of Forwarding Database entries that have been or would have been learned, but have been discarded due to a lack of storage space in the Forwarding Database.  If this counter is increasing, it indicates that the Forwarding Database is regularly becoming full (a condition that has unpleasant performance effects on the subnetwork).  If this counter has a significant value but is not presently increasing, it indicates that the problem has been occurring but is not persistent
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            self.parent = None
            self.dot1dtpagingtime = None
            self.dot1dtplearnedentrydiscards = None

        @property
        def _common_path(self):

            return '/BRIDGE-MIB:BRIDGE-MIB/BRIDGE-MIB:dot1dTp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dot1dtpagingtime is not None:
                return True

            if self.dot1dtplearnedentrydiscards is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _BRIDGE_MIB as meta
            return meta._meta_table['BridgeMib.Dot1Dtp']['meta_info']


    class Dot1Dbaseporttable(object):
        """
        A table that contains generic information about every
        port that is associated with this bridge.  Transparent,
        source\-route, and srt ports are included.
        
        .. attribute:: dot1dbaseportentry
        
        	A list of information for each port of the bridge
        	**type**\: list of    :py:class:`Dot1Dbaseportentry <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry>`
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            self.parent = None
            self.dot1dbaseportentry = YList()
            self.dot1dbaseportentry.parent = self
            self.dot1dbaseportentry.name = 'dot1dbaseportentry'


        class Dot1Dbaseportentry(object):
            """
            A list of information for each port of the bridge.
            
            .. attribute:: dot1dbaseport  <key>
            
            	The port number of the port for which this entry contains bridge management information
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: dot1dbaseportcircuit
            
            	For a port that (potentially) has the same value of dot1dBasePortIfIndex as another port on the same bridge. This object contains the name of an object instance unique to this port.  For example, in the case where multiple ports correspond one\-to\-one with multiple X.25 virtual circuits, this value might identify an (e.g., the first) object instance associated with the X.25 virtual circuit corresponding to this port.  For a port which has a unique value of dot1dBasePortIfIndex, this object can have the value { 0 0 }
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: dot1dbaseportdelayexceededdiscards
            
            	The number of frames discarded by this port due to excessive transit delay through the bridge.  It is incremented by both transparent and source route bridges
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1dbaseportifindex
            
            	The value of the instance of the ifIndex object, defined in IF\-MIB, for the interface corresponding to this port
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: dot1dbaseportmtuexceededdiscards
            
            	The number of frames discarded by this port due to an excessive size.  It is incremented by both transparent and source route bridges
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1dportcapabilities
            
            	Indicates the parts of IEEE 802.1D and 802.1Q that are optional on a per\-port basis, that are implemented by this device, and that are manageable through this MIB.  dot1qDot1qTagging(0), \-\- supports 802.1Q VLAN tagging of                       \-\- frames and GVRP. dot1qConfigurableAcceptableFrameTypes(1),                       \-\- allows modified values of                       \-\- dot1qPortAcceptableFrameTypes. dot1qIngressFiltering(2)                       \-\- supports the discarding of any                       \-\- frame received on a Port whose                       \-\- VLAN classification does not                       \-\- include that Port in its Member                       \-\- set
            	**type**\:   :py:class:`Dot1Dportcapabilities <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry.Dot1Dportcapabilities>`
            
            .. attribute:: dot1dportdefaultuserpriority
            
            	The default ingress User Priority for this port.  This only has effect on media, such as Ethernet, that do not support native User Priority.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: dot1dportgarpjointime
            
            	The GARP Join time, in centiseconds.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: dot1dportgarpleavealltime
            
            	The GARP LeaveAll time, in centiseconds.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: dot1dportgarpleavetime
            
            	The GARP Leave time, in centiseconds.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: dot1dportgmrpfailedregistrations
            
            	The total number of failed GMRP registrations, for any reason, in all VLANs, on this port
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1dportgmrplastpduorigin
            
            	The Source MAC Address of the last GMRP message received on this port
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1dportgmrpstatus
            
            	The administrative state of GMRP operation on this port.  The value enabled(1) indicates that GMRP is enabled on this port in all VLANs as long as dot1dGmrpStatus is also enabled(1). A value of disabled(2) indicates that GMRP is disabled on this port in all VLANs\: any GMRP packets received will be silently discarded, and no GMRP registrations will be propagated from other ports.  Setting this to a value of enabled(1) will be stored by the agent but will only take effect on the GMRP protocol operation if dot1dGmrpStatus also indicates the value enabled(1).  This object affects all GMRP Applicant and Registrar state machines on this port.  A transition from disabled(2) to enabled(1) will cause a reset of all GMRP state machines on this port.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:   :py:class:`EnabledstatusEnum <ydk.models.cisco_ios_xe.P_BRIDGE_MIB.EnabledstatusEnum>`
            
            .. attribute:: dot1dportnumtrafficclasses
            
            	The number of egress traffic classes supported on this port.  This object may optionally be read\-only.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  int
            
            	**range:** 1..8
            
            .. attribute:: dot1dportrestrictedgroupregistration
            
            	The state of Restricted Group Registration on this port. If the value of this control is true(1), then creation of a new dynamic entry is permitted only if there is a Static Filtering Entry for the VLAN concerned, in which the Registrar Administrative Control value is Normal Registration.  The value of this object MUST be retained across reinitializations of the management system
            	**type**\:  bool
            
            

            """

            _prefix = 'BRIDGE-MIB'
            _revision = '2005-09-19'

            def __init__(self):
                self.parent = None
                self.dot1dbaseport = None
                self.dot1dbaseportcircuit = None
                self.dot1dbaseportdelayexceededdiscards = None
                self.dot1dbaseportifindex = None
                self.dot1dbaseportmtuexceededdiscards = None
                self.dot1dportcapabilities = BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry.Dot1Dportcapabilities()
                self.dot1dportdefaultuserpriority = None
                self.dot1dportgarpjointime = None
                self.dot1dportgarpleavealltime = None
                self.dot1dportgarpleavetime = None
                self.dot1dportgmrpfailedregistrations = None
                self.dot1dportgmrplastpduorigin = None
                self.dot1dportgmrpstatus = None
                self.dot1dportnumtrafficclasses = None
                self.dot1dportrestrictedgroupregistration = None

            class Dot1Dportcapabilities(FixedBitsDict):
                """
                Dot1Dportcapabilities

                Indicates the parts of IEEE 802.1D and 802.1Q that are
                optional on a per\-port basis, that are implemented by
                this device, and that are manageable through this MIB.
                
                dot1qDot1qTagging(0), \-\- supports 802.1Q VLAN tagging of
                                      \-\- frames and GVRP.
                dot1qConfigurableAcceptableFrameTypes(1),
                                      \-\- allows modified values of
                                      \-\- dot1qPortAcceptableFrameTypes.
                dot1qIngressFiltering(2)
                                      \-\- supports the discarding of any
                                      \-\- frame received on a Port whose
                                      \-\- VLAN classification does not
                                      \-\- include that Port in its Member
                                      \-\- set.
                Keys are:- dot1qDot1qTagging , dot1qIngressFiltering , dot1qConfigurableAcceptableFrameTypes

                """

                def __init__(self):
                    self._dictionary = { 
                        'dot1qDot1qTagging':False,
                        'dot1qIngressFiltering':False,
                        'dot1qConfigurableAcceptableFrameTypes':False,
                    }
                    self._pos_map = { 
                        'dot1qDot1qTagging':0,
                        'dot1qIngressFiltering':2,
                        'dot1qConfigurableAcceptableFrameTypes':1,
                    }

            @property
            def _common_path(self):
                if self.dot1dbaseport is None:
                    raise YPYModelError('Key property dot1dbaseport is None')

                return '/BRIDGE-MIB:BRIDGE-MIB/BRIDGE-MIB:dot1dBasePortTable/BRIDGE-MIB:dot1dBasePortEntry[BRIDGE-MIB:dot1dBasePort = ' + str(self.dot1dbaseport) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dot1dbaseport is not None:
                    return True

                if self.dot1dbaseportcircuit is not None:
                    return True

                if self.dot1dbaseportdelayexceededdiscards is not None:
                    return True

                if self.dot1dbaseportifindex is not None:
                    return True

                if self.dot1dbaseportmtuexceededdiscards is not None:
                    return True

                if self.dot1dportcapabilities is not None:
                    if self.dot1dportcapabilities._has_data():
                        return True

                if self.dot1dportdefaultuserpriority is not None:
                    return True

                if self.dot1dportgarpjointime is not None:
                    return True

                if self.dot1dportgarpleavealltime is not None:
                    return True

                if self.dot1dportgarpleavetime is not None:
                    return True

                if self.dot1dportgmrpfailedregistrations is not None:
                    return True

                if self.dot1dportgmrplastpduorigin is not None:
                    return True

                if self.dot1dportgmrpstatus is not None:
                    return True

                if self.dot1dportnumtrafficclasses is not None:
                    return True

                if self.dot1dportrestrictedgroupregistration is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _BRIDGE_MIB as meta
                return meta._meta_table['BridgeMib.Dot1Dbaseporttable.Dot1Dbaseportentry']['meta_info']

        @property
        def _common_path(self):

            return '/BRIDGE-MIB:BRIDGE-MIB/BRIDGE-MIB:dot1dBasePortTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dot1dbaseportentry is not None:
                for child_ref in self.dot1dbaseportentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _BRIDGE_MIB as meta
            return meta._meta_table['BridgeMib.Dot1Dbaseporttable']['meta_info']


    class Dot1Dstpporttable(object):
        """
        A table that contains port\-specific information
        for the Spanning Tree Protocol.
        
        .. attribute:: dot1dstpportentry
        
        	A list of information maintained by every port about the Spanning Tree Protocol state for that port
        	**type**\: list of    :py:class:`Dot1Dstpportentry <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dstpporttable.Dot1Dstpportentry>`
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            self.parent = None
            self.dot1dstpportentry = YList()
            self.dot1dstpportentry.parent = self
            self.dot1dstpportentry.name = 'dot1dstpportentry'


        class Dot1Dstpportentry(object):
            """
            A list of information maintained by every port about
            the Spanning Tree Protocol state for that port.
            
            .. attribute:: dot1dstpport  <key>
            
            	The port number of the port for which this entry contains Spanning Tree Protocol management information
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: dot1dstpportdesignatedbridge
            
            	The Bridge Identifier of the bridge that this port considers to be the Designated Bridge for this port's segment
            	**type**\:  str
            
            	**length:** 8
            
            .. attribute:: dot1dstpportdesignatedcost
            
            	The path cost of the Designated Port of the segment connected to this port.  This value is compared to the Root Path Cost field in received bridge PDUs
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dot1dstpportdesignatedport
            
            	The Port Identifier of the port on the Designated Bridge for this port's segment
            	**type**\:  str
            
            	**length:** 2
            
            .. attribute:: dot1dstpportdesignatedroot
            
            	The unique Bridge Identifier of the Bridge recorded as the Root in the Configuration BPDUs transmitted by the Designated Bridge for the segment to which the port is attached
            	**type**\:  str
            
            	**length:** 8
            
            .. attribute:: dot1dstpportenable
            
            	The enabled/disabled status of the port
            	**type**\:   :py:class:`Dot1DstpportenableEnum <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dstpporttable.Dot1Dstpportentry.Dot1DstpportenableEnum>`
            
            .. attribute:: dot1dstpportforwardtransitions
            
            	The number of times this port has transitioned from the Learning state to the Forwarding state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot1dstpportpathcost
            
            	The contribution of this port to the path cost of paths towards the spanning tree root which include this port.  802.1D\-1998 recommends that the default value of this parameter be in inverse proportion to  the speed of the attached LAN.  New implementations should support dot1dStpPortPathCost32. If the port path costs exceeds the maximum value of this object then this object should report the maximum value, namely 65535.  Applications should try to read the dot1dStpPortPathCost32 object if this object reports the maximum value
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: dot1dstpportpathcost32
            
            	The contribution of this port to the path cost of paths towards the spanning tree root which include this port.  802.1D\-1998 recommends that the default value of this parameter be in inverse proportion to the speed of the attached LAN.  This object replaces dot1dStpPortPathCost to support IEEE 802.1t
            	**type**\:  int
            
            	**range:** 1..200000000
            
            .. attribute:: dot1dstpportpriority
            
            	The value of the priority field that is contained in the first (in network byte order) octet of the (2 octet long) Port ID.  The other octet of the Port ID is given by the value of dot1dStpPort. On bridges supporting IEEE 802.1t or IEEE 802.1w, permissible values are 0\-240, in steps of 16
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: dot1dstpportstate
            
            	The port's current state, as defined by application of the Spanning Tree Protocol.  This state controls what action a port takes on reception of a frame.  If the bridge has detected a port that is malfunctioning, it will place that port into the broken(6) state.  For ports that are disabled (see dot1dStpPortEnable), this object will have a value of disabled(1)
            	**type**\:   :py:class:`Dot1DstpportstateEnum <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dstpporttable.Dot1Dstpportentry.Dot1DstpportstateEnum>`
            
            .. attribute:: stpxlongstpportpathcost
            
            	The contribution of this port to the path cost (in 32 bits value) of paths towards the spanning tree root which include this port.  This object is used to configure the spanning tree port path cost in 32 bits value range when the stpxSpanningTreePathCostOperMode is long(2).  If the stpxSpanningTreePathCostOperMode is short(1), this  MIB object is not instantiated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'BRIDGE-MIB'
            _revision = '2005-09-19'

            def __init__(self):
                self.parent = None
                self.dot1dstpport = None
                self.dot1dstpportdesignatedbridge = None
                self.dot1dstpportdesignatedcost = None
                self.dot1dstpportdesignatedport = None
                self.dot1dstpportdesignatedroot = None
                self.dot1dstpportenable = None
                self.dot1dstpportforwardtransitions = None
                self.dot1dstpportpathcost = None
                self.dot1dstpportpathcost32 = None
                self.dot1dstpportpriority = None
                self.dot1dstpportstate = None
                self.stpxlongstpportpathcost = None

            class Dot1DstpportenableEnum(Enum):
                """
                Dot1DstpportenableEnum

                The enabled/disabled status of the port.

                .. data:: enabled = 1

                .. data:: disabled = 2

                """

                enabled = 1

                disabled = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _BRIDGE_MIB as meta
                    return meta._meta_table['BridgeMib.Dot1Dstpporttable.Dot1Dstpportentry.Dot1DstpportenableEnum']


            class Dot1DstpportstateEnum(Enum):
                """
                Dot1DstpportstateEnum

                The port's current state, as defined by application of

                the Spanning Tree Protocol.  This state controls what

                action a port takes on reception of a frame.  If the

                bridge has detected a port that is malfunctioning, it

                will place that port into the broken(6) state.  For

                ports that are disabled (see dot1dStpPortEnable), this

                object will have a value of disabled(1).

                .. data:: disabled = 1

                .. data:: blocking = 2

                .. data:: listening = 3

                .. data:: learning = 4

                .. data:: forwarding = 5

                .. data:: broken = 6

                """

                disabled = 1

                blocking = 2

                listening = 3

                learning = 4

                forwarding = 5

                broken = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _BRIDGE_MIB as meta
                    return meta._meta_table['BridgeMib.Dot1Dstpporttable.Dot1Dstpportentry.Dot1DstpportstateEnum']


            @property
            def _common_path(self):
                if self.dot1dstpport is None:
                    raise YPYModelError('Key property dot1dstpport is None')

                return '/BRIDGE-MIB:BRIDGE-MIB/BRIDGE-MIB:dot1dStpPortTable/BRIDGE-MIB:dot1dStpPortEntry[BRIDGE-MIB:dot1dStpPort = ' + str(self.dot1dstpport) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dot1dstpport is not None:
                    return True

                if self.dot1dstpportdesignatedbridge is not None:
                    return True

                if self.dot1dstpportdesignatedcost is not None:
                    return True

                if self.dot1dstpportdesignatedport is not None:
                    return True

                if self.dot1dstpportdesignatedroot is not None:
                    return True

                if self.dot1dstpportenable is not None:
                    return True

                if self.dot1dstpportforwardtransitions is not None:
                    return True

                if self.dot1dstpportpathcost is not None:
                    return True

                if self.dot1dstpportpathcost32 is not None:
                    return True

                if self.dot1dstpportpriority is not None:
                    return True

                if self.dot1dstpportstate is not None:
                    return True

                if self.stpxlongstpportpathcost is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _BRIDGE_MIB as meta
                return meta._meta_table['BridgeMib.Dot1Dstpporttable.Dot1Dstpportentry']['meta_info']

        @property
        def _common_path(self):

            return '/BRIDGE-MIB:BRIDGE-MIB/BRIDGE-MIB:dot1dStpPortTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dot1dstpportentry is not None:
                for child_ref in self.dot1dstpportentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _BRIDGE_MIB as meta
            return meta._meta_table['BridgeMib.Dot1Dstpporttable']['meta_info']


    class Dot1Dtpfdbtable(object):
        """
        A table that contains information about unicast
        entries for which the bridge has forwarding and/or
        filtering information.  This information is used
        by the transparent bridging function in
        determining how to propagate a received frame.
        
        .. attribute:: dot1dtpfdbentry
        
        	Information about a specific unicast MAC address for which the bridge has some forwarding and/or filtering information
        	**type**\: list of    :py:class:`Dot1Dtpfdbentry <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dtpfdbtable.Dot1Dtpfdbentry>`
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            self.parent = None
            self.dot1dtpfdbentry = YList()
            self.dot1dtpfdbentry.parent = self
            self.dot1dtpfdbentry.name = 'dot1dtpfdbentry'


        class Dot1Dtpfdbentry(object):
            """
            Information about a specific unicast MAC address
            for which the bridge has some forwarding and/or
            filtering information.
            
            .. attribute:: dot1dtpfdbaddress  <key>
            
            	A unicast MAC address for which the bridge has forwarding and/or filtering information
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1dtpfdbport
            
            	Either the value '0', or the port number of the port on which a frame having a source address equal to the value of the corresponding instance of dot1dTpFdbAddress has been seen.  A value of '0' indicates that the port number has not been learned, but that the bridge does have some forwarding/filtering information about this address (e.g., in the dot1dStaticTable).  Implementors are encouraged to assign the port value to this object whenever it is learned, even for addresses for which the corresponding value of dot1dTpFdbStatus is not learned(3)
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: dot1dtpfdbstatus
            
            	The status of this entry.  The meanings of the values are\:     other(1) \- none of the following.  This would         include the case where some other MIB object         (not the corresponding instance of         dot1dTpFdbPort, nor an entry in the         dot1dStaticTable) is being used to determine if         and how frames addressed to the value of the         corresponding instance of dot1dTpFdbAddress are         being forwarded.     invalid(2) \- this entry is no longer valid (e.g.,         it was learned but has since aged out), but has         not yet been flushed from the table.     learned(3) \- the value of the corresponding instance         of dot1dTpFdbPort was learned, and is being         used.     self(4) \- the value of the corresponding instance of         dot1dTpFdbAddress represents one of the bridge's         addresses.  The corresponding instance of         dot1dTpFdbPort indicates which of the bridge's         ports has this address.     mgmt(5) \- the value of the corresponding instance of         dot1dTpFdbAddress is also the value of an         existing instance of dot1dStaticAddress
            	**type**\:   :py:class:`Dot1DtpfdbstatusEnum <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dtpfdbtable.Dot1Dtpfdbentry.Dot1DtpfdbstatusEnum>`
            
            

            """

            _prefix = 'BRIDGE-MIB'
            _revision = '2005-09-19'

            def __init__(self):
                self.parent = None
                self.dot1dtpfdbaddress = None
                self.dot1dtpfdbport = None
                self.dot1dtpfdbstatus = None

            class Dot1DtpfdbstatusEnum(Enum):
                """
                Dot1DtpfdbstatusEnum

                The status of this entry.  The meanings of the

                values are\:

                    other(1) \- none of the following.  This would

                        include the case where some other MIB object

                        (not the corresponding instance of

                        dot1dTpFdbPort, nor an entry in the

                        dot1dStaticTable) is being used to determine if

                        and how frames addressed to the value of the

                        corresponding instance of dot1dTpFdbAddress are

                        being forwarded.

                    invalid(2) \- this entry is no longer valid (e.g.,

                        it was learned but has since aged out), but has

                        not yet been flushed from the table.

                    learned(3) \- the value of the corresponding instance

                        of dot1dTpFdbPort was learned, and is being

                        used.

                    self(4) \- the value of the corresponding instance of

                        dot1dTpFdbAddress represents one of the bridge's

                        addresses.  The corresponding instance of

                        dot1dTpFdbPort indicates which of the bridge's

                        ports has this address.

                    mgmt(5) \- the value of the corresponding instance of

                        dot1dTpFdbAddress is also the value of an

                        existing instance of dot1dStaticAddress.

                .. data:: other = 1

                .. data:: invalid = 2

                .. data:: learned = 3

                .. data:: self = 4

                .. data:: mgmt = 5

                """

                other = 1

                invalid = 2

                learned = 3

                self = 4

                mgmt = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _BRIDGE_MIB as meta
                    return meta._meta_table['BridgeMib.Dot1Dtpfdbtable.Dot1Dtpfdbentry.Dot1DtpfdbstatusEnum']


            @property
            def _common_path(self):
                if self.dot1dtpfdbaddress is None:
                    raise YPYModelError('Key property dot1dtpfdbaddress is None')

                return '/BRIDGE-MIB:BRIDGE-MIB/BRIDGE-MIB:dot1dTpFdbTable/BRIDGE-MIB:dot1dTpFdbEntry[BRIDGE-MIB:dot1dTpFdbAddress = ' + str(self.dot1dtpfdbaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dot1dtpfdbaddress is not None:
                    return True

                if self.dot1dtpfdbport is not None:
                    return True

                if self.dot1dtpfdbstatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _BRIDGE_MIB as meta
                return meta._meta_table['BridgeMib.Dot1Dtpfdbtable.Dot1Dtpfdbentry']['meta_info']

        @property
        def _common_path(self):

            return '/BRIDGE-MIB:BRIDGE-MIB/BRIDGE-MIB:dot1dTpFdbTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dot1dtpfdbentry is not None:
                for child_ref in self.dot1dtpfdbentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _BRIDGE_MIB as meta
            return meta._meta_table['BridgeMib.Dot1Dtpfdbtable']['meta_info']


    class Dot1Dtpporttable(object):
        """
        A table that contains information about every port that
        is associated with this transparent bridge.
        
        .. attribute:: dot1dtpportentry
        
        	A list of information for each port of a transparent bridge
        	**type**\: list of    :py:class:`Dot1Dtpportentry <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dtpporttable.Dot1Dtpportentry>`
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            self.parent = None
            self.dot1dtpportentry = YList()
            self.dot1dtpportentry.parent = self
            self.dot1dtpportentry.name = 'dot1dtpportentry'


        class Dot1Dtpportentry(object):
            """
            A list of information for each port of a transparent
            bridge.
            
            .. attribute:: dot1dtpport  <key>
            
            	The port number of the port for which this entry contains Transparent bridging management information
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: dot1dtpportindiscards
            
            	Count of received valid frames that were discarded (i.e., filtered) by the Forwarding Process
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: dot1dtpportinframes
            
            	The number of frames that have been received by this port from its segment.  Note that a frame received on the interface corresponding to this port is only counted by this object if and only if it is for a protocol being processed by the local bridging function, including bridge management frames
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            .. attribute:: dot1dtpportmaxinfo
            
            	The maximum size of the INFO (non\-MAC) field that  this port will receive or transmit
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: bytes
            
            .. attribute:: dot1dtpportoutframes
            
            	The number of frames that have been transmitted by this port to its segment.  Note that a frame transmitted on the interface corresponding to this port is only counted by this object if and only if it is for a protocol being processed by the local bridging function, including bridge management frames
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: frames
            
            

            """

            _prefix = 'BRIDGE-MIB'
            _revision = '2005-09-19'

            def __init__(self):
                self.parent = None
                self.dot1dtpport = None
                self.dot1dtpportindiscards = None
                self.dot1dtpportinframes = None
                self.dot1dtpportmaxinfo = None
                self.dot1dtpportoutframes = None

            @property
            def _common_path(self):
                if self.dot1dtpport is None:
                    raise YPYModelError('Key property dot1dtpport is None')

                return '/BRIDGE-MIB:BRIDGE-MIB/BRIDGE-MIB:dot1dTpPortTable/BRIDGE-MIB:dot1dTpPortEntry[BRIDGE-MIB:dot1dTpPort = ' + str(self.dot1dtpport) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dot1dtpport is not None:
                    return True

                if self.dot1dtpportindiscards is not None:
                    return True

                if self.dot1dtpportinframes is not None:
                    return True

                if self.dot1dtpportmaxinfo is not None:
                    return True

                if self.dot1dtpportoutframes is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _BRIDGE_MIB as meta
                return meta._meta_table['BridgeMib.Dot1Dtpporttable.Dot1Dtpportentry']['meta_info']

        @property
        def _common_path(self):

            return '/BRIDGE-MIB:BRIDGE-MIB/BRIDGE-MIB:dot1dTpPortTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dot1dtpportentry is not None:
                for child_ref in self.dot1dtpportentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _BRIDGE_MIB as meta
            return meta._meta_table['BridgeMib.Dot1Dtpporttable']['meta_info']


    class Dot1Dstatictable(object):
        """
        A table containing filtering information configured
        into the bridge by (local or network) management
        specifying the set of ports to which frames received
        from specific ports and containing specific destination
        addresses are allowed to be forwarded.  The value of
        zero in this table, as the port number from which frames
        with a specific destination address are received, is
        used to specify all ports for which there is no specific
        entry in this table for that particular destination
        address.  Entries are valid for unicast and for
        group/broadcast addresses.
        
        .. attribute:: dot1dstaticentry
        
        	Filtering information configured into the bridge by (local or network) management specifying the set of ports to which frames received from a specific port and containing a specific destination address are allowed to be forwarded
        	**type**\: list of    :py:class:`Dot1Dstaticentry <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dstatictable.Dot1Dstaticentry>`
        
        

        """

        _prefix = 'BRIDGE-MIB'
        _revision = '2005-09-19'

        def __init__(self):
            self.parent = None
            self.dot1dstaticentry = YList()
            self.dot1dstaticentry.parent = self
            self.dot1dstaticentry.name = 'dot1dstaticentry'


        class Dot1Dstaticentry(object):
            """
            Filtering information configured into the bridge by
            (local or network) management specifying the set of
            ports to which frames received from a specific port and
            containing a specific destination address are allowed to
            be forwarded.
            
            .. attribute:: dot1dstaticaddress  <key>
            
            	The destination MAC address in a frame to which this entry's filtering information applies.  This object can take the value of a unicast address, a group address, or the broadcast address
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot1dstaticreceiveport  <key>
            
            	Either the value '0', or the port number of the port from which a frame must be received in order for this entry's filtering information to apply.  A value of zero indicates that this entry applies on all ports of the bridge for which there is no other applicable entry
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: dot1dstaticallowedtogoto
            
            	The set of ports to which frames received from a specific port and destined for a specific MAC address, are allowed to be forwarded.  Each octet within the value of this object specifies a set of eight ports, with the first octet specifying ports 1 through 8, the second octet specifying ports 9 through 16, etc.  Within each octet, the most significant bit represents the lowest numbered port, and the least significant bit represents the highest numbered port.  Thus, each port of the bridge is represented by a single bit within the value of this object.  If that bit has a value of '1', then that port is included in the set of ports; the port is not included if its bit has a value of '0'.  (Note that the setting of the bit corresponding to the port from which a frame is received is irrelevant.)  The default value of this object is a string of ones of appropriate length.  The value of this object may exceed the required minimum maximum message size of some SNMP transport (484 bytes, in the case of SNMP over UDP, see RFC 3417, section 3.2). SNMP engines on bridges supporting a large number of ports must support appropriate maximum message sizes
            	**type**\:  str
            
            	**length:** 0..512
            
            .. attribute:: dot1dstaticstatus
            
            	This object indicates the status of this entry. The default value is permanent(3).     other(1) \- this entry is currently in use but the         conditions under which it will remain so are         different from each of the following values.     invalid(2) \- writing this value to the object         removes the corresponding entry.     permanent(3) \- this entry is currently in use and         will remain so after the next reset of the         bridge.     deleteOnReset(4) \- this entry is currently in use         and will remain so until the next reset of the         bridge.     deleteOnTimeout(5) \- this entry is currently in use         and will remain so until it is aged out
            	**type**\:   :py:class:`Dot1DstaticstatusEnum <ydk.models.cisco_ios_xe.BRIDGE_MIB.BridgeMib.Dot1Dstatictable.Dot1Dstaticentry.Dot1DstaticstatusEnum>`
            
            

            """

            _prefix = 'BRIDGE-MIB'
            _revision = '2005-09-19'

            def __init__(self):
                self.parent = None
                self.dot1dstaticaddress = None
                self.dot1dstaticreceiveport = None
                self.dot1dstaticallowedtogoto = None
                self.dot1dstaticstatus = None

            class Dot1DstaticstatusEnum(Enum):
                """
                Dot1DstaticstatusEnum

                This object indicates the status of this entry.

                The default value is permanent(3).

                    other(1) \- this entry is currently in use but the

                        conditions under which it will remain so are

                        different from each of the following values.

                    invalid(2) \- writing this value to the object

                        removes the corresponding entry.

                    permanent(3) \- this entry is currently in use and

                        will remain so after the next reset of the

                        bridge.

                    deleteOnReset(4) \- this entry is currently in use

                        and will remain so until the next reset of the

                        bridge.

                    deleteOnTimeout(5) \- this entry is currently in use

                        and will remain so until it is aged out.

                .. data:: other = 1

                .. data:: invalid = 2

                .. data:: permanent = 3

                .. data:: deleteOnReset = 4

                .. data:: deleteOnTimeout = 5

                """

                other = 1

                invalid = 2

                permanent = 3

                deleteOnReset = 4

                deleteOnTimeout = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _BRIDGE_MIB as meta
                    return meta._meta_table['BridgeMib.Dot1Dstatictable.Dot1Dstaticentry.Dot1DstaticstatusEnum']


            @property
            def _common_path(self):
                if self.dot1dstaticaddress is None:
                    raise YPYModelError('Key property dot1dstaticaddress is None')
                if self.dot1dstaticreceiveport is None:
                    raise YPYModelError('Key property dot1dstaticreceiveport is None')

                return '/BRIDGE-MIB:BRIDGE-MIB/BRIDGE-MIB:dot1dStaticTable/BRIDGE-MIB:dot1dStaticEntry[BRIDGE-MIB:dot1dStaticAddress = ' + str(self.dot1dstaticaddress) + '][BRIDGE-MIB:dot1dStaticReceivePort = ' + str(self.dot1dstaticreceiveport) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.dot1dstaticaddress is not None:
                    return True

                if self.dot1dstaticreceiveport is not None:
                    return True

                if self.dot1dstaticallowedtogoto is not None:
                    return True

                if self.dot1dstaticstatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _BRIDGE_MIB as meta
                return meta._meta_table['BridgeMib.Dot1Dstatictable.Dot1Dstaticentry']['meta_info']

        @property
        def _common_path(self):

            return '/BRIDGE-MIB:BRIDGE-MIB/BRIDGE-MIB:dot1dStaticTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.dot1dstaticentry is not None:
                for child_ref in self.dot1dstaticentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _BRIDGE_MIB as meta
            return meta._meta_table['BridgeMib.Dot1Dstatictable']['meta_info']

    @property
    def _common_path(self):

        return '/BRIDGE-MIB:BRIDGE-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.dot1dbase is not None and self.dot1dbase._has_data():
            return True

        if self.dot1dbaseporttable is not None and self.dot1dbaseporttable._has_data():
            return True

        if self.dot1dstatictable is not None and self.dot1dstatictable._has_data():
            return True

        if self.dot1dstp is not None and self.dot1dstp._has_data():
            return True

        if self.dot1dstpporttable is not None and self.dot1dstpporttable._has_data():
            return True

        if self.dot1dtp is not None and self.dot1dtp._has_data():
            return True

        if self.dot1dtpfdbtable is not None and self.dot1dtpfdbtable._has_data():
            return True

        if self.dot1dtpporttable is not None and self.dot1dtpporttable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _BRIDGE_MIB as meta
        return meta._meta_table['BridgeMib']['meta_info']



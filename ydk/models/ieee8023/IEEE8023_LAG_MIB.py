""" IEEE8023_LAG_MIB 

The Link Aggregation module for managing IEEE Std
802.3ad.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.lag.CISCO_LAG_MIB import ClagPortAdminStatus_Enum

class ChurnState_Enum(Enum):
    """
    ChurnState_Enum

    The state of the Churn Detection machine.

    """

    NOCHURN = 1

    CHURN = 2

    CHURNMONITOR = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ieee8023._meta import _IEEE8023_LAG_MIB as meta
        return meta._meta_table['ChurnState_Enum']


class LacpState_Bits(FixedBitsDict):
    """
    LacpState_Bits

    The Actor and Partner State values from the LACPDU.
    Keys are:- collecting , lacpActivity , aggregation , distributing , synchronization , defaulted , lacpTimeout , expired

    """

    def __init__(self):
        self._dictionary = { 
            'collecting':False,
            'lacpActivity':False,
            'aggregation':False,
            'distributing':False,
            'synchronization':False,
            'defaulted':False,
            'lacpTimeout':False,
            'expired':False,
        }
        self._pos_map = { 
            'collecting':4,
            'lacpActivity':0,
            'aggregation':2,
            'distributing':5,
            'synchronization':3,
            'defaulted':6,
            'lacpTimeout':1,
            'expired':7,
        }


class IEEE8023LAGMIB(object):
    """
    
    
    .. attribute:: dot3adaggportdebugtable
    
    	A table that contains Link Aggregation debug information about every port that is associated with this device.  A row appears in this table for each physical port
    	**type**\: :py:class:`Dot3adAggPortDebugTable <ydk.models.ieee8023.IEEE8023_LAG_MIB.IEEE8023LAGMIB.Dot3adAggPortDebugTable>`
    
    .. attribute:: dot3adaggportlisttable
    
    	A table that contains a list of all the ports associated with each Aggregator
    	**type**\: :py:class:`Dot3adAggPortListTable <ydk.models.ieee8023.IEEE8023_LAG_MIB.IEEE8023LAGMIB.Dot3adAggPortListTable>`
    
    .. attribute:: dot3adaggportstatstable
    
    	A table that contains Link Aggregation information about every port that is associated with this device. A row appears in this table for each physical port
    	**type**\: :py:class:`Dot3adAggPortStatsTable <ydk.models.ieee8023.IEEE8023_LAG_MIB.IEEE8023LAGMIB.Dot3adAggPortStatsTable>`
    
    .. attribute:: dot3adaggporttable
    
    	A table that contains Link Aggregation Control configuration information about every Aggregation Port associated with this device. A row appears in this table for each physical port
    	**type**\: :py:class:`Dot3adAggPortTable <ydk.models.ieee8023.IEEE8023_LAG_MIB.IEEE8023LAGMIB.Dot3adAggPortTable>`
    
    .. attribute:: dot3adaggtable
    
    	A table that contains information about every Aggregator that is associated with this System
    	**type**\: :py:class:`Dot3adAggTable <ydk.models.ieee8023.IEEE8023_LAG_MIB.IEEE8023LAGMIB.Dot3adAggTable>`
    
    .. attribute:: lagmibobjects
    
    	
    	**type**\: :py:class:`LagMIBObjects <ydk.models.ieee8023.IEEE8023_LAG_MIB.IEEE8023LAGMIB.LagMIBObjects>`
    
    

    """

    _prefix = 'ieee8023-lag'
    _revision = '2000-06-27'

    def __init__(self):
        self.dot3adaggportdebugtable = IEEE8023LAGMIB.Dot3adAggPortDebugTable()
        self.dot3adaggportdebugtable.parent = self
        self.dot3adaggportlisttable = IEEE8023LAGMIB.Dot3adAggPortListTable()
        self.dot3adaggportlisttable.parent = self
        self.dot3adaggportstatstable = IEEE8023LAGMIB.Dot3adAggPortStatsTable()
        self.dot3adaggportstatstable.parent = self
        self.dot3adaggporttable = IEEE8023LAGMIB.Dot3adAggPortTable()
        self.dot3adaggporttable.parent = self
        self.dot3adaggtable = IEEE8023LAGMIB.Dot3adAggTable()
        self.dot3adaggtable.parent = self
        self.lagmibobjects = IEEE8023LAGMIB.LagMIBObjects()
        self.lagmibobjects.parent = self


    class Dot3adAggPortDebugTable(object):
        """
        A table that contains Link Aggregation debug
        information about every port that is associated with
        this device.  A row appears in this table for each
        physical port.
        
        .. attribute:: dot3adaggportdebugentry
        
        	A list of the debug parameters for a port
        	**type**\: list of :py:class:`Dot3adAggPortDebugEntry <ydk.models.ieee8023.IEEE8023_LAG_MIB.IEEE8023LAGMIB.Dot3adAggPortDebugTable.Dot3adAggPortDebugEntry>`
        
        

        """

        _prefix = 'ieee8023-lag'
        _revision = '2000-06-27'

        def __init__(self):
            self.parent = None
            self.dot3adaggportdebugentry = YList()
            self.dot3adaggportdebugentry.parent = self
            self.dot3adaggportdebugentry.name = 'dot3adaggportdebugentry'


        class Dot3adAggPortDebugEntry(object):
            """
            A list of the debug parameters for a port.
            
            .. attribute:: dot3adaggportindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: dot3adaggportdebugactorchangecount
            
            	Count of the number of times the Actor's perception of the LAG ID for this Aggregation Port has changed. This value is read\-only
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3adaggportdebugactorchurncount
            
            	Count of the number of times the Actor Churn state machine has entered the ACTOR\_CHURN state. This value is read\-only
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3adaggportdebugactorchurnstate
            
            	The state of the Actor Churn Detection machine (43.4.17) for the Aggregation Port. A value of `noChurn' indicates that the state machine is in either the NO\_ACTOR\_CHURN or the ACTOR\_CHURN\_MONITOR state, and `churn' indicates that the state machine is in the ACTOR\_CHURN state. This value is read\-only
            	**type**\: :py:class:`ChurnState_Enum <ydk.models.ieee8023.IEEE8023_LAG_MIB.ChurnState_Enum>`
            
            .. attribute:: dot3adaggportdebugactorsynctransitioncount
            
            	Count of the number of times the Actor's Mux state machine (43.4.15) has entered the IN\_SYNC state. This value is read\-only
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3adaggportdebuglastrxtime
            
            	The value of aTimeSinceSystemReset (F.2.1) when the last LACPDU was received by this Aggregation Port. This value is read\-only
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3adaggportdebugmuxreason
            
            	A human\-readable text string indicating the reason for the most recent change of Mux machine state. This value is read\-only
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: dot3adaggportdebugmuxstate
            
            	This attribute holds the value `detached' if the Mux state machine (43.4.14) for the Aggregation Port is in the DETACHED state, `waiting' if the Mux state machine is in the WAITING state, `attached' if the Mux state machine for the Aggregation Port is in the ATTACHED state, `collecting' if the Mux state machine for the Aggregation Port is in the COLLECTING state, `distributing' if the Mux state machine for the Aggregation Port is in the DISTRIBUTING state, and `collectingDistributing' if the Mux state machine for the Aggregation Port is in the COLLECTING\_DISTRIBUTING state. This value is read\-only
            	**type**\: :py:class:`Dot3adAggPortDebugMuxState_Enum <ydk.models.ieee8023.IEEE8023_LAG_MIB.IEEE8023LAGMIB.Dot3adAggPortDebugTable.Dot3adAggPortDebugEntry.Dot3adAggPortDebugMuxState_Enum>`
            
            .. attribute:: dot3adaggportdebugpartnerchangecount
            
            	Count of the number of times the Partner's perception of the LAG ID (see 43.3.6.1) for this Aggregation Port has changed. This value is read\-only
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3adaggportdebugpartnerchurncount
            
            	Count of the number of times the Partner Churn state machine has entered the PARTNER\_CHURN state. This value is read\-only
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3adaggportdebugpartnerchurnstate
            
            	The state of the Partner Churn Detection machine (43.4.17) for the Aggregation Port. A value of `noChurn' indicates that the state machine is in either the NO\_PARTNER\_CHURN or the PARTNER\_CHURN\_MONITOR state, and `churn' indicates that the state machine is in the PARTNER\_CHURN state. This value is read\-only
            	**type**\: :py:class:`ChurnState_Enum <ydk.models.ieee8023.IEEE8023_LAG_MIB.ChurnState_Enum>`
            
            .. attribute:: dot3adaggportdebugpartnersynctransitioncount
            
            	Count of the number of times the Partner's Mux state machine (43.4.15) has entered the IN\_SYNC state. This value is read\-only
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3adaggportdebugrxstate
            
            	This attribute holds the value `currentRx' if the Receive state machine for the Aggregation Port is in the CURRENT state, `expired' if the Receive state machine is in the EXPIRED state, `defaulted' if the Receive state machine is in the DEFAULTED state, `initialize' if the Receive state machine is in the INITIALIZE state, `lacpDisabled' if the Receive state machine is in the LACP\_DISABLED state, or `portDisabled' if the Receive state machine is in the PORT\_DISABLED state. This value is read\-only
            	**type**\: :py:class:`Dot3adAggPortDebugRxState_Enum <ydk.models.ieee8023.IEEE8023_LAG_MIB.IEEE8023LAGMIB.Dot3adAggPortDebugTable.Dot3adAggPortDebugEntry.Dot3adAggPortDebugRxState_Enum>`
            
            

            """

            _prefix = 'ieee8023-lag'
            _revision = '2000-06-27'

            def __init__(self):
                self.parent = None
                self.dot3adaggportindex = None
                self.dot3adaggportdebugactorchangecount = None
                self.dot3adaggportdebugactorchurncount = None
                self.dot3adaggportdebugactorchurnstate = None
                self.dot3adaggportdebugactorsynctransitioncount = None
                self.dot3adaggportdebuglastrxtime = None
                self.dot3adaggportdebugmuxreason = None
                self.dot3adaggportdebugmuxstate = None
                self.dot3adaggportdebugpartnerchangecount = None
                self.dot3adaggportdebugpartnerchurncount = None
                self.dot3adaggportdebugpartnerchurnstate = None
                self.dot3adaggportdebugpartnersynctransitioncount = None
                self.dot3adaggportdebugrxstate = None

            class Dot3adAggPortDebugMuxState_Enum(Enum):
                """
                Dot3adAggPortDebugMuxState_Enum

                This attribute holds the value `detached' if the Mux
                state machine (43.4.14) for the Aggregation Port is in
                the DETACHED state, `waiting' if the Mux state machine
                is in the WAITING state, `attached' if the Mux state
                machine for the Aggregation Port is in the ATTACHED
                state, `collecting' if the Mux state machine for the
                Aggregation Port is in the COLLECTING state,
                `distributing' if the Mux state machine for the
                Aggregation Port is in the DISTRIBUTING state, and
                `collectingDistributing' if the Mux state machine for
                the Aggregation Port is in the COLLECTING\_DISTRIBUTING
                state. This value is read\-only.

                """

                DETACHED = 1

                WAITING = 2

                ATTACHED = 3

                COLLECTING = 4

                DISTRIBUTING = 5

                COLLECTINGDISTRIBUTING = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.ieee8023._meta import _IEEE8023_LAG_MIB as meta
                    return meta._meta_table['IEEE8023LAGMIB.Dot3adAggPortDebugTable.Dot3adAggPortDebugEntry.Dot3adAggPortDebugMuxState_Enum']


            class Dot3adAggPortDebugRxState_Enum(Enum):
                """
                Dot3adAggPortDebugRxState_Enum

                This attribute holds the value `currentRx' if the
                Receive state machine for the Aggregation Port is in the
                CURRENT state, `expired' if the Receive state machine is
                in the EXPIRED state, `defaulted' if the Receive state
                machine is in the DEFAULTED state, `initialize' if the
                Receive state machine is in the INITIALIZE state,
                `lacpDisabled' if the Receive state machine is in the
                LACP\_DISABLED state, or `portDisabled' if the Receive
                state machine is in the PORT\_DISABLED state.
                This value is read\-only.

                """

                CURRENTRX = 1

                EXPIRED = 2

                DEFAULTED = 3

                INITIALIZE = 4

                LACPDISABLED = 5

                PORTDISABLED = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.ieee8023._meta import _IEEE8023_LAG_MIB as meta
                    return meta._meta_table['IEEE8023LAGMIB.Dot3adAggPortDebugTable.Dot3adAggPortDebugEntry.Dot3adAggPortDebugRxState_Enum']


            @property
            def _common_path(self):
                if self.dot3adaggportindex is None:
                    raise YPYDataValidationError('Key property dot3adaggportindex is None')

                return '/IEEE8023-LAG-MIB:IEEE8023-LAG-MIB/IEEE8023-LAG-MIB:dot3adAggPortDebugTable/IEEE8023-LAG-MIB:dot3adAggPortDebugEntry[IEEE8023-LAG-MIB:dot3adAggPortIndex = ' + str(self.dot3adaggportindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot3adaggportindex is not None:
                    return True

                if self.dot3adaggportdebugactorchangecount is not None:
                    return True

                if self.dot3adaggportdebugactorchurncount is not None:
                    return True

                if self.dot3adaggportdebugactorchurnstate is not None:
                    return True

                if self.dot3adaggportdebugactorsynctransitioncount is not None:
                    return True

                if self.dot3adaggportdebuglastrxtime is not None:
                    return True

                if self.dot3adaggportdebugmuxreason is not None:
                    return True

                if self.dot3adaggportdebugmuxstate is not None:
                    return True

                if self.dot3adaggportdebugpartnerchangecount is not None:
                    return True

                if self.dot3adaggportdebugpartnerchurncount is not None:
                    return True

                if self.dot3adaggportdebugpartnerchurnstate is not None:
                    return True

                if self.dot3adaggportdebugpartnersynctransitioncount is not None:
                    return True

                if self.dot3adaggportdebugrxstate is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ieee8023._meta import _IEEE8023_LAG_MIB as meta
                return meta._meta_table['IEEE8023LAGMIB.Dot3adAggPortDebugTable.Dot3adAggPortDebugEntry']['meta_info']

        @property
        def _common_path(self):

            return '/IEEE8023-LAG-MIB:IEEE8023-LAG-MIB/IEEE8023-LAG-MIB:dot3adAggPortDebugTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot3adaggportdebugentry is not None:
                for child_ref in self.dot3adaggportdebugentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8023._meta import _IEEE8023_LAG_MIB as meta
            return meta._meta_table['IEEE8023LAGMIB.Dot3adAggPortDebugTable']['meta_info']


    class Dot3adAggPortListTable(object):
        """
        A table that contains a list of all the ports
        associated with each Aggregator.
        
        .. attribute:: dot3adaggportlistentry
        
        	A list of the ports associated with a given Aggregator. This is indexed by the ifIndex of the Aggregator
        	**type**\: list of :py:class:`Dot3adAggPortListEntry <ydk.models.ieee8023.IEEE8023_LAG_MIB.IEEE8023LAGMIB.Dot3adAggPortListTable.Dot3adAggPortListEntry>`
        
        

        """

        _prefix = 'ieee8023-lag'
        _revision = '2000-06-27'

        def __init__(self):
            self.parent = None
            self.dot3adaggportlistentry = YList()
            self.dot3adaggportlistentry.parent = self
            self.dot3adaggportlistentry.name = 'dot3adaggportlistentry'


        class Dot3adAggPortListEntry(object):
            """
            A list of the ports associated with a given Aggregator.
            This is indexed by the ifIndex of the Aggregator.
            
            .. attribute:: dot3adaggindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: clagaggportlistports
            
            	This object contains a list of ports currently associated with this Aggregator in the format of '[number\_of\_ports][cieIfDot1dBaseMappingPort1][...]  [cieIfDot1dBaseMappingPortn]'  where [number\_of\_ports] is of size 2 octet and indicates the number of ports contains in this object. It also indicates the number of cieIfDot1dBaseMappingPort field following this field.   [cieIfDot1dBaseMappingPort'n'] is the value of  cieIfDot1dBaseMappingPort of the 'n' port associated with this Aggregation and has size of 2 octets where n is up to [number\_of\_ports]
            	**type**\: str
            
            	**range:** 2..256
            
            .. attribute:: dot3adaggportlistports
            
            	The complete set of ports currently associated with this Aggregator.  Each bit set in this list represents an Actor Port member of this Link Aggregation
            	**type**\: str
            
            

            """

            _prefix = 'ieee8023-lag'
            _revision = '2000-06-27'

            def __init__(self):
                self.parent = None
                self.dot3adaggindex = None
                self.clagaggportlistports = None
                self.dot3adaggportlistports = None

            @property
            def _common_path(self):
                if self.dot3adaggindex is None:
                    raise YPYDataValidationError('Key property dot3adaggindex is None')

                return '/IEEE8023-LAG-MIB:IEEE8023-LAG-MIB/IEEE8023-LAG-MIB:dot3adAggPortListTable/IEEE8023-LAG-MIB:dot3adAggPortListEntry[IEEE8023-LAG-MIB:dot3adAggIndex = ' + str(self.dot3adaggindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot3adaggindex is not None:
                    return True

                if self.clagaggportlistports is not None:
                    return True

                if self.dot3adaggportlistports is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ieee8023._meta import _IEEE8023_LAG_MIB as meta
                return meta._meta_table['IEEE8023LAGMIB.Dot3adAggPortListTable.Dot3adAggPortListEntry']['meta_info']

        @property
        def _common_path(self):

            return '/IEEE8023-LAG-MIB:IEEE8023-LAG-MIB/IEEE8023-LAG-MIB:dot3adAggPortListTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot3adaggportlistentry is not None:
                for child_ref in self.dot3adaggportlistentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8023._meta import _IEEE8023_LAG_MIB as meta
            return meta._meta_table['IEEE8023LAGMIB.Dot3adAggPortListTable']['meta_info']


    class Dot3adAggPortStatsTable(object):
        """
        A table that contains Link Aggregation information
        about every port that is associated with this device.
        A row appears in this table for each physical port.
        
        .. attribute:: dot3adaggportstatsentry
        
        	A list of Link Aggregation Control Protocol statistics for each port on this device
        	**type**\: list of :py:class:`Dot3adAggPortStatsEntry <ydk.models.ieee8023.IEEE8023_LAG_MIB.IEEE8023LAGMIB.Dot3adAggPortStatsTable.Dot3adAggPortStatsEntry>`
        
        

        """

        _prefix = 'ieee8023-lag'
        _revision = '2000-06-27'

        def __init__(self):
            self.parent = None
            self.dot3adaggportstatsentry = YList()
            self.dot3adaggportstatsentry.parent = self
            self.dot3adaggportstatsentry.name = 'dot3adaggportstatsentry'


        class Dot3adAggPortStatsEntry(object):
            """
            A list of Link Aggregation Control Protocol statistics
            for each port on this device.
            
            .. attribute:: dot3adaggportindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: dot3adaggportstatsillegalrx
            
            	The number of frames received that carry the Slow Protocols Ethernet Type value (43B.4), but contain a badly formed PDU or an illegal value of Protocol Subtype (43B.4). This value is read\-only
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3adaggportstatslacpdusrx
            
            	The number of valid LACPDUs received on this Aggregation Port. This value is read\-only
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3adaggportstatslacpdustx
            
            	The number of LACPDUs transmitted on this Aggregation Port. This value is read\-only
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3adaggportstatsmarkerpdusrx
            
            	The number of valid Marker PDUs received on this Aggregation Port. This value is read\-only
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3adaggportstatsmarkerpdustx
            
            	The number of Marker PDUs transmitted on this Aggregation Port. This value is read\-only
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3adaggportstatsmarkerresponsepdusrx
            
            	The number of valid Marker Response PDUs received on this Aggregation Port. This value is read\-only
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3adaggportstatsmarkerresponsepdustx
            
            	The number of Marker Response PDUs transmitted on this Aggregation Port. This value is read\-only
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: dot3adaggportstatsunknownrx
            
            	The number of frames received that either\: \- carry the Slow Protocols Ethernet Type value (43B.4),   but contain an unknown PDU,  or\: \- are addressed to the Slow Protocols group MAC   Address (43B.3), but do not carry the Slow Protocols   Ethernet Type. This value is read\-only
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'ieee8023-lag'
            _revision = '2000-06-27'

            def __init__(self):
                self.parent = None
                self.dot3adaggportindex = None
                self.dot3adaggportstatsillegalrx = None
                self.dot3adaggportstatslacpdusrx = None
                self.dot3adaggportstatslacpdustx = None
                self.dot3adaggportstatsmarkerpdusrx = None
                self.dot3adaggportstatsmarkerpdustx = None
                self.dot3adaggportstatsmarkerresponsepdusrx = None
                self.dot3adaggportstatsmarkerresponsepdustx = None
                self.dot3adaggportstatsunknownrx = None

            @property
            def _common_path(self):
                if self.dot3adaggportindex is None:
                    raise YPYDataValidationError('Key property dot3adaggportindex is None')

                return '/IEEE8023-LAG-MIB:IEEE8023-LAG-MIB/IEEE8023-LAG-MIB:dot3adAggPortStatsTable/IEEE8023-LAG-MIB:dot3adAggPortStatsEntry[IEEE8023-LAG-MIB:dot3adAggPortIndex = ' + str(self.dot3adaggportindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot3adaggportindex is not None:
                    return True

                if self.dot3adaggportstatsillegalrx is not None:
                    return True

                if self.dot3adaggportstatslacpdusrx is not None:
                    return True

                if self.dot3adaggportstatslacpdustx is not None:
                    return True

                if self.dot3adaggportstatsmarkerpdusrx is not None:
                    return True

                if self.dot3adaggportstatsmarkerpdustx is not None:
                    return True

                if self.dot3adaggportstatsmarkerresponsepdusrx is not None:
                    return True

                if self.dot3adaggportstatsmarkerresponsepdustx is not None:
                    return True

                if self.dot3adaggportstatsunknownrx is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ieee8023._meta import _IEEE8023_LAG_MIB as meta
                return meta._meta_table['IEEE8023LAGMIB.Dot3adAggPortStatsTable.Dot3adAggPortStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/IEEE8023-LAG-MIB:IEEE8023-LAG-MIB/IEEE8023-LAG-MIB:dot3adAggPortStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot3adaggportstatsentry is not None:
                for child_ref in self.dot3adaggportstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8023._meta import _IEEE8023_LAG_MIB as meta
            return meta._meta_table['IEEE8023LAGMIB.Dot3adAggPortStatsTable']['meta_info']


    class Dot3adAggPortTable(object):
        """
        A table that contains Link Aggregation Control
        configuration information about every
        Aggregation Port associated with this device.
        A row appears in this table for each physical port.
        
        .. attribute:: dot3adaggportentry
        
        	A list of Link Aggregation Control configuration parameters for each Aggregation Port on this device
        	**type**\: list of :py:class:`Dot3adAggPortEntry <ydk.models.ieee8023.IEEE8023_LAG_MIB.IEEE8023LAGMIB.Dot3adAggPortTable.Dot3adAggPortEntry>`
        
        

        """

        _prefix = 'ieee8023-lag'
        _revision = '2000-06-27'

        def __init__(self):
            self.parent = None
            self.dot3adaggportentry = YList()
            self.dot3adaggportentry.parent = self
            self.dot3adaggportentry.name = 'dot3adaggportentry'


        class Dot3adAggPortEntry(object):
            """
            A list of Link Aggregation Control configuration
            parameters for each Aggregation Port on this device.
            
            .. attribute:: dot3adaggportindex
            
            	The ifIndex of the port
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: clagaggportadminstatus
            
            	The administrative status of the LACP protocol on this aggregation port
            	**type**\: :py:class:`ClagPortAdminStatus_Enum <ydk.models.lag.CISCO_LAG_MIB.ClagPortAdminStatus_Enum>`
            
            .. attribute:: clagaggportrate
            
            	Specifies the requested exchange rate of LACP packets on this interface. fast(1)  \:    The device requests its peers to send LACP packets                at fast rate to this interface. normal(2)\:    The decice requests its peers to send LACP packets               at normal rate to this interface
            	**type**\: :py:class:`ClagAggPortRate_Enum <ydk.models.ieee8023.IEEE8023_LAG_MIB.IEEE8023LAGMIB.Dot3adAggPortTable.Dot3adAggPortEntry.ClagAggPortRate_Enum>`
            
            .. attribute:: dot3adaggportactoradminkey
            
            	The current administrative value of the Key for the Aggregation Port. This is a 16\-bit read\-write value. The meaning of particular Key values is of local significance
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: dot3adaggportactoradminstate
            
            	A string of 8 bits, corresponding to the administrative values of Actor\_State (43.4.2) as transmitted by the Actor in LACPDUs. The first bit corresponds to bit 0 of Actor\_State (LACP\_Activity), the second bit corresponds to bit 1 (LACP\_Timeout), the third bit corresponds to bit 2 (Aggregation), the fourth bit corresponds to bit 3 (Synchronization), the fifth bit corresponds to bit 4 (Collecting), the sixth bit corresponds to bit 5 (Distributing), the seventh bit corresponds to bit 6 (Defaulted), and the eighth bit corresponds to bit 7 (Expired). These values allow administrative control over the values of LACP\_Activity, LACP\_Timeout and Aggregation. This attribute value is read\-write
            	**type**\: :py:class:`LacpState_Bits <ydk.models.ieee8023.IEEE8023_LAG_MIB.LacpState_Bits>`
            
            .. attribute:: dot3adaggportactoroperkey
            
            	The current operational value of the Key for the Aggregation Port. This is a 16\-bit read\-only value. The meaning of particular Key values is of local significance
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: dot3adaggportactoroperstate
            
            	A string of 8 bits, corresponding to the current operational values of Actor\_State as transmitted by the Actor in LACPDUs. The bit allocations are as defined in 30.7.2.1.20. This attribute value is read\-only
            	**type**\: :py:class:`LacpState_Bits <ydk.models.ieee8023.IEEE8023_LAG_MIB.LacpState_Bits>`
            
            .. attribute:: dot3adaggportactorport
            
            	The port number locally assigned to the Aggregation Port. The port number is communicated in LACPDUs as the Actor\_Port. This value is read\-only
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: dot3adaggportactorportpriority
            
            	The priority value assigned to this Aggregation Port. This 16\-bit value is read\-write
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: dot3adaggportactorsystemid
            
            	A 6\-octet read\-only MAC address value that defines the value of the System ID for the System that contains this Aggregation Port
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot3adaggportactorsystempriority
            
            	A 2\-octet read\-write value used to define the priority value associated with the Actor's System ID
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: dot3adaggportaggregateorindividual
            
            	A read\-only Boolean value indicating whether the Aggregation Port is able to Aggregate (`TRUE') or is only able to operate as an Individual link (`FALSE')
            	**type**\: bool
            
            .. attribute:: dot3adaggportattachedaggid
            
            	The identifier value of the Aggregator that this Aggregation Port is currently attached to. Zero indicates that the Aggregation Port is not currently attached to an Aggregator.  This value is read\-only
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: dot3adaggportpartneradminkey
            
            	The current administrative value of the Key for the protocol Partner. This is a 16\-bit read\-write value. The assigned value is used, along with the value of aAggPortPartnerAdminSystemPriority, aAggPortPartnerAdminSystemID, aAggPortPartnerAdminPort, and aAggPortPartnerAdminPortPriority, in order to achieve manually configured aggregation
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: dot3adaggportpartneradminport
            
            	The current administrative value of the port number for the protocol Partner. This is a 16\-bit read\-write value. The assigned value is used, along with the value of aAggPortPartnerAdminSystemPriority, aAggPortPartnerAdminSystemID, aAggPortPartnerAdminKey, and aAggPortPartnerAdminPortPriority, in order to achieve manually configured aggregation
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: dot3adaggportpartneradminportpriority
            
            	The current administrative value of the port priority for the protocol Partner. This is a 16\-bit read\-write value. The assigned value is used, along with the value of aAggPortPartnerAdminSystemPriority, aAggPortPartnerAdminSystemID, aAggPortPartnerAdminKey, and aAggPortPartnerAdminPort, in order to achieve manually configured aggregation
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: dot3adaggportpartneradminstate
            
            	A string of 8 bits, corresponding to the current administrative value of Actor\_State for the protocol Partner. The bit allocations are as defined in 30.7.2.1.20. This attribute value is read\-write. The assigned value is used in order to achieve manually configured aggregation
            	**type**\: :py:class:`LacpState_Bits <ydk.models.ieee8023.IEEE8023_LAG_MIB.LacpState_Bits>`
            
            .. attribute:: dot3adaggportpartneradminsystemid
            
            	A 6\-octet read\-write MACAddress value representing the administrative value of the Aggregation Port's protocol Partner's System ID. The assigned value is used, along with the value of aAggPortPartnerAdminSystemPriority, aAggPortPartnerAdminKey, aAggPortPartnerAdminPort, and aAggPortPartnerAdminPortPriority, in order to achieve manually configured aggregation
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot3adaggportpartneradminsystempriority
            
            	A 2\-octet read\-write value used to define the administrative value of priority associated with the Partner's System ID. The assigned value is used, along with the value of aAggPortPartnerAdminSystemID, aAggPortPartnerAdminKey, aAggPortPartnerAdminPort, and aAggPortPartnerAdminPortPriority, in order to achieve manually configured aggregation
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: dot3adaggportpartneroperkey
            
            	The current operational value of the Key for the protocol Partner. The value of this attribute may contain the manually configured value carried in aAggPortPartnerAdminKey if there is no protocol Partner. This is a 16\-bit read\-only value
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: dot3adaggportpartneroperport
            
            	The operational port number assigned to this Aggregation Port by the Aggregation Port's protocol Partner. The value of this attribute may contain the manually configured value carried in aAggPortPartnerAdminPort if there is no protocol Partner. This 16\-bit value is read\-only
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: dot3adaggportpartneroperportpriority
            
            	The priority value assigned to this Aggregation Port by the Partner. The value of this attribute may contain the manually configured value carried in aAggPortPartnerAdminPortPriority if there is no protocol Partner. This 16\-bit value is read\-only
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: dot3adaggportpartneroperstate
            
            	A string of 8 bits, corresponding to the current values of Actor\_State in the most recently received LACPDU transmitted by the protocol Partner. The bit allocations are as defined in 30.7.2.1.20. In the absence of an active protocol Partner, this value may reflect the manually configured value aAggPortPartnerAdminState. This attribute value is read\-only
            	**type**\: :py:class:`LacpState_Bits <ydk.models.ieee8023.IEEE8023_LAG_MIB.LacpState_Bits>`
            
            .. attribute:: dot3adaggportpartneropersystemid
            
            	A 6\-octet read\-only MACAddress value representing the current value of the Aggregation Port's protocol Partner's System ID. A value of zero indicates that there is no known protocol Partner. The value of this attribute may contain the manually configured value carried in aAggPortPartnerAdminSystemID if there is no protocol Partner
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot3adaggportpartneropersystempriority
            
            	A 2\-octet read\-only value indicating the operational value of priority associated with the Partner's System ID. The value of this attribute may contain the manually configured value carried in aAggPortPartnerAdminSystemPriority if there is no protocol Partner
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: dot3adaggportselectedaggid
            
            	The identifier value of the Aggregator that this Aggregation Port has currently selected. Zero indicates that the Aggregation Port has not selected an Aggregator, either because it is in the process of detaching from an Aggregator or because there is no suitable Aggregator available for it to select. This value is read\-only
            	**type**\: int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'ieee8023-lag'
            _revision = '2000-06-27'

            def __init__(self):
                self.parent = None
                self.dot3adaggportindex = None
                self.clagaggportadminstatus = None
                self.clagaggportrate = None
                self.dot3adaggportactoradminkey = None
                self.dot3adaggportactoradminstate = LacpState_Bits()
                self.dot3adaggportactoroperkey = None
                self.dot3adaggportactoroperstate = LacpState_Bits()
                self.dot3adaggportactorport = None
                self.dot3adaggportactorportpriority = None
                self.dot3adaggportactorsystemid = None
                self.dot3adaggportactorsystempriority = None
                self.dot3adaggportaggregateorindividual = None
                self.dot3adaggportattachedaggid = None
                self.dot3adaggportpartneradminkey = None
                self.dot3adaggportpartneradminport = None
                self.dot3adaggportpartneradminportpriority = None
                self.dot3adaggportpartneradminstate = LacpState_Bits()
                self.dot3adaggportpartneradminsystemid = None
                self.dot3adaggportpartneradminsystempriority = None
                self.dot3adaggportpartneroperkey = None
                self.dot3adaggportpartneroperport = None
                self.dot3adaggportpartneroperportpriority = None
                self.dot3adaggportpartneroperstate = LacpState_Bits()
                self.dot3adaggportpartneropersystemid = None
                self.dot3adaggportpartneropersystempriority = None
                self.dot3adaggportselectedaggid = None

            class ClagAggPortRate_Enum(Enum):
                """
                ClagAggPortRate_Enum

                Specifies the requested exchange rate of LACP packets
                on this interface.
                fast(1)  \:    The device requests its peers to send LACP packets 
                              at fast rate to this interface.
                normal(2)\:    The decice requests its peers to send LACP packets
                              at normal rate to this interface.

                """

                FAST = 1

                NORMAL = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.ieee8023._meta import _IEEE8023_LAG_MIB as meta
                    return meta._meta_table['IEEE8023LAGMIB.Dot3adAggPortTable.Dot3adAggPortEntry.ClagAggPortRate_Enum']


            @property
            def _common_path(self):
                if self.dot3adaggportindex is None:
                    raise YPYDataValidationError('Key property dot3adaggportindex is None')

                return '/IEEE8023-LAG-MIB:IEEE8023-LAG-MIB/IEEE8023-LAG-MIB:dot3adAggPortTable/IEEE8023-LAG-MIB:dot3adAggPortEntry[IEEE8023-LAG-MIB:dot3adAggPortIndex = ' + str(self.dot3adaggportindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot3adaggportindex is not None:
                    return True

                if self.clagaggportadminstatus is not None:
                    return True

                if self.clagaggportrate is not None:
                    return True

                if self.dot3adaggportactoradminkey is not None:
                    return True

                if self.dot3adaggportactoradminstate is not None:
                    if self.dot3adaggportactoradminstate._has_data():
                        return True

                if self.dot3adaggportactoroperkey is not None:
                    return True

                if self.dot3adaggportactoroperstate is not None:
                    if self.dot3adaggportactoroperstate._has_data():
                        return True

                if self.dot3adaggportactorport is not None:
                    return True

                if self.dot3adaggportactorportpriority is not None:
                    return True

                if self.dot3adaggportactorsystemid is not None:
                    return True

                if self.dot3adaggportactorsystempriority is not None:
                    return True

                if self.dot3adaggportaggregateorindividual is not None:
                    return True

                if self.dot3adaggportattachedaggid is not None:
                    return True

                if self.dot3adaggportpartneradminkey is not None:
                    return True

                if self.dot3adaggportpartneradminport is not None:
                    return True

                if self.dot3adaggportpartneradminportpriority is not None:
                    return True

                if self.dot3adaggportpartneradminstate is not None:
                    if self.dot3adaggportpartneradminstate._has_data():
                        return True

                if self.dot3adaggportpartneradminsystemid is not None:
                    return True

                if self.dot3adaggportpartneradminsystempriority is not None:
                    return True

                if self.dot3adaggportpartneroperkey is not None:
                    return True

                if self.dot3adaggportpartneroperport is not None:
                    return True

                if self.dot3adaggportpartneroperportpriority is not None:
                    return True

                if self.dot3adaggportpartneroperstate is not None:
                    if self.dot3adaggportpartneroperstate._has_data():
                        return True

                if self.dot3adaggportpartneropersystemid is not None:
                    return True

                if self.dot3adaggportpartneropersystempriority is not None:
                    return True

                if self.dot3adaggportselectedaggid is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ieee8023._meta import _IEEE8023_LAG_MIB as meta
                return meta._meta_table['IEEE8023LAGMIB.Dot3adAggPortTable.Dot3adAggPortEntry']['meta_info']

        @property
        def _common_path(self):

            return '/IEEE8023-LAG-MIB:IEEE8023-LAG-MIB/IEEE8023-LAG-MIB:dot3adAggPortTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot3adaggportentry is not None:
                for child_ref in self.dot3adaggportentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8023._meta import _IEEE8023_LAG_MIB as meta
            return meta._meta_table['IEEE8023LAGMIB.Dot3adAggPortTable']['meta_info']


    class Dot3adAggTable(object):
        """
        A table that contains information about every
        Aggregator that is associated with this System.
        
        .. attribute:: dot3adaggentry
        
        	A list of the Aggregator parameters. This is indexed by the ifIndex of the Aggregator
        	**type**\: list of :py:class:`Dot3adAggEntry <ydk.models.ieee8023.IEEE8023_LAG_MIB.IEEE8023LAGMIB.Dot3adAggTable.Dot3adAggEntry>`
        
        

        """

        _prefix = 'ieee8023-lag'
        _revision = '2000-06-27'

        def __init__(self):
            self.parent = None
            self.dot3adaggentry = YList()
            self.dot3adaggentry.parent = self
            self.dot3adaggentry.name = 'dot3adaggentry'


        class Dot3adAggEntry(object):
            """
            A list of the Aggregator parameters. This is indexed
            by the ifIndex of the Aggregator.
            
            .. attribute:: dot3adaggindex
            
            	The unique identifier allocated to this Aggregator by the local System.  This attribute identifies an Aggregator instance among the subordinate managed objects of the containing object. This value is read\-only
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: dot3adaggactoradminkey
            
            	The current administrative value of the Key for the Aggregator. The administrative Key value may differ from the operational Key value for the reasons discussed in 43.6.2. This is a 16\-bit, read\-write value. The meaning of particular Key values is of local significance
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: dot3adaggactoroperkey
            
            	The current operational value of the Key for the Aggregator. The administrative Key value may differ from the operational Key value for the reasons discussed in 43.6.2.  This is a 16\-bit read\-only value. The meaning of particular Key values is of local significance
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: dot3adaggactorsystemid
            
            	A 6\-octet read\-write MAC address value used as a unique identifier for the System that contains this Aggregator. NOTE\-From the perspective of the Link Aggregation mechanisms described in Clause 43, only a single combination of Actor's System ID and System Priority are considered, and no distinction is made between the values of these parameters for an Aggregator and the port(s) that are associated with it; i.e., the protocol is described in terms of the operation of aggregation within a single System. However, the managed objects provided for the Aggregator and the port both allow management of these parameters. The result of this is to permit a single piece of equipment to be configured by management to contain more than one System from the point of view of the operation of Link Aggregation. This may be of particular use in the configuration of equipment that has limited aggregation capability (see 43.6)
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot3adaggactorsystempriority
            
            	A 2\-octet read\-write value indicating the priority value associated with the Actor's System ID
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: dot3adaggaggregateorindividual
            
            	A read\-only Boolean value indicating whether the Aggregator represents an Aggregate (`TRUE') or an Individual link (`FALSE')
            	**type**\: bool
            
            .. attribute:: dot3adaggcollectormaxdelay
            
            	The value of this 16\-bit read\-write attribute defines the maximum delay, in tens of microseconds, that may be imposed by the Frame Collector between receiving a frame from an Aggregator Parser, and either delivering the frame to its MAC Client or discarding the frame (see 43.2.3.1.1)
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: dot3adaggmacaddress
            
            	A 6\-octet read\-only value carrying the individual MAC address assigned to the Aggregator
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot3adaggpartneroperkey
            
            	The current operational value of the Key for the Aggregator's current protocol Partner. This is a 16\-bit read\-only value. If the aggregation is manually configured, this Key value will be a value assigned by the local System
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: dot3adaggpartnersystemid
            
            	A 6\-octet read\-only MAC address value consisting of the unique identifier for the current protocol Partner of this Aggregator. A value of zero indicates that there is no known Partner. If the aggregation is manually configured, this System ID value will be a value assigned by the local System
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: dot3adaggpartnersystempriority
            
            	A 2\-octet read\-only value that indicates the priority value associated with the Partner's System ID. If the aggregation is manually configured, this System Priority value will be a value assigned by the local System
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'ieee8023-lag'
            _revision = '2000-06-27'

            def __init__(self):
                self.parent = None
                self.dot3adaggindex = None
                self.dot3adaggactoradminkey = None
                self.dot3adaggactoroperkey = None
                self.dot3adaggactorsystemid = None
                self.dot3adaggactorsystempriority = None
                self.dot3adaggaggregateorindividual = None
                self.dot3adaggcollectormaxdelay = None
                self.dot3adaggmacaddress = None
                self.dot3adaggpartneroperkey = None
                self.dot3adaggpartnersystemid = None
                self.dot3adaggpartnersystempriority = None

            @property
            def _common_path(self):
                if self.dot3adaggindex is None:
                    raise YPYDataValidationError('Key property dot3adaggindex is None')

                return '/IEEE8023-LAG-MIB:IEEE8023-LAG-MIB/IEEE8023-LAG-MIB:dot3adAggTable/IEEE8023-LAG-MIB:dot3adAggEntry[IEEE8023-LAG-MIB:dot3adAggIndex = ' + str(self.dot3adaggindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.dot3adaggindex is not None:
                    return True

                if self.dot3adaggactoradminkey is not None:
                    return True

                if self.dot3adaggactoroperkey is not None:
                    return True

                if self.dot3adaggactorsystemid is not None:
                    return True

                if self.dot3adaggactorsystempriority is not None:
                    return True

                if self.dot3adaggaggregateorindividual is not None:
                    return True

                if self.dot3adaggcollectormaxdelay is not None:
                    return True

                if self.dot3adaggmacaddress is not None:
                    return True

                if self.dot3adaggpartneroperkey is not None:
                    return True

                if self.dot3adaggpartnersystemid is not None:
                    return True

                if self.dot3adaggpartnersystempriority is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ieee8023._meta import _IEEE8023_LAG_MIB as meta
                return meta._meta_table['IEEE8023LAGMIB.Dot3adAggTable.Dot3adAggEntry']['meta_info']

        @property
        def _common_path(self):

            return '/IEEE8023-LAG-MIB:IEEE8023-LAG-MIB/IEEE8023-LAG-MIB:dot3adAggTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot3adaggentry is not None:
                for child_ref in self.dot3adaggentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8023._meta import _IEEE8023_LAG_MIB as meta
            return meta._meta_table['IEEE8023LAGMIB.Dot3adAggTable']['meta_info']


    class LagMIBObjects(object):
        """
        
        
        .. attribute:: dot3adtableslastchanged
        
        	This object indicates the time of the most recent change to the dot3adAggTable, dot3adAggPortListTable, or dot3adAggPortTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'ieee8023-lag'
        _revision = '2000-06-27'

        def __init__(self):
            self.parent = None
            self.dot3adtableslastchanged = None

        @property
        def _common_path(self):

            return '/IEEE8023-LAG-MIB:IEEE8023-LAG-MIB/IEEE8023-LAG-MIB:lagMIBObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.dot3adtableslastchanged is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ieee8023._meta import _IEEE8023_LAG_MIB as meta
            return meta._meta_table['IEEE8023LAGMIB.LagMIBObjects']['meta_info']

    @property
    def _common_path(self):

        return '/IEEE8023-LAG-MIB:IEEE8023-LAG-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.dot3adaggportdebugtable is not None and self.dot3adaggportdebugtable._has_data():
            return True

        if self.dot3adaggportdebugtable is not None and self.dot3adaggportdebugtable.is_presence():
            return True

        if self.dot3adaggportlisttable is not None and self.dot3adaggportlisttable._has_data():
            return True

        if self.dot3adaggportlisttable is not None and self.dot3adaggportlisttable.is_presence():
            return True

        if self.dot3adaggportstatstable is not None and self.dot3adaggportstatstable._has_data():
            return True

        if self.dot3adaggportstatstable is not None and self.dot3adaggportstatstable.is_presence():
            return True

        if self.dot3adaggporttable is not None and self.dot3adaggporttable._has_data():
            return True

        if self.dot3adaggporttable is not None and self.dot3adaggporttable.is_presence():
            return True

        if self.dot3adaggtable is not None and self.dot3adaggtable._has_data():
            return True

        if self.dot3adaggtable is not None and self.dot3adaggtable.is_presence():
            return True

        if self.lagmibobjects is not None and self.lagmibobjects._has_data():
            return True

        if self.lagmibobjects is not None and self.lagmibobjects.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ieee8023._meta import _IEEE8023_LAG_MIB as meta
        return meta._meta_table['IEEE8023LAGMIB']['meta_info']



""" TOKEN_RING_RMON_MIB 


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class EntryStatus_Enum(Enum):
    """
    EntryStatus_Enum

    """

    VALID = 1

    CREATEREQUEST = 2

    UNDERCREATION = 3

    INVALID = 4


    @staticmethod
    def _meta_info():
        from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
        return meta._meta_table['EntryStatus_Enum']



class TOKENRINGRMONMIB(object):
    """
    
    
    .. attribute:: ringstationconfigcontroltable
    
    	A list of ring station configuration control entries
    	**type**\: :py:class:`RingStationConfigControlTable <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationConfigControlTable>`
    
    .. attribute:: ringstationconfigtable
    
    	A list of configuration entries for stations on a ring monitored by this probe
    	**type**\: :py:class:`RingStationConfigTable <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationConfigTable>`
    
    .. attribute:: ringstationcontroltable
    
    	A list of ringStation table control entries
    	**type**\: :py:class:`RingStationControlTable <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationControlTable>`
    
    .. attribute:: ringstationordertable
    
    	A list of ring station entries for stations in the ring poll, ordered by their ring\-order
    	**type**\: :py:class:`RingStationOrderTable <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationOrderTable>`
    
    .. attribute:: ringstationtable
    
    	A list of ring station entries.  An entry will exist for each station that is now or has      previously been detected as physically present on this ring
    	**type**\: :py:class:`RingStationTable <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationTable>`
    
    .. attribute:: sourceroutingstatstable
    
    	A list of source routing statistics entries
    	**type**\: :py:class:`SourceRoutingStatsTable <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.SourceRoutingStatsTable>`
    
    .. attribute:: tokenringmlhistorytable
    
    	A list of Mac\-Layer Token Ring statistics      entries
    	**type**\: :py:class:`TokenRingMLHistoryTable <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.TokenRingMLHistoryTable>`
    
    .. attribute:: tokenringmlstatstable
    
    	A list of Mac\-Layer Token Ring statistics      entries
    	**type**\: :py:class:`TokenRingMLStatsTable <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.TokenRingMLStatsTable>`
    
    .. attribute:: tokenringphistorytable
    
    	A list of promiscuous Token Ring statistics entries
    	**type**\: :py:class:`TokenRingPHistoryTable <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.TokenRingPHistoryTable>`
    
    .. attribute:: tokenringpstatstable
    
    	A list of promiscuous Token Ring statistics entries
    	**type**\: :py:class:`TokenRingPStatsTable <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.TokenRingPStatsTable>`
    
    

    """

    _prefix = 'token-ring'

    def __init__(self):
        self.ringstationconfigcontroltable = TOKENRINGRMONMIB.RingStationConfigControlTable()
        self.ringstationconfigcontroltable.parent = self
        self.ringstationconfigtable = TOKENRINGRMONMIB.RingStationConfigTable()
        self.ringstationconfigtable.parent = self
        self.ringstationcontroltable = TOKENRINGRMONMIB.RingStationControlTable()
        self.ringstationcontroltable.parent = self
        self.ringstationordertable = TOKENRINGRMONMIB.RingStationOrderTable()
        self.ringstationordertable.parent = self
        self.ringstationtable = TOKENRINGRMONMIB.RingStationTable()
        self.ringstationtable.parent = self
        self.sourceroutingstatstable = TOKENRINGRMONMIB.SourceRoutingStatsTable()
        self.sourceroutingstatstable.parent = self
        self.tokenringmlhistorytable = TOKENRINGRMONMIB.TokenRingMLHistoryTable()
        self.tokenringmlhistorytable.parent = self
        self.tokenringmlstatstable = TOKENRINGRMONMIB.TokenRingMLStatsTable()
        self.tokenringmlstatstable.parent = self
        self.tokenringphistorytable = TOKENRINGRMONMIB.TokenRingPHistoryTable()
        self.tokenringphistorytable.parent = self
        self.tokenringpstatstable = TOKENRINGRMONMIB.TokenRingPStatsTable()
        self.tokenringpstatstable.parent = self


    class RingStationConfigControlTable(object):
        """
        A list of ring station configuration control
        entries.
        
        .. attribute:: ringstationconfigcontrolentry
        
        	This entry controls active management of stations by the probe.  One entry exists in this table for each active station in the ringStationTable
        	**type**\: list of :py:class:`RingStationConfigControlEntry <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationConfigControlTable.RingStationConfigControlEntry>`
        
        

        """

        _prefix = 'token-ring'

        def __init__(self):
            self.parent = None
            self.ringstationconfigcontrolentry = YList()
            self.ringstationconfigcontrolentry.parent = self
            self.ringstationconfigcontrolentry.name = 'ringstationconfigcontrolentry'


        class RingStationConfigControlEntry(object):
            """
            This entry controls active management of stations
            by the probe.  One entry exists in this table for
            each active station in the ringStationTable.
            
            .. attribute:: ringstationconfigcontrolifindex
            
            	The value of this object uniquely identifies the      interface on this remote network monitoring device on which this station was detected.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in MIB\-II [3]
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ringstationconfigcontrolmacaddress
            
            	The physical address of this station
            	**type**\: str
            
            	**range:** 6
            
            .. attribute:: ringstationconfigcontrolremove
            
            	Setting this object to `removing(2)' causes a Remove Station MAC frame to be sent.  The agent will set this object to `stable(1)' after processing the request
            	**type**\: :py:class:`RingStationConfigControlRemove_Enum <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationConfigControlTable.RingStationConfigControlEntry.RingStationConfigControlRemove_Enum>`
            
            .. attribute:: ringstationconfigcontrolupdatestats
            
            	Setting this object to `updating(2)' causes the configuration information associate with this entry to be updated.  The agent will set this object to `stable(1)' after processing the request
            	**type**\: :py:class:`RingStationConfigControlUpdateStats_Enum <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationConfigControlTable.RingStationConfigControlEntry.RingStationConfigControlUpdateStats_Enum>`
            
            

            """

            _prefix = 'token-ring'

            def __init__(self):
                self.parent = None
                self.ringstationconfigcontrolifindex = None
                self.ringstationconfigcontrolmacaddress = None
                self.ringstationconfigcontrolremove = None
                self.ringstationconfigcontrolupdatestats = None

            class RingStationConfigControlRemove_Enum(Enum):
                """
                RingStationConfigControlRemove_Enum

                Setting this object to `removing(2)' causes a
                Remove Station MAC frame to be sent.  The agent
                will set this object to `stable(1)' after
                processing the request.

                """

                STABLE = 1

                REMOVING = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
                    return meta._meta_table['TOKENRINGRMONMIB.RingStationConfigControlTable.RingStationConfigControlEntry.RingStationConfigControlRemove_Enum']


            class RingStationConfigControlUpdateStats_Enum(Enum):
                """
                RingStationConfigControlUpdateStats_Enum

                Setting this object to `updating(2)' causes the
                configuration information associate with this
                entry to be updated.  The agent will set this
                object to `stable(1)' after processing the
                request.

                """

                STABLE = 1

                UPDATING = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
                    return meta._meta_table['TOKENRINGRMONMIB.RingStationConfigControlTable.RingStationConfigControlEntry.RingStationConfigControlUpdateStats_Enum']


            @property
            def _common_path(self):
                if self.ringstationconfigcontrolifindex is None:
                    raise YPYDataValidationError('Key property ringstationconfigcontrolifindex is None')
                if self.ringstationconfigcontrolmacaddress is None:
                    raise YPYDataValidationError('Key property ringstationconfigcontrolmacaddress is None')

                return '/TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/TOKEN-RING-RMON-MIB:ringStationConfigControlTable/TOKEN-RING-RMON-MIB:ringStationConfigControlEntry[TOKEN-RING-RMON-MIB:ringStationConfigControlIfIndex = ' + str(self.ringstationconfigcontrolifindex) + '][TOKEN-RING-RMON-MIB:ringStationConfigControlMacAddress = ' + str(self.ringstationconfigcontrolmacaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ringstationconfigcontrolifindex is not None:
                    return True

                if self.ringstationconfigcontrolmacaddress is not None:
                    return True

                if self.ringstationconfigcontrolremove is not None:
                    return True

                if self.ringstationconfigcontrolupdatestats is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
                return meta._meta_table['TOKENRINGRMONMIB.RingStationConfigControlTable.RingStationConfigControlEntry']['meta_info']

        @property
        def _common_path(self):

            return '/TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/TOKEN-RING-RMON-MIB:ringStationConfigControlTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ringstationconfigcontrolentry is not None:
                for child_ref in self.ringstationconfigcontrolentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
            return meta._meta_table['TOKENRINGRMONMIB.RingStationConfigControlTable']['meta_info']


    class RingStationConfigTable(object):
        """
        A list of configuration entries for stations on a
        ring monitored by this probe.
        
        .. attribute:: ringstationconfigentry
        
        	A collection of statistics for a particular station that has been discovered on a ring monitored by this probe
        	**type**\: list of :py:class:`RingStationConfigEntry <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationConfigTable.RingStationConfigEntry>`
        
        

        """

        _prefix = 'token-ring'

        def __init__(self):
            self.parent = None
            self.ringstationconfigentry = YList()
            self.ringstationconfigentry.parent = self
            self.ringstationconfigentry.name = 'ringstationconfigentry'


        class RingStationConfigEntry(object):
            """
            A collection of statistics for a particular
            station that has been discovered on a ring
            monitored by this probe.
            
            .. attribute:: ringstationconfigifindex
            
            	The value of this object uniquely identifies the      interface on this remote network monitoring device on which this station was detected.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in MIB\-II [3]
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ringstationconfigmacaddress
            
            	The physical address of this station
            	**type**\: str
            
            	**range:** 6
            
            .. attribute:: ringstationconfigfunctionaladdress
            
            	the functional addresses recognized by this station
            	**type**\: str
            
            	**range:** 4
            
            .. attribute:: ringstationconfiggroupaddress
            
            	The low\-order 4 octets of the group address recognized by this station
            	**type**\: str
            
            	**range:** 4
            
            .. attribute:: ringstationconfiglocation
            
            	The assigned physical location of this station
            	**type**\: str
            
            	**range:** 4
            
            .. attribute:: ringstationconfigmicrocode
            
            	The microcode EC level of this station
            	**type**\: str
            
            	**range:** 10
            
            .. attribute:: ringstationconfigupdatetime
            
            	The value of sysUpTime at the time this configuration information was last updated (completely)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'token-ring'

            def __init__(self):
                self.parent = None
                self.ringstationconfigifindex = None
                self.ringstationconfigmacaddress = None
                self.ringstationconfigfunctionaladdress = None
                self.ringstationconfiggroupaddress = None
                self.ringstationconfiglocation = None
                self.ringstationconfigmicrocode = None
                self.ringstationconfigupdatetime = None

            @property
            def _common_path(self):
                if self.ringstationconfigifindex is None:
                    raise YPYDataValidationError('Key property ringstationconfigifindex is None')
                if self.ringstationconfigmacaddress is None:
                    raise YPYDataValidationError('Key property ringstationconfigmacaddress is None')

                return '/TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/TOKEN-RING-RMON-MIB:ringStationConfigTable/TOKEN-RING-RMON-MIB:ringStationConfigEntry[TOKEN-RING-RMON-MIB:ringStationConfigIfIndex = ' + str(self.ringstationconfigifindex) + '][TOKEN-RING-RMON-MIB:ringStationConfigMacAddress = ' + str(self.ringstationconfigmacaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ringstationconfigifindex is not None:
                    return True

                if self.ringstationconfigmacaddress is not None:
                    return True

                if self.ringstationconfigfunctionaladdress is not None:
                    return True

                if self.ringstationconfiggroupaddress is not None:
                    return True

                if self.ringstationconfiglocation is not None:
                    return True

                if self.ringstationconfigmicrocode is not None:
                    return True

                if self.ringstationconfigupdatetime is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
                return meta._meta_table['TOKENRINGRMONMIB.RingStationConfigTable.RingStationConfigEntry']['meta_info']

        @property
        def _common_path(self):

            return '/TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/TOKEN-RING-RMON-MIB:ringStationConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ringstationconfigentry is not None:
                for child_ref in self.ringstationconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
            return meta._meta_table['TOKENRINGRMONMIB.RingStationConfigTable']['meta_info']


    class RingStationControlTable(object):
        """
        A list of ringStation table control entries.
        
        .. attribute:: ringstationcontrolentry
        
        	A list of parameters that set up the discovery of stations on a particular interface and the collection of statistics about these stations
        	**type**\: list of :py:class:`RingStationControlEntry <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationControlTable.RingStationControlEntry>`
        
        

        """

        _prefix = 'token-ring'

        def __init__(self):
            self.parent = None
            self.ringstationcontrolentry = YList()
            self.ringstationcontrolentry.parent = self
            self.ringstationcontrolentry.name = 'ringstationcontrolentry'


        class RingStationControlEntry(object):
            """
            A list of parameters that set up the discovery of
            stations on a particular interface and the
            collection of statistics about these stations.
            
            .. attribute:: ringstationcontrolifindex
            
            	The value of this object uniquely identifies the interface on this remote network monitoring device from which ringStation data is collected.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in MIB\- II [3]
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: ringstationcontrolactivemonitor
            
            	The address of the Active Monitor on this segment.  If this address is unknown, this object shall be equal to six octets of zero
            	**type**\: str
            
            	**range:** 6
            
            .. attribute:: ringstationcontrolactivestations
            
            	The number of active ringStationEntries in the ringStationTable associated with this ringStationControlEntry
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ringstationcontrolbeaconnaun
            
            	The address of the NAUN in the last beacon frame received by the probe on this ring.  If no beacon frames have been received, this object shall be equal to six octets of zero
            	**type**\: str
            
            	**range:** 6
            
            .. attribute:: ringstationcontrolbeaconsender
            
            	The address of the sender of the last beacon frame received by the probe on this ring.  If no beacon frames have been received, this object shall be equal to six octets of zero
            	**type**\: str
            
            	**range:** 6
            
            .. attribute:: ringstationcontrolcreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationcontroldroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationcontrolorderchanges
            
            	The number of add and delete events in the ringStationOrderTable optionally associated with this ringStationControlEntry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationcontrolowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            .. attribute:: ringstationcontrolringstate
            
            	The current status of this ring
            	**type**\: :py:class:`RingStationControlRingState_Enum <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationControlTable.RingStationControlEntry.RingStationControlRingState_Enum>`
            
            .. attribute:: ringstationcontrolstatus
            
            	The status of this ringStationControl entry.  If this object is not equal to valid(1), all associated entries in the ringStationTable shall be deleted by the agent
            	**type**\: :py:class:`EntryStatus_Enum <ydk.models.token.TOKEN_RING_RMON_MIB.EntryStatus_Enum>`
            
            .. attribute:: ringstationcontroltablesize
            
            	The number of ringStationEntries in the ringStationTable associated with this ringStationControlEntry
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'token-ring'

            def __init__(self):
                self.parent = None
                self.ringstationcontrolifindex = None
                self.ringstationcontrolactivemonitor = None
                self.ringstationcontrolactivestations = None
                self.ringstationcontrolbeaconnaun = None
                self.ringstationcontrolbeaconsender = None
                self.ringstationcontrolcreatetime = None
                self.ringstationcontroldroppedframes = None
                self.ringstationcontrolorderchanges = None
                self.ringstationcontrolowner = None
                self.ringstationcontrolringstate = None
                self.ringstationcontrolstatus = None
                self.ringstationcontroltablesize = None

            class RingStationControlRingState_Enum(Enum):
                """
                RingStationControlRingState_Enum

                The current status of this ring.

                """

                NORMALOPERATION = 1

                RINGPURGESTATE = 2

                CLAIMTOKENSTATE = 3

                BEACONFRAMESTREAMINGSTATE = 4

                BEACONBITSTREAMINGSTATE = 5

                BEACONRINGSIGNALLOSSSTATE = 6

                BEACONSETRECOVERYMODESTATE = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
                    return meta._meta_table['TOKENRINGRMONMIB.RingStationControlTable.RingStationControlEntry.RingStationControlRingState_Enum']


            @property
            def _common_path(self):
                if self.ringstationcontrolifindex is None:
                    raise YPYDataValidationError('Key property ringstationcontrolifindex is None')

                return '/TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/TOKEN-RING-RMON-MIB:ringStationControlTable/TOKEN-RING-RMON-MIB:ringStationControlEntry[TOKEN-RING-RMON-MIB:ringStationControlIfIndex = ' + str(self.ringstationcontrolifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ringstationcontrolifindex is not None:
                    return True

                if self.ringstationcontrolactivemonitor is not None:
                    return True

                if self.ringstationcontrolactivestations is not None:
                    return True

                if self.ringstationcontrolbeaconnaun is not None:
                    return True

                if self.ringstationcontrolbeaconsender is not None:
                    return True

                if self.ringstationcontrolcreatetime is not None:
                    return True

                if self.ringstationcontroldroppedframes is not None:
                    return True

                if self.ringstationcontrolorderchanges is not None:
                    return True

                if self.ringstationcontrolowner is not None:
                    return True

                if self.ringstationcontrolringstate is not None:
                    return True

                if self.ringstationcontrolstatus is not None:
                    return True

                if self.ringstationcontroltablesize is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
                return meta._meta_table['TOKENRINGRMONMIB.RingStationControlTable.RingStationControlEntry']['meta_info']

        @property
        def _common_path(self):

            return '/TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/TOKEN-RING-RMON-MIB:ringStationControlTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ringstationcontrolentry is not None:
                for child_ref in self.ringstationcontrolentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
            return meta._meta_table['TOKENRINGRMONMIB.RingStationControlTable']['meta_info']


    class RingStationOrderTable(object):
        """
        A list of ring station entries for stations in
        the ring poll, ordered by their ring\-order.
        
        .. attribute:: ringstationorderentry
        
        	A collection of statistics for a particular      station that is active on a ring monitored by this device.  This table will contain information for every interface that has a ringStationControlStatus equal to valid
        	**type**\: list of :py:class:`RingStationOrderEntry <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationOrderTable.RingStationOrderEntry>`
        
        

        """

        _prefix = 'token-ring'

        def __init__(self):
            self.parent = None
            self.ringstationorderentry = YList()
            self.ringstationorderentry.parent = self
            self.ringstationorderentry.name = 'ringstationorderentry'


        class RingStationOrderEntry(object):
            """
            A collection of statistics for a particular
            
            
            
            
            
            station that is active on a ring monitored by this
            device.  This table will contain information for
            every interface that has a
            ringStationControlStatus equal to valid.
            
            .. attribute:: ringstationorderifindex
            
            	The value of this object uniquely identifies the interface on this remote network monitoring device on which this station was detected.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in MIB\-II [3]
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ringstationorderorderindex
            
            	This index denotes the location of this station with respect to other stations on the ring.  This index is one more than the number of hops downstream that this station is from the rmon probe.  The rmon probe itself gets the value one
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ringstationordermacaddress
            
            	The physical address of this station
            	**type**\: str
            
            	**range:** 6
            
            

            """

            _prefix = 'token-ring'

            def __init__(self):
                self.parent = None
                self.ringstationorderifindex = None
                self.ringstationorderorderindex = None
                self.ringstationordermacaddress = None

            @property
            def _common_path(self):
                if self.ringstationorderifindex is None:
                    raise YPYDataValidationError('Key property ringstationorderifindex is None')
                if self.ringstationorderorderindex is None:
                    raise YPYDataValidationError('Key property ringstationorderorderindex is None')

                return '/TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/TOKEN-RING-RMON-MIB:ringStationOrderTable/TOKEN-RING-RMON-MIB:ringStationOrderEntry[TOKEN-RING-RMON-MIB:ringStationOrderIfIndex = ' + str(self.ringstationorderifindex) + '][TOKEN-RING-RMON-MIB:ringStationOrderOrderIndex = ' + str(self.ringstationorderorderindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ringstationorderifindex is not None:
                    return True

                if self.ringstationorderorderindex is not None:
                    return True

                if self.ringstationordermacaddress is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
                return meta._meta_table['TOKENRINGRMONMIB.RingStationOrderTable.RingStationOrderEntry']['meta_info']

        @property
        def _common_path(self):

            return '/TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/TOKEN-RING-RMON-MIB:ringStationOrderTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ringstationorderentry is not None:
                for child_ref in self.ringstationorderentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
            return meta._meta_table['TOKENRINGRMONMIB.RingStationOrderTable']['meta_info']


    class RingStationTable(object):
        """
        A list of ring station entries.  An entry will
        exist for each station that is now or has
        
        
        
        
        
        previously been detected as physically present on
        this ring.
        
        .. attribute:: ringstationentry
        
        	A collection of statistics for a particular station that has been discovered on a ring monitored by this device
        	**type**\: list of :py:class:`RingStationEntry <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationTable.RingStationEntry>`
        
        

        """

        _prefix = 'token-ring'

        def __init__(self):
            self.parent = None
            self.ringstationentry = YList()
            self.ringstationentry.parent = self
            self.ringstationentry.name = 'ringstationentry'


        class RingStationEntry(object):
            """
            A collection of statistics for a particular
            station that has been discovered on a ring
            monitored by this device.
            
            .. attribute:: ringstationifindex
            
            	The value of this object uniquely identifies the interface on this remote network monitoring device on which this station was detected.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in MIB\-II [3]
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ringstationmacaddress
            
            	The physical address of this station
            	**type**\: str
            
            	**range:** 6
            
            .. attribute:: ringstationaborterrors
            
            	The total number of abort delimiters reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationacerrors
            
            	The total number of AC (Address Copied) errors reported in error reporting packets sent by the nearest active downstream neighbor of this station and detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationcongestionerrors
            
            	The total number of receive congestion errors reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationduplicateaddresses
            
            	The number of times this station experienced a duplicate address error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationframecopiederrors
            
            	The total number of frame copied errors reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationfrequencyerrors
            
            	The total number of frequency errors reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationinbeaconerrors
            
            	The total number of beacon frames sent by this station and detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationinbursterrors
            
            	The total number of burst errors reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationinlineerrors
            
            	The total number of line errors reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationinsertions
            
            	The number of times the probe detected this station inserting onto the ring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationinternalerrors
            
            	The total number of adapter internal errors reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationlastentertime
            
            	The value of sysUpTime at the time this station last entered the ring.  If the time is unknown, this value shall be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationlastexittime
            
            	The value of sysUpTime at the time the probe detected that this station last exited the ring. If the time is unknown, this value shall be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationlastnaun
            
            	The physical address of last known NAUN of this station
            	**type**\: str
            
            	**range:** 6
            
            .. attribute:: ringstationlostframeerrors
            
            	The total number of lost frame errors reported by this station in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationoutbeaconerrors
            
            	The total number of beacon frames detected by the probe that name this station as the NAUN
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationoutbursterrors
            
            	The total number of burst errors reported in error reporting packets sent by the nearest active downstream neighbor of this station and detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationoutlineerrors
            
            	The total number of line errors reported in error reporting packets sent by the nearest active downstream neighbor of this station and detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ringstationstationstatus
            
            	The status of this station on the ring
            	**type**\: :py:class:`RingStationStationStatus_Enum <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.RingStationTable.RingStationEntry.RingStationStationStatus_Enum>`
            
            .. attribute:: ringstationtokenerrors
            
            	The total number of token errors reported by this station in error reporting frames detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'token-ring'

            def __init__(self):
                self.parent = None
                self.ringstationifindex = None
                self.ringstationmacaddress = None
                self.ringstationaborterrors = None
                self.ringstationacerrors = None
                self.ringstationcongestionerrors = None
                self.ringstationduplicateaddresses = None
                self.ringstationframecopiederrors = None
                self.ringstationfrequencyerrors = None
                self.ringstationinbeaconerrors = None
                self.ringstationinbursterrors = None
                self.ringstationinlineerrors = None
                self.ringstationinsertions = None
                self.ringstationinternalerrors = None
                self.ringstationlastentertime = None
                self.ringstationlastexittime = None
                self.ringstationlastnaun = None
                self.ringstationlostframeerrors = None
                self.ringstationoutbeaconerrors = None
                self.ringstationoutbursterrors = None
                self.ringstationoutlineerrors = None
                self.ringstationstationstatus = None
                self.ringstationtokenerrors = None

            class RingStationStationStatus_Enum(Enum):
                """
                RingStationStationStatus_Enum

                The status of this station on the ring.

                """

                ACTIVE = 1

                INACTIVE = 2

                FORCEDREMOVAL = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
                    return meta._meta_table['TOKENRINGRMONMIB.RingStationTable.RingStationEntry.RingStationStationStatus_Enum']


            @property
            def _common_path(self):
                if self.ringstationifindex is None:
                    raise YPYDataValidationError('Key property ringstationifindex is None')
                if self.ringstationmacaddress is None:
                    raise YPYDataValidationError('Key property ringstationmacaddress is None')

                return '/TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/TOKEN-RING-RMON-MIB:ringStationTable/TOKEN-RING-RMON-MIB:ringStationEntry[TOKEN-RING-RMON-MIB:ringStationIfIndex = ' + str(self.ringstationifindex) + '][TOKEN-RING-RMON-MIB:ringStationMacAddress = ' + str(self.ringstationmacaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ringstationifindex is not None:
                    return True

                if self.ringstationmacaddress is not None:
                    return True

                if self.ringstationaborterrors is not None:
                    return True

                if self.ringstationacerrors is not None:
                    return True

                if self.ringstationcongestionerrors is not None:
                    return True

                if self.ringstationduplicateaddresses is not None:
                    return True

                if self.ringstationframecopiederrors is not None:
                    return True

                if self.ringstationfrequencyerrors is not None:
                    return True

                if self.ringstationinbeaconerrors is not None:
                    return True

                if self.ringstationinbursterrors is not None:
                    return True

                if self.ringstationinlineerrors is not None:
                    return True

                if self.ringstationinsertions is not None:
                    return True

                if self.ringstationinternalerrors is not None:
                    return True

                if self.ringstationlastentertime is not None:
                    return True

                if self.ringstationlastexittime is not None:
                    return True

                if self.ringstationlastnaun is not None:
                    return True

                if self.ringstationlostframeerrors is not None:
                    return True

                if self.ringstationoutbeaconerrors is not None:
                    return True

                if self.ringstationoutbursterrors is not None:
                    return True

                if self.ringstationoutlineerrors is not None:
                    return True

                if self.ringstationstationstatus is not None:
                    return True

                if self.ringstationtokenerrors is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
                return meta._meta_table['TOKENRINGRMONMIB.RingStationTable.RingStationEntry']['meta_info']

        @property
        def _common_path(self):

            return '/TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/TOKEN-RING-RMON-MIB:ringStationTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ringstationentry is not None:
                for child_ref in self.ringstationentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
            return meta._meta_table['TOKENRINGRMONMIB.RingStationTable']['meta_info']


    class SourceRoutingStatsTable(object):
        """
        A list of source routing statistics entries.
        
        .. attribute:: sourceroutingstatsentry
        
        	A collection of source routing statistics kept for a particular Token Ring interface
        	**type**\: list of :py:class:`SourceRoutingStatsEntry <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.SourceRoutingStatsTable.SourceRoutingStatsEntry>`
        
        

        """

        _prefix = 'token-ring'

        def __init__(self):
            self.parent = None
            self.sourceroutingstatsentry = YList()
            self.sourceroutingstatsentry.parent = self
            self.sourceroutingstatsentry.name = 'sourceroutingstatsentry'


        class SourceRoutingStatsEntry(object):
            """
            A collection of source routing statistics kept
            for a particular Token Ring interface.
            
            .. attribute:: sourceroutingstatsifindex
            
            	The value of this object uniquely identifies the interface on this remote network monitoring device on which source routing statistics will be detected.  The interface identified by a particular value of this object is the same interface as identified by the same value of the ifIndex object, defined in MIB\-II [3]
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: sourceroutingstats1hopframes
            
            	The total number of frames received whose route had 1 hop, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstats2hopsframes
            
            	The total number of frames received whose route had 2 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstats3hopsframes
            
            	The total number of frames received whose route had 3 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstats4hopsframes
            
            	The total number of frames received whose route had 4 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstats5hopsframes
            
            	The total number of frames received whose route had 5 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstats6hopsframes
            
            	The total number of frames received whose route had 6 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstats7hopsframes
            
            	The total number of frames received whose route had 7 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstats8hopsframes
            
            	The total number of frames received whose route had 8 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsallroutesbroadcastframes
            
            	The total number of good frames received that were All Routes Broadcast
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsallroutesbroadcastoctets
            
            	The total number of octets in good frames received that were All Routes Broadcast
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatscreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsdroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsinframes
            
            	The count of frames sent into this ring from another ring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsinoctets
            
            	The count of octets in good frames sent into this ring from another ring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatslocalllcframes
            
            	The total number of frames received who had no RIF field (or had a RIF field that only included the local ring's number) and were not All Route Broadcast Frames
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsmorethan8hopsframes
            
            	The total number of frames received whose route had more than 8 hops, were not All Route Broadcast Frames, and whose source or destination were on this ring (i.e. frames that had a RIF field and had this ring number in the first or last entry of the RIF field)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsoutframes
            
            	The count of frames sent from this ring to another ring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsoutoctets
            
            	The count of octets in good frames sent from this ring to another ring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            .. attribute:: sourceroutingstatsringnumber
            
            	The ring number of the ring monitored by this entry.  When any object in this entry is created, the probe will attempt to discover the ring number.  Only after the ring number is discovered will this object be created.  After creating an object in this entry, the management station should poll this object to detect when it is created.  Only after this object is created can the management station set the sourceRoutingStatsStatus entry to valid(1)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: sourceroutingstatssingleroutebroadcastframes
            
            	The total number of good frames received that were Single Route Broadcast
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatssingleroutesbroadcastoctets
            
            	The total number of octets in good frames received that were Single Route Broadcast
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsstatus
            
            	The status of this sourceRoutingStats entry
            	**type**\: :py:class:`EntryStatus_Enum <ydk.models.token.TOKEN_RING_RMON_MIB.EntryStatus_Enum>`
            
            .. attribute:: sourceroutingstatsthroughframes
            
            	The count of frames sent from another ring, through this ring, to another ring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sourceroutingstatsthroughoctets
            
            	The count of octets in good frames sent another ring, through this ring, to another ring
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'token-ring'

            def __init__(self):
                self.parent = None
                self.sourceroutingstatsifindex = None
                self.sourceroutingstats1hopframes = None
                self.sourceroutingstats2hopsframes = None
                self.sourceroutingstats3hopsframes = None
                self.sourceroutingstats4hopsframes = None
                self.sourceroutingstats5hopsframes = None
                self.sourceroutingstats6hopsframes = None
                self.sourceroutingstats7hopsframes = None
                self.sourceroutingstats8hopsframes = None
                self.sourceroutingstatsallroutesbroadcastframes = None
                self.sourceroutingstatsallroutesbroadcastoctets = None
                self.sourceroutingstatscreatetime = None
                self.sourceroutingstatsdroppedframes = None
                self.sourceroutingstatsinframes = None
                self.sourceroutingstatsinoctets = None
                self.sourceroutingstatslocalllcframes = None
                self.sourceroutingstatsmorethan8hopsframes = None
                self.sourceroutingstatsoutframes = None
                self.sourceroutingstatsoutoctets = None
                self.sourceroutingstatsowner = None
                self.sourceroutingstatsringnumber = None
                self.sourceroutingstatssingleroutebroadcastframes = None
                self.sourceroutingstatssingleroutesbroadcastoctets = None
                self.sourceroutingstatsstatus = None
                self.sourceroutingstatsthroughframes = None
                self.sourceroutingstatsthroughoctets = None

            @property
            def _common_path(self):
                if self.sourceroutingstatsifindex is None:
                    raise YPYDataValidationError('Key property sourceroutingstatsifindex is None')

                return '/TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/TOKEN-RING-RMON-MIB:sourceRoutingStatsTable/TOKEN-RING-RMON-MIB:sourceRoutingStatsEntry[TOKEN-RING-RMON-MIB:sourceRoutingStatsIfIndex = ' + str(self.sourceroutingstatsifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.sourceroutingstatsifindex is not None:
                    return True

                if self.sourceroutingstats1hopframes is not None:
                    return True

                if self.sourceroutingstats2hopsframes is not None:
                    return True

                if self.sourceroutingstats3hopsframes is not None:
                    return True

                if self.sourceroutingstats4hopsframes is not None:
                    return True

                if self.sourceroutingstats5hopsframes is not None:
                    return True

                if self.sourceroutingstats6hopsframes is not None:
                    return True

                if self.sourceroutingstats7hopsframes is not None:
                    return True

                if self.sourceroutingstats8hopsframes is not None:
                    return True

                if self.sourceroutingstatsallroutesbroadcastframes is not None:
                    return True

                if self.sourceroutingstatsallroutesbroadcastoctets is not None:
                    return True

                if self.sourceroutingstatscreatetime is not None:
                    return True

                if self.sourceroutingstatsdroppedframes is not None:
                    return True

                if self.sourceroutingstatsinframes is not None:
                    return True

                if self.sourceroutingstatsinoctets is not None:
                    return True

                if self.sourceroutingstatslocalllcframes is not None:
                    return True

                if self.sourceroutingstatsmorethan8hopsframes is not None:
                    return True

                if self.sourceroutingstatsoutframes is not None:
                    return True

                if self.sourceroutingstatsoutoctets is not None:
                    return True

                if self.sourceroutingstatsowner is not None:
                    return True

                if self.sourceroutingstatsringnumber is not None:
                    return True

                if self.sourceroutingstatssingleroutebroadcastframes is not None:
                    return True

                if self.sourceroutingstatssingleroutesbroadcastoctets is not None:
                    return True

                if self.sourceroutingstatsstatus is not None:
                    return True

                if self.sourceroutingstatsthroughframes is not None:
                    return True

                if self.sourceroutingstatsthroughoctets is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
                return meta._meta_table['TOKENRINGRMONMIB.SourceRoutingStatsTable.SourceRoutingStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/TOKEN-RING-RMON-MIB:sourceRoutingStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.sourceroutingstatsentry is not None:
                for child_ref in self.sourceroutingstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
            return meta._meta_table['TOKENRINGRMONMIB.SourceRoutingStatsTable']['meta_info']


    class TokenRingMLHistoryTable(object):
        """
        A list of Mac\-Layer Token Ring statistics
        
        
        
        
        
        entries.
        
        .. attribute:: tokenringmlhistoryentry
        
        	A collection of Mac\-Layer statistics kept for a particular Token Ring interface
        	**type**\: list of :py:class:`TokenRingMLHistoryEntry <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.TokenRingMLHistoryTable.TokenRingMLHistoryEntry>`
        
        

        """

        _prefix = 'token-ring'

        def __init__(self):
            self.parent = None
            self.tokenringmlhistoryentry = YList()
            self.tokenringmlhistoryentry.parent = self
            self.tokenringmlhistoryentry.name = 'tokenringmlhistoryentry'


        class TokenRingMLHistoryEntry(object):
            """
            A collection of Mac\-Layer statistics kept for a
            particular Token Ring interface.
            
            .. attribute:: tokenringmlhistoryindex
            
            	The history of which this entry is a part.  The history identified by a particular value of this index is the same history as identified by the same value of historyControlIndex
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: tokenringmlhistorysampleindex
            
            	An index that uniquely identifies the particular Mac\-Layer sample this entry represents among all Mac\-Layer samples associated with the same historyControlEntry.  This index starts at 1 and increases by one as each new sample is taken
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: tokenringmlhistoryaborterrors
            
            	The total number of abort delimiters reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryacerrors
            
            	The total number of AC (Address Copied) errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryactivestations
            
            	The maximum number of active stations on the ring detected by the probe during this sampling      interval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: tokenringmlhistorybeaconevents
            
            	The total number of times that the ring enters a beaconing state (beaconFrameStreamingState, beaconBitStreamingState, beaconSetRecoveryModeState, or beaconRingSignalLossState) during this sampling interval.  Note that a change of the source address of the beacon packet does not constitute a new beacon event
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorybeaconpkts
            
            	The total number of beacon MAC packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorybeacontime
            
            	The amount of time that the ring has been in the beaconing state during this sampling interval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: tokenringmlhistorybursterrors
            
            	The total number of burst errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryclaimtokenevents
            
            	The total number of times that the ring enters the claim token state from normal ring state or ring purge state during this sampling interval. The claim token state that comes from the beacon state is not counted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryclaimtokenpkts
            
            	The total number of claim token MAC packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorycongestionerrors
            
            	The total number of receive congestion errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorydropevents
            
            	The total number of events in which packets were      dropped by the probe due to lack of resources during this sampling interval.  Note that this number is not necessarily the number of packets dropped, it is just the number of times this condition has been detected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryframecopiederrors
            
            	The total number of frame copied errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryfrequencyerrors
            
            	The total number of frequency errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryinternalerrors
            
            	The total number of adapter internal errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryintervalstart
            
            	The value of sysUpTime at the start of the interval over which this sample was measured.  If the probe keeps track of the time of day, it should start the first sample of the history at a time such that when the next hour of the day begins, a sample is started at that instant.  Note that following this rule may require the probe to delay collecting the first sample of the history, as each sample must be of the same interval.  Also note that the sample which is currently being collected is not accessible in this table until the end of its interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorylineerrors
            
            	The total number of line errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorylostframeerrors
            
            	The total number of lost frame errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorymacoctets
            
            	The total number of octets of data in MAC packets (excluding those that were not good frames) received on the network during this sampling interval (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorymacpkts
            
            	The total number of MAC packets (excluding those that were not good frames) received during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorynaunchanges
            
            	The total number of NAUN changes detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryringpollevents
            
            	The total number of ring poll events detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryringpurgeevents
            
            	The total number of times that the ring entered the ring purge state from normal ring state during this sampling interval.  The ring purge state that comes from the claim token or beacon state is not counted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistoryringpurgepkts
            
            	The total number of Ring Purge MAC packets detected by the probe during this sampling      interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorysofterrorreports
            
            	The total number of soft error report frames detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlhistorytokenerrors
            
            	The total number of token errors reported in error reporting packets detected by the probe during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'token-ring'

            def __init__(self):
                self.parent = None
                self.tokenringmlhistoryindex = None
                self.tokenringmlhistorysampleindex = None
                self.tokenringmlhistoryaborterrors = None
                self.tokenringmlhistoryacerrors = None
                self.tokenringmlhistoryactivestations = None
                self.tokenringmlhistorybeaconevents = None
                self.tokenringmlhistorybeaconpkts = None
                self.tokenringmlhistorybeacontime = None
                self.tokenringmlhistorybursterrors = None
                self.tokenringmlhistoryclaimtokenevents = None
                self.tokenringmlhistoryclaimtokenpkts = None
                self.tokenringmlhistorycongestionerrors = None
                self.tokenringmlhistorydropevents = None
                self.tokenringmlhistoryframecopiederrors = None
                self.tokenringmlhistoryfrequencyerrors = None
                self.tokenringmlhistoryinternalerrors = None
                self.tokenringmlhistoryintervalstart = None
                self.tokenringmlhistorylineerrors = None
                self.tokenringmlhistorylostframeerrors = None
                self.tokenringmlhistorymacoctets = None
                self.tokenringmlhistorymacpkts = None
                self.tokenringmlhistorynaunchanges = None
                self.tokenringmlhistoryringpollevents = None
                self.tokenringmlhistoryringpurgeevents = None
                self.tokenringmlhistoryringpurgepkts = None
                self.tokenringmlhistorysofterrorreports = None
                self.tokenringmlhistorytokenerrors = None

            @property
            def _common_path(self):
                if self.tokenringmlhistoryindex is None:
                    raise YPYDataValidationError('Key property tokenringmlhistoryindex is None')
                if self.tokenringmlhistorysampleindex is None:
                    raise YPYDataValidationError('Key property tokenringmlhistorysampleindex is None')

                return '/TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/TOKEN-RING-RMON-MIB:tokenRingMLHistoryTable/TOKEN-RING-RMON-MIB:tokenRingMLHistoryEntry[TOKEN-RING-RMON-MIB:tokenRingMLHistoryIndex = ' + str(self.tokenringmlhistoryindex) + '][TOKEN-RING-RMON-MIB:tokenRingMLHistorySampleIndex = ' + str(self.tokenringmlhistorysampleindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.tokenringmlhistoryindex is not None:
                    return True

                if self.tokenringmlhistorysampleindex is not None:
                    return True

                if self.tokenringmlhistoryaborterrors is not None:
                    return True

                if self.tokenringmlhistoryacerrors is not None:
                    return True

                if self.tokenringmlhistoryactivestations is not None:
                    return True

                if self.tokenringmlhistorybeaconevents is not None:
                    return True

                if self.tokenringmlhistorybeaconpkts is not None:
                    return True

                if self.tokenringmlhistorybeacontime is not None:
                    return True

                if self.tokenringmlhistorybursterrors is not None:
                    return True

                if self.tokenringmlhistoryclaimtokenevents is not None:
                    return True

                if self.tokenringmlhistoryclaimtokenpkts is not None:
                    return True

                if self.tokenringmlhistorycongestionerrors is not None:
                    return True

                if self.tokenringmlhistorydropevents is not None:
                    return True

                if self.tokenringmlhistoryframecopiederrors is not None:
                    return True

                if self.tokenringmlhistoryfrequencyerrors is not None:
                    return True

                if self.tokenringmlhistoryinternalerrors is not None:
                    return True

                if self.tokenringmlhistoryintervalstart is not None:
                    return True

                if self.tokenringmlhistorylineerrors is not None:
                    return True

                if self.tokenringmlhistorylostframeerrors is not None:
                    return True

                if self.tokenringmlhistorymacoctets is not None:
                    return True

                if self.tokenringmlhistorymacpkts is not None:
                    return True

                if self.tokenringmlhistorynaunchanges is not None:
                    return True

                if self.tokenringmlhistoryringpollevents is not None:
                    return True

                if self.tokenringmlhistoryringpurgeevents is not None:
                    return True

                if self.tokenringmlhistoryringpurgepkts is not None:
                    return True

                if self.tokenringmlhistorysofterrorreports is not None:
                    return True

                if self.tokenringmlhistorytokenerrors is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
                return meta._meta_table['TOKENRINGRMONMIB.TokenRingMLHistoryTable.TokenRingMLHistoryEntry']['meta_info']

        @property
        def _common_path(self):

            return '/TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/TOKEN-RING-RMON-MIB:tokenRingMLHistoryTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.tokenringmlhistoryentry is not None:
                for child_ref in self.tokenringmlhistoryentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
            return meta._meta_table['TOKENRINGRMONMIB.TokenRingMLHistoryTable']['meta_info']


    class TokenRingMLStatsTable(object):
        """
        A list of Mac\-Layer Token Ring statistics
        
        
        
        
        
        entries.
        
        .. attribute:: tokenringmlstatsentry
        
        	A collection of Mac\-Layer statistics kept for a particular Token Ring interface
        	**type**\: list of :py:class:`TokenRingMLStatsEntry <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.TokenRingMLStatsTable.TokenRingMLStatsEntry>`
        
        

        """

        _prefix = 'token-ring'

        def __init__(self):
            self.parent = None
            self.tokenringmlstatsentry = YList()
            self.tokenringmlstatsentry.parent = self
            self.tokenringmlstatsentry.name = 'tokenringmlstatsentry'


        class TokenRingMLStatsEntry(object):
            """
            A collection of Mac\-Layer statistics kept for a
            particular Token Ring interface.
            
            .. attribute:: tokenringmlstatsindex
            
            	The value of this object uniquely identifies this tokenRingMLStats entry
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: tokenringmlstatsaborterrors
            
            	The total number of abort delimiters reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsacerrors
            
            	The total number of AC (Address Copied)  errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsbeaconevents
            
            	The total number of times that the ring enters a beaconing state (beaconFrameStreamingState, beaconBitStreamingState,      beaconSetRecoveryModeState, or beaconRingSignalLossState) from a non\-beaconing state.  Note that a change of the source address of the beacon packet does not constitute a new beacon event
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsbeaconpkts
            
            	The total number of beacon MAC packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsbeacontime
            
            	The total amount of time that the ring has been in the beaconing state
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: tokenringmlstatsbursterrors
            
            	The total number of burst errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsclaimtokenevents
            
            	The total number of times that the ring enters the claim token state from normal ring state or ring purge state.  The claim token state that comes in response to a beacon state is not counted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsclaimtokenpkts
            
            	The total number of claim token MAC packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatscongestionerrors
            
            	The total number of receive congestion errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatscreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsdatasource
            
            	This object identifies the source of the data that this tokenRingMLStats entry is configured to analyze.  This source can be any tokenRing interface on this device.  In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in MIB\-II [3], for the desired interface.  For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all error reports on the local network segment attached to the identified interface.  This object may not be modified if the associated tokenRingMLStatsStatus object is equal to valid(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: tokenringmlstatsdropevents
            
            	The total number of events in which packets were dropped by the probe due to lack of resources. Note that this number is not necessarily the number of packets dropped; it is just the number of times this condition has been detected.  This value is the same as the corresponding tokenRingPStatsDropEvents
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsdroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsframecopiederrors
            
            	The total number of frame copied errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsfrequencyerrors
            
            	The total number of frequency errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsinternalerrors
            
            	The total number of adapter internal errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatslineerrors
            
            	The total number of line errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatslostframeerrors
            
            	The total number of lost frame errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsmacoctets
            
            	The total number of octets of data in MAC packets (excluding those that were not good frames) received on the network (excluding framing bits but including FCS octets)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsmacpkts
            
            	The total number of MAC packets (excluding packets that were not good frames) received
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsnaunchanges
            
            	The total number of NAUN changes detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            .. attribute:: tokenringmlstatsringpollevents
            
            	The total number of ring poll events detected by the probe (i.e. the number of ring polls initiated by the active monitor that were detected)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsringpurgeevents
            
            	The total number of times that the ring enters the ring purge state from normal ring state.  The ring purge state that comes in response to the claim token or beacon state is not counted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsringpurgepkts
            
            	The total number of ring purge MAC packets detected by probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatssofterrorreports
            
            	The total number of soft error report frames detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringmlstatsstatus
            
            	The status of this tokenRingMLStats entry
            	**type**\: :py:class:`EntryStatus_Enum <ydk.models.token.TOKEN_RING_RMON_MIB.EntryStatus_Enum>`
            
            .. attribute:: tokenringmlstatstokenerrors
            
            	The total number of token errors reported in error reporting packets detected by the probe
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'token-ring'

            def __init__(self):
                self.parent = None
                self.tokenringmlstatsindex = None
                self.tokenringmlstatsaborterrors = None
                self.tokenringmlstatsacerrors = None
                self.tokenringmlstatsbeaconevents = None
                self.tokenringmlstatsbeaconpkts = None
                self.tokenringmlstatsbeacontime = None
                self.tokenringmlstatsbursterrors = None
                self.tokenringmlstatsclaimtokenevents = None
                self.tokenringmlstatsclaimtokenpkts = None
                self.tokenringmlstatscongestionerrors = None
                self.tokenringmlstatscreatetime = None
                self.tokenringmlstatsdatasource = None
                self.tokenringmlstatsdropevents = None
                self.tokenringmlstatsdroppedframes = None
                self.tokenringmlstatsframecopiederrors = None
                self.tokenringmlstatsfrequencyerrors = None
                self.tokenringmlstatsinternalerrors = None
                self.tokenringmlstatslineerrors = None
                self.tokenringmlstatslostframeerrors = None
                self.tokenringmlstatsmacoctets = None
                self.tokenringmlstatsmacpkts = None
                self.tokenringmlstatsnaunchanges = None
                self.tokenringmlstatsowner = None
                self.tokenringmlstatsringpollevents = None
                self.tokenringmlstatsringpurgeevents = None
                self.tokenringmlstatsringpurgepkts = None
                self.tokenringmlstatssofterrorreports = None
                self.tokenringmlstatsstatus = None
                self.tokenringmlstatstokenerrors = None

            @property
            def _common_path(self):
                if self.tokenringmlstatsindex is None:
                    raise YPYDataValidationError('Key property tokenringmlstatsindex is None')

                return '/TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/TOKEN-RING-RMON-MIB:tokenRingMLStatsTable/TOKEN-RING-RMON-MIB:tokenRingMLStatsEntry[TOKEN-RING-RMON-MIB:tokenRingMLStatsIndex = ' + str(self.tokenringmlstatsindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.tokenringmlstatsindex is not None:
                    return True

                if self.tokenringmlstatsaborterrors is not None:
                    return True

                if self.tokenringmlstatsacerrors is not None:
                    return True

                if self.tokenringmlstatsbeaconevents is not None:
                    return True

                if self.tokenringmlstatsbeaconpkts is not None:
                    return True

                if self.tokenringmlstatsbeacontime is not None:
                    return True

                if self.tokenringmlstatsbursterrors is not None:
                    return True

                if self.tokenringmlstatsclaimtokenevents is not None:
                    return True

                if self.tokenringmlstatsclaimtokenpkts is not None:
                    return True

                if self.tokenringmlstatscongestionerrors is not None:
                    return True

                if self.tokenringmlstatscreatetime is not None:
                    return True

                if self.tokenringmlstatsdatasource is not None:
                    return True

                if self.tokenringmlstatsdropevents is not None:
                    return True

                if self.tokenringmlstatsdroppedframes is not None:
                    return True

                if self.tokenringmlstatsframecopiederrors is not None:
                    return True

                if self.tokenringmlstatsfrequencyerrors is not None:
                    return True

                if self.tokenringmlstatsinternalerrors is not None:
                    return True

                if self.tokenringmlstatslineerrors is not None:
                    return True

                if self.tokenringmlstatslostframeerrors is not None:
                    return True

                if self.tokenringmlstatsmacoctets is not None:
                    return True

                if self.tokenringmlstatsmacpkts is not None:
                    return True

                if self.tokenringmlstatsnaunchanges is not None:
                    return True

                if self.tokenringmlstatsowner is not None:
                    return True

                if self.tokenringmlstatsringpollevents is not None:
                    return True

                if self.tokenringmlstatsringpurgeevents is not None:
                    return True

                if self.tokenringmlstatsringpurgepkts is not None:
                    return True

                if self.tokenringmlstatssofterrorreports is not None:
                    return True

                if self.tokenringmlstatsstatus is not None:
                    return True

                if self.tokenringmlstatstokenerrors is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
                return meta._meta_table['TOKENRINGRMONMIB.TokenRingMLStatsTable.TokenRingMLStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/TOKEN-RING-RMON-MIB:tokenRingMLStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.tokenringmlstatsentry is not None:
                for child_ref in self.tokenringmlstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
            return meta._meta_table['TOKENRINGRMONMIB.TokenRingMLStatsTable']['meta_info']


    class TokenRingPHistoryTable(object):
        """
        A list of promiscuous Token Ring statistics
        entries.
        
        .. attribute:: tokenringphistoryentry
        
        	A collection of promiscuous statistics kept for a particular Token Ring interface
        	**type**\: list of :py:class:`TokenRingPHistoryEntry <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.TokenRingPHistoryTable.TokenRingPHistoryEntry>`
        
        

        """

        _prefix = 'token-ring'

        def __init__(self):
            self.parent = None
            self.tokenringphistoryentry = YList()
            self.tokenringphistoryentry.parent = self
            self.tokenringphistoryentry.name = 'tokenringphistoryentry'


        class TokenRingPHistoryEntry(object):
            """
            A collection of promiscuous statistics kept for a
            particular Token Ring interface.
            
            .. attribute:: tokenringphistoryindex
            
            	The history of which this entry is a part.  The history identified by a particular value of this index is the same history as identified by the same value of historyControlIndex
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: tokenringphistorysampleindex
            
            	An index that uniquely identifies the particular sample this entry represents among all samples associated with the same historyControlEntry. This index starts at 1 and increases by one as each new sample is taken
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: tokenringphistorydatabroadcastpkts
            
            	The total number of good non\-MAC frames received during this sampling interval that were directed to an LLC broadcast address (0xFFFFFFFFFFFF or 0xC000FFFFFFFF)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatamulticastpkts
            
            	The total number of good non\-MAC frames received during this sampling interval that were directed to a local or global multicast or functional address.  Note that this number does not include packets directed to the broadcast address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydataoctets
            
            	The total number of octets of data in good frames received on the network (excluding framing bits but including FCS octets) in non\-MAC packets during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts
            
            	The total number of good non\-MAC frames received during this sampling interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts1024to2047octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 1024 and 2047 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts128to255octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 128 and 255 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts18to63octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 18 and 63 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts2048to4095octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 2048 and 4095 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts256to511octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between      256 and 511 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts4096to8191octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 4096 and 8191 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts512to1023octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 512 and 1023 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts64to127octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 64 and 127 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapkts8192to18000octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were between 8192 and 18000 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydatapktsgreaterthan18000octets
            
            	The total number of good non\-MAC frames received during this sampling interval that were greater than 18000 octets in length, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistorydropevents
            
            	The total number of events in which packets were dropped by the probe due to lack of resources during this sampling interval.  Note that this number is not necessarily the number of packets dropped, it is just the number of times this condition has been detected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringphistoryintervalstart
            
            	The value of sysUpTime at the start of the interval over which this sample was measured.  If the probe keeps track of the time of day, it should start the first sample of the history at a time such that when the next hour of the day begins, a sample is started at that instant.  Note that following this rule may require the probe to delay collecting the first sample of the history, as each sample must be of the same interval.  Also note that the sample which is currently being collected is not accessible in this table until the end of its interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'token-ring'

            def __init__(self):
                self.parent = None
                self.tokenringphistoryindex = None
                self.tokenringphistorysampleindex = None
                self.tokenringphistorydatabroadcastpkts = None
                self.tokenringphistorydatamulticastpkts = None
                self.tokenringphistorydataoctets = None
                self.tokenringphistorydatapkts = None
                self.tokenringphistorydatapkts1024to2047octets = None
                self.tokenringphistorydatapkts128to255octets = None
                self.tokenringphistorydatapkts18to63octets = None
                self.tokenringphistorydatapkts2048to4095octets = None
                self.tokenringphistorydatapkts256to511octets = None
                self.tokenringphistorydatapkts4096to8191octets = None
                self.tokenringphistorydatapkts512to1023octets = None
                self.tokenringphistorydatapkts64to127octets = None
                self.tokenringphistorydatapkts8192to18000octets = None
                self.tokenringphistorydatapktsgreaterthan18000octets = None
                self.tokenringphistorydropevents = None
                self.tokenringphistoryintervalstart = None

            @property
            def _common_path(self):
                if self.tokenringphistoryindex is None:
                    raise YPYDataValidationError('Key property tokenringphistoryindex is None')
                if self.tokenringphistorysampleindex is None:
                    raise YPYDataValidationError('Key property tokenringphistorysampleindex is None')

                return '/TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/TOKEN-RING-RMON-MIB:tokenRingPHistoryTable/TOKEN-RING-RMON-MIB:tokenRingPHistoryEntry[TOKEN-RING-RMON-MIB:tokenRingPHistoryIndex = ' + str(self.tokenringphistoryindex) + '][TOKEN-RING-RMON-MIB:tokenRingPHistorySampleIndex = ' + str(self.tokenringphistorysampleindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.tokenringphistoryindex is not None:
                    return True

                if self.tokenringphistorysampleindex is not None:
                    return True

                if self.tokenringphistorydatabroadcastpkts is not None:
                    return True

                if self.tokenringphistorydatamulticastpkts is not None:
                    return True

                if self.tokenringphistorydataoctets is not None:
                    return True

                if self.tokenringphistorydatapkts is not None:
                    return True

                if self.tokenringphistorydatapkts1024to2047octets is not None:
                    return True

                if self.tokenringphistorydatapkts128to255octets is not None:
                    return True

                if self.tokenringphistorydatapkts18to63octets is not None:
                    return True

                if self.tokenringphistorydatapkts2048to4095octets is not None:
                    return True

                if self.tokenringphistorydatapkts256to511octets is not None:
                    return True

                if self.tokenringphistorydatapkts4096to8191octets is not None:
                    return True

                if self.tokenringphistorydatapkts512to1023octets is not None:
                    return True

                if self.tokenringphistorydatapkts64to127octets is not None:
                    return True

                if self.tokenringphistorydatapkts8192to18000octets is not None:
                    return True

                if self.tokenringphistorydatapktsgreaterthan18000octets is not None:
                    return True

                if self.tokenringphistorydropevents is not None:
                    return True

                if self.tokenringphistoryintervalstart is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
                return meta._meta_table['TOKENRINGRMONMIB.TokenRingPHistoryTable.TokenRingPHistoryEntry']['meta_info']

        @property
        def _common_path(self):

            return '/TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/TOKEN-RING-RMON-MIB:tokenRingPHistoryTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.tokenringphistoryentry is not None:
                for child_ref in self.tokenringphistoryentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
            return meta._meta_table['TOKENRINGRMONMIB.TokenRingPHistoryTable']['meta_info']


    class TokenRingPStatsTable(object):
        """
        A list of promiscuous Token Ring statistics
        entries.
        
        .. attribute:: tokenringpstatsentry
        
        	A collection of promiscuous statistics kept for non\-MAC packets on a particular Token Ring interface
        	**type**\: list of :py:class:`TokenRingPStatsEntry <ydk.models.token.TOKEN_RING_RMON_MIB.TOKENRINGRMONMIB.TokenRingPStatsTable.TokenRingPStatsEntry>`
        
        

        """

        _prefix = 'token-ring'

        def __init__(self):
            self.parent = None
            self.tokenringpstatsentry = YList()
            self.tokenringpstatsentry.parent = self
            self.tokenringpstatsentry.name = 'tokenringpstatsentry'


        class TokenRingPStatsEntry(object):
            """
            A collection of promiscuous statistics kept for
            non\-MAC packets on a particular Token Ring
            interface.
            
            .. attribute:: tokenringpstatsindex
            
            	The value of this object uniquely identifies this tokenRingPStats entry
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: tokenringpstatscreatetime
            
            	The value of sysUpTime when this control entry was last activated. This can be used by the management station to ensure that the table has not been deleted and recreated between polls
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatabroadcastpkts
            
            	The total number of good non\-MAC frames received that were directed to an LLC broadcast address (0xFFFFFFFFFFFF or 0xC000FFFFFFFF)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatamulticastpkts
            
            	The total number of good non\-MAC frames received that were directed to a local or global multicast or functional address.  Note that this number does not include packets directed to the broadcast address
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdataoctets
            
            	The total number of octets of data in good frames received on the network (excluding framing bits but including FCS octets) in non\-MAC packets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts
            
            	The total number of non\-MAC packets in good frames.  received
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts1024to2047octets
            
            	The total number of good non\-MAC frames received that were between 1024 and 2047 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts128to255octets
            
            	The total number of good non\-MAC frames received that were between 128 and 255 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts18to63octets
            
            	The total number of good non\-MAC frames received that were between 18 and 63 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts2048to4095octets
            
            	The total number of good non\-MAC frames received that were between 2048 and 4095 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts256to511octets
            
            	The total number of good non\-MAC frames received that were between 256 and 511 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts4096to8191octets
            
            	The total number of good non\-MAC frames received that were between 4096 and 8191 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts512to1023octets
            
            	The total number of good non\-MAC frames received that were between 512 and 1023 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts64to127octets
            
            	The total number of good non\-MAC frames received that were between 64 and 127 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapkts8192to18000octets
            
            	The total number of good non\-MAC frames received that were between 8192 and 18000 octets in length inclusive, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatapktsgreaterthan18000octets
            
            	The total number of good non\-MAC frames received that were greater than 18000 octets in length, excluding framing bits but including FCS octets
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdatasource
            
            	This object identifies the source of the data that this tokenRingPStats entry is configured to analyze.  This source can be any tokenRing interface on this device.  In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in MIB\-II [3], for the desired interface.  For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1.  The statistics in this group reflect all non\-MAC packets on the local network segment attached to the identified interface.  This object may not be modified if the associated tokenRingPStatsStatus object is equal to valid(1)
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: tokenringpstatsdropevents
            
            	The total number of events in which packets were dropped by the probe due to lack of resources. Note that this number is not necessarily the number of packets dropped; it is just the number of times this condition has been detected.  This value is the same as the corresponding tokenRingMLStatsDropEvents
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsdroppedframes
            
            	The total number of frames which were received by the probe and therefore not accounted for in the \*StatsDropEvents, but for which the probe chose not to count for this entry for whatever reason.  Most often, this event occurs when the probe is out of some resources and decides to shed load from this collection.  This count does not include packets that were not counted because they had MAC\-layer errors.  Note that, unlike the dropEvents counter, this number is the exact number of frames dropped
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: tokenringpstatsowner
            
            	The entity that configured this entry and is therefore using the resources assigned to it
            	**type**\: str
            
            .. attribute:: tokenringpstatsstatus
            
            	The status of this tokenRingPStats entry
            	**type**\: :py:class:`EntryStatus_Enum <ydk.models.token.TOKEN_RING_RMON_MIB.EntryStatus_Enum>`
            
            

            """

            _prefix = 'token-ring'

            def __init__(self):
                self.parent = None
                self.tokenringpstatsindex = None
                self.tokenringpstatscreatetime = None
                self.tokenringpstatsdatabroadcastpkts = None
                self.tokenringpstatsdatamulticastpkts = None
                self.tokenringpstatsdataoctets = None
                self.tokenringpstatsdatapkts = None
                self.tokenringpstatsdatapkts1024to2047octets = None
                self.tokenringpstatsdatapkts128to255octets = None
                self.tokenringpstatsdatapkts18to63octets = None
                self.tokenringpstatsdatapkts2048to4095octets = None
                self.tokenringpstatsdatapkts256to511octets = None
                self.tokenringpstatsdatapkts4096to8191octets = None
                self.tokenringpstatsdatapkts512to1023octets = None
                self.tokenringpstatsdatapkts64to127octets = None
                self.tokenringpstatsdatapkts8192to18000octets = None
                self.tokenringpstatsdatapktsgreaterthan18000octets = None
                self.tokenringpstatsdatasource = None
                self.tokenringpstatsdropevents = None
                self.tokenringpstatsdroppedframes = None
                self.tokenringpstatsowner = None
                self.tokenringpstatsstatus = None

            @property
            def _common_path(self):
                if self.tokenringpstatsindex is None:
                    raise YPYDataValidationError('Key property tokenringpstatsindex is None')

                return '/TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/TOKEN-RING-RMON-MIB:tokenRingPStatsTable/TOKEN-RING-RMON-MIB:tokenRingPStatsEntry[TOKEN-RING-RMON-MIB:tokenRingPStatsIndex = ' + str(self.tokenringpstatsindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.tokenringpstatsindex is not None:
                    return True

                if self.tokenringpstatscreatetime is not None:
                    return True

                if self.tokenringpstatsdatabroadcastpkts is not None:
                    return True

                if self.tokenringpstatsdatamulticastpkts is not None:
                    return True

                if self.tokenringpstatsdataoctets is not None:
                    return True

                if self.tokenringpstatsdatapkts is not None:
                    return True

                if self.tokenringpstatsdatapkts1024to2047octets is not None:
                    return True

                if self.tokenringpstatsdatapkts128to255octets is not None:
                    return True

                if self.tokenringpstatsdatapkts18to63octets is not None:
                    return True

                if self.tokenringpstatsdatapkts2048to4095octets is not None:
                    return True

                if self.tokenringpstatsdatapkts256to511octets is not None:
                    return True

                if self.tokenringpstatsdatapkts4096to8191octets is not None:
                    return True

                if self.tokenringpstatsdatapkts512to1023octets is not None:
                    return True

                if self.tokenringpstatsdatapkts64to127octets is not None:
                    return True

                if self.tokenringpstatsdatapkts8192to18000octets is not None:
                    return True

                if self.tokenringpstatsdatapktsgreaterthan18000octets is not None:
                    return True

                if self.tokenringpstatsdatasource is not None:
                    return True

                if self.tokenringpstatsdropevents is not None:
                    return True

                if self.tokenringpstatsdroppedframes is not None:
                    return True

                if self.tokenringpstatsowner is not None:
                    return True

                if self.tokenringpstatsstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
                return meta._meta_table['TOKENRINGRMONMIB.TokenRingPStatsTable.TokenRingPStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB/TOKEN-RING-RMON-MIB:tokenRingPStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.tokenringpstatsentry is not None:
                for child_ref in self.tokenringpstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
            return meta._meta_table['TOKENRINGRMONMIB.TokenRingPStatsTable']['meta_info']

    @property
    def _common_path(self):

        return '/TOKEN-RING-RMON-MIB:TOKEN-RING-RMON-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.ringstationconfigcontroltable is not None and self.ringstationconfigcontroltable._has_data():
            return True

        if self.ringstationconfigcontroltable is not None and self.ringstationconfigcontroltable.is_presence():
            return True

        if self.ringstationconfigtable is not None and self.ringstationconfigtable._has_data():
            return True

        if self.ringstationconfigtable is not None and self.ringstationconfigtable.is_presence():
            return True

        if self.ringstationcontroltable is not None and self.ringstationcontroltable._has_data():
            return True

        if self.ringstationcontroltable is not None and self.ringstationcontroltable.is_presence():
            return True

        if self.ringstationordertable is not None and self.ringstationordertable._has_data():
            return True

        if self.ringstationordertable is not None and self.ringstationordertable.is_presence():
            return True

        if self.ringstationtable is not None and self.ringstationtable._has_data():
            return True

        if self.ringstationtable is not None and self.ringstationtable.is_presence():
            return True

        if self.sourceroutingstatstable is not None and self.sourceroutingstatstable._has_data():
            return True

        if self.sourceroutingstatstable is not None and self.sourceroutingstatstable.is_presence():
            return True

        if self.tokenringmlhistorytable is not None and self.tokenringmlhistorytable._has_data():
            return True

        if self.tokenringmlhistorytable is not None and self.tokenringmlhistorytable.is_presence():
            return True

        if self.tokenringmlstatstable is not None and self.tokenringmlstatstable._has_data():
            return True

        if self.tokenringmlstatstable is not None and self.tokenringmlstatstable.is_presence():
            return True

        if self.tokenringphistorytable is not None and self.tokenringphistorytable._has_data():
            return True

        if self.tokenringphistorytable is not None and self.tokenringphistorytable.is_presence():
            return True

        if self.tokenringpstatstable is not None and self.tokenringpstatstable._has_data():
            return True

        if self.tokenringpstatstable is not None and self.tokenringpstatstable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.token._meta import _TOKEN_RING_RMON_MIB as meta
        return meta._meta_table['TOKENRINGRMONMIB']['meta_info']



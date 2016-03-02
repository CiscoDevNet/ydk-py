""" PIM_MIB 

The MIB module for management of PIM routers.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum


class PIMMIB(object):
    """
    
    
    .. attribute:: pim
    
    	
    	**type**\: :py:class:`Pim <ydk.models.pim.PIM_MIB.PIMMIB.Pim>`
    
    .. attribute:: pimcandidaterptable
    
    	The (conceptual) table listing the IP multicast groups for which the local router is to advertise itself as a Candidate\-RP when the value of pimComponentCRPHoldTime is non\-zero.  If this table is empty, then the local router      will advertise itself as a Candidate\-RP for all groups (providing the value of pimComponentCRPHoldTime is non\- zero)
    	**type**\: :py:class:`PimCandidateRPTable <ydk.models.pim.PIM_MIB.PIMMIB.PimCandidateRPTable>`
    
    .. attribute:: pimcomponenttable
    
    	The (conceptual) table containing objects specific to a PIM domain.  One row exists for each domain to which the router is connected.  A PIM\-SM domain is defined as an area of the network over which Bootstrap messages are forwarded. Typically, a PIM\-SM router will be a member of exactly one domain.  This table also supports, however, routers which may form a border between two PIM\-SM domains and do not forward Bootstrap messages between them
    	**type**\: :py:class:`PimComponentTable <ydk.models.pim.PIM_MIB.PIMMIB.PimComponentTable>`
    
    .. attribute:: piminterfacetable
    
    	The (conceptual) table listing the router's PIM interfaces. IGMP and PIM are enabled on all interfaces listed in this table
    	**type**\: :py:class:`PimInterfaceTable <ydk.models.pim.PIM_MIB.PIMMIB.PimInterfaceTable>`
    
    .. attribute:: pimipmroutenexthoptable
    
    	The (conceptual) table listing PIM\-specific information on a subset of the rows of the ipMRouteNextHopTable defined in the IP Multicast MIB
    	**type**\: :py:class:`PimIpMRouteNextHopTable <ydk.models.pim.PIM_MIB.PIMMIB.PimIpMRouteNextHopTable>`
    
    .. attribute:: pimipmroutetable
    
    	The (conceptual) table listing PIM\-specific information on a subset of the rows of the ipMRouteTable defined in the IP Multicast MIB
    	**type**\: :py:class:`PimIpMRouteTable <ydk.models.pim.PIM_MIB.PIMMIB.PimIpMRouteTable>`
    
    .. attribute:: pimneighbortable
    
    	The (conceptual) table listing the router's PIM neighbors
    	**type**\: :py:class:`PimNeighborTable <ydk.models.pim.PIM_MIB.PIMMIB.PimNeighborTable>`
    
    .. attribute:: pimrpsettable
    
    	The (conceptual) table listing PIM information for candidate Rendezvous Points (RPs) for IP multicast groups. When the local router is the BSR, this information is obtained from received Candidate\-RP\-Advertisements.  When the local router is not the BSR, this information is obtained from received RP\-Set messages
    	**type**\: :py:class:`PimRPSetTable <ydk.models.pim.PIM_MIB.PIMMIB.PimRPSetTable>`
    
    .. attribute:: pimrptable
    
    	The (conceptual) table listing PIM version 1 information for the Rendezvous Points (RPs) for IP multicast groups. This table is deprecated since its function is replaced by the pimRPSetTable for PIM version 2
    	**type**\: :py:class:`PimRPTable <ydk.models.pim.PIM_MIB.PIMMIB.PimRPTable>`
    
    

    """

    _prefix = 'pim-mib'
    _revision = '2000-09-28'

    def __init__(self):
        self.pim = PIMMIB.Pim()
        self.pim.parent = self
        self.pimcandidaterptable = PIMMIB.PimCandidateRPTable()
        self.pimcandidaterptable.parent = self
        self.pimcomponenttable = PIMMIB.PimComponentTable()
        self.pimcomponenttable.parent = self
        self.piminterfacetable = PIMMIB.PimInterfaceTable()
        self.piminterfacetable.parent = self
        self.pimipmroutenexthoptable = PIMMIB.PimIpMRouteNextHopTable()
        self.pimipmroutenexthoptable.parent = self
        self.pimipmroutetable = PIMMIB.PimIpMRouteTable()
        self.pimipmroutetable.parent = self
        self.pimneighbortable = PIMMIB.PimNeighborTable()
        self.pimneighbortable.parent = self
        self.pimrpsettable = PIMMIB.PimRPSetTable()
        self.pimrpsettable.parent = self
        self.pimrptable = PIMMIB.PimRPTable()
        self.pimrptable.parent = self


    class Pim(object):
        """
        
        
        .. attribute:: pimjoinpruneinterval
        
        	The default interval at which periodic PIM\-SM Join/Prune messages are to be sent
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'pim-mib'
        _revision = '2000-09-28'

        def __init__(self):
            self.parent = None
            self.pimjoinpruneinterval = None

        @property
        def _common_path(self):

            return '/PIM-MIB:PIM-MIB/PIM-MIB:pim'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.pimjoinpruneinterval is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.pim._meta import _PIM_MIB as meta
            return meta._meta_table['PIMMIB.Pim']['meta_info']


    class PimCandidateRPTable(object):
        """
        The (conceptual) table listing the IP multicast groups for
        which the local router is to advertise itself as a
        Candidate\-RP when the value of pimComponentCRPHoldTime is
        non\-zero.  If this table is empty, then the local router
        
        
        
        
        
        will advertise itself as a Candidate\-RP for all groups
        (providing the value of pimComponentCRPHoldTime is non\-
        zero).
        
        .. attribute:: pimcandidaterpentry
        
        	An entry (conceptual row) in the pimCandidateRPTable
        	**type**\: list of :py:class:`PimCandidateRPEntry <ydk.models.pim.PIM_MIB.PIMMIB.PimCandidateRPTable.PimCandidateRPEntry>`
        
        

        """

        _prefix = 'pim-mib'
        _revision = '2000-09-28'

        def __init__(self):
            self.parent = None
            self.pimcandidaterpentry = YList()
            self.pimcandidaterpentry.parent = self
            self.pimcandidaterpentry.name = 'pimcandidaterpentry'


        class PimCandidateRPEntry(object):
            """
            An entry (conceptual row) in the pimCandidateRPTable.
            
            .. attribute:: pimcandidaterpgroupaddress
            
            	The IP multicast group address which, when combined with pimCandidateRPGroupMask, identifies a group prefix for which the local router will advertise itself as a Candidate\-RP
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimcandidaterpgroupmask
            
            	The multicast group address mask which, when combined with pimCandidateRPGroupMask, identifies a group prefix for which the local router will advertise itself as a Candidate\-RP
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimcandidaterpaddress
            
            	The (unicast) address of the interface which will be      advertised as a Candidate\-RP
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimcandidaterprowstatus
            
            	The status of this row, by which new entries may be created, or old entries deleted from this table
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'pim-mib'
            _revision = '2000-09-28'

            def __init__(self):
                self.parent = None
                self.pimcandidaterpgroupaddress = None
                self.pimcandidaterpgroupmask = None
                self.pimcandidaterpaddress = None
                self.pimcandidaterprowstatus = None

            @property
            def _common_path(self):
                if self.pimcandidaterpgroupaddress is None:
                    raise YPYDataValidationError('Key property pimcandidaterpgroupaddress is None')
                if self.pimcandidaterpgroupmask is None:
                    raise YPYDataValidationError('Key property pimcandidaterpgroupmask is None')

                return '/PIM-MIB:PIM-MIB/PIM-MIB:pimCandidateRPTable/PIM-MIB:pimCandidateRPEntry[PIM-MIB:pimCandidateRPGroupAddress = ' + str(self.pimcandidaterpgroupaddress) + '][PIM-MIB:pimCandidateRPGroupMask = ' + str(self.pimcandidaterpgroupmask) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.pimcandidaterpgroupaddress is not None:
                    return True

                if self.pimcandidaterpgroupmask is not None:
                    return True

                if self.pimcandidaterpaddress is not None:
                    return True

                if self.pimcandidaterprowstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.pim._meta import _PIM_MIB as meta
                return meta._meta_table['PIMMIB.PimCandidateRPTable.PimCandidateRPEntry']['meta_info']

        @property
        def _common_path(self):

            return '/PIM-MIB:PIM-MIB/PIM-MIB:pimCandidateRPTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.pimcandidaterpentry is not None:
                for child_ref in self.pimcandidaterpentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.pim._meta import _PIM_MIB as meta
            return meta._meta_table['PIMMIB.PimCandidateRPTable']['meta_info']


    class PimComponentTable(object):
        """
        The (conceptual) table containing objects specific to a PIM
        domain.  One row exists for each domain to which the router
        is connected.  A PIM\-SM domain is defined as an area of the
        network over which Bootstrap messages are forwarded.
        Typically, a PIM\-SM router will be a member of exactly one
        domain.  This table also supports, however, routers which
        may form a border between two PIM\-SM domains and do not
        forward Bootstrap messages between them.
        
        .. attribute:: pimcomponententry
        
        	An entry (conceptual row) in the pimComponentTable
        	**type**\: list of :py:class:`PimComponentEntry <ydk.models.pim.PIM_MIB.PIMMIB.PimComponentTable.PimComponentEntry>`
        
        

        """

        _prefix = 'pim-mib'
        _revision = '2000-09-28'

        def __init__(self):
            self.parent = None
            self.pimcomponententry = YList()
            self.pimcomponententry.parent = self
            self.pimcomponententry.name = 'pimcomponententry'


        class PimComponentEntry(object):
            """
            An entry (conceptual row) in the pimComponentTable.
            
            .. attribute:: pimcomponentindex
            
            	A number uniquely identifying the component.  Each protocol instance connected to a separate domain should have a different index value.  Routers that only support membership in a single PIM\-SM domain should use a pimComponentIndex value of 1
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: pimcomponentbsraddress
            
            	The IP address of the bootstrap router (BSR) for the local PIM region
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimcomponentbsrexpirytime
            
            	The minimum time remaining before the bootstrap router in the local domain will be declared down.  For candidate BSRs, this is the time until the component sends an RP\-Set message.  For other routers, this is the time until it may accept an RP\-Set message from a lower candidate BSR
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pimcomponentcrpholdtime
            
            	The holdtime of the component when it is a candidate RP in the local domain.  The value of 0 is used to indicate that the local system is not a Candidate\-RP
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: pimcomponentstatus
            
            	The status of this entry.  Creating the entry creates another protocol instance; destroying the entry disables a protocol instance
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'pim-mib'
            _revision = '2000-09-28'

            def __init__(self):
                self.parent = None
                self.pimcomponentindex = None
                self.pimcomponentbsraddress = None
                self.pimcomponentbsrexpirytime = None
                self.pimcomponentcrpholdtime = None
                self.pimcomponentstatus = None

            @property
            def _common_path(self):
                if self.pimcomponentindex is None:
                    raise YPYDataValidationError('Key property pimcomponentindex is None')

                return '/PIM-MIB:PIM-MIB/PIM-MIB:pimComponentTable/PIM-MIB:pimComponentEntry[PIM-MIB:pimComponentIndex = ' + str(self.pimcomponentindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.pimcomponentindex is not None:
                    return True

                if self.pimcomponentbsraddress is not None:
                    return True

                if self.pimcomponentbsrexpirytime is not None:
                    return True

                if self.pimcomponentcrpholdtime is not None:
                    return True

                if self.pimcomponentstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.pim._meta import _PIM_MIB as meta
                return meta._meta_table['PIMMIB.PimComponentTable.PimComponentEntry']['meta_info']

        @property
        def _common_path(self):

            return '/PIM-MIB:PIM-MIB/PIM-MIB:pimComponentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.pimcomponententry is not None:
                for child_ref in self.pimcomponententry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.pim._meta import _PIM_MIB as meta
            return meta._meta_table['PIMMIB.PimComponentTable']['meta_info']


    class PimInterfaceTable(object):
        """
        The (conceptual) table listing the router's PIM interfaces.
        IGMP and PIM are enabled on all interfaces listed in this
        table.
        
        .. attribute:: piminterfaceentry
        
        	An entry (conceptual row) in the pimInterfaceTable
        	**type**\: list of :py:class:`PimInterfaceEntry <ydk.models.pim.PIM_MIB.PIMMIB.PimInterfaceTable.PimInterfaceEntry>`
        
        

        """

        _prefix = 'pim-mib'
        _revision = '2000-09-28'

        def __init__(self):
            self.parent = None
            self.piminterfaceentry = YList()
            self.piminterfaceentry.parent = self
            self.piminterfaceentry.name = 'piminterfaceentry'


        class PimInterfaceEntry(object):
            """
            An entry (conceptual row) in the pimInterfaceTable.
            
            .. attribute:: piminterfaceifindex
            
            	The ifIndex value of this PIM interface
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: piminterfaceaddress
            
            	The IP address of the PIM interface
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: piminterfacecbsrpreference
            
            	The preference value for the local interface as a candidate bootstrap router.  The value of \-1 is used to indicate that the local interface is not a candidate BSR interface
            	**type**\: int
            
            	**range:** \-1..255
            
            .. attribute:: piminterfacedr
            
            	The Designated Router on this PIM interface.  For point\-to\- point interfaces, this object has the value 0.0.0.0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: piminterfacehellointerval
            
            	The frequency at which PIM Hello messages are transmitted on this interface
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: piminterfacejoinpruneinterval
            
            	The frequency at which PIM Join/Prune messages are transmitted on this PIM interface.  The default value of this object is the pimJoinPruneInterval
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: piminterfacemode
            
            	The configured mode of this PIM interface.  A value of sparseDense is only valid for PIMv1
            	**type**\: :py:class:`PimInterfaceMode_Enum <ydk.models.pim.PIM_MIB.PIMMIB.PimInterfaceTable.PimInterfaceEntry.PimInterfaceMode_Enum>`
            
            .. attribute:: piminterfacenetmask
            
            	The network mask for the IP address of the PIM interface
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: piminterfacestatus
            
            	The status of this entry.  Creating the entry enables PIM on the interface; destroying the entry disables PIM on the interface
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'pim-mib'
            _revision = '2000-09-28'

            def __init__(self):
                self.parent = None
                self.piminterfaceifindex = None
                self.piminterfaceaddress = None
                self.piminterfacecbsrpreference = None
                self.piminterfacedr = None
                self.piminterfacehellointerval = None
                self.piminterfacejoinpruneinterval = None
                self.piminterfacemode = None
                self.piminterfacenetmask = None
                self.piminterfacestatus = None

            class PimInterfaceMode_Enum(Enum):
                """
                PimInterfaceMode_Enum

                The configured mode of this PIM interface.  A value of
                sparseDense is only valid for PIMv1.

                """

                DENSE = 1

                SPARSE = 2

                SPARSEDENSE = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.pim._meta import _PIM_MIB as meta
                    return meta._meta_table['PIMMIB.PimInterfaceTable.PimInterfaceEntry.PimInterfaceMode_Enum']


            @property
            def _common_path(self):
                if self.piminterfaceifindex is None:
                    raise YPYDataValidationError('Key property piminterfaceifindex is None')

                return '/PIM-MIB:PIM-MIB/PIM-MIB:pimInterfaceTable/PIM-MIB:pimInterfaceEntry[PIM-MIB:pimInterfaceIfIndex = ' + str(self.piminterfaceifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.piminterfaceifindex is not None:
                    return True

                if self.piminterfaceaddress is not None:
                    return True

                if self.piminterfacecbsrpreference is not None:
                    return True

                if self.piminterfacedr is not None:
                    return True

                if self.piminterfacehellointerval is not None:
                    return True

                if self.piminterfacejoinpruneinterval is not None:
                    return True

                if self.piminterfacemode is not None:
                    return True

                if self.piminterfacenetmask is not None:
                    return True

                if self.piminterfacestatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.pim._meta import _PIM_MIB as meta
                return meta._meta_table['PIMMIB.PimInterfaceTable.PimInterfaceEntry']['meta_info']

        @property
        def _common_path(self):

            return '/PIM-MIB:PIM-MIB/PIM-MIB:pimInterfaceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.piminterfaceentry is not None:
                for child_ref in self.piminterfaceentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.pim._meta import _PIM_MIB as meta
            return meta._meta_table['PIMMIB.PimInterfaceTable']['meta_info']


    class PimIpMRouteNextHopTable(object):
        """
        The (conceptual) table listing PIM\-specific information on
        a subset of the rows of the ipMRouteNextHopTable defined in
        the IP Multicast MIB.
        
        .. attribute:: pimipmroutenexthopentry
        
        	An entry (conceptual row) in the pimIpMRouteNextHopTable. There is one entry per entry in the ipMRouteNextHopTable whose interface is running PIM and whose ipMRouteNextHopState is pruned(1)
        	**type**\: list of :py:class:`PimIpMRouteNextHopEntry <ydk.models.pim.PIM_MIB.PIMMIB.PimIpMRouteNextHopTable.PimIpMRouteNextHopEntry>`
        
        

        """

        _prefix = 'pim-mib'
        _revision = '2000-09-28'

        def __init__(self):
            self.parent = None
            self.pimipmroutenexthopentry = YList()
            self.pimipmroutenexthopentry.parent = self
            self.pimipmroutenexthopentry.name = 'pimipmroutenexthopentry'


        class PimIpMRouteNextHopEntry(object):
            """
            An entry (conceptual row) in the pimIpMRouteNextHopTable.
            There is one entry per entry in the ipMRouteNextHopTable
            whose interface is running PIM and whose
            ipMRouteNextHopState is pruned(1).
            
            .. attribute:: ipmroutenexthopaddress
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmroutenexthopgroup
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmroutenexthopifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipmroutenexthopsource
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmroutenexthopsourcemask
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimipmroutenexthopprunereason
            
            	This object indicates why the downstream interface was pruned, whether in response to a PIM prune message or due to PIM Assert processing
            	**type**\: :py:class:`PimIpMRouteNextHopPruneReason_Enum <ydk.models.pim.PIM_MIB.PIMMIB.PimIpMRouteNextHopTable.PimIpMRouteNextHopEntry.PimIpMRouteNextHopPruneReason_Enum>`
            
            

            """

            _prefix = 'pim-mib'
            _revision = '2000-09-28'

            def __init__(self):
                self.parent = None
                self.ipmroutenexthopaddress = None
                self.ipmroutenexthopgroup = None
                self.ipmroutenexthopifindex = None
                self.ipmroutenexthopsource = None
                self.ipmroutenexthopsourcemask = None
                self.pimipmroutenexthopprunereason = None

            class PimIpMRouteNextHopPruneReason_Enum(Enum):
                """
                PimIpMRouteNextHopPruneReason_Enum

                This object indicates why the downstream interface was
                pruned, whether in response to a PIM prune message or due to
                PIM Assert processing.

                """

                OTHER = 1

                PRUNE = 2

                ASSERT = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.pim._meta import _PIM_MIB as meta
                    return meta._meta_table['PIMMIB.PimIpMRouteNextHopTable.PimIpMRouteNextHopEntry.PimIpMRouteNextHopPruneReason_Enum']


            @property
            def _common_path(self):
                if self.ipmroutenexthopaddress is None:
                    raise YPYDataValidationError('Key property ipmroutenexthopaddress is None')
                if self.ipmroutenexthopgroup is None:
                    raise YPYDataValidationError('Key property ipmroutenexthopgroup is None')
                if self.ipmroutenexthopifindex is None:
                    raise YPYDataValidationError('Key property ipmroutenexthopifindex is None')
                if self.ipmroutenexthopsource is None:
                    raise YPYDataValidationError('Key property ipmroutenexthopsource is None')
                if self.ipmroutenexthopsourcemask is None:
                    raise YPYDataValidationError('Key property ipmroutenexthopsourcemask is None')

                return '/PIM-MIB:PIM-MIB/PIM-MIB:pimIpMRouteNextHopTable/PIM-MIB:pimIpMRouteNextHopEntry[PIM-MIB:ipMRouteNextHopAddress = ' + str(self.ipmroutenexthopaddress) + '][PIM-MIB:ipMRouteNextHopGroup = ' + str(self.ipmroutenexthopgroup) + '][PIM-MIB:ipMRouteNextHopIfIndex = ' + str(self.ipmroutenexthopifindex) + '][PIM-MIB:ipMRouteNextHopSource = ' + str(self.ipmroutenexthopsource) + '][PIM-MIB:ipMRouteNextHopSourceMask = ' + str(self.ipmroutenexthopsourcemask) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ipmroutenexthopaddress is not None:
                    return True

                if self.ipmroutenexthopgroup is not None:
                    return True

                if self.ipmroutenexthopifindex is not None:
                    return True

                if self.ipmroutenexthopsource is not None:
                    return True

                if self.ipmroutenexthopsourcemask is not None:
                    return True

                if self.pimipmroutenexthopprunereason is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.pim._meta import _PIM_MIB as meta
                return meta._meta_table['PIMMIB.PimIpMRouteNextHopTable.PimIpMRouteNextHopEntry']['meta_info']

        @property
        def _common_path(self):

            return '/PIM-MIB:PIM-MIB/PIM-MIB:pimIpMRouteNextHopTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.pimipmroutenexthopentry is not None:
                for child_ref in self.pimipmroutenexthopentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.pim._meta import _PIM_MIB as meta
            return meta._meta_table['PIMMIB.PimIpMRouteNextHopTable']['meta_info']


    class PimIpMRouteTable(object):
        """
        The (conceptual) table listing PIM\-specific information on
        a subset of the rows of the ipMRouteTable defined in the IP
        Multicast MIB.
        
        .. attribute:: pimipmrouteentry
        
        	An entry (conceptual row) in the pimIpMRouteTable.  There is one entry per entry in the ipMRouteTable whose incoming interface is running PIM
        	**type**\: list of :py:class:`PimIpMRouteEntry <ydk.models.pim.PIM_MIB.PIMMIB.PimIpMRouteTable.PimIpMRouteEntry>`
        
        

        """

        _prefix = 'pim-mib'
        _revision = '2000-09-28'

        def __init__(self):
            self.parent = None
            self.pimipmrouteentry = YList()
            self.pimipmrouteentry.parent = self
            self.pimipmrouteentry.name = 'pimipmrouteentry'


        class PimIpMRouteEntry(object):
            """
            An entry (conceptual row) in the pimIpMRouteTable.  There
            is one entry per entry in the ipMRouteTable whose incoming
            interface is running PIM.
            
            .. attribute:: ipmroutegroup
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmroutesource
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ipmroutesourcemask
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimipmrouteassertmetric
            
            	The metric advertised by the assert winner on the upstream interface, or 0 if no such assert is in received
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: pimipmrouteassertmetricpref
            
            	The preference advertised by the assert winner on the upstream interface, or 0 if no such assert is in effect
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: pimipmrouteassertrptbit
            
            	The value of the RPT\-bit advertised by the assert winner on the upstream interface, or false if no such assert is in effect
            	**type**\: bool
            
            .. attribute:: pimipmrouteflags
            
            	This object describes PIM\-specific flags related to a multicast state entry.  See the PIM Sparse Mode specification for the meaning of the RPT and SPT bits
            	**type**\: str
            
            	**range:** 1
            
            .. attribute:: pimipmrouteupstreamasserttimer
            
            	The time remaining before the router changes its upstream neighbor back to its RPF neighbor.  This timer is called the Assert timer in the PIM Sparse and Dense mode specification.      A value of 0 indicates that no Assert has changed the upstream neighbor away from the RPF neighbor
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'pim-mib'
            _revision = '2000-09-28'

            def __init__(self):
                self.parent = None
                self.ipmroutegroup = None
                self.ipmroutesource = None
                self.ipmroutesourcemask = None
                self.pimipmrouteassertmetric = None
                self.pimipmrouteassertmetricpref = None
                self.pimipmrouteassertrptbit = None
                self.pimipmrouteflags = None
                self.pimipmrouteupstreamasserttimer = None

            @property
            def _common_path(self):
                if self.ipmroutegroup is None:
                    raise YPYDataValidationError('Key property ipmroutegroup is None')
                if self.ipmroutesource is None:
                    raise YPYDataValidationError('Key property ipmroutesource is None')
                if self.ipmroutesourcemask is None:
                    raise YPYDataValidationError('Key property ipmroutesourcemask is None')

                return '/PIM-MIB:PIM-MIB/PIM-MIB:pimIpMRouteTable/PIM-MIB:pimIpMRouteEntry[PIM-MIB:ipMRouteGroup = ' + str(self.ipmroutegroup) + '][PIM-MIB:ipMRouteSource = ' + str(self.ipmroutesource) + '][PIM-MIB:ipMRouteSourceMask = ' + str(self.ipmroutesourcemask) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ipmroutegroup is not None:
                    return True

                if self.ipmroutesource is not None:
                    return True

                if self.ipmroutesourcemask is not None:
                    return True

                if self.pimipmrouteassertmetric is not None:
                    return True

                if self.pimipmrouteassertmetricpref is not None:
                    return True

                if self.pimipmrouteassertrptbit is not None:
                    return True

                if self.pimipmrouteflags is not None:
                    return True

                if self.pimipmrouteupstreamasserttimer is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.pim._meta import _PIM_MIB as meta
                return meta._meta_table['PIMMIB.PimIpMRouteTable.PimIpMRouteEntry']['meta_info']

        @property
        def _common_path(self):

            return '/PIM-MIB:PIM-MIB/PIM-MIB:pimIpMRouteTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.pimipmrouteentry is not None:
                for child_ref in self.pimipmrouteentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.pim._meta import _PIM_MIB as meta
            return meta._meta_table['PIMMIB.PimIpMRouteTable']['meta_info']


    class PimNeighborTable(object):
        """
        The (conceptual) table listing the router's PIM neighbors.
        
        .. attribute:: pimneighborentry
        
        	An entry (conceptual row) in the pimNeighborTable
        	**type**\: list of :py:class:`PimNeighborEntry <ydk.models.pim.PIM_MIB.PIMMIB.PimNeighborTable.PimNeighborEntry>`
        
        

        """

        _prefix = 'pim-mib'
        _revision = '2000-09-28'

        def __init__(self):
            self.parent = None
            self.pimneighborentry = YList()
            self.pimneighborentry.parent = self
            self.pimneighborentry.name = 'pimneighborentry'


        class PimNeighborEntry(object):
            """
            An entry (conceptual row) in the pimNeighborTable.
            
            .. attribute:: pimneighboraddress
            
            	The IP address of the PIM neighbor for which this entry contains information
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimneighborexpirytime
            
            	The minimum time remaining before this PIM neighbor will be aged out
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pimneighborifindex
            
            	The value of ifIndex for the interface used to reach this PIM neighbor
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: pimneighbormode
            
            	The active PIM mode of this neighbor.  This object is deprecated for PIMv2 routers since all neighbors on the interface must be either dense or sparse as determined by the protocol running on the interface
            	**type**\: :py:class:`PimNeighborMode_Enum <ydk.models.pim.PIM_MIB.PIMMIB.PimNeighborTable.PimNeighborEntry.PimNeighborMode_Enum>`
            
            .. attribute:: pimneighboruptime
            
            	The time since this PIM neighbor (last) became a neighbor of the local router
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'pim-mib'
            _revision = '2000-09-28'

            def __init__(self):
                self.parent = None
                self.pimneighboraddress = None
                self.pimneighborexpirytime = None
                self.pimneighborifindex = None
                self.pimneighbormode = None
                self.pimneighboruptime = None

            class PimNeighborMode_Enum(Enum):
                """
                PimNeighborMode_Enum

                The active PIM mode of this neighbor.  This object is
                deprecated for PIMv2 routers since all neighbors on the
                interface must be either dense or sparse as determined by
                the protocol running on the interface.

                """

                DENSE = 1

                SPARSE = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.pim._meta import _PIM_MIB as meta
                    return meta._meta_table['PIMMIB.PimNeighborTable.PimNeighborEntry.PimNeighborMode_Enum']


            @property
            def _common_path(self):
                if self.pimneighboraddress is None:
                    raise YPYDataValidationError('Key property pimneighboraddress is None')

                return '/PIM-MIB:PIM-MIB/PIM-MIB:pimNeighborTable/PIM-MIB:pimNeighborEntry[PIM-MIB:pimNeighborAddress = ' + str(self.pimneighboraddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.pimneighboraddress is not None:
                    return True

                if self.pimneighborexpirytime is not None:
                    return True

                if self.pimneighborifindex is not None:
                    return True

                if self.pimneighbormode is not None:
                    return True

                if self.pimneighboruptime is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.pim._meta import _PIM_MIB as meta
                return meta._meta_table['PIMMIB.PimNeighborTable.PimNeighborEntry']['meta_info']

        @property
        def _common_path(self):

            return '/PIM-MIB:PIM-MIB/PIM-MIB:pimNeighborTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.pimneighborentry is not None:
                for child_ref in self.pimneighborentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.pim._meta import _PIM_MIB as meta
            return meta._meta_table['PIMMIB.PimNeighborTable']['meta_info']


    class PimRPSetTable(object):
        """
        The (conceptual) table listing PIM information for
        candidate Rendezvous Points (RPs) for IP multicast groups.
        When the local router is the BSR, this information is
        obtained from received Candidate\-RP\-Advertisements.  When
        the local router is not the BSR, this information is
        obtained from received RP\-Set messages.
        
        .. attribute:: pimrpsetentry
        
        	An entry (conceptual row) in the pimRPSetTable
        	**type**\: list of :py:class:`PimRPSetEntry <ydk.models.pim.PIM_MIB.PIMMIB.PimRPSetTable.PimRPSetEntry>`
        
        

        """

        _prefix = 'pim-mib'
        _revision = '2000-09-28'

        def __init__(self):
            self.parent = None
            self.pimrpsetentry = YList()
            self.pimrpsetentry.parent = self
            self.pimrpsetentry.name = 'pimrpsetentry'


        class PimRPSetEntry(object):
            """
            An entry (conceptual row) in the pimRPSetTable.
            
            .. attribute:: pimrpsetaddress
            
            	The IP address of the Candidate\-RP
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimrpsetcomponent
            
            	 A number uniquely identifying the component.  Each protocol instance connected to a separate domain should have a different index value
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: pimrpsetgroupaddress
            
            	The IP multicast group address which, when combined with pimRPSetGroupMask, gives the group prefix for which this entry contains information about the Candidate\-RP
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimrpsetgroupmask
            
            	The multicast group address mask which, when combined with pimRPSetGroupAddress, gives the group prefix for which this entry contains information about the Candidate\-RP
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimrpsetexpirytime
            
            	The minimum time remaining before the Candidate\-RP will be declared down.  If the local router is not the BSR, this value is 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pimrpsetholdtime
            
            	The holdtime of a Candidate\-RP.  If the local router is not the BSR, this value is 0
            	**type**\: int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'pim-mib'
            _revision = '2000-09-28'

            def __init__(self):
                self.parent = None
                self.pimrpsetaddress = None
                self.pimrpsetcomponent = None
                self.pimrpsetgroupaddress = None
                self.pimrpsetgroupmask = None
                self.pimrpsetexpirytime = None
                self.pimrpsetholdtime = None

            @property
            def _common_path(self):
                if self.pimrpsetaddress is None:
                    raise YPYDataValidationError('Key property pimrpsetaddress is None')
                if self.pimrpsetcomponent is None:
                    raise YPYDataValidationError('Key property pimrpsetcomponent is None')
                if self.pimrpsetgroupaddress is None:
                    raise YPYDataValidationError('Key property pimrpsetgroupaddress is None')
                if self.pimrpsetgroupmask is None:
                    raise YPYDataValidationError('Key property pimrpsetgroupmask is None')

                return '/PIM-MIB:PIM-MIB/PIM-MIB:pimRPSetTable/PIM-MIB:pimRPSetEntry[PIM-MIB:pimRPSetAddress = ' + str(self.pimrpsetaddress) + '][PIM-MIB:pimRPSetComponent = ' + str(self.pimrpsetcomponent) + '][PIM-MIB:pimRPSetGroupAddress = ' + str(self.pimrpsetgroupaddress) + '][PIM-MIB:pimRPSetGroupMask = ' + str(self.pimrpsetgroupmask) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.pimrpsetaddress is not None:
                    return True

                if self.pimrpsetcomponent is not None:
                    return True

                if self.pimrpsetgroupaddress is not None:
                    return True

                if self.pimrpsetgroupmask is not None:
                    return True

                if self.pimrpsetexpirytime is not None:
                    return True

                if self.pimrpsetholdtime is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.pim._meta import _PIM_MIB as meta
                return meta._meta_table['PIMMIB.PimRPSetTable.PimRPSetEntry']['meta_info']

        @property
        def _common_path(self):

            return '/PIM-MIB:PIM-MIB/PIM-MIB:pimRPSetTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.pimrpsetentry is not None:
                for child_ref in self.pimrpsetentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.pim._meta import _PIM_MIB as meta
            return meta._meta_table['PIMMIB.PimRPSetTable']['meta_info']


    class PimRPTable(object):
        """
        The (conceptual) table listing PIM version 1 information
        for the Rendezvous Points (RPs) for IP multicast groups.
        This table is deprecated since its function is replaced by
        the pimRPSetTable for PIM version 2.
        
        .. attribute:: pimrpentry
        
        	An entry (conceptual row) in the pimRPTable.  There is one entry per RP address for each IP multicast group
        	**type**\: list of :py:class:`PimRPEntry <ydk.models.pim.PIM_MIB.PIMMIB.PimRPTable.PimRPEntry>`
        
        

        """

        _prefix = 'pim-mib'
        _revision = '2000-09-28'

        def __init__(self):
            self.parent = None
            self.pimrpentry = YList()
            self.pimrpentry.parent = self
            self.pimrpentry.name = 'pimrpentry'


        class PimRPEntry(object):
            """
            An entry (conceptual row) in the pimRPTable.  There is one
            entry per RP address for each IP multicast group.
            
            .. attribute:: pimrpaddress
            
            	The unicast address of the RP
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimrpgroupaddress
            
            	The IP multicast group address for which this entry contains information about an RP
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimrplastchange
            
            	The value of sysUpTime at the time when the corresponding instance of pimRPState last changed its value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pimrprowstatus
            
            	The status of this row, by which new entries may be created, or old entries deleted from this table
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: pimrpstate
            
            	The state of the RP
            	**type**\: :py:class:`PimRPState_Enum <ydk.models.pim.PIM_MIB.PIMMIB.PimRPTable.PimRPEntry.PimRPState_Enum>`
            
            .. attribute:: pimrpstatetimer
            
            	The minimum time remaining before the next state change. When pimRPState is up, this is the minimum time which must expire until it can be declared down.  When pimRPState is down, this is the time until it will be declared up (in order to retry)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'pim-mib'
            _revision = '2000-09-28'

            def __init__(self):
                self.parent = None
                self.pimrpaddress = None
                self.pimrpgroupaddress = None
                self.pimrplastchange = None
                self.pimrprowstatus = None
                self.pimrpstate = None
                self.pimrpstatetimer = None

            class PimRPState_Enum(Enum):
                """
                PimRPState_Enum

                The state of the RP.

                """

                UP = 1

                DOWN = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.pim._meta import _PIM_MIB as meta
                    return meta._meta_table['PIMMIB.PimRPTable.PimRPEntry.PimRPState_Enum']


            @property
            def _common_path(self):
                if self.pimrpaddress is None:
                    raise YPYDataValidationError('Key property pimrpaddress is None')
                if self.pimrpgroupaddress is None:
                    raise YPYDataValidationError('Key property pimrpgroupaddress is None')

                return '/PIM-MIB:PIM-MIB/PIM-MIB:pimRPTable/PIM-MIB:pimRPEntry[PIM-MIB:pimRPAddress = ' + str(self.pimrpaddress) + '][PIM-MIB:pimRPGroupAddress = ' + str(self.pimrpgroupaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.pimrpaddress is not None:
                    return True

                if self.pimrpgroupaddress is not None:
                    return True

                if self.pimrplastchange is not None:
                    return True

                if self.pimrprowstatus is not None:
                    return True

                if self.pimrpstate is not None:
                    return True

                if self.pimrpstatetimer is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.pim._meta import _PIM_MIB as meta
                return meta._meta_table['PIMMIB.PimRPTable.PimRPEntry']['meta_info']

        @property
        def _common_path(self):

            return '/PIM-MIB:PIM-MIB/PIM-MIB:pimRPTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.pimrpentry is not None:
                for child_ref in self.pimrpentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.pim._meta import _PIM_MIB as meta
            return meta._meta_table['PIMMIB.PimRPTable']['meta_info']

    @property
    def _common_path(self):

        return '/PIM-MIB:PIM-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.pim is not None and self.pim._has_data():
            return True

        if self.pim is not None and self.pim.is_presence():
            return True

        if self.pimcandidaterptable is not None and self.pimcandidaterptable._has_data():
            return True

        if self.pimcandidaterptable is not None and self.pimcandidaterptable.is_presence():
            return True

        if self.pimcomponenttable is not None and self.pimcomponenttable._has_data():
            return True

        if self.pimcomponenttable is not None and self.pimcomponenttable.is_presence():
            return True

        if self.piminterfacetable is not None and self.piminterfacetable._has_data():
            return True

        if self.piminterfacetable is not None and self.piminterfacetable.is_presence():
            return True

        if self.pimipmroutenexthoptable is not None and self.pimipmroutenexthoptable._has_data():
            return True

        if self.pimipmroutenexthoptable is not None and self.pimipmroutenexthoptable.is_presence():
            return True

        if self.pimipmroutetable is not None and self.pimipmroutetable._has_data():
            return True

        if self.pimipmroutetable is not None and self.pimipmroutetable.is_presence():
            return True

        if self.pimneighbortable is not None and self.pimneighbortable._has_data():
            return True

        if self.pimneighbortable is not None and self.pimneighbortable.is_presence():
            return True

        if self.pimrpsettable is not None and self.pimrpsettable._has_data():
            return True

        if self.pimrpsettable is not None and self.pimrpsettable.is_presence():
            return True

        if self.pimrptable is not None and self.pimrptable._has_data():
            return True

        if self.pimrptable is not None and self.pimrptable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.pim._meta import _PIM_MIB as meta
        return meta._meta_table['PIMMIB']['meta_info']



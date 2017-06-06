""" PIM_MIB 

The MIB module for management of PIM routers.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class PimMib(object):
    """
    
    
    .. attribute:: pim
    
    	
    	**type**\:   :py:class:`Pim <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pim>`
    
    .. attribute:: pimcandidaterptable
    
    	The (conceptual) table listing the IP multicast groups for which the local router is to advertise itself as a Candidate\-RP when the value of pimComponentCRPHoldTime is non\-zero.  If this table is empty, then the local router      will advertise itself as a Candidate\-RP for all groups (providing the value of pimComponentCRPHoldTime is non\- zero)
    	**type**\:   :py:class:`Pimcandidaterptable <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimcandidaterptable>`
    
    .. attribute:: pimcomponenttable
    
    	The (conceptual) table containing objects specific to a PIM domain.  One row exists for each domain to which the router is connected.  A PIM\-SM domain is defined as an area of the network over which Bootstrap messages are forwarded. Typically, a PIM\-SM router will be a member of exactly one domain.  This table also supports, however, routers which may form a border between two PIM\-SM domains and do not forward Bootstrap messages between them
    	**type**\:   :py:class:`Pimcomponenttable <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimcomponenttable>`
    
    .. attribute:: piminterfacetable
    
    	The (conceptual) table listing the router's PIM interfaces. IGMP and PIM are enabled on all interfaces listed in this table
    	**type**\:   :py:class:`Piminterfacetable <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Piminterfacetable>`
    
    .. attribute:: pimipmroutenexthoptable
    
    	The (conceptual) table listing PIM\-specific information on a subset of the rows of the ipMRouteNextHopTable defined in the IP Multicast MIB
    	**type**\:   :py:class:`Pimipmroutenexthoptable <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimipmroutenexthoptable>`
    
    .. attribute:: pimipmroutetable
    
    	The (conceptual) table listing PIM\-specific information on a subset of the rows of the ipMRouteTable defined in the IP Multicast MIB
    	**type**\:   :py:class:`Pimipmroutetable <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimipmroutetable>`
    
    .. attribute:: pimneighbortable
    
    	The (conceptual) table listing the router's PIM neighbors
    	**type**\:   :py:class:`Pimneighbortable <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimneighbortable>`
    
    .. attribute:: pimrpsettable
    
    	The (conceptual) table listing PIM information for candidate Rendezvous Points (RPs) for IP multicast groups. When the local router is the BSR, this information is obtained from received Candidate\-RP\-Advertisements.  When the local router is not the BSR, this information is obtained from received RP\-Set messages
    	**type**\:   :py:class:`Pimrpsettable <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimrpsettable>`
    
    .. attribute:: pimrptable
    
    	The (conceptual) table listing PIM version 1 information for the Rendezvous Points (RPs) for IP multicast groups. This table is deprecated since its function is replaced by the pimRPSetTable for PIM version 2
    	**type**\:   :py:class:`Pimrptable <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimrptable>`
    
    	**status**\: deprecated
    
    

    """

    _prefix = 'PIM-MIB'
    _revision = '2000-09-28'

    def __init__(self):
        self.pim = PimMib.Pim()
        self.pim.parent = self
        self.pimcandidaterptable = PimMib.Pimcandidaterptable()
        self.pimcandidaterptable.parent = self
        self.pimcomponenttable = PimMib.Pimcomponenttable()
        self.pimcomponenttable.parent = self
        self.piminterfacetable = PimMib.Piminterfacetable()
        self.piminterfacetable.parent = self
        self.pimipmroutenexthoptable = PimMib.Pimipmroutenexthoptable()
        self.pimipmroutenexthoptable.parent = self
        self.pimipmroutetable = PimMib.Pimipmroutetable()
        self.pimipmroutetable.parent = self
        self.pimneighbortable = PimMib.Pimneighbortable()
        self.pimneighbortable.parent = self
        self.pimrpsettable = PimMib.Pimrpsettable()
        self.pimrpsettable.parent = self
        self.pimrptable = PimMib.Pimrptable()
        self.pimrptable.parent = self


    class Pim(object):
        """
        
        
        .. attribute:: pimjoinpruneinterval
        
        	The default interval at which periodic PIM\-SM Join/Prune messages are to be sent
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        	**units**\: seconds
        
        

        """

        _prefix = 'PIM-MIB'
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
            if self.pimjoinpruneinterval is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _PIM_MIB as meta
            return meta._meta_table['PimMib.Pim']['meta_info']


    class Piminterfacetable(object):
        """
        The (conceptual) table listing the router's PIM interfaces.
        IGMP and PIM are enabled on all interfaces listed in this
        table.
        
        .. attribute:: piminterfaceentry
        
        	An entry (conceptual row) in the pimInterfaceTable
        	**type**\: list of    :py:class:`Piminterfaceentry <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Piminterfacetable.Piminterfaceentry>`
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            self.parent = None
            self.piminterfaceentry = YList()
            self.piminterfaceentry.parent = self
            self.piminterfaceentry.name = 'piminterfaceentry'


        class Piminterfaceentry(object):
            """
            An entry (conceptual row) in the pimInterfaceTable.
            
            .. attribute:: piminterfaceifindex  <key>
            
            	The ifIndex value of this PIM interface
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: piminterfaceaddress
            
            	The IP address of the PIM interface
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: piminterfacecbsrpreference
            
            	The preference value for the local interface as a candidate bootstrap router.  The value of \-1 is used to indicate that the local interface is not a candidate BSR interface
            	**type**\:  int
            
            	**range:** \-1..255
            
            .. attribute:: piminterfacedr
            
            	The Designated Router on this PIM interface.  For point\-to\- point interfaces, this object has the value 0.0.0.0
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: piminterfacehellointerval
            
            	The frequency at which PIM Hello messages are transmitted on this interface
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: seconds
            
            .. attribute:: piminterfacejoinpruneinterval
            
            	The frequency at which PIM Join/Prune messages are transmitted on this PIM interface.  The default value of this object is the pimJoinPruneInterval
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: seconds
            
            .. attribute:: piminterfacemode
            
            	The configured mode of this PIM interface.  A value of sparseDense is only valid for PIMv1
            	**type**\:   :py:class:`PiminterfacemodeEnum <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Piminterfacetable.Piminterfaceentry.PiminterfacemodeEnum>`
            
            .. attribute:: piminterfacenetmask
            
            	The network mask for the IP address of the PIM interface
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: piminterfacestatus
            
            	The status of this entry.  Creating the entry enables PIM on the interface; destroying the entry disables PIM on the interface
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            

            """

            _prefix = 'PIM-MIB'
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

            class PiminterfacemodeEnum(Enum):
                """
                PiminterfacemodeEnum

                The configured mode of this PIM interface.  A value of

                sparseDense is only valid for PIMv1.

                .. data:: dense = 1

                .. data:: sparse = 2

                .. data:: sparseDense = 3

                """

                dense = 1

                sparse = 2

                sparseDense = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _PIM_MIB as meta
                    return meta._meta_table['PimMib.Piminterfacetable.Piminterfaceentry.PiminterfacemodeEnum']


            @property
            def _common_path(self):
                if self.piminterfaceifindex is None:
                    raise YPYModelError('Key property piminterfaceifindex is None')

                return '/PIM-MIB:PIM-MIB/PIM-MIB:pimInterfaceTable/PIM-MIB:pimInterfaceEntry[PIM-MIB:pimInterfaceIfIndex = ' + str(self.piminterfaceifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _PIM_MIB as meta
                return meta._meta_table['PimMib.Piminterfacetable.Piminterfaceentry']['meta_info']

        @property
        def _common_path(self):

            return '/PIM-MIB:PIM-MIB/PIM-MIB:pimInterfaceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.piminterfaceentry is not None:
                for child_ref in self.piminterfaceentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _PIM_MIB as meta
            return meta._meta_table['PimMib.Piminterfacetable']['meta_info']


    class Pimneighbortable(object):
        """
        The (conceptual) table listing the router's PIM neighbors.
        
        .. attribute:: pimneighborentry
        
        	An entry (conceptual row) in the pimNeighborTable
        	**type**\: list of    :py:class:`Pimneighborentry <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimneighbortable.Pimneighborentry>`
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            self.parent = None
            self.pimneighborentry = YList()
            self.pimneighborentry.parent = self
            self.pimneighborentry.name = 'pimneighborentry'


        class Pimneighborentry(object):
            """
            An entry (conceptual row) in the pimNeighborTable.
            
            .. attribute:: pimneighboraddress  <key>
            
            	The IP address of the PIM neighbor for which this entry contains information
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimneighborexpirytime
            
            	The minimum time remaining before this PIM neighbor will be aged out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pimneighborifindex
            
            	The value of ifIndex for the interface used to reach this PIM neighbor
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: pimneighbormode
            
            	The active PIM mode of this neighbor.  This object is deprecated for PIMv2 routers since all neighbors on the interface must be either dense or sparse as determined by the protocol running on the interface
            	**type**\:   :py:class:`PimneighbormodeEnum <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimneighbortable.Pimneighborentry.PimneighbormodeEnum>`
            
            	**status**\: deprecated
            
            .. attribute:: pimneighboruptime
            
            	The time since this PIM neighbor (last) became a neighbor of the local router
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'PIM-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                self.parent = None
                self.pimneighboraddress = None
                self.pimneighborexpirytime = None
                self.pimneighborifindex = None
                self.pimneighbormode = None
                self.pimneighboruptime = None

            class PimneighbormodeEnum(Enum):
                """
                PimneighbormodeEnum

                The active PIM mode of this neighbor.  This object is

                deprecated for PIMv2 routers since all neighbors on the

                interface must be either dense or sparse as determined by

                the protocol running on the interface.

                .. data:: dense = 1

                .. data:: sparse = 2

                """

                dense = 1

                sparse = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _PIM_MIB as meta
                    return meta._meta_table['PimMib.Pimneighbortable.Pimneighborentry.PimneighbormodeEnum']


            @property
            def _common_path(self):
                if self.pimneighboraddress is None:
                    raise YPYModelError('Key property pimneighboraddress is None')

                return '/PIM-MIB:PIM-MIB/PIM-MIB:pimNeighborTable/PIM-MIB:pimNeighborEntry[PIM-MIB:pimNeighborAddress = ' + str(self.pimneighboraddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _PIM_MIB as meta
                return meta._meta_table['PimMib.Pimneighbortable.Pimneighborentry']['meta_info']

        @property
        def _common_path(self):

            return '/PIM-MIB:PIM-MIB/PIM-MIB:pimNeighborTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.pimneighborentry is not None:
                for child_ref in self.pimneighborentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _PIM_MIB as meta
            return meta._meta_table['PimMib.Pimneighbortable']['meta_info']


    class Pimipmroutetable(object):
        """
        The (conceptual) table listing PIM\-specific information on
        a subset of the rows of the ipMRouteTable defined in the IP
        Multicast MIB.
        
        .. attribute:: pimipmrouteentry
        
        	An entry (conceptual row) in the pimIpMRouteTable.  There is one entry per entry in the ipMRouteTable whose incoming interface is running PIM
        	**type**\: list of    :py:class:`Pimipmrouteentry <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimipmroutetable.Pimipmrouteentry>`
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            self.parent = None
            self.pimipmrouteentry = YList()
            self.pimipmrouteentry.parent = self
            self.pimipmrouteentry.name = 'pimipmrouteentry'


        class Pimipmrouteentry(object):
            """
            An entry (conceptual row) in the pimIpMRouteTable.  There
            is one entry per entry in the ipMRouteTable whose incoming
            interface is running PIM.
            
            .. attribute:: ipmroutegroup  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ipmroutegroup <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutetable.Ipmrouteentry>`
            
            .. attribute:: ipmroutesource  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ipmroutesource <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutetable.Ipmrouteentry>`
            
            .. attribute:: ipmroutesourcemask  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ipmroutesourcemask <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutetable.Ipmrouteentry>`
            
            .. attribute:: pimipmrouteassertmetric
            
            	The metric advertised by the assert winner on the upstream interface, or 0 if no such assert is in received
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: pimipmrouteassertmetricpref
            
            	The preference advertised by the assert winner on the upstream interface, or 0 if no such assert is in effect
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: pimipmrouteassertrptbit
            
            	The value of the RPT\-bit advertised by the assert winner on the upstream interface, or false if no such assert is in effect
            	**type**\:  bool
            
            .. attribute:: pimipmrouteflags
            
            	This object describes PIM\-specific flags related to a multicast state entry.  See the PIM Sparse Mode specification for the meaning of the RPT and SPT bits
            	**type**\:  str
            
            	**length:** 1
            
            .. attribute:: pimipmrouteupstreamasserttimer
            
            	The time remaining before the router changes its upstream neighbor back to its RPF neighbor.  This timer is called the Assert timer in the PIM Sparse and Dense mode specification.      A value of 0 indicates that no Assert has changed the upstream neighbor away from the RPF neighbor
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'PIM-MIB'
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
                    raise YPYModelError('Key property ipmroutegroup is None')
                if self.ipmroutesource is None:
                    raise YPYModelError('Key property ipmroutesource is None')
                if self.ipmroutesourcemask is None:
                    raise YPYModelError('Key property ipmroutesourcemask is None')

                return '/PIM-MIB:PIM-MIB/PIM-MIB:pimIpMRouteTable/PIM-MIB:pimIpMRouteEntry[PIM-MIB:ipMRouteGroup = ' + str(self.ipmroutegroup) + '][PIM-MIB:ipMRouteSource = ' + str(self.ipmroutesource) + '][PIM-MIB:ipMRouteSourceMask = ' + str(self.ipmroutesourcemask) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _PIM_MIB as meta
                return meta._meta_table['PimMib.Pimipmroutetable.Pimipmrouteentry']['meta_info']

        @property
        def _common_path(self):

            return '/PIM-MIB:PIM-MIB/PIM-MIB:pimIpMRouteTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.pimipmrouteentry is not None:
                for child_ref in self.pimipmrouteentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _PIM_MIB as meta
            return meta._meta_table['PimMib.Pimipmroutetable']['meta_info']


    class Pimrptable(object):
        """
        The (conceptual) table listing PIM version 1 information
        for the Rendezvous Points (RPs) for IP multicast groups.
        This table is deprecated since its function is replaced by
        the pimRPSetTable for PIM version 2.
        
        .. attribute:: pimrpentry
        
        	An entry (conceptual row) in the pimRPTable.  There is one entry per RP address for each IP multicast group
        	**type**\: list of    :py:class:`Pimrpentry <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimrptable.Pimrpentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            self.parent = None
            self.pimrpentry = YList()
            self.pimrpentry.parent = self
            self.pimrpentry.name = 'pimrpentry'


        class Pimrpentry(object):
            """
            An entry (conceptual row) in the pimRPTable.  There is one
            entry per RP address for each IP multicast group.
            
            .. attribute:: pimrpgroupaddress  <key>
            
            	The IP multicast group address for which this entry contains information about an RP
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: pimrpaddress  <key>
            
            	The unicast address of the RP
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: pimrplastchange
            
            	The value of sysUpTime at the time when the corresponding instance of pimRPState last changed its value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: pimrprowstatus
            
            	The status of this row, by which new entries may be created, or old entries deleted from this table
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            	**status**\: deprecated
            
            .. attribute:: pimrpstate
            
            	The state of the RP
            	**type**\:   :py:class:`PimrpstateEnum <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimrptable.Pimrpentry.PimrpstateEnum>`
            
            	**status**\: deprecated
            
            .. attribute:: pimrpstatetimer
            
            	The minimum time remaining before the next state change. When pimRPState is up, this is the minimum time which must expire until it can be declared down.  When pimRPState is down, this is the time until it will be declared up (in order to retry)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'PIM-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                self.parent = None
                self.pimrpgroupaddress = None
                self.pimrpaddress = None
                self.pimrplastchange = None
                self.pimrprowstatus = None
                self.pimrpstate = None
                self.pimrpstatetimer = None

            class PimrpstateEnum(Enum):
                """
                PimrpstateEnum

                The state of the RP.

                .. data:: up = 1

                .. data:: down = 2

                """

                up = 1

                down = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _PIM_MIB as meta
                    return meta._meta_table['PimMib.Pimrptable.Pimrpentry.PimrpstateEnum']


            @property
            def _common_path(self):
                if self.pimrpgroupaddress is None:
                    raise YPYModelError('Key property pimrpgroupaddress is None')
                if self.pimrpaddress is None:
                    raise YPYModelError('Key property pimrpaddress is None')

                return '/PIM-MIB:PIM-MIB/PIM-MIB:pimRPTable/PIM-MIB:pimRPEntry[PIM-MIB:pimRPGroupAddress = ' + str(self.pimrpgroupaddress) + '][PIM-MIB:pimRPAddress = ' + str(self.pimrpaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.pimrpgroupaddress is not None:
                    return True

                if self.pimrpaddress is not None:
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _PIM_MIB as meta
                return meta._meta_table['PimMib.Pimrptable.Pimrpentry']['meta_info']

        @property
        def _common_path(self):

            return '/PIM-MIB:PIM-MIB/PIM-MIB:pimRPTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.pimrpentry is not None:
                for child_ref in self.pimrpentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _PIM_MIB as meta
            return meta._meta_table['PimMib.Pimrptable']['meta_info']


    class Pimrpsettable(object):
        """
        The (conceptual) table listing PIM information for
        candidate Rendezvous Points (RPs) for IP multicast groups.
        When the local router is the BSR, this information is
        obtained from received Candidate\-RP\-Advertisements.  When
        the local router is not the BSR, this information is
        obtained from received RP\-Set messages.
        
        .. attribute:: pimrpsetentry
        
        	An entry (conceptual row) in the pimRPSetTable
        	**type**\: list of    :py:class:`Pimrpsetentry <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimrpsettable.Pimrpsetentry>`
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            self.parent = None
            self.pimrpsetentry = YList()
            self.pimrpsetentry.parent = self
            self.pimrpsetentry.name = 'pimrpsetentry'


        class Pimrpsetentry(object):
            """
            An entry (conceptual row) in the pimRPSetTable.
            
            .. attribute:: pimrpsetcomponent  <key>
            
            	 A number uniquely identifying the component.  Each protocol instance connected to a separate domain should have a different index value
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: pimrpsetgroupaddress  <key>
            
            	The IP multicast group address which, when combined with pimRPSetGroupMask, gives the group prefix for which this entry contains information about the Candidate\-RP
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimrpsetgroupmask  <key>
            
            	The multicast group address mask which, when combined with pimRPSetGroupAddress, gives the group prefix for which this entry contains information about the Candidate\-RP
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimrpsetaddress  <key>
            
            	The IP address of the Candidate\-RP
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimrpsetexpirytime
            
            	The minimum time remaining before the Candidate\-RP will be declared down.  If the local router is not the BSR, this value is 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pimrpsetholdtime
            
            	The holdtime of a Candidate\-RP.  If the local router is not the BSR, this value is 0
            	**type**\:  int
            
            	**range:** 0..255
            
            	**units**\: seconds
            
            

            """

            _prefix = 'PIM-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                self.parent = None
                self.pimrpsetcomponent = None
                self.pimrpsetgroupaddress = None
                self.pimrpsetgroupmask = None
                self.pimrpsetaddress = None
                self.pimrpsetexpirytime = None
                self.pimrpsetholdtime = None

            @property
            def _common_path(self):
                if self.pimrpsetcomponent is None:
                    raise YPYModelError('Key property pimrpsetcomponent is None')
                if self.pimrpsetgroupaddress is None:
                    raise YPYModelError('Key property pimrpsetgroupaddress is None')
                if self.pimrpsetgroupmask is None:
                    raise YPYModelError('Key property pimrpsetgroupmask is None')
                if self.pimrpsetaddress is None:
                    raise YPYModelError('Key property pimrpsetaddress is None')

                return '/PIM-MIB:PIM-MIB/PIM-MIB:pimRPSetTable/PIM-MIB:pimRPSetEntry[PIM-MIB:pimRPSetComponent = ' + str(self.pimrpsetcomponent) + '][PIM-MIB:pimRPSetGroupAddress = ' + str(self.pimrpsetgroupaddress) + '][PIM-MIB:pimRPSetGroupMask = ' + str(self.pimrpsetgroupmask) + '][PIM-MIB:pimRPSetAddress = ' + str(self.pimrpsetaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.pimrpsetcomponent is not None:
                    return True

                if self.pimrpsetgroupaddress is not None:
                    return True

                if self.pimrpsetgroupmask is not None:
                    return True

                if self.pimrpsetaddress is not None:
                    return True

                if self.pimrpsetexpirytime is not None:
                    return True

                if self.pimrpsetholdtime is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _PIM_MIB as meta
                return meta._meta_table['PimMib.Pimrpsettable.Pimrpsetentry']['meta_info']

        @property
        def _common_path(self):

            return '/PIM-MIB:PIM-MIB/PIM-MIB:pimRPSetTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.pimrpsetentry is not None:
                for child_ref in self.pimrpsetentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _PIM_MIB as meta
            return meta._meta_table['PimMib.Pimrpsettable']['meta_info']


    class Pimipmroutenexthoptable(object):
        """
        The (conceptual) table listing PIM\-specific information on
        a subset of the rows of the ipMRouteNextHopTable defined in
        the IP Multicast MIB.
        
        .. attribute:: pimipmroutenexthopentry
        
        	An entry (conceptual row) in the pimIpMRouteNextHopTable. There is one entry per entry in the ipMRouteNextHopTable whose interface is running PIM and whose ipMRouteNextHopState is pruned(1)
        	**type**\: list of    :py:class:`Pimipmroutenexthopentry <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimipmroutenexthoptable.Pimipmroutenexthopentry>`
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            self.parent = None
            self.pimipmroutenexthopentry = YList()
            self.pimipmroutenexthopentry.parent = self
            self.pimipmroutenexthopentry.name = 'pimipmroutenexthopentry'


        class Pimipmroutenexthopentry(object):
            """
            An entry (conceptual row) in the pimIpMRouteNextHopTable.
            There is one entry per entry in the ipMRouteNextHopTable
            whose interface is running PIM and whose
            ipMRouteNextHopState is pruned(1).
            
            .. attribute:: ipmroutenexthopgroup  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ipmroutenexthopgroup <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry>`
            
            .. attribute:: ipmroutenexthopsource  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ipmroutenexthopsource <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry>`
            
            .. attribute:: ipmroutenexthopsourcemask  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ipmroutenexthopsourcemask <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry>`
            
            .. attribute:: ipmroutenexthopifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ipmroutenexthopifindex <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry>`
            
            .. attribute:: ipmroutenexthopaddress  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ipmroutenexthopaddress <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry>`
            
            .. attribute:: pimipmroutenexthopprunereason
            
            	This object indicates why the downstream interface was pruned, whether in response to a PIM prune message or due to PIM Assert processing
            	**type**\:   :py:class:`PimipmroutenexthopprunereasonEnum <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimipmroutenexthoptable.Pimipmroutenexthopentry.PimipmroutenexthopprunereasonEnum>`
            
            

            """

            _prefix = 'PIM-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                self.parent = None
                self.ipmroutenexthopgroup = None
                self.ipmroutenexthopsource = None
                self.ipmroutenexthopsourcemask = None
                self.ipmroutenexthopifindex = None
                self.ipmroutenexthopaddress = None
                self.pimipmroutenexthopprunereason = None

            class PimipmroutenexthopprunereasonEnum(Enum):
                """
                PimipmroutenexthopprunereasonEnum

                This object indicates why the downstream interface was

                pruned, whether in response to a PIM prune message or due to

                PIM Assert processing.

                .. data:: other = 1

                .. data:: prune = 2

                .. data:: assert_ = 3

                """

                other = 1

                prune = 2

                assert_ = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _PIM_MIB as meta
                    return meta._meta_table['PimMib.Pimipmroutenexthoptable.Pimipmroutenexthopentry.PimipmroutenexthopprunereasonEnum']


            @property
            def _common_path(self):
                if self.ipmroutenexthopgroup is None:
                    raise YPYModelError('Key property ipmroutenexthopgroup is None')
                if self.ipmroutenexthopsource is None:
                    raise YPYModelError('Key property ipmroutenexthopsource is None')
                if self.ipmroutenexthopsourcemask is None:
                    raise YPYModelError('Key property ipmroutenexthopsourcemask is None')
                if self.ipmroutenexthopifindex is None:
                    raise YPYModelError('Key property ipmroutenexthopifindex is None')
                if self.ipmroutenexthopaddress is None:
                    raise YPYModelError('Key property ipmroutenexthopaddress is None')

                return '/PIM-MIB:PIM-MIB/PIM-MIB:pimIpMRouteNextHopTable/PIM-MIB:pimIpMRouteNextHopEntry[PIM-MIB:ipMRouteNextHopGroup = ' + str(self.ipmroutenexthopgroup) + '][PIM-MIB:ipMRouteNextHopSource = ' + str(self.ipmroutenexthopsource) + '][PIM-MIB:ipMRouteNextHopSourceMask = ' + str(self.ipmroutenexthopsourcemask) + '][PIM-MIB:ipMRouteNextHopIfIndex = ' + str(self.ipmroutenexthopifindex) + '][PIM-MIB:ipMRouteNextHopAddress = ' + str(self.ipmroutenexthopaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ipmroutenexthopgroup is not None:
                    return True

                if self.ipmroutenexthopsource is not None:
                    return True

                if self.ipmroutenexthopsourcemask is not None:
                    return True

                if self.ipmroutenexthopifindex is not None:
                    return True

                if self.ipmroutenexthopaddress is not None:
                    return True

                if self.pimipmroutenexthopprunereason is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _PIM_MIB as meta
                return meta._meta_table['PimMib.Pimipmroutenexthoptable.Pimipmroutenexthopentry']['meta_info']

        @property
        def _common_path(self):

            return '/PIM-MIB:PIM-MIB/PIM-MIB:pimIpMRouteNextHopTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.pimipmroutenexthopentry is not None:
                for child_ref in self.pimipmroutenexthopentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _PIM_MIB as meta
            return meta._meta_table['PimMib.Pimipmroutenexthoptable']['meta_info']


    class Pimcandidaterptable(object):
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
        	**type**\: list of    :py:class:`Pimcandidaterpentry <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimcandidaterptable.Pimcandidaterpentry>`
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            self.parent = None
            self.pimcandidaterpentry = YList()
            self.pimcandidaterpentry.parent = self
            self.pimcandidaterpentry.name = 'pimcandidaterpentry'


        class Pimcandidaterpentry(object):
            """
            An entry (conceptual row) in the pimCandidateRPTable.
            
            .. attribute:: pimcandidaterpgroupaddress  <key>
            
            	The IP multicast group address which, when combined with pimCandidateRPGroupMask, identifies a group prefix for which the local router will advertise itself as a Candidate\-RP
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimcandidaterpgroupmask  <key>
            
            	The multicast group address mask which, when combined with pimCandidateRPGroupMask, identifies a group prefix for which the local router will advertise itself as a Candidate\-RP
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimcandidaterpaddress
            
            	The (unicast) address of the interface which will be      advertised as a Candidate\-RP
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimcandidaterprowstatus
            
            	The status of this row, by which new entries may be created, or old entries deleted from this table
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            

            """

            _prefix = 'PIM-MIB'
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
                    raise YPYModelError('Key property pimcandidaterpgroupaddress is None')
                if self.pimcandidaterpgroupmask is None:
                    raise YPYModelError('Key property pimcandidaterpgroupmask is None')

                return '/PIM-MIB:PIM-MIB/PIM-MIB:pimCandidateRPTable/PIM-MIB:pimCandidateRPEntry[PIM-MIB:pimCandidateRPGroupAddress = ' + str(self.pimcandidaterpgroupaddress) + '][PIM-MIB:pimCandidateRPGroupMask = ' + str(self.pimcandidaterpgroupmask) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.pimcandidaterpgroupaddress is not None:
                    return True

                if self.pimcandidaterpgroupmask is not None:
                    return True

                if self.pimcandidaterpaddress is not None:
                    return True

                if self.pimcandidaterprowstatus is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _PIM_MIB as meta
                return meta._meta_table['PimMib.Pimcandidaterptable.Pimcandidaterpentry']['meta_info']

        @property
        def _common_path(self):

            return '/PIM-MIB:PIM-MIB/PIM-MIB:pimCandidateRPTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.pimcandidaterpentry is not None:
                for child_ref in self.pimcandidaterpentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _PIM_MIB as meta
            return meta._meta_table['PimMib.Pimcandidaterptable']['meta_info']


    class Pimcomponenttable(object):
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
        	**type**\: list of    :py:class:`Pimcomponententry <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimcomponenttable.Pimcomponententry>`
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            self.parent = None
            self.pimcomponententry = YList()
            self.pimcomponententry.parent = self
            self.pimcomponententry.name = 'pimcomponententry'


        class Pimcomponententry(object):
            """
            An entry (conceptual row) in the pimComponentTable.
            
            .. attribute:: pimcomponentindex  <key>
            
            	A number uniquely identifying the component.  Each protocol instance connected to a separate domain should have a different index value.  Routers that only support membership in a single PIM\-SM domain should use a pimComponentIndex value of 1
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: pimcomponentbsraddress
            
            	The IP address of the bootstrap router (BSR) for the local PIM region
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimcomponentbsrexpirytime
            
            	The minimum time remaining before the bootstrap router in the local domain will be declared down.  For candidate BSRs, this is the time until the component sends an RP\-Set message.  For other routers, this is the time until it may accept an RP\-Set message from a lower candidate BSR
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pimcomponentcrpholdtime
            
            	The holdtime of the component when it is a candidate RP in the local domain.  The value of 0 is used to indicate that the local system is not a Candidate\-RP
            	**type**\:  int
            
            	**range:** 0..255
            
            	**units**\: seconds
            
            .. attribute:: pimcomponentstatus
            
            	The status of this entry.  Creating the entry creates another protocol instance; destroying the entry disables a protocol instance
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            

            """

            _prefix = 'PIM-MIB'
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
                    raise YPYModelError('Key property pimcomponentindex is None')

                return '/PIM-MIB:PIM-MIB/PIM-MIB:pimComponentTable/PIM-MIB:pimComponentEntry[PIM-MIB:pimComponentIndex = ' + str(self.pimcomponentindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _PIM_MIB as meta
                return meta._meta_table['PimMib.Pimcomponenttable.Pimcomponententry']['meta_info']

        @property
        def _common_path(self):

            return '/PIM-MIB:PIM-MIB/PIM-MIB:pimComponentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.pimcomponententry is not None:
                for child_ref in self.pimcomponententry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _PIM_MIB as meta
            return meta._meta_table['PimMib.Pimcomponenttable']['meta_info']

    @property
    def _common_path(self):

        return '/PIM-MIB:PIM-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.pim is not None and self.pim._has_data():
            return True

        if self.pimcandidaterptable is not None and self.pimcandidaterptable._has_data():
            return True

        if self.pimcomponenttable is not None and self.pimcomponenttable._has_data():
            return True

        if self.piminterfacetable is not None and self.piminterfacetable._has_data():
            return True

        if self.pimipmroutenexthoptable is not None and self.pimipmroutenexthoptable._has_data():
            return True

        if self.pimipmroutetable is not None and self.pimipmroutetable._has_data():
            return True

        if self.pimneighbortable is not None and self.pimneighbortable._has_data():
            return True

        if self.pimrpsettable is not None and self.pimrpsettable._has_data():
            return True

        if self.pimrptable is not None and self.pimrptable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _PIM_MIB as meta
        return meta._meta_table['PimMib']['meta_info']



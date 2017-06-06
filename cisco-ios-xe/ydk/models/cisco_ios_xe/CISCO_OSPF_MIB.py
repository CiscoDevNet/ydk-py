""" CISCO_OSPF_MIB 

An extension to the MIB module defined in
RFC 1850 for managing OSPF implimentation. 
Most of the MIB definitions are based on
the IETF draft 
< draft\-ietf\-ospf\-mib\-update\-05.txt > . 
Support for OSPF Sham link is also added

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CiscoOspfMib(object):
    """
    
    
    .. attribute:: cospfgeneralgroup
    
    	
    	**type**\:   :py:class:`Cospfgeneralgroup <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfgeneralgroup>`
    
    .. attribute:: cospflocallsdbtable
    
    	The OSPF Process's Link\-Local Link State Database for non\-virtual links
    	**type**\:   :py:class:`Cospflocallsdbtable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospflocallsdbtable>`
    
    .. attribute:: cospflsdbtable
    
    	The OSPF Process's Link State Database. This  table is meant for Opaque LSA's
    	**type**\:   :py:class:`Cospflsdbtable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospflsdbtable>`
    
    .. attribute:: cospfshamlinknbrtable
    
    	A table of sham link neighbor information
    	**type**\:   :py:class:`Cospfshamlinknbrtable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfshamlinknbrtable>`
    
    .. attribute:: cospfshamlinkstable
    
    	Information about this router's sham links
    	**type**\:   :py:class:`Cospfshamlinkstable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfshamlinkstable>`
    
    .. attribute:: cospfshamlinktable
    
    	Information about this router's sham links
    	**type**\:   :py:class:`Cospfshamlinktable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfshamlinktable>`
    
    	**status**\: deprecated
    
    .. attribute:: cospfvirtlocallsdbtable
    
    	The OSPF Process's Link\-Local Link State Database for virtual links
    	**type**\:   :py:class:`Cospfvirtlocallsdbtable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfvirtlocallsdbtable>`
    
    

    """

    _prefix = 'CISCO-OSPF-MIB'
    _revision = '2003-07-18'

    def __init__(self):
        self.cospfgeneralgroup = CiscoOspfMib.Cospfgeneralgroup()
        self.cospfgeneralgroup.parent = self
        self.cospflocallsdbtable = CiscoOspfMib.Cospflocallsdbtable()
        self.cospflocallsdbtable.parent = self
        self.cospflsdbtable = CiscoOspfMib.Cospflsdbtable()
        self.cospflsdbtable.parent = self
        self.cospfshamlinknbrtable = CiscoOspfMib.Cospfshamlinknbrtable()
        self.cospfshamlinknbrtable.parent = self
        self.cospfshamlinkstable = CiscoOspfMib.Cospfshamlinkstable()
        self.cospfshamlinkstable.parent = self
        self.cospfshamlinktable = CiscoOspfMib.Cospfshamlinktable()
        self.cospfshamlinktable.parent = self
        self.cospfvirtlocallsdbtable = CiscoOspfMib.Cospfvirtlocallsdbtable()
        self.cospfvirtlocallsdbtable.parent = self


    class Cospfgeneralgroup(object):
        """
        
        
        .. attribute:: cospfopaqueaslsacksumsum
        
        	The 32\-bit unsigned sum of the Opaque AS  link\-state advertisements' LS checksums contained link state database
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cospfopaqueaslsacount
        
        	The total number of Opaque AS link\-state advertisements in the link state database
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cospfopaquelsasupport
        
        	The router's support for Opaque LSA types
        	**type**\:  bool
        
        .. attribute:: cospfrfc1583compatibility
        
        	Indicates metrics used to choose among multiple AS\- external\-LSAs. When cospfRFC1583Compatibility is set to enabled, only cost will be used when choosing among multiple AS\-external\-LSAs advertising the same destination. When cospfRFC1583Compatibility is set to disabled, preference will be driven first by type of path using cost only to break ties
        	**type**\:  bool
        
        .. attribute:: cospftrafficengineeringsupport
        
        	The router's support for OSPF traffic engineering
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            self.parent = None
            self.cospfopaqueaslsacksumsum = None
            self.cospfopaqueaslsacount = None
            self.cospfopaquelsasupport = None
            self.cospfrfc1583compatibility = None
            self.cospftrafficengineeringsupport = None

        @property
        def _common_path(self):

            return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfGeneralGroup'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cospfopaqueaslsacksumsum is not None:
                return True

            if self.cospfopaqueaslsacount is not None:
                return True

            if self.cospfopaquelsasupport is not None:
                return True

            if self.cospfrfc1583compatibility is not None:
                return True

            if self.cospftrafficengineeringsupport is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_MIB as meta
            return meta._meta_table['CiscoOspfMib.Cospfgeneralgroup']['meta_info']


    class Cospflsdbtable(object):
        """
        The OSPF Process's Link State Database. This 
        table is meant for Opaque LSA's
        
        .. attribute:: cospflsdbentry
        
        	A single Link State Advertisement
        	**type**\: list of    :py:class:`Cospflsdbentry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospflsdbtable.Cospflsdbentry>`
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            self.parent = None
            self.cospflsdbentry = YList()
            self.cospflsdbentry.parent = self
            self.cospflsdbentry.name = 'cospflsdbentry'


        class Cospflsdbentry(object):
            """
            A single Link State Advertisement.
            
            .. attribute:: ospflsdbareaid  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ospflsdbareaid <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospflsdbtable.Ospflsdbentry>`
            
            .. attribute:: cospflsdbtype  <key>
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\:   :py:class:`CospflsdbtypeEnum <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospflsdbtable.Cospflsdbentry.CospflsdbtypeEnum>`
            
            .. attribute:: ospflsdblsid  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ospflsdblsid <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospflsdbtable.Ospflsdbentry>`
            
            .. attribute:: ospflsdbrouterid  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ospflsdbrouterid <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospflsdbtable.Ospflsdbentry>`
            
            .. attribute:: cospflsdbadvertisement
            
            	The entire Link State Advertisement, including its header
            	**type**\:  str
            
            	**length:** 1..65535
            
            .. attribute:: cospflsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cospflsdbchecksum
            
            	This field is the  checksum  of  the  complete contents  of  the  advertisement, excepting the age field.  The age field is excepted  so  that an   advertisement's  age  can  be  incremented without updating the  checksum.   The  checksum used  is  the same that is used for ISO connectionless datagrams; it is commonly referred  to as the Fletcher checksum
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cospflsdbsequence
            
            	The sequence number field is a  signed  32\-bit integer.   It  is used to detect old and duplicate link state advertisements.  The  space  of sequence  numbers  is  linearly  ordered.   The larger the sequence number the more recent  the advertisement
            	**type**\:  int
            
            	**range:** 1..147483647
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                self.parent = None
                self.ospflsdbareaid = None
                self.cospflsdbtype = None
                self.ospflsdblsid = None
                self.ospflsdbrouterid = None
                self.cospflsdbadvertisement = None
                self.cospflsdbage = None
                self.cospflsdbchecksum = None
                self.cospflsdbsequence = None

            class CospflsdbtypeEnum(Enum):
                """
                CospflsdbtypeEnum

                The type of the link state advertisement.

                Each link state type has a separate advertisement format.

                .. data:: areaOpaqueLink = 10

                .. data:: asOpaqueLink = 11

                """

                areaOpaqueLink = 10

                asOpaqueLink = 11


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_MIB as meta
                    return meta._meta_table['CiscoOspfMib.Cospflsdbtable.Cospflsdbentry.CospflsdbtypeEnum']


            @property
            def _common_path(self):
                if self.ospflsdbareaid is None:
                    raise YPYModelError('Key property ospflsdbareaid is None')
                if self.cospflsdbtype is None:
                    raise YPYModelError('Key property cospflsdbtype is None')
                if self.ospflsdblsid is None:
                    raise YPYModelError('Key property ospflsdblsid is None')
                if self.ospflsdbrouterid is None:
                    raise YPYModelError('Key property ospflsdbrouterid is None')

                return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfLsdbTable/CISCO-OSPF-MIB:cospfLsdbEntry[CISCO-OSPF-MIB:ospfLsdbAreaId = ' + str(self.ospflsdbareaid) + '][CISCO-OSPF-MIB:cospfLsdbType = ' + str(self.cospflsdbtype) + '][CISCO-OSPF-MIB:ospfLsdbLsid = ' + str(self.ospflsdblsid) + '][CISCO-OSPF-MIB:ospfLsdbRouterId = ' + str(self.ospflsdbrouterid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ospflsdbareaid is not None:
                    return True

                if self.cospflsdbtype is not None:
                    return True

                if self.ospflsdblsid is not None:
                    return True

                if self.ospflsdbrouterid is not None:
                    return True

                if self.cospflsdbadvertisement is not None:
                    return True

                if self.cospflsdbage is not None:
                    return True

                if self.cospflsdbchecksum is not None:
                    return True

                if self.cospflsdbsequence is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_MIB as meta
                return meta._meta_table['CiscoOspfMib.Cospflsdbtable.Cospflsdbentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfLsdbTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cospflsdbentry is not None:
                for child_ref in self.cospflsdbentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_MIB as meta
            return meta._meta_table['CiscoOspfMib.Cospflsdbtable']['meta_info']


    class Cospfshamlinktable(object):
        """
        Information about this router's sham links
        
        .. attribute:: cospfshamlinkentry
        
        	Information about a single sham link
        	**type**\: list of    :py:class:`Cospfshamlinkentry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfshamlinktable.Cospfshamlinkentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            self.parent = None
            self.cospfshamlinkentry = YList()
            self.cospfshamlinkentry.parent = self
            self.cospfshamlinkentry.name = 'cospfshamlinkentry'


        class Cospfshamlinkentry(object):
            """
            Information about a single sham link
            
            .. attribute:: cospfshamlinkareaid  <key>
            
            	The  Transit  Area  that  the   Virtual   Link traverses.  By definition, this is not 0.0.0.0
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinklocalipaddress  <key>
            
            	The Local IP address of the sham link
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkneighborid  <key>
            
            	The Router ID of the other end router of the sham link
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkevents
            
            	The number of state changes or error events on this sham link
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkhellointerval
            
            	The length of time, in  seconds,  between  the Hello  packets that the router sends on the sham link
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkmetric
            
            	The Metric to be advertised
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkretransinterval
            
            	The number of seconds between  link\-state  advertisement retransmissions,  for  adjacencies belonging to this  link.   This  value  is also used when retransmitting database description   and  link\-state  request  packets. This value   should  be well over the expected round trip time
            	**type**\:  int
            
            	**range:** 0..3600
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkrtrdeadinterval
            
            	The number of seconds that  a  router's  Hello packets  have  not been seen before it's neighbors declare the router down.  This  should  be some  multiple  of  the  Hello  interval
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkstate
            
            	OSPF sham link states
            	**type**\:   :py:class:`CospfshamlinkstateEnum <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfshamlinktable.Cospfshamlinkentry.CospfshamlinkstateEnum>`
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                self.parent = None
                self.cospfshamlinkareaid = None
                self.cospfshamlinklocalipaddress = None
                self.cospfshamlinkneighborid = None
                self.cospfshamlinkevents = None
                self.cospfshamlinkhellointerval = None
                self.cospfshamlinkmetric = None
                self.cospfshamlinkretransinterval = None
                self.cospfshamlinkrtrdeadinterval = None
                self.cospfshamlinkstate = None

            class CospfshamlinkstateEnum(Enum):
                """
                CospfshamlinkstateEnum

                OSPF sham link states.

                .. data:: down = 1

                .. data:: pointToPoint = 4

                """

                down = 1

                pointToPoint = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_MIB as meta
                    return meta._meta_table['CiscoOspfMib.Cospfshamlinktable.Cospfshamlinkentry.CospfshamlinkstateEnum']


            @property
            def _common_path(self):
                if self.cospfshamlinkareaid is None:
                    raise YPYModelError('Key property cospfshamlinkareaid is None')
                if self.cospfshamlinklocalipaddress is None:
                    raise YPYModelError('Key property cospfshamlinklocalipaddress is None')
                if self.cospfshamlinkneighborid is None:
                    raise YPYModelError('Key property cospfshamlinkneighborid is None')

                return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfShamLinkTable/CISCO-OSPF-MIB:cospfShamLinkEntry[CISCO-OSPF-MIB:cospfShamLinkAreaId = ' + str(self.cospfshamlinkareaid) + '][CISCO-OSPF-MIB:cospfShamLinkLocalIpAddress = ' + str(self.cospfshamlinklocalipaddress) + '][CISCO-OSPF-MIB:cospfShamLinkNeighborId = ' + str(self.cospfshamlinkneighborid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cospfshamlinkareaid is not None:
                    return True

                if self.cospfshamlinklocalipaddress is not None:
                    return True

                if self.cospfshamlinkneighborid is not None:
                    return True

                if self.cospfshamlinkevents is not None:
                    return True

                if self.cospfshamlinkhellointerval is not None:
                    return True

                if self.cospfshamlinkmetric is not None:
                    return True

                if self.cospfshamlinkretransinterval is not None:
                    return True

                if self.cospfshamlinkrtrdeadinterval is not None:
                    return True

                if self.cospfshamlinkstate is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_MIB as meta
                return meta._meta_table['CiscoOspfMib.Cospfshamlinktable.Cospfshamlinkentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfShamLinkTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cospfshamlinkentry is not None:
                for child_ref in self.cospfshamlinkentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_MIB as meta
            return meta._meta_table['CiscoOspfMib.Cospfshamlinktable']['meta_info']


    class Cospflocallsdbtable(object):
        """
        The OSPF Process's Link\-Local Link State Database
        for non\-virtual links.
        
        .. attribute:: cospflocallsdbentry
        
        	A single Link State Advertisement
        	**type**\: list of    :py:class:`Cospflocallsdbentry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospflocallsdbtable.Cospflocallsdbentry>`
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            self.parent = None
            self.cospflocallsdbentry = YList()
            self.cospflocallsdbentry.parent = self
            self.cospflocallsdbentry.name = 'cospflocallsdbentry'


        class Cospflocallsdbentry(object):
            """
            A single Link State Advertisement.
            
            .. attribute:: cospflocallsdbipaddress  <key>
            
            	The IP Address of the interface from which the LSA was received if the interface is numbered
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospflocallsdbaddresslessif  <key>
            
            	The Interface Index of the interface from which the LSA was received if the interface is unnumbered
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cospflocallsdbtype  <key>
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\:   :py:class:`CospflocallsdbtypeEnum <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospflocallsdbtable.Cospflocallsdbentry.CospflocallsdbtypeEnum>`
            
            .. attribute:: cospflocallsdblsid  <key>
            
            	The Link State ID is an LS Type Specific field containing a 32 bit identifier in IP address format; it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospflocallsdbrouterid  <key>
            
            	The 32 bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospflocallsdbadvertisement
            
            	The entire Link State Advertisement, including its header
            	**type**\:  str
            
            	**length:** 1..65535
            
            .. attribute:: cospflocallsdbage
            
            	This field is the age of the link state advertisement  in seconds
            	**type**\:  int
            
            	**range:** 0..3600
            
            .. attribute:: cospflocallsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field. The age field is excepted so that an advertisement's age can be incremented without updating the checksum. The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred  to as the Fletcher checksum
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospflocallsdbsequence
            
            	The sequence number field is a signed 32\-bit integer. It is used to detect old and duplicate link state advertisements. The space of sequence numbers is linearly ordered. The larger the sequence number the more recent the advertisement
            	**type**\:  int
            
            	**range:** \-2147483647..2147483647
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                self.parent = None
                self.cospflocallsdbipaddress = None
                self.cospflocallsdbaddresslessif = None
                self.cospflocallsdbtype = None
                self.cospflocallsdblsid = None
                self.cospflocallsdbrouterid = None
                self.cospflocallsdbadvertisement = None
                self.cospflocallsdbage = None
                self.cospflocallsdbchecksum = None
                self.cospflocallsdbsequence = None

            class CospflocallsdbtypeEnum(Enum):
                """
                CospflocallsdbtypeEnum

                The type of the link state advertisement.

                Each link state type has a separate advertisement format.

                .. data:: localOpaqueLink = 9

                """

                localOpaqueLink = 9


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_MIB as meta
                    return meta._meta_table['CiscoOspfMib.Cospflocallsdbtable.Cospflocallsdbentry.CospflocallsdbtypeEnum']


            @property
            def _common_path(self):
                if self.cospflocallsdbipaddress is None:
                    raise YPYModelError('Key property cospflocallsdbipaddress is None')
                if self.cospflocallsdbaddresslessif is None:
                    raise YPYModelError('Key property cospflocallsdbaddresslessif is None')
                if self.cospflocallsdbtype is None:
                    raise YPYModelError('Key property cospflocallsdbtype is None')
                if self.cospflocallsdblsid is None:
                    raise YPYModelError('Key property cospflocallsdblsid is None')
                if self.cospflocallsdbrouterid is None:
                    raise YPYModelError('Key property cospflocallsdbrouterid is None')

                return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfLocalLsdbTable/CISCO-OSPF-MIB:cospfLocalLsdbEntry[CISCO-OSPF-MIB:cospfLocalLsdbIpAddress = ' + str(self.cospflocallsdbipaddress) + '][CISCO-OSPF-MIB:cospfLocalLsdbAddressLessIf = ' + str(self.cospflocallsdbaddresslessif) + '][CISCO-OSPF-MIB:cospfLocalLsdbType = ' + str(self.cospflocallsdbtype) + '][CISCO-OSPF-MIB:cospfLocalLsdbLsid = ' + str(self.cospflocallsdblsid) + '][CISCO-OSPF-MIB:cospfLocalLsdbRouterId = ' + str(self.cospflocallsdbrouterid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cospflocallsdbipaddress is not None:
                    return True

                if self.cospflocallsdbaddresslessif is not None:
                    return True

                if self.cospflocallsdbtype is not None:
                    return True

                if self.cospflocallsdblsid is not None:
                    return True

                if self.cospflocallsdbrouterid is not None:
                    return True

                if self.cospflocallsdbadvertisement is not None:
                    return True

                if self.cospflocallsdbage is not None:
                    return True

                if self.cospflocallsdbchecksum is not None:
                    return True

                if self.cospflocallsdbsequence is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_MIB as meta
                return meta._meta_table['CiscoOspfMib.Cospflocallsdbtable.Cospflocallsdbentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfLocalLsdbTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cospflocallsdbentry is not None:
                for child_ref in self.cospflocallsdbentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_MIB as meta
            return meta._meta_table['CiscoOspfMib.Cospflocallsdbtable']['meta_info']


    class Cospfvirtlocallsdbtable(object):
        """
        The OSPF Process's Link\-Local Link State Database
        for virtual links.
        
        .. attribute:: cospfvirtlocallsdbentry
        
        	A single Link State Advertisement
        	**type**\: list of    :py:class:`Cospfvirtlocallsdbentry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfvirtlocallsdbtable.Cospfvirtlocallsdbentry>`
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            self.parent = None
            self.cospfvirtlocallsdbentry = YList()
            self.cospfvirtlocallsdbentry.parent = self
            self.cospfvirtlocallsdbentry.name = 'cospfvirtlocallsdbentry'


        class Cospfvirtlocallsdbentry(object):
            """
            A single Link State Advertisement.
            
            .. attribute:: cospfvirtlocallsdbtransitarea  <key>
            
            	The Transit Area that the Virtual Link traverses. By definition, this is not 0.0.0.0
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfvirtlocallsdbneighbor  <key>
            
            	The Router ID of the Virtual Neighbor
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfvirtlocallsdbtype  <key>
            
            	The type of the link state advertisement. Each  link state type has a separate advertisement format
            	**type**\:   :py:class:`CospfvirtlocallsdbtypeEnum <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfvirtlocallsdbtable.Cospfvirtlocallsdbentry.CospfvirtlocallsdbtypeEnum>`
            
            .. attribute:: cospfvirtlocallsdblsid  <key>
            
            	The Link State ID is an LS Type Specific field containing a 32 bit identifier in IP address format; it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfvirtlocallsdbrouterid  <key>
            
            	The 32 bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfvirtlocallsdbadvertisement
            
            	The entire Link State Advertisement, including its header
            	**type**\:  str
            
            	**length:** 1..65535
            
            .. attribute:: cospfvirtlocallsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\:  int
            
            	**range:** 0..3600
            
            .. attribute:: cospfvirtlocallsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field. The age field is excepted so that an advertisement's age can be incremented without updating the checksum. The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred  to as the Fletcher checksum
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfvirtlocallsdbsequence
            
            	The sequence number field is a  signed  32\-bit integer. It is used to detect old and duplicate link state advertisements. The space of sequence numbers is linearly ordered. The larger the sequence number the more recent the advertisement
            	**type**\:  int
            
            	**range:** \-2147483647..2147483647
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                self.parent = None
                self.cospfvirtlocallsdbtransitarea = None
                self.cospfvirtlocallsdbneighbor = None
                self.cospfvirtlocallsdbtype = None
                self.cospfvirtlocallsdblsid = None
                self.cospfvirtlocallsdbrouterid = None
                self.cospfvirtlocallsdbadvertisement = None
                self.cospfvirtlocallsdbage = None
                self.cospfvirtlocallsdbchecksum = None
                self.cospfvirtlocallsdbsequence = None

            class CospfvirtlocallsdbtypeEnum(Enum):
                """
                CospfvirtlocallsdbtypeEnum

                The type of the link state advertisement.

                Each  link state type has a separate advertisement format.

                .. data:: localOpaqueLink = 9

                """

                localOpaqueLink = 9


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_MIB as meta
                    return meta._meta_table['CiscoOspfMib.Cospfvirtlocallsdbtable.Cospfvirtlocallsdbentry.CospfvirtlocallsdbtypeEnum']


            @property
            def _common_path(self):
                if self.cospfvirtlocallsdbtransitarea is None:
                    raise YPYModelError('Key property cospfvirtlocallsdbtransitarea is None')
                if self.cospfvirtlocallsdbneighbor is None:
                    raise YPYModelError('Key property cospfvirtlocallsdbneighbor is None')
                if self.cospfvirtlocallsdbtype is None:
                    raise YPYModelError('Key property cospfvirtlocallsdbtype is None')
                if self.cospfvirtlocallsdblsid is None:
                    raise YPYModelError('Key property cospfvirtlocallsdblsid is None')
                if self.cospfvirtlocallsdbrouterid is None:
                    raise YPYModelError('Key property cospfvirtlocallsdbrouterid is None')

                return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfVirtLocalLsdbTable/CISCO-OSPF-MIB:cospfVirtLocalLsdbEntry[CISCO-OSPF-MIB:cospfVirtLocalLsdbTransitArea = ' + str(self.cospfvirtlocallsdbtransitarea) + '][CISCO-OSPF-MIB:cospfVirtLocalLsdbNeighbor = ' + str(self.cospfvirtlocallsdbneighbor) + '][CISCO-OSPF-MIB:cospfVirtLocalLsdbType = ' + str(self.cospfvirtlocallsdbtype) + '][CISCO-OSPF-MIB:cospfVirtLocalLsdbLsid = ' + str(self.cospfvirtlocallsdblsid) + '][CISCO-OSPF-MIB:cospfVirtLocalLsdbRouterId = ' + str(self.cospfvirtlocallsdbrouterid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cospfvirtlocallsdbtransitarea is not None:
                    return True

                if self.cospfvirtlocallsdbneighbor is not None:
                    return True

                if self.cospfvirtlocallsdbtype is not None:
                    return True

                if self.cospfvirtlocallsdblsid is not None:
                    return True

                if self.cospfvirtlocallsdbrouterid is not None:
                    return True

                if self.cospfvirtlocallsdbadvertisement is not None:
                    return True

                if self.cospfvirtlocallsdbage is not None:
                    return True

                if self.cospfvirtlocallsdbchecksum is not None:
                    return True

                if self.cospfvirtlocallsdbsequence is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_MIB as meta
                return meta._meta_table['CiscoOspfMib.Cospfvirtlocallsdbtable.Cospfvirtlocallsdbentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfVirtLocalLsdbTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cospfvirtlocallsdbentry is not None:
                for child_ref in self.cospfvirtlocallsdbentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_MIB as meta
            return meta._meta_table['CiscoOspfMib.Cospfvirtlocallsdbtable']['meta_info']


    class Cospfshamlinknbrtable(object):
        """
        A table of sham link neighbor information.
        
        .. attribute:: cospfshamlinknbrentry
        
        	Sham link neighbor information
        	**type**\: list of    :py:class:`Cospfshamlinknbrentry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfshamlinknbrtable.Cospfshamlinknbrentry>`
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            self.parent = None
            self.cospfshamlinknbrentry = YList()
            self.cospfshamlinknbrentry.parent = self
            self.cospfshamlinknbrentry.name = 'cospfshamlinknbrentry'


        class Cospfshamlinknbrentry(object):
            """
            Sham link neighbor information.
            
            .. attribute:: cospfshamlinkslocalipaddrtype  <key>
            
            	
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: cospfshamlinkslocalipaddr  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`cospfshamlinkslocalipaddr <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfshamlinkstable.Cospfshamlinksentry>`
            
            .. attribute:: cospfshamlinknbrarea  <key>
            
            	The area to which the sham link is part of
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfshamlinknbripaddrtype  <key>
            
            	The type of internet address of this sham link neighbor's IP address
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: cospfshamlinknbripaddr  <key>
            
            	The IP address this sham link neighbor is using
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cospfshamlinknbrevents
            
            	The number of  times  this sham link has changed state or an error has occurred
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfshamlinknbrhellosuppressed
            
            	Indicates whether Hellos are being  suppressed to the neighbor
            	**type**\:  bool
            
            .. attribute:: cospfshamlinknbrlsretransqlen
            
            	The  current  length  of  the   retransmission queue. The retransmission queue is maintained for LSAs that have been flooded but not acknowledged on this adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfshamlinknbroptions
            
            	A Bit Mask corresponding to the neighbor's options field.  Bit 1, if set, indicates that the  system  will operate  on  Type of Service metrics other than TOS 0.  If zero, the neighbor will  ignore  all metrics except the TOS 0 metric.  Bit 2, if set, indicates  that  the  system  is Network  Multicast  capable; ie, that it implements  OSPF Multicast Routing
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cospfshamlinknbrrtrid
            
            	A 32\-bit integer uniquely identifying the neighboring router
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfshamlinknbrstate
            
            	The state of this sham link neighbor relation\- ship
            	**type**\:   :py:class:`CospfshamlinknbrstateEnum <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfshamlinknbrtable.Cospfshamlinknbrentry.CospfshamlinknbrstateEnum>`
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                self.parent = None
                self.cospfshamlinkslocalipaddrtype = None
                self.cospfshamlinkslocalipaddr = None
                self.cospfshamlinknbrarea = None
                self.cospfshamlinknbripaddrtype = None
                self.cospfshamlinknbripaddr = None
                self.cospfshamlinknbrevents = None
                self.cospfshamlinknbrhellosuppressed = None
                self.cospfshamlinknbrlsretransqlen = None
                self.cospfshamlinknbroptions = None
                self.cospfshamlinknbrrtrid = None
                self.cospfshamlinknbrstate = None

            class CospfshamlinknbrstateEnum(Enum):
                """
                CospfshamlinknbrstateEnum

                The state of this sham link neighbor relation\-

                ship.

                .. data:: down = 1

                .. data:: attempt = 2

                .. data:: init = 3

                .. data:: twoWay = 4

                .. data:: exchangeStart = 5

                .. data:: exchange = 6

                .. data:: loading = 7

                .. data:: full = 8

                """

                down = 1

                attempt = 2

                init = 3

                twoWay = 4

                exchangeStart = 5

                exchange = 6

                loading = 7

                full = 8


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_MIB as meta
                    return meta._meta_table['CiscoOspfMib.Cospfshamlinknbrtable.Cospfshamlinknbrentry.CospfshamlinknbrstateEnum']


            @property
            def _common_path(self):
                if self.cospfshamlinkslocalipaddrtype is None:
                    raise YPYModelError('Key property cospfshamlinkslocalipaddrtype is None')
                if self.cospfshamlinkslocalipaddr is None:
                    raise YPYModelError('Key property cospfshamlinkslocalipaddr is None')
                if self.cospfshamlinknbrarea is None:
                    raise YPYModelError('Key property cospfshamlinknbrarea is None')
                if self.cospfshamlinknbripaddrtype is None:
                    raise YPYModelError('Key property cospfshamlinknbripaddrtype is None')
                if self.cospfshamlinknbripaddr is None:
                    raise YPYModelError('Key property cospfshamlinknbripaddr is None')

                return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfShamLinkNbrTable/CISCO-OSPF-MIB:cospfShamLinkNbrEntry[CISCO-OSPF-MIB:cospfShamLinksLocalIpAddrType = ' + str(self.cospfshamlinkslocalipaddrtype) + '][CISCO-OSPF-MIB:cospfShamLinksLocalIpAddr = ' + str(self.cospfshamlinkslocalipaddr) + '][CISCO-OSPF-MIB:cospfShamLinkNbrArea = ' + str(self.cospfshamlinknbrarea) + '][CISCO-OSPF-MIB:cospfShamLinkNbrIpAddrType = ' + str(self.cospfshamlinknbripaddrtype) + '][CISCO-OSPF-MIB:cospfShamLinkNbrIpAddr = ' + str(self.cospfshamlinknbripaddr) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cospfshamlinkslocalipaddrtype is not None:
                    return True

                if self.cospfshamlinkslocalipaddr is not None:
                    return True

                if self.cospfshamlinknbrarea is not None:
                    return True

                if self.cospfshamlinknbripaddrtype is not None:
                    return True

                if self.cospfshamlinknbripaddr is not None:
                    return True

                if self.cospfshamlinknbrevents is not None:
                    return True

                if self.cospfshamlinknbrhellosuppressed is not None:
                    return True

                if self.cospfshamlinknbrlsretransqlen is not None:
                    return True

                if self.cospfshamlinknbroptions is not None:
                    return True

                if self.cospfshamlinknbrrtrid is not None:
                    return True

                if self.cospfshamlinknbrstate is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_MIB as meta
                return meta._meta_table['CiscoOspfMib.Cospfshamlinknbrtable.Cospfshamlinknbrentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfShamLinkNbrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cospfshamlinknbrentry is not None:
                for child_ref in self.cospfshamlinknbrentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_MIB as meta
            return meta._meta_table['CiscoOspfMib.Cospfshamlinknbrtable']['meta_info']


    class Cospfshamlinkstable(object):
        """
        Information about this router's sham links.
        
        .. attribute:: cospfshamlinksentry
        
        	Information about a single sham link
        	**type**\: list of    :py:class:`Cospfshamlinksentry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfshamlinkstable.Cospfshamlinksentry>`
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            self.parent = None
            self.cospfshamlinksentry = YList()
            self.cospfshamlinksentry.parent = self
            self.cospfshamlinksentry.name = 'cospfshamlinksentry'


        class Cospfshamlinksentry(object):
            """
            Information about a single sham link.
            
            .. attribute:: cospfshamlinksareaid  <key>
            
            	The area that this sham link is part of
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfshamlinkslocalipaddrtype  <key>
            
            	The type of internet address of this sham link's local IP address
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: cospfshamlinkslocalipaddr  <key>
            
            	The Local IP address of the sham link
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cospfshamlinksremoteipaddrtype  <key>
            
            	The type of internet address of this sham link's remote IP address
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
            .. attribute:: cospfshamlinksremoteipaddr  <key>
            
            	The IP address of the other end router of the sham link
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cospfshamlinksevents
            
            	The number of state changes or error events on this sham link
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfshamlinkshellointerval
            
            	The length of time, in  seconds,  between  the Hello  packets that the router sends on the sham link
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: cospfshamlinksmetric
            
            	The Metric to be advertised
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cospfshamlinksretransinterval
            
            	The number of seconds between  link\-state  advertisement retransmissions, for adjacencies belonging to this link. This value is also used when retransmitting database  description and link\-state request packets. This value should be well over the expected round trip time
            	**type**\:  int
            
            	**range:** 0..3600
            
            .. attribute:: cospfshamlinksrtrdeadinterval
            
            	The number of seconds that  a  router's  Hello packets  have  not been seen before it's neighbors declare the router down.  This  should  be some  multiple  of  the  Hello  interval
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cospfshamlinksstate
            
            	OSPF sham link states
            	**type**\:   :py:class:`CospfshamlinksstateEnum <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfshamlinkstable.Cospfshamlinksentry.CospfshamlinksstateEnum>`
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                self.parent = None
                self.cospfshamlinksareaid = None
                self.cospfshamlinkslocalipaddrtype = None
                self.cospfshamlinkslocalipaddr = None
                self.cospfshamlinksremoteipaddrtype = None
                self.cospfshamlinksremoteipaddr = None
                self.cospfshamlinksevents = None
                self.cospfshamlinkshellointerval = None
                self.cospfshamlinksmetric = None
                self.cospfshamlinksretransinterval = None
                self.cospfshamlinksrtrdeadinterval = None
                self.cospfshamlinksstate = None

            class CospfshamlinksstateEnum(Enum):
                """
                CospfshamlinksstateEnum

                OSPF sham link states.

                .. data:: down = 1

                .. data:: pointToPoint = 4

                """

                down = 1

                pointToPoint = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_MIB as meta
                    return meta._meta_table['CiscoOspfMib.Cospfshamlinkstable.Cospfshamlinksentry.CospfshamlinksstateEnum']


            @property
            def _common_path(self):
                if self.cospfshamlinksareaid is None:
                    raise YPYModelError('Key property cospfshamlinksareaid is None')
                if self.cospfshamlinkslocalipaddrtype is None:
                    raise YPYModelError('Key property cospfshamlinkslocalipaddrtype is None')
                if self.cospfshamlinkslocalipaddr is None:
                    raise YPYModelError('Key property cospfshamlinkslocalipaddr is None')
                if self.cospfshamlinksremoteipaddrtype is None:
                    raise YPYModelError('Key property cospfshamlinksremoteipaddrtype is None')
                if self.cospfshamlinksremoteipaddr is None:
                    raise YPYModelError('Key property cospfshamlinksremoteipaddr is None')

                return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfShamLinksTable/CISCO-OSPF-MIB:cospfShamLinksEntry[CISCO-OSPF-MIB:cospfShamLinksAreaId = ' + str(self.cospfshamlinksareaid) + '][CISCO-OSPF-MIB:cospfShamLinksLocalIpAddrType = ' + str(self.cospfshamlinkslocalipaddrtype) + '][CISCO-OSPF-MIB:cospfShamLinksLocalIpAddr = ' + str(self.cospfshamlinkslocalipaddr) + '][CISCO-OSPF-MIB:cospfShamLinksRemoteIpAddrType = ' + str(self.cospfshamlinksremoteipaddrtype) + '][CISCO-OSPF-MIB:cospfShamLinksRemoteIpAddr = ' + str(self.cospfshamlinksremoteipaddr) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cospfshamlinksareaid is not None:
                    return True

                if self.cospfshamlinkslocalipaddrtype is not None:
                    return True

                if self.cospfshamlinkslocalipaddr is not None:
                    return True

                if self.cospfshamlinksremoteipaddrtype is not None:
                    return True

                if self.cospfshamlinksremoteipaddr is not None:
                    return True

                if self.cospfshamlinksevents is not None:
                    return True

                if self.cospfshamlinkshellointerval is not None:
                    return True

                if self.cospfshamlinksmetric is not None:
                    return True

                if self.cospfshamlinksretransinterval is not None:
                    return True

                if self.cospfshamlinksrtrdeadinterval is not None:
                    return True

                if self.cospfshamlinksstate is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_MIB as meta
                return meta._meta_table['CiscoOspfMib.Cospfshamlinkstable.Cospfshamlinksentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfShamLinksTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cospfshamlinksentry is not None:
                for child_ref in self.cospfshamlinksentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_MIB as meta
            return meta._meta_table['CiscoOspfMib.Cospfshamlinkstable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cospfgeneralgroup is not None and self.cospfgeneralgroup._has_data():
            return True

        if self.cospflocallsdbtable is not None and self.cospflocallsdbtable._has_data():
            return True

        if self.cospflsdbtable is not None and self.cospflsdbtable._has_data():
            return True

        if self.cospfshamlinknbrtable is not None and self.cospfshamlinknbrtable._has_data():
            return True

        if self.cospfshamlinkstable is not None and self.cospfshamlinkstable._has_data():
            return True

        if self.cospfshamlinktable is not None and self.cospfshamlinktable._has_data():
            return True

        if self.cospfvirtlocallsdbtable is not None and self.cospfvirtlocallsdbtable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_OSPF_MIB as meta
        return meta._meta_table['CiscoOspfMib']['meta_info']



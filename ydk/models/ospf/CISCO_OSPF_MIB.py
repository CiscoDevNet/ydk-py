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

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.inet.INET_ADDRESS_MIB import InetAddressType_Enum


class CISCOOSPFMIB(object):
    """
    
    
    .. attribute:: cospfgeneralgroup
    
    	
    	**type**\: :py:class:`CospfGeneralGroup <ydk.models.ospf.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfGeneralGroup>`
    
    .. attribute:: cospflocallsdbtable
    
    	The OSPF Process's Link\-Local Link State Database for non\-virtual links
    	**type**\: :py:class:`CospfLocalLsdbTable <ydk.models.ospf.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfLocalLsdbTable>`
    
    .. attribute:: cospflsdbtable
    
    	The OSPF Process's Link State Database. This  table is meant for Opaque LSA's
    	**type**\: :py:class:`CospfLsdbTable <ydk.models.ospf.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfLsdbTable>`
    
    .. attribute:: cospfshamlinknbrtable
    
    	A table of sham link neighbor information
    	**type**\: :py:class:`CospfShamLinkNbrTable <ydk.models.ospf.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfShamLinkNbrTable>`
    
    .. attribute:: cospfshamlinkstable
    
    	Information about this router's sham links
    	**type**\: :py:class:`CospfShamLinksTable <ydk.models.ospf.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfShamLinksTable>`
    
    .. attribute:: cospfshamlinktable
    
    	Information about this router's sham links
    	**type**\: :py:class:`CospfShamLinkTable <ydk.models.ospf.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfShamLinkTable>`
    
    .. attribute:: cospfvirtlocallsdbtable
    
    	The OSPF Process's Link\-Local Link State Database for virtual links
    	**type**\: :py:class:`CospfVirtLocalLsdbTable <ydk.models.ospf.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfVirtLocalLsdbTable>`
    
    

    """

    _prefix = 'cisco-ospf'
    _revision = '2003-07-18'

    def __init__(self):
        self.cospfgeneralgroup = CISCOOSPFMIB.CospfGeneralGroup()
        self.cospfgeneralgroup.parent = self
        self.cospflocallsdbtable = CISCOOSPFMIB.CospfLocalLsdbTable()
        self.cospflocallsdbtable.parent = self
        self.cospflsdbtable = CISCOOSPFMIB.CospfLsdbTable()
        self.cospflsdbtable.parent = self
        self.cospfshamlinknbrtable = CISCOOSPFMIB.CospfShamLinkNbrTable()
        self.cospfshamlinknbrtable.parent = self
        self.cospfshamlinkstable = CISCOOSPFMIB.CospfShamLinksTable()
        self.cospfshamlinkstable.parent = self
        self.cospfshamlinktable = CISCOOSPFMIB.CospfShamLinkTable()
        self.cospfshamlinktable.parent = self
        self.cospfvirtlocallsdbtable = CISCOOSPFMIB.CospfVirtLocalLsdbTable()
        self.cospfvirtlocallsdbtable.parent = self


    class CospfGeneralGroup(object):
        """
        
        
        .. attribute:: cospfopaqueaslsacksumsum
        
        	The 32\-bit unsigned sum of the Opaque AS  link\-state advertisements' LS checksums contained link state database
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cospfopaqueaslsacount
        
        	The total number of Opaque AS link\-state advertisements in the link state database
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cospfopaquelsasupport
        
        	The router's support for Opaque LSA types
        	**type**\: bool
        
        .. attribute:: cospfrfc1583compatibility
        
        	Indicates metrics used to choose among multiple AS\- external\-LSAs. When cospfRFC1583Compatibility is set to enabled, only cost will be used when choosing among multiple AS\-external\-LSAs advertising the same destination. When cospfRFC1583Compatibility is set to disabled, preference will be driven first by type of path using cost only to break ties
        	**type**\: bool
        
        .. attribute:: cospftrafficengineeringsupport
        
        	The router's support for OSPF traffic engineering
        	**type**\: bool
        
        

        """

        _prefix = 'cisco-ospf'
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
            if not self.is_config():
                return False
            if self.is_presence():
                return True
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

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _CISCO_OSPF_MIB as meta
            return meta._meta_table['CISCOOSPFMIB.CospfGeneralGroup']['meta_info']


    class CospfLocalLsdbTable(object):
        """
        The OSPF Process's Link\-Local Link State Database
        for non\-virtual links.
        
        .. attribute:: cospflocallsdbentry
        
        	A single Link State Advertisement
        	**type**\: list of :py:class:`CospfLocalLsdbEntry <ydk.models.ospf.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfLocalLsdbTable.CospfLocalLsdbEntry>`
        
        

        """

        _prefix = 'cisco-ospf'
        _revision = '2003-07-18'

        def __init__(self):
            self.parent = None
            self.cospflocallsdbentry = YList()
            self.cospflocallsdbentry.parent = self
            self.cospflocallsdbentry.name = 'cospflocallsdbentry'


        class CospfLocalLsdbEntry(object):
            """
            A single Link State Advertisement.
            
            .. attribute:: cospflocallsdbaddresslessif
            
            	The Interface Index of the interface from which the LSA was received if the interface is unnumbered
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cospflocallsdbipaddress
            
            	The IP Address of the interface from which the LSA was received if the interface is numbered
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospflocallsdblsid
            
            	The Link State ID is an LS Type Specific field containing a 32 bit identifier in IP address format; it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospflocallsdbrouterid
            
            	The 32 bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospflocallsdbtype
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\: :py:class:`CospfLocalLsdbType_Enum <ydk.models.ospf.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfLocalLsdbTable.CospfLocalLsdbEntry.CospfLocalLsdbType_Enum>`
            
            .. attribute:: cospflocallsdbadvertisement
            
            	The entire Link State Advertisement, including its header
            	**type**\: str
            
            	**range:** 1..65535
            
            .. attribute:: cospflocallsdbage
            
            	This field is the age of the link state advertisement  in seconds
            	**type**\: int
            
            	**range:** 0..3600
            
            .. attribute:: cospflocallsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field. The age field is excepted so that an advertisement's age can be incremented without updating the checksum. The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred  to as the Fletcher checksum
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospflocallsdbsequence
            
            	The sequence number field is a signed 32\-bit integer. It is used to detect old and duplicate link state advertisements. The space of sequence numbers is linearly ordered. The larger the sequence number the more recent the advertisement
            	**type**\: int
            
            	**range:** \-2147483647..2147483647
            
            

            """

            _prefix = 'cisco-ospf'
            _revision = '2003-07-18'

            def __init__(self):
                self.parent = None
                self.cospflocallsdbaddresslessif = None
                self.cospflocallsdbipaddress = None
                self.cospflocallsdblsid = None
                self.cospflocallsdbrouterid = None
                self.cospflocallsdbtype = None
                self.cospflocallsdbadvertisement = None
                self.cospflocallsdbage = None
                self.cospflocallsdbchecksum = None
                self.cospflocallsdbsequence = None

            class CospfLocalLsdbType_Enum(Enum):
                """
                CospfLocalLsdbType_Enum

                The type of the link state advertisement.
                Each link state type has a separate advertisement format.

                """

                LOCALOPAQUELINK = 9


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _CISCO_OSPF_MIB as meta
                    return meta._meta_table['CISCOOSPFMIB.CospfLocalLsdbTable.CospfLocalLsdbEntry.CospfLocalLsdbType_Enum']


            @property
            def _common_path(self):
                if self.cospflocallsdbaddresslessif is None:
                    raise YPYDataValidationError('Key property cospflocallsdbaddresslessif is None')
                if self.cospflocallsdbipaddress is None:
                    raise YPYDataValidationError('Key property cospflocallsdbipaddress is None')
                if self.cospflocallsdblsid is None:
                    raise YPYDataValidationError('Key property cospflocallsdblsid is None')
                if self.cospflocallsdbrouterid is None:
                    raise YPYDataValidationError('Key property cospflocallsdbrouterid is None')
                if self.cospflocallsdbtype is None:
                    raise YPYDataValidationError('Key property cospflocallsdbtype is None')

                return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfLocalLsdbTable/CISCO-OSPF-MIB:cospfLocalLsdbEntry[CISCO-OSPF-MIB:cospfLocalLsdbAddressLessIf = ' + str(self.cospflocallsdbaddresslessif) + '][CISCO-OSPF-MIB:cospfLocalLsdbIpAddress = ' + str(self.cospflocallsdbipaddress) + '][CISCO-OSPF-MIB:cospfLocalLsdbLsid = ' + str(self.cospflocallsdblsid) + '][CISCO-OSPF-MIB:cospfLocalLsdbRouterId = ' + str(self.cospflocallsdbrouterid) + '][CISCO-OSPF-MIB:cospfLocalLsdbType = ' + str(self.cospflocallsdbtype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cospflocallsdbaddresslessif is not None:
                    return True

                if self.cospflocallsdbipaddress is not None:
                    return True

                if self.cospflocallsdblsid is not None:
                    return True

                if self.cospflocallsdbrouterid is not None:
                    return True

                if self.cospflocallsdbtype is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _CISCO_OSPF_MIB as meta
                return meta._meta_table['CISCOOSPFMIB.CospfLocalLsdbTable.CospfLocalLsdbEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfLocalLsdbTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cospflocallsdbentry is not None:
                for child_ref in self.cospflocallsdbentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _CISCO_OSPF_MIB as meta
            return meta._meta_table['CISCOOSPFMIB.CospfLocalLsdbTable']['meta_info']


    class CospfLsdbTable(object):
        """
        The OSPF Process's Link State Database. This 
        table is meant for Opaque LSA's
        
        .. attribute:: cospflsdbentry
        
        	A single Link State Advertisement
        	**type**\: list of :py:class:`CospfLsdbEntry <ydk.models.ospf.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfLsdbTable.CospfLsdbEntry>`
        
        

        """

        _prefix = 'cisco-ospf'
        _revision = '2003-07-18'

        def __init__(self):
            self.parent = None
            self.cospflsdbentry = YList()
            self.cospflsdbentry.parent = self
            self.cospflsdbentry.name = 'cospflsdbentry'


        class CospfLsdbEntry(object):
            """
            A single Link State Advertisement.
            
            .. attribute:: cospflsdbtype
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\: :py:class:`CospfLsdbType_Enum <ydk.models.ospf.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfLsdbTable.CospfLsdbEntry.CospfLsdbType_Enum>`
            
            .. attribute:: ospflsdbareaid
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospflsdblsid
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ospflsdbrouterid
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospflsdbadvertisement
            
            	The entire Link State Advertisement, including its header
            	**type**\: str
            
            	**range:** 1..65535
            
            .. attribute:: cospflsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cospflsdbchecksum
            
            	This field is the  checksum  of  the  complete contents  of  the  advertisement, excepting the age field.  The age field is excepted  so  that an   advertisement's  age  can  be  incremented without updating the  checksum.   The  checksum used  is  the same that is used for ISO connectionless datagrams; it is commonly referred  to as the Fletcher checksum
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cospflsdbsequence
            
            	The sequence number field is a  signed  32\-bit integer.   It  is used to detect old and duplicate link state advertisements.  The  space  of sequence  numbers  is  linearly  ordered.   The larger the sequence number the more recent  the advertisement
            	**type**\: int
            
            	**range:** 1..147483647
            
            

            """

            _prefix = 'cisco-ospf'
            _revision = '2003-07-18'

            def __init__(self):
                self.parent = None
                self.cospflsdbtype = None
                self.ospflsdbareaid = None
                self.ospflsdblsid = None
                self.ospflsdbrouterid = None
                self.cospflsdbadvertisement = None
                self.cospflsdbage = None
                self.cospflsdbchecksum = None
                self.cospflsdbsequence = None

            class CospfLsdbType_Enum(Enum):
                """
                CospfLsdbType_Enum

                The type of the link state advertisement.
                Each link state type has a separate advertisement format.

                """

                AREAOPAQUELINK = 10

                ASOPAQUELINK = 11


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _CISCO_OSPF_MIB as meta
                    return meta._meta_table['CISCOOSPFMIB.CospfLsdbTable.CospfLsdbEntry.CospfLsdbType_Enum']


            @property
            def _common_path(self):
                if self.cospflsdbtype is None:
                    raise YPYDataValidationError('Key property cospflsdbtype is None')
                if self.ospflsdbareaid is None:
                    raise YPYDataValidationError('Key property ospflsdbareaid is None')
                if self.ospflsdblsid is None:
                    raise YPYDataValidationError('Key property ospflsdblsid is None')
                if self.ospflsdbrouterid is None:
                    raise YPYDataValidationError('Key property ospflsdbrouterid is None')

                return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfLsdbTable/CISCO-OSPF-MIB:cospfLsdbEntry[CISCO-OSPF-MIB:cospfLsdbType = ' + str(self.cospflsdbtype) + '][CISCO-OSPF-MIB:ospfLsdbAreaId = ' + str(self.ospflsdbareaid) + '][CISCO-OSPF-MIB:ospfLsdbLsid = ' + str(self.ospflsdblsid) + '][CISCO-OSPF-MIB:ospfLsdbRouterId = ' + str(self.ospflsdbrouterid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cospflsdbtype is not None:
                    return True

                if self.ospflsdbareaid is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _CISCO_OSPF_MIB as meta
                return meta._meta_table['CISCOOSPFMIB.CospfLsdbTable.CospfLsdbEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfLsdbTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cospflsdbentry is not None:
                for child_ref in self.cospflsdbentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _CISCO_OSPF_MIB as meta
            return meta._meta_table['CISCOOSPFMIB.CospfLsdbTable']['meta_info']


    class CospfShamLinkNbrTable(object):
        """
        A table of sham link neighbor information.
        
        .. attribute:: cospfshamlinknbrentry
        
        	Sham link neighbor information
        	**type**\: list of :py:class:`CospfShamLinkNbrEntry <ydk.models.ospf.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfShamLinkNbrTable.CospfShamLinkNbrEntry>`
        
        

        """

        _prefix = 'cisco-ospf'
        _revision = '2003-07-18'

        def __init__(self):
            self.parent = None
            self.cospfshamlinknbrentry = YList()
            self.cospfshamlinknbrentry.parent = self
            self.cospfshamlinknbrentry.name = 'cospfshamlinknbrentry'


        class CospfShamLinkNbrEntry(object):
            """
            Sham link neighbor information.
            
            .. attribute:: cospfshamlinknbrarea
            
            	The area to which the sham link is part of
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfshamlinknbripaddr
            
            	The IP address this sham link neighbor is using
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cospfshamlinknbripaddrtype
            
            	The type of internet address of this sham link neighbor's IP address
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cospfshamlinkslocalipaddr
            
            	
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cospfshamlinkslocalipaddrtype
            
            	
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cospfshamlinknbrevents
            
            	The number of  times  this sham link has changed state or an error has occurred
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfshamlinknbrhellosuppressed
            
            	Indicates whether Hellos are being  suppressed to the neighbor
            	**type**\: bool
            
            .. attribute:: cospfshamlinknbrlsretransqlen
            
            	The  current  length  of  the   retransmission queue. The retransmission queue is maintained for LSAs that have been flooded but not acknowledged on this adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfshamlinknbroptions
            
            	A Bit Mask corresponding to the neighbor's options field.  Bit 1, if set, indicates that the  system  will operate  on  Type of Service metrics other than TOS 0.  If zero, the neighbor will  ignore  all metrics except the TOS 0 metric.  Bit 2, if set, indicates  that  the  system  is Network  Multicast  capable; ie, that it implements  OSPF Multicast Routing
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cospfshamlinknbrrtrid
            
            	A 32\-bit integer uniquely identifying the neighboring router
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfshamlinknbrstate
            
            	The state of this sham link neighbor relation\- ship
            	**type**\: :py:class:`CospfShamLinkNbrState_Enum <ydk.models.ospf.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfShamLinkNbrTable.CospfShamLinkNbrEntry.CospfShamLinkNbrState_Enum>`
            
            

            """

            _prefix = 'cisco-ospf'
            _revision = '2003-07-18'

            def __init__(self):
                self.parent = None
                self.cospfshamlinknbrarea = None
                self.cospfshamlinknbripaddr = None
                self.cospfshamlinknbripaddrtype = None
                self.cospfshamlinkslocalipaddr = None
                self.cospfshamlinkslocalipaddrtype = None
                self.cospfshamlinknbrevents = None
                self.cospfshamlinknbrhellosuppressed = None
                self.cospfshamlinknbrlsretransqlen = None
                self.cospfshamlinknbroptions = None
                self.cospfshamlinknbrrtrid = None
                self.cospfshamlinknbrstate = None

            class CospfShamLinkNbrState_Enum(Enum):
                """
                CospfShamLinkNbrState_Enum

                The state of this sham link neighbor relation\-
                ship.

                """

                DOWN = 1

                ATTEMPT = 2

                INIT = 3

                TWOWAY = 4

                EXCHANGESTART = 5

                EXCHANGE = 6

                LOADING = 7

                FULL = 8


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _CISCO_OSPF_MIB as meta
                    return meta._meta_table['CISCOOSPFMIB.CospfShamLinkNbrTable.CospfShamLinkNbrEntry.CospfShamLinkNbrState_Enum']


            @property
            def _common_path(self):
                if self.cospfshamlinknbrarea is None:
                    raise YPYDataValidationError('Key property cospfshamlinknbrarea is None')
                if self.cospfshamlinknbripaddr is None:
                    raise YPYDataValidationError('Key property cospfshamlinknbripaddr is None')
                if self.cospfshamlinknbripaddrtype is None:
                    raise YPYDataValidationError('Key property cospfshamlinknbripaddrtype is None')
                if self.cospfshamlinkslocalipaddr is None:
                    raise YPYDataValidationError('Key property cospfshamlinkslocalipaddr is None')
                if self.cospfshamlinkslocalipaddrtype is None:
                    raise YPYDataValidationError('Key property cospfshamlinkslocalipaddrtype is None')

                return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfShamLinkNbrTable/CISCO-OSPF-MIB:cospfShamLinkNbrEntry[CISCO-OSPF-MIB:cospfShamLinkNbrArea = ' + str(self.cospfshamlinknbrarea) + '][CISCO-OSPF-MIB:cospfShamLinkNbrIpAddr = ' + str(self.cospfshamlinknbripaddr) + '][CISCO-OSPF-MIB:cospfShamLinkNbrIpAddrType = ' + str(self.cospfshamlinknbripaddrtype) + '][CISCO-OSPF-MIB:cospfShamLinksLocalIpAddr = ' + str(self.cospfshamlinkslocalipaddr) + '][CISCO-OSPF-MIB:cospfShamLinksLocalIpAddrType = ' + str(self.cospfshamlinkslocalipaddrtype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cospfshamlinknbrarea is not None:
                    return True

                if self.cospfshamlinknbripaddr is not None:
                    return True

                if self.cospfshamlinknbripaddrtype is not None:
                    return True

                if self.cospfshamlinkslocalipaddr is not None:
                    return True

                if self.cospfshamlinkslocalipaddrtype is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _CISCO_OSPF_MIB as meta
                return meta._meta_table['CISCOOSPFMIB.CospfShamLinkNbrTable.CospfShamLinkNbrEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfShamLinkNbrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cospfshamlinknbrentry is not None:
                for child_ref in self.cospfshamlinknbrentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _CISCO_OSPF_MIB as meta
            return meta._meta_table['CISCOOSPFMIB.CospfShamLinkNbrTable']['meta_info']


    class CospfShamLinkTable(object):
        """
        Information about this router's sham links
        
        .. attribute:: cospfshamlinkentry
        
        	Information about a single sham link
        	**type**\: list of :py:class:`CospfShamLinkEntry <ydk.models.ospf.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfShamLinkTable.CospfShamLinkEntry>`
        
        

        """

        _prefix = 'cisco-ospf'
        _revision = '2003-07-18'

        def __init__(self):
            self.parent = None
            self.cospfshamlinkentry = YList()
            self.cospfshamlinkentry.parent = self
            self.cospfshamlinkentry.name = 'cospfshamlinkentry'


        class CospfShamLinkEntry(object):
            """
            Information about a single sham link
            
            .. attribute:: cospfshamlinkareaid
            
            	The  Transit  Area  that  the   Virtual   Link traverses.  By definition, this is not 0.0.0.0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfshamlinklocalipaddress
            
            	The Local IP address of the sham link
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfshamlinkneighborid
            
            	The Router ID of the other end router of the sham link
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfshamlinkevents
            
            	The number of state changes or error events on this sham link
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfshamlinkhellointerval
            
            	The length of time, in  seconds,  between  the Hello  packets that the router sends on the sham link
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: cospfshamlinkmetric
            
            	The Metric to be advertised
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cospfshamlinkretransinterval
            
            	The number of seconds between  link\-state  advertisement retransmissions,  for  adjacencies belonging to this  link.   This  value  is also used when retransmitting database description   and  link\-state  request  packets. This value   should  be well over the expected round trip time
            	**type**\: int
            
            	**range:** 0..3600
            
            .. attribute:: cospfshamlinkrtrdeadinterval
            
            	The number of seconds that  a  router's  Hello packets  have  not been seen before it's neighbors declare the router down.  This  should  be some  multiple  of  the  Hello  interval
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cospfshamlinkstate
            
            	OSPF sham link states
            	**type**\: :py:class:`CospfShamLinkState_Enum <ydk.models.ospf.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfShamLinkTable.CospfShamLinkEntry.CospfShamLinkState_Enum>`
            
            

            """

            _prefix = 'cisco-ospf'
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

            class CospfShamLinkState_Enum(Enum):
                """
                CospfShamLinkState_Enum

                OSPF sham link states.

                """

                DOWN = 1

                POINTTOPOINT = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _CISCO_OSPF_MIB as meta
                    return meta._meta_table['CISCOOSPFMIB.CospfShamLinkTable.CospfShamLinkEntry.CospfShamLinkState_Enum']


            @property
            def _common_path(self):
                if self.cospfshamlinkareaid is None:
                    raise YPYDataValidationError('Key property cospfshamlinkareaid is None')
                if self.cospfshamlinklocalipaddress is None:
                    raise YPYDataValidationError('Key property cospfshamlinklocalipaddress is None')
                if self.cospfshamlinkneighborid is None:
                    raise YPYDataValidationError('Key property cospfshamlinkneighborid is None')

                return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfShamLinkTable/CISCO-OSPF-MIB:cospfShamLinkEntry[CISCO-OSPF-MIB:cospfShamLinkAreaId = ' + str(self.cospfshamlinkareaid) + '][CISCO-OSPF-MIB:cospfShamLinkLocalIpAddress = ' + str(self.cospfshamlinklocalipaddress) + '][CISCO-OSPF-MIB:cospfShamLinkNeighborId = ' + str(self.cospfshamlinkneighborid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _CISCO_OSPF_MIB as meta
                return meta._meta_table['CISCOOSPFMIB.CospfShamLinkTable.CospfShamLinkEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfShamLinkTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cospfshamlinkentry is not None:
                for child_ref in self.cospfshamlinkentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _CISCO_OSPF_MIB as meta
            return meta._meta_table['CISCOOSPFMIB.CospfShamLinkTable']['meta_info']


    class CospfShamLinksTable(object):
        """
        Information about this router's sham links.
        
        .. attribute:: cospfshamlinksentry
        
        	Information about a single sham link
        	**type**\: list of :py:class:`CospfShamLinksEntry <ydk.models.ospf.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfShamLinksTable.CospfShamLinksEntry>`
        
        

        """

        _prefix = 'cisco-ospf'
        _revision = '2003-07-18'

        def __init__(self):
            self.parent = None
            self.cospfshamlinksentry = YList()
            self.cospfshamlinksentry.parent = self
            self.cospfshamlinksentry.name = 'cospfshamlinksentry'


        class CospfShamLinksEntry(object):
            """
            Information about a single sham link.
            
            .. attribute:: cospfshamlinksareaid
            
            	The area that this sham link is part of
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfshamlinkslocalipaddr
            
            	The Local IP address of the sham link
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cospfshamlinkslocalipaddrtype
            
            	The type of internet address of this sham link's local IP address
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cospfshamlinksremoteipaddr
            
            	The IP address of the other end router of the sham link
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cospfshamlinksremoteipaddrtype
            
            	The type of internet address of this sham link's remote IP address
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cospfshamlinksevents
            
            	The number of state changes or error events on this sham link
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfshamlinkshellointerval
            
            	The length of time, in  seconds,  between  the Hello  packets that the router sends on the sham link
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: cospfshamlinksmetric
            
            	The Metric to be advertised
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cospfshamlinksretransinterval
            
            	The number of seconds between  link\-state  advertisement retransmissions, for adjacencies belonging to this link. This value is also used when retransmitting database  description and link\-state request packets. This value should be well over the expected round trip time
            	**type**\: int
            
            	**range:** 0..3600
            
            .. attribute:: cospfshamlinksrtrdeadinterval
            
            	The number of seconds that  a  router's  Hello packets  have  not been seen before it's neighbors declare the router down.  This  should  be some  multiple  of  the  Hello  interval
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cospfshamlinksstate
            
            	OSPF sham link states
            	**type**\: :py:class:`CospfShamLinksState_Enum <ydk.models.ospf.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfShamLinksTable.CospfShamLinksEntry.CospfShamLinksState_Enum>`
            
            

            """

            _prefix = 'cisco-ospf'
            _revision = '2003-07-18'

            def __init__(self):
                self.parent = None
                self.cospfshamlinksareaid = None
                self.cospfshamlinkslocalipaddr = None
                self.cospfshamlinkslocalipaddrtype = None
                self.cospfshamlinksremoteipaddr = None
                self.cospfshamlinksremoteipaddrtype = None
                self.cospfshamlinksevents = None
                self.cospfshamlinkshellointerval = None
                self.cospfshamlinksmetric = None
                self.cospfshamlinksretransinterval = None
                self.cospfshamlinksrtrdeadinterval = None
                self.cospfshamlinksstate = None

            class CospfShamLinksState_Enum(Enum):
                """
                CospfShamLinksState_Enum

                OSPF sham link states.

                """

                DOWN = 1

                POINTTOPOINT = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _CISCO_OSPF_MIB as meta
                    return meta._meta_table['CISCOOSPFMIB.CospfShamLinksTable.CospfShamLinksEntry.CospfShamLinksState_Enum']


            @property
            def _common_path(self):
                if self.cospfshamlinksareaid is None:
                    raise YPYDataValidationError('Key property cospfshamlinksareaid is None')
                if self.cospfshamlinkslocalipaddr is None:
                    raise YPYDataValidationError('Key property cospfshamlinkslocalipaddr is None')
                if self.cospfshamlinkslocalipaddrtype is None:
                    raise YPYDataValidationError('Key property cospfshamlinkslocalipaddrtype is None')
                if self.cospfshamlinksremoteipaddr is None:
                    raise YPYDataValidationError('Key property cospfshamlinksremoteipaddr is None')
                if self.cospfshamlinksremoteipaddrtype is None:
                    raise YPYDataValidationError('Key property cospfshamlinksremoteipaddrtype is None')

                return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfShamLinksTable/CISCO-OSPF-MIB:cospfShamLinksEntry[CISCO-OSPF-MIB:cospfShamLinksAreaId = ' + str(self.cospfshamlinksareaid) + '][CISCO-OSPF-MIB:cospfShamLinksLocalIpAddr = ' + str(self.cospfshamlinkslocalipaddr) + '][CISCO-OSPF-MIB:cospfShamLinksLocalIpAddrType = ' + str(self.cospfshamlinkslocalipaddrtype) + '][CISCO-OSPF-MIB:cospfShamLinksRemoteIpAddr = ' + str(self.cospfshamlinksremoteipaddr) + '][CISCO-OSPF-MIB:cospfShamLinksRemoteIpAddrType = ' + str(self.cospfshamlinksremoteipaddrtype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cospfshamlinksareaid is not None:
                    return True

                if self.cospfshamlinkslocalipaddr is not None:
                    return True

                if self.cospfshamlinkslocalipaddrtype is not None:
                    return True

                if self.cospfshamlinksremoteipaddr is not None:
                    return True

                if self.cospfshamlinksremoteipaddrtype is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _CISCO_OSPF_MIB as meta
                return meta._meta_table['CISCOOSPFMIB.CospfShamLinksTable.CospfShamLinksEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfShamLinksTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cospfshamlinksentry is not None:
                for child_ref in self.cospfshamlinksentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _CISCO_OSPF_MIB as meta
            return meta._meta_table['CISCOOSPFMIB.CospfShamLinksTable']['meta_info']


    class CospfVirtLocalLsdbTable(object):
        """
        The OSPF Process's Link\-Local Link State Database
        for virtual links.
        
        .. attribute:: cospfvirtlocallsdbentry
        
        	A single Link State Advertisement
        	**type**\: list of :py:class:`CospfVirtLocalLsdbEntry <ydk.models.ospf.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfVirtLocalLsdbTable.CospfVirtLocalLsdbEntry>`
        
        

        """

        _prefix = 'cisco-ospf'
        _revision = '2003-07-18'

        def __init__(self):
            self.parent = None
            self.cospfvirtlocallsdbentry = YList()
            self.cospfvirtlocallsdbentry.parent = self
            self.cospfvirtlocallsdbentry.name = 'cospfvirtlocallsdbentry'


        class CospfVirtLocalLsdbEntry(object):
            """
            A single Link State Advertisement.
            
            .. attribute:: cospfvirtlocallsdblsid
            
            	The Link State ID is an LS Type Specific field containing a 32 bit identifier in IP address format; it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfvirtlocallsdbneighbor
            
            	The Router ID of the Virtual Neighbor
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfvirtlocallsdbrouterid
            
            	The 32 bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfvirtlocallsdbtransitarea
            
            	The Transit Area that the Virtual Link traverses. By definition, this is not 0.0.0.0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfvirtlocallsdbtype
            
            	The type of the link state advertisement. Each  link state type has a separate advertisement format
            	**type**\: :py:class:`CospfVirtLocalLsdbType_Enum <ydk.models.ospf.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfVirtLocalLsdbTable.CospfVirtLocalLsdbEntry.CospfVirtLocalLsdbType_Enum>`
            
            .. attribute:: cospfvirtlocallsdbadvertisement
            
            	The entire Link State Advertisement, including its header
            	**type**\: str
            
            	**range:** 1..65535
            
            .. attribute:: cospfvirtlocallsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\: int
            
            	**range:** 0..3600
            
            .. attribute:: cospfvirtlocallsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field. The age field is excepted so that an advertisement's age can be incremented without updating the checksum. The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred  to as the Fletcher checksum
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfvirtlocallsdbsequence
            
            	The sequence number field is a  signed  32\-bit integer. It is used to detect old and duplicate link state advertisements. The space of sequence numbers is linearly ordered. The larger the sequence number the more recent the advertisement
            	**type**\: int
            
            	**range:** \-2147483647..2147483647
            
            

            """

            _prefix = 'cisco-ospf'
            _revision = '2003-07-18'

            def __init__(self):
                self.parent = None
                self.cospfvirtlocallsdblsid = None
                self.cospfvirtlocallsdbneighbor = None
                self.cospfvirtlocallsdbrouterid = None
                self.cospfvirtlocallsdbtransitarea = None
                self.cospfvirtlocallsdbtype = None
                self.cospfvirtlocallsdbadvertisement = None
                self.cospfvirtlocallsdbage = None
                self.cospfvirtlocallsdbchecksum = None
                self.cospfvirtlocallsdbsequence = None

            class CospfVirtLocalLsdbType_Enum(Enum):
                """
                CospfVirtLocalLsdbType_Enum

                The type of the link state advertisement.
                Each  link state type has a separate advertisement format.

                """

                LOCALOPAQUELINK = 9


                @staticmethod
                def _meta_info():
                    from ydk.models.ospf._meta import _CISCO_OSPF_MIB as meta
                    return meta._meta_table['CISCOOSPFMIB.CospfVirtLocalLsdbTable.CospfVirtLocalLsdbEntry.CospfVirtLocalLsdbType_Enum']


            @property
            def _common_path(self):
                if self.cospfvirtlocallsdblsid is None:
                    raise YPYDataValidationError('Key property cospfvirtlocallsdblsid is None')
                if self.cospfvirtlocallsdbneighbor is None:
                    raise YPYDataValidationError('Key property cospfvirtlocallsdbneighbor is None')
                if self.cospfvirtlocallsdbrouterid is None:
                    raise YPYDataValidationError('Key property cospfvirtlocallsdbrouterid is None')
                if self.cospfvirtlocallsdbtransitarea is None:
                    raise YPYDataValidationError('Key property cospfvirtlocallsdbtransitarea is None')
                if self.cospfvirtlocallsdbtype is None:
                    raise YPYDataValidationError('Key property cospfvirtlocallsdbtype is None')

                return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfVirtLocalLsdbTable/CISCO-OSPF-MIB:cospfVirtLocalLsdbEntry[CISCO-OSPF-MIB:cospfVirtLocalLsdbLsid = ' + str(self.cospfvirtlocallsdblsid) + '][CISCO-OSPF-MIB:cospfVirtLocalLsdbNeighbor = ' + str(self.cospfvirtlocallsdbneighbor) + '][CISCO-OSPF-MIB:cospfVirtLocalLsdbRouterId = ' + str(self.cospfvirtlocallsdbrouterid) + '][CISCO-OSPF-MIB:cospfVirtLocalLsdbTransitArea = ' + str(self.cospfvirtlocallsdbtransitarea) + '][CISCO-OSPF-MIB:cospfVirtLocalLsdbType = ' + str(self.cospfvirtlocallsdbtype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cospfvirtlocallsdblsid is not None:
                    return True

                if self.cospfvirtlocallsdbneighbor is not None:
                    return True

                if self.cospfvirtlocallsdbrouterid is not None:
                    return True

                if self.cospfvirtlocallsdbtransitarea is not None:
                    return True

                if self.cospfvirtlocallsdbtype is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ospf._meta import _CISCO_OSPF_MIB as meta
                return meta._meta_table['CISCOOSPFMIB.CospfVirtLocalLsdbTable.CospfVirtLocalLsdbEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB/CISCO-OSPF-MIB:cospfVirtLocalLsdbTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cospfvirtlocallsdbentry is not None:
                for child_ref in self.cospfvirtlocallsdbentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ospf._meta import _CISCO_OSPF_MIB as meta
            return meta._meta_table['CISCOOSPFMIB.CospfVirtLocalLsdbTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-OSPF-MIB:CISCO-OSPF-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cospfgeneralgroup is not None and self.cospfgeneralgroup._has_data():
            return True

        if self.cospfgeneralgroup is not None and self.cospfgeneralgroup.is_presence():
            return True

        if self.cospflocallsdbtable is not None and self.cospflocallsdbtable._has_data():
            return True

        if self.cospflocallsdbtable is not None and self.cospflocallsdbtable.is_presence():
            return True

        if self.cospflsdbtable is not None and self.cospflsdbtable._has_data():
            return True

        if self.cospflsdbtable is not None and self.cospflsdbtable.is_presence():
            return True

        if self.cospfshamlinknbrtable is not None and self.cospfshamlinknbrtable._has_data():
            return True

        if self.cospfshamlinknbrtable is not None and self.cospfshamlinknbrtable.is_presence():
            return True

        if self.cospfshamlinkstable is not None and self.cospfshamlinkstable._has_data():
            return True

        if self.cospfshamlinkstable is not None and self.cospfshamlinkstable.is_presence():
            return True

        if self.cospfshamlinktable is not None and self.cospfshamlinktable._has_data():
            return True

        if self.cospfshamlinktable is not None and self.cospfshamlinktable.is_presence():
            return True

        if self.cospfvirtlocallsdbtable is not None and self.cospfvirtlocallsdbtable._has_data():
            return True

        if self.cospfvirtlocallsdbtable is not None and self.cospfvirtlocallsdbtable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ospf._meta import _CISCO_OSPF_MIB as meta
        return meta._meta_table['CISCOOSPFMIB']['meta_info']



""" CISCO_OSPF_MIB 

An extension to the MIB module defined in
RFC 1850 for managing OSPF implimentation. 
Most of the MIB definitions are based on
the IETF draft 
< draft\-ietf\-ospf\-mib\-update\-05.txt > . 
Support for OSPF Sham link is also added

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOOSPFMIB(Entity):
    """
    
    
    .. attribute:: cospfgeneralgroup
    
    	
    	**type**\:  :py:class:`CospfGeneralGroup <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfGeneralGroup>`
    
    .. attribute:: cospflsdbtable
    
    	The OSPF Process's Link State Database. This  table is meant for Opaque LSA's
    	**type**\:  :py:class:`CospfLsdbTable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfLsdbTable>`
    
    .. attribute:: cospfshamlinktable
    
    	Information about this router's sham links
    	**type**\:  :py:class:`CospfShamLinkTable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfShamLinkTable>`
    
    	**status**\: deprecated
    
    .. attribute:: cospflocallsdbtable
    
    	The OSPF Process's Link\-Local Link State Database for non\-virtual links
    	**type**\:  :py:class:`CospfLocalLsdbTable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfLocalLsdbTable>`
    
    .. attribute:: cospfvirtlocallsdbtable
    
    	The OSPF Process's Link\-Local Link State Database for virtual links
    	**type**\:  :py:class:`CospfVirtLocalLsdbTable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfVirtLocalLsdbTable>`
    
    .. attribute:: cospfshamlinknbrtable
    
    	A table of sham link neighbor information
    	**type**\:  :py:class:`CospfShamLinkNbrTable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfShamLinkNbrTable>`
    
    .. attribute:: cospfshamlinkstable
    
    	Information about this router's sham links
    	**type**\:  :py:class:`CospfShamLinksTable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfShamLinksTable>`
    
    

    """

    _prefix = 'CISCO-OSPF-MIB'
    _revision = '2003-07-18'

    def __init__(self):
        super(CISCOOSPFMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-OSPF-MIB"
        self.yang_parent_name = "CISCO-OSPF-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cospfGeneralGroup", ("cospfgeneralgroup", CISCOOSPFMIB.CospfGeneralGroup)), ("cospfLsdbTable", ("cospflsdbtable", CISCOOSPFMIB.CospfLsdbTable)), ("cospfShamLinkTable", ("cospfshamlinktable", CISCOOSPFMIB.CospfShamLinkTable)), ("cospfLocalLsdbTable", ("cospflocallsdbtable", CISCOOSPFMIB.CospfLocalLsdbTable)), ("cospfVirtLocalLsdbTable", ("cospfvirtlocallsdbtable", CISCOOSPFMIB.CospfVirtLocalLsdbTable)), ("cospfShamLinkNbrTable", ("cospfshamlinknbrtable", CISCOOSPFMIB.CospfShamLinkNbrTable)), ("cospfShamLinksTable", ("cospfshamlinkstable", CISCOOSPFMIB.CospfShamLinksTable))])
        self._leafs = OrderedDict()

        self.cospfgeneralgroup = CISCOOSPFMIB.CospfGeneralGroup()
        self.cospfgeneralgroup.parent = self
        self._children_name_map["cospfgeneralgroup"] = "cospfGeneralGroup"

        self.cospflsdbtable = CISCOOSPFMIB.CospfLsdbTable()
        self.cospflsdbtable.parent = self
        self._children_name_map["cospflsdbtable"] = "cospfLsdbTable"

        self.cospfshamlinktable = CISCOOSPFMIB.CospfShamLinkTable()
        self.cospfshamlinktable.parent = self
        self._children_name_map["cospfshamlinktable"] = "cospfShamLinkTable"

        self.cospflocallsdbtable = CISCOOSPFMIB.CospfLocalLsdbTable()
        self.cospflocallsdbtable.parent = self
        self._children_name_map["cospflocallsdbtable"] = "cospfLocalLsdbTable"

        self.cospfvirtlocallsdbtable = CISCOOSPFMIB.CospfVirtLocalLsdbTable()
        self.cospfvirtlocallsdbtable.parent = self
        self._children_name_map["cospfvirtlocallsdbtable"] = "cospfVirtLocalLsdbTable"

        self.cospfshamlinknbrtable = CISCOOSPFMIB.CospfShamLinkNbrTable()
        self.cospfshamlinknbrtable.parent = self
        self._children_name_map["cospfshamlinknbrtable"] = "cospfShamLinkNbrTable"

        self.cospfshamlinkstable = CISCOOSPFMIB.CospfShamLinksTable()
        self.cospfshamlinkstable.parent = self
        self._children_name_map["cospfshamlinkstable"] = "cospfShamLinksTable"
        self._segment_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOOSPFMIB, [], name, value)


    class CospfGeneralGroup(Entity):
        """
        
        
        .. attribute:: cospfrfc1583compatibility
        
        	Indicates metrics used to choose among multiple AS\- external\-LSAs. When cospfRFC1583Compatibility is set to enabled, only cost will be used when choosing among multiple AS\-external\-LSAs advertising the same destination. When cospfRFC1583Compatibility is set to disabled, preference will be driven first by type of path using cost only to break ties
        	**type**\: bool
        
        .. attribute:: cospfopaquelsasupport
        
        	The router's support for Opaque LSA types
        	**type**\: bool
        
        .. attribute:: cospftrafficengineeringsupport
        
        	The router's support for OSPF traffic engineering
        	**type**\: bool
        
        .. attribute:: cospfopaqueaslsacount
        
        	The total number of Opaque AS link\-state advertisements in the link state database
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cospfopaqueaslsacksumsum
        
        	The 32\-bit unsigned sum of the Opaque AS  link\-state advertisements' LS checksums contained link state database
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            super(CISCOOSPFMIB.CospfGeneralGroup, self).__init__()

            self.yang_name = "cospfGeneralGroup"
            self.yang_parent_name = "CISCO-OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cospfrfc1583compatibility', (YLeaf(YType.boolean, 'cospfRFC1583Compatibility'), ['bool'])),
                ('cospfopaquelsasupport', (YLeaf(YType.boolean, 'cospfOpaqueLsaSupport'), ['bool'])),
                ('cospftrafficengineeringsupport', (YLeaf(YType.boolean, 'cospfTrafficEngineeringSupport'), ['bool'])),
                ('cospfopaqueaslsacount', (YLeaf(YType.uint32, 'cospfOpaqueASLsaCount'), ['int'])),
                ('cospfopaqueaslsacksumsum', (YLeaf(YType.uint32, 'cospfOpaqueASLsaCksumSum'), ['int'])),
            ])
            self.cospfrfc1583compatibility = None
            self.cospfopaquelsasupport = None
            self.cospftrafficengineeringsupport = None
            self.cospfopaqueaslsacount = None
            self.cospfopaqueaslsacksumsum = None
            self._segment_path = lambda: "cospfGeneralGroup"
            self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOOSPFMIB.CospfGeneralGroup, [u'cospfrfc1583compatibility', u'cospfopaquelsasupport', u'cospftrafficengineeringsupport', u'cospfopaqueaslsacount', u'cospfopaqueaslsacksumsum'], name, value)


    class CospfLsdbTable(Entity):
        """
        The OSPF Process's Link State Database. This 
        table is meant for Opaque LSA's
        
        .. attribute:: cospflsdbentry
        
        	A single Link State Advertisement
        	**type**\: list of  		 :py:class:`CospfLsdbEntry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfLsdbTable.CospfLsdbEntry>`
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            super(CISCOOSPFMIB.CospfLsdbTable, self).__init__()

            self.yang_name = "cospfLsdbTable"
            self.yang_parent_name = "CISCO-OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cospfLsdbEntry", ("cospflsdbentry", CISCOOSPFMIB.CospfLsdbTable.CospfLsdbEntry))])
            self._leafs = OrderedDict()

            self.cospflsdbentry = YList(self)
            self._segment_path = lambda: "cospfLsdbTable"
            self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOOSPFMIB.CospfLsdbTable, [], name, value)


        class CospfLsdbEntry(Entity):
            """
            A single Link State Advertisement.
            
            .. attribute:: ospflsdbareaid  (key)
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ospflsdbareaid <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfLsdbTable.OspfLsdbEntry>`
            
            .. attribute:: cospflsdbtype  (key)
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\:  :py:class:`CospfLsdbType <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfLsdbTable.CospfLsdbEntry.CospfLsdbType>`
            
            .. attribute:: ospflsdblsid  (key)
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ospflsdblsid <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfLsdbTable.OspfLsdbEntry>`
            
            .. attribute:: ospflsdbrouterid  (key)
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ospflsdbrouterid <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.OspfLsdbTable.OspfLsdbEntry>`
            
            .. attribute:: cospflsdbsequence
            
            	The sequence number field is a  signed  32\-bit integer.   It  is used to detect old and duplicate link state advertisements.  The  space  of sequence  numbers  is  linearly  ordered.   The larger the sequence number the more recent  the advertisement
            	**type**\: int
            
            	**range:** 1..147483647
            
            .. attribute:: cospflsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cospflsdbchecksum
            
            	This field is the  checksum  of  the  complete contents  of  the  advertisement, excepting the age field.  The age field is excepted  so  that an   advertisement's  age  can  be  incremented without updating the  checksum.   The  checksum used  is  the same that is used for ISO connectionless datagrams; it is commonly referred  to as the Fletcher checksum
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cospflsdbadvertisement
            
            	The entire Link State Advertisement, including its header
            	**type**\: str
            
            	**length:** 1..65535
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                super(CISCOOSPFMIB.CospfLsdbTable.CospfLsdbEntry, self).__init__()

                self.yang_name = "cospfLsdbEntry"
                self.yang_parent_name = "cospfLsdbTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ospflsdbareaid','cospflsdbtype','ospflsdblsid','ospflsdbrouterid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ospflsdbareaid', (YLeaf(YType.str, 'ospfLsdbAreaId'), ['str'])),
                    ('cospflsdbtype', (YLeaf(YType.enumeration, 'cospfLsdbType'), [('ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CISCOOSPFMIB', 'CospfLsdbTable.CospfLsdbEntry.CospfLsdbType')])),
                    ('ospflsdblsid', (YLeaf(YType.str, 'ospfLsdbLsid'), ['str'])),
                    ('ospflsdbrouterid', (YLeaf(YType.str, 'ospfLsdbRouterId'), ['str'])),
                    ('cospflsdbsequence', (YLeaf(YType.int32, 'cospfLsdbSequence'), ['int'])),
                    ('cospflsdbage', (YLeaf(YType.int32, 'cospfLsdbAge'), ['int'])),
                    ('cospflsdbchecksum', (YLeaf(YType.int32, 'cospfLsdbChecksum'), ['int'])),
                    ('cospflsdbadvertisement', (YLeaf(YType.str, 'cospfLsdbAdvertisement'), ['str'])),
                ])
                self.ospflsdbareaid = None
                self.cospflsdbtype = None
                self.ospflsdblsid = None
                self.ospflsdbrouterid = None
                self.cospflsdbsequence = None
                self.cospflsdbage = None
                self.cospflsdbchecksum = None
                self.cospflsdbadvertisement = None
                self._segment_path = lambda: "cospfLsdbEntry" + "[ospfLsdbAreaId='" + str(self.ospflsdbareaid) + "']" + "[cospfLsdbType='" + str(self.cospflsdbtype) + "']" + "[ospfLsdbLsid='" + str(self.ospflsdblsid) + "']" + "[ospfLsdbRouterId='" + str(self.ospflsdbrouterid) + "']"
                self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/cospfLsdbTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOOSPFMIB.CospfLsdbTable.CospfLsdbEntry, [u'ospflsdbareaid', u'cospflsdbtype', u'ospflsdblsid', u'ospflsdbrouterid', u'cospflsdbsequence', u'cospflsdbage', u'cospflsdbchecksum', u'cospflsdbadvertisement'], name, value)

            class CospfLsdbType(Enum):
                """
                CospfLsdbType (Enum Class)

                The type of the link state advertisement.

                Each link state type has a separate advertisement format.

                .. data:: areaOpaqueLink = 10

                .. data:: asOpaqueLink = 11

                """

                areaOpaqueLink = Enum.YLeaf(10, "areaOpaqueLink")

                asOpaqueLink = Enum.YLeaf(11, "asOpaqueLink")



    class CospfShamLinkTable(Entity):
        """
        Information about this router's sham links
        
        .. attribute:: cospfshamlinkentry
        
        	Information about a single sham link
        	**type**\: list of  		 :py:class:`CospfShamLinkEntry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfShamLinkTable.CospfShamLinkEntry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            super(CISCOOSPFMIB.CospfShamLinkTable, self).__init__()

            self.yang_name = "cospfShamLinkTable"
            self.yang_parent_name = "CISCO-OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cospfShamLinkEntry", ("cospfshamlinkentry", CISCOOSPFMIB.CospfShamLinkTable.CospfShamLinkEntry))])
            self._leafs = OrderedDict()

            self.cospfshamlinkentry = YList(self)
            self._segment_path = lambda: "cospfShamLinkTable"
            self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOOSPFMIB.CospfShamLinkTable, [], name, value)


        class CospfShamLinkEntry(Entity):
            """
            Information about a single sham link
            
            .. attribute:: cospfshamlinkareaid  (key)
            
            	The  Transit  Area  that  the   Virtual   Link traverses.  By definition, this is not 0.0.0.0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinklocalipaddress  (key)
            
            	The Local IP address of the sham link
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkneighborid  (key)
            
            	The Router ID of the other end router of the sham link
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkretransinterval
            
            	The number of seconds between  link\-state  advertisement retransmissions,  for  adjacencies belonging to this  link.   This  value  is also used when retransmitting database description   and  link\-state  request  packets. This value   should  be well over the expected round trip time
            	**type**\: int
            
            	**range:** 0..3600
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkhellointerval
            
            	The length of time, in  seconds,  between  the Hello  packets that the router sends on the sham link
            	**type**\: int
            
            	**range:** 1..65535
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkrtrdeadinterval
            
            	The number of seconds that  a  router's  Hello packets  have  not been seen before it's neighbors declare the router down.  This  should  be some  multiple  of  the  Hello  interval
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkstate
            
            	OSPF sham link states
            	**type**\:  :py:class:`CospfShamLinkState <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfShamLinkTable.CospfShamLinkEntry.CospfShamLinkState>`
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkevents
            
            	The number of state changes or error events on this sham link
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkmetric
            
            	The Metric to be advertised
            	**type**\: int
            
            	**range:** 0..65535
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                super(CISCOOSPFMIB.CospfShamLinkTable.CospfShamLinkEntry, self).__init__()

                self.yang_name = "cospfShamLinkEntry"
                self.yang_parent_name = "cospfShamLinkTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cospfshamlinkareaid','cospfshamlinklocalipaddress','cospfshamlinkneighborid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cospfshamlinkareaid', (YLeaf(YType.str, 'cospfShamLinkAreaId'), ['str'])),
                    ('cospfshamlinklocalipaddress', (YLeaf(YType.str, 'cospfShamLinkLocalIpAddress'), ['str'])),
                    ('cospfshamlinkneighborid', (YLeaf(YType.str, 'cospfShamLinkNeighborId'), ['str'])),
                    ('cospfshamlinkretransinterval', (YLeaf(YType.int32, 'cospfShamLinkRetransInterval'), ['int'])),
                    ('cospfshamlinkhellointerval', (YLeaf(YType.int32, 'cospfShamLinkHelloInterval'), ['int'])),
                    ('cospfshamlinkrtrdeadinterval', (YLeaf(YType.int32, 'cospfShamLinkRtrDeadInterval'), ['int'])),
                    ('cospfshamlinkstate', (YLeaf(YType.enumeration, 'cospfShamLinkState'), [('ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CISCOOSPFMIB', 'CospfShamLinkTable.CospfShamLinkEntry.CospfShamLinkState')])),
                    ('cospfshamlinkevents', (YLeaf(YType.uint32, 'cospfShamLinkEvents'), ['int'])),
                    ('cospfshamlinkmetric', (YLeaf(YType.int32, 'cospfShamLinkMetric'), ['int'])),
                ])
                self.cospfshamlinkareaid = None
                self.cospfshamlinklocalipaddress = None
                self.cospfshamlinkneighborid = None
                self.cospfshamlinkretransinterval = None
                self.cospfshamlinkhellointerval = None
                self.cospfshamlinkrtrdeadinterval = None
                self.cospfshamlinkstate = None
                self.cospfshamlinkevents = None
                self.cospfshamlinkmetric = None
                self._segment_path = lambda: "cospfShamLinkEntry" + "[cospfShamLinkAreaId='" + str(self.cospfshamlinkareaid) + "']" + "[cospfShamLinkLocalIpAddress='" + str(self.cospfshamlinklocalipaddress) + "']" + "[cospfShamLinkNeighborId='" + str(self.cospfshamlinkneighborid) + "']"
                self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/cospfShamLinkTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOOSPFMIB.CospfShamLinkTable.CospfShamLinkEntry, [u'cospfshamlinkareaid', u'cospfshamlinklocalipaddress', u'cospfshamlinkneighborid', u'cospfshamlinkretransinterval', u'cospfshamlinkhellointerval', u'cospfshamlinkrtrdeadinterval', u'cospfshamlinkstate', u'cospfshamlinkevents', u'cospfshamlinkmetric'], name, value)

            class CospfShamLinkState(Enum):
                """
                CospfShamLinkState (Enum Class)

                OSPF sham link states.

                .. data:: down = 1

                .. data:: pointToPoint = 4

                """

                down = Enum.YLeaf(1, "down")

                pointToPoint = Enum.YLeaf(4, "pointToPoint")



    class CospfLocalLsdbTable(Entity):
        """
        The OSPF Process's Link\-Local Link State Database
        for non\-virtual links.
        
        .. attribute:: cospflocallsdbentry
        
        	A single Link State Advertisement
        	**type**\: list of  		 :py:class:`CospfLocalLsdbEntry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfLocalLsdbTable.CospfLocalLsdbEntry>`
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            super(CISCOOSPFMIB.CospfLocalLsdbTable, self).__init__()

            self.yang_name = "cospfLocalLsdbTable"
            self.yang_parent_name = "CISCO-OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cospfLocalLsdbEntry", ("cospflocallsdbentry", CISCOOSPFMIB.CospfLocalLsdbTable.CospfLocalLsdbEntry))])
            self._leafs = OrderedDict()

            self.cospflocallsdbentry = YList(self)
            self._segment_path = lambda: "cospfLocalLsdbTable"
            self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOOSPFMIB.CospfLocalLsdbTable, [], name, value)


        class CospfLocalLsdbEntry(Entity):
            """
            A single Link State Advertisement.
            
            .. attribute:: cospflocallsdbipaddress  (key)
            
            	The IP Address of the interface from which the LSA was received if the interface is numbered
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospflocallsdbaddresslessif  (key)
            
            	The Interface Index of the interface from which the LSA was received if the interface is unnumbered
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cospflocallsdbtype  (key)
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\:  :py:class:`CospfLocalLsdbType <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfLocalLsdbTable.CospfLocalLsdbEntry.CospfLocalLsdbType>`
            
            .. attribute:: cospflocallsdblsid  (key)
            
            	The Link State ID is an LS Type Specific field containing a 32 bit identifier in IP address format; it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospflocallsdbrouterid  (key)
            
            	The 32 bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospflocallsdbsequence
            
            	The sequence number field is a signed 32\-bit integer. It is used to detect old and duplicate link state advertisements. The space of sequence numbers is linearly ordered. The larger the sequence number the more recent the advertisement
            	**type**\: int
            
            	**range:** \-2147483647..2147483647
            
            .. attribute:: cospflocallsdbage
            
            	This field is the age of the link state advertisement  in seconds
            	**type**\: int
            
            	**range:** 0..3600
            
            .. attribute:: cospflocallsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field. The age field is excepted so that an advertisement's age can be incremented without updating the checksum. The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred  to as the Fletcher checksum
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospflocallsdbadvertisement
            
            	The entire Link State Advertisement, including its header
            	**type**\: str
            
            	**length:** 1..65535
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                super(CISCOOSPFMIB.CospfLocalLsdbTable.CospfLocalLsdbEntry, self).__init__()

                self.yang_name = "cospfLocalLsdbEntry"
                self.yang_parent_name = "cospfLocalLsdbTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cospflocallsdbipaddress','cospflocallsdbaddresslessif','cospflocallsdbtype','cospflocallsdblsid','cospflocallsdbrouterid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cospflocallsdbipaddress', (YLeaf(YType.str, 'cospfLocalLsdbIpAddress'), ['str'])),
                    ('cospflocallsdbaddresslessif', (YLeaf(YType.int32, 'cospfLocalLsdbAddressLessIf'), ['int'])),
                    ('cospflocallsdbtype', (YLeaf(YType.enumeration, 'cospfLocalLsdbType'), [('ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CISCOOSPFMIB', 'CospfLocalLsdbTable.CospfLocalLsdbEntry.CospfLocalLsdbType')])),
                    ('cospflocallsdblsid', (YLeaf(YType.str, 'cospfLocalLsdbLsid'), ['str'])),
                    ('cospflocallsdbrouterid', (YLeaf(YType.str, 'cospfLocalLsdbRouterId'), ['str'])),
                    ('cospflocallsdbsequence', (YLeaf(YType.int32, 'cospfLocalLsdbSequence'), ['int'])),
                    ('cospflocallsdbage', (YLeaf(YType.int32, 'cospfLocalLsdbAge'), ['int'])),
                    ('cospflocallsdbchecksum', (YLeaf(YType.uint32, 'cospfLocalLsdbChecksum'), ['int'])),
                    ('cospflocallsdbadvertisement', (YLeaf(YType.str, 'cospfLocalLsdbAdvertisement'), ['str'])),
                ])
                self.cospflocallsdbipaddress = None
                self.cospflocallsdbaddresslessif = None
                self.cospflocallsdbtype = None
                self.cospflocallsdblsid = None
                self.cospflocallsdbrouterid = None
                self.cospflocallsdbsequence = None
                self.cospflocallsdbage = None
                self.cospflocallsdbchecksum = None
                self.cospflocallsdbadvertisement = None
                self._segment_path = lambda: "cospfLocalLsdbEntry" + "[cospfLocalLsdbIpAddress='" + str(self.cospflocallsdbipaddress) + "']" + "[cospfLocalLsdbAddressLessIf='" + str(self.cospflocallsdbaddresslessif) + "']" + "[cospfLocalLsdbType='" + str(self.cospflocallsdbtype) + "']" + "[cospfLocalLsdbLsid='" + str(self.cospflocallsdblsid) + "']" + "[cospfLocalLsdbRouterId='" + str(self.cospflocallsdbrouterid) + "']"
                self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/cospfLocalLsdbTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOOSPFMIB.CospfLocalLsdbTable.CospfLocalLsdbEntry, [u'cospflocallsdbipaddress', u'cospflocallsdbaddresslessif', u'cospflocallsdbtype', u'cospflocallsdblsid', u'cospflocallsdbrouterid', u'cospflocallsdbsequence', u'cospflocallsdbage', u'cospflocallsdbchecksum', u'cospflocallsdbadvertisement'], name, value)

            class CospfLocalLsdbType(Enum):
                """
                CospfLocalLsdbType (Enum Class)

                The type of the link state advertisement.

                Each link state type has a separate advertisement format.

                .. data:: localOpaqueLink = 9

                """

                localOpaqueLink = Enum.YLeaf(9, "localOpaqueLink")



    class CospfVirtLocalLsdbTable(Entity):
        """
        The OSPF Process's Link\-Local Link State Database
        for virtual links.
        
        .. attribute:: cospfvirtlocallsdbentry
        
        	A single Link State Advertisement
        	**type**\: list of  		 :py:class:`CospfVirtLocalLsdbEntry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfVirtLocalLsdbTable.CospfVirtLocalLsdbEntry>`
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            super(CISCOOSPFMIB.CospfVirtLocalLsdbTable, self).__init__()

            self.yang_name = "cospfVirtLocalLsdbTable"
            self.yang_parent_name = "CISCO-OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cospfVirtLocalLsdbEntry", ("cospfvirtlocallsdbentry", CISCOOSPFMIB.CospfVirtLocalLsdbTable.CospfVirtLocalLsdbEntry))])
            self._leafs = OrderedDict()

            self.cospfvirtlocallsdbentry = YList(self)
            self._segment_path = lambda: "cospfVirtLocalLsdbTable"
            self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOOSPFMIB.CospfVirtLocalLsdbTable, [], name, value)


        class CospfVirtLocalLsdbEntry(Entity):
            """
            A single Link State Advertisement.
            
            .. attribute:: cospfvirtlocallsdbtransitarea  (key)
            
            	The Transit Area that the Virtual Link traverses. By definition, this is not 0.0.0.0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfvirtlocallsdbneighbor  (key)
            
            	The Router ID of the Virtual Neighbor
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfvirtlocallsdbtype  (key)
            
            	The type of the link state advertisement. Each  link state type has a separate advertisement format
            	**type**\:  :py:class:`CospfVirtLocalLsdbType <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfVirtLocalLsdbTable.CospfVirtLocalLsdbEntry.CospfVirtLocalLsdbType>`
            
            .. attribute:: cospfvirtlocallsdblsid  (key)
            
            	The Link State ID is an LS Type Specific field containing a 32 bit identifier in IP address format; it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfvirtlocallsdbrouterid  (key)
            
            	The 32 bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfvirtlocallsdbsequence
            
            	The sequence number field is a  signed  32\-bit integer. It is used to detect old and duplicate link state advertisements. The space of sequence numbers is linearly ordered. The larger the sequence number the more recent the advertisement
            	**type**\: int
            
            	**range:** \-2147483647..2147483647
            
            .. attribute:: cospfvirtlocallsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\: int
            
            	**range:** 0..3600
            
            .. attribute:: cospfvirtlocallsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field. The age field is excepted so that an advertisement's age can be incremented without updating the checksum. The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred  to as the Fletcher checksum
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfvirtlocallsdbadvertisement
            
            	The entire Link State Advertisement, including its header
            	**type**\: str
            
            	**length:** 1..65535
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                super(CISCOOSPFMIB.CospfVirtLocalLsdbTable.CospfVirtLocalLsdbEntry, self).__init__()

                self.yang_name = "cospfVirtLocalLsdbEntry"
                self.yang_parent_name = "cospfVirtLocalLsdbTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cospfvirtlocallsdbtransitarea','cospfvirtlocallsdbneighbor','cospfvirtlocallsdbtype','cospfvirtlocallsdblsid','cospfvirtlocallsdbrouterid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cospfvirtlocallsdbtransitarea', (YLeaf(YType.str, 'cospfVirtLocalLsdbTransitArea'), ['str'])),
                    ('cospfvirtlocallsdbneighbor', (YLeaf(YType.str, 'cospfVirtLocalLsdbNeighbor'), ['str'])),
                    ('cospfvirtlocallsdbtype', (YLeaf(YType.enumeration, 'cospfVirtLocalLsdbType'), [('ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CISCOOSPFMIB', 'CospfVirtLocalLsdbTable.CospfVirtLocalLsdbEntry.CospfVirtLocalLsdbType')])),
                    ('cospfvirtlocallsdblsid', (YLeaf(YType.str, 'cospfVirtLocalLsdbLsid'), ['str'])),
                    ('cospfvirtlocallsdbrouterid', (YLeaf(YType.str, 'cospfVirtLocalLsdbRouterId'), ['str'])),
                    ('cospfvirtlocallsdbsequence', (YLeaf(YType.int32, 'cospfVirtLocalLsdbSequence'), ['int'])),
                    ('cospfvirtlocallsdbage', (YLeaf(YType.int32, 'cospfVirtLocalLsdbAge'), ['int'])),
                    ('cospfvirtlocallsdbchecksum', (YLeaf(YType.uint32, 'cospfVirtLocalLsdbChecksum'), ['int'])),
                    ('cospfvirtlocallsdbadvertisement', (YLeaf(YType.str, 'cospfVirtLocalLsdbAdvertisement'), ['str'])),
                ])
                self.cospfvirtlocallsdbtransitarea = None
                self.cospfvirtlocallsdbneighbor = None
                self.cospfvirtlocallsdbtype = None
                self.cospfvirtlocallsdblsid = None
                self.cospfvirtlocallsdbrouterid = None
                self.cospfvirtlocallsdbsequence = None
                self.cospfvirtlocallsdbage = None
                self.cospfvirtlocallsdbchecksum = None
                self.cospfvirtlocallsdbadvertisement = None
                self._segment_path = lambda: "cospfVirtLocalLsdbEntry" + "[cospfVirtLocalLsdbTransitArea='" + str(self.cospfvirtlocallsdbtransitarea) + "']" + "[cospfVirtLocalLsdbNeighbor='" + str(self.cospfvirtlocallsdbneighbor) + "']" + "[cospfVirtLocalLsdbType='" + str(self.cospfvirtlocallsdbtype) + "']" + "[cospfVirtLocalLsdbLsid='" + str(self.cospfvirtlocallsdblsid) + "']" + "[cospfVirtLocalLsdbRouterId='" + str(self.cospfvirtlocallsdbrouterid) + "']"
                self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/cospfVirtLocalLsdbTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOOSPFMIB.CospfVirtLocalLsdbTable.CospfVirtLocalLsdbEntry, [u'cospfvirtlocallsdbtransitarea', u'cospfvirtlocallsdbneighbor', u'cospfvirtlocallsdbtype', u'cospfvirtlocallsdblsid', u'cospfvirtlocallsdbrouterid', u'cospfvirtlocallsdbsequence', u'cospfvirtlocallsdbage', u'cospfvirtlocallsdbchecksum', u'cospfvirtlocallsdbadvertisement'], name, value)

            class CospfVirtLocalLsdbType(Enum):
                """
                CospfVirtLocalLsdbType (Enum Class)

                The type of the link state advertisement.

                Each  link state type has a separate advertisement format.

                .. data:: localOpaqueLink = 9

                """

                localOpaqueLink = Enum.YLeaf(9, "localOpaqueLink")



    class CospfShamLinkNbrTable(Entity):
        """
        A table of sham link neighbor information.
        
        .. attribute:: cospfshamlinknbrentry
        
        	Sham link neighbor information
        	**type**\: list of  		 :py:class:`CospfShamLinkNbrEntry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfShamLinkNbrTable.CospfShamLinkNbrEntry>`
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            super(CISCOOSPFMIB.CospfShamLinkNbrTable, self).__init__()

            self.yang_name = "cospfShamLinkNbrTable"
            self.yang_parent_name = "CISCO-OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cospfShamLinkNbrEntry", ("cospfshamlinknbrentry", CISCOOSPFMIB.CospfShamLinkNbrTable.CospfShamLinkNbrEntry))])
            self._leafs = OrderedDict()

            self.cospfshamlinknbrentry = YList(self)
            self._segment_path = lambda: "cospfShamLinkNbrTable"
            self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOOSPFMIB.CospfShamLinkNbrTable, [], name, value)


        class CospfShamLinkNbrEntry(Entity):
            """
            Sham link neighbor information.
            
            .. attribute:: cospfshamlinkslocalipaddrtype  (key)
            
            	
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cospfshamlinkslocalipaddr  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`cospfshamlinkslocalipaddr <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfShamLinksTable.CospfShamLinksEntry>`
            
            .. attribute:: cospfshamlinknbrarea  (key)
            
            	The area to which the sham link is part of
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfshamlinknbripaddrtype  (key)
            
            	The type of internet address of this sham link neighbor's IP address
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cospfshamlinknbripaddr  (key)
            
            	The IP address this sham link neighbor is using
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cospfshamlinknbrrtrid
            
            	A 32\-bit integer uniquely identifying the neighboring router
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfshamlinknbroptions
            
            	A Bit Mask corresponding to the neighbor's options field.  Bit 1, if set, indicates that the  system  will operate  on  Type of Service metrics other than TOS 0.  If zero, the neighbor will  ignore  all metrics except the TOS 0 metric.  Bit 2, if set, indicates  that  the  system  is Network  Multicast  capable; ie, that it implements  OSPF Multicast Routing
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cospfshamlinknbrstate
            
            	The state of this sham link neighbor relation\- ship
            	**type**\:  :py:class:`CospfShamLinkNbrState <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfShamLinkNbrTable.CospfShamLinkNbrEntry.CospfShamLinkNbrState>`
            
            .. attribute:: cospfshamlinknbrevents
            
            	The number of  times  this sham link has changed state or an error has occurred
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfshamlinknbrlsretransqlen
            
            	The  current  length  of  the   retransmission queue. The retransmission queue is maintained for LSAs that have been flooded but not acknowledged on this adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfshamlinknbrhellosuppressed
            
            	Indicates whether Hellos are being  suppressed to the neighbor
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                super(CISCOOSPFMIB.CospfShamLinkNbrTable.CospfShamLinkNbrEntry, self).__init__()

                self.yang_name = "cospfShamLinkNbrEntry"
                self.yang_parent_name = "cospfShamLinkNbrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cospfshamlinkslocalipaddrtype','cospfshamlinkslocalipaddr','cospfshamlinknbrarea','cospfshamlinknbripaddrtype','cospfshamlinknbripaddr']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cospfshamlinkslocalipaddrtype', (YLeaf(YType.enumeration, 'cospfShamLinksLocalIpAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cospfshamlinkslocalipaddr', (YLeaf(YType.str, 'cospfShamLinksLocalIpAddr'), ['str'])),
                    ('cospfshamlinknbrarea', (YLeaf(YType.str, 'cospfShamLinkNbrArea'), ['str'])),
                    ('cospfshamlinknbripaddrtype', (YLeaf(YType.enumeration, 'cospfShamLinkNbrIpAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cospfshamlinknbripaddr', (YLeaf(YType.str, 'cospfShamLinkNbrIpAddr'), ['str'])),
                    ('cospfshamlinknbrrtrid', (YLeaf(YType.str, 'cospfShamLinkNbrRtrId'), ['str'])),
                    ('cospfshamlinknbroptions', (YLeaf(YType.int32, 'cospfShamLinkNbrOptions'), ['int'])),
                    ('cospfshamlinknbrstate', (YLeaf(YType.enumeration, 'cospfShamLinkNbrState'), [('ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CISCOOSPFMIB', 'CospfShamLinkNbrTable.CospfShamLinkNbrEntry.CospfShamLinkNbrState')])),
                    ('cospfshamlinknbrevents', (YLeaf(YType.uint32, 'cospfShamLinkNbrEvents'), ['int'])),
                    ('cospfshamlinknbrlsretransqlen', (YLeaf(YType.uint32, 'cospfShamLinkNbrLsRetransQLen'), ['int'])),
                    ('cospfshamlinknbrhellosuppressed', (YLeaf(YType.boolean, 'cospfShamLinkNbrHelloSuppressed'), ['bool'])),
                ])
                self.cospfshamlinkslocalipaddrtype = None
                self.cospfshamlinkslocalipaddr = None
                self.cospfshamlinknbrarea = None
                self.cospfshamlinknbripaddrtype = None
                self.cospfshamlinknbripaddr = None
                self.cospfshamlinknbrrtrid = None
                self.cospfshamlinknbroptions = None
                self.cospfshamlinknbrstate = None
                self.cospfshamlinknbrevents = None
                self.cospfshamlinknbrlsretransqlen = None
                self.cospfshamlinknbrhellosuppressed = None
                self._segment_path = lambda: "cospfShamLinkNbrEntry" + "[cospfShamLinksLocalIpAddrType='" + str(self.cospfshamlinkslocalipaddrtype) + "']" + "[cospfShamLinksLocalIpAddr='" + str(self.cospfshamlinkslocalipaddr) + "']" + "[cospfShamLinkNbrArea='" + str(self.cospfshamlinknbrarea) + "']" + "[cospfShamLinkNbrIpAddrType='" + str(self.cospfshamlinknbripaddrtype) + "']" + "[cospfShamLinkNbrIpAddr='" + str(self.cospfshamlinknbripaddr) + "']"
                self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/cospfShamLinkNbrTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOOSPFMIB.CospfShamLinkNbrTable.CospfShamLinkNbrEntry, [u'cospfshamlinkslocalipaddrtype', u'cospfshamlinkslocalipaddr', u'cospfshamlinknbrarea', u'cospfshamlinknbripaddrtype', u'cospfshamlinknbripaddr', u'cospfshamlinknbrrtrid', u'cospfshamlinknbroptions', u'cospfshamlinknbrstate', u'cospfshamlinknbrevents', u'cospfshamlinknbrlsretransqlen', u'cospfshamlinknbrhellosuppressed'], name, value)

            class CospfShamLinkNbrState(Enum):
                """
                CospfShamLinkNbrState (Enum Class)

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

                down = Enum.YLeaf(1, "down")

                attempt = Enum.YLeaf(2, "attempt")

                init = Enum.YLeaf(3, "init")

                twoWay = Enum.YLeaf(4, "twoWay")

                exchangeStart = Enum.YLeaf(5, "exchangeStart")

                exchange = Enum.YLeaf(6, "exchange")

                loading = Enum.YLeaf(7, "loading")

                full = Enum.YLeaf(8, "full")



    class CospfShamLinksTable(Entity):
        """
        Information about this router's sham links.
        
        .. attribute:: cospfshamlinksentry
        
        	Information about a single sham link
        	**type**\: list of  		 :py:class:`CospfShamLinksEntry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfShamLinksTable.CospfShamLinksEntry>`
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            super(CISCOOSPFMIB.CospfShamLinksTable, self).__init__()

            self.yang_name = "cospfShamLinksTable"
            self.yang_parent_name = "CISCO-OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cospfShamLinksEntry", ("cospfshamlinksentry", CISCOOSPFMIB.CospfShamLinksTable.CospfShamLinksEntry))])
            self._leafs = OrderedDict()

            self.cospfshamlinksentry = YList(self)
            self._segment_path = lambda: "cospfShamLinksTable"
            self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOOSPFMIB.CospfShamLinksTable, [], name, value)


        class CospfShamLinksEntry(Entity):
            """
            Information about a single sham link.
            
            .. attribute:: cospfshamlinksareaid  (key)
            
            	The area that this sham link is part of
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfshamlinkslocalipaddrtype  (key)
            
            	The type of internet address of this sham link's local IP address
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cospfshamlinkslocalipaddr  (key)
            
            	The Local IP address of the sham link
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cospfshamlinksremoteipaddrtype  (key)
            
            	The type of internet address of this sham link's remote IP address
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cospfshamlinksremoteipaddr  (key)
            
            	The IP address of the other end router of the sham link
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cospfshamlinksretransinterval
            
            	The number of seconds between  link\-state  advertisement retransmissions, for adjacencies belonging to this link. This value is also used when retransmitting database  description and link\-state request packets. This value should be well over the expected round trip time
            	**type**\: int
            
            	**range:** 0..3600
            
            .. attribute:: cospfshamlinkshellointerval
            
            	The length of time, in  seconds,  between  the Hello  packets that the router sends on the sham link
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: cospfshamlinksrtrdeadinterval
            
            	The number of seconds that  a  router's  Hello packets  have  not been seen before it's neighbors declare the router down.  This  should  be some  multiple  of  the  Hello  interval
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cospfshamlinksstate
            
            	OSPF sham link states
            	**type**\:  :py:class:`CospfShamLinksState <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.CospfShamLinksTable.CospfShamLinksEntry.CospfShamLinksState>`
            
            .. attribute:: cospfshamlinksevents
            
            	The number of state changes or error events on this sham link
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfshamlinksmetric
            
            	The Metric to be advertised
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                super(CISCOOSPFMIB.CospfShamLinksTable.CospfShamLinksEntry, self).__init__()

                self.yang_name = "cospfShamLinksEntry"
                self.yang_parent_name = "cospfShamLinksTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cospfshamlinksareaid','cospfshamlinkslocalipaddrtype','cospfshamlinkslocalipaddr','cospfshamlinksremoteipaddrtype','cospfshamlinksremoteipaddr']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cospfshamlinksareaid', (YLeaf(YType.str, 'cospfShamLinksAreaId'), ['str'])),
                    ('cospfshamlinkslocalipaddrtype', (YLeaf(YType.enumeration, 'cospfShamLinksLocalIpAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cospfshamlinkslocalipaddr', (YLeaf(YType.str, 'cospfShamLinksLocalIpAddr'), ['str'])),
                    ('cospfshamlinksremoteipaddrtype', (YLeaf(YType.enumeration, 'cospfShamLinksRemoteIpAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cospfshamlinksremoteipaddr', (YLeaf(YType.str, 'cospfShamLinksRemoteIpAddr'), ['str'])),
                    ('cospfshamlinksretransinterval', (YLeaf(YType.int32, 'cospfShamLinksRetransInterval'), ['int'])),
                    ('cospfshamlinkshellointerval', (YLeaf(YType.int32, 'cospfShamLinksHelloInterval'), ['int'])),
                    ('cospfshamlinksrtrdeadinterval', (YLeaf(YType.int32, 'cospfShamLinksRtrDeadInterval'), ['int'])),
                    ('cospfshamlinksstate', (YLeaf(YType.enumeration, 'cospfShamLinksState'), [('ydk.models.cisco_ios_xe.CISCO_OSPF_MIB', 'CISCOOSPFMIB', 'CospfShamLinksTable.CospfShamLinksEntry.CospfShamLinksState')])),
                    ('cospfshamlinksevents', (YLeaf(YType.uint32, 'cospfShamLinksEvents'), ['int'])),
                    ('cospfshamlinksmetric', (YLeaf(YType.int32, 'cospfShamLinksMetric'), ['int'])),
                ])
                self.cospfshamlinksareaid = None
                self.cospfshamlinkslocalipaddrtype = None
                self.cospfshamlinkslocalipaddr = None
                self.cospfshamlinksremoteipaddrtype = None
                self.cospfshamlinksremoteipaddr = None
                self.cospfshamlinksretransinterval = None
                self.cospfshamlinkshellointerval = None
                self.cospfshamlinksrtrdeadinterval = None
                self.cospfshamlinksstate = None
                self.cospfshamlinksevents = None
                self.cospfshamlinksmetric = None
                self._segment_path = lambda: "cospfShamLinksEntry" + "[cospfShamLinksAreaId='" + str(self.cospfshamlinksareaid) + "']" + "[cospfShamLinksLocalIpAddrType='" + str(self.cospfshamlinkslocalipaddrtype) + "']" + "[cospfShamLinksLocalIpAddr='" + str(self.cospfshamlinkslocalipaddr) + "']" + "[cospfShamLinksRemoteIpAddrType='" + str(self.cospfshamlinksremoteipaddrtype) + "']" + "[cospfShamLinksRemoteIpAddr='" + str(self.cospfshamlinksremoteipaddr) + "']"
                self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/cospfShamLinksTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOOSPFMIB.CospfShamLinksTable.CospfShamLinksEntry, [u'cospfshamlinksareaid', u'cospfshamlinkslocalipaddrtype', u'cospfshamlinkslocalipaddr', u'cospfshamlinksremoteipaddrtype', u'cospfshamlinksremoteipaddr', u'cospfshamlinksretransinterval', u'cospfshamlinkshellointerval', u'cospfshamlinksrtrdeadinterval', u'cospfshamlinksstate', u'cospfshamlinksevents', u'cospfshamlinksmetric'], name, value)

            class CospfShamLinksState(Enum):
                """
                CospfShamLinksState (Enum Class)

                OSPF sham link states.

                .. data:: down = 1

                .. data:: pointToPoint = 4

                """

                down = Enum.YLeaf(1, "down")

                pointToPoint = Enum.YLeaf(4, "pointToPoint")


    def clone_ptr(self):
        self._top_entity = CISCOOSPFMIB()
        return self._top_entity


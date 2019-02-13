""" DOCS_L2VPN_MIB 

This is the management MIB for devices complying to the  
DOCSIS L2VPN Feature.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class DocsNsiEncapSubtype(Enum):
    """
    DocsNsiEncapSubtype (Enum Class)

    An enumerated integer that defines the default  

    encapsulation on NSI ports of an L2VPN\-forwarded packet. 

    A CMTS implementation MUST support ieee802.1q(2). 

    A CMTS MAY omit support for all NSI  encapsulations  

    other than ieee802.1q(2).

    .. data:: other = 1

    .. data:: ieee8021q = 2

    .. data:: ieee8021ad = 3

    .. data:: mpls = 4

    .. data:: l2tpv3 = 5

    """

    other = Enum.YLeaf(1, "other")

    ieee8021q = Enum.YLeaf(2, "ieee8021q")

    ieee8021ad = Enum.YLeaf(3, "ieee8021ad")

    mpls = Enum.YLeaf(4, "mpls")

    l2tpv3 = Enum.YLeaf(5, "l2tpv3")



class DOCSL2VPNMIB(Entity):
    """
    
    
    .. attribute:: docsl2vpnidtoindextable
    
    	Table indexed by the octet string DocsL2vpnIdentifier that  provides the local agent's internally assigned docsL2vpnIdx  value for that DocsL2vpnIdentifier value. The mapping of   DocsL2vpnIdentifier to docsL2vpnIdx is 1\-1. The agent   must instantiate a row in both docsL2vpnIndexToIdTable and  docsL2vpnIdToIndexTable for each known L2VPN Identifier
    	**type**\:  :py:class:`DocsL2vpnIdToIndexTable <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnIdToIndexTable>`
    
    	**config**\: False
    
    .. attribute:: docsl2vpnindextoidtable
    
    	Table indexed by agent's local docsL2vpnIdx that provides  the global L2VPN Identifier. The mapping of docsL2vpnIdx to  DocsL2vpnIdentifier is 1\-1. The agent must instantiate a   row in both docsL2vpnIndexToIdTable and   docsL2vpnIdToIndexTable for each known L2VPN
    	**type**\:  :py:class:`DocsL2vpnIndexToIdTable <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnIndexToIdTable>`
    
    	**config**\: False
    
    .. attribute:: docsl2vpncmtable
    
    	This table describes L2VPN per\-CM information that  is in common with all L2VPNs for the CM, regardless  of forwarding mode
    	**type**\:  :py:class:`DocsL2vpnCmTable <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnCmTable>`
    
    	**config**\: False
    
    .. attribute:: docsl2vpnvpncmtable
    
    	This table describes the operation of L2VPN forwarding  on each CM
    	**type**\:  :py:class:`DocsL2vpnVpnCmTable <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnVpnCmTable>`
    
    	**config**\: False
    
    .. attribute:: docsl2vpnvpncmstatstable
    
    	This table contains statistics for forwarding of   packets to and from a CM on each VPN
    	**type**\:  :py:class:`DocsL2vpnVpnCmStatsTable <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnVpnCmStatsTable>`
    
    	**config**\: False
    
    .. attribute:: docsl2vpnportstatustable
    
    	This table displays summary information for the  run\-time state of each VPN that is currently operating   on each bridge port
    	**type**\:  :py:class:`DocsL2vpnPortStatusTable <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnPortStatusTable>`
    
    	**config**\: False
    
    .. attribute:: docsl2vpnsfstatustable
    
    	This table displays SF\-specific L2VPN forwarding status   for each upstream service flow configured with a per\-SF    L2VPN Encoding.    Objects which were signaled in a per\-SF L2VPN Encoding but   apply for the entire CM are shown in the    docsL2vpnVpnCmTable
    	**type**\:  :py:class:`DocsL2vpnSfStatusTable <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnSfStatusTable>`
    
    	**config**\: False
    
    .. attribute:: docsl2vpnpktclasstable
    
    	This table provides the L2VPN\-specific objects for  packet classifiers that apply to only L2VPN traffic.   The indices of this table are a subset of the  indices of classifiers in docsQosPktClassTable
    	**type**\:  :py:class:`DocsL2vpnPktClassTable <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnPktClassTable>`
    
    	**config**\: False
    
    .. attribute:: docsl2vpncmnsitable
    
    	This table describes the NSI configuration for a single  CM when operating in point\-to\-point forwarding mode for an  L2VPN
    	**type**\:  :py:class:`DocsL2vpnCmNsiTable <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnCmNsiTable>`
    
    	**config**\: False
    
    .. attribute:: docsl2vpncmvpncpetable
    
    	This table is a list of CPEs, indexed by the VPNs on a   Cable Modem
    	**type**\:  :py:class:`DocsL2vpnCmVpnCpeTable <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnCmVpnCpeTable>`
    
    	**config**\: False
    
    .. attribute:: docsl2vpnvpncmcpetable
    
    	This table contains a list of bridging CPEs, indexed by  L2VPN Index and the corresponding CMs on that VPN
    	**type**\:  :py:class:`DocsL2vpnVpnCmCpeTable <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnVpnCmCpeTable>`
    
    	**config**\: False
    
    .. attribute:: docsl2vpndot1qtpfdbexttable
    
    	This table contains packet counters for   Unicast MAC Addresses within a VPN
    	**type**\:  :py:class:`DocsL2vpnDot1qTpFdbExtTable <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnDot1qTpFdbExtTable>`
    
    	**config**\: False
    
    .. attribute:: docsl2vpndot1qtpgroupexttable
    
    	This table contains packet counters for   Multicast MAC Addresses within a VPN
    	**type**\:  :py:class:`DocsL2vpnDot1qTpGroupExtTable <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnDot1qTpGroupExtTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'DOCS-L2VPN-MIB'
    _revision = '2006-03-28'

    def __init__(self):
        super(DOCSL2VPNMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "DOCS-L2VPN-MIB"
        self.yang_parent_name = "DOCS-L2VPN-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("docsL2vpnIdToIndexTable", ("docsl2vpnidtoindextable", DOCSL2VPNMIB.DocsL2vpnIdToIndexTable)), ("docsL2vpnIndexToIdTable", ("docsl2vpnindextoidtable", DOCSL2VPNMIB.DocsL2vpnIndexToIdTable)), ("docsL2vpnCmTable", ("docsl2vpncmtable", DOCSL2VPNMIB.DocsL2vpnCmTable)), ("docsL2vpnVpnCmTable", ("docsl2vpnvpncmtable", DOCSL2VPNMIB.DocsL2vpnVpnCmTable)), ("docsL2vpnVpnCmStatsTable", ("docsl2vpnvpncmstatstable", DOCSL2VPNMIB.DocsL2vpnVpnCmStatsTable)), ("docsL2vpnPortStatusTable", ("docsl2vpnportstatustable", DOCSL2VPNMIB.DocsL2vpnPortStatusTable)), ("docsL2vpnSfStatusTable", ("docsl2vpnsfstatustable", DOCSL2VPNMIB.DocsL2vpnSfStatusTable)), ("docsL2vpnPktClassTable", ("docsl2vpnpktclasstable", DOCSL2VPNMIB.DocsL2vpnPktClassTable)), ("docsL2vpnCmNsiTable", ("docsl2vpncmnsitable", DOCSL2VPNMIB.DocsL2vpnCmNsiTable)), ("docsL2vpnCmVpnCpeTable", ("docsl2vpncmvpncpetable", DOCSL2VPNMIB.DocsL2vpnCmVpnCpeTable)), ("docsL2vpnVpnCmCpeTable", ("docsl2vpnvpncmcpetable", DOCSL2VPNMIB.DocsL2vpnVpnCmCpeTable)), ("docsL2vpnDot1qTpFdbExtTable", ("docsl2vpndot1qtpfdbexttable", DOCSL2VPNMIB.DocsL2vpnDot1qTpFdbExtTable)), ("docsL2vpnDot1qTpGroupExtTable", ("docsl2vpndot1qtpgroupexttable", DOCSL2VPNMIB.DocsL2vpnDot1qTpGroupExtTable))])
        self._leafs = OrderedDict()

        self.docsl2vpnidtoindextable = DOCSL2VPNMIB.DocsL2vpnIdToIndexTable()
        self.docsl2vpnidtoindextable.parent = self
        self._children_name_map["docsl2vpnidtoindextable"] = "docsL2vpnIdToIndexTable"

        self.docsl2vpnindextoidtable = DOCSL2VPNMIB.DocsL2vpnIndexToIdTable()
        self.docsl2vpnindextoidtable.parent = self
        self._children_name_map["docsl2vpnindextoidtable"] = "docsL2vpnIndexToIdTable"

        self.docsl2vpncmtable = DOCSL2VPNMIB.DocsL2vpnCmTable()
        self.docsl2vpncmtable.parent = self
        self._children_name_map["docsl2vpncmtable"] = "docsL2vpnCmTable"

        self.docsl2vpnvpncmtable = DOCSL2VPNMIB.DocsL2vpnVpnCmTable()
        self.docsl2vpnvpncmtable.parent = self
        self._children_name_map["docsl2vpnvpncmtable"] = "docsL2vpnVpnCmTable"

        self.docsl2vpnvpncmstatstable = DOCSL2VPNMIB.DocsL2vpnVpnCmStatsTable()
        self.docsl2vpnvpncmstatstable.parent = self
        self._children_name_map["docsl2vpnvpncmstatstable"] = "docsL2vpnVpnCmStatsTable"

        self.docsl2vpnportstatustable = DOCSL2VPNMIB.DocsL2vpnPortStatusTable()
        self.docsl2vpnportstatustable.parent = self
        self._children_name_map["docsl2vpnportstatustable"] = "docsL2vpnPortStatusTable"

        self.docsl2vpnsfstatustable = DOCSL2VPNMIB.DocsL2vpnSfStatusTable()
        self.docsl2vpnsfstatustable.parent = self
        self._children_name_map["docsl2vpnsfstatustable"] = "docsL2vpnSfStatusTable"

        self.docsl2vpnpktclasstable = DOCSL2VPNMIB.DocsL2vpnPktClassTable()
        self.docsl2vpnpktclasstable.parent = self
        self._children_name_map["docsl2vpnpktclasstable"] = "docsL2vpnPktClassTable"

        self.docsl2vpncmnsitable = DOCSL2VPNMIB.DocsL2vpnCmNsiTable()
        self.docsl2vpncmnsitable.parent = self
        self._children_name_map["docsl2vpncmnsitable"] = "docsL2vpnCmNsiTable"

        self.docsl2vpncmvpncpetable = DOCSL2VPNMIB.DocsL2vpnCmVpnCpeTable()
        self.docsl2vpncmvpncpetable.parent = self
        self._children_name_map["docsl2vpncmvpncpetable"] = "docsL2vpnCmVpnCpeTable"

        self.docsl2vpnvpncmcpetable = DOCSL2VPNMIB.DocsL2vpnVpnCmCpeTable()
        self.docsl2vpnvpncmcpetable.parent = self
        self._children_name_map["docsl2vpnvpncmcpetable"] = "docsL2vpnVpnCmCpeTable"

        self.docsl2vpndot1qtpfdbexttable = DOCSL2VPNMIB.DocsL2vpnDot1qTpFdbExtTable()
        self.docsl2vpndot1qtpfdbexttable.parent = self
        self._children_name_map["docsl2vpndot1qtpfdbexttable"] = "docsL2vpnDot1qTpFdbExtTable"

        self.docsl2vpndot1qtpgroupexttable = DOCSL2VPNMIB.DocsL2vpnDot1qTpGroupExtTable()
        self.docsl2vpndot1qtpgroupexttable.parent = self
        self._children_name_map["docsl2vpndot1qtpgroupexttable"] = "docsL2vpnDot1qTpGroupExtTable"
        self._segment_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(DOCSL2VPNMIB, [], name, value)


    class DocsL2vpnIdToIndexTable(Entity):
        """
        Table indexed by the octet string DocsL2vpnIdentifier that 
        provides the local agent's internally assigned docsL2vpnIdx 
        value for that DocsL2vpnIdentifier value. The mapping of  
        DocsL2vpnIdentifier to docsL2vpnIdx is 1\-1. The agent  
        must instantiate a row in both docsL2vpnIndexToIdTable and 
        docsL2vpnIdToIndexTable for each known L2VPN Identifier.
        
        .. attribute:: docsl2vpnidtoindexentry
        
        	Maps a DocsL2vpnIdentifier octet string into the local   agent's locally assigned docsL2vpnIdx value
        	**type**\: list of  		 :py:class:`DocsL2vpnIdToIndexEntry <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnIdToIndexTable.DocsL2vpnIdToIndexEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DOCS-L2VPN-MIB'
        _revision = '2006-03-28'

        def __init__(self):
            super(DOCSL2VPNMIB.DocsL2vpnIdToIndexTable, self).__init__()

            self.yang_name = "docsL2vpnIdToIndexTable"
            self.yang_parent_name = "DOCS-L2VPN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsL2vpnIdToIndexEntry", ("docsl2vpnidtoindexentry", DOCSL2VPNMIB.DocsL2vpnIdToIndexTable.DocsL2vpnIdToIndexEntry))])
            self._leafs = OrderedDict()

            self.docsl2vpnidtoindexentry = YList(self)
            self._segment_path = lambda: "docsL2vpnIdToIndexTable"
            self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnIdToIndexTable, [], name, value)


        class DocsL2vpnIdToIndexEntry(Entity):
            """
            Maps a DocsL2vpnIdentifier octet string into the local  
            agent's locally assigned docsL2vpnIdx value.
            
            .. attribute:: docsl2vpnid  (key)
            
            	An externally configured octet string that identifies an  L2VPN
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: docsl2vpnidtoindexidx
            
            	An internally assigned index value for a known L2VPN
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'DOCS-L2VPN-MIB'
            _revision = '2006-03-28'

            def __init__(self):
                super(DOCSL2VPNMIB.DocsL2vpnIdToIndexTable.DocsL2vpnIdToIndexEntry, self).__init__()

                self.yang_name = "docsL2vpnIdToIndexEntry"
                self.yang_parent_name = "docsL2vpnIdToIndexTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsl2vpnid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsl2vpnid', (YLeaf(YType.str, 'docsL2vpnId'), ['str'])),
                    ('docsl2vpnidtoindexidx', (YLeaf(YType.uint32, 'docsL2vpnIdToIndexIdx'), ['int'])),
                ])
                self.docsl2vpnid = None
                self.docsl2vpnidtoindexidx = None
                self._segment_path = lambda: "docsL2vpnIdToIndexEntry" + "[docsL2vpnId='" + str(self.docsl2vpnid) + "']"
                self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/docsL2vpnIdToIndexTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnIdToIndexTable.DocsL2vpnIdToIndexEntry, [u'docsl2vpnid', u'docsl2vpnidtoindexidx'], name, value)




    class DocsL2vpnIndexToIdTable(Entity):
        """
        Table indexed by agent's local docsL2vpnIdx that provides 
        the global L2VPN Identifier. The mapping of docsL2vpnIdx to 
        DocsL2vpnIdentifier is 1\-1. The agent must instantiate a  
        row in both docsL2vpnIndexToIdTable and  
        docsL2vpnIdToIndexTable for each known L2VPN.
        
        .. attribute:: docsl2vpnindextoidentry
        
        	Provides the L2VPN Identifier for each locally\-assigned   L2vpn Index
        	**type**\: list of  		 :py:class:`DocsL2vpnIndexToIdEntry <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnIndexToIdTable.DocsL2vpnIndexToIdEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DOCS-L2VPN-MIB'
        _revision = '2006-03-28'

        def __init__(self):
            super(DOCSL2VPNMIB.DocsL2vpnIndexToIdTable, self).__init__()

            self.yang_name = "docsL2vpnIndexToIdTable"
            self.yang_parent_name = "DOCS-L2VPN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsL2vpnIndexToIdEntry", ("docsl2vpnindextoidentry", DOCSL2VPNMIB.DocsL2vpnIndexToIdTable.DocsL2vpnIndexToIdEntry))])
            self._leafs = OrderedDict()

            self.docsl2vpnindextoidentry = YList(self)
            self._segment_path = lambda: "docsL2vpnIndexToIdTable"
            self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnIndexToIdTable, [], name, value)


        class DocsL2vpnIndexToIdEntry(Entity):
            """
            Provides the L2VPN Identifier for each locally\-assigned  
            L2vpn Index.
            
            .. attribute:: docsl2vpnidx  (key)
            
            	An internally assigned index value for a known L2VPN
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: docsl2vpnindextoidid
            
            	An administered octet string that externally identifies an  L2VPN
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'DOCS-L2VPN-MIB'
            _revision = '2006-03-28'

            def __init__(self):
                super(DOCSL2VPNMIB.DocsL2vpnIndexToIdTable.DocsL2vpnIndexToIdEntry, self).__init__()

                self.yang_name = "docsL2vpnIndexToIdEntry"
                self.yang_parent_name = "docsL2vpnIndexToIdTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsl2vpnidx']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsl2vpnidx', (YLeaf(YType.uint32, 'docsL2vpnIdx'), ['int'])),
                    ('docsl2vpnindextoidid', (YLeaf(YType.str, 'docsL2vpnIndexToIdId'), ['str'])),
                ])
                self.docsl2vpnidx = None
                self.docsl2vpnindextoidid = None
                self._segment_path = lambda: "docsL2vpnIndexToIdEntry" + "[docsL2vpnIdx='" + str(self.docsl2vpnidx) + "']"
                self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/docsL2vpnIndexToIdTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnIndexToIdTable.DocsL2vpnIndexToIdEntry, [u'docsl2vpnidx', u'docsl2vpnindextoidid'], name, value)




    class DocsL2vpnCmTable(Entity):
        """
        This table describes L2VPN per\-CM information that 
        is in common with all L2VPNs for the CM, regardless 
        of forwarding mode.
        
        .. attribute:: docsl2vpncmentry
        
        	An entry is indexed by Cable Modem Index that  describes L2VPN information for a single CM that is in  common with all L2VPNs implemented by the CM,  regardless of the L2VPN forwarding mode.   An entry in this table is created for every CM that   registers with a forwarding L2VPN encoding
        	**type**\: list of  		 :py:class:`DocsL2vpnCmEntry <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnCmTable.DocsL2vpnCmEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DOCS-L2VPN-MIB'
        _revision = '2006-03-28'

        def __init__(self):
            super(DOCSL2VPNMIB.DocsL2vpnCmTable, self).__init__()

            self.yang_name = "docsL2vpnCmTable"
            self.yang_parent_name = "DOCS-L2VPN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsL2vpnCmEntry", ("docsl2vpncmentry", DOCSL2VPNMIB.DocsL2vpnCmTable.DocsL2vpnCmEntry))])
            self._leafs = OrderedDict()

            self.docsl2vpncmentry = YList(self)
            self._segment_path = lambda: "docsL2vpnCmTable"
            self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnCmTable, [], name, value)


        class DocsL2vpnCmEntry(Entity):
            """
            An entry is indexed by Cable Modem Index that 
            describes L2VPN information for a single CM that is in 
            common with all L2VPNs implemented by the CM, 
            regardless of the L2VPN forwarding mode. 
            
            An entry in this table is created for every CM that  
            registers with a forwarding L2VPN encoding.
            
            .. attribute:: docsifcmtscmstatusindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`docsifcmtscmstatusindex <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsCmStatusTable.DocsIfCmtsCmStatusEntry>`
            
            	**config**\: False
            
            .. attribute:: docsl2vpncmcompliantcapability
            
            	This object reports whether an L2VPN forwarding CM is  compliant with the DOCSIS L2VPN specification, as reported  in the L2VPN Capability encoding in the CM's registration  request message.   If the capability encoding was omitted, this object must  report the value false(2)
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: docsl2vpncmdutfilteringcapability
            
            	This object reports whether an L2VPN forwarding CM is  capable of Downstream Unencrypted Traffic (DUT) Filtering,  as reported in the CM's registration request message.   If the capability encoding was omitted, this object must  report the value false(2)
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: docsl2vpncmdutcmim
            
            	This object reports the value configured in a per\-CM   L2VPN Encoding for Downstream Unencrypted Traffic (DUT)  Cable Modem Interface Mask (CMIM).    The DUT CMIM is a bit string with a '1' for each bit   position K for an internal or external CM interface with   ifIndex K to which the CM permits DUT to be forwarded. A CM  capable of DUT filtering MUST discard DUT to interfaces  with a '0' in the DUT CMIM.    If a CM's top\-level registration request L2VPN Encoding  contained no DUT CMIM subtype, this object is reported  with its default value of a '1' in bit position 0   (corresponding to the eCM's own 'self' host) and a '1' in   each bit position K for which an eSAFE interface exists at  ifIndex K. In other words, the default DUT CMIM includes   the eCM and all eSAFE interfaces.   This value is reported independently of whether the CM is  actually capable of performing DUT filtering
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: docsl2vpncmdhcpsnooping
            
            	This object reports the value of the Enable DHCP Snooping  subtype of a top\-level L2VPN Encoding.    It has the syntax of a CM Interface List bitmask and  represents a set of CM MAC bridge interfaces   corresponding to eSAFE hosts for which the CMTS is enabled   to snoop DHCP traffic in order to learn the eSAFE host MAC  address on that interface.     Only bits corresponding to eSAFE host MAC addresses may be  validly set in this object, including cpe(1) for ePS  and the eSAFE interfaces in bits positions 16 through 31
            	**type**\:  :py:class:`DocsL2vpnIfList <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DocsL2vpnIfList>`
            
            	**config**\: False
            
            

            """

            _prefix = 'DOCS-L2VPN-MIB'
            _revision = '2006-03-28'

            def __init__(self):
                super(DOCSL2VPNMIB.DocsL2vpnCmTable.DocsL2vpnCmEntry, self).__init__()

                self.yang_name = "docsL2vpnCmEntry"
                self.yang_parent_name = "docsL2vpnCmTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsifcmtscmstatusindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsifcmtscmstatusindex', (YLeaf(YType.str, 'docsIfCmtsCmStatusIndex'), ['int'])),
                    ('docsl2vpncmcompliantcapability', (YLeaf(YType.boolean, 'docsL2vpnCmCompliantCapability'), ['bool'])),
                    ('docsl2vpncmdutfilteringcapability', (YLeaf(YType.boolean, 'docsL2vpnCmDutFilteringCapability'), ['bool'])),
                    ('docsl2vpncmdutcmim', (YLeaf(YType.str, 'docsL2vpnCmDutCMIM'), ['str'])),
                    ('docsl2vpncmdhcpsnooping', (YLeaf(YType.bits, 'docsL2vpnCmDhcpSnooping'), ['Bits'])),
                ])
                self.docsifcmtscmstatusindex = None
                self.docsl2vpncmcompliantcapability = None
                self.docsl2vpncmdutfilteringcapability = None
                self.docsl2vpncmdutcmim = None
                self.docsl2vpncmdhcpsnooping = Bits()
                self._segment_path = lambda: "docsL2vpnCmEntry" + "[docsIfCmtsCmStatusIndex='" + str(self.docsifcmtscmstatusindex) + "']"
                self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/docsL2vpnCmTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnCmTable.DocsL2vpnCmEntry, [u'docsifcmtscmstatusindex', u'docsl2vpncmcompliantcapability', u'docsl2vpncmdutfilteringcapability', u'docsl2vpncmdutcmim', u'docsl2vpncmdhcpsnooping'], name, value)




    class DocsL2vpnVpnCmTable(Entity):
        """
        This table describes the operation of L2VPN forwarding 
        on each CM.
        
        .. attribute:: docsl2vpnvpncmentry
        
        	An entry is indexed by VPN ID and Cable Modem Index that  describes the operation of L2VPN forwarding for a single  L2VPN on a single CM
        	**type**\: list of  		 :py:class:`DocsL2vpnVpnCmEntry <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnVpnCmTable.DocsL2vpnVpnCmEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DOCS-L2VPN-MIB'
        _revision = '2006-03-28'

        def __init__(self):
            super(DOCSL2VPNMIB.DocsL2vpnVpnCmTable, self).__init__()

            self.yang_name = "docsL2vpnVpnCmTable"
            self.yang_parent_name = "DOCS-L2VPN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsL2vpnVpnCmEntry", ("docsl2vpnvpncmentry", DOCSL2VPNMIB.DocsL2vpnVpnCmTable.DocsL2vpnVpnCmEntry))])
            self._leafs = OrderedDict()

            self.docsl2vpnvpncmentry = YList(self)
            self._segment_path = lambda: "docsL2vpnVpnCmTable"
            self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnVpnCmTable, [], name, value)


        class DocsL2vpnVpnCmEntry(Entity):
            """
            An entry is indexed by VPN ID and Cable Modem Index that 
            describes the operation of L2VPN forwarding for a single 
            L2VPN on a single CM.
            
            .. attribute:: docsl2vpnidx  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`docsl2vpnidx <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnIndexToIdTable.DocsL2vpnIndexToIdEntry>`
            
            	**config**\: False
            
            .. attribute:: docsifcmtscmstatusindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`docsifcmtscmstatusindex <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsCmStatusTable.DocsIfCmtsCmStatusEntry>`
            
            	**config**\: False
            
            .. attribute:: docsl2vpnvpncmcmim
            
            	A Cable Modem Interface Mask represents a set of   MAC bridge interfaces within the CM. This object  represents the CMIM within a forwarding per\-SF L2VPN   encoding, which specifies a set of CM MAC bridge   interfaces to which L2VPN forwarding is restricted.   If the CMIM Subtype is omitted from a forwarding  per\-SF encoding, its default value includes only  cpePrimary(1) and cableMac(2), which can be encoded  with a single octet with the value 0x60
            	**type**\:  :py:class:`DocsL2vpnIfList <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DocsL2vpnIfList>`
            
            	**config**\: False
            
            .. attribute:: docsl2vpnvpncmindividualsaid
            
            	The BPI+ Security Association ID in which traffic intended  for point\-to\-point forwarding through an individual CM is   forwarded.    If the CMTS does not allocate an individual SAID for  multipoint forwarding (as is recommended),it MUST   report this object as zero
            	**type**\: int
            
            	**range:** 0..16383
            
            	**config**\: False
            
            .. attribute:: docsl2vpnvpncmvendorspecific
            
            	This object encodes the concatenation of all Vendor   Specific Subtype encodings that appeared in any   registration per\-CM L2VPN Encoding associated with this   entry
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'DOCS-L2VPN-MIB'
            _revision = '2006-03-28'

            def __init__(self):
                super(DOCSL2VPNMIB.DocsL2vpnVpnCmTable.DocsL2vpnVpnCmEntry, self).__init__()

                self.yang_name = "docsL2vpnVpnCmEntry"
                self.yang_parent_name = "docsL2vpnVpnCmTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsl2vpnidx','docsifcmtscmstatusindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsl2vpnidx', (YLeaf(YType.str, 'docsL2vpnIdx'), ['int'])),
                    ('docsifcmtscmstatusindex', (YLeaf(YType.str, 'docsIfCmtsCmStatusIndex'), ['int'])),
                    ('docsl2vpnvpncmcmim', (YLeaf(YType.bits, 'docsL2vpnVpnCmCMIM'), ['Bits'])),
                    ('docsl2vpnvpncmindividualsaid', (YLeaf(YType.int32, 'docsL2vpnVpnCmIndividualSAId'), ['int'])),
                    ('docsl2vpnvpncmvendorspecific', (YLeaf(YType.str, 'docsL2vpnVpnCmVendorSpecific'), ['str'])),
                ])
                self.docsl2vpnidx = None
                self.docsifcmtscmstatusindex = None
                self.docsl2vpnvpncmcmim = Bits()
                self.docsl2vpnvpncmindividualsaid = None
                self.docsl2vpnvpncmvendorspecific = None
                self._segment_path = lambda: "docsL2vpnVpnCmEntry" + "[docsL2vpnIdx='" + str(self.docsl2vpnidx) + "']" + "[docsIfCmtsCmStatusIndex='" + str(self.docsifcmtscmstatusindex) + "']"
                self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/docsL2vpnVpnCmTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnVpnCmTable.DocsL2vpnVpnCmEntry, [u'docsl2vpnidx', u'docsifcmtscmstatusindex', u'docsl2vpnvpncmcmim', u'docsl2vpnvpncmindividualsaid', u'docsl2vpnvpncmvendorspecific'], name, value)




    class DocsL2vpnVpnCmStatsTable(Entity):
        """
        This table contains statistics for forwarding of  
        packets to and from a CM on each VPN.
        
        .. attribute:: docsl2vpnvpncmstatsentry
        
        	An entry is indexed by VPN ID and Cable Modem Index
        	**type**\: list of  		 :py:class:`DocsL2vpnVpnCmStatsEntry <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnVpnCmStatsTable.DocsL2vpnVpnCmStatsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DOCS-L2VPN-MIB'
        _revision = '2006-03-28'

        def __init__(self):
            super(DOCSL2VPNMIB.DocsL2vpnVpnCmStatsTable, self).__init__()

            self.yang_name = "docsL2vpnVpnCmStatsTable"
            self.yang_parent_name = "DOCS-L2VPN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsL2vpnVpnCmStatsEntry", ("docsl2vpnvpncmstatsentry", DOCSL2VPNMIB.DocsL2vpnVpnCmStatsTable.DocsL2vpnVpnCmStatsEntry))])
            self._leafs = OrderedDict()

            self.docsl2vpnvpncmstatsentry = YList(self)
            self._segment_path = lambda: "docsL2vpnVpnCmStatsTable"
            self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnVpnCmStatsTable, [], name, value)


        class DocsL2vpnVpnCmStatsEntry(Entity):
            """
            An entry is indexed by VPN ID and Cable Modem Index.
            
            .. attribute:: docsl2vpnidx  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`docsl2vpnidx <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnIndexToIdTable.DocsL2vpnIndexToIdEntry>`
            
            	**config**\: False
            
            .. attribute:: docsifcmtscmstatusindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`docsifcmtscmstatusindex <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsCmStatusTable.DocsIfCmtsCmStatusEntry>`
            
            	**config**\: False
            
            .. attribute:: docsl2vpnvpncmstatsupstreampkts
            
            	The number of L2vpn\-forwarded packets received  from this instance's Cable Modem on  this instance's L2VPN
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: docsl2vpnvpncmstatsupstreambytes
            
            	The number of L2vpn\-forwarded bytes received  from this instance's Cable Modem on  this instance's L2VPN
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: docsl2vpnvpncmstatsupstreamdiscards
            
            	The number of L2\-forwarded packets   discarded from this instance's   Cable Modem on this instance's VPN
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: docsl2vpnvpncmstatsdownstreampkts
            
            	The number of L2\-forwarded packets  transmitted to this instance's  Cable Modem on this instance's VPN
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: docsl2vpnvpncmstatsdownstreambytes
            
            	The number of L2\-forwarded bytes  transmitted to this instance's  Cable Modem on this instance's VPN
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: docsl2vpnvpncmstatsdownstreamdiscards
            
            	The number of L2\-forwarded packets that were discarded   before they could be transmitted to this instance's   Cable Modem on this instance's VPN
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'DOCS-L2VPN-MIB'
            _revision = '2006-03-28'

            def __init__(self):
                super(DOCSL2VPNMIB.DocsL2vpnVpnCmStatsTable.DocsL2vpnVpnCmStatsEntry, self).__init__()

                self.yang_name = "docsL2vpnVpnCmStatsEntry"
                self.yang_parent_name = "docsL2vpnVpnCmStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsl2vpnidx','docsifcmtscmstatusindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsl2vpnidx', (YLeaf(YType.str, 'docsL2vpnIdx'), ['int'])),
                    ('docsifcmtscmstatusindex', (YLeaf(YType.str, 'docsIfCmtsCmStatusIndex'), ['int'])),
                    ('docsl2vpnvpncmstatsupstreampkts', (YLeaf(YType.uint32, 'docsL2vpnVpnCmStatsUpstreamPkts'), ['int'])),
                    ('docsl2vpnvpncmstatsupstreambytes', (YLeaf(YType.uint32, 'docsL2vpnVpnCmStatsUpstreamBytes'), ['int'])),
                    ('docsl2vpnvpncmstatsupstreamdiscards', (YLeaf(YType.uint32, 'docsL2vpnVpnCmStatsUpstreamDiscards'), ['int'])),
                    ('docsl2vpnvpncmstatsdownstreampkts', (YLeaf(YType.uint32, 'docsL2vpnVpnCmStatsDownstreamPkts'), ['int'])),
                    ('docsl2vpnvpncmstatsdownstreambytes', (YLeaf(YType.uint32, 'docsL2vpnVpnCmStatsDownstreamBytes'), ['int'])),
                    ('docsl2vpnvpncmstatsdownstreamdiscards', (YLeaf(YType.uint32, 'docsL2vpnVpnCmStatsDownstreamDiscards'), ['int'])),
                ])
                self.docsl2vpnidx = None
                self.docsifcmtscmstatusindex = None
                self.docsl2vpnvpncmstatsupstreampkts = None
                self.docsl2vpnvpncmstatsupstreambytes = None
                self.docsl2vpnvpncmstatsupstreamdiscards = None
                self.docsl2vpnvpncmstatsdownstreampkts = None
                self.docsl2vpnvpncmstatsdownstreambytes = None
                self.docsl2vpnvpncmstatsdownstreamdiscards = None
                self._segment_path = lambda: "docsL2vpnVpnCmStatsEntry" + "[docsL2vpnIdx='" + str(self.docsl2vpnidx) + "']" + "[docsIfCmtsCmStatusIndex='" + str(self.docsifcmtscmstatusindex) + "']"
                self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/docsL2vpnVpnCmStatsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnVpnCmStatsTable.DocsL2vpnVpnCmStatsEntry, [u'docsl2vpnidx', u'docsifcmtscmstatusindex', u'docsl2vpnvpncmstatsupstreampkts', u'docsl2vpnvpncmstatsupstreambytes', u'docsl2vpnvpncmstatsupstreamdiscards', u'docsl2vpnvpncmstatsdownstreampkts', u'docsl2vpnvpncmstatsdownstreambytes', u'docsl2vpnvpncmstatsdownstreamdiscards'], name, value)




    class DocsL2vpnPortStatusTable(Entity):
        """
        This table displays summary information for the 
        run\-time state of each VPN that is currently operating  
        on each bridge port.
        
        .. attribute:: docsl2vpnportstatusentry
        
        	Information specific to the operation of L2VPN forwarding  on a particular CMTS 'bridge port'. A CMTS 'bridge port'   may be defined by the CMTS vendor, but is advantageously a  single DOCSIS MAC Domain
        	**type**\: list of  		 :py:class:`DocsL2vpnPortStatusEntry <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnPortStatusTable.DocsL2vpnPortStatusEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DOCS-L2VPN-MIB'
        _revision = '2006-03-28'

        def __init__(self):
            super(DOCSL2VPNMIB.DocsL2vpnPortStatusTable, self).__init__()

            self.yang_name = "docsL2vpnPortStatusTable"
            self.yang_parent_name = "DOCS-L2VPN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsL2vpnPortStatusEntry", ("docsl2vpnportstatusentry", DOCSL2VPNMIB.DocsL2vpnPortStatusTable.DocsL2vpnPortStatusEntry))])
            self._leafs = OrderedDict()

            self.docsl2vpnportstatusentry = YList(self)
            self._segment_path = lambda: "docsL2vpnPortStatusTable"
            self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnPortStatusTable, [], name, value)


        class DocsL2vpnPortStatusEntry(Entity):
            """
            Information specific to the operation of L2VPN forwarding 
            on a particular CMTS 'bridge port'. A CMTS 'bridge port'  
            may be defined by the CMTS vendor, but is advantageously a 
            single DOCSIS MAC Domain.
            
            .. attribute:: dot1dbaseport  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`dot1dbaseport <ydk.models.cisco_ios_xe.BRIDGE_MIB.BRIDGEMIB.Dot1dBasePortTable.Dot1dBasePortEntry>`
            
            	**config**\: False
            
            .. attribute:: docsl2vpnidx  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`docsl2vpnidx <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnIndexToIdTable.DocsL2vpnIndexToIdEntry>`
            
            	**config**\: False
            
            .. attribute:: docsl2vpnportstatusgroupsaid
            
            	The Group SAID associated with this VPN on a   particular CMTS MAC domain. This SAID is used to encrypt  all downstream flooded bridge traffic sent to CMs on   this VPN and CMTS MAC domain bridge port.    A value of '0' means there is no associated Group SAID for  this VPN and bridge port, e.g., if the L2VPN uses  point\-to\-point individual SAIDs only for forwarding.   A bridge port that is not a CMTS MAC  domain will report a value of '0'
            	**type**\: int
            
            	**range:** 0..16383
            
            	**config**\: False
            
            

            """

            _prefix = 'DOCS-L2VPN-MIB'
            _revision = '2006-03-28'

            def __init__(self):
                super(DOCSL2VPNMIB.DocsL2vpnPortStatusTable.DocsL2vpnPortStatusEntry, self).__init__()

                self.yang_name = "docsL2vpnPortStatusEntry"
                self.yang_parent_name = "docsL2vpnPortStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1dbaseport','docsl2vpnidx']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1dbaseport', (YLeaf(YType.str, 'dot1dBasePort'), ['int'])),
                    ('docsl2vpnidx', (YLeaf(YType.str, 'docsL2vpnIdx'), ['int'])),
                    ('docsl2vpnportstatusgroupsaid', (YLeaf(YType.int32, 'docsL2vpnPortStatusGroupSAId'), ['int'])),
                ])
                self.dot1dbaseport = None
                self.docsl2vpnidx = None
                self.docsl2vpnportstatusgroupsaid = None
                self._segment_path = lambda: "docsL2vpnPortStatusEntry" + "[dot1dBasePort='" + str(self.dot1dbaseport) + "']" + "[docsL2vpnIdx='" + str(self.docsl2vpnidx) + "']"
                self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/docsL2vpnPortStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnPortStatusTable.DocsL2vpnPortStatusEntry, [u'dot1dbaseport', u'docsl2vpnidx', u'docsl2vpnportstatusgroupsaid'], name, value)




    class DocsL2vpnSfStatusTable(Entity):
        """
        This table displays SF\-specific L2VPN forwarding status  
        for each upstream service flow configured with a per\-SF  
         L2VPN Encoding. 
        
         Objects which were signaled in a per\-SF L2VPN Encoding but 
         apply for the entire CM are shown in the  
         docsL2vpnVpnCmTable.
        
        .. attribute:: docsl2vpnsfstatusentry
        
        	SF\-specific L2VPN forwarding status information for each  upstream service flow configured with a per\-SF L2VPN   Encoding. The ifIndex is of type docsCableMacLayer(127)
        	**type**\: list of  		 :py:class:`DocsL2vpnSfStatusEntry <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnSfStatusTable.DocsL2vpnSfStatusEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DOCS-L2VPN-MIB'
        _revision = '2006-03-28'

        def __init__(self):
            super(DOCSL2VPNMIB.DocsL2vpnSfStatusTable, self).__init__()

            self.yang_name = "docsL2vpnSfStatusTable"
            self.yang_parent_name = "DOCS-L2VPN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsL2vpnSfStatusEntry", ("docsl2vpnsfstatusentry", DOCSL2VPNMIB.DocsL2vpnSfStatusTable.DocsL2vpnSfStatusEntry))])
            self._leafs = OrderedDict()

            self.docsl2vpnsfstatusentry = YList(self)
            self._segment_path = lambda: "docsL2vpnSfStatusTable"
            self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnSfStatusTable, [], name, value)


        class DocsL2vpnSfStatusEntry(Entity):
            """
            SF\-specific L2VPN forwarding status information for each 
            upstream service flow configured with a per\-SF L2VPN  
            Encoding. The ifIndex is of type docsCableMacLayer(127).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: docsqosserviceflowid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`docsqosserviceflowid <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosServiceFlowTable.DocsQosServiceFlowEntry>`
            
            	**config**\: False
            
            .. attribute:: docsl2vpnsfstatusl2vpnid
            
            	This object represents the value of the L2VPN Identifier  subtype of a per\-SF L2VPN Encoding
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: docsl2vpnsfstatusingressuserpriority
            
            	This object provides the configured Ingress User Priority  subtype of a per\-SF L2VPN Encoding for this CM. If the   subtype was omitted, this object's value is zero
            	**type**\: int
            
            	**range:** 0..7
            
            	**config**\: False
            
            .. attribute:: docsl2vpnsfstatusvendorspecific
            
            	This object provides the set of configured Vendor Specific  subtypes within a per\-SF L2VPN Encoding for a CM. If no   Vendor Specific subtype was specified, this object is a   zero length octet string. If one or more Vendor Specific   subtype parameters was specified, this object represents   the concatenation of all such subtypes
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'DOCS-L2VPN-MIB'
            _revision = '2006-03-28'

            def __init__(self):
                super(DOCSL2VPNMIB.DocsL2vpnSfStatusTable.DocsL2vpnSfStatusEntry, self).__init__()

                self.yang_name = "docsL2vpnSfStatusEntry"
                self.yang_parent_name = "docsL2vpnSfStatusTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsqosserviceflowid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsqosserviceflowid', (YLeaf(YType.str, 'docsQosServiceFlowId'), ['int'])),
                    ('docsl2vpnsfstatusl2vpnid', (YLeaf(YType.str, 'docsL2vpnSfStatusL2vpnId'), ['str'])),
                    ('docsl2vpnsfstatusingressuserpriority', (YLeaf(YType.uint32, 'docsL2vpnSfStatusIngressUserPriority'), ['int'])),
                    ('docsl2vpnsfstatusvendorspecific', (YLeaf(YType.str, 'docsL2vpnSfStatusVendorSpecific'), ['str'])),
                ])
                self.ifindex = None
                self.docsqosserviceflowid = None
                self.docsl2vpnsfstatusl2vpnid = None
                self.docsl2vpnsfstatusingressuserpriority = None
                self.docsl2vpnsfstatusvendorspecific = None
                self._segment_path = lambda: "docsL2vpnSfStatusEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsQosServiceFlowId='" + str(self.docsqosserviceflowid) + "']"
                self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/docsL2vpnSfStatusTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnSfStatusTable.DocsL2vpnSfStatusEntry, [u'ifindex', u'docsqosserviceflowid', u'docsl2vpnsfstatusl2vpnid', u'docsl2vpnsfstatusingressuserpriority', u'docsl2vpnsfstatusvendorspecific'], name, value)




    class DocsL2vpnPktClassTable(Entity):
        """
        This table provides the L2VPN\-specific objects for 
        packet classifiers that apply to only L2VPN traffic.  
        The indices of this table are a subset of the 
        indices of classifiers in docsQosPktClassTable.
        
        .. attribute:: docsl2vpnpktclassentry
        
        	An entry in this table extends a single row  of docsQosPktClassTable for a rule that applies only to  downstream L2VPN forwarded packets.  The index ifIndex is an ifType of docsCableMaclayer(127)
        	**type**\: list of  		 :py:class:`DocsL2vpnPktClassEntry <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnPktClassTable.DocsL2vpnPktClassEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DOCS-L2VPN-MIB'
        _revision = '2006-03-28'

        def __init__(self):
            super(DOCSL2VPNMIB.DocsL2vpnPktClassTable, self).__init__()

            self.yang_name = "docsL2vpnPktClassTable"
            self.yang_parent_name = "DOCS-L2VPN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsL2vpnPktClassEntry", ("docsl2vpnpktclassentry", DOCSL2VPNMIB.DocsL2vpnPktClassTable.DocsL2vpnPktClassEntry))])
            self._leafs = OrderedDict()

            self.docsl2vpnpktclassentry = YList(self)
            self._segment_path = lambda: "docsL2vpnPktClassTable"
            self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnPktClassTable, [], name, value)


        class DocsL2vpnPktClassEntry(Entity):
            """
            An entry in this table extends a single row 
            of docsQosPktClassTable for a rule that applies only to 
            downstream L2VPN forwarded packets. 
            The index ifIndex is an ifType of docsCableMaclayer(127).
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: docsqosserviceflowid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`docsqosserviceflowid <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosServiceFlowTable.DocsQosServiceFlowEntry>`
            
            	**config**\: False
            
            .. attribute:: docsqospktclassid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..65535
            
            	**refers to**\:  :py:class:`docsqospktclassid <ydk.models.cisco_ios_xe.DOCS_QOS_MIB.DOCSQOSMIB.DocsQosPktClassTable.DocsQosPktClassEntry>`
            
            	**config**\: False
            
            .. attribute:: docsl2vpnpktclassl2vpnid
            
            	The locally assigned L2VPN index corresponding to the VPN  Identifier subtype of a Downstream Classifier L2VPN   Encoding
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: docsl2vpnpktclassuserprirangelow
            
            	The lower priority of the user Priority Range subtype  of a Downstream Classifier L2VPN Encoding. If the subtype  was omitted, this object has value 0
            	**type**\: int
            
            	**range:** 0..7
            
            	**config**\: False
            
            .. attribute:: docsl2vpnpktclassuserprirangehigh
            
            	The higher priority of the user Priority Range subtype  of a Downstream Classifier L2VPN Encoding. If the subtype  was omitted, this object has value 7
            	**type**\: int
            
            	**range:** 0..7
            
            	**config**\: False
            
            .. attribute:: docsl2vpnpktclasscmim
            
            	The Cable Modem Interface Mask (CMIM) signaled in a   Packet Classifier Encoding.  In a Downstream Packet   Classifier Encoding, a specified CMIM value restricts the   classifier to match packets with a Destination MAC address  corresponding to the interfaces indicated in the CMIM mask.  The eCM self and any eSAFE interface bits correspond to  the individual eCM and eSAFE host MAC addresses.   In an Upstream Packet Classifier encoding, a specified CMIM  value restricts the classifier to match packets with an   ingress bridge port interface matching the bits in the   CMIM value.   If the CMIM subtype was omitted, this object should be   reported as a zero length octet string
            	**type**\:  :py:class:`DocsL2vpnIfList <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DocsL2vpnIfList>`
            
            	**config**\: False
            
            .. attribute:: docsl2vpnpktclassvendorspecific
            
            	This object provides the set of configured   Vendor Specific subtypes within a Packet Classifier   Encoding for a CM. If no Vendor Specific subtype was   specified, this object is a zero length octet string.   If one or more Vendor Specific subtype parameters was   specified, this object represents the concatenation of all  such subtypes
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'DOCS-L2VPN-MIB'
            _revision = '2006-03-28'

            def __init__(self):
                super(DOCSL2VPNMIB.DocsL2vpnPktClassTable.DocsL2vpnPktClassEntry, self).__init__()

                self.yang_name = "docsL2vpnPktClassEntry"
                self.yang_parent_name = "docsL2vpnPktClassTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','docsqosserviceflowid','docsqospktclassid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('docsqosserviceflowid', (YLeaf(YType.str, 'docsQosServiceFlowId'), ['int'])),
                    ('docsqospktclassid', (YLeaf(YType.str, 'docsQosPktClassId'), ['int'])),
                    ('docsl2vpnpktclassl2vpnid', (YLeaf(YType.str, 'docsL2vpnPktClassL2vpnId'), ['str'])),
                    ('docsl2vpnpktclassuserprirangelow', (YLeaf(YType.uint32, 'docsL2vpnPktClassUserPriRangeLow'), ['int'])),
                    ('docsl2vpnpktclassuserprirangehigh', (YLeaf(YType.uint32, 'docsL2vpnPktClassUserPriRangeHigh'), ['int'])),
                    ('docsl2vpnpktclasscmim', (YLeaf(YType.bits, 'docsL2vpnPktClassCMIM'), ['Bits'])),
                    ('docsl2vpnpktclassvendorspecific', (YLeaf(YType.str, 'docsL2vpnPktClassVendorSpecific'), ['str'])),
                ])
                self.ifindex = None
                self.docsqosserviceflowid = None
                self.docsqospktclassid = None
                self.docsl2vpnpktclassl2vpnid = None
                self.docsl2vpnpktclassuserprirangelow = None
                self.docsl2vpnpktclassuserprirangehigh = None
                self.docsl2vpnpktclasscmim = Bits()
                self.docsl2vpnpktclassvendorspecific = None
                self._segment_path = lambda: "docsL2vpnPktClassEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[docsQosServiceFlowId='" + str(self.docsqosserviceflowid) + "']" + "[docsQosPktClassId='" + str(self.docsqospktclassid) + "']"
                self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/docsL2vpnPktClassTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnPktClassTable.DocsL2vpnPktClassEntry, [u'ifindex', u'docsqosserviceflowid', u'docsqospktclassid', u'docsl2vpnpktclassl2vpnid', u'docsl2vpnpktclassuserprirangelow', u'docsl2vpnpktclassuserprirangehigh', u'docsl2vpnpktclasscmim', u'docsl2vpnpktclassvendorspecific'], name, value)




    class DocsL2vpnCmNsiTable(Entity):
        """
        This table describes the NSI configuration for a single 
        CM when operating in point\-to\-point forwarding mode for an 
        L2VPN.
        
        .. attribute:: docsl2vpncmnsientry
        
        	An entry indexed by VPN ID and Cable Modem Index that  describes the point\-to\-point forwarding between a single  NSI encapsulation and a single CM. This table is   implemented only for a CM forwarding an L2VPN on a   point\-to\-point basis. It is associated with a single   per\-CM L2VPN encoding
        	**type**\: list of  		 :py:class:`DocsL2vpnCmNsiEntry <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnCmNsiTable.DocsL2vpnCmNsiEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DOCS-L2VPN-MIB'
        _revision = '2006-03-28'

        def __init__(self):
            super(DOCSL2VPNMIB.DocsL2vpnCmNsiTable, self).__init__()

            self.yang_name = "docsL2vpnCmNsiTable"
            self.yang_parent_name = "DOCS-L2VPN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsL2vpnCmNsiEntry", ("docsl2vpncmnsientry", DOCSL2VPNMIB.DocsL2vpnCmNsiTable.DocsL2vpnCmNsiEntry))])
            self._leafs = OrderedDict()

            self.docsl2vpncmnsientry = YList(self)
            self._segment_path = lambda: "docsL2vpnCmNsiTable"
            self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnCmNsiTable, [], name, value)


        class DocsL2vpnCmNsiEntry(Entity):
            """
            An entry indexed by VPN ID and Cable Modem Index that 
            describes the point\-to\-point forwarding between a single 
            NSI encapsulation and a single CM. This table is  
            implemented only for a CM forwarding an L2VPN on a  
            point\-to\-point basis. It is associated with a single  
            per\-CM L2VPN encoding.
            
            .. attribute:: docsl2vpnidx  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`docsl2vpnidx <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnIndexToIdTable.DocsL2vpnIndexToIdEntry>`
            
            	**config**\: False
            
            .. attribute:: docsifcmtscmstatusindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`docsifcmtscmstatusindex <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsCmStatusTable.DocsIfCmtsCmStatusEntry>`
            
            	**config**\: False
            
            .. attribute:: docsl2vpncmnsiencapsubtype
            
            	The General Encapsulation Information (GEI) subtype of the  Network System Interface (NSI) encapsulation configured  for the CM
            	**type**\:  :py:class:`DocsNsiEncapSubtype <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DocsNsiEncapSubtype>`
            
            	**config**\: False
            
            .. attribute:: docsl2vpncmnsiencapvalue
            
            	The encapsulation value for L2VPN forwarded packets on NSI  ports
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: docsl2vpncmnsiagi
            
            	This object is the configuration of any Attachment Group   Identifier subtype in the per\-SF L2VPN Encoding   represented by this row. If the subtype was omitted, this   object's value is a zero length string
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: docsl2vpncmnsisaii
            
            	This object is the configuration of any Source   Attachment Individual ID subtype in the L2VPN Encoding   represented by this row. If the subtype was omitted, this  object's value is a zero length string
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: docsl2vpncmnsitaii
            
            	This object is the configuration of any Target  Attachment Individual ID subtype in the L2VPN Encoding  represented by this row. If the subtype was omitted, this  object's value is a zero length string
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'DOCS-L2VPN-MIB'
            _revision = '2006-03-28'

            def __init__(self):
                super(DOCSL2VPNMIB.DocsL2vpnCmNsiTable.DocsL2vpnCmNsiEntry, self).__init__()

                self.yang_name = "docsL2vpnCmNsiEntry"
                self.yang_parent_name = "docsL2vpnCmNsiTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsl2vpnidx','docsifcmtscmstatusindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsl2vpnidx', (YLeaf(YType.str, 'docsL2vpnIdx'), ['int'])),
                    ('docsifcmtscmstatusindex', (YLeaf(YType.str, 'docsIfCmtsCmStatusIndex'), ['int'])),
                    ('docsl2vpncmnsiencapsubtype', (YLeaf(YType.enumeration, 'docsL2vpnCmNsiEncapSubtype'), [('ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB', 'DocsNsiEncapSubtype', '')])),
                    ('docsl2vpncmnsiencapvalue', (YLeaf(YType.str, 'docsL2vpnCmNsiEncapValue'), ['str'])),
                    ('docsl2vpncmnsiagi', (YLeaf(YType.str, 'docsL2vpnCmNsiAGI'), ['str'])),
                    ('docsl2vpncmnsisaii', (YLeaf(YType.str, 'docsL2vpnCmNsiSAII'), ['str'])),
                    ('docsl2vpncmnsitaii', (YLeaf(YType.str, 'docsL2vpnCmNsiTAII'), ['str'])),
                ])
                self.docsl2vpnidx = None
                self.docsifcmtscmstatusindex = None
                self.docsl2vpncmnsiencapsubtype = None
                self.docsl2vpncmnsiencapvalue = None
                self.docsl2vpncmnsiagi = None
                self.docsl2vpncmnsisaii = None
                self.docsl2vpncmnsitaii = None
                self._segment_path = lambda: "docsL2vpnCmNsiEntry" + "[docsL2vpnIdx='" + str(self.docsl2vpnidx) + "']" + "[docsIfCmtsCmStatusIndex='" + str(self.docsifcmtscmstatusindex) + "']"
                self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/docsL2vpnCmNsiTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnCmNsiTable.DocsL2vpnCmNsiEntry, [u'docsl2vpnidx', u'docsifcmtscmstatusindex', u'docsl2vpncmnsiencapsubtype', u'docsl2vpncmnsiencapvalue', u'docsl2vpncmnsiagi', u'docsl2vpncmnsisaii', u'docsl2vpncmnsitaii'], name, value)




    class DocsL2vpnCmVpnCpeTable(Entity):
        """
        This table is a list of CPEs, indexed by the VPNs on a  
        Cable Modem.
        
        .. attribute:: docsl2vpncmvpncpeentry
        
        	This table is a list of CPEs, indexed by the VPNs on a   Cable Modem
        	**type**\: list of  		 :py:class:`DocsL2vpnCmVpnCpeEntry <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnCmVpnCpeTable.DocsL2vpnCmVpnCpeEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DOCS-L2VPN-MIB'
        _revision = '2006-03-28'

        def __init__(self):
            super(DOCSL2VPNMIB.DocsL2vpnCmVpnCpeTable, self).__init__()

            self.yang_name = "docsL2vpnCmVpnCpeTable"
            self.yang_parent_name = "DOCS-L2VPN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsL2vpnCmVpnCpeEntry", ("docsl2vpncmvpncpeentry", DOCSL2VPNMIB.DocsL2vpnCmVpnCpeTable.DocsL2vpnCmVpnCpeEntry))])
            self._leafs = OrderedDict()

            self.docsl2vpncmvpncpeentry = YList(self)
            self._segment_path = lambda: "docsL2vpnCmVpnCpeTable"
            self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnCmVpnCpeTable, [], name, value)


        class DocsL2vpnCmVpnCpeEntry(Entity):
            """
            This table is a list of CPEs, indexed by the VPNs on a  
            Cable Modem.
            
            .. attribute:: docsifcmtscmstatusindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`docsifcmtscmstatusindex <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsCmStatusTable.DocsIfCmtsCmStatusEntry>`
            
            	**config**\: False
            
            .. attribute:: docsl2vpnidx  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`docsl2vpnidx <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnIndexToIdTable.DocsL2vpnIndexToIdEntry>`
            
            	**config**\: False
            
            .. attribute:: docsl2vpncmvpncpemacaddress  (key)
            
            	The Customer Premise Equipment (CPE) Mac Address  that is attached to this instances Cable Modem  and bridging on this instance's VPN Id
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**config**\: False
            
            

            """

            _prefix = 'DOCS-L2VPN-MIB'
            _revision = '2006-03-28'

            def __init__(self):
                super(DOCSL2VPNMIB.DocsL2vpnCmVpnCpeTable.DocsL2vpnCmVpnCpeEntry, self).__init__()

                self.yang_name = "docsL2vpnCmVpnCpeEntry"
                self.yang_parent_name = "docsL2vpnCmVpnCpeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsifcmtscmstatusindex','docsl2vpnidx','docsl2vpncmvpncpemacaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsifcmtscmstatusindex', (YLeaf(YType.str, 'docsIfCmtsCmStatusIndex'), ['int'])),
                    ('docsl2vpnidx', (YLeaf(YType.str, 'docsL2vpnIdx'), ['int'])),
                    ('docsl2vpncmvpncpemacaddress', (YLeaf(YType.str, 'docsL2vpnCmVpnCpeMacAddress'), ['str'])),
                ])
                self.docsifcmtscmstatusindex = None
                self.docsl2vpnidx = None
                self.docsl2vpncmvpncpemacaddress = None
                self._segment_path = lambda: "docsL2vpnCmVpnCpeEntry" + "[docsIfCmtsCmStatusIndex='" + str(self.docsifcmtscmstatusindex) + "']" + "[docsL2vpnIdx='" + str(self.docsl2vpnidx) + "']" + "[docsL2vpnCmVpnCpeMacAddress='" + str(self.docsl2vpncmvpncpemacaddress) + "']"
                self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/docsL2vpnCmVpnCpeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnCmVpnCpeTable.DocsL2vpnCmVpnCpeEntry, [u'docsifcmtscmstatusindex', u'docsl2vpnidx', u'docsl2vpncmvpncpemacaddress'], name, value)




    class DocsL2vpnVpnCmCpeTable(Entity):
        """
        This table contains a list of bridging CPEs, indexed by 
        L2VPN Index and the corresponding CMs on that VPN.
        
        .. attribute:: docsl2vpnvpncmcpeentry
        
        	This table contains a list of bridging CPEs, indexed by  VPN and the corresponding CMs on that VPN
        	**type**\: list of  		 :py:class:`DocsL2vpnVpnCmCpeEntry <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnVpnCmCpeTable.DocsL2vpnVpnCmCpeEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DOCS-L2VPN-MIB'
        _revision = '2006-03-28'

        def __init__(self):
            super(DOCSL2VPNMIB.DocsL2vpnVpnCmCpeTable, self).__init__()

            self.yang_name = "docsL2vpnVpnCmCpeTable"
            self.yang_parent_name = "DOCS-L2VPN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsL2vpnVpnCmCpeEntry", ("docsl2vpnvpncmcpeentry", DOCSL2VPNMIB.DocsL2vpnVpnCmCpeTable.DocsL2vpnVpnCmCpeEntry))])
            self._leafs = OrderedDict()

            self.docsl2vpnvpncmcpeentry = YList(self)
            self._segment_path = lambda: "docsL2vpnVpnCmCpeTable"
            self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnVpnCmCpeTable, [], name, value)


        class DocsL2vpnVpnCmCpeEntry(Entity):
            """
            This table contains a list of bridging CPEs, indexed by 
            VPN and the corresponding CMs on that VPN.
            
            .. attribute:: docsl2vpnidx  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`docsl2vpnidx <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnIndexToIdTable.DocsL2vpnIndexToIdEntry>`
            
            	**config**\: False
            
            .. attribute:: docsifcmtscmstatusindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`docsifcmtscmstatusindex <ydk.models.cisco_ios_xe.DOCS_IF_MIB.DOCSIFMIB.DocsIfCmtsCmStatusTable.DocsIfCmtsCmStatusEntry>`
            
            	**config**\: False
            
            .. attribute:: docsl2vpnvpncmcpemacaddress  (key)
            
            	The Customer Premise Equipment (CPE) Mac Address  that is attached to this instances Cable Modem  and bridging on this instance's L2vpn Index
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**config**\: False
            
            

            """

            _prefix = 'DOCS-L2VPN-MIB'
            _revision = '2006-03-28'

            def __init__(self):
                super(DOCSL2VPNMIB.DocsL2vpnVpnCmCpeTable.DocsL2vpnVpnCmCpeEntry, self).__init__()

                self.yang_name = "docsL2vpnVpnCmCpeEntry"
                self.yang_parent_name = "docsL2vpnVpnCmCpeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsl2vpnidx','docsifcmtscmstatusindex','docsl2vpnvpncmcpemacaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsl2vpnidx', (YLeaf(YType.str, 'docsL2vpnIdx'), ['int'])),
                    ('docsifcmtscmstatusindex', (YLeaf(YType.str, 'docsIfCmtsCmStatusIndex'), ['int'])),
                    ('docsl2vpnvpncmcpemacaddress', (YLeaf(YType.str, 'docsL2vpnVpnCmCpeMacAddress'), ['str'])),
                ])
                self.docsl2vpnidx = None
                self.docsifcmtscmstatusindex = None
                self.docsl2vpnvpncmcpemacaddress = None
                self._segment_path = lambda: "docsL2vpnVpnCmCpeEntry" + "[docsL2vpnIdx='" + str(self.docsl2vpnidx) + "']" + "[docsIfCmtsCmStatusIndex='" + str(self.docsifcmtscmstatusindex) + "']" + "[docsL2vpnVpnCmCpeMacAddress='" + str(self.docsl2vpnvpncmcpemacaddress) + "']"
                self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/docsL2vpnVpnCmCpeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnVpnCmCpeTable.DocsL2vpnVpnCmCpeEntry, [u'docsl2vpnidx', u'docsifcmtscmstatusindex', u'docsl2vpnvpncmcpemacaddress'], name, value)




    class DocsL2vpnDot1qTpFdbExtTable(Entity):
        """
        This table contains packet counters for  
        Unicast MAC Addresses within a VPN.
        
        .. attribute:: docsl2vpndot1qtpfdbextentry
        
        	This table extends the dot1qTpFdbTable only for RF network  bridge port entries.  It is implemented by an agent only  if the agent implements dot1qTpFdbTable for RF network  bridge ports
        	**type**\: list of  		 :py:class:`DocsL2vpnDot1qTpFdbExtEntry <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnDot1qTpFdbExtTable.DocsL2vpnDot1qTpFdbExtEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DOCS-L2VPN-MIB'
        _revision = '2006-03-28'

        def __init__(self):
            super(DOCSL2VPNMIB.DocsL2vpnDot1qTpFdbExtTable, self).__init__()

            self.yang_name = "docsL2vpnDot1qTpFdbExtTable"
            self.yang_parent_name = "DOCS-L2VPN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsL2vpnDot1qTpFdbExtEntry", ("docsl2vpndot1qtpfdbextentry", DOCSL2VPNMIB.DocsL2vpnDot1qTpFdbExtTable.DocsL2vpnDot1qTpFdbExtEntry))])
            self._leafs = OrderedDict()

            self.docsl2vpndot1qtpfdbextentry = YList(self)
            self._segment_path = lambda: "docsL2vpnDot1qTpFdbExtTable"
            self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnDot1qTpFdbExtTable, [], name, value)


        class DocsL2vpnDot1qTpFdbExtEntry(Entity):
            """
            This table extends the dot1qTpFdbTable only for RF network 
            bridge port entries.  It is implemented by an agent only 
            if the agent implements dot1qTpFdbTable for RF network 
            bridge ports.
            
            .. attribute:: dot1qfdbid  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`dot1qfdbid <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qFdbTable.Dot1qFdbEntry>`
            
            	**config**\: False
            
            .. attribute:: dot1qtpfdbaddress  (key)
            
            	
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**refers to**\:  :py:class:`dot1qtpfdbaddress <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qTpFdbTable.Dot1qTpFdbEntry>`
            
            	**config**\: False
            
            .. attribute:: docsl2vpndot1qtpfdbexttransmitpkts
            
            	The number of packets where the Destination   MAC Address matched this instance   dot1qTpFdbAddress and packet was bridged on  a VPN, where the VPN ID matched this   instance's dot1qFdbId
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: docsl2vpndot1qtpfdbextreceivepkts
            
            	The number of packets where the Source MAC   Address matched this instance dot1qTpFdbAddress  and the packet was bridged on a VPN,  where the docsL2vpnIdx matched this instance's   dot1qFdbId
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'DOCS-L2VPN-MIB'
            _revision = '2006-03-28'

            def __init__(self):
                super(DOCSL2VPNMIB.DocsL2vpnDot1qTpFdbExtTable.DocsL2vpnDot1qTpFdbExtEntry, self).__init__()

                self.yang_name = "docsL2vpnDot1qTpFdbExtEntry"
                self.yang_parent_name = "docsL2vpnDot1qTpFdbExtTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1qfdbid','dot1qtpfdbaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1qfdbid', (YLeaf(YType.str, 'dot1qFdbId'), ['int'])),
                    ('dot1qtpfdbaddress', (YLeaf(YType.str, 'dot1qTpFdbAddress'), ['str'])),
                    ('docsl2vpndot1qtpfdbexttransmitpkts', (YLeaf(YType.uint32, 'docsL2vpnDot1qTpFdbExtTransmitPkts'), ['int'])),
                    ('docsl2vpndot1qtpfdbextreceivepkts', (YLeaf(YType.uint32, 'docsL2vpnDot1qTpFdbExtReceivePkts'), ['int'])),
                ])
                self.dot1qfdbid = None
                self.dot1qtpfdbaddress = None
                self.docsl2vpndot1qtpfdbexttransmitpkts = None
                self.docsl2vpndot1qtpfdbextreceivepkts = None
                self._segment_path = lambda: "docsL2vpnDot1qTpFdbExtEntry" + "[dot1qFdbId='" + str(self.dot1qfdbid) + "']" + "[dot1qTpFdbAddress='" + str(self.dot1qtpfdbaddress) + "']"
                self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/docsL2vpnDot1qTpFdbExtTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnDot1qTpFdbExtTable.DocsL2vpnDot1qTpFdbExtEntry, [u'dot1qfdbid', u'dot1qtpfdbaddress', u'docsl2vpndot1qtpfdbexttransmitpkts', u'docsl2vpndot1qtpfdbextreceivepkts'], name, value)




    class DocsL2vpnDot1qTpGroupExtTable(Entity):
        """
        This table contains packet counters for  
        Multicast MAC Addresses within a VPN.
        
        .. attribute:: docsl2vpndot1qtpgroupextentry
        
        	This table extends the dot1qTpGroupTable only for RF   Network bridge port entries.  It is implemented by an agent  Only if the agent implements dot1qTpGroupTable for RF   network bridge ports
        	**type**\: list of  		 :py:class:`DocsL2vpnDot1qTpGroupExtEntry <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DOCSL2VPNMIB.DocsL2vpnDot1qTpGroupExtTable.DocsL2vpnDot1qTpGroupExtEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'DOCS-L2VPN-MIB'
        _revision = '2006-03-28'

        def __init__(self):
            super(DOCSL2VPNMIB.DocsL2vpnDot1qTpGroupExtTable, self).__init__()

            self.yang_name = "docsL2vpnDot1qTpGroupExtTable"
            self.yang_parent_name = "DOCS-L2VPN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsL2vpnDot1qTpGroupExtEntry", ("docsl2vpndot1qtpgroupextentry", DOCSL2VPNMIB.DocsL2vpnDot1qTpGroupExtTable.DocsL2vpnDot1qTpGroupExtEntry))])
            self._leafs = OrderedDict()

            self.docsl2vpndot1qtpgroupextentry = YList(self)
            self._segment_path = lambda: "docsL2vpnDot1qTpGroupExtTable"
            self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnDot1qTpGroupExtTable, [], name, value)


        class DocsL2vpnDot1qTpGroupExtEntry(Entity):
            """
            This table extends the dot1qTpGroupTable only for RF  
            Network bridge port entries.  It is implemented by an agent 
            Only if the agent implements dot1qTpGroupTable for RF  
            network bridge ports.
            
            .. attribute:: dot1qvlanindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`dot1qvlanindex <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry>`
            
            	**config**\: False
            
            .. attribute:: dot1qtpgroupaddress  (key)
            
            	
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**refers to**\:  :py:class:`dot1qtpgroupaddress <ydk.models.cisco_ios_xe.Q_BRIDGE_MIB.QBRIDGEMIB.Dot1qTpGroupTable.Dot1qTpGroupEntry>`
            
            	**config**\: False
            
            .. attribute:: docsl2vpndot1qtpgroupexttransmitpkts
            
            	The number of packets where the Destination   MAC Address matched this instance   dot1qTpGroupAddress and packet was bridged on  a VPN, where the docsL2vpnIdx matched this   instance's dot1qVlanIndex
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: docsl2vpndot1qtpgroupextreceivepkts
            
            	The number of packets where the Source MAC   Address matched this instance dot1qTpGroupAddress  and the packet was bridged on a VPN,  where the docsL2vpnIdx matched this instance's   dot1qVlanIndex
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'DOCS-L2VPN-MIB'
            _revision = '2006-03-28'

            def __init__(self):
                super(DOCSL2VPNMIB.DocsL2vpnDot1qTpGroupExtTable.DocsL2vpnDot1qTpGroupExtEntry, self).__init__()

                self.yang_name = "docsL2vpnDot1qTpGroupExtEntry"
                self.yang_parent_name = "docsL2vpnDot1qTpGroupExtTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot1qvlanindex','dot1qtpgroupaddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot1qvlanindex', (YLeaf(YType.str, 'dot1qVlanIndex'), ['int'])),
                    ('dot1qtpgroupaddress', (YLeaf(YType.str, 'dot1qTpGroupAddress'), ['str'])),
                    ('docsl2vpndot1qtpgroupexttransmitpkts', (YLeaf(YType.uint32, 'docsL2vpnDot1qTpGroupExtTransmitPkts'), ['int'])),
                    ('docsl2vpndot1qtpgroupextreceivepkts', (YLeaf(YType.uint32, 'docsL2vpnDot1qTpGroupExtReceivePkts'), ['int'])),
                ])
                self.dot1qvlanindex = None
                self.dot1qtpgroupaddress = None
                self.docsl2vpndot1qtpgroupexttransmitpkts = None
                self.docsl2vpndot1qtpgroupextreceivepkts = None
                self._segment_path = lambda: "docsL2vpnDot1qTpGroupExtEntry" + "[dot1qVlanIndex='" + str(self.dot1qvlanindex) + "']" + "[dot1qTpGroupAddress='" + str(self.dot1qtpgroupaddress) + "']"
                self._absolute_path = lambda: "DOCS-L2VPN-MIB:DOCS-L2VPN-MIB/docsL2vpnDot1qTpGroupExtTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSL2VPNMIB.DocsL2vpnDot1qTpGroupExtTable.DocsL2vpnDot1qTpGroupExtEntry, [u'dot1qvlanindex', u'dot1qtpgroupaddress', u'docsl2vpndot1qtpgroupexttransmitpkts', u'docsl2vpndot1qtpgroupextreceivepkts'], name, value)



    def clone_ptr(self):
        self._top_entity = DOCSL2VPNMIB()
        return self._top_entity




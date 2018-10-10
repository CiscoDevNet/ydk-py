""" OLD_CISCO_INTERFACES_MIB 


"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class OLDCISCOINTERFACESMIB(Entity):
    """
    
    
    .. attribute:: liftable
    
    	A list of interface entries
    	**type**\:  :py:class:`LifTable <ydk.models.cisco_ios_xe.OLD_CISCO_INTERFACES_MIB.OLDCISCOINTERFACESMIB.LifTable>`
    
    	**status**\: obsolete
    
    .. attribute:: lfsiptable
    
    	A list of card entries for 4T, HSSI, Mx serial or FSIP
    	**type**\:  :py:class:`LFSIPTable <ydk.models.cisco_ios_xe.OLD_CISCO_INTERFACES_MIB.OLDCISCOINTERFACESMIB.LFSIPTable>`
    
    	**status**\: obsolete
    
    

    """

    _prefix = 'OLD-CISCO-INTERFACES-MIB'

    def __init__(self):
        super(OLDCISCOINTERFACESMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "OLD-CISCO-INTERFACES-MIB"
        self.yang_parent_name = "OLD-CISCO-INTERFACES-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("lifTable", ("liftable", OLDCISCOINTERFACESMIB.LifTable)), ("lFSIPTable", ("lfsiptable", OLDCISCOINTERFACESMIB.LFSIPTable))])
        self._leafs = OrderedDict()

        self.liftable = OLDCISCOINTERFACESMIB.LifTable()
        self.liftable.parent = self
        self._children_name_map["liftable"] = "lifTable"

        self.lfsiptable = OLDCISCOINTERFACESMIB.LFSIPTable()
        self.lfsiptable.parent = self
        self._children_name_map["lfsiptable"] = "lFSIPTable"
        self._segment_path = lambda: "OLD-CISCO-INTERFACES-MIB:OLD-CISCO-INTERFACES-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(OLDCISCOINTERFACESMIB, [], name, value)


    class LifTable(Entity):
        """
        A list of interface entries.
        
        .. attribute:: lifentry
        
        	A collection of additional objects in the cisco interface
        	**type**\: list of  		 :py:class:`LifEntry <ydk.models.cisco_ios_xe.OLD_CISCO_INTERFACES_MIB.OLDCISCOINTERFACESMIB.LifTable.LifEntry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'OLD-CISCO-INTERFACES-MIB'

        def __init__(self):
            super(OLDCISCOINTERFACESMIB.LifTable, self).__init__()

            self.yang_name = "lifTable"
            self.yang_parent_name = "OLD-CISCO-INTERFACES-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("lifEntry", ("lifentry", OLDCISCOINTERFACESMIB.LifTable.LifEntry))])
            self._leafs = OrderedDict()

            self.lifentry = YList(self)
            self._segment_path = lambda: "lifTable"
            self._absolute_path = lambda: "OLD-CISCO-INTERFACES-MIB:OLD-CISCO-INTERFACES-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OLDCISCOINTERFACESMIB.LifTable, [], name, value)


        class LifEntry(Entity):
            """
            A collection of additional objects in the
            cisco interface.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.RFC1213_MIB.RFC1213MIB.IfTable.IfEntry>`
            
            .. attribute:: locifhardtype
            
            	Returns the type of interface
            	**type**\: str
            
            	**status**\: obsolete
            
            .. attribute:: lociflineprot
            
            	Boolean whether interface line protocol is up or not
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: lociflastin
            
            	Elapsed time in milliseconds since last line protocol input packet was received
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: lociflastout
            
            	Elapsed time in milliseconds since last line protocol output packet was transmitted
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: lociflastouthang
            
            	Elapsed time in milliseconds since last line protocol output packet could not be successfully transmitted
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: locifinbitssec
            
            	Five minute exponentially\-decayed moving average of input bits per second
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: locifinpktssec
            
            	Five minute exponentially\-decayed moving average of input packets per second
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: locifoutbitssec
            
            	Five minute exponentially\-decayed moving average of output bits per second
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: locifoutpktssec
            
            	Five minute exponentially\-decayed moving average of output packets per second
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: locifinrunts
            
            	Number of packets input which were smaller then the allowable physical media permitted
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: locifingiants
            
            	Number of input packets which were larger then the physical media permitted
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: locifincrc
            
            	Number of input packets which had cyclic redundancy checksum errors
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: locifinframe
            
            	Number of input packet which were misaligned
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: locifinoverrun
            
            	Count of input which arrived too quickly for the to hardware receive
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: locifinignored
            
            	Number of input packets which were simply ignored by this interface
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: locifinabort
            
            	Number of input packets which were aborted
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: locifresets
            
            	Number of times the interface internally reset
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: locifrestarts
            
            	Number of times interface needed to be completely restarted
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: locifkeep
            
            	Boolean whether keepalives are enabled on this interface
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: locifreason
            
            	Reason for interface last status change
            	**type**\: str
            
            	**status**\: obsolete
            
            .. attribute:: locifcartrans
            
            	Number of times interface saw the carrier signal transition
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: locifreliab
            
            	The reliability of the interface. Used by IGRP
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: locifdelay
            
            	The amount of delay in microseconds of the interface. Used by IGRP
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: locifload
            
            	The loading factor of the interface. Used by IGRP
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: locifcollisions
            
            	The number of output collisions detected on this interface
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: locifinputqueuedrops
            
            	The number of packets dropped because the input queue was full
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: locifoutputqueuedrops
            
            	The number of packets dropped because the output queue was full
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: locifdescr
            
            	User configurable interface description
            	**type**\: str
            
            	**status**\: obsolete
            
            .. attribute:: locifslowinpkts
            
            	Packet count for Inbound traffic routed with slow switching
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifslowoutpkts
            
            	Packet count for Outbound traffic routed with slow switching
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifslowinoctets
            
            	Octet count for Inbound traffic routed with slow switching
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifslowoutoctets
            
            	Octet count for Outbound traffic routed with slow switching
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: lociffastinpkts
            
            	Packet count for Inbound traffic routed with fast switching
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: lociffastoutpkts
            
            	Packet count for Outbound traffic routed with fast switching
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: lociffastinoctets
            
            	Octet count for Inbound traffic routed with fast switching
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: lociffastoutoctets
            
            	Octet count for Outbound traffic routed with fast switching
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifotherinpkts
            
            	Other protocol input packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifotheroutpkts
            
            	Other protocol output packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifotherinoctets
            
            	Other protocol input octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifotheroutoctets
            
            	Other protocol output octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifipinpkts
            
            	ip protocol input packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifipoutpkts
            
            	ip protocol output packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifipinoctets
            
            	ip protocol input octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifipoutoctets
            
            	ip protocol output octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifdecnetinpkts
            
            	Decnet protocol input packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifdecnetoutpkts
            
            	Decnet protocol output packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifdecnetinoctets
            
            	Decnet protocol input byte count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifdecnetoutoctets
            
            	Decnet protocol output byte count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifxnsinpkts
            
            	XNS protocol input packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifxnsoutpkts
            
            	XNS protocol output packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifxnsinoctets
            
            	XNS protocol input byte count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifxnsoutoctets
            
            	XNS protocol output byte count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifclnsinpkts
            
            	CLNS protocol input packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifclnsoutpkts
            
            	CLNS protocol output packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifclnsinoctets
            
            	CLNS protocol input byte count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifclnsoutoctets
            
            	CLNS protocol output byte count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifappletalkinpkts
            
            	Appletalk protocol input packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifappletalkoutpkts
            
            	Appletalk protocol output packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifappletalkinoctets
            
            	Appletalk protocol input octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifappletalkoutoctets
            
            	Appletalk protocol output octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifnovellinpkts
            
            	Novell protocol input packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifnovelloutpkts
            
            	Novell protocol output packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifnovellinoctets
            
            	Novell protocol input octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifnovelloutoctets
            
            	Novell protocol output octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifapolloinpkts
            
            	Apollo protocol input packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifapollooutpkts
            
            	Apollo protocol output packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifapolloinoctets
            
            	Apollo protocol input octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifapollooutoctets
            
            	Apollo protocol output octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifvinesinpkts
            
            	Vines protocol input packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifvinesoutpkts
            
            	Vines protocol output packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifvinesinoctets
            
            	Vines protocol input octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifvinesoutoctets
            
            	Vines protocol output octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifbridgedinpkts
            
            	Bridged protocol input packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifbridgedoutpkts
            
            	Bridged protocol output packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifbridgedinoctets
            
            	Bridged protocol input octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifbridgedoutoctets
            
            	Bridged protocol output octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifsrbinpkts
            
            	SRB protocol input packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifsrboutpkts
            
            	SRB protocol output packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifsrbinoctets
            
            	SRB protocol input octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifsrboutoctets
            
            	SRB protocol output octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifchaosinpkts
            
            	Choas protocol input packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifchaosoutpkts
            
            	Choas protocol output packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifchaosinoctets
            
            	Choas protocol input octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifchaosoutoctets
            
            	Choas protocol output octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifpupinpkts
            
            	PUP protocol input packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifpupoutpkts
            
            	PUP protocol output packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifpupinoctets
            
            	PUP protocol input octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifpupoutoctets
            
            	PUP protocol output octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifmopinpkts
            
            	MOP protocol input packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifmopoutpkts
            
            	MOP protocol output packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifmopinoctets
            
            	MOP protocol input octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifmopoutoctets
            
            	MOP protocol output octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: lociflanmaninpkts
            
            	LanMan protocol input packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: lociflanmanoutpkts
            
            	LanMan protocol output packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: lociflanmaninoctets
            
            	LanMan protocol input octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: lociflanmanoutoctets
            
            	LanMan protocol output octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifstuninpkts
            
            	STUN protocol input packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifstunoutpkts
            
            	STUN protocol output packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifstuninoctets
            
            	STUN protocol input octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifstunoutoctets
            
            	STUN protocol output octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifspaninpkts
            
            	Spanning tree input protocol packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifspanoutpkts
            
            	Spanning tree output protocol packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifspaninoctets
            
            	Spanning tree input octet packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifspanoutoctets
            
            	Spanning tree output octet packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifarpinpkts
            
            	Arp protocol input packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifarpoutpkts
            
            	Arp protocol output packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifarpinoctets
            
            	Arp protocol input octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifarpoutoctets
            
            	Arp protocol output octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifprobeinpkts
            
            	Probe protocol input packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifprobeoutpkts
            
            	Probe protocol output packet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifprobeinoctets
            
            	Probe protocol input octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifprobeoutoctets
            
            	Probe protocol output octet count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: locifdribbleinputs
            
            	The number of good packets received with the dribble condition present
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'OLD-CISCO-INTERFACES-MIB'

            def __init__(self):
                super(OLDCISCOINTERFACESMIB.LifTable.LifEntry, self).__init__()

                self.yang_name = "lifEntry"
                self.yang_parent_name = "lifTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('locifhardtype', (YLeaf(YType.str, 'locIfHardType'), ['str'])),
                    ('lociflineprot', (YLeaf(YType.int32, 'locIfLineProt'), ['int'])),
                    ('lociflastin', (YLeaf(YType.int32, 'locIfLastIn'), ['int'])),
                    ('lociflastout', (YLeaf(YType.int32, 'locIfLastOut'), ['int'])),
                    ('lociflastouthang', (YLeaf(YType.int32, 'locIfLastOutHang'), ['int'])),
                    ('locifinbitssec', (YLeaf(YType.int32, 'locIfInBitsSec'), ['int'])),
                    ('locifinpktssec', (YLeaf(YType.int32, 'locIfInPktsSec'), ['int'])),
                    ('locifoutbitssec', (YLeaf(YType.int32, 'locIfOutBitsSec'), ['int'])),
                    ('locifoutpktssec', (YLeaf(YType.int32, 'locIfOutPktsSec'), ['int'])),
                    ('locifinrunts', (YLeaf(YType.int32, 'locIfInRunts'), ['int'])),
                    ('locifingiants', (YLeaf(YType.int32, 'locIfInGiants'), ['int'])),
                    ('locifincrc', (YLeaf(YType.int32, 'locIfInCRC'), ['int'])),
                    ('locifinframe', (YLeaf(YType.int32, 'locIfInFrame'), ['int'])),
                    ('locifinoverrun', (YLeaf(YType.int32, 'locIfInOverrun'), ['int'])),
                    ('locifinignored', (YLeaf(YType.int32, 'locIfInIgnored'), ['int'])),
                    ('locifinabort', (YLeaf(YType.int32, 'locIfInAbort'), ['int'])),
                    ('locifresets', (YLeaf(YType.int32, 'locIfResets'), ['int'])),
                    ('locifrestarts', (YLeaf(YType.int32, 'locIfRestarts'), ['int'])),
                    ('locifkeep', (YLeaf(YType.int32, 'locIfKeep'), ['int'])),
                    ('locifreason', (YLeaf(YType.str, 'locIfReason'), ['str'])),
                    ('locifcartrans', (YLeaf(YType.int32, 'locIfCarTrans'), ['int'])),
                    ('locifreliab', (YLeaf(YType.int32, 'locIfReliab'), ['int'])),
                    ('locifdelay', (YLeaf(YType.int32, 'locIfDelay'), ['int'])),
                    ('locifload', (YLeaf(YType.int32, 'locIfLoad'), ['int'])),
                    ('locifcollisions', (YLeaf(YType.int32, 'locIfCollisions'), ['int'])),
                    ('locifinputqueuedrops', (YLeaf(YType.int32, 'locIfInputQueueDrops'), ['int'])),
                    ('locifoutputqueuedrops', (YLeaf(YType.int32, 'locIfOutputQueueDrops'), ['int'])),
                    ('locifdescr', (YLeaf(YType.str, 'locIfDescr'), ['str'])),
                    ('locifslowinpkts', (YLeaf(YType.uint32, 'locIfSlowInPkts'), ['int'])),
                    ('locifslowoutpkts', (YLeaf(YType.uint32, 'locIfSlowOutPkts'), ['int'])),
                    ('locifslowinoctets', (YLeaf(YType.uint32, 'locIfSlowInOctets'), ['int'])),
                    ('locifslowoutoctets', (YLeaf(YType.uint32, 'locIfSlowOutOctets'), ['int'])),
                    ('lociffastinpkts', (YLeaf(YType.uint32, 'locIfFastInPkts'), ['int'])),
                    ('lociffastoutpkts', (YLeaf(YType.uint32, 'locIfFastOutPkts'), ['int'])),
                    ('lociffastinoctets', (YLeaf(YType.uint32, 'locIfFastInOctets'), ['int'])),
                    ('lociffastoutoctets', (YLeaf(YType.uint32, 'locIfFastOutOctets'), ['int'])),
                    ('locifotherinpkts', (YLeaf(YType.uint32, 'locIfotherInPkts'), ['int'])),
                    ('locifotheroutpkts', (YLeaf(YType.uint32, 'locIfotherOutPkts'), ['int'])),
                    ('locifotherinoctets', (YLeaf(YType.uint32, 'locIfotherInOctets'), ['int'])),
                    ('locifotheroutoctets', (YLeaf(YType.uint32, 'locIfotherOutOctets'), ['int'])),
                    ('locifipinpkts', (YLeaf(YType.uint32, 'locIfipInPkts'), ['int'])),
                    ('locifipoutpkts', (YLeaf(YType.uint32, 'locIfipOutPkts'), ['int'])),
                    ('locifipinoctets', (YLeaf(YType.uint32, 'locIfipInOctets'), ['int'])),
                    ('locifipoutoctets', (YLeaf(YType.uint32, 'locIfipOutOctets'), ['int'])),
                    ('locifdecnetinpkts', (YLeaf(YType.uint32, 'locIfdecnetInPkts'), ['int'])),
                    ('locifdecnetoutpkts', (YLeaf(YType.uint32, 'locIfdecnetOutPkts'), ['int'])),
                    ('locifdecnetinoctets', (YLeaf(YType.uint32, 'locIfdecnetInOctets'), ['int'])),
                    ('locifdecnetoutoctets', (YLeaf(YType.uint32, 'locIfdecnetOutOctets'), ['int'])),
                    ('locifxnsinpkts', (YLeaf(YType.uint32, 'locIfxnsInPkts'), ['int'])),
                    ('locifxnsoutpkts', (YLeaf(YType.uint32, 'locIfxnsOutPkts'), ['int'])),
                    ('locifxnsinoctets', (YLeaf(YType.uint32, 'locIfxnsInOctets'), ['int'])),
                    ('locifxnsoutoctets', (YLeaf(YType.uint32, 'locIfxnsOutOctets'), ['int'])),
                    ('locifclnsinpkts', (YLeaf(YType.uint32, 'locIfclnsInPkts'), ['int'])),
                    ('locifclnsoutpkts', (YLeaf(YType.uint32, 'locIfclnsOutPkts'), ['int'])),
                    ('locifclnsinoctets', (YLeaf(YType.uint32, 'locIfclnsInOctets'), ['int'])),
                    ('locifclnsoutoctets', (YLeaf(YType.uint32, 'locIfclnsOutOctets'), ['int'])),
                    ('locifappletalkinpkts', (YLeaf(YType.uint32, 'locIfappletalkInPkts'), ['int'])),
                    ('locifappletalkoutpkts', (YLeaf(YType.uint32, 'locIfappletalkOutPkts'), ['int'])),
                    ('locifappletalkinoctets', (YLeaf(YType.uint32, 'locIfappletalkInOctets'), ['int'])),
                    ('locifappletalkoutoctets', (YLeaf(YType.uint32, 'locIfappletalkOutOctets'), ['int'])),
                    ('locifnovellinpkts', (YLeaf(YType.uint32, 'locIfnovellInPkts'), ['int'])),
                    ('locifnovelloutpkts', (YLeaf(YType.uint32, 'locIfnovellOutPkts'), ['int'])),
                    ('locifnovellinoctets', (YLeaf(YType.uint32, 'locIfnovellInOctets'), ['int'])),
                    ('locifnovelloutoctets', (YLeaf(YType.uint32, 'locIfnovellOutOctets'), ['int'])),
                    ('locifapolloinpkts', (YLeaf(YType.uint32, 'locIfapolloInPkts'), ['int'])),
                    ('locifapollooutpkts', (YLeaf(YType.uint32, 'locIfapolloOutPkts'), ['int'])),
                    ('locifapolloinoctets', (YLeaf(YType.uint32, 'locIfapolloInOctets'), ['int'])),
                    ('locifapollooutoctets', (YLeaf(YType.uint32, 'locIfapolloOutOctets'), ['int'])),
                    ('locifvinesinpkts', (YLeaf(YType.uint32, 'locIfvinesInPkts'), ['int'])),
                    ('locifvinesoutpkts', (YLeaf(YType.uint32, 'locIfvinesOutPkts'), ['int'])),
                    ('locifvinesinoctets', (YLeaf(YType.uint32, 'locIfvinesInOctets'), ['int'])),
                    ('locifvinesoutoctets', (YLeaf(YType.uint32, 'locIfvinesOutOctets'), ['int'])),
                    ('locifbridgedinpkts', (YLeaf(YType.uint32, 'locIfbridgedInPkts'), ['int'])),
                    ('locifbridgedoutpkts', (YLeaf(YType.uint32, 'locIfbridgedOutPkts'), ['int'])),
                    ('locifbridgedinoctets', (YLeaf(YType.uint32, 'locIfbridgedInOctets'), ['int'])),
                    ('locifbridgedoutoctets', (YLeaf(YType.uint32, 'locIfbridgedOutOctets'), ['int'])),
                    ('locifsrbinpkts', (YLeaf(YType.uint32, 'locIfsrbInPkts'), ['int'])),
                    ('locifsrboutpkts', (YLeaf(YType.uint32, 'locIfsrbOutPkts'), ['int'])),
                    ('locifsrbinoctets', (YLeaf(YType.uint32, 'locIfsrbInOctets'), ['int'])),
                    ('locifsrboutoctets', (YLeaf(YType.uint32, 'locIfsrbOutOctets'), ['int'])),
                    ('locifchaosinpkts', (YLeaf(YType.uint32, 'locIfchaosInPkts'), ['int'])),
                    ('locifchaosoutpkts', (YLeaf(YType.uint32, 'locIfchaosOutPkts'), ['int'])),
                    ('locifchaosinoctets', (YLeaf(YType.uint32, 'locIfchaosInOctets'), ['int'])),
                    ('locifchaosoutoctets', (YLeaf(YType.uint32, 'locIfchaosOutOctets'), ['int'])),
                    ('locifpupinpkts', (YLeaf(YType.uint32, 'locIfpupInPkts'), ['int'])),
                    ('locifpupoutpkts', (YLeaf(YType.uint32, 'locIfpupOutPkts'), ['int'])),
                    ('locifpupinoctets', (YLeaf(YType.uint32, 'locIfpupInOctets'), ['int'])),
                    ('locifpupoutoctets', (YLeaf(YType.uint32, 'locIfpupOutOctets'), ['int'])),
                    ('locifmopinpkts', (YLeaf(YType.uint32, 'locIfmopInPkts'), ['int'])),
                    ('locifmopoutpkts', (YLeaf(YType.uint32, 'locIfmopOutPkts'), ['int'])),
                    ('locifmopinoctets', (YLeaf(YType.uint32, 'locIfmopInOctets'), ['int'])),
                    ('locifmopoutoctets', (YLeaf(YType.uint32, 'locIfmopOutOctets'), ['int'])),
                    ('lociflanmaninpkts', (YLeaf(YType.uint32, 'locIflanmanInPkts'), ['int'])),
                    ('lociflanmanoutpkts', (YLeaf(YType.uint32, 'locIflanmanOutPkts'), ['int'])),
                    ('lociflanmaninoctets', (YLeaf(YType.uint32, 'locIflanmanInOctets'), ['int'])),
                    ('lociflanmanoutoctets', (YLeaf(YType.uint32, 'locIflanmanOutOctets'), ['int'])),
                    ('locifstuninpkts', (YLeaf(YType.uint32, 'locIfstunInPkts'), ['int'])),
                    ('locifstunoutpkts', (YLeaf(YType.uint32, 'locIfstunOutPkts'), ['int'])),
                    ('locifstuninoctets', (YLeaf(YType.uint32, 'locIfstunInOctets'), ['int'])),
                    ('locifstunoutoctets', (YLeaf(YType.uint32, 'locIfstunOutOctets'), ['int'])),
                    ('locifspaninpkts', (YLeaf(YType.uint32, 'locIfspanInPkts'), ['int'])),
                    ('locifspanoutpkts', (YLeaf(YType.uint32, 'locIfspanOutPkts'), ['int'])),
                    ('locifspaninoctets', (YLeaf(YType.uint32, 'locIfspanInOctets'), ['int'])),
                    ('locifspanoutoctets', (YLeaf(YType.uint32, 'locIfspanOutOctets'), ['int'])),
                    ('locifarpinpkts', (YLeaf(YType.uint32, 'locIfarpInPkts'), ['int'])),
                    ('locifarpoutpkts', (YLeaf(YType.uint32, 'locIfarpOutPkts'), ['int'])),
                    ('locifarpinoctets', (YLeaf(YType.uint32, 'locIfarpInOctets'), ['int'])),
                    ('locifarpoutoctets', (YLeaf(YType.uint32, 'locIfarpOutOctets'), ['int'])),
                    ('locifprobeinpkts', (YLeaf(YType.uint32, 'locIfprobeInPkts'), ['int'])),
                    ('locifprobeoutpkts', (YLeaf(YType.uint32, 'locIfprobeOutPkts'), ['int'])),
                    ('locifprobeinoctets', (YLeaf(YType.uint32, 'locIfprobeInOctets'), ['int'])),
                    ('locifprobeoutoctets', (YLeaf(YType.uint32, 'locIfprobeOutOctets'), ['int'])),
                    ('locifdribbleinputs', (YLeaf(YType.uint32, 'locIfDribbleInputs'), ['int'])),
                ])
                self.ifindex = None
                self.locifhardtype = None
                self.lociflineprot = None
                self.lociflastin = None
                self.lociflastout = None
                self.lociflastouthang = None
                self.locifinbitssec = None
                self.locifinpktssec = None
                self.locifoutbitssec = None
                self.locifoutpktssec = None
                self.locifinrunts = None
                self.locifingiants = None
                self.locifincrc = None
                self.locifinframe = None
                self.locifinoverrun = None
                self.locifinignored = None
                self.locifinabort = None
                self.locifresets = None
                self.locifrestarts = None
                self.locifkeep = None
                self.locifreason = None
                self.locifcartrans = None
                self.locifreliab = None
                self.locifdelay = None
                self.locifload = None
                self.locifcollisions = None
                self.locifinputqueuedrops = None
                self.locifoutputqueuedrops = None
                self.locifdescr = None
                self.locifslowinpkts = None
                self.locifslowoutpkts = None
                self.locifslowinoctets = None
                self.locifslowoutoctets = None
                self.lociffastinpkts = None
                self.lociffastoutpkts = None
                self.lociffastinoctets = None
                self.lociffastoutoctets = None
                self.locifotherinpkts = None
                self.locifotheroutpkts = None
                self.locifotherinoctets = None
                self.locifotheroutoctets = None
                self.locifipinpkts = None
                self.locifipoutpkts = None
                self.locifipinoctets = None
                self.locifipoutoctets = None
                self.locifdecnetinpkts = None
                self.locifdecnetoutpkts = None
                self.locifdecnetinoctets = None
                self.locifdecnetoutoctets = None
                self.locifxnsinpkts = None
                self.locifxnsoutpkts = None
                self.locifxnsinoctets = None
                self.locifxnsoutoctets = None
                self.locifclnsinpkts = None
                self.locifclnsoutpkts = None
                self.locifclnsinoctets = None
                self.locifclnsoutoctets = None
                self.locifappletalkinpkts = None
                self.locifappletalkoutpkts = None
                self.locifappletalkinoctets = None
                self.locifappletalkoutoctets = None
                self.locifnovellinpkts = None
                self.locifnovelloutpkts = None
                self.locifnovellinoctets = None
                self.locifnovelloutoctets = None
                self.locifapolloinpkts = None
                self.locifapollooutpkts = None
                self.locifapolloinoctets = None
                self.locifapollooutoctets = None
                self.locifvinesinpkts = None
                self.locifvinesoutpkts = None
                self.locifvinesinoctets = None
                self.locifvinesoutoctets = None
                self.locifbridgedinpkts = None
                self.locifbridgedoutpkts = None
                self.locifbridgedinoctets = None
                self.locifbridgedoutoctets = None
                self.locifsrbinpkts = None
                self.locifsrboutpkts = None
                self.locifsrbinoctets = None
                self.locifsrboutoctets = None
                self.locifchaosinpkts = None
                self.locifchaosoutpkts = None
                self.locifchaosinoctets = None
                self.locifchaosoutoctets = None
                self.locifpupinpkts = None
                self.locifpupoutpkts = None
                self.locifpupinoctets = None
                self.locifpupoutoctets = None
                self.locifmopinpkts = None
                self.locifmopoutpkts = None
                self.locifmopinoctets = None
                self.locifmopoutoctets = None
                self.lociflanmaninpkts = None
                self.lociflanmanoutpkts = None
                self.lociflanmaninoctets = None
                self.lociflanmanoutoctets = None
                self.locifstuninpkts = None
                self.locifstunoutpkts = None
                self.locifstuninoctets = None
                self.locifstunoutoctets = None
                self.locifspaninpkts = None
                self.locifspanoutpkts = None
                self.locifspaninoctets = None
                self.locifspanoutoctets = None
                self.locifarpinpkts = None
                self.locifarpoutpkts = None
                self.locifarpinoctets = None
                self.locifarpoutoctets = None
                self.locifprobeinpkts = None
                self.locifprobeoutpkts = None
                self.locifprobeinoctets = None
                self.locifprobeoutoctets = None
                self.locifdribbleinputs = None
                self._segment_path = lambda: "lifEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "OLD-CISCO-INTERFACES-MIB:OLD-CISCO-INTERFACES-MIB/lifTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OLDCISCOINTERFACESMIB.LifTable.LifEntry, ['ifindex', 'locifhardtype', 'lociflineprot', 'lociflastin', 'lociflastout', 'lociflastouthang', 'locifinbitssec', 'locifinpktssec', 'locifoutbitssec', 'locifoutpktssec', 'locifinrunts', 'locifingiants', 'locifincrc', 'locifinframe', 'locifinoverrun', 'locifinignored', 'locifinabort', 'locifresets', 'locifrestarts', 'locifkeep', 'locifreason', 'locifcartrans', 'locifreliab', 'locifdelay', 'locifload', 'locifcollisions', 'locifinputqueuedrops', 'locifoutputqueuedrops', 'locifdescr', 'locifslowinpkts', 'locifslowoutpkts', 'locifslowinoctets', 'locifslowoutoctets', 'lociffastinpkts', 'lociffastoutpkts', 'lociffastinoctets', 'lociffastoutoctets', 'locifotherinpkts', 'locifotheroutpkts', 'locifotherinoctets', 'locifotheroutoctets', 'locifipinpkts', 'locifipoutpkts', 'locifipinoctets', 'locifipoutoctets', 'locifdecnetinpkts', 'locifdecnetoutpkts', 'locifdecnetinoctets', 'locifdecnetoutoctets', 'locifxnsinpkts', 'locifxnsoutpkts', 'locifxnsinoctets', 'locifxnsoutoctets', 'locifclnsinpkts', 'locifclnsoutpkts', 'locifclnsinoctets', 'locifclnsoutoctets', 'locifappletalkinpkts', 'locifappletalkoutpkts', 'locifappletalkinoctets', 'locifappletalkoutoctets', 'locifnovellinpkts', 'locifnovelloutpkts', 'locifnovellinoctets', 'locifnovelloutoctets', 'locifapolloinpkts', 'locifapollooutpkts', 'locifapolloinoctets', 'locifapollooutoctets', 'locifvinesinpkts', 'locifvinesoutpkts', 'locifvinesinoctets', 'locifvinesoutoctets', 'locifbridgedinpkts', 'locifbridgedoutpkts', 'locifbridgedinoctets', 'locifbridgedoutoctets', 'locifsrbinpkts', 'locifsrboutpkts', 'locifsrbinoctets', 'locifsrboutoctets', 'locifchaosinpkts', 'locifchaosoutpkts', 'locifchaosinoctets', 'locifchaosoutoctets', 'locifpupinpkts', 'locifpupoutpkts', 'locifpupinoctets', 'locifpupoutoctets', 'locifmopinpkts', 'locifmopoutpkts', 'locifmopinoctets', 'locifmopoutoctets', 'lociflanmaninpkts', 'lociflanmanoutpkts', 'lociflanmaninoctets', 'lociflanmanoutoctets', 'locifstuninpkts', 'locifstunoutpkts', 'locifstuninoctets', 'locifstunoutoctets', 'locifspaninpkts', 'locifspanoutpkts', 'locifspaninoctets', 'locifspanoutoctets', 'locifarpinpkts', 'locifarpoutpkts', 'locifarpinoctets', 'locifarpoutoctets', 'locifprobeinpkts', 'locifprobeoutpkts', 'locifprobeinoctets', 'locifprobeoutoctets', 'locifdribbleinputs'], name, value)


    class LFSIPTable(Entity):
        """
        A list of card entries for 4T, HSSI,
        Mx serial or FSIP.
        
        .. attribute:: lfsipentry
        
        	A collection of objects specific to 4T, HSSI, Mx serial or FSIP
        	**type**\: list of  		 :py:class:`LFSIPEntry <ydk.models.cisco_ios_xe.OLD_CISCO_INTERFACES_MIB.OLDCISCOINTERFACESMIB.LFSIPTable.LFSIPEntry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'OLD-CISCO-INTERFACES-MIB'

        def __init__(self):
            super(OLDCISCOINTERFACESMIB.LFSIPTable, self).__init__()

            self.yang_name = "lFSIPTable"
            self.yang_parent_name = "OLD-CISCO-INTERFACES-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("lFSIPEntry", ("lfsipentry", OLDCISCOINTERFACESMIB.LFSIPTable.LFSIPEntry))])
            self._leafs = OrderedDict()

            self.lfsipentry = YList(self)
            self._segment_path = lambda: "lFSIPTable"
            self._absolute_path = lambda: "OLD-CISCO-INTERFACES-MIB:OLD-CISCO-INTERFACES-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OLDCISCOINTERFACESMIB.LFSIPTable, [], name, value)


        class LFSIPEntry(Entity):
            """
            A collection of objects specific to 4T,
            HSSI, Mx serial or FSIP.
            
            .. attribute:: lociffsipindex  (key)
            
            	Interface index of this card corresponding to its ifIndex
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: lociffsiptype
            
            	Is this FSIP line DCE or DTE
            	**type**\:  :py:class:`LocIfFSIPtype <ydk.models.cisco_ios_xe.OLD_CISCO_INTERFACES_MIB.OLDCISCOINTERFACESMIB.LFSIPTable.LFSIPEntry.LocIfFSIPtype>`
            
            	**status**\: obsolete
            
            .. attribute:: lociffsiprts
            
            	Is the RTS signal up or down
            	**type**\:  :py:class:`LocIfFSIPrts <ydk.models.cisco_ios_xe.OLD_CISCO_INTERFACES_MIB.OLDCISCOINTERFACESMIB.LFSIPTable.LFSIPEntry.LocIfFSIPrts>`
            
            	**status**\: obsolete
            
            .. attribute:: lociffsipcts
            
            	Is the CTS signal up or down
            	**type**\:  :py:class:`LocIfFSIPcts <ydk.models.cisco_ios_xe.OLD_CISCO_INTERFACES_MIB.OLDCISCOINTERFACESMIB.LFSIPTable.LFSIPEntry.LocIfFSIPcts>`
            
            	**status**\: obsolete
            
            .. attribute:: lociffsipdtr
            
            	Is the DTR signal up or down
            	**type**\:  :py:class:`LocIfFSIPdtr <ydk.models.cisco_ios_xe.OLD_CISCO_INTERFACES_MIB.OLDCISCOINTERFACESMIB.LFSIPTable.LFSIPEntry.LocIfFSIPdtr>`
            
            	**status**\: obsolete
            
            .. attribute:: lociffsipdcd
            
            	Is the DCD signal up or down
            	**type**\:  :py:class:`LocIfFSIPdcd <ydk.models.cisco_ios_xe.OLD_CISCO_INTERFACES_MIB.OLDCISCOINTERFACESMIB.LFSIPTable.LFSIPEntry.LocIfFSIPdcd>`
            
            	**status**\: obsolete
            
            .. attribute:: lociffsipdsr
            
            	Is the DSR signal up or down
            	**type**\:  :py:class:`LocIfFSIPdsr <ydk.models.cisco_ios_xe.OLD_CISCO_INTERFACES_MIB.OLDCISCOINTERFACESMIB.LFSIPTable.LFSIPEntry.LocIfFSIPdsr>`
            
            	**status**\: obsolete
            
            .. attribute:: lociffsiprxclockrate
            
            	Received clock rate
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: lociffsiprxclockratehi
            
            	Use when received clock rate  is greater than 2^32 (gigabits)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: lociffsipporttype
            
            	Cable Type of 4T, HSSI, Mx serial or FSIP
            	**type**\:  :py:class:`LocIfFSIPportType <ydk.models.cisco_ios_xe.OLD_CISCO_INTERFACES_MIB.OLDCISCOINTERFACESMIB.LFSIPTable.LFSIPEntry.LocIfFSIPportType>`
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'OLD-CISCO-INTERFACES-MIB'

            def __init__(self):
                super(OLDCISCOINTERFACESMIB.LFSIPTable.LFSIPEntry, self).__init__()

                self.yang_name = "lFSIPEntry"
                self.yang_parent_name = "lFSIPTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['lociffsipindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('lociffsipindex', (YLeaf(YType.int32, 'locIfFSIPIndex'), ['int'])),
                    ('lociffsiptype', (YLeaf(YType.enumeration, 'locIfFSIPtype'), [('ydk.models.cisco_ios_xe.OLD_CISCO_INTERFACES_MIB', 'OLDCISCOINTERFACESMIB', 'LFSIPTable.LFSIPEntry.LocIfFSIPtype')])),
                    ('lociffsiprts', (YLeaf(YType.enumeration, 'locIfFSIPrts'), [('ydk.models.cisco_ios_xe.OLD_CISCO_INTERFACES_MIB', 'OLDCISCOINTERFACESMIB', 'LFSIPTable.LFSIPEntry.LocIfFSIPrts')])),
                    ('lociffsipcts', (YLeaf(YType.enumeration, 'locIfFSIPcts'), [('ydk.models.cisco_ios_xe.OLD_CISCO_INTERFACES_MIB', 'OLDCISCOINTERFACESMIB', 'LFSIPTable.LFSIPEntry.LocIfFSIPcts')])),
                    ('lociffsipdtr', (YLeaf(YType.enumeration, 'locIfFSIPdtr'), [('ydk.models.cisco_ios_xe.OLD_CISCO_INTERFACES_MIB', 'OLDCISCOINTERFACESMIB', 'LFSIPTable.LFSIPEntry.LocIfFSIPdtr')])),
                    ('lociffsipdcd', (YLeaf(YType.enumeration, 'locIfFSIPdcd'), [('ydk.models.cisco_ios_xe.OLD_CISCO_INTERFACES_MIB', 'OLDCISCOINTERFACESMIB', 'LFSIPTable.LFSIPEntry.LocIfFSIPdcd')])),
                    ('lociffsipdsr', (YLeaf(YType.enumeration, 'locIfFSIPdsr'), [('ydk.models.cisco_ios_xe.OLD_CISCO_INTERFACES_MIB', 'OLDCISCOINTERFACESMIB', 'LFSIPTable.LFSIPEntry.LocIfFSIPdsr')])),
                    ('lociffsiprxclockrate', (YLeaf(YType.int32, 'locIfFSIPrxClockrate'), ['int'])),
                    ('lociffsiprxclockratehi', (YLeaf(YType.int32, 'locIfFSIPrxClockrateHi'), ['int'])),
                    ('lociffsipporttype', (YLeaf(YType.enumeration, 'locIfFSIPportType'), [('ydk.models.cisco_ios_xe.OLD_CISCO_INTERFACES_MIB', 'OLDCISCOINTERFACESMIB', 'LFSIPTable.LFSIPEntry.LocIfFSIPportType')])),
                ])
                self.lociffsipindex = None
                self.lociffsiptype = None
                self.lociffsiprts = None
                self.lociffsipcts = None
                self.lociffsipdtr = None
                self.lociffsipdcd = None
                self.lociffsipdsr = None
                self.lociffsiprxclockrate = None
                self.lociffsiprxclockratehi = None
                self.lociffsipporttype = None
                self._segment_path = lambda: "lFSIPEntry" + "[locIfFSIPIndex='" + str(self.lociffsipindex) + "']"
                self._absolute_path = lambda: "OLD-CISCO-INTERFACES-MIB:OLD-CISCO-INTERFACES-MIB/lFSIPTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OLDCISCOINTERFACESMIB.LFSIPTable.LFSIPEntry, ['lociffsipindex', 'lociffsiptype', 'lociffsiprts', 'lociffsipcts', 'lociffsipdtr', 'lociffsipdcd', 'lociffsipdsr', 'lociffsiprxclockrate', 'lociffsiprxclockratehi', 'lociffsipporttype'], name, value)

            class LocIfFSIPcts(Enum):
                """
                LocIfFSIPcts (Enum Class)

                Is the CTS signal up or down

                .. data:: notAvailable = 1

                .. data:: up = 2

                .. data:: down = 3

                """

                notAvailable = Enum.YLeaf(1, "notAvailable")

                up = Enum.YLeaf(2, "up")

                down = Enum.YLeaf(3, "down")


            class LocIfFSIPdcd(Enum):
                """
                LocIfFSIPdcd (Enum Class)

                Is the DCD signal up or down

                .. data:: notAvailable = 1

                .. data:: up = 2

                .. data:: down = 3

                """

                notAvailable = Enum.YLeaf(1, "notAvailable")

                up = Enum.YLeaf(2, "up")

                down = Enum.YLeaf(3, "down")


            class LocIfFSIPdsr(Enum):
                """
                LocIfFSIPdsr (Enum Class)

                Is the DSR signal up or down

                .. data:: notAvailable = 1

                .. data:: up = 2

                .. data:: down = 3

                """

                notAvailable = Enum.YLeaf(1, "notAvailable")

                up = Enum.YLeaf(2, "up")

                down = Enum.YLeaf(3, "down")


            class LocIfFSIPdtr(Enum):
                """
                LocIfFSIPdtr (Enum Class)

                Is the DTR signal up or down

                .. data:: notAvailable = 1

                .. data:: up = 2

                .. data:: down = 3

                """

                notAvailable = Enum.YLeaf(1, "notAvailable")

                up = Enum.YLeaf(2, "up")

                down = Enum.YLeaf(3, "down")


            class LocIfFSIPportType(Enum):
                """
                LocIfFSIPportType (Enum Class)

                Cable Type of 4T, HSSI, Mx serial or FSIP

                .. data:: noCable = 1

                .. data:: rs232 = 2

                .. data:: rs422 = 3

                .. data:: rs423 = 4

                .. data:: v35 = 5

                .. data:: x21 = 6

                .. data:: rs449 = 7

                .. data:: rs530 = 8

                .. data:: hssi = 9

                .. data:: g703unbal = 10

                .. data:: g703bal = 11

                .. data:: jt2unbal = 12

                """

                noCable = Enum.YLeaf(1, "noCable")

                rs232 = Enum.YLeaf(2, "rs232")

                rs422 = Enum.YLeaf(3, "rs422")

                rs423 = Enum.YLeaf(4, "rs423")

                v35 = Enum.YLeaf(5, "v35")

                x21 = Enum.YLeaf(6, "x21")

                rs449 = Enum.YLeaf(7, "rs449")

                rs530 = Enum.YLeaf(8, "rs530")

                hssi = Enum.YLeaf(9, "hssi")

                g703unbal = Enum.YLeaf(10, "g703unbal")

                g703bal = Enum.YLeaf(11, "g703bal")

                jt2unbal = Enum.YLeaf(12, "jt2unbal")


            class LocIfFSIPrts(Enum):
                """
                LocIfFSIPrts (Enum Class)

                Is the RTS signal up or down

                .. data:: notAvailable = 1

                .. data:: up = 2

                .. data:: down = 3

                """

                notAvailable = Enum.YLeaf(1, "notAvailable")

                up = Enum.YLeaf(2, "up")

                down = Enum.YLeaf(3, "down")


            class LocIfFSIPtype(Enum):
                """
                LocIfFSIPtype (Enum Class)

                Is this FSIP line DCE or DTE

                .. data:: notAvailable = 1

                .. data:: dte = 2

                .. data:: dce = 3

                """

                notAvailable = Enum.YLeaf(1, "notAvailable")

                dte = Enum.YLeaf(2, "dte")

                dce = Enum.YLeaf(3, "dce")


    def clone_ptr(self):
        self._top_entity = OLDCISCOINTERFACESMIB()
        return self._top_entity


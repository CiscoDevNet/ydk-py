""" CISCO_ETHERLIKE_EXT_MIB 

The MIB module to describe generic objects for
ethernet\-like network interfaces. 

This MIB provides ethernet\-like network interfaces 
information that are either excluded by EtherLike\-MIB 
or specific to Cisco products.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOETHERLIKEEXTMIB(Entity):
    """
    
    
    .. attribute:: ceedot3pauseexttable
    
    	A list of additional descriptive and status information about the MAC Control PAUSE  function on the ethernet\-like interfaces  attached to a particular system, in extension to dot3PauseTable in EtherLike\-MIB. There will be  one row in this table for each ethernet\-like  interface in the system which supports the MAC  Control PAUSE function
    	**type**\:  :py:class:`CeeDot3PauseExtTable <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable>`
    
    .. attribute:: ceesubinterfacetable
    
    	This table provides the subinterface related information associated to the Ethernet\-like interfaces.  The subinterface is a division of one physical interface into multiple logical interfaces. As an example of what a typical subinterface setup might look like on a device, a single Ethernet port such as GigabitEthernet0/0 would be subdivided into Gi0/0.1, Gi0/0.2, Gi0/0.3 and so on, each one performing as if it were a separate interface
    	**type**\:  :py:class:`CeeSubInterfaceTable <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CISCOETHERLIKEEXTMIB.CeeSubInterfaceTable>`
    
    

    """

    _prefix = 'CISCO-ETHERLIKE-EXT-MIB'
    _revision = '2010-06-04'

    def __init__(self):
        super(CISCOETHERLIKEEXTMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-ETHERLIKE-EXT-MIB"
        self.yang_parent_name = "CISCO-ETHERLIKE-EXT-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ceeDot3PauseExtTable", ("ceedot3pauseexttable", CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable)), ("ceeSubInterfaceTable", ("ceesubinterfacetable", CISCOETHERLIKEEXTMIB.CeeSubInterfaceTable))])
        self._leafs = OrderedDict()

        self.ceedot3pauseexttable = CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable()
        self.ceedot3pauseexttable.parent = self
        self._children_name_map["ceedot3pauseexttable"] = "ceeDot3PauseExtTable"

        self.ceesubinterfacetable = CISCOETHERLIKEEXTMIB.CeeSubInterfaceTable()
        self.ceesubinterfacetable.parent = self
        self._children_name_map["ceesubinterfacetable"] = "ceeSubInterfaceTable"
        self._segment_path = lambda: "CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOETHERLIKEEXTMIB, [], name, value)


    class CeeDot3PauseExtTable(Entity):
        """
        A list of additional descriptive and status
        information about the MAC Control PAUSE 
        function on the ethernet\-like interfaces 
        attached to a particular system, in extension to
        dot3PauseTable in EtherLike\-MIB. There will be 
        one row in this table for each ethernet\-like 
        interface in the system which supports the MAC 
        Control PAUSE function.
        
        .. attribute:: ceedot3pauseextentry
        
        	An entry in the table, containing additional information about the MAC Control PAUSE function  on a single ethernet\-like interface, in extension  to dot3PauseEntry in Etherlike\-MIB
        	**type**\: list of  		 :py:class:`CeeDot3PauseExtEntry <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable.CeeDot3PauseExtEntry>`
        
        

        """

        _prefix = 'CISCO-ETHERLIKE-EXT-MIB'
        _revision = '2010-06-04'

        def __init__(self):
            super(CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable, self).__init__()

            self.yang_name = "ceeDot3PauseExtTable"
            self.yang_parent_name = "CISCO-ETHERLIKE-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ceeDot3PauseExtEntry", ("ceedot3pauseextentry", CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable.CeeDot3PauseExtEntry))])
            self._leafs = OrderedDict()

            self.ceedot3pauseextentry = YList(self)
            self._segment_path = lambda: "ceeDot3PauseExtTable"
            self._absolute_path = lambda: "CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable, [], name, value)


        class CeeDot3PauseExtEntry(Entity):
            """
            An entry in the table, containing additional
            information about the MAC Control PAUSE function 
            on a single ethernet\-like interface, in extension 
            to dot3PauseEntry in Etherlike\-MIB.
            
            .. attribute:: dot3statsindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`dot3statsindex <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3StatsTable.Dot3StatsEntry>`
            
            .. attribute:: ceedot3pauseextadminmode
            
            	Indicates preference to send or process pause frames on this interface. txDesired(0)  \-  indicates preference to send pause                   frames, but autonegotiates flow                   control. This bit can only be                   turned on when the corresponding                   instance of dot3PauseAdminMode                   has the value of 'enabledXmit' or                   'enabledXmitAndRcv'. rxDesired(1)  \-  indicates preference to process                   pause frames, but autonegotiates                   flow control. This bit can only be                   turned on when the corresponding                   instance of dot3PauseAdminMode                   has the value of 'enabledRcv' or                   'enabledXmitAndRcv'
            	**type**\:  :py:class:`CeeDot3PauseExtAdminMode <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable.CeeDot3PauseExtEntry.CeeDot3PauseExtAdminMode>`
            
            .. attribute:: ceedot3pauseextopermode
            
            	Provides additional information about the flow control operational status on this interface. txDisagree(0) \- the transmit pause function on                  this interface is disabled due to                  disagreement from the far end on                  negotiation. rxDisagree(1) \- the receive pause function on                   this interface is disabled due to                  disagreement from the far end on                  negotiation. txDesired(2)  \- the transmit pause function on                  this interface is desired. rxDesired(3)  \- the receive pause function on                   this interface is desired
            	**type**\:  :py:class:`CeeDot3PauseExtOperMode <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable.CeeDot3PauseExtEntry.CeeDot3PauseExtOperMode>`
            
            

            """

            _prefix = 'CISCO-ETHERLIKE-EXT-MIB'
            _revision = '2010-06-04'

            def __init__(self):
                super(CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable.CeeDot3PauseExtEntry, self).__init__()

                self.yang_name = "ceeDot3PauseExtEntry"
                self.yang_parent_name = "ceeDot3PauseExtTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot3statsindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot3statsindex', (YLeaf(YType.str, 'dot3StatsIndex'), ['int'])),
                    ('ceedot3pauseextadminmode', (YLeaf(YType.bits, 'ceeDot3PauseExtAdminMode'), ['Bits'])),
                    ('ceedot3pauseextopermode', (YLeaf(YType.bits, 'ceeDot3PauseExtOperMode'), ['Bits'])),
                ])
                self.dot3statsindex = None
                self.ceedot3pauseextadminmode = Bits()
                self.ceedot3pauseextopermode = Bits()
                self._segment_path = lambda: "ceeDot3PauseExtEntry" + "[dot3StatsIndex='" + str(self.dot3statsindex) + "']"
                self._absolute_path = lambda: "CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB/ceeDot3PauseExtTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOETHERLIKEEXTMIB.CeeDot3PauseExtTable.CeeDot3PauseExtEntry, ['dot3statsindex', 'ceedot3pauseextadminmode', 'ceedot3pauseextopermode'], name, value)


    class CeeSubInterfaceTable(Entity):
        """
        This table provides the subinterface related information
        associated to the Ethernet\-like interfaces.
        
        The subinterface is a division of one physical interface into
        multiple logical interfaces. As an example of what a typical
        subinterface setup might look like on a device, a single
        Ethernet port such as GigabitEthernet0/0 would be subdivided
        into Gi0/0.1, Gi0/0.2, Gi0/0.3 and so on, each one performing as
        if it were a separate interface.
        
        .. attribute:: ceesubinterfaceentry
        
        	This table contains a row for each Ethernet\-like interface by it's ifTable ifIndex in the system, which supports the sub\-interface.  An entry is created by an agent, when it detects a Ethernet\-like interface is created in ifTable and it  can support sub\-interface.  An entry is deleted by an agent, when the ifTable entry associated to the Ethernet\-like interface is deleted. Typically, when the card is removed from the device
        	**type**\: list of  		 :py:class:`CeeSubInterfaceEntry <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CISCOETHERLIKEEXTMIB.CeeSubInterfaceTable.CeeSubInterfaceEntry>`
        
        

        """

        _prefix = 'CISCO-ETHERLIKE-EXT-MIB'
        _revision = '2010-06-04'

        def __init__(self):
            super(CISCOETHERLIKEEXTMIB.CeeSubInterfaceTable, self).__init__()

            self.yang_name = "ceeSubInterfaceTable"
            self.yang_parent_name = "CISCO-ETHERLIKE-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ceeSubInterfaceEntry", ("ceesubinterfaceentry", CISCOETHERLIKEEXTMIB.CeeSubInterfaceTable.CeeSubInterfaceEntry))])
            self._leafs = OrderedDict()

            self.ceesubinterfaceentry = YList(self)
            self._segment_path = lambda: "ceeSubInterfaceTable"
            self._absolute_path = lambda: "CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOETHERLIKEEXTMIB.CeeSubInterfaceTable, [], name, value)


        class CeeSubInterfaceEntry(Entity):
            """
            This table contains a row for each Ethernet\-like interface
            by it's ifTable ifIndex in the system, which supports the
            sub\-interface.
            
            An entry is created by an agent, when it detects a
            Ethernet\-like interface is created in ifTable and it 
            can support sub\-interface.
            
            An entry is deleted by an agent, when the ifTable entry
            associated to the Ethernet\-like interface is deleted.
            Typically, when the card is removed from the device.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: ceesubinterfacecount
            
            	This object represents the number of subinterfaces created on a Ethernet\-like interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: subifs
            
            

            """

            _prefix = 'CISCO-ETHERLIKE-EXT-MIB'
            _revision = '2010-06-04'

            def __init__(self):
                super(CISCOETHERLIKEEXTMIB.CeeSubInterfaceTable.CeeSubInterfaceEntry, self).__init__()

                self.yang_name = "ceeSubInterfaceEntry"
                self.yang_parent_name = "ceeSubInterfaceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('ceesubinterfacecount', (YLeaf(YType.uint32, 'ceeSubInterfaceCount'), ['int'])),
                ])
                self.ifindex = None
                self.ceesubinterfacecount = None
                self._segment_path = lambda: "ceeSubInterfaceEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB/ceeSubInterfaceTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOETHERLIKEEXTMIB.CeeSubInterfaceTable.CeeSubInterfaceEntry, ['ifindex', 'ceesubinterfacecount'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOETHERLIKEEXTMIB()
        return self._top_entity


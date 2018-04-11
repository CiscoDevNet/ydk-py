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
    	**type**\:  :py:class:`Ceedot3Pauseexttable <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CISCOETHERLIKEEXTMIB.Ceedot3Pauseexttable>`
    
    .. attribute:: ceesubinterfacetable
    
    	This table provides the subinterface related information associated to the Ethernet\-like interfaces.  The subinterface is a division of one physical interface into multiple logical interfaces. As an example of what a typical subinterface setup might look like on a device, a single Ethernet port such as GigabitEthernet0/0 would be subdivided into Gi0/0.1, Gi0/0.2, Gi0/0.3 and so on, each one performing as if it were a separate interface
    	**type**\:  :py:class:`Ceesubinterfacetable <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CISCOETHERLIKEEXTMIB.Ceesubinterfacetable>`
    
    

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
        self._child_container_classes = OrderedDict([("ceeDot3PauseExtTable", ("ceedot3pauseexttable", CISCOETHERLIKEEXTMIB.Ceedot3Pauseexttable)), ("ceeSubInterfaceTable", ("ceesubinterfacetable", CISCOETHERLIKEEXTMIB.Ceesubinterfacetable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.ceedot3pauseexttable = CISCOETHERLIKEEXTMIB.Ceedot3Pauseexttable()
        self.ceedot3pauseexttable.parent = self
        self._children_name_map["ceedot3pauseexttable"] = "ceeDot3PauseExtTable"
        self._children_yang_names.add("ceeDot3PauseExtTable")

        self.ceesubinterfacetable = CISCOETHERLIKEEXTMIB.Ceesubinterfacetable()
        self.ceesubinterfacetable.parent = self
        self._children_name_map["ceesubinterfacetable"] = "ceeSubInterfaceTable"
        self._children_yang_names.add("ceeSubInterfaceTable")
        self._segment_path = lambda: "CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB"


    class Ceedot3Pauseexttable(Entity):
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
        	**type**\: list of  		 :py:class:`Ceedot3Pauseextentry <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CISCOETHERLIKEEXTMIB.Ceedot3Pauseexttable.Ceedot3Pauseextentry>`
        
        

        """

        _prefix = 'CISCO-ETHERLIKE-EXT-MIB'
        _revision = '2010-06-04'

        def __init__(self):
            super(CISCOETHERLIKEEXTMIB.Ceedot3Pauseexttable, self).__init__()

            self.yang_name = "ceeDot3PauseExtTable"
            self.yang_parent_name = "CISCO-ETHERLIKE-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ceeDot3PauseExtEntry", ("ceedot3pauseextentry", CISCOETHERLIKEEXTMIB.Ceedot3Pauseexttable.Ceedot3Pauseextentry))])
            self._leafs = OrderedDict()

            self.ceedot3pauseextentry = YList(self)
            self._segment_path = lambda: "ceeDot3PauseExtTable"
            self._absolute_path = lambda: "CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOETHERLIKEEXTMIB.Ceedot3Pauseexttable, [], name, value)


        class Ceedot3Pauseextentry(Entity):
            """
            An entry in the table, containing additional
            information about the MAC Control PAUSE function 
            on a single ethernet\-like interface, in extension 
            to dot3PauseEntry in Etherlike\-MIB.
            
            .. attribute:: dot3statsindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`dot3statsindex <ydk.models.cisco_ios_xe.EtherLike_MIB.EtherLikeMIB.Dot3Statstable.Dot3Statsentry>`
            
            .. attribute:: ceedot3pauseextadminmode
            
            	Indicates preference to send or process pause frames on this interface. txDesired(0)  \-  indicates preference to send pause                   frames, but autonegotiates flow                   control. This bit can only be                   turned on when the corresponding                   instance of dot3PauseAdminMode                   has the value of 'enabledXmit' or                   'enabledXmitAndRcv'. rxDesired(1)  \-  indicates preference to process                   pause frames, but autonegotiates                   flow control. This bit can only be                   turned on when the corresponding                   instance of dot3PauseAdminMode                   has the value of 'enabledRcv' or                   'enabledXmitAndRcv'
            	**type**\:  :py:class:`Ceedot3Pauseextadminmode <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CISCOETHERLIKEEXTMIB.Ceedot3Pauseexttable.Ceedot3Pauseextentry.Ceedot3Pauseextadminmode>`
            
            .. attribute:: ceedot3pauseextopermode
            
            	Provides additional information about the flow control operational status on this interface. txDisagree(0) \- the transmit pause function on                  this interface is disabled due to                  disagreement from the far end on                  negotiation. rxDisagree(1) \- the receive pause function on                   this interface is disabled due to                  disagreement from the far end on                  negotiation. txDesired(2)  \- the transmit pause function on                  this interface is desired. rxDesired(3)  \- the receive pause function on                   this interface is desired
            	**type**\:  :py:class:`Ceedot3Pauseextopermode <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CISCOETHERLIKEEXTMIB.Ceedot3Pauseexttable.Ceedot3Pauseextentry.Ceedot3Pauseextopermode>`
            
            

            """

            _prefix = 'CISCO-ETHERLIKE-EXT-MIB'
            _revision = '2010-06-04'

            def __init__(self):
                super(CISCOETHERLIKEEXTMIB.Ceedot3Pauseexttable.Ceedot3Pauseextentry, self).__init__()

                self.yang_name = "ceeDot3PauseExtEntry"
                self.yang_parent_name = "ceeDot3PauseExtTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['dot3statsindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dot3statsindex', YLeaf(YType.str, 'dot3StatsIndex')),
                    ('ceedot3pauseextadminmode', YLeaf(YType.bits, 'ceeDot3PauseExtAdminMode')),
                    ('ceedot3pauseextopermode', YLeaf(YType.bits, 'ceeDot3PauseExtOperMode')),
                ])
                self.dot3statsindex = None
                self.ceedot3pauseextadminmode = Bits()
                self.ceedot3pauseextopermode = Bits()
                self._segment_path = lambda: "ceeDot3PauseExtEntry" + "[dot3StatsIndex='" + str(self.dot3statsindex) + "']"
                self._absolute_path = lambda: "CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB/ceeDot3PauseExtTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOETHERLIKEEXTMIB.Ceedot3Pauseexttable.Ceedot3Pauseextentry, ['dot3statsindex', 'ceedot3pauseextadminmode', 'ceedot3pauseextopermode'], name, value)


    class Ceesubinterfacetable(Entity):
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
        	**type**\: list of  		 :py:class:`Ceesubinterfaceentry <ydk.models.cisco_ios_xe.CISCO_ETHERLIKE_EXT_MIB.CISCOETHERLIKEEXTMIB.Ceesubinterfacetable.Ceesubinterfaceentry>`
        
        

        """

        _prefix = 'CISCO-ETHERLIKE-EXT-MIB'
        _revision = '2010-06-04'

        def __init__(self):
            super(CISCOETHERLIKEEXTMIB.Ceesubinterfacetable, self).__init__()

            self.yang_name = "ceeSubInterfaceTable"
            self.yang_parent_name = "CISCO-ETHERLIKE-EXT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ceeSubInterfaceEntry", ("ceesubinterfaceentry", CISCOETHERLIKEEXTMIB.Ceesubinterfacetable.Ceesubinterfaceentry))])
            self._leafs = OrderedDict()

            self.ceesubinterfaceentry = YList(self)
            self._segment_path = lambda: "ceeSubInterfaceTable"
            self._absolute_path = lambda: "CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOETHERLIKEEXTMIB.Ceesubinterfacetable, [], name, value)


        class Ceesubinterfaceentry(Entity):
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
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: ceesubinterfacecount
            
            	This object represents the number of subinterfaces created on a Ethernet\-like interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: subifs
            
            

            """

            _prefix = 'CISCO-ETHERLIKE-EXT-MIB'
            _revision = '2010-06-04'

            def __init__(self):
                super(CISCOETHERLIKEEXTMIB.Ceesubinterfacetable.Ceesubinterfaceentry, self).__init__()

                self.yang_name = "ceeSubInterfaceEntry"
                self.yang_parent_name = "ceeSubInterfaceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('ceesubinterfacecount', YLeaf(YType.uint32, 'ceeSubInterfaceCount')),
                ])
                self.ifindex = None
                self.ceesubinterfacecount = None
                self._segment_path = lambda: "ceeSubInterfaceEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-ETHERLIKE-EXT-MIB:CISCO-ETHERLIKE-EXT-MIB/ceeSubInterfaceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOETHERLIKEEXTMIB.Ceesubinterfacetable.Ceesubinterfaceentry, ['ifindex', 'ceesubinterfacecount'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOETHERLIKEEXTMIB()
        return self._top_entity


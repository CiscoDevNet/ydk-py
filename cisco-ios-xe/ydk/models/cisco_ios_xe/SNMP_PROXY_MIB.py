""" SNMP_PROXY_MIB 

This MIB module defines MIB objects which provide
mechanisms to remotely configure the parameters
used by a proxy forwarding application.

Copyright (C) The Internet Society (2002). This
version of this MIB module is part of RFC 3413;
see the RFC itself for full legal notices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SNMPPROXYMIB(Entity):
    """
    
    
    .. attribute:: snmpproxytable
    
    	The table of translation parameters used by proxy forwarder applications for forwarding SNMP messages
    	**type**\:  :py:class:`Snmpproxytable <ydk.models.cisco_ios_xe.SNMP_PROXY_MIB.SNMPPROXYMIB.Snmpproxytable>`
    
    

    """

    _prefix = 'SNMP-PROXY-MIB'
    _revision = '2002-10-14'

    def __init__(self):
        super(SNMPPROXYMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "SNMP-PROXY-MIB"
        self.yang_parent_name = "SNMP-PROXY-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("snmpProxyTable", ("snmpproxytable", SNMPPROXYMIB.Snmpproxytable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.snmpproxytable = SNMPPROXYMIB.Snmpproxytable()
        self.snmpproxytable.parent = self
        self._children_name_map["snmpproxytable"] = "snmpProxyTable"
        self._children_yang_names.add("snmpProxyTable")
        self._segment_path = lambda: "SNMP-PROXY-MIB:SNMP-PROXY-MIB"


    class Snmpproxytable(Entity):
        """
        The table of translation parameters used by proxy forwarder
        applications for forwarding SNMP messages.
        
        .. attribute:: snmpproxyentry
        
        	A set of translation parameters used by a proxy forwarder application for forwarding SNMP messages.  Entries in the snmpProxyTable are created and deleted using the snmpProxyRowStatus object
        	**type**\: list of  		 :py:class:`Snmpproxyentry <ydk.models.cisco_ios_xe.SNMP_PROXY_MIB.SNMPPROXYMIB.Snmpproxytable.Snmpproxyentry>`
        
        

        """

        _prefix = 'SNMP-PROXY-MIB'
        _revision = '2002-10-14'

        def __init__(self):
            super(SNMPPROXYMIB.Snmpproxytable, self).__init__()

            self.yang_name = "snmpProxyTable"
            self.yang_parent_name = "SNMP-PROXY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("snmpProxyEntry", ("snmpproxyentry", SNMPPROXYMIB.Snmpproxytable.Snmpproxyentry))])
            self._leafs = OrderedDict()

            self.snmpproxyentry = YList(self)
            self._segment_path = lambda: "snmpProxyTable"
            self._absolute_path = lambda: "SNMP-PROXY-MIB:SNMP-PROXY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPPROXYMIB.Snmpproxytable, [], name, value)


        class Snmpproxyentry(Entity):
            """
            A set of translation parameters used by a proxy forwarder
            application for forwarding SNMP messages.
            
            Entries in the snmpProxyTable are created and deleted
            using the snmpProxyRowStatus object.
            
            .. attribute:: snmpproxyname  (key)
            
            	The locally arbitrary, but unique identifier associated with this snmpProxyEntry
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: snmpproxytype
            
            	The type of message that may be forwarded using the translation parameters defined by this entry
            	**type**\:  :py:class:`Snmpproxytype <ydk.models.cisco_ios_xe.SNMP_PROXY_MIB.SNMPPROXYMIB.Snmpproxytable.Snmpproxyentry.Snmpproxytype>`
            
            .. attribute:: snmpproxycontextengineid
            
            	The contextEngineID contained in messages that may be forwarded using the translation parameters defined by this entry
            	**type**\: str
            
            	**length:** 5..32
            
            .. attribute:: snmpproxycontextname
            
            	The contextName contained in messages that may be forwarded using the translation parameters defined by this entry.  This object is optional, and if not supported, the contextName contained in a message is ignored when selecting an entry in the snmpProxyTable
            	**type**\: str
            
            .. attribute:: snmpproxytargetparamsin
            
            	This object selects an entry in the snmpTargetParamsTable. The selected entry is used to determine which row of the snmpProxyTable to use for forwarding received messages
            	**type**\: str
            
            .. attribute:: snmpproxysingletargetout
            
            	This object selects a management target defined in the snmpTargetAddrTable (in the SNMP\-TARGET\-MIB).  The selected target is defined by an entry in the snmpTargetAddrTable whose index value (snmpTargetAddrName) is equal to this object.  This object is only used when selection of a single target is required (i.e. when forwarding an incoming read or write request)
            	**type**\: str
            
            .. attribute:: snmpproxymultipletargetout
            
            	This object selects a set of management targets defined in the snmpTargetAddrTable (in the SNMP\-TARGET\-MIB).  This object is only used when selection of multiple targets is required (i.e. when forwarding an incoming notification)
            	**type**\: str
            
            .. attribute:: snmpproxystoragetype
            
            	The storage type of this conceptual row. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: snmpproxyrowstatus
            
            	The status of this conceptual row.  To create a row in this table, a manager must set this object to either createAndGo(4) or createAndWait(5).  The following objects may not be modified while the value of this object is active(1)\:     \- snmpProxyType     \- snmpProxyContextEngineID     \- snmpProxyContextName     \- snmpProxyTargetParamsIn     \- snmpProxySingleTargetOut     \- snmpProxyMultipleTargetOut
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'SNMP-PROXY-MIB'
            _revision = '2002-10-14'

            def __init__(self):
                super(SNMPPROXYMIB.Snmpproxytable.Snmpproxyentry, self).__init__()

                self.yang_name = "snmpProxyEntry"
                self.yang_parent_name = "snmpProxyTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['snmpproxyname']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('snmpproxyname', YLeaf(YType.str, 'snmpProxyName')),
                    ('snmpproxytype', YLeaf(YType.enumeration, 'snmpProxyType')),
                    ('snmpproxycontextengineid', YLeaf(YType.str, 'snmpProxyContextEngineID')),
                    ('snmpproxycontextname', YLeaf(YType.str, 'snmpProxyContextName')),
                    ('snmpproxytargetparamsin', YLeaf(YType.str, 'snmpProxyTargetParamsIn')),
                    ('snmpproxysingletargetout', YLeaf(YType.str, 'snmpProxySingleTargetOut')),
                    ('snmpproxymultipletargetout', YLeaf(YType.str, 'snmpProxyMultipleTargetOut')),
                    ('snmpproxystoragetype', YLeaf(YType.enumeration, 'snmpProxyStorageType')),
                    ('snmpproxyrowstatus', YLeaf(YType.enumeration, 'snmpProxyRowStatus')),
                ])
                self.snmpproxyname = None
                self.snmpproxytype = None
                self.snmpproxycontextengineid = None
                self.snmpproxycontextname = None
                self.snmpproxytargetparamsin = None
                self.snmpproxysingletargetout = None
                self.snmpproxymultipletargetout = None
                self.snmpproxystoragetype = None
                self.snmpproxyrowstatus = None
                self._segment_path = lambda: "snmpProxyEntry" + "[snmpProxyName='" + str(self.snmpproxyname) + "']"
                self._absolute_path = lambda: "SNMP-PROXY-MIB:SNMP-PROXY-MIB/snmpProxyTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SNMPPROXYMIB.Snmpproxytable.Snmpproxyentry, ['snmpproxyname', 'snmpproxytype', 'snmpproxycontextengineid', 'snmpproxycontextname', 'snmpproxytargetparamsin', 'snmpproxysingletargetout', 'snmpproxymultipletargetout', 'snmpproxystoragetype', 'snmpproxyrowstatus'], name, value)

            class Snmpproxytype(Enum):
                """
                Snmpproxytype (Enum Class)

                The type of message that may be forwarded using

                the translation parameters defined by this entry.

                .. data:: read = 1

                .. data:: write = 2

                .. data:: trap = 3

                .. data:: inform = 4

                """

                read = Enum.YLeaf(1, "read")

                write = Enum.YLeaf(2, "write")

                trap = Enum.YLeaf(3, "trap")

                inform = Enum.YLeaf(4, "inform")


    def clone_ptr(self):
        self._top_entity = SNMPPROXYMIB()
        return self._top_entity


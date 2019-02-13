""" CLAB_TOPO_MIB 

This MIB module contains the management objects for the
management of fiber nodes in the Cable plant.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CLABTOPOMIB(Entity):
    """
    
    
    .. attribute:: clabtopofibernodecfgtable
    
    	This object defines the cable HFC plant Fiber Nodes known at a CMTS. This object supports the creation and deletion of multiple instances
    	**type**\:  :py:class:`ClabTopoFiberNodeCfgTable <ydk.models.cisco_ios_xe.CLAB_TOPO_MIB.CLABTOPOMIB.ClabTopoFiberNodeCfgTable>`
    
    	**config**\: False
    
    .. attribute:: clabtopochfncfgtable
    
    	This object defines the RF topology by defining the connectivity of a CMTS's downstream and upstream channels to the fiber nodes. Each instance of this object describes connectivity of one downstream or upstream channel with a single fiber node. This object supports the creation and deletion of multiple instances
    	**type**\:  :py:class:`ClabTopoChFnCfgTable <ydk.models.cisco_ios_xe.CLAB_TOPO_MIB.CLABTOPOMIB.ClabTopoChFnCfgTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CLAB-TOPO-MIB'
    _revision = '2006-12-07'

    def __init__(self):
        super(CLABTOPOMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CLAB-TOPO-MIB"
        self.yang_parent_name = "CLAB-TOPO-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("clabTopoFiberNodeCfgTable", ("clabtopofibernodecfgtable", CLABTOPOMIB.ClabTopoFiberNodeCfgTable)), ("clabTopoChFnCfgTable", ("clabtopochfncfgtable", CLABTOPOMIB.ClabTopoChFnCfgTable))])
        self._leafs = OrderedDict()

        self.clabtopofibernodecfgtable = CLABTOPOMIB.ClabTopoFiberNodeCfgTable()
        self.clabtopofibernodecfgtable.parent = self
        self._children_name_map["clabtopofibernodecfgtable"] = "clabTopoFiberNodeCfgTable"

        self.clabtopochfncfgtable = CLABTOPOMIB.ClabTopoChFnCfgTable()
        self.clabtopochfncfgtable.parent = self
        self._children_name_map["clabtopochfncfgtable"] = "clabTopoChFnCfgTable"
        self._segment_path = lambda: "CLAB-TOPO-MIB:CLAB-TOPO-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CLABTOPOMIB, [], name, value)


    class ClabTopoFiberNodeCfgTable(Entity):
        """
        This object defines the cable HFC plant Fiber Nodes
        known at a CMTS.
        This object supports the creation and deletion of multiple
        instances.
        
        .. attribute:: clabtopofibernodecfgentry
        
        	The conceptual row of clabTopoFiberNodeCfg. The CMTS persists all instances of FiberNodeCfg across reinitializations
        	**type**\: list of  		 :py:class:`ClabTopoFiberNodeCfgEntry <ydk.models.cisco_ios_xe.CLAB_TOPO_MIB.CLABTOPOMIB.ClabTopoFiberNodeCfgTable.ClabTopoFiberNodeCfgEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CLAB-TOPO-MIB'
        _revision = '2006-12-07'

        def __init__(self):
            super(CLABTOPOMIB.ClabTopoFiberNodeCfgTable, self).__init__()

            self.yang_name = "clabTopoFiberNodeCfgTable"
            self.yang_parent_name = "CLAB-TOPO-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("clabTopoFiberNodeCfgEntry", ("clabtopofibernodecfgentry", CLABTOPOMIB.ClabTopoFiberNodeCfgTable.ClabTopoFiberNodeCfgEntry))])
            self._leafs = OrderedDict()

            self.clabtopofibernodecfgentry = YList(self)
            self._segment_path = lambda: "clabTopoFiberNodeCfgTable"
            self._absolute_path = lambda: "CLAB-TOPO-MIB:CLAB-TOPO-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CLABTOPOMIB.ClabTopoFiberNodeCfgTable, [], name, value)


        class ClabTopoFiberNodeCfgEntry(Entity):
            """
            The conceptual row of clabTopoFiberNodeCfg.
            The CMTS persists all instances of FiberNodeCfg
            across reinitializations.
            
            .. attribute:: clabtopofibernodecfgnodename  (key)
            
            	This key represents a human\-readable name for a fiber node
            	**type**\: str
            
            	**length:** 1..16
            
            	**config**\: False
            
            .. attribute:: clabtopofibernodecfgnodedescr
            
            	Administratively configured human\-readable description of the fiber node
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: clabtopofibernodecfgrowstatus
            
            	The status of this instance
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CLAB-TOPO-MIB'
            _revision = '2006-12-07'

            def __init__(self):
                super(CLABTOPOMIB.ClabTopoFiberNodeCfgTable.ClabTopoFiberNodeCfgEntry, self).__init__()

                self.yang_name = "clabTopoFiberNodeCfgEntry"
                self.yang_parent_name = "clabTopoFiberNodeCfgTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['clabtopofibernodecfgnodename']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('clabtopofibernodecfgnodename', (YLeaf(YType.str, 'clabTopoFiberNodeCfgNodeName'), ['str'])),
                    ('clabtopofibernodecfgnodedescr', (YLeaf(YType.str, 'clabTopoFiberNodeCfgNodeDescr'), ['str'])),
                    ('clabtopofibernodecfgrowstatus', (YLeaf(YType.enumeration, 'clabTopoFiberNodeCfgRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.clabtopofibernodecfgnodename = None
                self.clabtopofibernodecfgnodedescr = None
                self.clabtopofibernodecfgrowstatus = None
                self._segment_path = lambda: "clabTopoFiberNodeCfgEntry" + "[clabTopoFiberNodeCfgNodeName='" + str(self.clabtopofibernodecfgnodename) + "']"
                self._absolute_path = lambda: "CLAB-TOPO-MIB:CLAB-TOPO-MIB/clabTopoFiberNodeCfgTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CLABTOPOMIB.ClabTopoFiberNodeCfgTable.ClabTopoFiberNodeCfgEntry, [u'clabtopofibernodecfgnodename', u'clabtopofibernodecfgnodedescr', u'clabtopofibernodecfgrowstatus'], name, value)




    class ClabTopoChFnCfgTable(Entity):
        """
        This object defines the RF topology by defining the
        connectivity of a CMTS's downstream and upstream channels
        to the fiber nodes. Each instance of this object
        describes connectivity of one downstream or upstream
        channel with a single fiber node.
        This object supports the creation and deletion of multiple
        instances.
        
        .. attribute:: clabtopochfncfgentry
        
        	The conceptual row of clabTopoChFnCfg. The CMTS persists all instances of ChFnCfg across reinitializations
        	**type**\: list of  		 :py:class:`ClabTopoChFnCfgEntry <ydk.models.cisco_ios_xe.CLAB_TOPO_MIB.CLABTOPOMIB.ClabTopoChFnCfgTable.ClabTopoChFnCfgEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CLAB-TOPO-MIB'
        _revision = '2006-12-07'

        def __init__(self):
            super(CLABTOPOMIB.ClabTopoChFnCfgTable, self).__init__()

            self.yang_name = "clabTopoChFnCfgTable"
            self.yang_parent_name = "CLAB-TOPO-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("clabTopoChFnCfgEntry", ("clabtopochfncfgentry", CLABTOPOMIB.ClabTopoChFnCfgTable.ClabTopoChFnCfgEntry))])
            self._leafs = OrderedDict()

            self.clabtopochfncfgentry = YList(self)
            self._segment_path = lambda: "clabTopoChFnCfgTable"
            self._absolute_path = lambda: "CLAB-TOPO-MIB:CLAB-TOPO-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CLABTOPOMIB.ClabTopoChFnCfgTable, [], name, value)


        class ClabTopoChFnCfgEntry(Entity):
            """
            The conceptual row of clabTopoChFnCfg.
            The CMTS persists all instances of ChFnCfg
            across reinitializations.
            
            .. attribute:: clabtopofibernodecfgnodename  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..16
            
            	**refers to**\:  :py:class:`clabtopofibernodecfgnodename <ydk.models.cisco_ios_xe.CLAB_TOPO_MIB.CLABTOPOMIB.ClabTopoFiberNodeCfgTable.ClabTopoFiberNodeCfgEntry>`
            
            	**config**\: False
            
            .. attribute:: clabtopochfncfgchifindex  (key)
            
            	This key represents the interface index of an upstream or downstream channel associated with this fiber node. In the upstream direction, only ifIndices docsCableUpstream channels are reflected
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: clabtopochfncfgrowstatus
            
            	The status of this instance
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CLAB-TOPO-MIB'
            _revision = '2006-12-07'

            def __init__(self):
                super(CLABTOPOMIB.ClabTopoChFnCfgTable.ClabTopoChFnCfgEntry, self).__init__()

                self.yang_name = "clabTopoChFnCfgEntry"
                self.yang_parent_name = "clabTopoChFnCfgTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['clabtopofibernodecfgnodename','clabtopochfncfgchifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('clabtopofibernodecfgnodename', (YLeaf(YType.str, 'clabTopoFiberNodeCfgNodeName'), ['str'])),
                    ('clabtopochfncfgchifindex', (YLeaf(YType.int32, 'clabTopoChFnCfgChIfIndex'), ['int'])),
                    ('clabtopochfncfgrowstatus', (YLeaf(YType.enumeration, 'clabTopoChFnCfgRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.clabtopofibernodecfgnodename = None
                self.clabtopochfncfgchifindex = None
                self.clabtopochfncfgrowstatus = None
                self._segment_path = lambda: "clabTopoChFnCfgEntry" + "[clabTopoFiberNodeCfgNodeName='" + str(self.clabtopofibernodecfgnodename) + "']" + "[clabTopoChFnCfgChIfIndex='" + str(self.clabtopochfncfgchifindex) + "']"
                self._absolute_path = lambda: "CLAB-TOPO-MIB:CLAB-TOPO-MIB/clabTopoChFnCfgTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CLABTOPOMIB.ClabTopoChFnCfgTable.ClabTopoChFnCfgEntry, [u'clabtopofibernodecfgnodename', u'clabtopochfncfgchifindex', u'clabtopochfncfgrowstatus'], name, value)



    def clone_ptr(self):
        self._top_entity = CLABTOPOMIB()
        return self._top_entity




""" Cisco_IOS_XR_asr9k_lc_fca_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-lc\-fca package operational data.

This module contains definitions
for the following management objects\:
  mpa\-internal\: Management LAN Operational data space
  mpa\: mpa

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SpaFailureReason(Enum):
    """
    SpaFailureReason (Enum Class)

    SPA failure reasons

    .. data:: spa_failure_reason_unknown = 1

    	spa failure reason unknown

    .. data:: spa_failure_reason_spi_failure = 2

    	spa failure reason spi failure

    .. data:: spa_failure_reason_boot = 3

    	spa failure reason boot

    .. data:: spa_failure_reason_hw_failed = 4

    	spa failure reason hw failed

    .. data:: spa_failure_reason_sw_failed = 5

    	spa failure reason sw failed

    .. data:: spa_failure_reason_sw_restart = 6

    	spa failure reason sw restart

    .. data:: spa_failure_reason_check_fpd = 7

    	spa failure reason check fpd

    .. data:: spa_failure_reason_read_type = 8

    	spa failure reason read type

    """

    spa_failure_reason_unknown = Enum.YLeaf(1, "spa-failure-reason-unknown")

    spa_failure_reason_spi_failure = Enum.YLeaf(2, "spa-failure-reason-spi-failure")

    spa_failure_reason_boot = Enum.YLeaf(3, "spa-failure-reason-boot")

    spa_failure_reason_hw_failed = Enum.YLeaf(4, "spa-failure-reason-hw-failed")

    spa_failure_reason_sw_failed = Enum.YLeaf(5, "spa-failure-reason-sw-failed")

    spa_failure_reason_sw_restart = Enum.YLeaf(6, "spa-failure-reason-sw-restart")

    spa_failure_reason_check_fpd = Enum.YLeaf(7, "spa-failure-reason-check-fpd")

    spa_failure_reason_read_type = Enum.YLeaf(8, "spa-failure-reason-read-type")


class SpaOperState(Enum):
    """
    SpaOperState (Enum Class)

    SPA operational states

    .. data:: spa_state_reset = 1

    	spa state reset

    .. data:: spa_state_failed = 2

    	spa state failed

    .. data:: spa_state_booting = 3

    	spa state booting

    .. data:: spa_state_ready = 4

    	spa state ready

    """

    spa_state_reset = Enum.YLeaf(1, "spa-state-reset")

    spa_state_failed = Enum.YLeaf(2, "spa-state-failed")

    spa_state_booting = Enum.YLeaf(3, "spa-state-booting")

    spa_state_ready = Enum.YLeaf(4, "spa-state-ready")


class SpaResetReason(Enum):
    """
    SpaResetReason (Enum Class)

    SPA reset reasons

    .. data:: spa_reset_reason_unknown = 1

    	spa reset reason unknown

    .. data:: spa_reset_reason_manual = 2

    	spa reset reason manual

    .. data:: spa_reset_reason_fpd_upgrade = 3

    	spa reset reason fpd upgrade

    .. data:: spa_reset_reason_audit_fail = 4

    	spa reset reason audit fail

    .. data:: spa_reset_reason_failure = 5

    	spa reset reason failure

    """

    spa_reset_reason_unknown = Enum.YLeaf(1, "spa-reset-reason-unknown")

    spa_reset_reason_manual = Enum.YLeaf(2, "spa-reset-reason-manual")

    spa_reset_reason_fpd_upgrade = Enum.YLeaf(3, "spa-reset-reason-fpd-upgrade")

    spa_reset_reason_audit_fail = Enum.YLeaf(4, "spa-reset-reason-audit-fail")

    spa_reset_reason_failure = Enum.YLeaf(5, "spa-reset-reason-failure")



class MpaInternal(Entity):
    """
    Management LAN Operational data space
    
    .. attribute:: nodes
    
    	Table of nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.MpaInternal.Nodes>`
    
    

    """

    _prefix = 'asr9k-lc-fca-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(MpaInternal, self).__init__()
        self._top_entity = None

        self.yang_name = "mpa-internal"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-lc-fca-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("nodes", ("nodes", MpaInternal.Nodes))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.nodes = MpaInternal.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-lc-fca-oper:mpa-internal"


    class Nodes(Entity):
        """
        Table of nodes
        
        .. attribute:: node
        
        	Number
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.MpaInternal.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-lc-fca-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(MpaInternal.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "mpa-internal"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", MpaInternal.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-lc-fca-oper:mpa-internal/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MpaInternal.Nodes, [], name, value)


        class Node(Entity):
            """
            Number
            
            .. attribute:: node  (key)
            
            	node number
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: bay
            
            	Number
            	**type**\: list of  		 :py:class:`Bay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.MpaInternal.Nodes.Node.Bay>`
            
            

            """

            _prefix = 'asr9k-lc-fca-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MpaInternal.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("bay", ("bay", MpaInternal.Nodes.Node.Bay))])
                self._leafs = OrderedDict([
                    ('node', YLeaf(YType.str, 'node')),
                ])
                self.node = None

                self.bay = YList(self)
                self._segment_path = lambda: "node" + "[node='" + str(self.node) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-lc-fca-oper:mpa-internal/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MpaInternal.Nodes.Node, ['node'], name, value)


            class Bay(Entity):
                """
                Number
                
                .. attribute:: number  (key)
                
                	bay number
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ifsubsies
                
                	Table of Ifsubsys
                	**type**\:  :py:class:`Ifsubsies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.MpaInternal.Nodes.Node.Bay.Ifsubsies>`
                
                

                """

                _prefix = 'asr9k-lc-fca-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MpaInternal.Nodes.Node.Bay, self).__init__()

                    self.yang_name = "bay"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['number']
                    self._child_container_classes = OrderedDict([("ifsubsies", ("ifsubsies", MpaInternal.Nodes.Node.Bay.Ifsubsies))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('number', YLeaf(YType.int32, 'number')),
                    ])
                    self.number = None

                    self.ifsubsies = MpaInternal.Nodes.Node.Bay.Ifsubsies()
                    self.ifsubsies.parent = self
                    self._children_name_map["ifsubsies"] = "ifsubsies"
                    self._children_yang_names.add("ifsubsies")
                    self._segment_path = lambda: "bay" + "[number='" + str(self.number) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(MpaInternal.Nodes.Node.Bay, ['number'], name, value)


                class Ifsubsies(Entity):
                    """
                    Table of Ifsubsys
                    
                    .. attribute:: ifsubsy
                    
                    	Number
                    	**type**\: list of  		 :py:class:`Ifsubsy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy>`
                    
                    

                    """

                    _prefix = 'asr9k-lc-fca-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MpaInternal.Nodes.Node.Bay.Ifsubsies, self).__init__()

                        self.yang_name = "ifsubsies"
                        self.yang_parent_name = "bay"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("ifsubsy", ("ifsubsy", MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy))])
                        self._leafs = OrderedDict()

                        self.ifsubsy = YList(self)
                        self._segment_path = lambda: "ifsubsies"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MpaInternal.Nodes.Node.Bay.Ifsubsies, [], name, value)


                    class Ifsubsy(Entity):
                        """
                        Number
                        
                        .. attribute:: number  (key)
                        
                        	ifsubsys number
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: mpa_internal_info
                        
                        	mpa internal info
                        	**type**\:  :py:class:`MpaInternalInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy.MpaInternalInfo>`
                        
                        

                        """

                        _prefix = 'asr9k-lc-fca-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy, self).__init__()

                            self.yang_name = "ifsubsy"
                            self.yang_parent_name = "ifsubsies"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['number']
                            self._child_container_classes = OrderedDict([("mpa-internal-info", ("mpa_internal_info", MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy.MpaInternalInfo))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('number', YLeaf(YType.str, 'number')),
                            ])
                            self.number = None

                            self.mpa_internal_info = MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy.MpaInternalInfo()
                            self.mpa_internal_info.parent = self
                            self._children_name_map["mpa_internal_info"] = "mpa-internal-info"
                            self._children_yang_names.add("mpa-internal-info")
                            self._segment_path = lambda: "ifsubsy" + "[number='" + str(self.number) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy, ['number'], name, value)


                        class MpaInternalInfo(Entity):
                            """
                            mpa internal info
                            
                            .. attribute:: bay
                            
                            	bay
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ifsubsys
                            
                            	ifsubsys
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: if_state
                            
                            	if state
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: if_event
                            
                            	if event
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: ep_type
                            
                            	ep type
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ep_state
                            
                            	ep state
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: ep_presence
                            
                            	ep presence
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: ep_idprom_major
                            
                            	ep idprom major
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: ep_idprom_minor
                            
                            	ep idprom minor
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: ep_idprom_data
                            
                            	ep idprom data
                            	**type**\: str
                            
                            	**length:** 0..256
                            
                            

                            """

                            _prefix = 'asr9k-lc-fca-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy.MpaInternalInfo, self).__init__()

                                self.yang_name = "mpa-internal-info"
                                self.yang_parent_name = "ifsubsy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('bay', YLeaf(YType.uint32, 'bay')),
                                    ('ifsubsys', YLeaf(YType.uint32, 'ifsubsys')),
                                    ('if_state', YLeaf(YType.uint8, 'if-state')),
                                    ('if_event', YLeaf(YType.uint8, 'if-event')),
                                    ('ep_type', YLeaf(YType.uint32, 'ep-type')),
                                    ('ep_state', YLeaf(YType.uint8, 'ep-state')),
                                    ('ep_presence', YLeaf(YType.uint8, 'ep-presence')),
                                    ('ep_idprom_major', YLeaf(YType.uint8, 'ep-idprom-major')),
                                    ('ep_idprom_minor', YLeaf(YType.uint8, 'ep-idprom-minor')),
                                    ('ep_idprom_data', YLeaf(YType.str, 'ep-idprom-data')),
                                ])
                                self.bay = None
                                self.ifsubsys = None
                                self.if_state = None
                                self.if_event = None
                                self.ep_type = None
                                self.ep_state = None
                                self.ep_presence = None
                                self.ep_idprom_major = None
                                self.ep_idprom_minor = None
                                self.ep_idprom_data = None
                                self._segment_path = lambda: "mpa-internal-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy.MpaInternalInfo, ['bay', 'ifsubsys', 'if_state', 'if_event', 'ep_type', 'ep_state', 'ep_presence', 'ep_idprom_major', 'ep_idprom_minor', 'ep_idprom_data'], name, value)

    def clone_ptr(self):
        self._top_entity = MpaInternal()
        return self._top_entity

class Mpa(Entity):
    """
    mpa
    
    .. attribute:: nodes
    
    	Table of nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.Mpa.Nodes>`
    
    

    """

    _prefix = 'asr9k-lc-fca-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Mpa, self).__init__()
        self._top_entity = None

        self.yang_name = "mpa"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-lc-fca-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("nodes", ("nodes", Mpa.Nodes))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.nodes = Mpa.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-lc-fca-oper:mpa"


    class Nodes(Entity):
        """
        Table of nodes
        
        .. attribute:: node
        
        	Number
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.Mpa.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-lc-fca-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Mpa.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "mpa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", Mpa.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-lc-fca-oper:mpa/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Mpa.Nodes, [], name, value)


        class Node(Entity):
            """
            Number
            
            .. attribute:: node  (key)
            
            	node number
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: bay
            
            	Number
            	**type**\: list of  		 :py:class:`Bay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.Mpa.Nodes.Node.Bay>`
            
            

            """

            _prefix = 'asr9k-lc-fca-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Mpa.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("bay", ("bay", Mpa.Nodes.Node.Bay))])
                self._leafs = OrderedDict([
                    ('node', YLeaf(YType.str, 'node')),
                ])
                self.node = None

                self.bay = YList(self)
                self._segment_path = lambda: "node" + "[node='" + str(self.node) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-lc-fca-oper:mpa/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mpa.Nodes.Node, ['node'], name, value)


            class Bay(Entity):
                """
                Number
                
                .. attribute:: number  (key)
                
                	bay number
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: mpa_detail_table
                
                	Table of Mpa Detail Info
                	**type**\:  :py:class:`MpaDetailTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.Mpa.Nodes.Node.Bay.MpaDetailTable>`
                
                

                """

                _prefix = 'asr9k-lc-fca-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Mpa.Nodes.Node.Bay, self).__init__()

                    self.yang_name = "bay"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['number']
                    self._child_container_classes = OrderedDict([("mpa-detail-table", ("mpa_detail_table", Mpa.Nodes.Node.Bay.MpaDetailTable))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('number', YLeaf(YType.int32, 'number')),
                    ])
                    self.number = None

                    self.mpa_detail_table = Mpa.Nodes.Node.Bay.MpaDetailTable()
                    self.mpa_detail_table.parent = self
                    self._children_name_map["mpa_detail_table"] = "mpa-detail-table"
                    self._children_yang_names.add("mpa-detail-table")
                    self._segment_path = lambda: "bay" + "[number='" + str(self.number) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Mpa.Nodes.Node.Bay, ['number'], name, value)


                class MpaDetailTable(Entity):
                    """
                    Table of Mpa Detail Info
                    
                    .. attribute:: mpa_detail
                    
                    	mpa detail status info
                    	**type**\:  :py:class:`MpaDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.Mpa.Nodes.Node.Bay.MpaDetailTable.MpaDetail>`
                    
                    

                    """

                    _prefix = 'asr9k-lc-fca-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Mpa.Nodes.Node.Bay.MpaDetailTable, self).__init__()

                        self.yang_name = "mpa-detail-table"
                        self.yang_parent_name = "bay"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("mpa-detail", ("mpa_detail", Mpa.Nodes.Node.Bay.MpaDetailTable.MpaDetail))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.mpa_detail = Mpa.Nodes.Node.Bay.MpaDetailTable.MpaDetail()
                        self.mpa_detail.parent = self
                        self._children_name_map["mpa_detail"] = "mpa-detail"
                        self._children_yang_names.add("mpa-detail")
                        self._segment_path = lambda: "mpa-detail-table"


                    class MpaDetail(Entity):
                        """
                        mpa detail status info
                        
                        .. attribute:: bay_number
                        
                        	BAY number
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: is_spa_inserted
                        
                        	If SPA inserted
                        	**type**\: bool
                        
                        .. attribute:: spa_type
                        
                        	SPA type
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: is_spa_admin_up
                        
                        	If SPA admin state is Up
                        	**type**\: bool
                        
                        .. attribute:: spa_oper_state
                        
                        	SPA operational state
                        	**type**\:  :py:class:`SpaOperState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.SpaOperState>`
                        
                        .. attribute:: is_spa_power_admin_up
                        
                        	If SPA power admin state is Up
                        	**type**\: bool
                        
                        .. attribute:: is_spa_powered
                        
                        	If SPA powered
                        	**type**\: bool
                        
                        .. attribute:: is_spa_in_reset
                        
                        	If SPA in reset
                        	**type**\: bool
                        
                        .. attribute:: last_reset_reason
                        
                        	Last reset reason
                        	**type**\:  :py:class:`SpaResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.SpaResetReason>`
                        
                        .. attribute:: last_failure_reason
                        
                        	Last Failure Reason
                        	**type**\:  :py:class:`SpaFailureReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper.SpaFailureReason>`
                        
                        .. attribute:: insertion_time
                        
                        	Time when SPA last insertedin calendar format\: seconds since00\:00\:00 UTC, January 1, 1970
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: last_ready_time
                        
                        	Time when SPA last reached Ready statein calendar format\: seconds since00\:00\:00 UTC, January 1, 1970
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: up_time
                        
                        	Uptime in seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'asr9k-lc-fca-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Mpa.Nodes.Node.Bay.MpaDetailTable.MpaDetail, self).__init__()

                            self.yang_name = "mpa-detail"
                            self.yang_parent_name = "mpa-detail-table"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('bay_number', YLeaf(YType.uint16, 'bay-number')),
                                ('is_spa_inserted', YLeaf(YType.boolean, 'is-spa-inserted')),
                                ('spa_type', YLeaf(YType.uint16, 'spa-type')),
                                ('is_spa_admin_up', YLeaf(YType.boolean, 'is-spa-admin-up')),
                                ('spa_oper_state', YLeaf(YType.enumeration, 'spa-oper-state')),
                                ('is_spa_power_admin_up', YLeaf(YType.boolean, 'is-spa-power-admin-up')),
                                ('is_spa_powered', YLeaf(YType.boolean, 'is-spa-powered')),
                                ('is_spa_in_reset', YLeaf(YType.boolean, 'is-spa-in-reset')),
                                ('last_reset_reason', YLeaf(YType.enumeration, 'last-reset-reason')),
                                ('last_failure_reason', YLeaf(YType.enumeration, 'last-failure-reason')),
                                ('insertion_time', YLeaf(YType.uint32, 'insertion-time')),
                                ('last_ready_time', YLeaf(YType.uint32, 'last-ready-time')),
                                ('up_time', YLeaf(YType.uint32, 'up-time')),
                            ])
                            self.bay_number = None
                            self.is_spa_inserted = None
                            self.spa_type = None
                            self.is_spa_admin_up = None
                            self.spa_oper_state = None
                            self.is_spa_power_admin_up = None
                            self.is_spa_powered = None
                            self.is_spa_in_reset = None
                            self.last_reset_reason = None
                            self.last_failure_reason = None
                            self.insertion_time = None
                            self.last_ready_time = None
                            self.up_time = None
                            self._segment_path = lambda: "mpa-detail"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mpa.Nodes.Node.Bay.MpaDetailTable.MpaDetail, ['bay_number', 'is_spa_inserted', 'spa_type', 'is_spa_admin_up', 'spa_oper_state', 'is_spa_power_admin_up', 'is_spa_powered', 'is_spa_in_reset', 'last_reset_reason', 'last_failure_reason', 'insertion_time', 'last_ready_time', 'up_time'], name, value)

    def clone_ptr(self):
        self._top_entity = Mpa()
        return self._top_entity


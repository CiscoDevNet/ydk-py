""" Cisco_IOS_XR_sysadmin_ship 

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin operational.

This module defines operational data for
sysadmin ship process.

Copyright(c) 2010\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Stat(Entity):
    """
    SHIP Info
    
    .. attribute:: ship_comp
    
    	Select ship client component
    	**type**\: list of  		 :py:class:`ShipComp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ship.Stat.ShipComp>`
    
    

    """

    _prefix = 'ship'
    _revision = '2017-05-09'

    def __init__(self):
        super(Stat, self).__init__()
        self._top_entity = None

        self.yang_name = "stat"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-ship"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ship_comp", ("ship_comp", Stat.ShipComp))])
        self._leafs = OrderedDict()

        self.ship_comp = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-ship:stat"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Stat, [], name, value)


    class ShipComp(Entity):
        """
        Select ship client component
        
        .. attribute:: comp_name  (key)
        
        	Name of component
        	**type**\: str
        
        .. attribute:: process
        
        	
        	**type**\: list of  		 :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ship.Stat.ShipComp.Process>`
        
        

        """

        _prefix = 'ship'
        _revision = '2017-05-09'

        def __init__(self):
            super(Stat.ShipComp, self).__init__()

            self.yang_name = "ship_comp"
            self.yang_parent_name = "stat"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['comp_name']
            self._child_classes = OrderedDict([("process", ("process", Stat.ShipComp.Process))])
            self._leafs = OrderedDict([
                ('comp_name', (YLeaf(YType.str, 'comp-name'), ['str'])),
            ])
            self.comp_name = None

            self.process = YList(self)
            self._segment_path = lambda: "ship_comp" + "[comp-name='" + str(self.comp_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-ship:stat/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Stat.ShipComp, ['comp_name'], name, value)


        class Process(Entity):
            """
            
            
            .. attribute:: process_name  (key)
            
            	
            	**type**\: str
            
            .. attribute:: client
            
            	
            	**type**\: list of  		 :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ship.Stat.ShipComp.Process.Client>`
            
            

            """

            _prefix = 'ship'
            _revision = '2017-05-09'

            def __init__(self):
                super(Stat.ShipComp.Process, self).__init__()

                self.yang_name = "process"
                self.yang_parent_name = "ship_comp"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['process_name']
                self._child_classes = OrderedDict([("client", ("client", Stat.ShipComp.Process.Client))])
                self._leafs = OrderedDict([
                    ('process_name', (YLeaf(YType.str, 'process-name'), ['str'])),
                ])
                self.process_name = None

                self.client = YList(self)
                self._segment_path = lambda: "process" + "[process-name='" + str(self.process_name) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Stat.ShipComp.Process, ['process_name'], name, value)


            class Client(Entity):
                """
                
                
                .. attribute:: client_name  (key)
                
                	
                	**type**\: str
                
                .. attribute:: cat
                
                	
                	**type**\: list of  		 :py:class:`Cat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ship.Stat.ShipComp.Process.Client.Cat>`
                
                

                """

                _prefix = 'ship'
                _revision = '2017-05-09'

                def __init__(self):
                    super(Stat.ShipComp.Process.Client, self).__init__()

                    self.yang_name = "client"
                    self.yang_parent_name = "process"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['client_name']
                    self._child_classes = OrderedDict([("cat", ("cat", Stat.ShipComp.Process.Client.Cat))])
                    self._leafs = OrderedDict([
                        ('client_name', (YLeaf(YType.str, 'client-name'), ['str'])),
                    ])
                    self.client_name = None

                    self.cat = YList(self)
                    self._segment_path = lambda: "client" + "[client-name='" + str(self.client_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Stat.ShipComp.Process.Client, ['client_name'], name, value)


                class Cat(Entity):
                    """
                    
                    
                    .. attribute:: cat_name  (key)
                    
                    	
                    	**type**\:  :py:class:`CatName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ship.Stat.ShipComp.Process.Client.Cat.CatName>`
                    
                    .. attribute:: counter_32b
                    
                    	
                    	**type**\: list of  		 :py:class:`Counter32b <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ship.Stat.ShipComp.Process.Client.Cat.Counter32b>`
                    
                    

                    """

                    _prefix = 'ship'
                    _revision = '2017-05-09'

                    def __init__(self):
                        super(Stat.ShipComp.Process.Client.Cat, self).__init__()

                        self.yang_name = "cat"
                        self.yang_parent_name = "client"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['cat_name']
                        self._child_classes = OrderedDict([("counter-32b", ("counter_32b", Stat.ShipComp.Process.Client.Cat.Counter32b))])
                        self._leafs = OrderedDict([
                            ('cat_name', (YLeaf(YType.enumeration, 'cat-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_ship', 'Stat', 'ShipComp.Process.Client.Cat.CatName')])),
                        ])
                        self.cat_name = None

                        self.counter_32b = YList(self)
                        self._segment_path = lambda: "cat" + "[cat-name='" + str(self.cat_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Stat.ShipComp.Process.Client.Cat, ['cat_name'], name, value)

                    class CatName(Enum):
                        """
                        CatName (Enum Class)

                        .. data:: SHIP_TRANSPORT_COUNTERS = 0

                        .. data:: SHIP_SERVER_COUNTERS = 1

                        .. data:: SHIP_CLIENT_LIB_COUNTERS = 2

                        .. data:: SHIP_REPLICATION_COUNTERS = 3

                        .. data:: SHIP_READER_REPLICA_COUNTERS = 4

                        .. data:: SHIP_WRITER_REPLICA_COUNTERS = 5

                        .. data:: SHIP_TRANSPORT_COUNTERS_FAILOVER = 6

                        .. data:: SHIP_SERVER_COUNTERS_FAILOVER = 7

                        .. data:: SHIP_CLIENT_LIB_COUNTERS_FAILOVER = 8

                        .. data:: SHIP_REPLICATION_COUNTERS_FAILOVER = 9

                        .. data:: SHIP_TRANSPORT_ERRORS = 10

                        .. data:: SHIP_SERVER_ERRORS = 11

                        .. data:: SHIP_CLIENT_LIB_ERRORS = 12

                        .. data:: SHIP_REPLICATION_ERRORS = 13

                        .. data:: SHIP_READER_REPLICA_ERRORS = 14

                        .. data:: SHIP_WRITER_REPLICA_ERRORS = 15

                        .. data:: SHIP_TRANSPORT_ERRORS_FAILOVER = 16

                        .. data:: SHIP_SERVER_ERRORS_FAILOVER = 17

                        .. data:: SHIP_CLIENT_LIB_ERRORS_FAILOVER = 18

                        .. data:: SHIP_REPLICATION_ERRORS_FAILOVER = 19

                        .. data:: FEATURE_MA_COUNTERS = 20

                        .. data:: FEATURE_MA_COUNTERS_ERRORS = 21

                        .. data:: FEATURE_MA_COUNTERS_FAILOVER = 22

                        .. data:: VIRTUAL_INTERFACE_MA_COUNTERS = 23

                        .. data:: VIRTUAL_INTERFACE_MA_COUNTERS_ERRORS = 24

                        .. data:: VIRTUAL_INTERFACE_MA_COUNTERS_FAILOVER = 25

                        .. data:: FEATURE_EA_COUNTERS = 26

                        .. data:: FEATURE_EA_COUNTERS_ERRORS = 27

                        .. data:: VIRTUAL_INTERFACE_EA_COUNTERS = 28

                        .. data:: VIRTUAL_INTERFACE_EA_COUNTERS_ERRORS = 29

                        .. data:: VIRTUAL_INTERFACE_EA_COUNTERS_FAILOVER = 30

                        .. data:: SHIP_HISTOGRAM_COUNTERS = 31

                        .. data:: SHIP_WATERMARK_COUNTERS = 32

                        .. data:: SHIP_NODE_COUNTERS = 33

                        """

                        SHIP_TRANSPORT_COUNTERS = Enum.YLeaf(0, "SHIP_TRANSPORT_COUNTERS")

                        SHIP_SERVER_COUNTERS = Enum.YLeaf(1, "SHIP_SERVER_COUNTERS")

                        SHIP_CLIENT_LIB_COUNTERS = Enum.YLeaf(2, "SHIP_CLIENT_LIB_COUNTERS")

                        SHIP_REPLICATION_COUNTERS = Enum.YLeaf(3, "SHIP_REPLICATION_COUNTERS")

                        SHIP_READER_REPLICA_COUNTERS = Enum.YLeaf(4, "SHIP_READER_REPLICA_COUNTERS")

                        SHIP_WRITER_REPLICA_COUNTERS = Enum.YLeaf(5, "SHIP_WRITER_REPLICA_COUNTERS")

                        SHIP_TRANSPORT_COUNTERS_FAILOVER = Enum.YLeaf(6, "SHIP_TRANSPORT_COUNTERS_FAILOVER")

                        SHIP_SERVER_COUNTERS_FAILOVER = Enum.YLeaf(7, "SHIP_SERVER_COUNTERS_FAILOVER")

                        SHIP_CLIENT_LIB_COUNTERS_FAILOVER = Enum.YLeaf(8, "SHIP_CLIENT_LIB_COUNTERS_FAILOVER")

                        SHIP_REPLICATION_COUNTERS_FAILOVER = Enum.YLeaf(9, "SHIP_REPLICATION_COUNTERS_FAILOVER")

                        SHIP_TRANSPORT_ERRORS = Enum.YLeaf(10, "SHIP_TRANSPORT_ERRORS")

                        SHIP_SERVER_ERRORS = Enum.YLeaf(11, "SHIP_SERVER_ERRORS")

                        SHIP_CLIENT_LIB_ERRORS = Enum.YLeaf(12, "SHIP_CLIENT_LIB_ERRORS")

                        SHIP_REPLICATION_ERRORS = Enum.YLeaf(13, "SHIP_REPLICATION_ERRORS")

                        SHIP_READER_REPLICA_ERRORS = Enum.YLeaf(14, "SHIP_READER_REPLICA_ERRORS")

                        SHIP_WRITER_REPLICA_ERRORS = Enum.YLeaf(15, "SHIP_WRITER_REPLICA_ERRORS")

                        SHIP_TRANSPORT_ERRORS_FAILOVER = Enum.YLeaf(16, "SHIP_TRANSPORT_ERRORS_FAILOVER")

                        SHIP_SERVER_ERRORS_FAILOVER = Enum.YLeaf(17, "SHIP_SERVER_ERRORS_FAILOVER")

                        SHIP_CLIENT_LIB_ERRORS_FAILOVER = Enum.YLeaf(18, "SHIP_CLIENT_LIB_ERRORS_FAILOVER")

                        SHIP_REPLICATION_ERRORS_FAILOVER = Enum.YLeaf(19, "SHIP_REPLICATION_ERRORS_FAILOVER")

                        FEATURE_MA_COUNTERS = Enum.YLeaf(20, "FEATURE_MA_COUNTERS")

                        FEATURE_MA_COUNTERS_ERRORS = Enum.YLeaf(21, "FEATURE_MA_COUNTERS_ERRORS")

                        FEATURE_MA_COUNTERS_FAILOVER = Enum.YLeaf(22, "FEATURE_MA_COUNTERS_FAILOVER")

                        VIRTUAL_INTERFACE_MA_COUNTERS = Enum.YLeaf(23, "VIRTUAL_INTERFACE_MA_COUNTERS")

                        VIRTUAL_INTERFACE_MA_COUNTERS_ERRORS = Enum.YLeaf(24, "VIRTUAL_INTERFACE_MA_COUNTERS_ERRORS")

                        VIRTUAL_INTERFACE_MA_COUNTERS_FAILOVER = Enum.YLeaf(25, "VIRTUAL_INTERFACE_MA_COUNTERS_FAILOVER")

                        FEATURE_EA_COUNTERS = Enum.YLeaf(26, "FEATURE_EA_COUNTERS")

                        FEATURE_EA_COUNTERS_ERRORS = Enum.YLeaf(27, "FEATURE_EA_COUNTERS_ERRORS")

                        VIRTUAL_INTERFACE_EA_COUNTERS = Enum.YLeaf(28, "VIRTUAL_INTERFACE_EA_COUNTERS")

                        VIRTUAL_INTERFACE_EA_COUNTERS_ERRORS = Enum.YLeaf(29, "VIRTUAL_INTERFACE_EA_COUNTERS_ERRORS")

                        VIRTUAL_INTERFACE_EA_COUNTERS_FAILOVER = Enum.YLeaf(30, "VIRTUAL_INTERFACE_EA_COUNTERS_FAILOVER")

                        SHIP_HISTOGRAM_COUNTERS = Enum.YLeaf(31, "SHIP_HISTOGRAM_COUNTERS")

                        SHIP_WATERMARK_COUNTERS = Enum.YLeaf(32, "SHIP_WATERMARK_COUNTERS")

                        SHIP_NODE_COUNTERS = Enum.YLeaf(33, "SHIP_NODE_COUNTERS")



                    class Counter32b(Entity):
                        """
                        
                        
                        .. attribute:: counter_name  (key)
                        
                        	
                        	**type**\: str
                        
                        .. attribute:: counter_value
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: watermark
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: time_stamp
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: hist_info1
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hist_info2
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hist_info3
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hist_info4
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hist_info5
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hist_info6
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hist_info7
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hist_info8
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ship'
                        _revision = '2017-05-09'

                        def __init__(self):
                            super(Stat.ShipComp.Process.Client.Cat.Counter32b, self).__init__()

                            self.yang_name = "counter-32b"
                            self.yang_parent_name = "cat"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['counter_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('counter_name', (YLeaf(YType.str, 'counter-name'), ['str'])),
                                ('counter_value', (YLeaf(YType.uint32, 'counter-value'), ['int'])),
                                ('watermark', (YLeaf(YType.uint32, 'watermark'), ['int'])),
                                ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                                ('hist_info1', (YLeaf(YType.uint32, 'hist-info1'), ['int'])),
                                ('hist_info2', (YLeaf(YType.uint32, 'hist-info2'), ['int'])),
                                ('hist_info3', (YLeaf(YType.uint32, 'hist-info3'), ['int'])),
                                ('hist_info4', (YLeaf(YType.uint32, 'hist-info4'), ['int'])),
                                ('hist_info5', (YLeaf(YType.uint32, 'hist-info5'), ['int'])),
                                ('hist_info6', (YLeaf(YType.uint32, 'hist-info6'), ['int'])),
                                ('hist_info7', (YLeaf(YType.uint32, 'hist-info7'), ['int'])),
                                ('hist_info8', (YLeaf(YType.uint32, 'hist-info8'), ['int'])),
                            ])
                            self.counter_name = None
                            self.counter_value = None
                            self.watermark = None
                            self.time_stamp = None
                            self.hist_info1 = None
                            self.hist_info2 = None
                            self.hist_info3 = None
                            self.hist_info4 = None
                            self.hist_info5 = None
                            self.hist_info6 = None
                            self.hist_info7 = None
                            self.hist_info8 = None
                            self._segment_path = lambda: "counter-32b" + "[counter-name='" + str(self.counter_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Stat.ShipComp.Process.Client.Cat.Counter32b, ['counter_name', 'counter_value', 'watermark', 'time_stamp', 'hist_info1', 'hist_info2', 'hist_info3', 'hist_info4', 'hist_info5', 'hist_info6', 'hist_info7', 'hist_info8'], name, value)

    def clone_ptr(self):
        self._top_entity = Stat()
        return self._top_entity


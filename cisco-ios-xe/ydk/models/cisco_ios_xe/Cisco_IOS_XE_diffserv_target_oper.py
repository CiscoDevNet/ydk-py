""" Cisco_IOS_XE_diffserv_target_oper 

This module contains a collection of YANG definitions for
Diffserv operational dataCopyright (c) 2017 by Cisco Systems, Inc.All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Direction(Identity):
    """
    This is identity of traffic direction
    
    

    """

    _prefix = 'diffserv-target-oper'
    _revision = '2017-02-09'

    def __init__(self):
        super(Direction, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-diffserv-target-oper", "Cisco-IOS-XE-diffserv-target-oper", "Cisco-IOS-XE-diffserv-target-oper:direction")


class DiffservInterfacesState(Entity):
    """
    Interface configuration parameters.
    
    .. attribute:: diffserv_interface
    
    	The list of configured interfaces on the device
    	**type**\: list of  		 :py:class:`DiffservInterface <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.DiffservInterfacesState.DiffservInterface>`
    
    

    """

    _prefix = 'diffserv-target-oper'
    _revision = '2017-02-09'

    def __init__(self):
        super(DiffservInterfacesState, self).__init__()
        self._top_entity = None

        self.yang_name = "diffserv-interfaces-state"
        self.yang_parent_name = "Cisco-IOS-XE-diffserv-target-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("diffserv-interface", ("diffserv_interface", DiffservInterfacesState.DiffservInterface))])
        self._leafs = OrderedDict()

        self.diffserv_interface = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-diffserv-target-oper:diffserv-interfaces-state"

    def __setattr__(self, name, value):
        self._perform_setattr(DiffservInterfacesState, [], name, value)


    class DiffservInterface(Entity):
        """
        The list of configured interfaces on the device.
        
        .. attribute:: name  (key)
        
        	The name of the interface
        	**type**\: str
        
        .. attribute:: diffserv_target_entry
        
        	policy target for inbound or outbound direction
        	**type**\: list of  		 :py:class:`DiffservTargetEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.DiffservInterfacesState.DiffservInterface.DiffservTargetEntry>`
        
        

        """

        _prefix = 'diffserv-target-oper'
        _revision = '2017-02-09'

        def __init__(self):
            super(DiffservInterfacesState.DiffservInterface, self).__init__()

            self.yang_name = "diffserv-interface"
            self.yang_parent_name = "diffserv-interfaces-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("diffserv-target-entry", ("diffserv_target_entry", DiffservInterfacesState.DiffservInterface.DiffservTargetEntry))])
            self._leafs = OrderedDict([
                ('name', YLeaf(YType.str, 'name')),
            ])
            self.name = None

            self.diffserv_target_entry = YList(self)
            self._segment_path = lambda: "diffserv-interface" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-diffserv-target-oper:diffserv-interfaces-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DiffservInterfacesState.DiffservInterface, ['name'], name, value)


        class DiffservTargetEntry(Entity):
            """
            policy target for inbound or outbound direction
            
            .. attribute:: direction  (key)
            
            	Direction fo the traffic flow either inbound or outbound
            	**type**\:  :py:class:`Direction <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.Direction>`
            
            .. attribute:: policy_name  (key)
            
            	Policy entry name
            	**type**\: str
            
            .. attribute:: diffserv_target_classifier_statistics
            
            	Statistics for each Classifier Entry in a Policy
            	**type**\: list of  		 :py:class:`DiffservTargetClassifierStatistics <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics>`
            
            

            """

            _prefix = 'diffserv-target-oper'
            _revision = '2017-02-09'

            def __init__(self):
                super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry, self).__init__()

                self.yang_name = "diffserv-target-entry"
                self.yang_parent_name = "diffserv-interface"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['direction','policy_name']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("diffserv-target-classifier-statistics", ("diffserv_target_classifier_statistics", DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics))])
                self._leafs = OrderedDict([
                    ('direction', YLeaf(YType.identityref, 'direction')),
                    ('policy_name', YLeaf(YType.str, 'policy-name')),
                ])
                self.direction = None
                self.policy_name = None

                self.diffserv_target_classifier_statistics = YList(self)
                self._segment_path = lambda: "diffserv-target-entry" + "[direction='" + str(self.direction) + "']" + "[policy-name='" + str(self.policy_name) + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry, ['direction', 'policy_name'], name, value)


            class DiffservTargetClassifierStatistics(Entity):
                """
                Statistics for each Classifier Entry in a Policy
                
                .. attribute:: classifier_entry_name  (key)
                
                	Classifier Entry Name
                	**type**\: str
                
                .. attribute:: parent_path  (key)
                
                	Path of the Classifier Entry in a hierarchial policy 
                	**type**\: str
                
                .. attribute:: classifier_entry_statistics
                
                	 This group defines the classifier filter statistics of  each classifier entry         
                	**type**\:  :py:class:`ClassifierEntryStatistics <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics>`
                
                .. attribute:: meter_statistics
                
                	Meter statistics
                	**type**\: list of  		 :py:class:`MeterStatistics <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics>`
                
                .. attribute:: queuing_statistics
                
                	queue related statistics 
                	**type**\:  :py:class:`QueuingStatistics <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics>`
                
                

                """

                _prefix = 'diffserv-target-oper'
                _revision = '2017-02-09'

                def __init__(self):
                    super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics, self).__init__()

                    self.yang_name = "diffserv-target-classifier-statistics"
                    self.yang_parent_name = "diffserv-target-entry"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['classifier_entry_name','parent_path']
                    self._child_container_classes = OrderedDict([("classifier-entry-statistics", ("classifier_entry_statistics", DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics)), ("queuing-statistics", ("queuing_statistics", DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics))])
                    self._child_list_classes = OrderedDict([("meter-statistics", ("meter_statistics", DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics))])
                    self._leafs = OrderedDict([
                        ('classifier_entry_name', YLeaf(YType.str, 'classifier-entry-name')),
                        ('parent_path', YLeaf(YType.str, 'parent-path')),
                    ])
                    self.classifier_entry_name = None
                    self.parent_path = None

                    self.classifier_entry_statistics = DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics()
                    self.classifier_entry_statistics.parent = self
                    self._children_name_map["classifier_entry_statistics"] = "classifier-entry-statistics"
                    self._children_yang_names.add("classifier-entry-statistics")

                    self.queuing_statistics = DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics()
                    self.queuing_statistics.parent = self
                    self._children_name_map["queuing_statistics"] = "queuing-statistics"
                    self._children_yang_names.add("queuing-statistics")

                    self.meter_statistics = YList(self)
                    self._segment_path = lambda: "diffserv-target-classifier-statistics" + "[classifier-entry-name='" + str(self.classifier_entry_name) + "']" + "[parent-path='" + str(self.parent_path) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics, ['classifier_entry_name', 'parent_path'], name, value)


                class ClassifierEntryStatistics(Entity):
                    """
                    
                    This group defines the classifier filter statistics of 
                    each classifier entry
                           
                    
                    
                    .. attribute:: classified_pkts
                    
                    	 Number of total packets which filtered  to the classifier\-entry
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: classified_bytes
                    
                    	 Number of total bytes which filtered   to the classifier\-entry
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: classified_rate
                    
                    	 Rate of average data flow through the   classifier\-entry
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bits-per-second
                    
                    

                    """

                    _prefix = 'diffserv-target-oper'
                    _revision = '2017-02-09'

                    def __init__(self):
                        super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics, self).__init__()

                        self.yang_name = "classifier-entry-statistics"
                        self.yang_parent_name = "diffserv-target-classifier-statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('classified_pkts', YLeaf(YType.uint64, 'classified-pkts')),
                            ('classified_bytes', YLeaf(YType.uint64, 'classified-bytes')),
                            ('classified_rate', YLeaf(YType.uint64, 'classified-rate')),
                        ])
                        self.classified_pkts = None
                        self.classified_bytes = None
                        self.classified_rate = None
                        self._segment_path = lambda: "classifier-entry-statistics"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics, ['classified_pkts', 'classified_bytes', 'classified_rate'], name, value)


                class MeterStatistics(Entity):
                    """
                    Meter statistics
                    
                    .. attribute:: meter_id  (key)
                    
                    	Meter Identifier
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: meter_succeed_pkts
                    
                    	Number of packets which succeed the meter
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: meter_succeed_bytes
                    
                    	Bytes of packets which succeed the meter
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: meter_failed_pkts
                    
                    	Number of packets which failed the meter
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: meter_failed_bytes
                    
                    	Bytes of packets which failed the meter
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'diffserv-target-oper'
                    _revision = '2017-02-09'

                    def __init__(self):
                        super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics, self).__init__()

                        self.yang_name = "meter-statistics"
                        self.yang_parent_name = "diffserv-target-classifier-statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['meter_id']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('meter_id', YLeaf(YType.uint16, 'meter-id')),
                            ('meter_succeed_pkts', YLeaf(YType.uint64, 'meter-succeed-pkts')),
                            ('meter_succeed_bytes', YLeaf(YType.uint64, 'meter-succeed-bytes')),
                            ('meter_failed_pkts', YLeaf(YType.uint64, 'meter-failed-pkts')),
                            ('meter_failed_bytes', YLeaf(YType.uint64, 'meter-failed-bytes')),
                        ])
                        self.meter_id = None
                        self.meter_succeed_pkts = None
                        self.meter_succeed_bytes = None
                        self.meter_failed_pkts = None
                        self.meter_failed_bytes = None
                        self._segment_path = lambda: "meter-statistics" + "[meter-id='" + str(self.meter_id) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics, ['meter_id', 'meter_succeed_pkts', 'meter_succeed_bytes', 'meter_failed_pkts', 'meter_failed_bytes'], name, value)


                class QueuingStatistics(Entity):
                    """
                    queue related statistics 
                    
                    .. attribute:: output_pkts
                    
                    	Number of packets transmitted from queue 
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_bytes
                    
                    	Number of bytes transmitted from queue 
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: queue_size_pkts
                    
                    	Number of packets currently buffered 
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: queue_size_bytes
                    
                    	Number of bytes currently buffered 
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: drop_pkts
                    
                    	Total number of packets dropped 
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: drop_bytes
                    
                    	Total number of bytes dropped 
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: wred_stats
                    
                    	Container for WRED statistics
                    	**type**\:  :py:class:`WredStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats>`
                    
                    

                    """

                    _prefix = 'diffserv-target-oper'
                    _revision = '2017-02-09'

                    def __init__(self):
                        super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics, self).__init__()

                        self.yang_name = "queuing-statistics"
                        self.yang_parent_name = "diffserv-target-classifier-statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("wred-stats", ("wred_stats", DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('output_pkts', YLeaf(YType.uint64, 'output-pkts')),
                            ('output_bytes', YLeaf(YType.uint64, 'output-bytes')),
                            ('queue_size_pkts', YLeaf(YType.uint64, 'queue-size-pkts')),
                            ('queue_size_bytes', YLeaf(YType.uint64, 'queue-size-bytes')),
                            ('drop_pkts', YLeaf(YType.uint64, 'drop-pkts')),
                            ('drop_bytes', YLeaf(YType.uint64, 'drop-bytes')),
                        ])
                        self.output_pkts = None
                        self.output_bytes = None
                        self.queue_size_pkts = None
                        self.queue_size_bytes = None
                        self.drop_pkts = None
                        self.drop_bytes = None

                        self.wred_stats = DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats()
                        self.wred_stats.parent = self
                        self._children_name_map["wred_stats"] = "wred-stats"
                        self._children_yang_names.add("wred-stats")
                        self._segment_path = lambda: "queuing-statistics"

                    def __setattr__(self, name, value):
                        self._perform_setattr(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics, ['output_pkts', 'output_bytes', 'queue_size_pkts', 'queue_size_bytes', 'drop_pkts', 'drop_bytes'], name, value)


                    class WredStats(Entity):
                        """
                        Container for WRED statistics
                        
                        .. attribute:: early_drop_pkts
                        
                        	Early drop packets 
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: early_drop_bytes
                        
                        	Early drop bytes 
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'diffserv-target-oper'
                        _revision = '2017-02-09'

                        def __init__(self):
                            super(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats, self).__init__()

                            self.yang_name = "wred-stats"
                            self.yang_parent_name = "queuing-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('early_drop_pkts', YLeaf(YType.uint64, 'early-drop-pkts')),
                                ('early_drop_bytes', YLeaf(YType.uint64, 'early-drop-bytes')),
                            ])
                            self.early_drop_pkts = None
                            self.early_drop_bytes = None
                            self._segment_path = lambda: "wred-stats"

                        def __setattr__(self, name, value):
                            self._perform_setattr(DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats, ['early_drop_pkts', 'early_drop_bytes'], name, value)

    def clone_ptr(self):
        self._top_entity = DiffservInterfacesState()
        return self._top_entity

class Inbound(Identity):
    """
    Direction of traffic coming into the network entry
    
    

    """

    _prefix = 'diffserv-target-oper'
    _revision = '2017-02-09'

    def __init__(self):
        super(Inbound, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-diffserv-target-oper", "Cisco-IOS-XE-diffserv-target-oper", "Cisco-IOS-XE-diffserv-target-oper:inbound")


class Outbound(Identity):
    """
    Direction of traffic going out of the network entry
    
    

    """

    _prefix = 'diffserv-target-oper'
    _revision = '2017-02-09'

    def __init__(self):
        super(Outbound, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-diffserv-target-oper", "Cisco-IOS-XE-diffserv-target-oper", "Cisco-IOS-XE-diffserv-target-oper:outbound")



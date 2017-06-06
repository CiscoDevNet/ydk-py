""" Cisco_IOS_XE_diffserv_target_oper 

This module contains a collection of YANG definitions for
Diffserv operational dataCopyright (c) 2017 by Cisco Systems, Inc.All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class DirectionIdentity(object):
    """
    This is identity of traffic direction
    
    

    """

    _prefix = 'diffserv-target-oper'
    _revision = '2017-02-09'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_diffserv_target_oper as meta
        return meta._meta_table['DirectionIdentity']['meta_info']


class DiffservInterfacesState(object):
    """
    Interface configuration parameters.
    
    .. attribute:: diffserv_interface
    
    	The list of configured interfaces on the device
    	**type**\: list of    :py:class:`DiffservInterface <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.DiffservInterfacesState.DiffservInterface>`
    
    

    """

    _prefix = 'diffserv-target-oper'
    _revision = '2017-02-09'

    def __init__(self):
        self.diffserv_interface = YList()
        self.diffserv_interface.parent = self
        self.diffserv_interface.name = 'diffserv_interface'


    class DiffservInterface(object):
        """
        The list of configured interfaces on the device.
        
        .. attribute:: name  <key>
        
        	The name of the interface
        	**type**\:  str
        
        .. attribute:: diffserv_target_entry
        
        	policy target for inbound or outbound direction
        	**type**\: list of    :py:class:`DiffservTargetEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.DiffservInterfacesState.DiffservInterface.DiffservTargetEntry>`
        
        

        """

        _prefix = 'diffserv-target-oper'
        _revision = '2017-02-09'

        def __init__(self):
            self.parent = None
            self.name = None
            self.diffserv_target_entry = YList()
            self.diffserv_target_entry.parent = self
            self.diffserv_target_entry.name = 'diffserv_target_entry'


        class DiffservTargetEntry(object):
            """
            policy target for inbound or outbound direction
            
            .. attribute:: direction  <key>
            
            	Direction fo the traffic flow either inbound or outbound
            	**type**\:   :py:class:`DirectionIdentity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.DirectionIdentity>`
            
            .. attribute:: policy_name  <key>
            
            	Policy entry name
            	**type**\:  str
            
            .. attribute:: diffserv_target_classifier_statistics
            
            	Statistics for each Classifier Entry in a Policy
            	**type**\: list of    :py:class:`DiffservTargetClassifierStatistics <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics>`
            
            

            """

            _prefix = 'diffserv-target-oper'
            _revision = '2017-02-09'

            def __init__(self):
                self.parent = None
                self.direction = None
                self.policy_name = None
                self.diffserv_target_classifier_statistics = YList()
                self.diffserv_target_classifier_statistics.parent = self
                self.diffserv_target_classifier_statistics.name = 'diffserv_target_classifier_statistics'


            class DiffservTargetClassifierStatistics(object):
                """
                Statistics for each Classifier Entry in a Policy
                
                .. attribute:: classifier_entry_name  <key>
                
                	Classifier Entry Name
                	**type**\:  str
                
                .. attribute:: parent_path  <key>
                
                	Path of the Classifier Entry in a hierarchial policy 
                	**type**\:  str
                
                .. attribute:: classifier_entry_statistics
                
                	 This group defines the classifier filter statistics of  each classifier entry         
                	**type**\:   :py:class:`ClassifierEntryStatistics <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics>`
                
                .. attribute:: meter_statistics
                
                	Meter statistics
                	**type**\: list of    :py:class:`MeterStatistics <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics>`
                
                .. attribute:: queuing_statistics
                
                	queue related statistics 
                	**type**\:   :py:class:`QueuingStatistics <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics>`
                
                

                """

                _prefix = 'diffserv-target-oper'
                _revision = '2017-02-09'

                def __init__(self):
                    self.parent = None
                    self.classifier_entry_name = None
                    self.parent_path = None
                    self.classifier_entry_statistics = DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics()
                    self.classifier_entry_statistics.parent = self
                    self.meter_statistics = YList()
                    self.meter_statistics.parent = self
                    self.meter_statistics.name = 'meter_statistics'
                    self.queuing_statistics = DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics()
                    self.queuing_statistics.parent = self


                class ClassifierEntryStatistics(object):
                    """
                    
                    This group defines the classifier filter statistics of 
                    each classifier entry
                           
                    
                    
                    .. attribute:: classified_bytes
                    
                    	 Number of total bytes which filtered   to the classifier\-entry
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: classified_pkts
                    
                    	 Number of total packets which filtered  to the classifier\-entry
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: classified_rate
                    
                    	 Rate of average data flow through the   classifier\-entry
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bits-per-second
                    
                    

                    """

                    _prefix = 'diffserv-target-oper'
                    _revision = '2017-02-09'

                    def __init__(self):
                        self.parent = None
                        self.classified_bytes = None
                        self.classified_pkts = None
                        self.classified_rate = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-diffserv-target-oper:classifier-entry-statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.classified_bytes is not None:
                            return True

                        if self.classified_pkts is not None:
                            return True

                        if self.classified_rate is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_diffserv_target_oper as meta
                        return meta._meta_table['DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.ClassifierEntryStatistics']['meta_info']


                class MeterStatistics(object):
                    """
                    Meter statistics
                    
                    .. attribute:: meter_id  <key>
                    
                    	Meter Identifier
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: meter_failed_bytes
                    
                    	Bytes of packets which failed the meter
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: meter_failed_pkts
                    
                    	Number of packets which failed the meter
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: meter_succeed_bytes
                    
                    	Bytes of packets which succeed the meter
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: meter_succeed_pkts
                    
                    	Number of packets which succeed the meter
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'diffserv-target-oper'
                    _revision = '2017-02-09'

                    def __init__(self):
                        self.parent = None
                        self.meter_id = None
                        self.meter_failed_bytes = None
                        self.meter_failed_pkts = None
                        self.meter_succeed_bytes = None
                        self.meter_succeed_pkts = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.meter_id is None:
                            raise YPYModelError('Key property meter_id is None')

                        return self.parent._common_path +'/Cisco-IOS-XE-diffserv-target-oper:meter-statistics[Cisco-IOS-XE-diffserv-target-oper:meter-id = ' + str(self.meter_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.meter_id is not None:
                            return True

                        if self.meter_failed_bytes is not None:
                            return True

                        if self.meter_failed_pkts is not None:
                            return True

                        if self.meter_succeed_bytes is not None:
                            return True

                        if self.meter_succeed_pkts is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_diffserv_target_oper as meta
                        return meta._meta_table['DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.MeterStatistics']['meta_info']


                class QueuingStatistics(object):
                    """
                    queue related statistics 
                    
                    .. attribute:: drop_bytes
                    
                    	Total number of bytes dropped 
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: drop_pkts
                    
                    	Total number of packets dropped 
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_bytes
                    
                    	Number of bytes transmitted from queue 
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_pkts
                    
                    	Number of packets transmitted from queue 
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: queue_size_bytes
                    
                    	Number of bytes currently buffered 
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: queue_size_pkts
                    
                    	Number of packets currently buffered 
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: wred_stats
                    
                    	Container for WRED statistics
                    	**type**\:   :py:class:`WredStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_diffserv_target_oper.DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats>`
                    
                    

                    """

                    _prefix = 'diffserv-target-oper'
                    _revision = '2017-02-09'

                    def __init__(self):
                        self.parent = None
                        self.drop_bytes = None
                        self.drop_pkts = None
                        self.output_bytes = None
                        self.output_pkts = None
                        self.queue_size_bytes = None
                        self.queue_size_pkts = None
                        self.wred_stats = DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats()
                        self.wred_stats.parent = self


                    class WredStats(object):
                        """
                        Container for WRED statistics
                        
                        .. attribute:: early_drop_bytes
                        
                        	Early drop bytes 
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: early_drop_pkts
                        
                        	Early drop packets 
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'diffserv-target-oper'
                        _revision = '2017-02-09'

                        def __init__(self):
                            self.parent = None
                            self.early_drop_bytes = None
                            self.early_drop_pkts = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XE-diffserv-target-oper:wred-stats'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.early_drop_bytes is not None:
                                return True

                            if self.early_drop_pkts is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_diffserv_target_oper as meta
                            return meta._meta_table['DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics.WredStats']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-diffserv-target-oper:queuing-statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.drop_bytes is not None:
                            return True

                        if self.drop_pkts is not None:
                            return True

                        if self.output_bytes is not None:
                            return True

                        if self.output_pkts is not None:
                            return True

                        if self.queue_size_bytes is not None:
                            return True

                        if self.queue_size_pkts is not None:
                            return True

                        if self.wred_stats is not None and self.wred_stats._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_diffserv_target_oper as meta
                        return meta._meta_table['DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics.QueuingStatistics']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.classifier_entry_name is None:
                        raise YPYModelError('Key property classifier_entry_name is None')
                    if self.parent_path is None:
                        raise YPYModelError('Key property parent_path is None')

                    return self.parent._common_path +'/Cisco-IOS-XE-diffserv-target-oper:diffserv-target-classifier-statistics[Cisco-IOS-XE-diffserv-target-oper:classifier-entry-name = ' + str(self.classifier_entry_name) + '][Cisco-IOS-XE-diffserv-target-oper:parent-path = ' + str(self.parent_path) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.classifier_entry_name is not None:
                        return True

                    if self.parent_path is not None:
                        return True

                    if self.classifier_entry_statistics is not None and self.classifier_entry_statistics._has_data():
                        return True

                    if self.meter_statistics is not None:
                        for child_ref in self.meter_statistics:
                            if child_ref._has_data():
                                return True

                    if self.queuing_statistics is not None and self.queuing_statistics._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_diffserv_target_oper as meta
                    return meta._meta_table['DiffservInterfacesState.DiffservInterface.DiffservTargetEntry.DiffservTargetClassifierStatistics']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')
                if self.direction is None:
                    raise YPYModelError('Key property direction is None')
                if self.policy_name is None:
                    raise YPYModelError('Key property policy_name is None')

                return self.parent._common_path +'/Cisco-IOS-XE-diffserv-target-oper:diffserv-target-entry[Cisco-IOS-XE-diffserv-target-oper:direction = ' + str(self.direction) + '][Cisco-IOS-XE-diffserv-target-oper:policy-name = ' + str(self.policy_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.direction is not None:
                    return True

                if self.policy_name is not None:
                    return True

                if self.diffserv_target_classifier_statistics is not None:
                    for child_ref in self.diffserv_target_classifier_statistics:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_diffserv_target_oper as meta
                return meta._meta_table['DiffservInterfacesState.DiffservInterface.DiffservTargetEntry']['meta_info']

        @property
        def _common_path(self):
            if self.name is None:
                raise YPYModelError('Key property name is None')

            return '/Cisco-IOS-XE-diffserv-target-oper:diffserv-interfaces-state/Cisco-IOS-XE-diffserv-target-oper:diffserv-interface[Cisco-IOS-XE-diffserv-target-oper:name = ' + str(self.name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.name is not None:
                return True

            if self.diffserv_target_entry is not None:
                for child_ref in self.diffserv_target_entry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_diffserv_target_oper as meta
            return meta._meta_table['DiffservInterfacesState.DiffservInterface']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-diffserv-target-oper:diffserv-interfaces-state'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.diffserv_interface is not None:
            for child_ref in self.diffserv_interface:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_diffserv_target_oper as meta
        return meta._meta_table['DiffservInterfacesState']['meta_info']


class InboundIdentity(DirectionIdentity):
    """
    Direction of traffic coming into the network entry
    
    

    """

    _prefix = 'diffserv-target-oper'
    _revision = '2017-02-09'

    def __init__(self):
        DirectionIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_diffserv_target_oper as meta
        return meta._meta_table['InboundIdentity']['meta_info']


class OutboundIdentity(DirectionIdentity):
    """
    Direction of traffic going out of the network entry
    
    

    """

    _prefix = 'diffserv-target-oper'
    _revision = '2017-02-09'

    def __init__(self):
        DirectionIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_diffserv_target_oper as meta
        return meta._meta_table['OutboundIdentity']['meta_info']



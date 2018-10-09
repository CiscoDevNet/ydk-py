""" Cisco_IOS_XE_utd_oper 

This module contains a collection of YANG definitions for
monitoring Unified Threat Defense (UTD).
Copyright (c) 2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class UtdOperStatusVal(Enum):
    """
    UtdOperStatusVal (Enum Class)

    Unified Threat Defense (UTD) operational status

    .. data:: utd_oper_status_unknown = 0

    	Unified Threat Defense (UTD) operational status is unknown - Unable to determine status

    .. data:: utd_oper_status_green = 1

    	Unified Threat Defense (UTD) operational status is green - Working as expected

    .. data:: utd_oper_status_yellow = 2

    	Unified Threat Defense (UTD) operational status is yellow - Minor problem

    .. data:: utd_oper_status_red = 3

    	Unified Threat Defense (UTD) operational status is red - Major problem

    .. data:: utd_oper_status_down = 4

    	Unified Threat Defense (UTD) operational status is down - Communication has been lost

    """

    utd_oper_status_unknown = Enum.YLeaf(0, "utd-oper-status-unknown")

    utd_oper_status_green = Enum.YLeaf(1, "utd-oper-status-green")

    utd_oper_status_yellow = Enum.YLeaf(2, "utd-oper-status-yellow")

    utd_oper_status_red = Enum.YLeaf(3, "utd-oper-status-red")

    utd_oper_status_down = Enum.YLeaf(4, "utd-oper-status-down")



class UtdOperData(Entity):
    """
    Unified Threat Defense (UTD) operational data
    
    .. attribute:: utd_engine_status
    
    	Unified Threat Defense (UTD) engine status
    	**type**\:  :py:class:`UtdEngineStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_utd_oper.UtdOperData.UtdEngineStatus>`
    
    	**presence node**\: True
    
    .. attribute:: utd_ips_update_status
    
    	Unified Threat Defense (UTD) Intrusion Prevention System (IPS) update status
    	**type**\:  :py:class:`UtdIpsUpdateStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_utd_oper.UtdOperData.UtdIpsUpdateStatus>`
    
    	**presence node**\: True
    
    .. attribute:: utd_urlf_update_status
    
    	Unified Threat Defense (UTD) URL\-Filtering (URLF) update status
    	**type**\:  :py:class:`UtdUrlfUpdateStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_utd_oper.UtdOperData.UtdUrlfUpdateStatus>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'utd-ios-xe-oper'
    _revision = '2018-04-04'

    def __init__(self):
        super(UtdOperData, self).__init__()
        self._top_entity = None

        self.yang_name = "utd-oper-data"
        self.yang_parent_name = "Cisco-IOS-XE-utd-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("utd-engine-status", ("utd_engine_status", UtdOperData.UtdEngineStatus)), ("utd-ips-update-status", ("utd_ips_update_status", UtdOperData.UtdIpsUpdateStatus)), ("utd-urlf-update-status", ("utd_urlf_update_status", UtdOperData.UtdUrlfUpdateStatus))])
        self._leafs = OrderedDict()

        self.utd_engine_status = None
        self._children_name_map["utd_engine_status"] = "utd-engine-status"

        self.utd_ips_update_status = None
        self._children_name_map["utd_ips_update_status"] = "utd-ips-update-status"

        self.utd_urlf_update_status = None
        self._children_name_map["utd_urlf_update_status"] = "utd-urlf-update-status"
        self._segment_path = lambda: "Cisco-IOS-XE-utd-oper:utd-oper-data"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(UtdOperData, [], name, value)


    class UtdEngineStatus(Entity):
        """
        Unified Threat Defense (UTD) engine status
        
        .. attribute:: version
        
        	Engine version
        	**type**\: str
        
        .. attribute:: profile
        
        	Profile
        	**type**\: str
        
        .. attribute:: status
        
        	Overall status
        	**type**\:  :py:class:`UtdOperStatusVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_utd_oper.UtdOperStatusVal>`
        
        .. attribute:: reason
        
        	Overall status reason
        	**type**\: str
        
        .. attribute:: memory_usage
        
        	Percentage of memory used
        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
        
        	**range:** \-92233720368547758.08..92233720368547758.07
        
        	**units**\: percent
        
        .. attribute:: memory_status
        
        	Status of memory usage
        	**type**\:  :py:class:`UtdOperStatusVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_utd_oper.UtdOperStatusVal>`
        
        .. attribute:: utd_engine_instance_status
        
        	Status of engine instances
        	**type**\: list of  		 :py:class:`UtdEngineInstanceStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_utd_oper.UtdOperData.UtdEngineStatus.UtdEngineInstanceStatus>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'utd-ios-xe-oper'
        _revision = '2018-04-04'

        def __init__(self):
            super(UtdOperData.UtdEngineStatus, self).__init__()

            self.yang_name = "utd-engine-status"
            self.yang_parent_name = "utd-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("utd-engine-instance-status", ("utd_engine_instance_status", UtdOperData.UtdEngineStatus.UtdEngineInstanceStatus))])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                ('profile', (YLeaf(YType.str, 'profile'), ['str'])),
                ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_utd_oper', 'UtdOperStatusVal', '')])),
                ('reason', (YLeaf(YType.str, 'reason'), ['str'])),
                ('memory_usage', (YLeaf(YType.str, 'memory-usage'), ['Decimal64'])),
                ('memory_status', (YLeaf(YType.enumeration, 'memory-status'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_utd_oper', 'UtdOperStatusVal', '')])),
            ])
            self.version = None
            self.profile = None
            self.status = None
            self.reason = None
            self.memory_usage = None
            self.memory_status = None

            self.utd_engine_instance_status = YList(self)
            self._segment_path = lambda: "utd-engine-status"
            self._absolute_path = lambda: "Cisco-IOS-XE-utd-oper:utd-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(UtdOperData.UtdEngineStatus, ['version', 'profile', 'status', 'reason', 'memory_usage', 'memory_status'], name, value)


        class UtdEngineInstanceStatus(Entity):
            """
            Status of engine instances
            
            .. attribute:: id  (key)
            
            	Engine instance ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: running
            
            	Engine instance running
            	**type**\: bool
            
            .. attribute:: status
            
            	Engine instance status
            	**type**\:  :py:class:`UtdOperStatusVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_utd_oper.UtdOperStatusVal>`
            
            .. attribute:: reason
            
            	Engine instance status reason
            	**type**\: str
            
            

            """

            _prefix = 'utd-ios-xe-oper'
            _revision = '2018-04-04'

            def __init__(self):
                super(UtdOperData.UtdEngineStatus.UtdEngineInstanceStatus, self).__init__()

                self.yang_name = "utd-engine-instance-status"
                self.yang_parent_name = "utd-engine-status"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['id']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                    ('running', (YLeaf(YType.boolean, 'running'), ['bool'])),
                    ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_utd_oper', 'UtdOperStatusVal', '')])),
                    ('reason', (YLeaf(YType.str, 'reason'), ['str'])),
                ])
                self.id = None
                self.running = None
                self.status = None
                self.reason = None
                self._segment_path = lambda: "utd-engine-instance-status" + "[id='" + str(self.id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-utd-oper:utd-oper-data/utd-engine-status/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(UtdOperData.UtdEngineStatus.UtdEngineInstanceStatus, ['id', 'running', 'status', 'reason'], name, value)


    class UtdIpsUpdateStatus(Entity):
        """
        Unified Threat Defense (UTD) Intrusion Prevention System (IPS) update status
        
        .. attribute:: ips_update_status
        
        	Intrusion Prevention System (IPS) update status
        	**type**\:  :py:class:`IpsUpdateStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_utd_oper.UtdOperData.UtdIpsUpdateStatus.IpsUpdateStatus>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'utd-ios-xe-oper'
        _revision = '2018-04-04'

        def __init__(self):
            super(UtdOperData.UtdIpsUpdateStatus, self).__init__()

            self.yang_name = "utd-ips-update-status"
            self.yang_parent_name = "utd-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ips-update-status", ("ips_update_status", UtdOperData.UtdIpsUpdateStatus.IpsUpdateStatus))])
            self.is_presence_container = True
            self._leafs = OrderedDict()

            self.ips_update_status = UtdOperData.UtdIpsUpdateStatus.IpsUpdateStatus()
            self.ips_update_status.parent = self
            self._children_name_map["ips_update_status"] = "ips-update-status"
            self._segment_path = lambda: "utd-ips-update-status"
            self._absolute_path = lambda: "Cisco-IOS-XE-utd-oper:utd-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(UtdOperData.UtdIpsUpdateStatus, [], name, value)


        class IpsUpdateStatus(Entity):
            """
            Intrusion Prevention System (IPS) update status
            
            .. attribute:: version
            
            	Version
            	**type**\: str
            
            .. attribute:: last_update_time
            
            	Time of last attempted update
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: last_update_status
            
            	Status of last attempted update
            	**type**\:  :py:class:`UtdUpdateStatusVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_utd_common_oper.UtdUpdateStatusVal>`
            
            .. attribute:: last_update_reason
            
            	Reason for last attempted update failure
            	**type**\: str
            
            .. attribute:: last_successful_update_time
            
            	Time of last successful update
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            

            """

            _prefix = 'utd-ios-xe-oper'
            _revision = '2018-04-04'

            def __init__(self):
                super(UtdOperData.UtdIpsUpdateStatus.IpsUpdateStatus, self).__init__()

                self.yang_name = "ips-update-status"
                self.yang_parent_name = "utd-ips-update-status"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('version', (YLeaf(YType.str, 'version'), ['str'])),
                    ('last_update_time', (YLeaf(YType.str, 'last-update-time'), ['str'])),
                    ('last_update_status', (YLeaf(YType.enumeration, 'last-update-status'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_utd_common_oper', 'UtdUpdateStatusVal', '')])),
                    ('last_update_reason', (YLeaf(YType.str, 'last-update-reason'), ['str'])),
                    ('last_successful_update_time', (YLeaf(YType.str, 'last-successful-update-time'), ['str'])),
                ])
                self.version = None
                self.last_update_time = None
                self.last_update_status = None
                self.last_update_reason = None
                self.last_successful_update_time = None
                self._segment_path = lambda: "ips-update-status"
                self._absolute_path = lambda: "Cisco-IOS-XE-utd-oper:utd-oper-data/utd-ips-update-status/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(UtdOperData.UtdIpsUpdateStatus.IpsUpdateStatus, ['version', 'last_update_time', 'last_update_status', 'last_update_reason', 'last_successful_update_time'], name, value)


    class UtdUrlfUpdateStatus(Entity):
        """
        Unified Threat Defense (UTD) URL\-Filtering (URLF) update status
        
        .. attribute:: urlf_update_status
        
        	URL\-Filtering (URLF) update status
        	**type**\:  :py:class:`UrlfUpdateStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_utd_oper.UtdOperData.UtdUrlfUpdateStatus.UrlfUpdateStatus>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'utd-ios-xe-oper'
        _revision = '2018-04-04'

        def __init__(self):
            super(UtdOperData.UtdUrlfUpdateStatus, self).__init__()

            self.yang_name = "utd-urlf-update-status"
            self.yang_parent_name = "utd-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("urlf-update-status", ("urlf_update_status", UtdOperData.UtdUrlfUpdateStatus.UrlfUpdateStatus))])
            self.is_presence_container = True
            self._leafs = OrderedDict()

            self.urlf_update_status = UtdOperData.UtdUrlfUpdateStatus.UrlfUpdateStatus()
            self.urlf_update_status.parent = self
            self._children_name_map["urlf_update_status"] = "urlf-update-status"
            self._segment_path = lambda: "utd-urlf-update-status"
            self._absolute_path = lambda: "Cisco-IOS-XE-utd-oper:utd-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(UtdOperData.UtdUrlfUpdateStatus, [], name, value)


        class UrlfUpdateStatus(Entity):
            """
            URL\-Filtering (URLF) update status
            
            .. attribute:: version
            
            	Version
            	**type**\: str
            
            .. attribute:: last_update_time
            
            	Time of last attempted update
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: last_update_status
            
            	Status of last attempted update
            	**type**\:  :py:class:`UtdUpdateStatusVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_utd_common_oper.UtdUpdateStatusVal>`
            
            .. attribute:: last_update_reason
            
            	Reason for last attempted update failure
            	**type**\: str
            
            .. attribute:: last_successful_update_time
            
            	Time of last successful update
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            

            """

            _prefix = 'utd-ios-xe-oper'
            _revision = '2018-04-04'

            def __init__(self):
                super(UtdOperData.UtdUrlfUpdateStatus.UrlfUpdateStatus, self).__init__()

                self.yang_name = "urlf-update-status"
                self.yang_parent_name = "utd-urlf-update-status"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('version', (YLeaf(YType.str, 'version'), ['str'])),
                    ('last_update_time', (YLeaf(YType.str, 'last-update-time'), ['str'])),
                    ('last_update_status', (YLeaf(YType.enumeration, 'last-update-status'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_utd_common_oper', 'UtdUpdateStatusVal', '')])),
                    ('last_update_reason', (YLeaf(YType.str, 'last-update-reason'), ['str'])),
                    ('last_successful_update_time', (YLeaf(YType.str, 'last-successful-update-time'), ['str'])),
                ])
                self.version = None
                self.last_update_time = None
                self.last_update_status = None
                self.last_update_reason = None
                self.last_successful_update_time = None
                self._segment_path = lambda: "urlf-update-status"
                self._absolute_path = lambda: "Cisco-IOS-XE-utd-oper:utd-oper-data/utd-urlf-update-status/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(UtdOperData.UtdUrlfUpdateStatus.UrlfUpdateStatus, ['version', 'last_update_time', 'last_update_status', 'last_update_reason', 'last_successful_update_time'], name, value)

    def clone_ptr(self):
        self._top_entity = UtdOperData()
        return self._top_entity


""" Cisco_IOS_XR_aaa_locald_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-locald package operational data.

This module contains definitions
for the following management objects\:
  aaa\: AAA operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Aaa(Entity):
    """
    AAA operational data
    
    .. attribute:: all_tasks
    
    	All tasks supported by system
    	**type**\:   :py:class:`AllTasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.AllTasks>`
    
    .. attribute:: authen_method
    
    	Current users authentication method
    	**type**\:   :py:class:`AuthenMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.AuthenMethod>`
    
    .. attribute:: current_usergroup
    
    	Specific Usergroup Information
    	**type**\:   :py:class:`CurrentUsergroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.CurrentUsergroup>`
    
    .. attribute:: currentuser_detail
    
    	Current user specific details
    	**type**\:   :py:class:`CurrentuserDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.CurrentuserDetail>`
    
    .. attribute:: diameter
    
    	Diameter operational data
    	**type**\:   :py:class:`Diameter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter>`
    
    .. attribute:: radius
    
    	RADIUS operational data
    	**type**\:   :py:class:`Radius <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius>`
    
    .. attribute:: tacacs
    
    	TACACS operational data
    	**type**\:   :py:class:`Tacacs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs>`
    
    .. attribute:: task_map
    
    	Task map of current user
    	**type**\:   :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.TaskMap>`
    
    .. attribute:: taskgroups
    
    	Individual taskgroups container
    	**type**\:   :py:class:`Taskgroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups>`
    
    .. attribute:: usergroups
    
    	Container for individual usergroup Information
    	**type**\:   :py:class:`Usergroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups>`
    
    .. attribute:: users
    
    	Container for individual local user information
    	**type**\:   :py:class:`Users <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users>`
    
    

    """

    _prefix = 'aaa-locald-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Aaa, self).__init__()
        self._top_entity = None

        self.yang_name = "aaa"
        self.yang_parent_name = "Cisco-IOS-XR-aaa-locald-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"all-tasks" : ("all_tasks", Aaa.AllTasks), "authen-method" : ("authen_method", Aaa.AuthenMethod), "current-usergroup" : ("current_usergroup", Aaa.CurrentUsergroup), "currentuser-detail" : ("currentuser_detail", Aaa.CurrentuserDetail), "diameter" : ("diameter", Aaa.Diameter), "radius" : ("radius", Aaa.Radius), "tacacs" : ("tacacs", Aaa.Tacacs), "task-map" : ("task_map", Aaa.TaskMap), "taskgroups" : ("taskgroups", Aaa.Taskgroups), "usergroups" : ("usergroups", Aaa.Usergroups), "users" : ("users", Aaa.Users)}
        self._child_list_classes = {}

        self.all_tasks = Aaa.AllTasks()
        self.all_tasks.parent = self
        self._children_name_map["all_tasks"] = "all-tasks"
        self._children_yang_names.add("all-tasks")

        self.authen_method = Aaa.AuthenMethod()
        self.authen_method.parent = self
        self._children_name_map["authen_method"] = "authen-method"
        self._children_yang_names.add("authen-method")

        self.current_usergroup = Aaa.CurrentUsergroup()
        self.current_usergroup.parent = self
        self._children_name_map["current_usergroup"] = "current-usergroup"
        self._children_yang_names.add("current-usergroup")

        self.currentuser_detail = Aaa.CurrentuserDetail()
        self.currentuser_detail.parent = self
        self._children_name_map["currentuser_detail"] = "currentuser-detail"
        self._children_yang_names.add("currentuser-detail")

        self.diameter = Aaa.Diameter()
        self.diameter.parent = self
        self._children_name_map["diameter"] = "diameter"
        self._children_yang_names.add("diameter")

        self.radius = Aaa.Radius()
        self.radius.parent = self
        self._children_name_map["radius"] = "radius"
        self._children_yang_names.add("radius")

        self.tacacs = Aaa.Tacacs()
        self.tacacs.parent = self
        self._children_name_map["tacacs"] = "tacacs"
        self._children_yang_names.add("tacacs")

        self.task_map = Aaa.TaskMap()
        self.task_map.parent = self
        self._children_name_map["task_map"] = "task-map"
        self._children_yang_names.add("task-map")

        self.taskgroups = Aaa.Taskgroups()
        self.taskgroups.parent = self
        self._children_name_map["taskgroups"] = "taskgroups"
        self._children_yang_names.add("taskgroups")

        self.usergroups = Aaa.Usergroups()
        self.usergroups.parent = self
        self._children_name_map["usergroups"] = "usergroups"
        self._children_yang_names.add("usergroups")

        self.users = Aaa.Users()
        self.users.parent = self
        self._children_name_map["users"] = "users"
        self._children_yang_names.add("users")
        self._segment_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa"


    class AllTasks(Entity):
        """
        All tasks supported by system
        
        .. attribute:: task_id
        
        	Names of available task\-ids
        	**type**\:  list of str
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.AllTasks, self).__init__()

            self.yang_name = "all-tasks"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.task_id = YLeafList(YType.str, "task-id")
            self._segment_path = lambda: "all-tasks"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.AllTasks, ['task_id'], name, value)


    class AuthenMethod(Entity):
        """
        Current users authentication method
        
        .. attribute:: authenmethod
        
        	Authentication method
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: name
        
        	Name of the usergroup
        	**type**\:  str
        
        .. attribute:: taskmap
        
        	Task map details
        	**type**\:  list of str
        
        .. attribute:: usergroup
        
        	Component usergroups
        	**type**\:  list of str
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.AuthenMethod, self).__init__()

            self.yang_name = "authen-method"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.authenmethod = YLeaf(YType.int32, "authenmethod")

            self.name = YLeaf(YType.str, "name")

            self.taskmap = YLeafList(YType.str, "taskmap")

            self.usergroup = YLeafList(YType.str, "usergroup")
            self._segment_path = lambda: "authen-method"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.AuthenMethod, ['authenmethod', 'name', 'taskmap', 'usergroup'], name, value)


    class CurrentUsergroup(Entity):
        """
        Specific Usergroup Information
        
        .. attribute:: authenmethod
        
        	Authentication method
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: name
        
        	Name of the usergroup
        	**type**\:  str
        
        .. attribute:: taskmap
        
        	Task map details
        	**type**\:  list of str
        
        .. attribute:: usergroup
        
        	Component usergroups
        	**type**\:  list of str
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.CurrentUsergroup, self).__init__()

            self.yang_name = "current-usergroup"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.authenmethod = YLeaf(YType.int32, "authenmethod")

            self.name = YLeaf(YType.str, "name")

            self.taskmap = YLeafList(YType.str, "taskmap")

            self.usergroup = YLeafList(YType.str, "usergroup")
            self._segment_path = lambda: "current-usergroup"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.CurrentUsergroup, ['authenmethod', 'name', 'taskmap', 'usergroup'], name, value)


    class CurrentuserDetail(Entity):
        """
        Current user specific details
        
        .. attribute:: authenmethod
        
        	Authentication method
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: name
        
        	Name of the usergroup
        	**type**\:  str
        
        .. attribute:: taskmap
        
        	Task map details
        	**type**\:  list of str
        
        .. attribute:: usergroup
        
        	Component usergroups
        	**type**\:  list of str
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.CurrentuserDetail, self).__init__()

            self.yang_name = "currentuser-detail"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.authenmethod = YLeaf(YType.int32, "authenmethod")

            self.name = YLeaf(YType.str, "name")

            self.taskmap = YLeafList(YType.str, "taskmap")

            self.usergroup = YLeafList(YType.str, "usergroup")
            self._segment_path = lambda: "currentuser-detail"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.CurrentuserDetail, ['authenmethod', 'name', 'taskmap', 'usergroup'], name, value)


    class Diameter(Entity):
        """
        Diameter operational data
        
        .. attribute:: gx
        
        	Diameter global gx data
        	**type**\:   :py:class:`Gx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Gx>`
        
        .. attribute:: gx_session_ids
        
        	Diameter Gx Session data list
        	**type**\:   :py:class:`GxSessionIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GxSessionIds>`
        
        .. attribute:: gx_statistics
        
        	Diameter Gx Statistics data
        	**type**\:   :py:class:`GxStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GxStatistics>`
        
        .. attribute:: gy
        
        	Diameter global gy data
        	**type**\:   :py:class:`Gy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Gy>`
        
        .. attribute:: gy_session_ids
        
        	Diameter Gy Session data list
        	**type**\:   :py:class:`GySessionIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GySessionIds>`
        
        .. attribute:: gy_statistics
        
        	Diameter Gy Statistics data
        	**type**\:   :py:class:`GyStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GyStatistics>`
        
        .. attribute:: nas
        
        	Diameter NAS data
        	**type**\:   :py:class:`Nas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Nas>`
        
        .. attribute:: nas_session
        
        	Diameter Nas Session data
        	**type**\:   :py:class:`NasSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.NasSession>`
        
        .. attribute:: nas_summary
        
        	Diameter NAS summary
        	**type**\:   :py:class:`NasSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.NasSummary>`
        
        .. attribute:: peers
        
        	Diameter peer global data
        	**type**\:   :py:class:`Peers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Peers>`
        
        

        """

        _prefix = 'aaa-diameter-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Diameter, self).__init__()

            self.yang_name = "diameter"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"gx" : ("gx", Aaa.Diameter.Gx), "gx-session-ids" : ("gx_session_ids", Aaa.Diameter.GxSessionIds), "gx-statistics" : ("gx_statistics", Aaa.Diameter.GxStatistics), "gy" : ("gy", Aaa.Diameter.Gy), "gy-session-ids" : ("gy_session_ids", Aaa.Diameter.GySessionIds), "gy-statistics" : ("gy_statistics", Aaa.Diameter.GyStatistics), "nas" : ("nas", Aaa.Diameter.Nas), "nas-session" : ("nas_session", Aaa.Diameter.NasSession), "nas-summary" : ("nas_summary", Aaa.Diameter.NasSummary), "peers" : ("peers", Aaa.Diameter.Peers)}
            self._child_list_classes = {}

            self.gx = Aaa.Diameter.Gx()
            self.gx.parent = self
            self._children_name_map["gx"] = "gx"
            self._children_yang_names.add("gx")

            self.gx_session_ids = Aaa.Diameter.GxSessionIds()
            self.gx_session_ids.parent = self
            self._children_name_map["gx_session_ids"] = "gx-session-ids"
            self._children_yang_names.add("gx-session-ids")

            self.gx_statistics = Aaa.Diameter.GxStatistics()
            self.gx_statistics.parent = self
            self._children_name_map["gx_statistics"] = "gx-statistics"
            self._children_yang_names.add("gx-statistics")

            self.gy = Aaa.Diameter.Gy()
            self.gy.parent = self
            self._children_name_map["gy"] = "gy"
            self._children_yang_names.add("gy")

            self.gy_session_ids = Aaa.Diameter.GySessionIds()
            self.gy_session_ids.parent = self
            self._children_name_map["gy_session_ids"] = "gy-session-ids"
            self._children_yang_names.add("gy-session-ids")

            self.gy_statistics = Aaa.Diameter.GyStatistics()
            self.gy_statistics.parent = self
            self._children_name_map["gy_statistics"] = "gy-statistics"
            self._children_yang_names.add("gy-statistics")

            self.nas = Aaa.Diameter.Nas()
            self.nas.parent = self
            self._children_name_map["nas"] = "nas"
            self._children_yang_names.add("nas")

            self.nas_session = Aaa.Diameter.NasSession()
            self.nas_session.parent = self
            self._children_name_map["nas_session"] = "nas-session"
            self._children_yang_names.add("nas-session")

            self.nas_summary = Aaa.Diameter.NasSummary()
            self.nas_summary.parent = self
            self._children_name_map["nas_summary"] = "nas-summary"
            self._children_yang_names.add("nas-summary")

            self.peers = Aaa.Diameter.Peers()
            self.peers.parent = self
            self._children_name_map["peers"] = "peers"
            self._children_yang_names.add("peers")
            self._segment_path = lambda: "Cisco-IOS-XR-aaa-diameter-oper:diameter"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self._segment_path()


        class Gx(Entity):
            """
            Diameter global gx data
            
            .. attribute:: is_enabled
            
            	Gx state
            	**type**\:  bool
            
            .. attribute:: retransmits
            
            	Gx retransmit count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tx_timer
            
            	Gx transaction timer in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.Gx, self).__init__()

                self.yang_name = "gx"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.is_enabled = YLeaf(YType.boolean, "is-enabled")

                self.retransmits = YLeaf(YType.uint32, "retransmits")

                self.tx_timer = YLeaf(YType.uint32, "tx-timer")
                self._segment_path = lambda: "gx"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.Gx, ['is_enabled', 'retransmits', 'tx_timer'], name, value)


        class GxSessionIds(Entity):
            """
            Diameter Gx Session data list
            
            .. attribute:: gx_session_id
            
            	Diameter Gx Session data
            	**type**\: list of    :py:class:`GxSessionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GxSessionIds.GxSessionId>`
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.GxSessionIds, self).__init__()

                self.yang_name = "gx-session-ids"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"gx-session-id" : ("gx_session_id", Aaa.Diameter.GxSessionIds.GxSessionId)}

                self.gx_session_id = YList(self)
                self._segment_path = lambda: "gx-session-ids"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.GxSessionIds, [], name, value)


            class GxSessionId(Entity):
                """
                Diameter Gx Session data
                
                .. attribute:: session_id  <key>
                
                	Session Id
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: aaa_session_id
                
                	AAA session id
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: diameter_session_id
                
                	Diameter session id
                	**type**\:  str
                
                .. attribute:: request_number
                
                	Request Number
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: request_type
                
                	Request Type
                	**type**\:  str
                
                .. attribute:: retry_count
                
                	Gx Retry count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: session_state
                
                	Session State
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-diameter-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Diameter.GxSessionIds.GxSessionId, self).__init__()

                    self.yang_name = "gx-session-id"
                    self.yang_parent_name = "gx-session-ids"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.session_id = YLeaf(YType.int32, "session-id")

                    self.aaa_session_id = YLeaf(YType.uint32, "aaa-session-id")

                    self.diameter_session_id = YLeaf(YType.str, "diameter-session-id")

                    self.request_number = YLeaf(YType.uint32, "request-number")

                    self.request_type = YLeaf(YType.str, "request-type")

                    self.retry_count = YLeaf(YType.uint32, "retry-count")

                    self.session_state = YLeaf(YType.str, "session-state")
                    self._segment_path = lambda: "gx-session-id" + "[session-id='" + self.session_id.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/gx-session-ids/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Diameter.GxSessionIds.GxSessionId, ['session_id', 'aaa_session_id', 'diameter_session_id', 'request_number', 'request_type', 'retry_count', 'session_state'], name, value)


        class GxStatistics(Entity):
            """
            Diameter Gx Statistics data
            
            .. attribute:: active_sessions
            
            	Total Active Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asa_sent_error_messages
            
            	ASA Sent Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asa_sent_messsages
            
            	ASA Sent Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asr_received_error_messages
            
            	ASR Received Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asr_received_messages
            
            	ASR Received Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_final_error_messages
            
            	CCA Final Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_final_messages
            
            	CCA Final Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_init_error_messages
            
            	CCA Initial Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_init_messages
            
            	CCA Initial Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_update_error_messages
            
            	CCA Update Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_update_messages
            
            	CCA Update Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_failed_messages
            
            	CCR Final Messages Failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_messages
            
            	CCR Final Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_retry_messages
            
            	CCR Final Messages retry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_timed_out_messages
            
            	CCR Final Messages Timed Out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_failed_messages
            
            	CCR Initial Messages Failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_messages
            
            	CCR Initial Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_retry_messages
            
            	CCR Initial Messages retry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_timed_out_messages
            
            	CCR Initial Messages Timed Out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_failed_messages
            
            	CCR Update Messages Failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_messages
            
            	CCR Update Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_retry_messages
            
            	CCR Update Messages retry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_timed_out_messages
            
            	CCR Update Messages Timed Out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: close_sessions
            
            	Total Closed Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: open_sessions
            
            	Total Opened Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: raa_sent_error_messages
            
            	RAA Sent Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: raa_sent_messages
            
            	RAA Sent Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rar_received_error_messages
            
            	RAR Received Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rar_received_messages
            
            	RAR Received Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: restore_sessions
            
            	Restore Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: session_termination_messages
            
            	Session Termination from server
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: unknown_request_messages
            
            	Unknown Request Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.GxStatistics, self).__init__()

                self.yang_name = "gx-statistics"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.active_sessions = YLeaf(YType.uint32, "active-sessions")

                self.asa_sent_error_messages = YLeaf(YType.uint32, "asa-sent-error-messages")

                self.asa_sent_messsages = YLeaf(YType.uint32, "asa-sent-messsages")

                self.asr_received_error_messages = YLeaf(YType.uint32, "asr-received-error-messages")

                self.asr_received_messages = YLeaf(YType.uint32, "asr-received-messages")

                self.cca_final_error_messages = YLeaf(YType.uint32, "cca-final-error-messages")

                self.cca_final_messages = YLeaf(YType.uint32, "cca-final-messages")

                self.cca_init_error_messages = YLeaf(YType.uint32, "cca-init-error-messages")

                self.cca_init_messages = YLeaf(YType.uint32, "cca-init-messages")

                self.cca_update_error_messages = YLeaf(YType.uint32, "cca-update-error-messages")

                self.cca_update_messages = YLeaf(YType.uint32, "cca-update-messages")

                self.ccr_final_failed_messages = YLeaf(YType.uint32, "ccr-final-failed-messages")

                self.ccr_final_messages = YLeaf(YType.uint32, "ccr-final-messages")

                self.ccr_final_retry_messages = YLeaf(YType.uint32, "ccr-final-retry-messages")

                self.ccr_final_timed_out_messages = YLeaf(YType.uint32, "ccr-final-timed-out-messages")

                self.ccr_init_failed_messages = YLeaf(YType.uint32, "ccr-init-failed-messages")

                self.ccr_init_messages = YLeaf(YType.uint32, "ccr-init-messages")

                self.ccr_init_retry_messages = YLeaf(YType.uint32, "ccr-init-retry-messages")

                self.ccr_init_timed_out_messages = YLeaf(YType.uint32, "ccr-init-timed-out-messages")

                self.ccr_update_failed_messages = YLeaf(YType.uint32, "ccr-update-failed-messages")

                self.ccr_update_messages = YLeaf(YType.uint32, "ccr-update-messages")

                self.ccr_update_retry_messages = YLeaf(YType.uint32, "ccr-update-retry-messages")

                self.ccr_update_timed_out_messages = YLeaf(YType.uint32, "ccr-update-timed-out-messages")

                self.close_sessions = YLeaf(YType.uint32, "close-sessions")

                self.open_sessions = YLeaf(YType.uint32, "open-sessions")

                self.raa_sent_error_messages = YLeaf(YType.uint32, "raa-sent-error-messages")

                self.raa_sent_messages = YLeaf(YType.uint32, "raa-sent-messages")

                self.rar_received_error_messages = YLeaf(YType.uint32, "rar-received-error-messages")

                self.rar_received_messages = YLeaf(YType.uint32, "rar-received-messages")

                self.restore_sessions = YLeaf(YType.uint32, "restore-sessions")

                self.session_termination_messages = YLeaf(YType.uint32, "session-termination-messages")

                self.unknown_request_messages = YLeaf(YType.uint32, "unknown-request-messages")
                self._segment_path = lambda: "gx-statistics"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.GxStatistics, ['active_sessions', 'asa_sent_error_messages', 'asa_sent_messsages', 'asr_received_error_messages', 'asr_received_messages', 'cca_final_error_messages', 'cca_final_messages', 'cca_init_error_messages', 'cca_init_messages', 'cca_update_error_messages', 'cca_update_messages', 'ccr_final_failed_messages', 'ccr_final_messages', 'ccr_final_retry_messages', 'ccr_final_timed_out_messages', 'ccr_init_failed_messages', 'ccr_init_messages', 'ccr_init_retry_messages', 'ccr_init_timed_out_messages', 'ccr_update_failed_messages', 'ccr_update_messages', 'ccr_update_retry_messages', 'ccr_update_timed_out_messages', 'close_sessions', 'open_sessions', 'raa_sent_error_messages', 'raa_sent_messages', 'rar_received_error_messages', 'rar_received_messages', 'restore_sessions', 'session_termination_messages', 'unknown_request_messages'], name, value)


        class Gy(Entity):
            """
            Diameter global gy data
            
            .. attribute:: is_enabled
            
            	Gy state
            	**type**\:  bool
            
            .. attribute:: retransmits
            
            	Gy retransmit count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tx_timer
            
            	Gy transaction timer in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.Gy, self).__init__()

                self.yang_name = "gy"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.is_enabled = YLeaf(YType.boolean, "is-enabled")

                self.retransmits = YLeaf(YType.uint32, "retransmits")

                self.tx_timer = YLeaf(YType.uint32, "tx-timer")
                self._segment_path = lambda: "gy"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.Gy, ['is_enabled', 'retransmits', 'tx_timer'], name, value)


        class GySessionIds(Entity):
            """
            Diameter Gy Session data list
            
            .. attribute:: gy_session_id
            
            	Diameter Gy Session data
            	**type**\: list of    :py:class:`GySessionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GySessionIds.GySessionId>`
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.GySessionIds, self).__init__()

                self.yang_name = "gy-session-ids"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"gy-session-id" : ("gy_session_id", Aaa.Diameter.GySessionIds.GySessionId)}

                self.gy_session_id = YList(self)
                self._segment_path = lambda: "gy-session-ids"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.GySessionIds, [], name, value)


            class GySessionId(Entity):
                """
                Diameter Gy Session data
                
                .. attribute:: session_id  <key>
                
                	Session Id
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: aaa_session_id
                
                	AAA session id
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: diameter_session_id
                
                	Diameter session id
                	**type**\:  str
                
                .. attribute:: parent_aaa_session_id
                
                	AAA Parent session id
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: request_number
                
                	Request Number
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: request_type
                
                	Request Type
                	**type**\:  str
                
                .. attribute:: retry_count
                
                	Gy Retry count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: session_state
                
                	Session State
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-diameter-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Diameter.GySessionIds.GySessionId, self).__init__()

                    self.yang_name = "gy-session-id"
                    self.yang_parent_name = "gy-session-ids"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.session_id = YLeaf(YType.int32, "session-id")

                    self.aaa_session_id = YLeaf(YType.uint32, "aaa-session-id")

                    self.diameter_session_id = YLeaf(YType.str, "diameter-session-id")

                    self.parent_aaa_session_id = YLeaf(YType.uint32, "parent-aaa-session-id")

                    self.request_number = YLeaf(YType.uint32, "request-number")

                    self.request_type = YLeaf(YType.str, "request-type")

                    self.retry_count = YLeaf(YType.uint32, "retry-count")

                    self.session_state = YLeaf(YType.str, "session-state")
                    self._segment_path = lambda: "gy-session-id" + "[session-id='" + self.session_id.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/gy-session-ids/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Diameter.GySessionIds.GySessionId, ['session_id', 'aaa_session_id', 'diameter_session_id', 'parent_aaa_session_id', 'request_number', 'request_type', 'retry_count', 'session_state'], name, value)


        class GyStatistics(Entity):
            """
            Diameter Gy Statistics data
            
            .. attribute:: active_sessions
            
            	Total Active Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asa_sent_error_messages
            
            	ASA Sent Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asa_sent_messages
            
            	ASA Sent Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asr_received_error_messages
            
            	ASR Received Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asr_received_messages
            
            	ASR Received Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_final_error_messages
            
            	CCA Final Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_final_messages
            
            	CCA Final Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_init_error_messages
            
            	CCA Initial Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_init_messages
            
            	CCA Initial Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_update_error_messages
            
            	CCA Update Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_update_messages
            
            	CCA Update Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_failed_messages
            
            	CCR Final Messages Failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_messages
            
            	CCR Final Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_retry_messages
            
            	CCR Final Messages retry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_timed_out_messages
            
            	CCR Final Messages Timed Out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_failed_messages
            
            	CCR Initial Messages Failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_messages
            
            	CCR Initial Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_retry_messages
            
            	CCR Initial Messages retry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_timed_out_messages
            
            	CCR Initial Messages Timed Out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_failed_messages
            
            	CCR Update Messages Failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_messages
            
            	CCR Update Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_retry_messages
            
            	CCR Update Messages retry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_timed_out_messages
            
            	CCR Update Messages Timed Out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: close_sessions
            
            	Total Closed Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: open_sessions
            
            	Total Opened Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: raa_sent_error_messages
            
            	RAA Sent Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: raa_sent_messages
            
            	RAA Sent Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rar_received_error_messages
            
            	RAR Received Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rar_received_messages
            
            	RAR Received Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: restore_sessions
            
            	Restore Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: unknown_request_messages
            
            	Unknown Request Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.GyStatistics, self).__init__()

                self.yang_name = "gy-statistics"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.active_sessions = YLeaf(YType.uint32, "active-sessions")

                self.asa_sent_error_messages = YLeaf(YType.uint32, "asa-sent-error-messages")

                self.asa_sent_messages = YLeaf(YType.uint32, "asa-sent-messages")

                self.asr_received_error_messages = YLeaf(YType.uint32, "asr-received-error-messages")

                self.asr_received_messages = YLeaf(YType.uint32, "asr-received-messages")

                self.cca_final_error_messages = YLeaf(YType.uint32, "cca-final-error-messages")

                self.cca_final_messages = YLeaf(YType.uint32, "cca-final-messages")

                self.cca_init_error_messages = YLeaf(YType.uint32, "cca-init-error-messages")

                self.cca_init_messages = YLeaf(YType.uint32, "cca-init-messages")

                self.cca_update_error_messages = YLeaf(YType.uint32, "cca-update-error-messages")

                self.cca_update_messages = YLeaf(YType.uint32, "cca-update-messages")

                self.ccr_final_failed_messages = YLeaf(YType.uint32, "ccr-final-failed-messages")

                self.ccr_final_messages = YLeaf(YType.uint32, "ccr-final-messages")

                self.ccr_final_retry_messages = YLeaf(YType.uint32, "ccr-final-retry-messages")

                self.ccr_final_timed_out_messages = YLeaf(YType.uint32, "ccr-final-timed-out-messages")

                self.ccr_init_failed_messages = YLeaf(YType.uint32, "ccr-init-failed-messages")

                self.ccr_init_messages = YLeaf(YType.uint32, "ccr-init-messages")

                self.ccr_init_retry_messages = YLeaf(YType.uint32, "ccr-init-retry-messages")

                self.ccr_init_timed_out_messages = YLeaf(YType.uint32, "ccr-init-timed-out-messages")

                self.ccr_update_failed_messages = YLeaf(YType.uint32, "ccr-update-failed-messages")

                self.ccr_update_messages = YLeaf(YType.uint32, "ccr-update-messages")

                self.ccr_update_retry_messages = YLeaf(YType.uint32, "ccr-update-retry-messages")

                self.ccr_update_timed_out_messages = YLeaf(YType.uint32, "ccr-update-timed-out-messages")

                self.close_sessions = YLeaf(YType.uint32, "close-sessions")

                self.open_sessions = YLeaf(YType.uint32, "open-sessions")

                self.raa_sent_error_messages = YLeaf(YType.uint32, "raa-sent-error-messages")

                self.raa_sent_messages = YLeaf(YType.uint32, "raa-sent-messages")

                self.rar_received_error_messages = YLeaf(YType.uint32, "rar-received-error-messages")

                self.rar_received_messages = YLeaf(YType.uint32, "rar-received-messages")

                self.restore_sessions = YLeaf(YType.uint32, "restore-sessions")

                self.unknown_request_messages = YLeaf(YType.uint32, "unknown-request-messages")
                self._segment_path = lambda: "gy-statistics"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.GyStatistics, ['active_sessions', 'asa_sent_error_messages', 'asa_sent_messages', 'asr_received_error_messages', 'asr_received_messages', 'cca_final_error_messages', 'cca_final_messages', 'cca_init_error_messages', 'cca_init_messages', 'cca_update_error_messages', 'cca_update_messages', 'ccr_final_failed_messages', 'ccr_final_messages', 'ccr_final_retry_messages', 'ccr_final_timed_out_messages', 'ccr_init_failed_messages', 'ccr_init_messages', 'ccr_init_retry_messages', 'ccr_init_timed_out_messages', 'ccr_update_failed_messages', 'ccr_update_messages', 'ccr_update_retry_messages', 'ccr_update_timed_out_messages', 'close_sessions', 'open_sessions', 'raa_sent_error_messages', 'raa_sent_messages', 'rar_received_error_messages', 'rar_received_messages', 'restore_sessions', 'unknown_request_messages'], name, value)


        class Nas(Entity):
            """
            Diameter NAS data
            
            .. attribute:: aaanas_id
            
            	AAA NAS id
            	**type**\:  str
            
            .. attribute:: list_of_nas
            
            	List of NAS Entries
            	**type**\: list of    :py:class:`ListOfNas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Nas.ListOfNas>`
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.Nas, self).__init__()

                self.yang_name = "nas"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"list-of-nas" : ("list_of_nas", Aaa.Diameter.Nas.ListOfNas)}

                self.aaanas_id = YLeaf(YType.str, "aaanas-id")

                self.list_of_nas = YList(self)
                self._segment_path = lambda: "nas"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.Nas, ['aaanas_id'], name, value)


            class ListOfNas(Entity):
                """
                List of NAS Entries
                
                .. attribute:: aaa_session_id
                
                	AAA session id
                	**type**\:  str
                
                .. attribute:: accounting_intrim_in_packets
                
                	Accounting intrim packet response in
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_intrim_out_packets
                
                	Accounting intrim requests packets out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_status
                
                	Diameter ACR status start
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_status_stop
                
                	Diameter ACR status stop
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authentication_status
                
                	Diameter AAR status
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authorization_status
                
                	Diameter AAR status
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: diameter_session_id
                
                	Diameter session id
                	**type**\:  str
                
                .. attribute:: disconnect_status
                
                	Diameter STR status
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: method_list
                
                	Method list used for authentication
                	**type**\:  str
                
                .. attribute:: server_used_list
                
                	Server used for authentication
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-diameter-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Diameter.Nas.ListOfNas, self).__init__()

                    self.yang_name = "list-of-nas"
                    self.yang_parent_name = "nas"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.aaa_session_id = YLeaf(YType.str, "aaa-session-id")

                    self.accounting_intrim_in_packets = YLeaf(YType.uint32, "accounting-intrim-in-packets")

                    self.accounting_intrim_out_packets = YLeaf(YType.uint32, "accounting-intrim-out-packets")

                    self.accounting_status = YLeaf(YType.uint32, "accounting-status")

                    self.accounting_status_stop = YLeaf(YType.uint32, "accounting-status-stop")

                    self.authentication_status = YLeaf(YType.uint32, "authentication-status")

                    self.authorization_status = YLeaf(YType.uint32, "authorization-status")

                    self.diameter_session_id = YLeaf(YType.str, "diameter-session-id")

                    self.disconnect_status = YLeaf(YType.uint32, "disconnect-status")

                    self.method_list = YLeaf(YType.str, "method-list")

                    self.server_used_list = YLeaf(YType.str, "server-used-list")
                    self._segment_path = lambda: "list-of-nas"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/nas/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Diameter.Nas.ListOfNas, ['aaa_session_id', 'accounting_intrim_in_packets', 'accounting_intrim_out_packets', 'accounting_status', 'accounting_status_stop', 'authentication_status', 'authorization_status', 'diameter_session_id', 'disconnect_status', 'method_list', 'server_used_list'], name, value)


        class NasSession(Entity):
            """
            Diameter Nas Session data
            
            .. attribute:: aaanas_id
            
            	AAA NAS id
            	**type**\:  str
            
            .. attribute:: list_of_nas
            
            	List of NAS Entries
            	**type**\: list of    :py:class:`ListOfNas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.NasSession.ListOfNas>`
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.NasSession, self).__init__()

                self.yang_name = "nas-session"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"list-of-nas" : ("list_of_nas", Aaa.Diameter.NasSession.ListOfNas)}

                self.aaanas_id = YLeaf(YType.str, "aaanas-id")

                self.list_of_nas = YList(self)
                self._segment_path = lambda: "nas-session"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.NasSession, ['aaanas_id'], name, value)


            class ListOfNas(Entity):
                """
                List of NAS Entries
                
                .. attribute:: aaa_session_id
                
                	AAA session id
                	**type**\:  str
                
                .. attribute:: accounting_intrim_in_packets
                
                	Accounting intrim packet response in
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_intrim_out_packets
                
                	Accounting intrim requests packets out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_status
                
                	Diameter ACR status start
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_status_stop
                
                	Diameter ACR status stop
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authentication_status
                
                	Diameter AAR status
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authorization_status
                
                	Diameter AAR status
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: diameter_session_id
                
                	Diameter session id
                	**type**\:  str
                
                .. attribute:: disconnect_status
                
                	Diameter STR status
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: method_list
                
                	Method list used for authentication
                	**type**\:  str
                
                .. attribute:: server_used_list
                
                	Server used for authentication
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-diameter-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Diameter.NasSession.ListOfNas, self).__init__()

                    self.yang_name = "list-of-nas"
                    self.yang_parent_name = "nas-session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.aaa_session_id = YLeaf(YType.str, "aaa-session-id")

                    self.accounting_intrim_in_packets = YLeaf(YType.uint32, "accounting-intrim-in-packets")

                    self.accounting_intrim_out_packets = YLeaf(YType.uint32, "accounting-intrim-out-packets")

                    self.accounting_status = YLeaf(YType.uint32, "accounting-status")

                    self.accounting_status_stop = YLeaf(YType.uint32, "accounting-status-stop")

                    self.authentication_status = YLeaf(YType.uint32, "authentication-status")

                    self.authorization_status = YLeaf(YType.uint32, "authorization-status")

                    self.diameter_session_id = YLeaf(YType.str, "diameter-session-id")

                    self.disconnect_status = YLeaf(YType.uint32, "disconnect-status")

                    self.method_list = YLeaf(YType.str, "method-list")

                    self.server_used_list = YLeaf(YType.str, "server-used-list")
                    self._segment_path = lambda: "list-of-nas"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/nas-session/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Diameter.NasSession.ListOfNas, ['aaa_session_id', 'accounting_intrim_in_packets', 'accounting_intrim_out_packets', 'accounting_status', 'accounting_status_stop', 'authentication_status', 'authorization_status', 'diameter_session_id', 'disconnect_status', 'method_list', 'server_used_list'], name, value)


        class NasSummary(Entity):
            """
            Diameter NAS summary
            
            .. attribute:: accounting_interim_failed_packets
            
            	Accounting interim response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_interim_request_in_packets
            
            	Accounting Interim request from cleint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_interim_request_out_packets
            
            	Accounting interim requests packets out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_interim_response_out_packets
            
            	Accounting interim response frwd to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_interim_success_packets
            
            	Accounting interim response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_intrim_response_in_packets
            
            	Accounting interim packet response in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_request_out_packets
            
            	Accounting requests packets out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_response_in_packets
            
            	Accounting packet response in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_start_failed_packets
            
            	Accounting start response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_start_request_packets
            
            	Accounting start request from cleint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_start_response_packets
            
            	Accounting start response forward to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_start_success_packets
            
            	Accounting start response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_failed_packets
            
            	Accounting stop response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_request_in_packets
            
            	Acct stop request from cleint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_request_out_packets
            
            	Accounting stop requests packets out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_response_in_packets
            
            	Accounting stop packet response in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_response_out_packets
            
            	Acct stop response forward to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_success_response_packets
            
            	Accounting stop response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authen_request_in_packets
            
            	Authentication request from client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authen_request_out_packets
            
            	Authentication request pkt out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authen_response_fail_packets
            
            	Authentication response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authen_response_in_packets
            
            	Authentication response pkt in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authen_response_out_packets
            
            	Authentication response frwd to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authen_success_packets
            
            	Authentication response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_in_packets
            
            	Authorization response packet in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_out_packets
            
            	Authorization request packet out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_request_in_packets
            
            	Authourization request from cleint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_response_fail_packets
            
            	Authentication response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_response_out_packets
            
            	Authourization response frwd to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_response_success_packets
            
            	Authentication response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_failed_packets
            
            	COA response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_request_in_packets
            
            	COA/RAR Request packet in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_request_packets
            
            	COA request from client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_response_out_packets
            
            	COA/RAR Response packet out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_response_packets
            
            	COA response forward to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_success_packets
            
            	COA response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_failed_response_packets
            
            	Disconnect response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_request_in_packets
            
            	Disconnect request from cleint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_request_out_packets
            
            	Disconnect request pkt out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_response_in_packets
            
            	Disconnect response packets in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_response_out_packets
            
            	Disconnect response forward to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_success_response_packets
            
            	Disconnect response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_failed_packets
            
            	POD response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_in_packets
            
            	POD/RAR Request packets in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_out_packets
            
            	PAD/RAR Response packets out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_request_in_packets
            
            	POD request from cleint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_response_out_packets
            
            	POD response forward to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_success_packets
            
            	POD response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.NasSummary, self).__init__()

                self.yang_name = "nas-summary"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.accounting_interim_failed_packets = YLeaf(YType.uint32, "accounting-interim-failed-packets")

                self.accounting_interim_request_in_packets = YLeaf(YType.uint32, "accounting-interim-request-in-packets")

                self.accounting_interim_request_out_packets = YLeaf(YType.uint32, "accounting-interim-request-out-packets")

                self.accounting_interim_response_out_packets = YLeaf(YType.uint32, "accounting-interim-response-out-packets")

                self.accounting_interim_success_packets = YLeaf(YType.uint32, "accounting-interim-success-packets")

                self.accounting_intrim_response_in_packets = YLeaf(YType.uint32, "accounting-intrim-response-in-packets")

                self.accounting_request_out_packets = YLeaf(YType.uint32, "accounting-request-out-packets")

                self.accounting_response_in_packets = YLeaf(YType.uint32, "accounting-response-in-packets")

                self.accounting_start_failed_packets = YLeaf(YType.uint32, "accounting-start-failed-packets")

                self.accounting_start_request_packets = YLeaf(YType.uint32, "accounting-start-request-packets")

                self.accounting_start_response_packets = YLeaf(YType.uint32, "accounting-start-response-packets")

                self.accounting_start_success_packets = YLeaf(YType.uint32, "accounting-start-success-packets")

                self.accounting_stop_failed_packets = YLeaf(YType.uint32, "accounting-stop-failed-packets")

                self.accounting_stop_request_in_packets = YLeaf(YType.uint32, "accounting-stop-request-in-packets")

                self.accounting_stop_request_out_packets = YLeaf(YType.uint32, "accounting-stop-request-out-packets")

                self.accounting_stop_response_in_packets = YLeaf(YType.uint32, "accounting-stop-response-in-packets")

                self.accounting_stop_response_out_packets = YLeaf(YType.uint32, "accounting-stop-response-out-packets")

                self.accounting_stop_success_response_packets = YLeaf(YType.uint32, "accounting-stop-success-response-packets")

                self.authen_request_in_packets = YLeaf(YType.uint32, "authen-request-in-packets")

                self.authen_request_out_packets = YLeaf(YType.uint32, "authen-request-out-packets")

                self.authen_response_fail_packets = YLeaf(YType.uint32, "authen-response-fail-packets")

                self.authen_response_in_packets = YLeaf(YType.uint32, "authen-response-in-packets")

                self.authen_response_out_packets = YLeaf(YType.uint32, "authen-response-out-packets")

                self.authen_success_packets = YLeaf(YType.uint32, "authen-success-packets")

                self.authorization_in_packets = YLeaf(YType.uint32, "authorization-in-packets")

                self.authorization_out_packets = YLeaf(YType.uint32, "authorization-out-packets")

                self.authorization_request_in_packets = YLeaf(YType.uint32, "authorization-request-in-packets")

                self.authorization_response_fail_packets = YLeaf(YType.uint32, "authorization-response-fail-packets")

                self.authorization_response_out_packets = YLeaf(YType.uint32, "authorization-response-out-packets")

                self.authorization_response_success_packets = YLeaf(YType.uint32, "authorization-response-success-packets")

                self.coa_failed_packets = YLeaf(YType.uint32, "coa-failed-packets")

                self.coa_request_in_packets = YLeaf(YType.uint32, "coa-request-in-packets")

                self.coa_request_packets = YLeaf(YType.uint32, "coa-request-packets")

                self.coa_response_out_packets = YLeaf(YType.uint32, "coa-response-out-packets")

                self.coa_response_packets = YLeaf(YType.uint32, "coa-response-packets")

                self.coa_success_packets = YLeaf(YType.uint32, "coa-success-packets")

                self.disconnect_failed_response_packets = YLeaf(YType.uint32, "disconnect-failed-response-packets")

                self.disconnect_request_in_packets = YLeaf(YType.uint32, "disconnect-request-in-packets")

                self.disconnect_request_out_packets = YLeaf(YType.uint32, "disconnect-request-out-packets")

                self.disconnect_response_in_packets = YLeaf(YType.uint32, "disconnect-response-in-packets")

                self.disconnect_response_out_packets = YLeaf(YType.uint32, "disconnect-response-out-packets")

                self.disconnect_success_response_packets = YLeaf(YType.uint32, "disconnect-success-response-packets")

                self.pod_failed_packets = YLeaf(YType.uint32, "pod-failed-packets")

                self.pod_in_packets = YLeaf(YType.uint32, "pod-in-packets")

                self.pod_out_packets = YLeaf(YType.uint32, "pod-out-packets")

                self.pod_request_in_packets = YLeaf(YType.uint32, "pod-request-in-packets")

                self.pod_response_out_packets = YLeaf(YType.uint32, "pod-response-out-packets")

                self.pod_success_packets = YLeaf(YType.uint32, "pod-success-packets")
                self._segment_path = lambda: "nas-summary"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.NasSummary, ['accounting_interim_failed_packets', 'accounting_interim_request_in_packets', 'accounting_interim_request_out_packets', 'accounting_interim_response_out_packets', 'accounting_interim_success_packets', 'accounting_intrim_response_in_packets', 'accounting_request_out_packets', 'accounting_response_in_packets', 'accounting_start_failed_packets', 'accounting_start_request_packets', 'accounting_start_response_packets', 'accounting_start_success_packets', 'accounting_stop_failed_packets', 'accounting_stop_request_in_packets', 'accounting_stop_request_out_packets', 'accounting_stop_response_in_packets', 'accounting_stop_response_out_packets', 'accounting_stop_success_response_packets', 'authen_request_in_packets', 'authen_request_out_packets', 'authen_response_fail_packets', 'authen_response_in_packets', 'authen_response_out_packets', 'authen_success_packets', 'authorization_in_packets', 'authorization_out_packets', 'authorization_request_in_packets', 'authorization_response_fail_packets', 'authorization_response_out_packets', 'authorization_response_success_packets', 'coa_failed_packets', 'coa_request_in_packets', 'coa_request_packets', 'coa_response_out_packets', 'coa_response_packets', 'coa_success_packets', 'disconnect_failed_response_packets', 'disconnect_request_in_packets', 'disconnect_request_out_packets', 'disconnect_response_in_packets', 'disconnect_response_out_packets', 'disconnect_success_response_packets', 'pod_failed_packets', 'pod_in_packets', 'pod_out_packets', 'pod_request_in_packets', 'pod_response_out_packets', 'pod_success_packets'], name, value)


        class Peers(Entity):
            """
            Diameter peer global data
            
            .. attribute:: conn_retry_timer
            
            	Connection retry timer in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: origin_host
            
            	Origin Host
            	**type**\:  str
            
            .. attribute:: origin_realm
            
            	Origin Realm
            	**type**\:  str
            
            .. attribute:: peer
            
            	Peer List
            	**type**\: list of    :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Peers.Peer>`
            
            .. attribute:: source_interface
            
            	Source Interface
            	**type**\:  str
            
            .. attribute:: tls_trustpoint
            
            	TLS Trustpoint
            	**type**\:  str
            
            .. attribute:: trans_max
            
            	Maximum number of transactions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: trans_total
            
            	Total number of transactions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: transaction_timer
            
            	Transaction timer in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: watchdog_timer
            
            	Watch dog timer in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.Peers, self).__init__()

                self.yang_name = "peers"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"peer" : ("peer", Aaa.Diameter.Peers.Peer)}

                self.conn_retry_timer = YLeaf(YType.uint32, "conn-retry-timer")

                self.origin_host = YLeaf(YType.str, "origin-host")

                self.origin_realm = YLeaf(YType.str, "origin-realm")

                self.source_interface = YLeaf(YType.str, "source-interface")

                self.tls_trustpoint = YLeaf(YType.str, "tls-trustpoint")

                self.trans_max = YLeaf(YType.uint32, "trans-max")

                self.trans_total = YLeaf(YType.uint32, "trans-total")

                self.transaction_timer = YLeaf(YType.uint32, "transaction-timer")

                self.watchdog_timer = YLeaf(YType.uint32, "watchdog-timer")

                self.peer = YList(self)
                self._segment_path = lambda: "peers"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.Peers, ['conn_retry_timer', 'origin_host', 'origin_realm', 'source_interface', 'tls_trustpoint', 'trans_max', 'trans_total', 'transaction_timer', 'watchdog_timer'], name, value)


            class Peer(Entity):
                """
                Peer List
                
                .. attribute:: address
                
                	IPv4 or IPv6 address of DIAMETER peer
                	**type**\:  str
                
                .. attribute:: conn_retry_timer
                
                	Connection retry timer in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: destination_host
                
                	Destination host name
                	**type**\:  str
                
                .. attribute:: destination_realm
                
                	Destination realm
                	**type**\:  str
                
                .. attribute:: firmware_revision
                
                	Firmware revision
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_aa_as
                
                	Incoming AAAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ac_as
                
                	Incoming ACAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ac_rs
                
                	Incoming ACRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_as_as
                
                	Incoming ASAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_as_rs
                
                	Incoming ASRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_cc_as
                
                	Incoming CCAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_cc_rs
                
                	Incoming CCRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ce_as
                
                	Incoming CEAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ce_rs
                
                	Incoming CERs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_dp_as
                
                	Incoming DPAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_dp_rs
                
                	Incoming DPRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_dw_as
                
                	Incoming DWAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_dw_rs
                
                	Incoming DWRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ra_as
                
                	Incoming RAAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ra_rs
                
                	Incoming RARs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_st_as
                
                	Incoming STAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_st_rs
                
                	Incoming STRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: last_disconnect_cause
                
                	Last Disconnect Reason
                	**type**\:   :py:class:`DisconnectCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.DisconnectCause>`
                
                .. attribute:: malformed_requests
                
                	Malformed Requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_aa_rs
                
                	Outgoing AARs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ac_as
                
                	Outgoing ACAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ac_rs
                
                	Outgoing ACRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_as_as
                
                	Outgoing ASAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_as_rs
                
                	Outgoing ASRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_cc_as
                
                	Outgoing CCAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_cc_rs
                
                	Outgoing CCRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ce_as
                
                	Outgoing CEAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ce_rs
                
                	Outgoing CERs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_dp_as
                
                	Outgoing DPAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_dp_rs
                
                	Outgoing DPRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_dw_as
                
                	Outgoing DWAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_dw_rs
                
                	Outgoing DWRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ra_as
                
                	Outgoing RAAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ra_rs
                
                	Outgoing RARs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_st_as
                
                	Outgoing STAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_st_rs
                
                	Outgoing STRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_index
                
                	Peer Index
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_name
                
                	Peer Name
                	**type**\:  str
                
                .. attribute:: peer_type
                
                	Peer Type
                	**type**\:   :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.Peer>`
                
                .. attribute:: port
                
                	Port number on which the peeris running
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: port_connect
                
                	Local Connection port
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: protocol_type
                
                	Protocol Type
                	**type**\:   :py:class:`ProtocolTypeValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.ProtocolTypeValue>`
                
                .. attribute:: received_permanent_fails
                
                	Permanent Failures Received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_proto_errors
                
                	Protocol Error Received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_transient_fails
                
                	Transient failures Received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: security_type
                
                	Security type used to transport
                	**type**\:   :py:class:`SecurityTypeValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.SecurityTypeValue>`
                
                .. attribute:: sent_permanent_fails
                
                	Permanent Failures Sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sent_proto_errors
                
                	Protocol Error Sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sent_transient_fails
                
                	Transient failures Sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: source_interface
                
                	Source Interface
                	**type**\:  str
                
                .. attribute:: state
                
                	Peer Connection Status
                	**type**\:   :py:class:`PeerStateValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.PeerStateValue>`
                
                .. attribute:: state_duration
                
                	State Duration in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: transaction_timer
                
                	Transaction timer in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: transport_down
                
                	Transport Down
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: vrf_name
                
                	Vrf Name
                	**type**\:  str
                
                .. attribute:: watchdog_timer
                
                	Watch dog timer in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: who_init_disconnect
                
                	Who Initiated Disconnect
                	**type**\:   :py:class:`WhoInitiatedDisconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.WhoInitiatedDisconnect>`
                
                

                """

                _prefix = 'aaa-diameter-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Diameter.Peers.Peer, self).__init__()

                    self.yang_name = "peer"
                    self.yang_parent_name = "peers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.address = YLeaf(YType.str, "address")

                    self.conn_retry_timer = YLeaf(YType.uint32, "conn-retry-timer")

                    self.destination_host = YLeaf(YType.str, "destination-host")

                    self.destination_realm = YLeaf(YType.str, "destination-realm")

                    self.firmware_revision = YLeaf(YType.uint32, "firmware-revision")

                    self.in_aa_as = YLeaf(YType.uint32, "in-aa-as")

                    self.in_ac_as = YLeaf(YType.uint32, "in-ac-as")

                    self.in_ac_rs = YLeaf(YType.uint32, "in-ac-rs")

                    self.in_as_as = YLeaf(YType.uint32, "in-as-as")

                    self.in_as_rs = YLeaf(YType.uint32, "in-as-rs")

                    self.in_cc_as = YLeaf(YType.uint32, "in-cc-as")

                    self.in_cc_rs = YLeaf(YType.uint32, "in-cc-rs")

                    self.in_ce_as = YLeaf(YType.uint32, "in-ce-as")

                    self.in_ce_rs = YLeaf(YType.uint32, "in-ce-rs")

                    self.in_dp_as = YLeaf(YType.uint32, "in-dp-as")

                    self.in_dp_rs = YLeaf(YType.uint32, "in-dp-rs")

                    self.in_dw_as = YLeaf(YType.uint32, "in-dw-as")

                    self.in_dw_rs = YLeaf(YType.uint32, "in-dw-rs")

                    self.in_ra_as = YLeaf(YType.uint32, "in-ra-as")

                    self.in_ra_rs = YLeaf(YType.uint32, "in-ra-rs")

                    self.in_st_as = YLeaf(YType.uint32, "in-st-as")

                    self.in_st_rs = YLeaf(YType.uint32, "in-st-rs")

                    self.last_disconnect_cause = YLeaf(YType.enumeration, "last-disconnect-cause")

                    self.malformed_requests = YLeaf(YType.uint32, "malformed-requests")

                    self.out_aa_rs = YLeaf(YType.uint32, "out-aa-rs")

                    self.out_ac_as = YLeaf(YType.uint32, "out-ac-as")

                    self.out_ac_rs = YLeaf(YType.uint32, "out-ac-rs")

                    self.out_as_as = YLeaf(YType.uint32, "out-as-as")

                    self.out_as_rs = YLeaf(YType.uint32, "out-as-rs")

                    self.out_cc_as = YLeaf(YType.uint32, "out-cc-as")

                    self.out_cc_rs = YLeaf(YType.uint32, "out-cc-rs")

                    self.out_ce_as = YLeaf(YType.uint32, "out-ce-as")

                    self.out_ce_rs = YLeaf(YType.uint32, "out-ce-rs")

                    self.out_dp_as = YLeaf(YType.uint32, "out-dp-as")

                    self.out_dp_rs = YLeaf(YType.uint32, "out-dp-rs")

                    self.out_dw_as = YLeaf(YType.uint32, "out-dw-as")

                    self.out_dw_rs = YLeaf(YType.uint32, "out-dw-rs")

                    self.out_ra_as = YLeaf(YType.uint32, "out-ra-as")

                    self.out_ra_rs = YLeaf(YType.uint32, "out-ra-rs")

                    self.out_st_as = YLeaf(YType.uint32, "out-st-as")

                    self.out_st_rs = YLeaf(YType.uint32, "out-st-rs")

                    self.peer_index = YLeaf(YType.uint32, "peer-index")

                    self.peer_name = YLeaf(YType.str, "peer-name")

                    self.peer_type = YLeaf(YType.enumeration, "peer-type")

                    self.port = YLeaf(YType.uint32, "port")

                    self.port_connect = YLeaf(YType.uint32, "port-connect")

                    self.protocol_type = YLeaf(YType.enumeration, "protocol-type")

                    self.received_permanent_fails = YLeaf(YType.uint32, "received-permanent-fails")

                    self.received_proto_errors = YLeaf(YType.uint32, "received-proto-errors")

                    self.received_transient_fails = YLeaf(YType.uint32, "received-transient-fails")

                    self.security_type = YLeaf(YType.enumeration, "security-type")

                    self.sent_permanent_fails = YLeaf(YType.uint32, "sent-permanent-fails")

                    self.sent_proto_errors = YLeaf(YType.uint32, "sent-proto-errors")

                    self.sent_transient_fails = YLeaf(YType.uint32, "sent-transient-fails")

                    self.source_interface = YLeaf(YType.str, "source-interface")

                    self.state = YLeaf(YType.enumeration, "state")

                    self.state_duration = YLeaf(YType.uint32, "state-duration")

                    self.transaction_timer = YLeaf(YType.uint32, "transaction-timer")

                    self.transport_down = YLeaf(YType.uint32, "transport-down")

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.watchdog_timer = YLeaf(YType.uint32, "watchdog-timer")

                    self.who_init_disconnect = YLeaf(YType.enumeration, "who-init-disconnect")
                    self._segment_path = lambda: "peer"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/peers/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Diameter.Peers.Peer, ['address', 'conn_retry_timer', 'destination_host', 'destination_realm', 'firmware_revision', 'in_aa_as', 'in_ac_as', 'in_ac_rs', 'in_as_as', 'in_as_rs', 'in_cc_as', 'in_cc_rs', 'in_ce_as', 'in_ce_rs', 'in_dp_as', 'in_dp_rs', 'in_dw_as', 'in_dw_rs', 'in_ra_as', 'in_ra_rs', 'in_st_as', 'in_st_rs', 'last_disconnect_cause', 'malformed_requests', 'out_aa_rs', 'out_ac_as', 'out_ac_rs', 'out_as_as', 'out_as_rs', 'out_cc_as', 'out_cc_rs', 'out_ce_as', 'out_ce_rs', 'out_dp_as', 'out_dp_rs', 'out_dw_as', 'out_dw_rs', 'out_ra_as', 'out_ra_rs', 'out_st_as', 'out_st_rs', 'peer_index', 'peer_name', 'peer_type', 'port', 'port_connect', 'protocol_type', 'received_permanent_fails', 'received_proto_errors', 'received_transient_fails', 'security_type', 'sent_permanent_fails', 'sent_proto_errors', 'sent_transient_fails', 'source_interface', 'state', 'state_duration', 'transaction_timer', 'transport_down', 'vrf_name', 'watchdog_timer', 'who_init_disconnect'], name, value)


    class Radius(Entity):
        """
        RADIUS operational data
        
        .. attribute:: global_
        
        	RADIUS Client Information
        	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.Global_>`
        
        .. attribute:: radius_source_interface
        
        	RADIUS source interfaces
        	**type**\:   :py:class:`RadiusSourceInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.RadiusSourceInterface>`
        
        .. attribute:: servers
        
        	List of RADIUS servers configured
        	**type**\:   :py:class:`Servers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.Servers>`
        
        

        """

        _prefix = 'aaa-protocol-radius-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Aaa.Radius, self).__init__()

            self.yang_name = "radius"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"global" : ("global_", Aaa.Radius.Global_), "radius-source-interface" : ("radius_source_interface", Aaa.Radius.RadiusSourceInterface), "servers" : ("servers", Aaa.Radius.Servers)}
            self._child_list_classes = {}

            self.global_ = Aaa.Radius.Global_()
            self.global_.parent = self
            self._children_name_map["global_"] = "global"
            self._children_yang_names.add("global")

            self.radius_source_interface = Aaa.Radius.RadiusSourceInterface()
            self.radius_source_interface.parent = self
            self._children_name_map["radius_source_interface"] = "radius-source-interface"
            self._children_yang_names.add("radius-source-interface")

            self.servers = Aaa.Radius.Servers()
            self.servers.parent = self
            self._children_name_map["servers"] = "servers"
            self._children_yang_names.add("servers")
            self._segment_path = lambda: "Cisco-IOS-XR-aaa-protocol-radius-oper:radius"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self._segment_path()


        class Global_(Entity):
            """
            RADIUS Client Information
            
            .. attribute:: accounting_nas_id
            
            	NAS\-Identifier of the RADIUSaccounting client
            	**type**\:  str
            
            .. attribute:: authentication_nas_id
            
            	NAS\-Identifier of the RADIUSauthentication client
            	**type**\:  str
            
            .. attribute:: unknown_accounting_response
            
            	Number of RADIUS Accounting\-Responsepackets received from unknownaddresses
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: unknown_authentication_response
            
            	Number of RADIUS Access\-Responsepackets received from unknownaddresses
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'aaa-protocol-radius-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Aaa.Radius.Global_, self).__init__()

                self.yang_name = "global"
                self.yang_parent_name = "radius"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.accounting_nas_id = YLeaf(YType.str, "accounting-nas-id")

                self.authentication_nas_id = YLeaf(YType.str, "authentication-nas-id")

                self.unknown_accounting_response = YLeaf(YType.uint32, "unknown-accounting-response")

                self.unknown_authentication_response = YLeaf(YType.uint32, "unknown-authentication-response")
                self._segment_path = lambda: "global"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Radius.Global_, ['accounting_nas_id', 'authentication_nas_id', 'unknown_accounting_response', 'unknown_authentication_response'], name, value)


        class RadiusSourceInterface(Entity):
            """
            RADIUS source interfaces
            
            .. attribute:: list_of_source_interface
            
            	List of source interfaces
            	**type**\: list of    :py:class:`ListOfSourceInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.RadiusSourceInterface.ListOfSourceInterface>`
            
            

            """

            _prefix = 'aaa-protocol-radius-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Aaa.Radius.RadiusSourceInterface, self).__init__()

                self.yang_name = "radius-source-interface"
                self.yang_parent_name = "radius"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"list-of-source-interface" : ("list_of_source_interface", Aaa.Radius.RadiusSourceInterface.ListOfSourceInterface)}

                self.list_of_source_interface = YList(self)
                self._segment_path = lambda: "radius-source-interface"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Radius.RadiusSourceInterface, [], name, value)


            class ListOfSourceInterface(Entity):
                """
                List of source interfaces
                
                .. attribute:: interface_name
                
                	Name of the source interface
                	**type**\:  str
                
                .. attribute:: ipaddrv4
                
                	IP address buffer
                	**type**\:  str
                
                	**length:** 0..16
                
                .. attribute:: ipaddrv6
                
                	IP address buffer
                	**type**\:  str
                
                	**length:** 0..46
                
                .. attribute:: vrfid
                
                	VRF Id
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Aaa.Radius.RadiusSourceInterface.ListOfSourceInterface, self).__init__()

                    self.yang_name = "list-of-source-interface"
                    self.yang_parent_name = "radius-source-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.ipaddrv4 = YLeaf(YType.str, "ipaddrv4")

                    self.ipaddrv6 = YLeaf(YType.str, "ipaddrv6")

                    self.vrfid = YLeaf(YType.uint32, "vrfid")
                    self._segment_path = lambda: "list-of-source-interface"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/radius-source-interface/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Radius.RadiusSourceInterface.ListOfSourceInterface, ['interface_name', 'ipaddrv4', 'ipaddrv6', 'vrfid'], name, value)


        class Servers(Entity):
            """
            List of RADIUS servers configured
            
            .. attribute:: server
            
            	RADIUS Server
            	**type**\: list of    :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.Servers.Server>`
            
            

            """

            _prefix = 'aaa-protocol-radius-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Aaa.Radius.Servers, self).__init__()

                self.yang_name = "servers"
                self.yang_parent_name = "radius"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"server" : ("server", Aaa.Radius.Servers.Server)}

                self.server = YList(self)
                self._segment_path = lambda: "servers"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Radius.Servers, [], name, value)


            class Server(Entity):
                """
                RADIUS Server
                
                .. attribute:: aborts
                
                	Total number of requests aborted
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_accepts
                
                	Number of access accepts
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_challenges
                
                	Number of access challenges
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_rejects
                
                	Number of access rejects
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_request_retransmits
                
                	Number of retransmitted                          access requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_requests
                
                	Number of access requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_timeouts
                
                	Number of access packets timed\-out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_port
                
                	Accounting port
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_requests
                
                	Number of accounting requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_responses
                
                	Number of accounting responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_retransmits
                
                	Number of retransmitted                          accounting requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_rtt
                
                	Round\-trip time for accounting                   in milliseconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: accounting_timeouts
                
                	Number of accounting packets                     timed\-out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_incorrect_responses
                
                	Number of incorrect accounting responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_port_number
                
                	Accounting Port number (standard port 1646)
                	**type**\:  int
                
                	**range:** 1..65535
                
                .. attribute:: acct_response_time
                
                	Average response time for authentication requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_server_error_responses
                
                	Number of server error accounting responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_transaction_failure
                
                	Number of failed authentication transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_transaction_successess
                
                	Number of succeeded authentication transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_unexpected_responses
                
                	Number of unexpected accounting responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: auth_port_number
                
                	Authentication Port number (standard port 1645)
                	**type**\:  int
                
                	**range:** 1..65535
                
                .. attribute:: authen_incorrect_responses
                
                	Number of incorrect authentication responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authen_response_time
                
                	Average response time for authentication requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authen_server_error_responses
                
                	Number of server error authentication responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authen_transaction_failure
                
                	Number of failed authentication transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authen_transaction_successess
                
                	Number of succeeded authentication transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authen_unexpected_responses
                
                	Number of unexpected authentication responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authentication_port
                
                	Authentication port
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authentication_rtt
                
                	Round\-trip time for authentication               in milliseconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: author_incorrect_responses
                
                	Number of incorrect authorization responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_request_timeouts
                
                	Number of access packets timed out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_requests
                
                	Number of access requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_response_time
                
                	Average response time for authorization requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_server_error_responses
                
                	Number of server error authorization responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_transaction_failure
                
                	Number of failed authorization transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_transaction_successess
                
                	Number of succeeded authorization transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_unexpected_responses
                
                	Number of unexpected authorization responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_access_authenticators
                
                	Number of bad access authenticators
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_access_responses
                
                	Number of bad access responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_accounting_authenticators
                
                	Number of bad accounting                         authenticators
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_accounting_responses
                
                	Number of bad accounting responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_state_duration
                
                	Elapsed time the server has been in              current state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: currently_throttled_access_reqs
                
                	No of currently throttled access reqs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dead_detect_time
                
                	Per\-server dead\-detect time in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: dead_detect_tries
                
                	Per\-server dead\-detect tries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dead_time
                
                	Per\-server deadtime in minutes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: minute
                
                .. attribute:: dropped_access_responses
                
                	Number of access responses dropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dropped_accounting_responses
                
                	Number of accounting responses                   dropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: family
                
                	IP address Family
                	**type**\:  str
                
                .. attribute:: group_name
                
                	Server group name for private server
                	**type**\:  str
                
                .. attribute:: ip_address
                
                	IP address of RADIUS server
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: ip_address_xr
                
                	IP address buffer
                	**type**\:  str
                
                .. attribute:: ipv4_address
                
                	IP address of RADIUS server
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: is_a_private_server
                
                	Is a private server
                	**type**\:  bool
                
                .. attribute:: is_quarantined
                
                	flag to indicate Server is quarantined           or not (Automated TEST in progress)
                	**type**\:  bool
                
                .. attribute:: last_deadtime
                
                	Time of Server being in DEAD state,              after last UP
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_acct_throttled
                
                	Max throttled acct transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_throttled_access_reqs
                
                	Max throttled access reqs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: packets_in
                
                	Total number of incoming packets read
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: packets_out
                
                	Total number of outgoing packets sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pending_access_requests
                
                	Number of pending access requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pending_accounting_requets
                
                	Number of pending accounting requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: previous_state_duration
                
                	Elapsed time the server was been in              previous state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: priority
                
                	A number that indicates the priority             of the server
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: redirected_requests
                
                	Number of requests redirected
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: replies_expected
                
                	Number of replies expected to arrive
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: retransmit
                
                	Per\-server retransmit
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: state
                
                	State of the server UP/DOWN
                	**type**\:  str
                
                .. attribute:: throttled_access_reqs
                
                	No of throttled access reqs stats
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttled_acct_failures_stats
                
                	No of acct discarded transaction
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttled_acct_timed_out_stats
                
                	No of acct transaction that is throttled is timedout
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttled_acct_transactions
                
                	No of throttled acct transactions stats
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttled_dropped_reqs
                
                	No of discarded access reqs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttled_timed_out_reqs
                
                	No of access reqs that is throttled is timedout
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttleda_acct_transactions
                
                	No of currently throttled acct transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: timeout_xr
                
                	Per\-server timeout in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: timeouts
                
                	Total number of packets timed\-out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_deadtime
                
                	Total time of Server being in DEAD               state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_acct_pending
                
                	Total acct test pending
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_acct_reqs
                
                	 Total acct test req
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_acct_response
                
                	Total acct test response
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_acct_timeouts
                
                	Total acct test timeouts
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_auth_pending
                
                	Total auth test pending
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_auth_reqs
                
                	Total auth test request
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_auth_response
                
                	Total auth test response
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_auth_timeouts
                
                	Total auth test timeouts
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: unknown_access_types
                
                	Number of packets received with unknown          type from authentication server
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: unknown_accounting_types
                
                	Number of packets received with unknown          type from accounting server
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Aaa.Radius.Servers.Server, self).__init__()

                    self.yang_name = "server"
                    self.yang_parent_name = "servers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.aborts = YLeaf(YType.uint32, "aborts")

                    self.access_accepts = YLeaf(YType.uint32, "access-accepts")

                    self.access_challenges = YLeaf(YType.uint32, "access-challenges")

                    self.access_rejects = YLeaf(YType.uint32, "access-rejects")

                    self.access_request_retransmits = YLeaf(YType.uint32, "access-request-retransmits")

                    self.access_requests = YLeaf(YType.uint32, "access-requests")

                    self.access_timeouts = YLeaf(YType.uint32, "access-timeouts")

                    self.accounting_port = YLeaf(YType.uint32, "accounting-port")

                    self.accounting_requests = YLeaf(YType.uint32, "accounting-requests")

                    self.accounting_responses = YLeaf(YType.uint32, "accounting-responses")

                    self.accounting_retransmits = YLeaf(YType.uint32, "accounting-retransmits")

                    self.accounting_rtt = YLeaf(YType.uint32, "accounting-rtt")

                    self.accounting_timeouts = YLeaf(YType.uint32, "accounting-timeouts")

                    self.acct_incorrect_responses = YLeaf(YType.uint32, "acct-incorrect-responses")

                    self.acct_port_number = YLeaf(YType.uint32, "acct-port-number")

                    self.acct_response_time = YLeaf(YType.uint32, "acct-response-time")

                    self.acct_server_error_responses = YLeaf(YType.uint32, "acct-server-error-responses")

                    self.acct_transaction_failure = YLeaf(YType.uint32, "acct-transaction-failure")

                    self.acct_transaction_successess = YLeaf(YType.uint32, "acct-transaction-successess")

                    self.acct_unexpected_responses = YLeaf(YType.uint32, "acct-unexpected-responses")

                    self.auth_port_number = YLeaf(YType.uint32, "auth-port-number")

                    self.authen_incorrect_responses = YLeaf(YType.uint32, "authen-incorrect-responses")

                    self.authen_response_time = YLeaf(YType.uint32, "authen-response-time")

                    self.authen_server_error_responses = YLeaf(YType.uint32, "authen-server-error-responses")

                    self.authen_transaction_failure = YLeaf(YType.uint32, "authen-transaction-failure")

                    self.authen_transaction_successess = YLeaf(YType.uint32, "authen-transaction-successess")

                    self.authen_unexpected_responses = YLeaf(YType.uint32, "authen-unexpected-responses")

                    self.authentication_port = YLeaf(YType.uint32, "authentication-port")

                    self.authentication_rtt = YLeaf(YType.uint32, "authentication-rtt")

                    self.author_incorrect_responses = YLeaf(YType.uint32, "author-incorrect-responses")

                    self.author_request_timeouts = YLeaf(YType.uint32, "author-request-timeouts")

                    self.author_requests = YLeaf(YType.uint32, "author-requests")

                    self.author_response_time = YLeaf(YType.uint32, "author-response-time")

                    self.author_server_error_responses = YLeaf(YType.uint32, "author-server-error-responses")

                    self.author_transaction_failure = YLeaf(YType.uint32, "author-transaction-failure")

                    self.author_transaction_successess = YLeaf(YType.uint32, "author-transaction-successess")

                    self.author_unexpected_responses = YLeaf(YType.uint32, "author-unexpected-responses")

                    self.bad_access_authenticators = YLeaf(YType.uint32, "bad-access-authenticators")

                    self.bad_access_responses = YLeaf(YType.uint32, "bad-access-responses")

                    self.bad_accounting_authenticators = YLeaf(YType.uint32, "bad-accounting-authenticators")

                    self.bad_accounting_responses = YLeaf(YType.uint32, "bad-accounting-responses")

                    self.current_state_duration = YLeaf(YType.uint32, "current-state-duration")

                    self.currently_throttled_access_reqs = YLeaf(YType.uint32, "currently-throttled-access-reqs")

                    self.dead_detect_time = YLeaf(YType.uint32, "dead-detect-time")

                    self.dead_detect_tries = YLeaf(YType.uint32, "dead-detect-tries")

                    self.dead_time = YLeaf(YType.uint32, "dead-time")

                    self.dropped_access_responses = YLeaf(YType.uint32, "dropped-access-responses")

                    self.dropped_accounting_responses = YLeaf(YType.uint32, "dropped-accounting-responses")

                    self.family = YLeaf(YType.str, "family")

                    self.group_name = YLeaf(YType.str, "group-name")

                    self.ip_address = YLeaf(YType.str, "ip-address")

                    self.ip_address_xr = YLeaf(YType.str, "ip-address-xr")

                    self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                    self.is_a_private_server = YLeaf(YType.boolean, "is-a-private-server")

                    self.is_quarantined = YLeaf(YType.boolean, "is-quarantined")

                    self.last_deadtime = YLeaf(YType.uint32, "last-deadtime")

                    self.max_acct_throttled = YLeaf(YType.uint32, "max-acct-throttled")

                    self.max_throttled_access_reqs = YLeaf(YType.uint32, "max-throttled-access-reqs")

                    self.packets_in = YLeaf(YType.uint32, "packets-in")

                    self.packets_out = YLeaf(YType.uint32, "packets-out")

                    self.pending_access_requests = YLeaf(YType.uint32, "pending-access-requests")

                    self.pending_accounting_requets = YLeaf(YType.uint32, "pending-accounting-requets")

                    self.previous_state_duration = YLeaf(YType.uint32, "previous-state-duration")

                    self.priority = YLeaf(YType.uint32, "priority")

                    self.redirected_requests = YLeaf(YType.uint32, "redirected-requests")

                    self.replies_expected = YLeaf(YType.uint32, "replies-expected")

                    self.retransmit = YLeaf(YType.uint32, "retransmit")

                    self.state = YLeaf(YType.str, "state")

                    self.throttled_access_reqs = YLeaf(YType.uint32, "throttled-access-reqs")

                    self.throttled_acct_failures_stats = YLeaf(YType.uint32, "throttled-acct-failures-stats")

                    self.throttled_acct_timed_out_stats = YLeaf(YType.uint32, "throttled-acct-timed-out-stats")

                    self.throttled_acct_transactions = YLeaf(YType.uint32, "throttled-acct-transactions")

                    self.throttled_dropped_reqs = YLeaf(YType.uint32, "throttled-dropped-reqs")

                    self.throttled_timed_out_reqs = YLeaf(YType.uint32, "throttled-timed-out-reqs")

                    self.throttleda_acct_transactions = YLeaf(YType.uint32, "throttleda-acct-transactions")

                    self.timeout_xr = YLeaf(YType.uint32, "timeout-xr")

                    self.timeouts = YLeaf(YType.uint32, "timeouts")

                    self.total_deadtime = YLeaf(YType.uint32, "total-deadtime")

                    self.total_test_acct_pending = YLeaf(YType.uint32, "total-test-acct-pending")

                    self.total_test_acct_reqs = YLeaf(YType.uint32, "total-test-acct-reqs")

                    self.total_test_acct_response = YLeaf(YType.uint32, "total-test-acct-response")

                    self.total_test_acct_timeouts = YLeaf(YType.uint32, "total-test-acct-timeouts")

                    self.total_test_auth_pending = YLeaf(YType.uint32, "total-test-auth-pending")

                    self.total_test_auth_reqs = YLeaf(YType.uint32, "total-test-auth-reqs")

                    self.total_test_auth_response = YLeaf(YType.uint32, "total-test-auth-response")

                    self.total_test_auth_timeouts = YLeaf(YType.uint32, "total-test-auth-timeouts")

                    self.unknown_access_types = YLeaf(YType.uint32, "unknown-access-types")

                    self.unknown_accounting_types = YLeaf(YType.uint32, "unknown-accounting-types")
                    self._segment_path = lambda: "server"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/servers/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Radius.Servers.Server, ['aborts', 'access_accepts', 'access_challenges', 'access_rejects', 'access_request_retransmits', 'access_requests', 'access_timeouts', 'accounting_port', 'accounting_requests', 'accounting_responses', 'accounting_retransmits', 'accounting_rtt', 'accounting_timeouts', 'acct_incorrect_responses', 'acct_port_number', 'acct_response_time', 'acct_server_error_responses', 'acct_transaction_failure', 'acct_transaction_successess', 'acct_unexpected_responses', 'auth_port_number', 'authen_incorrect_responses', 'authen_response_time', 'authen_server_error_responses', 'authen_transaction_failure', 'authen_transaction_successess', 'authen_unexpected_responses', 'authentication_port', 'authentication_rtt', 'author_incorrect_responses', 'author_request_timeouts', 'author_requests', 'author_response_time', 'author_server_error_responses', 'author_transaction_failure', 'author_transaction_successess', 'author_unexpected_responses', 'bad_access_authenticators', 'bad_access_responses', 'bad_accounting_authenticators', 'bad_accounting_responses', 'current_state_duration', 'currently_throttled_access_reqs', 'dead_detect_time', 'dead_detect_tries', 'dead_time', 'dropped_access_responses', 'dropped_accounting_responses', 'family', 'group_name', 'ip_address', 'ip_address_xr', 'ipv4_address', 'is_a_private_server', 'is_quarantined', 'last_deadtime', 'max_acct_throttled', 'max_throttled_access_reqs', 'packets_in', 'packets_out', 'pending_access_requests', 'pending_accounting_requets', 'previous_state_duration', 'priority', 'redirected_requests', 'replies_expected', 'retransmit', 'state', 'throttled_access_reqs', 'throttled_acct_failures_stats', 'throttled_acct_timed_out_stats', 'throttled_acct_transactions', 'throttled_dropped_reqs', 'throttled_timed_out_reqs', 'throttleda_acct_transactions', 'timeout_xr', 'timeouts', 'total_deadtime', 'total_test_acct_pending', 'total_test_acct_reqs', 'total_test_acct_response', 'total_test_acct_timeouts', 'total_test_auth_pending', 'total_test_auth_reqs', 'total_test_auth_response', 'total_test_auth_timeouts', 'unknown_access_types', 'unknown_accounting_types'], name, value)


    class Tacacs(Entity):
        """
        TACACS operational data
        
        .. attribute:: requests
        
        	TACACS Active Request List
        	**type**\:   :py:class:`Requests <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Requests>`
        
        .. attribute:: server_groups
        
        	TACACS sg Information
        	**type**\:   :py:class:`ServerGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.ServerGroups>`
        
        .. attribute:: servers
        
        	TACACS server Information
        	**type**\:   :py:class:`Servers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Servers>`
        
        

        """

        _prefix = 'aaa-tacacs-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Tacacs, self).__init__()

            self.yang_name = "tacacs"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"requests" : ("requests", Aaa.Tacacs.Requests), "server-groups" : ("server_groups", Aaa.Tacacs.ServerGroups), "servers" : ("servers", Aaa.Tacacs.Servers)}
            self._child_list_classes = {}

            self.requests = Aaa.Tacacs.Requests()
            self.requests.parent = self
            self._children_name_map["requests"] = "requests"
            self._children_yang_names.add("requests")

            self.server_groups = Aaa.Tacacs.ServerGroups()
            self.server_groups.parent = self
            self._children_name_map["server_groups"] = "server-groups"
            self._children_yang_names.add("server-groups")

            self.servers = Aaa.Tacacs.Servers()
            self.servers.parent = self
            self._children_name_map["servers"] = "servers"
            self._children_yang_names.add("servers")
            self._segment_path = lambda: "Cisco-IOS-XR-aaa-tacacs-oper:tacacs"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self._segment_path()


        class Requests(Entity):
            """
            TACACS Active Request List
            
            .. attribute:: request
            
            	request
            	**type**\: list of    :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Requests.Request>`
            
            

            """

            _prefix = 'aaa-tacacs-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Tacacs.Requests, self).__init__()

                self.yang_name = "requests"
                self.yang_parent_name = "tacacs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"request" : ("request", Aaa.Tacacs.Requests.Request)}

                self.request = YList(self)
                self._segment_path = lambda: "requests"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Tacacs.Requests, [], name, value)


            class Request(Entity):
                """
                request
                
                .. attribute:: tacacs_requestbag
                
                	tacacs requestbag
                	**type**\: list of    :py:class:`TacacsRequestbag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Requests.Request.TacacsRequestbag>`
                
                

                """

                _prefix = 'aaa-tacacs-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Tacacs.Requests.Request, self).__init__()

                    self.yang_name = "request"
                    self.yang_parent_name = "requests"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"tacacs-requestbag" : ("tacacs_requestbag", Aaa.Tacacs.Requests.Request.TacacsRequestbag)}

                    self.tacacs_requestbag = YList(self)
                    self._segment_path = lambda: "request"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/requests/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Tacacs.Requests.Request, [], name, value)


                class TacacsRequestbag(Entity):
                    """
                    tacacs requestbag
                    
                    .. attribute:: bytes_in
                    
                    	bytes read from socket
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_out
                    
                    	bytes written
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: in_pak_size
                    
                    	size of the packet to be received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: out_pak_size
                    
                    	size of the packet to be sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pak_type
                    
                    	the type of packet
                    	**type**\:  str
                    
                    .. attribute:: session_id
                    
                    	same as in pkt hdr
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: sock
                    
                    	socket number
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: time_remaining
                    
                    	time remaining for this request
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'aaa-tacacs-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Tacacs.Requests.Request.TacacsRequestbag, self).__init__()

                        self.yang_name = "tacacs-requestbag"
                        self.yang_parent_name = "request"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.bytes_in = YLeaf(YType.uint32, "bytes-in")

                        self.bytes_out = YLeaf(YType.uint32, "bytes-out")

                        self.in_pak_size = YLeaf(YType.uint32, "in-pak-size")

                        self.out_pak_size = YLeaf(YType.uint32, "out-pak-size")

                        self.pak_type = YLeaf(YType.str, "pak-type")

                        self.session_id = YLeaf(YType.int32, "session-id")

                        self.sock = YLeaf(YType.int32, "sock")

                        self.time_remaining = YLeaf(YType.uint32, "time-remaining")
                        self._segment_path = lambda: "tacacs-requestbag"
                        self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/requests/request/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Tacacs.Requests.Request.TacacsRequestbag, ['bytes_in', 'bytes_out', 'in_pak_size', 'out_pak_size', 'pak_type', 'session_id', 'sock', 'time_remaining'], name, value)


        class ServerGroups(Entity):
            """
            TACACS sg Information
            
            .. attribute:: server_group
            
            	server group
            	**type**\: list of    :py:class:`ServerGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.ServerGroups.ServerGroup>`
            
            

            """

            _prefix = 'aaa-tacacs-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Tacacs.ServerGroups, self).__init__()

                self.yang_name = "server-groups"
                self.yang_parent_name = "tacacs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"server-group" : ("server_group", Aaa.Tacacs.ServerGroups.ServerGroup)}

                self.server_group = YList(self)
                self._segment_path = lambda: "server-groups"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Tacacs.ServerGroups, [], name, value)


            class ServerGroup(Entity):
                """
                server group
                
                .. attribute:: group_name
                
                	name of the server group
                	**type**\:  str
                
                .. attribute:: server
                
                	list of servers in this group
                	**type**\: list of    :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.ServerGroups.ServerGroup.Server>`
                
                .. attribute:: sg_map_num
                
                	server group mapped number
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: vrf_name
                
                	vrf of the group
                	**type**\:  str
                
                	**length:** 0..33
                
                

                """

                _prefix = 'aaa-tacacs-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Tacacs.ServerGroups.ServerGroup, self).__init__()

                    self.yang_name = "server-group"
                    self.yang_parent_name = "server-groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"server" : ("server", Aaa.Tacacs.ServerGroups.ServerGroup.Server)}

                    self.group_name = YLeaf(YType.str, "group-name")

                    self.sg_map_num = YLeaf(YType.uint32, "sg-map-num")

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.server = YList(self)
                    self._segment_path = lambda: "server-group"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/server-groups/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Tacacs.ServerGroups.ServerGroup, ['group_name', 'sg_map_num', 'vrf_name'], name, value)


                class Server(Entity):
                    """
                    list of servers in this group
                    
                    .. attribute:: aborts
                    
                    	abort count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: addr
                    
                    	internet address of T+ server
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: addr_buf
                    
                    	IP address buffer
                    	**type**\:  str
                    
                    	**length:** 0..46
                    
                    .. attribute:: bytes_in
                    
                    	# of bytes read
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_out
                    
                    	# of bytes out
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: closes
                    
                    	socket closes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: conn_up
                    
                    	is the server connected ?
                    	**type**\:  bool
                    
                    .. attribute:: errors
                    
                    	error count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: family
                    
                    	IP address Family
                    	**type**\:  str
                    
                    	**length:** 0..5
                    
                    .. attribute:: is_private
                    
                    	is this a private server ?
                    	**type**\:  bool
                    
                    .. attribute:: opens
                    
                    	socket opens
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: paks_in
                    
                    	# of incoming packets read
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: paks_out
                    
                    	# of outgoing packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: port
                    
                    	per server port to use
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: replies_expected
                    
                    	# of replies expected to arrive
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: single_connect
                    
                    	is this a single connect server ?
                    	**type**\:  bool
                    
                    .. attribute:: timeout
                    
                    	per\-server timeout
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: up
                    
                    	is the server UP or down ?
                    	**type**\:  bool
                    
                    .. attribute:: vrf_name
                    
                    	VRF in which server is reachable
                    	**type**\:  str
                    
                    	**length:** 0..33
                    
                    

                    """

                    _prefix = 'aaa-tacacs-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Tacacs.ServerGroups.ServerGroup.Server, self).__init__()

                        self.yang_name = "server"
                        self.yang_parent_name = "server-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.aborts = YLeaf(YType.uint32, "aborts")

                        self.addr = YLeaf(YType.str, "addr")

                        self.addr_buf = YLeaf(YType.str, "addr-buf")

                        self.bytes_in = YLeaf(YType.uint32, "bytes-in")

                        self.bytes_out = YLeaf(YType.uint32, "bytes-out")

                        self.closes = YLeaf(YType.uint32, "closes")

                        self.conn_up = YLeaf(YType.boolean, "conn-up")

                        self.errors = YLeaf(YType.uint32, "errors")

                        self.family = YLeaf(YType.str, "family")

                        self.is_private = YLeaf(YType.boolean, "is-private")

                        self.opens = YLeaf(YType.uint32, "opens")

                        self.paks_in = YLeaf(YType.uint32, "paks-in")

                        self.paks_out = YLeaf(YType.uint32, "paks-out")

                        self.port = YLeaf(YType.uint32, "port")

                        self.replies_expected = YLeaf(YType.uint32, "replies-expected")

                        self.single_connect = YLeaf(YType.boolean, "single-connect")

                        self.timeout = YLeaf(YType.uint32, "timeout")

                        self.up = YLeaf(YType.boolean, "up")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")
                        self._segment_path = lambda: "server"
                        self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/server-groups/server-group/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Tacacs.ServerGroups.ServerGroup.Server, ['aborts', 'addr', 'addr_buf', 'bytes_in', 'bytes_out', 'closes', 'conn_up', 'errors', 'family', 'is_private', 'opens', 'paks_in', 'paks_out', 'port', 'replies_expected', 'single_connect', 'timeout', 'up', 'vrf_name'], name, value)


        class Servers(Entity):
            """
            TACACS server Information
            
            .. attribute:: server
            
            	server
            	**type**\: list of    :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Servers.Server>`
            
            

            """

            _prefix = 'aaa-tacacs-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Tacacs.Servers, self).__init__()

                self.yang_name = "servers"
                self.yang_parent_name = "tacacs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"server" : ("server", Aaa.Tacacs.Servers.Server)}

                self.server = YList(self)
                self._segment_path = lambda: "servers"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Tacacs.Servers, [], name, value)


            class Server(Entity):
                """
                server
                
                .. attribute:: aborts
                
                	abort count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: addr
                
                	internet address of T+ server
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: addr_buf
                
                	IP address buffer
                	**type**\:  str
                
                	**length:** 0..46
                
                .. attribute:: bytes_in
                
                	# of bytes read
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: byte
                
                .. attribute:: bytes_out
                
                	# of bytes out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: byte
                
                .. attribute:: closes
                
                	socket closes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: conn_up
                
                	is the server connected ?
                	**type**\:  bool
                
                .. attribute:: errors
                
                	error count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: family
                
                	IP address Family
                	**type**\:  str
                
                	**length:** 0..5
                
                .. attribute:: is_private
                
                	is this a private server ?
                	**type**\:  bool
                
                .. attribute:: opens
                
                	socket opens
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: paks_in
                
                	# of incoming packets read
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: paks_out
                
                	# of outgoing packets sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: port
                
                	per server port to use
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: replies_expected
                
                	# of replies expected to arrive
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: single_connect
                
                	is this a single connect server ?
                	**type**\:  bool
                
                .. attribute:: timeout
                
                	per\-server timeout
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: up
                
                	is the server UP or down ?
                	**type**\:  bool
                
                .. attribute:: vrf_name
                
                	VRF in which server is reachable
                	**type**\:  str
                
                	**length:** 0..33
                
                

                """

                _prefix = 'aaa-tacacs-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Tacacs.Servers.Server, self).__init__()

                    self.yang_name = "server"
                    self.yang_parent_name = "servers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.aborts = YLeaf(YType.uint32, "aborts")

                    self.addr = YLeaf(YType.str, "addr")

                    self.addr_buf = YLeaf(YType.str, "addr-buf")

                    self.bytes_in = YLeaf(YType.uint32, "bytes-in")

                    self.bytes_out = YLeaf(YType.uint32, "bytes-out")

                    self.closes = YLeaf(YType.uint32, "closes")

                    self.conn_up = YLeaf(YType.boolean, "conn-up")

                    self.errors = YLeaf(YType.uint32, "errors")

                    self.family = YLeaf(YType.str, "family")

                    self.is_private = YLeaf(YType.boolean, "is-private")

                    self.opens = YLeaf(YType.uint32, "opens")

                    self.paks_in = YLeaf(YType.uint32, "paks-in")

                    self.paks_out = YLeaf(YType.uint32, "paks-out")

                    self.port = YLeaf(YType.uint32, "port")

                    self.replies_expected = YLeaf(YType.uint32, "replies-expected")

                    self.single_connect = YLeaf(YType.boolean, "single-connect")

                    self.timeout = YLeaf(YType.uint32, "timeout")

                    self.up = YLeaf(YType.boolean, "up")

                    self.vrf_name = YLeaf(YType.str, "vrf-name")
                    self._segment_path = lambda: "server"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/servers/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Tacacs.Servers.Server, ['aborts', 'addr', 'addr_buf', 'bytes_in', 'bytes_out', 'closes', 'conn_up', 'errors', 'family', 'is_private', 'opens', 'paks_in', 'paks_out', 'port', 'replies_expected', 'single_connect', 'timeout', 'up', 'vrf_name'], name, value)


    class TaskMap(Entity):
        """
        Task map of current user
        
        .. attribute:: authenmethod
        
        	Authentication method
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: name
        
        	Name of the usergroup
        	**type**\:  str
        
        .. attribute:: taskmap
        
        	Task map details
        	**type**\:  list of str
        
        .. attribute:: usergroup
        
        	Component usergroups
        	**type**\:  list of str
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.TaskMap, self).__init__()

            self.yang_name = "task-map"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.authenmethod = YLeaf(YType.int32, "authenmethod")

            self.name = YLeaf(YType.str, "name")

            self.taskmap = YLeafList(YType.str, "taskmap")

            self.usergroup = YLeafList(YType.str, "usergroup")
            self._segment_path = lambda: "task-map"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.TaskMap, ['authenmethod', 'name', 'taskmap', 'usergroup'], name, value)


    class Taskgroups(Entity):
        """
        Individual taskgroups container
        
        .. attribute:: taskgroup
        
        	Specific Taskgroup Information
        	**type**\: list of    :py:class:`Taskgroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup>`
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Taskgroups, self).__init__()

            self.yang_name = "taskgroups"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"taskgroup" : ("taskgroup", Aaa.Taskgroups.Taskgroup)}

            self.taskgroup = YList(self)
            self._segment_path = lambda: "taskgroups"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.Taskgroups, [], name, value)


        class Taskgroup(Entity):
            """
            Specific Taskgroup Information
            
            .. attribute:: name  <key>
            
            	Taskgroup name
            	**type**\:  str
            
            .. attribute:: included_task_ids
            
            	Task\-ids included
            	**type**\:   :py:class:`IncludedTaskIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.IncludedTaskIds>`
            
            .. attribute:: name_xr
            
            	Name of the taskgroup
            	**type**\:  str
            
            .. attribute:: task_map
            
            	Computed task map
            	**type**\:   :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.TaskMap>`
            
            

            """

            _prefix = 'aaa-locald-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Taskgroups.Taskgroup, self).__init__()

                self.yang_name = "taskgroup"
                self.yang_parent_name = "taskgroups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"included-task-ids" : ("included_task_ids", Aaa.Taskgroups.Taskgroup.IncludedTaskIds), "task-map" : ("task_map", Aaa.Taskgroups.Taskgroup.TaskMap)}
                self._child_list_classes = {}

                self.name = YLeaf(YType.str, "name")

                self.name_xr = YLeaf(YType.str, "name-xr")

                self.included_task_ids = Aaa.Taskgroups.Taskgroup.IncludedTaskIds()
                self.included_task_ids.parent = self
                self._children_name_map["included_task_ids"] = "included-task-ids"
                self._children_yang_names.add("included-task-ids")

                self.task_map = Aaa.Taskgroups.Taskgroup.TaskMap()
                self.task_map.parent = self
                self._children_name_map["task_map"] = "task-map"
                self._children_yang_names.add("task-map")
                self._segment_path = lambda: "taskgroup" + "[name='" + self.name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/taskgroups/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Taskgroups.Taskgroup, ['name', 'name_xr'], name, value)


            class IncludedTaskIds(Entity):
                """
                Task\-ids included
                
                .. attribute:: tasks
                
                	List of permitted tasks
                	**type**\: list of    :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks>`
                
                

                """

                _prefix = 'aaa-locald-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Taskgroups.Taskgroup.IncludedTaskIds, self).__init__()

                    self.yang_name = "included-task-ids"
                    self.yang_parent_name = "taskgroup"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"tasks" : ("tasks", Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks)}

                    self.tasks = YList(self)
                    self._segment_path = lambda: "included-task-ids"

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Taskgroups.Taskgroup.IncludedTaskIds, [], name, value)


                class Tasks(Entity):
                    """
                    List of permitted tasks
                    
                    .. attribute:: debug
                    
                    	Is debug permitted?
                    	**type**\:  bool
                    
                    .. attribute:: execute
                    
                    	Is execute permitted?
                    	**type**\:  bool
                    
                    .. attribute:: read
                    
                    	Is read permitted?
                    	**type**\:  bool
                    
                    .. attribute:: task_id
                    
                    	Name of the task\-id
                    	**type**\:  str
                    
                    .. attribute:: write
                    
                    	Is write permitted?
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks, self).__init__()

                        self.yang_name = "tasks"
                        self.yang_parent_name = "included-task-ids"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.debug = YLeaf(YType.boolean, "debug")

                        self.execute = YLeaf(YType.boolean, "execute")

                        self.read = YLeaf(YType.boolean, "read")

                        self.task_id = YLeaf(YType.str, "task-id")

                        self.write = YLeaf(YType.boolean, "write")
                        self._segment_path = lambda: "tasks"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks, ['debug', 'execute', 'read', 'task_id', 'write'], name, value)


            class TaskMap(Entity):
                """
                Computed task map
                
                .. attribute:: tasks
                
                	List of permitted tasks
                	**type**\: list of    :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.TaskMap.Tasks>`
                
                

                """

                _prefix = 'aaa-locald-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Taskgroups.Taskgroup.TaskMap, self).__init__()

                    self.yang_name = "task-map"
                    self.yang_parent_name = "taskgroup"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"tasks" : ("tasks", Aaa.Taskgroups.Taskgroup.TaskMap.Tasks)}

                    self.tasks = YList(self)
                    self._segment_path = lambda: "task-map"

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Taskgroups.Taskgroup.TaskMap, [], name, value)


                class Tasks(Entity):
                    """
                    List of permitted tasks
                    
                    .. attribute:: debug
                    
                    	Is debug permitted?
                    	**type**\:  bool
                    
                    .. attribute:: execute
                    
                    	Is execute permitted?
                    	**type**\:  bool
                    
                    .. attribute:: read
                    
                    	Is read permitted?
                    	**type**\:  bool
                    
                    .. attribute:: task_id
                    
                    	Name of the task\-id
                    	**type**\:  str
                    
                    .. attribute:: write
                    
                    	Is write permitted?
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Taskgroups.Taskgroup.TaskMap.Tasks, self).__init__()

                        self.yang_name = "tasks"
                        self.yang_parent_name = "task-map"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.debug = YLeaf(YType.boolean, "debug")

                        self.execute = YLeaf(YType.boolean, "execute")

                        self.read = YLeaf(YType.boolean, "read")

                        self.task_id = YLeaf(YType.str, "task-id")

                        self.write = YLeaf(YType.boolean, "write")
                        self._segment_path = lambda: "tasks"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Taskgroups.Taskgroup.TaskMap.Tasks, ['debug', 'execute', 'read', 'task_id', 'write'], name, value)


    class Usergroups(Entity):
        """
        Container for individual usergroup Information
        
        .. attribute:: usergroup
        
        	Specific Usergroup Information
        	**type**\: list of    :py:class:`Usergroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup>`
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Usergroups, self).__init__()

            self.yang_name = "usergroups"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"usergroup" : ("usergroup", Aaa.Usergroups.Usergroup)}

            self.usergroup = YList(self)
            self._segment_path = lambda: "usergroups"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.Usergroups, [], name, value)


        class Usergroup(Entity):
            """
            Specific Usergroup Information
            
            .. attribute:: name  <key>
            
            	Usergroup name
            	**type**\:  str
            
            .. attribute:: name_xr
            
            	Name of the usergroup
            	**type**\:  str
            
            .. attribute:: task_map
            
            	Computed task map
            	**type**\:   :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.TaskMap>`
            
            .. attribute:: taskgroup
            
            	Component taskgroups
            	**type**\: list of    :py:class:`Taskgroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup>`
            
            

            """

            _prefix = 'aaa-locald-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Usergroups.Usergroup, self).__init__()

                self.yang_name = "usergroup"
                self.yang_parent_name = "usergroups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"task-map" : ("task_map", Aaa.Usergroups.Usergroup.TaskMap)}
                self._child_list_classes = {"taskgroup" : ("taskgroup", Aaa.Usergroups.Usergroup.Taskgroup)}

                self.name = YLeaf(YType.str, "name")

                self.name_xr = YLeaf(YType.str, "name-xr")

                self.task_map = Aaa.Usergroups.Usergroup.TaskMap()
                self.task_map.parent = self
                self._children_name_map["task_map"] = "task-map"
                self._children_yang_names.add("task-map")

                self.taskgroup = YList(self)
                self._segment_path = lambda: "usergroup" + "[name='" + self.name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/usergroups/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Usergroups.Usergroup, ['name', 'name_xr'], name, value)


            class TaskMap(Entity):
                """
                Computed task map
                
                .. attribute:: tasks
                
                	List of permitted tasks
                	**type**\: list of    :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.TaskMap.Tasks>`
                
                

                """

                _prefix = 'aaa-locald-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Usergroups.Usergroup.TaskMap, self).__init__()

                    self.yang_name = "task-map"
                    self.yang_parent_name = "usergroup"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"tasks" : ("tasks", Aaa.Usergroups.Usergroup.TaskMap.Tasks)}

                    self.tasks = YList(self)
                    self._segment_path = lambda: "task-map"

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Usergroups.Usergroup.TaskMap, [], name, value)


                class Tasks(Entity):
                    """
                    List of permitted tasks
                    
                    .. attribute:: debug
                    
                    	Is debug permitted?
                    	**type**\:  bool
                    
                    .. attribute:: execute
                    
                    	Is execute permitted?
                    	**type**\:  bool
                    
                    .. attribute:: read
                    
                    	Is read permitted?
                    	**type**\:  bool
                    
                    .. attribute:: task_id
                    
                    	Name of the task\-id
                    	**type**\:  str
                    
                    .. attribute:: write
                    
                    	Is write permitted?
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Usergroups.Usergroup.TaskMap.Tasks, self).__init__()

                        self.yang_name = "tasks"
                        self.yang_parent_name = "task-map"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.debug = YLeaf(YType.boolean, "debug")

                        self.execute = YLeaf(YType.boolean, "execute")

                        self.read = YLeaf(YType.boolean, "read")

                        self.task_id = YLeaf(YType.str, "task-id")

                        self.write = YLeaf(YType.boolean, "write")
                        self._segment_path = lambda: "tasks"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Usergroups.Usergroup.TaskMap.Tasks, ['debug', 'execute', 'read', 'task_id', 'write'], name, value)


            class Taskgroup(Entity):
                """
                Component taskgroups
                
                .. attribute:: included_task_ids
                
                	Task\-ids included
                	**type**\:   :py:class:`IncludedTaskIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds>`
                
                .. attribute:: name_xr
                
                	Name of the taskgroup
                	**type**\:  str
                
                .. attribute:: task_map
                
                	Computed task map
                	**type**\:   :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.TaskMap>`
                
                

                """

                _prefix = 'aaa-locald-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Usergroups.Usergroup.Taskgroup, self).__init__()

                    self.yang_name = "taskgroup"
                    self.yang_parent_name = "usergroup"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"included-task-ids" : ("included_task_ids", Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds), "task-map" : ("task_map", Aaa.Usergroups.Usergroup.Taskgroup.TaskMap)}
                    self._child_list_classes = {}

                    self.name_xr = YLeaf(YType.str, "name-xr")

                    self.included_task_ids = Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds()
                    self.included_task_ids.parent = self
                    self._children_name_map["included_task_ids"] = "included-task-ids"
                    self._children_yang_names.add("included-task-ids")

                    self.task_map = Aaa.Usergroups.Usergroup.Taskgroup.TaskMap()
                    self.task_map.parent = self
                    self._children_name_map["task_map"] = "task-map"
                    self._children_yang_names.add("task-map")
                    self._segment_path = lambda: "taskgroup"

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Usergroups.Usergroup.Taskgroup, ['name_xr'], name, value)


                class IncludedTaskIds(Entity):
                    """
                    Task\-ids included
                    
                    .. attribute:: tasks
                    
                    	List of permitted tasks
                    	**type**\: list of    :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks>`
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds, self).__init__()

                        self.yang_name = "included-task-ids"
                        self.yang_parent_name = "taskgroup"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"tasks" : ("tasks", Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks)}

                        self.tasks = YList(self)
                        self._segment_path = lambda: "included-task-ids"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds, [], name, value)


                    class Tasks(Entity):
                        """
                        List of permitted tasks
                        
                        .. attribute:: debug
                        
                        	Is debug permitted?
                        	**type**\:  bool
                        
                        .. attribute:: execute
                        
                        	Is execute permitted?
                        	**type**\:  bool
                        
                        .. attribute:: read
                        
                        	Is read permitted?
                        	**type**\:  bool
                        
                        .. attribute:: task_id
                        
                        	Name of the task\-id
                        	**type**\:  str
                        
                        .. attribute:: write
                        
                        	Is write permitted?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'aaa-locald-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks, self).__init__()

                            self.yang_name = "tasks"
                            self.yang_parent_name = "included-task-ids"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.debug = YLeaf(YType.boolean, "debug")

                            self.execute = YLeaf(YType.boolean, "execute")

                            self.read = YLeaf(YType.boolean, "read")

                            self.task_id = YLeaf(YType.str, "task-id")

                            self.write = YLeaf(YType.boolean, "write")
                            self._segment_path = lambda: "tasks"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks, ['debug', 'execute', 'read', 'task_id', 'write'], name, value)


                class TaskMap(Entity):
                    """
                    Computed task map
                    
                    .. attribute:: tasks
                    
                    	List of permitted tasks
                    	**type**\: list of    :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks>`
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Usergroups.Usergroup.Taskgroup.TaskMap, self).__init__()

                        self.yang_name = "task-map"
                        self.yang_parent_name = "taskgroup"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"tasks" : ("tasks", Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks)}

                        self.tasks = YList(self)
                        self._segment_path = lambda: "task-map"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Usergroups.Usergroup.Taskgroup.TaskMap, [], name, value)


                    class Tasks(Entity):
                        """
                        List of permitted tasks
                        
                        .. attribute:: debug
                        
                        	Is debug permitted?
                        	**type**\:  bool
                        
                        .. attribute:: execute
                        
                        	Is execute permitted?
                        	**type**\:  bool
                        
                        .. attribute:: read
                        
                        	Is read permitted?
                        	**type**\:  bool
                        
                        .. attribute:: task_id
                        
                        	Name of the task\-id
                        	**type**\:  str
                        
                        .. attribute:: write
                        
                        	Is write permitted?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'aaa-locald-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks, self).__init__()

                            self.yang_name = "tasks"
                            self.yang_parent_name = "task-map"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.debug = YLeaf(YType.boolean, "debug")

                            self.execute = YLeaf(YType.boolean, "execute")

                            self.read = YLeaf(YType.boolean, "read")

                            self.task_id = YLeaf(YType.str, "task-id")

                            self.write = YLeaf(YType.boolean, "write")
                            self._segment_path = lambda: "tasks"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks, ['debug', 'execute', 'read', 'task_id', 'write'], name, value)


    class Users(Entity):
        """
        Container for individual local user information
        
        .. attribute:: user
        
        	Specific local user information
        	**type**\: list of    :py:class:`User <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users.User>`
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Users, self).__init__()

            self.yang_name = "users"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"user" : ("user", Aaa.Users.User)}

            self.user = YList(self)
            self._segment_path = lambda: "users"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.Users, [], name, value)


        class User(Entity):
            """
            Specific local user information
            
            .. attribute:: name  <key>
            
            	Username
            	**type**\:  str
            
            .. attribute:: admin_user
            
            	Is admin plane user ?
            	**type**\:  bool
            
            .. attribute:: first_user
            
            	Is first user ?
            	**type**\:  bool
            
            .. attribute:: name_xr
            
            	Username
            	**type**\:  str
            
            .. attribute:: task_map
            
            	Computed taskmap
            	**type**\:   :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users.User.TaskMap>`
            
            .. attribute:: usergroup
            
            	Member usergroups
            	**type**\:  list of str
            
            

            """

            _prefix = 'aaa-locald-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Users.User, self).__init__()

                self.yang_name = "user"
                self.yang_parent_name = "users"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"task-map" : ("task_map", Aaa.Users.User.TaskMap)}
                self._child_list_classes = {}

                self.name = YLeaf(YType.str, "name")

                self.admin_user = YLeaf(YType.boolean, "admin-user")

                self.first_user = YLeaf(YType.boolean, "first-user")

                self.name_xr = YLeaf(YType.str, "name-xr")

                self.usergroup = YLeafList(YType.str, "usergroup")

                self.task_map = Aaa.Users.User.TaskMap()
                self.task_map.parent = self
                self._children_name_map["task_map"] = "task-map"
                self._children_yang_names.add("task-map")
                self._segment_path = lambda: "user" + "[name='" + self.name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/users/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Users.User, ['name', 'admin_user', 'first_user', 'name_xr', 'usergroup'], name, value)


            class TaskMap(Entity):
                """
                Computed taskmap
                
                .. attribute:: tasks
                
                	List of permitted tasks
                	**type**\: list of    :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users.User.TaskMap.Tasks>`
                
                

                """

                _prefix = 'aaa-locald-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Users.User.TaskMap, self).__init__()

                    self.yang_name = "task-map"
                    self.yang_parent_name = "user"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"tasks" : ("tasks", Aaa.Users.User.TaskMap.Tasks)}

                    self.tasks = YList(self)
                    self._segment_path = lambda: "task-map"

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Users.User.TaskMap, [], name, value)


                class Tasks(Entity):
                    """
                    List of permitted tasks
                    
                    .. attribute:: debug
                    
                    	Is debug permitted?
                    	**type**\:  bool
                    
                    .. attribute:: execute
                    
                    	Is execute permitted?
                    	**type**\:  bool
                    
                    .. attribute:: read
                    
                    	Is read permitted?
                    	**type**\:  bool
                    
                    .. attribute:: task_id
                    
                    	Name of the task\-id
                    	**type**\:  str
                    
                    .. attribute:: write
                    
                    	Is write permitted?
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Users.User.TaskMap.Tasks, self).__init__()

                        self.yang_name = "tasks"
                        self.yang_parent_name = "task-map"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.debug = YLeaf(YType.boolean, "debug")

                        self.execute = YLeaf(YType.boolean, "execute")

                        self.read = YLeaf(YType.boolean, "read")

                        self.task_id = YLeaf(YType.str, "task-id")

                        self.write = YLeaf(YType.boolean, "write")
                        self._segment_path = lambda: "tasks"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Users.User.TaskMap.Tasks, ['debug', 'execute', 'read', 'task_id', 'write'], name, value)

    def clone_ptr(self):
        self._top_entity = Aaa()
        return self._top_entity


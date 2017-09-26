""" Cisco_IOS_XR_tty_management_cmd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tty\-management\-cmd package operational data.

This module contains definitions
for the following management objects\:
  show\-users\: Show users statistics

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ShowUsers(Entity):
    """
    Show users statistics
    
    .. attribute:: sessions
    
    	Show users statistics
    	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_cmd_oper.ShowUsers.Sessions>`
    
    

    """

    _prefix = 'tty-management-cmd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(ShowUsers, self).__init__()
        self._top_entity = None

        self.yang_name = "show-users"
        self.yang_parent_name = "Cisco-IOS-XR-tty-management-cmd-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"sessions" : ("sessions", ShowUsers.Sessions)}
        self._child_list_classes = {}

        self.sessions = ShowUsers.Sessions()
        self.sessions.parent = self
        self._children_name_map["sessions"] = "sessions"
        self._children_yang_names.add("sessions")
        self._segment_path = lambda: "Cisco-IOS-XR-tty-management-cmd-oper:show-users"


    class Sessions(Entity):
        """
        Show users statistics
        
        .. attribute:: session
        
        	Show users statistics
        	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_cmd_oper.ShowUsers.Sessions.Session>`
        
        

        """

        _prefix = 'tty-management-cmd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ShowUsers.Sessions, self).__init__()

            self.yang_name = "sessions"
            self.yang_parent_name = "show-users"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"session" : ("session", ShowUsers.Sessions.Session)}

            self.session = YList(self)
            self._segment_path = lambda: "sessions"
            self._absolute_path = lambda: "Cisco-IOS-XR-tty-management-cmd-oper:show-users/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ShowUsers.Sessions, [], name, value)


        class Session(Entity):
            """
            Show users statistics
            
            .. attribute:: session_id  <key>
            
            	Session Id
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: conns
            
            	No. of Connections
            	**type**\:  str
            
            .. attribute:: idle_string
            
            	Idle Time
            	**type**\:  str
            
            .. attribute:: line
            
            	Line Number
            	**type**\:  str
            
            .. attribute:: location
            
            	location
            	**type**\:  str
            
            .. attribute:: service
            
            	Service Name
            	**type**\:  str
            
            .. attribute:: user
            
            	User Name
            	**type**\:  str
            
            

            """

            _prefix = 'tty-management-cmd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ShowUsers.Sessions.Session, self).__init__()

                self.yang_name = "session"
                self.yang_parent_name = "sessions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.session_id = YLeaf(YType.int32, "session-id")

                self.conns = YLeaf(YType.str, "conns")

                self.idle_string = YLeaf(YType.str, "idle-string")

                self.line = YLeaf(YType.str, "line")

                self.location = YLeaf(YType.str, "location")

                self.service = YLeaf(YType.str, "service")

                self.user = YLeaf(YType.str, "user")
                self._segment_path = lambda: "session" + "[session-id='" + self.session_id.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tty-management-cmd-oper:show-users/sessions/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ShowUsers.Sessions.Session, ['session_id', 'conns', 'idle_string', 'line', 'location', 'service', 'user'], name, value)

    def clone_ptr(self):
        self._top_entity = ShowUsers()
        return self._top_entity


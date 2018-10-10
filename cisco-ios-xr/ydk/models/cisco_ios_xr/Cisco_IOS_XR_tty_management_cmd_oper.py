""" Cisco_IOS_XR_tty_management_cmd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tty\-management\-cmd package operational data.

This module contains definitions
for the following management objects\:
  show\-users\: Show users statistics

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class ShowUsers(Entity):
    """
    Show users statistics
    
    .. attribute:: sessions
    
    	Show users statistics
    	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_cmd_oper.ShowUsers.Sessions>`
    
    

    """

    _prefix = 'tty-management-cmd-oper'
    _revision = '2017-09-07'

    def __init__(self):
        super(ShowUsers, self).__init__()
        self._top_entity = None

        self.yang_name = "show-users"
        self.yang_parent_name = "Cisco-IOS-XR-tty-management-cmd-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("sessions", ("sessions", ShowUsers.Sessions))])
        self._leafs = OrderedDict()

        self.sessions = ShowUsers.Sessions()
        self.sessions.parent = self
        self._children_name_map["sessions"] = "sessions"
        self._segment_path = lambda: "Cisco-IOS-XR-tty-management-cmd-oper:show-users"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ShowUsers, [], name, value)


    class Sessions(Entity):
        """
        Show users statistics
        
        .. attribute:: session
        
        	Show users statistics
        	**type**\: list of  		 :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_cmd_oper.ShowUsers.Sessions.Session>`
        
        

        """

        _prefix = 'tty-management-cmd-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(ShowUsers.Sessions, self).__init__()

            self.yang_name = "sessions"
            self.yang_parent_name = "show-users"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("session", ("session", ShowUsers.Sessions.Session))])
            self._leafs = OrderedDict()

            self.session = YList(self)
            self._segment_path = lambda: "sessions"
            self._absolute_path = lambda: "Cisco-IOS-XR-tty-management-cmd-oper:show-users/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ShowUsers.Sessions, [], name, value)


        class Session(Entity):
            """
            Show users statistics
            
            .. attribute:: session_id  (key)
            
            	Session Id
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: line
            
            	Line Number
            	**type**\: str
            
            .. attribute:: user
            
            	User Name
            	**type**\: str
            
            .. attribute:: service
            
            	Service Name
            	**type**\: str
            
            .. attribute:: conns
            
            	No. of Connections
            	**type**\: str
            
            .. attribute:: idle_string
            
            	Idle Time
            	**type**\: str
            
            .. attribute:: location
            
            	location
            	**type**\: str
            
            

            """

            _prefix = 'tty-management-cmd-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(ShowUsers.Sessions.Session, self).__init__()

                self.yang_name = "session"
                self.yang_parent_name = "sessions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['session_id']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                    ('line', (YLeaf(YType.str, 'line'), ['str'])),
                    ('user', (YLeaf(YType.str, 'user'), ['str'])),
                    ('service', (YLeaf(YType.str, 'service'), ['str'])),
                    ('conns', (YLeaf(YType.str, 'conns'), ['str'])),
                    ('idle_string', (YLeaf(YType.str, 'idle-string'), ['str'])),
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                ])
                self.session_id = None
                self.line = None
                self.user = None
                self.service = None
                self.conns = None
                self.idle_string = None
                self.location = None
                self._segment_path = lambda: "session" + "[session-id='" + str(self.session_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tty-management-cmd-oper:show-users/sessions/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ShowUsers.Sessions.Session, ['session_id', u'line', u'user', u'service', u'conns', u'idle_string', u'location'], name, value)

    def clone_ptr(self):
        self._top_entity = ShowUsers()
        return self._top_entity


""" Cisco_IOS_XR_tty_management_cmd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tty\-management\-cmd package operational data.

This module contains definitions
for the following management objects\:
  show\-users\: Show users statistics

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class ShowUsers(object):
    """
    Show users statistics
    
    .. attribute:: sessions
    
    	Show users statistics
    	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_cmd_oper.ShowUsers.Sessions>`
    
    

    """

    _prefix = 'tty-management-cmd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.sessions = ShowUsers.Sessions()
        self.sessions.parent = self


    class Sessions(object):
        """
        Show users statistics
        
        .. attribute:: session
        
        	Show users statistics
        	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_cmd_oper.ShowUsers.Sessions.Session>`
        
        

        """

        _prefix = 'tty-management-cmd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.session = YList()
            self.session.parent = self
            self.session.name = 'session'


        class Session(object):
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
                self.parent = None
                self.session_id = None
                self.conns = None
                self.idle_string = None
                self.line = None
                self.location = None
                self.service = None
                self.user = None

            @property
            def _common_path(self):
                if self.session_id is None:
                    raise YPYModelError('Key property session_id is None')

                return '/Cisco-IOS-XR-tty-management-cmd-oper:show-users/Cisco-IOS-XR-tty-management-cmd-oper:sessions/Cisco-IOS-XR-tty-management-cmd-oper:session[Cisco-IOS-XR-tty-management-cmd-oper:session-id = ' + str(self.session_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.session_id is not None:
                    return True

                if self.conns is not None:
                    return True

                if self.idle_string is not None:
                    return True

                if self.line is not None:
                    return True

                if self.location is not None:
                    return True

                if self.service is not None:
                    return True

                if self.user is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_management_cmd_oper as meta
                return meta._meta_table['ShowUsers.Sessions.Session']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tty-management-cmd-oper:show-users/Cisco-IOS-XR-tty-management-cmd-oper:sessions'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.session is not None:
                for child_ref in self.session:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_management_cmd_oper as meta
            return meta._meta_table['ShowUsers.Sessions']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-tty-management-cmd-oper:show-users'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.sessions is not None and self.sessions._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tty_management_cmd_oper as meta
        return meta._meta_table['ShowUsers']['meta_info']



""" Cisco_IOS_XR_aaa_locald_admin_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-locald package admin\-plane configuration.

This module contains definitions
for the following management objects\:
  aaa\: Admin plane AAA configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Aaa(object):
    """
    Admin plane AAA configuration
    
    .. attribute:: usernames
    
    	Configure local username
    	**type**\:   :py:class:`Usernames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg.Aaa.Usernames>`
    
    

    """

    _prefix = 'aaa-locald-admin-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.usernames = Aaa.Usernames()
        self.usernames.parent = self


    class Usernames(object):
        """
        Configure local username
        
        .. attribute:: username
        
        	Admin Username
        	**type**\: list of    :py:class:`Username <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg.Aaa.Usernames.Username>`
        
        

        """

        _prefix = 'aaa-locald-admin-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.username = YList()
            self.username.parent = self
            self.username.name = 'username'


        class Username(object):
            """
            Admin Username
            
            .. attribute:: name  <key>
            
            	Username
            	**type**\:  str
            
            .. attribute:: secret
            
            	Specify the secret for the admin user
            	**type**\:  str
            
            	**pattern:** (!.+)\|([^!].+)
            
            .. attribute:: usergroup_under_usernames
            
            	Specify the usergroup to which this admin user belongs
            	**type**\:   :py:class:`UsergroupUnderUsernames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg.Aaa.Usernames.Username.UsergroupUnderUsernames>`
            
            

            """

            _prefix = 'aaa-locald-admin-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.name = None
                self.secret = None
                self.usergroup_under_usernames = Aaa.Usernames.Username.UsergroupUnderUsernames()
                self.usergroup_under_usernames.parent = self


            class UsergroupUnderUsernames(object):
                """
                Specify the usergroup to which this admin user
                belongs
                
                .. attribute:: usergroup_under_username
                
                	Name of the usergroup
                	**type**\: list of    :py:class:`UsergroupUnderUsername <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg.Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername>`
                
                

                """

                _prefix = 'aaa-locald-admin-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.usergroup_under_username = YList()
                    self.usergroup_under_username.parent = self
                    self.usergroup_under_username.name = 'usergroup_under_username'


                class UsergroupUnderUsername(object):
                    """
                    Name of the usergroup
                    
                    .. attribute:: name  <key>
                    
                    	Name of the usergroup
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    

                    """

                    _prefix = 'aaa-locald-admin-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.name is None:
                            raise YPYModelError('Key property name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-admin-cfg:usergroup-under-username[Cisco-IOS-XR-aaa-locald-admin-cfg:name = ' + str(self.name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_admin_cfg as meta
                        return meta._meta_table['Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-admin-cfg:usergroup-under-usernames'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.usergroup_under_username is not None:
                        for child_ref in self.usergroup_under_username:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_admin_cfg as meta
                    return meta._meta_table['Aaa.Usernames.Username.UsergroupUnderUsernames']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-aaa-locald-admin-cfg:aaa/Cisco-IOS-XR-aaa-locald-admin-cfg:usernames/Cisco-IOS-XR-aaa-locald-admin-cfg:username[Cisco-IOS-XR-aaa-locald-admin-cfg:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.secret is not None:
                    return True

                if self.usergroup_under_usernames is not None and self.usergroup_under_usernames._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_admin_cfg as meta
                return meta._meta_table['Aaa.Usernames.Username']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-locald-admin-cfg:aaa/Cisco-IOS-XR-aaa-locald-admin-cfg:usernames'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.username is not None:
                for child_ref in self.username:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_admin_cfg as meta
            return meta._meta_table['Aaa.Usernames']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-aaa-locald-admin-cfg:aaa'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.usernames is not None and self.usernames._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_admin_cfg as meta
        return meta._meta_table['Aaa']['meta_info']



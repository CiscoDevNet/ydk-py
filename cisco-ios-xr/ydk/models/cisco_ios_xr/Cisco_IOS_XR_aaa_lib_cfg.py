""" Cisco_IOS_XR_aaa_lib_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-lib package configuration.

This module contains definitions
for the following management objects\:
  aaa\: Authentication, Authorization and Accounting

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
    Authentication, Authorization and Accounting
    
    .. attribute:: aaa_dot1x
    
    	AAA Dot1x
    	**type**\:   :py:class:`AaaDot1X <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaDot1X>`
    
    .. attribute:: aaa_mobile
    
    	AAA Mobile
    	**type**\:   :py:class:`AaaMobile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaMobile>`
    
    .. attribute:: aaa_subscriber
    
    	AAA subscriber
    	**type**\:   :py:class:`AaaSubscriber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber>`
    
    .. attribute:: accounting_update
    
    	Configuration related to 'update' accounting
    	**type**\:   :py:class:`AccountingUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AccountingUpdate>`
    
    	**presence node**\: True
    
    .. attribute:: accountings
    
    	AAA accounting
    	**type**\:   :py:class:`Accountings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Accountings>`
    
    .. attribute:: authentications
    
    	AAA authentication
    	**type**\:   :py:class:`Authentications <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Authentications>`
    
    .. attribute:: authorizations
    
    	AAA authorization
    	**type**\:   :py:class:`Authorizations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Authorizations>`
    
    .. attribute:: banner
    
    	AAA banner
    	**type**\:   :py:class:`Banner <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Banner>`
    
    .. attribute:: default_taskgroup
    
    	This class is used for setting the default taskgroup to be used for remote server authentication
    	**type**\:  str
    
    .. attribute:: diameter
    
    	Diameter base protocol
    	**type**\:   :py:class:`Diameter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter>`
    
    .. attribute:: radius
    
    	Remote Access Dial\-In User Service
    	**type**\:   :py:class:`Radius <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius>`
    
    .. attribute:: radius_attribute
    
    	AAA RADIUS attribute configurations
    	**type**\:   :py:class:`RadiusAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute>`
    
    .. attribute:: server_groups
    
    	AAA group definitions
    	**type**\:   :py:class:`ServerGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups>`
    
    .. attribute:: tacacs
    
    	Modify TACACS+ query parameters
    	**type**\:   :py:class:`Tacacs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs>`
    
    .. attribute:: taskgroups
    
    	Specify a taskgroup to inherit from
    	**type**\:   :py:class:`Taskgroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups>`
    
    .. attribute:: usergroups
    
    	Specify a Usergroup to inherit from
    	**type**\:   :py:class:`Usergroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups>`
    
    .. attribute:: usernames
    
    	Configure local usernames
    	**type**\:   :py:class:`Usernames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usernames>`
    
    

    """

    _prefix = 'aaa-lib-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.aaa_dot1x = Aaa.AaaDot1X()
        self.aaa_dot1x.parent = self
        self.aaa_mobile = Aaa.AaaMobile()
        self.aaa_mobile.parent = self
        self.aaa_subscriber = Aaa.AaaSubscriber()
        self.aaa_subscriber.parent = self
        self.accounting_update = None
        self.accountings = Aaa.Accountings()
        self.accountings.parent = self
        self.authentications = Aaa.Authentications()
        self.authentications.parent = self
        self.authorizations = Aaa.Authorizations()
        self.authorizations.parent = self
        self.banner = Aaa.Banner()
        self.banner.parent = self
        self.default_taskgroup = None
        self.diameter = Aaa.Diameter()
        self.diameter.parent = self
        self.radius = Aaa.Radius()
        self.radius.parent = self
        self.radius_attribute = Aaa.RadiusAttribute()
        self.radius_attribute.parent = self
        self.server_groups = Aaa.ServerGroups()
        self.server_groups.parent = self
        self.tacacs = Aaa.Tacacs()
        self.tacacs.parent = self
        self.taskgroups = Aaa.Taskgroups()
        self.taskgroups.parent = self
        self.usergroups = Aaa.Usergroups()
        self.usergroups.parent = self
        self.usernames = Aaa.Usernames()
        self.usernames.parent = self


    class Accountings(object):
        """
        AAA accounting
        
        .. attribute:: accounting
        
        	Configurations related to accounting
        	**type**\: list of    :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Accountings.Accounting>`
        
        

        """

        _prefix = 'aaa-lib-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.accounting = YList()
            self.accounting.parent = self
            self.accounting.name = 'accounting'


        class Accounting(object):
            """
            Configurations related to accounting
            
            .. attribute:: type  <key>
            
            	exec\:Account exec sessions, commands\: Account CLI commands
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: listname  <key>
            
            	Named accounting list
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: broadcast
            
            	Broadcast
            	**type**\:   :py:class:`AaaAccountingBroadcastEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaAccountingBroadcastEnum>`
            
            .. attribute:: method
            
            	Method Types
            	**type**\:  list of   :py:class:`AaaMethodEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethodEnum>`
            
            .. attribute:: rp_failover
            
            	rpfailover
            	**type**\:   :py:class:`AaaAccountingRpFailoverEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaAccountingRpFailoverEnum>`
            
            .. attribute:: server_group_name
            
            	Server group names
            	**type**\:  list of str
            
            .. attribute:: type_xr
            
            	Stop only/Start Stop
            	**type**\:   :py:class:`AaaAccountingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaAccountingEnum>`
            
            

            """

            _prefix = 'aaa-lib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.type = None
                self.listname = None
                self.broadcast = None
                self.method = YLeafList()
                self.method.parent = self
                self.method.name = 'method'
                self.rp_failover = None
                self.server_group_name = YLeafList()
                self.server_group_name.parent = self
                self.server_group_name.name = 'server_group_name'
                self.type_xr = None

            @property
            def _common_path(self):
                if self.type is None:
                    raise YPYModelError('Key property type is None')
                if self.listname is None:
                    raise YPYModelError('Key property listname is None')

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-lib-cfg:accountings/Cisco-IOS-XR-aaa-lib-cfg:accounting[Cisco-IOS-XR-aaa-lib-cfg:type = ' + str(self.type) + '][Cisco-IOS-XR-aaa-lib-cfg:listname = ' + str(self.listname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.type is not None:
                    return True

                if self.listname is not None:
                    return True

                if self.broadcast is not None:
                    return True

                if self.method is not None:
                    for child in self.method:
                        if child is not None:
                            return True

                if self.rp_failover is not None:
                    return True

                if self.server_group_name is not None:
                    for child in self.server_group_name:
                        if child is not None:
                            return True

                if self.type_xr is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Accountings.Accounting']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-lib-cfg:accountings'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.accounting is not None:
                for child_ref in self.accounting:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
            return meta._meta_table['Aaa.Accountings']['meta_info']


    class Authorizations(object):
        """
        AAA authorization
        
        .. attribute:: authorization
        
        	Configurations related to authorization
        	**type**\: list of    :py:class:`Authorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Authorizations.Authorization>`
        
        

        """

        _prefix = 'aaa-lib-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.authorization = YList()
            self.authorization.parent = self
            self.authorization.name = 'authorization'


        class Authorization(object):
            """
            Configurations related to authorization
            
            .. attribute:: type  <key>
            
            	network\: Authorize IKE requests, commands\: Authorize CLI commands
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: listname  <key>
            
            	List name for AAA authorization
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: method
            
            	Methods
            	**type**\:  list of   :py:class:`AaaMethodEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethodEnum>`
            
            .. attribute:: server_group_name
            
            	Server group names
            	**type**\:  list of str
            
            

            """

            _prefix = 'aaa-lib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.type = None
                self.listname = None
                self.method = YLeafList()
                self.method.parent = self
                self.method.name = 'method'
                self.server_group_name = YLeafList()
                self.server_group_name.parent = self
                self.server_group_name.name = 'server_group_name'

            @property
            def _common_path(self):
                if self.type is None:
                    raise YPYModelError('Key property type is None')
                if self.listname is None:
                    raise YPYModelError('Key property listname is None')

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-lib-cfg:authorizations/Cisco-IOS-XR-aaa-lib-cfg:authorization[Cisco-IOS-XR-aaa-lib-cfg:type = ' + str(self.type) + '][Cisco-IOS-XR-aaa-lib-cfg:listname = ' + str(self.listname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.type is not None:
                    return True

                if self.listname is not None:
                    return True

                if self.method is not None:
                    for child in self.method:
                        if child is not None:
                            return True

                if self.server_group_name is not None:
                    for child in self.server_group_name:
                        if child is not None:
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Authorizations.Authorization']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-lib-cfg:authorizations'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.authorization is not None:
                for child_ref in self.authorization:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
            return meta._meta_table['Aaa.Authorizations']['meta_info']


    class AccountingUpdate(object):
        """
        Configuration related to 'update' accounting
        
        .. attribute:: periodic_interval
        
        	Periodic update interval in minutes
        	**type**\:  int
        
        	**range:** 0..35791394
        
        	**units**\: minute
        
        .. attribute:: type
        
        	newinfo/periodic
        	**type**\:   :py:class:`AaaAccountingUpdateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaAccountingUpdateEnum>`
        
        	**mandatory**\: True
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'aaa-lib-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.periodic_interval = None
            self.type = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-lib-cfg:accounting-update'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.periodic_interval is not None:
                return True

            if self.type is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
            return meta._meta_table['Aaa.AccountingUpdate']['meta_info']


    class Banner(object):
        """
        AAA banner
        
        .. attribute:: login
        
        	AAA login banner
        	**type**\:  str
        
        

        """

        _prefix = 'aaa-lib-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.login = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-lib-cfg:banner'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.login is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
            return meta._meta_table['Aaa.Banner']['meta_info']


    class Authentications(object):
        """
        AAA authentication
        
        .. attribute:: authentication
        
        	Configurations related to authentication
        	**type**\: list of    :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Authentications.Authentication>`
        
        

        """

        _prefix = 'aaa-lib-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.authentication = YList()
            self.authentication.parent = self
            self.authentication.name = 'authentication'


        class Authentication(object):
            """
            Configurations related to authentication
            
            .. attribute:: type  <key>
            
            	login\: Authenticate login sessions, ppp\: Authenticate ppp sessions
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: listname  <key>
            
            	List name for AAA authentication
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: method
            
            	Methods
            	**type**\:  list of   :py:class:`AaaMethodEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethodEnum>`
            
            .. attribute:: server_group_name
            
            	Server group names
            	**type**\:  list of str
            
            

            """

            _prefix = 'aaa-lib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.type = None
                self.listname = None
                self.method = YLeafList()
                self.method.parent = self
                self.method.name = 'method'
                self.server_group_name = YLeafList()
                self.server_group_name.parent = self
                self.server_group_name.name = 'server_group_name'

            @property
            def _common_path(self):
                if self.type is None:
                    raise YPYModelError('Key property type is None')
                if self.listname is None:
                    raise YPYModelError('Key property listname is None')

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-lib-cfg:authentications/Cisco-IOS-XR-aaa-lib-cfg:authentication[Cisco-IOS-XR-aaa-lib-cfg:type = ' + str(self.type) + '][Cisco-IOS-XR-aaa-lib-cfg:listname = ' + str(self.listname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.type is not None:
                    return True

                if self.listname is not None:
                    return True

                if self.method is not None:
                    for child in self.method:
                        if child is not None:
                            return True

                if self.server_group_name is not None:
                    for child in self.server_group_name:
                        if child is not None:
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Authentications.Authentication']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-lib-cfg:authentications'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.authentication is not None:
                for child_ref in self.authentication:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
            return meta._meta_table['Aaa.Authentications']['meta_info']


    class AaaSubscriber(object):
        """
        AAA subscriber
        
        .. attribute:: accountings
        
        	AAA accounting
        	**type**\:   :py:class:`Accountings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.Accountings>`
        
        .. attribute:: authentications
        
        	AAA authentication
        	**type**\:   :py:class:`Authentications <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.Authentications>`
        
        .. attribute:: authorizations
        
        	AAA authorization
        	**type**\:   :py:class:`Authorizations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.Authorizations>`
        
        .. attribute:: policy_if_authors
        
        	AAA authorization policy
        	**type**\:   :py:class:`PolicyIfAuthors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.PolicyIfAuthors>`
        
        .. attribute:: prepaid_authors
        
        	AAA authorization prepaid
        	**type**\:   :py:class:`PrepaidAuthors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.PrepaidAuthors>`
        
        .. attribute:: service_accounting
        
        	Set accounting parameters for Service
        	**type**\:   :py:class:`ServiceAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.ServiceAccounting>`
        
        

        """

        _prefix = 'aaa-aaacore-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.accountings = Aaa.AaaSubscriber.Accountings()
            self.accountings.parent = self
            self.authentications = Aaa.AaaSubscriber.Authentications()
            self.authentications.parent = self
            self.authorizations = Aaa.AaaSubscriber.Authorizations()
            self.authorizations.parent = self
            self.policy_if_authors = Aaa.AaaSubscriber.PolicyIfAuthors()
            self.policy_if_authors.parent = self
            self.prepaid_authors = Aaa.AaaSubscriber.PrepaidAuthors()
            self.prepaid_authors.parent = self
            self.service_accounting = Aaa.AaaSubscriber.ServiceAccounting()
            self.service_accounting.parent = self


        class PolicyIfAuthors(object):
            """
            AAA authorization policy
            
            .. attribute:: policy_if_author
            
            	Configurations related to authorization
            	**type**\: list of    :py:class:`PolicyIfAuthor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.PolicyIfAuthors.PolicyIfAuthor>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.policy_if_author = YList()
                self.policy_if_author.parent = self
                self.policy_if_author.name = 'policy_if_author'


            class PolicyIfAuthor(object):
                """
                Configurations related to authorization
                
                .. attribute:: type  <key>
                
                	Set authorization lists
                	**type**\:  str
                
                	**pattern:** (subscriber)\|(service)\|(policy\-if)\|(prepaid)\|(dot1x)
                
                .. attribute:: listname  <key>
                
                	Named authorization list
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: method
                
                	Method Types
                	**type**\:  list of   :py:class:`AaaMethodEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethodEnum>`
                
                .. attribute:: server_group_name
                
                	Server group names
                	**type**\:  list of str
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.type = None
                    self.listname = None
                    self.method = YLeafList()
                    self.method.parent = self
                    self.method.name = 'method'
                    self.server_group_name = YLeafList()
                    self.server_group_name.parent = self
                    self.server_group_name.name = 'server_group_name'

                @property
                def _common_path(self):
                    if self.type is None:
                        raise YPYModelError('Key property type is None')
                    if self.listname is None:
                        raise YPYModelError('Key property listname is None')

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/Cisco-IOS-XR-aaa-aaacore-cfg:policy-if-authors/Cisco-IOS-XR-aaa-aaacore-cfg:policy-if-author[Cisco-IOS-XR-aaa-aaacore-cfg:type = ' + str(self.type) + '][Cisco-IOS-XR-aaa-aaacore-cfg:listname = ' + str(self.listname) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.type is not None:
                        return True

                    if self.listname is not None:
                        return True

                    if self.method is not None:
                        for child in self.method:
                            if child is not None:
                                return True

                    if self.server_group_name is not None:
                        for child in self.server_group_name:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.AaaSubscriber.PolicyIfAuthors.PolicyIfAuthor']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/Cisco-IOS-XR-aaa-aaacore-cfg:policy-if-authors'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.policy_if_author is not None:
                    for child_ref in self.policy_if_author:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.AaaSubscriber.PolicyIfAuthors']['meta_info']


        class Accountings(object):
            """
            AAA accounting
            
            .. attribute:: accounting
            
            	Configurations related to accounting
            	**type**\: list of    :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.Accountings.Accounting>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.accounting = YList()
                self.accounting.parent = self
                self.accounting.name = 'accounting'


            class Accounting(object):
                """
                Configurations related to accounting
                
                .. attribute:: type  <key>
                
                	Set accounting lists
                	**type**\:  str
                
                	**pattern:** (subscriber)\|(service)\|(policy\-if)\|(prepaid)\|(dot1x)
                
                .. attribute:: listname  <key>
                
                	Named accounting list
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: broadcast
                
                	Broadcast
                	**type**\:   :py:class:`AaaAccountingBroadcastEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaAccountingBroadcastEnum>`
                
                	**mandatory**\: True
                
                .. attribute:: method
                
                	Method Types
                	**type**\:  list of   :py:class:`AaaMethodEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethodEnum>`
                
                .. attribute:: server_group_name
                
                	Server group names
                	**type**\:  list of str
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.type = None
                    self.listname = None
                    self.broadcast = None
                    self.method = YLeafList()
                    self.method.parent = self
                    self.method.name = 'method'
                    self.server_group_name = YLeafList()
                    self.server_group_name.parent = self
                    self.server_group_name.name = 'server_group_name'

                @property
                def _common_path(self):
                    if self.type is None:
                        raise YPYModelError('Key property type is None')
                    if self.listname is None:
                        raise YPYModelError('Key property listname is None')

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/Cisco-IOS-XR-aaa-aaacore-cfg:accountings/Cisco-IOS-XR-aaa-aaacore-cfg:accounting[Cisco-IOS-XR-aaa-aaacore-cfg:type = ' + str(self.type) + '][Cisco-IOS-XR-aaa-aaacore-cfg:listname = ' + str(self.listname) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.type is not None:
                        return True

                    if self.listname is not None:
                        return True

                    if self.broadcast is not None:
                        return True

                    if self.method is not None:
                        for child in self.method:
                            if child is not None:
                                return True

                    if self.server_group_name is not None:
                        for child in self.server_group_name:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.AaaSubscriber.Accountings.Accounting']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/Cisco-IOS-XR-aaa-aaacore-cfg:accountings'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.accounting is not None:
                    for child_ref in self.accounting:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.AaaSubscriber.Accountings']['meta_info']


        class ServiceAccounting(object):
            """
            Set accounting parameters for Service
            
            .. attribute:: type
            
            	Send extended/brief service accounting records
            	**type**\:   :py:class:`AaaServiceAccountingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_aaacore_cfg.AaaServiceAccountingEnum>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.type = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/Cisco-IOS-XR-aaa-aaacore-cfg:service-accounting'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.type is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.AaaSubscriber.ServiceAccounting']['meta_info']


        class PrepaidAuthors(object):
            """
            AAA authorization prepaid
            
            .. attribute:: prepaid_author
            
            	Configurations related to authorization
            	**type**\: list of    :py:class:`PrepaidAuthor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.PrepaidAuthors.PrepaidAuthor>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.prepaid_author = YList()
                self.prepaid_author.parent = self
                self.prepaid_author.name = 'prepaid_author'


            class PrepaidAuthor(object):
                """
                Configurations related to authorization
                
                .. attribute:: type  <key>
                
                	Set authorization lists
                	**type**\:  str
                
                	**pattern:** (subscriber)\|(service)\|(policy\-if)\|(prepaid)\|(dot1x)
                
                .. attribute:: listname  <key>
                
                	Named authorization list
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: method
                
                	Method Types
                	**type**\:  list of   :py:class:`AaaMethodEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethodEnum>`
                
                .. attribute:: server_group_name
                
                	Server group names
                	**type**\:  list of str
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.type = None
                    self.listname = None
                    self.method = YLeafList()
                    self.method.parent = self
                    self.method.name = 'method'
                    self.server_group_name = YLeafList()
                    self.server_group_name.parent = self
                    self.server_group_name.name = 'server_group_name'

                @property
                def _common_path(self):
                    if self.type is None:
                        raise YPYModelError('Key property type is None')
                    if self.listname is None:
                        raise YPYModelError('Key property listname is None')

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/Cisco-IOS-XR-aaa-aaacore-cfg:prepaid-authors/Cisco-IOS-XR-aaa-aaacore-cfg:prepaid-author[Cisco-IOS-XR-aaa-aaacore-cfg:type = ' + str(self.type) + '][Cisco-IOS-XR-aaa-aaacore-cfg:listname = ' + str(self.listname) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.type is not None:
                        return True

                    if self.listname is not None:
                        return True

                    if self.method is not None:
                        for child in self.method:
                            if child is not None:
                                return True

                    if self.server_group_name is not None:
                        for child in self.server_group_name:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.AaaSubscriber.PrepaidAuthors.PrepaidAuthor']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/Cisco-IOS-XR-aaa-aaacore-cfg:prepaid-authors'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.prepaid_author is not None:
                    for child_ref in self.prepaid_author:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.AaaSubscriber.PrepaidAuthors']['meta_info']


        class Authorizations(object):
            """
            AAA authorization
            
            .. attribute:: authorization
            
            	Configurations related to authorization
            	**type**\: list of    :py:class:`Authorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.Authorizations.Authorization>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.authorization = YList()
                self.authorization.parent = self
                self.authorization.name = 'authorization'


            class Authorization(object):
                """
                Configurations related to authorization
                
                .. attribute:: type  <key>
                
                	Set authorization lists
                	**type**\:  str
                
                	**pattern:** (subscriber)\|(service)\|(policy\-if)\|(prepaid)\|(dot1x)
                
                .. attribute:: listname  <key>
                
                	Named authorization list
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: method
                
                	Method Types
                	**type**\:  list of   :py:class:`AaaMethodEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethodEnum>`
                
                .. attribute:: server_group_name
                
                	Server group names
                	**type**\:  list of str
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.type = None
                    self.listname = None
                    self.method = YLeafList()
                    self.method.parent = self
                    self.method.name = 'method'
                    self.server_group_name = YLeafList()
                    self.server_group_name.parent = self
                    self.server_group_name.name = 'server_group_name'

                @property
                def _common_path(self):
                    if self.type is None:
                        raise YPYModelError('Key property type is None')
                    if self.listname is None:
                        raise YPYModelError('Key property listname is None')

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/Cisco-IOS-XR-aaa-aaacore-cfg:authorizations/Cisco-IOS-XR-aaa-aaacore-cfg:authorization[Cisco-IOS-XR-aaa-aaacore-cfg:type = ' + str(self.type) + '][Cisco-IOS-XR-aaa-aaacore-cfg:listname = ' + str(self.listname) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.type is not None:
                        return True

                    if self.listname is not None:
                        return True

                    if self.method is not None:
                        for child in self.method:
                            if child is not None:
                                return True

                    if self.server_group_name is not None:
                        for child in self.server_group_name:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.AaaSubscriber.Authorizations.Authorization']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/Cisco-IOS-XR-aaa-aaacore-cfg:authorizations'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.authorization is not None:
                    for child_ref in self.authorization:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.AaaSubscriber.Authorizations']['meta_info']


        class Authentications(object):
            """
            AAA authentication
            
            .. attribute:: authentication
            
            	Configurations related to authentication
            	**type**\: list of    :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.Authentications.Authentication>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.authentication = YList()
                self.authentication.parent = self
                self.authentication.name = 'authentication'


            class Authentication(object):
                """
                Configurations related to authentication
                
                .. attribute:: type  <key>
                
                	Set authentication lists
                	**type**\:  str
                
                	**pattern:** (subscriber)\|(service)\|(policy\-if)\|(prepaid)\|(dot1x)
                
                .. attribute:: listname  <key>
                
                	Named authentication list
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: method
                
                	Method Types
                	**type**\:  list of   :py:class:`AaaMethodEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethodEnum>`
                
                .. attribute:: server_group_name
                
                	Server group names
                	**type**\:  list of str
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.type = None
                    self.listname = None
                    self.method = YLeafList()
                    self.method.parent = self
                    self.method.name = 'method'
                    self.server_group_name = YLeafList()
                    self.server_group_name.parent = self
                    self.server_group_name.name = 'server_group_name'

                @property
                def _common_path(self):
                    if self.type is None:
                        raise YPYModelError('Key property type is None')
                    if self.listname is None:
                        raise YPYModelError('Key property listname is None')

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/Cisco-IOS-XR-aaa-aaacore-cfg:authentications/Cisco-IOS-XR-aaa-aaacore-cfg:authentication[Cisco-IOS-XR-aaa-aaacore-cfg:type = ' + str(self.type) + '][Cisco-IOS-XR-aaa-aaacore-cfg:listname = ' + str(self.listname) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.type is not None:
                        return True

                    if self.listname is not None:
                        return True

                    if self.method is not None:
                        for child in self.method:
                            if child is not None:
                                return True

                    if self.server_group_name is not None:
                        for child in self.server_group_name:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.AaaSubscriber.Authentications.Authentication']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/Cisco-IOS-XR-aaa-aaacore-cfg:authentications'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.authentication is not None:
                    for child_ref in self.authentication:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.AaaSubscriber.Authentications']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.accountings is not None and self.accountings._has_data():
                return True

            if self.authentications is not None and self.authentications._has_data():
                return True

            if self.authorizations is not None and self.authorizations._has_data():
                return True

            if self.policy_if_authors is not None and self.policy_if_authors._has_data():
                return True

            if self.prepaid_authors is not None and self.prepaid_authors._has_data():
                return True

            if self.service_accounting is not None and self.service_accounting._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
            return meta._meta_table['Aaa.AaaSubscriber']['meta_info']


    class AaaMobile(object):
        """
        AAA Mobile
        
        .. attribute:: mobiles
        
        	AAA Mobile Accounting
        	**type**\:   :py:class:`Mobiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaMobile.Mobiles>`
        
        

        """

        _prefix = 'aaa-aaacore-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.mobiles = Aaa.AaaMobile.Mobiles()
            self.mobiles.parent = self


        class Mobiles(object):
            """
            AAA Mobile Accounting
            
            .. attribute:: mobile
            
            	Configurations related to accounting
            	**type**\: list of    :py:class:`Mobile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaMobile.Mobiles.Mobile>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.mobile = YList()
                self.mobile.parent = self
                self.mobile.name = 'mobile'


            class Mobile(object):
                """
                Configurations related to accounting
                
                .. attribute:: listname  <key>
                
                	Named accounting list
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: broadcast
                
                	Broadcast
                	**type**\:   :py:class:`AaaAccountingBroadcastEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaAccountingBroadcastEnum>`
                
                	**mandatory**\: True
                
                .. attribute:: method
                
                	Method Types
                	**type**\:  list of   :py:class:`AaaMethodEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethodEnum>`
                
                .. attribute:: server_group_name
                
                	Server group names
                	**type**\:  list of str
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.listname = None
                    self.broadcast = None
                    self.method = YLeafList()
                    self.method.parent = self
                    self.method.name = 'method'
                    self.server_group_name = YLeafList()
                    self.server_group_name.parent = self
                    self.server_group_name.name = 'server_group_name'

                @property
                def _common_path(self):
                    if self.listname is None:
                        raise YPYModelError('Key property listname is None')

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-mobile/Cisco-IOS-XR-aaa-aaacore-cfg:mobiles/Cisco-IOS-XR-aaa-aaacore-cfg:mobile[Cisco-IOS-XR-aaa-aaacore-cfg:listname = ' + str(self.listname) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.listname is not None:
                        return True

                    if self.broadcast is not None:
                        return True

                    if self.method is not None:
                        for child in self.method:
                            if child is not None:
                                return True

                    if self.server_group_name is not None:
                        for child in self.server_group_name:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.AaaMobile.Mobiles.Mobile']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-mobile/Cisco-IOS-XR-aaa-aaacore-cfg:mobiles'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.mobile is not None:
                    for child_ref in self.mobile:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.AaaMobile.Mobiles']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-mobile'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.mobiles is not None and self.mobiles._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
            return meta._meta_table['Aaa.AaaMobile']['meta_info']


    class AaaDot1X(object):
        """
        AAA Dot1x
        
        .. attribute:: authentications
        
        	AAA authentication
        	**type**\:   :py:class:`Authentications <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaDot1X.Authentications>`
        
        

        """

        _prefix = 'aaa-aaacore-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.authentications = Aaa.AaaDot1X.Authentications()
            self.authentications.parent = self


        class Authentications(object):
            """
            AAA authentication
            
            .. attribute:: authentication
            
            	Configurations related to authentication
            	**type**\: list of    :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaDot1X.Authentications.Authentication>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.authentication = YList()
                self.authentication.parent = self
                self.authentication.name = 'authentication'


            class Authentication(object):
                """
                Configurations related to authentication
                
                .. attribute:: type  <key>
                
                	Set authentication lists
                	**type**\:  str
                
                	**pattern:** (subscriber)\|(service)\|(policy\-if)\|(prepaid)\|(dot1x)
                
                .. attribute:: listname  <key>
                
                	Named authentication list
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: method
                
                	Method Types
                	**type**\:  list of   :py:class:`AaaMethodEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethodEnum>`
                
                .. attribute:: server_group_name
                
                	Server group names
                	**type**\:  list of str
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.type = None
                    self.listname = None
                    self.method = YLeafList()
                    self.method.parent = self
                    self.method.name = 'method'
                    self.server_group_name = YLeafList()
                    self.server_group_name.parent = self
                    self.server_group_name.name = 'server_group_name'

                @property
                def _common_path(self):
                    if self.type is None:
                        raise YPYModelError('Key property type is None')
                    if self.listname is None:
                        raise YPYModelError('Key property listname is None')

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-dot1x/Cisco-IOS-XR-aaa-aaacore-cfg:authentications/Cisco-IOS-XR-aaa-aaacore-cfg:authentication[Cisco-IOS-XR-aaa-aaacore-cfg:type = ' + str(self.type) + '][Cisco-IOS-XR-aaa-aaacore-cfg:listname = ' + str(self.listname) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.type is not None:
                        return True

                    if self.listname is not None:
                        return True

                    if self.method is not None:
                        for child in self.method:
                            if child is not None:
                                return True

                    if self.server_group_name is not None:
                        for child in self.server_group_name:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.AaaDot1X.Authentications.Authentication']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-dot1x/Cisco-IOS-XR-aaa-aaacore-cfg:authentications'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.authentication is not None:
                    for child_ref in self.authentication:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.AaaDot1X.Authentications']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-dot1x'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.authentications is not None and self.authentications._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
            return meta._meta_table['Aaa.AaaDot1X']['meta_info']


    class RadiusAttribute(object):
        """
        AAA RADIUS attribute configurations
        
        .. attribute:: called_station
        
        	AAA called station id attribute
        	**type**\:   :py:class:`CalledStation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.CalledStation>`
        
        .. attribute:: calling_station
        
        	AAA calling station id attribute
        	**type**\:   :py:class:`CallingStation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.CallingStation>`
        
        .. attribute:: format_others
        
        	AAA nas\-port\-id attribute format
        	**type**\:   :py:class:`FormatOthers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.FormatOthers>`
        
        .. attribute:: nas_port
        
        	AAA nas\-port\-id attribute
        	**type**\:   :py:class:`NasPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.NasPort>`
        
        .. attribute:: nas_port_id
        
        	AAA nas\-port\-id attribute
        	**type**\:   :py:class:`NasPortId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.NasPortId>`
        
        

        """

        _prefix = 'aaa-aaacore-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.called_station = Aaa.RadiusAttribute.CalledStation()
            self.called_station.parent = self
            self.calling_station = Aaa.RadiusAttribute.CallingStation()
            self.calling_station.parent = self
            self.format_others = Aaa.RadiusAttribute.FormatOthers()
            self.format_others.parent = self
            self.nas_port = Aaa.RadiusAttribute.NasPort()
            self.nas_port.parent = self
            self.nas_port_id = Aaa.RadiusAttribute.NasPortId()
            self.nas_port_id.parent = self


        class NasPortId(object):
            """
            AAA nas\-port\-id attribute
            
            .. attribute:: formats
            
            	AAA nas\-port\-id attribute format
            	**type**\:   :py:class:`Formats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.NasPortId.Formats>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.formats = Aaa.RadiusAttribute.NasPortId.Formats()
                self.formats.parent = self


            class Formats(object):
                """
                AAA nas\-port\-id attribute format
                
                .. attribute:: format
                
                	nas\-port\-id attribute format
                	**type**\: list of    :py:class:`Format <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.NasPortId.Formats.Format>`
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.format = YList()
                    self.format.parent = self
                    self.format.name = 'format'


                class Format(object):
                    """
                    nas\-port\-id attribute format
                    
                    .. attribute:: type  <key>
                    
                    	Nas\-Port\-Type value to apply format name on
                    	**type**\:  int
                    
                    	**range:** 0..45
                    
                    .. attribute:: format_name
                    
                    	AAA nas\-port attribute format
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'aaa-aaacore-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.type = None
                        self.format_name = None

                    @property
                    def _common_path(self):
                        if self.type is None:
                            raise YPYModelError('Key property type is None')

                        return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/Cisco-IOS-XR-aaa-aaacore-cfg:nas-port-id/Cisco-IOS-XR-aaa-aaacore-cfg:formats/Cisco-IOS-XR-aaa-aaacore-cfg:format[Cisco-IOS-XR-aaa-aaacore-cfg:type = ' + str(self.type) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.type is not None:
                            return True

                        if self.format_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.RadiusAttribute.NasPortId.Formats.Format']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/Cisco-IOS-XR-aaa-aaacore-cfg:nas-port-id/Cisco-IOS-XR-aaa-aaacore-cfg:formats'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.format is not None:
                        for child_ref in self.format:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.RadiusAttribute.NasPortId.Formats']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/Cisco-IOS-XR-aaa-aaacore-cfg:nas-port-id'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.formats is not None and self.formats._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.RadiusAttribute.NasPortId']['meta_info']


        class CallingStation(object):
            """
            AAA calling station id attribute
            
            .. attribute:: formats
            
            	AAA nas\-port\-id attribute format
            	**type**\:   :py:class:`Formats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.CallingStation.Formats>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.formats = Aaa.RadiusAttribute.CallingStation.Formats()
                self.formats.parent = self


            class Formats(object):
                """
                AAA nas\-port\-id attribute format
                
                .. attribute:: format
                
                	nas\-port\-id attribute format
                	**type**\: list of    :py:class:`Format <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.CallingStation.Formats.Format>`
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.format = YList()
                    self.format.parent = self
                    self.format.name = 'format'


                class Format(object):
                    """
                    nas\-port\-id attribute format
                    
                    .. attribute:: type  <key>
                    
                    	Nas\-Port\-Type value to apply format name on
                    	**type**\:  int
                    
                    	**range:** 0..45
                    
                    .. attribute:: format_name
                    
                    	AAA nas\-port attribute format
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'aaa-aaacore-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.type = None
                        self.format_name = None

                    @property
                    def _common_path(self):
                        if self.type is None:
                            raise YPYModelError('Key property type is None')

                        return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/Cisco-IOS-XR-aaa-aaacore-cfg:calling-station/Cisco-IOS-XR-aaa-aaacore-cfg:formats/Cisco-IOS-XR-aaa-aaacore-cfg:format[Cisco-IOS-XR-aaa-aaacore-cfg:type = ' + str(self.type) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.type is not None:
                            return True

                        if self.format_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.RadiusAttribute.CallingStation.Formats.Format']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/Cisco-IOS-XR-aaa-aaacore-cfg:calling-station/Cisco-IOS-XR-aaa-aaacore-cfg:formats'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.format is not None:
                        for child_ref in self.format:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.RadiusAttribute.CallingStation.Formats']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/Cisco-IOS-XR-aaa-aaacore-cfg:calling-station'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.formats is not None and self.formats._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.RadiusAttribute.CallingStation']['meta_info']


        class CalledStation(object):
            """
            AAA called station id attribute
            
            .. attribute:: formats
            
            	AAA nas\-port\-id attribute format
            	**type**\:   :py:class:`Formats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.CalledStation.Formats>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.formats = Aaa.RadiusAttribute.CalledStation.Formats()
                self.formats.parent = self


            class Formats(object):
                """
                AAA nas\-port\-id attribute format
                
                .. attribute:: format
                
                	nas\-port\-id attribute format
                	**type**\: list of    :py:class:`Format <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.CalledStation.Formats.Format>`
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.format = YList()
                    self.format.parent = self
                    self.format.name = 'format'


                class Format(object):
                    """
                    nas\-port\-id attribute format
                    
                    .. attribute:: type  <key>
                    
                    	Nas\-Port\-Type value to apply format name on
                    	**type**\:  int
                    
                    	**range:** 0..45
                    
                    .. attribute:: format_name
                    
                    	AAA nas\-port attribute format
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'aaa-aaacore-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.type = None
                        self.format_name = None

                    @property
                    def _common_path(self):
                        if self.type is None:
                            raise YPYModelError('Key property type is None')

                        return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/Cisco-IOS-XR-aaa-aaacore-cfg:called-station/Cisco-IOS-XR-aaa-aaacore-cfg:formats/Cisco-IOS-XR-aaa-aaacore-cfg:format[Cisco-IOS-XR-aaa-aaacore-cfg:type = ' + str(self.type) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.type is not None:
                            return True

                        if self.format_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.RadiusAttribute.CalledStation.Formats.Format']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/Cisco-IOS-XR-aaa-aaacore-cfg:called-station/Cisco-IOS-XR-aaa-aaacore-cfg:formats'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.format is not None:
                        for child_ref in self.format:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.RadiusAttribute.CalledStation.Formats']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/Cisco-IOS-XR-aaa-aaacore-cfg:called-station'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.formats is not None and self.formats._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.RadiusAttribute.CalledStation']['meta_info']


        class NasPort(object):
            """
            AAA nas\-port\-id attribute
            
            .. attribute:: format_extendeds
            
            	AAA nas\-port\-id attribute format
            	**type**\:   :py:class:`FormatExtendeds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.NasPort.FormatExtendeds>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.format_extendeds = Aaa.RadiusAttribute.NasPort.FormatExtendeds()
                self.format_extendeds.parent = self


            class FormatExtendeds(object):
                """
                AAA nas\-port\-id attribute format
                
                .. attribute:: format_extended
                
                	nas\-port\-id extended attribute
                	**type**\: list of    :py:class:`FormatExtended <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.NasPort.FormatExtendeds.FormatExtended>`
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.format_extended = YList()
                    self.format_extended.parent = self
                    self.format_extended.name = 'format_extended'


                class FormatExtended(object):
                    """
                    nas\-port\-id extended attribute
                    
                    .. attribute:: value  <key>
                    
                    	format type
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: type  <key>
                    
                    	AAA nas\-port attribute format
                    	**type**\:  int
                    
                    	**range:** 0..45
                    
                    .. attribute:: format_identifier
                    
                    	A 32 character string representing the format to be used
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'aaa-aaacore-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.value = None
                        self.type = None
                        self.format_identifier = None

                    @property
                    def _common_path(self):
                        if self.value is None:
                            raise YPYModelError('Key property value is None')
                        if self.type is None:
                            raise YPYModelError('Key property type is None')

                        return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/Cisco-IOS-XR-aaa-aaacore-cfg:nas-port/Cisco-IOS-XR-aaa-aaacore-cfg:format-extendeds/Cisco-IOS-XR-aaa-aaacore-cfg:format-extended[Cisco-IOS-XR-aaa-aaacore-cfg:value = ' + str(self.value) + '][Cisco-IOS-XR-aaa-aaacore-cfg:type = ' + str(self.type) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.value is not None:
                            return True

                        if self.type is not None:
                            return True

                        if self.format_identifier is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.RadiusAttribute.NasPort.FormatExtendeds.FormatExtended']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/Cisco-IOS-XR-aaa-aaacore-cfg:nas-port/Cisco-IOS-XR-aaa-aaacore-cfg:format-extendeds'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.format_extended is not None:
                        for child_ref in self.format_extended:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.RadiusAttribute.NasPort.FormatExtendeds']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/Cisco-IOS-XR-aaa-aaacore-cfg:nas-port'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.format_extendeds is not None and self.format_extendeds._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.RadiusAttribute.NasPort']['meta_info']


        class FormatOthers(object):
            """
            AAA nas\-port\-id attribute format
            
            .. attribute:: format_other
            
            	Other configs
            	**type**\: list of    :py:class:`FormatOther <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.FormatOthers.FormatOther>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.format_other = YList()
                self.format_other.parent = self
                self.format_other.name = 'format_other'


            class FormatOther(object):
                """
                Other configs
                
                .. attribute:: nas_port_type_name  <key>
                
                	Nas\-Port\-Type value to apply format name on
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: attribute_config1
                
                	Argument1
                	**type**\:  str
                
                .. attribute:: attribute_config10
                
                	Argument10
                	**type**\:  str
                
                .. attribute:: attribute_config11
                
                	Argument11
                	**type**\:  str
                
                .. attribute:: attribute_config12
                
                	Argument12
                	**type**\:  str
                
                .. attribute:: attribute_config13
                
                	Argument13
                	**type**\:  str
                
                .. attribute:: attribute_config14
                
                	Argument14
                	**type**\:  str
                
                .. attribute:: attribute_config15
                
                	Argument15
                	**type**\:  str
                
                .. attribute:: attribute_config16
                
                	Argument16
                	**type**\:  str
                
                .. attribute:: attribute_config17
                
                	Argument17
                	**type**\:  str
                
                .. attribute:: attribute_config18
                
                	Argument18
                	**type**\:  str
                
                .. attribute:: attribute_config19
                
                	Argument19
                	**type**\:  int
                
                	**range:** 1..253
                
                .. attribute:: attribute_config2
                
                	Argument2
                	**type**\:  str
                
                .. attribute:: attribute_config3
                
                	Argument3
                	**type**\:  str
                
                .. attribute:: attribute_config4
                
                	Argument4
                	**type**\:  str
                
                .. attribute:: attribute_config5
                
                	Argument5
                	**type**\:  str
                
                .. attribute:: attribute_config6
                
                	Argument6
                	**type**\:  str
                
                .. attribute:: attribute_config7
                
                	Argument7
                	**type**\:  str
                
                .. attribute:: attribute_config8
                
                	Argument8
                	**type**\:  str
                
                .. attribute:: attribute_config9
                
                	Argument9
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.nas_port_type_name = None
                    self.attribute_config1 = None
                    self.attribute_config10 = None
                    self.attribute_config11 = None
                    self.attribute_config12 = None
                    self.attribute_config13 = None
                    self.attribute_config14 = None
                    self.attribute_config15 = None
                    self.attribute_config16 = None
                    self.attribute_config17 = None
                    self.attribute_config18 = None
                    self.attribute_config19 = None
                    self.attribute_config2 = None
                    self.attribute_config3 = None
                    self.attribute_config4 = None
                    self.attribute_config5 = None
                    self.attribute_config6 = None
                    self.attribute_config7 = None
                    self.attribute_config8 = None
                    self.attribute_config9 = None

                @property
                def _common_path(self):
                    if self.nas_port_type_name is None:
                        raise YPYModelError('Key property nas_port_type_name is None')

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/Cisco-IOS-XR-aaa-aaacore-cfg:format-others/Cisco-IOS-XR-aaa-aaacore-cfg:format-other[Cisco-IOS-XR-aaa-aaacore-cfg:nas-port-type-name = ' + str(self.nas_port_type_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.nas_port_type_name is not None:
                        return True

                    if self.attribute_config1 is not None:
                        return True

                    if self.attribute_config10 is not None:
                        return True

                    if self.attribute_config11 is not None:
                        return True

                    if self.attribute_config12 is not None:
                        return True

                    if self.attribute_config13 is not None:
                        return True

                    if self.attribute_config14 is not None:
                        return True

                    if self.attribute_config15 is not None:
                        return True

                    if self.attribute_config16 is not None:
                        return True

                    if self.attribute_config17 is not None:
                        return True

                    if self.attribute_config18 is not None:
                        return True

                    if self.attribute_config19 is not None:
                        return True

                    if self.attribute_config2 is not None:
                        return True

                    if self.attribute_config3 is not None:
                        return True

                    if self.attribute_config4 is not None:
                        return True

                    if self.attribute_config5 is not None:
                        return True

                    if self.attribute_config6 is not None:
                        return True

                    if self.attribute_config7 is not None:
                        return True

                    if self.attribute_config8 is not None:
                        return True

                    if self.attribute_config9 is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.RadiusAttribute.FormatOthers.FormatOther']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/Cisco-IOS-XR-aaa-aaacore-cfg:format-others'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.format_other is not None:
                    for child_ref in self.format_other:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.RadiusAttribute.FormatOthers']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.called_station is not None and self.called_station._has_data():
                return True

            if self.calling_station is not None and self.calling_station._has_data():
                return True

            if self.format_others is not None and self.format_others._has_data():
                return True

            if self.nas_port is not None and self.nas_port._has_data():
                return True

            if self.nas_port_id is not None and self.nas_port_id._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
            return meta._meta_table['Aaa.RadiusAttribute']['meta_info']


    class ServerGroups(object):
        """
        AAA group definitions
        
        .. attribute:: diameter_server_groups
        
        	DIAMETER server group definition
        	**type**\:   :py:class:`DiameterServerGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.DiameterServerGroups>`
        
        .. attribute:: radius_server_groups
        
        	RADIUS server group definition
        	**type**\:   :py:class:`RadiusServerGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups>`
        
        .. attribute:: tacacs_server_groups
        
        	TACACS+ server\-group definition
        	**type**\:   :py:class:`TacacsServerGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups>`
        
        

        """

        _prefix = 'aaa-locald-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.diameter_server_groups = Aaa.ServerGroups.DiameterServerGroups()
            self.diameter_server_groups.parent = self
            self.radius_server_groups = Aaa.ServerGroups.RadiusServerGroups()
            self.radius_server_groups.parent = self
            self.tacacs_server_groups = Aaa.ServerGroups.TacacsServerGroups()
            self.tacacs_server_groups.parent = self


        class DiameterServerGroups(object):
            """
            DIAMETER server group definition
            
            .. attribute:: diameter_server_group
            
            	DIAMETER server group name
            	**type**\: list of    :py:class:`DiameterServerGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup>`
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.diameter_server_group = YList()
                self.diameter_server_group.parent = self
                self.diameter_server_group.name = 'diameter_server_group'


            class DiameterServerGroup(object):
                """
                DIAMETER server group name
                
                .. attribute:: server_group_name  <key>
                
                	DIAMETER server group name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: servers
                
                	List of DIAMETER servers present in the group
                	**type**\:   :py:class:`Servers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers>`
                
                

                """

                _prefix = 'aaa-diameter-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.server_group_name = None
                    self.servers = Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers()
                    self.servers.parent = self


                class Servers(object):
                    """
                    List of DIAMETER servers present in the group
                    
                    .. attribute:: server
                    
                    	A server to include in the server group
                    	**type**\: list of    :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers.Server>`
                    
                    

                    """

                    _prefix = 'aaa-diameter-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.server = YList()
                        self.server.parent = self
                        self.server.name = 'server'


                    class Server(object):
                        """
                        A server to include in the server group
                        
                        .. attribute:: ordering_index  <key>
                        
                        	This is used to sort the servers in the order of precedence
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: peer_name  <key>
                        
                        	Name for the diameter peer configuration
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        

                        """

                        _prefix = 'aaa-diameter-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ordering_index = None
                            self.peer_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.ordering_index is None:
                                raise YPYModelError('Key property ordering_index is None')
                            if self.peer_name is None:
                                raise YPYModelError('Key property peer_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-aaa-diameter-cfg:server[Cisco-IOS-XR-aaa-diameter-cfg:ordering-index = ' + str(self.ordering_index) + '][Cisco-IOS-XR-aaa-diameter-cfg:peer-name = ' + str(self.peer_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.ordering_index is not None:
                                return True

                            if self.peer_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                            return meta._meta_table['Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers.Server']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-diameter-cfg:servers'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.server is not None:
                            for child_ref in self.server:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers']['meta_info']

                @property
                def _common_path(self):
                    if self.server_group_name is None:
                        raise YPYModelError('Key property server_group_name is None')

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:server-groups/Cisco-IOS-XR-aaa-diameter-cfg:diameter-server-groups/Cisco-IOS-XR-aaa-diameter-cfg:diameter-server-group[Cisco-IOS-XR-aaa-diameter-cfg:server-group-name = ' + str(self.server_group_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.server_group_name is not None:
                        return True

                    if self.servers is not None and self.servers._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:server-groups/Cisco-IOS-XR-aaa-diameter-cfg:diameter-server-groups'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.diameter_server_group is not None:
                    for child_ref in self.diameter_server_group:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.ServerGroups.DiameterServerGroups']['meta_info']


        class RadiusServerGroups(object):
            """
            RADIUS server group definition
            
            .. attribute:: radius_server_group
            
            	RADIUS server group name
            	**type**\: list of    :py:class:`RadiusServerGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.radius_server_group = YList()
                self.radius_server_group.parent = self
                self.radius_server_group.name = 'radius_server_group'


            class RadiusServerGroup(object):
                """
                RADIUS server group name
                
                .. attribute:: server_group_name  <key>
                
                	RADIUS server group name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: accounting
                
                	List of filters in server group
                	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting>`
                
                .. attribute:: authorization
                
                	List of filters in server group
                	**type**\:   :py:class:`Authorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization>`
                
                .. attribute:: dead_time
                
                	This indicates the length of time (in minutes) for which RADIUS servers present in this group remain marked as dead
                	**type**\:  int
                
                	**range:** 1..1440
                
                	**units**\: minute
                
                .. attribute:: load_balance
                
                	Radius load\-balancing options
                	**type**\:   :py:class:`LoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance>`
                
                .. attribute:: private_servers
                
                	List of private RADIUS servers present in the group
                	**type**\:   :py:class:`PrivateServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers>`
                
                .. attribute:: server_group_throttle
                
                	Radius throttling options
                	**type**\:   :py:class:`ServerGroupThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.ServerGroupThrottle>`
                
                .. attribute:: servers
                
                	List of RADIUS servers present in the group
                	**type**\:   :py:class:`Servers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers>`
                
                .. attribute:: source_interface
                
                	Specify interface for source address in RADIUS packets
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: vrf
                
                	Specify VRF name of RADIUS group
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.server_group_name = None
                    self.accounting = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting()
                    self.accounting.parent = self
                    self.authorization = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization()
                    self.authorization.parent = self
                    self.dead_time = None
                    self.load_balance = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance()
                    self.load_balance.parent = self
                    self.private_servers = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers()
                    self.private_servers.parent = self
                    self.server_group_throttle = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.ServerGroupThrottle()
                    self.server_group_throttle.parent = self
                    self.servers = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers()
                    self.servers.parent = self
                    self.source_interface = None
                    self.vrf = None


                class Accounting(object):
                    """
                    List of filters in server group
                    
                    .. attribute:: reply
                    
                    	Specify a filter in server group
                    	**type**\:   :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Reply>`
                    
                    .. attribute:: request
                    
                    	Specify a filter in server group
                    	**type**\:   :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Request>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.reply = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Reply()
                        self.reply.parent = self
                        self.request = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Request()
                        self.request.parent = self


                    class Request(object):
                        """
                        Specify a filter in server group
                        
                        .. attribute:: action
                        
                        	Specify the attribute list type accept or reject
                        	**type**\:   :py:class:`AaaActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaActionEnum>`
                        
                        .. attribute:: attribute_list_name
                        
                        	Name of RADIUS attribute list
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.action = None
                            self.attribute_list_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-cfg:request'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.action is not None:
                                return True

                            if self.attribute_list_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                            return meta._meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Request']['meta_info']


                    class Reply(object):
                        """
                        Specify a filter in server group
                        
                        .. attribute:: action
                        
                        	Specify the attribute list type accept or reject
                        	**type**\:   :py:class:`AaaActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaActionEnum>`
                        
                        .. attribute:: attribute_list_name
                        
                        	Name of RADIUS attribute list
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.action = None
                            self.attribute_list_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-cfg:reply'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.action is not None:
                                return True

                            if self.attribute_list_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                            return meta._meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Reply']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-cfg:accounting'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.reply is not None and self.reply._has_data():
                            return True

                        if self.request is not None and self.request._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting']['meta_info']


                class Servers(object):
                    """
                    List of RADIUS servers present in the group
                    
                    .. attribute:: server
                    
                    	A server to include in the server group
                    	**type**\: list of    :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers.Server>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.server = YList()
                        self.server.parent = self
                        self.server.name = 'server'


                    class Server(object):
                        """
                        A server to include in the server group
                        
                        .. attribute:: ordering_index  <key>
                        
                        	This is used to sort the servers in the order of precedence
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ip_address  <key>
                        
                        	IP address of RADIUS server
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: auth_port_number  <key>
                        
                        	Authentication Port number (standard port 1645)
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: acct_port_number  <key>
                        
                        	Accounting Port number (standard port 1646)
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ordering_index = None
                            self.ip_address = None
                            self.auth_port_number = None
                            self.acct_port_number = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.ordering_index is None:
                                raise YPYModelError('Key property ordering_index is None')
                            if self.ip_address is None:
                                raise YPYModelError('Key property ip_address is None')
                            if self.auth_port_number is None:
                                raise YPYModelError('Key property auth_port_number is None')
                            if self.acct_port_number is None:
                                raise YPYModelError('Key property acct_port_number is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-cfg:server[Cisco-IOS-XR-aaa-protocol-radius-cfg:ordering-index = ' + str(self.ordering_index) + '][Cisco-IOS-XR-aaa-protocol-radius-cfg:ip-address = ' + str(self.ip_address) + '][Cisco-IOS-XR-aaa-protocol-radius-cfg:auth-port-number = ' + str(self.auth_port_number) + '][Cisco-IOS-XR-aaa-protocol-radius-cfg:acct-port-number = ' + str(self.acct_port_number) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.ordering_index is not None:
                                return True

                            if self.ip_address is not None:
                                return True

                            if self.auth_port_number is not None:
                                return True

                            if self.acct_port_number is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                            return meta._meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers.Server']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-cfg:servers'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.server is not None:
                            for child_ref in self.server:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers']['meta_info']


                class PrivateServers(object):
                    """
                    List of private RADIUS servers present in the
                    group
                    
                    .. attribute:: private_server
                    
                    	A private server to include in the server group
                    	**type**\: list of    :py:class:`PrivateServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers.PrivateServer>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.private_server = YList()
                        self.private_server.parent = self
                        self.private_server.name = 'private_server'


                    class PrivateServer(object):
                        """
                        A private server to include in the server
                        group
                        
                        .. attribute:: ordering_index  <key>
                        
                        	This is used to sort the servers in the order of precedence
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ip_address  <key>
                        
                        	IP address of RADIUS server
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: auth_port_number  <key>
                        
                        	Authentication Port number (standard port 1645)
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: acct_port_number  <key>
                        
                        	Accounting Port number (standard port 1646)
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: idle_time
                        
                        	Idle time for the radius Server
                        	**type**\:  int
                        
                        	**range:** 1..60
                        
                        	**default value**\: 5
                        
                        .. attribute:: ignore_accounting_port
                        
                        	Ignore Accounting port
                        	**type**\:  bool
                        
                        .. attribute:: ignore_auth_port
                        
                        	Ignore authentication Port
                        	**type**\:  bool
                        
                        .. attribute:: private_key
                        
                        	RADIUS encryption key
                        	**type**\:  str
                        
                        	**pattern:** (!.+)\|([^!].+)
                        
                        .. attribute:: private_retransmit
                        
                        	Number of times to retransmit a request to the RADIUS server
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        	**default value**\: 3
                        
                        .. attribute:: private_timeout
                        
                        	Time to wait for a RADIUS server to reply
                        	**type**\:  int
                        
                        	**range:** 1..1000
                        
                        	**default value**\: 5
                        
                        .. attribute:: username
                        
                        	Username to be tested for automated testing
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ordering_index = None
                            self.ip_address = None
                            self.auth_port_number = None
                            self.acct_port_number = None
                            self.idle_time = None
                            self.ignore_accounting_port = None
                            self.ignore_auth_port = None
                            self.private_key = None
                            self.private_retransmit = None
                            self.private_timeout = None
                            self.username = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.ordering_index is None:
                                raise YPYModelError('Key property ordering_index is None')
                            if self.ip_address is None:
                                raise YPYModelError('Key property ip_address is None')
                            if self.auth_port_number is None:
                                raise YPYModelError('Key property auth_port_number is None')
                            if self.acct_port_number is None:
                                raise YPYModelError('Key property acct_port_number is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-cfg:private-server[Cisco-IOS-XR-aaa-protocol-radius-cfg:ordering-index = ' + str(self.ordering_index) + '][Cisco-IOS-XR-aaa-protocol-radius-cfg:ip-address = ' + str(self.ip_address) + '][Cisco-IOS-XR-aaa-protocol-radius-cfg:auth-port-number = ' + str(self.auth_port_number) + '][Cisco-IOS-XR-aaa-protocol-radius-cfg:acct-port-number = ' + str(self.acct_port_number) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.ordering_index is not None:
                                return True

                            if self.ip_address is not None:
                                return True

                            if self.auth_port_number is not None:
                                return True

                            if self.acct_port_number is not None:
                                return True

                            if self.idle_time is not None:
                                return True

                            if self.ignore_accounting_port is not None:
                                return True

                            if self.ignore_auth_port is not None:
                                return True

                            if self.private_key is not None:
                                return True

                            if self.private_retransmit is not None:
                                return True

                            if self.private_timeout is not None:
                                return True

                            if self.username is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                            return meta._meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers.PrivateServer']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-cfg:private-servers'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.private_server is not None:
                            for child_ref in self.private_server:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers']['meta_info']


                class ServerGroupThrottle(object):
                    """
                    Radius throttling options
                    
                    .. attribute:: access
                    
                    	To flow control the number of access requests sent to a radius server
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**default value**\: 0
                    
                    .. attribute:: access_timeout
                    
                    	Specify the number of timeouts exceeding which a throttled access request is dropped
                    	**type**\:  int
                    
                    	**range:** 1..10
                    
                    	**default value**\: 3
                    
                    .. attribute:: accounting
                    
                    	To flow control the number of accounting requests sent to a radius server
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**default value**\: 0
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.access = None
                        self.access_timeout = None
                        self.accounting = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-cfg:server-group-throttle'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.access is not None:
                            return True

                        if self.access_timeout is not None:
                            return True

                        if self.accounting is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.ServerGroupThrottle']['meta_info']


                class LoadBalance(object):
                    """
                    Radius load\-balancing options
                    
                    .. attribute:: method
                    
                    	Method by which the next host will be picked
                    	**type**\:   :py:class:`Method <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.method = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method()
                        self.method.parent = self


                    class Method(object):
                        """
                        Method by which the next host will be picked
                        
                        .. attribute:: name
                        
                        	Batch size for selection of the server
                        	**type**\:   :py:class:`Name <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method.Name>`
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.name = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method.Name()
                            self.name.parent = self


                        class Name(object):
                            """
                            Batch size for selection of the server
                            
                            .. attribute:: batch_size
                            
                            	Batch size for selection of the server
                            	**type**\:  int
                            
                            	**range:** 1..1500
                            
                            	**default value**\: 25
                            
                            .. attribute:: ignore_preferred_server
                            
                            	Disable preferred server for this Server Group
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**default value**\: 1
                            
                            .. attribute:: least_outstanding
                            
                            	Pick the server with the least transactions outstanding
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**default value**\: 4
                            
                            

                            """

                            _prefix = 'aaa-protocol-radius-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.batch_size = None
                                self.ignore_preferred_server = None
                                self.least_outstanding = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-cfg:name'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.batch_size is not None:
                                    return True

                                if self.ignore_preferred_server is not None:
                                    return True

                                if self.least_outstanding is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                                return meta._meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method.Name']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-cfg:method'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.name is not None and self.name._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                            return meta._meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-cfg:load-balance'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.method is not None and self.method._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance']['meta_info']


                class Authorization(object):
                    """
                    List of filters in server group
                    
                    .. attribute:: reply
                    
                    	Specify a filter in server group
                    	**type**\:   :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Reply>`
                    
                    .. attribute:: request
                    
                    	Specify a filter in server group
                    	**type**\:   :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Request>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.reply = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Reply()
                        self.reply.parent = self
                        self.request = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Request()
                        self.request.parent = self


                    class Request(object):
                        """
                        Specify a filter in server group
                        
                        .. attribute:: action
                        
                        	Specify the attribute list type accept or reject
                        	**type**\:   :py:class:`AaaActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaActionEnum>`
                        
                        .. attribute:: attribute_list_name
                        
                        	Name of RADIUS attribute list
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.action = None
                            self.attribute_list_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-cfg:request'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.action is not None:
                                return True

                            if self.attribute_list_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                            return meta._meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Request']['meta_info']


                    class Reply(object):
                        """
                        Specify a filter in server group
                        
                        .. attribute:: action
                        
                        	Specify the attribute list type accept or reject
                        	**type**\:   :py:class:`AaaActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaActionEnum>`
                        
                        .. attribute:: attribute_list_name
                        
                        	Name of RADIUS attribute list
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.action = None
                            self.attribute_list_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-cfg:reply'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.action is not None:
                                return True

                            if self.attribute_list_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                            return meta._meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Reply']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-cfg:authorization'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.reply is not None and self.reply._has_data():
                            return True

                        if self.request is not None and self.request._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization']['meta_info']

                @property
                def _common_path(self):
                    if self.server_group_name is None:
                        raise YPYModelError('Key property server_group_name is None')

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:server-groups/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius-server-groups/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius-server-group[Cisco-IOS-XR-aaa-protocol-radius-cfg:server-group-name = ' + str(self.server_group_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.server_group_name is not None:
                        return True

                    if self.accounting is not None and self.accounting._has_data():
                        return True

                    if self.authorization is not None and self.authorization._has_data():
                        return True

                    if self.dead_time is not None:
                        return True

                    if self.load_balance is not None and self.load_balance._has_data():
                        return True

                    if self.private_servers is not None and self.private_servers._has_data():
                        return True

                    if self.server_group_throttle is not None and self.server_group_throttle._has_data():
                        return True

                    if self.servers is not None and self.servers._has_data():
                        return True

                    if self.source_interface is not None:
                        return True

                    if self.vrf is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:server-groups/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius-server-groups'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.radius_server_group is not None:
                    for child_ref in self.radius_server_group:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.ServerGroups.RadiusServerGroups']['meta_info']


        class TacacsServerGroups(object):
            """
            TACACS+ server\-group definition
            
            .. attribute:: tacacs_server_group
            
            	TACACS+ Server group name
            	**type**\: list of    :py:class:`TacacsServerGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup>`
            
            

            """

            _prefix = 'aaa-tacacs-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.tacacs_server_group = YList()
                self.tacacs_server_group.parent = self
                self.tacacs_server_group.name = 'tacacs_server_group'


            class TacacsServerGroup(object):
                """
                TACACS+ Server group name
                
                .. attribute:: server_group_name  <key>
                
                	TACACS+ Server group name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: private_servers
                
                	List of private TACACS servers present in the group
                	**type**\:   :py:class:`PrivateServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers>`
                
                .. attribute:: servers
                
                	Specify a TACACS+ server
                	**type**\:   :py:class:`Servers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers>`
                
                .. attribute:: vrf
                
                	Specify VRF name of TACACS group
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-tacacs-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.server_group_name = None
                    self.private_servers = Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers()
                    self.private_servers.parent = self
                    self.servers = Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers()
                    self.servers.parent = self
                    self.vrf = None


                class Servers(object):
                    """
                    Specify a TACACS+ server
                    
                    .. attribute:: server
                    
                    	A server to include in the server group
                    	**type**\: list of    :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers.Server>`
                    
                    

                    """

                    _prefix = 'aaa-tacacs-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.server = YList()
                        self.server.parent = self
                        self.server.name = 'server'


                    class Server(object):
                        """
                        A server to include in the server group
                        
                        .. attribute:: ordering_index  <key>
                        
                        	This is used to sort the servers in the order of precedence
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ip_address  <key>
                        
                        	IP address of TACACS+ server
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        

                        """

                        _prefix = 'aaa-tacacs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ordering_index = None
                            self.ip_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.ordering_index is None:
                                raise YPYModelError('Key property ordering_index is None')
                            if self.ip_address is None:
                                raise YPYModelError('Key property ip_address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-aaa-tacacs-cfg:server[Cisco-IOS-XR-aaa-tacacs-cfg:ordering-index = ' + str(self.ordering_index) + '][Cisco-IOS-XR-aaa-tacacs-cfg:ip-address = ' + str(self.ip_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.ordering_index is not None:
                                return True

                            if self.ip_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                            return meta._meta_table['Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers.Server']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-tacacs-cfg:servers'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.server is not None:
                            for child_ref in self.server:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers']['meta_info']


                class PrivateServers(object):
                    """
                    List of private TACACS servers present in the
                    group
                    
                    .. attribute:: private_server
                    
                    	A private server to include in the server group
                    	**type**\: list of    :py:class:`PrivateServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers.PrivateServer>`
                    
                    

                    """

                    _prefix = 'aaa-tacacs-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.private_server = YList()
                        self.private_server.parent = self
                        self.private_server.name = 'private_server'


                    class PrivateServer(object):
                        """
                        A private server to include in the server
                        group
                        
                        .. attribute:: ordering_index  <key>
                        
                        	This is used to sort the servers in the order of precedence
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ip_address  <key>
                        
                        	IP address of TACACS+ server
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: port_number  <key>
                        
                        	Port number (standard 49)
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: key
                        
                        	Set TACACS+ encryption key
                        	**type**\:  str
                        
                        	**pattern:** (!.+)\|([^!].+)
                        
                        .. attribute:: timeout
                        
                        	Time to wait for a TACACS+ server to reply
                        	**type**\:  int
                        
                        	**range:** 1..1000
                        
                        	**default value**\: 5
                        
                        

                        """

                        _prefix = 'aaa-tacacs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ordering_index = None
                            self.ip_address = None
                            self.port_number = None
                            self.key = None
                            self.timeout = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.ordering_index is None:
                                raise YPYModelError('Key property ordering_index is None')
                            if self.ip_address is None:
                                raise YPYModelError('Key property ip_address is None')
                            if self.port_number is None:
                                raise YPYModelError('Key property port_number is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-aaa-tacacs-cfg:private-server[Cisco-IOS-XR-aaa-tacacs-cfg:ordering-index = ' + str(self.ordering_index) + '][Cisco-IOS-XR-aaa-tacacs-cfg:ip-address = ' + str(self.ip_address) + '][Cisco-IOS-XR-aaa-tacacs-cfg:port-number = ' + str(self.port_number) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.ordering_index is not None:
                                return True

                            if self.ip_address is not None:
                                return True

                            if self.port_number is not None:
                                return True

                            if self.key is not None:
                                return True

                            if self.timeout is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                            return meta._meta_table['Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers.PrivateServer']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-tacacs-cfg:private-servers'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.private_server is not None:
                            for child_ref in self.private_server:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers']['meta_info']

                @property
                def _common_path(self):
                    if self.server_group_name is None:
                        raise YPYModelError('Key property server_group_name is None')

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:server-groups/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs-server-groups/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs-server-group[Cisco-IOS-XR-aaa-tacacs-cfg:server-group-name = ' + str(self.server_group_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.server_group_name is not None:
                        return True

                    if self.private_servers is not None and self.private_servers._has_data():
                        return True

                    if self.servers is not None and self.servers._has_data():
                        return True

                    if self.vrf is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:server-groups/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs-server-groups'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.tacacs_server_group is not None:
                    for child_ref in self.tacacs_server_group:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.ServerGroups.TacacsServerGroups']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:server-groups'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.diameter_server_groups is not None and self.diameter_server_groups._has_data():
                return True

            if self.radius_server_groups is not None and self.radius_server_groups._has_data():
                return True

            if self.tacacs_server_groups is not None and self.tacacs_server_groups._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
            return meta._meta_table['Aaa.ServerGroups']['meta_info']


    class Usernames(object):
        """
        Configure local usernames
        
        .. attribute:: username
        
        	Local username
        	**type**\: list of    :py:class:`Username <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usernames.Username>`
        
        

        """

        _prefix = 'aaa-locald-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.username = YList()
            self.username.parent = self
            self.username.name = 'username'


        class Username(object):
            """
            Local username
            
            .. attribute:: ordering_index  <key>
            
            	This is used to sort the users in the order of precedence
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: name  <key>
            
            	Username
            	**type**\:  str
            
            .. attribute:: password
            
            	Specify the password for the user
            	**type**\:  str
            
            	**pattern:** (!.+)\|([^!].+)
            
            .. attribute:: secret
            
            	Specify the secret for the user
            	**type**\:  str
            
            	**pattern:** (!.+)\|([^!].+)
            
            .. attribute:: usergroup_under_usernames
            
            	Specify the usergroup to which this user belongs
            	**type**\:   :py:class:`UsergroupUnderUsernames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usernames.Username.UsergroupUnderUsernames>`
            
            

            """

            _prefix = 'aaa-locald-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.ordering_index = None
                self.name = None
                self.password = None
                self.secret = None
                self.usergroup_under_usernames = Aaa.Usernames.Username.UsergroupUnderUsernames()
                self.usergroup_under_usernames.parent = self


            class UsergroupUnderUsernames(object):
                """
                Specify the usergroup to which this user
                belongs
                
                .. attribute:: usergroup_under_username
                
                	Name of the usergroup
                	**type**\: list of    :py:class:`UsergroupUnderUsername <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername>`
                
                

                """

                _prefix = 'aaa-locald-cfg'
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

                    _prefix = 'aaa-locald-cfg'
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

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-cfg:usergroup-under-username[Cisco-IOS-XR-aaa-locald-cfg:name = ' + str(self.name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-cfg:usergroup-under-usernames'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.Usernames.Username.UsergroupUnderUsernames']['meta_info']

            @property
            def _common_path(self):
                if self.ordering_index is None:
                    raise YPYModelError('Key property ordering_index is None')
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:usernames/Cisco-IOS-XR-aaa-locald-cfg:username[Cisco-IOS-XR-aaa-locald-cfg:ordering-index = ' + str(self.ordering_index) + '][Cisco-IOS-XR-aaa-locald-cfg:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.ordering_index is not None:
                    return True

                if self.name is not None:
                    return True

                if self.password is not None:
                    return True

                if self.secret is not None:
                    return True

                if self.usergroup_under_usernames is not None and self.usergroup_under_usernames._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Usernames.Username']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:usernames'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
            return meta._meta_table['Aaa.Usernames']['meta_info']


    class Taskgroups(object):
        """
        Specify a taskgroup to inherit from
        
        .. attribute:: taskgroup
        
        	Taskgroup name
        	**type**\: list of    :py:class:`Taskgroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups.Taskgroup>`
        
        

        """

        _prefix = 'aaa-locald-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.taskgroup = YList()
            self.taskgroup.parent = self
            self.taskgroup.name = 'taskgroup'


        class Taskgroup(object):
            """
            Taskgroup name
            
            .. attribute:: name  <key>
            
            	Taskgroup name
            	**type**\:  str
            
            .. attribute:: description
            
            	Description for the task group
            	**type**\:  str
            
            .. attribute:: taskgroup_under_taskgroups
            
            	Specify a taskgroup to inherit from
            	**type**\:   :py:class:`TaskgroupUnderTaskgroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups>`
            
            .. attribute:: tasks
            
            	Specify task IDs to be part of this group
            	**type**\:   :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups.Taskgroup.Tasks>`
            
            

            """

            _prefix = 'aaa-locald-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.name = None
                self.description = None
                self.taskgroup_under_taskgroups = Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups()
                self.taskgroup_under_taskgroups.parent = self
                self.tasks = Aaa.Taskgroups.Taskgroup.Tasks()
                self.tasks.parent = self


            class TaskgroupUnderTaskgroups(object):
                """
                Specify a taskgroup to inherit from
                
                .. attribute:: taskgroup_under_taskgroup
                
                	Name of the task group to include
                	**type**\: list of    :py:class:`TaskgroupUnderTaskgroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups.TaskgroupUnderTaskgroup>`
                
                

                """

                _prefix = 'aaa-locald-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.taskgroup_under_taskgroup = YList()
                    self.taskgroup_under_taskgroup.parent = self
                    self.taskgroup_under_taskgroup.name = 'taskgroup_under_taskgroup'


                class TaskgroupUnderTaskgroup(object):
                    """
                    Name of the task group to include
                    
                    .. attribute:: name  <key>
                    
                    	Name of the task group to include
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    

                    """

                    _prefix = 'aaa-locald-cfg'
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

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-cfg:taskgroup-under-taskgroup[Cisco-IOS-XR-aaa-locald-cfg:name = ' + str(self.name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups.TaskgroupUnderTaskgroup']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-cfg:taskgroup-under-taskgroups'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.taskgroup_under_taskgroup is not None:
                        for child_ref in self.taskgroup_under_taskgroup:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups']['meta_info']


            class Tasks(object):
                """
                Specify task IDs to be part of this group
                
                .. attribute:: task
                
                	Task ID to be included
                	**type**\: list of    :py:class:`Task <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups.Taskgroup.Tasks.Task>`
                
                

                """

                _prefix = 'aaa-locald-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.task = YList()
                    self.task.parent = self
                    self.task.name = 'task'


                class Task(object):
                    """
                    Task ID to be included
                    
                    .. attribute:: type  <key>
                    
                    	This specifies the operation permitted for this task eg\: read/write/execute/debug
                    	**type**\:   :py:class:`AaaLocaldTaskClassEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_cfg.AaaLocaldTaskClassEnum>`
                    
                    .. attribute:: task_id  <key>
                    
                    	Task ID to which permission is to be granted (please use class AllTasks to get a list of valid task IDs)
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'aaa-locald-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.type = None
                        self.task_id = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.type is None:
                            raise YPYModelError('Key property type is None')
                        if self.task_id is None:
                            raise YPYModelError('Key property task_id is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-cfg:task[Cisco-IOS-XR-aaa-locald-cfg:type = ' + str(self.type) + '][Cisco-IOS-XR-aaa-locald-cfg:task-id = ' + str(self.task_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.type is not None:
                            return True

                        if self.task_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.Taskgroups.Taskgroup.Tasks.Task']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-cfg:tasks'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.task is not None:
                        for child_ref in self.task:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.Taskgroups.Taskgroup.Tasks']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:taskgroups/Cisco-IOS-XR-aaa-locald-cfg:taskgroup[Cisco-IOS-XR-aaa-locald-cfg:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.description is not None:
                    return True

                if self.taskgroup_under_taskgroups is not None and self.taskgroup_under_taskgroups._has_data():
                    return True

                if self.tasks is not None and self.tasks._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Taskgroups.Taskgroup']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:taskgroups'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.taskgroup is not None:
                for child_ref in self.taskgroup:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
            return meta._meta_table['Aaa.Taskgroups']['meta_info']


    class Usergroups(object):
        """
        Specify a Usergroup to inherit from
        
        .. attribute:: usergroup
        
        	Usergroup name
        	**type**\: list of    :py:class:`Usergroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups.Usergroup>`
        
        

        """

        _prefix = 'aaa-locald-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.usergroup = YList()
            self.usergroup.parent = self
            self.usergroup.name = 'usergroup'


        class Usergroup(object):
            """
            Usergroup name
            
            .. attribute:: name  <key>
            
            	Usergroup name
            	**type**\:  str
            
            .. attribute:: description
            
            	Description for the user group
            	**type**\:  str
            
            .. attribute:: taskgroup_under_usergroups
            
            	Task group associated with this group
            	**type**\:   :py:class:`TaskgroupUnderUsergroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups>`
            
            .. attribute:: usergroup_under_usergroups
            
            	User group to be inherited by this group
            	**type**\:   :py:class:`UsergroupUnderUsergroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups>`
            
            

            """

            _prefix = 'aaa-locald-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.name = None
                self.description = None
                self.taskgroup_under_usergroups = Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups()
                self.taskgroup_under_usergroups.parent = self
                self.usergroup_under_usergroups = Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups()
                self.usergroup_under_usergroups.parent = self


            class TaskgroupUnderUsergroups(object):
                """
                Task group associated with this group
                
                .. attribute:: taskgroup_under_usergroup
                
                	Name of the task group
                	**type**\: list of    :py:class:`TaskgroupUnderUsergroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups.TaskgroupUnderUsergroup>`
                
                

                """

                _prefix = 'aaa-locald-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.taskgroup_under_usergroup = YList()
                    self.taskgroup_under_usergroup.parent = self
                    self.taskgroup_under_usergroup.name = 'taskgroup_under_usergroup'


                class TaskgroupUnderUsergroup(object):
                    """
                    Name of the task group
                    
                    .. attribute:: name  <key>
                    
                    	Name of the task group
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    

                    """

                    _prefix = 'aaa-locald-cfg'
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

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-cfg:taskgroup-under-usergroup[Cisco-IOS-XR-aaa-locald-cfg:name = ' + str(self.name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups.TaskgroupUnderUsergroup']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-cfg:taskgroup-under-usergroups'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.taskgroup_under_usergroup is not None:
                        for child_ref in self.taskgroup_under_usergroup:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups']['meta_info']


            class UsergroupUnderUsergroups(object):
                """
                User group to be inherited by this group
                
                .. attribute:: usergroup_under_usergroup
                
                	Name of the user group
                	**type**\: list of    :py:class:`UsergroupUnderUsergroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups.UsergroupUnderUsergroup>`
                
                

                """

                _prefix = 'aaa-locald-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.usergroup_under_usergroup = YList()
                    self.usergroup_under_usergroup.parent = self
                    self.usergroup_under_usergroup.name = 'usergroup_under_usergroup'


                class UsergroupUnderUsergroup(object):
                    """
                    Name of the user group
                    
                    .. attribute:: name  <key>
                    
                    	Name of the user group
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    

                    """

                    _prefix = 'aaa-locald-cfg'
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

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-cfg:usergroup-under-usergroup[Cisco-IOS-XR-aaa-locald-cfg:name = ' + str(self.name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups.UsergroupUnderUsergroup']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-cfg:usergroup-under-usergroups'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.usergroup_under_usergroup is not None:
                        for child_ref in self.usergroup_under_usergroup:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:usergroups/Cisco-IOS-XR-aaa-locald-cfg:usergroup[Cisco-IOS-XR-aaa-locald-cfg:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.description is not None:
                    return True

                if self.taskgroup_under_usergroups is not None and self.taskgroup_under_usergroups._has_data():
                    return True

                if self.usergroup_under_usergroups is not None and self.usergroup_under_usergroups._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Usergroups.Usergroup']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:usergroups'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.usergroup is not None:
                for child_ref in self.usergroup:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
            return meta._meta_table['Aaa.Usergroups']['meta_info']


    class Diameter(object):
        """
        Diameter base protocol
        
        .. attribute:: diameter_timer
        
        	Timers used for the peer
        	**type**\:   :py:class:`DiameterTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.DiameterTimer>`
        
        .. attribute:: diameter_tls
        
        	TLS sub commands
        	**type**\:   :py:class:`DiameterTls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.DiameterTls>`
        
        .. attribute:: diams
        
        	Attribute list configuration for test command
        	**type**\:   :py:class:`Diams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Diams>`
        
        .. attribute:: gx
        
        	Start diameter policy\-if
        	**type**\:   :py:class:`Gx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Gx>`
        
        .. attribute:: gy
        
        	Start diameter policy\-if
        	**type**\:   :py:class:`Gy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Gy>`
        
        .. attribute:: nas
        
        	Start diameter Nas
        	**type**\:   :py:class:`Nas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Nas>`
        
        .. attribute:: origin
        
        	Origin sub commands
        	**type**\:   :py:class:`Origin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Origin>`
        
        .. attribute:: peers
        
        	List of diameter peers
        	**type**\:   :py:class:`Peers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Peers>`
        
        .. attribute:: source_interface
        
        	Specify interface for source address in DIAMETER packets
        	**type**\:  str
        
        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
        
        .. attribute:: vendor
        
        	Vendor specific
        	**type**\:   :py:class:`Vendor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Vendor>`
        
        

        """

        _prefix = 'aaa-diameter-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.diameter_timer = Aaa.Diameter.DiameterTimer()
            self.diameter_timer.parent = self
            self.diameter_tls = Aaa.Diameter.DiameterTls()
            self.diameter_tls.parent = self
            self.diams = Aaa.Diameter.Diams()
            self.diams.parent = self
            self.gx = Aaa.Diameter.Gx()
            self.gx.parent = self
            self.gy = Aaa.Diameter.Gy()
            self.gy.parent = self
            self.nas = Aaa.Diameter.Nas()
            self.nas.parent = self
            self.origin = Aaa.Diameter.Origin()
            self.origin.parent = self
            self.peers = Aaa.Diameter.Peers()
            self.peers.parent = self
            self.source_interface = None
            self.vendor = Aaa.Diameter.Vendor()
            self.vendor.parent = self


        class Gy(object):
            """
            Start diameter policy\-if
            
            .. attribute:: dest_host
            
            	Destination Host name in FQDN format
            	**type**\:  str
            
            .. attribute:: retransmit
            
            	Set retransmit count
            	**type**\:  int
            
            	**range:** 1..10
            
            .. attribute:: tx_timer
            
            	Transaction timer value
            	**type**\:  int
            
            	**range:** 1..1000
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.dest_host = None
                self.retransmit = None
                self.tx_timer = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/Cisco-IOS-XR-aaa-diameter-cfg:gy'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.dest_host is not None:
                    return True

                if self.retransmit is not None:
                    return True

                if self.tx_timer is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Diameter.Gy']['meta_info']


        class Origin(object):
            """
            Origin sub commands
            
            .. attribute:: host
            
            	Host name in FQDN format
            	**type**\:  str
            
            .. attribute:: realm
            
            	Origin Realm String
            	**type**\:  str
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.host = None
                self.realm = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/Cisco-IOS-XR-aaa-diameter-cfg:origin'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.host is not None:
                    return True

                if self.realm is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Diameter.Origin']['meta_info']


        class Nas(object):
            """
            Start diameter Nas
            
            .. attribute:: dest_host
            
            	Destination Host name in FQDN format
            	**type**\:  str
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.dest_host = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/Cisco-IOS-XR-aaa-diameter-cfg:nas'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.dest_host is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Diameter.Nas']['meta_info']


        class DiameterTls(object):
            """
            TLS sub commands
            
            .. attribute:: trustpoint
            
            	Trustpoint label to be used
            	**type**\:  str
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.trustpoint = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/Cisco-IOS-XR-aaa-diameter-cfg:diameter-tls'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.trustpoint is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Diameter.DiameterTls']['meta_info']


        class Peers(object):
            """
            List of diameter peers
            
            .. attribute:: peer
            
            	Diameter peer instance
            	**type**\: list of    :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Peers.Peer>`
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.peer = YList()
                self.peer.parent = self
                self.peer.name = 'peer'


            class Peer(object):
                """
                Diameter peer instance
                
                .. attribute:: peer_name  <key>
                
                	Name for the diameter peer configuration
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: host_destination
                
                	Destination host information
                	**type**\:  str
                
                .. attribute:: ipv4_address
                
                	IPv4 address of diameter server
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6_address
                
                	IPv6 address of diameter server
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: peer_timer
                
                	Timers used for the peer
                	**type**\:   :py:class:`PeerTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Peers.Peer.PeerTimer>`
                
                .. attribute:: peer_type
                
                	Peer Type
                	**type**\:   :py:class:`PeerType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Peers.Peer.PeerType>`
                
                .. attribute:: realm_destination
                
                	Realm to which the peer belongs to
                	**type**\:  str
                
                .. attribute:: source_interface
                
                	Specify interface for source address in DIAMETER packets
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: tcp_transport
                
                	Specify a Diameter transport protocol
                	**type**\:  int
                
                	**range:** 1..65535
                
                .. attribute:: tls_transport
                
                	Specify a Diameter security type
                	**type**\:  int
                
                	**range:** 0..1
                
                .. attribute:: vrf_ip
                
                	VRF the peer belongs to
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-diameter-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.peer_name = None
                    self.host_destination = None
                    self.ipv4_address = None
                    self.ipv6_address = None
                    self.peer_timer = Aaa.Diameter.Peers.Peer.PeerTimer()
                    self.peer_timer.parent = self
                    self.peer_type = Aaa.Diameter.Peers.Peer.PeerType()
                    self.peer_type.parent = self
                    self.realm_destination = None
                    self.source_interface = None
                    self.tcp_transport = None
                    self.tls_transport = None
                    self.vrf_ip = None


                class PeerTimer(object):
                    """
                    Timers used for the peer
                    
                    .. attribute:: connection
                    
                    	Timer value in seconds
                    	**type**\:  int
                    
                    	**range:** 1..1000
                    
                    	**default value**\: 5
                    
                    .. attribute:: transaction
                    
                    	Timer value in seconds
                    	**type**\:  int
                    
                    	**range:** 1..1000
                    
                    	**default value**\: 5
                    
                    .. attribute:: watchdog
                    
                    	Timer value in seconds
                    	**type**\:  int
                    
                    	**range:** 1..1000
                    
                    	**default value**\: 5
                    
                    

                    """

                    _prefix = 'aaa-diameter-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.connection = None
                        self.transaction = None
                        self.watchdog = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-diameter-cfg:peer-timer'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.connection is not None:
                            return True

                        if self.transaction is not None:
                            return True

                        if self.watchdog is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.Diameter.Peers.Peer.PeerTimer']['meta_info']


                class PeerType(object):
                    """
                    Peer Type
                    
                    .. attribute:: server
                    
                    	Enabled or disabled
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'aaa-diameter-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.server = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-diameter-cfg:peer-type'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.server is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.Diameter.Peers.Peer.PeerType']['meta_info']

                @property
                def _common_path(self):
                    if self.peer_name is None:
                        raise YPYModelError('Key property peer_name is None')

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/Cisco-IOS-XR-aaa-diameter-cfg:peers/Cisco-IOS-XR-aaa-diameter-cfg:peer[Cisco-IOS-XR-aaa-diameter-cfg:peer-name = ' + str(self.peer_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.peer_name is not None:
                        return True

                    if self.host_destination is not None:
                        return True

                    if self.ipv4_address is not None:
                        return True

                    if self.ipv6_address is not None:
                        return True

                    if self.peer_timer is not None and self.peer_timer._has_data():
                        return True

                    if self.peer_type is not None and self.peer_type._has_data():
                        return True

                    if self.realm_destination is not None:
                        return True

                    if self.source_interface is not None:
                        return True

                    if self.tcp_transport is not None:
                        return True

                    if self.tls_transport is not None:
                        return True

                    if self.vrf_ip is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.Diameter.Peers.Peer']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/Cisco-IOS-XR-aaa-diameter-cfg:peers'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.peer is not None:
                    for child_ref in self.peer:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Diameter.Peers']['meta_info']


        class Diams(object):
            """
            Attribute list configuration for test command
            
            .. attribute:: diam
            
            	attribute list configuration
            	**type**\: list of    :py:class:`Diam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Diams.Diam>`
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.diam = YList()
                self.diam.parent = self
                self.diam.name = 'diam'


            class Diam(object):
                """
                attribute list configuration
                
                .. attribute:: list_id  <key>
                
                	attribute list number
                	**type**\:  int
                
                	**range:** 0..99
                
                .. attribute:: diam_attr_defs
                
                	Specify an attribute definition
                	**type**\:   :py:class:`DiamAttrDefs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Diams.Diam.DiamAttrDefs>`
                
                

                """

                _prefix = 'aaa-diameter-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.list_id = None
                    self.diam_attr_defs = Aaa.Diameter.Diams.Diam.DiamAttrDefs()
                    self.diam_attr_defs.parent = self


                class DiamAttrDefs(object):
                    """
                    Specify an attribute definition
                    
                    .. attribute:: diam_attr_def
                    
                    	vendor id
                    	**type**\: list of    :py:class:`DiamAttrDef <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef>`
                    
                    

                    """

                    _prefix = 'aaa-diameter-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.diam_attr_def = YList()
                        self.diam_attr_def.parent = self
                        self.diam_attr_def.name = 'diam_attr_def'


                    class DiamAttrDef(object):
                        """
                        vendor id
                        
                        .. attribute:: vendor_id  <key>
                        
                        	value for vendor id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: attribute_id  <key>
                        
                        	enter attribute id
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: diam_attr_value
                        
                        	attr subcommands
                        	**type**\:   :py:class:`DiamAttrValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef.DiamAttrValue>`
                        
                        

                        """

                        _prefix = 'aaa-diameter-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.vendor_id = None
                            self.attribute_id = None
                            self.diam_attr_value = Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef.DiamAttrValue()
                            self.diam_attr_value.parent = self


                        class DiamAttrValue(object):
                            """
                            attr subcommands
                            
                            .. attribute:: data_type
                            
                            	Dataypte of attribute
                            	**type**\:  int
                            
                            	**range:** 0..23
                            
                            .. attribute:: mandatory
                            
                            	Is mandatory?
                            	**type**\:  int
                            
                            	**range:** 0..1
                            
                            .. attribute:: type_binary
                            
                            	Binary type
                            	**type**\:  str
                            
                            .. attribute:: type_boolean
                            
                            	Boolean type
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: type_enum
                            
                            	Enumeration type
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: type_grouped
                            
                            	Grouped attribute
                            	**type**\:  int
                            
                            	**range:** 0..99
                            
                            .. attribute:: type_identity
                            
                            	Diameter\-identity type
                            	**type**\:  str
                            
                            .. attribute:: type_ipv4_address
                            
                            	IPv4 address type
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: type_string
                            
                            	String type
                            	**type**\:  str
                            
                            .. attribute:: type_ulong
                            
                            	Numeric type
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'aaa-diameter-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.data_type = None
                                self.mandatory = None
                                self.type_binary = None
                                self.type_boolean = None
                                self.type_enum = None
                                self.type_grouped = None
                                self.type_identity = None
                                self.type_ipv4_address = None
                                self.type_string = None
                                self.type_ulong = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-aaa-diameter-cfg:diam-attr-value'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.data_type is not None:
                                    return True

                                if self.mandatory is not None:
                                    return True

                                if self.type_binary is not None:
                                    return True

                                if self.type_boolean is not None:
                                    return True

                                if self.type_enum is not None:
                                    return True

                                if self.type_grouped is not None:
                                    return True

                                if self.type_identity is not None:
                                    return True

                                if self.type_ipv4_address is not None:
                                    return True

                                if self.type_string is not None:
                                    return True

                                if self.type_ulong is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                                return meta._meta_table['Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef.DiamAttrValue']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.vendor_id is None:
                                raise YPYModelError('Key property vendor_id is None')
                            if self.attribute_id is None:
                                raise YPYModelError('Key property attribute_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-aaa-diameter-cfg:diam-attr-def[Cisco-IOS-XR-aaa-diameter-cfg:vendor-id = ' + str(self.vendor_id) + '][Cisco-IOS-XR-aaa-diameter-cfg:attribute-id = ' + str(self.attribute_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.vendor_id is not None:
                                return True

                            if self.attribute_id is not None:
                                return True

                            if self.diam_attr_value is not None and self.diam_attr_value._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                            return meta._meta_table['Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-diameter-cfg:diam-attr-defs'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.diam_attr_def is not None:
                            for child_ref in self.diam_attr_def:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.Diameter.Diams.Diam.DiamAttrDefs']['meta_info']

                @property
                def _common_path(self):
                    if self.list_id is None:
                        raise YPYModelError('Key property list_id is None')

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/Cisco-IOS-XR-aaa-diameter-cfg:diams/Cisco-IOS-XR-aaa-diameter-cfg:diam[Cisco-IOS-XR-aaa-diameter-cfg:list-id = ' + str(self.list_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.list_id is not None:
                        return True

                    if self.diam_attr_defs is not None and self.diam_attr_defs._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.Diameter.Diams.Diam']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/Cisco-IOS-XR-aaa-diameter-cfg:diams'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.diam is not None:
                    for child_ref in self.diam:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Diameter.Diams']['meta_info']


        class Gx(object):
            """
            Start diameter policy\-if
            
            .. attribute:: dest_host
            
            	Destination Host name in FQDN format
            	**type**\:  str
            
            .. attribute:: retransmit
            
            	Set retransmit count
            	**type**\:  int
            
            	**range:** 1..10
            
            .. attribute:: tx_timer
            
            	Transaction timer value
            	**type**\:  int
            
            	**range:** 1..1000
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.dest_host = None
                self.retransmit = None
                self.tx_timer = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/Cisco-IOS-XR-aaa-diameter-cfg:gx'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.dest_host is not None:
                    return True

                if self.retransmit is not None:
                    return True

                if self.tx_timer is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Diameter.Gx']['meta_info']


        class DiameterTimer(object):
            """
            Timers used for the peer
            
            .. attribute:: connection
            
            	Timer value in seconds
            	**type**\:  int
            
            	**range:** 1..1000
            
            .. attribute:: transaction
            
            	Timer value in seconds
            	**type**\:  int
            
            	**range:** 1..1000
            
            .. attribute:: watchdog
            
            	Timer value in seconds
            	**type**\:  int
            
            	**range:** 1..1000
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.connection = None
                self.transaction = None
                self.watchdog = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/Cisco-IOS-XR-aaa-diameter-cfg:diameter-timer'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.connection is not None:
                    return True

                if self.transaction is not None:
                    return True

                if self.watchdog is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Diameter.DiameterTimer']['meta_info']


        class Vendor(object):
            """
            Vendor specific
            
            .. attribute:: supported
            
            	Supported vendors
            	**type**\:   :py:class:`Supported <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Vendor.Supported>`
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.supported = Aaa.Diameter.Vendor.Supported()
                self.supported.parent = self


            class Supported(object):
                """
                Supported vendors
                
                .. attribute:: cisco
                
                	Cisco attribute support
                	**type**\:  bool
                
                .. attribute:: etsi
                
                	Etsi attribute support
                	**type**\:  bool
                
                .. attribute:: threegpp
                
                	3GPP attribute support
                	**type**\:  bool
                
                .. attribute:: vodafone
                
                	Vodafone attribute support
                	**type**\:  bool
                
                

                """

                _prefix = 'aaa-diameter-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.cisco = None
                    self.etsi = None
                    self.threegpp = None
                    self.vodafone = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/Cisco-IOS-XR-aaa-diameter-cfg:vendor/Cisco-IOS-XR-aaa-diameter-cfg:supported'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.cisco is not None:
                        return True

                    if self.etsi is not None:
                        return True

                    if self.threegpp is not None:
                        return True

                    if self.vodafone is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.Diameter.Vendor.Supported']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/Cisco-IOS-XR-aaa-diameter-cfg:vendor'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.supported is not None and self.supported._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Diameter.Vendor']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.diameter_timer is not None and self.diameter_timer._has_data():
                return True

            if self.diameter_tls is not None and self.diameter_tls._has_data():
                return True

            if self.diams is not None and self.diams._has_data():
                return True

            if self.gx is not None and self.gx._has_data():
                return True

            if self.gy is not None and self.gy._has_data():
                return True

            if self.nas is not None and self.nas._has_data():
                return True

            if self.origin is not None and self.origin._has_data():
                return True

            if self.peers is not None and self.peers._has_data():
                return True

            if self.source_interface is not None:
                return True

            if self.vendor is not None and self.vendor._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
            return meta._meta_table['Aaa.Diameter']['meta_info']


    class Radius(object):
        """
        Remote Access Dial\-In User Service
        
        .. attribute:: attributes
        
        	Table of attribute list
        	**type**\:   :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Attributes>`
        
        .. attribute:: dead_criteria
        
        	RADIUS server dead criteria
        	**type**\:   :py:class:`DeadCriteria <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.DeadCriteria>`
        
        .. attribute:: dead_time
        
        	This indicates the length of time (in minutes) for which a RADIUS server remains marked as dead
        	**type**\:  int
        
        	**range:** 1..1440
        
        	**units**\: minute
        
        .. attribute:: disallow
        
        	disallow null\-username
        	**type**\:   :py:class:`Disallow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Disallow>`
        
        .. attribute:: dynamic_authorization
        
        	RADIUS dynamic authorization
        	**type**\:   :py:class:`DynamicAuthorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.DynamicAuthorization>`
        
        .. attribute:: hosts
        
        	List of RADIUS servers
        	**type**\:   :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Hosts>`
        
        .. attribute:: idle_time
        
        	Idle time for RADIUS server
        	**type**\:  int
        
        	**range:** 1..1000
        
        	**default value**\: 5
        
        .. attribute:: ignore_accounting_port
        
        	Time to wait for a RADIUS server to reply
        	**type**\:  bool
        
        .. attribute:: ignore_auth_port
        
        	Time to wait for a RADIUS server to reply
        	**type**\:  bool
        
        .. attribute:: ipv4
        
        	IPv4 configuration
        	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Ipv4>`
        
        .. attribute:: ipv6
        
        	IPv6 configuration
        	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Ipv6>`
        
        .. attribute:: key
        
        	RADIUS encryption key
        	**type**\:  str
        
        	**pattern:** (!.+)\|([^!].+)
        
        .. attribute:: load_balance_options
        
        	Radius load\-balancing options
        	**type**\:   :py:class:`LoadBalanceOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.LoadBalanceOptions>`
        
        .. attribute:: radius_attribute
        
        	attribute
        	**type**\:   :py:class:`RadiusAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute>`
        
        .. attribute:: retransmit
        
        	Number of times to retransmit a request to the RADIUS server(0\-Disable)
        	**type**\:  int
        
        	**range:** 0..100
        
        	**default value**\: 3
        
        .. attribute:: source_port
        
        	Source port
        	**type**\:   :py:class:`SourcePort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.SourcePort>`
        
        .. attribute:: throttle
        
        	Radius throttling options
        	**type**\:   :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Throttle>`
        
        .. attribute:: timeout
        
        	Time to wait for a RADIUS server to reply
        	**type**\:  int
        
        	**range:** 1..1000
        
        	**default value**\: 5
        
        .. attribute:: username
        
        	Username to be tested for automated testing
        	**type**\:  str
        
        .. attribute:: vrfs
        
        	List of VRFs
        	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Vrfs>`
        
        .. attribute:: vsa
        
        	Unknown VSA (Vendor Specific Attribute) ignore configuration for RADIUS server
        	**type**\:   :py:class:`Vsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Vsa>`
        
        

        """

        _prefix = 'aaa-protocol-radius-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.attributes = Aaa.Radius.Attributes()
            self.attributes.parent = self
            self.dead_criteria = Aaa.Radius.DeadCriteria()
            self.dead_criteria.parent = self
            self.dead_time = None
            self.disallow = Aaa.Radius.Disallow()
            self.disallow.parent = self
            self.dynamic_authorization = Aaa.Radius.DynamicAuthorization()
            self.dynamic_authorization.parent = self
            self.hosts = Aaa.Radius.Hosts()
            self.hosts.parent = self
            self.idle_time = None
            self.ignore_accounting_port = None
            self.ignore_auth_port = None
            self.ipv4 = Aaa.Radius.Ipv4()
            self.ipv4.parent = self
            self.ipv6 = Aaa.Radius.Ipv6()
            self.ipv6.parent = self
            self.key = None
            self.load_balance_options = Aaa.Radius.LoadBalanceOptions()
            self.load_balance_options.parent = self
            self.radius_attribute = Aaa.Radius.RadiusAttribute()
            self.radius_attribute.parent = self
            self.retransmit = None
            self.source_port = Aaa.Radius.SourcePort()
            self.source_port.parent = self
            self.throttle = Aaa.Radius.Throttle()
            self.throttle.parent = self
            self.timeout = None
            self.username = None
            self.vrfs = Aaa.Radius.Vrfs()
            self.vrfs.parent = self
            self.vsa = Aaa.Radius.Vsa()
            self.vsa.parent = self


        class Hosts(object):
            """
            List of RADIUS servers
            
            .. attribute:: host
            
            	Instance of a RADIUS server
            	**type**\: list of    :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Hosts.Host>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.host = YList()
                self.host.parent = self
                self.host.name = 'host'


            class Host(object):
                """
                Instance of a RADIUS server
                
                .. attribute:: ordering_index  <key>
                
                	This is used to sort the servers in the order of precedence
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ip_address  <key>
                
                	IP address of RADIUS server
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: auth_port_number  <key>
                
                	Authentication Port number (standard port 1645)
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: acct_port_number  <key>
                
                	Accounting Port number (standard port 1646)
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: host_key
                
                	RADIUS encryption key
                	**type**\:  str
                
                	**pattern:** (!.+)\|([^!].+)
                
                .. attribute:: host_retransmit
                
                	Number of times to retransmit a request to the RADIUS server
                	**type**\:  int
                
                	**range:** 1..100
                
                	**default value**\: 3
                
                .. attribute:: host_timeout
                
                	Time to wait for a RADIUS server to reply
                	**type**\:  int
                
                	**range:** 1..1000
                
                	**default value**\: 5
                
                .. attribute:: idle_time
                
                	Idle time for RADIUS server
                	**type**\:  int
                
                	**range:** 1..1000
                
                	**default value**\: 5
                
                .. attribute:: ignore_accounting_port
                
                	Time to wait for a RADIUS server to reply
                	**type**\:  bool
                
                .. attribute:: ignore_auth_port
                
                	Time to wait for a RADIUS server to reply
                	**type**\:  bool
                
                .. attribute:: username
                
                	Username to be tested for automated testing
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ordering_index = None
                    self.ip_address = None
                    self.auth_port_number = None
                    self.acct_port_number = None
                    self.host_key = None
                    self.host_retransmit = None
                    self.host_timeout = None
                    self.idle_time = None
                    self.ignore_accounting_port = None
                    self.ignore_auth_port = None
                    self.username = None

                @property
                def _common_path(self):
                    if self.ordering_index is None:
                        raise YPYModelError('Key property ordering_index is None')
                    if self.ip_address is None:
                        raise YPYModelError('Key property ip_address is None')
                    if self.auth_port_number is None:
                        raise YPYModelError('Key property auth_port_number is None')
                    if self.acct_port_number is None:
                        raise YPYModelError('Key property acct_port_number is None')

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:hosts/Cisco-IOS-XR-aaa-protocol-radius-cfg:host[Cisco-IOS-XR-aaa-protocol-radius-cfg:ordering-index = ' + str(self.ordering_index) + '][Cisco-IOS-XR-aaa-protocol-radius-cfg:ip-address = ' + str(self.ip_address) + '][Cisco-IOS-XR-aaa-protocol-radius-cfg:auth-port-number = ' + str(self.auth_port_number) + '][Cisco-IOS-XR-aaa-protocol-radius-cfg:acct-port-number = ' + str(self.acct_port_number) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ordering_index is not None:
                        return True

                    if self.ip_address is not None:
                        return True

                    if self.auth_port_number is not None:
                        return True

                    if self.acct_port_number is not None:
                        return True

                    if self.host_key is not None:
                        return True

                    if self.host_retransmit is not None:
                        return True

                    if self.host_timeout is not None:
                        return True

                    if self.idle_time is not None:
                        return True

                    if self.ignore_accounting_port is not None:
                        return True

                    if self.ignore_auth_port is not None:
                        return True

                    if self.username is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.Radius.Hosts.Host']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:hosts'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.host is not None:
                    for child_ref in self.host:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Radius.Hosts']['meta_info']


        class DeadCriteria(object):
            """
            RADIUS server dead criteria
            
            .. attribute:: time
            
            	The minimum amount of time which must elapse since the router last received a valid RADIUS packet from the server prior to marking it dead
            	**type**\:  int
            
            	**range:** 1..120
            
            .. attribute:: tries
            
            	The number of consecutive timeouts the router must experience in order to mark the server as dead. All transmissions, including the initial transmit and all retransmits, will be counted
            	**type**\:  int
            
            	**range:** 1..100
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.time = None
                self.tries = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:dead-criteria'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.time is not None:
                    return True

                if self.tries is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Radius.DeadCriteria']['meta_info']


        class Disallow(object):
            """
            disallow null\-username
            
            .. attribute:: null_username
            
            	Disallow null\-username
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.null_username = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:disallow'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.null_username is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Radius.Disallow']['meta_info']


        class Ipv6(object):
            """
            IPv6 configuration
            
            .. attribute:: dscp
            
            	Specify the DSCP value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`AaaDscpValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaDscpValueEnum>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            
            ----
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.dscp = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:ipv6'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.dscp is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Radius.Ipv6']['meta_info']


        class DynamicAuthorization(object):
            """
            RADIUS dynamic authorization
            
            .. attribute:: authentication_type
            
            	RADIUS  dynamic  authorization  type
            	**type**\:   :py:class:`AaaAuthenticationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaAuthenticationEnum>`
            
            .. attribute:: clients
            
            	Client data
            	**type**\:   :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.DynamicAuthorization.Clients>`
            
            .. attribute:: ignore
            
            	Ignore option for server key or session key
            	**type**\:   :py:class:`AaaSelectKeyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaSelectKeyEnum>`
            
            .. attribute:: port
            
            	Specify the COA server port to listen on
            	**type**\:  int
            
            	**range:** 1000..5000
            
            .. attribute:: server_key
            
            	RADIUS CoA client encryption key
            	**type**\:  str
            
            	**pattern:** (!.+)\|([^!].+)
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.authentication_type = None
                self.clients = Aaa.Radius.DynamicAuthorization.Clients()
                self.clients.parent = self
                self.ignore = None
                self.port = None
                self.server_key = None


            class Clients(object):
                """
                Client data
                
                .. attribute:: client
                
                	Client data
                	**type**\: list of    :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.DynamicAuthorization.Clients.Client>`
                
                .. attribute:: client_vrf_name
                
                	Client data
                	**type**\: list of    :py:class:`ClientVrfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.DynamicAuthorization.Clients.ClientVrfName>`
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.client = YList()
                    self.client.parent = self
                    self.client.name = 'client'
                    self.client_vrf_name = YList()
                    self.client_vrf_name.parent = self
                    self.client_vrf_name.name = 'client_vrf_name'


                class Client(object):
                    """
                    Client data
                    
                    .. attribute:: ip_address  <key>
                    
                    	IP address of COA client
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: server_key
                    
                    	RADIUS CoA client encryption key
                    	**type**\:  str
                    
                    	**pattern:** (!.+)\|([^!].+)
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ip_address = None
                        self.server_key = None

                    @property
                    def _common_path(self):
                        if self.ip_address is None:
                            raise YPYModelError('Key property ip_address is None')

                        return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:dynamic-authorization/Cisco-IOS-XR-aaa-protocol-radius-cfg:clients/Cisco-IOS-XR-aaa-protocol-radius-cfg:client[Cisco-IOS-XR-aaa-protocol-radius-cfg:ip-address = ' + str(self.ip_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.ip_address is not None:
                            return True

                        if self.server_key is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.Radius.DynamicAuthorization.Clients.Client']['meta_info']


                class ClientVrfName(object):
                    """
                    Client data
                    
                    .. attribute:: vrf_name  <key>
                    
                    	VRF name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: ip_address  <key>
                    
                    	IP address of COA client
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: server_key
                    
                    	RADIUS CoA client encryption key
                    	**type**\:  str
                    
                    	**pattern:** (!.+)\|([^!].+)
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.vrf_name = None
                        self.ip_address = None
                        self.server_key = None

                    @property
                    def _common_path(self):
                        if self.vrf_name is None:
                            raise YPYModelError('Key property vrf_name is None')
                        if self.ip_address is None:
                            raise YPYModelError('Key property ip_address is None')

                        return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:dynamic-authorization/Cisco-IOS-XR-aaa-protocol-radius-cfg:clients/Cisco-IOS-XR-aaa-protocol-radius-cfg:client-vrf-name[Cisco-IOS-XR-aaa-protocol-radius-cfg:vrf-name = ' + str(self.vrf_name) + '][Cisco-IOS-XR-aaa-protocol-radius-cfg:ip-address = ' + str(self.ip_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.vrf_name is not None:
                            return True

                        if self.ip_address is not None:
                            return True

                        if self.server_key is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.Radius.DynamicAuthorization.Clients.ClientVrfName']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:dynamic-authorization/Cisco-IOS-XR-aaa-protocol-radius-cfg:clients'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.client is not None:
                        for child_ref in self.client:
                            if child_ref._has_data():
                                return True

                    if self.client_vrf_name is not None:
                        for child_ref in self.client_vrf_name:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.Radius.DynamicAuthorization.Clients']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:dynamic-authorization'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.authentication_type is not None:
                    return True

                if self.clients is not None and self.clients._has_data():
                    return True

                if self.ignore is not None:
                    return True

                if self.port is not None:
                    return True

                if self.server_key is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Radius.DynamicAuthorization']['meta_info']


        class LoadBalanceOptions(object):
            """
            Radius load\-balancing options
            
            .. attribute:: load_balance_method
            
            	Method by which the next host will be picked
            	**type**\:   :py:class:`LoadBalanceMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.load_balance_method = Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod()
                self.load_balance_method.parent = self


            class LoadBalanceMethod(object):
                """
                Method by which the next host will be picked
                
                .. attribute:: batch_size
                
                	Batch size for selection of the server
                	**type**\:   :py:class:`BatchSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod.BatchSize>`
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.batch_size = Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod.BatchSize()
                    self.batch_size.parent = self


                class BatchSize(object):
                    """
                    Batch size for selection of the server
                    
                    .. attribute:: batch_size
                    
                    	Batch size for selection of the server
                    	**type**\:  int
                    
                    	**range:** 1..1500
                    
                    	**default value**\: 25
                    
                    .. attribute:: ignore_preferred_server
                    
                    	Disable preferred server for this Server Group
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**default value**\: 1
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.batch_size = None
                        self.ignore_preferred_server = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:load-balance-options/Cisco-IOS-XR-aaa-protocol-radius-cfg:load-balance-method/Cisco-IOS-XR-aaa-protocol-radius-cfg:batch-size'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.batch_size is not None:
                            return True

                        if self.ignore_preferred_server is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod.BatchSize']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:load-balance-options/Cisco-IOS-XR-aaa-protocol-radius-cfg:load-balance-method'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.batch_size is not None and self.batch_size._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:load-balance-options'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.load_balance_method is not None and self.load_balance_method._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Radius.LoadBalanceOptions']['meta_info']


        class Vrfs(object):
            """
            List of VRFs
            
            .. attribute:: vrf
            
            	A VRF
            	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Vrfs.Vrf>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.vrf = YList()
                self.vrf.parent = self
                self.vrf.name = 'vrf'


            class Vrf(object):
                """
                A VRF
                
                .. attribute:: vrf_name  <key>
                
                	VRF name. Specify 'default' for defalut VRF
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: source_interface
                
                	Specify interface for source address in RADIUS packets
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.vrf_name = None
                    self.source_interface = None

                @property
                def _common_path(self):
                    if self.vrf_name is None:
                        raise YPYModelError('Key property vrf_name is None')

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:vrfs/Cisco-IOS-XR-aaa-protocol-radius-cfg:vrf[Cisco-IOS-XR-aaa-protocol-radius-cfg:vrf-name = ' + str(self.vrf_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.vrf_name is not None:
                        return True

                    if self.source_interface is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.Radius.Vrfs.Vrf']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:vrfs'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.vrf is not None:
                    for child_ref in self.vrf:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Radius.Vrfs']['meta_info']


        class Throttle(object):
            """
            Radius throttling options
            
            .. attribute:: access
            
            	To flow control the number of access requests sent to a radius server
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**default value**\: 0
            
            .. attribute:: access_timeout
            
            	Specify the number of timeouts exceeding which a throttled access request is dropped
            	**type**\:  int
            
            	**range:** 1..10
            
            	**default value**\: 3
            
            .. attribute:: accounting
            
            	To flow control the number of accounting requests sent to a radius server
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**default value**\: 0
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.access = None
                self.access_timeout = None
                self.accounting = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:throttle'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.access is not None:
                    return True

                if self.access_timeout is not None:
                    return True

                if self.accounting is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Radius.Throttle']['meta_info']


        class Vsa(object):
            """
            Unknown VSA (Vendor Specific Attribute) ignore
            configuration for RADIUS server
            
            .. attribute:: attribute
            
            	Vendor Specific Attribute
            	**type**\:   :py:class:`Attribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Vsa.Attribute>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.attribute = Aaa.Radius.Vsa.Attribute()
                self.attribute.parent = self


            class Attribute(object):
                """
                Vendor Specific Attribute
                
                .. attribute:: ignore
                
                	Ignore the VSA
                	**type**\:   :py:class:`Ignore <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Vsa.Attribute.Ignore>`
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ignore = Aaa.Radius.Vsa.Attribute.Ignore()
                    self.ignore.parent = self


                class Ignore(object):
                    """
                    Ignore the VSA
                    
                    .. attribute:: unknown
                    
                    	Ignore the VSA and no prefix will reject the unknown VSA
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.unknown = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:vsa/Cisco-IOS-XR-aaa-protocol-radius-cfg:attribute/Cisco-IOS-XR-aaa-protocol-radius-cfg:ignore'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.unknown is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.Radius.Vsa.Attribute.Ignore']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:vsa/Cisco-IOS-XR-aaa-protocol-radius-cfg:attribute'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ignore is not None and self.ignore._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.Radius.Vsa.Attribute']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:vsa'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.attribute is not None and self.attribute._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Radius.Vsa']['meta_info']


        class Ipv4(object):
            """
            IPv4 configuration
            
            .. attribute:: dscp
            
            	Specify the DSCP value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`AaaDscpValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaDscpValueEnum>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            
            ----
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.dscp = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:ipv4'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.dscp is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Radius.Ipv4']['meta_info']


        class RadiusAttribute(object):
            """
            attribute
            
            .. attribute:: acct_multi_session_id
            
            	Acct\-Session\-Id attribute(44)
            	**type**\:   :py:class:`AcctMultiSessionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute.AcctMultiSessionId>`
            
            .. attribute:: acct_session_id
            
            	Acct\-Session\-Id attribute(44)
            	**type**\:   :py:class:`AcctSessionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute.AcctSessionId>`
            
            .. attribute:: filter_id_11
            
            	Filter\-Id attribute configuration
            	**type**\:   :py:class:`FilterId11 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute.FilterId11>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.acct_multi_session_id = Aaa.Radius.RadiusAttribute.AcctMultiSessionId()
                self.acct_multi_session_id.parent = self
                self.acct_session_id = Aaa.Radius.RadiusAttribute.AcctSessionId()
                self.acct_session_id.parent = self
                self.filter_id_11 = Aaa.Radius.RadiusAttribute.FilterId11()
                self.filter_id_11.parent = self


            class FilterId11(object):
                """
                Filter\-Id attribute configuration
                
                .. attribute:: defaults
                
                	Set the attribute default direction
                	**type**\:   :py:class:`Defaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute.FilterId11.Defaults>`
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.defaults = Aaa.Radius.RadiusAttribute.FilterId11.Defaults()
                    self.defaults.parent = self


                class Defaults(object):
                    """
                    Set the attribute default direction
                    
                    .. attribute:: direction
                    
                    	Filtering is applied to ingress(inbound)/egress(outbound) packets only
                    	**type**\:   :py:class:`AaaDirectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaDirectionEnum>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.direction = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius-attribute/Cisco-IOS-XR-aaa-protocol-radius-cfg:filter-id-11/Cisco-IOS-XR-aaa-protocol-radius-cfg:defaults'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.direction is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.Radius.RadiusAttribute.FilterId11.Defaults']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius-attribute/Cisco-IOS-XR-aaa-protocol-radius-cfg:filter-id-11'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.defaults is not None and self.defaults._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.Radius.RadiusAttribute.FilterId11']['meta_info']


            class AcctMultiSessionId(object):
                """
                Acct\-Session\-Id attribute(44)
                
                .. attribute:: include_parent_session_id
                
                	Prepend Acct\-Session\-Id attribute with Nas\-Port\-Id
                	**type**\:   :py:class:`IncludeParentSessionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute.AcctMultiSessionId.IncludeParentSessionId>`
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.include_parent_session_id = Aaa.Radius.RadiusAttribute.AcctMultiSessionId.IncludeParentSessionId()
                    self.include_parent_session_id.parent = self


                class IncludeParentSessionId(object):
                    """
                    Prepend Acct\-Session\-Id attribute with
                    Nas\-Port\-Id
                    
                    .. attribute:: config
                    
                    	false/true
                    	**type**\:   :py:class:`AaaConfigEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaConfigEnum>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.config = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius-attribute/Cisco-IOS-XR-aaa-protocol-radius-cfg:acct-multi-session-id/Cisco-IOS-XR-aaa-protocol-radius-cfg:include-parent-session-id'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.config is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.Radius.RadiusAttribute.AcctMultiSessionId.IncludeParentSessionId']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius-attribute/Cisco-IOS-XR-aaa-protocol-radius-cfg:acct-multi-session-id'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.include_parent_session_id is not None and self.include_parent_session_id._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.Radius.RadiusAttribute.AcctMultiSessionId']['meta_info']


            class AcctSessionId(object):
                """
                Acct\-Session\-Id attribute(44)
                
                .. attribute:: prepend_nas_port_id
                
                	Prepend Acct\-Session\-Id attribute with Nas\-Port\-Id
                	**type**\:   :py:class:`PrependNasPortId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute.AcctSessionId.PrependNasPortId>`
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.prepend_nas_port_id = Aaa.Radius.RadiusAttribute.AcctSessionId.PrependNasPortId()
                    self.prepend_nas_port_id.parent = self


                class PrependNasPortId(object):
                    """
                    Prepend Acct\-Session\-Id attribute with
                    Nas\-Port\-Id
                    
                    .. attribute:: config
                    
                    	false/true
                    	**type**\:   :py:class:`AaaConfigEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaConfigEnum>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.config = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius-attribute/Cisco-IOS-XR-aaa-protocol-radius-cfg:acct-session-id/Cisco-IOS-XR-aaa-protocol-radius-cfg:prepend-nas-port-id'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.config is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                        return meta._meta_table['Aaa.Radius.RadiusAttribute.AcctSessionId.PrependNasPortId']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius-attribute/Cisco-IOS-XR-aaa-protocol-radius-cfg:acct-session-id'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.prepend_nas_port_id is not None and self.prepend_nas_port_id._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.Radius.RadiusAttribute.AcctSessionId']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius-attribute'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.acct_multi_session_id is not None and self.acct_multi_session_id._has_data():
                    return True

                if self.acct_session_id is not None and self.acct_session_id._has_data():
                    return True

                if self.filter_id_11 is not None and self.filter_id_11._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Radius.RadiusAttribute']['meta_info']


        class Attributes(object):
            """
            Table of attribute list
            
            .. attribute:: attribute
            
            	Attribute list name
            	**type**\: list of    :py:class:`Attribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Attributes.Attribute>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.attribute = YList()
                self.attribute.parent = self
                self.attribute.name = 'attribute'


            class Attribute(object):
                """
                Attribute list name
                
                .. attribute:: attribute_list_name  <key>
                
                	Attribute list name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: attribute
                
                	Specify RADIUS attribute
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.attribute_list_name = None
                    self.attribute = None

                @property
                def _common_path(self):
                    if self.attribute_list_name is None:
                        raise YPYModelError('Key property attribute_list_name is None')

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:attributes/Cisco-IOS-XR-aaa-protocol-radius-cfg:attribute[Cisco-IOS-XR-aaa-protocol-radius-cfg:attribute-list-name = ' + str(self.attribute_list_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.attribute_list_name is not None:
                        return True

                    if self.attribute is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.Radius.Attributes.Attribute']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:attributes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.attribute is not None:
                    for child_ref in self.attribute:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Radius.Attributes']['meta_info']


        class SourcePort(object):
            """
            Source port
            
            .. attribute:: extended
            
            	Enable source\-port extend 
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.extended = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:source-port'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.extended is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Radius.SourcePort']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.attributes is not None and self.attributes._has_data():
                return True

            if self.dead_criteria is not None and self.dead_criteria._has_data():
                return True

            if self.dead_time is not None:
                return True

            if self.disallow is not None and self.disallow._has_data():
                return True

            if self.dynamic_authorization is not None and self.dynamic_authorization._has_data():
                return True

            if self.hosts is not None and self.hosts._has_data():
                return True

            if self.idle_time is not None:
                return True

            if self.ignore_accounting_port is not None:
                return True

            if self.ignore_auth_port is not None:
                return True

            if self.ipv4 is not None and self.ipv4._has_data():
                return True

            if self.ipv6 is not None and self.ipv6._has_data():
                return True

            if self.key is not None:
                return True

            if self.load_balance_options is not None and self.load_balance_options._has_data():
                return True

            if self.radius_attribute is not None and self.radius_attribute._has_data():
                return True

            if self.retransmit is not None:
                return True

            if self.source_port is not None and self.source_port._has_data():
                return True

            if self.throttle is not None and self.throttle._has_data():
                return True

            if self.timeout is not None:
                return True

            if self.username is not None:
                return True

            if self.vrfs is not None and self.vrfs._has_data():
                return True

            if self.vsa is not None and self.vsa._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
            return meta._meta_table['Aaa.Radius']['meta_info']


    class Tacacs(object):
        """
        Modify TACACS+ query parameters
        
        .. attribute:: hosts
        
        	Specify a TACACS+ server
        	**type**\:   :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Hosts>`
        
        .. attribute:: ipv4
        
        	IPv4 configuration
        	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Ipv4>`
        
        .. attribute:: ipv6
        
        	IPv6 configuration
        	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Ipv6>`
        
        .. attribute:: key
        
        	Set TACACS+ encryption key
        	**type**\:  str
        
        	**pattern:** (!.+)\|([^!].+)
        
        .. attribute:: single_connect
        
        	Use a single connection for all sessions for a given TACACS+ server
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: timeout
        
        	Time to wait for a TACACS+ server to reply
        	**type**\:  int
        
        	**range:** 1..1000
        
        	**default value**\: 5
        
        .. attribute:: vrfs
        
        	List of VRFs
        	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Vrfs>`
        
        

        """

        _prefix = 'aaa-tacacs-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.hosts = Aaa.Tacacs.Hosts()
            self.hosts.parent = self
            self.ipv4 = Aaa.Tacacs.Ipv4()
            self.ipv4.parent = self
            self.ipv6 = Aaa.Tacacs.Ipv6()
            self.ipv6.parent = self
            self.key = None
            self.single_connect = None
            self.timeout = None
            self.vrfs = Aaa.Tacacs.Vrfs()
            self.vrfs.parent = self


        class Ipv6(object):
            """
            IPv6 configuration
            
            .. attribute:: dscp
            
            	Specify the DSCP value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`TacacsDscpValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_tacacs_cfg.TacacsDscpValueEnum>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            
            ----
            

            """

            _prefix = 'aaa-tacacs-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.dscp = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs/Cisco-IOS-XR-aaa-tacacs-cfg:ipv6'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.dscp is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Tacacs.Ipv6']['meta_info']


        class Hosts(object):
            """
            Specify a TACACS+ server
            
            .. attribute:: host
            
            	One of the TACACS+ servers
            	**type**\: list of    :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Hosts.Host>`
            
            

            """

            _prefix = 'aaa-tacacs-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.host = YList()
                self.host.parent = self
                self.host.name = 'host'


            class Host(object):
                """
                One of the TACACS+ servers
                
                .. attribute:: ordering_index  <key>
                
                	This is used to sort the servers in the order of precedence
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ip_address  <key>
                
                	IP address of TACACS+ server
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: port_number  <key>
                
                	Port number (standard 49)
                	**type**\:  int
                
                	**range:** 1..65535
                
                .. attribute:: key
                
                	Set TACACS+ encryption key
                	**type**\:  str
                
                	**pattern:** (!.+)\|([^!].+)
                
                .. attribute:: single_connect
                
                	Use a single connection for all sessions for a given TACACS+ server
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: timeout
                
                	Time to wait for a TACACS+ server to reply
                	**type**\:  int
                
                	**range:** 1..1000
                
                	**default value**\: 5
                
                

                """

                _prefix = 'aaa-tacacs-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ordering_index = None
                    self.ip_address = None
                    self.port_number = None
                    self.key = None
                    self.single_connect = None
                    self.timeout = None

                @property
                def _common_path(self):
                    if self.ordering_index is None:
                        raise YPYModelError('Key property ordering_index is None')
                    if self.ip_address is None:
                        raise YPYModelError('Key property ip_address is None')
                    if self.port_number is None:
                        raise YPYModelError('Key property port_number is None')

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs/Cisco-IOS-XR-aaa-tacacs-cfg:hosts/Cisco-IOS-XR-aaa-tacacs-cfg:host[Cisco-IOS-XR-aaa-tacacs-cfg:ordering-index = ' + str(self.ordering_index) + '][Cisco-IOS-XR-aaa-tacacs-cfg:ip-address = ' + str(self.ip_address) + '][Cisco-IOS-XR-aaa-tacacs-cfg:port-number = ' + str(self.port_number) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ordering_index is not None:
                        return True

                    if self.ip_address is not None:
                        return True

                    if self.port_number is not None:
                        return True

                    if self.key is not None:
                        return True

                    if self.single_connect is not None:
                        return True

                    if self.timeout is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.Tacacs.Hosts.Host']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs/Cisco-IOS-XR-aaa-tacacs-cfg:hosts'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.host is not None:
                    for child_ref in self.host:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Tacacs.Hosts']['meta_info']


        class Ipv4(object):
            """
            IPv4 configuration
            
            .. attribute:: dscp
            
            	Specify the DSCP value
            	**type**\: one of the below types:
            
            	**type**\:   :py:class:`TacacsDscpValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_tacacs_cfg.TacacsDscpValueEnum>`
            
            
            ----
            	**type**\:  int
            
            	**range:** 0..63
            
            
            ----
            

            """

            _prefix = 'aaa-tacacs-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.dscp = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs/Cisco-IOS-XR-aaa-tacacs-cfg:ipv4'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.dscp is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Tacacs.Ipv4']['meta_info']


        class Vrfs(object):
            """
            List of VRFs
            
            .. attribute:: vrf
            
            	A VRF
            	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Vrfs.Vrf>`
            
            

            """

            _prefix = 'aaa-tacacs-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.vrf = YList()
                self.vrf.parent = self
                self.vrf.name = 'vrf'


            class Vrf(object):
                """
                A VRF
                
                .. attribute:: vrf_name  <key>
                
                	VRF name. Specify 'default' for default VRF
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: source_interface
                
                	Specify interface for source address in TACACS+ packets
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                

                """

                _prefix = 'aaa-tacacs-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.vrf_name = None
                    self.source_interface = None

                @property
                def _common_path(self):
                    if self.vrf_name is None:
                        raise YPYModelError('Key property vrf_name is None')

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs/Cisco-IOS-XR-aaa-tacacs-cfg:vrfs/Cisco-IOS-XR-aaa-tacacs-cfg:vrf[Cisco-IOS-XR-aaa-tacacs-cfg:vrf-name = ' + str(self.vrf_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.vrf_name is not None:
                        return True

                    if self.source_interface is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                    return meta._meta_table['Aaa.Tacacs.Vrfs.Vrf']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs/Cisco-IOS-XR-aaa-tacacs-cfg:vrfs'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.vrf is not None:
                    for child_ref in self.vrf:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
                return meta._meta_table['Aaa.Tacacs.Vrfs']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.hosts is not None and self.hosts._has_data():
                return True

            if self.ipv4 is not None and self.ipv4._has_data():
                return True

            if self.ipv6 is not None and self.ipv6._has_data():
                return True

            if self.key is not None:
                return True

            if self.single_connect is not None:
                return True

            if self.timeout is not None:
                return True

            if self.vrfs is not None and self.vrfs._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
            return meta._meta_table['Aaa.Tacacs']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-aaa-lib-cfg:aaa'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.aaa_dot1x is not None and self.aaa_dot1x._has_data():
            return True

        if self.aaa_mobile is not None and self.aaa_mobile._has_data():
            return True

        if self.aaa_subscriber is not None and self.aaa_subscriber._has_data():
            return True

        if self.accounting_update is not None and self.accounting_update._has_data():
            return True

        if self.accountings is not None and self.accountings._has_data():
            return True

        if self.authentications is not None and self.authentications._has_data():
            return True

        if self.authorizations is not None and self.authorizations._has_data():
            return True

        if self.banner is not None and self.banner._has_data():
            return True

        if self.default_taskgroup is not None:
            return True

        if self.diameter is not None and self.diameter._has_data():
            return True

        if self.radius is not None and self.radius._has_data():
            return True

        if self.radius_attribute is not None and self.radius_attribute._has_data():
            return True

        if self.server_groups is not None and self.server_groups._has_data():
            return True

        if self.tacacs is not None and self.tacacs._has_data():
            return True

        if self.taskgroups is not None and self.taskgroups._has_data():
            return True

        if self.usergroups is not None and self.usergroups._has_data():
            return True

        if self.usernames is not None and self.usernames._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
        return meta._meta_table['Aaa']['meta_info']



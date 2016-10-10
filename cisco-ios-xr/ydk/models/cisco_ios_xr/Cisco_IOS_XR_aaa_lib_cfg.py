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



class AaaAccountingBroadcastEnum(Enum):
    """
    AaaAccountingBroadcastEnum

    Aaa accounting broadcast

    .. data:: NOT_SET = 0

    	Not Set

    .. data:: SET = 1

    	broadcast

    """

    NOT_SET = 0

    SET = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
        return meta._meta_table['AaaAccountingBroadcastEnum']


class AaaAccountingEnum(Enum):
    """
    AaaAccountingEnum

    Aaa accounting

    .. data:: NOT_SET = 0

    	Not Set

    .. data:: START_STOP = 1

    	Start Stop

    .. data:: STOP_ONLY = 2

    	Stop Only

    """

    NOT_SET = 0

    START_STOP = 1

    STOP_ONLY = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
        return meta._meta_table['AaaAccountingEnum']


class AaaAccountingRpFailoverEnum(Enum):
    """
    AaaAccountingRpFailoverEnum

    Aaa accounting rp failover

    .. data:: NOT_SET = 0

    	Not Set

    .. data:: SET = 1

    	rpfailover

    """

    NOT_SET = 0

    SET = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
        return meta._meta_table['AaaAccountingRpFailoverEnum']


class AaaAccountingUpdateEnum(Enum):
    """
    AaaAccountingUpdateEnum

    Aaa accounting update

    .. data:: NONE = 0

    	Not Set

    .. data:: NEWINFO = 3

    	Update records for new accountable information

    	only

    .. data:: PERIODIC = 4

    	Update records at periodic intervals

    """

    NONE = 0

    NEWINFO = 3

    PERIODIC = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
        return meta._meta_table['AaaAccountingUpdateEnum']


class AaaMethodEnum(Enum):
    """
    AaaMethodEnum

    Aaa method

    .. data:: NOT_SET = 0

    	Not Set

    .. data:: NONE = 1

    	None

    .. data:: LOCAL = 2

    	Local

    .. data:: RADIUS = 3

    	Radius

    .. data:: TACACS_PLUS = 4

    	TACACS+

    .. data:: DSMD = 5

    	DSMD

    .. data:: SGBP = 6

    	SGBP

    .. data:: ACCT_D = 7

    	AcctD

    .. data:: ERROR = 8

    	Error

    .. data:: IF_AUTHENTICATED = 9

    	If Authenticated

    .. data:: SERVER_GROUP = 10

    	Server Group

    .. data:: SERVER_GROUP_NOT_DEFINED = 11

    	Server Group Not Defined

    .. data:: LINE = 12

    	Line

    .. data:: ENABLE = 13

    	Enable

    .. data:: KERBEROS = 14

    	Kerberos

    .. data:: DIAMETER = 15

    	Diameter

    .. data:: LAST = 16

    	Last

    """

    NOT_SET = 0

    NONE = 1

    LOCAL = 2

    RADIUS = 3

    TACACS_PLUS = 4

    DSMD = 5

    SGBP = 6

    ACCT_D = 7

    ERROR = 8

    IF_AUTHENTICATED = 9

    SERVER_GROUP = 10

    SERVER_GROUP_NOT_DEFINED = 11

    LINE = 12

    ENABLE = 13

    KERBEROS = 14

    DIAMETER = 15

    LAST = 16


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
        return meta._meta_table['AaaMethodEnum']



class Aaa(object):
    """
    Authentication, Authorization and Accounting
    
    .. attribute:: accounting_update
    
    	Configuration related to 'update' accounting
    	**type**\:  :py:class:`AccountingUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AccountingUpdate>`
    
    .. attribute:: accountings
    
    	AAA accounting
    	**type**\:  :py:class:`Accountings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Accountings>`
    
    .. attribute:: authentications
    
    	AAA authentication
    	**type**\:  :py:class:`Authentications <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Authentications>`
    
    .. attribute:: authorizations
    
    	AAA authorization
    	**type**\:  :py:class:`Authorizations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Authorizations>`
    
    .. attribute:: default_taskgroup
    
    	This class is used for setting the default taskgroup to be used for remote server authentication
    	**type**\:  str
    
    .. attribute:: radius
    
    	Remote Access Dial\-In User Service
    	**type**\:  :py:class:`Radius <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius>`
    
    .. attribute:: server_groups
    
    	AAA group definitions
    	**type**\:  :py:class:`ServerGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups>`
    
    .. attribute:: tacacs
    
    	Modify TACACS+ query parameters
    	**type**\:  :py:class:`Tacacs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs>`
    
    .. attribute:: taskgroups
    
    	Specify a taskgroup to inherit from
    	**type**\:  :py:class:`Taskgroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups>`
    
    .. attribute:: usergroups
    
    	Specify a Usergroup to inherit from
    	**type**\:  :py:class:`Usergroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups>`
    
    .. attribute:: usernames
    
    	Configure local usernames
    	**type**\:  :py:class:`Usernames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usernames>`
    
    

    """

    _prefix = 'aaa-lib-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.accounting_update = None
        self.accountings = Aaa.Accountings()
        self.accountings.parent = self
        self.authentications = Aaa.Authentications()
        self.authentications.parent = self
        self.authorizations = Aaa.Authorizations()
        self.authorizations.parent = self
        self.default_taskgroup = None
        self.radius = Aaa.Radius()
        self.radius.parent = self
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
        	**type**\: list of  :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Accountings.Accounting>`
        
        

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
            
            .. attribute:: listname  <key>
            
            	Named accounting list
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: type  <key>
            
            	exec\:Account exec sessions, commands\: Account CLI commands
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: broadcast
            
            	Broadcast
            	**type**\:  :py:class:`AaaAccountingBroadcastEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.AaaAccountingBroadcastEnum>`
            
            .. attribute:: method
            
            	Method Types
            	**type**\:  list of :py:class:`AaaMethodEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.AaaMethodEnum>`
            
            .. attribute:: rp_failover
            
            	rpfailover
            	**type**\:  :py:class:`AaaAccountingRpFailoverEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.AaaAccountingRpFailoverEnum>`
            
            .. attribute:: server_group_name
            
            	Server group names
            	**type**\:  list of str
            
            .. attribute:: type_xr
            
            	Stop only/Start Stop
            	**type**\:  :py:class:`AaaAccountingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.AaaAccountingEnum>`
            
            

            """

            _prefix = 'aaa-lib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.listname = None
                self.type = None
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
                if self.listname is None:
                    raise YPYModelError('Key property listname is None')
                if self.type is None:
                    raise YPYModelError('Key property type is None')

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-lib-cfg:accountings/Cisco-IOS-XR-aaa-lib-cfg:accounting[Cisco-IOS-XR-aaa-lib-cfg:listname = ' + str(self.listname) + '][Cisco-IOS-XR-aaa-lib-cfg:type = ' + str(self.type) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.listname is not None:
                    return True

                if self.type is not None:
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
            if not self.is_config():
                return False
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
        	**type**\: list of  :py:class:`Authorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Authorizations.Authorization>`
        
        

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
            
            .. attribute:: listname  <key>
            
            	List name for AAA authorization
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: type  <key>
            
            	network\: Authorize IKE requests, commands\: Authorize CLI commands
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: method
            
            	Methods
            	**type**\:  list of :py:class:`AaaMethodEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.AaaMethodEnum>`
            
            .. attribute:: server_group_name
            
            	Server group names
            	**type**\:  list of str
            
            

            """

            _prefix = 'aaa-lib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.listname = None
                self.type = None
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
                if self.type is None:
                    raise YPYModelError('Key property type is None')

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-lib-cfg:authorizations/Cisco-IOS-XR-aaa-lib-cfg:authorization[Cisco-IOS-XR-aaa-lib-cfg:listname = ' + str(self.listname) + '][Cisco-IOS-XR-aaa-lib-cfg:type = ' + str(self.type) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.listname is not None:
                    return True

                if self.type is not None:
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
            if not self.is_config():
                return False
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
        
        .. attribute:: type
        
        	newinfo/periodic
        	**type**\:  :py:class:`AaaAccountingUpdateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.AaaAccountingUpdateEnum>`
        
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
            if not self.is_config():
                return False
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


    class Authentications(object):
        """
        AAA authentication
        
        .. attribute:: authentication
        
        	Configurations related to authentication
        	**type**\: list of  :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Authentications.Authentication>`
        
        

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
            
            .. attribute:: listname  <key>
            
            	List name for AAA authentication
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: type  <key>
            
            	login\: Authenticate login sessions, ppp\: Authenticate ppp sessions
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: method
            
            	Methods
            	**type**\:  list of :py:class:`AaaMethodEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.AaaMethodEnum>`
            
            .. attribute:: server_group_name
            
            	Server group names
            	**type**\:  list of str
            
            

            """

            _prefix = 'aaa-lib-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.listname = None
                self.type = None
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
                if self.type is None:
                    raise YPYModelError('Key property type is None')

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-lib-cfg:authentications/Cisco-IOS-XR-aaa-lib-cfg:authentication[Cisco-IOS-XR-aaa-lib-cfg:listname = ' + str(self.listname) + '][Cisco-IOS-XR-aaa-lib-cfg:type = ' + str(self.type) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.listname is not None:
                    return True

                if self.type is not None:
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
            if not self.is_config():
                return False
            if self.authentication is not None:
                for child_ref in self.authentication:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
            return meta._meta_table['Aaa.Authentications']['meta_info']


    class ServerGroups(object):
        """
        AAA group definitions
        
        .. attribute:: radius_server_groups
        
        	RADIUS server group definition
        	**type**\:  :py:class:`RadiusServerGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups>`
        
        .. attribute:: tacacs_server_groups
        
        	TACACS+ server\-group definition
        	**type**\:  :py:class:`TacacsServerGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups>`
        
        

        """

        _prefix = 'aaa-locald-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.radius_server_groups = Aaa.ServerGroups.RadiusServerGroups()
            self.radius_server_groups.parent = self
            self.tacacs_server_groups = Aaa.ServerGroups.TacacsServerGroups()
            self.tacacs_server_groups.parent = self


        class RadiusServerGroups(object):
            """
            RADIUS server group definition
            
            .. attribute:: radius_server_group
            
            	RADIUS server group name
            	**type**\: list of  :py:class:`RadiusServerGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup>`
            
            

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
                	**type**\:  :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting>`
                
                .. attribute:: authorization
                
                	List of filters in server group
                	**type**\:  :py:class:`Authorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization>`
                
                .. attribute:: dead_time
                
                	This indicates the length of time (in minutes) for which RADIUS servers present in this group remain marked as dead
                	**type**\:  int
                
                	**range:** 1..1440
                
                .. attribute:: load_balance
                
                	Radius load\-balancing options
                	**type**\:  :py:class:`LoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance>`
                
                .. attribute:: private_servers
                
                	List of private RADIUS servers present in the group
                	**type**\:  :py:class:`PrivateServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers>`
                
                .. attribute:: server_group_throttle
                
                	Radius throttling options
                	**type**\:  :py:class:`ServerGroupThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.ServerGroupThrottle>`
                
                .. attribute:: servers
                
                	List of RADIUS servers present in the group
                	**type**\:  :py:class:`Servers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers>`
                
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
                    	**type**\:  :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Reply>`
                    
                    .. attribute:: request
                    
                    	Specify a filter in server group
                    	**type**\:  :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Request>`
                    
                    

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
                        	**type**\:  :py:class:`AaaActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaActionEnum>`
                        
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
                            if not self.is_config():
                                return False
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
                        	**type**\:  :py:class:`AaaActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaActionEnum>`
                        
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
                            if not self.is_config():
                                return False
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
                        if not self.is_config():
                            return False
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
                    	**type**\: list of  :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers.Server>`
                    
                    

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
                        
                        .. attribute:: acct_port_number  <key>
                        
                        	Accounting Port number (standard port 1646)
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: auth_port_number  <key>
                        
                        	Authentication Port number (standard port 1645)
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: ip_address  <key>
                        
                        	IP address of RADIUS server
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: ordering_index  <key>
                        
                        	This is used to sort the servers in the order of precedence
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.acct_port_number = None
                            self.auth_port_number = None
                            self.ip_address = None
                            self.ordering_index = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.acct_port_number is None:
                                raise YPYModelError('Key property acct_port_number is None')
                            if self.auth_port_number is None:
                                raise YPYModelError('Key property auth_port_number is None')
                            if self.ip_address is None:
                                raise YPYModelError('Key property ip_address is None')
                            if self.ordering_index is None:
                                raise YPYModelError('Key property ordering_index is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-cfg:server[Cisco-IOS-XR-aaa-protocol-radius-cfg:acct-port-number = ' + str(self.acct_port_number) + '][Cisco-IOS-XR-aaa-protocol-radius-cfg:auth-port-number = ' + str(self.auth_port_number) + '][Cisco-IOS-XR-aaa-protocol-radius-cfg:ip-address = ' + str(self.ip_address) + '][Cisco-IOS-XR-aaa-protocol-radius-cfg:ordering-index = ' + str(self.ordering_index) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.acct_port_number is not None:
                                return True

                            if self.auth_port_number is not None:
                                return True

                            if self.ip_address is not None:
                                return True

                            if self.ordering_index is not None:
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
                        if not self.is_config():
                            return False
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
                    	**type**\: list of  :py:class:`PrivateServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers.PrivateServer>`
                    
                    

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
                        
                        .. attribute:: acct_port_number  <key>
                        
                        	Accounting Port number (standard port 1646)
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: auth_port_number  <key>
                        
                        	Authentication Port number (standard port 1645)
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: ip_address  <key>
                        
                        	IP address of RADIUS server
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: ordering_index  <key>
                        
                        	This is used to sort the servers in the order of precedence
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: idle_time
                        
                        	Idle time for the radius Server
                        	**type**\:  int
                        
                        	**range:** 1..60
                        
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
                        
                        .. attribute:: private_timeout
                        
                        	Time to wait for a RADIUS server to reply
                        	**type**\:  int
                        
                        	**range:** 1..1000
                        
                        .. attribute:: username
                        
                        	Username to be tested for automated testing
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.acct_port_number = None
                            self.auth_port_number = None
                            self.ip_address = None
                            self.ordering_index = None
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
                            if self.acct_port_number is None:
                                raise YPYModelError('Key property acct_port_number is None')
                            if self.auth_port_number is None:
                                raise YPYModelError('Key property auth_port_number is None')
                            if self.ip_address is None:
                                raise YPYModelError('Key property ip_address is None')
                            if self.ordering_index is None:
                                raise YPYModelError('Key property ordering_index is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-aaa-protocol-radius-cfg:private-server[Cisco-IOS-XR-aaa-protocol-radius-cfg:acct-port-number = ' + str(self.acct_port_number) + '][Cisco-IOS-XR-aaa-protocol-radius-cfg:auth-port-number = ' + str(self.auth_port_number) + '][Cisco-IOS-XR-aaa-protocol-radius-cfg:ip-address = ' + str(self.ip_address) + '][Cisco-IOS-XR-aaa-protocol-radius-cfg:ordering-index = ' + str(self.ordering_index) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.acct_port_number is not None:
                                return True

                            if self.auth_port_number is not None:
                                return True

                            if self.ip_address is not None:
                                return True

                            if self.ordering_index is not None:
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
                        if not self.is_config():
                            return False
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
                    
                    .. attribute:: access_timeout
                    
                    	Specify the number of timeouts exceeding which a throttled access request is dropped
                    	**type**\:  int
                    
                    	**range:** 1..10
                    
                    .. attribute:: accounting
                    
                    	To flow control the number of accounting requests sent to a radius server
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

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
                        if not self.is_config():
                            return False
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
                    	**type**\:  :py:class:`Method <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method>`
                    
                    

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
                        	**type**\:  :py:class:`Name <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method.Name>`
                        
                        

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
                            
                            .. attribute:: ignore_preferred_server
                            
                            	Disable preferred server for this Server Group
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: least_outstanding
                            
                            	Pick the server with the least transactions outstanding
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

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
                                if not self.is_config():
                                    return False
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
                            if not self.is_config():
                                return False
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
                        if not self.is_config():
                            return False
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
                    	**type**\:  :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Reply>`
                    
                    .. attribute:: request
                    
                    	Specify a filter in server group
                    	**type**\:  :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Request>`
                    
                    

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
                        	**type**\:  :py:class:`AaaActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaActionEnum>`
                        
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
                            if not self.is_config():
                                return False
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
                        	**type**\:  :py:class:`AaaActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaActionEnum>`
                        
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
                            if not self.is_config():
                                return False
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
                        if not self.is_config():
                            return False
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
                    if not self.is_config():
                        return False
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
                if not self.is_config():
                    return False
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
            	**type**\: list of  :py:class:`TacacsServerGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup>`
            
            

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
                	**type**\:  :py:class:`PrivateServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers>`
                
                .. attribute:: servers
                
                	Specify a TACACS+ server
                	**type**\:  :py:class:`Servers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers>`
                
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
                    	**type**\: list of  :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers.Server>`
                    
                    

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
                        
                        .. attribute:: ip_address  <key>
                        
                        	IP address of TACACS+ server
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: ordering_index  <key>
                        
                        	This is used to sort the servers in the order of precedence
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        

                        """

                        _prefix = 'aaa-tacacs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ip_address = None
                            self.ordering_index = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.ip_address is None:
                                raise YPYModelError('Key property ip_address is None')
                            if self.ordering_index is None:
                                raise YPYModelError('Key property ordering_index is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-aaa-tacacs-cfg:server[Cisco-IOS-XR-aaa-tacacs-cfg:ip-address = ' + str(self.ip_address) + '][Cisco-IOS-XR-aaa-tacacs-cfg:ordering-index = ' + str(self.ordering_index) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.ip_address is not None:
                                return True

                            if self.ordering_index is not None:
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
                        if not self.is_config():
                            return False
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
                    	**type**\: list of  :py:class:`PrivateServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers.PrivateServer>`
                    
                    

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
                        
                        .. attribute:: ip_address  <key>
                        
                        	IP address of TACACS+ server
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: ordering_index  <key>
                        
                        	This is used to sort the servers in the order of precedence
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
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
                        
                        

                        """

                        _prefix = 'aaa-tacacs-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ip_address = None
                            self.ordering_index = None
                            self.port_number = None
                            self.key = None
                            self.timeout = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.ip_address is None:
                                raise YPYModelError('Key property ip_address is None')
                            if self.ordering_index is None:
                                raise YPYModelError('Key property ordering_index is None')
                            if self.port_number is None:
                                raise YPYModelError('Key property port_number is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-aaa-tacacs-cfg:private-server[Cisco-IOS-XR-aaa-tacacs-cfg:ip-address = ' + str(self.ip_address) + '][Cisco-IOS-XR-aaa-tacacs-cfg:ordering-index = ' + str(self.ordering_index) + '][Cisco-IOS-XR-aaa-tacacs-cfg:port-number = ' + str(self.port_number) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.ip_address is not None:
                                return True

                            if self.ordering_index is not None:
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
                        if not self.is_config():
                            return False
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
                    if not self.is_config():
                        return False
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
                if not self.is_config():
                    return False
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
            if not self.is_config():
                return False
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
        	**type**\: list of  :py:class:`Username <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usernames.Username>`
        
        

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
            
            .. attribute:: name  <key>
            
            	Username
            	**type**\:  str
            
            .. attribute:: ordering_index  <key>
            
            	This is used to sort the users in the order of precedence
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
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
            	**type**\:  :py:class:`UsergroupUnderUsernames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usernames.Username.UsergroupUnderUsernames>`
            
            

            """

            _prefix = 'aaa-locald-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.name = None
                self.ordering_index = None
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
                	**type**\: list of  :py:class:`UsergroupUnderUsername <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername>`
                
                

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
                        if not self.is_config():
                            return False
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
                    if not self.is_config():
                        return False
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
                if self.name is None:
                    raise YPYModelError('Key property name is None')
                if self.ordering_index is None:
                    raise YPYModelError('Key property ordering_index is None')

                return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:usernames/Cisco-IOS-XR-aaa-locald-cfg:username[Cisco-IOS-XR-aaa-locald-cfg:name = ' + str(self.name) + '][Cisco-IOS-XR-aaa-locald-cfg:ordering-index = ' + str(self.ordering_index) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.name is not None:
                    return True

                if self.ordering_index is not None:
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
            if not self.is_config():
                return False
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
        	**type**\: list of  :py:class:`Taskgroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups.Taskgroup>`
        
        

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
            	**type**\:  :py:class:`TaskgroupUnderTaskgroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups>`
            
            .. attribute:: tasks
            
            	Specify task IDs to be part of this group
            	**type**\:  :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups.Taskgroup.Tasks>`
            
            

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
                	**type**\: list of  :py:class:`TaskgroupUnderTaskgroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups.TaskgroupUnderTaskgroup>`
                
                

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
                        if not self.is_config():
                            return False
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
                    if not self.is_config():
                        return False
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
                	**type**\: list of  :py:class:`Task <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups.Taskgroup.Tasks.Task>`
                
                

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
                    
                    .. attribute:: task_id  <key>
                    
                    	Task ID to which permission is to be granted (please use class AllTasks to get a list of valid task IDs)
                    	**type**\:  str
                    
                    .. attribute:: type  <key>
                    
                    	This specifies the operation permitted for this task eg\: read/write/execute/debug
                    	**type**\:  :py:class:`AaaLocaldTaskClassEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_cfg.AaaLocaldTaskClassEnum>`
                    
                    

                    """

                    _prefix = 'aaa-locald-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.task_id = None
                        self.type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.task_id is None:
                            raise YPYModelError('Key property task_id is None')
                        if self.type is None:
                            raise YPYModelError('Key property type is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-cfg:task[Cisco-IOS-XR-aaa-locald-cfg:task-id = ' + str(self.task_id) + '][Cisco-IOS-XR-aaa-locald-cfg:type = ' + str(self.type) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.task_id is not None:
                            return True

                        if self.type is not None:
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
                    if not self.is_config():
                        return False
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
                if not self.is_config():
                    return False
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
            if not self.is_config():
                return False
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
        	**type**\: list of  :py:class:`Usergroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups.Usergroup>`
        
        

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
            	**type**\:  :py:class:`TaskgroupUnderUsergroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups>`
            
            .. attribute:: usergroup_under_usergroups
            
            	User group to be inherited by this group
            	**type**\:  :py:class:`UsergroupUnderUsergroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups>`
            
            

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
                	**type**\: list of  :py:class:`TaskgroupUnderUsergroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups.TaskgroupUnderUsergroup>`
                
                

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
                        if not self.is_config():
                            return False
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
                    if not self.is_config():
                        return False
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
                	**type**\: list of  :py:class:`UsergroupUnderUsergroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups.UsergroupUnderUsergroup>`
                
                

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
                        if not self.is_config():
                            return False
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
                    if not self.is_config():
                        return False
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
                if not self.is_config():
                    return False
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
            if not self.is_config():
                return False
            if self.usergroup is not None:
                for child_ref in self.usergroup:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_lib_cfg as meta
            return meta._meta_table['Aaa.Usergroups']['meta_info']


    class Radius(object):
        """
        Remote Access Dial\-In User Service
        
        .. attribute:: attributes
        
        	Table of attribute list
        	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Attributes>`
        
        .. attribute:: dead_criteria
        
        	RADIUS server dead criteria
        	**type**\:  :py:class:`DeadCriteria <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.DeadCriteria>`
        
        .. attribute:: dead_time
        
        	This indicates the length of time (in minutes) for which a RADIUS server remains marked as dead
        	**type**\:  int
        
        	**range:** 1..1440
        
        .. attribute:: disallow
        
        	disallow null\-username
        	**type**\:  :py:class:`Disallow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Disallow>`
        
        .. attribute:: dynamic_authorization
        
        	RADIUS dynamic authorization
        	**type**\:  :py:class:`DynamicAuthorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.DynamicAuthorization>`
        
        .. attribute:: hosts
        
        	List of RADIUS servers
        	**type**\:  :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Hosts>`
        
        .. attribute:: idle_time
        
        	Idle time for RADIUS server
        	**type**\:  int
        
        	**range:** 1..1000
        
        .. attribute:: ignore_accounting_port
        
        	Time to wait for a RADIUS server to reply
        	**type**\:  bool
        
        .. attribute:: ignore_auth_port
        
        	Time to wait for a RADIUS server to reply
        	**type**\:  bool
        
        .. attribute:: ipv4
        
        	IPv4 configuration
        	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Ipv4>`
        
        .. attribute:: ipv6
        
        	IPv6 configuration
        	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Ipv6>`
        
        .. attribute:: key
        
        	RADIUS encryption key
        	**type**\:  str
        
        	**pattern:** (!.+)\|([^!].+)
        
        .. attribute:: load_balance_options
        
        	Radius load\-balancing options
        	**type**\:  :py:class:`LoadBalanceOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.LoadBalanceOptions>`
        
        .. attribute:: radius_attribute
        
        	attribute
        	**type**\:  :py:class:`RadiusAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute>`
        
        .. attribute:: retransmit
        
        	Number of times to retransmit a request to the RADIUS server
        	**type**\:  int
        
        	**range:** 1..100
        
        .. attribute:: source_port
        
        	Source port
        	**type**\:  :py:class:`SourcePort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.SourcePort>`
        
        .. attribute:: throttle
        
        	Radius throttling options
        	**type**\:  :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Throttle>`
        
        .. attribute:: timeout
        
        	Time to wait for a RADIUS server to reply
        	**type**\:  int
        
        	**range:** 1..1000
        
        .. attribute:: username
        
        	Username to be tested for automated testing
        	**type**\:  str
        
        .. attribute:: vrfs
        
        	List of VRFs
        	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Vrfs>`
        
        .. attribute:: vsa
        
        	Unknown VSA (Vendor Specific Attribute) ignore configuration for RADIUS server
        	**type**\:  :py:class:`Vsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Vsa>`
        
        

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
            	**type**\: list of  :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Hosts.Host>`
            
            

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
                
                .. attribute:: acct_port_number  <key>
                
                	Accounting Port number (standard port 1646)
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: auth_port_number  <key>
                
                	Authentication Port number (standard port 1645)
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: ip_address  <key>
                
                	IP address of RADIUS server
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: ordering_index  <key>
                
                	This is used to sort the servers in the order of precedence
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: host_key
                
                	RADIUS encryption key
                	**type**\:  str
                
                	**pattern:** (!.+)\|([^!].+)
                
                .. attribute:: host_retransmit
                
                	Number of times to retransmit a request to the RADIUS server
                	**type**\:  int
                
                	**range:** 1..100
                
                .. attribute:: host_timeout
                
                	Time to wait for a RADIUS server to reply
                	**type**\:  int
                
                	**range:** 1..1000
                
                .. attribute:: idle_time
                
                	Idle time for RADIUS server
                	**type**\:  int
                
                	**range:** 1..1000
                
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
                    self.acct_port_number = None
                    self.auth_port_number = None
                    self.ip_address = None
                    self.ordering_index = None
                    self.host_key = None
                    self.host_retransmit = None
                    self.host_timeout = None
                    self.idle_time = None
                    self.ignore_accounting_port = None
                    self.ignore_auth_port = None
                    self.username = None

                @property
                def _common_path(self):
                    if self.acct_port_number is None:
                        raise YPYModelError('Key property acct_port_number is None')
                    if self.auth_port_number is None:
                        raise YPYModelError('Key property auth_port_number is None')
                    if self.ip_address is None:
                        raise YPYModelError('Key property ip_address is None')
                    if self.ordering_index is None:
                        raise YPYModelError('Key property ordering_index is None')

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:hosts/Cisco-IOS-XR-aaa-protocol-radius-cfg:host[Cisco-IOS-XR-aaa-protocol-radius-cfg:acct-port-number = ' + str(self.acct_port_number) + '][Cisco-IOS-XR-aaa-protocol-radius-cfg:auth-port-number = ' + str(self.auth_port_number) + '][Cisco-IOS-XR-aaa-protocol-radius-cfg:ip-address = ' + str(self.ip_address) + '][Cisco-IOS-XR-aaa-protocol-radius-cfg:ordering-index = ' + str(self.ordering_index) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.acct_port_number is not None:
                        return True

                    if self.auth_port_number is not None:
                        return True

                    if self.ip_address is not None:
                        return True

                    if self.ordering_index is not None:
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
                if not self.is_config():
                    return False
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
                if not self.is_config():
                    return False
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
                if not self.is_config():
                    return False
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
            
            	**type**\:  :py:class:`AaaDscpValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaDscpValueEnum>`
            
            
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
                if not self.is_config():
                    return False
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
            	**type**\:  :py:class:`AaaAuthenticationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaAuthenticationEnum>`
            
            .. attribute:: clients
            
            	Client data
            	**type**\:  :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.DynamicAuthorization.Clients>`
            
            .. attribute:: ignore
            
            	Ignore option for server key or session key
            	**type**\:  :py:class:`AaaSelectKeyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaSelectKeyEnum>`
            
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
                	**type**\: list of  :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.DynamicAuthorization.Clients.Client>`
                
                .. attribute:: client_vrf_name
                
                	Client data
                	**type**\: list of  :py:class:`ClientVrfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.DynamicAuthorization.Clients.ClientVrfName>`
                
                

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
                        if not self.is_config():
                            return False
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
                    
                    .. attribute:: ip_address  <key>
                    
                    	IP address of COA client
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: vrf_name  <key>
                    
                    	VRF name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
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
                        self.vrf_name = None
                        self.server_key = None

                    @property
                    def _common_path(self):
                        if self.ip_address is None:
                            raise YPYModelError('Key property ip_address is None')
                        if self.vrf_name is None:
                            raise YPYModelError('Key property vrf_name is None')

                        return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/Cisco-IOS-XR-aaa-protocol-radius-cfg:dynamic-authorization/Cisco-IOS-XR-aaa-protocol-radius-cfg:clients/Cisco-IOS-XR-aaa-protocol-radius-cfg:client-vrf-name[Cisco-IOS-XR-aaa-protocol-radius-cfg:ip-address = ' + str(self.ip_address) + '][Cisco-IOS-XR-aaa-protocol-radius-cfg:vrf-name = ' + str(self.vrf_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.ip_address is not None:
                            return True

                        if self.vrf_name is not None:
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
                    if not self.is_config():
                        return False
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
                if not self.is_config():
                    return False
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
            	**type**\:  :py:class:`LoadBalanceMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod>`
            
            

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
                	**type**\:  :py:class:`BatchSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod.BatchSize>`
                
                

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
                    
                    .. attribute:: ignore_preferred_server
                    
                    	Disable preferred server for this Server Group
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

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
                        if not self.is_config():
                            return False
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
                    if not self.is_config():
                        return False
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
                if not self.is_config():
                    return False
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
            	**type**\: list of  :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Vrfs.Vrf>`
            
            

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
                    if not self.is_config():
                        return False
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
                if not self.is_config():
                    return False
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
            
            .. attribute:: access_timeout
            
            	Specify the number of timeouts exceeding which a throttled access request is dropped
            	**type**\:  int
            
            	**range:** 1..10
            
            .. attribute:: accounting
            
            	To flow control the number of accounting requests sent to a radius server
            	**type**\:  int
            
            	**range:** 0..65535
            
            

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
                if not self.is_config():
                    return False
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
            	**type**\:  :py:class:`Attribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Vsa.Attribute>`
            
            

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
                	**type**\:  :py:class:`Ignore <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Vsa.Attribute.Ignore>`
                
                

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
                    	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                    
                    

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
                        if not self.is_config():
                            return False
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
                    if not self.is_config():
                        return False
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
                if not self.is_config():
                    return False
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
            
            	**type**\:  :py:class:`AaaDscpValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaDscpValueEnum>`
            
            
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
                if not self.is_config():
                    return False
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
            	**type**\:  :py:class:`AcctMultiSessionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute.AcctMultiSessionId>`
            
            .. attribute:: acct_session_id
            
            	Acct\-Session\-Id attribute(44)
            	**type**\:  :py:class:`AcctSessionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute.AcctSessionId>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.acct_multi_session_id = Aaa.Radius.RadiusAttribute.AcctMultiSessionId()
                self.acct_multi_session_id.parent = self
                self.acct_session_id = Aaa.Radius.RadiusAttribute.AcctSessionId()
                self.acct_session_id.parent = self


            class AcctMultiSessionId(object):
                """
                Acct\-Session\-Id attribute(44)
                
                .. attribute:: include_parent_session_id
                
                	Prepend Acct\-Session\-Id attribute with Nas\-Port\-Id
                	**type**\:  :py:class:`IncludeParentSessionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute.AcctMultiSessionId.IncludeParentSessionId>`
                
                

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
                    	**type**\:  :py:class:`AaaConfigEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaConfigEnum>`
                    
                    

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
                        if not self.is_config():
                            return False
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
                    if not self.is_config():
                        return False
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
                	**type**\:  :py:class:`PrependNasPortId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute.AcctSessionId.PrependNasPortId>`
                
                

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
                    	**type**\:  :py:class:`AaaConfigEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaConfigEnum>`
                    
                    

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
                        if not self.is_config():
                            return False
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
                    if not self.is_config():
                        return False
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
                if not self.is_config():
                    return False
                if self.acct_multi_session_id is not None and self.acct_multi_session_id._has_data():
                    return True

                if self.acct_session_id is not None and self.acct_session_id._has_data():
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
            	**type**\: list of  :py:class:`Attribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Attributes.Attribute>`
            
            

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
                    if not self.is_config():
                        return False
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
                if not self.is_config():
                    return False
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
            	**type**\:  :py:class:`Empty <ydk.types.Empty>`
            
            

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
                if not self.is_config():
                    return False
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
            if not self.is_config():
                return False
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
        	**type**\:  :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Hosts>`
        
        .. attribute:: ipv4
        
        	IPv4 configuration
        	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Ipv4>`
        
        .. attribute:: ipv6
        
        	IPv6 configuration
        	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Ipv6>`
        
        .. attribute:: key
        
        	Set TACACS+ encryption key
        	**type**\:  str
        
        	**pattern:** (!.+)\|([^!].+)
        
        .. attribute:: single_connect
        
        	Use a single connection for all sessions for a given TACACS+ server
        	**type**\:  bool
        
        .. attribute:: timeout
        
        	Time to wait for a TACACS+ server to reply
        	**type**\:  int
        
        	**range:** 1..1000
        
        .. attribute:: vrfs
        
        	List of VRFs
        	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Vrfs>`
        
        

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
            
            	**type**\:  :py:class:`TacacsDscpValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_tacacs_cfg.TacacsDscpValueEnum>`
            
            
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
                if not self.is_config():
                    return False
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
            	**type**\: list of  :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Hosts.Host>`
            
            

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
                
                .. attribute:: ip_address  <key>
                
                	IP address of TACACS+ server
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: ordering_index  <key>
                
                	This is used to sort the servers in the order of precedence
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
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
                
                .. attribute:: timeout
                
                	Time to wait for a TACACS+ server to reply
                	**type**\:  int
                
                	**range:** 1..1000
                
                

                """

                _prefix = 'aaa-tacacs-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ip_address = None
                    self.ordering_index = None
                    self.port_number = None
                    self.key = None
                    self.single_connect = None
                    self.timeout = None

                @property
                def _common_path(self):
                    if self.ip_address is None:
                        raise YPYModelError('Key property ip_address is None')
                    if self.ordering_index is None:
                        raise YPYModelError('Key property ordering_index is None')
                    if self.port_number is None:
                        raise YPYModelError('Key property port_number is None')

                    return '/Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs/Cisco-IOS-XR-aaa-tacacs-cfg:hosts/Cisco-IOS-XR-aaa-tacacs-cfg:host[Cisco-IOS-XR-aaa-tacacs-cfg:ip-address = ' + str(self.ip_address) + '][Cisco-IOS-XR-aaa-tacacs-cfg:ordering-index = ' + str(self.ordering_index) + '][Cisco-IOS-XR-aaa-tacacs-cfg:port-number = ' + str(self.port_number) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.ip_address is not None:
                        return True

                    if self.ordering_index is not None:
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
                if not self.is_config():
                    return False
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
            
            	**type**\:  :py:class:`TacacsDscpValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_tacacs_cfg.TacacsDscpValueEnum>`
            
            
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
                if not self.is_config():
                    return False
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
            	**type**\: list of  :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Vrfs.Vrf>`
            
            

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
                    if not self.is_config():
                        return False
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
                if not self.is_config():
                    return False
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
            if not self.is_config():
                return False
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
        if not self.is_config():
            return False
        if self.accounting_update is not None and self.accounting_update._has_data():
            return True

        if self.accountings is not None and self.accountings._has_data():
            return True

        if self.authentications is not None and self.authentications._has_data():
            return True

        if self.authorizations is not None and self.authorizations._has_data():
            return True

        if self.default_taskgroup is not None:
            return True

        if self.radius is not None and self.radius._has_data():
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



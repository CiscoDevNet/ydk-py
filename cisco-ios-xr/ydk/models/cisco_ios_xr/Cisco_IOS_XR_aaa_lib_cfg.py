""" Cisco_IOS_XR_aaa_lib_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-lib package configuration.

This module contains definitions
for the following management objects\:
  aaa\: Authentication, Authorization and Accounting

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Aaa(Entity):
    """
    Authentication, Authorization and Accounting
    
    .. attribute:: accountings
    
    	AAA accounting
    	**type**\:  :py:class:`Accountings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Accountings>`
    
    .. attribute:: authorizations
    
    	AAA authorization
    	**type**\:  :py:class:`Authorizations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Authorizations>`
    
    .. attribute:: accounting_update
    
    	Configuration related to 'update' accounting
    	**type**\:  :py:class:`AccountingUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AccountingUpdate>`
    
    	**presence node**\: True
    
    .. attribute:: banner
    
    	AAA banner
    	**type**\:  :py:class:`Banner <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Banner>`
    
    .. attribute:: authentications
    
    	AAA authentication
    	**type**\:  :py:class:`Authentications <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Authentications>`
    
    .. attribute:: aaa_subscriber
    
    	AAA subscriber
    	**type**\:  :py:class:`AaaSubscriber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber>`
    
    .. attribute:: aaa_mobile
    
    	AAA Mobile
    	**type**\:  :py:class:`AaaMobile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaMobile>`
    
    .. attribute:: aaa_dot1x
    
    	AAA Dot1x
    	**type**\:  :py:class:`AaaDot1x <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaDot1x>`
    
    .. attribute:: radius_attribute
    
    	AAA RADIUS attribute configurations
    	**type**\:  :py:class:`RadiusAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute>`
    
    .. attribute:: password_policies
    
    	Configure password\-policy
    	**type**\:  :py:class:`PasswordPolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.PasswordPolicies>`
    
    .. attribute:: server_groups
    
    	AAA group definitions
    	**type**\:  :py:class:`ServerGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups>`
    
    .. attribute:: default_taskgroup
    
    	This class is used for setting the default taskgroup to be used for remote server authentication
    	**type**\: str
    
    .. attribute:: usernames
    
    	Configure local usernames
    	**type**\:  :py:class:`Usernames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usernames>`
    
    .. attribute:: taskgroups
    
    	Specify a taskgroup to inherit from
    	**type**\:  :py:class:`Taskgroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups>`
    
    .. attribute:: usergroups
    
    	Specify a Usergroup to inherit from
    	**type**\:  :py:class:`Usergroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups>`
    
    .. attribute:: radius
    
    	Remote Access Dial\-In User Service
    	**type**\:  :py:class:`Radius <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius>`
    
    .. attribute:: diameter
    
    	Diameter base protocol
    	**type**\:  :py:class:`Diameter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter>`
    
    .. attribute:: intercept
    
    	Enable LI RADIUS Feature
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: tacacs
    
    	Modify TACACS+ query parameters
    	**type**\:  :py:class:`Tacacs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs>`
    
    

    """

    _prefix = 'aaa-lib-cfg'
    _revision = '2017-11-14'

    def __init__(self):
        super(Aaa, self).__init__()
        self._top_entity = None

        self.yang_name = "aaa"
        self.yang_parent_name = "Cisco-IOS-XR-aaa-lib-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("accountings", ("accountings", Aaa.Accountings)), ("authorizations", ("authorizations", Aaa.Authorizations)), ("accounting-update", ("accounting_update", Aaa.AccountingUpdate)), ("banner", ("banner", Aaa.Banner)), ("authentications", ("authentications", Aaa.Authentications)), ("Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber", ("aaa_subscriber", Aaa.AaaSubscriber)), ("Cisco-IOS-XR-aaa-aaacore-cfg:aaa-mobile", ("aaa_mobile", Aaa.AaaMobile)), ("Cisco-IOS-XR-aaa-aaacore-cfg:aaa-dot1x", ("aaa_dot1x", Aaa.AaaDot1x)), ("Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute", ("radius_attribute", Aaa.RadiusAttribute)), ("Cisco-IOS-XR-aaa-locald-cfg:password-policies", ("password_policies", Aaa.PasswordPolicies)), ("Cisco-IOS-XR-aaa-locald-cfg:server-groups", ("server_groups", Aaa.ServerGroups)), ("Cisco-IOS-XR-aaa-locald-cfg:usernames", ("usernames", Aaa.Usernames)), ("Cisco-IOS-XR-aaa-locald-cfg:taskgroups", ("taskgroups", Aaa.Taskgroups)), ("Cisco-IOS-XR-aaa-locald-cfg:usergroups", ("usergroups", Aaa.Usergroups)), ("Cisco-IOS-XR-aaa-protocol-radius-cfg:radius", ("radius", Aaa.Radius)), ("Cisco-IOS-XR-aaa-diameter-cfg:diameter", ("diameter", Aaa.Diameter)), ("Cisco-IOS-XR-aaa-tacacs-cfg:tacacs", ("tacacs", Aaa.Tacacs))])
        self._leafs = OrderedDict([
            ('default_taskgroup', (YLeaf(YType.str, 'Cisco-IOS-XR-aaa-locald-cfg:default-taskgroup'), ['str'])),
            ('intercept', (YLeaf(YType.empty, 'Cisco-IOS-XR-aaa-li-cfg:intercept'), ['Empty'])),
        ])
        self.default_taskgroup = None
        self.intercept = None

        self.accountings = Aaa.Accountings()
        self.accountings.parent = self
        self._children_name_map["accountings"] = "accountings"

        self.authorizations = Aaa.Authorizations()
        self.authorizations.parent = self
        self._children_name_map["authorizations"] = "authorizations"

        self.accounting_update = None
        self._children_name_map["accounting_update"] = "accounting-update"

        self.banner = Aaa.Banner()
        self.banner.parent = self
        self._children_name_map["banner"] = "banner"

        self.authentications = Aaa.Authentications()
        self.authentications.parent = self
        self._children_name_map["authentications"] = "authentications"

        self.aaa_subscriber = Aaa.AaaSubscriber()
        self.aaa_subscriber.parent = self
        self._children_name_map["aaa_subscriber"] = "Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber"

        self.aaa_mobile = Aaa.AaaMobile()
        self.aaa_mobile.parent = self
        self._children_name_map["aaa_mobile"] = "Cisco-IOS-XR-aaa-aaacore-cfg:aaa-mobile"

        self.aaa_dot1x = Aaa.AaaDot1x()
        self.aaa_dot1x.parent = self
        self._children_name_map["aaa_dot1x"] = "Cisco-IOS-XR-aaa-aaacore-cfg:aaa-dot1x"

        self.radius_attribute = Aaa.RadiusAttribute()
        self.radius_attribute.parent = self
        self._children_name_map["radius_attribute"] = "Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute"

        self.password_policies = Aaa.PasswordPolicies()
        self.password_policies.parent = self
        self._children_name_map["password_policies"] = "Cisco-IOS-XR-aaa-locald-cfg:password-policies"

        self.server_groups = Aaa.ServerGroups()
        self.server_groups.parent = self
        self._children_name_map["server_groups"] = "Cisco-IOS-XR-aaa-locald-cfg:server-groups"

        self.usernames = Aaa.Usernames()
        self.usernames.parent = self
        self._children_name_map["usernames"] = "Cisco-IOS-XR-aaa-locald-cfg:usernames"

        self.taskgroups = Aaa.Taskgroups()
        self.taskgroups.parent = self
        self._children_name_map["taskgroups"] = "Cisco-IOS-XR-aaa-locald-cfg:taskgroups"

        self.usergroups = Aaa.Usergroups()
        self.usergroups.parent = self
        self._children_name_map["usergroups"] = "Cisco-IOS-XR-aaa-locald-cfg:usergroups"

        self.radius = Aaa.Radius()
        self.radius.parent = self
        self._children_name_map["radius"] = "Cisco-IOS-XR-aaa-protocol-radius-cfg:radius"

        self.diameter = Aaa.Diameter()
        self.diameter.parent = self
        self._children_name_map["diameter"] = "Cisco-IOS-XR-aaa-diameter-cfg:diameter"

        self.tacacs = Aaa.Tacacs()
        self.tacacs.parent = self
        self._children_name_map["tacacs"] = "Cisco-IOS-XR-aaa-tacacs-cfg:tacacs"
        self._segment_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Aaa, [u'default_taskgroup', 'intercept'], name, value)


    class Accountings(Entity):
        """
        AAA accounting
        
        .. attribute:: accounting
        
        	Configurations related to accounting
        	**type**\: list of  		 :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Accountings.Accounting>`
        
        

        """

        _prefix = 'aaa-lib-cfg'
        _revision = '2017-11-14'

        def __init__(self):
            super(Aaa.Accountings, self).__init__()

            self.yang_name = "accountings"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("accounting", ("accounting", Aaa.Accountings.Accounting))])
            self._leafs = OrderedDict()

            self.accounting = YList(self)
            self._segment_path = lambda: "accountings"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.Accountings, [], name, value)


        class Accounting(Entity):
            """
            Configurations related to accounting
            
            .. attribute:: type  (key)
            
            	exec\:Account exec sessions, commands\: Account CLI commands
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: listname  (key)
            
            	Named accounting list
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: rp_failover
            
            	rpfailover
            	**type**\:  :py:class:`AaaAccountingRpFailover <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaAccountingRpFailover>`
            
            .. attribute:: broadcast
            
            	Broadcast
            	**type**\:  :py:class:`AaaAccountingBroadcast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaAccountingBroadcast>`
            
            .. attribute:: type_xr
            
            	Stop only/Start Stop
            	**type**\:  :py:class:`AaaAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaAccounting>`
            
            .. attribute:: method1
            
            	Method Type
            	**type**\:  :py:class:`AaaMethodAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethodAccounting>`
            
            .. attribute:: method2
            
            	Method Type
            	**type**\:  :py:class:`AaaMethodAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethodAccounting>`
            
            .. attribute:: method3
            
            	Method Type
            	**type**\:  :py:class:`AaaMethodAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethodAccounting>`
            
            .. attribute:: method4
            
            	Method Type
            	**type**\:  :py:class:`AaaMethodAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethodAccounting>`
            
            .. attribute:: server_group_name1
            
            	Server group name
            	**type**\: str
            
            .. attribute:: server_group_name2
            
            	Server group name
            	**type**\: str
            
            .. attribute:: server_group_name3
            
            	Server group name
            	**type**\: str
            
            .. attribute:: server_group_name4
            
            	Server group name
            	**type**\: str
            
            

            """

            _prefix = 'aaa-lib-cfg'
            _revision = '2017-11-14'

            def __init__(self):
                super(Aaa.Accountings.Accounting, self).__init__()

                self.yang_name = "accounting"
                self.yang_parent_name = "accountings"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['type','listname']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('type', (YLeaf(YType.str, 'type'), ['str'])),
                    ('listname', (YLeaf(YType.str, 'listname'), ['str'])),
                    ('rp_failover', (YLeaf(YType.enumeration, 'rp-failover'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaAccountingRpFailover', '')])),
                    ('broadcast', (YLeaf(YType.enumeration, 'broadcast'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaAccountingBroadcast', '')])),
                    ('type_xr', (YLeaf(YType.enumeration, 'type-xr'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaAccounting', '')])),
                    ('method1', (YLeaf(YType.enumeration, 'method1'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethodAccounting', '')])),
                    ('method2', (YLeaf(YType.enumeration, 'method2'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethodAccounting', '')])),
                    ('method3', (YLeaf(YType.enumeration, 'method3'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethodAccounting', '')])),
                    ('method4', (YLeaf(YType.enumeration, 'method4'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethodAccounting', '')])),
                    ('server_group_name1', (YLeaf(YType.str, 'server-group-name1'), ['str'])),
                    ('server_group_name2', (YLeaf(YType.str, 'server-group-name2'), ['str'])),
                    ('server_group_name3', (YLeaf(YType.str, 'server-group-name3'), ['str'])),
                    ('server_group_name4', (YLeaf(YType.str, 'server-group-name4'), ['str'])),
                ])
                self.type = None
                self.listname = None
                self.rp_failover = None
                self.broadcast = None
                self.type_xr = None
                self.method1 = None
                self.method2 = None
                self.method3 = None
                self.method4 = None
                self.server_group_name1 = None
                self.server_group_name2 = None
                self.server_group_name3 = None
                self.server_group_name4 = None
                self._segment_path = lambda: "accounting" + "[type='" + str(self.type) + "']" + "[listname='" + str(self.listname) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/accountings/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Accountings.Accounting, [u'type', u'listname', u'rp_failover', u'broadcast', u'type_xr', u'method1', u'method2', u'method3', u'method4', u'server_group_name1', u'server_group_name2', u'server_group_name3', u'server_group_name4'], name, value)


    class Authorizations(Entity):
        """
        AAA authorization
        
        .. attribute:: authorization
        
        	Configurations related to authorization
        	**type**\: list of  		 :py:class:`Authorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Authorizations.Authorization>`
        
        

        """

        _prefix = 'aaa-lib-cfg'
        _revision = '2017-11-14'

        def __init__(self):
            super(Aaa.Authorizations, self).__init__()

            self.yang_name = "authorizations"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("authorization", ("authorization", Aaa.Authorizations.Authorization))])
            self._leafs = OrderedDict()

            self.authorization = YList(self)
            self._segment_path = lambda: "authorizations"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.Authorizations, [], name, value)


        class Authorization(Entity):
            """
            Configurations related to authorization
            
            .. attribute:: type  (key)
            
            	network\: Authorize IKE requests, commands\: Authorize CLI commands
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: listname  (key)
            
            	List name for AAA authorization
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: method1
            
            	Method Type
            	**type**\:  :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
            
            .. attribute:: method2
            
            	Method Type
            	**type**\:  :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
            
            .. attribute:: method3
            
            	Method Type
            	**type**\:  :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
            
            .. attribute:: method4
            
            	Method Type
            	**type**\:  :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
            
            .. attribute:: server_group_name1
            
            	Server group name
            	**type**\: str
            
            .. attribute:: server_group_name2
            
            	Server group name
            	**type**\: str
            
            .. attribute:: server_group_name3
            
            	Server group name
            	**type**\: str
            
            .. attribute:: server_group_name4
            
            	Server group name
            	**type**\: str
            
            

            """

            _prefix = 'aaa-lib-cfg'
            _revision = '2017-11-14'

            def __init__(self):
                super(Aaa.Authorizations.Authorization, self).__init__()

                self.yang_name = "authorization"
                self.yang_parent_name = "authorizations"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['type','listname']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('type', (YLeaf(YType.str, 'type'), ['str'])),
                    ('listname', (YLeaf(YType.str, 'listname'), ['str'])),
                    ('method1', (YLeaf(YType.enumeration, 'method1'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethod', '')])),
                    ('method2', (YLeaf(YType.enumeration, 'method2'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethod', '')])),
                    ('method3', (YLeaf(YType.enumeration, 'method3'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethod', '')])),
                    ('method4', (YLeaf(YType.enumeration, 'method4'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethod', '')])),
                    ('server_group_name1', (YLeaf(YType.str, 'server-group-name1'), ['str'])),
                    ('server_group_name2', (YLeaf(YType.str, 'server-group-name2'), ['str'])),
                    ('server_group_name3', (YLeaf(YType.str, 'server-group-name3'), ['str'])),
                    ('server_group_name4', (YLeaf(YType.str, 'server-group-name4'), ['str'])),
                ])
                self.type = None
                self.listname = None
                self.method1 = None
                self.method2 = None
                self.method3 = None
                self.method4 = None
                self.server_group_name1 = None
                self.server_group_name2 = None
                self.server_group_name3 = None
                self.server_group_name4 = None
                self._segment_path = lambda: "authorization" + "[type='" + str(self.type) + "']" + "[listname='" + str(self.listname) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/authorizations/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Authorizations.Authorization, [u'type', u'listname', u'method1', u'method2', u'method3', u'method4', u'server_group_name1', u'server_group_name2', u'server_group_name3', u'server_group_name4'], name, value)


    class AccountingUpdate(Entity):
        """
        Configuration related to 'update' accounting
        
        .. attribute:: type
        
        	newinfo/periodic
        	**type**\:  :py:class:`AaaAccountingUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaAccountingUpdate>`
        
        	**mandatory**\: True
        
        .. attribute:: periodic_interval
        
        	Periodic update interval in minutes
        	**type**\: int
        
        	**range:** 0..35791394
        
        	**units**\: minute
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'aaa-lib-cfg'
        _revision = '2017-11-14'

        def __init__(self):
            super(Aaa.AccountingUpdate, self).__init__()

            self.yang_name = "accounting-update"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaAccountingUpdate', '')])),
                ('periodic_interval', (YLeaf(YType.uint32, 'periodic-interval'), ['int'])),
            ])
            self.type = None
            self.periodic_interval = None
            self._segment_path = lambda: "accounting-update"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.AccountingUpdate, [u'type', u'periodic_interval'], name, value)


    class Banner(Entity):
        """
        AAA banner
        
        .. attribute:: login
        
        	AAA login banner
        	**type**\: str
        
        

        """

        _prefix = 'aaa-lib-cfg'
        _revision = '2017-11-14'

        def __init__(self):
            super(Aaa.Banner, self).__init__()

            self.yang_name = "banner"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('login', (YLeaf(YType.str, 'login'), ['str'])),
            ])
            self.login = None
            self._segment_path = lambda: "banner"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.Banner, [u'login'], name, value)


    class Authentications(Entity):
        """
        AAA authentication
        
        .. attribute:: authentication
        
        	Configurations related to authentication
        	**type**\: list of  		 :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Authentications.Authentication>`
        
        

        """

        _prefix = 'aaa-lib-cfg'
        _revision = '2017-11-14'

        def __init__(self):
            super(Aaa.Authentications, self).__init__()

            self.yang_name = "authentications"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("authentication", ("authentication", Aaa.Authentications.Authentication))])
            self._leafs = OrderedDict()

            self.authentication = YList(self)
            self._segment_path = lambda: "authentications"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.Authentications, [], name, value)


        class Authentication(Entity):
            """
            Configurations related to authentication
            
            .. attribute:: type  (key)
            
            	login\: Authenticate login sessions, ppp\: Authenticate ppp sessions
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: listname  (key)
            
            	List name for AAA authentication
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: method1
            
            	Method Type
            	**type**\:  :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
            
            .. attribute:: method2
            
            	Method Type
            	**type**\:  :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
            
            .. attribute:: method3
            
            	Method Type
            	**type**\:  :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
            
            .. attribute:: method4
            
            	Method Type
            	**type**\:  :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
            
            .. attribute:: server_group_name1
            
            	Server group name
            	**type**\: str
            
            .. attribute:: server_group_name2
            
            	Server group name
            	**type**\: str
            
            .. attribute:: server_group_name3
            
            	Server group name
            	**type**\: str
            
            .. attribute:: server_group_name4
            
            	Server group name
            	**type**\: str
            
            

            """

            _prefix = 'aaa-lib-cfg'
            _revision = '2017-11-14'

            def __init__(self):
                super(Aaa.Authentications.Authentication, self).__init__()

                self.yang_name = "authentication"
                self.yang_parent_name = "authentications"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['type','listname']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('type', (YLeaf(YType.str, 'type'), ['str'])),
                    ('listname', (YLeaf(YType.str, 'listname'), ['str'])),
                    ('method1', (YLeaf(YType.enumeration, 'method1'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethod', '')])),
                    ('method2', (YLeaf(YType.enumeration, 'method2'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethod', '')])),
                    ('method3', (YLeaf(YType.enumeration, 'method3'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethod', '')])),
                    ('method4', (YLeaf(YType.enumeration, 'method4'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethod', '')])),
                    ('server_group_name1', (YLeaf(YType.str, 'server-group-name1'), ['str'])),
                    ('server_group_name2', (YLeaf(YType.str, 'server-group-name2'), ['str'])),
                    ('server_group_name3', (YLeaf(YType.str, 'server-group-name3'), ['str'])),
                    ('server_group_name4', (YLeaf(YType.str, 'server-group-name4'), ['str'])),
                ])
                self.type = None
                self.listname = None
                self.method1 = None
                self.method2 = None
                self.method3 = None
                self.method4 = None
                self.server_group_name1 = None
                self.server_group_name2 = None
                self.server_group_name3 = None
                self.server_group_name4 = None
                self._segment_path = lambda: "authentication" + "[type='" + str(self.type) + "']" + "[listname='" + str(self.listname) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/authentications/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Authentications.Authentication, [u'type', u'listname', u'method1', u'method2', u'method3', u'method4', u'server_group_name1', u'server_group_name2', u'server_group_name3', u'server_group_name4'], name, value)


    class AaaSubscriber(Entity):
        """
        AAA subscriber
        
        .. attribute:: policy_if_authors
        
        	AAA authorization policy
        	**type**\:  :py:class:`PolicyIfAuthors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.PolicyIfAuthors>`
        
        .. attribute:: accountings
        
        	AAA accounting
        	**type**\:  :py:class:`Accountings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.Accountings>`
        
        .. attribute:: service_accounting
        
        	Set accounting parameters for Service
        	**type**\:  :py:class:`ServiceAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.ServiceAccounting>`
        
        .. attribute:: prepaid_authors
        
        	AAA authorization prepaid
        	**type**\:  :py:class:`PrepaidAuthors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.PrepaidAuthors>`
        
        .. attribute:: authorizations
        
        	AAA authorization
        	**type**\:  :py:class:`Authorizations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.Authorizations>`
        
        .. attribute:: authentications
        
        	AAA authentication
        	**type**\:  :py:class:`Authentications <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.Authentications>`
        
        

        """

        _prefix = 'aaa-aaacore-cfg'
        _revision = '2018-09-04'

        def __init__(self):
            super(Aaa.AaaSubscriber, self).__init__()

            self.yang_name = "aaa-subscriber"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("policy-if-authors", ("policy_if_authors", Aaa.AaaSubscriber.PolicyIfAuthors)), ("accountings", ("accountings", Aaa.AaaSubscriber.Accountings)), ("service-accounting", ("service_accounting", Aaa.AaaSubscriber.ServiceAccounting)), ("prepaid-authors", ("prepaid_authors", Aaa.AaaSubscriber.PrepaidAuthors)), ("authorizations", ("authorizations", Aaa.AaaSubscriber.Authorizations)), ("authentications", ("authentications", Aaa.AaaSubscriber.Authentications))])
            self._leafs = OrderedDict()

            self.policy_if_authors = Aaa.AaaSubscriber.PolicyIfAuthors()
            self.policy_if_authors.parent = self
            self._children_name_map["policy_if_authors"] = "policy-if-authors"

            self.accountings = Aaa.AaaSubscriber.Accountings()
            self.accountings.parent = self
            self._children_name_map["accountings"] = "accountings"

            self.service_accounting = Aaa.AaaSubscriber.ServiceAccounting()
            self.service_accounting.parent = self
            self._children_name_map["service_accounting"] = "service-accounting"

            self.prepaid_authors = Aaa.AaaSubscriber.PrepaidAuthors()
            self.prepaid_authors.parent = self
            self._children_name_map["prepaid_authors"] = "prepaid-authors"

            self.authorizations = Aaa.AaaSubscriber.Authorizations()
            self.authorizations.parent = self
            self._children_name_map["authorizations"] = "authorizations"

            self.authentications = Aaa.AaaSubscriber.Authentications()
            self.authentications.parent = self
            self._children_name_map["authentications"] = "authentications"
            self._segment_path = lambda: "Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.AaaSubscriber, [], name, value)


        class PolicyIfAuthors(Entity):
            """
            AAA authorization policy
            
            .. attribute:: policy_if_author
            
            	Configurations related to authorization
            	**type**\: list of  		 :py:class:`PolicyIfAuthor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.PolicyIfAuthors.PolicyIfAuthor>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2018-09-04'

            def __init__(self):
                super(Aaa.AaaSubscriber.PolicyIfAuthors, self).__init__()

                self.yang_name = "policy-if-authors"
                self.yang_parent_name = "aaa-subscriber"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("policy-if-author", ("policy_if_author", Aaa.AaaSubscriber.PolicyIfAuthors.PolicyIfAuthor))])
                self._leafs = OrderedDict()

                self.policy_if_author = YList(self)
                self._segment_path = lambda: "policy-if-authors"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.AaaSubscriber.PolicyIfAuthors, [], name, value)


            class PolicyIfAuthor(Entity):
                """
                Configurations related to authorization
                
                .. attribute:: type  (key)
                
                	Set authorization lists
                	**type**\: str
                
                	**pattern:** (subscriber)\|(service)\|(policy\-if)\|(prepaid)\|(dot1x)
                
                .. attribute:: listname  (key)
                
                	Named authorization list
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: method
                
                	Method Types
                	**type**\: list of   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
                
                .. attribute:: server_group_name
                
                	Server group names
                	**type**\: list of str
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2018-09-04'

                def __init__(self):
                    super(Aaa.AaaSubscriber.PolicyIfAuthors.PolicyIfAuthor, self).__init__()

                    self.yang_name = "policy-if-author"
                    self.yang_parent_name = "policy-if-authors"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['type','listname']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('type', (YLeaf(YType.str, 'type'), ['str'])),
                        ('listname', (YLeaf(YType.str, 'listname'), ['str'])),
                        ('method', (YLeafList(YType.enumeration, 'method'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethod', '')])),
                        ('server_group_name', (YLeafList(YType.str, 'server-group-name'), ['str'])),
                    ])
                    self.type = None
                    self.listname = None
                    self.method = []
                    self.server_group_name = []
                    self._segment_path = lambda: "policy-if-author" + "[type='" + str(self.type) + "']" + "[listname='" + str(self.listname) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/policy-if-authors/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.AaaSubscriber.PolicyIfAuthors.PolicyIfAuthor, ['type', 'listname', 'method', 'server_group_name'], name, value)


        class Accountings(Entity):
            """
            AAA accounting
            
            .. attribute:: accounting
            
            	Configurations related to accounting
            	**type**\: list of  		 :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.Accountings.Accounting>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2018-09-04'

            def __init__(self):
                super(Aaa.AaaSubscriber.Accountings, self).__init__()

                self.yang_name = "accountings"
                self.yang_parent_name = "aaa-subscriber"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("accounting", ("accounting", Aaa.AaaSubscriber.Accountings.Accounting))])
                self._leafs = OrderedDict()

                self.accounting = YList(self)
                self._segment_path = lambda: "accountings"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.AaaSubscriber.Accountings, [], name, value)


            class Accounting(Entity):
                """
                Configurations related to accounting
                
                .. attribute:: type  (key)
                
                	Set accounting lists
                	**type**\: str
                
                	**pattern:** (subscriber)\|(service)\|(policy\-if)\|(prepaid)\|(dot1x)
                
                .. attribute:: listname  (key)
                
                	Named accounting list
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: broadcast
                
                	Broadcast
                	**type**\:  :py:class:`AaaAccountingBroadcast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaAccountingBroadcast>`
                
                	**mandatory**\: True
                
                .. attribute:: method
                
                	Method Types
                	**type**\: list of   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
                
                .. attribute:: server_group_name
                
                	Server group names
                	**type**\: list of str
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2018-09-04'

                def __init__(self):
                    super(Aaa.AaaSubscriber.Accountings.Accounting, self).__init__()

                    self.yang_name = "accounting"
                    self.yang_parent_name = "accountings"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['type','listname']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('type', (YLeaf(YType.str, 'type'), ['str'])),
                        ('listname', (YLeaf(YType.str, 'listname'), ['str'])),
                        ('broadcast', (YLeaf(YType.enumeration, 'broadcast'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaAccountingBroadcast', '')])),
                        ('method', (YLeafList(YType.enumeration, 'method'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethod', '')])),
                        ('server_group_name', (YLeafList(YType.str, 'server-group-name'), ['str'])),
                    ])
                    self.type = None
                    self.listname = None
                    self.broadcast = None
                    self.method = []
                    self.server_group_name = []
                    self._segment_path = lambda: "accounting" + "[type='" + str(self.type) + "']" + "[listname='" + str(self.listname) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/accountings/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.AaaSubscriber.Accountings.Accounting, ['type', 'listname', 'broadcast', 'method', 'server_group_name'], name, value)


        class ServiceAccounting(Entity):
            """
            Set accounting parameters for Service
            
            .. attribute:: type
            
            	Send extended/brief service accounting records
            	**type**\:  :py:class:`AaaServiceAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_aaacore_cfg.AaaServiceAccounting>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2018-09-04'

            def __init__(self):
                super(Aaa.AaaSubscriber.ServiceAccounting, self).__init__()

                self.yang_name = "service-accounting"
                self.yang_parent_name = "aaa-subscriber"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_aaacore_cfg', 'AaaServiceAccounting', '')])),
                ])
                self.type = None
                self._segment_path = lambda: "service-accounting"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.AaaSubscriber.ServiceAccounting, ['type'], name, value)


        class PrepaidAuthors(Entity):
            """
            AAA authorization prepaid
            
            .. attribute:: prepaid_author
            
            	Configurations related to authorization
            	**type**\: list of  		 :py:class:`PrepaidAuthor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.PrepaidAuthors.PrepaidAuthor>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2018-09-04'

            def __init__(self):
                super(Aaa.AaaSubscriber.PrepaidAuthors, self).__init__()

                self.yang_name = "prepaid-authors"
                self.yang_parent_name = "aaa-subscriber"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("prepaid-author", ("prepaid_author", Aaa.AaaSubscriber.PrepaidAuthors.PrepaidAuthor))])
                self._leafs = OrderedDict()

                self.prepaid_author = YList(self)
                self._segment_path = lambda: "prepaid-authors"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.AaaSubscriber.PrepaidAuthors, [], name, value)


            class PrepaidAuthor(Entity):
                """
                Configurations related to authorization
                
                .. attribute:: type  (key)
                
                	Set authorization lists
                	**type**\: str
                
                	**pattern:** (subscriber)\|(service)\|(policy\-if)\|(prepaid)\|(dot1x)
                
                .. attribute:: listname  (key)
                
                	Named authorization list
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: method
                
                	Method Types
                	**type**\: list of   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
                
                .. attribute:: server_group_name
                
                	Server group names
                	**type**\: list of str
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2018-09-04'

                def __init__(self):
                    super(Aaa.AaaSubscriber.PrepaidAuthors.PrepaidAuthor, self).__init__()

                    self.yang_name = "prepaid-author"
                    self.yang_parent_name = "prepaid-authors"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['type','listname']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('type', (YLeaf(YType.str, 'type'), ['str'])),
                        ('listname', (YLeaf(YType.str, 'listname'), ['str'])),
                        ('method', (YLeafList(YType.enumeration, 'method'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethod', '')])),
                        ('server_group_name', (YLeafList(YType.str, 'server-group-name'), ['str'])),
                    ])
                    self.type = None
                    self.listname = None
                    self.method = []
                    self.server_group_name = []
                    self._segment_path = lambda: "prepaid-author" + "[type='" + str(self.type) + "']" + "[listname='" + str(self.listname) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/prepaid-authors/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.AaaSubscriber.PrepaidAuthors.PrepaidAuthor, ['type', 'listname', 'method', 'server_group_name'], name, value)


        class Authorizations(Entity):
            """
            AAA authorization
            
            .. attribute:: authorization
            
            	Configurations related to authorization
            	**type**\: list of  		 :py:class:`Authorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.Authorizations.Authorization>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2018-09-04'

            def __init__(self):
                super(Aaa.AaaSubscriber.Authorizations, self).__init__()

                self.yang_name = "authorizations"
                self.yang_parent_name = "aaa-subscriber"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("authorization", ("authorization", Aaa.AaaSubscriber.Authorizations.Authorization))])
                self._leafs = OrderedDict()

                self.authorization = YList(self)
                self._segment_path = lambda: "authorizations"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.AaaSubscriber.Authorizations, [], name, value)


            class Authorization(Entity):
                """
                Configurations related to authorization
                
                .. attribute:: type  (key)
                
                	Set authorization lists
                	**type**\: str
                
                	**pattern:** (subscriber)\|(service)\|(policy\-if)\|(prepaid)\|(dot1x)
                
                .. attribute:: listname  (key)
                
                	Named authorization list
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: method
                
                	Method Types
                	**type**\: list of   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
                
                .. attribute:: server_group_name
                
                	Server group names
                	**type**\: list of str
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2018-09-04'

                def __init__(self):
                    super(Aaa.AaaSubscriber.Authorizations.Authorization, self).__init__()

                    self.yang_name = "authorization"
                    self.yang_parent_name = "authorizations"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['type','listname']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('type', (YLeaf(YType.str, 'type'), ['str'])),
                        ('listname', (YLeaf(YType.str, 'listname'), ['str'])),
                        ('method', (YLeafList(YType.enumeration, 'method'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethod', '')])),
                        ('server_group_name', (YLeafList(YType.str, 'server-group-name'), ['str'])),
                    ])
                    self.type = None
                    self.listname = None
                    self.method = []
                    self.server_group_name = []
                    self._segment_path = lambda: "authorization" + "[type='" + str(self.type) + "']" + "[listname='" + str(self.listname) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/authorizations/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.AaaSubscriber.Authorizations.Authorization, ['type', 'listname', 'method', 'server_group_name'], name, value)


        class Authentications(Entity):
            """
            AAA authentication
            
            .. attribute:: authentication
            
            	Configurations related to authentication
            	**type**\: list of  		 :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaSubscriber.Authentications.Authentication>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2018-09-04'

            def __init__(self):
                super(Aaa.AaaSubscriber.Authentications, self).__init__()

                self.yang_name = "authentications"
                self.yang_parent_name = "aaa-subscriber"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("authentication", ("authentication", Aaa.AaaSubscriber.Authentications.Authentication))])
                self._leafs = OrderedDict()

                self.authentication = YList(self)
                self._segment_path = lambda: "authentications"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.AaaSubscriber.Authentications, [], name, value)


            class Authentication(Entity):
                """
                Configurations related to authentication
                
                .. attribute:: type  (key)
                
                	Set authentication lists
                	**type**\: str
                
                	**pattern:** (subscriber)\|(service)\|(policy\-if)\|(prepaid)\|(dot1x)
                
                .. attribute:: listname  (key)
                
                	Named authentication list
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: method
                
                	Method Types
                	**type**\: list of   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
                
                .. attribute:: server_group_name
                
                	Server group names
                	**type**\: list of str
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2018-09-04'

                def __init__(self):
                    super(Aaa.AaaSubscriber.Authentications.Authentication, self).__init__()

                    self.yang_name = "authentication"
                    self.yang_parent_name = "authentications"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['type','listname']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('type', (YLeaf(YType.str, 'type'), ['str'])),
                        ('listname', (YLeaf(YType.str, 'listname'), ['str'])),
                        ('method', (YLeafList(YType.enumeration, 'method'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethod', '')])),
                        ('server_group_name', (YLeafList(YType.str, 'server-group-name'), ['str'])),
                    ])
                    self.type = None
                    self.listname = None
                    self.method = []
                    self.server_group_name = []
                    self._segment_path = lambda: "authentication" + "[type='" + str(self.type) + "']" + "[listname='" + str(self.listname) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-subscriber/authentications/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.AaaSubscriber.Authentications.Authentication, ['type', 'listname', 'method', 'server_group_name'], name, value)


    class AaaMobile(Entity):
        """
        AAA Mobile
        
        .. attribute:: mobiles
        
        	AAA Mobile Accounting
        	**type**\:  :py:class:`Mobiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaMobile.Mobiles>`
        
        

        """

        _prefix = 'aaa-aaacore-cfg'
        _revision = '2018-09-04'

        def __init__(self):
            super(Aaa.AaaMobile, self).__init__()

            self.yang_name = "aaa-mobile"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mobiles", ("mobiles", Aaa.AaaMobile.Mobiles))])
            self._leafs = OrderedDict()

            self.mobiles = Aaa.AaaMobile.Mobiles()
            self.mobiles.parent = self
            self._children_name_map["mobiles"] = "mobiles"
            self._segment_path = lambda: "Cisco-IOS-XR-aaa-aaacore-cfg:aaa-mobile"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.AaaMobile, [], name, value)


        class Mobiles(Entity):
            """
            AAA Mobile Accounting
            
            .. attribute:: mobile
            
            	Configurations related to accounting
            	**type**\: list of  		 :py:class:`Mobile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaMobile.Mobiles.Mobile>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2018-09-04'

            def __init__(self):
                super(Aaa.AaaMobile.Mobiles, self).__init__()

                self.yang_name = "mobiles"
                self.yang_parent_name = "aaa-mobile"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("mobile", ("mobile", Aaa.AaaMobile.Mobiles.Mobile))])
                self._leafs = OrderedDict()

                self.mobile = YList(self)
                self._segment_path = lambda: "mobiles"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-mobile/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.AaaMobile.Mobiles, [], name, value)


            class Mobile(Entity):
                """
                Configurations related to accounting
                
                .. attribute:: listname  (key)
                
                	Named accounting list
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: broadcast
                
                	Broadcast
                	**type**\:  :py:class:`AaaAccountingBroadcast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaAccountingBroadcast>`
                
                	**mandatory**\: True
                
                .. attribute:: method
                
                	Method Types
                	**type**\: list of   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
                
                .. attribute:: server_group_name
                
                	Server group names
                	**type**\: list of str
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2018-09-04'

                def __init__(self):
                    super(Aaa.AaaMobile.Mobiles.Mobile, self).__init__()

                    self.yang_name = "mobile"
                    self.yang_parent_name = "mobiles"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['listname']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('listname', (YLeaf(YType.str, 'listname'), ['str'])),
                        ('broadcast', (YLeaf(YType.enumeration, 'broadcast'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaAccountingBroadcast', '')])),
                        ('method', (YLeafList(YType.enumeration, 'method'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethod', '')])),
                        ('server_group_name', (YLeafList(YType.str, 'server-group-name'), ['str'])),
                    ])
                    self.listname = None
                    self.broadcast = None
                    self.method = []
                    self.server_group_name = []
                    self._segment_path = lambda: "mobile" + "[listname='" + str(self.listname) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-mobile/mobiles/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.AaaMobile.Mobiles.Mobile, ['listname', 'broadcast', 'method', 'server_group_name'], name, value)


    class AaaDot1x(Entity):
        """
        AAA Dot1x
        
        .. attribute:: authentications
        
        	AAA authentication
        	**type**\:  :py:class:`Authentications <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaDot1x.Authentications>`
        
        

        """

        _prefix = 'aaa-aaacore-cfg'
        _revision = '2018-09-04'

        def __init__(self):
            super(Aaa.AaaDot1x, self).__init__()

            self.yang_name = "aaa-dot1x"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("authentications", ("authentications", Aaa.AaaDot1x.Authentications))])
            self._leafs = OrderedDict()

            self.authentications = Aaa.AaaDot1x.Authentications()
            self.authentications.parent = self
            self._children_name_map["authentications"] = "authentications"
            self._segment_path = lambda: "Cisco-IOS-XR-aaa-aaacore-cfg:aaa-dot1x"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.AaaDot1x, [], name, value)


        class Authentications(Entity):
            """
            AAA authentication
            
            .. attribute:: authentication
            
            	Configurations related to authentication
            	**type**\: list of  		 :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.AaaDot1x.Authentications.Authentication>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2018-09-04'

            def __init__(self):
                super(Aaa.AaaDot1x.Authentications, self).__init__()

                self.yang_name = "authentications"
                self.yang_parent_name = "aaa-dot1x"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("authentication", ("authentication", Aaa.AaaDot1x.Authentications.Authentication))])
                self._leafs = OrderedDict()

                self.authentication = YList(self)
                self._segment_path = lambda: "authentications"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-dot1x/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.AaaDot1x.Authentications, [], name, value)


            class Authentication(Entity):
                """
                Configurations related to authentication
                
                .. attribute:: type  (key)
                
                	Set authentication lists
                	**type**\: str
                
                	**pattern:** (subscriber)\|(service)\|(policy\-if)\|(prepaid)\|(dot1x)
                
                .. attribute:: listname  (key)
                
                	Named authentication list
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: method
                
                	Method Types
                	**type**\: list of   :py:class:`AaaMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes.AaaMethod>`
                
                .. attribute:: server_group_name
                
                	Server group names
                	**type**\: list of str
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2018-09-04'

                def __init__(self):
                    super(Aaa.AaaDot1x.Authentications.Authentication, self).__init__()

                    self.yang_name = "authentication"
                    self.yang_parent_name = "authentications"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['type','listname']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('type', (YLeaf(YType.str, 'type'), ['str'])),
                        ('listname', (YLeaf(YType.str, 'listname'), ['str'])),
                        ('method', (YLeafList(YType.enumeration, 'method'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethod', '')])),
                        ('server_group_name', (YLeafList(YType.str, 'server-group-name'), ['str'])),
                    ])
                    self.type = None
                    self.listname = None
                    self.method = []
                    self.server_group_name = []
                    self._segment_path = lambda: "authentication" + "[type='" + str(self.type) + "']" + "[listname='" + str(self.listname) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:aaa-dot1x/authentications/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.AaaDot1x.Authentications.Authentication, ['type', 'listname', 'method', 'server_group_name'], name, value)


    class RadiusAttribute(Entity):
        """
        AAA RADIUS attribute configurations
        
        .. attribute:: nas_port_id
        
        	AAA nas\-port\-id attribute
        	**type**\:  :py:class:`NasPortId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.NasPortId>`
        
        .. attribute:: calling_station
        
        	AAA calling station id attribute
        	**type**\:  :py:class:`CallingStation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.CallingStation>`
        
        .. attribute:: called_station
        
        	AAA called station id attribute
        	**type**\:  :py:class:`CalledStation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.CalledStation>`
        
        .. attribute:: nas_port
        
        	AAA nas\-port\-id attribute
        	**type**\:  :py:class:`NasPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.NasPort>`
        
        .. attribute:: format_others
        
        	AAA nas\-port\-id attribute format
        	**type**\:  :py:class:`FormatOthers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.FormatOthers>`
        
        

        """

        _prefix = 'aaa-aaacore-cfg'
        _revision = '2018-09-04'

        def __init__(self):
            super(Aaa.RadiusAttribute, self).__init__()

            self.yang_name = "radius-attribute"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("nas-port-id", ("nas_port_id", Aaa.RadiusAttribute.NasPortId)), ("calling-station", ("calling_station", Aaa.RadiusAttribute.CallingStation)), ("called-station", ("called_station", Aaa.RadiusAttribute.CalledStation)), ("nas-port", ("nas_port", Aaa.RadiusAttribute.NasPort)), ("format-others", ("format_others", Aaa.RadiusAttribute.FormatOthers))])
            self._leafs = OrderedDict()

            self.nas_port_id = Aaa.RadiusAttribute.NasPortId()
            self.nas_port_id.parent = self
            self._children_name_map["nas_port_id"] = "nas-port-id"

            self.calling_station = Aaa.RadiusAttribute.CallingStation()
            self.calling_station.parent = self
            self._children_name_map["calling_station"] = "calling-station"

            self.called_station = Aaa.RadiusAttribute.CalledStation()
            self.called_station.parent = self
            self._children_name_map["called_station"] = "called-station"

            self.nas_port = Aaa.RadiusAttribute.NasPort()
            self.nas_port.parent = self
            self._children_name_map["nas_port"] = "nas-port"

            self.format_others = Aaa.RadiusAttribute.FormatOthers()
            self.format_others.parent = self
            self._children_name_map["format_others"] = "format-others"
            self._segment_path = lambda: "Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.RadiusAttribute, [], name, value)


        class NasPortId(Entity):
            """
            AAA nas\-port\-id attribute
            
            .. attribute:: formats
            
            	AAA nas\-port\-id attribute format
            	**type**\:  :py:class:`Formats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.NasPortId.Formats>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2018-09-04'

            def __init__(self):
                super(Aaa.RadiusAttribute.NasPortId, self).__init__()

                self.yang_name = "nas-port-id"
                self.yang_parent_name = "radius-attribute"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("formats", ("formats", Aaa.RadiusAttribute.NasPortId.Formats))])
                self._leafs = OrderedDict()

                self.formats = Aaa.RadiusAttribute.NasPortId.Formats()
                self.formats.parent = self
                self._children_name_map["formats"] = "formats"
                self._segment_path = lambda: "nas-port-id"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.RadiusAttribute.NasPortId, [], name, value)


            class Formats(Entity):
                """
                AAA nas\-port\-id attribute format
                
                .. attribute:: format
                
                	nas\-port\-id attribute format
                	**type**\: list of  		 :py:class:`Format <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.NasPortId.Formats.Format>`
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2018-09-04'

                def __init__(self):
                    super(Aaa.RadiusAttribute.NasPortId.Formats, self).__init__()

                    self.yang_name = "formats"
                    self.yang_parent_name = "nas-port-id"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("format", ("format", Aaa.RadiusAttribute.NasPortId.Formats.Format))])
                    self._leafs = OrderedDict()

                    self.format = YList(self)
                    self._segment_path = lambda: "formats"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/nas-port-id/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.RadiusAttribute.NasPortId.Formats, [], name, value)


                class Format(Entity):
                    """
                    nas\-port\-id attribute format
                    
                    .. attribute:: type  (key)
                    
                    	Nas\-Port\-Type value to apply format name on
                    	**type**\: int
                    
                    	**range:** 0..45
                    
                    .. attribute:: format_name
                    
                    	AAA nas\-port attribute format
                    	**type**\: str
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'aaa-aaacore-cfg'
                    _revision = '2018-09-04'

                    def __init__(self):
                        super(Aaa.RadiusAttribute.NasPortId.Formats.Format, self).__init__()

                        self.yang_name = "format"
                        self.yang_parent_name = "formats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['type']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('type', (YLeaf(YType.uint32, 'type'), ['int'])),
                            ('format_name', (YLeaf(YType.str, 'format-name'), ['str'])),
                        ])
                        self.type = None
                        self.format_name = None
                        self._segment_path = lambda: "format" + "[type='" + str(self.type) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/nas-port-id/formats/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.RadiusAttribute.NasPortId.Formats.Format, ['type', 'format_name'], name, value)


        class CallingStation(Entity):
            """
            AAA calling station id attribute
            
            .. attribute:: formats
            
            	AAA nas\-port\-id attribute format
            	**type**\:  :py:class:`Formats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.CallingStation.Formats>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2018-09-04'

            def __init__(self):
                super(Aaa.RadiusAttribute.CallingStation, self).__init__()

                self.yang_name = "calling-station"
                self.yang_parent_name = "radius-attribute"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("formats", ("formats", Aaa.RadiusAttribute.CallingStation.Formats))])
                self._leafs = OrderedDict()

                self.formats = Aaa.RadiusAttribute.CallingStation.Formats()
                self.formats.parent = self
                self._children_name_map["formats"] = "formats"
                self._segment_path = lambda: "calling-station"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.RadiusAttribute.CallingStation, [], name, value)


            class Formats(Entity):
                """
                AAA nas\-port\-id attribute format
                
                .. attribute:: format
                
                	nas\-port\-id attribute format
                	**type**\: list of  		 :py:class:`Format <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.CallingStation.Formats.Format>`
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2018-09-04'

                def __init__(self):
                    super(Aaa.RadiusAttribute.CallingStation.Formats, self).__init__()

                    self.yang_name = "formats"
                    self.yang_parent_name = "calling-station"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("format", ("format", Aaa.RadiusAttribute.CallingStation.Formats.Format))])
                    self._leafs = OrderedDict()

                    self.format = YList(self)
                    self._segment_path = lambda: "formats"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/calling-station/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.RadiusAttribute.CallingStation.Formats, [], name, value)


                class Format(Entity):
                    """
                    nas\-port\-id attribute format
                    
                    .. attribute:: type  (key)
                    
                    	Nas\-Port\-Type value to apply format name on
                    	**type**\: int
                    
                    	**range:** 0..45
                    
                    .. attribute:: format_name
                    
                    	AAA nas\-port attribute format
                    	**type**\: str
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'aaa-aaacore-cfg'
                    _revision = '2018-09-04'

                    def __init__(self):
                        super(Aaa.RadiusAttribute.CallingStation.Formats.Format, self).__init__()

                        self.yang_name = "format"
                        self.yang_parent_name = "formats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['type']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('type', (YLeaf(YType.uint32, 'type'), ['int'])),
                            ('format_name', (YLeaf(YType.str, 'format-name'), ['str'])),
                        ])
                        self.type = None
                        self.format_name = None
                        self._segment_path = lambda: "format" + "[type='" + str(self.type) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/calling-station/formats/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.RadiusAttribute.CallingStation.Formats.Format, ['type', 'format_name'], name, value)


        class CalledStation(Entity):
            """
            AAA called station id attribute
            
            .. attribute:: formats
            
            	AAA nas\-port\-id attribute format
            	**type**\:  :py:class:`Formats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.CalledStation.Formats>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2018-09-04'

            def __init__(self):
                super(Aaa.RadiusAttribute.CalledStation, self).__init__()

                self.yang_name = "called-station"
                self.yang_parent_name = "radius-attribute"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("formats", ("formats", Aaa.RadiusAttribute.CalledStation.Formats))])
                self._leafs = OrderedDict()

                self.formats = Aaa.RadiusAttribute.CalledStation.Formats()
                self.formats.parent = self
                self._children_name_map["formats"] = "formats"
                self._segment_path = lambda: "called-station"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.RadiusAttribute.CalledStation, [], name, value)


            class Formats(Entity):
                """
                AAA nas\-port\-id attribute format
                
                .. attribute:: format
                
                	nas\-port\-id attribute format
                	**type**\: list of  		 :py:class:`Format <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.CalledStation.Formats.Format>`
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2018-09-04'

                def __init__(self):
                    super(Aaa.RadiusAttribute.CalledStation.Formats, self).__init__()

                    self.yang_name = "formats"
                    self.yang_parent_name = "called-station"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("format", ("format", Aaa.RadiusAttribute.CalledStation.Formats.Format))])
                    self._leafs = OrderedDict()

                    self.format = YList(self)
                    self._segment_path = lambda: "formats"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/called-station/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.RadiusAttribute.CalledStation.Formats, [], name, value)


                class Format(Entity):
                    """
                    nas\-port\-id attribute format
                    
                    .. attribute:: type  (key)
                    
                    	Nas\-Port\-Type value to apply format name on
                    	**type**\: int
                    
                    	**range:** 0..45
                    
                    .. attribute:: format_name
                    
                    	AAA nas\-port attribute format
                    	**type**\: str
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'aaa-aaacore-cfg'
                    _revision = '2018-09-04'

                    def __init__(self):
                        super(Aaa.RadiusAttribute.CalledStation.Formats.Format, self).__init__()

                        self.yang_name = "format"
                        self.yang_parent_name = "formats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['type']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('type', (YLeaf(YType.uint32, 'type'), ['int'])),
                            ('format_name', (YLeaf(YType.str, 'format-name'), ['str'])),
                        ])
                        self.type = None
                        self.format_name = None
                        self._segment_path = lambda: "format" + "[type='" + str(self.type) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/called-station/formats/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.RadiusAttribute.CalledStation.Formats.Format, ['type', 'format_name'], name, value)


        class NasPort(Entity):
            """
            AAA nas\-port\-id attribute
            
            .. attribute:: format_extendeds
            
            	AAA nas\-port\-id attribute format
            	**type**\:  :py:class:`FormatExtendeds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.NasPort.FormatExtendeds>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2018-09-04'

            def __init__(self):
                super(Aaa.RadiusAttribute.NasPort, self).__init__()

                self.yang_name = "nas-port"
                self.yang_parent_name = "radius-attribute"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("format-extendeds", ("format_extendeds", Aaa.RadiusAttribute.NasPort.FormatExtendeds))])
                self._leafs = OrderedDict()

                self.format_extendeds = Aaa.RadiusAttribute.NasPort.FormatExtendeds()
                self.format_extendeds.parent = self
                self._children_name_map["format_extendeds"] = "format-extendeds"
                self._segment_path = lambda: "nas-port"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.RadiusAttribute.NasPort, [], name, value)


            class FormatExtendeds(Entity):
                """
                AAA nas\-port\-id attribute format
                
                .. attribute:: format_extended
                
                	nas\-port\-id extended attribute
                	**type**\: list of  		 :py:class:`FormatExtended <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.NasPort.FormatExtendeds.FormatExtended>`
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2018-09-04'

                def __init__(self):
                    super(Aaa.RadiusAttribute.NasPort.FormatExtendeds, self).__init__()

                    self.yang_name = "format-extendeds"
                    self.yang_parent_name = "nas-port"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("format-extended", ("format_extended", Aaa.RadiusAttribute.NasPort.FormatExtendeds.FormatExtended))])
                    self._leafs = OrderedDict()

                    self.format_extended = YList(self)
                    self._segment_path = lambda: "format-extendeds"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/nas-port/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.RadiusAttribute.NasPort.FormatExtendeds, [], name, value)


                class FormatExtended(Entity):
                    """
                    nas\-port\-id extended attribute
                    
                    .. attribute:: value  (key)
                    
                    	format type
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: type  (key)
                    
                    	AAA nas\-port attribute format
                    	**type**\: int
                    
                    	**range:** 0..45
                    
                    .. attribute:: format_identifier
                    
                    	A 32 character string representing the format to be used
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'aaa-aaacore-cfg'
                    _revision = '2018-09-04'

                    def __init__(self):
                        super(Aaa.RadiusAttribute.NasPort.FormatExtendeds.FormatExtended, self).__init__()

                        self.yang_name = "format-extended"
                        self.yang_parent_name = "format-extendeds"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['value','type']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('value', (YLeaf(YType.str, 'value'), ['str'])),
                            ('type', (YLeaf(YType.uint32, 'type'), ['int'])),
                            ('format_identifier', (YLeaf(YType.str, 'format-identifier'), ['str'])),
                        ])
                        self.value = None
                        self.type = None
                        self.format_identifier = None
                        self._segment_path = lambda: "format-extended" + "[value='" + str(self.value) + "']" + "[type='" + str(self.type) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/nas-port/format-extendeds/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.RadiusAttribute.NasPort.FormatExtendeds.FormatExtended, ['value', 'type', 'format_identifier'], name, value)


        class FormatOthers(Entity):
            """
            AAA nas\-port\-id attribute format
            
            .. attribute:: format_other
            
            	Other configs
            	**type**\: list of  		 :py:class:`FormatOther <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.RadiusAttribute.FormatOthers.FormatOther>`
            
            

            """

            _prefix = 'aaa-aaacore-cfg'
            _revision = '2018-09-04'

            def __init__(self):
                super(Aaa.RadiusAttribute.FormatOthers, self).__init__()

                self.yang_name = "format-others"
                self.yang_parent_name = "radius-attribute"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("format-other", ("format_other", Aaa.RadiusAttribute.FormatOthers.FormatOther))])
                self._leafs = OrderedDict()

                self.format_other = YList(self)
                self._segment_path = lambda: "format-others"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.RadiusAttribute.FormatOthers, [], name, value)


            class FormatOther(Entity):
                """
                Other configs
                
                .. attribute:: nas_port_type_name  (key)
                
                	Nas\-Port\-Type value to apply format name on
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: attribute_config1
                
                	Argument1
                	**type**\: str
                
                .. attribute:: attribute_config2
                
                	Argument2
                	**type**\: str
                
                .. attribute:: attribute_config3
                
                	Argument3
                	**type**\: str
                
                .. attribute:: attribute_config4
                
                	Argument4
                	**type**\: str
                
                .. attribute:: attribute_config5
                
                	Argument5
                	**type**\: str
                
                .. attribute:: attribute_config6
                
                	Argument6
                	**type**\: str
                
                .. attribute:: attribute_config7
                
                	Argument7
                	**type**\: str
                
                .. attribute:: attribute_config8
                
                	Argument8
                	**type**\: str
                
                .. attribute:: attribute_config9
                
                	Argument9
                	**type**\: str
                
                .. attribute:: attribute_config10
                
                	Argument10
                	**type**\: str
                
                .. attribute:: attribute_config11
                
                	Argument11
                	**type**\: str
                
                .. attribute:: attribute_config12
                
                	Argument12
                	**type**\: str
                
                .. attribute:: attribute_config13
                
                	Argument13
                	**type**\: str
                
                .. attribute:: attribute_config14
                
                	Argument14
                	**type**\: str
                
                .. attribute:: attribute_config15
                
                	Argument15
                	**type**\: str
                
                .. attribute:: attribute_config16
                
                	Argument16
                	**type**\: str
                
                .. attribute:: attribute_config17
                
                	Argument17
                	**type**\: str
                
                .. attribute:: attribute_config18
                
                	Argument18
                	**type**\: str
                
                .. attribute:: attribute_config19
                
                	Argument19
                	**type**\: int
                
                	**range:** 1..253
                
                

                """

                _prefix = 'aaa-aaacore-cfg'
                _revision = '2018-09-04'

                def __init__(self):
                    super(Aaa.RadiusAttribute.FormatOthers.FormatOther, self).__init__()

                    self.yang_name = "format-other"
                    self.yang_parent_name = "format-others"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['nas_port_type_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('nas_port_type_name', (YLeaf(YType.str, 'nas-port-type-name'), ['str'])),
                        ('attribute_config1', (YLeaf(YType.str, 'attribute-config1'), ['str'])),
                        ('attribute_config2', (YLeaf(YType.str, 'attribute-config2'), ['str'])),
                        ('attribute_config3', (YLeaf(YType.str, 'attribute-config3'), ['str'])),
                        ('attribute_config4', (YLeaf(YType.str, 'attribute-config4'), ['str'])),
                        ('attribute_config5', (YLeaf(YType.str, 'attribute-config5'), ['str'])),
                        ('attribute_config6', (YLeaf(YType.str, 'attribute-config6'), ['str'])),
                        ('attribute_config7', (YLeaf(YType.str, 'attribute-config7'), ['str'])),
                        ('attribute_config8', (YLeaf(YType.str, 'attribute-config8'), ['str'])),
                        ('attribute_config9', (YLeaf(YType.str, 'attribute-config9'), ['str'])),
                        ('attribute_config10', (YLeaf(YType.str, 'attribute-config10'), ['str'])),
                        ('attribute_config11', (YLeaf(YType.str, 'attribute-config11'), ['str'])),
                        ('attribute_config12', (YLeaf(YType.str, 'attribute-config12'), ['str'])),
                        ('attribute_config13', (YLeaf(YType.str, 'attribute-config13'), ['str'])),
                        ('attribute_config14', (YLeaf(YType.str, 'attribute-config14'), ['str'])),
                        ('attribute_config15', (YLeaf(YType.str, 'attribute-config15'), ['str'])),
                        ('attribute_config16', (YLeaf(YType.str, 'attribute-config16'), ['str'])),
                        ('attribute_config17', (YLeaf(YType.str, 'attribute-config17'), ['str'])),
                        ('attribute_config18', (YLeaf(YType.str, 'attribute-config18'), ['str'])),
                        ('attribute_config19', (YLeaf(YType.uint32, 'attribute-config19'), ['int'])),
                    ])
                    self.nas_port_type_name = None
                    self.attribute_config1 = None
                    self.attribute_config2 = None
                    self.attribute_config3 = None
                    self.attribute_config4 = None
                    self.attribute_config5 = None
                    self.attribute_config6 = None
                    self.attribute_config7 = None
                    self.attribute_config8 = None
                    self.attribute_config9 = None
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
                    self._segment_path = lambda: "format-other" + "[nas-port-type-name='" + str(self.nas_port_type_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-aaacore-cfg:radius-attribute/format-others/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.RadiusAttribute.FormatOthers.FormatOther, ['nas_port_type_name', 'attribute_config1', 'attribute_config2', 'attribute_config3', 'attribute_config4', 'attribute_config5', 'attribute_config6', 'attribute_config7', 'attribute_config8', 'attribute_config9', 'attribute_config10', 'attribute_config11', 'attribute_config12', 'attribute_config13', 'attribute_config14', 'attribute_config15', 'attribute_config16', 'attribute_config17', 'attribute_config18', 'attribute_config19'], name, value)


    class PasswordPolicies(Entity):
        """
        Configure password\-policy
        
        .. attribute:: password_policy
        
        	Password Policy name
        	**type**\: list of  		 :py:class:`PasswordPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.PasswordPolicies.PasswordPolicy>`
        
        

        """

        _prefix = 'aaa-locald-cfg'
        _revision = '2018-06-04'

        def __init__(self):
            super(Aaa.PasswordPolicies, self).__init__()

            self.yang_name = "password-policies"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("password-policy", ("password_policy", Aaa.PasswordPolicies.PasswordPolicy))])
            self._leafs = OrderedDict()

            self.password_policy = YList(self)
            self._segment_path = lambda: "Cisco-IOS-XR-aaa-locald-cfg:password-policies"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.PasswordPolicies, [], name, value)


        class PasswordPolicy(Entity):
            """
            Password Policy name
            
            .. attribute:: name  (key)
            
            	Password Policy name
            	**type**\: str
            
            	**length:** 1..252
            
            .. attribute:: lifetime
            
            	Liftime of the password
            	**type**\:  :py:class:`Lifetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.PasswordPolicies.PasswordPolicy.Lifetime>`
            
            .. attribute:: lockout_time
            
            	Lockout time for the maximum authentication failures
            	**type**\:  :py:class:`LockoutTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.PasswordPolicies.PasswordPolicy.LockoutTime>`
            
            .. attribute:: lower_case
            
            	Number of lower\-case characters
            	**type**\: int
            
            	**range:** 0..253
            
            .. attribute:: upper_case
            
            	Number of upper\-case characters
            	**type**\: int
            
            	**range:** 0..253
            
            .. attribute:: max_length
            
            	Maximum length of the password
            	**type**\: int
            
            	**range:** 2..253
            
            .. attribute:: min_char_change
            
            	Number of characters change required between old and new passwords
            	**type**\: int
            
            	**range:** 0..253
            
            .. attribute:: special_char
            
            	Number of special characters
            	**type**\: int
            
            	**range:** 0..253
            
            .. attribute:: numeric
            
            	Number of numeric characters
            	**type**\: int
            
            	**range:** 0..253
            
            .. attribute:: min_length
            
            	Minimum length of the password
            	**type**\: int
            
            	**range:** 2..253
            
            .. attribute:: authen_max_attempts
            
            	Number of maximum authentication attempts
            	**type**\: int
            
            	**range:** 1..24
            
            

            """

            _prefix = 'aaa-locald-cfg'
            _revision = '2018-06-04'

            def __init__(self):
                super(Aaa.PasswordPolicies.PasswordPolicy, self).__init__()

                self.yang_name = "password-policy"
                self.yang_parent_name = "password-policies"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("lifetime", ("lifetime", Aaa.PasswordPolicies.PasswordPolicy.Lifetime)), ("lockout-time", ("lockout_time", Aaa.PasswordPolicies.PasswordPolicy.LockoutTime))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('lower_case', (YLeaf(YType.uint32, 'lower-case'), ['int'])),
                    ('upper_case', (YLeaf(YType.uint32, 'upper-case'), ['int'])),
                    ('max_length', (YLeaf(YType.uint32, 'max-length'), ['int'])),
                    ('min_char_change', (YLeaf(YType.uint32, 'min-char-change'), ['int'])),
                    ('special_char', (YLeaf(YType.uint32, 'special-char'), ['int'])),
                    ('numeric', (YLeaf(YType.uint32, 'numeric'), ['int'])),
                    ('min_length', (YLeaf(YType.uint32, 'min-length'), ['int'])),
                    ('authen_max_attempts', (YLeaf(YType.uint32, 'authen-max-attempts'), ['int'])),
                ])
                self.name = None
                self.lower_case = None
                self.upper_case = None
                self.max_length = None
                self.min_char_change = None
                self.special_char = None
                self.numeric = None
                self.min_length = None
                self.authen_max_attempts = None

                self.lifetime = Aaa.PasswordPolicies.PasswordPolicy.Lifetime()
                self.lifetime.parent = self
                self._children_name_map["lifetime"] = "lifetime"

                self.lockout_time = Aaa.PasswordPolicies.PasswordPolicy.LockoutTime()
                self.lockout_time.parent = self
                self._children_name_map["lockout_time"] = "lockout-time"
                self._segment_path = lambda: "password-policy" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:password-policies/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.PasswordPolicies.PasswordPolicy, [u'name', u'lower_case', u'upper_case', u'max_length', u'min_char_change', u'special_char', u'numeric', u'min_length', u'authen_max_attempts'], name, value)


            class Lifetime(Entity):
                """
                Liftime of the password
                
                .. attribute:: years
                
                	Number of years
                	**type**\: int
                
                	**range:** 0..99
                
                .. attribute:: months
                
                	Number of months
                	**type**\: int
                
                	**range:** 0..11
                
                .. attribute:: hours
                
                	Number of hours
                	**type**\: int
                
                	**range:** 0..23
                
                	**units**\: hour
                
                .. attribute:: minutes
                
                	Number of minutes
                	**type**\: int
                
                	**range:** 0..59
                
                	**units**\: minute
                
                .. attribute:: seconds
                
                	Number of seconds
                	**type**\: int
                
                	**range:** 30..59
                
                	**units**\: second
                
                .. attribute:: days
                
                	Number of days
                	**type**\: int
                
                	**range:** 0..30
                
                	**units**\: day
                
                

                """

                _prefix = 'aaa-locald-cfg'
                _revision = '2018-06-04'

                def __init__(self):
                    super(Aaa.PasswordPolicies.PasswordPolicy.Lifetime, self).__init__()

                    self.yang_name = "lifetime"
                    self.yang_parent_name = "password-policy"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('years', (YLeaf(YType.uint32, 'years'), ['int'])),
                        ('months', (YLeaf(YType.uint32, 'months'), ['int'])),
                        ('hours', (YLeaf(YType.uint32, 'hours'), ['int'])),
                        ('minutes', (YLeaf(YType.uint32, 'minutes'), ['int'])),
                        ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                        ('days', (YLeaf(YType.uint32, 'days'), ['int'])),
                    ])
                    self.years = None
                    self.months = None
                    self.hours = None
                    self.minutes = None
                    self.seconds = None
                    self.days = None
                    self._segment_path = lambda: "lifetime"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.PasswordPolicies.PasswordPolicy.Lifetime, [u'years', u'months', u'hours', u'minutes', u'seconds', u'days'], name, value)


            class LockoutTime(Entity):
                """
                Lockout time for the maximum authentication
                failures
                
                .. attribute:: hours
                
                	Number of hours
                	**type**\: int
                
                	**range:** 0..23
                
                	**units**\: hour
                
                .. attribute:: minutes
                
                	Number of minutes
                	**type**\: int
                
                	**range:** 0..59
                
                	**units**\: minute
                
                .. attribute:: seconds
                
                	Number of seconds
                	**type**\: int
                
                	**range:** 0..59
                
                	**units**\: second
                
                .. attribute:: days
                
                	Number of days
                	**type**\: int
                
                	**range:** 0..255
                
                	**units**\: day
                
                

                """

                _prefix = 'aaa-locald-cfg'
                _revision = '2018-06-04'

                def __init__(self):
                    super(Aaa.PasswordPolicies.PasswordPolicy.LockoutTime, self).__init__()

                    self.yang_name = "lockout-time"
                    self.yang_parent_name = "password-policy"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('hours', (YLeaf(YType.uint32, 'hours'), ['int'])),
                        ('minutes', (YLeaf(YType.uint32, 'minutes'), ['int'])),
                        ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                        ('days', (YLeaf(YType.uint32, 'days'), ['int'])),
                    ])
                    self.hours = None
                    self.minutes = None
                    self.seconds = None
                    self.days = None
                    self._segment_path = lambda: "lockout-time"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.PasswordPolicies.PasswordPolicy.LockoutTime, [u'hours', u'minutes', u'seconds', u'days'], name, value)


    class ServerGroups(Entity):
        """
        AAA group definitions
        
        .. attribute:: radius_server_groups
        
        	RADIUS server group definition
        	**type**\:  :py:class:`RadiusServerGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups>`
        
        .. attribute:: diameter_server_groups
        
        	DIAMETER server group definition
        	**type**\:  :py:class:`DiameterServerGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.DiameterServerGroups>`
        
        .. attribute:: tacacs_server_groups
        
        	TACACS+ server\-group definition
        	**type**\:  :py:class:`TacacsServerGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups>`
        
        

        """

        _prefix = 'aaa-locald-cfg'
        _revision = '2018-06-04'

        def __init__(self):
            super(Aaa.ServerGroups, self).__init__()

            self.yang_name = "server-groups"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("Cisco-IOS-XR-aaa-protocol-radius-cfg:radius-server-groups", ("radius_server_groups", Aaa.ServerGroups.RadiusServerGroups)), ("Cisco-IOS-XR-aaa-diameter-cfg:diameter-server-groups", ("diameter_server_groups", Aaa.ServerGroups.DiameterServerGroups)), ("Cisco-IOS-XR-aaa-tacacs-cfg:tacacs-server-groups", ("tacacs_server_groups", Aaa.ServerGroups.TacacsServerGroups))])
            self._leafs = OrderedDict()

            self.radius_server_groups = Aaa.ServerGroups.RadiusServerGroups()
            self.radius_server_groups.parent = self
            self._children_name_map["radius_server_groups"] = "Cisco-IOS-XR-aaa-protocol-radius-cfg:radius-server-groups"

            self.diameter_server_groups = Aaa.ServerGroups.DiameterServerGroups()
            self.diameter_server_groups.parent = self
            self._children_name_map["diameter_server_groups"] = "Cisco-IOS-XR-aaa-diameter-cfg:diameter-server-groups"

            self.tacacs_server_groups = Aaa.ServerGroups.TacacsServerGroups()
            self.tacacs_server_groups.parent = self
            self._children_name_map["tacacs_server_groups"] = "Cisco-IOS-XR-aaa-tacacs-cfg:tacacs-server-groups"
            self._segment_path = lambda: "Cisco-IOS-XR-aaa-locald-cfg:server-groups"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.ServerGroups, [], name, value)


        class RadiusServerGroups(Entity):
            """
            RADIUS server group definition
            
            .. attribute:: radius_server_group
            
            	RADIUS server group name
            	**type**\: list of  		 :py:class:`RadiusServerGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.ServerGroups.RadiusServerGroups, self).__init__()

                self.yang_name = "radius-server-groups"
                self.yang_parent_name = "server-groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("radius-server-group", ("radius_server_group", Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup))])
                self._leafs = OrderedDict()

                self.radius_server_group = YList(self)
                self._segment_path = lambda: "Cisco-IOS-XR-aaa-protocol-radius-cfg:radius-server-groups"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:server-groups/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.ServerGroups.RadiusServerGroups, [], name, value)


            class RadiusServerGroup(Entity):
                """
                RADIUS server group name
                
                .. attribute:: server_group_name  (key)
                
                	RADIUS server group name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: accounting
                
                	List of filters in server group
                	**type**\:  :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting>`
                
                .. attribute:: servers
                
                	List of RADIUS servers present in the group
                	**type**\:  :py:class:`Servers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers>`
                
                .. attribute:: private_servers
                
                	List of private RADIUS servers present in the group
                	**type**\:  :py:class:`PrivateServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers>`
                
                .. attribute:: server_group_throttle
                
                	Radius throttling options
                	**type**\:  :py:class:`ServerGroupThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.ServerGroupThrottle>`
                
                .. attribute:: load_balance
                
                	Radius load\-balancing options
                	**type**\:  :py:class:`LoadBalance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance>`
                
                .. attribute:: authorization
                
                	List of filters in server group
                	**type**\:  :py:class:`Authorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization>`
                
                .. attribute:: dead_time
                
                	This indicates the length of time (in minutes) for which RADIUS servers present in this group remain marked as dead
                	**type**\: int
                
                	**range:** 1..1440
                
                	**units**\: minute
                
                .. attribute:: source_interface
                
                	Specify interface for source address in RADIUS packets
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: vrf
                
                	Specify VRF name of RADIUS group
                	**type**\: str
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup, self).__init__()

                    self.yang_name = "radius-server-group"
                    self.yang_parent_name = "radius-server-groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['server_group_name']
                    self._child_classes = OrderedDict([("accounting", ("accounting", Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting)), ("servers", ("servers", Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers)), ("private-servers", ("private_servers", Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers)), ("server-group-throttle", ("server_group_throttle", Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.ServerGroupThrottle)), ("load-balance", ("load_balance", Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance)), ("authorization", ("authorization", Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization))])
                    self._leafs = OrderedDict([
                        ('server_group_name', (YLeaf(YType.str, 'server-group-name'), ['str'])),
                        ('dead_time', (YLeaf(YType.uint32, 'dead-time'), ['int'])),
                        ('source_interface', (YLeaf(YType.str, 'source-interface'), ['str'])),
                        ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                    ])
                    self.server_group_name = None
                    self.dead_time = None
                    self.source_interface = None
                    self.vrf = None

                    self.accounting = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting()
                    self.accounting.parent = self
                    self._children_name_map["accounting"] = "accounting"

                    self.servers = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers()
                    self.servers.parent = self
                    self._children_name_map["servers"] = "servers"

                    self.private_servers = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers()
                    self.private_servers.parent = self
                    self._children_name_map["private_servers"] = "private-servers"

                    self.server_group_throttle = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.ServerGroupThrottle()
                    self.server_group_throttle.parent = self
                    self._children_name_map["server_group_throttle"] = "server-group-throttle"

                    self.load_balance = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance()
                    self.load_balance.parent = self
                    self._children_name_map["load_balance"] = "load-balance"

                    self.authorization = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization()
                    self.authorization.parent = self
                    self._children_name_map["authorization"] = "authorization"
                    self._segment_path = lambda: "radius-server-group" + "[server-group-name='" + str(self.server_group_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:server-groups/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius-server-groups/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup, ['server_group_name', 'dead_time', 'source_interface', 'vrf'], name, value)


                class Accounting(Entity):
                    """
                    List of filters in server group
                    
                    .. attribute:: request
                    
                    	Specify a filter in server group
                    	**type**\:  :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Request>`
                    
                    .. attribute:: reply
                    
                    	Specify a filter in server group
                    	**type**\:  :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Reply>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting, self).__init__()

                        self.yang_name = "accounting"
                        self.yang_parent_name = "radius-server-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("request", ("request", Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Request)), ("reply", ("reply", Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Reply))])
                        self._leafs = OrderedDict()

                        self.request = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Request()
                        self.request.parent = self
                        self._children_name_map["request"] = "request"

                        self.reply = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Reply()
                        self.reply.parent = self
                        self._children_name_map["reply"] = "reply"
                        self._segment_path = lambda: "accounting"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting, [], name, value)


                    class Request(Entity):
                        """
                        Specify a filter in server group
                        
                        .. attribute:: action
                        
                        	Specify the attribute list type accept or reject
                        	**type**\:  :py:class:`AaaAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaAction>`
                        
                        .. attribute:: attribute_list_name
                        
                        	Name of RADIUS attribute list
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Request, self).__init__()

                            self.yang_name = "request"
                            self.yang_parent_name = "accounting"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('action', (YLeaf(YType.enumeration, 'action'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaAction', '')])),
                                ('attribute_list_name', (YLeaf(YType.str, 'attribute-list-name'), ['str'])),
                            ])
                            self.action = None
                            self.attribute_list_name = None
                            self._segment_path = lambda: "request"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Request, ['action', 'attribute_list_name'], name, value)


                    class Reply(Entity):
                        """
                        Specify a filter in server group
                        
                        .. attribute:: action
                        
                        	Specify the attribute list type accept or reject
                        	**type**\:  :py:class:`AaaAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaAction>`
                        
                        .. attribute:: attribute_list_name
                        
                        	Name of RADIUS attribute list
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Reply, self).__init__()

                            self.yang_name = "reply"
                            self.yang_parent_name = "accounting"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('action', (YLeaf(YType.enumeration, 'action'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaAction', '')])),
                                ('attribute_list_name', (YLeaf(YType.str, 'attribute-list-name'), ['str'])),
                            ])
                            self.action = None
                            self.attribute_list_name = None
                            self._segment_path = lambda: "reply"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Reply, ['action', 'attribute_list_name'], name, value)


                class Servers(Entity):
                    """
                    List of RADIUS servers present in the group
                    
                    .. attribute:: server
                    
                    	A server to include in the server group
                    	**type**\: list of  		 :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers.Server>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers, self).__init__()

                        self.yang_name = "servers"
                        self.yang_parent_name = "radius-server-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("server", ("server", Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers.Server))])
                        self._leafs = OrderedDict()

                        self.server = YList(self)
                        self._segment_path = lambda: "servers"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers, [], name, value)


                    class Server(Entity):
                        """
                        A server to include in the server group
                        
                        .. attribute:: ordering_index  (key)
                        
                        	This is used to sort the servers in the order of precedence
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_address  (key)
                        
                        	IP address of RADIUS server
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: auth_port_number  (key)
                        
                        	Authentication Port number (standard port 1645)
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: acct_port_number  (key)
                        
                        	Accounting Port number (standard port 1646)
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers.Server, self).__init__()

                            self.yang_name = "server"
                            self.yang_parent_name = "servers"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['ordering_index','ip_address','auth_port_number','acct_port_number']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ordering_index', (YLeaf(YType.uint32, 'ordering-index'), ['int'])),
                                ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
                                ('auth_port_number', (YLeaf(YType.uint16, 'auth-port-number'), ['int'])),
                                ('acct_port_number', (YLeaf(YType.uint16, 'acct-port-number'), ['int'])),
                            ])
                            self.ordering_index = None
                            self.ip_address = None
                            self.auth_port_number = None
                            self.acct_port_number = None
                            self._segment_path = lambda: "server" + "[ordering-index='" + str(self.ordering_index) + "']" + "[ip-address='" + str(self.ip_address) + "']" + "[auth-port-number='" + str(self.auth_port_number) + "']" + "[acct-port-number='" + str(self.acct_port_number) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers.Server, ['ordering_index', 'ip_address', 'auth_port_number', 'acct_port_number'], name, value)


                class PrivateServers(Entity):
                    """
                    List of private RADIUS servers present in the
                    group
                    
                    .. attribute:: private_server
                    
                    	A private server to include in the server group
                    	**type**\: list of  		 :py:class:`PrivateServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers.PrivateServer>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers, self).__init__()

                        self.yang_name = "private-servers"
                        self.yang_parent_name = "radius-server-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("private-server", ("private_server", Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers.PrivateServer))])
                        self._leafs = OrderedDict()

                        self.private_server = YList(self)
                        self._segment_path = lambda: "private-servers"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers, [], name, value)


                    class PrivateServer(Entity):
                        """
                        A private server to include in the server
                        group
                        
                        .. attribute:: ordering_index  (key)
                        
                        	This is used to sort the servers in the order of precedence
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_address  (key)
                        
                        	IP address of RADIUS server
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: auth_port_number  (key)
                        
                        	Authentication Port number (standard port 1645)
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: acct_port_number  (key)
                        
                        	Accounting Port number (standard port 1646)
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: private_timeout
                        
                        	Time to wait for a RADIUS server to reply
                        	**type**\: int
                        
                        	**range:** 1..1000
                        
                        	**default value**\: 5
                        
                        .. attribute:: ignore_accounting_port
                        
                        	Ignore Accounting port
                        	**type**\: bool
                        
                        .. attribute:: private_retransmit
                        
                        	Number of times to retransmit a request to the RADIUS server
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        	**default value**\: 3
                        
                        .. attribute:: idle_time
                        
                        	Idle time for the radius Server
                        	**type**\: int
                        
                        	**range:** 1..60
                        
                        	**default value**\: 5
                        
                        .. attribute:: private_key
                        
                        	RADIUS encryption key
                        	**type**\: str
                        
                        	**pattern:** (!.+)\|([^!].+)
                        
                        .. attribute:: username
                        
                        	Username to be tested for automated testing
                        	**type**\: str
                        
                        .. attribute:: ignore_auth_port
                        
                        	Ignore authentication Port
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers.PrivateServer, self).__init__()

                            self.yang_name = "private-server"
                            self.yang_parent_name = "private-servers"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['ordering_index','ip_address','auth_port_number','acct_port_number']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ordering_index', (YLeaf(YType.uint32, 'ordering-index'), ['int'])),
                                ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
                                ('auth_port_number', (YLeaf(YType.uint16, 'auth-port-number'), ['int'])),
                                ('acct_port_number', (YLeaf(YType.uint16, 'acct-port-number'), ['int'])),
                                ('private_timeout', (YLeaf(YType.uint32, 'private-timeout'), ['int'])),
                                ('ignore_accounting_port', (YLeaf(YType.boolean, 'ignore-accounting-port'), ['bool'])),
                                ('private_retransmit', (YLeaf(YType.uint32, 'private-retransmit'), ['int'])),
                                ('idle_time', (YLeaf(YType.uint32, 'idle-time'), ['int'])),
                                ('private_key', (YLeaf(YType.str, 'private-key'), ['str'])),
                                ('username', (YLeaf(YType.str, 'username'), ['str'])),
                                ('ignore_auth_port', (YLeaf(YType.boolean, 'ignore-auth-port'), ['bool'])),
                            ])
                            self.ordering_index = None
                            self.ip_address = None
                            self.auth_port_number = None
                            self.acct_port_number = None
                            self.private_timeout = None
                            self.ignore_accounting_port = None
                            self.private_retransmit = None
                            self.idle_time = None
                            self.private_key = None
                            self.username = None
                            self.ignore_auth_port = None
                            self._segment_path = lambda: "private-server" + "[ordering-index='" + str(self.ordering_index) + "']" + "[ip-address='" + str(self.ip_address) + "']" + "[auth-port-number='" + str(self.auth_port_number) + "']" + "[acct-port-number='" + str(self.acct_port_number) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers.PrivateServer, ['ordering_index', 'ip_address', 'auth_port_number', 'acct_port_number', 'private_timeout', 'ignore_accounting_port', 'private_retransmit', 'idle_time', 'private_key', 'username', 'ignore_auth_port'], name, value)


                class ServerGroupThrottle(Entity):
                    """
                    Radius throttling options
                    
                    .. attribute:: access
                    
                    	To flow control the number of access requests sent to a radius server
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**default value**\: 0
                    
                    .. attribute:: accounting
                    
                    	To flow control the number of accounting requests sent to a radius server
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**default value**\: 0
                    
                    .. attribute:: access_timeout
                    
                    	Specify the number of timeouts exceeding which a throttled access request is dropped
                    	**type**\: int
                    
                    	**range:** 1..10
                    
                    	**default value**\: 3
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.ServerGroupThrottle, self).__init__()

                        self.yang_name = "server-group-throttle"
                        self.yang_parent_name = "radius-server-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('access', (YLeaf(YType.uint32, 'access'), ['int'])),
                            ('accounting', (YLeaf(YType.uint32, 'accounting'), ['int'])),
                            ('access_timeout', (YLeaf(YType.uint32, 'access-timeout'), ['int'])),
                        ])
                        self.access = None
                        self.accounting = None
                        self.access_timeout = None
                        self._segment_path = lambda: "server-group-throttle"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.ServerGroupThrottle, ['access', 'accounting', 'access_timeout'], name, value)


                class LoadBalance(Entity):
                    """
                    Radius load\-balancing options
                    
                    .. attribute:: method
                    
                    	Method by which the next host will be picked
                    	**type**\:  :py:class:`Method <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance, self).__init__()

                        self.yang_name = "load-balance"
                        self.yang_parent_name = "radius-server-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("method", ("method", Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method))])
                        self._leafs = OrderedDict()

                        self.method = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method()
                        self.method.parent = self
                        self._children_name_map["method"] = "method"
                        self._segment_path = lambda: "load-balance"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance, [], name, value)


                    class Method(Entity):
                        """
                        Method by which the next host will be picked
                        
                        .. attribute:: name
                        
                        	Batch size for selection of the server
                        	**type**\:  :py:class:`Name <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method.Name>`
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method, self).__init__()

                            self.yang_name = "method"
                            self.yang_parent_name = "load-balance"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("name", ("name", Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method.Name))])
                            self._leafs = OrderedDict()

                            self.name = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method.Name()
                            self.name.parent = self
                            self._children_name_map["name"] = "name"
                            self._segment_path = lambda: "method"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method, [], name, value)


                        class Name(Entity):
                            """
                            Batch size for selection of the server
                            
                            .. attribute:: least_outstanding
                            
                            	Pick the server with the least transactions outstanding
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**default value**\: 4
                            
                            .. attribute:: batch_size
                            
                            	Batch size for selection of the server
                            	**type**\: int
                            
                            	**range:** 1..1500
                            
                            	**default value**\: 25
                            
                            .. attribute:: ignore_preferred_server
                            
                            	Disable preferred server for this Server Group
                            	**type**\: bool
                            
                            	**default value**\: true
                            
                            

                            """

                            _prefix = 'aaa-protocol-radius-cfg'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method.Name, self).__init__()

                                self.yang_name = "name"
                                self.yang_parent_name = "method"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('least_outstanding', (YLeaf(YType.uint32, 'least-outstanding'), ['int'])),
                                    ('batch_size', (YLeaf(YType.uint32, 'batch-size'), ['int'])),
                                    ('ignore_preferred_server', (YLeaf(YType.boolean, 'ignore-preferred-server'), ['bool'])),
                                ])
                                self.least_outstanding = None
                                self.batch_size = None
                                self.ignore_preferred_server = None
                                self._segment_path = lambda: "name"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method.Name, ['least_outstanding', 'batch_size', 'ignore_preferred_server'], name, value)


                class Authorization(Entity):
                    """
                    List of filters in server group
                    
                    .. attribute:: request
                    
                    	Specify a filter in server group
                    	**type**\:  :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Request>`
                    
                    .. attribute:: reply
                    
                    	Specify a filter in server group
                    	**type**\:  :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Reply>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization, self).__init__()

                        self.yang_name = "authorization"
                        self.yang_parent_name = "radius-server-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("request", ("request", Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Request)), ("reply", ("reply", Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Reply))])
                        self._leafs = OrderedDict()

                        self.request = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Request()
                        self.request.parent = self
                        self._children_name_map["request"] = "request"

                        self.reply = Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Reply()
                        self.reply.parent = self
                        self._children_name_map["reply"] = "reply"
                        self._segment_path = lambda: "authorization"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization, [], name, value)


                    class Request(Entity):
                        """
                        Specify a filter in server group
                        
                        .. attribute:: action
                        
                        	Specify the attribute list type accept or reject
                        	**type**\:  :py:class:`AaaAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaAction>`
                        
                        .. attribute:: attribute_list_name
                        
                        	Name of RADIUS attribute list
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Request, self).__init__()

                            self.yang_name = "request"
                            self.yang_parent_name = "authorization"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('action', (YLeaf(YType.enumeration, 'action'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaAction', '')])),
                                ('attribute_list_name', (YLeaf(YType.str, 'attribute-list-name'), ['str'])),
                            ])
                            self.action = None
                            self.attribute_list_name = None
                            self._segment_path = lambda: "request"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Request, ['action', 'attribute_list_name'], name, value)


                    class Reply(Entity):
                        """
                        Specify a filter in server group
                        
                        .. attribute:: action
                        
                        	Specify the attribute list type accept or reject
                        	**type**\:  :py:class:`AaaAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaAction>`
                        
                        .. attribute:: attribute_list_name
                        
                        	Name of RADIUS attribute list
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Reply, self).__init__()

                            self.yang_name = "reply"
                            self.yang_parent_name = "authorization"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('action', (YLeaf(YType.enumeration, 'action'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaAction', '')])),
                                ('attribute_list_name', (YLeaf(YType.str, 'attribute-list-name'), ['str'])),
                            ])
                            self.action = None
                            self.attribute_list_name = None
                            self._segment_path = lambda: "reply"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Reply, ['action', 'attribute_list_name'], name, value)


        class DiameterServerGroups(Entity):
            """
            DIAMETER server group definition
            
            .. attribute:: diameter_server_group
            
            	DIAMETER server group name
            	**type**\: list of  		 :py:class:`DiameterServerGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup>`
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2017-11-13'

            def __init__(self):
                super(Aaa.ServerGroups.DiameterServerGroups, self).__init__()

                self.yang_name = "diameter-server-groups"
                self.yang_parent_name = "server-groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("diameter-server-group", ("diameter_server_group", Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup))])
                self._leafs = OrderedDict()

                self.diameter_server_group = YList(self)
                self._segment_path = lambda: "Cisco-IOS-XR-aaa-diameter-cfg:diameter-server-groups"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:server-groups/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.ServerGroups.DiameterServerGroups, [], name, value)


            class DiameterServerGroup(Entity):
                """
                DIAMETER server group name
                
                .. attribute:: server_group_name  (key)
                
                	DIAMETER server group name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: servers
                
                	List of DIAMETER servers present in the group
                	**type**\:  :py:class:`Servers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers>`
                
                

                """

                _prefix = 'aaa-diameter-cfg'
                _revision = '2017-11-13'

                def __init__(self):
                    super(Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup, self).__init__()

                    self.yang_name = "diameter-server-group"
                    self.yang_parent_name = "diameter-server-groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['server_group_name']
                    self._child_classes = OrderedDict([("servers", ("servers", Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers))])
                    self._leafs = OrderedDict([
                        ('server_group_name', (YLeaf(YType.str, 'server-group-name'), ['str'])),
                    ])
                    self.server_group_name = None

                    self.servers = Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers()
                    self.servers.parent = self
                    self._children_name_map["servers"] = "servers"
                    self._segment_path = lambda: "diameter-server-group" + "[server-group-name='" + str(self.server_group_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:server-groups/Cisco-IOS-XR-aaa-diameter-cfg:diameter-server-groups/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup, ['server_group_name'], name, value)


                class Servers(Entity):
                    """
                    List of DIAMETER servers present in the group
                    
                    .. attribute:: server
                    
                    	A server to include in the server group
                    	**type**\: list of  		 :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers.Server>`
                    
                    

                    """

                    _prefix = 'aaa-diameter-cfg'
                    _revision = '2017-11-13'

                    def __init__(self):
                        super(Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers, self).__init__()

                        self.yang_name = "servers"
                        self.yang_parent_name = "diameter-server-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("server", ("server", Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers.Server))])
                        self._leafs = OrderedDict()

                        self.server = YList(self)
                        self._segment_path = lambda: "servers"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers, [], name, value)


                    class Server(Entity):
                        """
                        A server to include in the server group
                        
                        .. attribute:: ordering_index  (key)
                        
                        	This is used to sort the servers in the order of precedence
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: peer_name  (key)
                        
                        	Name for the diameter peer configuration
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        

                        """

                        _prefix = 'aaa-diameter-cfg'
                        _revision = '2017-11-13'

                        def __init__(self):
                            super(Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers.Server, self).__init__()

                            self.yang_name = "server"
                            self.yang_parent_name = "servers"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['ordering_index','peer_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ordering_index', (YLeaf(YType.uint32, 'ordering-index'), ['int'])),
                                ('peer_name', (YLeaf(YType.str, 'peer-name'), ['str'])),
                            ])
                            self.ordering_index = None
                            self.peer_name = None
                            self._segment_path = lambda: "server" + "[ordering-index='" + str(self.ordering_index) + "']" + "[peer-name='" + str(self.peer_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers.Server, ['ordering_index', 'peer_name'], name, value)


        class TacacsServerGroups(Entity):
            """
            TACACS+ server\-group definition
            
            .. attribute:: tacacs_server_group
            
            	TACACS+ Server group name
            	**type**\: list of  		 :py:class:`TacacsServerGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup>`
            
            

            """

            _prefix = 'aaa-tacacs-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.ServerGroups.TacacsServerGroups, self).__init__()

                self.yang_name = "tacacs-server-groups"
                self.yang_parent_name = "server-groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("tacacs-server-group", ("tacacs_server_group", Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup))])
                self._leafs = OrderedDict()

                self.tacacs_server_group = YList(self)
                self._segment_path = lambda: "Cisco-IOS-XR-aaa-tacacs-cfg:tacacs-server-groups"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:server-groups/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.ServerGroups.TacacsServerGroups, [], name, value)


            class TacacsServerGroup(Entity):
                """
                TACACS+ Server group name
                
                .. attribute:: server_group_name  (key)
                
                	TACACS+ Server group name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: servers
                
                	Specify a TACACS+ server
                	**type**\:  :py:class:`Servers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers>`
                
                .. attribute:: private_servers
                
                	List of private TACACS servers present in the group
                	**type**\:  :py:class:`PrivateServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers>`
                
                .. attribute:: vrf
                
                	Specify VRF name of TACACS group
                	**type**\: str
                
                

                """

                _prefix = 'aaa-tacacs-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup, self).__init__()

                    self.yang_name = "tacacs-server-group"
                    self.yang_parent_name = "tacacs-server-groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['server_group_name']
                    self._child_classes = OrderedDict([("servers", ("servers", Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers)), ("private-servers", ("private_servers", Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers))])
                    self._leafs = OrderedDict([
                        ('server_group_name', (YLeaf(YType.str, 'server-group-name'), ['str'])),
                        ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                    ])
                    self.server_group_name = None
                    self.vrf = None

                    self.servers = Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers()
                    self.servers.parent = self
                    self._children_name_map["servers"] = "servers"

                    self.private_servers = Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers()
                    self.private_servers.parent = self
                    self._children_name_map["private_servers"] = "private-servers"
                    self._segment_path = lambda: "tacacs-server-group" + "[server-group-name='" + str(self.server_group_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:server-groups/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs-server-groups/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup, ['server_group_name', 'vrf'], name, value)


                class Servers(Entity):
                    """
                    Specify a TACACS+ server
                    
                    .. attribute:: server
                    
                    	A server to include in the server group
                    	**type**\: list of  		 :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers.Server>`
                    
                    

                    """

                    _prefix = 'aaa-tacacs-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers, self).__init__()

                        self.yang_name = "servers"
                        self.yang_parent_name = "tacacs-server-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("server", ("server", Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers.Server))])
                        self._leafs = OrderedDict()

                        self.server = YList(self)
                        self._segment_path = lambda: "servers"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers, [], name, value)


                    class Server(Entity):
                        """
                        A server to include in the server group
                        
                        .. attribute:: ordering_index  (key)
                        
                        	This is used to sort the servers in the order of precedence
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_address  (key)
                        
                        	IP address of TACACS+ server
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'aaa-tacacs-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers.Server, self).__init__()

                            self.yang_name = "server"
                            self.yang_parent_name = "servers"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['ordering_index','ip_address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ordering_index', (YLeaf(YType.uint32, 'ordering-index'), ['int'])),
                                ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
                            ])
                            self.ordering_index = None
                            self.ip_address = None
                            self._segment_path = lambda: "server" + "[ordering-index='" + str(self.ordering_index) + "']" + "[ip-address='" + str(self.ip_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers.Server, ['ordering_index', 'ip_address'], name, value)


                class PrivateServers(Entity):
                    """
                    List of private TACACS servers present in the
                    group
                    
                    .. attribute:: private_server
                    
                    	A private server to include in the server group
                    	**type**\: list of  		 :py:class:`PrivateServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers.PrivateServer>`
                    
                    

                    """

                    _prefix = 'aaa-tacacs-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers, self).__init__()

                        self.yang_name = "private-servers"
                        self.yang_parent_name = "tacacs-server-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("private-server", ("private_server", Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers.PrivateServer))])
                        self._leafs = OrderedDict()

                        self.private_server = YList(self)
                        self._segment_path = lambda: "private-servers"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers, [], name, value)


                    class PrivateServer(Entity):
                        """
                        A private server to include in the server
                        group
                        
                        .. attribute:: ordering_index  (key)
                        
                        	This is used to sort the servers in the order of precedence
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ip_address  (key)
                        
                        	IP address of TACACS+ server
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: port_number  (key)
                        
                        	Port number (standard 49)
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: key
                        
                        	Set TACACS+ encryption key
                        	**type**\: str
                        
                        	**pattern:** (!.+)\|([^!].+)
                        
                        .. attribute:: timeout
                        
                        	Time to wait for a TACACS+ server to reply
                        	**type**\: int
                        
                        	**range:** 1..1000
                        
                        	**default value**\: 5
                        
                        

                        """

                        _prefix = 'aaa-tacacs-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers.PrivateServer, self).__init__()

                            self.yang_name = "private-server"
                            self.yang_parent_name = "private-servers"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['ordering_index','ip_address','port_number']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ordering_index', (YLeaf(YType.uint32, 'ordering-index'), ['int'])),
                                ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
                                ('port_number', (YLeaf(YType.uint32, 'port-number'), ['int'])),
                                ('key', (YLeaf(YType.str, 'key'), ['str'])),
                                ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                            ])
                            self.ordering_index = None
                            self.ip_address = None
                            self.port_number = None
                            self.key = None
                            self.timeout = None
                            self._segment_path = lambda: "private-server" + "[ordering-index='" + str(self.ordering_index) + "']" + "[ip-address='" + str(self.ip_address) + "']" + "[port-number='" + str(self.port_number) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers.PrivateServer, ['ordering_index', 'ip_address', 'port_number', 'key', 'timeout'], name, value)


    class Usernames(Entity):
        """
        Configure local usernames
        
        .. attribute:: username
        
        	Local username
        	**type**\: list of  		 :py:class:`Username <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usernames.Username>`
        
        

        """

        _prefix = 'aaa-locald-cfg'
        _revision = '2018-06-04'

        def __init__(self):
            super(Aaa.Usernames, self).__init__()

            self.yang_name = "usernames"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("username", ("username", Aaa.Usernames.Username))])
            self._leafs = OrderedDict()

            self.username = YList(self)
            self._segment_path = lambda: "Cisco-IOS-XR-aaa-locald-cfg:usernames"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.Usernames, [], name, value)


        class Username(Entity):
            """
            Local username
            
            .. attribute:: ordering_index  (key)
            
            	This is used to sort the users in the order of precedence
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: name  (key)
            
            	Username
            	**type**\: str
            
            .. attribute:: password_policy
            
            	Mention Password policy for the user
            	**type**\:  :py:class:`PasswordPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usernames.Username.PasswordPolicy>`
            
            .. attribute:: usergroup_under_usernames
            
            	Specify the usergroup to which this user belongs
            	**type**\:  :py:class:`UsergroupUnderUsernames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usernames.Username.UsergroupUnderUsernames>`
            
            .. attribute:: secret
            
            	Specify the secret for the user
            	**type**\: str
            
            	**pattern:** (!.+)\|([^!].+)
            
            .. attribute:: password
            
            	Specify the password for the user
            	**type**\: str
            
            	**pattern:** (!.+)\|([^!].+)
            
            

            """

            _prefix = 'aaa-locald-cfg'
            _revision = '2018-06-04'

            def __init__(self):
                super(Aaa.Usernames.Username, self).__init__()

                self.yang_name = "username"
                self.yang_parent_name = "usernames"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ordering_index','name']
                self._child_classes = OrderedDict([("password-policy", ("password_policy", Aaa.Usernames.Username.PasswordPolicy)), ("usergroup-under-usernames", ("usergroup_under_usernames", Aaa.Usernames.Username.UsergroupUnderUsernames))])
                self._leafs = OrderedDict([
                    ('ordering_index', (YLeaf(YType.uint32, 'ordering-index'), ['int'])),
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('secret', (YLeaf(YType.str, 'secret'), ['str'])),
                    ('password', (YLeaf(YType.str, 'password'), ['str'])),
                ])
                self.ordering_index = None
                self.name = None
                self.secret = None
                self.password = None

                self.password_policy = Aaa.Usernames.Username.PasswordPolicy()
                self.password_policy.parent = self
                self._children_name_map["password_policy"] = "password-policy"

                self.usergroup_under_usernames = Aaa.Usernames.Username.UsergroupUnderUsernames()
                self.usergroup_under_usernames.parent = self
                self._children_name_map["usergroup_under_usernames"] = "usergroup-under-usernames"
                self._segment_path = lambda: "username" + "[ordering-index='" + str(self.ordering_index) + "']" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:usernames/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Usernames.Username, [u'ordering_index', u'name', u'secret', u'password'], name, value)


            class PasswordPolicy(Entity):
                """
                Mention Password policy for the user
                
                .. attribute:: name
                
                	Password Policy name
                	**type**\: str
                
                	**length:** 1..252
                
                .. attribute:: password
                
                	The user's password
                	**type**\: str
                
                	**pattern:** (!.+)\|([^!].+)
                
                

                """

                _prefix = 'aaa-locald-cfg'
                _revision = '2018-06-04'

                def __init__(self):
                    super(Aaa.Usernames.Username.PasswordPolicy, self).__init__()

                    self.yang_name = "password-policy"
                    self.yang_parent_name = "username"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('password', (YLeaf(YType.str, 'password'), ['str'])),
                    ])
                    self.name = None
                    self.password = None
                    self._segment_path = lambda: "password-policy"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Usernames.Username.PasswordPolicy, [u'name', u'password'], name, value)


            class UsergroupUnderUsernames(Entity):
                """
                Specify the usergroup to which this user
                belongs
                
                .. attribute:: usergroup_under_username
                
                	Name of the usergroup
                	**type**\: list of  		 :py:class:`UsergroupUnderUsername <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername>`
                
                

                """

                _prefix = 'aaa-locald-cfg'
                _revision = '2018-06-04'

                def __init__(self):
                    super(Aaa.Usernames.Username.UsergroupUnderUsernames, self).__init__()

                    self.yang_name = "usergroup-under-usernames"
                    self.yang_parent_name = "username"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("usergroup-under-username", ("usergroup_under_username", Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername))])
                    self._leafs = OrderedDict()

                    self.usergroup_under_username = YList(self)
                    self._segment_path = lambda: "usergroup-under-usernames"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Usernames.Username.UsergroupUnderUsernames, [], name, value)


                class UsergroupUnderUsername(Entity):
                    """
                    Name of the usergroup
                    
                    .. attribute:: name  (key)
                    
                    	Name of the usergroup
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    

                    """

                    _prefix = 'aaa-locald-cfg'
                    _revision = '2018-06-04'

                    def __init__(self):
                        super(Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername, self).__init__()

                        self.yang_name = "usergroup-under-username"
                        self.yang_parent_name = "usergroup-under-usernames"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ])
                        self.name = None
                        self._segment_path = lambda: "usergroup-under-username" + "[name='" + str(self.name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername, [u'name'], name, value)


    class Taskgroups(Entity):
        """
        Specify a taskgroup to inherit from
        
        .. attribute:: taskgroup
        
        	Taskgroup name
        	**type**\: list of  		 :py:class:`Taskgroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups.Taskgroup>`
        
        

        """

        _prefix = 'aaa-locald-cfg'
        _revision = '2018-06-04'

        def __init__(self):
            super(Aaa.Taskgroups, self).__init__()

            self.yang_name = "taskgroups"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("taskgroup", ("taskgroup", Aaa.Taskgroups.Taskgroup))])
            self._leafs = OrderedDict()

            self.taskgroup = YList(self)
            self._segment_path = lambda: "Cisco-IOS-XR-aaa-locald-cfg:taskgroups"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.Taskgroups, [], name, value)


        class Taskgroup(Entity):
            """
            Taskgroup name
            
            .. attribute:: name  (key)
            
            	Taskgroup name
            	**type**\: str
            
            .. attribute:: taskgroup_under_taskgroups
            
            	Specify a taskgroup to inherit from
            	**type**\:  :py:class:`TaskgroupUnderTaskgroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups>`
            
            .. attribute:: tasks
            
            	Specify task IDs to be part of this group
            	**type**\:  :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups.Taskgroup.Tasks>`
            
            .. attribute:: description
            
            	Description for the task group
            	**type**\: str
            
            

            """

            _prefix = 'aaa-locald-cfg'
            _revision = '2018-06-04'

            def __init__(self):
                super(Aaa.Taskgroups.Taskgroup, self).__init__()

                self.yang_name = "taskgroup"
                self.yang_parent_name = "taskgroups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("taskgroup-under-taskgroups", ("taskgroup_under_taskgroups", Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups)), ("tasks", ("tasks", Aaa.Taskgroups.Taskgroup.Tasks))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                ])
                self.name = None
                self.description = None

                self.taskgroup_under_taskgroups = Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups()
                self.taskgroup_under_taskgroups.parent = self
                self._children_name_map["taskgroup_under_taskgroups"] = "taskgroup-under-taskgroups"

                self.tasks = Aaa.Taskgroups.Taskgroup.Tasks()
                self.tasks.parent = self
                self._children_name_map["tasks"] = "tasks"
                self._segment_path = lambda: "taskgroup" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:taskgroups/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Taskgroups.Taskgroup, [u'name', u'description'], name, value)


            class TaskgroupUnderTaskgroups(Entity):
                """
                Specify a taskgroup to inherit from
                
                .. attribute:: taskgroup_under_taskgroup
                
                	Name of the task group to include
                	**type**\: list of  		 :py:class:`TaskgroupUnderTaskgroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups.TaskgroupUnderTaskgroup>`
                
                

                """

                _prefix = 'aaa-locald-cfg'
                _revision = '2018-06-04'

                def __init__(self):
                    super(Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups, self).__init__()

                    self.yang_name = "taskgroup-under-taskgroups"
                    self.yang_parent_name = "taskgroup"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("taskgroup-under-taskgroup", ("taskgroup_under_taskgroup", Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups.TaskgroupUnderTaskgroup))])
                    self._leafs = OrderedDict()

                    self.taskgroup_under_taskgroup = YList(self)
                    self._segment_path = lambda: "taskgroup-under-taskgroups"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups, [], name, value)


                class TaskgroupUnderTaskgroup(Entity):
                    """
                    Name of the task group to include
                    
                    .. attribute:: name  (key)
                    
                    	Name of the task group to include
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    

                    """

                    _prefix = 'aaa-locald-cfg'
                    _revision = '2018-06-04'

                    def __init__(self):
                        super(Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups.TaskgroupUnderTaskgroup, self).__init__()

                        self.yang_name = "taskgroup-under-taskgroup"
                        self.yang_parent_name = "taskgroup-under-taskgroups"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ])
                        self.name = None
                        self._segment_path = lambda: "taskgroup-under-taskgroup" + "[name='" + str(self.name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups.TaskgroupUnderTaskgroup, [u'name'], name, value)


            class Tasks(Entity):
                """
                Specify task IDs to be part of this group
                
                .. attribute:: task
                
                	Task ID to be included
                	**type**\: list of  		 :py:class:`Task <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Taskgroups.Taskgroup.Tasks.Task>`
                
                

                """

                _prefix = 'aaa-locald-cfg'
                _revision = '2018-06-04'

                def __init__(self):
                    super(Aaa.Taskgroups.Taskgroup.Tasks, self).__init__()

                    self.yang_name = "tasks"
                    self.yang_parent_name = "taskgroup"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("task", ("task", Aaa.Taskgroups.Taskgroup.Tasks.Task))])
                    self._leafs = OrderedDict()

                    self.task = YList(self)
                    self._segment_path = lambda: "tasks"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Taskgroups.Taskgroup.Tasks, [], name, value)


                class Task(Entity):
                    """
                    Task ID to be included
                    
                    .. attribute:: type  (key)
                    
                    	This specifies the operation permitted for this task eg\: read/write/execute/debug
                    	**type**\:  :py:class:`AaaLocaldTaskClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_cfg.AaaLocaldTaskClass>`
                    
                    .. attribute:: task_id  (key)
                    
                    	Task ID to which permission is to be granted (please use class AllTasks to get a list of valid task IDs)
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'aaa-locald-cfg'
                    _revision = '2018-06-04'

                    def __init__(self):
                        super(Aaa.Taskgroups.Taskgroup.Tasks.Task, self).__init__()

                        self.yang_name = "task"
                        self.yang_parent_name = "tasks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['type','task_id']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_cfg', 'AaaLocaldTaskClass', '')])),
                            ('task_id', (YLeaf(YType.str, 'task-id'), ['str'])),
                        ])
                        self.type = None
                        self.task_id = None
                        self._segment_path = lambda: "task" + "[type='" + str(self.type) + "']" + "[task-id='" + str(self.task_id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Taskgroups.Taskgroup.Tasks.Task, [u'type', u'task_id'], name, value)


    class Usergroups(Entity):
        """
        Specify a Usergroup to inherit from
        
        .. attribute:: usergroup
        
        	Usergroup name
        	**type**\: list of  		 :py:class:`Usergroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups.Usergroup>`
        
        

        """

        _prefix = 'aaa-locald-cfg'
        _revision = '2018-06-04'

        def __init__(self):
            super(Aaa.Usergroups, self).__init__()

            self.yang_name = "usergroups"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("usergroup", ("usergroup", Aaa.Usergroups.Usergroup))])
            self._leafs = OrderedDict()

            self.usergroup = YList(self)
            self._segment_path = lambda: "Cisco-IOS-XR-aaa-locald-cfg:usergroups"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.Usergroups, [], name, value)


        class Usergroup(Entity):
            """
            Usergroup name
            
            .. attribute:: name  (key)
            
            	Usergroup name
            	**type**\: str
            
            .. attribute:: taskgroup_under_usergroups
            
            	Task group associated with this group
            	**type**\:  :py:class:`TaskgroupUnderUsergroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups>`
            
            .. attribute:: usergroup_under_usergroups
            
            	User group to be inherited by this group
            	**type**\:  :py:class:`UsergroupUnderUsergroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups>`
            
            .. attribute:: description
            
            	Description for the user group
            	**type**\: str
            
            

            """

            _prefix = 'aaa-locald-cfg'
            _revision = '2018-06-04'

            def __init__(self):
                super(Aaa.Usergroups.Usergroup, self).__init__()

                self.yang_name = "usergroup"
                self.yang_parent_name = "usergroups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("taskgroup-under-usergroups", ("taskgroup_under_usergroups", Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups)), ("usergroup-under-usergroups", ("usergroup_under_usergroups", Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                ])
                self.name = None
                self.description = None

                self.taskgroup_under_usergroups = Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups()
                self.taskgroup_under_usergroups.parent = self
                self._children_name_map["taskgroup_under_usergroups"] = "taskgroup-under-usergroups"

                self.usergroup_under_usergroups = Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups()
                self.usergroup_under_usergroups.parent = self
                self._children_name_map["usergroup_under_usergroups"] = "usergroup-under-usergroups"
                self._segment_path = lambda: "usergroup" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-locald-cfg:usergroups/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Usergroups.Usergroup, [u'name', u'description'], name, value)


            class TaskgroupUnderUsergroups(Entity):
                """
                Task group associated with this group
                
                .. attribute:: taskgroup_under_usergroup
                
                	Name of the task group
                	**type**\: list of  		 :py:class:`TaskgroupUnderUsergroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups.TaskgroupUnderUsergroup>`
                
                

                """

                _prefix = 'aaa-locald-cfg'
                _revision = '2018-06-04'

                def __init__(self):
                    super(Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups, self).__init__()

                    self.yang_name = "taskgroup-under-usergroups"
                    self.yang_parent_name = "usergroup"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("taskgroup-under-usergroup", ("taskgroup_under_usergroup", Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups.TaskgroupUnderUsergroup))])
                    self._leafs = OrderedDict()

                    self.taskgroup_under_usergroup = YList(self)
                    self._segment_path = lambda: "taskgroup-under-usergroups"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups, [], name, value)


                class TaskgroupUnderUsergroup(Entity):
                    """
                    Name of the task group
                    
                    .. attribute:: name  (key)
                    
                    	Name of the task group
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    

                    """

                    _prefix = 'aaa-locald-cfg'
                    _revision = '2018-06-04'

                    def __init__(self):
                        super(Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups.TaskgroupUnderUsergroup, self).__init__()

                        self.yang_name = "taskgroup-under-usergroup"
                        self.yang_parent_name = "taskgroup-under-usergroups"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ])
                        self.name = None
                        self._segment_path = lambda: "taskgroup-under-usergroup" + "[name='" + str(self.name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups.TaskgroupUnderUsergroup, [u'name'], name, value)


            class UsergroupUnderUsergroups(Entity):
                """
                User group to be inherited by this group
                
                .. attribute:: usergroup_under_usergroup
                
                	Name of the user group
                	**type**\: list of  		 :py:class:`UsergroupUnderUsergroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups.UsergroupUnderUsergroup>`
                
                

                """

                _prefix = 'aaa-locald-cfg'
                _revision = '2018-06-04'

                def __init__(self):
                    super(Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups, self).__init__()

                    self.yang_name = "usergroup-under-usergroups"
                    self.yang_parent_name = "usergroup"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("usergroup-under-usergroup", ("usergroup_under_usergroup", Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups.UsergroupUnderUsergroup))])
                    self._leafs = OrderedDict()

                    self.usergroup_under_usergroup = YList(self)
                    self._segment_path = lambda: "usergroup-under-usergroups"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups, [], name, value)


                class UsergroupUnderUsergroup(Entity):
                    """
                    Name of the user group
                    
                    .. attribute:: name  (key)
                    
                    	Name of the user group
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    

                    """

                    _prefix = 'aaa-locald-cfg'
                    _revision = '2018-06-04'

                    def __init__(self):
                        super(Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups.UsergroupUnderUsergroup, self).__init__()

                        self.yang_name = "usergroup-under-usergroup"
                        self.yang_parent_name = "usergroup-under-usergroups"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ])
                        self.name = None
                        self._segment_path = lambda: "usergroup-under-usergroup" + "[name='" + str(self.name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups.UsergroupUnderUsergroup, [u'name'], name, value)


    class Radius(Entity):
        """
        Remote Access Dial\-In User Service
        
        .. attribute:: hosts
        
        	List of RADIUS servers
        	**type**\:  :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Hosts>`
        
        .. attribute:: dead_criteria
        
        	RADIUS server dead criteria
        	**type**\:  :py:class:`DeadCriteria <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.DeadCriteria>`
        
        .. attribute:: disallow
        
        	disallow null\-username
        	**type**\:  :py:class:`Disallow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Disallow>`
        
        .. attribute:: ipv6
        
        	IPv6 configuration
        	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Ipv6>`
        
        .. attribute:: dynamic_authorization
        
        	RADIUS dynamic authorization
        	**type**\:  :py:class:`DynamicAuthorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.DynamicAuthorization>`
        
        .. attribute:: load_balance_options
        
        	Radius load\-balancing options
        	**type**\:  :py:class:`LoadBalanceOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.LoadBalanceOptions>`
        
        .. attribute:: vrfs
        
        	List of VRFs
        	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Vrfs>`
        
        .. attribute:: throttle
        
        	Radius throttling options
        	**type**\:  :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Throttle>`
        
        .. attribute:: vsa
        
        	Unknown VSA (Vendor Specific Attribute) ignore configuration for RADIUS server
        	**type**\:  :py:class:`Vsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Vsa>`
        
        .. attribute:: ipv4
        
        	IPv4 configuration
        	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Ipv4>`
        
        .. attribute:: radius_attribute
        
        	attribute
        	**type**\:  :py:class:`RadiusAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute>`
        
        .. attribute:: attributes
        
        	Table of attribute list
        	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Attributes>`
        
        .. attribute:: source_port
        
        	Source port
        	**type**\:  :py:class:`SourcePort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.SourcePort>`
        
        .. attribute:: retransmit
        
        	Number of times to retransmit a request to the RADIUS server(0\-Disable)
        	**type**\: int
        
        	**range:** 0..100
        
        	**default value**\: 3
        
        .. attribute:: dead_time
        
        	This indicates the length of time (in minutes) for which a RADIUS server remains marked as dead
        	**type**\: int
        
        	**range:** 1..1440
        
        	**units**\: minute
        
        .. attribute:: key
        
        	RADIUS encryption key
        	**type**\: str
        
        	**pattern:** (!.+)\|([^!].+)
        
        .. attribute:: timeout
        
        	Time to wait for a RADIUS server to reply
        	**type**\: int
        
        	**range:** 1..1000
        
        	**default value**\: 5
        
        .. attribute:: ignore_accounting_port
        
        	Time to wait for a RADIUS server to reply
        	**type**\: bool
        
        .. attribute:: idle_time
        
        	Idle time for RADIUS server
        	**type**\: int
        
        	**range:** 1..1000
        
        	**default value**\: 5
        
        .. attribute:: username
        
        	Username to be tested for automated testing
        	**type**\: str
        
        .. attribute:: ignore_auth_port
        
        	Time to wait for a RADIUS server to reply
        	**type**\: bool
        
        

        """

        _prefix = 'aaa-protocol-radius-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(Aaa.Radius, self).__init__()

            self.yang_name = "radius"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("hosts", ("hosts", Aaa.Radius.Hosts)), ("dead-criteria", ("dead_criteria", Aaa.Radius.DeadCriteria)), ("disallow", ("disallow", Aaa.Radius.Disallow)), ("ipv6", ("ipv6", Aaa.Radius.Ipv6)), ("dynamic-authorization", ("dynamic_authorization", Aaa.Radius.DynamicAuthorization)), ("load-balance-options", ("load_balance_options", Aaa.Radius.LoadBalanceOptions)), ("vrfs", ("vrfs", Aaa.Radius.Vrfs)), ("throttle", ("throttle", Aaa.Radius.Throttle)), ("vsa", ("vsa", Aaa.Radius.Vsa)), ("ipv4", ("ipv4", Aaa.Radius.Ipv4)), ("radius-attribute", ("radius_attribute", Aaa.Radius.RadiusAttribute)), ("attributes", ("attributes", Aaa.Radius.Attributes)), ("source-port", ("source_port", Aaa.Radius.SourcePort))])
            self._leafs = OrderedDict([
                ('retransmit', (YLeaf(YType.uint32, 'retransmit'), ['int'])),
                ('dead_time', (YLeaf(YType.uint32, 'dead-time'), ['int'])),
                ('key', (YLeaf(YType.str, 'key'), ['str'])),
                ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                ('ignore_accounting_port', (YLeaf(YType.boolean, 'ignore-accounting-port'), ['bool'])),
                ('idle_time', (YLeaf(YType.uint32, 'idle-time'), ['int'])),
                ('username', (YLeaf(YType.str, 'username'), ['str'])),
                ('ignore_auth_port', (YLeaf(YType.boolean, 'ignore-auth-port'), ['bool'])),
            ])
            self.retransmit = None
            self.dead_time = None
            self.key = None
            self.timeout = None
            self.ignore_accounting_port = None
            self.idle_time = None
            self.username = None
            self.ignore_auth_port = None

            self.hosts = Aaa.Radius.Hosts()
            self.hosts.parent = self
            self._children_name_map["hosts"] = "hosts"

            self.dead_criteria = Aaa.Radius.DeadCriteria()
            self.dead_criteria.parent = self
            self._children_name_map["dead_criteria"] = "dead-criteria"

            self.disallow = Aaa.Radius.Disallow()
            self.disallow.parent = self
            self._children_name_map["disallow"] = "disallow"

            self.ipv6 = Aaa.Radius.Ipv6()
            self.ipv6.parent = self
            self._children_name_map["ipv6"] = "ipv6"

            self.dynamic_authorization = Aaa.Radius.DynamicAuthorization()
            self.dynamic_authorization.parent = self
            self._children_name_map["dynamic_authorization"] = "dynamic-authorization"

            self.load_balance_options = Aaa.Radius.LoadBalanceOptions()
            self.load_balance_options.parent = self
            self._children_name_map["load_balance_options"] = "load-balance-options"

            self.vrfs = Aaa.Radius.Vrfs()
            self.vrfs.parent = self
            self._children_name_map["vrfs"] = "vrfs"

            self.throttle = Aaa.Radius.Throttle()
            self.throttle.parent = self
            self._children_name_map["throttle"] = "throttle"

            self.vsa = Aaa.Radius.Vsa()
            self.vsa.parent = self
            self._children_name_map["vsa"] = "vsa"

            self.ipv4 = Aaa.Radius.Ipv4()
            self.ipv4.parent = self
            self._children_name_map["ipv4"] = "ipv4"

            self.radius_attribute = Aaa.Radius.RadiusAttribute()
            self.radius_attribute.parent = self
            self._children_name_map["radius_attribute"] = "radius-attribute"

            self.attributes = Aaa.Radius.Attributes()
            self.attributes.parent = self
            self._children_name_map["attributes"] = "attributes"

            self.source_port = Aaa.Radius.SourcePort()
            self.source_port.parent = self
            self._children_name_map["source_port"] = "source-port"
            self._segment_path = lambda: "Cisco-IOS-XR-aaa-protocol-radius-cfg:radius"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.Radius, ['retransmit', 'dead_time', 'key', 'timeout', 'ignore_accounting_port', 'idle_time', 'username', 'ignore_auth_port'], name, value)


        class Hosts(Entity):
            """
            List of RADIUS servers
            
            .. attribute:: host
            
            	Instance of a RADIUS server
            	**type**\: list of  		 :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Hosts.Host>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Radius.Hosts, self).__init__()

                self.yang_name = "hosts"
                self.yang_parent_name = "radius"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("host", ("host", Aaa.Radius.Hosts.Host))])
                self._leafs = OrderedDict()

                self.host = YList(self)
                self._segment_path = lambda: "hosts"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Radius.Hosts, [], name, value)


            class Host(Entity):
                """
                Instance of a RADIUS server
                
                .. attribute:: ordering_index  (key)
                
                	This is used to sort the servers in the order of precedence
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ip_address  (key)
                
                	IP address of RADIUS server
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: auth_port_number  (key)
                
                	Authentication Port number (standard port 1645)
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: acct_port_number  (key)
                
                	Accounting Port number (standard port 1646)
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: host_retransmit
                
                	Number of times to retransmit a request to the RADIUS server
                	**type**\: int
                
                	**range:** 1..100
                
                	**default value**\: 3
                
                .. attribute:: host_timeout
                
                	Time to wait for a RADIUS server to reply
                	**type**\: int
                
                	**range:** 1..1000
                
                	**default value**\: 5
                
                .. attribute:: host_key
                
                	RADIUS encryption key
                	**type**\: str
                
                	**pattern:** (!.+)\|([^!].+)
                
                .. attribute:: ignore_accounting_port
                
                	Time to wait for a RADIUS server to reply
                	**type**\: bool
                
                .. attribute:: idle_time
                
                	Idle time for RADIUS server
                	**type**\: int
                
                	**range:** 1..1000
                
                	**default value**\: 5
                
                .. attribute:: username
                
                	Username to be tested for automated testing
                	**type**\: str
                
                .. attribute:: ignore_auth_port
                
                	Time to wait for a RADIUS server to reply
                	**type**\: bool
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Aaa.Radius.Hosts.Host, self).__init__()

                    self.yang_name = "host"
                    self.yang_parent_name = "hosts"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['ordering_index','ip_address','auth_port_number','acct_port_number']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ordering_index', (YLeaf(YType.uint32, 'ordering-index'), ['int'])),
                        ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
                        ('auth_port_number', (YLeaf(YType.uint16, 'auth-port-number'), ['int'])),
                        ('acct_port_number', (YLeaf(YType.uint16, 'acct-port-number'), ['int'])),
                        ('host_retransmit', (YLeaf(YType.uint32, 'host-retransmit'), ['int'])),
                        ('host_timeout', (YLeaf(YType.uint32, 'host-timeout'), ['int'])),
                        ('host_key', (YLeaf(YType.str, 'host-key'), ['str'])),
                        ('ignore_accounting_port', (YLeaf(YType.boolean, 'ignore-accounting-port'), ['bool'])),
                        ('idle_time', (YLeaf(YType.uint32, 'idle-time'), ['int'])),
                        ('username', (YLeaf(YType.str, 'username'), ['str'])),
                        ('ignore_auth_port', (YLeaf(YType.boolean, 'ignore-auth-port'), ['bool'])),
                    ])
                    self.ordering_index = None
                    self.ip_address = None
                    self.auth_port_number = None
                    self.acct_port_number = None
                    self.host_retransmit = None
                    self.host_timeout = None
                    self.host_key = None
                    self.ignore_accounting_port = None
                    self.idle_time = None
                    self.username = None
                    self.ignore_auth_port = None
                    self._segment_path = lambda: "host" + "[ordering-index='" + str(self.ordering_index) + "']" + "[ip-address='" + str(self.ip_address) + "']" + "[auth-port-number='" + str(self.auth_port_number) + "']" + "[acct-port-number='" + str(self.acct_port_number) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/hosts/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Radius.Hosts.Host, ['ordering_index', 'ip_address', 'auth_port_number', 'acct_port_number', 'host_retransmit', 'host_timeout', 'host_key', 'ignore_accounting_port', 'idle_time', 'username', 'ignore_auth_port'], name, value)


        class DeadCriteria(Entity):
            """
            RADIUS server dead criteria
            
            .. attribute:: tries
            
            	The number of consecutive timeouts the router must experience in order to mark the server as dead. All transmissions, including the initial transmit and all retransmits, will be counted
            	**type**\: int
            
            	**range:** 1..100
            
            .. attribute:: time
            
            	The minimum amount of time which must elapse since the router last received a valid RADIUS packet from the server prior to marking it dead
            	**type**\: int
            
            	**range:** 1..120
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Radius.DeadCriteria, self).__init__()

                self.yang_name = "dead-criteria"
                self.yang_parent_name = "radius"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('tries', (YLeaf(YType.uint32, 'tries'), ['int'])),
                    ('time', (YLeaf(YType.uint32, 'time'), ['int'])),
                ])
                self.tries = None
                self.time = None
                self._segment_path = lambda: "dead-criteria"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Radius.DeadCriteria, ['tries', 'time'], name, value)


        class Disallow(Entity):
            """
            disallow null\-username
            
            .. attribute:: null_username
            
            	Disallow null\-username
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Radius.Disallow, self).__init__()

                self.yang_name = "disallow"
                self.yang_parent_name = "radius"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('null_username', (YLeaf(YType.uint32, 'null-username'), ['int'])),
                ])
                self.null_username = None
                self._segment_path = lambda: "disallow"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Radius.Disallow, ['null_username'], name, value)


        class Ipv6(Entity):
            """
            IPv6 configuration
            
            .. attribute:: dscp
            
            	Specify the DSCP value
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`AaaDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaDscpValue>`
            
            		**type**\: int
            
            			**range:** 0..63
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Radius.Ipv6, self).__init__()

                self.yang_name = "ipv6"
                self.yang_parent_name = "radius"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dscp', (YLeaf(YType.str, 'dscp'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaDscpValue', ''),'int'])),
                ])
                self.dscp = None
                self._segment_path = lambda: "ipv6"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Radius.Ipv6, ['dscp'], name, value)


        class DynamicAuthorization(Entity):
            """
            RADIUS dynamic authorization
            
            .. attribute:: clients
            
            	Client data
            	**type**\:  :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.DynamicAuthorization.Clients>`
            
            .. attribute:: ignore
            
            	Ignore option for server key or session key
            	**type**\:  :py:class:`AaaSelectKey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaSelectKey>`
            
            .. attribute:: port
            
            	Specify the COA server port to listen on
            	**type**\: int
            
            	**range:** 1000..5000
            
            .. attribute:: authentication_type
            
            	RADIUS  dynamic  authorization  type
            	**type**\:  :py:class:`AaaAuthentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaAuthentication>`
            
            .. attribute:: server_key
            
            	RADIUS CoA client encryption key
            	**type**\: str
            
            	**pattern:** (!.+)\|([^!].+)
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Radius.DynamicAuthorization, self).__init__()

                self.yang_name = "dynamic-authorization"
                self.yang_parent_name = "radius"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("clients", ("clients", Aaa.Radius.DynamicAuthorization.Clients))])
                self._leafs = OrderedDict([
                    ('ignore', (YLeaf(YType.enumeration, 'ignore'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaSelectKey', '')])),
                    ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                    ('authentication_type', (YLeaf(YType.enumeration, 'authentication-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaAuthentication', '')])),
                    ('server_key', (YLeaf(YType.str, 'server-key'), ['str'])),
                ])
                self.ignore = None
                self.port = None
                self.authentication_type = None
                self.server_key = None

                self.clients = Aaa.Radius.DynamicAuthorization.Clients()
                self.clients.parent = self
                self._children_name_map["clients"] = "clients"
                self._segment_path = lambda: "dynamic-authorization"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Radius.DynamicAuthorization, ['ignore', 'port', 'authentication_type', 'server_key'], name, value)


            class Clients(Entity):
                """
                Client data
                
                .. attribute:: client
                
                	Client data
                	**type**\: list of  		 :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.DynamicAuthorization.Clients.Client>`
                
                .. attribute:: client_vrf_name
                
                	Client data
                	**type**\: list of  		 :py:class:`ClientVrfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.DynamicAuthorization.Clients.ClientVrfName>`
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Aaa.Radius.DynamicAuthorization.Clients, self).__init__()

                    self.yang_name = "clients"
                    self.yang_parent_name = "dynamic-authorization"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("client", ("client", Aaa.Radius.DynamicAuthorization.Clients.Client)), ("client-vrf-name", ("client_vrf_name", Aaa.Radius.DynamicAuthorization.Clients.ClientVrfName))])
                    self._leafs = OrderedDict()

                    self.client = YList(self)
                    self.client_vrf_name = YList(self)
                    self._segment_path = lambda: "clients"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/dynamic-authorization/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Radius.DynamicAuthorization.Clients, [], name, value)


                class Client(Entity):
                    """
                    Client data
                    
                    .. attribute:: ip_address  (key)
                    
                    	IP address of COA client
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: server_key
                    
                    	RADIUS CoA client encryption key
                    	**type**\: str
                    
                    	**pattern:** (!.+)\|([^!].+)
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Aaa.Radius.DynamicAuthorization.Clients.Client, self).__init__()

                        self.yang_name = "client"
                        self.yang_parent_name = "clients"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['ip_address']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
                            ('server_key', (YLeaf(YType.str, 'server-key'), ['str'])),
                        ])
                        self.ip_address = None
                        self.server_key = None
                        self._segment_path = lambda: "client" + "[ip-address='" + str(self.ip_address) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/dynamic-authorization/clients/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Radius.DynamicAuthorization.Clients.Client, ['ip_address', 'server_key'], name, value)


                class ClientVrfName(Entity):
                    """
                    Client data
                    
                    .. attribute:: vrf_name  (key)
                    
                    	VRF name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: ip_address  (key)
                    
                    	IP address of COA client
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: server_key
                    
                    	RADIUS CoA client encryption key
                    	**type**\: str
                    
                    	**pattern:** (!.+)\|([^!].+)
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Aaa.Radius.DynamicAuthorization.Clients.ClientVrfName, self).__init__()

                        self.yang_name = "client-vrf-name"
                        self.yang_parent_name = "clients"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['vrf_name','ip_address']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
                            ('server_key', (YLeaf(YType.str, 'server-key'), ['str'])),
                        ])
                        self.vrf_name = None
                        self.ip_address = None
                        self.server_key = None
                        self._segment_path = lambda: "client-vrf-name" + "[vrf-name='" + str(self.vrf_name) + "']" + "[ip-address='" + str(self.ip_address) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/dynamic-authorization/clients/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Radius.DynamicAuthorization.Clients.ClientVrfName, ['vrf_name', 'ip_address', 'server_key'], name, value)


        class LoadBalanceOptions(Entity):
            """
            Radius load\-balancing options
            
            .. attribute:: load_balance_method
            
            	Method by which the next host will be picked
            	**type**\:  :py:class:`LoadBalanceMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Radius.LoadBalanceOptions, self).__init__()

                self.yang_name = "load-balance-options"
                self.yang_parent_name = "radius"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("load-balance-method", ("load_balance_method", Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod))])
                self._leafs = OrderedDict()

                self.load_balance_method = Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod()
                self.load_balance_method.parent = self
                self._children_name_map["load_balance_method"] = "load-balance-method"
                self._segment_path = lambda: "load-balance-options"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Radius.LoadBalanceOptions, [], name, value)


            class LoadBalanceMethod(Entity):
                """
                Method by which the next host will be picked
                
                .. attribute:: batch_size
                
                	Batch size for selection of the server
                	**type**\:  :py:class:`BatchSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod.BatchSize>`
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod, self).__init__()

                    self.yang_name = "load-balance-method"
                    self.yang_parent_name = "load-balance-options"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("batch-size", ("batch_size", Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod.BatchSize))])
                    self._leafs = OrderedDict()

                    self.batch_size = Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod.BatchSize()
                    self.batch_size.parent = self
                    self._children_name_map["batch_size"] = "batch-size"
                    self._segment_path = lambda: "load-balance-method"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/load-balance-options/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod, [], name, value)


                class BatchSize(Entity):
                    """
                    Batch size for selection of the server
                    
                    .. attribute:: batch_size
                    
                    	Batch size for selection of the server
                    	**type**\: int
                    
                    	**range:** 1..1500
                    
                    	**default value**\: 25
                    
                    .. attribute:: ignore_preferred_server
                    
                    	Disable preferred server for this Server Group
                    	**type**\: bool
                    
                    	**default value**\: true
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod.BatchSize, self).__init__()

                        self.yang_name = "batch-size"
                        self.yang_parent_name = "load-balance-method"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('batch_size', (YLeaf(YType.uint32, 'batch-size'), ['int'])),
                            ('ignore_preferred_server', (YLeaf(YType.boolean, 'ignore-preferred-server'), ['bool'])),
                        ])
                        self.batch_size = None
                        self.ignore_preferred_server = None
                        self._segment_path = lambda: "batch-size"
                        self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/load-balance-options/load-balance-method/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod.BatchSize, ['batch_size', 'ignore_preferred_server'], name, value)


        class Vrfs(Entity):
            """
            List of VRFs
            
            .. attribute:: vrf
            
            	A VRF
            	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Vrfs.Vrf>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Radius.Vrfs, self).__init__()

                self.yang_name = "vrfs"
                self.yang_parent_name = "radius"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("vrf", ("vrf", Aaa.Radius.Vrfs.Vrf))])
                self._leafs = OrderedDict()

                self.vrf = YList(self)
                self._segment_path = lambda: "vrfs"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Radius.Vrfs, [], name, value)


            class Vrf(Entity):
                """
                A VRF
                
                .. attribute:: vrf_name  (key)
                
                	VRF name. Specify 'default' for defalut VRF
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: source_interface
                
                	Specify interface for source address in RADIUS packets
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Aaa.Radius.Vrfs.Vrf, self).__init__()

                    self.yang_name = "vrf"
                    self.yang_parent_name = "vrfs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['vrf_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                        ('source_interface', (YLeaf(YType.str, 'source-interface'), ['str'])),
                    ])
                    self.vrf_name = None
                    self.source_interface = None
                    self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/vrfs/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Radius.Vrfs.Vrf, ['vrf_name', 'source_interface'], name, value)


        class Throttle(Entity):
            """
            Radius throttling options
            
            .. attribute:: access
            
            	To flow control the number of access requests sent to a radius server
            	**type**\: int
            
            	**range:** 0..65535
            
            	**default value**\: 0
            
            .. attribute:: accounting
            
            	To flow control the number of accounting requests sent to a radius server
            	**type**\: int
            
            	**range:** 0..65535
            
            	**default value**\: 0
            
            .. attribute:: access_timeout
            
            	Specify the number of timeouts exceeding which a throttled access request is dropped
            	**type**\: int
            
            	**range:** 1..10
            
            	**default value**\: 3
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Radius.Throttle, self).__init__()

                self.yang_name = "throttle"
                self.yang_parent_name = "radius"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('access', (YLeaf(YType.uint32, 'access'), ['int'])),
                    ('accounting', (YLeaf(YType.uint32, 'accounting'), ['int'])),
                    ('access_timeout', (YLeaf(YType.uint32, 'access-timeout'), ['int'])),
                ])
                self.access = None
                self.accounting = None
                self.access_timeout = None
                self._segment_path = lambda: "throttle"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Radius.Throttle, ['access', 'accounting', 'access_timeout'], name, value)


        class Vsa(Entity):
            """
            Unknown VSA (Vendor Specific Attribute) ignore
            configuration for RADIUS server
            
            .. attribute:: attribute
            
            	Vendor Specific Attribute
            	**type**\:  :py:class:`Attribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Vsa.Attribute>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Radius.Vsa, self).__init__()

                self.yang_name = "vsa"
                self.yang_parent_name = "radius"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("attribute", ("attribute", Aaa.Radius.Vsa.Attribute))])
                self._leafs = OrderedDict()

                self.attribute = Aaa.Radius.Vsa.Attribute()
                self.attribute.parent = self
                self._children_name_map["attribute"] = "attribute"
                self._segment_path = lambda: "vsa"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Radius.Vsa, [], name, value)


            class Attribute(Entity):
                """
                Vendor Specific Attribute
                
                .. attribute:: ignore
                
                	Ignore the VSA
                	**type**\:  :py:class:`Ignore <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Vsa.Attribute.Ignore>`
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Aaa.Radius.Vsa.Attribute, self).__init__()

                    self.yang_name = "attribute"
                    self.yang_parent_name = "vsa"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ignore", ("ignore", Aaa.Radius.Vsa.Attribute.Ignore))])
                    self._leafs = OrderedDict()

                    self.ignore = Aaa.Radius.Vsa.Attribute.Ignore()
                    self.ignore.parent = self
                    self._children_name_map["ignore"] = "ignore"
                    self._segment_path = lambda: "attribute"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/vsa/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Radius.Vsa.Attribute, [], name, value)


                class Ignore(Entity):
                    """
                    Ignore the VSA
                    
                    .. attribute:: unknown
                    
                    	Ignore the VSA and no prefix will reject the unknown VSA
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Aaa.Radius.Vsa.Attribute.Ignore, self).__init__()

                        self.yang_name = "ignore"
                        self.yang_parent_name = "attribute"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('unknown', (YLeaf(YType.empty, 'unknown'), ['Empty'])),
                        ])
                        self.unknown = None
                        self._segment_path = lambda: "ignore"
                        self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/vsa/attribute/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Radius.Vsa.Attribute.Ignore, ['unknown'], name, value)


        class Ipv4(Entity):
            """
            IPv4 configuration
            
            .. attribute:: dscp
            
            	Specify the DSCP value
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`AaaDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaDscpValue>`
            
            		**type**\: int
            
            			**range:** 0..63
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Radius.Ipv4, self).__init__()

                self.yang_name = "ipv4"
                self.yang_parent_name = "radius"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dscp', (YLeaf(YType.str, 'dscp'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaDscpValue', ''),'int'])),
                ])
                self.dscp = None
                self._segment_path = lambda: "ipv4"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Radius.Ipv4, ['dscp'], name, value)


        class RadiusAttribute(Entity):
            """
            attribute
            
            .. attribute:: filter_id_11
            
            	Filter\-Id attribute configuration
            	**type**\:  :py:class:`FilterId11 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute.FilterId11>`
            
            .. attribute:: acct_multi_session_id
            
            	Acct\-Session\-Id attribute(44)
            	**type**\:  :py:class:`AcctMultiSessionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute.AcctMultiSessionId>`
            
            .. attribute:: acct_session_id
            
            	Acct\-Session\-Id attribute(44)
            	**type**\:  :py:class:`AcctSessionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute.AcctSessionId>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Radius.RadiusAttribute, self).__init__()

                self.yang_name = "radius-attribute"
                self.yang_parent_name = "radius"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("filter-id-11", ("filter_id_11", Aaa.Radius.RadiusAttribute.FilterId11)), ("acct-multi-session-id", ("acct_multi_session_id", Aaa.Radius.RadiusAttribute.AcctMultiSessionId)), ("acct-session-id", ("acct_session_id", Aaa.Radius.RadiusAttribute.AcctSessionId))])
                self._leafs = OrderedDict()

                self.filter_id_11 = Aaa.Radius.RadiusAttribute.FilterId11()
                self.filter_id_11.parent = self
                self._children_name_map["filter_id_11"] = "filter-id-11"

                self.acct_multi_session_id = Aaa.Radius.RadiusAttribute.AcctMultiSessionId()
                self.acct_multi_session_id.parent = self
                self._children_name_map["acct_multi_session_id"] = "acct-multi-session-id"

                self.acct_session_id = Aaa.Radius.RadiusAttribute.AcctSessionId()
                self.acct_session_id.parent = self
                self._children_name_map["acct_session_id"] = "acct-session-id"
                self._segment_path = lambda: "radius-attribute"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Radius.RadiusAttribute, [], name, value)


            class FilterId11(Entity):
                """
                Filter\-Id attribute configuration
                
                .. attribute:: defaults
                
                	Set the attribute default direction
                	**type**\:  :py:class:`Defaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute.FilterId11.Defaults>`
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Aaa.Radius.RadiusAttribute.FilterId11, self).__init__()

                    self.yang_name = "filter-id-11"
                    self.yang_parent_name = "radius-attribute"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("defaults", ("defaults", Aaa.Radius.RadiusAttribute.FilterId11.Defaults))])
                    self._leafs = OrderedDict()

                    self.defaults = Aaa.Radius.RadiusAttribute.FilterId11.Defaults()
                    self.defaults.parent = self
                    self._children_name_map["defaults"] = "defaults"
                    self._segment_path = lambda: "filter-id-11"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/radius-attribute/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Radius.RadiusAttribute.FilterId11, [], name, value)


                class Defaults(Entity):
                    """
                    Set the attribute default direction
                    
                    .. attribute:: direction
                    
                    	Filtering is applied to ingress(inbound)/egress(outbound) packets only
                    	**type**\:  :py:class:`AaaDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaDirection>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Aaa.Radius.RadiusAttribute.FilterId11.Defaults, self).__init__()

                        self.yang_name = "defaults"
                        self.yang_parent_name = "filter-id-11"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaDirection', '')])),
                        ])
                        self.direction = None
                        self._segment_path = lambda: "defaults"
                        self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/radius-attribute/filter-id-11/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Radius.RadiusAttribute.FilterId11.Defaults, ['direction'], name, value)


            class AcctMultiSessionId(Entity):
                """
                Acct\-Session\-Id attribute(44)
                
                .. attribute:: include_parent_session_id
                
                	Prepend Acct\-Session\-Id attribute with Nas\-Port\-Id
                	**type**\:  :py:class:`IncludeParentSessionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute.AcctMultiSessionId.IncludeParentSessionId>`
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Aaa.Radius.RadiusAttribute.AcctMultiSessionId, self).__init__()

                    self.yang_name = "acct-multi-session-id"
                    self.yang_parent_name = "radius-attribute"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("include-parent-session-id", ("include_parent_session_id", Aaa.Radius.RadiusAttribute.AcctMultiSessionId.IncludeParentSessionId))])
                    self._leafs = OrderedDict()

                    self.include_parent_session_id = Aaa.Radius.RadiusAttribute.AcctMultiSessionId.IncludeParentSessionId()
                    self.include_parent_session_id.parent = self
                    self._children_name_map["include_parent_session_id"] = "include-parent-session-id"
                    self._segment_path = lambda: "acct-multi-session-id"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/radius-attribute/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Radius.RadiusAttribute.AcctMultiSessionId, [], name, value)


                class IncludeParentSessionId(Entity):
                    """
                    Prepend Acct\-Session\-Id attribute with
                    Nas\-Port\-Id
                    
                    .. attribute:: config
                    
                    	false/true
                    	**type**\:  :py:class:`AaaConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaConfig>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Aaa.Radius.RadiusAttribute.AcctMultiSessionId.IncludeParentSessionId, self).__init__()

                        self.yang_name = "include-parent-session-id"
                        self.yang_parent_name = "acct-multi-session-id"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('config', (YLeaf(YType.enumeration, 'config'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaConfig', '')])),
                        ])
                        self.config = None
                        self._segment_path = lambda: "include-parent-session-id"
                        self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/radius-attribute/acct-multi-session-id/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Radius.RadiusAttribute.AcctMultiSessionId.IncludeParentSessionId, ['config'], name, value)


            class AcctSessionId(Entity):
                """
                Acct\-Session\-Id attribute(44)
                
                .. attribute:: prepend_nas_port_id
                
                	Prepend Acct\-Session\-Id attribute with Nas\-Port\-Id
                	**type**\:  :py:class:`PrependNasPortId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.RadiusAttribute.AcctSessionId.PrependNasPortId>`
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Aaa.Radius.RadiusAttribute.AcctSessionId, self).__init__()

                    self.yang_name = "acct-session-id"
                    self.yang_parent_name = "radius-attribute"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("prepend-nas-port-id", ("prepend_nas_port_id", Aaa.Radius.RadiusAttribute.AcctSessionId.PrependNasPortId))])
                    self._leafs = OrderedDict()

                    self.prepend_nas_port_id = Aaa.Radius.RadiusAttribute.AcctSessionId.PrependNasPortId()
                    self.prepend_nas_port_id.parent = self
                    self._children_name_map["prepend_nas_port_id"] = "prepend-nas-port-id"
                    self._segment_path = lambda: "acct-session-id"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/radius-attribute/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Radius.RadiusAttribute.AcctSessionId, [], name, value)


                class PrependNasPortId(Entity):
                    """
                    Prepend Acct\-Session\-Id attribute with
                    Nas\-Port\-Id
                    
                    .. attribute:: config
                    
                    	false/true
                    	**type**\:  :py:class:`AaaConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg.AaaConfig>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Aaa.Radius.RadiusAttribute.AcctSessionId.PrependNasPortId, self).__init__()

                        self.yang_name = "prepend-nas-port-id"
                        self.yang_parent_name = "acct-session-id"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('config', (YLeaf(YType.enumeration, 'config'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaConfig', '')])),
                        ])
                        self.config = None
                        self._segment_path = lambda: "prepend-nas-port-id"
                        self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/radius-attribute/acct-session-id/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Radius.RadiusAttribute.AcctSessionId.PrependNasPortId, ['config'], name, value)


        class Attributes(Entity):
            """
            Table of attribute list
            
            .. attribute:: attribute
            
            	Attribute list name
            	**type**\: list of  		 :py:class:`Attribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Attributes.Attribute>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Radius.Attributes, self).__init__()

                self.yang_name = "attributes"
                self.yang_parent_name = "radius"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("attribute", ("attribute", Aaa.Radius.Attributes.Attribute))])
                self._leafs = OrderedDict()

                self.attribute = YList(self)
                self._segment_path = lambda: "attributes"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Radius.Attributes, [], name, value)


            class Attribute(Entity):
                """
                Attribute list name
                
                .. attribute:: attribute_list_name  (key)
                
                	Attribute list name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: vendor_ids
                
                	Vendor Specific Attribute
                	**type**\:  :py:class:`VendorIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Attributes.Attribute.VendorIds>`
                
                .. attribute:: attribute
                
                	Specify RADIUS attribute
                	**type**\: str
                
                

                """

                _prefix = 'aaa-protocol-radius-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Aaa.Radius.Attributes.Attribute, self).__init__()

                    self.yang_name = "attribute"
                    self.yang_parent_name = "attributes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['attribute_list_name']
                    self._child_classes = OrderedDict([("vendor-ids", ("vendor_ids", Aaa.Radius.Attributes.Attribute.VendorIds))])
                    self._leafs = OrderedDict([
                        ('attribute_list_name', (YLeaf(YType.str, 'attribute-list-name'), ['str'])),
                        ('attribute', (YLeaf(YType.str, 'attribute'), ['str'])),
                    ])
                    self.attribute_list_name = None
                    self.attribute = None

                    self.vendor_ids = Aaa.Radius.Attributes.Attribute.VendorIds()
                    self.vendor_ids.parent = self
                    self._children_name_map["vendor_ids"] = "vendor-ids"
                    self._segment_path = lambda: "attribute" + "[attribute-list-name='" + str(self.attribute_list_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/attributes/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Radius.Attributes.Attribute, ['attribute_list_name', 'attribute'], name, value)


                class VendorIds(Entity):
                    """
                    Vendor Specific Attribute
                    
                    .. attribute:: vendor_id
                    
                    	Vendor ID of vsa
                    	**type**\: list of  		 :py:class:`VendorId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Attributes.Attribute.VendorIds.VendorId>`
                    
                    

                    """

                    _prefix = 'aaa-protocol-radius-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Aaa.Radius.Attributes.Attribute.VendorIds, self).__init__()

                        self.yang_name = "vendor-ids"
                        self.yang_parent_name = "attribute"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("vendor-id", ("vendor_id", Aaa.Radius.Attributes.Attribute.VendorIds.VendorId))])
                        self._leafs = OrderedDict()

                        self.vendor_id = YList(self)
                        self._segment_path = lambda: "vendor-ids"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Radius.Attributes.Attribute.VendorIds, [], name, value)


                    class VendorId(Entity):
                        """
                        Vendor ID of vsa
                        
                        .. attribute:: vendor_id  (key)
                        
                        	Vendor Id of vsa
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: vendor_type
                        
                        	Vendor Type of vsa
                        	**type**\: list of  		 :py:class:`VendorType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Attributes.Attribute.VendorIds.VendorId.VendorType>`
                        
                        

                        """

                        _prefix = 'aaa-protocol-radius-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(Aaa.Radius.Attributes.Attribute.VendorIds.VendorId, self).__init__()

                            self.yang_name = "vendor-id"
                            self.yang_parent_name = "vendor-ids"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['vendor_id']
                            self._child_classes = OrderedDict([("vendor-type", ("vendor_type", Aaa.Radius.Attributes.Attribute.VendorIds.VendorId.VendorType))])
                            self._leafs = OrderedDict([
                                ('vendor_id', (YLeaf(YType.uint32, 'vendor-id'), ['int'])),
                            ])
                            self.vendor_id = None

                            self.vendor_type = YList(self)
                            self._segment_path = lambda: "vendor-id" + "[vendor-id='" + str(self.vendor_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aaa.Radius.Attributes.Attribute.VendorIds.VendorId, ['vendor_id'], name, value)


                        class VendorType(Entity):
                            """
                            Vendor Type of vsa
                            
                            .. attribute:: vendor_type  (key)
                            
                            	Vendor Type of vsa
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: attribute_name
                            
                            	Attribute Name of vsa
                            	**type**\: list of  		 :py:class:`AttributeName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Attributes.Attribute.VendorIds.VendorId.VendorType.AttributeName>`
                            
                            

                            """

                            _prefix = 'aaa-protocol-radius-cfg'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(Aaa.Radius.Attributes.Attribute.VendorIds.VendorId.VendorType, self).__init__()

                                self.yang_name = "vendor-type"
                                self.yang_parent_name = "vendor-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['vendor_type']
                                self._child_classes = OrderedDict([("attribute-name", ("attribute_name", Aaa.Radius.Attributes.Attribute.VendorIds.VendorId.VendorType.AttributeName))])
                                self._leafs = OrderedDict([
                                    ('vendor_type', (YLeaf(YType.uint32, 'vendor-type'), ['int'])),
                                ])
                                self.vendor_type = None

                                self.attribute_name = YList(self)
                                self._segment_path = lambda: "vendor-type" + "[vendor-type='" + str(self.vendor_type) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Aaa.Radius.Attributes.Attribute.VendorIds.VendorId.VendorType, ['vendor_type'], name, value)


                            class AttributeName(Entity):
                                """
                                Attribute Name of vsa
                                
                                .. attribute:: attribute_name  (key)
                                
                                	Attribute Name of vsa
                                	**type**\: str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: attribute_name_absent
                                
                                	AttributeName of vsa is absent
                                	**type**\: list of  		 :py:class:`AttributeNameAbsent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Attributes.Attribute.VendorIds.VendorId.VendorType.AttributeName.AttributeNameAbsent>`
                                
                                

                                """

                                _prefix = 'aaa-protocol-radius-cfg'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(Aaa.Radius.Attributes.Attribute.VendorIds.VendorId.VendorType.AttributeName, self).__init__()

                                    self.yang_name = "attribute-name"
                                    self.yang_parent_name = "vendor-type"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['attribute_name']
                                    self._child_classes = OrderedDict([("attribute-name-absent", ("attribute_name_absent", Aaa.Radius.Attributes.Attribute.VendorIds.VendorId.VendorType.AttributeName.AttributeNameAbsent))])
                                    self._leafs = OrderedDict([
                                        ('attribute_name', (YLeaf(YType.str, 'attribute-name'), ['str'])),
                                    ])
                                    self.attribute_name = None

                                    self.attribute_name_absent = YList(self)
                                    self._segment_path = lambda: "attribute-name" + "[attribute-name='" + str(self.attribute_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Aaa.Radius.Attributes.Attribute.VendorIds.VendorId.VendorType.AttributeName, ['attribute_name'], name, value)


                                class AttributeNameAbsent(Entity):
                                    """
                                    AttributeName of vsa is absent
                                    
                                    .. attribute:: attribute_name_absent  (key)
                                    
                                    	AttributeName of vsa is absent
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: attribute_name_present
                                    
                                    	AttributeName of vsa is present
                                    	**type**\: list of  		 :py:class:`AttributeNamePresent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Radius.Attributes.Attribute.VendorIds.VendorId.VendorType.AttributeName.AttributeNameAbsent.AttributeNamePresent>`
                                    
                                    

                                    """

                                    _prefix = 'aaa-protocol-radius-cfg'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(Aaa.Radius.Attributes.Attribute.VendorIds.VendorId.VendorType.AttributeName.AttributeNameAbsent, self).__init__()

                                        self.yang_name = "attribute-name-absent"
                                        self.yang_parent_name = "attribute-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['attribute_name_absent']
                                        self._child_classes = OrderedDict([("attribute-name-present", ("attribute_name_present", Aaa.Radius.Attributes.Attribute.VendorIds.VendorId.VendorType.AttributeName.AttributeNameAbsent.AttributeNamePresent))])
                                        self._leafs = OrderedDict([
                                            ('attribute_name_absent', (YLeaf(YType.uint32, 'attribute-name-absent'), ['int'])),
                                        ])
                                        self.attribute_name_absent = None

                                        self.attribute_name_present = YList(self)
                                        self._segment_path = lambda: "attribute-name-absent" + "[attribute-name-absent='" + str(self.attribute_name_absent) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Aaa.Radius.Attributes.Attribute.VendorIds.VendorId.VendorType.AttributeName.AttributeNameAbsent, ['attribute_name_absent'], name, value)


                                    class AttributeNamePresent(Entity):
                                        """
                                        AttributeName of vsa is present
                                        
                                        .. attribute:: attribute_name_present  (key)
                                        
                                        	AttributeName of vsa is present
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'aaa-protocol-radius-cfg'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(Aaa.Radius.Attributes.Attribute.VendorIds.VendorId.VendorType.AttributeName.AttributeNameAbsent.AttributeNamePresent, self).__init__()

                                            self.yang_name = "attribute-name-present"
                                            self.yang_parent_name = "attribute-name-absent"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['attribute_name_present']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('attribute_name_present', (YLeaf(YType.uint32, 'attribute-name-present'), ['int'])),
                                            ])
                                            self.attribute_name_present = None
                                            self._segment_path = lambda: "attribute-name-present" + "[attribute-name-present='" + str(self.attribute_name_present) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Aaa.Radius.Attributes.Attribute.VendorIds.VendorId.VendorType.AttributeName.AttributeNameAbsent.AttributeNamePresent, ['attribute_name_present'], name, value)


        class SourcePort(Entity):
            """
            Source port
            
            .. attribute:: extended
            
            	Enable source\-port extend 
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'aaa-protocol-radius-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Radius.SourcePort, self).__init__()

                self.yang_name = "source-port"
                self.yang_parent_name = "radius"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('extended', (YLeaf(YType.empty, 'extended'), ['Empty'])),
                ])
                self.extended = None
                self._segment_path = lambda: "source-port"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-protocol-radius-cfg:radius/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Radius.SourcePort, ['extended'], name, value)


    class Diameter(Entity):
        """
        Diameter base protocol
        
        .. attribute:: gy
        
        	Start diameter policy\-if
        	**type**\:  :py:class:`Gy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Gy>`
        
        .. attribute:: origin
        
        	Origin sub commands
        	**type**\:  :py:class:`Origin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Origin>`
        
        .. attribute:: nas
        
        	Start diameter Nas
        	**type**\:  :py:class:`Nas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Nas>`
        
        .. attribute:: diameter_tls
        
        	TLS sub commands
        	**type**\:  :py:class:`DiameterTls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.DiameterTls>`
        
        .. attribute:: peers
        
        	List of diameter peers
        	**type**\:  :py:class:`Peers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Peers>`
        
        .. attribute:: diams
        
        	Attribute list configuration for test command
        	**type**\:  :py:class:`Diams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Diams>`
        
        .. attribute:: gx
        
        	Start diameter policy\-if
        	**type**\:  :py:class:`Gx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Gx>`
        
        .. attribute:: services
        
        	Service sub commands
        	**type**\:  :py:class:`Services <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Services>`
        
        .. attribute:: diameter_timer
        
        	Timers used for the peer
        	**type**\:  :py:class:`DiameterTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.DiameterTimer>`
        
        .. attribute:: vendor
        
        	Vendor specific
        	**type**\:  :py:class:`Vendor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Vendor>`
        
        .. attribute:: source_interface
        
        	Specify interface for source address in DIAMETER packets
        	**type**\: str
        
        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
        
        

        """

        _prefix = 'aaa-diameter-cfg'
        _revision = '2017-11-13'

        def __init__(self):
            super(Aaa.Diameter, self).__init__()

            self.yang_name = "diameter"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("gy", ("gy", Aaa.Diameter.Gy)), ("origin", ("origin", Aaa.Diameter.Origin)), ("nas", ("nas", Aaa.Diameter.Nas)), ("diameter-tls", ("diameter_tls", Aaa.Diameter.DiameterTls)), ("peers", ("peers", Aaa.Diameter.Peers)), ("diams", ("diams", Aaa.Diameter.Diams)), ("gx", ("gx", Aaa.Diameter.Gx)), ("services", ("services", Aaa.Diameter.Services)), ("diameter-timer", ("diameter_timer", Aaa.Diameter.DiameterTimer)), ("vendor", ("vendor", Aaa.Diameter.Vendor))])
            self._leafs = OrderedDict([
                ('source_interface', (YLeaf(YType.str, 'source-interface'), ['str'])),
            ])
            self.source_interface = None

            self.gy = Aaa.Diameter.Gy()
            self.gy.parent = self
            self._children_name_map["gy"] = "gy"

            self.origin = Aaa.Diameter.Origin()
            self.origin.parent = self
            self._children_name_map["origin"] = "origin"

            self.nas = Aaa.Diameter.Nas()
            self.nas.parent = self
            self._children_name_map["nas"] = "nas"

            self.diameter_tls = Aaa.Diameter.DiameterTls()
            self.diameter_tls.parent = self
            self._children_name_map["diameter_tls"] = "diameter-tls"

            self.peers = Aaa.Diameter.Peers()
            self.peers.parent = self
            self._children_name_map["peers"] = "peers"

            self.diams = Aaa.Diameter.Diams()
            self.diams.parent = self
            self._children_name_map["diams"] = "diams"

            self.gx = Aaa.Diameter.Gx()
            self.gx.parent = self
            self._children_name_map["gx"] = "gx"

            self.services = Aaa.Diameter.Services()
            self.services.parent = self
            self._children_name_map["services"] = "services"

            self.diameter_timer = Aaa.Diameter.DiameterTimer()
            self.diameter_timer.parent = self
            self._children_name_map["diameter_timer"] = "diameter-timer"

            self.vendor = Aaa.Diameter.Vendor()
            self.vendor.parent = self
            self._children_name_map["vendor"] = "vendor"
            self._segment_path = lambda: "Cisco-IOS-XR-aaa-diameter-cfg:diameter"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.Diameter, ['source_interface'], name, value)


        class Gy(Entity):
            """
            Start diameter policy\-if
            
            .. attribute:: retransmit
            
            	Set retransmit count
            	**type**\: int
            
            	**range:** 1..10
            
            .. attribute:: dest_host
            
            	Destination Host name in FQDN format
            	**type**\: str
            
            .. attribute:: tx_timer
            
            	Transaction timer value
            	**type**\: int
            
            	**range:** 6..1000
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2017-11-13'

            def __init__(self):
                super(Aaa.Diameter.Gy, self).__init__()

                self.yang_name = "gy"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('retransmit', (YLeaf(YType.uint32, 'retransmit'), ['int'])),
                    ('dest_host', (YLeaf(YType.str, 'dest-host'), ['str'])),
                    ('tx_timer', (YLeaf(YType.uint32, 'tx-timer'), ['int'])),
                ])
                self.retransmit = None
                self.dest_host = None
                self.tx_timer = None
                self._segment_path = lambda: "gy"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.Gy, ['retransmit', 'dest_host', 'tx_timer'], name, value)


        class Origin(Entity):
            """
            Origin sub commands
            
            .. attribute:: realm
            
            	Origin Realm String
            	**type**\: str
            
            .. attribute:: host
            
            	Host name in FQDN format
            	**type**\: str
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2017-11-13'

            def __init__(self):
                super(Aaa.Diameter.Origin, self).__init__()

                self.yang_name = "origin"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('realm', (YLeaf(YType.str, 'realm'), ['str'])),
                    ('host', (YLeaf(YType.str, 'host'), ['str'])),
                ])
                self.realm = None
                self.host = None
                self._segment_path = lambda: "origin"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.Origin, ['realm', 'host'], name, value)


        class Nas(Entity):
            """
            Start diameter Nas
            
            .. attribute:: dest_host
            
            	Destination Host name in FQDN format
            	**type**\: str
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2017-11-13'

            def __init__(self):
                super(Aaa.Diameter.Nas, self).__init__()

                self.yang_name = "nas"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dest_host', (YLeaf(YType.str, 'dest-host'), ['str'])),
                ])
                self.dest_host = None
                self._segment_path = lambda: "nas"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.Nas, ['dest_host'], name, value)


        class DiameterTls(Entity):
            """
            TLS sub commands
            
            .. attribute:: trustpoint
            
            	Trustpoint label to be used
            	**type**\: str
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2017-11-13'

            def __init__(self):
                super(Aaa.Diameter.DiameterTls, self).__init__()

                self.yang_name = "diameter-tls"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('trustpoint', (YLeaf(YType.str, 'trustpoint'), ['str'])),
                ])
                self.trustpoint = None
                self._segment_path = lambda: "diameter-tls"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.DiameterTls, ['trustpoint'], name, value)


        class Peers(Entity):
            """
            List of diameter peers
            
            .. attribute:: peer
            
            	Diameter peer instance
            	**type**\: list of  		 :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Peers.Peer>`
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2017-11-13'

            def __init__(self):
                super(Aaa.Diameter.Peers, self).__init__()

                self.yang_name = "peers"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("peer", ("peer", Aaa.Diameter.Peers.Peer))])
                self._leafs = OrderedDict()

                self.peer = YList(self)
                self._segment_path = lambda: "peers"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.Peers, [], name, value)


            class Peer(Entity):
                """
                Diameter peer instance
                
                .. attribute:: peer_name  (key)
                
                	Name for the diameter peer configuration
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: peer_timer
                
                	Timers used for the peer
                	**type**\:  :py:class:`PeerTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Peers.Peer.PeerTimer>`
                
                .. attribute:: peer_type
                
                	Peer Type
                	**type**\:  :py:class:`PeerType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Peers.Peer.PeerType>`
                
                .. attribute:: host_destination
                
                	Destination host information
                	**type**\: str
                
                .. attribute:: ipv4_address
                
                	IPv4 address of diameter server
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: realm_destination
                
                	Realm to which the peer belongs to
                	**type**\: str
                
                .. attribute:: tcp_transport
                
                	Specify a Diameter transport protocol
                	**type**\: int
                
                	**range:** 1..65535
                
                .. attribute:: source_interface
                
                	Specify interface for source address in DIAMETER packets
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: ipv6_address
                
                	IPv6 address of diameter server
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: tls_transport
                
                	Specify a Diameter security type
                	**type**\: int
                
                	**range:** 0..1
                
                .. attribute:: vrf_ip
                
                	VRF the peer belongs to
                	**type**\: str
                
                

                """

                _prefix = 'aaa-diameter-cfg'
                _revision = '2017-11-13'

                def __init__(self):
                    super(Aaa.Diameter.Peers.Peer, self).__init__()

                    self.yang_name = "peer"
                    self.yang_parent_name = "peers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['peer_name']
                    self._child_classes = OrderedDict([("peer-timer", ("peer_timer", Aaa.Diameter.Peers.Peer.PeerTimer)), ("peer-type", ("peer_type", Aaa.Diameter.Peers.Peer.PeerType))])
                    self._leafs = OrderedDict([
                        ('peer_name', (YLeaf(YType.str, 'peer-name'), ['str'])),
                        ('host_destination', (YLeaf(YType.str, 'host-destination'), ['str'])),
                        ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                        ('realm_destination', (YLeaf(YType.str, 'realm-destination'), ['str'])),
                        ('tcp_transport', (YLeaf(YType.uint32, 'tcp-transport'), ['int'])),
                        ('source_interface', (YLeaf(YType.str, 'source-interface'), ['str'])),
                        ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                        ('tls_transport', (YLeaf(YType.uint32, 'tls-transport'), ['int'])),
                        ('vrf_ip', (YLeaf(YType.str, 'vrf-ip'), ['str'])),
                    ])
                    self.peer_name = None
                    self.host_destination = None
                    self.ipv4_address = None
                    self.realm_destination = None
                    self.tcp_transport = None
                    self.source_interface = None
                    self.ipv6_address = None
                    self.tls_transport = None
                    self.vrf_ip = None

                    self.peer_timer = Aaa.Diameter.Peers.Peer.PeerTimer()
                    self.peer_timer.parent = self
                    self._children_name_map["peer_timer"] = "peer-timer"

                    self.peer_type = Aaa.Diameter.Peers.Peer.PeerType()
                    self.peer_type.parent = self
                    self._children_name_map["peer_type"] = "peer-type"
                    self._segment_path = lambda: "peer" + "[peer-name='" + str(self.peer_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/peers/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Diameter.Peers.Peer, ['peer_name', 'host_destination', 'ipv4_address', 'realm_destination', 'tcp_transport', 'source_interface', 'ipv6_address', 'tls_transport', 'vrf_ip'], name, value)


                class PeerTimer(Entity):
                    """
                    Timers used for the peer
                    
                    .. attribute:: transaction
                    
                    	Timer value in seconds
                    	**type**\: int
                    
                    	**range:** 6..1000
                    
                    .. attribute:: connection
                    
                    	Timer value in seconds
                    	**type**\: int
                    
                    	**range:** 6..1000
                    
                    .. attribute:: watchdog
                    
                    	Timer value in seconds
                    	**type**\: int
                    
                    	**range:** 6..1000
                    
                    

                    """

                    _prefix = 'aaa-diameter-cfg'
                    _revision = '2017-11-13'

                    def __init__(self):
                        super(Aaa.Diameter.Peers.Peer.PeerTimer, self).__init__()

                        self.yang_name = "peer-timer"
                        self.yang_parent_name = "peer"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('transaction', (YLeaf(YType.uint32, 'transaction'), ['int'])),
                            ('connection', (YLeaf(YType.uint32, 'connection'), ['int'])),
                            ('watchdog', (YLeaf(YType.uint32, 'watchdog'), ['int'])),
                        ])
                        self.transaction = None
                        self.connection = None
                        self.watchdog = None
                        self._segment_path = lambda: "peer-timer"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Diameter.Peers.Peer.PeerTimer, ['transaction', 'connection', 'watchdog'], name, value)


                class PeerType(Entity):
                    """
                    Peer Type
                    
                    .. attribute:: server
                    
                    	Enabled or disabled
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'aaa-diameter-cfg'
                    _revision = '2017-11-13'

                    def __init__(self):
                        super(Aaa.Diameter.Peers.Peer.PeerType, self).__init__()

                        self.yang_name = "peer-type"
                        self.yang_parent_name = "peer"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('server', (YLeaf(YType.boolean, 'server'), ['bool'])),
                        ])
                        self.server = None
                        self._segment_path = lambda: "peer-type"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Diameter.Peers.Peer.PeerType, ['server'], name, value)


        class Diams(Entity):
            """
            Attribute list configuration for test command
            
            .. attribute:: diam
            
            	attribute list configuration
            	**type**\: list of  		 :py:class:`Diam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Diams.Diam>`
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2017-11-13'

            def __init__(self):
                super(Aaa.Diameter.Diams, self).__init__()

                self.yang_name = "diams"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("diam", ("diam", Aaa.Diameter.Diams.Diam))])
                self._leafs = OrderedDict()

                self.diam = YList(self)
                self._segment_path = lambda: "diams"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.Diams, [], name, value)


            class Diam(Entity):
                """
                attribute list configuration
                
                .. attribute:: list_id  (key)
                
                	attribute list number
                	**type**\: int
                
                	**range:** 0..99
                
                .. attribute:: diam_attr_defs
                
                	Specify an attribute definition
                	**type**\:  :py:class:`DiamAttrDefs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Diams.Diam.DiamAttrDefs>`
                
                

                """

                _prefix = 'aaa-diameter-cfg'
                _revision = '2017-11-13'

                def __init__(self):
                    super(Aaa.Diameter.Diams.Diam, self).__init__()

                    self.yang_name = "diam"
                    self.yang_parent_name = "diams"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['list_id']
                    self._child_classes = OrderedDict([("diam-attr-defs", ("diam_attr_defs", Aaa.Diameter.Diams.Diam.DiamAttrDefs))])
                    self._leafs = OrderedDict([
                        ('list_id', (YLeaf(YType.uint32, 'list-id'), ['int'])),
                    ])
                    self.list_id = None

                    self.diam_attr_defs = Aaa.Diameter.Diams.Diam.DiamAttrDefs()
                    self.diam_attr_defs.parent = self
                    self._children_name_map["diam_attr_defs"] = "diam-attr-defs"
                    self._segment_path = lambda: "diam" + "[list-id='" + str(self.list_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/diams/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Diameter.Diams.Diam, ['list_id'], name, value)


                class DiamAttrDefs(Entity):
                    """
                    Specify an attribute definition
                    
                    .. attribute:: diam_attr_def
                    
                    	vendor id
                    	**type**\: list of  		 :py:class:`DiamAttrDef <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef>`
                    
                    

                    """

                    _prefix = 'aaa-diameter-cfg'
                    _revision = '2017-11-13'

                    def __init__(self):
                        super(Aaa.Diameter.Diams.Diam.DiamAttrDefs, self).__init__()

                        self.yang_name = "diam-attr-defs"
                        self.yang_parent_name = "diam"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("diam-attr-def", ("diam_attr_def", Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef))])
                        self._leafs = OrderedDict()

                        self.diam_attr_def = YList(self)
                        self._segment_path = lambda: "diam-attr-defs"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Diameter.Diams.Diam.DiamAttrDefs, [], name, value)


                    class DiamAttrDef(Entity):
                        """
                        vendor id
                        
                        .. attribute:: vendor_id  (key)
                        
                        	value for vendor id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: attribute_id  (key)
                        
                        	enter attribute id
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: diam_attr_value
                        
                        	attr subcommands
                        	**type**\:  :py:class:`DiamAttrValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef.DiamAttrValue>`
                        
                        

                        """

                        _prefix = 'aaa-diameter-cfg'
                        _revision = '2017-11-13'

                        def __init__(self):
                            super(Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef, self).__init__()

                            self.yang_name = "diam-attr-def"
                            self.yang_parent_name = "diam-attr-defs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['vendor_id','attribute_id']
                            self._child_classes = OrderedDict([("diam-attr-value", ("diam_attr_value", Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef.DiamAttrValue))])
                            self._leafs = OrderedDict([
                                ('vendor_id', (YLeaf(YType.uint32, 'vendor-id'), ['int'])),
                                ('attribute_id', (YLeaf(YType.uint32, 'attribute-id'), ['int'])),
                            ])
                            self.vendor_id = None
                            self.attribute_id = None

                            self.diam_attr_value = Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef.DiamAttrValue()
                            self.diam_attr_value.parent = self
                            self._children_name_map["diam_attr_value"] = "diam-attr-value"
                            self._segment_path = lambda: "diam-attr-def" + "[vendor-id='" + str(self.vendor_id) + "']" + "[attribute-id='" + str(self.attribute_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef, ['vendor_id', 'attribute_id'], name, value)


                        class DiamAttrValue(Entity):
                            """
                            attr subcommands
                            
                            .. attribute:: type_string
                            
                            	String type
                            	**type**\: str
                            
                            .. attribute:: type_ipv4_address
                            
                            	IPv4 address type
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: type_binary
                            
                            	Binary type
                            	**type**\: str
                            
                            .. attribute:: type_boolean
                            
                            	Boolean type
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: type_enum
                            
                            	Enumeration type
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: type_grouped
                            
                            	Grouped attribute
                            	**type**\: int
                            
                            	**range:** 0..99
                            
                            .. attribute:: type_ulong
                            
                            	Numeric type
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: type_identity
                            
                            	Diameter\-identity type
                            	**type**\: str
                            
                            .. attribute:: data_type
                            
                            	Dataypte of attribute
                            	**type**\: int
                            
                            	**range:** 0..23
                            
                            .. attribute:: mandatory
                            
                            	Is mandatory?
                            	**type**\: int
                            
                            	**range:** 0..1
                            
                            

                            """

                            _prefix = 'aaa-diameter-cfg'
                            _revision = '2017-11-13'

                            def __init__(self):
                                super(Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef.DiamAttrValue, self).__init__()

                                self.yang_name = "diam-attr-value"
                                self.yang_parent_name = "diam-attr-def"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('type_string', (YLeaf(YType.str, 'type-string'), ['str'])),
                                    ('type_ipv4_address', (YLeaf(YType.str, 'type-ipv4-address'), ['str'])),
                                    ('type_binary', (YLeaf(YType.str, 'type-binary'), ['str'])),
                                    ('type_boolean', (YLeaf(YType.uint32, 'type-boolean'), ['int'])),
                                    ('type_enum', (YLeaf(YType.uint32, 'type-enum'), ['int'])),
                                    ('type_grouped', (YLeaf(YType.uint32, 'type-grouped'), ['int'])),
                                    ('type_ulong', (YLeaf(YType.uint32, 'type-ulong'), ['int'])),
                                    ('type_identity', (YLeaf(YType.str, 'type-identity'), ['str'])),
                                    ('data_type', (YLeaf(YType.uint32, 'data-type'), ['int'])),
                                    ('mandatory', (YLeaf(YType.uint32, 'mandatory'), ['int'])),
                                ])
                                self.type_string = None
                                self.type_ipv4_address = None
                                self.type_binary = None
                                self.type_boolean = None
                                self.type_enum = None
                                self.type_grouped = None
                                self.type_ulong = None
                                self.type_identity = None
                                self.data_type = None
                                self.mandatory = None
                                self._segment_path = lambda: "diam-attr-value"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef.DiamAttrValue, ['type_string', 'type_ipv4_address', 'type_binary', 'type_boolean', 'type_enum', 'type_grouped', 'type_ulong', 'type_identity', 'data_type', 'mandatory'], name, value)


        class Gx(Entity):
            """
            Start diameter policy\-if
            
            .. attribute:: retransmit
            
            	Set retransmit count
            	**type**\: int
            
            	**range:** 1..10
            
            .. attribute:: dest_host
            
            	Destination Host name in FQDN format
            	**type**\: str
            
            .. attribute:: tx_timer
            
            	Transaction timer value
            	**type**\: int
            
            	**range:** 6..1000
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2017-11-13'

            def __init__(self):
                super(Aaa.Diameter.Gx, self).__init__()

                self.yang_name = "gx"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('retransmit', (YLeaf(YType.uint32, 'retransmit'), ['int'])),
                    ('dest_host', (YLeaf(YType.str, 'dest-host'), ['str'])),
                    ('tx_timer', (YLeaf(YType.uint32, 'tx-timer'), ['int'])),
                ])
                self.retransmit = None
                self.dest_host = None
                self.tx_timer = None
                self._segment_path = lambda: "gx"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.Gx, ['retransmit', 'dest_host', 'tx_timer'], name, value)


        class Services(Entity):
            """
            Service sub commands
            
            .. attribute:: service
            
            	Diameter Service instance
            	**type**\: list of  		 :py:class:`Service <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Services.Service>`
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2017-11-13'

            def __init__(self):
                super(Aaa.Diameter.Services, self).__init__()

                self.yang_name = "services"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("service", ("service", Aaa.Diameter.Services.Service))])
                self._leafs = OrderedDict()

                self.service = YList(self)
                self._segment_path = lambda: "services"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.Services, [], name, value)


            class Service(Entity):
                """
                Diameter Service instance
                
                .. attribute:: service_name  (key)
                
                	Name for the diameter Service configuration
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: monitoring_key
                
                	Name for the diameter Service Monitoring configuration
                	**type**\: str
                
                

                """

                _prefix = 'aaa-diameter-cfg'
                _revision = '2017-11-13'

                def __init__(self):
                    super(Aaa.Diameter.Services.Service, self).__init__()

                    self.yang_name = "service"
                    self.yang_parent_name = "services"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['service_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('service_name', (YLeaf(YType.str, 'service-name'), ['str'])),
                        ('monitoring_key', (YLeaf(YType.str, 'monitoring-key'), ['str'])),
                    ])
                    self.service_name = None
                    self.monitoring_key = None
                    self._segment_path = lambda: "service" + "[service-name='" + str(self.service_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/services/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Diameter.Services.Service, ['service_name', 'monitoring_key'], name, value)


        class DiameterTimer(Entity):
            """
            Timers used for the peer
            
            .. attribute:: transaction
            
            	Timer value in seconds
            	**type**\: int
            
            	**range:** 6..1000
            
            .. attribute:: connection
            
            	Timer value in seconds
            	**type**\: int
            
            	**range:** 6..1000
            
            .. attribute:: watchdog
            
            	Timer value in seconds
            	**type**\: int
            
            	**range:** 6..1000
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2017-11-13'

            def __init__(self):
                super(Aaa.Diameter.DiameterTimer, self).__init__()

                self.yang_name = "diameter-timer"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('transaction', (YLeaf(YType.uint32, 'transaction'), ['int'])),
                    ('connection', (YLeaf(YType.uint32, 'connection'), ['int'])),
                    ('watchdog', (YLeaf(YType.uint32, 'watchdog'), ['int'])),
                ])
                self.transaction = None
                self.connection = None
                self.watchdog = None
                self._segment_path = lambda: "diameter-timer"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.DiameterTimer, ['transaction', 'connection', 'watchdog'], name, value)


        class Vendor(Entity):
            """
            Vendor specific
            
            .. attribute:: supported
            
            	Supported vendors
            	**type**\:  :py:class:`Supported <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Diameter.Vendor.Supported>`
            
            

            """

            _prefix = 'aaa-diameter-cfg'
            _revision = '2017-11-13'

            def __init__(self):
                super(Aaa.Diameter.Vendor, self).__init__()

                self.yang_name = "vendor"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("supported", ("supported", Aaa.Diameter.Vendor.Supported))])
                self._leafs = OrderedDict()

                self.supported = Aaa.Diameter.Vendor.Supported()
                self.supported.parent = self
                self._children_name_map["supported"] = "supported"
                self._segment_path = lambda: "vendor"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.Vendor, [], name, value)


            class Supported(Entity):
                """
                Supported vendors
                
                .. attribute:: cisco
                
                	Cisco attribute support
                	**type**\: bool
                
                .. attribute:: threegpp
                
                	3GPP attribute support
                	**type**\: bool
                
                .. attribute:: etsi
                
                	Etsi attribute support
                	**type**\: bool
                
                .. attribute:: vodafone
                
                	Vodafone attribute support
                	**type**\: bool
                
                

                """

                _prefix = 'aaa-diameter-cfg'
                _revision = '2017-11-13'

                def __init__(self):
                    super(Aaa.Diameter.Vendor.Supported, self).__init__()

                    self.yang_name = "supported"
                    self.yang_parent_name = "vendor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('cisco', (YLeaf(YType.boolean, 'cisco'), ['bool'])),
                        ('threegpp', (YLeaf(YType.boolean, 'threegpp'), ['bool'])),
                        ('etsi', (YLeaf(YType.boolean, 'etsi'), ['bool'])),
                        ('vodafone', (YLeaf(YType.boolean, 'vodafone'), ['bool'])),
                    ])
                    self.cisco = None
                    self.threegpp = None
                    self.etsi = None
                    self.vodafone = None
                    self._segment_path = lambda: "supported"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-diameter-cfg:diameter/vendor/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Diameter.Vendor.Supported, ['cisco', 'threegpp', 'etsi', 'vodafone'], name, value)


    class Tacacs(Entity):
        """
        Modify TACACS+ query parameters
        
        .. attribute:: ipv6
        
        	IPv6 configuration
        	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Ipv6>`
        
        .. attribute:: hosts
        
        	Specify a TACACS+ server
        	**type**\:  :py:class:`Hosts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Hosts>`
        
        .. attribute:: ipv4
        
        	IPv4 configuration
        	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Ipv4>`
        
        .. attribute:: vrfs
        
        	List of VRFs
        	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Vrfs>`
        
        .. attribute:: key
        
        	Set TACACS+ encryption key
        	**type**\: str
        
        	**pattern:** (!.+)\|([^!].+)
        
        .. attribute:: timeout
        
        	Time to wait for a TACACS+ server to reply
        	**type**\: int
        
        	**range:** 1..1000
        
        	**default value**\: 5
        
        .. attribute:: single_connect
        
        	Use a single connection for all sessions for a given TACACS+ server
        	**type**\: bool
        
        	**default value**\: false
        
        

        """

        _prefix = 'aaa-tacacs-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(Aaa.Tacacs, self).__init__()

            self.yang_name = "tacacs"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ipv6", ("ipv6", Aaa.Tacacs.Ipv6)), ("hosts", ("hosts", Aaa.Tacacs.Hosts)), ("ipv4", ("ipv4", Aaa.Tacacs.Ipv4)), ("vrfs", ("vrfs", Aaa.Tacacs.Vrfs))])
            self._leafs = OrderedDict([
                ('key', (YLeaf(YType.str, 'key'), ['str'])),
                ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                ('single_connect', (YLeaf(YType.boolean, 'single-connect'), ['bool'])),
            ])
            self.key = None
            self.timeout = None
            self.single_connect = None

            self.ipv6 = Aaa.Tacacs.Ipv6()
            self.ipv6.parent = self
            self._children_name_map["ipv6"] = "ipv6"

            self.hosts = Aaa.Tacacs.Hosts()
            self.hosts.parent = self
            self._children_name_map["hosts"] = "hosts"

            self.ipv4 = Aaa.Tacacs.Ipv4()
            self.ipv4.parent = self
            self._children_name_map["ipv4"] = "ipv4"

            self.vrfs = Aaa.Tacacs.Vrfs()
            self.vrfs.parent = self
            self._children_name_map["vrfs"] = "vrfs"
            self._segment_path = lambda: "Cisco-IOS-XR-aaa-tacacs-cfg:tacacs"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.Tacacs, ['key', 'timeout', 'single_connect'], name, value)


        class Ipv6(Entity):
            """
            IPv6 configuration
            
            .. attribute:: dscp
            
            	Specify the DSCP value
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`TacacsDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_tacacs_cfg.TacacsDscpValue>`
            
            		**type**\: int
            
            			**range:** 0..63
            
            

            """

            _prefix = 'aaa-tacacs-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Tacacs.Ipv6, self).__init__()

                self.yang_name = "ipv6"
                self.yang_parent_name = "tacacs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dscp', (YLeaf(YType.str, 'dscp'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_tacacs_cfg', 'TacacsDscpValue', ''),'int'])),
                ])
                self.dscp = None
                self._segment_path = lambda: "ipv6"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Tacacs.Ipv6, ['dscp'], name, value)


        class Hosts(Entity):
            """
            Specify a TACACS+ server
            
            .. attribute:: host
            
            	One of the TACACS+ servers
            	**type**\: list of  		 :py:class:`Host <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Hosts.Host>`
            
            

            """

            _prefix = 'aaa-tacacs-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Tacacs.Hosts, self).__init__()

                self.yang_name = "hosts"
                self.yang_parent_name = "tacacs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("host", ("host", Aaa.Tacacs.Hosts.Host))])
                self._leafs = OrderedDict()

                self.host = YList(self)
                self._segment_path = lambda: "hosts"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Tacacs.Hosts, [], name, value)


            class Host(Entity):
                """
                One of the TACACS+ servers
                
                .. attribute:: ordering_index  (key)
                
                	This is used to sort the servers in the order of precedence
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ip_address  (key)
                
                	IP address of TACACS+ server
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: port_number  (key)
                
                	Port number (standard 49)
                	**type**\: int
                
                	**range:** 1..65535
                
                .. attribute:: key
                
                	Set TACACS+ encryption key
                	**type**\: str
                
                	**pattern:** (!.+)\|([^!].+)
                
                .. attribute:: timeout
                
                	Time to wait for a TACACS+ server to reply
                	**type**\: int
                
                	**range:** 1..1000
                
                	**default value**\: 5
                
                .. attribute:: single_connect
                
                	Use a single connection for all sessions for a given TACACS+ server
                	**type**\: bool
                
                	**default value**\: false
                
                

                """

                _prefix = 'aaa-tacacs-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Aaa.Tacacs.Hosts.Host, self).__init__()

                    self.yang_name = "host"
                    self.yang_parent_name = "hosts"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['ordering_index','ip_address','port_number']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ordering_index', (YLeaf(YType.uint32, 'ordering-index'), ['int'])),
                        ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
                        ('port_number', (YLeaf(YType.uint32, 'port-number'), ['int'])),
                        ('key', (YLeaf(YType.str, 'key'), ['str'])),
                        ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                        ('single_connect', (YLeaf(YType.boolean, 'single-connect'), ['bool'])),
                    ])
                    self.ordering_index = None
                    self.ip_address = None
                    self.port_number = None
                    self.key = None
                    self.timeout = None
                    self.single_connect = None
                    self._segment_path = lambda: "host" + "[ordering-index='" + str(self.ordering_index) + "']" + "[ip-address='" + str(self.ip_address) + "']" + "[port-number='" + str(self.port_number) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs/hosts/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Tacacs.Hosts.Host, ['ordering_index', 'ip_address', 'port_number', 'key', 'timeout', 'single_connect'], name, value)


        class Ipv4(Entity):
            """
            IPv4 configuration
            
            .. attribute:: dscp
            
            	Specify the DSCP value
            	**type**\: union of the below types:
            
            		**type**\:  :py:class:`TacacsDscpValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_tacacs_cfg.TacacsDscpValue>`
            
            		**type**\: int
            
            			**range:** 0..63
            
            

            """

            _prefix = 'aaa-tacacs-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Tacacs.Ipv4, self).__init__()

                self.yang_name = "ipv4"
                self.yang_parent_name = "tacacs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('dscp', (YLeaf(YType.str, 'dscp'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_tacacs_cfg', 'TacacsDscpValue', ''),'int'])),
                ])
                self.dscp = None
                self._segment_path = lambda: "ipv4"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Tacacs.Ipv4, ['dscp'], name, value)


        class Vrfs(Entity):
            """
            List of VRFs
            
            .. attribute:: vrf
            
            	A VRF
            	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg.Aaa.Tacacs.Vrfs.Vrf>`
            
            

            """

            _prefix = 'aaa-tacacs-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Tacacs.Vrfs, self).__init__()

                self.yang_name = "vrfs"
                self.yang_parent_name = "tacacs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("vrf", ("vrf", Aaa.Tacacs.Vrfs.Vrf))])
                self._leafs = OrderedDict()

                self.vrf = YList(self)
                self._segment_path = lambda: "vrfs"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Tacacs.Vrfs, [], name, value)


            class Vrf(Entity):
                """
                A VRF
                
                .. attribute:: vrf_name  (key)
                
                	VRF name. Specify 'default' for default VRF
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: source_interface
                
                	Specify interface for source address in TACACS+ packets
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                

                """

                _prefix = 'aaa-tacacs-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Aaa.Tacacs.Vrfs.Vrf, self).__init__()

                    self.yang_name = "vrf"
                    self.yang_parent_name = "vrfs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['vrf_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                        ('source_interface', (YLeaf(YType.str, 'source-interface'), ['str'])),
                    ])
                    self.vrf_name = None
                    self.source_interface = None
                    self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-lib-cfg:aaa/Cisco-IOS-XR-aaa-tacacs-cfg:tacacs/vrfs/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Tacacs.Vrfs.Vrf, ['vrf_name', 'source_interface'], name, value)

    def clone_ptr(self):
        self._top_entity = Aaa()
        return self._top_entity


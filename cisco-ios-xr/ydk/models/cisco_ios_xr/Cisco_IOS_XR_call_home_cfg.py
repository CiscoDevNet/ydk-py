""" Cisco_IOS_XR_call_home_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR call\-home package configuration.

This module contains definitions
for the following management objects\:
  call\-home\: Set CallHome parameters

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CallHomeDayOfWeek(Enum):
    """
    CallHomeDayOfWeek (Enum Class)

    Call home day of week

    .. data:: sunday = 0

    	Sunday

    .. data:: monday = 1

    	Monday

    .. data:: tuesday = 2

    	Tuesday

    .. data:: wednesday = 3

    	Wednesday

    .. data:: thursday = 4

    	Thursday

    .. data:: friday = 5

    	Friday

    .. data:: saturday = 6

    	Saturday

    """

    sunday = Enum.YLeaf(0, "sunday")

    monday = Enum.YLeaf(1, "monday")

    tuesday = Enum.YLeaf(2, "tuesday")

    wednesday = Enum.YLeaf(3, "wednesday")

    thursday = Enum.YLeaf(4, "thursday")

    friday = Enum.YLeaf(5, "friday")

    saturday = Enum.YLeaf(6, "saturday")


class CallHomeEventSeverity(Enum):
    """
    CallHomeEventSeverity (Enum Class)

    Call home event severity

    .. data:: debugging = 0

    	Debugging event

    .. data:: normal = 1

    	Normal event

    .. data:: notification = 2

    	Notification event

    .. data:: warning = 3

    	Warning event

    .. data:: minor = 4

    	Minor event

    .. data:: major = 5

    	Major event

    .. data:: critical = 6

    	Critical event

    .. data:: fatal = 7

    	Fatal event

    .. data:: disaster = 8

    	Disaster event

    .. data:: catastrophic = 9

    	Catastrophic event

    """

    debugging = Enum.YLeaf(0, "debugging")

    normal = Enum.YLeaf(1, "normal")

    notification = Enum.YLeaf(2, "notification")

    warning = Enum.YLeaf(3, "warning")

    minor = Enum.YLeaf(4, "minor")

    major = Enum.YLeaf(5, "major")

    critical = Enum.YLeaf(6, "critical")

    fatal = Enum.YLeaf(7, "fatal")

    disaster = Enum.YLeaf(8, "disaster")

    catastrophic = Enum.YLeaf(9, "catastrophic")


class CallHomeMailSendInterval(Enum):
    """
    CallHomeMailSendInterval (Enum Class)

    Call home mail send interval

    .. data:: daily = 0

    	Daily call-home message

    .. data:: weekly = 1

    	Weekly call-home message

    .. data:: monthly = 2

    	Monthly call-home message

    """

    daily = Enum.YLeaf(0, "daily")

    weekly = Enum.YLeaf(1, "weekly")

    monthly = Enum.YLeaf(2, "monthly")


class CallHomeTransMethod(Enum):
    """
    CallHomeTransMethod (Enum Class)

    Call home trans method

    .. data:: email = 1

    	To add email address to lthis profile

    .. data:: http = 2

    	To add destination address(1-200) characters

    """

    email = Enum.YLeaf(1, "email")

    http = Enum.YLeaf(2, "http")


class DataPrivacyLevel(Enum):
    """
    DataPrivacyLevel (Enum Class)

    Data privacy level

    .. data:: normal = 0

    	Normal

    .. data:: high = 1

    	High

    .. data:: host_name = 2

    	HostName

    """

    normal = Enum.YLeaf(0, "normal")

    high = Enum.YLeaf(1, "high")

    host_name = Enum.YLeaf(2, "host-name")


class SnapshotInterval(Enum):
    """
    SnapshotInterval (Enum Class)

    Snapshot interval

    .. data:: daily = 0

    	Daily call-home message

    .. data:: weekly = 1

    	Weekly call-home message

    .. data:: monthly = 2

    	Monthly call-home message

    """

    daily = Enum.YLeaf(0, "daily")

    weekly = Enum.YLeaf(1, "weekly")

    monthly = Enum.YLeaf(2, "monthly")



class CallHome(Entity):
    """
    Set CallHome parameters
    
    .. attribute:: mail_servers
    
    	List of call\-home mail\_server
    	**type**\:  :py:class:`MailServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.MailServers>`
    
    .. attribute:: syslog_throttling
    
    	Enable or disable call\-home syslog message throttling
    	**type**\:  :py:class:`SyslogThrottling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.SyslogThrottling>`
    
    .. attribute:: http_proxy
    
    	http proxy server address and port
    	**type**\:  :py:class:`HttpProxy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.HttpProxy>`
    
    .. attribute:: profiles
    
    	List of profiles
    	**type**\:  :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles>`
    
    .. attribute:: alert_groups
    
    	List of alert\-group
    	**type**\:  :py:class:`AlertGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.AlertGroups>`
    
    .. attribute:: data_privacies
    
    	Set call\-home data\-privacy
    	**type**\:  :py:class:`DataPrivacies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.DataPrivacies>`
    
    .. attribute:: alert_group_config
    
    	alert\-group config
    	**type**\:  :py:class:`AlertGroupConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.AlertGroupConfig>`
    
    .. attribute:: authorization
    
    	Config aaa authorization, default username is callhome
    	**type**\:  :py:class:`Authorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Authorization>`
    
    .. attribute:: customer_id
    
    	Customer identification for Cisco Smart Call Home
    	**type**\: str
    
    	**length:** 1..64
    
    .. attribute:: phone_number
    
    	Phone number of the contact person
    	**type**\: str
    
    	**length:** 1..17
    
    .. attribute:: contact_smart_licensing
    
    	System Contact is Smart Licensing
    	**type**\: bool
    
    .. attribute:: contact_email_address
    
    	Contact person's email address
    	**type**\: str
    
    	**length:** 1..194
    
    .. attribute:: rate_limit
    
    	Call\-home event trigger rate\-limit threshold per minute
    	**type**\: int
    
    	**range:** 1..5
    
    .. attribute:: site_id
    
    	Site identification for Cisco Smart Call Home
    	**type**\: str
    
    	**length:** 1..200
    
    .. attribute:: vrf
    
    	Vrf routing/forwarding instance name
    	**type**\: str
    
    	**length:** 1..32
    
    .. attribute:: street_address
    
    	Street address, city, state, and zip code
    	**type**\: str
    
    	**length:** 1..200
    
    .. attribute:: source_interface
    
    	Source interface name to send call\-home messages
    	**type**\: str
    
    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
    
    .. attribute:: contract_id
    
    	Contract identification for Cisco Smart Call Home
    	**type**\: str
    
    	**length:** 1..64
    
    .. attribute:: reply_to
    
    	Call home msg's reply\-to email address
    	**type**\: str
    
    .. attribute:: from_
    
    	Call home msg's from email address
    	**type**\: str
    
    .. attribute:: active
    
    	Enable call\-home service
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'call-home-cfg'
    _revision = '2018-06-21'

    def __init__(self):
        super(CallHome, self).__init__()
        self._top_entity = None

        self.yang_name = "call-home"
        self.yang_parent_name = "Cisco-IOS-XR-call-home-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("mail-servers", ("mail_servers", CallHome.MailServers)), ("syslog-throttling", ("syslog_throttling", CallHome.SyslogThrottling)), ("http-proxy", ("http_proxy", CallHome.HttpProxy)), ("profiles", ("profiles", CallHome.Profiles)), ("alert-groups", ("alert_groups", CallHome.AlertGroups)), ("data-privacies", ("data_privacies", CallHome.DataPrivacies)), ("alert-group-config", ("alert_group_config", CallHome.AlertGroupConfig)), ("authorization", ("authorization", CallHome.Authorization))])
        self._leafs = OrderedDict([
            ('customer_id', (YLeaf(YType.str, 'customer-id'), ['str'])),
            ('phone_number', (YLeaf(YType.str, 'phone-number'), ['str'])),
            ('contact_smart_licensing', (YLeaf(YType.boolean, 'contact-smart-licensing'), ['bool'])),
            ('contact_email_address', (YLeaf(YType.str, 'contact-email-address'), ['str'])),
            ('rate_limit', (YLeaf(YType.uint32, 'rate-limit'), ['int'])),
            ('site_id', (YLeaf(YType.str, 'site-id'), ['str'])),
            ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
            ('street_address', (YLeaf(YType.str, 'street-address'), ['str'])),
            ('source_interface', (YLeaf(YType.str, 'source-interface'), ['str'])),
            ('contract_id', (YLeaf(YType.str, 'contract-id'), ['str'])),
            ('reply_to', (YLeaf(YType.str, 'reply-to'), ['str'])),
            ('from_', (YLeaf(YType.str, 'from'), ['str'])),
            ('active', (YLeaf(YType.empty, 'active'), ['Empty'])),
        ])
        self.customer_id = None
        self.phone_number = None
        self.contact_smart_licensing = None
        self.contact_email_address = None
        self.rate_limit = None
        self.site_id = None
        self.vrf = None
        self.street_address = None
        self.source_interface = None
        self.contract_id = None
        self.reply_to = None
        self.from_ = None
        self.active = None

        self.mail_servers = CallHome.MailServers()
        self.mail_servers.parent = self
        self._children_name_map["mail_servers"] = "mail-servers"

        self.syslog_throttling = CallHome.SyslogThrottling()
        self.syslog_throttling.parent = self
        self._children_name_map["syslog_throttling"] = "syslog-throttling"

        self.http_proxy = CallHome.HttpProxy()
        self.http_proxy.parent = self
        self._children_name_map["http_proxy"] = "http-proxy"

        self.profiles = CallHome.Profiles()
        self.profiles.parent = self
        self._children_name_map["profiles"] = "profiles"

        self.alert_groups = CallHome.AlertGroups()
        self.alert_groups.parent = self
        self._children_name_map["alert_groups"] = "alert-groups"

        self.data_privacies = CallHome.DataPrivacies()
        self.data_privacies.parent = self
        self._children_name_map["data_privacies"] = "data-privacies"

        self.alert_group_config = CallHome.AlertGroupConfig()
        self.alert_group_config.parent = self
        self._children_name_map["alert_group_config"] = "alert-group-config"

        self.authorization = CallHome.Authorization()
        self.authorization.parent = self
        self._children_name_map["authorization"] = "authorization"
        self._segment_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CallHome, ['customer_id', 'phone_number', 'contact_smart_licensing', 'contact_email_address', 'rate_limit', 'site_id', 'vrf', 'street_address', 'source_interface', 'contract_id', 'reply_to', 'from_', 'active'], name, value)


    class MailServers(Entity):
        """
        List of call\-home mail\_server
        
        .. attribute:: mail_server
        
        	Email server
        	**type**\: list of  		 :py:class:`MailServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.MailServers.MailServer>`
        
        

        """

        _prefix = 'call-home-cfg'
        _revision = '2018-06-21'

        def __init__(self):
            super(CallHome.MailServers, self).__init__()

            self.yang_name = "mail-servers"
            self.yang_parent_name = "call-home"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mail-server", ("mail_server", CallHome.MailServers.MailServer))])
            self._leafs = OrderedDict()

            self.mail_server = YList(self)
            self._segment_path = lambda: "mail-servers"
            self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CallHome.MailServers, [], name, value)


        class MailServer(Entity):
            """
            Email server
            
            .. attribute:: mail_serv_address  (key)
            
            	Email server
            	**type**\: str
            
            .. attribute:: priority
            
            	Mail server with lower # will be used first
            	**type**\: int
            
            	**range:** 1..100
            
            

            """

            _prefix = 'call-home-cfg'
            _revision = '2018-06-21'

            def __init__(self):
                super(CallHome.MailServers.MailServer, self).__init__()

                self.yang_name = "mail-server"
                self.yang_parent_name = "mail-servers"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mail_serv_address']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mail_serv_address', (YLeaf(YType.str, 'mail-serv-address'), ['str'])),
                    ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                ])
                self.mail_serv_address = None
                self.priority = None
                self._segment_path = lambda: "mail-server" + "[mail-serv-address='" + str(self.mail_serv_address) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/mail-servers/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CallHome.MailServers.MailServer, ['mail_serv_address', 'priority'], name, value)


    class SyslogThrottling(Entity):
        """
        Enable or disable call\-home syslog message
        throttling
        
        .. attribute:: active
        
        	Active syslog throttling
        	**type**\: bool
        
        

        """

        _prefix = 'call-home-cfg'
        _revision = '2018-06-21'

        def __init__(self):
            super(CallHome.SyslogThrottling, self).__init__()

            self.yang_name = "syslog-throttling"
            self.yang_parent_name = "call-home"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('active', (YLeaf(YType.boolean, 'active'), ['bool'])),
            ])
            self.active = None
            self._segment_path = lambda: "syslog-throttling"
            self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CallHome.SyslogThrottling, ['active'], name, value)


    class HttpProxy(Entity):
        """
        http proxy server address and port
        
        .. attribute:: server_address
        
        	http proxy server address
        	**type**\: str
        
        .. attribute:: port
        
        	http proxy server's port
        	**type**\: int
        
        	**range:** 1..65535
        
        

        """

        _prefix = 'call-home-cfg'
        _revision = '2018-06-21'

        def __init__(self):
            super(CallHome.HttpProxy, self).__init__()

            self.yang_name = "http-proxy"
            self.yang_parent_name = "call-home"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('server_address', (YLeaf(YType.str, 'server-address'), ['str'])),
                ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
            ])
            self.server_address = None
            self.port = None
            self._segment_path = lambda: "http-proxy"
            self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CallHome.HttpProxy, ['server_address', 'port'], name, value)


    class Profiles(Entity):
        """
        List of profiles
        
        .. attribute:: profile
        
        	A specific profile
        	**type**\: list of  		 :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile>`
        
        

        """

        _prefix = 'call-home-cfg'
        _revision = '2018-06-21'

        def __init__(self):
            super(CallHome.Profiles, self).__init__()

            self.yang_name = "profiles"
            self.yang_parent_name = "call-home"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("profile", ("profile", CallHome.Profiles.Profile))])
            self._leafs = OrderedDict()

            self.profile = YList(self)
            self._segment_path = lambda: "profiles"
            self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CallHome.Profiles, [], name, value)


        class Profile(Entity):
            """
            A specific profile
            
            .. attribute:: profile_name  (key)
            
            	Profile name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: report_type
            
            	Choose what data to report
            	**type**\:  :py:class:`ReportType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.ReportType>`
            
            .. attribute:: methods
            
            	Transport method (http or email)
            	**type**\:  :py:class:`Methods <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.Methods>`
            
            .. attribute:: addresses
            
            	List of destination address
            	**type**\:  :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.Addresses>`
            
            .. attribute:: subscribe_alert_group
            
            	Subscribe to alert\-group
            	**type**\:  :py:class:`SubscribeAlertGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.SubscribeAlertGroup>`
            
            .. attribute:: create
            
            	Create a profile
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: message_format
            
            	none
            	**type**\: str
            
            .. attribute:: anonymous
            
            	Enable call\-home anonymous reporting only
            	**type**\: bool
            
            .. attribute:: message_size_limit
            
            	To specify message size limit for this profile
            	**type**\: int
            
            	**range:** 50..3145728
            
            .. attribute:: active
            
            	Activate the current profile
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'call-home-cfg'
            _revision = '2018-06-21'

            def __init__(self):
                super(CallHome.Profiles.Profile, self).__init__()

                self.yang_name = "profile"
                self.yang_parent_name = "profiles"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['profile_name']
                self._child_classes = OrderedDict([("report-type", ("report_type", CallHome.Profiles.Profile.ReportType)), ("methods", ("methods", CallHome.Profiles.Profile.Methods)), ("addresses", ("addresses", CallHome.Profiles.Profile.Addresses)), ("subscribe-alert-group", ("subscribe_alert_group", CallHome.Profiles.Profile.SubscribeAlertGroup))])
                self._leafs = OrderedDict([
                    ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                    ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                    ('message_format', (YLeaf(YType.str, 'message-format'), ['str'])),
                    ('anonymous', (YLeaf(YType.boolean, 'anonymous'), ['bool'])),
                    ('message_size_limit', (YLeaf(YType.uint32, 'message-size-limit'), ['int'])),
                    ('active', (YLeaf(YType.empty, 'active'), ['Empty'])),
                ])
                self.profile_name = None
                self.create = None
                self.message_format = None
                self.anonymous = None
                self.message_size_limit = None
                self.active = None

                self.report_type = CallHome.Profiles.Profile.ReportType()
                self.report_type.parent = self
                self._children_name_map["report_type"] = "report-type"

                self.methods = CallHome.Profiles.Profile.Methods()
                self.methods.parent = self
                self._children_name_map["methods"] = "methods"

                self.addresses = CallHome.Profiles.Profile.Addresses()
                self.addresses.parent = self
                self._children_name_map["addresses"] = "addresses"

                self.subscribe_alert_group = CallHome.Profiles.Profile.SubscribeAlertGroup()
                self.subscribe_alert_group.parent = self
                self._children_name_map["subscribe_alert_group"] = "subscribe-alert-group"
                self._segment_path = lambda: "profile" + "[profile-name='" + str(self.profile_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/profiles/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CallHome.Profiles.Profile, ['profile_name', 'create', 'message_format', 'anonymous', 'message_size_limit', 'active'], name, value)


            class ReportType(Entity):
                """
                Choose what data to report
                
                .. attribute:: reporting_callhome_data
                
                	Report smart call\-home data
                	**type**\:  :py:class:`ReportingCallhomeData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.ReportType.ReportingCallhomeData>`
                
                .. attribute:: reporting_licensing_data
                
                	Report smart licensing data
                	**type**\:  :py:class:`ReportingLicensingData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.ReportType.ReportingLicensingData>`
                
                

                """

                _prefix = 'call-home-cfg'
                _revision = '2018-06-21'

                def __init__(self):
                    super(CallHome.Profiles.Profile.ReportType, self).__init__()

                    self.yang_name = "report-type"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("reporting-callhome-data", ("reporting_callhome_data", CallHome.Profiles.Profile.ReportType.ReportingCallhomeData)), ("reporting-licensing-data", ("reporting_licensing_data", CallHome.Profiles.Profile.ReportType.ReportingLicensingData))])
                    self._leafs = OrderedDict()

                    self.reporting_callhome_data = CallHome.Profiles.Profile.ReportType.ReportingCallhomeData()
                    self.reporting_callhome_data.parent = self
                    self._children_name_map["reporting_callhome_data"] = "reporting-callhome-data"

                    self.reporting_licensing_data = CallHome.Profiles.Profile.ReportType.ReportingLicensingData()
                    self.reporting_licensing_data.parent = self
                    self._children_name_map["reporting_licensing_data"] = "reporting-licensing-data"
                    self._segment_path = lambda: "report-type"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(CallHome.Profiles.Profile.ReportType, [], name, value)


                class ReportingCallhomeData(Entity):
                    """
                    Report smart call\-home data
                    
                    .. attribute:: enable
                    
                    	Enable report smart call\-home data
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'call-home-cfg'
                    _revision = '2018-06-21'

                    def __init__(self):
                        super(CallHome.Profiles.Profile.ReportType.ReportingCallhomeData, self).__init__()

                        self.yang_name = "reporting-callhome-data"
                        self.yang_parent_name = "report-type"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                        ])
                        self.enable = None
                        self._segment_path = lambda: "reporting-callhome-data"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(CallHome.Profiles.Profile.ReportType.ReportingCallhomeData, ['enable'], name, value)


                class ReportingLicensingData(Entity):
                    """
                    Report smart licensing data
                    
                    .. attribute:: enable
                    
                    	Enable report smart licensing data
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'call-home-cfg'
                    _revision = '2018-06-21'

                    def __init__(self):
                        super(CallHome.Profiles.Profile.ReportType.ReportingLicensingData, self).__init__()

                        self.yang_name = "reporting-licensing-data"
                        self.yang_parent_name = "report-type"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                        ])
                        self.enable = None
                        self._segment_path = lambda: "reporting-licensing-data"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(CallHome.Profiles.Profile.ReportType.ReportingLicensingData, ['enable'], name, value)


            class Methods(Entity):
                """
                Transport method (http or email)
                
                .. attribute:: method
                
                	Transport method
                	**type**\: list of  		 :py:class:`Method <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.Methods.Method>`
                
                

                """

                _prefix = 'call-home-cfg'
                _revision = '2018-06-21'

                def __init__(self):
                    super(CallHome.Profiles.Profile.Methods, self).__init__()

                    self.yang_name = "methods"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("method", ("method", CallHome.Profiles.Profile.Methods.Method))])
                    self._leafs = OrderedDict()

                    self.method = YList(self)
                    self._segment_path = lambda: "methods"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(CallHome.Profiles.Profile.Methods, [], name, value)


                class Method(Entity):
                    """
                    Transport method
                    
                    .. attribute:: method  (key)
                    
                    	Transport Method
                    	**type**\:  :py:class:`CallHomeTransMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHomeTransMethod>`
                    
                    .. attribute:: enable
                    
                    	Enable this transport method
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'call-home-cfg'
                    _revision = '2018-06-21'

                    def __init__(self):
                        super(CallHome.Profiles.Profile.Methods.Method, self).__init__()

                        self.yang_name = "method"
                        self.yang_parent_name = "methods"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['method']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('method', (YLeaf(YType.enumeration, 'method'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg', 'CallHomeTransMethod', '')])),
                            ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                        ])
                        self.method = None
                        self.enable = None
                        self._segment_path = lambda: "method" + "[method='" + str(self.method) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(CallHome.Profiles.Profile.Methods.Method, ['method', 'enable'], name, value)


            class Addresses(Entity):
                """
                List of destination address
                
                .. attribute:: address
                
                	A specific address
                	**type**\: list of  		 :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.Addresses.Address>`
                
                

                """

                _prefix = 'call-home-cfg'
                _revision = '2018-06-21'

                def __init__(self):
                    super(CallHome.Profiles.Profile.Addresses, self).__init__()

                    self.yang_name = "addresses"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("address", ("address", CallHome.Profiles.Profile.Addresses.Address))])
                    self._leafs = OrderedDict()

                    self.address = YList(self)
                    self._segment_path = lambda: "addresses"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(CallHome.Profiles.Profile.Addresses, [], name, value)


                class Address(Entity):
                    """
                    A specific address
                    
                    .. attribute:: method  (key)
                    
                    	Transpotation Method
                    	**type**\:  :py:class:`CallHomeTransMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHomeTransMethod>`
                    
                    .. attribute:: destination_addr  (key)
                    
                    	Destination address (1\-200) characters
                    	**type**\: str
                    
                    	**length:** 1..200
                    
                    .. attribute:: enable
                    
                    	Set the address
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'call-home-cfg'
                    _revision = '2018-06-21'

                    def __init__(self):
                        super(CallHome.Profiles.Profile.Addresses.Address, self).__init__()

                        self.yang_name = "address"
                        self.yang_parent_name = "addresses"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['method','destination_addr']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('method', (YLeaf(YType.enumeration, 'method'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg', 'CallHomeTransMethod', '')])),
                            ('destination_addr', (YLeaf(YType.str, 'destination-addr'), ['str'])),
                            ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                        ])
                        self.method = None
                        self.destination_addr = None
                        self.enable = None
                        self._segment_path = lambda: "address" + "[method='" + str(self.method) + "']" + "[destination-addr='" + str(self.destination_addr) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(CallHome.Profiles.Profile.Addresses.Address, ['method', 'destination_addr', 'enable'], name, value)


            class SubscribeAlertGroup(Entity):
                """
                Subscribe to alert\-group
                
                .. attribute:: environment
                
                	environmental info
                	**type**\:  :py:class:`Environment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.SubscribeAlertGroup.Environment>`
                
                .. attribute:: configuration
                
                	configuration info
                	**type**\:  :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.SubscribeAlertGroup.Configuration>`
                
                .. attribute:: snapshot
                
                	snapshot info
                	**type**\:  :py:class:`Snapshot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.SubscribeAlertGroup.Snapshot>`
                
                .. attribute:: inventory
                
                	inventory info
                	**type**\:  :py:class:`Inventory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.SubscribeAlertGroup.Inventory>`
                
                .. attribute:: crash
                
                	Crash info
                	**type**\:  :py:class:`Crash <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.SubscribeAlertGroup.Crash>`
                
                .. attribute:: syslogs
                
                	syslog info
                	**type**\:  :py:class:`Syslogs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.SubscribeAlertGroup.Syslogs>`
                
                

                """

                _prefix = 'call-home-cfg'
                _revision = '2018-06-21'

                def __init__(self):
                    super(CallHome.Profiles.Profile.SubscribeAlertGroup, self).__init__()

                    self.yang_name = "subscribe-alert-group"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("environment", ("environment", CallHome.Profiles.Profile.SubscribeAlertGroup.Environment)), ("configuration", ("configuration", CallHome.Profiles.Profile.SubscribeAlertGroup.Configuration)), ("snapshot", ("snapshot", CallHome.Profiles.Profile.SubscribeAlertGroup.Snapshot)), ("inventory", ("inventory", CallHome.Profiles.Profile.SubscribeAlertGroup.Inventory)), ("crash", ("crash", CallHome.Profiles.Profile.SubscribeAlertGroup.Crash)), ("syslogs", ("syslogs", CallHome.Profiles.Profile.SubscribeAlertGroup.Syslogs))])
                    self._leafs = OrderedDict()

                    self.environment = CallHome.Profiles.Profile.SubscribeAlertGroup.Environment()
                    self.environment.parent = self
                    self._children_name_map["environment"] = "environment"

                    self.configuration = CallHome.Profiles.Profile.SubscribeAlertGroup.Configuration()
                    self.configuration.parent = self
                    self._children_name_map["configuration"] = "configuration"

                    self.snapshot = CallHome.Profiles.Profile.SubscribeAlertGroup.Snapshot()
                    self.snapshot.parent = self
                    self._children_name_map["snapshot"] = "snapshot"

                    self.inventory = CallHome.Profiles.Profile.SubscribeAlertGroup.Inventory()
                    self.inventory.parent = self
                    self._children_name_map["inventory"] = "inventory"

                    self.crash = CallHome.Profiles.Profile.SubscribeAlertGroup.Crash()
                    self.crash.parent = self
                    self._children_name_map["crash"] = "crash"

                    self.syslogs = CallHome.Profiles.Profile.SubscribeAlertGroup.Syslogs()
                    self.syslogs.parent = self
                    self._children_name_map["syslogs"] = "syslogs"
                    self._segment_path = lambda: "subscribe-alert-group"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(CallHome.Profiles.Profile.SubscribeAlertGroup, [], name, value)


                class Environment(Entity):
                    """
                    environmental info
                    
                    .. attribute:: severity
                    
                    	Severity
                    	**type**\:  :py:class:`CallHomeEventSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHomeEventSeverity>`
                    
                    

                    """

                    _prefix = 'call-home-cfg'
                    _revision = '2018-06-21'

                    def __init__(self):
                        super(CallHome.Profiles.Profile.SubscribeAlertGroup.Environment, self).__init__()

                        self.yang_name = "environment"
                        self.yang_parent_name = "subscribe-alert-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg', 'CallHomeEventSeverity', '')])),
                        ])
                        self.severity = None
                        self._segment_path = lambda: "environment"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(CallHome.Profiles.Profile.SubscribeAlertGroup.Environment, ['severity'], name, value)


                class Configuration(Entity):
                    """
                    configuration info
                    
                    .. attribute:: periodic
                    
                    	Periodic call\-home message
                    	**type**\:  :py:class:`Periodic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.SubscribeAlertGroup.Configuration.Periodic>`
                    
                    .. attribute:: subscribe
                    
                    	Subscribe the alert\-group
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'call-home-cfg'
                    _revision = '2018-06-21'

                    def __init__(self):
                        super(CallHome.Profiles.Profile.SubscribeAlertGroup.Configuration, self).__init__()

                        self.yang_name = "configuration"
                        self.yang_parent_name = "subscribe-alert-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("periodic", ("periodic", CallHome.Profiles.Profile.SubscribeAlertGroup.Configuration.Periodic))])
                        self._leafs = OrderedDict([
                            ('subscribe', (YLeaf(YType.empty, 'subscribe'), ['Empty'])),
                        ])
                        self.subscribe = None

                        self.periodic = CallHome.Profiles.Profile.SubscribeAlertGroup.Configuration.Periodic()
                        self.periodic.parent = self
                        self._children_name_map["periodic"] = "periodic"
                        self._segment_path = lambda: "configuration"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(CallHome.Profiles.Profile.SubscribeAlertGroup.Configuration, ['subscribe'], name, value)


                    class Periodic(Entity):
                        """
                        Periodic call\-home message
                        
                        .. attribute:: interval
                        
                        	none
                        	**type**\:  :py:class:`CallHomeMailSendInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHomeMailSendInterval>`
                        
                        .. attribute:: day
                        
                        	Day
                        	**type**\: int
                        
                        	**range:** 0..31
                        
                        .. attribute:: weekday
                        
                        	Day of week
                        	**type**\:  :py:class:`CallHomeDayOfWeek <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHomeDayOfWeek>`
                        
                        .. attribute:: hour
                        
                        	Hour
                        	**type**\: int
                        
                        	**range:** 0..23
                        
                        .. attribute:: minute
                        
                        	Minute
                        	**type**\: int
                        
                        	**range:** 0..59
                        
                        

                        """

                        _prefix = 'call-home-cfg'
                        _revision = '2018-06-21'

                        def __init__(self):
                            super(CallHome.Profiles.Profile.SubscribeAlertGroup.Configuration.Periodic, self).__init__()

                            self.yang_name = "periodic"
                            self.yang_parent_name = "configuration"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interval', (YLeaf(YType.enumeration, 'interval'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg', 'CallHomeMailSendInterval', '')])),
                                ('day', (YLeaf(YType.uint32, 'day'), ['int'])),
                                ('weekday', (YLeaf(YType.enumeration, 'weekday'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg', 'CallHomeDayOfWeek', '')])),
                                ('hour', (YLeaf(YType.uint32, 'hour'), ['int'])),
                                ('minute', (YLeaf(YType.uint32, 'minute'), ['int'])),
                            ])
                            self.interval = None
                            self.day = None
                            self.weekday = None
                            self.hour = None
                            self.minute = None
                            self._segment_path = lambda: "periodic"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(CallHome.Profiles.Profile.SubscribeAlertGroup.Configuration.Periodic, ['interval', 'day', 'weekday', 'hour', 'minute'], name, value)


                class Snapshot(Entity):
                    """
                    snapshot info
                    
                    .. attribute:: periodic
                    
                    	Periodic call\-home message
                    	**type**\:  :py:class:`Periodic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.SubscribeAlertGroup.Snapshot.Periodic>`
                    
                    

                    """

                    _prefix = 'call-home-cfg'
                    _revision = '2018-06-21'

                    def __init__(self):
                        super(CallHome.Profiles.Profile.SubscribeAlertGroup.Snapshot, self).__init__()

                        self.yang_name = "snapshot"
                        self.yang_parent_name = "subscribe-alert-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("periodic", ("periodic", CallHome.Profiles.Profile.SubscribeAlertGroup.Snapshot.Periodic))])
                        self._leafs = OrderedDict()

                        self.periodic = CallHome.Profiles.Profile.SubscribeAlertGroup.Snapshot.Periodic()
                        self.periodic.parent = self
                        self._children_name_map["periodic"] = "periodic"
                        self._segment_path = lambda: "snapshot"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(CallHome.Profiles.Profile.SubscribeAlertGroup.Snapshot, [], name, value)


                    class Periodic(Entity):
                        """
                        Periodic call\-home message
                        
                        .. attribute:: interval
                        
                        	none
                        	**type**\:  :py:class:`SnapshotInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.SnapshotInterval>`
                        
                        .. attribute:: day
                        
                        	Day of month
                        	**type**\: int
                        
                        	**range:** 0..31
                        
                        .. attribute:: weekday
                        
                        	Day of week
                        	**type**\:  :py:class:`CallHomeDayOfWeek <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHomeDayOfWeek>`
                        
                        .. attribute:: hour
                        
                        	Hour
                        	**type**\: int
                        
                        	**range:** 0..23
                        
                        .. attribute:: minute
                        
                        	Minute
                        	**type**\: int
                        
                        	**range:** 0..59
                        
                        

                        """

                        _prefix = 'call-home-cfg'
                        _revision = '2018-06-21'

                        def __init__(self):
                            super(CallHome.Profiles.Profile.SubscribeAlertGroup.Snapshot.Periodic, self).__init__()

                            self.yang_name = "periodic"
                            self.yang_parent_name = "snapshot"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interval', (YLeaf(YType.enumeration, 'interval'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg', 'SnapshotInterval', '')])),
                                ('day', (YLeaf(YType.uint32, 'day'), ['int'])),
                                ('weekday', (YLeaf(YType.enumeration, 'weekday'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg', 'CallHomeDayOfWeek', '')])),
                                ('hour', (YLeaf(YType.uint32, 'hour'), ['int'])),
                                ('minute', (YLeaf(YType.uint32, 'minute'), ['int'])),
                            ])
                            self.interval = None
                            self.day = None
                            self.weekday = None
                            self.hour = None
                            self.minute = None
                            self._segment_path = lambda: "periodic"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(CallHome.Profiles.Profile.SubscribeAlertGroup.Snapshot.Periodic, ['interval', 'day', 'weekday', 'hour', 'minute'], name, value)


                class Inventory(Entity):
                    """
                    inventory info
                    
                    .. attribute:: periodic
                    
                    	Periodic call\-home message
                    	**type**\:  :py:class:`Periodic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.SubscribeAlertGroup.Inventory.Periodic>`
                    
                    .. attribute:: subscribe
                    
                    	Subscribe the alert\-group
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'call-home-cfg'
                    _revision = '2018-06-21'

                    def __init__(self):
                        super(CallHome.Profiles.Profile.SubscribeAlertGroup.Inventory, self).__init__()

                        self.yang_name = "inventory"
                        self.yang_parent_name = "subscribe-alert-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("periodic", ("periodic", CallHome.Profiles.Profile.SubscribeAlertGroup.Inventory.Periodic))])
                        self._leafs = OrderedDict([
                            ('subscribe', (YLeaf(YType.empty, 'subscribe'), ['Empty'])),
                        ])
                        self.subscribe = None

                        self.periodic = CallHome.Profiles.Profile.SubscribeAlertGroup.Inventory.Periodic()
                        self.periodic.parent = self
                        self._children_name_map["periodic"] = "periodic"
                        self._segment_path = lambda: "inventory"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(CallHome.Profiles.Profile.SubscribeAlertGroup.Inventory, ['subscribe'], name, value)


                    class Periodic(Entity):
                        """
                        Periodic call\-home message
                        
                        .. attribute:: interval
                        
                        	none
                        	**type**\:  :py:class:`CallHomeMailSendInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHomeMailSendInterval>`
                        
                        .. attribute:: day
                        
                        	Day of month
                        	**type**\: int
                        
                        	**range:** 0..31
                        
                        .. attribute:: weekday
                        
                        	Day of week
                        	**type**\:  :py:class:`CallHomeDayOfWeek <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHomeDayOfWeek>`
                        
                        .. attribute:: hour
                        
                        	Hour
                        	**type**\: int
                        
                        	**range:** 0..23
                        
                        .. attribute:: minute
                        
                        	Minute
                        	**type**\: int
                        
                        	**range:** 0..59
                        
                        

                        """

                        _prefix = 'call-home-cfg'
                        _revision = '2018-06-21'

                        def __init__(self):
                            super(CallHome.Profiles.Profile.SubscribeAlertGroup.Inventory.Periodic, self).__init__()

                            self.yang_name = "periodic"
                            self.yang_parent_name = "inventory"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interval', (YLeaf(YType.enumeration, 'interval'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg', 'CallHomeMailSendInterval', '')])),
                                ('day', (YLeaf(YType.uint32, 'day'), ['int'])),
                                ('weekday', (YLeaf(YType.enumeration, 'weekday'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg', 'CallHomeDayOfWeek', '')])),
                                ('hour', (YLeaf(YType.uint32, 'hour'), ['int'])),
                                ('minute', (YLeaf(YType.uint32, 'minute'), ['int'])),
                            ])
                            self.interval = None
                            self.day = None
                            self.weekday = None
                            self.hour = None
                            self.minute = None
                            self._segment_path = lambda: "periodic"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(CallHome.Profiles.Profile.SubscribeAlertGroup.Inventory.Periodic, ['interval', 'day', 'weekday', 'hour', 'minute'], name, value)


                class Crash(Entity):
                    """
                    Crash info
                    
                    .. attribute:: subscribe
                    
                    	Subscribe crash group
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'call-home-cfg'
                    _revision = '2018-06-21'

                    def __init__(self):
                        super(CallHome.Profiles.Profile.SubscribeAlertGroup.Crash, self).__init__()

                        self.yang_name = "crash"
                        self.yang_parent_name = "subscribe-alert-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('subscribe', (YLeaf(YType.empty, 'subscribe'), ['Empty'])),
                        ])
                        self.subscribe = None
                        self._segment_path = lambda: "crash"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(CallHome.Profiles.Profile.SubscribeAlertGroup.Crash, ['subscribe'], name, value)


                class Syslogs(Entity):
                    """
                    syslog info
                    
                    .. attribute:: syslog
                    
                    	Syslog message pattern to be matched
                    	**type**\: list of  		 :py:class:`Syslog <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.SubscribeAlertGroup.Syslogs.Syslog>`
                    
                    

                    """

                    _prefix = 'call-home-cfg'
                    _revision = '2018-06-21'

                    def __init__(self):
                        super(CallHome.Profiles.Profile.SubscribeAlertGroup.Syslogs, self).__init__()

                        self.yang_name = "syslogs"
                        self.yang_parent_name = "subscribe-alert-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("syslog", ("syslog", CallHome.Profiles.Profile.SubscribeAlertGroup.Syslogs.Syslog))])
                        self._leafs = OrderedDict()

                        self.syslog = YList(self)
                        self._segment_path = lambda: "syslogs"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(CallHome.Profiles.Profile.SubscribeAlertGroup.Syslogs, [], name, value)


                    class Syslog(Entity):
                        """
                        Syslog message pattern to be matched
                        
                        .. attribute:: syslog_pattern  (key)
                        
                        	Syslog message pattern to be matched
                        	**type**\: str
                        
                        	**length:** 1..80
                        
                        .. attribute:: severity
                        
                        	Severity
                        	**type**\:  :py:class:`CallHomeEventSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHomeEventSeverity>`
                        
                        

                        """

                        _prefix = 'call-home-cfg'
                        _revision = '2018-06-21'

                        def __init__(self):
                            super(CallHome.Profiles.Profile.SubscribeAlertGroup.Syslogs.Syslog, self).__init__()

                            self.yang_name = "syslog"
                            self.yang_parent_name = "syslogs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['syslog_pattern']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('syslog_pattern', (YLeaf(YType.str, 'syslog-pattern'), ['str'])),
                                ('severity', (YLeaf(YType.enumeration, 'severity'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg', 'CallHomeEventSeverity', '')])),
                            ])
                            self.syslog_pattern = None
                            self.severity = None
                            self._segment_path = lambda: "syslog" + "[syslog-pattern='" + str(self.syslog_pattern) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(CallHome.Profiles.Profile.SubscribeAlertGroup.Syslogs.Syslog, ['syslog_pattern', 'severity'], name, value)


    class AlertGroups(Entity):
        """
        List of alert\-group
        
        .. attribute:: alert_group
        
        	A specific alert\-group
        	**type**\: list of  		 :py:class:`AlertGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.AlertGroups.AlertGroup>`
        
        

        """

        _prefix = 'call-home-cfg'
        _revision = '2018-06-21'

        def __init__(self):
            super(CallHome.AlertGroups, self).__init__()

            self.yang_name = "alert-groups"
            self.yang_parent_name = "call-home"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("alert-group", ("alert_group", CallHome.AlertGroups.AlertGroup))])
            self._leafs = OrderedDict()

            self.alert_group = YList(self)
            self._segment_path = lambda: "alert-groups"
            self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CallHome.AlertGroups, [], name, value)


        class AlertGroup(Entity):
            """
            A specific alert\-group
            
            .. attribute:: alert_group_name  (key)
            
            	none
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: enable
            
            	Enable the alert\-group
            	**type**\: bool
            
            .. attribute:: disable
            
            	Disable the alert\-group
            	**type**\: bool
            
            

            """

            _prefix = 'call-home-cfg'
            _revision = '2018-06-21'

            def __init__(self):
                super(CallHome.AlertGroups.AlertGroup, self).__init__()

                self.yang_name = "alert-group"
                self.yang_parent_name = "alert-groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['alert_group_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('alert_group_name', (YLeaf(YType.str, 'alert-group-name'), ['str'])),
                    ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                    ('disable', (YLeaf(YType.boolean, 'disable'), ['bool'])),
                ])
                self.alert_group_name = None
                self.enable = None
                self.disable = None
                self._segment_path = lambda: "alert-group" + "[alert-group-name='" + str(self.alert_group_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/alert-groups/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CallHome.AlertGroups.AlertGroup, ['alert_group_name', 'enable', 'disable'], name, value)


    class DataPrivacies(Entity):
        """
        Set call\-home data\-privacy
        
        .. attribute:: data_privacy
        
        	level hostname
        	**type**\: list of  		 :py:class:`DataPrivacy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.DataPrivacies.DataPrivacy>`
        
        

        """

        _prefix = 'call-home-cfg'
        _revision = '2018-06-21'

        def __init__(self):
            super(CallHome.DataPrivacies, self).__init__()

            self.yang_name = "data-privacies"
            self.yang_parent_name = "call-home"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("data-privacy", ("data_privacy", CallHome.DataPrivacies.DataPrivacy))])
            self._leafs = OrderedDict()

            self.data_privacy = YList(self)
            self._segment_path = lambda: "data-privacies"
            self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CallHome.DataPrivacies, [], name, value)


        class DataPrivacy(Entity):
            """
            level hostname
            
            .. attribute:: host_name  (key)
            
            	Data privacy type (hostname or level)
            	**type**\: str
            
            .. attribute:: level
            
            	Set call\-home data\-privacy level
            	**type**\:  :py:class:`DataPrivacyLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.DataPrivacyLevel>`
            
            

            """

            _prefix = 'call-home-cfg'
            _revision = '2018-06-21'

            def __init__(self):
                super(CallHome.DataPrivacies.DataPrivacy, self).__init__()

                self.yang_name = "data-privacy"
                self.yang_parent_name = "data-privacies"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['host_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('host_name', (YLeaf(YType.str, 'host-name'), ['str'])),
                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg', 'DataPrivacyLevel', '')])),
                ])
                self.host_name = None
                self.level = None
                self._segment_path = lambda: "data-privacy" + "[host-name='" + str(self.host_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/data-privacies/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CallHome.DataPrivacies.DataPrivacy, ['host_name', 'level'], name, value)


    class AlertGroupConfig(Entity):
        """
        alert\-group config
        
        .. attribute:: snapshot_commands
        
        	snapshot for adding CLI command
        	**type**\:  :py:class:`SnapshotCommands <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.AlertGroupConfig.SnapshotCommands>`
        
        

        """

        _prefix = 'call-home-cfg'
        _revision = '2018-06-21'

        def __init__(self):
            super(CallHome.AlertGroupConfig, self).__init__()

            self.yang_name = "alert-group-config"
            self.yang_parent_name = "call-home"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("snapshot-commands", ("snapshot_commands", CallHome.AlertGroupConfig.SnapshotCommands))])
            self._leafs = OrderedDict()

            self.snapshot_commands = CallHome.AlertGroupConfig.SnapshotCommands()
            self.snapshot_commands.parent = self
            self._children_name_map["snapshot_commands"] = "snapshot-commands"
            self._segment_path = lambda: "alert-group-config"
            self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CallHome.AlertGroupConfig, [], name, value)


        class SnapshotCommands(Entity):
            """
            snapshot for adding CLI command
            
            .. attribute:: snapshot_command
            
            	A specific CLI cmd for snapshot
            	**type**\: list of  		 :py:class:`SnapshotCommand <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.AlertGroupConfig.SnapshotCommands.SnapshotCommand>`
            
            

            """

            _prefix = 'call-home-cfg'
            _revision = '2018-06-21'

            def __init__(self):
                super(CallHome.AlertGroupConfig.SnapshotCommands, self).__init__()

                self.yang_name = "snapshot-commands"
                self.yang_parent_name = "alert-group-config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("snapshot-command", ("snapshot_command", CallHome.AlertGroupConfig.SnapshotCommands.SnapshotCommand))])
                self._leafs = OrderedDict()

                self.snapshot_command = YList(self)
                self._segment_path = lambda: "snapshot-commands"
                self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/alert-group-config/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CallHome.AlertGroupConfig.SnapshotCommands, [], name, value)


            class SnapshotCommand(Entity):
                """
                A specific CLI cmd for snapshot
                
                .. attribute:: command  (key)
                
                	new added command
                	**type**\: str
                
                	**length:** 1..127
                
                .. attribute:: active
                
                	enable snapshot cmd
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'call-home-cfg'
                _revision = '2018-06-21'

                def __init__(self):
                    super(CallHome.AlertGroupConfig.SnapshotCommands.SnapshotCommand, self).__init__()

                    self.yang_name = "snapshot-command"
                    self.yang_parent_name = "snapshot-commands"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['command']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('command', (YLeaf(YType.str, 'command'), ['str'])),
                        ('active', (YLeaf(YType.empty, 'active'), ['Empty'])),
                    ])
                    self.command = None
                    self.active = None
                    self._segment_path = lambda: "snapshot-command" + "[command='" + str(self.command) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/alert-group-config/snapshot-commands/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(CallHome.AlertGroupConfig.SnapshotCommands.SnapshotCommand, ['command', 'active'], name, value)


    class Authorization(Entity):
        """
        Config aaa authorization, default username is
        callhome
        
        .. attribute:: username
        
        	Username for authorization. default is callhome
        	**type**\: str
        
        	**length:** 1..64
        
        .. attribute:: active
        
        	Enable call\-home aaa\-authorization
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'call-home-cfg'
        _revision = '2018-06-21'

        def __init__(self):
            super(CallHome.Authorization, self).__init__()

            self.yang_name = "authorization"
            self.yang_parent_name = "call-home"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('username', (YLeaf(YType.str, 'username'), ['str'])),
                ('active', (YLeaf(YType.empty, 'active'), ['Empty'])),
            ])
            self.username = None
            self.active = None
            self._segment_path = lambda: "authorization"
            self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CallHome.Authorization, ['username', 'active'], name, value)

    def clone_ptr(self):
        self._top_entity = CallHome()
        return self._top_entity


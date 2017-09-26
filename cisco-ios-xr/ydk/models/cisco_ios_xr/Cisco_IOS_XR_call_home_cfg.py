""" Cisco_IOS_XR_call_home_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR call\-home package configuration.

This module contains definitions
for the following management objects\:
  call\-home\: Set CallHome parameters

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CallHomeDayOfWeek(Enum):
    """
    CallHomeDayOfWeek

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
    CallHomeEventSeverity

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
    CallHomeMailSendInterval

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
    CallHomeTransMethod

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
    DataPrivacyLevel

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
    SnapshotInterval

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
    
    .. attribute:: active
    
    	Enable call\-home service
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: alert_group_config
    
    	alert\-group config
    	**type**\:   :py:class:`AlertGroupConfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.AlertGroupConfig>`
    
    .. attribute:: alert_groups
    
    	List of alert\-group
    	**type**\:   :py:class:`AlertGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.AlertGroups>`
    
    .. attribute:: authorization
    
    	Config aaa authorization, default username is callhome
    	**type**\:   :py:class:`Authorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Authorization>`
    
    .. attribute:: contact_email_address
    
    	Contact person's email address
    	**type**\:  str
    
    	**length:** 1..194
    
    .. attribute:: contact_smart_licensing
    
    	System Contact is Smart Licensing
    	**type**\:  bool
    
    .. attribute:: contract_id
    
    	Contract identification for Cisco Smart Call Home
    	**type**\:  str
    
    	**length:** 1..64
    
    .. attribute:: customer_id
    
    	Customer identification for Cisco Smart Call Home
    	**type**\:  str
    
    	**length:** 1..64
    
    .. attribute:: data_privacies
    
    	Set call\-home data\-privacy
    	**type**\:   :py:class:`DataPrivacies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.DataPrivacies>`
    
    .. attribute:: from_
    
    	Call home msg's from email address
    	**type**\:  str
    
    .. attribute:: http_proxy
    
    	http proxy server address and port
    	**type**\:   :py:class:`HttpProxy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.HttpProxy>`
    
    .. attribute:: mail_servers
    
    	List of call\-home mail\_server
    	**type**\:   :py:class:`MailServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.MailServers>`
    
    .. attribute:: phone_number
    
    	Phone number of the contact person
    	**type**\:  str
    
    	**length:** 1..17
    
    .. attribute:: profiles
    
    	List of profiles
    	**type**\:   :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles>`
    
    .. attribute:: rate_limit
    
    	Call\-home event trigger rate\-limit threshold per minute
    	**type**\:  int
    
    	**range:** 1..5
    
    .. attribute:: reply_to
    
    	Call home msg's reply\-to email address
    	**type**\:  str
    
    .. attribute:: site_id
    
    	Site identification for Cisco Smart Call Home
    	**type**\:  str
    
    	**length:** 1..200
    
    .. attribute:: smart_licensing
    
    	Enable/disable licensing messages. By default is enabled
    	**type**\:   :py:class:`SmartLicensing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.SmartLicensing>`
    
    .. attribute:: source_interface
    
    	Source interface name to send call\-home messages
    	**type**\:  str
    
    	**pattern:** [a\-zA\-Z0\-9./\-]+
    
    .. attribute:: street_address
    
    	Street address, city, state, and zip code
    	**type**\:  str
    
    	**length:** 1..200
    
    .. attribute:: syslog_throttling
    
    	Enable or disable call\-home syslog message throttling
    	**type**\:   :py:class:`SyslogThrottling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.SyslogThrottling>`
    
    .. attribute:: vrf
    
    	Vrf routing/forwarding instance name
    	**type**\:  str
    
    	**length:** 1..32
    
    

    """

    _prefix = 'call-home-cfg'
    _revision = '2017-03-13'

    def __init__(self):
        super(CallHome, self).__init__()
        self._top_entity = None

        self.yang_name = "call-home"
        self.yang_parent_name = "Cisco-IOS-XR-call-home-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"alert-group-config" : ("alert_group_config", CallHome.AlertGroupConfig), "alert-groups" : ("alert_groups", CallHome.AlertGroups), "authorization" : ("authorization", CallHome.Authorization), "data-privacies" : ("data_privacies", CallHome.DataPrivacies), "http-proxy" : ("http_proxy", CallHome.HttpProxy), "mail-servers" : ("mail_servers", CallHome.MailServers), "profiles" : ("profiles", CallHome.Profiles), "smart-licensing" : ("smart_licensing", CallHome.SmartLicensing), "syslog-throttling" : ("syslog_throttling", CallHome.SyslogThrottling)}
        self._child_list_classes = {}

        self.active = YLeaf(YType.empty, "active")

        self.contact_email_address = YLeaf(YType.str, "contact-email-address")

        self.contact_smart_licensing = YLeaf(YType.boolean, "contact-smart-licensing")

        self.contract_id = YLeaf(YType.str, "contract-id")

        self.customer_id = YLeaf(YType.str, "customer-id")

        self.from_ = YLeaf(YType.str, "from")

        self.phone_number = YLeaf(YType.str, "phone-number")

        self.rate_limit = YLeaf(YType.uint32, "rate-limit")

        self.reply_to = YLeaf(YType.str, "reply-to")

        self.site_id = YLeaf(YType.str, "site-id")

        self.source_interface = YLeaf(YType.str, "source-interface")

        self.street_address = YLeaf(YType.str, "street-address")

        self.vrf = YLeaf(YType.str, "vrf")

        self.alert_group_config = CallHome.AlertGroupConfig()
        self.alert_group_config.parent = self
        self._children_name_map["alert_group_config"] = "alert-group-config"
        self._children_yang_names.add("alert-group-config")

        self.alert_groups = CallHome.AlertGroups()
        self.alert_groups.parent = self
        self._children_name_map["alert_groups"] = "alert-groups"
        self._children_yang_names.add("alert-groups")

        self.authorization = CallHome.Authorization()
        self.authorization.parent = self
        self._children_name_map["authorization"] = "authorization"
        self._children_yang_names.add("authorization")

        self.data_privacies = CallHome.DataPrivacies()
        self.data_privacies.parent = self
        self._children_name_map["data_privacies"] = "data-privacies"
        self._children_yang_names.add("data-privacies")

        self.http_proxy = CallHome.HttpProxy()
        self.http_proxy.parent = self
        self._children_name_map["http_proxy"] = "http-proxy"
        self._children_yang_names.add("http-proxy")

        self.mail_servers = CallHome.MailServers()
        self.mail_servers.parent = self
        self._children_name_map["mail_servers"] = "mail-servers"
        self._children_yang_names.add("mail-servers")

        self.profiles = CallHome.Profiles()
        self.profiles.parent = self
        self._children_name_map["profiles"] = "profiles"
        self._children_yang_names.add("profiles")

        self.smart_licensing = CallHome.SmartLicensing()
        self.smart_licensing.parent = self
        self._children_name_map["smart_licensing"] = "smart-licensing"
        self._children_yang_names.add("smart-licensing")

        self.syslog_throttling = CallHome.SyslogThrottling()
        self.syslog_throttling.parent = self
        self._children_name_map["syslog_throttling"] = "syslog-throttling"
        self._children_yang_names.add("syslog-throttling")
        self._segment_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home"

    def __setattr__(self, name, value):
        self._perform_setattr(CallHome, ['active', 'contact_email_address', 'contact_smart_licensing', 'contract_id', 'customer_id', 'from_', 'phone_number', 'rate_limit', 'reply_to', 'site_id', 'source_interface', 'street_address', 'vrf'], name, value)


    class AlertGroupConfig(Entity):
        """
        alert\-group config
        
        .. attribute:: snapshot_commands
        
        	snapshot for adding CLI command
        	**type**\:   :py:class:`SnapshotCommands <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.AlertGroupConfig.SnapshotCommands>`
        
        

        """

        _prefix = 'call-home-cfg'
        _revision = '2017-03-13'

        def __init__(self):
            super(CallHome.AlertGroupConfig, self).__init__()

            self.yang_name = "alert-group-config"
            self.yang_parent_name = "call-home"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"snapshot-commands" : ("snapshot_commands", CallHome.AlertGroupConfig.SnapshotCommands)}
            self._child_list_classes = {}

            self.snapshot_commands = CallHome.AlertGroupConfig.SnapshotCommands()
            self.snapshot_commands.parent = self
            self._children_name_map["snapshot_commands"] = "snapshot-commands"
            self._children_yang_names.add("snapshot-commands")
            self._segment_path = lambda: "alert-group-config"
            self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/%s" % self._segment_path()


        class SnapshotCommands(Entity):
            """
            snapshot for adding CLI command
            
            .. attribute:: snapshot_command
            
            	A specific CLI cmd for snapshot
            	**type**\: list of    :py:class:`SnapshotCommand <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.AlertGroupConfig.SnapshotCommands.SnapshotCommand>`
            
            

            """

            _prefix = 'call-home-cfg'
            _revision = '2017-03-13'

            def __init__(self):
                super(CallHome.AlertGroupConfig.SnapshotCommands, self).__init__()

                self.yang_name = "snapshot-commands"
                self.yang_parent_name = "alert-group-config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"snapshot-command" : ("snapshot_command", CallHome.AlertGroupConfig.SnapshotCommands.SnapshotCommand)}

                self.snapshot_command = YList(self)
                self._segment_path = lambda: "snapshot-commands"
                self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/alert-group-config/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CallHome.AlertGroupConfig.SnapshotCommands, [], name, value)


            class SnapshotCommand(Entity):
                """
                A specific CLI cmd for snapshot
                
                .. attribute:: command  <key>
                
                	new added command
                	**type**\:  str
                
                	**length:** 1..127
                
                .. attribute:: active
                
                	enable snapshot cmd
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'call-home-cfg'
                _revision = '2017-03-13'

                def __init__(self):
                    super(CallHome.AlertGroupConfig.SnapshotCommands.SnapshotCommand, self).__init__()

                    self.yang_name = "snapshot-command"
                    self.yang_parent_name = "snapshot-commands"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.command = YLeaf(YType.str, "command")

                    self.active = YLeaf(YType.empty, "active")
                    self._segment_path = lambda: "snapshot-command" + "[command='" + self.command.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/alert-group-config/snapshot-commands/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(CallHome.AlertGroupConfig.SnapshotCommands.SnapshotCommand, ['command', 'active'], name, value)


    class AlertGroups(Entity):
        """
        List of alert\-group
        
        .. attribute:: alert_group
        
        	A specific alert\-group
        	**type**\: list of    :py:class:`AlertGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.AlertGroups.AlertGroup>`
        
        

        """

        _prefix = 'call-home-cfg'
        _revision = '2017-03-13'

        def __init__(self):
            super(CallHome.AlertGroups, self).__init__()

            self.yang_name = "alert-groups"
            self.yang_parent_name = "call-home"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"alert-group" : ("alert_group", CallHome.AlertGroups.AlertGroup)}

            self.alert_group = YList(self)
            self._segment_path = lambda: "alert-groups"
            self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CallHome.AlertGroups, [], name, value)


        class AlertGroup(Entity):
            """
            A specific alert\-group
            
            .. attribute:: alert_group_name  <key>
            
            	none
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: disable
            
            	Disable the alert\-group
            	**type**\:  bool
            
            .. attribute:: enable
            
            	Enable the alert\-group
            	**type**\:  bool
            
            

            """

            _prefix = 'call-home-cfg'
            _revision = '2017-03-13'

            def __init__(self):
                super(CallHome.AlertGroups.AlertGroup, self).__init__()

                self.yang_name = "alert-group"
                self.yang_parent_name = "alert-groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.alert_group_name = YLeaf(YType.str, "alert-group-name")

                self.disable = YLeaf(YType.boolean, "disable")

                self.enable = YLeaf(YType.boolean, "enable")
                self._segment_path = lambda: "alert-group" + "[alert-group-name='" + self.alert_group_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/alert-groups/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CallHome.AlertGroups.AlertGroup, ['alert_group_name', 'disable', 'enable'], name, value)


    class Authorization(Entity):
        """
        Config aaa authorization, default username is
        callhome
        
        .. attribute:: active
        
        	Enable call\-home aaa\-authorization
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: username
        
        	Username for authorization. default is callhome
        	**type**\:  str
        
        	**length:** 1..64
        
        

        """

        _prefix = 'call-home-cfg'
        _revision = '2017-03-13'

        def __init__(self):
            super(CallHome.Authorization, self).__init__()

            self.yang_name = "authorization"
            self.yang_parent_name = "call-home"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.active = YLeaf(YType.empty, "active")

            self.username = YLeaf(YType.str, "username")
            self._segment_path = lambda: "authorization"
            self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CallHome.Authorization, ['active', 'username'], name, value)


    class DataPrivacies(Entity):
        """
        Set call\-home data\-privacy
        
        .. attribute:: data_privacy
        
        	level hostname
        	**type**\: list of    :py:class:`DataPrivacy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.DataPrivacies.DataPrivacy>`
        
        

        """

        _prefix = 'call-home-cfg'
        _revision = '2017-03-13'

        def __init__(self):
            super(CallHome.DataPrivacies, self).__init__()

            self.yang_name = "data-privacies"
            self.yang_parent_name = "call-home"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"data-privacy" : ("data_privacy", CallHome.DataPrivacies.DataPrivacy)}

            self.data_privacy = YList(self)
            self._segment_path = lambda: "data-privacies"
            self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CallHome.DataPrivacies, [], name, value)


        class DataPrivacy(Entity):
            """
            level hostname
            
            .. attribute:: host_name  <key>
            
            	Data privacy type (hostname or level)
            	**type**\:  str
            
            .. attribute:: level
            
            	Set call\-home data\-privacy level
            	**type**\:   :py:class:`DataPrivacyLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.DataPrivacyLevel>`
            
            

            """

            _prefix = 'call-home-cfg'
            _revision = '2017-03-13'

            def __init__(self):
                super(CallHome.DataPrivacies.DataPrivacy, self).__init__()

                self.yang_name = "data-privacy"
                self.yang_parent_name = "data-privacies"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.host_name = YLeaf(YType.str, "host-name")

                self.level = YLeaf(YType.enumeration, "level")
                self._segment_path = lambda: "data-privacy" + "[host-name='" + self.host_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/data-privacies/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CallHome.DataPrivacies.DataPrivacy, ['host_name', 'level'], name, value)


    class HttpProxy(Entity):
        """
        http proxy server address and port
        
        .. attribute:: port
        
        	http proxy server's port
        	**type**\:  int
        
        	**range:** 1..65535
        
        .. attribute:: server_address
        
        	http proxy server address
        	**type**\:  str
        
        

        """

        _prefix = 'call-home-cfg'
        _revision = '2017-03-13'

        def __init__(self):
            super(CallHome.HttpProxy, self).__init__()

            self.yang_name = "http-proxy"
            self.yang_parent_name = "call-home"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.port = YLeaf(YType.uint16, "port")

            self.server_address = YLeaf(YType.str, "server-address")
            self._segment_path = lambda: "http-proxy"
            self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CallHome.HttpProxy, ['port', 'server_address'], name, value)


    class MailServers(Entity):
        """
        List of call\-home mail\_server
        
        .. attribute:: mail_server
        
        	Email server
        	**type**\: list of    :py:class:`MailServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.MailServers.MailServer>`
        
        

        """

        _prefix = 'call-home-cfg'
        _revision = '2017-03-13'

        def __init__(self):
            super(CallHome.MailServers, self).__init__()

            self.yang_name = "mail-servers"
            self.yang_parent_name = "call-home"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"mail-server" : ("mail_server", CallHome.MailServers.MailServer)}

            self.mail_server = YList(self)
            self._segment_path = lambda: "mail-servers"
            self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CallHome.MailServers, [], name, value)


        class MailServer(Entity):
            """
            Email server
            
            .. attribute:: mail_serv_address  <key>
            
            	Email server
            	**type**\:  str
            
            .. attribute:: priority
            
            	Mail server with lower # will be used first
            	**type**\:  int
            
            	**range:** 1..100
            
            

            """

            _prefix = 'call-home-cfg'
            _revision = '2017-03-13'

            def __init__(self):
                super(CallHome.MailServers.MailServer, self).__init__()

                self.yang_name = "mail-server"
                self.yang_parent_name = "mail-servers"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.mail_serv_address = YLeaf(YType.str, "mail-serv-address")

                self.priority = YLeaf(YType.uint32, "priority")
                self._segment_path = lambda: "mail-server" + "[mail-serv-address='" + self.mail_serv_address.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/mail-servers/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CallHome.MailServers.MailServer, ['mail_serv_address', 'priority'], name, value)


    class Profiles(Entity):
        """
        List of profiles
        
        .. attribute:: profile
        
        	A specific profile
        	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile>`
        
        

        """

        _prefix = 'call-home-cfg'
        _revision = '2017-03-13'

        def __init__(self):
            super(CallHome.Profiles, self).__init__()

            self.yang_name = "profiles"
            self.yang_parent_name = "call-home"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"profile" : ("profile", CallHome.Profiles.Profile)}

            self.profile = YList(self)
            self._segment_path = lambda: "profiles"
            self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CallHome.Profiles, [], name, value)


        class Profile(Entity):
            """
            A specific profile
            
            .. attribute:: profile_name  <key>
            
            	Profile name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: active
            
            	Activate the current profile
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: addresses
            
            	List of destination address
            	**type**\:   :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.Addresses>`
            
            .. attribute:: anonymous
            
            	Enable call\-home anonymous reporting only
            	**type**\:  bool
            
            .. attribute:: create
            
            	Create a profile
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: message_format
            
            	none
            	**type**\:  str
            
            .. attribute:: message_size_limit
            
            	To specify message size limit for this profile
            	**type**\:  int
            
            	**range:** 50..3145728
            
            .. attribute:: methods
            
            	Transport method (http or email)
            	**type**\:   :py:class:`Methods <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.Methods>`
            
            .. attribute:: report_type
            
            	Choose what data to report
            	**type**\:   :py:class:`ReportType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.ReportType>`
            
            .. attribute:: subscribe_alert_group
            
            	Subscribe to alert\-group
            	**type**\:   :py:class:`SubscribeAlertGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.SubscribeAlertGroup>`
            
            

            """

            _prefix = 'call-home-cfg'
            _revision = '2017-03-13'

            def __init__(self):
                super(CallHome.Profiles.Profile, self).__init__()

                self.yang_name = "profile"
                self.yang_parent_name = "profiles"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"addresses" : ("addresses", CallHome.Profiles.Profile.Addresses), "methods" : ("methods", CallHome.Profiles.Profile.Methods), "report-type" : ("report_type", CallHome.Profiles.Profile.ReportType), "subscribe-alert-group" : ("subscribe_alert_group", CallHome.Profiles.Profile.SubscribeAlertGroup)}
                self._child_list_classes = {}

                self.profile_name = YLeaf(YType.str, "profile-name")

                self.active = YLeaf(YType.empty, "active")

                self.anonymous = YLeaf(YType.boolean, "anonymous")

                self.create = YLeaf(YType.empty, "create")

                self.message_format = YLeaf(YType.str, "message-format")

                self.message_size_limit = YLeaf(YType.uint32, "message-size-limit")

                self.addresses = CallHome.Profiles.Profile.Addresses()
                self.addresses.parent = self
                self._children_name_map["addresses"] = "addresses"
                self._children_yang_names.add("addresses")

                self.methods = CallHome.Profiles.Profile.Methods()
                self.methods.parent = self
                self._children_name_map["methods"] = "methods"
                self._children_yang_names.add("methods")

                self.report_type = CallHome.Profiles.Profile.ReportType()
                self.report_type.parent = self
                self._children_name_map["report_type"] = "report-type"
                self._children_yang_names.add("report-type")

                self.subscribe_alert_group = CallHome.Profiles.Profile.SubscribeAlertGroup()
                self.subscribe_alert_group.parent = self
                self._children_name_map["subscribe_alert_group"] = "subscribe-alert-group"
                self._children_yang_names.add("subscribe-alert-group")
                self._segment_path = lambda: "profile" + "[profile-name='" + self.profile_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/profiles/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CallHome.Profiles.Profile, ['profile_name', 'active', 'anonymous', 'create', 'message_format', 'message_size_limit'], name, value)


            class Addresses(Entity):
                """
                List of destination address
                
                .. attribute:: address
                
                	A specific address
                	**type**\: list of    :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.Addresses.Address>`
                
                

                """

                _prefix = 'call-home-cfg'
                _revision = '2017-03-13'

                def __init__(self):
                    super(CallHome.Profiles.Profile.Addresses, self).__init__()

                    self.yang_name = "addresses"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"address" : ("address", CallHome.Profiles.Profile.Addresses.Address)}

                    self.address = YList(self)
                    self._segment_path = lambda: "addresses"

                def __setattr__(self, name, value):
                    self._perform_setattr(CallHome.Profiles.Profile.Addresses, [], name, value)


                class Address(Entity):
                    """
                    A specific address
                    
                    .. attribute:: method  <key>
                    
                    	Transpotation Method
                    	**type**\:   :py:class:`CallHomeTransMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHomeTransMethod>`
                    
                    .. attribute:: destination_addr  <key>
                    
                    	Destination address (1\-200) characters
                    	**type**\:  str
                    
                    	**length:** 1..200
                    
                    .. attribute:: enable
                    
                    	Set the address
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'call-home-cfg'
                    _revision = '2017-03-13'

                    def __init__(self):
                        super(CallHome.Profiles.Profile.Addresses.Address, self).__init__()

                        self.yang_name = "address"
                        self.yang_parent_name = "addresses"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.method = YLeaf(YType.enumeration, "method")

                        self.destination_addr = YLeaf(YType.str, "destination-addr")

                        self.enable = YLeaf(YType.boolean, "enable")
                        self._segment_path = lambda: "address" + "[method='" + self.method.get() + "']" + "[destination-addr='" + self.destination_addr.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CallHome.Profiles.Profile.Addresses.Address, ['method', 'destination_addr', 'enable'], name, value)


            class Methods(Entity):
                """
                Transport method (http or email)
                
                .. attribute:: method
                
                	Transport method
                	**type**\: list of    :py:class:`Method <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.Methods.Method>`
                
                

                """

                _prefix = 'call-home-cfg'
                _revision = '2017-03-13'

                def __init__(self):
                    super(CallHome.Profiles.Profile.Methods, self).__init__()

                    self.yang_name = "methods"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"method" : ("method", CallHome.Profiles.Profile.Methods.Method)}

                    self.method = YList(self)
                    self._segment_path = lambda: "methods"

                def __setattr__(self, name, value):
                    self._perform_setattr(CallHome.Profiles.Profile.Methods, [], name, value)


                class Method(Entity):
                    """
                    Transport method
                    
                    .. attribute:: method  <key>
                    
                    	Transport Method
                    	**type**\:   :py:class:`CallHomeTransMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHomeTransMethod>`
                    
                    .. attribute:: enable
                    
                    	Enable this transport method
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'call-home-cfg'
                    _revision = '2017-03-13'

                    def __init__(self):
                        super(CallHome.Profiles.Profile.Methods.Method, self).__init__()

                        self.yang_name = "method"
                        self.yang_parent_name = "methods"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.method = YLeaf(YType.enumeration, "method")

                        self.enable = YLeaf(YType.boolean, "enable")
                        self._segment_path = lambda: "method" + "[method='" + self.method.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CallHome.Profiles.Profile.Methods.Method, ['method', 'enable'], name, value)


            class ReportType(Entity):
                """
                Choose what data to report
                
                .. attribute:: reporting_callhome_data
                
                	Report smart call\-home data
                	**type**\:   :py:class:`ReportingCallhomeData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.ReportType.ReportingCallhomeData>`
                
                .. attribute:: reporting_licensing_data
                
                	Report smart licensing data
                	**type**\:   :py:class:`ReportingLicensingData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.ReportType.ReportingLicensingData>`
                
                

                """

                _prefix = 'call-home-cfg'
                _revision = '2017-03-13'

                def __init__(self):
                    super(CallHome.Profiles.Profile.ReportType, self).__init__()

                    self.yang_name = "report-type"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"reporting-callhome-data" : ("reporting_callhome_data", CallHome.Profiles.Profile.ReportType.ReportingCallhomeData), "reporting-licensing-data" : ("reporting_licensing_data", CallHome.Profiles.Profile.ReportType.ReportingLicensingData)}
                    self._child_list_classes = {}

                    self.reporting_callhome_data = CallHome.Profiles.Profile.ReportType.ReportingCallhomeData()
                    self.reporting_callhome_data.parent = self
                    self._children_name_map["reporting_callhome_data"] = "reporting-callhome-data"
                    self._children_yang_names.add("reporting-callhome-data")

                    self.reporting_licensing_data = CallHome.Profiles.Profile.ReportType.ReportingLicensingData()
                    self.reporting_licensing_data.parent = self
                    self._children_name_map["reporting_licensing_data"] = "reporting-licensing-data"
                    self._children_yang_names.add("reporting-licensing-data")
                    self._segment_path = lambda: "report-type"


                class ReportingCallhomeData(Entity):
                    """
                    Report smart call\-home data
                    
                    .. attribute:: enable
                    
                    	Enable report smart call\-home data
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'call-home-cfg'
                    _revision = '2017-03-13'

                    def __init__(self):
                        super(CallHome.Profiles.Profile.ReportType.ReportingCallhomeData, self).__init__()

                        self.yang_name = "reporting-callhome-data"
                        self.yang_parent_name = "report-type"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.enable = YLeaf(YType.boolean, "enable")
                        self._segment_path = lambda: "reporting-callhome-data"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CallHome.Profiles.Profile.ReportType.ReportingCallhomeData, ['enable'], name, value)


                class ReportingLicensingData(Entity):
                    """
                    Report smart licensing data
                    
                    .. attribute:: enable
                    
                    	Enable report smart licensing data
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'call-home-cfg'
                    _revision = '2017-03-13'

                    def __init__(self):
                        super(CallHome.Profiles.Profile.ReportType.ReportingLicensingData, self).__init__()

                        self.yang_name = "reporting-licensing-data"
                        self.yang_parent_name = "report-type"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.enable = YLeaf(YType.boolean, "enable")
                        self._segment_path = lambda: "reporting-licensing-data"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CallHome.Profiles.Profile.ReportType.ReportingLicensingData, ['enable'], name, value)


            class SubscribeAlertGroup(Entity):
                """
                Subscribe to alert\-group
                
                .. attribute:: configuration
                
                	configuration info
                	**type**\:   :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.SubscribeAlertGroup.Configuration>`
                
                .. attribute:: crash
                
                	Crash info
                	**type**\:   :py:class:`Crash <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.SubscribeAlertGroup.Crash>`
                
                .. attribute:: environment
                
                	environmental info
                	**type**\:   :py:class:`Environment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.SubscribeAlertGroup.Environment>`
                
                .. attribute:: inventory
                
                	inventory info
                	**type**\:   :py:class:`Inventory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.SubscribeAlertGroup.Inventory>`
                
                .. attribute:: snapshot
                
                	snapshot info
                	**type**\:   :py:class:`Snapshot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.SubscribeAlertGroup.Snapshot>`
                
                .. attribute:: syslogs
                
                	syslog info
                	**type**\:   :py:class:`Syslogs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.SubscribeAlertGroup.Syslogs>`
                
                

                """

                _prefix = 'call-home-cfg'
                _revision = '2017-03-13'

                def __init__(self):
                    super(CallHome.Profiles.Profile.SubscribeAlertGroup, self).__init__()

                    self.yang_name = "subscribe-alert-group"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"configuration" : ("configuration", CallHome.Profiles.Profile.SubscribeAlertGroup.Configuration), "crash" : ("crash", CallHome.Profiles.Profile.SubscribeAlertGroup.Crash), "environment" : ("environment", CallHome.Profiles.Profile.SubscribeAlertGroup.Environment), "inventory" : ("inventory", CallHome.Profiles.Profile.SubscribeAlertGroup.Inventory), "snapshot" : ("snapshot", CallHome.Profiles.Profile.SubscribeAlertGroup.Snapshot), "syslogs" : ("syslogs", CallHome.Profiles.Profile.SubscribeAlertGroup.Syslogs)}
                    self._child_list_classes = {}

                    self.configuration = CallHome.Profiles.Profile.SubscribeAlertGroup.Configuration()
                    self.configuration.parent = self
                    self._children_name_map["configuration"] = "configuration"
                    self._children_yang_names.add("configuration")

                    self.crash = CallHome.Profiles.Profile.SubscribeAlertGroup.Crash()
                    self.crash.parent = self
                    self._children_name_map["crash"] = "crash"
                    self._children_yang_names.add("crash")

                    self.environment = CallHome.Profiles.Profile.SubscribeAlertGroup.Environment()
                    self.environment.parent = self
                    self._children_name_map["environment"] = "environment"
                    self._children_yang_names.add("environment")

                    self.inventory = CallHome.Profiles.Profile.SubscribeAlertGroup.Inventory()
                    self.inventory.parent = self
                    self._children_name_map["inventory"] = "inventory"
                    self._children_yang_names.add("inventory")

                    self.snapshot = CallHome.Profiles.Profile.SubscribeAlertGroup.Snapshot()
                    self.snapshot.parent = self
                    self._children_name_map["snapshot"] = "snapshot"
                    self._children_yang_names.add("snapshot")

                    self.syslogs = CallHome.Profiles.Profile.SubscribeAlertGroup.Syslogs()
                    self.syslogs.parent = self
                    self._children_name_map["syslogs"] = "syslogs"
                    self._children_yang_names.add("syslogs")
                    self._segment_path = lambda: "subscribe-alert-group"


                class Configuration(Entity):
                    """
                    configuration info
                    
                    .. attribute:: periodic
                    
                    	Periodic call\-home message
                    	**type**\:   :py:class:`Periodic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.SubscribeAlertGroup.Configuration.Periodic>`
                    
                    .. attribute:: subscribe
                    
                    	Subscribe the alert\-group
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'call-home-cfg'
                    _revision = '2017-03-13'

                    def __init__(self):
                        super(CallHome.Profiles.Profile.SubscribeAlertGroup.Configuration, self).__init__()

                        self.yang_name = "configuration"
                        self.yang_parent_name = "subscribe-alert-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"periodic" : ("periodic", CallHome.Profiles.Profile.SubscribeAlertGroup.Configuration.Periodic)}
                        self._child_list_classes = {}

                        self.subscribe = YLeaf(YType.empty, "subscribe")

                        self.periodic = CallHome.Profiles.Profile.SubscribeAlertGroup.Configuration.Periodic()
                        self.periodic.parent = self
                        self._children_name_map["periodic"] = "periodic"
                        self._children_yang_names.add("periodic")
                        self._segment_path = lambda: "configuration"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CallHome.Profiles.Profile.SubscribeAlertGroup.Configuration, ['subscribe'], name, value)


                    class Periodic(Entity):
                        """
                        Periodic call\-home message
                        
                        .. attribute:: day
                        
                        	Day
                        	**type**\:  int
                        
                        	**range:** 0..31
                        
                        .. attribute:: hour
                        
                        	Hour
                        	**type**\:  int
                        
                        	**range:** 0..23
                        
                        .. attribute:: interval
                        
                        	none
                        	**type**\:   :py:class:`CallHomeMailSendInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHomeMailSendInterval>`
                        
                        .. attribute:: minute
                        
                        	Minute
                        	**type**\:  int
                        
                        	**range:** 0..59
                        
                        .. attribute:: weekday
                        
                        	Day of week
                        	**type**\:   :py:class:`CallHomeDayOfWeek <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHomeDayOfWeek>`
                        
                        

                        """

                        _prefix = 'call-home-cfg'
                        _revision = '2017-03-13'

                        def __init__(self):
                            super(CallHome.Profiles.Profile.SubscribeAlertGroup.Configuration.Periodic, self).__init__()

                            self.yang_name = "periodic"
                            self.yang_parent_name = "configuration"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.day = YLeaf(YType.uint32, "day")

                            self.hour = YLeaf(YType.uint32, "hour")

                            self.interval = YLeaf(YType.enumeration, "interval")

                            self.minute = YLeaf(YType.uint32, "minute")

                            self.weekday = YLeaf(YType.enumeration, "weekday")
                            self._segment_path = lambda: "periodic"

                        def __setattr__(self, name, value):
                            self._perform_setattr(CallHome.Profiles.Profile.SubscribeAlertGroup.Configuration.Periodic, ['day', 'hour', 'interval', 'minute', 'weekday'], name, value)


                class Crash(Entity):
                    """
                    Crash info
                    
                    .. attribute:: subscribe
                    
                    	Subscribe crash group
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'call-home-cfg'
                    _revision = '2017-03-13'

                    def __init__(self):
                        super(CallHome.Profiles.Profile.SubscribeAlertGroup.Crash, self).__init__()

                        self.yang_name = "crash"
                        self.yang_parent_name = "subscribe-alert-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.subscribe = YLeaf(YType.empty, "subscribe")
                        self._segment_path = lambda: "crash"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CallHome.Profiles.Profile.SubscribeAlertGroup.Crash, ['subscribe'], name, value)


                class Environment(Entity):
                    """
                    environmental info
                    
                    .. attribute:: severity
                    
                    	Severity
                    	**type**\:   :py:class:`CallHomeEventSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHomeEventSeverity>`
                    
                    

                    """

                    _prefix = 'call-home-cfg'
                    _revision = '2017-03-13'

                    def __init__(self):
                        super(CallHome.Profiles.Profile.SubscribeAlertGroup.Environment, self).__init__()

                        self.yang_name = "environment"
                        self.yang_parent_name = "subscribe-alert-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.severity = YLeaf(YType.enumeration, "severity")
                        self._segment_path = lambda: "environment"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CallHome.Profiles.Profile.SubscribeAlertGroup.Environment, ['severity'], name, value)


                class Inventory(Entity):
                    """
                    inventory info
                    
                    .. attribute:: periodic
                    
                    	Periodic call\-home message
                    	**type**\:   :py:class:`Periodic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.SubscribeAlertGroup.Inventory.Periodic>`
                    
                    .. attribute:: subscribe
                    
                    	Subscribe the alert\-group
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'call-home-cfg'
                    _revision = '2017-03-13'

                    def __init__(self):
                        super(CallHome.Profiles.Profile.SubscribeAlertGroup.Inventory, self).__init__()

                        self.yang_name = "inventory"
                        self.yang_parent_name = "subscribe-alert-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"periodic" : ("periodic", CallHome.Profiles.Profile.SubscribeAlertGroup.Inventory.Periodic)}
                        self._child_list_classes = {}

                        self.subscribe = YLeaf(YType.empty, "subscribe")

                        self.periodic = CallHome.Profiles.Profile.SubscribeAlertGroup.Inventory.Periodic()
                        self.periodic.parent = self
                        self._children_name_map["periodic"] = "periodic"
                        self._children_yang_names.add("periodic")
                        self._segment_path = lambda: "inventory"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CallHome.Profiles.Profile.SubscribeAlertGroup.Inventory, ['subscribe'], name, value)


                    class Periodic(Entity):
                        """
                        Periodic call\-home message
                        
                        .. attribute:: day
                        
                        	Day of month
                        	**type**\:  int
                        
                        	**range:** 0..31
                        
                        .. attribute:: hour
                        
                        	Hour
                        	**type**\:  int
                        
                        	**range:** 0..23
                        
                        .. attribute:: interval
                        
                        	none
                        	**type**\:   :py:class:`CallHomeMailSendInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHomeMailSendInterval>`
                        
                        .. attribute:: minute
                        
                        	Minute
                        	**type**\:  int
                        
                        	**range:** 0..59
                        
                        .. attribute:: weekday
                        
                        	Day of week
                        	**type**\:   :py:class:`CallHomeDayOfWeek <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHomeDayOfWeek>`
                        
                        

                        """

                        _prefix = 'call-home-cfg'
                        _revision = '2017-03-13'

                        def __init__(self):
                            super(CallHome.Profiles.Profile.SubscribeAlertGroup.Inventory.Periodic, self).__init__()

                            self.yang_name = "periodic"
                            self.yang_parent_name = "inventory"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.day = YLeaf(YType.uint32, "day")

                            self.hour = YLeaf(YType.uint32, "hour")

                            self.interval = YLeaf(YType.enumeration, "interval")

                            self.minute = YLeaf(YType.uint32, "minute")

                            self.weekday = YLeaf(YType.enumeration, "weekday")
                            self._segment_path = lambda: "periodic"

                        def __setattr__(self, name, value):
                            self._perform_setattr(CallHome.Profiles.Profile.SubscribeAlertGroup.Inventory.Periodic, ['day', 'hour', 'interval', 'minute', 'weekday'], name, value)


                class Snapshot(Entity):
                    """
                    snapshot info
                    
                    .. attribute:: periodic
                    
                    	Periodic call\-home message
                    	**type**\:   :py:class:`Periodic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.SubscribeAlertGroup.Snapshot.Periodic>`
                    
                    

                    """

                    _prefix = 'call-home-cfg'
                    _revision = '2017-03-13'

                    def __init__(self):
                        super(CallHome.Profiles.Profile.SubscribeAlertGroup.Snapshot, self).__init__()

                        self.yang_name = "snapshot"
                        self.yang_parent_name = "subscribe-alert-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"periodic" : ("periodic", CallHome.Profiles.Profile.SubscribeAlertGroup.Snapshot.Periodic)}
                        self._child_list_classes = {}

                        self.periodic = CallHome.Profiles.Profile.SubscribeAlertGroup.Snapshot.Periodic()
                        self.periodic.parent = self
                        self._children_name_map["periodic"] = "periodic"
                        self._children_yang_names.add("periodic")
                        self._segment_path = lambda: "snapshot"


                    class Periodic(Entity):
                        """
                        Periodic call\-home message
                        
                        .. attribute:: day
                        
                        	Day of month
                        	**type**\:  int
                        
                        	**range:** 0..31
                        
                        .. attribute:: hour
                        
                        	Hour
                        	**type**\:  int
                        
                        	**range:** 0..23
                        
                        .. attribute:: interval
                        
                        	none
                        	**type**\:   :py:class:`SnapshotInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.SnapshotInterval>`
                        
                        .. attribute:: minute
                        
                        	Minute
                        	**type**\:  int
                        
                        	**range:** 0..59
                        
                        .. attribute:: weekday
                        
                        	Day of week
                        	**type**\:   :py:class:`CallHomeDayOfWeek <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHomeDayOfWeek>`
                        
                        

                        """

                        _prefix = 'call-home-cfg'
                        _revision = '2017-03-13'

                        def __init__(self):
                            super(CallHome.Profiles.Profile.SubscribeAlertGroup.Snapshot.Periodic, self).__init__()

                            self.yang_name = "periodic"
                            self.yang_parent_name = "snapshot"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.day = YLeaf(YType.uint32, "day")

                            self.hour = YLeaf(YType.uint32, "hour")

                            self.interval = YLeaf(YType.enumeration, "interval")

                            self.minute = YLeaf(YType.uint32, "minute")

                            self.weekday = YLeaf(YType.enumeration, "weekday")
                            self._segment_path = lambda: "periodic"

                        def __setattr__(self, name, value):
                            self._perform_setattr(CallHome.Profiles.Profile.SubscribeAlertGroup.Snapshot.Periodic, ['day', 'hour', 'interval', 'minute', 'weekday'], name, value)


                class Syslogs(Entity):
                    """
                    syslog info
                    
                    .. attribute:: syslog
                    
                    	Syslog message pattern to be matched
                    	**type**\: list of    :py:class:`Syslog <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHome.Profiles.Profile.SubscribeAlertGroup.Syslogs.Syslog>`
                    
                    

                    """

                    _prefix = 'call-home-cfg'
                    _revision = '2017-03-13'

                    def __init__(self):
                        super(CallHome.Profiles.Profile.SubscribeAlertGroup.Syslogs, self).__init__()

                        self.yang_name = "syslogs"
                        self.yang_parent_name = "subscribe-alert-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"syslog" : ("syslog", CallHome.Profiles.Profile.SubscribeAlertGroup.Syslogs.Syslog)}

                        self.syslog = YList(self)
                        self._segment_path = lambda: "syslogs"

                    def __setattr__(self, name, value):
                        self._perform_setattr(CallHome.Profiles.Profile.SubscribeAlertGroup.Syslogs, [], name, value)


                    class Syslog(Entity):
                        """
                        Syslog message pattern to be matched
                        
                        .. attribute:: syslog_pattern  <key>
                        
                        	Syslog message pattern to be matched
                        	**type**\:  str
                        
                        	**length:** 1..80
                        
                        .. attribute:: severity
                        
                        	Severity
                        	**type**\:   :py:class:`CallHomeEventSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_call_home_cfg.CallHomeEventSeverity>`
                        
                        

                        """

                        _prefix = 'call-home-cfg'
                        _revision = '2017-03-13'

                        def __init__(self):
                            super(CallHome.Profiles.Profile.SubscribeAlertGroup.Syslogs.Syslog, self).__init__()

                            self.yang_name = "syslog"
                            self.yang_parent_name = "syslogs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.syslog_pattern = YLeaf(YType.str, "syslog-pattern")

                            self.severity = YLeaf(YType.enumeration, "severity")
                            self._segment_path = lambda: "syslog" + "[syslog-pattern='" + self.syslog_pattern.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(CallHome.Profiles.Profile.SubscribeAlertGroup.Syslogs.Syslog, ['syslog_pattern', 'severity'], name, value)


    class SmartLicensing(Entity):
        """
        Enable/disable licensing messages. By default is
        enabled.
        
        .. attribute:: active
        
        	Active the smart\-licensing
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: profile_name
        
        	To specify existing profile name used for TG so that licensing message
        	**type**\:  str
        
        

        """

        _prefix = 'call-home-cfg'
        _revision = '2017-03-13'

        def __init__(self):
            super(CallHome.SmartLicensing, self).__init__()

            self.yang_name = "smart-licensing"
            self.yang_parent_name = "call-home"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.active = YLeaf(YType.empty, "active")

            self.profile_name = YLeaf(YType.str, "profile-name")
            self._segment_path = lambda: "smart-licensing"
            self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CallHome.SmartLicensing, ['active', 'profile_name'], name, value)


    class SyslogThrottling(Entity):
        """
        Enable or disable call\-home syslog message
        throttling
        
        .. attribute:: active
        
        	Active syslog throttling
        	**type**\:  bool
        
        

        """

        _prefix = 'call-home-cfg'
        _revision = '2017-03-13'

        def __init__(self):
            super(CallHome.SyslogThrottling, self).__init__()

            self.yang_name = "syslog-throttling"
            self.yang_parent_name = "call-home"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.active = YLeaf(YType.boolean, "active")
            self._segment_path = lambda: "syslog-throttling"
            self._absolute_path = lambda: "Cisco-IOS-XR-call-home-cfg:call-home/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CallHome.SyslogThrottling, ['active'], name, value)

    def clone_ptr(self):
        self._top_entity = CallHome()
        return self._top_entity


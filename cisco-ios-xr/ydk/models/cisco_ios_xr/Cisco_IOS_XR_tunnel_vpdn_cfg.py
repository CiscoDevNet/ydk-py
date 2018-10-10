""" Cisco_IOS_XR_tunnel_vpdn_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tunnel\-vpdn package configuration.

This module contains definitions
for the following management objects\:
  vpdn\: VPDN configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class DfBit(Enum):
    """
    DfBit (Enum Class)

    Df bit

    .. data:: clear = 0

    	Clear df bit

    .. data:: reflect = 1

    	Reflect df bit from inner ip header

    .. data:: set = 2

    	Set df bit

    """

    clear = Enum.YLeaf(0, "clear")

    reflect = Enum.YLeaf(1, "reflect")

    set = Enum.YLeaf(2, "set")


class Option(Enum):
    """
    Option (Enum Class)

    Option

    .. data:: local = 1

    	Log VPDN events locally

    .. data:: user = 2

    	Log VPDN user events

    .. data:: dead_cache = 8

    	Log VPDN dead cache

    .. data:: tunnel_drop = 16

    	Log VPDN tunnel drops

    """

    local = Enum.YLeaf(1, "local")

    user = Enum.YLeaf(2, "user")

    dead_cache = Enum.YLeaf(8, "dead-cache")

    tunnel_drop = Enum.YLeaf(16, "tunnel-drop")



class Vpdn(Entity):
    """
    VPDN configuration
    
    .. attribute:: history
    
    	VPDN history logging
    	**type**\:  :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.History>`
    
    .. attribute:: redundancy
    
    	Enable VPDN redundancy
    	**type**\:  :py:class:`Redundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Redundancy>`
    
    .. attribute:: local
    
    	VPDN Local radius process configuration
    	**type**\:  :py:class:`Local <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Local>`
    
    .. attribute:: templates
    
    	Table of Template
    	**type**\:  :py:class:`Templates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates>`
    
    .. attribute:: caller_id
    
    	Options to apply on calling station ID
    	**type**\:  :py:class:`CallerId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.CallerId>`
    
    .. attribute:: vpd_ngroups
    
    	Table of VPDNgroup
    	**type**\:  :py:class:`VpdNgroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.VpdNgroups>`
    
    .. attribute:: loggings
    
    	Table of Logging
    	**type**\:  :py:class:`Loggings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Loggings>`
    
    .. attribute:: l2tp
    
    	L2TPv2 protocol commands
    	**type**\:  :py:class:`L2tp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.L2tp>`
    
    .. attribute:: session_limit
    
    	Maximum simultaneous VPDN sessions
    	**type**\: int
    
    	**range:** 1..131072
    
    .. attribute:: enable
    
    	Enable VPDN configuration. Deletion of this object also causes deletion of all associated objects under VPDN
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: soft_shut
    
    	New session no longer allowed
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'tunnel-vpdn-cfg'
    _revision = '2017-09-07'

    def __init__(self):
        super(Vpdn, self).__init__()
        self._top_entity = None

        self.yang_name = "vpdn"
        self.yang_parent_name = "Cisco-IOS-XR-tunnel-vpdn-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("history", ("history", Vpdn.History)), ("redundancy", ("redundancy", Vpdn.Redundancy)), ("local", ("local", Vpdn.Local)), ("templates", ("templates", Vpdn.Templates)), ("caller-id", ("caller_id", Vpdn.CallerId)), ("vpd-ngroups", ("vpd_ngroups", Vpdn.VpdNgroups)), ("loggings", ("loggings", Vpdn.Loggings)), ("l2tp", ("l2tp", Vpdn.L2tp))])
        self._leafs = OrderedDict([
            ('session_limit', (YLeaf(YType.uint32, 'session-limit'), ['int'])),
            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ('soft_shut', (YLeaf(YType.empty, 'soft-shut'), ['Empty'])),
        ])
        self.session_limit = None
        self.enable = None
        self.soft_shut = None

        self.history = Vpdn.History()
        self.history.parent = self
        self._children_name_map["history"] = "history"

        self.redundancy = Vpdn.Redundancy()
        self.redundancy.parent = self
        self._children_name_map["redundancy"] = "redundancy"

        self.local = Vpdn.Local()
        self.local.parent = self
        self._children_name_map["local"] = "local"

        self.templates = Vpdn.Templates()
        self.templates.parent = self
        self._children_name_map["templates"] = "templates"

        self.caller_id = Vpdn.CallerId()
        self.caller_id.parent = self
        self._children_name_map["caller_id"] = "caller-id"

        self.vpd_ngroups = Vpdn.VpdNgroups()
        self.vpd_ngroups.parent = self
        self._children_name_map["vpd_ngroups"] = "vpd-ngroups"

        self.loggings = Vpdn.Loggings()
        self.loggings.parent = self
        self._children_name_map["loggings"] = "loggings"

        self.l2tp = Vpdn.L2tp()
        self.l2tp.parent = self
        self._children_name_map["l2tp"] = "l2tp"
        self._segment_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Vpdn, ['session_limit', 'enable', 'soft_shut'], name, value)


    class History(Entity):
        """
        VPDN history logging
        
        .. attribute:: failure
        
        	User failure
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(Vpdn.History, self).__init__()

            self.yang_name = "history"
            self.yang_parent_name = "vpdn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('failure', (YLeaf(YType.empty, 'failure'), ['Empty'])),
            ])
            self.failure = None
            self._segment_path = lambda: "history"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vpdn.History, ['failure'], name, value)


    class Redundancy(Entity):
        """
        Enable VPDN redundancy
        
        .. attribute:: process_failures
        
        	Process crash configuration
        	**type**\:  :py:class:`ProcessFailures <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Redundancy.ProcessFailures>`
        
        .. attribute:: enable
        
        	Enable Enable VPDN redundancy. Deletion of this object also causes deletion of all associated objects under Redundancy
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(Vpdn.Redundancy, self).__init__()

            self.yang_name = "redundancy"
            self.yang_parent_name = "vpdn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("process-failures", ("process_failures", Vpdn.Redundancy.ProcessFailures))])
            self._leafs = OrderedDict([
                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ])
            self.enable = None

            self.process_failures = Vpdn.Redundancy.ProcessFailures()
            self.process_failures.parent = self
            self._children_name_map["process_failures"] = "process-failures"
            self._segment_path = lambda: "redundancy"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vpdn.Redundancy, ['enable'], name, value)


        class ProcessFailures(Entity):
            """
            Process crash configuration
            
            .. attribute:: switchover
            
            	Force a switchover if the process crashes
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'tunnel-vpdn-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Vpdn.Redundancy.ProcessFailures, self).__init__()

                self.yang_name = "process-failures"
                self.yang_parent_name = "redundancy"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('switchover', (YLeaf(YType.empty, 'switchover'), ['Empty'])),
                ])
                self.switchover = None
                self._segment_path = lambda: "process-failures"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/redundancy/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vpdn.Redundancy.ProcessFailures, ['switchover'], name, value)


    class Local(Entity):
        """
        VPDN Local radius process configuration
        
        .. attribute:: secret_text
        
        	secret password
        	**type**\: str
        
        	**length:** 1..32
        
        .. attribute:: path
        
        	local path of the saved profile
        	**type**\: str
        
        	**length:** 1..64
        
        .. attribute:: cache_disabled
        
        	Set constant integer
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: port
        
        	port value
        	**type**\: int
        
        	**range:** 1..65535
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(Vpdn.Local, self).__init__()

            self.yang_name = "local"
            self.yang_parent_name = "vpdn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('secret_text', (YLeaf(YType.str, 'secret-text'), ['str'])),
                ('path', (YLeaf(YType.str, 'path'), ['str'])),
                ('cache_disabled', (YLeaf(YType.empty, 'cache-disabled'), ['Empty'])),
                ('port', (YLeaf(YType.uint16, 'port'), ['int'])),
            ])
            self.secret_text = None
            self.path = None
            self.cache_disabled = None
            self.port = None
            self._segment_path = lambda: "local"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vpdn.Local, ['secret_text', 'path', 'cache_disabled', 'port'], name, value)


    class Templates(Entity):
        """
        Table of Template
        
        .. attribute:: template
        
        	VPDN template configuration
        	**type**\: list of  		 :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates.Template>`
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(Vpdn.Templates, self).__init__()

            self.yang_name = "templates"
            self.yang_parent_name = "vpdn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("template", ("template", Vpdn.Templates.Template))])
            self._leafs = OrderedDict()

            self.template = YList(self)
            self._segment_path = lambda: "templates"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vpdn.Templates, [], name, value)


        class Template(Entity):
            """
            VPDN template configuration
            
            .. attribute:: template_name  (key)
            
            	VPDN template name
            	**type**\: str
            
            	**length:** 1..63
            
            .. attribute:: caller_id
            
            	Options to apply on calling station id
            	**type**\:  :py:class:`CallerId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates.Template.CallerId>`
            
            .. attribute:: vpn
            
            	VPN ID/VRF name
            	**type**\:  :py:class:`Vpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates.Template.Vpn>`
            
            .. attribute:: tunnel
            
            	L2TP tunnel commands
            	**type**\:  :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates.Template.Tunnel>`
            
            .. attribute:: ip
            
            	Set IP TOS value
            	**type**\:  :py:class:`Ip <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates.Template.Ip>`
            
            .. attribute:: ipv4
            
            	IPv4 settings for tunnel
            	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates.Template.Ipv4>`
            
            .. attribute:: cisco_avp100_format_e_enable
            
            	To support NAS\-Port format e in Cisco AVP 100
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: description
            
            	Up to 100 characters describing this VPDN template
            	**type**\: str
            
            	**length:** 1..100
            
            .. attribute:: l2tp_class
            
            	L2TP class  command
            	**type**\: str
            
            	**length:** 1..79
            
            .. attribute:: dsl_line_forwarding
            
            	Forward DSL Line Info attributes
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'tunnel-vpdn-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Vpdn.Templates.Template, self).__init__()

                self.yang_name = "template"
                self.yang_parent_name = "templates"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['template_name']
                self._child_classes = OrderedDict([("caller-id", ("caller_id", Vpdn.Templates.Template.CallerId)), ("vpn", ("vpn", Vpdn.Templates.Template.Vpn)), ("tunnel", ("tunnel", Vpdn.Templates.Template.Tunnel)), ("ip", ("ip", Vpdn.Templates.Template.Ip)), ("ipv4", ("ipv4", Vpdn.Templates.Template.Ipv4))])
                self._leafs = OrderedDict([
                    ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                    ('cisco_avp100_format_e_enable', (YLeaf(YType.empty, 'cisco-avp100-format-e-enable'), ['Empty'])),
                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                    ('l2tp_class', (YLeaf(YType.str, 'l2tp-class'), ['str'])),
                    ('dsl_line_forwarding', (YLeaf(YType.empty, 'dsl-line-forwarding'), ['Empty'])),
                ])
                self.template_name = None
                self.cisco_avp100_format_e_enable = None
                self.description = None
                self.l2tp_class = None
                self.dsl_line_forwarding = None

                self.caller_id = Vpdn.Templates.Template.CallerId()
                self.caller_id.parent = self
                self._children_name_map["caller_id"] = "caller-id"

                self.vpn = Vpdn.Templates.Template.Vpn()
                self.vpn.parent = self
                self._children_name_map["vpn"] = "vpn"

                self.tunnel = Vpdn.Templates.Template.Tunnel()
                self.tunnel.parent = self
                self._children_name_map["tunnel"] = "tunnel"

                self.ip = Vpdn.Templates.Template.Ip()
                self.ip.parent = self
                self._children_name_map["ip"] = "ip"

                self.ipv4 = Vpdn.Templates.Template.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"
                self._segment_path = lambda: "template" + "[template-name='" + str(self.template_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/templates/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vpdn.Templates.Template, ['template_name', 'cisco_avp100_format_e_enable', 'description', 'l2tp_class', 'dsl_line_forwarding'], name, value)


            class CallerId(Entity):
                """
                Options to apply on calling station id
                
                .. attribute:: mask
                
                	Mask characters by method
                	**type**\: str
                
                	**length:** 1..63
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Vpdn.Templates.Template.CallerId, self).__init__()

                    self.yang_name = "caller-id"
                    self.yang_parent_name = "template"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('mask', (YLeaf(YType.str, 'mask'), ['str'])),
                    ])
                    self.mask = None
                    self._segment_path = lambda: "caller-id"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vpdn.Templates.Template.CallerId, ['mask'], name, value)


            class Vpn(Entity):
                """
                VPN ID/VRF name
                
                .. attribute:: id
                
                	VPN ID
                	**type**\:  :py:class:`Id <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates.Template.Vpn.Id>`
                
                .. attribute:: vrf
                
                	VRF name
                	**type**\: str
                
                	**length:** 1..32
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Vpdn.Templates.Template.Vpn, self).__init__()

                    self.yang_name = "vpn"
                    self.yang_parent_name = "template"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("id", ("id", Vpdn.Templates.Template.Vpn.Id))])
                    self._leafs = OrderedDict([
                        ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                    ])
                    self.vrf = None

                    self.id = Vpdn.Templates.Template.Vpn.Id()
                    self.id.parent = self
                    self._children_name_map["id"] = "id"
                    self._segment_path = lambda: "vpn"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vpdn.Templates.Template.Vpn, ['vrf'], name, value)


                class Id(Entity):
                    """
                    VPN ID
                    
                    .. attribute:: oui
                    
                    	VPN ID, (OUI\:VPN\-Index) format(hex), 3 bytes OUI Part
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                    
                    .. attribute:: index
                    
                    	VPN ID, (OUI\:VPN\-Index) format(hex), 4 bytes VPN\_Index Part
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                    
                    

                    """

                    _prefix = 'tunnel-vpdn-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Vpdn.Templates.Template.Vpn.Id, self).__init__()

                        self.yang_name = "id"
                        self.yang_parent_name = "vpn"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('oui', (YLeaf(YType.str, 'oui'), ['str'])),
                            ('index', (YLeaf(YType.str, 'index'), ['str'])),
                        ])
                        self.oui = None
                        self.index = None
                        self._segment_path = lambda: "id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vpdn.Templates.Template.Vpn.Id, ['oui', 'index'], name, value)


            class Tunnel(Entity):
                """
                L2TP tunnel commands
                
                .. attribute:: busy_timeout
                
                	Busy time out value in seconds
                	**type**\: int
                
                	**range:** 60..65535
                
                	**units**\: second
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Vpdn.Templates.Template.Tunnel, self).__init__()

                    self.yang_name = "tunnel"
                    self.yang_parent_name = "template"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('busy_timeout', (YLeaf(YType.uint32, 'busy-timeout'), ['int'])),
                    ])
                    self.busy_timeout = None
                    self._segment_path = lambda: "tunnel"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vpdn.Templates.Template.Tunnel, ['busy_timeout'], name, value)


            class Ip(Entity):
                """
                Set IP TOS value
                
                .. attribute:: tos
                
                	Set constant integer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Vpdn.Templates.Template.Ip, self).__init__()

                    self.yang_name = "ip"
                    self.yang_parent_name = "template"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('tos', (YLeaf(YType.uint32, 'tos'), ['int'])),
                    ])
                    self.tos = None
                    self._segment_path = lambda: "ip"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vpdn.Templates.Template.Ip, ['tos'], name, value)


            class Ipv4(Entity):
                """
                IPv4 settings for tunnel
                
                .. attribute:: df_bit
                
                	IPv4 don't fragment bit set/clear/reflect
                	**type**\:  :py:class:`DfBit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.DfBit>`
                
                .. attribute:: source
                
                	Enter an IP address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Vpdn.Templates.Template.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "template"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('df_bit', (YLeaf(YType.enumeration, 'df-bit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'DfBit', '')])),
                        ('source', (YLeaf(YType.str, 'source'), ['str'])),
                    ])
                    self.df_bit = None
                    self.source = None
                    self._segment_path = lambda: "ipv4"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vpdn.Templates.Template.Ipv4, ['df_bit', 'source'], name, value)


    class CallerId(Entity):
        """
        Options to apply on calling station ID
        
        .. attribute:: mask
        
        	Mask characters by method
        	**type**\: str
        
        	**length:** 1..63
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(Vpdn.CallerId, self).__init__()

            self.yang_name = "caller-id"
            self.yang_parent_name = "vpdn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('mask', (YLeaf(YType.str, 'mask'), ['str'])),
            ])
            self.mask = None
            self._segment_path = lambda: "caller-id"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vpdn.CallerId, ['mask'], name, value)


    class VpdNgroups(Entity):
        """
        Table of VPDNgroup
        
        .. attribute:: vpd_ngroup
        
        	vpdn\-group configuration
        	**type**\: list of  		 :py:class:`VpdNgroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.VpdNgroups.VpdNgroup>`
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(Vpdn.VpdNgroups, self).__init__()

            self.yang_name = "vpd-ngroups"
            self.yang_parent_name = "vpdn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vpd-ngroup", ("vpd_ngroup", Vpdn.VpdNgroups.VpdNgroup))])
            self._leafs = OrderedDict()

            self.vpd_ngroup = YList(self)
            self._segment_path = lambda: "vpd-ngroups"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vpdn.VpdNgroups, [], name, value)


        class VpdNgroup(Entity):
            """
            vpdn\-group configuration
            
            .. attribute:: vpd_ngroupname  (key)
            
            	vpdn\-group name
            	**type**\: str
            
            	**length:** 1..63
            
            .. attribute:: vpn_id
            
            	Vpn id
            	**type**\:  :py:class:`VpnId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.VpdNgroups.VpdNgroup.VpnId>`
            
            .. attribute:: ip
            
            	set ip tos value
            	**type**\:  :py:class:`Ip <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.VpdNgroups.VpdNgroup.Ip>`
            
            .. attribute:: dsl_line_forwarding
            
            	Forward DSL Line Info attributes
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: cisco_avp100_format_e_enable
            
            	To support NAS\-Port format e in cisco AVP 100
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: desc
            
            	upto 100 characters describing this VPDN group
            	**type**\: str
            
            	**length:** 1..100
            
            .. attribute:: attribute
            
            	match substring
            	**type**\: str
            
            	**length:** 1..63
            
            .. attribute:: l2tp_class
            
            	l2tp class name
            	**type**\: str
            
            	**length:** 1..79
            
            .. attribute:: tunnel_busy_timeout
            
            	Busy list timeout length
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: vrf_name
            
            	Vrf name
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: sr_ctemplate
            
            	Source vpdn\-template
            	**type**\: str
            
            	**length:** 1..63
            
            

            """

            _prefix = 'tunnel-vpdn-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Vpdn.VpdNgroups.VpdNgroup, self).__init__()

                self.yang_name = "vpd-ngroup"
                self.yang_parent_name = "vpd-ngroups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vpd_ngroupname']
                self._child_classes = OrderedDict([("vpn-id", ("vpn_id", Vpdn.VpdNgroups.VpdNgroup.VpnId)), ("ip", ("ip", Vpdn.VpdNgroups.VpdNgroup.Ip))])
                self._leafs = OrderedDict([
                    ('vpd_ngroupname', (YLeaf(YType.str, 'vpd-ngroupname'), ['str'])),
                    ('dsl_line_forwarding', (YLeaf(YType.empty, 'dsl-line-forwarding'), ['Empty'])),
                    ('cisco_avp100_format_e_enable', (YLeaf(YType.empty, 'cisco-avp100-format-e-enable'), ['Empty'])),
                    ('desc', (YLeaf(YType.str, 'desc'), ['str'])),
                    ('attribute', (YLeaf(YType.str, 'attribute'), ['str'])),
                    ('l2tp_class', (YLeaf(YType.str, 'l2tp-class'), ['str'])),
                    ('tunnel_busy_timeout', (YLeaf(YType.uint32, 'tunnel-busy-timeout'), ['int'])),
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ('sr_ctemplate', (YLeaf(YType.str, 'sr-ctemplate'), ['str'])),
                ])
                self.vpd_ngroupname = None
                self.dsl_line_forwarding = None
                self.cisco_avp100_format_e_enable = None
                self.desc = None
                self.attribute = None
                self.l2tp_class = None
                self.tunnel_busy_timeout = None
                self.vrf_name = None
                self.sr_ctemplate = None

                self.vpn_id = Vpdn.VpdNgroups.VpdNgroup.VpnId()
                self.vpn_id.parent = self
                self._children_name_map["vpn_id"] = "vpn-id"

                self.ip = Vpdn.VpdNgroups.VpdNgroup.Ip()
                self.ip.parent = self
                self._children_name_map["ip"] = "ip"
                self._segment_path = lambda: "vpd-ngroup" + "[vpd-ngroupname='" + str(self.vpd_ngroupname) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/vpd-ngroups/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vpdn.VpdNgroups.VpdNgroup, ['vpd_ngroupname', 'dsl_line_forwarding', 'cisco_avp100_format_e_enable', 'desc', 'attribute', 'l2tp_class', 'tunnel_busy_timeout', 'vrf_name', 'sr_ctemplate'], name, value)


            class VpnId(Entity):
                """
                Vpn id
                
                .. attribute:: vpn_id_oui
                
                	VPN ID, (OUI\:VPN\-Index) format(hex), 3 bytes OUI Part
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: vpn_id_index
                
                	VPN ID, (OUI\:VPN\-Index) format(hex), 4 bytes VPN\_Index Part
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Vpdn.VpdNgroups.VpdNgroup.VpnId, self).__init__()

                    self.yang_name = "vpn-id"
                    self.yang_parent_name = "vpd-ngroup"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('vpn_id_oui', (YLeaf(YType.str, 'vpn-id-oui'), ['str'])),
                        ('vpn_id_index', (YLeaf(YType.str, 'vpn-id-index'), ['str'])),
                    ])
                    self.vpn_id_oui = None
                    self.vpn_id_index = None
                    self._segment_path = lambda: "vpn-id"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vpdn.VpdNgroups.VpdNgroup.VpnId, ['vpn_id_oui', 'vpn_id_index'], name, value)


            class Ip(Entity):
                """
                set ip tos value
                
                .. attribute:: tos
                
                	ip tos value
                	**type**\: int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Vpdn.VpdNgroups.VpdNgroup.Ip, self).__init__()

                    self.yang_name = "ip"
                    self.yang_parent_name = "vpd-ngroup"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('tos', (YLeaf(YType.uint32, 'tos'), ['int'])),
                    ])
                    self.tos = None
                    self._segment_path = lambda: "ip"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vpdn.VpdNgroups.VpdNgroup.Ip, ['tos'], name, value)


    class Loggings(Entity):
        """
        Table of Logging
        
        .. attribute:: logging
        
        	Configure logging for VPDN
        	**type**\: list of  		 :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Loggings.Logging>`
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(Vpdn.Loggings, self).__init__()

            self.yang_name = "loggings"
            self.yang_parent_name = "vpdn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("logging", ("logging", Vpdn.Loggings.Logging))])
            self._leafs = OrderedDict()

            self.logging = YList(self)
            self._segment_path = lambda: "loggings"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vpdn.Loggings, [], name, value)


        class Logging(Entity):
            """
            Configure logging for VPDN
            
            .. attribute:: option  (key)
            
            	VPDN logging options
            	**type**\:  :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Option>`
            
            

            """

            _prefix = 'tunnel-vpdn-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Vpdn.Loggings.Logging, self).__init__()

                self.yang_name = "logging"
                self.yang_parent_name = "loggings"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['option']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('option', (YLeaf(YType.enumeration, 'option'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'Option', '')])),
                ])
                self.option = None
                self._segment_path = lambda: "logging" + "[option='" + str(self.option) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/loggings/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vpdn.Loggings.Logging, ['option'], name, value)


    class L2tp(Entity):
        """
        L2TPv2 protocol commands
        
        .. attribute:: session_id
        
        	Session ID commands
        	**type**\:  :py:class:`SessionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.L2tp.SessionId>`
        
        .. attribute:: tcp_mss_adjust
        
        	TCP MSS adjust value. The acceptable values might be further limited depending on platform
        	**type**\: int
        
        	**range:** 1280..1460
        
        .. attribute:: reassembly
        
        	L2TP IP packet reassembly enable
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(Vpdn.L2tp, self).__init__()

            self.yang_name = "l2tp"
            self.yang_parent_name = "vpdn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("session-id", ("session_id", Vpdn.L2tp.SessionId))])
            self._leafs = OrderedDict([
                ('tcp_mss_adjust', (YLeaf(YType.uint32, 'tcp-mss-adjust'), ['int'])),
                ('reassembly', (YLeaf(YType.empty, 'reassembly'), ['Empty'])),
            ])
            self.tcp_mss_adjust = None
            self.reassembly = None

            self.session_id = Vpdn.L2tp.SessionId()
            self.session_id.parent = self
            self._children_name_map["session_id"] = "session-id"
            self._segment_path = lambda: "l2tp"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vpdn.L2tp, ['tcp_mss_adjust', 'reassembly'], name, value)


        class SessionId(Entity):
            """
            Session ID commands
            
            .. attribute:: space
            
            	Session ID space commands
            	**type**\:  :py:class:`Space <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.L2tp.SessionId.Space>`
            
            

            """

            _prefix = 'tunnel-vpdn-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(Vpdn.L2tp.SessionId, self).__init__()

                self.yang_name = "session-id"
                self.yang_parent_name = "l2tp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("space", ("space", Vpdn.L2tp.SessionId.Space))])
                self._leafs = OrderedDict()

                self.space = Vpdn.L2tp.SessionId.Space()
                self.space.parent = self
                self._children_name_map["space"] = "space"
                self._segment_path = lambda: "session-id"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/l2tp/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vpdn.L2tp.SessionId, [], name, value)


            class Space(Entity):
                """
                Session ID space commands
                
                .. attribute:: hierarchy
                
                	Session ID space hierarchical command
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Vpdn.L2tp.SessionId.Space, self).__init__()

                    self.yang_name = "space"
                    self.yang_parent_name = "session-id"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('hierarchy', (YLeaf(YType.empty, 'hierarchy'), ['Empty'])),
                    ])
                    self.hierarchy = None
                    self._segment_path = lambda: "space"
                    self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/l2tp/session-id/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vpdn.L2tp.SessionId.Space, ['hierarchy'], name, value)

    def clone_ptr(self):
        self._top_entity = Vpdn()
        return self._top_entity


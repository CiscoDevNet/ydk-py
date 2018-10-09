""" Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-pppoe\-ma\-gbl package configuration.

This module contains definitions
for the following management objects\:
  pppoe\-cfg\: PPPOE configuration data

This YANG module augments the
  Cisco\-IOS\-XR\-subscriber\-infra\-tmplmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class PppoeInvalidSessionIdBehavior(Enum):
    """
    PppoeInvalidSessionIdBehavior (Enum Class)

    Pppoe invalid session id behavior

    .. data:: drop = 0

    	Drop packets with an invalid session ID

    .. data:: log = 1

    	Log packets with an invalid session ID

    """

    drop = Enum.YLeaf(0, "drop")

    log = Enum.YLeaf(1, "log")



class PppoeCfg(Entity):
    """
    PPPOE configuration data
    
    .. attribute:: pppoe_bba_groups
    
    	PPPoE BBA\-Group configuration data
    	**type**\:  :py:class:`PppoeBbaGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups>`
    
    .. attribute:: session_id_space_flat
    
    	Disable per\-parent session ID spaces
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: in_flight_window
    
    	Set the PPPoE in\-flight window size
    	**type**\: int
    
    	**range:** 1..20000
    
    

    """

    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
    _revision = '2017-09-30'

    def __init__(self):
        super(PppoeCfg, self).__init__()
        self._top_entity = None

        self.yang_name = "pppoe-cfg"
        self.yang_parent_name = "Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("pppoe-bba-groups", ("pppoe_bba_groups", PppoeCfg.PppoeBbaGroups))])
        self._leafs = OrderedDict([
            ('session_id_space_flat', (YLeaf(YType.empty, 'session-id-space-flat'), ['Empty'])),
            ('in_flight_window', (YLeaf(YType.uint32, 'in-flight-window'), ['int'])),
        ])
        self.session_id_space_flat = None
        self.in_flight_window = None

        self.pppoe_bba_groups = PppoeCfg.PppoeBbaGroups()
        self.pppoe_bba_groups.parent = self
        self._children_name_map["pppoe_bba_groups"] = "pppoe-bba-groups"
        self._segment_path = lambda: "Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:pppoe-cfg"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PppoeCfg, ['session_id_space_flat', 'in_flight_window'], name, value)


    class PppoeBbaGroups(Entity):
        """
        PPPoE BBA\-Group configuration data
        
        .. attribute:: pppoe_bba_group
        
        	PPPoE BBA\-Group configuration data
        	**type**\: list of  		 :py:class:`PppoeBbaGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup>`
        
        

        """

        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
        _revision = '2017-09-30'

        def __init__(self):
            super(PppoeCfg.PppoeBbaGroups, self).__init__()

            self.yang_name = "pppoe-bba-groups"
            self.yang_parent_name = "pppoe-cfg"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("pppoe-bba-group", ("pppoe_bba_group", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup))])
            self._leafs = OrderedDict()

            self.pppoe_bba_group = YList(self)
            self._segment_path = lambda: "pppoe-bba-groups"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:pppoe-cfg/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PppoeCfg.PppoeBbaGroups, [], name, value)


        class PppoeBbaGroup(Entity):
            """
            PPPoE BBA\-Group configuration data
            
            .. attribute:: bba_group  (key)
            
            	BBA\-Group name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: tag
            
            	PPPoE tag configuration data
            	**type**\:  :py:class:`Tag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag>`
            
            .. attribute:: sessions
            
            	PPPoE session configuration data
            	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions>`
            
            .. attribute:: control_packets
            
            	PPPoE control\-packet configuration data
            	**type**\:  :py:class:`ControlPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.ControlPackets>`
            
            .. attribute:: pa_do_delay
            
            	PPPoE PADO delay configuration data
            	**type**\:  :py:class:`PaDoDelay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay>`
            
            	**presence node**\: True
            
            .. attribute:: completion_timeout
            
            	PPPoE session completion timeout
            	**type**\: int
            
            	**range:** 30..600
            
            .. attribute:: invalid_session_id
            
            	Invalid session\-ID behavior
            	**type**\:  :py:class:`PppoeInvalidSessionIdBehavior <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeInvalidSessionIdBehavior>`
            
            .. attribute:: enable_padt_after_shut_down
            
            	Enable padt after shutdown
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: mtu
            
            	PPPoE default MTU
            	**type**\: int
            
            	**range:** 500..2000
            
            

            """

            _prefix = 'subscriber-pppoe-ma-gbl-cfg'
            _revision = '2017-09-30'

            def __init__(self):
                super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup, self).__init__()

                self.yang_name = "pppoe-bba-group"
                self.yang_parent_name = "pppoe-bba-groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['bba_group']
                self._child_classes = OrderedDict([("tag", ("tag", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag)), ("sessions", ("sessions", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions)), ("control-packets", ("control_packets", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.ControlPackets)), ("pa-do-delay", ("pa_do_delay", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay))])
                self._leafs = OrderedDict([
                    ('bba_group', (YLeaf(YType.str, 'bba-group'), ['str'])),
                    ('completion_timeout', (YLeaf(YType.uint32, 'completion-timeout'), ['int'])),
                    ('invalid_session_id', (YLeaf(YType.enumeration, 'invalid-session-id'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg', 'PppoeInvalidSessionIdBehavior', '')])),
                    ('enable_padt_after_shut_down', (YLeaf(YType.empty, 'enable-padt-after-shut-down'), ['Empty'])),
                    ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                ])
                self.bba_group = None
                self.completion_timeout = None
                self.invalid_session_id = None
                self.enable_padt_after_shut_down = None
                self.mtu = None

                self.tag = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag()
                self.tag.parent = self
                self._children_name_map["tag"] = "tag"

                self.sessions = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"

                self.control_packets = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.ControlPackets()
                self.control_packets.parent = self
                self._children_name_map["control_packets"] = "control-packets"

                self.pa_do_delay = None
                self._children_name_map["pa_do_delay"] = "pa-do-delay"
                self._segment_path = lambda: "pppoe-bba-group" + "[bba-group='" + str(self.bba_group) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:pppoe-cfg/pppoe-bba-groups/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup, ['bba_group', 'completion_timeout', 'invalid_session_id', 'enable_padt_after_shut_down', 'mtu'], name, value)


            class Tag(Entity):
                """
                PPPoE tag configuration data
                
                .. attribute:: padr
                
                	PADR packets
                	**type**\:  :py:class:`Padr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.Padr>`
                
                .. attribute:: service_name_configureds
                
                	Service name
                	**type**\:  :py:class:`ServiceNameConfigureds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds>`
                
                .. attribute:: ppp_max_payload
                
                	Minimum and maximum payloads
                	**type**\:  :py:class:`PppMaxPayload <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.PppMaxPayload>`
                
                	**presence node**\: True
                
                .. attribute:: ppp_max_payload_deny
                
                	Ignore the ppp\-max\-payload tag
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: service_selection_disable
                
                	Disable advertising of unrequested service names
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ac_name
                
                	The name to include in the AC tag
                	**type**\: str
                
                

                """

                _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                _revision = '2017-09-30'

                def __init__(self):
                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag, self).__init__()

                    self.yang_name = "tag"
                    self.yang_parent_name = "pppoe-bba-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("padr", ("padr", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.Padr)), ("service-name-configureds", ("service_name_configureds", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds)), ("ppp-max-payload", ("ppp_max_payload", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.PppMaxPayload))])
                    self._leafs = OrderedDict([
                        ('ppp_max_payload_deny', (YLeaf(YType.empty, 'ppp-max-payload-deny'), ['Empty'])),
                        ('service_selection_disable', (YLeaf(YType.empty, 'service-selection-disable'), ['Empty'])),
                        ('ac_name', (YLeaf(YType.str, 'ac-name'), ['str'])),
                    ])
                    self.ppp_max_payload_deny = None
                    self.service_selection_disable = None
                    self.ac_name = None

                    self.padr = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.Padr()
                    self.padr.parent = self
                    self._children_name_map["padr"] = "padr"

                    self.service_name_configureds = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds()
                    self.service_name_configureds.parent = self
                    self._children_name_map["service_name_configureds"] = "service-name-configureds"

                    self.ppp_max_payload = None
                    self._children_name_map["ppp_max_payload"] = "ppp-max-payload"
                    self._segment_path = lambda: "tag"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag, ['ppp_max_payload_deny', 'service_selection_disable', 'ac_name'], name, value)


                class Padr(Entity):
                    """
                    PADR packets
                    
                    .. attribute:: session_unique_relay_session_id
                    
                    	Allow sessions to come up with unique relay\-session\-id in padr
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: invalid_payload_allow
                    
                    	Allow sessions to come up with invalid\-payload
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.Padr, self).__init__()

                        self.yang_name = "padr"
                        self.yang_parent_name = "tag"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('session_unique_relay_session_id', (YLeaf(YType.empty, 'session-unique-relay-session-id'), ['Empty'])),
                            ('invalid_payload_allow', (YLeaf(YType.empty, 'invalid-payload-allow'), ['Empty'])),
                        ])
                        self.session_unique_relay_session_id = None
                        self.invalid_payload_allow = None
                        self._segment_path = lambda: "padr"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.Padr, ['session_unique_relay_session_id', 'invalid_payload_allow'], name, value)


                class ServiceNameConfigureds(Entity):
                    """
                    Service name
                    
                    .. attribute:: service_name_configured
                    
                    	Service name supported on this group
                    	**type**\: list of  		 :py:class:`ServiceNameConfigured <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds.ServiceNameConfigured>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds, self).__init__()

                        self.yang_name = "service-name-configureds"
                        self.yang_parent_name = "tag"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("service-name-configured", ("service_name_configured", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds.ServiceNameConfigured))])
                        self._leafs = OrderedDict()

                        self.service_name_configured = YList(self)
                        self._segment_path = lambda: "service-name-configureds"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds, [], name, value)


                    class ServiceNameConfigured(Entity):
                        """
                        Service name supported on this group
                        
                        .. attribute:: name  (key)
                        
                        	Service name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                        _revision = '2017-09-30'

                        def __init__(self):
                            super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds.ServiceNameConfigured, self).__init__()

                            self.yang_name = "service-name-configured"
                            self.yang_parent_name = "service-name-configureds"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ])
                            self.name = None
                            self._segment_path = lambda: "service-name-configured" + "[name='" + str(self.name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds.ServiceNameConfigured, ['name'], name, value)


                class PppMaxPayload(Entity):
                    """
                    Minimum and maximum payloads
                    
                    .. attribute:: min
                    
                    	Minimum payload
                    	**type**\: int
                    
                    	**range:** 500..2000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: max
                    
                    	Maximum payload
                    	**type**\: int
                    
                    	**range:** 500..2000
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.PppMaxPayload, self).__init__()

                        self.yang_name = "ppp-max-payload"
                        self.yang_parent_name = "tag"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('min', (YLeaf(YType.uint32, 'min'), ['int'])),
                            ('max', (YLeaf(YType.uint32, 'max'), ['int'])),
                        ])
                        self.min = None
                        self.max = None
                        self._segment_path = lambda: "ppp-max-payload"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.PppMaxPayload, ['min', 'max'], name, value)


            class Sessions(Entity):
                """
                PPPoE session configuration data
                
                .. attribute:: vlan_throttle
                
                	Set VLAN (inner + outer tags) session throttle
                	**type**\:  :py:class:`VlanThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: inner_vlan_throttle
                
                	Set Inner VLAN session throttle
                	**type**\:  :py:class:`InnerVlanThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: remote_id_limit
                
                	Set Remote ID session limit and threshold
                	**type**\:  :py:class:`RemoteIdLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdLimit>`
                
                	**presence node**\: True
                
                .. attribute:: mac_iwf_access_interface_throttle
                
                	Set per\-MAC/Access interface throttle for IWF sessions
                	**type**\:  :py:class:`MacIwfAccessInterfaceThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: access_interface_limit
                
                	Set per\-access interface limit
                	**type**\:  :py:class:`AccessInterfaceLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.AccessInterfaceLimit>`
                
                	**presence node**\: True
                
                .. attribute:: mac_access_interface_throttle
                
                	Set per\-MAC/Access Interface throttle
                	**type**\:  :py:class:`MacAccessInterfaceThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: outer_vlan_limit
                
                	Set Outer VLAN session limit and threshold
                	**type**\:  :py:class:`OuterVlanLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanLimit>`
                
                	**presence node**\: True
                
                .. attribute:: circuit_id_throttle
                
                	Set Circuit ID session throttle
                	**type**\:  :py:class:`CircuitIdThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: mac_limit
                
                	Set per\-MAC address session limit and threshold
                	**type**\:  :py:class:`MacLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacLimit>`
                
                	**presence node**\: True
                
                .. attribute:: circuit_id_limit
                
                	Set Circuit ID session limit and threshold
                	**type**\:  :py:class:`CircuitIdLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdLimit>`
                
                	**presence node**\: True
                
                .. attribute:: mac_iwf_limit
                
                	Set per\-MAC session limit and threshold for IWF sessions
                	**type**\:  :py:class:`MacIwfLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfLimit>`
                
                	**presence node**\: True
                
                .. attribute:: mac_iwf_access_interface_limit
                
                	Set per\-MAC access interface session limit and threshold for IWF sessions
                	**type**\:  :py:class:`MacIwfAccessInterfaceLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceLimit>`
                
                	**presence node**\: True
                
                .. attribute:: inner_vlan_limit
                
                	Set Inner VLAN session limit and threshold
                	**type**\:  :py:class:`InnerVlanLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanLimit>`
                
                	**presence node**\: True
                
                .. attribute:: outer_vlan_throttle
                
                	Set Outer VLAN session throttle
                	**type**\:  :py:class:`OuterVlanThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: mac_throttle
                
                	Set per\-MAC throttle
                	**type**\:  :py:class:`MacThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: circuit_id_and_remote_id_limit
                
                	Set Circuit ID and Remote ID session limit/threshold
                	**type**\:  :py:class:`CircuitIdAndRemoteIdLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdLimit>`
                
                	**presence node**\: True
                
                .. attribute:: vlan_limit
                
                	Set VLAN (inner + outer tags) session limit and threshold
                	**type**\:  :py:class:`VlanLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanLimit>`
                
                	**presence node**\: True
                
                .. attribute:: mac_access_interface_limit
                
                	Set per\-MAC access interface session limit and threshold
                	**type**\:  :py:class:`MacAccessInterfaceLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceLimit>`
                
                	**presence node**\: True
                
                .. attribute:: remote_id_throttle
                
                	Set Remote ID session throttle
                	**type**\:  :py:class:`RemoteIdThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: max_limit
                
                	Set per\-card session limit and threshold
                	**type**\:  :py:class:`MaxLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MaxLimit>`
                
                	**presence node**\: True
                
                .. attribute:: circuit_id_and_remote_id_throttle
                
                	Set Circuit ID and Remote ID session throttle
                	**type**\:  :py:class:`CircuitIdAndRemoteIdThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdThrottle>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                _revision = '2017-09-30'

                def __init__(self):
                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "pppoe-bba-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("vlan-throttle", ("vlan_throttle", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanThrottle)), ("inner-vlan-throttle", ("inner_vlan_throttle", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanThrottle)), ("remote-id-limit", ("remote_id_limit", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdLimit)), ("mac-iwf-access-interface-throttle", ("mac_iwf_access_interface_throttle", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceThrottle)), ("access-interface-limit", ("access_interface_limit", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.AccessInterfaceLimit)), ("mac-access-interface-throttle", ("mac_access_interface_throttle", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceThrottle)), ("outer-vlan-limit", ("outer_vlan_limit", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanLimit)), ("circuit-id-throttle", ("circuit_id_throttle", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdThrottle)), ("mac-limit", ("mac_limit", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacLimit)), ("circuit-id-limit", ("circuit_id_limit", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdLimit)), ("mac-iwf-limit", ("mac_iwf_limit", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfLimit)), ("mac-iwf-access-interface-limit", ("mac_iwf_access_interface_limit", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceLimit)), ("inner-vlan-limit", ("inner_vlan_limit", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanLimit)), ("outer-vlan-throttle", ("outer_vlan_throttle", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanThrottle)), ("mac-throttle", ("mac_throttle", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacThrottle)), ("circuit-id-and-remote-id-limit", ("circuit_id_and_remote_id_limit", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdLimit)), ("vlan-limit", ("vlan_limit", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanLimit)), ("mac-access-interface-limit", ("mac_access_interface_limit", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceLimit)), ("remote-id-throttle", ("remote_id_throttle", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdThrottle)), ("max-limit", ("max_limit", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MaxLimit)), ("circuit-id-and-remote-id-throttle", ("circuit_id_and_remote_id_throttle", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdThrottle))])
                    self._leafs = OrderedDict()

                    self.vlan_throttle = None
                    self._children_name_map["vlan_throttle"] = "vlan-throttle"

                    self.inner_vlan_throttle = None
                    self._children_name_map["inner_vlan_throttle"] = "inner-vlan-throttle"

                    self.remote_id_limit = None
                    self._children_name_map["remote_id_limit"] = "remote-id-limit"

                    self.mac_iwf_access_interface_throttle = None
                    self._children_name_map["mac_iwf_access_interface_throttle"] = "mac-iwf-access-interface-throttle"

                    self.access_interface_limit = None
                    self._children_name_map["access_interface_limit"] = "access-interface-limit"

                    self.mac_access_interface_throttle = None
                    self._children_name_map["mac_access_interface_throttle"] = "mac-access-interface-throttle"

                    self.outer_vlan_limit = None
                    self._children_name_map["outer_vlan_limit"] = "outer-vlan-limit"

                    self.circuit_id_throttle = None
                    self._children_name_map["circuit_id_throttle"] = "circuit-id-throttle"

                    self.mac_limit = None
                    self._children_name_map["mac_limit"] = "mac-limit"

                    self.circuit_id_limit = None
                    self._children_name_map["circuit_id_limit"] = "circuit-id-limit"

                    self.mac_iwf_limit = None
                    self._children_name_map["mac_iwf_limit"] = "mac-iwf-limit"

                    self.mac_iwf_access_interface_limit = None
                    self._children_name_map["mac_iwf_access_interface_limit"] = "mac-iwf-access-interface-limit"

                    self.inner_vlan_limit = None
                    self._children_name_map["inner_vlan_limit"] = "inner-vlan-limit"

                    self.outer_vlan_throttle = None
                    self._children_name_map["outer_vlan_throttle"] = "outer-vlan-throttle"

                    self.mac_throttle = None
                    self._children_name_map["mac_throttle"] = "mac-throttle"

                    self.circuit_id_and_remote_id_limit = None
                    self._children_name_map["circuit_id_and_remote_id_limit"] = "circuit-id-and-remote-id-limit"

                    self.vlan_limit = None
                    self._children_name_map["vlan_limit"] = "vlan-limit"

                    self.mac_access_interface_limit = None
                    self._children_name_map["mac_access_interface_limit"] = "mac-access-interface-limit"

                    self.remote_id_throttle = None
                    self._children_name_map["remote_id_throttle"] = "remote-id-throttle"

                    self.max_limit = None
                    self._children_name_map["max_limit"] = "max-limit"

                    self.circuit_id_and_remote_id_throttle = None
                    self._children_name_map["circuit_id_and_remote_id_throttle"] = "circuit-id-and-remote-id-throttle"
                    self._segment_path = lambda: "sessions"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions, [], name, value)


                class VlanThrottle(Entity):
                    """
                    Set VLAN (inner + outer tags) session
                    throttle
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\: int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\: int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanThrottle, self).__init__()

                        self.yang_name = "vlan-throttle"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('throttle', (YLeaf(YType.uint32, 'throttle'), ['int'])),
                            ('request_period', (YLeaf(YType.uint32, 'request-period'), ['int'])),
                            ('blocking_period', (YLeaf(YType.uint32, 'blocking-period'), ['int'])),
                        ])
                        self.throttle = None
                        self.request_period = None
                        self.blocking_period = None
                        self._segment_path = lambda: "vlan-throttle"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanThrottle, ['throttle', 'request_period', 'blocking_period'], name, value)


                class InnerVlanThrottle(Entity):
                    """
                    Set Inner VLAN session throttle
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\: int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\: int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanThrottle, self).__init__()

                        self.yang_name = "inner-vlan-throttle"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('throttle', (YLeaf(YType.uint32, 'throttle'), ['int'])),
                            ('request_period', (YLeaf(YType.uint32, 'request-period'), ['int'])),
                            ('blocking_period', (YLeaf(YType.uint32, 'blocking-period'), ['int'])),
                        ])
                        self.throttle = None
                        self.request_period = None
                        self.blocking_period = None
                        self._segment_path = lambda: "inner-vlan-throttle"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanThrottle, ['throttle', 'request_period', 'blocking_period'], name, value)


                class RemoteIdLimit(Entity):
                    """
                    Set Remote ID session limit and threshold
                    
                    .. attribute:: limit
                    
                    	Per\-Remote ID limit
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-Remote ID threshold
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdLimit, self).__init__()

                        self.yang_name = "remote-id-limit"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                            ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                        ])
                        self.limit = None
                        self.threshold = None
                        self._segment_path = lambda: "remote-id-limit"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdLimit, ['limit', 'threshold'], name, value)


                class MacIwfAccessInterfaceThrottle(Entity):
                    """
                    Set per\-MAC/Access interface throttle for IWF
                    sessions
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\: int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\: int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceThrottle, self).__init__()

                        self.yang_name = "mac-iwf-access-interface-throttle"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('throttle', (YLeaf(YType.uint32, 'throttle'), ['int'])),
                            ('request_period', (YLeaf(YType.uint32, 'request-period'), ['int'])),
                            ('blocking_period', (YLeaf(YType.uint32, 'blocking-period'), ['int'])),
                        ])
                        self.throttle = None
                        self.request_period = None
                        self.blocking_period = None
                        self._segment_path = lambda: "mac-iwf-access-interface-throttle"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceThrottle, ['throttle', 'request_period', 'blocking_period'], name, value)


                class AccessInterfaceLimit(Entity):
                    """
                    Set per\-access interface limit
                    
                    .. attribute:: limit
                    
                    	Per\-access interface session limit
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-access interface session threshold
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.AccessInterfaceLimit, self).__init__()

                        self.yang_name = "access-interface-limit"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                            ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                        ])
                        self.limit = None
                        self.threshold = None
                        self._segment_path = lambda: "access-interface-limit"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.AccessInterfaceLimit, ['limit', 'threshold'], name, value)


                class MacAccessInterfaceThrottle(Entity):
                    """
                    Set per\-MAC/Access Interface throttle
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\: int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\: int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceThrottle, self).__init__()

                        self.yang_name = "mac-access-interface-throttle"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('throttle', (YLeaf(YType.uint32, 'throttle'), ['int'])),
                            ('request_period', (YLeaf(YType.uint32, 'request-period'), ['int'])),
                            ('blocking_period', (YLeaf(YType.uint32, 'blocking-period'), ['int'])),
                        ])
                        self.throttle = None
                        self.request_period = None
                        self.blocking_period = None
                        self._segment_path = lambda: "mac-access-interface-throttle"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceThrottle, ['throttle', 'request_period', 'blocking_period'], name, value)


                class OuterVlanLimit(Entity):
                    """
                    Set Outer VLAN session limit and threshold
                    
                    .. attribute:: limit
                    
                    	Per\-Outer VLAN limit
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-Outer VLAN threshold
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanLimit, self).__init__()

                        self.yang_name = "outer-vlan-limit"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                            ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                        ])
                        self.limit = None
                        self.threshold = None
                        self._segment_path = lambda: "outer-vlan-limit"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanLimit, ['limit', 'threshold'], name, value)


                class CircuitIdThrottle(Entity):
                    """
                    Set Circuit ID session throttle
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\: int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\: int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdThrottle, self).__init__()

                        self.yang_name = "circuit-id-throttle"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('throttle', (YLeaf(YType.uint32, 'throttle'), ['int'])),
                            ('request_period', (YLeaf(YType.uint32, 'request-period'), ['int'])),
                            ('blocking_period', (YLeaf(YType.uint32, 'blocking-period'), ['int'])),
                        ])
                        self.throttle = None
                        self.request_period = None
                        self.blocking_period = None
                        self._segment_path = lambda: "circuit-id-throttle"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdThrottle, ['throttle', 'request_period', 'blocking_period'], name, value)


                class MacLimit(Entity):
                    """
                    Set per\-MAC address session limit and
                    threshold
                    
                    .. attribute:: limit
                    
                    	Per\-MAC session limit
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-MAC session threshold
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacLimit, self).__init__()

                        self.yang_name = "mac-limit"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                            ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                        ])
                        self.limit = None
                        self.threshold = None
                        self._segment_path = lambda: "mac-limit"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacLimit, ['limit', 'threshold'], name, value)


                class CircuitIdLimit(Entity):
                    """
                    Set Circuit ID session limit and threshold
                    
                    .. attribute:: limit
                    
                    	Per\-Circuit ID limit
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-Circuit ID threshold
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdLimit, self).__init__()

                        self.yang_name = "circuit-id-limit"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                            ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                        ])
                        self.limit = None
                        self.threshold = None
                        self._segment_path = lambda: "circuit-id-limit"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdLimit, ['limit', 'threshold'], name, value)


                class MacIwfLimit(Entity):
                    """
                    Set per\-MAC session limit and threshold for
                    IWF sessions
                    
                    .. attribute:: limit
                    
                    	Per\-MAC session limit for IWF sessions
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-MAC session threshold for IWF sessions
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfLimit, self).__init__()

                        self.yang_name = "mac-iwf-limit"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                            ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                        ])
                        self.limit = None
                        self.threshold = None
                        self._segment_path = lambda: "mac-iwf-limit"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfLimit, ['limit', 'threshold'], name, value)


                class MacIwfAccessInterfaceLimit(Entity):
                    """
                    Set per\-MAC access interface session limit
                    and threshold for IWF sessions
                    
                    .. attribute:: limit
                    
                    	Per\-MAC access interface session limit for IWF sessions
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-MAC access interface session threshold for IWF sessions
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceLimit, self).__init__()

                        self.yang_name = "mac-iwf-access-interface-limit"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                            ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                        ])
                        self.limit = None
                        self.threshold = None
                        self._segment_path = lambda: "mac-iwf-access-interface-limit"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceLimit, ['limit', 'threshold'], name, value)


                class InnerVlanLimit(Entity):
                    """
                    Set Inner VLAN session limit and threshold
                    
                    .. attribute:: limit
                    
                    	Per\-Inner VLAN limit
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-Inner VLAN threshold
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanLimit, self).__init__()

                        self.yang_name = "inner-vlan-limit"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                            ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                        ])
                        self.limit = None
                        self.threshold = None
                        self._segment_path = lambda: "inner-vlan-limit"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanLimit, ['limit', 'threshold'], name, value)


                class OuterVlanThrottle(Entity):
                    """
                    Set Outer VLAN session throttle
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\: int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\: int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanThrottle, self).__init__()

                        self.yang_name = "outer-vlan-throttle"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('throttle', (YLeaf(YType.uint32, 'throttle'), ['int'])),
                            ('request_period', (YLeaf(YType.uint32, 'request-period'), ['int'])),
                            ('blocking_period', (YLeaf(YType.uint32, 'blocking-period'), ['int'])),
                        ])
                        self.throttle = None
                        self.request_period = None
                        self.blocking_period = None
                        self._segment_path = lambda: "outer-vlan-throttle"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanThrottle, ['throttle', 'request_period', 'blocking_period'], name, value)


                class MacThrottle(Entity):
                    """
                    Set per\-MAC throttle
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\: int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\: int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacThrottle, self).__init__()

                        self.yang_name = "mac-throttle"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('throttle', (YLeaf(YType.uint32, 'throttle'), ['int'])),
                            ('request_period', (YLeaf(YType.uint32, 'request-period'), ['int'])),
                            ('blocking_period', (YLeaf(YType.uint32, 'blocking-period'), ['int'])),
                        ])
                        self.throttle = None
                        self.request_period = None
                        self.blocking_period = None
                        self._segment_path = lambda: "mac-throttle"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacThrottle, ['throttle', 'request_period', 'blocking_period'], name, value)


                class CircuitIdAndRemoteIdLimit(Entity):
                    """
                    Set Circuit ID and Remote ID session
                    limit/threshold
                    
                    .. attribute:: limit
                    
                    	Per\-Circuit ID limit
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-Circuit ID threshold
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdLimit, self).__init__()

                        self.yang_name = "circuit-id-and-remote-id-limit"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                            ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                        ])
                        self.limit = None
                        self.threshold = None
                        self._segment_path = lambda: "circuit-id-and-remote-id-limit"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdLimit, ['limit', 'threshold'], name, value)


                class VlanLimit(Entity):
                    """
                    Set VLAN (inner + outer tags) session limit
                    and threshold
                    
                    .. attribute:: limit
                    
                    	Per\-VLAN (inner + outer tags) limit
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-VLAN (inner + outer tags) threshold
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanLimit, self).__init__()

                        self.yang_name = "vlan-limit"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                            ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                        ])
                        self.limit = None
                        self.threshold = None
                        self._segment_path = lambda: "vlan-limit"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanLimit, ['limit', 'threshold'], name, value)


                class MacAccessInterfaceLimit(Entity):
                    """
                    Set per\-MAC access interface session limit
                    and threshold
                    
                    .. attribute:: limit
                    
                    	Per\-MAC access interface session limit
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-MAC access interface session threshold
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceLimit, self).__init__()

                        self.yang_name = "mac-access-interface-limit"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                            ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                        ])
                        self.limit = None
                        self.threshold = None
                        self._segment_path = lambda: "mac-access-interface-limit"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceLimit, ['limit', 'threshold'], name, value)


                class RemoteIdThrottle(Entity):
                    """
                    Set Remote ID session throttle
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\: int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\: int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdThrottle, self).__init__()

                        self.yang_name = "remote-id-throttle"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('throttle', (YLeaf(YType.uint32, 'throttle'), ['int'])),
                            ('request_period', (YLeaf(YType.uint32, 'request-period'), ['int'])),
                            ('blocking_period', (YLeaf(YType.uint32, 'blocking-period'), ['int'])),
                        ])
                        self.throttle = None
                        self.request_period = None
                        self.blocking_period = None
                        self._segment_path = lambda: "remote-id-throttle"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdThrottle, ['throttle', 'request_period', 'blocking_period'], name, value)


                class MaxLimit(Entity):
                    """
                    Set per\-card session limit and threshold
                    
                    .. attribute:: limit
                    
                    	Per\-card session limit
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-card session threshold
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MaxLimit, self).__init__()

                        self.yang_name = "max-limit"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                            ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                        ])
                        self.limit = None
                        self.threshold = None
                        self._segment_path = lambda: "max-limit"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MaxLimit, ['limit', 'threshold'], name, value)


                class CircuitIdAndRemoteIdThrottle(Entity):
                    """
                    Set Circuit ID and Remote ID session throttle
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\: int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\: int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdThrottle, self).__init__()

                        self.yang_name = "circuit-id-and-remote-id-throttle"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('throttle', (YLeaf(YType.uint32, 'throttle'), ['int'])),
                            ('request_period', (YLeaf(YType.uint32, 'request-period'), ['int'])),
                            ('blocking_period', (YLeaf(YType.uint32, 'blocking-period'), ['int'])),
                        ])
                        self.throttle = None
                        self.request_period = None
                        self.blocking_period = None
                        self._segment_path = lambda: "circuit-id-and-remote-id-throttle"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdThrottle, ['throttle', 'request_period', 'blocking_period'], name, value)


            class ControlPackets(Entity):
                """
                PPPoE control\-packet configuration data
                
                .. attribute:: priority
                
                	Set the Priority to use for PPP and PPPoE control packets
                	**type**\: int
                
                	**range:** 0..7
                
                

                """

                _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                _revision = '2017-09-30'

                def __init__(self):
                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.ControlPackets, self).__init__()

                    self.yang_name = "control-packets"
                    self.yang_parent_name = "pppoe-bba-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                    ])
                    self.priority = None
                    self._segment_path = lambda: "control-packets"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.ControlPackets, ['priority'], name, value)


            class PaDoDelay(Entity):
                """
                PPPoE PADO delay configuration data
                
                .. attribute:: remote_id_substrings
                
                	Delay the PADO response when the received Remote ID contains the given string
                	**type**\:  :py:class:`RemoteIdSubstrings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings>`
                
                .. attribute:: remote_id_strings
                
                	Delay the PADO response when there is an exact match on the received Remote ID
                	**type**\:  :py:class:`RemoteIdStrings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings>`
                
                .. attribute:: service_name_strings
                
                	Delay the PADO response when there is an exact match on the received Service Name
                	**type**\:  :py:class:`ServiceNameStrings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings>`
                
                .. attribute:: circuit_id_substrings
                
                	Delay the PADO response when the received Circuit ID contains the given string
                	**type**\:  :py:class:`CircuitIdSubstrings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings>`
                
                .. attribute:: service_name_substrings
                
                	Delay the PADO response when the received Service Name contains the given string
                	**type**\:  :py:class:`ServiceNameSubstrings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings>`
                
                .. attribute:: circuit_id_strings
                
                	Delay the PADO response when there is an exact match on the received Circuit ID
                	**type**\:  :py:class:`CircuitIdStrings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings>`
                
                .. attribute:: default
                
                	PADO delay (in milliseconds)
                	**type**\: int
                
                	**range:** 0..10000
                
                	**mandatory**\: True
                
                	**units**\: millisecond
                
                .. attribute:: circuit_id
                
                	Configure PADO delay dependent on the received Circuit ID
                	**type**\: int
                
                	**range:** 0..10000
                
                	**units**\: millisecond
                
                .. attribute:: remote_id
                
                	Configure PADO delay dependent on the received Remote ID
                	**type**\: int
                
                	**range:** 0..10000
                
                	**units**\: millisecond
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                _revision = '2017-09-30'

                def __init__(self):
                    super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay, self).__init__()

                    self.yang_name = "pa-do-delay"
                    self.yang_parent_name = "pppoe-bba-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("remote-id-substrings", ("remote_id_substrings", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings)), ("remote-id-strings", ("remote_id_strings", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings)), ("service-name-strings", ("service_name_strings", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings)), ("circuit-id-substrings", ("circuit_id_substrings", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings)), ("service-name-substrings", ("service_name_substrings", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings)), ("circuit-id-strings", ("circuit_id_strings", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings))])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('default', (YLeaf(YType.uint32, 'default'), ['int'])),
                        ('circuit_id', (YLeaf(YType.uint32, 'circuit-id'), ['int'])),
                        ('remote_id', (YLeaf(YType.uint32, 'remote-id'), ['int'])),
                    ])
                    self.default = None
                    self.circuit_id = None
                    self.remote_id = None

                    self.remote_id_substrings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings()
                    self.remote_id_substrings.parent = self
                    self._children_name_map["remote_id_substrings"] = "remote-id-substrings"

                    self.remote_id_strings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings()
                    self.remote_id_strings.parent = self
                    self._children_name_map["remote_id_strings"] = "remote-id-strings"

                    self.service_name_strings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings()
                    self.service_name_strings.parent = self
                    self._children_name_map["service_name_strings"] = "service-name-strings"

                    self.circuit_id_substrings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings()
                    self.circuit_id_substrings.parent = self
                    self._children_name_map["circuit_id_substrings"] = "circuit-id-substrings"

                    self.service_name_substrings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings()
                    self.service_name_substrings.parent = self
                    self._children_name_map["service_name_substrings"] = "service-name-substrings"

                    self.circuit_id_strings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings()
                    self.circuit_id_strings.parent = self
                    self._children_name_map["circuit_id_strings"] = "circuit-id-strings"
                    self._segment_path = lambda: "pa-do-delay"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay, ['default', 'circuit_id', 'remote_id'], name, value)


                class RemoteIdSubstrings(Entity):
                    """
                    Delay the PADO response when the received
                    Remote ID contains the given string
                    
                    .. attribute:: remote_id_substring
                    
                    	Delay the PADO response when the received Remote ID contains the given string
                    	**type**\: list of  		 :py:class:`RemoteIdSubstring <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings.RemoteIdSubstring>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings, self).__init__()

                        self.yang_name = "remote-id-substrings"
                        self.yang_parent_name = "pa-do-delay"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("remote-id-substring", ("remote_id_substring", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings.RemoteIdSubstring))])
                        self._leafs = OrderedDict()

                        self.remote_id_substring = YList(self)
                        self._segment_path = lambda: "remote-id-substrings"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings, [], name, value)


                    class RemoteIdSubstring(Entity):
                        """
                        Delay the PADO response when the received
                        Remote ID contains the given string
                        
                        .. attribute:: name  (key)
                        
                        	The string to be contained within the received Remote ID
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: delay
                        
                        	PADO delay (in milliseconds)
                        	**type**\: int
                        
                        	**range:** 0..10000
                        
                        	**mandatory**\: True
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                        _revision = '2017-09-30'

                        def __init__(self):
                            super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings.RemoteIdSubstring, self).__init__()

                            self.yang_name = "remote-id-substring"
                            self.yang_parent_name = "remote-id-substrings"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ('delay', (YLeaf(YType.uint32, 'delay'), ['int'])),
                            ])
                            self.name = None
                            self.delay = None
                            self._segment_path = lambda: "remote-id-substring" + "[name='" + str(self.name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings.RemoteIdSubstring, ['name', 'delay'], name, value)


                class RemoteIdStrings(Entity):
                    """
                    Delay the PADO response when there is an
                    exact match on the received Remote ID
                    
                    .. attribute:: remote_id_string
                    
                    	Delay the PADO response when there is an exact match on the received Remote ID
                    	**type**\: list of  		 :py:class:`RemoteIdString <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings.RemoteIdString>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings, self).__init__()

                        self.yang_name = "remote-id-strings"
                        self.yang_parent_name = "pa-do-delay"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("remote-id-string", ("remote_id_string", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings.RemoteIdString))])
                        self._leafs = OrderedDict()

                        self.remote_id_string = YList(self)
                        self._segment_path = lambda: "remote-id-strings"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings, [], name, value)


                    class RemoteIdString(Entity):
                        """
                        Delay the PADO response when there is an
                        exact match on the received Remote ID
                        
                        .. attribute:: name  (key)
                        
                        	The string to exactly match the received Remote ID
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: delay
                        
                        	PADO delay (in milliseconds)
                        	**type**\: int
                        
                        	**range:** 0..10000
                        
                        	**mandatory**\: True
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                        _revision = '2017-09-30'

                        def __init__(self):
                            super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings.RemoteIdString, self).__init__()

                            self.yang_name = "remote-id-string"
                            self.yang_parent_name = "remote-id-strings"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ('delay', (YLeaf(YType.uint32, 'delay'), ['int'])),
                            ])
                            self.name = None
                            self.delay = None
                            self._segment_path = lambda: "remote-id-string" + "[name='" + str(self.name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings.RemoteIdString, ['name', 'delay'], name, value)


                class ServiceNameStrings(Entity):
                    """
                    Delay the PADO response when there is an
                    exact match on the received Service Name
                    
                    .. attribute:: service_name_string
                    
                    	Delay the PADO response when there is an exact match on the received Service Name
                    	**type**\: list of  		 :py:class:`ServiceNameString <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings.ServiceNameString>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings, self).__init__()

                        self.yang_name = "service-name-strings"
                        self.yang_parent_name = "pa-do-delay"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("service-name-string", ("service_name_string", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings.ServiceNameString))])
                        self._leafs = OrderedDict()

                        self.service_name_string = YList(self)
                        self._segment_path = lambda: "service-name-strings"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings, [], name, value)


                    class ServiceNameString(Entity):
                        """
                        Delay the PADO response when there is an
                        exact match on the received Service Name
                        
                        .. attribute:: name  (key)
                        
                        	The string to exactly match the received Service Name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: delay
                        
                        	PADO delay (in milliseconds)
                        	**type**\: int
                        
                        	**range:** 0..10000
                        
                        	**mandatory**\: True
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                        _revision = '2017-09-30'

                        def __init__(self):
                            super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings.ServiceNameString, self).__init__()

                            self.yang_name = "service-name-string"
                            self.yang_parent_name = "service-name-strings"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ('delay', (YLeaf(YType.uint32, 'delay'), ['int'])),
                            ])
                            self.name = None
                            self.delay = None
                            self._segment_path = lambda: "service-name-string" + "[name='" + str(self.name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings.ServiceNameString, ['name', 'delay'], name, value)


                class CircuitIdSubstrings(Entity):
                    """
                    Delay the PADO response when the received
                    Circuit ID contains the given string
                    
                    .. attribute:: circuit_id_substring
                    
                    	Delay the PADO response when the received Circuit ID contains the given string
                    	**type**\: list of  		 :py:class:`CircuitIdSubstring <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings.CircuitIdSubstring>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings, self).__init__()

                        self.yang_name = "circuit-id-substrings"
                        self.yang_parent_name = "pa-do-delay"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("circuit-id-substring", ("circuit_id_substring", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings.CircuitIdSubstring))])
                        self._leafs = OrderedDict()

                        self.circuit_id_substring = YList(self)
                        self._segment_path = lambda: "circuit-id-substrings"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings, [], name, value)


                    class CircuitIdSubstring(Entity):
                        """
                        Delay the PADO response when the received
                        Circuit ID contains the given string
                        
                        .. attribute:: name  (key)
                        
                        	The string to be contained within the received Circuit ID
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: delay
                        
                        	PADO delay (in milliseconds)
                        	**type**\: int
                        
                        	**range:** 0..10000
                        
                        	**mandatory**\: True
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                        _revision = '2017-09-30'

                        def __init__(self):
                            super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings.CircuitIdSubstring, self).__init__()

                            self.yang_name = "circuit-id-substring"
                            self.yang_parent_name = "circuit-id-substrings"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ('delay', (YLeaf(YType.uint32, 'delay'), ['int'])),
                            ])
                            self.name = None
                            self.delay = None
                            self._segment_path = lambda: "circuit-id-substring" + "[name='" + str(self.name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings.CircuitIdSubstring, ['name', 'delay'], name, value)


                class ServiceNameSubstrings(Entity):
                    """
                    Delay the PADO response when the received
                    Service Name contains the given string
                    
                    .. attribute:: service_name_substring
                    
                    	Delay the PADO response when the received Service Name contains the given string
                    	**type**\: list of  		 :py:class:`ServiceNameSubstring <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings.ServiceNameSubstring>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings, self).__init__()

                        self.yang_name = "service-name-substrings"
                        self.yang_parent_name = "pa-do-delay"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("service-name-substring", ("service_name_substring", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings.ServiceNameSubstring))])
                        self._leafs = OrderedDict()

                        self.service_name_substring = YList(self)
                        self._segment_path = lambda: "service-name-substrings"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings, [], name, value)


                    class ServiceNameSubstring(Entity):
                        """
                        Delay the PADO response when the received
                        Service Name contains the given string
                        
                        .. attribute:: name  (key)
                        
                        	The string to be contained within the received Service Name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: delay
                        
                        	PADO delay (in milliseconds)
                        	**type**\: int
                        
                        	**range:** 0..10000
                        
                        	**mandatory**\: True
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                        _revision = '2017-09-30'

                        def __init__(self):
                            super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings.ServiceNameSubstring, self).__init__()

                            self.yang_name = "service-name-substring"
                            self.yang_parent_name = "service-name-substrings"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ('delay', (YLeaf(YType.uint32, 'delay'), ['int'])),
                            ])
                            self.name = None
                            self.delay = None
                            self._segment_path = lambda: "service-name-substring" + "[name='" + str(self.name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings.ServiceNameSubstring, ['name', 'delay'], name, value)


                class CircuitIdStrings(Entity):
                    """
                    Delay the PADO response when there is an
                    exact match on the received Circuit ID
                    
                    .. attribute:: circuit_id_string
                    
                    	Delay the PADO response when there is an exact match on the received Circuit ID
                    	**type**\: list of  		 :py:class:`CircuitIdString <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings.CircuitIdString>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings, self).__init__()

                        self.yang_name = "circuit-id-strings"
                        self.yang_parent_name = "pa-do-delay"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("circuit-id-string", ("circuit_id_string", PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings.CircuitIdString))])
                        self._leafs = OrderedDict()

                        self.circuit_id_string = YList(self)
                        self._segment_path = lambda: "circuit-id-strings"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings, [], name, value)


                    class CircuitIdString(Entity):
                        """
                        Delay the PADO response when there is an
                        exact match on the received Circuit ID
                        
                        .. attribute:: name  (key)
                        
                        	The string to exactly match the received Circuit ID
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: delay
                        
                        	PADO delay (in milliseconds)
                        	**type**\: int
                        
                        	**range:** 0..10000
                        
                        	**mandatory**\: True
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                        _revision = '2017-09-30'

                        def __init__(self):
                            super(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings.CircuitIdString, self).__init__()

                            self.yang_name = "circuit-id-string"
                            self.yang_parent_name = "circuit-id-strings"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ('delay', (YLeaf(YType.uint32, 'delay'), ['int'])),
                            ])
                            self.name = None
                            self.delay = None
                            self._segment_path = lambda: "circuit-id-string" + "[name='" + str(self.name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings.CircuitIdString, ['name', 'delay'], name, value)

    def clone_ptr(self):
        self._top_entity = PppoeCfg()
        return self._top_entity


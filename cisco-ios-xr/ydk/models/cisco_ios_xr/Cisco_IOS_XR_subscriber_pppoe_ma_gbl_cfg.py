""" Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-pppoe\-ma\-gbl package configuration.

This module contains definitions
for the following management objects\:
  pppoe\-cfg\: PPPOE configuration data

This YANG module augments the
  Cisco\-IOS\-XR\-subscriber\-infra\-tmplmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class PppoeInvalidSessionIdBehaviorEnum(Enum):
    """
    PppoeInvalidSessionIdBehaviorEnum

    Pppoe invalid session id behavior

    .. data:: drop = 0

    	Drop packets with an invalid session ID

    .. data:: log = 1

    	Log packets with an invalid session ID

    """

    drop = 0

    log = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
        return meta._meta_table['PppoeInvalidSessionIdBehaviorEnum']



class PppoeCfg(object):
    """
    PPPOE configuration data
    
    .. attribute:: in_flight_window
    
    	Set the PPPoE in\-flight window size
    	**type**\:  int
    
    	**range:** 1..20000
    
    .. attribute:: pppoe_bba_groups
    
    	PPPoE BBA\-Group configuration data
    	**type**\:   :py:class:`PppoeBbaGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups>`
    
    .. attribute:: session_id_space_flat
    
    	Disable per\-parent session ID spaces
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.in_flight_window = None
        self.pppoe_bba_groups = PppoeCfg.PppoeBbaGroups()
        self.pppoe_bba_groups.parent = self
        self.session_id_space_flat = None


    class PppoeBbaGroups(object):
        """
        PPPoE BBA\-Group configuration data
        
        .. attribute:: pppoe_bba_group
        
        	PPPoE BBA\-Group configuration data
        	**type**\: list of    :py:class:`PppoeBbaGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup>`
        
        

        """

        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.pppoe_bba_group = YList()
            self.pppoe_bba_group.parent = self
            self.pppoe_bba_group.name = 'pppoe_bba_group'


        class PppoeBbaGroup(object):
            """
            PPPoE BBA\-Group configuration data
            
            .. attribute:: bba_group  <key>
            
            	BBA\-Group name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: completion_timeout
            
            	PPPoE session completion timeout
            	**type**\:  int
            
            	**range:** 30..600
            
            .. attribute:: control_packets
            
            	PPPoE control\-packet configuration data
            	**type**\:   :py:class:`ControlPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.ControlPackets>`
            
            .. attribute:: enable_padt_after_shut_down
            
            	Enable padt after shutdown
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: invalid_session_id
            
            	Invalid session\-ID behavior
            	**type**\:   :py:class:`PppoeInvalidSessionIdBehaviorEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeInvalidSessionIdBehaviorEnum>`
            
            .. attribute:: mtu
            
            	PPPoE default MTU
            	**type**\:  int
            
            	**range:** 500..2000
            
            .. attribute:: pa_do_delay
            
            	PPPoE PADO delay configuration data
            	**type**\:   :py:class:`PaDoDelay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay>`
            
            .. attribute:: sessions
            
            	PPPoE session configuration data
            	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions>`
            
            .. attribute:: tag
            
            	PPPoE tag configuration data
            	**type**\:   :py:class:`Tag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag>`
            
            

            """

            _prefix = 'subscriber-pppoe-ma-gbl-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.bba_group = None
                self.completion_timeout = None
                self.control_packets = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.ControlPackets()
                self.control_packets.parent = self
                self.enable_padt_after_shut_down = None
                self.invalid_session_id = None
                self.mtu = None
                self.pa_do_delay = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay()
                self.pa_do_delay.parent = self
                self.sessions = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions()
                self.sessions.parent = self
                self.tag = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag()
                self.tag.parent = self


            class Tag(object):
                """
                PPPoE tag configuration data
                
                .. attribute:: ac_name
                
                	The name to include in the AC tag
                	**type**\:  str
                
                .. attribute:: padr
                
                	PADR packets
                	**type**\:   :py:class:`Padr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.Padr>`
                
                .. attribute:: ppp_max_payload
                
                	Minimum and maximum payloads
                	**type**\:   :py:class:`PppMaxPayload <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.PppMaxPayload>`
                
                .. attribute:: ppp_max_payload_deny
                
                	Ignore the ppp\-max\-payload tag
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: service_name_configureds
                
                	Service name
                	**type**\:   :py:class:`ServiceNameConfigureds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds>`
                
                .. attribute:: service_selection_disable
                
                	Disable advertising of unrequested service names
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ac_name = None
                    self.padr = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.Padr()
                    self.padr.parent = self
                    self.ppp_max_payload = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.PppMaxPayload()
                    self.ppp_max_payload.parent = self
                    self.ppp_max_payload_deny = None
                    self.service_name_configureds = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds()
                    self.service_name_configureds.parent = self
                    self.service_selection_disable = None


                class Padr(object):
                    """
                    PADR packets
                    
                    .. attribute:: invalid_payload_allow
                    
                    	Allow sessions to come up with invalid\-payload
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: session_unique_relay_session_id
                    
                    	Allow sessions to come up with unique relay\-session\-id in padr
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.invalid_payload_allow = None
                        self.session_unique_relay_session_id = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:padr'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.invalid_payload_allow is not None:
                            return True

                        if self.session_unique_relay_session_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.Padr']['meta_info']


                class ServiceNameConfigureds(object):
                    """
                    Service name
                    
                    .. attribute:: service_name_configured
                    
                    	Service name supported on this group
                    	**type**\: list of    :py:class:`ServiceNameConfigured <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds.ServiceNameConfigured>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.service_name_configured = YList()
                        self.service_name_configured.parent = self
                        self.service_name_configured.name = 'service_name_configured'


                    class ServiceNameConfigured(object):
                        """
                        Service name supported on this group
                        
                        .. attribute:: name  <key>
                        
                        	Service name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
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

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:service-name-configured[Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:name = ' + str(self.name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                            return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds.ServiceNameConfigured']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:service-name-configureds'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.service_name_configured is not None:
                            for child_ref in self.service_name_configured:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.ServiceNameConfigureds']['meta_info']


                class PppMaxPayload(object):
                    """
                    Minimum and maximum payloads
                    
                    .. attribute:: max
                    
                    	Maximum payload
                    	**type**\:  int
                    
                    	**range:** 500..2000
                    
                    .. attribute:: min
                    
                    	Minimum payload
                    	**type**\:  int
                    
                    	**range:** 500..2000
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.max = None
                        self.min = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:ppp-max-payload'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.max is not None:
                            return True

                        if self.min is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag.PppMaxPayload']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:tag'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ac_name is not None:
                        return True

                    if self.padr is not None and self.padr._has_data():
                        return True

                    if self.ppp_max_payload is not None and self.ppp_max_payload._has_data():
                        return True

                    if self.ppp_max_payload_deny is not None:
                        return True

                    if self.service_name_configureds is not None and self.service_name_configureds._has_data():
                        return True

                    if self.service_selection_disable is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                    return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Tag']['meta_info']


            class Sessions(object):
                """
                PPPoE session configuration data
                
                .. attribute:: access_interface_limit
                
                	Set per\-access interface limit
                	**type**\:   :py:class:`AccessInterfaceLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.AccessInterfaceLimit>`
                
                	**presence node**\: True
                
                .. attribute:: circuit_id_and_remote_id_limit
                
                	Set Circuit ID and Remote ID session limit/threshold
                	**type**\:   :py:class:`CircuitIdAndRemoteIdLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdLimit>`
                
                	**presence node**\: True
                
                .. attribute:: circuit_id_and_remote_id_throttle
                
                	Set Circuit ID and Remote ID session throttle
                	**type**\:   :py:class:`CircuitIdAndRemoteIdThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: circuit_id_limit
                
                	Set Circuit ID session limit and threshold
                	**type**\:   :py:class:`CircuitIdLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdLimit>`
                
                	**presence node**\: True
                
                .. attribute:: circuit_id_throttle
                
                	Set Circuit ID session throttle
                	**type**\:   :py:class:`CircuitIdThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: inner_vlan_limit
                
                	Set Inner VLAN session limit and threshold
                	**type**\:   :py:class:`InnerVlanLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanLimit>`
                
                	**presence node**\: True
                
                .. attribute:: inner_vlan_throttle
                
                	Set Inner VLAN session throttle
                	**type**\:   :py:class:`InnerVlanThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: mac_access_interface_limit
                
                	Set per\-MAC access interface session limit and threshold
                	**type**\:   :py:class:`MacAccessInterfaceLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceLimit>`
                
                	**presence node**\: True
                
                .. attribute:: mac_access_interface_throttle
                
                	Set per\-MAC/Access Interface throttle
                	**type**\:   :py:class:`MacAccessInterfaceThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: mac_iwf_access_interface_limit
                
                	Set per\-MAC access interface session limit and threshold for IWF sessions
                	**type**\:   :py:class:`MacIwfAccessInterfaceLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceLimit>`
                
                	**presence node**\: True
                
                .. attribute:: mac_iwf_access_interface_throttle
                
                	Set per\-MAC/Access interface throttle for IWF sessions
                	**type**\:   :py:class:`MacIwfAccessInterfaceThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: mac_iwf_limit
                
                	Set per\-MAC session limit and threshold for IWF sessions
                	**type**\:   :py:class:`MacIwfLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfLimit>`
                
                	**presence node**\: True
                
                .. attribute:: mac_limit
                
                	Set per\-MAC address session limit and threshold
                	**type**\:   :py:class:`MacLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacLimit>`
                
                	**presence node**\: True
                
                .. attribute:: mac_throttle
                
                	Set per\-MAC throttle
                	**type**\:   :py:class:`MacThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: max_limit
                
                	Set per\-card session limit and threshold
                	**type**\:   :py:class:`MaxLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MaxLimit>`
                
                	**presence node**\: True
                
                .. attribute:: outer_vlan_limit
                
                	Set Outer VLAN session limit and threshold
                	**type**\:   :py:class:`OuterVlanLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanLimit>`
                
                	**presence node**\: True
                
                .. attribute:: outer_vlan_throttle
                
                	Set Outer VLAN session throttle
                	**type**\:   :py:class:`OuterVlanThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: remote_id_limit
                
                	Set Remote ID session limit and threshold
                	**type**\:   :py:class:`RemoteIdLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdLimit>`
                
                	**presence node**\: True
                
                .. attribute:: remote_id_throttle
                
                	Set Remote ID session throttle
                	**type**\:   :py:class:`RemoteIdThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdThrottle>`
                
                	**presence node**\: True
                
                .. attribute:: vlan_limit
                
                	Set VLAN (inner + outer tags) session limit and threshold
                	**type**\:   :py:class:`VlanLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanLimit>`
                
                	**presence node**\: True
                
                .. attribute:: vlan_throttle
                
                	Set VLAN (inner + outer tags) session throttle
                	**type**\:   :py:class:`VlanThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanThrottle>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.access_interface_limit = None
                    self.circuit_id_and_remote_id_limit = None
                    self.circuit_id_and_remote_id_throttle = None
                    self.circuit_id_limit = None
                    self.circuit_id_throttle = None
                    self.inner_vlan_limit = None
                    self.inner_vlan_throttle = None
                    self.mac_access_interface_limit = None
                    self.mac_access_interface_throttle = None
                    self.mac_iwf_access_interface_limit = None
                    self.mac_iwf_access_interface_throttle = None
                    self.mac_iwf_limit = None
                    self.mac_limit = None
                    self.mac_throttle = None
                    self.max_limit = None
                    self.outer_vlan_limit = None
                    self.outer_vlan_throttle = None
                    self.remote_id_limit = None
                    self.remote_id_throttle = None
                    self.vlan_limit = None
                    self.vlan_throttle = None


                class VlanThrottle(object):
                    """
                    Set VLAN (inner + outer tags) session
                    throttle
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.blocking_period = None
                        self.request_period = None
                        self.throttle = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:vlan-throttle'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.blocking_period is not None:
                            return True

                        if self.request_period is not None:
                            return True

                        if self.throttle is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanThrottle']['meta_info']


                class InnerVlanThrottle(object):
                    """
                    Set Inner VLAN session throttle
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.blocking_period = None
                        self.request_period = None
                        self.throttle = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:inner-vlan-throttle'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.blocking_period is not None:
                            return True

                        if self.request_period is not None:
                            return True

                        if self.throttle is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanThrottle']['meta_info']


                class RemoteIdLimit(object):
                    """
                    Set Remote ID session limit and threshold
                    
                    .. attribute:: limit
                    
                    	Per\-Remote ID limit
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-Remote ID threshold
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.limit = None
                        self.threshold = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:remote-id-limit'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.limit is not None:
                            return True

                        if self.threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdLimit']['meta_info']


                class MacIwfAccessInterfaceThrottle(object):
                    """
                    Set per\-MAC/Access interface throttle for IWF
                    sessions
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.blocking_period = None
                        self.request_period = None
                        self.throttle = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:mac-iwf-access-interface-throttle'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.blocking_period is not None:
                            return True

                        if self.request_period is not None:
                            return True

                        if self.throttle is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceThrottle']['meta_info']


                class AccessInterfaceLimit(object):
                    """
                    Set per\-access interface limit
                    
                    .. attribute:: limit
                    
                    	Per\-access interface session limit
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-access interface session threshold
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.limit = None
                        self.threshold = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:access-interface-limit'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.limit is not None:
                            return True

                        if self.threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.AccessInterfaceLimit']['meta_info']


                class MacAccessInterfaceThrottle(object):
                    """
                    Set per\-MAC/Access Interface throttle
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.blocking_period = None
                        self.request_period = None
                        self.throttle = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:mac-access-interface-throttle'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.blocking_period is not None:
                            return True

                        if self.request_period is not None:
                            return True

                        if self.throttle is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceThrottle']['meta_info']


                class OuterVlanLimit(object):
                    """
                    Set Outer VLAN session limit and threshold
                    
                    .. attribute:: limit
                    
                    	Per\-Outer VLAN limit
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-Outer VLAN threshold
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.limit = None
                        self.threshold = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:outer-vlan-limit'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.limit is not None:
                            return True

                        if self.threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanLimit']['meta_info']


                class CircuitIdThrottle(object):
                    """
                    Set Circuit ID session throttle
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.blocking_period = None
                        self.request_period = None
                        self.throttle = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:circuit-id-throttle'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.blocking_period is not None:
                            return True

                        if self.request_period is not None:
                            return True

                        if self.throttle is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdThrottle']['meta_info']


                class MacLimit(object):
                    """
                    Set per\-MAC address session limit and
                    threshold
                    
                    .. attribute:: limit
                    
                    	Per\-MAC session limit
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-MAC session threshold
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.limit = None
                        self.threshold = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:mac-limit'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.limit is not None:
                            return True

                        if self.threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacLimit']['meta_info']


                class CircuitIdLimit(object):
                    """
                    Set Circuit ID session limit and threshold
                    
                    .. attribute:: limit
                    
                    	Per\-Circuit ID limit
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-Circuit ID threshold
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.limit = None
                        self.threshold = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:circuit-id-limit'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.limit is not None:
                            return True

                        if self.threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdLimit']['meta_info']


                class MacIwfLimit(object):
                    """
                    Set per\-MAC session limit and threshold for
                    IWF sessions
                    
                    .. attribute:: limit
                    
                    	Per\-MAC session limit for IWF sessions
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-MAC session threshold for IWF sessions
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.limit = None
                        self.threshold = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:mac-iwf-limit'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.limit is not None:
                            return True

                        if self.threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfLimit']['meta_info']


                class MacIwfAccessInterfaceLimit(object):
                    """
                    Set per\-MAC access interface session limit
                    and threshold for IWF sessions
                    
                    .. attribute:: limit
                    
                    	Per\-MAC access interface session limit for IWF sessions
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-MAC access interface session threshold for IWF sessions
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.limit = None
                        self.threshold = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:mac-iwf-access-interface-limit'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.limit is not None:
                            return True

                        if self.threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacIwfAccessInterfaceLimit']['meta_info']


                class InnerVlanLimit(object):
                    """
                    Set Inner VLAN session limit and threshold
                    
                    .. attribute:: limit
                    
                    	Per\-Inner VLAN limit
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-Inner VLAN threshold
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.limit = None
                        self.threshold = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:inner-vlan-limit'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.limit is not None:
                            return True

                        if self.threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.InnerVlanLimit']['meta_info']


                class OuterVlanThrottle(object):
                    """
                    Set Outer VLAN session throttle
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.blocking_period = None
                        self.request_period = None
                        self.throttle = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:outer-vlan-throttle'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.blocking_period is not None:
                            return True

                        if self.request_period is not None:
                            return True

                        if self.throttle is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.OuterVlanThrottle']['meta_info']


                class MacThrottle(object):
                    """
                    Set per\-MAC throttle
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.blocking_period = None
                        self.request_period = None
                        self.throttle = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:mac-throttle'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.blocking_period is not None:
                            return True

                        if self.request_period is not None:
                            return True

                        if self.throttle is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacThrottle']['meta_info']


                class CircuitIdAndRemoteIdLimit(object):
                    """
                    Set Circuit ID and Remote ID session
                    limit/threshold
                    
                    .. attribute:: limit
                    
                    	Per\-Circuit ID limit
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-Circuit ID threshold
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.limit = None
                        self.threshold = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:circuit-id-and-remote-id-limit'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.limit is not None:
                            return True

                        if self.threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdLimit']['meta_info']


                class VlanLimit(object):
                    """
                    Set VLAN (inner + outer tags) session limit
                    and threshold
                    
                    .. attribute:: limit
                    
                    	Per\-VLAN (inner + outer tags) limit
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-VLAN (inner + outer tags) threshold
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.limit = None
                        self.threshold = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:vlan-limit'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.limit is not None:
                            return True

                        if self.threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.VlanLimit']['meta_info']


                class MacAccessInterfaceLimit(object):
                    """
                    Set per\-MAC access interface session limit
                    and threshold
                    
                    .. attribute:: limit
                    
                    	Per\-MAC access interface session limit
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-MAC access interface session threshold
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.limit = None
                        self.threshold = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:mac-access-interface-limit'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.limit is not None:
                            return True

                        if self.threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MacAccessInterfaceLimit']['meta_info']


                class RemoteIdThrottle(object):
                    """
                    Set Remote ID session throttle
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.blocking_period = None
                        self.request_period = None
                        self.throttle = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:remote-id-throttle'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.blocking_period is not None:
                            return True

                        if self.request_period is not None:
                            return True

                        if self.throttle is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.RemoteIdThrottle']['meta_info']


                class MaxLimit(object):
                    """
                    Set per\-card session limit and threshold
                    
                    .. attribute:: limit
                    
                    	Per\-card session limit
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold
                    
                    	Per\-card session threshold
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.limit = None
                        self.threshold = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:max-limit'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.limit is not None:
                            return True

                        if self.threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.MaxLimit']['meta_info']


                class CircuitIdAndRemoteIdThrottle(object):
                    """
                    Set Circuit ID and Remote ID session throttle
                    
                    .. attribute:: blocking_period
                    
                    	Throttle blocking period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: request_period
                    
                    	Throttle request period
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**mandatory**\: True
                    
                    .. attribute:: throttle
                    
                    	Number of requests at which to throttle
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.blocking_period = None
                        self.request_period = None
                        self.throttle = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:circuit-id-and-remote-id-throttle'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.blocking_period is not None:
                            return True

                        if self.request_period is not None:
                            return True

                        if self.throttle is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions.CircuitIdAndRemoteIdThrottle']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:sessions'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.access_interface_limit is not None and self.access_interface_limit._has_data():
                        return True

                    if self.circuit_id_and_remote_id_limit is not None and self.circuit_id_and_remote_id_limit._has_data():
                        return True

                    if self.circuit_id_and_remote_id_throttle is not None and self.circuit_id_and_remote_id_throttle._has_data():
                        return True

                    if self.circuit_id_limit is not None and self.circuit_id_limit._has_data():
                        return True

                    if self.circuit_id_throttle is not None and self.circuit_id_throttle._has_data():
                        return True

                    if self.inner_vlan_limit is not None and self.inner_vlan_limit._has_data():
                        return True

                    if self.inner_vlan_throttle is not None and self.inner_vlan_throttle._has_data():
                        return True

                    if self.mac_access_interface_limit is not None and self.mac_access_interface_limit._has_data():
                        return True

                    if self.mac_access_interface_throttle is not None and self.mac_access_interface_throttle._has_data():
                        return True

                    if self.mac_iwf_access_interface_limit is not None and self.mac_iwf_access_interface_limit._has_data():
                        return True

                    if self.mac_iwf_access_interface_throttle is not None and self.mac_iwf_access_interface_throttle._has_data():
                        return True

                    if self.mac_iwf_limit is not None and self.mac_iwf_limit._has_data():
                        return True

                    if self.mac_limit is not None and self.mac_limit._has_data():
                        return True

                    if self.mac_throttle is not None and self.mac_throttle._has_data():
                        return True

                    if self.max_limit is not None and self.max_limit._has_data():
                        return True

                    if self.outer_vlan_limit is not None and self.outer_vlan_limit._has_data():
                        return True

                    if self.outer_vlan_throttle is not None and self.outer_vlan_throttle._has_data():
                        return True

                    if self.remote_id_limit is not None and self.remote_id_limit._has_data():
                        return True

                    if self.remote_id_throttle is not None and self.remote_id_throttle._has_data():
                        return True

                    if self.vlan_limit is not None and self.vlan_limit._has_data():
                        return True

                    if self.vlan_throttle is not None and self.vlan_throttle._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                    return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.Sessions']['meta_info']


            class ControlPackets(object):
                """
                PPPoE control\-packet configuration data
                
                .. attribute:: priority
                
                	Set the Priority to use for PPP and PPPoE control packets
                	**type**\:  int
                
                	**range:** 0..7
                
                

                """

                _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.priority = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:control-packets'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.priority is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                    return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.ControlPackets']['meta_info']


            class PaDoDelay(object):
                """
                PPPoE PADO delay configuration data
                
                .. attribute:: circuit_id
                
                	Configure PADO delay dependent on the received Circuit ID
                	**type**\:  int
                
                	**range:** 0..10000
                
                	**units**\: millisecond
                
                .. attribute:: circuit_id_strings
                
                	Delay the PADO response when there is an exact match on the received Circuit ID
                	**type**\:   :py:class:`CircuitIdStrings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings>`
                
                .. attribute:: circuit_id_substrings
                
                	Delay the PADO response when the received Circuit ID contains the given string
                	**type**\:   :py:class:`CircuitIdSubstrings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings>`
                
                .. attribute:: default
                
                	PADO delay (in milliseconds)
                	**type**\:  int
                
                	**range:** 0..10000
                
                	**units**\: millisecond
                
                .. attribute:: remote_id
                
                	Configure PADO delay dependent on the received Remote ID
                	**type**\:  int
                
                	**range:** 0..10000
                
                	**units**\: millisecond
                
                .. attribute:: remote_id_strings
                
                	Delay the PADO response when there is an exact match on the received Remote ID
                	**type**\:   :py:class:`RemoteIdStrings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings>`
                
                .. attribute:: remote_id_substrings
                
                	Delay the PADO response when the received Remote ID contains the given string
                	**type**\:   :py:class:`RemoteIdSubstrings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings>`
                
                .. attribute:: service_name_strings
                
                	Delay the PADO response when there is an exact match on the received Service Name
                	**type**\:   :py:class:`ServiceNameStrings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings>`
                
                .. attribute:: service_name_substrings
                
                	Delay the PADO response when the received Service Name contains the given string
                	**type**\:   :py:class:`ServiceNameSubstrings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings>`
                
                

                """

                _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.circuit_id = None
                    self.circuit_id_strings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings()
                    self.circuit_id_strings.parent = self
                    self.circuit_id_substrings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings()
                    self.circuit_id_substrings.parent = self
                    self.default = None
                    self.remote_id = None
                    self.remote_id_strings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings()
                    self.remote_id_strings.parent = self
                    self.remote_id_substrings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings()
                    self.remote_id_substrings.parent = self
                    self.service_name_strings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings()
                    self.service_name_strings.parent = self
                    self.service_name_substrings = PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings()
                    self.service_name_substrings.parent = self


                class RemoteIdSubstrings(object):
                    """
                    Delay the PADO response when the received
                    Remote ID contains the given string
                    
                    .. attribute:: remote_id_substring
                    
                    	Delay the PADO response when the received Remote ID contains the given string
                    	**type**\: list of    :py:class:`RemoteIdSubstring <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings.RemoteIdSubstring>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.remote_id_substring = YList()
                        self.remote_id_substring.parent = self
                        self.remote_id_substring.name = 'remote_id_substring'


                    class RemoteIdSubstring(object):
                        """
                        Delay the PADO response when the received
                        Remote ID contains the given string
                        
                        .. attribute:: name  <key>
                        
                        	The string to be contained within the received Remote ID
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: delay
                        
                        	PADO delay (in milliseconds)
                        	**type**\:  int
                        
                        	**range:** 0..10000
                        
                        	**mandatory**\: True
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.name = None
                            self.delay = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.name is None:
                                raise YPYModelError('Key property name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:remote-id-substring[Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:name = ' + str(self.name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.name is not None:
                                return True

                            if self.delay is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                            return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings.RemoteIdSubstring']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:remote-id-substrings'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.remote_id_substring is not None:
                            for child_ref in self.remote_id_substring:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdSubstrings']['meta_info']


                class RemoteIdStrings(object):
                    """
                    Delay the PADO response when there is an
                    exact match on the received Remote ID
                    
                    .. attribute:: remote_id_string
                    
                    	Delay the PADO response when there is an exact match on the received Remote ID
                    	**type**\: list of    :py:class:`RemoteIdString <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings.RemoteIdString>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.remote_id_string = YList()
                        self.remote_id_string.parent = self
                        self.remote_id_string.name = 'remote_id_string'


                    class RemoteIdString(object):
                        """
                        Delay the PADO response when there is an
                        exact match on the received Remote ID
                        
                        .. attribute:: name  <key>
                        
                        	The string to exactly match the received Remote ID
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: delay
                        
                        	PADO delay (in milliseconds)
                        	**type**\:  int
                        
                        	**range:** 0..10000
                        
                        	**mandatory**\: True
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.name = None
                            self.delay = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.name is None:
                                raise YPYModelError('Key property name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:remote-id-string[Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:name = ' + str(self.name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.name is not None:
                                return True

                            if self.delay is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                            return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings.RemoteIdString']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:remote-id-strings'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.remote_id_string is not None:
                            for child_ref in self.remote_id_string:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.RemoteIdStrings']['meta_info']


                class ServiceNameStrings(object):
                    """
                    Delay the PADO response when there is an
                    exact match on the received Service Name
                    
                    .. attribute:: service_name_string
                    
                    	Delay the PADO response when there is an exact match on the received Service Name
                    	**type**\: list of    :py:class:`ServiceNameString <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings.ServiceNameString>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.service_name_string = YList()
                        self.service_name_string.parent = self
                        self.service_name_string.name = 'service_name_string'


                    class ServiceNameString(object):
                        """
                        Delay the PADO response when there is an
                        exact match on the received Service Name
                        
                        .. attribute:: name  <key>
                        
                        	The string to exactly match the received Service Name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: delay
                        
                        	PADO delay (in milliseconds)
                        	**type**\:  int
                        
                        	**range:** 0..10000
                        
                        	**mandatory**\: True
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.name = None
                            self.delay = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.name is None:
                                raise YPYModelError('Key property name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:service-name-string[Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:name = ' + str(self.name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.name is not None:
                                return True

                            if self.delay is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                            return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings.ServiceNameString']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:service-name-strings'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.service_name_string is not None:
                            for child_ref in self.service_name_string:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameStrings']['meta_info']


                class CircuitIdSubstrings(object):
                    """
                    Delay the PADO response when the received
                    Circuit ID contains the given string
                    
                    .. attribute:: circuit_id_substring
                    
                    	Delay the PADO response when the received Circuit ID contains the given string
                    	**type**\: list of    :py:class:`CircuitIdSubstring <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings.CircuitIdSubstring>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.circuit_id_substring = YList()
                        self.circuit_id_substring.parent = self
                        self.circuit_id_substring.name = 'circuit_id_substring'


                    class CircuitIdSubstring(object):
                        """
                        Delay the PADO response when the received
                        Circuit ID contains the given string
                        
                        .. attribute:: name  <key>
                        
                        	The string to be contained within the received Circuit ID
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: delay
                        
                        	PADO delay (in milliseconds)
                        	**type**\:  int
                        
                        	**range:** 0..10000
                        
                        	**mandatory**\: True
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.name = None
                            self.delay = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.name is None:
                                raise YPYModelError('Key property name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:circuit-id-substring[Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:name = ' + str(self.name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.name is not None:
                                return True

                            if self.delay is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                            return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings.CircuitIdSubstring']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:circuit-id-substrings'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.circuit_id_substring is not None:
                            for child_ref in self.circuit_id_substring:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdSubstrings']['meta_info']


                class ServiceNameSubstrings(object):
                    """
                    Delay the PADO response when the received
                    Service Name contains the given string
                    
                    .. attribute:: service_name_substring
                    
                    	Delay the PADO response when the received Service Name contains the given string
                    	**type**\: list of    :py:class:`ServiceNameSubstring <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings.ServiceNameSubstring>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.service_name_substring = YList()
                        self.service_name_substring.parent = self
                        self.service_name_substring.name = 'service_name_substring'


                    class ServiceNameSubstring(object):
                        """
                        Delay the PADO response when the received
                        Service Name contains the given string
                        
                        .. attribute:: name  <key>
                        
                        	The string to be contained within the received Service Name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: delay
                        
                        	PADO delay (in milliseconds)
                        	**type**\:  int
                        
                        	**range:** 0..10000
                        
                        	**mandatory**\: True
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.name = None
                            self.delay = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.name is None:
                                raise YPYModelError('Key property name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:service-name-substring[Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:name = ' + str(self.name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.name is not None:
                                return True

                            if self.delay is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                            return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings.ServiceNameSubstring']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:service-name-substrings'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.service_name_substring is not None:
                            for child_ref in self.service_name_substring:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.ServiceNameSubstrings']['meta_info']


                class CircuitIdStrings(object):
                    """
                    Delay the PADO response when there is an
                    exact match on the received Circuit ID
                    
                    .. attribute:: circuit_id_string
                    
                    	Delay the PADO response when there is an exact match on the received Circuit ID
                    	**type**\: list of    :py:class:`CircuitIdString <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg.PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings.CircuitIdString>`
                    
                    

                    """

                    _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.circuit_id_string = YList()
                        self.circuit_id_string.parent = self
                        self.circuit_id_string.name = 'circuit_id_string'


                    class CircuitIdString(object):
                        """
                        Delay the PADO response when there is an
                        exact match on the received Circuit ID
                        
                        .. attribute:: name  <key>
                        
                        	The string to exactly match the received Circuit ID
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: delay
                        
                        	PADO delay (in milliseconds)
                        	**type**\:  int
                        
                        	**range:** 0..10000
                        
                        	**mandatory**\: True
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'subscriber-pppoe-ma-gbl-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.name = None
                            self.delay = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.name is None:
                                raise YPYModelError('Key property name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:circuit-id-string[Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:name = ' + str(self.name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.name is not None:
                                return True

                            if self.delay is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                            return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings.CircuitIdString']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:circuit-id-strings'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.circuit_id_string is not None:
                            for child_ref in self.circuit_id_string:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                        return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay.CircuitIdStrings']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:pa-do-delay'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.circuit_id is not None:
                        return True

                    if self.circuit_id_strings is not None and self.circuit_id_strings._has_data():
                        return True

                    if self.circuit_id_substrings is not None and self.circuit_id_substrings._has_data():
                        return True

                    if self.default is not None:
                        return True

                    if self.remote_id is not None:
                        return True

                    if self.remote_id_strings is not None and self.remote_id_strings._has_data():
                        return True

                    if self.remote_id_substrings is not None and self.remote_id_substrings._has_data():
                        return True

                    if self.service_name_strings is not None and self.service_name_strings._has_data():
                        return True

                    if self.service_name_substrings is not None and self.service_name_substrings._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                    return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup.PaDoDelay']['meta_info']

            @property
            def _common_path(self):
                if self.bba_group is None:
                    raise YPYModelError('Key property bba_group is None')

                return '/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:pppoe-cfg/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:pppoe-bba-groups/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:pppoe-bba-group[Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:bba-group = ' + str(self.bba_group) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.bba_group is not None:
                    return True

                if self.completion_timeout is not None:
                    return True

                if self.control_packets is not None and self.control_packets._has_data():
                    return True

                if self.enable_padt_after_shut_down is not None:
                    return True

                if self.invalid_session_id is not None:
                    return True

                if self.mtu is not None:
                    return True

                if self.pa_do_delay is not None and self.pa_do_delay._has_data():
                    return True

                if self.sessions is not None and self.sessions._has_data():
                    return True

                if self.tag is not None and self.tag._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
                return meta._meta_table['PppoeCfg.PppoeBbaGroups.PppoeBbaGroup']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:pppoe-cfg/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:pppoe-bba-groups'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.pppoe_bba_group is not None:
                for child_ref in self.pppoe_bba_group:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
            return meta._meta_table['PppoeCfg.PppoeBbaGroups']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-subscriber-pppoe-ma-gbl-cfg:pppoe-cfg'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.in_flight_window is not None:
            return True

        if self.pppoe_bba_groups is not None and self.pppoe_bba_groups._has_data():
            return True

        if self.session_id_space_flat is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_pppoe_ma_gbl_cfg as meta
        return meta._meta_table['PppoeCfg']['meta_info']



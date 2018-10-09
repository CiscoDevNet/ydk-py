""" Cisco_IOS_XE_virtual_service_cfg 

This module contains a collection of YANG definitions
for virtual service configurational data.
Copyright (c) 2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class VirtualServiceCfgData(Entity):
    """
    Virtual Service configurational data
    
    .. attribute:: apps
    
    	Application list
    	**type**\:  :py:class:`Apps <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_cfg.VirtualServiceCfgData.Apps>`
    
    .. attribute:: controls
    
    	App\-hosting control
    	**type**\:  :py:class:`Controls <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_cfg.VirtualServiceCfgData.Controls>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'virtual-service-ios-xe-cfg'
    _revision = '2018-01-01'

    def __init__(self):
        super(VirtualServiceCfgData, self).__init__()
        self._top_entity = None

        self.yang_name = "virtual-service-cfg-data"
        self.yang_parent_name = "Cisco-IOS-XE-virtual-service-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("apps", ("apps", VirtualServiceCfgData.Apps)), ("controls", ("controls", VirtualServiceCfgData.Controls))])
        self._leafs = OrderedDict()

        self.apps = VirtualServiceCfgData.Apps()
        self.apps.parent = self
        self._children_name_map["apps"] = "apps"

        self.controls = None
        self._children_name_map["controls"] = "controls"
        self._segment_path = lambda: "Cisco-IOS-XE-virtual-service-cfg:virtual-service-cfg-data"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(VirtualServiceCfgData, [], name, value)


    class Apps(Entity):
        """
        Application list
        
        .. attribute:: app
        
        	Application info
        	**type**\: list of  		 :py:class:`App <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_cfg.VirtualServiceCfgData.Apps.App>`
        
        

        """

        _prefix = 'virtual-service-ios-xe-cfg'
        _revision = '2018-01-01'

        def __init__(self):
            super(VirtualServiceCfgData.Apps, self).__init__()

            self.yang_name = "apps"
            self.yang_parent_name = "virtual-service-cfg-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("app", ("app", VirtualServiceCfgData.Apps.App))])
            self._leafs = OrderedDict()

            self.app = YList(self)
            self._segment_path = lambda: "apps"
            self._absolute_path = lambda: "Cisco-IOS-XE-virtual-service-cfg:virtual-service-cfg-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(VirtualServiceCfgData.Apps, [], name, value)


        class App(Entity):
            """
            Application info
            
            .. attribute:: application_name  (key)
            
            	Application name
            	**type**\: str
            
            	**pattern:** [0\-9a\-zA\-Z]\*
            
            .. attribute:: application_network_resource
            
            	Application Network Resource Information
            	**type**\:  :py:class:`ApplicationNetworkResource <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_cfg.VirtualServiceCfgData.Apps.App.ApplicationNetworkResource>`
            
            .. attribute:: application_resource_profile
            
            	Application Resource profile
            	**type**\:  :py:class:`ApplicationResourceProfile <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_cfg.VirtualServiceCfgData.Apps.App.ApplicationResourceProfile>`
            
            .. attribute:: application_attached_device
            
            	Application attached device
            	**type**\:  :py:class:`ApplicationAttachedDevice <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_cfg.VirtualServiceCfgData.Apps.App.ApplicationAttachedDevice>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-cfg'
            _revision = '2018-01-01'

            def __init__(self):
                super(VirtualServiceCfgData.Apps.App, self).__init__()

                self.yang_name = "app"
                self.yang_parent_name = "apps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['application_name']
                self._child_classes = OrderedDict([("application-network-resource", ("application_network_resource", VirtualServiceCfgData.Apps.App.ApplicationNetworkResource)), ("application-resource-profile", ("application_resource_profile", VirtualServiceCfgData.Apps.App.ApplicationResourceProfile)), ("application-attached-device", ("application_attached_device", VirtualServiceCfgData.Apps.App.ApplicationAttachedDevice))])
                self._leafs = OrderedDict([
                    ('application_name', (YLeaf(YType.str, 'application-name'), ['str'])),
                ])
                self.application_name = None

                self.application_network_resource = VirtualServiceCfgData.Apps.App.ApplicationNetworkResource()
                self.application_network_resource.parent = self
                self._children_name_map["application_network_resource"] = "application-network-resource"

                self.application_resource_profile = VirtualServiceCfgData.Apps.App.ApplicationResourceProfile()
                self.application_resource_profile.parent = self
                self._children_name_map["application_resource_profile"] = "application-resource-profile"

                self.application_attached_device = VirtualServiceCfgData.Apps.App.ApplicationAttachedDevice()
                self.application_attached_device.parent = self
                self._children_name_map["application_attached_device"] = "application-attached-device"
                self._segment_path = lambda: "app" + "[application-name='" + str(self.application_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-virtual-service-cfg:virtual-service-cfg-data/apps/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(VirtualServiceCfgData.Apps.App, ['application_name'], name, value)


            class ApplicationNetworkResource(Entity):
                """
                Application Network Resource Information
                
                .. attribute:: vnic_gateway_0
                
                	Vnic gateway
                	**type**\: str
                
                	**pattern:** [0\-9]\*
                
                .. attribute:: virtualportgroup_guest_interface_name_1
                
                	VirtualPortGroup guest interface name as number in range of 0 .. 3
                	**type**\: str
                
                	**pattern:** [0\-3]\*
                
                .. attribute:: virtualportgroup_guest_ip_address_1
                
                	Guest interface IP address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: virtualportgroup_guest_ip_netmask_1
                
                	Guest IP netmask
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: virtualportgroup_application_default_gateway_1
                
                	VirtualPortGroup application default gateway IP address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: nameserver_0
                
                	Name server IP address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: virtualportgroup_guest_interface_default_gateway_1
                
                	VirtualPortGroup default gateway guest interface
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: vnic_gateway_1
                
                	Vnic gateway
                	**type**\: str
                
                	**pattern:** [0\-9]\*
                
                .. attribute:: virtualportgroup_guest_interface_name_2
                
                	VirtualPortGroup guest interface name as number in range of 0 .. 3
                	**type**\: str
                
                	**pattern:** [0\-3]\*
                
                .. attribute:: virtualportgroup_guest_ip_address_2
                
                	Guest interface IP address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: virtualportgroup_guest_ip_netmask_2
                
                	Guest IP netmask
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: virtualportgroup_application_gateway_2
                
                	VirtualPortGroup application qateway IP address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: nameserver_1
                
                	Name server IP address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: virtualportgroup_guest_interface_default_gateway_2
                
                	VirtualPortGroup default gateway guest interface
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: vnic_gateway_2
                
                	Vnic gateway
                	**type**\: str
                
                	**pattern:** [0\-9]\*
                
                .. attribute:: virtualportgroup_guest_interface_name_3
                
                	VirtualPortGroup guest interface name as number in range of 0 .. 3
                	**type**\: str
                
                	**pattern:** [0\-3]\*
                
                .. attribute:: virtualportgroup_guest_ip_address_3
                
                	Guest interface IP address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: virtualportgroup_guest_ip_netmask_3
                
                	Guest IP netmask
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: virtualportgroup_application_gateway_3
                
                	VirtualPortGroup application gateway IP address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: nameserver2
                
                	Name server IP address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: virtualportgroup_guest_interface_default_gateway_3
                
                	VirtualPortGroup default gateway guest interface
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: vnic_gateway_3
                
                	Vnic gateway
                	**type**\: str
                
                	**pattern:** [0\-9]\*
                
                .. attribute:: virtualportgroup_guest_interface_name_4
                
                	VirtualPortGroup guest interface name as number in range of 0 .. 3
                	**type**\: str
                
                	**pattern:** [0\-3]\*
                
                .. attribute:: virtualportgroup_guest_ip_address_4
                
                	Guest interface IP address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: virtualportgroup_guest_ip_netmask_4
                
                	Guest IP netmask
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: virtualportgroup_application_gateway_4
                
                	VirtualPortGroup application gateway IP address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: nameserver_3
                
                	Name server IP address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: virtualportgroup_guest_interface_default_gateway_4
                
                	VirtualPortGroup default gateway guest interface
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: management_interface_name
                
                	Management port guest interface name as number in range of 0 .. 3
                	**type**\: str
                
                	**pattern:** [0\-3]\*
                
                .. attribute:: management_guest_ip_address
                
                	Guest management port interface IP address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: management_guest_ip_netmask
                
                	Guest management port interface IP netmask
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: management_application_gateway
                
                	Management port application gateway IP address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: nameseerver4
                
                	Name server IP address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: management_guest_interface_default_gateway
                
                	Management port default gateway guest interface
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: application_mac_address
                
                	Application MAC address
                	**type**\:  :py:class:`ApplicationMacAddress <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_cfg.VirtualServiceCfgData.Apps.App.ApplicationNetworkResource.ApplicationMacAddress>`
                
                

                """

                _prefix = 'virtual-service-ios-xe-cfg'
                _revision = '2018-01-01'

                def __init__(self):
                    super(VirtualServiceCfgData.Apps.App.ApplicationNetworkResource, self).__init__()

                    self.yang_name = "application-network-resource"
                    self.yang_parent_name = "app"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("application-mac-address", ("application_mac_address", VirtualServiceCfgData.Apps.App.ApplicationNetworkResource.ApplicationMacAddress))])
                    self._leafs = OrderedDict([
                        ('vnic_gateway_0', (YLeaf(YType.str, 'vnic-gateway-0'), ['str'])),
                        ('virtualportgroup_guest_interface_name_1', (YLeaf(YType.str, 'virtualportgroup-guest-interface-name-1'), ['str'])),
                        ('virtualportgroup_guest_ip_address_1', (YLeaf(YType.str, 'virtualportgroup-guest-ip-address-1'), ['str','str'])),
                        ('virtualportgroup_guest_ip_netmask_1', (YLeaf(YType.str, 'virtualportgroup-guest-ip-netmask-1'), ['str','str'])),
                        ('virtualportgroup_application_default_gateway_1', (YLeaf(YType.str, 'virtualportgroup-application-default-gateway-1'), ['str','str'])),
                        ('nameserver_0', (YLeaf(YType.str, 'nameserver-0'), ['str','str'])),
                        ('virtualportgroup_guest_interface_default_gateway_1', (YLeaf(YType.uint8, 'virtualportgroup-guest-interface-default-gateway-1'), ['int'])),
                        ('vnic_gateway_1', (YLeaf(YType.str, 'vnic-gateway-1'), ['str'])),
                        ('virtualportgroup_guest_interface_name_2', (YLeaf(YType.str, 'virtualportgroup-guest-interface-name-2'), ['str'])),
                        ('virtualportgroup_guest_ip_address_2', (YLeaf(YType.str, 'virtualportgroup-guest-ip-address-2'), ['str','str'])),
                        ('virtualportgroup_guest_ip_netmask_2', (YLeaf(YType.str, 'virtualportgroup-guest-ip-netmask-2'), ['str','str'])),
                        ('virtualportgroup_application_gateway_2', (YLeaf(YType.str, 'virtualportgroup-application-gateway-2'), ['str','str'])),
                        ('nameserver_1', (YLeaf(YType.str, 'nameserver-1'), ['str','str'])),
                        ('virtualportgroup_guest_interface_default_gateway_2', (YLeaf(YType.uint8, 'virtualportgroup-guest-interface-default-gateway-2'), ['int'])),
                        ('vnic_gateway_2', (YLeaf(YType.str, 'vnic-gateway-2'), ['str'])),
                        ('virtualportgroup_guest_interface_name_3', (YLeaf(YType.str, 'virtualportgroup-guest-interface-name-3'), ['str'])),
                        ('virtualportgroup_guest_ip_address_3', (YLeaf(YType.str, 'virtualportgroup-guest-ip-address-3'), ['str','str'])),
                        ('virtualportgroup_guest_ip_netmask_3', (YLeaf(YType.str, 'virtualportgroup-guest-ip-netmask-3'), ['str','str'])),
                        ('virtualportgroup_application_gateway_3', (YLeaf(YType.str, 'virtualportgroup-application-gateway-3'), ['str','str'])),
                        ('nameserver2', (YLeaf(YType.str, 'nameserver2'), ['str','str'])),
                        ('virtualportgroup_guest_interface_default_gateway_3', (YLeaf(YType.uint8, 'virtualportgroup-guest-interface-default-gateway-3'), ['int'])),
                        ('vnic_gateway_3', (YLeaf(YType.str, 'vnic-gateway-3'), ['str'])),
                        ('virtualportgroup_guest_interface_name_4', (YLeaf(YType.str, 'virtualportgroup-guest-interface-name-4'), ['str'])),
                        ('virtualportgroup_guest_ip_address_4', (YLeaf(YType.str, 'virtualportgroup-guest-ip-address-4'), ['str','str'])),
                        ('virtualportgroup_guest_ip_netmask_4', (YLeaf(YType.str, 'virtualportgroup-guest-ip-netmask-4'), ['str','str'])),
                        ('virtualportgroup_application_gateway_4', (YLeaf(YType.str, 'virtualportgroup-application-gateway-4'), ['str','str'])),
                        ('nameserver_3', (YLeaf(YType.str, 'nameserver-3'), ['str','str'])),
                        ('virtualportgroup_guest_interface_default_gateway_4', (YLeaf(YType.uint8, 'virtualportgroup-guest-interface-default-gateway-4'), ['int'])),
                        ('management_interface_name', (YLeaf(YType.str, 'management-interface-name'), ['str'])),
                        ('management_guest_ip_address', (YLeaf(YType.str, 'management-guest-ip-address'), ['str','str'])),
                        ('management_guest_ip_netmask', (YLeaf(YType.str, 'management-guest-ip-netmask'), ['str','str'])),
                        ('management_application_gateway', (YLeaf(YType.str, 'management-application-gateway'), ['str','str'])),
                        ('nameseerver4', (YLeaf(YType.str, 'nameseerver4'), ['str','str'])),
                        ('management_guest_interface_default_gateway', (YLeaf(YType.uint8, 'management-guest-interface-default-gateway'), ['int'])),
                    ])
                    self.vnic_gateway_0 = None
                    self.virtualportgroup_guest_interface_name_1 = None
                    self.virtualportgroup_guest_ip_address_1 = None
                    self.virtualportgroup_guest_ip_netmask_1 = None
                    self.virtualportgroup_application_default_gateway_1 = None
                    self.nameserver_0 = None
                    self.virtualportgroup_guest_interface_default_gateway_1 = None
                    self.vnic_gateway_1 = None
                    self.virtualportgroup_guest_interface_name_2 = None
                    self.virtualportgroup_guest_ip_address_2 = None
                    self.virtualportgroup_guest_ip_netmask_2 = None
                    self.virtualportgroup_application_gateway_2 = None
                    self.nameserver_1 = None
                    self.virtualportgroup_guest_interface_default_gateway_2 = None
                    self.vnic_gateway_2 = None
                    self.virtualportgroup_guest_interface_name_3 = None
                    self.virtualportgroup_guest_ip_address_3 = None
                    self.virtualportgroup_guest_ip_netmask_3 = None
                    self.virtualportgroup_application_gateway_3 = None
                    self.nameserver2 = None
                    self.virtualportgroup_guest_interface_default_gateway_3 = None
                    self.vnic_gateway_3 = None
                    self.virtualportgroup_guest_interface_name_4 = None
                    self.virtualportgroup_guest_ip_address_4 = None
                    self.virtualportgroup_guest_ip_netmask_4 = None
                    self.virtualportgroup_application_gateway_4 = None
                    self.nameserver_3 = None
                    self.virtualportgroup_guest_interface_default_gateway_4 = None
                    self.management_interface_name = None
                    self.management_guest_ip_address = None
                    self.management_guest_ip_netmask = None
                    self.management_application_gateway = None
                    self.nameseerver4 = None
                    self.management_guest_interface_default_gateway = None

                    self.application_mac_address = VirtualServiceCfgData.Apps.App.ApplicationNetworkResource.ApplicationMacAddress()
                    self.application_mac_address.parent = self
                    self._children_name_map["application_mac_address"] = "application-mac-address"
                    self._segment_path = lambda: "application-network-resource"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualServiceCfgData.Apps.App.ApplicationNetworkResource, ['vnic_gateway_0', 'virtualportgroup_guest_interface_name_1', 'virtualportgroup_guest_ip_address_1', 'virtualportgroup_guest_ip_netmask_1', 'virtualportgroup_application_default_gateway_1', 'nameserver_0', 'virtualportgroup_guest_interface_default_gateway_1', 'vnic_gateway_1', 'virtualportgroup_guest_interface_name_2', 'virtualportgroup_guest_ip_address_2', 'virtualportgroup_guest_ip_netmask_2', 'virtualportgroup_application_gateway_2', 'nameserver_1', 'virtualportgroup_guest_interface_default_gateway_2', 'vnic_gateway_2', 'virtualportgroup_guest_interface_name_3', 'virtualportgroup_guest_ip_address_3', 'virtualportgroup_guest_ip_netmask_3', 'virtualportgroup_application_gateway_3', 'nameserver2', 'virtualportgroup_guest_interface_default_gateway_3', 'vnic_gateway_3', 'virtualportgroup_guest_interface_name_4', 'virtualportgroup_guest_ip_address_4', 'virtualportgroup_guest_ip_netmask_4', 'virtualportgroup_application_gateway_4', 'nameserver_3', 'virtualportgroup_guest_interface_default_gateway_4', 'management_interface_name', 'management_guest_ip_address', 'management_guest_ip_netmask', 'management_application_gateway', 'nameseerver4', 'management_guest_interface_default_gateway'], name, value)


                class ApplicationMacAddress(Entity):
                    """
                    Application MAC address
                    
                    .. attribute:: mac_address
                    
                    	MAC address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: mac_interface_name
                    
                    	MAC interface name
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-zA\-Z]\*
                    
                    

                    """

                    _prefix = 'virtual-service-ios-xe-cfg'
                    _revision = '2018-01-01'

                    def __init__(self):
                        super(VirtualServiceCfgData.Apps.App.ApplicationNetworkResource.ApplicationMacAddress, self).__init__()

                        self.yang_name = "application-mac-address"
                        self.yang_parent_name = "application-network-resource"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                            ('mac_interface_name', (YLeaf(YType.str, 'mac-interface-name'), ['str'])),
                        ])
                        self.mac_address = None
                        self.mac_interface_name = None
                        self._segment_path = lambda: "application-mac-address"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(VirtualServiceCfgData.Apps.App.ApplicationNetworkResource.ApplicationMacAddress, ['mac_address', 'mac_interface_name'], name, value)


            class ApplicationResourceProfile(Entity):
                """
                Application Resource profile
                
                .. attribute:: profile_name
                
                	Resource profile name
                	**type**\: str
                
                	**pattern:** [0\-9a\-zA\-Z]\*
                
                .. attribute:: vcpu
                
                	Amount of VCPUs allocated for the application
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: cpu_units
                
                	Amount of reserved cpu in unit
                	**type**\: int
                
                	**range:** 0..20000
                
                	**default value**\: 0
                
                .. attribute:: memory_capacity_mb
                
                	Amount of reserved memory in MB
                	**type**\: int
                
                	**range:** 0..4096
                
                	**default value**\: 0
                
                .. attribute:: disk_size_mb
                
                	Disk size in MB
                	**type**\: int
                
                	**range:** 0..8192
                
                	**default value**\: 0
                
                .. attribute:: pkg_profile_name
                
                	Resource package profile name
                	**type**\: str
                
                	**pattern:** [0\-9a\-zA\-Z]\*
                
                

                """

                _prefix = 'virtual-service-ios-xe-cfg'
                _revision = '2018-01-01'

                def __init__(self):
                    super(VirtualServiceCfgData.Apps.App.ApplicationResourceProfile, self).__init__()

                    self.yang_name = "application-resource-profile"
                    self.yang_parent_name = "app"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                        ('vcpu', (YLeaf(YType.uint16, 'vcpu'), ['int'])),
                        ('cpu_units', (YLeaf(YType.uint16, 'cpu-units'), ['int'])),
                        ('memory_capacity_mb', (YLeaf(YType.uint16, 'memory-capacity-mb'), ['int'])),
                        ('disk_size_mb', (YLeaf(YType.uint16, 'disk-size-mb'), ['int'])),
                        ('pkg_profile_name', (YLeaf(YType.str, 'pkg-profile-name'), ['str'])),
                    ])
                    self.profile_name = None
                    self.vcpu = None
                    self.cpu_units = None
                    self.memory_capacity_mb = None
                    self.disk_size_mb = None
                    self.pkg_profile_name = None
                    self._segment_path = lambda: "application-resource-profile"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualServiceCfgData.Apps.App.ApplicationResourceProfile, ['profile_name', 'vcpu', 'cpu_units', 'memory_capacity_mb', 'disk_size_mb', 'pkg_profile_name'], name, value)


            class ApplicationAttachedDevice(Entity):
                """
                Application attached device
                
                .. attribute:: device_name
                
                	device name
                	**type**\: str
                
                	**pattern:** [0\-9a\-zA\-Z]\*
                
                

                """

                _prefix = 'virtual-service-ios-xe-cfg'
                _revision = '2018-01-01'

                def __init__(self):
                    super(VirtualServiceCfgData.Apps.App.ApplicationAttachedDevice, self).__init__()

                    self.yang_name = "application-attached-device"
                    self.yang_parent_name = "app"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('device_name', (YLeaf(YType.str, 'device-name'), ['str'])),
                    ])
                    self.device_name = None
                    self._segment_path = lambda: "application-attached-device"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualServiceCfgData.Apps.App.ApplicationAttachedDevice, ['device_name'], name, value)


    class Controls(Entity):
        """
        App\-hosting control
        
        .. attribute:: application_hosting_infra_enable_statue
        
        	Application hosting Infra enable status
        	**type**\: int
        
        	**range:** 0..255
        
        	**default value**\: 0
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'virtual-service-ios-xe-cfg'
        _revision = '2018-01-01'

        def __init__(self):
            super(VirtualServiceCfgData.Controls, self).__init__()

            self.yang_name = "controls"
            self.yang_parent_name = "virtual-service-cfg-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('application_hosting_infra_enable_statue', (YLeaf(YType.uint8, 'application-hosting-infra-enable-statue'), ['int'])),
            ])
            self.application_hosting_infra_enable_statue = None
            self._segment_path = lambda: "controls"
            self._absolute_path = lambda: "Cisco-IOS-XE-virtual-service-cfg:virtual-service-cfg-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(VirtualServiceCfgData.Controls, ['application_hosting_infra_enable_statue'], name, value)

    def clone_ptr(self):
        self._top_entity = VirtualServiceCfgData()
        return self._top_entity


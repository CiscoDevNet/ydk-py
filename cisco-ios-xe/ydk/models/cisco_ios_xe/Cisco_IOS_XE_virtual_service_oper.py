""" Cisco_IOS_XE_virtual_service_oper 

This module contains a collection of YANG definitions for monitoring
virtual services in a Network Element.Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class VirtualServices(Entity):
    """
    Names and Status of virtual services on the device
    
    .. attribute:: virtual_service
    
    	A virtual service
    	**type**\: list of    :py:class:`VirtualService <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService>`
    
    

    """

    _prefix = 'virtual-service-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(VirtualServices, self).__init__()
        self._top_entity = None

        self.yang_name = "virtual-services"
        self.yang_parent_name = "Cisco-IOS-XE-virtual-service-oper"

        self.virtual_service = YList(self)

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in () and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(VirtualServices, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(VirtualServices, self).__setattr__(name, value)


    class VirtualService(Entity):
        """
        A virtual service.
        
        .. attribute:: name  <key>
        
        	The name of the virtual service
        	**type**\:  str
        
        .. attribute:: attached_devices
        
        	Details for the devices attached to this virtual service
        	**type**\:   :py:class:`AttachedDevices <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.AttachedDevices>`
        
        .. attribute:: details
        
        	Details of the virtual service
        	**type**\:   :py:class:`Details <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details>`
        
        .. attribute:: guest_routes
        
        	Routes for the guest interface
        	**type**\:   :py:class:`GuestRoutes <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.GuestRoutes>`
        
        .. attribute:: network_interfaces
        
        	Details for the network interfaces
        	**type**\:   :py:class:`NetworkInterfaces <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.NetworkInterfaces>`
        
        .. attribute:: network_utils
        
        	list of the network utilizations for the virtual\-service
        	**type**\:   :py:class:`NetworkUtils <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.NetworkUtils>`
        
        .. attribute:: storage_utils
        
        	List of the storage utilizations for the virtual\-service
        	**type**\:   :py:class:`StorageUtils <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.StorageUtils>`
        
        .. attribute:: utilization
        
        	Utilization of device resources for a virtual\-service
        	**type**\:   :py:class:`Utilization <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Utilization>`
        
        

        """

        _prefix = 'virtual-service-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(VirtualServices.VirtualService, self).__init__()

            self.yang_name = "virtual-service"
            self.yang_parent_name = "virtual-services"

            self.name = YLeaf(YType.str, "name")

            self.attached_devices = VirtualServices.VirtualService.AttachedDevices()
            self.attached_devices.parent = self
            self._children_name_map["attached_devices"] = "attached-devices"
            self._children_yang_names.add("attached-devices")

            self.details = VirtualServices.VirtualService.Details()
            self.details.parent = self
            self._children_name_map["details"] = "details"
            self._children_yang_names.add("details")

            self.guest_routes = VirtualServices.VirtualService.GuestRoutes()
            self.guest_routes.parent = self
            self._children_name_map["guest_routes"] = "guest-routes"
            self._children_yang_names.add("guest-routes")

            self.network_interfaces = VirtualServices.VirtualService.NetworkInterfaces()
            self.network_interfaces.parent = self
            self._children_name_map["network_interfaces"] = "network-interfaces"
            self._children_yang_names.add("network-interfaces")

            self.network_utils = VirtualServices.VirtualService.NetworkUtils()
            self.network_utils.parent = self
            self._children_name_map["network_utils"] = "network-utils"
            self._children_yang_names.add("network-utils")

            self.storage_utils = VirtualServices.VirtualService.StorageUtils()
            self.storage_utils.parent = self
            self._children_name_map["storage_utils"] = "storage-utils"
            self._children_yang_names.add("storage-utils")

            self.utilization = VirtualServices.VirtualService.Utilization()
            self.utilization.parent = self
            self._children_name_map["utilization"] = "utilization"
            self._children_yang_names.add("utilization")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("name") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(VirtualServices.VirtualService, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(VirtualServices.VirtualService, self).__setattr__(name, value)


        class Details(Entity):
            """
            Details of the virtual service.
            
            .. attribute:: activated_profile_name
            
            	The activated profile name
            	**type**\:  str
            
            .. attribute:: detailed_guest_status
            
            	Details on the guest status
            	**type**\:   :py:class:`DetailedGuestStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.DetailedGuestStatus>`
            
            .. attribute:: guest_interface
            
            	The name of a guest interface
            	**type**\:  str
            
            .. attribute:: package_information
            
            	Details of the package for the virtual\-service
            	**type**\:   :py:class:`PackageInformation <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.PackageInformation>`
            
            .. attribute:: resource_admission
            
            	Resources being allocated for the virtual\-service
            	**type**\:   :py:class:`ResourceAdmission <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.ResourceAdmission>`
            
            .. attribute:: resource_reservation
            
            	Details of the resources reserved for this virtual service
            	**type**\:   :py:class:`ResourceReservation <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.ResourceReservation>`
            
            .. attribute:: state
            
            	State of the virtual service
            	**type**\:  str
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(VirtualServices.VirtualService.Details, self).__init__()

                self.yang_name = "details"
                self.yang_parent_name = "virtual-service"

                self.activated_profile_name = YLeaf(YType.str, "activated-profile-name")

                self.guest_interface = YLeaf(YType.str, "guest-interface")

                self.state = YLeaf(YType.str, "state")

                self.detailed_guest_status = VirtualServices.VirtualService.Details.DetailedGuestStatus()
                self.detailed_guest_status.parent = self
                self._children_name_map["detailed_guest_status"] = "detailed-guest-status"
                self._children_yang_names.add("detailed-guest-status")

                self.package_information = VirtualServices.VirtualService.Details.PackageInformation()
                self.package_information.parent = self
                self._children_name_map["package_information"] = "package-information"
                self._children_yang_names.add("package-information")

                self.resource_admission = VirtualServices.VirtualService.Details.ResourceAdmission()
                self.resource_admission.parent = self
                self._children_name_map["resource_admission"] = "resource-admission"
                self._children_yang_names.add("resource-admission")

                self.resource_reservation = VirtualServices.VirtualService.Details.ResourceReservation()
                self.resource_reservation.parent = self
                self._children_name_map["resource_reservation"] = "resource-reservation"
                self._children_yang_names.add("resource-reservation")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("activated_profile_name",
                                "guest_interface",
                                "state") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(VirtualServices.VirtualService.Details, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(VirtualServices.VirtualService.Details, self).__setattr__(name, value)


            class PackageInformation(Entity):
                """
                Details of the package for the virtual\-service.
                
                .. attribute:: application
                
                	Details of the application
                	**type**\:   :py:class:`Application <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.PackageInformation.Application>`
                
                .. attribute:: licensing
                
                	Details about the license
                	**type**\:   :py:class:`Licensing <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.PackageInformation.Licensing>`
                
                .. attribute:: name
                
                	Name of the package for the virtual\-service
                	**type**\:  str
                
                .. attribute:: path
                
                	Path to the package
                	**type**\:  str
                
                .. attribute:: signing
                
                	Details of the key signing
                	**type**\:   :py:class:`Signing <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.PackageInformation.Signing>`
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(VirtualServices.VirtualService.Details.PackageInformation, self).__init__()

                    self.yang_name = "package-information"
                    self.yang_parent_name = "details"

                    self.name = YLeaf(YType.str, "name")

                    self.path = YLeaf(YType.str, "path")

                    self.application = VirtualServices.VirtualService.Details.PackageInformation.Application()
                    self.application.parent = self
                    self._children_name_map["application"] = "application"
                    self._children_yang_names.add("application")

                    self.licensing = VirtualServices.VirtualService.Details.PackageInformation.Licensing()
                    self.licensing.parent = self
                    self._children_name_map["licensing"] = "licensing"
                    self._children_yang_names.add("licensing")

                    self.signing = VirtualServices.VirtualService.Details.PackageInformation.Signing()
                    self.signing.parent = self
                    self._children_name_map["signing"] = "signing"
                    self._children_yang_names.add("signing")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("name",
                                    "path") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(VirtualServices.VirtualService.Details.PackageInformation, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(VirtualServices.VirtualService.Details.PackageInformation, self).__setattr__(name, value)


                class Application(Entity):
                    """
                    Details of the application.
                    
                    .. attribute:: description
                    
                    	Description of the application
                    	**type**\:  str
                    
                    .. attribute:: installed_version
                    
                    	Version of the application
                    	**type**\:  str
                    
                    .. attribute:: name
                    
                    	Name of the application
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'virtual-service-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(VirtualServices.VirtualService.Details.PackageInformation.Application, self).__init__()

                        self.yang_name = "application"
                        self.yang_parent_name = "package-information"

                        self.description = YLeaf(YType.str, "description")

                        self.installed_version = YLeaf(YType.str, "installed-version")

                        self.name = YLeaf(YType.str, "name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("description",
                                        "installed_version",
                                        "name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(VirtualServices.VirtualService.Details.PackageInformation.Application, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(VirtualServices.VirtualService.Details.PackageInformation.Application, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.description.is_set or
                            self.installed_version.is_set or
                            self.name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.description.yfilter != YFilter.not_set or
                            self.installed_version.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "application" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.description.get_name_leafdata())
                        if (self.installed_version.is_set or self.installed_version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.installed_version.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "description" or name == "installed-version" or name == "name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "description"):
                            self.description = value
                            self.description.value_namespace = name_space
                            self.description.value_namespace_prefix = name_space_prefix
                        if(value_path == "installed-version"):
                            self.installed_version = value
                            self.installed_version.value_namespace = name_space
                            self.installed_version.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix


                class Signing(Entity):
                    """
                    Details of the key signing.
                    
                    .. attribute:: key_type
                    
                    	The Type of the signed key
                    	**type**\:  str
                    
                    .. attribute:: method
                    
                    	The method the key was signed
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'virtual-service-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(VirtualServices.VirtualService.Details.PackageInformation.Signing, self).__init__()

                        self.yang_name = "signing"
                        self.yang_parent_name = "package-information"

                        self.key_type = YLeaf(YType.str, "key-type")

                        self.method = YLeaf(YType.str, "method")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("key_type",
                                        "method") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(VirtualServices.VirtualService.Details.PackageInformation.Signing, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(VirtualServices.VirtualService.Details.PackageInformation.Signing, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.key_type.is_set or
                            self.method.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.key_type.yfilter != YFilter.not_set or
                            self.method.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "signing" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.key_type.is_set or self.key_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.key_type.get_name_leafdata())
                        if (self.method.is_set or self.method.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.method.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "key-type" or name == "method"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "key-type"):
                            self.key_type = value
                            self.key_type.value_namespace = name_space
                            self.key_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "method"):
                            self.method = value
                            self.method.value_namespace = name_space
                            self.method.value_namespace_prefix = name_space_prefix


                class Licensing(Entity):
                    """
                    Details about the license.
                    
                    .. attribute:: name
                    
                    	The name of the license
                    	**type**\:  str
                    
                    .. attribute:: version
                    
                    	The version of the license
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'virtual-service-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(VirtualServices.VirtualService.Details.PackageInformation.Licensing, self).__init__()

                        self.yang_name = "licensing"
                        self.yang_parent_name = "package-information"

                        self.name = YLeaf(YType.str, "name")

                        self.version = YLeaf(YType.str, "version")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("name",
                                        "version") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(VirtualServices.VirtualService.Details.PackageInformation.Licensing, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(VirtualServices.VirtualService.Details.PackageInformation.Licensing, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.name.is_set or
                            self.version.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set or
                            self.version.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "licensing" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())
                        if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.version.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "name" or name == "version"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix
                        if(value_path == "version"):
                            self.version = value
                            self.version.value_namespace = name_space
                            self.version.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.name.is_set or
                        self.path.is_set or
                        (self.application is not None and self.application.has_data()) or
                        (self.licensing is not None and self.licensing.has_data()) or
                        (self.signing is not None and self.signing.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.path.yfilter != YFilter.not_set or
                        (self.application is not None and self.application.has_operation()) or
                        (self.licensing is not None and self.licensing.has_operation()) or
                        (self.signing is not None and self.signing.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "package-information" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())
                    if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "application"):
                        if (self.application is None):
                            self.application = VirtualServices.VirtualService.Details.PackageInformation.Application()
                            self.application.parent = self
                            self._children_name_map["application"] = "application"
                        return self.application

                    if (child_yang_name == "licensing"):
                        if (self.licensing is None):
                            self.licensing = VirtualServices.VirtualService.Details.PackageInformation.Licensing()
                            self.licensing.parent = self
                            self._children_name_map["licensing"] = "licensing"
                        return self.licensing

                    if (child_yang_name == "signing"):
                        if (self.signing is None):
                            self.signing = VirtualServices.VirtualService.Details.PackageInformation.Signing()
                            self.signing.parent = self
                            self._children_name_map["signing"] = "signing"
                        return self.signing

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "application" or name == "licensing" or name == "signing" or name == "name" or name == "path"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "path"):
                        self.path = value
                        self.path.value_namespace = name_space
                        self.path.value_namespace_prefix = name_space_prefix


            class DetailedGuestStatus(Entity):
                """
                Details on the guest status.
                
                .. attribute:: processes
                
                	All the processes
                	**type**\:   :py:class:`Processes <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.DetailedGuestStatus.Processes>`
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(VirtualServices.VirtualService.Details.DetailedGuestStatus, self).__init__()

                    self.yang_name = "detailed-guest-status"
                    self.yang_parent_name = "details"

                    self.processes = VirtualServices.VirtualService.Details.DetailedGuestStatus.Processes()
                    self.processes.parent = self
                    self._children_name_map["processes"] = "processes"
                    self._children_yang_names.add("processes")


                class Processes(Entity):
                    """
                    All the processes.
                    
                    .. attribute:: memory
                    
                    	Memory of the proccess
                    	**type**\:  str
                    
                    .. attribute:: name
                    
                    	Name of the proccess
                    	**type**\:  str
                    
                    .. attribute:: pid
                    
                    	Process ID
                    	**type**\:  str
                    
                    .. attribute:: status
                    
                    	Status of the proccess
                    	**type**\:  str
                    
                    .. attribute:: uptime
                    
                    	Up time of the proccess
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'virtual-service-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(VirtualServices.VirtualService.Details.DetailedGuestStatus.Processes, self).__init__()

                        self.yang_name = "processes"
                        self.yang_parent_name = "detailed-guest-status"

                        self.memory = YLeaf(YType.str, "memory")

                        self.name = YLeaf(YType.str, "name")

                        self.pid = YLeaf(YType.str, "pid")

                        self.status = YLeaf(YType.str, "status")

                        self.uptime = YLeaf(YType.str, "uptime")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("memory",
                                        "name",
                                        "pid",
                                        "status",
                                        "uptime") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(VirtualServices.VirtualService.Details.DetailedGuestStatus.Processes, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(VirtualServices.VirtualService.Details.DetailedGuestStatus.Processes, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.memory.is_set or
                            self.name.is_set or
                            self.pid.is_set or
                            self.status.is_set or
                            self.uptime.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.memory.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set or
                            self.pid.yfilter != YFilter.not_set or
                            self.status.yfilter != YFilter.not_set or
                            self.uptime.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "processes" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.memory.is_set or self.memory.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.memory.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())
                        if (self.pid.is_set or self.pid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pid.get_name_leafdata())
                        if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.status.get_name_leafdata())
                        if (self.uptime.is_set or self.uptime.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.uptime.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "memory" or name == "name" or name == "pid" or name == "status" or name == "uptime"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "memory"):
                            self.memory = value
                            self.memory.value_namespace = name_space
                            self.memory.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix
                        if(value_path == "pid"):
                            self.pid = value
                            self.pid.value_namespace = name_space
                            self.pid.value_namespace_prefix = name_space_prefix
                        if(value_path == "status"):
                            self.status = value
                            self.status.value_namespace = name_space
                            self.status.value_namespace_prefix = name_space_prefix
                        if(value_path == "uptime"):
                            self.uptime = value
                            self.uptime.value_namespace = name_space
                            self.uptime.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.processes is not None and self.processes.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.processes is not None and self.processes.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "detailed-guest-status" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "processes"):
                        if (self.processes is None):
                            self.processes = VirtualServices.VirtualService.Details.DetailedGuestStatus.Processes()
                            self.processes.parent = self
                            self._children_name_map["processes"] = "processes"
                        return self.processes

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "processes"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class ResourceReservation(Entity):
                """
                Details of the resources reserved for this virtual service.
                
                .. attribute:: cpu
                
                	The percentage of reserved cpu
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: disk
                
                	The amount of reserverd disk space in MB
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: memory
                
                	The amount of reserved memory in MB
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(VirtualServices.VirtualService.Details.ResourceReservation, self).__init__()

                    self.yang_name = "resource-reservation"
                    self.yang_parent_name = "details"

                    self.cpu = YLeaf(YType.uint64, "cpu")

                    self.disk = YLeaf(YType.uint64, "disk")

                    self.memory = YLeaf(YType.uint64, "memory")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("cpu",
                                    "disk",
                                    "memory") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(VirtualServices.VirtualService.Details.ResourceReservation, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(VirtualServices.VirtualService.Details.ResourceReservation, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.cpu.is_set or
                        self.disk.is_set or
                        self.memory.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.cpu.yfilter != YFilter.not_set or
                        self.disk.yfilter != YFilter.not_set or
                        self.memory.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "resource-reservation" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.cpu.is_set or self.cpu.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cpu.get_name_leafdata())
                    if (self.disk.is_set or self.disk.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.disk.get_name_leafdata())
                    if (self.memory.is_set or self.memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.memory.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "cpu" or name == "disk" or name == "memory"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "cpu"):
                        self.cpu = value
                        self.cpu.value_namespace = name_space
                        self.cpu.value_namespace_prefix = name_space_prefix
                    if(value_path == "disk"):
                        self.disk = value
                        self.disk.value_namespace = name_space
                        self.disk.value_namespace_prefix = name_space_prefix
                    if(value_path == "memory"):
                        self.memory = value
                        self.memory.value_namespace = name_space
                        self.memory.value_namespace_prefix = name_space_prefix


            class ResourceAdmission(Entity):
                """
                Resources being allocated for the virtual\-service.
                
                .. attribute:: cpu
                
                	The percentage of cpu being allocated for the virtual\-service
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: disk_space
                
                	The amount of disk space being allocated for the virtual\-service
                	**type**\:  str
                
                .. attribute:: memory
                
                	The amount of memory being allocated for the virtual\-service
                	**type**\:  str
                
                .. attribute:: state
                
                	Thes status the of the resource allocation
                	**type**\:  str
                
                .. attribute:: vcpus
                
                	The amount of VCPUs being allocated for the virtual\-service
                	**type**\:  str
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(VirtualServices.VirtualService.Details.ResourceAdmission, self).__init__()

                    self.yang_name = "resource-admission"
                    self.yang_parent_name = "details"

                    self.cpu = YLeaf(YType.uint64, "cpu")

                    self.disk_space = YLeaf(YType.str, "disk-space")

                    self.memory = YLeaf(YType.str, "memory")

                    self.state = YLeaf(YType.str, "state")

                    self.vcpus = YLeaf(YType.str, "vcpus")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("cpu",
                                    "disk_space",
                                    "memory",
                                    "state",
                                    "vcpus") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(VirtualServices.VirtualService.Details.ResourceAdmission, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(VirtualServices.VirtualService.Details.ResourceAdmission, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.cpu.is_set or
                        self.disk_space.is_set or
                        self.memory.is_set or
                        self.state.is_set or
                        self.vcpus.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.cpu.yfilter != YFilter.not_set or
                        self.disk_space.yfilter != YFilter.not_set or
                        self.memory.yfilter != YFilter.not_set or
                        self.state.yfilter != YFilter.not_set or
                        self.vcpus.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "resource-admission" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.cpu.is_set or self.cpu.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cpu.get_name_leafdata())
                    if (self.disk_space.is_set or self.disk_space.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.disk_space.get_name_leafdata())
                    if (self.memory.is_set or self.memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.memory.get_name_leafdata())
                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state.get_name_leafdata())
                    if (self.vcpus.is_set or self.vcpus.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vcpus.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "cpu" or name == "disk-space" or name == "memory" or name == "state" or name == "vcpus"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "cpu"):
                        self.cpu = value
                        self.cpu.value_namespace = name_space
                        self.cpu.value_namespace_prefix = name_space_prefix
                    if(value_path == "disk-space"):
                        self.disk_space = value
                        self.disk_space.value_namespace = name_space
                        self.disk_space.value_namespace_prefix = name_space_prefix
                    if(value_path == "memory"):
                        self.memory = value
                        self.memory.value_namespace = name_space
                        self.memory.value_namespace_prefix = name_space_prefix
                    if(value_path == "state"):
                        self.state = value
                        self.state.value_namespace = name_space
                        self.state.value_namespace_prefix = name_space_prefix
                    if(value_path == "vcpus"):
                        self.vcpus = value
                        self.vcpus.value_namespace = name_space
                        self.vcpus.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.activated_profile_name.is_set or
                    self.guest_interface.is_set or
                    self.state.is_set or
                    (self.detailed_guest_status is not None and self.detailed_guest_status.has_data()) or
                    (self.package_information is not None and self.package_information.has_data()) or
                    (self.resource_admission is not None and self.resource_admission.has_data()) or
                    (self.resource_reservation is not None and self.resource_reservation.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.activated_profile_name.yfilter != YFilter.not_set or
                    self.guest_interface.yfilter != YFilter.not_set or
                    self.state.yfilter != YFilter.not_set or
                    (self.detailed_guest_status is not None and self.detailed_guest_status.has_operation()) or
                    (self.package_information is not None and self.package_information.has_operation()) or
                    (self.resource_admission is not None and self.resource_admission.has_operation()) or
                    (self.resource_reservation is not None and self.resource_reservation.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "details" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.activated_profile_name.is_set or self.activated_profile_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.activated_profile_name.get_name_leafdata())
                if (self.guest_interface.is_set or self.guest_interface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.guest_interface.get_name_leafdata())
                if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.state.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "detailed-guest-status"):
                    if (self.detailed_guest_status is None):
                        self.detailed_guest_status = VirtualServices.VirtualService.Details.DetailedGuestStatus()
                        self.detailed_guest_status.parent = self
                        self._children_name_map["detailed_guest_status"] = "detailed-guest-status"
                    return self.detailed_guest_status

                if (child_yang_name == "package-information"):
                    if (self.package_information is None):
                        self.package_information = VirtualServices.VirtualService.Details.PackageInformation()
                        self.package_information.parent = self
                        self._children_name_map["package_information"] = "package-information"
                    return self.package_information

                if (child_yang_name == "resource-admission"):
                    if (self.resource_admission is None):
                        self.resource_admission = VirtualServices.VirtualService.Details.ResourceAdmission()
                        self.resource_admission.parent = self
                        self._children_name_map["resource_admission"] = "resource-admission"
                    return self.resource_admission

                if (child_yang_name == "resource-reservation"):
                    if (self.resource_reservation is None):
                        self.resource_reservation = VirtualServices.VirtualService.Details.ResourceReservation()
                        self.resource_reservation.parent = self
                        self._children_name_map["resource_reservation"] = "resource-reservation"
                    return self.resource_reservation

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "detailed-guest-status" or name == "package-information" or name == "resource-admission" or name == "resource-reservation" or name == "activated-profile-name" or name == "guest-interface" or name == "state"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "activated-profile-name"):
                    self.activated_profile_name = value
                    self.activated_profile_name.value_namespace = name_space
                    self.activated_profile_name.value_namespace_prefix = name_space_prefix
                if(value_path == "guest-interface"):
                    self.guest_interface = value
                    self.guest_interface.value_namespace = name_space
                    self.guest_interface.value_namespace_prefix = name_space_prefix
                if(value_path == "state"):
                    self.state = value
                    self.state.value_namespace = name_space
                    self.state.value_namespace_prefix = name_space_prefix


        class Utilization(Entity):
            """
            Utilization of device resources for a virtual\-service.
            
            .. attribute:: cpu_util
            
            	Details on the CPU utilization for the virtual\-service
            	**type**\:   :py:class:`CpuUtil <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Utilization.CpuUtil>`
            
            .. attribute:: memory_util
            
            	Details on the memory usage for the virtual\-service
            	**type**\:   :py:class:`MemoryUtil <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Utilization.MemoryUtil>`
            
            .. attribute:: name
            
            	The name of the virtual service
            	**type**\:  str
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(VirtualServices.VirtualService.Utilization, self).__init__()

                self.yang_name = "utilization"
                self.yang_parent_name = "virtual-service"

                self.name = YLeaf(YType.str, "name")

                self.cpu_util = VirtualServices.VirtualService.Utilization.CpuUtil()
                self.cpu_util.parent = self
                self._children_name_map["cpu_util"] = "cpu-util"
                self._children_yang_names.add("cpu-util")

                self.memory_util = VirtualServices.VirtualService.Utilization.MemoryUtil()
                self.memory_util.parent = self
                self._children_name_map["memory_util"] = "memory-util"
                self._children_yang_names.add("memory-util")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(VirtualServices.VirtualService.Utilization, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(VirtualServices.VirtualService.Utilization, self).__setattr__(name, value)


            class CpuUtil(Entity):
                """
                Details on the CPU utilization for the virtual\-service.
                
                .. attribute:: actual_application_util
                
                	Percetnage of CPU actual utilization for the virtual\-service
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: cpu_state
                
                	The state of the CPU utilization for the virtual\-service
                	**type**\:  str
                
                .. attribute:: requested_application_util
                
                	Percentage of requested CPU utilization by the virtual\-service
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(VirtualServices.VirtualService.Utilization.CpuUtil, self).__init__()

                    self.yang_name = "cpu-util"
                    self.yang_parent_name = "utilization"

                    self.actual_application_util = YLeaf(YType.uint64, "actual-application-util")

                    self.cpu_state = YLeaf(YType.str, "cpu-state")

                    self.requested_application_util = YLeaf(YType.uint64, "requested-application-util")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("actual_application_util",
                                    "cpu_state",
                                    "requested_application_util") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(VirtualServices.VirtualService.Utilization.CpuUtil, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(VirtualServices.VirtualService.Utilization.CpuUtil, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.actual_application_util.is_set or
                        self.cpu_state.is_set or
                        self.requested_application_util.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.actual_application_util.yfilter != YFilter.not_set or
                        self.cpu_state.yfilter != YFilter.not_set or
                        self.requested_application_util.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cpu-util" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.actual_application_util.is_set or self.actual_application_util.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.actual_application_util.get_name_leafdata())
                    if (self.cpu_state.is_set or self.cpu_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cpu_state.get_name_leafdata())
                    if (self.requested_application_util.is_set or self.requested_application_util.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.requested_application_util.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "actual-application-util" or name == "cpu-state" or name == "requested-application-util"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "actual-application-util"):
                        self.actual_application_util = value
                        self.actual_application_util.value_namespace = name_space
                        self.actual_application_util.value_namespace_prefix = name_space_prefix
                    if(value_path == "cpu-state"):
                        self.cpu_state = value
                        self.cpu_state.value_namespace = name_space
                        self.cpu_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "requested-application-util"):
                        self.requested_application_util = value
                        self.requested_application_util.value_namespace = name_space
                        self.requested_application_util.value_namespace_prefix = name_space_prefix


            class MemoryUtil(Entity):
                """
                Details on the memory usage for the virtual\-service.
                
                .. attribute:: memory_allocation
                
                	Amount of memory being allocated for the virtual\-service in KB
                	**type**\:  str
                
                .. attribute:: memory_used
                
                	Amount of memory being used for the virtual\-service in KB
                	**type**\:  str
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(VirtualServices.VirtualService.Utilization.MemoryUtil, self).__init__()

                    self.yang_name = "memory-util"
                    self.yang_parent_name = "utilization"

                    self.memory_allocation = YLeaf(YType.str, "memory-allocation")

                    self.memory_used = YLeaf(YType.str, "memory-used")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("memory_allocation",
                                    "memory_used") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(VirtualServices.VirtualService.Utilization.MemoryUtil, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(VirtualServices.VirtualService.Utilization.MemoryUtil, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.memory_allocation.is_set or
                        self.memory_used.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.memory_allocation.yfilter != YFilter.not_set or
                        self.memory_used.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "memory-util" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.memory_allocation.is_set or self.memory_allocation.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.memory_allocation.get_name_leafdata())
                    if (self.memory_used.is_set or self.memory_used.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.memory_used.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "memory-allocation" or name == "memory-used"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "memory-allocation"):
                        self.memory_allocation = value
                        self.memory_allocation.value_namespace = name_space
                        self.memory_allocation.value_namespace_prefix = name_space_prefix
                    if(value_path == "memory-used"):
                        self.memory_used = value
                        self.memory_used.value_namespace = name_space
                        self.memory_used.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.name.is_set or
                    (self.cpu_util is not None and self.cpu_util.has_data()) or
                    (self.memory_util is not None and self.memory_util.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    (self.cpu_util is not None and self.cpu_util.has_operation()) or
                    (self.memory_util is not None and self.memory_util.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "utilization" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "cpu-util"):
                    if (self.cpu_util is None):
                        self.cpu_util = VirtualServices.VirtualService.Utilization.CpuUtil()
                        self.cpu_util.parent = self
                        self._children_name_map["cpu_util"] = "cpu-util"
                    return self.cpu_util

                if (child_yang_name == "memory-util"):
                    if (self.memory_util is None):
                        self.memory_util = VirtualServices.VirtualService.Utilization.MemoryUtil()
                        self.memory_util.parent = self
                        self._children_name_map["memory_util"] = "memory-util"
                    return self.memory_util

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpu-util" or name == "memory-util" or name == "name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix


        class NetworkUtils(Entity):
            """
            list of the network utilizations for the virtual\-service.
            
            .. attribute:: network_util
            
            	Details on a network utilization for the virtual\-service
            	**type**\: list of    :py:class:`NetworkUtil <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.NetworkUtils.NetworkUtil>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(VirtualServices.VirtualService.NetworkUtils, self).__init__()

                self.yang_name = "network-utils"
                self.yang_parent_name = "virtual-service"

                self.network_util = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(VirtualServices.VirtualService.NetworkUtils, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(VirtualServices.VirtualService.NetworkUtils, self).__setattr__(name, value)


            class NetworkUtil(Entity):
                """
                Details on a network utilization for the virtual\-service.
                
                .. attribute:: name  <key>
                
                	The name of the network that is being used for the virtual\-service
                	**type**\:  str
                
                .. attribute:: alias  <key>
                
                	The alias of the network that is being used for the virtual\-service
                	**type**\:  str
                
                .. attribute:: rx_bytes
                
                	The number of rx bytes being utilized for the virtual\-service
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_errors
                
                	The number of rx errors
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_packets
                
                	The number of rx packets being utilized for the virtual\-service
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_bytes
                
                	The number of tx bytes being utilized for the virtual\-service
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_errors
                
                	The number of tx errors
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_packets
                
                	The number of tx packets being utilized for the virtual\-service
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(VirtualServices.VirtualService.NetworkUtils.NetworkUtil, self).__init__()

                    self.yang_name = "network-util"
                    self.yang_parent_name = "network-utils"

                    self.name = YLeaf(YType.str, "name")

                    self.alias = YLeaf(YType.str, "alias")

                    self.rx_bytes = YLeaf(YType.uint64, "rx-bytes")

                    self.rx_errors = YLeaf(YType.uint64, "rx-errors")

                    self.rx_packets = YLeaf(YType.uint64, "rx-packets")

                    self.tx_bytes = YLeaf(YType.uint64, "tx-bytes")

                    self.tx_errors = YLeaf(YType.uint64, "tx-errors")

                    self.tx_packets = YLeaf(YType.uint64, "tx-packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("name",
                                    "alias",
                                    "rx_bytes",
                                    "rx_errors",
                                    "rx_packets",
                                    "tx_bytes",
                                    "tx_errors",
                                    "tx_packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(VirtualServices.VirtualService.NetworkUtils.NetworkUtil, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(VirtualServices.VirtualService.NetworkUtils.NetworkUtil, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.name.is_set or
                        self.alias.is_set or
                        self.rx_bytes.is_set or
                        self.rx_errors.is_set or
                        self.rx_packets.is_set or
                        self.tx_bytes.is_set or
                        self.tx_errors.is_set or
                        self.tx_packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.alias.yfilter != YFilter.not_set or
                        self.rx_bytes.yfilter != YFilter.not_set or
                        self.rx_errors.yfilter != YFilter.not_set or
                        self.rx_packets.yfilter != YFilter.not_set or
                        self.tx_bytes.yfilter != YFilter.not_set or
                        self.tx_errors.yfilter != YFilter.not_set or
                        self.tx_packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "network-util" + "[name='" + self.name.get() + "']" + "[alias='" + self.alias.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())
                    if (self.alias.is_set or self.alias.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.alias.get_name_leafdata())
                    if (self.rx_bytes.is_set or self.rx_bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_bytes.get_name_leafdata())
                    if (self.rx_errors.is_set or self.rx_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_errors.get_name_leafdata())
                    if (self.rx_packets.is_set or self.rx_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_packets.get_name_leafdata())
                    if (self.tx_bytes.is_set or self.tx_bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_bytes.get_name_leafdata())
                    if (self.tx_errors.is_set or self.tx_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_errors.get_name_leafdata())
                    if (self.tx_packets.is_set or self.tx_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "name" or name == "alias" or name == "rx-bytes" or name == "rx-errors" or name == "rx-packets" or name == "tx-bytes" or name == "tx-errors" or name == "tx-packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "alias"):
                        self.alias = value
                        self.alias.value_namespace = name_space
                        self.alias.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-bytes"):
                        self.rx_bytes = value
                        self.rx_bytes.value_namespace = name_space
                        self.rx_bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-errors"):
                        self.rx_errors = value
                        self.rx_errors.value_namespace = name_space
                        self.rx_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-packets"):
                        self.rx_packets = value
                        self.rx_packets.value_namespace = name_space
                        self.rx_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-bytes"):
                        self.tx_bytes = value
                        self.tx_bytes.value_namespace = name_space
                        self.tx_bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-errors"):
                        self.tx_errors = value
                        self.tx_errors.value_namespace = name_space
                        self.tx_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-packets"):
                        self.tx_packets = value
                        self.tx_packets.value_namespace = name_space
                        self.tx_packets.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.network_util:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.network_util:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "network-utils" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "network-util"):
                    for c in self.network_util:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = VirtualServices.VirtualService.NetworkUtils.NetworkUtil()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.network_util.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "network-util"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class StorageUtils(Entity):
            """
            List of the storage utilizations for the virtual\-service.
            
            .. attribute:: storage_util
            
            	Details on a storage utilization for the virtual\-service
            	**type**\: list of    :py:class:`StorageUtil <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.StorageUtils.StorageUtil>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(VirtualServices.VirtualService.StorageUtils, self).__init__()

                self.yang_name = "storage-utils"
                self.yang_parent_name = "virtual-service"

                self.storage_util = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(VirtualServices.VirtualService.StorageUtils, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(VirtualServices.VirtualService.StorageUtils, self).__setattr__(name, value)


            class StorageUtil(Entity):
                """
                Details on a storage utilization for the virtual\-service.
                
                .. attribute:: name  <key>
                
                	The name of the storage process being used for the virtual\-service
                	**type**\:  str
                
                .. attribute:: alias  <key>
                
                	The alias of the storage process being used for the virtual\-service
                	**type**\:  str
                
                .. attribute:: available
                
                	The available storage in 1K blocks
                	**type**\:  str
                
                .. attribute:: capacity
                
                	The storage capactity in 1K blocks
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: errors
                
                	The name of errors on the storage process
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rd_bytes
                
                	The number of RD bytes being used for the virtual\-service
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rd_requests
                
                	The number of rd requests being used for the virtual\-service
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: usage
                
                	The percetage of storage capactiy being used
                	**type**\:  str
                
                .. attribute:: used
                
                	The number of 1K blocks being used
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wr_bytes
                
                	The number of WR bytes for the virtual\-service
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wr_requests
                
                	The number of WR requests for the virtual\-service
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(VirtualServices.VirtualService.StorageUtils.StorageUtil, self).__init__()

                    self.yang_name = "storage-util"
                    self.yang_parent_name = "storage-utils"

                    self.name = YLeaf(YType.str, "name")

                    self.alias = YLeaf(YType.str, "alias")

                    self.available = YLeaf(YType.str, "available")

                    self.capacity = YLeaf(YType.uint64, "capacity")

                    self.errors = YLeaf(YType.uint64, "errors")

                    self.rd_bytes = YLeaf(YType.uint64, "rd-bytes")

                    self.rd_requests = YLeaf(YType.uint64, "rd-requests")

                    self.usage = YLeaf(YType.str, "usage")

                    self.used = YLeaf(YType.uint64, "used")

                    self.wr_bytes = YLeaf(YType.uint64, "wr-bytes")

                    self.wr_requests = YLeaf(YType.uint64, "wr-requests")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("name",
                                    "alias",
                                    "available",
                                    "capacity",
                                    "errors",
                                    "rd_bytes",
                                    "rd_requests",
                                    "usage",
                                    "used",
                                    "wr_bytes",
                                    "wr_requests") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(VirtualServices.VirtualService.StorageUtils.StorageUtil, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(VirtualServices.VirtualService.StorageUtils.StorageUtil, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.name.is_set or
                        self.alias.is_set or
                        self.available.is_set or
                        self.capacity.is_set or
                        self.errors.is_set or
                        self.rd_bytes.is_set or
                        self.rd_requests.is_set or
                        self.usage.is_set or
                        self.used.is_set or
                        self.wr_bytes.is_set or
                        self.wr_requests.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.alias.yfilter != YFilter.not_set or
                        self.available.yfilter != YFilter.not_set or
                        self.capacity.yfilter != YFilter.not_set or
                        self.errors.yfilter != YFilter.not_set or
                        self.rd_bytes.yfilter != YFilter.not_set or
                        self.rd_requests.yfilter != YFilter.not_set or
                        self.usage.yfilter != YFilter.not_set or
                        self.used.yfilter != YFilter.not_set or
                        self.wr_bytes.yfilter != YFilter.not_set or
                        self.wr_requests.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "storage-util" + "[name='" + self.name.get() + "']" + "[alias='" + self.alias.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())
                    if (self.alias.is_set or self.alias.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.alias.get_name_leafdata())
                    if (self.available.is_set or self.available.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.available.get_name_leafdata())
                    if (self.capacity.is_set or self.capacity.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.capacity.get_name_leafdata())
                    if (self.errors.is_set or self.errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.errors.get_name_leafdata())
                    if (self.rd_bytes.is_set or self.rd_bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rd_bytes.get_name_leafdata())
                    if (self.rd_requests.is_set or self.rd_requests.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rd_requests.get_name_leafdata())
                    if (self.usage.is_set or self.usage.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.usage.get_name_leafdata())
                    if (self.used.is_set or self.used.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.used.get_name_leafdata())
                    if (self.wr_bytes.is_set or self.wr_bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.wr_bytes.get_name_leafdata())
                    if (self.wr_requests.is_set or self.wr_requests.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.wr_requests.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "name" or name == "alias" or name == "available" or name == "capacity" or name == "errors" or name == "rd-bytes" or name == "rd-requests" or name == "usage" or name == "used" or name == "wr-bytes" or name == "wr-requests"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "alias"):
                        self.alias = value
                        self.alias.value_namespace = name_space
                        self.alias.value_namespace_prefix = name_space_prefix
                    if(value_path == "available"):
                        self.available = value
                        self.available.value_namespace = name_space
                        self.available.value_namespace_prefix = name_space_prefix
                    if(value_path == "capacity"):
                        self.capacity = value
                        self.capacity.value_namespace = name_space
                        self.capacity.value_namespace_prefix = name_space_prefix
                    if(value_path == "errors"):
                        self.errors = value
                        self.errors.value_namespace = name_space
                        self.errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "rd-bytes"):
                        self.rd_bytes = value
                        self.rd_bytes.value_namespace = name_space
                        self.rd_bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "rd-requests"):
                        self.rd_requests = value
                        self.rd_requests.value_namespace = name_space
                        self.rd_requests.value_namespace_prefix = name_space_prefix
                    if(value_path == "usage"):
                        self.usage = value
                        self.usage.value_namespace = name_space
                        self.usage.value_namespace_prefix = name_space_prefix
                    if(value_path == "used"):
                        self.used = value
                        self.used.value_namespace = name_space
                        self.used.value_namespace_prefix = name_space_prefix
                    if(value_path == "wr-bytes"):
                        self.wr_bytes = value
                        self.wr_bytes.value_namespace = name_space
                        self.wr_bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "wr-requests"):
                        self.wr_requests = value
                        self.wr_requests.value_namespace = name_space
                        self.wr_requests.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.storage_util:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.storage_util:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "storage-utils" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "storage-util"):
                    for c in self.storage_util:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = VirtualServices.VirtualService.StorageUtils.StorageUtil()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.storage_util.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "storage-util"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class AttachedDevices(Entity):
            """
            Details for the devices attached to this virtual service.
            
            .. attribute:: attached_device
            
            	List of attached devices
            	**type**\: list of    :py:class:`AttachedDevice <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.AttachedDevices.AttachedDevice>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(VirtualServices.VirtualService.AttachedDevices, self).__init__()

                self.yang_name = "attached-devices"
                self.yang_parent_name = "virtual-service"

                self.attached_device = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(VirtualServices.VirtualService.AttachedDevices, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(VirtualServices.VirtualService.AttachedDevices, self).__setattr__(name, value)


            class AttachedDevice(Entity):
                """
                List of attached devices.
                
                .. attribute:: name  <key>
                
                	The name of the attached device
                	**type**\:  str
                
                .. attribute:: alias
                
                	The alias for the attached device
                	**type**\:  str
                
                .. attribute:: type
                
                	The type of the attached device
                	**type**\:  str
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(VirtualServices.VirtualService.AttachedDevices.AttachedDevice, self).__init__()

                    self.yang_name = "attached-device"
                    self.yang_parent_name = "attached-devices"

                    self.name = YLeaf(YType.str, "name")

                    self.alias = YLeaf(YType.str, "alias")

                    self.type = YLeaf(YType.str, "type")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("name",
                                    "alias",
                                    "type") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(VirtualServices.VirtualService.AttachedDevices.AttachedDevice, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(VirtualServices.VirtualService.AttachedDevices.AttachedDevice, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.name.is_set or
                        self.alias.is_set or
                        self.type.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.alias.yfilter != YFilter.not_set or
                        self.type.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "attached-device" + "[name='" + self.name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())
                    if (self.alias.is_set or self.alias.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.alias.get_name_leafdata())
                    if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.type.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "name" or name == "alias" or name == "type"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "alias"):
                        self.alias = value
                        self.alias.value_namespace = name_space
                        self.alias.value_namespace_prefix = name_space_prefix
                    if(value_path == "type"):
                        self.type = value
                        self.type.value_namespace = name_space
                        self.type.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.attached_device:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.attached_device:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "attached-devices" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "attached-device"):
                    for c in self.attached_device:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = VirtualServices.VirtualService.AttachedDevices.AttachedDevice()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.attached_device.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "attached-device"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class NetworkInterfaces(Entity):
            """
            Details for the network interfaces.
            
            .. attribute:: network_interface
            
            	Details for a network interface
            	**type**\: list of    :py:class:`NetworkInterface <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.NetworkInterfaces.NetworkInterface>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(VirtualServices.VirtualService.NetworkInterfaces, self).__init__()

                self.yang_name = "network-interfaces"
                self.yang_parent_name = "virtual-service"

                self.network_interface = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(VirtualServices.VirtualService.NetworkInterfaces, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(VirtualServices.VirtualService.NetworkInterfaces, self).__setattr__(name, value)


            class NetworkInterface(Entity):
                """
                Details for a network interface.
                
                .. attribute:: mac_address  <key>
                
                	The MAC address for the network interface
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: attached_interface
                
                	Name of the the attached interface
                	**type**\:  str
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(VirtualServices.VirtualService.NetworkInterfaces.NetworkInterface, self).__init__()

                    self.yang_name = "network-interface"
                    self.yang_parent_name = "network-interfaces"

                    self.mac_address = YLeaf(YType.str, "mac-address")

                    self.attached_interface = YLeaf(YType.str, "attached-interface")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("mac_address",
                                    "attached_interface") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(VirtualServices.VirtualService.NetworkInterfaces.NetworkInterface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(VirtualServices.VirtualService.NetworkInterfaces.NetworkInterface, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.mac_address.is_set or
                        self.attached_interface.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.mac_address.yfilter != YFilter.not_set or
                        self.attached_interface.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "network-interface" + "[mac-address='" + self.mac_address.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mac_address.get_name_leafdata())
                    if (self.attached_interface.is_set or self.attached_interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.attached_interface.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "mac-address" or name == "attached-interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "mac-address"):
                        self.mac_address = value
                        self.mac_address.value_namespace = name_space
                        self.mac_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "attached-interface"):
                        self.attached_interface = value
                        self.attached_interface.value_namespace = name_space
                        self.attached_interface.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.network_interface:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.network_interface:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "network-interfaces" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "network-interface"):
                    for c in self.network_interface:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = VirtualServices.VirtualService.NetworkInterfaces.NetworkInterface()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.network_interface.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "network-interface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class GuestRoutes(Entity):
            """
            Routes for the guest interface.
            
            .. attribute:: guest_route
            
            	List of guest routes for a guest interface
            	**type**\: list of    :py:class:`GuestRoute <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.GuestRoutes.GuestRoute>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(VirtualServices.VirtualService.GuestRoutes, self).__init__()

                self.yang_name = "guest-routes"
                self.yang_parent_name = "virtual-service"

                self.guest_route = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(VirtualServices.VirtualService.GuestRoutes, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(VirtualServices.VirtualService.GuestRoutes, self).__setattr__(name, value)


            class GuestRoute(Entity):
                """
                List of guest routes for a guest interface.
                
                .. attribute:: route  <key>
                
                	A guest route for a guest interface
                	**type**\:  str
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(VirtualServices.VirtualService.GuestRoutes.GuestRoute, self).__init__()

                    self.yang_name = "guest-route"
                    self.yang_parent_name = "guest-routes"

                    self.route = YLeaf(YType.str, "route")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("route") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(VirtualServices.VirtualService.GuestRoutes.GuestRoute, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(VirtualServices.VirtualService.GuestRoutes.GuestRoute, self).__setattr__(name, value)

                def has_data(self):
                    return self.route.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.route.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "guest-route" + "[route='" + self.route.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.route.is_set or self.route.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.route.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "route"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "route"):
                        self.route = value
                        self.route.value_namespace = name_space
                        self.route.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.guest_route:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.guest_route:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "guest-routes" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "guest-route"):
                    for c in self.guest_route:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = VirtualServices.VirtualService.GuestRoutes.GuestRoute()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.guest_route.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "guest-route"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.name.is_set or
                (self.attached_devices is not None and self.attached_devices.has_data()) or
                (self.details is not None and self.details.has_data()) or
                (self.guest_routes is not None and self.guest_routes.has_data()) or
                (self.network_interfaces is not None and self.network_interfaces.has_data()) or
                (self.network_utils is not None and self.network_utils.has_data()) or
                (self.storage_utils is not None and self.storage_utils.has_data()) or
                (self.utilization is not None and self.utilization.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.name.yfilter != YFilter.not_set or
                (self.attached_devices is not None and self.attached_devices.has_operation()) or
                (self.details is not None and self.details.has_operation()) or
                (self.guest_routes is not None and self.guest_routes.has_operation()) or
                (self.network_interfaces is not None and self.network_interfaces.has_operation()) or
                (self.network_utils is not None and self.network_utils.has_operation()) or
                (self.storage_utils is not None and self.storage_utils.has_operation()) or
                (self.utilization is not None and self.utilization.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "virtual-service" + "[name='" + self.name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-virtual-service-oper:virtual-services/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.name.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "attached-devices"):
                if (self.attached_devices is None):
                    self.attached_devices = VirtualServices.VirtualService.AttachedDevices()
                    self.attached_devices.parent = self
                    self._children_name_map["attached_devices"] = "attached-devices"
                return self.attached_devices

            if (child_yang_name == "details"):
                if (self.details is None):
                    self.details = VirtualServices.VirtualService.Details()
                    self.details.parent = self
                    self._children_name_map["details"] = "details"
                return self.details

            if (child_yang_name == "guest-routes"):
                if (self.guest_routes is None):
                    self.guest_routes = VirtualServices.VirtualService.GuestRoutes()
                    self.guest_routes.parent = self
                    self._children_name_map["guest_routes"] = "guest-routes"
                return self.guest_routes

            if (child_yang_name == "network-interfaces"):
                if (self.network_interfaces is None):
                    self.network_interfaces = VirtualServices.VirtualService.NetworkInterfaces()
                    self.network_interfaces.parent = self
                    self._children_name_map["network_interfaces"] = "network-interfaces"
                return self.network_interfaces

            if (child_yang_name == "network-utils"):
                if (self.network_utils is None):
                    self.network_utils = VirtualServices.VirtualService.NetworkUtils()
                    self.network_utils.parent = self
                    self._children_name_map["network_utils"] = "network-utils"
                return self.network_utils

            if (child_yang_name == "storage-utils"):
                if (self.storage_utils is None):
                    self.storage_utils = VirtualServices.VirtualService.StorageUtils()
                    self.storage_utils.parent = self
                    self._children_name_map["storage_utils"] = "storage-utils"
                return self.storage_utils

            if (child_yang_name == "utilization"):
                if (self.utilization is None):
                    self.utilization = VirtualServices.VirtualService.Utilization()
                    self.utilization.parent = self
                    self._children_name_map["utilization"] = "utilization"
                return self.utilization

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "attached-devices" or name == "details" or name == "guest-routes" or name == "network-interfaces" or name == "network-utils" or name == "storage-utils" or name == "utilization" or name == "name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "name"):
                self.name = value
                self.name.value_namespace = name_space
                self.name.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.virtual_service:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.virtual_service:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-virtual-service-oper:virtual-services" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "virtual-service"):
            for c in self.virtual_service:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = VirtualServices.VirtualService()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.virtual_service.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "virtual-service"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = VirtualServices()
        return self._top_entity


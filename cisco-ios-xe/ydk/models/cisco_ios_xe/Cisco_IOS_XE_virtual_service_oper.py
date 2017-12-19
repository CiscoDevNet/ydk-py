""" Cisco_IOS_XE_virtual_service_oper 

This module contains a collection of YANG definitions for monitoring
virtual services in a Network Element.Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class VirtualServices(Entity):
    """
    Names and Status of virtual services on the device
    
    .. attribute:: virtual_service
    
    	A virtual service
    	**type**\: list of  		 :py:class:`VirtualService <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService>`
    
    

    """

    _prefix = 'virtual-service-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(VirtualServices, self).__init__()
        self._top_entity = None

        self.yang_name = "virtual-services"
        self.yang_parent_name = "Cisco-IOS-XE-virtual-service-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"virtual-service" : ("virtual_service", VirtualServices.VirtualService)}

        self.virtual_service = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-virtual-service-oper:virtual-services"

    def __setattr__(self, name, value):
        self._perform_setattr(VirtualServices, [], name, value)


    class VirtualService(Entity):
        """
        A virtual service.
        
        .. attribute:: name  <key>
        
        	The name of the virtual service
        	**type**\: str
        
        .. attribute:: details
        
        	Details of the virtual service
        	**type**\:  :py:class:`Details <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details>`
        
        .. attribute:: utilization
        
        	Utilization of device resources for a virtual\-service
        	**type**\:  :py:class:`Utilization <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Utilization>`
        
        .. attribute:: network_utils
        
        	list of the network utilizations for the virtual\-service
        	**type**\:  :py:class:`NetworkUtils <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.NetworkUtils>`
        
        .. attribute:: storage_utils
        
        	List of the storage utilizations for the virtual\-service
        	**type**\:  :py:class:`StorageUtils <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.StorageUtils>`
        
        .. attribute:: attached_devices
        
        	Details for the devices attached to this virtual service
        	**type**\:  :py:class:`AttachedDevices <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.AttachedDevices>`
        
        .. attribute:: network_interfaces
        
        	Details for the network interfaces
        	**type**\:  :py:class:`NetworkInterfaces <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.NetworkInterfaces>`
        
        .. attribute:: guest_routes
        
        	Routes for the guest interface
        	**type**\:  :py:class:`GuestRoutes <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.GuestRoutes>`
        
        

        """

        _prefix = 'virtual-service-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(VirtualServices.VirtualService, self).__init__()

            self.yang_name = "virtual-service"
            self.yang_parent_name = "virtual-services"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"details" : ("details", VirtualServices.VirtualService.Details), "utilization" : ("utilization", VirtualServices.VirtualService.Utilization), "network-utils" : ("network_utils", VirtualServices.VirtualService.NetworkUtils), "storage-utils" : ("storage_utils", VirtualServices.VirtualService.StorageUtils), "attached-devices" : ("attached_devices", VirtualServices.VirtualService.AttachedDevices), "network-interfaces" : ("network_interfaces", VirtualServices.VirtualService.NetworkInterfaces), "guest-routes" : ("guest_routes", VirtualServices.VirtualService.GuestRoutes)}
            self._child_list_classes = {}

            self.name = YLeaf(YType.str, "name")

            self.details = VirtualServices.VirtualService.Details()
            self.details.parent = self
            self._children_name_map["details"] = "details"
            self._children_yang_names.add("details")

            self.utilization = VirtualServices.VirtualService.Utilization()
            self.utilization.parent = self
            self._children_name_map["utilization"] = "utilization"
            self._children_yang_names.add("utilization")

            self.network_utils = VirtualServices.VirtualService.NetworkUtils()
            self.network_utils.parent = self
            self._children_name_map["network_utils"] = "network-utils"
            self._children_yang_names.add("network-utils")

            self.storage_utils = VirtualServices.VirtualService.StorageUtils()
            self.storage_utils.parent = self
            self._children_name_map["storage_utils"] = "storage-utils"
            self._children_yang_names.add("storage-utils")

            self.attached_devices = VirtualServices.VirtualService.AttachedDevices()
            self.attached_devices.parent = self
            self._children_name_map["attached_devices"] = "attached-devices"
            self._children_yang_names.add("attached-devices")

            self.network_interfaces = VirtualServices.VirtualService.NetworkInterfaces()
            self.network_interfaces.parent = self
            self._children_name_map["network_interfaces"] = "network-interfaces"
            self._children_yang_names.add("network-interfaces")

            self.guest_routes = VirtualServices.VirtualService.GuestRoutes()
            self.guest_routes.parent = self
            self._children_name_map["guest_routes"] = "guest-routes"
            self._children_yang_names.add("guest-routes")
            self._segment_path = lambda: "virtual-service" + "[name='" + self.name.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-virtual-service-oper:virtual-services/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(VirtualServices.VirtualService, ['name'], name, value)


        class Details(Entity):
            """
            Details of the virtual service.
            
            .. attribute:: state
            
            	State of the virtual service
            	**type**\: str
            
            .. attribute:: package_information
            
            	Details of the package for the virtual\-service
            	**type**\:  :py:class:`PackageInformation <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.PackageInformation>`
            
            .. attribute:: detailed_guest_status
            
            	Details on the guest status
            	**type**\:  :py:class:`DetailedGuestStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.DetailedGuestStatus>`
            
            .. attribute:: activated_profile_name
            
            	The activated profile name
            	**type**\: str
            
            .. attribute:: resource_reservation
            
            	Details of the resources reserved for this virtual service
            	**type**\:  :py:class:`ResourceReservation <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.ResourceReservation>`
            
            .. attribute:: guest_interface
            
            	The name of a guest interface
            	**type**\: str
            
            .. attribute:: resource_admission
            
            	Resources being allocated for the virtual\-service
            	**type**\:  :py:class:`ResourceAdmission <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.ResourceAdmission>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(VirtualServices.VirtualService.Details, self).__init__()

                self.yang_name = "details"
                self.yang_parent_name = "virtual-service"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {"package-information" : ("package_information", VirtualServices.VirtualService.Details.PackageInformation), "detailed-guest-status" : ("detailed_guest_status", VirtualServices.VirtualService.Details.DetailedGuestStatus), "resource-reservation" : ("resource_reservation", VirtualServices.VirtualService.Details.ResourceReservation), "resource-admission" : ("resource_admission", VirtualServices.VirtualService.Details.ResourceAdmission)}
                self._child_list_classes = {}

                self.state = YLeaf(YType.str, "state")

                self.activated_profile_name = YLeaf(YType.str, "activated-profile-name")

                self.guest_interface = YLeaf(YType.str, "guest-interface")

                self.package_information = VirtualServices.VirtualService.Details.PackageInformation()
                self.package_information.parent = self
                self._children_name_map["package_information"] = "package-information"
                self._children_yang_names.add("package-information")

                self.detailed_guest_status = VirtualServices.VirtualService.Details.DetailedGuestStatus()
                self.detailed_guest_status.parent = self
                self._children_name_map["detailed_guest_status"] = "detailed-guest-status"
                self._children_yang_names.add("detailed-guest-status")

                self.resource_reservation = VirtualServices.VirtualService.Details.ResourceReservation()
                self.resource_reservation.parent = self
                self._children_name_map["resource_reservation"] = "resource-reservation"
                self._children_yang_names.add("resource-reservation")

                self.resource_admission = VirtualServices.VirtualService.Details.ResourceAdmission()
                self.resource_admission.parent = self
                self._children_name_map["resource_admission"] = "resource-admission"
                self._children_yang_names.add("resource-admission")
                self._segment_path = lambda: "details"

            def __setattr__(self, name, value):
                self._perform_setattr(VirtualServices.VirtualService.Details, ['state', 'activated_profile_name', 'guest_interface'], name, value)


            class PackageInformation(Entity):
                """
                Details of the package for the virtual\-service.
                
                .. attribute:: name
                
                	Name of the package for the virtual\-service
                	**type**\: str
                
                .. attribute:: path
                
                	Path to the package
                	**type**\: str
                
                .. attribute:: application
                
                	Details of the application
                	**type**\:  :py:class:`Application <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.PackageInformation.Application>`
                
                .. attribute:: signing
                
                	Details of the key signing
                	**type**\:  :py:class:`Signing <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.PackageInformation.Signing>`
                
                .. attribute:: licensing
                
                	Details about the license
                	**type**\:  :py:class:`Licensing <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.PackageInformation.Licensing>`
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(VirtualServices.VirtualService.Details.PackageInformation, self).__init__()

                    self.yang_name = "package-information"
                    self.yang_parent_name = "details"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"application" : ("application", VirtualServices.VirtualService.Details.PackageInformation.Application), "signing" : ("signing", VirtualServices.VirtualService.Details.PackageInformation.Signing), "licensing" : ("licensing", VirtualServices.VirtualService.Details.PackageInformation.Licensing)}
                    self._child_list_classes = {}

                    self.name = YLeaf(YType.str, "name")

                    self.path = YLeaf(YType.str, "path")

                    self.application = VirtualServices.VirtualService.Details.PackageInformation.Application()
                    self.application.parent = self
                    self._children_name_map["application"] = "application"
                    self._children_yang_names.add("application")

                    self.signing = VirtualServices.VirtualService.Details.PackageInformation.Signing()
                    self.signing.parent = self
                    self._children_name_map["signing"] = "signing"
                    self._children_yang_names.add("signing")

                    self.licensing = VirtualServices.VirtualService.Details.PackageInformation.Licensing()
                    self.licensing.parent = self
                    self._children_name_map["licensing"] = "licensing"
                    self._children_yang_names.add("licensing")
                    self._segment_path = lambda: "package-information"

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualServices.VirtualService.Details.PackageInformation, ['name', 'path'], name, value)


                class Application(Entity):
                    """
                    Details of the application.
                    
                    .. attribute:: name
                    
                    	Name of the application
                    	**type**\: str
                    
                    .. attribute:: installed_version
                    
                    	Version of the application
                    	**type**\: str
                    
                    .. attribute:: description
                    
                    	Description of the application
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'virtual-service-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(VirtualServices.VirtualService.Details.PackageInformation.Application, self).__init__()

                        self.yang_name = "application"
                        self.yang_parent_name = "package-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.name = YLeaf(YType.str, "name")

                        self.installed_version = YLeaf(YType.str, "installed-version")

                        self.description = YLeaf(YType.str, "description")
                        self._segment_path = lambda: "application"

                    def __setattr__(self, name, value):
                        self._perform_setattr(VirtualServices.VirtualService.Details.PackageInformation.Application, ['name', 'installed_version', 'description'], name, value)


                class Signing(Entity):
                    """
                    Details of the key signing.
                    
                    .. attribute:: key_type
                    
                    	The Type of the signed key
                    	**type**\: str
                    
                    .. attribute:: method
                    
                    	The method the key was signed
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'virtual-service-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(VirtualServices.VirtualService.Details.PackageInformation.Signing, self).__init__()

                        self.yang_name = "signing"
                        self.yang_parent_name = "package-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.key_type = YLeaf(YType.str, "key-type")

                        self.method = YLeaf(YType.str, "method")
                        self._segment_path = lambda: "signing"

                    def __setattr__(self, name, value):
                        self._perform_setattr(VirtualServices.VirtualService.Details.PackageInformation.Signing, ['key_type', 'method'], name, value)


                class Licensing(Entity):
                    """
                    Details about the license.
                    
                    .. attribute:: name
                    
                    	The name of the license
                    	**type**\: str
                    
                    .. attribute:: version
                    
                    	The version of the license
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'virtual-service-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(VirtualServices.VirtualService.Details.PackageInformation.Licensing, self).__init__()

                        self.yang_name = "licensing"
                        self.yang_parent_name = "package-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.name = YLeaf(YType.str, "name")

                        self.version = YLeaf(YType.str, "version")
                        self._segment_path = lambda: "licensing"

                    def __setattr__(self, name, value):
                        self._perform_setattr(VirtualServices.VirtualService.Details.PackageInformation.Licensing, ['name', 'version'], name, value)


            class DetailedGuestStatus(Entity):
                """
                Details on the guest status.
                
                .. attribute:: processes
                
                	All the processes
                	**type**\:  :py:class:`Processes <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.DetailedGuestStatus.Processes>`
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(VirtualServices.VirtualService.Details.DetailedGuestStatus, self).__init__()

                    self.yang_name = "detailed-guest-status"
                    self.yang_parent_name = "details"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"processes" : ("processes", VirtualServices.VirtualService.Details.DetailedGuestStatus.Processes)}
                    self._child_list_classes = {}

                    self.processes = VirtualServices.VirtualService.Details.DetailedGuestStatus.Processes()
                    self.processes.parent = self
                    self._children_name_map["processes"] = "processes"
                    self._children_yang_names.add("processes")
                    self._segment_path = lambda: "detailed-guest-status"


                class Processes(Entity):
                    """
                    All the processes.
                    
                    .. attribute:: name
                    
                    	Name of the proccess
                    	**type**\: str
                    
                    .. attribute:: status
                    
                    	Status of the proccess
                    	**type**\: str
                    
                    .. attribute:: pid
                    
                    	Process ID
                    	**type**\: str
                    
                    .. attribute:: uptime
                    
                    	Up time of the proccess
                    	**type**\: str
                    
                    .. attribute:: memory
                    
                    	Memory of the proccess
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'virtual-service-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(VirtualServices.VirtualService.Details.DetailedGuestStatus.Processes, self).__init__()

                        self.yang_name = "processes"
                        self.yang_parent_name = "detailed-guest-status"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.name = YLeaf(YType.str, "name")

                        self.status = YLeaf(YType.str, "status")

                        self.pid = YLeaf(YType.str, "pid")

                        self.uptime = YLeaf(YType.str, "uptime")

                        self.memory = YLeaf(YType.str, "memory")
                        self._segment_path = lambda: "processes"

                    def __setattr__(self, name, value):
                        self._perform_setattr(VirtualServices.VirtualService.Details.DetailedGuestStatus.Processes, ['name', 'status', 'pid', 'uptime', 'memory'], name, value)


            class ResourceReservation(Entity):
                """
                Details of the resources reserved for this virtual service.
                
                .. attribute:: disk
                
                	The amount of reserverd disk space in MB
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: memory
                
                	The amount of reserved memory in MB
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: cpu
                
                	The percentage of reserved cpu
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(VirtualServices.VirtualService.Details.ResourceReservation, self).__init__()

                    self.yang_name = "resource-reservation"
                    self.yang_parent_name = "details"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.disk = YLeaf(YType.uint64, "disk")

                    self.memory = YLeaf(YType.uint64, "memory")

                    self.cpu = YLeaf(YType.uint64, "cpu")
                    self._segment_path = lambda: "resource-reservation"

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualServices.VirtualService.Details.ResourceReservation, ['disk', 'memory', 'cpu'], name, value)


            class ResourceAdmission(Entity):
                """
                Resources being allocated for the virtual\-service.
                
                .. attribute:: state
                
                	Thes status the of the resource allocation
                	**type**\: str
                
                .. attribute:: disk_space
                
                	The amount of disk space being allocated for the virtual\-service
                	**type**\: str
                
                .. attribute:: memory
                
                	The amount of memory being allocated for the virtual\-service
                	**type**\: str
                
                .. attribute:: cpu
                
                	The percentage of cpu being allocated for the virtual\-service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: vcpus
                
                	The amount of VCPUs being allocated for the virtual\-service
                	**type**\: str
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(VirtualServices.VirtualService.Details.ResourceAdmission, self).__init__()

                    self.yang_name = "resource-admission"
                    self.yang_parent_name = "details"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.state = YLeaf(YType.str, "state")

                    self.disk_space = YLeaf(YType.str, "disk-space")

                    self.memory = YLeaf(YType.str, "memory")

                    self.cpu = YLeaf(YType.uint64, "cpu")

                    self.vcpus = YLeaf(YType.str, "vcpus")
                    self._segment_path = lambda: "resource-admission"

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualServices.VirtualService.Details.ResourceAdmission, ['state', 'disk_space', 'memory', 'cpu', 'vcpus'], name, value)


        class Utilization(Entity):
            """
            Utilization of device resources for a virtual\-service.
            
            .. attribute:: name
            
            	The name of the virtual service
            	**type**\: str
            
            .. attribute:: cpu_util
            
            	Details on the CPU utilization for the virtual\-service
            	**type**\:  :py:class:`CpuUtil <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Utilization.CpuUtil>`
            
            .. attribute:: memory_util
            
            	Details on the memory usage for the virtual\-service
            	**type**\:  :py:class:`MemoryUtil <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Utilization.MemoryUtil>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(VirtualServices.VirtualService.Utilization, self).__init__()

                self.yang_name = "utilization"
                self.yang_parent_name = "virtual-service"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {"cpu-util" : ("cpu_util", VirtualServices.VirtualService.Utilization.CpuUtil), "memory-util" : ("memory_util", VirtualServices.VirtualService.Utilization.MemoryUtil)}
                self._child_list_classes = {}

                self.name = YLeaf(YType.str, "name")

                self.cpu_util = VirtualServices.VirtualService.Utilization.CpuUtil()
                self.cpu_util.parent = self
                self._children_name_map["cpu_util"] = "cpu-util"
                self._children_yang_names.add("cpu-util")

                self.memory_util = VirtualServices.VirtualService.Utilization.MemoryUtil()
                self.memory_util.parent = self
                self._children_name_map["memory_util"] = "memory-util"
                self._children_yang_names.add("memory-util")
                self._segment_path = lambda: "utilization"

            def __setattr__(self, name, value):
                self._perform_setattr(VirtualServices.VirtualService.Utilization, ['name'], name, value)


            class CpuUtil(Entity):
                """
                Details on the CPU utilization for the virtual\-service.
                
                .. attribute:: requested_application_util
                
                	Percentage of requested CPU utilization by the virtual\-service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: actual_application_util
                
                	Percetnage of CPU actual utilization for the virtual\-service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: cpu_state
                
                	The state of the CPU utilization for the virtual\-service
                	**type**\: str
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(VirtualServices.VirtualService.Utilization.CpuUtil, self).__init__()

                    self.yang_name = "cpu-util"
                    self.yang_parent_name = "utilization"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.requested_application_util = YLeaf(YType.uint64, "requested-application-util")

                    self.actual_application_util = YLeaf(YType.uint64, "actual-application-util")

                    self.cpu_state = YLeaf(YType.str, "cpu-state")
                    self._segment_path = lambda: "cpu-util"

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualServices.VirtualService.Utilization.CpuUtil, ['requested_application_util', 'actual_application_util', 'cpu_state'], name, value)


            class MemoryUtil(Entity):
                """
                Details on the memory usage for the virtual\-service.
                
                .. attribute:: memory_allocation
                
                	Amount of memory being allocated for the virtual\-service in KB
                	**type**\: str
                
                .. attribute:: memory_used
                
                	Amount of memory being used for the virtual\-service in KB
                	**type**\: str
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(VirtualServices.VirtualService.Utilization.MemoryUtil, self).__init__()

                    self.yang_name = "memory-util"
                    self.yang_parent_name = "utilization"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.memory_allocation = YLeaf(YType.str, "memory-allocation")

                    self.memory_used = YLeaf(YType.str, "memory-used")
                    self._segment_path = lambda: "memory-util"

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualServices.VirtualService.Utilization.MemoryUtil, ['memory_allocation', 'memory_used'], name, value)


        class NetworkUtils(Entity):
            """
            list of the network utilizations for the virtual\-service.
            
            .. attribute:: network_util
            
            	Details on a network utilization for the virtual\-service
            	**type**\: list of  		 :py:class:`NetworkUtil <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.NetworkUtils.NetworkUtil>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(VirtualServices.VirtualService.NetworkUtils, self).__init__()

                self.yang_name = "network-utils"
                self.yang_parent_name = "virtual-service"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"network-util" : ("network_util", VirtualServices.VirtualService.NetworkUtils.NetworkUtil)}

                self.network_util = YList(self)
                self._segment_path = lambda: "network-utils"

            def __setattr__(self, name, value):
                self._perform_setattr(VirtualServices.VirtualService.NetworkUtils, [], name, value)


            class NetworkUtil(Entity):
                """
                Details on a network utilization for the virtual\-service.
                
                .. attribute:: name  <key>
                
                	The name of the network that is being used for the virtual\-service
                	**type**\: str
                
                .. attribute:: alias  <key>
                
                	The alias of the network that is being used for the virtual\-service
                	**type**\: str
                
                .. attribute:: rx_packets
                
                	The number of rx packets being utilized for the virtual\-service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_bytes
                
                	The number of rx bytes being utilized for the virtual\-service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_errors
                
                	The number of rx errors
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_packets
                
                	The number of tx packets being utilized for the virtual\-service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_bytes
                
                	The number of tx bytes being utilized for the virtual\-service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_errors
                
                	The number of tx errors
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(VirtualServices.VirtualService.NetworkUtils.NetworkUtil, self).__init__()

                    self.yang_name = "network-util"
                    self.yang_parent_name = "network-utils"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.name = YLeaf(YType.str, "name")

                    self.alias = YLeaf(YType.str, "alias")

                    self.rx_packets = YLeaf(YType.uint64, "rx-packets")

                    self.rx_bytes = YLeaf(YType.uint64, "rx-bytes")

                    self.rx_errors = YLeaf(YType.uint64, "rx-errors")

                    self.tx_packets = YLeaf(YType.uint64, "tx-packets")

                    self.tx_bytes = YLeaf(YType.uint64, "tx-bytes")

                    self.tx_errors = YLeaf(YType.uint64, "tx-errors")
                    self._segment_path = lambda: "network-util" + "[name='" + self.name.get() + "']" + "[alias='" + self.alias.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualServices.VirtualService.NetworkUtils.NetworkUtil, ['name', 'alias', 'rx_packets', 'rx_bytes', 'rx_errors', 'tx_packets', 'tx_bytes', 'tx_errors'], name, value)


        class StorageUtils(Entity):
            """
            List of the storage utilizations for the virtual\-service.
            
            .. attribute:: storage_util
            
            	Details on a storage utilization for the virtual\-service
            	**type**\: list of  		 :py:class:`StorageUtil <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.StorageUtils.StorageUtil>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(VirtualServices.VirtualService.StorageUtils, self).__init__()

                self.yang_name = "storage-utils"
                self.yang_parent_name = "virtual-service"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"storage-util" : ("storage_util", VirtualServices.VirtualService.StorageUtils.StorageUtil)}

                self.storage_util = YList(self)
                self._segment_path = lambda: "storage-utils"

            def __setattr__(self, name, value):
                self._perform_setattr(VirtualServices.VirtualService.StorageUtils, [], name, value)


            class StorageUtil(Entity):
                """
                Details on a storage utilization for the virtual\-service.
                
                .. attribute:: name  <key>
                
                	The name of the storage process being used for the virtual\-service
                	**type**\: str
                
                .. attribute:: alias  <key>
                
                	The alias of the storage process being used for the virtual\-service
                	**type**\: str
                
                .. attribute:: rd_bytes
                
                	The number of RD bytes being used for the virtual\-service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rd_requests
                
                	The number of rd requests being used for the virtual\-service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: errors
                
                	The name of errors on the storage process
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wr_bytes
                
                	The number of WR bytes for the virtual\-service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wr_requests
                
                	The number of WR requests for the virtual\-service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: capacity
                
                	The storage capactity in 1K blocks
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: available
                
                	The available storage in 1K blocks
                	**type**\: str
                
                .. attribute:: used
                
                	The number of 1K blocks being used
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: usage
                
                	The percetage of storage capactiy being used
                	**type**\: str
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(VirtualServices.VirtualService.StorageUtils.StorageUtil, self).__init__()

                    self.yang_name = "storage-util"
                    self.yang_parent_name = "storage-utils"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.name = YLeaf(YType.str, "name")

                    self.alias = YLeaf(YType.str, "alias")

                    self.rd_bytes = YLeaf(YType.uint64, "rd-bytes")

                    self.rd_requests = YLeaf(YType.uint64, "rd-requests")

                    self.errors = YLeaf(YType.uint64, "errors")

                    self.wr_bytes = YLeaf(YType.uint64, "wr-bytes")

                    self.wr_requests = YLeaf(YType.uint64, "wr-requests")

                    self.capacity = YLeaf(YType.uint64, "capacity")

                    self.available = YLeaf(YType.str, "available")

                    self.used = YLeaf(YType.uint64, "used")

                    self.usage = YLeaf(YType.str, "usage")
                    self._segment_path = lambda: "storage-util" + "[name='" + self.name.get() + "']" + "[alias='" + self.alias.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualServices.VirtualService.StorageUtils.StorageUtil, ['name', 'alias', 'rd_bytes', 'rd_requests', 'errors', 'wr_bytes', 'wr_requests', 'capacity', 'available', 'used', 'usage'], name, value)


        class AttachedDevices(Entity):
            """
            Details for the devices attached to this virtual service.
            
            .. attribute:: attached_device
            
            	List of attached devices
            	**type**\: list of  		 :py:class:`AttachedDevice <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.AttachedDevices.AttachedDevice>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(VirtualServices.VirtualService.AttachedDevices, self).__init__()

                self.yang_name = "attached-devices"
                self.yang_parent_name = "virtual-service"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"attached-device" : ("attached_device", VirtualServices.VirtualService.AttachedDevices.AttachedDevice)}

                self.attached_device = YList(self)
                self._segment_path = lambda: "attached-devices"

            def __setattr__(self, name, value):
                self._perform_setattr(VirtualServices.VirtualService.AttachedDevices, [], name, value)


            class AttachedDevice(Entity):
                """
                List of attached devices.
                
                .. attribute:: name  <key>
                
                	The name of the attached device
                	**type**\: str
                
                .. attribute:: type
                
                	The type of the attached device
                	**type**\: str
                
                .. attribute:: alias
                
                	The alias for the attached device
                	**type**\: str
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(VirtualServices.VirtualService.AttachedDevices.AttachedDevice, self).__init__()

                    self.yang_name = "attached-device"
                    self.yang_parent_name = "attached-devices"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.name = YLeaf(YType.str, "name")

                    self.type = YLeaf(YType.str, "type")

                    self.alias = YLeaf(YType.str, "alias")
                    self._segment_path = lambda: "attached-device" + "[name='" + self.name.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualServices.VirtualService.AttachedDevices.AttachedDevice, ['name', 'type', 'alias'], name, value)


        class NetworkInterfaces(Entity):
            """
            Details for the network interfaces.
            
            .. attribute:: network_interface
            
            	Details for a network interface
            	**type**\: list of  		 :py:class:`NetworkInterface <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.NetworkInterfaces.NetworkInterface>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(VirtualServices.VirtualService.NetworkInterfaces, self).__init__()

                self.yang_name = "network-interfaces"
                self.yang_parent_name = "virtual-service"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"network-interface" : ("network_interface", VirtualServices.VirtualService.NetworkInterfaces.NetworkInterface)}

                self.network_interface = YList(self)
                self._segment_path = lambda: "network-interfaces"

            def __setattr__(self, name, value):
                self._perform_setattr(VirtualServices.VirtualService.NetworkInterfaces, [], name, value)


            class NetworkInterface(Entity):
                """
                Details for a network interface.
                
                .. attribute:: mac_address  <key>
                
                	The MAC address for the network interface
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: attached_interface
                
                	Name of the the attached interface
                	**type**\: str
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(VirtualServices.VirtualService.NetworkInterfaces.NetworkInterface, self).__init__()

                    self.yang_name = "network-interface"
                    self.yang_parent_name = "network-interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.mac_address = YLeaf(YType.str, "mac-address")

                    self.attached_interface = YLeaf(YType.str, "attached-interface")
                    self._segment_path = lambda: "network-interface" + "[mac-address='" + self.mac_address.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualServices.VirtualService.NetworkInterfaces.NetworkInterface, ['mac_address', 'attached_interface'], name, value)


        class GuestRoutes(Entity):
            """
            Routes for the guest interface.
            
            .. attribute:: guest_route
            
            	List of guest routes for a guest interface
            	**type**\: list of  		 :py:class:`GuestRoute <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.GuestRoutes.GuestRoute>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(VirtualServices.VirtualService.GuestRoutes, self).__init__()

                self.yang_name = "guest-routes"
                self.yang_parent_name = "virtual-service"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"guest-route" : ("guest_route", VirtualServices.VirtualService.GuestRoutes.GuestRoute)}

                self.guest_route = YList(self)
                self._segment_path = lambda: "guest-routes"

            def __setattr__(self, name, value):
                self._perform_setattr(VirtualServices.VirtualService.GuestRoutes, [], name, value)


            class GuestRoute(Entity):
                """
                List of guest routes for a guest interface.
                
                .. attribute:: route  <key>
                
                	A guest route for a guest interface
                	**type**\: str
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(VirtualServices.VirtualService.GuestRoutes.GuestRoute, self).__init__()

                    self.yang_name = "guest-route"
                    self.yang_parent_name = "guest-routes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.route = YLeaf(YType.str, "route")
                    self._segment_path = lambda: "guest-route" + "[route='" + self.route.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualServices.VirtualService.GuestRoutes.GuestRoute, ['route'], name, value)

    def clone_ptr(self):
        self._top_entity = VirtualServices()
        return self._top_entity


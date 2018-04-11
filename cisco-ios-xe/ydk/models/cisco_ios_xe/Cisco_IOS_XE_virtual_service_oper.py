""" Cisco_IOS_XE_virtual_service_oper 

This module contains a collection of YANG definitions for
monitoring virtual services in a Network Element.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class VirtualServices(Entity):
    """
    Information on all virtual services
    
    .. attribute:: virtual_service
    
    	List of virtual services
    	**type**\: list of  		 :py:class:`VirtualService <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService>`
    
    

    """

    _prefix = 'virtual-service-ios-xe-oper'
    _revision = '2017-09-25'

    def __init__(self):
        super(VirtualServices, self).__init__()
        self._top_entity = None

        self.yang_name = "virtual-services"
        self.yang_parent_name = "Cisco-IOS-XE-virtual-service-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("virtual-service", ("virtual_service", VirtualServices.VirtualService))])
        self._leafs = OrderedDict()

        self.virtual_service = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-virtual-service-oper:virtual-services"

    def __setattr__(self, name, value):
        self._perform_setattr(VirtualServices, [], name, value)


    class VirtualService(Entity):
        """
        List of virtual services
        
        .. attribute:: name  (key)
        
        	Virtual service name
        	**type**\: str
        
        .. attribute:: details
        
        	Virtual service details
        	**type**\:  :py:class:`Details <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details>`
        
        .. attribute:: utilization
        
        	Virtual service resource utilization details
        	**type**\:  :py:class:`Utilization <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Utilization>`
        
        .. attribute:: network_utils
        
        	Virtual service network utilization details
        	**type**\:  :py:class:`NetworkUtils <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.NetworkUtils>`
        
        .. attribute:: storage_utils
        
        	Virtual service storage utilization details
        	**type**\:  :py:class:`StorageUtils <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.StorageUtils>`
        
        .. attribute:: processes
        
        	Virtual service process details
        	**type**\:  :py:class:`Processes <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Processes>`
        
        .. attribute:: attached_devices
        
        	Virtual service attached device details
        	**type**\:  :py:class:`AttachedDevices <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.AttachedDevices>`
        
        .. attribute:: network_interfaces
        
        	Virtual service network interface details
        	**type**\:  :py:class:`NetworkInterfaces <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.NetworkInterfaces>`
        
        .. attribute:: guest_routes
        
        	Virtual service guest route details
        	**type**\:  :py:class:`GuestRoutes <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.GuestRoutes>`
        
        

        """

        _prefix = 'virtual-service-ios-xe-oper'
        _revision = '2017-09-25'

        def __init__(self):
            super(VirtualServices.VirtualService, self).__init__()

            self.yang_name = "virtual-service"
            self.yang_parent_name = "virtual-services"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_container_classes = OrderedDict([("details", ("details", VirtualServices.VirtualService.Details)), ("utilization", ("utilization", VirtualServices.VirtualService.Utilization)), ("network-utils", ("network_utils", VirtualServices.VirtualService.NetworkUtils)), ("storage-utils", ("storage_utils", VirtualServices.VirtualService.StorageUtils)), ("processes", ("processes", VirtualServices.VirtualService.Processes)), ("attached-devices", ("attached_devices", VirtualServices.VirtualService.AttachedDevices)), ("network-interfaces", ("network_interfaces", VirtualServices.VirtualService.NetworkInterfaces)), ("guest-routes", ("guest_routes", VirtualServices.VirtualService.GuestRoutes))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('name', YLeaf(YType.str, 'name')),
            ])
            self.name = None

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

            self.processes = VirtualServices.VirtualService.Processes()
            self.processes.parent = self
            self._children_name_map["processes"] = "processes"
            self._children_yang_names.add("processes")

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
            self._segment_path = lambda: "virtual-service" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-virtual-service-oper:virtual-services/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(VirtualServices.VirtualService, ['name'], name, value)


        class Details(Entity):
            """
            Virtual service details
            
            .. attribute:: state
            
            	State of the virtual service
            	**type**\: str
            
            .. attribute:: package_information
            
            	Virtual service packaging information
            	**type**\:  :py:class:`PackageInformation <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.PackageInformation>`
            
            .. attribute:: detailed_guest_status
            
            	Guest status details
            	**type**\:  :py:class:`DetailedGuestStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.DetailedGuestStatus>`
            
            .. attribute:: activated_profile_name
            
            	Activated profile name
            	**type**\: str
            
            .. attribute:: resource_reservation
            
            	Resource reservation details
            	**type**\:  :py:class:`ResourceReservation <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.ResourceReservation>`
            
            .. attribute:: guest_interface
            
            	Guest interface name
            	**type**\: str
            
            .. attribute:: resource_admission
            
            	Resources allocated for the virtual service
            	**type**\:  :py:class:`ResourceAdmission <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.ResourceAdmission>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-09-25'

            def __init__(self):
                super(VirtualServices.VirtualService.Details, self).__init__()

                self.yang_name = "details"
                self.yang_parent_name = "virtual-service"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("package-information", ("package_information", VirtualServices.VirtualService.Details.PackageInformation)), ("detailed-guest-status", ("detailed_guest_status", VirtualServices.VirtualService.Details.DetailedGuestStatus)), ("resource-reservation", ("resource_reservation", VirtualServices.VirtualService.Details.ResourceReservation)), ("resource-admission", ("resource_admission", VirtualServices.VirtualService.Details.ResourceAdmission))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('state', YLeaf(YType.str, 'state')),
                    ('activated_profile_name', YLeaf(YType.str, 'activated-profile-name')),
                    ('guest_interface', YLeaf(YType.str, 'guest-interface')),
                ])
                self.state = None
                self.activated_profile_name = None
                self.guest_interface = None

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
                Virtual service packaging information
                
                .. attribute:: name
                
                	Package name
                	**type**\: str
                
                .. attribute:: path
                
                	Package path
                	**type**\: str
                
                .. attribute:: application
                
                	Application details
                	**type**\:  :py:class:`Application <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.PackageInformation.Application>`
                
                .. attribute:: signing
                
                	Key signing details
                	**type**\:  :py:class:`Signing <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.PackageInformation.Signing>`
                
                .. attribute:: licensing
                
                	Licensing details
                	**type**\:  :py:class:`Licensing <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.PackageInformation.Licensing>`
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(VirtualServices.VirtualService.Details.PackageInformation, self).__init__()

                    self.yang_name = "package-information"
                    self.yang_parent_name = "details"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("application", ("application", VirtualServices.VirtualService.Details.PackageInformation.Application)), ("signing", ("signing", VirtualServices.VirtualService.Details.PackageInformation.Signing)), ("licensing", ("licensing", VirtualServices.VirtualService.Details.PackageInformation.Licensing))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                        ('path', YLeaf(YType.str, 'path')),
                    ])
                    self.name = None
                    self.path = None

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
                    Application details
                    
                    .. attribute:: name
                    
                    	Application name
                    	**type**\: str
                    
                    .. attribute:: installed_version
                    
                    	Application version
                    	**type**\: str
                    
                    .. attribute:: description
                    
                    	Application description
                    	**type**\: str
                    
                    .. attribute:: type
                    
                    	Application type
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'virtual-service-ios-xe-oper'
                    _revision = '2017-09-25'

                    def __init__(self):
                        super(VirtualServices.VirtualService.Details.PackageInformation.Application, self).__init__()

                        self.yang_name = "application"
                        self.yang_parent_name = "package-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', YLeaf(YType.str, 'name')),
                            ('installed_version', YLeaf(YType.str, 'installed-version')),
                            ('description', YLeaf(YType.str, 'description')),
                            ('type', YLeaf(YType.str, 'type')),
                        ])
                        self.name = None
                        self.installed_version = None
                        self.description = None
                        self.type = None
                        self._segment_path = lambda: "application"

                    def __setattr__(self, name, value):
                        self._perform_setattr(VirtualServices.VirtualService.Details.PackageInformation.Application, ['name', 'installed_version', 'description', 'type'], name, value)


                class Signing(Entity):
                    """
                    Key signing details
                    
                    .. attribute:: key_type
                    
                    	Signed key type
                    	**type**\: str
                    
                    .. attribute:: method
                    
                    	Method the key was signed
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'virtual-service-ios-xe-oper'
                    _revision = '2017-09-25'

                    def __init__(self):
                        super(VirtualServices.VirtualService.Details.PackageInformation.Signing, self).__init__()

                        self.yang_name = "signing"
                        self.yang_parent_name = "package-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('key_type', YLeaf(YType.str, 'key-type')),
                            ('method', YLeaf(YType.str, 'method')),
                        ])
                        self.key_type = None
                        self.method = None
                        self._segment_path = lambda: "signing"

                    def __setattr__(self, name, value):
                        self._perform_setattr(VirtualServices.VirtualService.Details.PackageInformation.Signing, ['key_type', 'method'], name, value)


                class Licensing(Entity):
                    """
                    Licensing details
                    
                    .. attribute:: name
                    
                    	License name
                    	**type**\: str
                    
                    .. attribute:: version
                    
                    	License version
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'virtual-service-ios-xe-oper'
                    _revision = '2017-09-25'

                    def __init__(self):
                        super(VirtualServices.VirtualService.Details.PackageInformation.Licensing, self).__init__()

                        self.yang_name = "licensing"
                        self.yang_parent_name = "package-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', YLeaf(YType.str, 'name')),
                            ('version', YLeaf(YType.str, 'version')),
                        ])
                        self.name = None
                        self.version = None
                        self._segment_path = lambda: "licensing"

                    def __setattr__(self, name, value):
                        self._perform_setattr(VirtualServices.VirtualService.Details.PackageInformation.Licensing, ['name', 'version'], name, value)


            class DetailedGuestStatus(Entity):
                """
                Guest status details
                
                .. attribute:: processes
                
                	List of all processes
                	**type**\:  :py:class:`Processes <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.DetailedGuestStatus.Processes>`
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(VirtualServices.VirtualService.Details.DetailedGuestStatus, self).__init__()

                    self.yang_name = "detailed-guest-status"
                    self.yang_parent_name = "details"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("processes", ("processes", VirtualServices.VirtualService.Details.DetailedGuestStatus.Processes))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.processes = VirtualServices.VirtualService.Details.DetailedGuestStatus.Processes()
                    self.processes.parent = self
                    self._children_name_map["processes"] = "processes"
                    self._children_yang_names.add("processes")
                    self._segment_path = lambda: "detailed-guest-status"


                class Processes(Entity):
                    """
                    List of all processes
                    
                    .. attribute:: name
                    
                    	Process name
                    	**type**\: str
                    
                    .. attribute:: status
                    
                    	Process status
                    	**type**\: str
                    
                    .. attribute:: pid
                    
                    	Process ID
                    	**type**\: str
                    
                    .. attribute:: uptime
                    
                    	Process uptime
                    	**type**\: str
                    
                    .. attribute:: memory
                    
                    	Amount of process memory
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'virtual-service-ios-xe-oper'
                    _revision = '2017-09-25'

                    def __init__(self):
                        super(VirtualServices.VirtualService.Details.DetailedGuestStatus.Processes, self).__init__()

                        self.yang_name = "processes"
                        self.yang_parent_name = "detailed-guest-status"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', YLeaf(YType.str, 'name')),
                            ('status', YLeaf(YType.str, 'status')),
                            ('pid', YLeaf(YType.str, 'pid')),
                            ('uptime', YLeaf(YType.str, 'uptime')),
                            ('memory', YLeaf(YType.str, 'memory')),
                        ])
                        self.name = None
                        self.status = None
                        self.pid = None
                        self.uptime = None
                        self.memory = None
                        self._segment_path = lambda: "processes"

                    def __setattr__(self, name, value):
                        self._perform_setattr(VirtualServices.VirtualService.Details.DetailedGuestStatus.Processes, ['name', 'status', 'pid', 'uptime', 'memory'], name, value)


            class ResourceReservation(Entity):
                """
                Resource reservation details
                
                .. attribute:: disk
                
                	Amount of reserverd disk space in MB
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: memory
                
                	Amount of reserved memory in MB
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: cpu
                
                	Amount of reserved cpu in unit
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(VirtualServices.VirtualService.Details.ResourceReservation, self).__init__()

                    self.yang_name = "resource-reservation"
                    self.yang_parent_name = "details"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('disk', YLeaf(YType.uint64, 'disk')),
                        ('memory', YLeaf(YType.uint64, 'memory')),
                        ('cpu', YLeaf(YType.uint64, 'cpu')),
                    ])
                    self.disk = None
                    self.memory = None
                    self.cpu = None
                    self._segment_path = lambda: "resource-reservation"

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualServices.VirtualService.Details.ResourceReservation, ['disk', 'memory', 'cpu'], name, value)


            class ResourceAdmission(Entity):
                """
                Resources allocated for the virtual service
                
                .. attribute:: state
                
                	Status of the resource allocation
                	**type**\: str
                
                .. attribute:: disk_space
                
                	Amount of disk space allocated for the virtual service in MB
                	**type**\: str
                
                .. attribute:: memory
                
                	Amount of memory allocated for the virtual service in MB
                	**type**\: str
                
                .. attribute:: cpu
                
                	Percentage of cpu allocated for the virtual\-service in unit
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: vcpus
                
                	Amount of VCPUs allocated for the virtual service
                	**type**\: str
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(VirtualServices.VirtualService.Details.ResourceAdmission, self).__init__()

                    self.yang_name = "resource-admission"
                    self.yang_parent_name = "details"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('state', YLeaf(YType.str, 'state')),
                        ('disk_space', YLeaf(YType.str, 'disk-space')),
                        ('memory', YLeaf(YType.str, 'memory')),
                        ('cpu', YLeaf(YType.uint64, 'cpu')),
                        ('vcpus', YLeaf(YType.str, 'vcpus')),
                    ])
                    self.state = None
                    self.disk_space = None
                    self.memory = None
                    self.cpu = None
                    self.vcpus = None
                    self._segment_path = lambda: "resource-admission"

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualServices.VirtualService.Details.ResourceAdmission, ['state', 'disk_space', 'memory', 'cpu', 'vcpus'], name, value)


        class Utilization(Entity):
            """
            Virtual service resource utilization details
            
            .. attribute:: name
            
            	Name of the virtual service
            	**type**\: str
            
            .. attribute:: cpu_util
            
            	CPU utilization information
            	**type**\:  :py:class:`CpuUtil <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Utilization.CpuUtil>`
            
            .. attribute:: memory_util
            
            	Memory utilization information
            	**type**\:  :py:class:`MemoryUtil <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Utilization.MemoryUtil>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-09-25'

            def __init__(self):
                super(VirtualServices.VirtualService.Utilization, self).__init__()

                self.yang_name = "utilization"
                self.yang_parent_name = "virtual-service"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("cpu-util", ("cpu_util", VirtualServices.VirtualService.Utilization.CpuUtil)), ("memory-util", ("memory_util", VirtualServices.VirtualService.Utilization.MemoryUtil))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', YLeaf(YType.str, 'name')),
                ])
                self.name = None

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
                CPU utilization information
                
                .. attribute:: requested_application_util
                
                	Amount of requested CPU utilization by the virtual service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: actual_application_util
                
                	Percetnage of CPU actual utilization for the virtual service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: cpu_state
                
                	State of the CPU utilization for the virtual\-service
                	**type**\: str
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(VirtualServices.VirtualService.Utilization.CpuUtil, self).__init__()

                    self.yang_name = "cpu-util"
                    self.yang_parent_name = "utilization"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('requested_application_util', YLeaf(YType.uint64, 'requested-application-util')),
                        ('actual_application_util', YLeaf(YType.uint64, 'actual-application-util')),
                        ('cpu_state', YLeaf(YType.str, 'cpu-state')),
                    ])
                    self.requested_application_util = None
                    self.actual_application_util = None
                    self.cpu_state = None
                    self._segment_path = lambda: "cpu-util"

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualServices.VirtualService.Utilization.CpuUtil, ['requested_application_util', 'actual_application_util', 'cpu_state'], name, value)


            class MemoryUtil(Entity):
                """
                Memory utilization information
                
                .. attribute:: memory_allocation
                
                	Amount of memory allocated for the virtual service in MB
                	**type**\: str
                
                .. attribute:: memory_used
                
                	Amount of used memory for the virtual service in KB
                	**type**\: str
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(VirtualServices.VirtualService.Utilization.MemoryUtil, self).__init__()

                    self.yang_name = "memory-util"
                    self.yang_parent_name = "utilization"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('memory_allocation', YLeaf(YType.str, 'memory-allocation')),
                        ('memory_used', YLeaf(YType.str, 'memory-used')),
                    ])
                    self.memory_allocation = None
                    self.memory_used = None
                    self._segment_path = lambda: "memory-util"

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualServices.VirtualService.Utilization.MemoryUtil, ['memory_allocation', 'memory_used'], name, value)


        class NetworkUtils(Entity):
            """
            Virtual service network utilization details
            
            .. attribute:: network_util
            
            	A list of network utilization details
            	**type**\: list of  		 :py:class:`NetworkUtil <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.NetworkUtils.NetworkUtil>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-09-25'

            def __init__(self):
                super(VirtualServices.VirtualService.NetworkUtils, self).__init__()

                self.yang_name = "network-utils"
                self.yang_parent_name = "virtual-service"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("network-util", ("network_util", VirtualServices.VirtualService.NetworkUtils.NetworkUtil))])
                self._leafs = OrderedDict()

                self.network_util = YList(self)
                self._segment_path = lambda: "network-utils"

            def __setattr__(self, name, value):
                self._perform_setattr(VirtualServices.VirtualService.NetworkUtils, [], name, value)


            class NetworkUtil(Entity):
                """
                A list of network utilization details
                
                .. attribute:: name  (key)
                
                	Name of the network used for the virtual service
                	**type**\: str
                
                .. attribute:: alias
                
                	Alias of the network used by the virtual service
                	**type**\: str
                
                .. attribute:: rx_packets
                
                	Number of packets received by the virtual service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_bytes
                
                	Number of octets received by the virtual service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_errors
                
                	Number of RX errors by the virtual service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_packets
                
                	Number of packets transmitted by the virtual service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_bytes
                
                	Number of octets transmitted by the virtual service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_errors
                
                	Number of TX errors by the virtual service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(VirtualServices.VirtualService.NetworkUtils.NetworkUtil, self).__init__()

                    self.yang_name = "network-util"
                    self.yang_parent_name = "network-utils"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['name']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                        ('alias', YLeaf(YType.str, 'alias')),
                        ('rx_packets', YLeaf(YType.uint64, 'rx-packets')),
                        ('rx_bytes', YLeaf(YType.uint64, 'rx-bytes')),
                        ('rx_errors', YLeaf(YType.uint64, 'rx-errors')),
                        ('tx_packets', YLeaf(YType.uint64, 'tx-packets')),
                        ('tx_bytes', YLeaf(YType.uint64, 'tx-bytes')),
                        ('tx_errors', YLeaf(YType.uint64, 'tx-errors')),
                    ])
                    self.name = None
                    self.alias = None
                    self.rx_packets = None
                    self.rx_bytes = None
                    self.rx_errors = None
                    self.tx_packets = None
                    self.tx_bytes = None
                    self.tx_errors = None
                    self._segment_path = lambda: "network-util" + "[name='" + str(self.name) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualServices.VirtualService.NetworkUtils.NetworkUtil, ['name', 'alias', 'rx_packets', 'rx_bytes', 'rx_errors', 'tx_packets', 'tx_bytes', 'tx_errors'], name, value)


        class StorageUtils(Entity):
            """
            Virtual service storage utilization details
            
            .. attribute:: storage_util
            
            	List of storage utilization details
            	**type**\: list of  		 :py:class:`StorageUtil <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.StorageUtils.StorageUtil>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-09-25'

            def __init__(self):
                super(VirtualServices.VirtualService.StorageUtils, self).__init__()

                self.yang_name = "storage-utils"
                self.yang_parent_name = "virtual-service"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("storage-util", ("storage_util", VirtualServices.VirtualService.StorageUtils.StorageUtil))])
                self._leafs = OrderedDict()

                self.storage_util = YList(self)
                self._segment_path = lambda: "storage-utils"

            def __setattr__(self, name, value):
                self._perform_setattr(VirtualServices.VirtualService.StorageUtils, [], name, value)


            class StorageUtil(Entity):
                """
                List of storage utilization details
                
                .. attribute:: name  (key)
                
                	Name of the storage device used for the virtual service
                	**type**\: str
                
                .. attribute:: alias
                
                	Alias of the storage device used by the virtual service
                	**type**\: str
                
                .. attribute:: rd_bytes
                
                	Number of bytes read by the virtual service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rd_requests
                
                	Number of read requests made by the virtual service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: errors
                
                	Number of storage error seen by the virtual service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wr_bytes
                
                	Number of bytes written by the virtual service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wr_requests
                
                	Number of write requests made by the virtual service
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: capacity
                
                	Storage capactity in 1K blocks
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: available
                
                	Available storage in 1K blocks
                	**type**\: str
                
                .. attribute:: used
                
                	Used storage in 1K blocks
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: usage
                
                	Percetage of storage capactiy used by the virtual service
                	**type**\: str
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(VirtualServices.VirtualService.StorageUtils.StorageUtil, self).__init__()

                    self.yang_name = "storage-util"
                    self.yang_parent_name = "storage-utils"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['name']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                        ('alias', YLeaf(YType.str, 'alias')),
                        ('rd_bytes', YLeaf(YType.uint64, 'rd-bytes')),
                        ('rd_requests', YLeaf(YType.uint64, 'rd-requests')),
                        ('errors', YLeaf(YType.uint64, 'errors')),
                        ('wr_bytes', YLeaf(YType.uint64, 'wr-bytes')),
                        ('wr_requests', YLeaf(YType.uint64, 'wr-requests')),
                        ('capacity', YLeaf(YType.uint64, 'capacity')),
                        ('available', YLeaf(YType.str, 'available')),
                        ('used', YLeaf(YType.uint64, 'used')),
                        ('usage', YLeaf(YType.str, 'usage')),
                    ])
                    self.name = None
                    self.alias = None
                    self.rd_bytes = None
                    self.rd_requests = None
                    self.errors = None
                    self.wr_bytes = None
                    self.wr_requests = None
                    self.capacity = None
                    self.available = None
                    self.used = None
                    self.usage = None
                    self._segment_path = lambda: "storage-util" + "[name='" + str(self.name) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualServices.VirtualService.StorageUtils.StorageUtil, ['name', 'alias', 'rd_bytes', 'rd_requests', 'errors', 'wr_bytes', 'wr_requests', 'capacity', 'available', 'used', 'usage'], name, value)


        class Processes(Entity):
            """
            Virtual service process details
            
            .. attribute:: process
            
            	List of process details
            	**type**\: list of  		 :py:class:`Process <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Processes.Process>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-09-25'

            def __init__(self):
                super(VirtualServices.VirtualService.Processes, self).__init__()

                self.yang_name = "processes"
                self.yang_parent_name = "virtual-service"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("process", ("process", VirtualServices.VirtualService.Processes.Process))])
                self._leafs = OrderedDict()

                self.process = YList(self)
                self._segment_path = lambda: "processes"

            def __setattr__(self, name, value):
                self._perform_setattr(VirtualServices.VirtualService.Processes, [], name, value)


            class Process(Entity):
                """
                List of process details
                
                .. attribute:: name  (key)
                
                	Process name
                	**type**\: str
                
                .. attribute:: status
                
                	Process status
                	**type**\: str
                
                .. attribute:: pid
                
                	Process ID
                	**type**\: str
                
                .. attribute:: uptime
                
                	Process uptime
                	**type**\: str
                
                .. attribute:: memory
                
                	Amount of process memory
                	**type**\: str
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(VirtualServices.VirtualService.Processes.Process, self).__init__()

                    self.yang_name = "process"
                    self.yang_parent_name = "processes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['name']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                        ('status', YLeaf(YType.str, 'status')),
                        ('pid', YLeaf(YType.str, 'pid')),
                        ('uptime', YLeaf(YType.str, 'uptime')),
                        ('memory', YLeaf(YType.str, 'memory')),
                    ])
                    self.name = None
                    self.status = None
                    self.pid = None
                    self.uptime = None
                    self.memory = None
                    self._segment_path = lambda: "process" + "[name='" + str(self.name) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualServices.VirtualService.Processes.Process, ['name', 'status', 'pid', 'uptime', 'memory'], name, value)


        class AttachedDevices(Entity):
            """
            Virtual service attached device details
            
            .. attribute:: attached_device
            
            	A list of attached device details
            	**type**\: list of  		 :py:class:`AttachedDevice <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.AttachedDevices.AttachedDevice>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-09-25'

            def __init__(self):
                super(VirtualServices.VirtualService.AttachedDevices, self).__init__()

                self.yang_name = "attached-devices"
                self.yang_parent_name = "virtual-service"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("attached-device", ("attached_device", VirtualServices.VirtualService.AttachedDevices.AttachedDevice))])
                self._leafs = OrderedDict()

                self.attached_device = YList(self)
                self._segment_path = lambda: "attached-devices"

            def __setattr__(self, name, value):
                self._perform_setattr(VirtualServices.VirtualService.AttachedDevices, [], name, value)


            class AttachedDevice(Entity):
                """
                A list of attached device details
                
                .. attribute:: name  (key)
                
                	Attached device name
                	**type**\: str
                
                .. attribute:: type
                
                	Attached device type
                	**type**\: str
                
                .. attribute:: alias
                
                	Attached device alias
                	**type**\: str
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(VirtualServices.VirtualService.AttachedDevices.AttachedDevice, self).__init__()

                    self.yang_name = "attached-device"
                    self.yang_parent_name = "attached-devices"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['name']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                        ('type', YLeaf(YType.str, 'type')),
                        ('alias', YLeaf(YType.str, 'alias')),
                    ])
                    self.name = None
                    self.type = None
                    self.alias = None
                    self._segment_path = lambda: "attached-device" + "[name='" + str(self.name) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualServices.VirtualService.AttachedDevices.AttachedDevice, ['name', 'type', 'alias'], name, value)


        class NetworkInterfaces(Entity):
            """
            Virtual service network interface details
            
            .. attribute:: network_interface
            
            	A list of network interface details
            	**type**\: list of  		 :py:class:`NetworkInterface <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.NetworkInterfaces.NetworkInterface>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-09-25'

            def __init__(self):
                super(VirtualServices.VirtualService.NetworkInterfaces, self).__init__()

                self.yang_name = "network-interfaces"
                self.yang_parent_name = "virtual-service"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("network-interface", ("network_interface", VirtualServices.VirtualService.NetworkInterfaces.NetworkInterface))])
                self._leafs = OrderedDict()

                self.network_interface = YList(self)
                self._segment_path = lambda: "network-interfaces"

            def __setattr__(self, name, value):
                self._perform_setattr(VirtualServices.VirtualService.NetworkInterfaces, [], name, value)


            class NetworkInterface(Entity):
                """
                A list of network interface details
                
                .. attribute:: mac_address  (key)
                
                	MAC address for the network interface
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: attached_interface
                
                	Attached interface name
                	**type**\: str
                
                .. attribute:: ipv4_address
                
                	IPv4 address for the network interface
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(VirtualServices.VirtualService.NetworkInterfaces.NetworkInterface, self).__init__()

                    self.yang_name = "network-interface"
                    self.yang_parent_name = "network-interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['mac_address']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('mac_address', YLeaf(YType.str, 'mac-address')),
                        ('attached_interface', YLeaf(YType.str, 'attached-interface')),
                        ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                    ])
                    self.mac_address = None
                    self.attached_interface = None
                    self.ipv4_address = None
                    self._segment_path = lambda: "network-interface" + "[mac-address='" + str(self.mac_address) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualServices.VirtualService.NetworkInterfaces.NetworkInterface, ['mac_address', 'attached_interface', 'ipv4_address'], name, value)


        class GuestRoutes(Entity):
            """
            Virtual service guest route details
            
            .. attribute:: guest_route
            
            	List of guest routes for a guest interface
            	**type**\: list of  		 :py:class:`GuestRoute <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.GuestRoutes.GuestRoute>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-09-25'

            def __init__(self):
                super(VirtualServices.VirtualService.GuestRoutes, self).__init__()

                self.yang_name = "guest-routes"
                self.yang_parent_name = "virtual-service"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("guest-route", ("guest_route", VirtualServices.VirtualService.GuestRoutes.GuestRoute))])
                self._leafs = OrderedDict()

                self.guest_route = YList(self)
                self._segment_path = lambda: "guest-routes"

            def __setattr__(self, name, value):
                self._perform_setattr(VirtualServices.VirtualService.GuestRoutes, [], name, value)


            class GuestRoute(Entity):
                """
                List of guest routes for a guest interface
                
                .. attribute:: route  (key)
                
                	Guest route of the guest interface
                	**type**\: str
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(VirtualServices.VirtualService.GuestRoutes.GuestRoute, self).__init__()

                    self.yang_name = "guest-route"
                    self.yang_parent_name = "guest-routes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['route']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('route', YLeaf(YType.str, 'route')),
                    ])
                    self.route = None
                    self._segment_path = lambda: "guest-route" + "[route='" + str(self.route) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(VirtualServices.VirtualService.GuestRoutes.GuestRoute, ['route'], name, value)

    def clone_ptr(self):
        self._top_entity = VirtualServices()
        return self._top_entity


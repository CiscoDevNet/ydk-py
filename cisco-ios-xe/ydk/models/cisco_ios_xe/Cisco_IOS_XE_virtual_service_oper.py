""" Cisco_IOS_XE_virtual_service_oper 

This module contains a collection of YANG definitions for monitoring
virtual services in a Network Element.Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class VirtualServices(object):
    """
    Names and Status of virtual services on the device
    
    .. attribute:: virtual_service
    
    	A virtual service
    	**type**\: list of    :py:class:`VirtualService <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService>`
    
    

    """

    _prefix = 'virtual-service-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        self.virtual_service = YList()
        self.virtual_service.parent = self
        self.virtual_service.name = 'virtual_service'


    class VirtualService(object):
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
            self.parent = None
            self.name = None
            self.attached_devices = VirtualServices.VirtualService.AttachedDevices()
            self.attached_devices.parent = self
            self.details = VirtualServices.VirtualService.Details()
            self.details.parent = self
            self.guest_routes = VirtualServices.VirtualService.GuestRoutes()
            self.guest_routes.parent = self
            self.network_interfaces = VirtualServices.VirtualService.NetworkInterfaces()
            self.network_interfaces.parent = self
            self.network_utils = VirtualServices.VirtualService.NetworkUtils()
            self.network_utils.parent = self
            self.storage_utils = VirtualServices.VirtualService.StorageUtils()
            self.storage_utils.parent = self
            self.utilization = VirtualServices.VirtualService.Utilization()
            self.utilization.parent = self


        class Details(object):
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
                self.parent = None
                self.activated_profile_name = None
                self.detailed_guest_status = VirtualServices.VirtualService.Details.DetailedGuestStatus()
                self.detailed_guest_status.parent = self
                self.guest_interface = None
                self.package_information = VirtualServices.VirtualService.Details.PackageInformation()
                self.package_information.parent = self
                self.resource_admission = VirtualServices.VirtualService.Details.ResourceAdmission()
                self.resource_admission.parent = self
                self.resource_reservation = VirtualServices.VirtualService.Details.ResourceReservation()
                self.resource_reservation.parent = self
                self.state = None


            class PackageInformation(object):
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
                    self.parent = None
                    self.application = VirtualServices.VirtualService.Details.PackageInformation.Application()
                    self.application.parent = self
                    self.licensing = VirtualServices.VirtualService.Details.PackageInformation.Licensing()
                    self.licensing.parent = self
                    self.name = None
                    self.path = None
                    self.signing = VirtualServices.VirtualService.Details.PackageInformation.Signing()
                    self.signing.parent = self


                class Application(object):
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
                        self.parent = None
                        self.description = None
                        self.installed_version = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-virtual-service-oper:application'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.description is not None:
                            return True

                        if self.installed_version is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
                        return meta._meta_table['VirtualServices.VirtualService.Details.PackageInformation.Application']['meta_info']


                class Signing(object):
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
                        self.parent = None
                        self.key_type = None
                        self.method = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-virtual-service-oper:signing'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.key_type is not None:
                            return True

                        if self.method is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
                        return meta._meta_table['VirtualServices.VirtualService.Details.PackageInformation.Signing']['meta_info']


                class Licensing(object):
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
                        self.parent = None
                        self.name = None
                        self.version = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-virtual-service-oper:licensing'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.name is not None:
                            return True

                        if self.version is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
                        return meta._meta_table['VirtualServices.VirtualService.Details.PackageInformation.Licensing']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-virtual-service-oper:package-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.application is not None and self.application._has_data():
                        return True

                    if self.licensing is not None and self.licensing._has_data():
                        return True

                    if self.name is not None:
                        return True

                    if self.path is not None:
                        return True

                    if self.signing is not None and self.signing._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
                    return meta._meta_table['VirtualServices.VirtualService.Details.PackageInformation']['meta_info']


            class DetailedGuestStatus(object):
                """
                Details on the guest status.
                
                .. attribute:: processes
                
                	All the processes
                	**type**\:   :py:class:`Processes <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.Details.DetailedGuestStatus.Processes>`
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.processes = VirtualServices.VirtualService.Details.DetailedGuestStatus.Processes()
                    self.processes.parent = self


                class Processes(object):
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
                        self.parent = None
                        self.memory = None
                        self.name = None
                        self.pid = None
                        self.status = None
                        self.uptime = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-virtual-service-oper:processes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.memory is not None:
                            return True

                        if self.name is not None:
                            return True

                        if self.pid is not None:
                            return True

                        if self.status is not None:
                            return True

                        if self.uptime is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
                        return meta._meta_table['VirtualServices.VirtualService.Details.DetailedGuestStatus.Processes']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-virtual-service-oper:detailed-guest-status'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.processes is not None and self.processes._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
                    return meta._meta_table['VirtualServices.VirtualService.Details.DetailedGuestStatus']['meta_info']


            class ResourceReservation(object):
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
                    self.parent = None
                    self.cpu = None
                    self.disk = None
                    self.memory = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-virtual-service-oper:resource-reservation'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.cpu is not None:
                        return True

                    if self.disk is not None:
                        return True

                    if self.memory is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
                    return meta._meta_table['VirtualServices.VirtualService.Details.ResourceReservation']['meta_info']


            class ResourceAdmission(object):
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
                    self.parent = None
                    self.cpu = None
                    self.disk_space = None
                    self.memory = None
                    self.state = None
                    self.vcpus = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-virtual-service-oper:resource-admission'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.cpu is not None:
                        return True

                    if self.disk_space is not None:
                        return True

                    if self.memory is not None:
                        return True

                    if self.state is not None:
                        return True

                    if self.vcpus is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
                    return meta._meta_table['VirtualServices.VirtualService.Details.ResourceAdmission']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XE-virtual-service-oper:details'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.activated_profile_name is not None:
                    return True

                if self.detailed_guest_status is not None and self.detailed_guest_status._has_data():
                    return True

                if self.guest_interface is not None:
                    return True

                if self.package_information is not None and self.package_information._has_data():
                    return True

                if self.resource_admission is not None and self.resource_admission._has_data():
                    return True

                if self.resource_reservation is not None and self.resource_reservation._has_data():
                    return True

                if self.state is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
                return meta._meta_table['VirtualServices.VirtualService.Details']['meta_info']


        class Utilization(object):
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
                self.parent = None
                self.cpu_util = VirtualServices.VirtualService.Utilization.CpuUtil()
                self.cpu_util.parent = self
                self.memory_util = VirtualServices.VirtualService.Utilization.MemoryUtil()
                self.memory_util.parent = self
                self.name = None


            class CpuUtil(object):
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
                    self.parent = None
                    self.actual_application_util = None
                    self.cpu_state = None
                    self.requested_application_util = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-virtual-service-oper:cpu-util'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.actual_application_util is not None:
                        return True

                    if self.cpu_state is not None:
                        return True

                    if self.requested_application_util is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
                    return meta._meta_table['VirtualServices.VirtualService.Utilization.CpuUtil']['meta_info']


            class MemoryUtil(object):
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
                    self.parent = None
                    self.memory_allocation = None
                    self.memory_used = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-virtual-service-oper:memory-util'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.memory_allocation is not None:
                        return True

                    if self.memory_used is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
                    return meta._meta_table['VirtualServices.VirtualService.Utilization.MemoryUtil']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XE-virtual-service-oper:utilization'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cpu_util is not None and self.cpu_util._has_data():
                    return True

                if self.memory_util is not None and self.memory_util._has_data():
                    return True

                if self.name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
                return meta._meta_table['VirtualServices.VirtualService.Utilization']['meta_info']


        class NetworkUtils(object):
            """
            list of the network utilizations for the virtual\-service.
            
            .. attribute:: network_util
            
            	Details on a network utilization for the virtual\-service
            	**type**\: list of    :py:class:`NetworkUtil <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.NetworkUtils.NetworkUtil>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.network_util = YList()
                self.network_util.parent = self
                self.network_util.name = 'network_util'


            class NetworkUtil(object):
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
                    self.parent = None
                    self.name = None
                    self.alias = None
                    self.rx_bytes = None
                    self.rx_errors = None
                    self.rx_packets = None
                    self.tx_bytes = None
                    self.tx_errors = None
                    self.tx_packets = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.name is None:
                        raise YPYModelError('Key property name is None')
                    if self.alias is None:
                        raise YPYModelError('Key property alias is None')

                    return self.parent._common_path +'/Cisco-IOS-XE-virtual-service-oper:network-util[Cisco-IOS-XE-virtual-service-oper:name = ' + str(self.name) + '][Cisco-IOS-XE-virtual-service-oper:alias = ' + str(self.alias) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.alias is not None:
                        return True

                    if self.rx_bytes is not None:
                        return True

                    if self.rx_errors is not None:
                        return True

                    if self.rx_packets is not None:
                        return True

                    if self.tx_bytes is not None:
                        return True

                    if self.tx_errors is not None:
                        return True

                    if self.tx_packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
                    return meta._meta_table['VirtualServices.VirtualService.NetworkUtils.NetworkUtil']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XE-virtual-service-oper:network-utils'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.network_util is not None:
                    for child_ref in self.network_util:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
                return meta._meta_table['VirtualServices.VirtualService.NetworkUtils']['meta_info']


        class StorageUtils(object):
            """
            List of the storage utilizations for the virtual\-service.
            
            .. attribute:: storage_util
            
            	Details on a storage utilization for the virtual\-service
            	**type**\: list of    :py:class:`StorageUtil <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.StorageUtils.StorageUtil>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.storage_util = YList()
                self.storage_util.parent = self
                self.storage_util.name = 'storage_util'


            class StorageUtil(object):
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
                    self.parent = None
                    self.name = None
                    self.alias = None
                    self.available = None
                    self.capacity = None
                    self.errors = None
                    self.rd_bytes = None
                    self.rd_requests = None
                    self.usage = None
                    self.used = None
                    self.wr_bytes = None
                    self.wr_requests = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.name is None:
                        raise YPYModelError('Key property name is None')
                    if self.alias is None:
                        raise YPYModelError('Key property alias is None')

                    return self.parent._common_path +'/Cisco-IOS-XE-virtual-service-oper:storage-util[Cisco-IOS-XE-virtual-service-oper:name = ' + str(self.name) + '][Cisco-IOS-XE-virtual-service-oper:alias = ' + str(self.alias) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.alias is not None:
                        return True

                    if self.available is not None:
                        return True

                    if self.capacity is not None:
                        return True

                    if self.errors is not None:
                        return True

                    if self.rd_bytes is not None:
                        return True

                    if self.rd_requests is not None:
                        return True

                    if self.usage is not None:
                        return True

                    if self.used is not None:
                        return True

                    if self.wr_bytes is not None:
                        return True

                    if self.wr_requests is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
                    return meta._meta_table['VirtualServices.VirtualService.StorageUtils.StorageUtil']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XE-virtual-service-oper:storage-utils'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.storage_util is not None:
                    for child_ref in self.storage_util:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
                return meta._meta_table['VirtualServices.VirtualService.StorageUtils']['meta_info']


        class AttachedDevices(object):
            """
            Details for the devices attached to this virtual service.
            
            .. attribute:: attached_device
            
            	List of attached devices
            	**type**\: list of    :py:class:`AttachedDevice <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.AttachedDevices.AttachedDevice>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.attached_device = YList()
                self.attached_device.parent = self
                self.attached_device.name = 'attached_device'


            class AttachedDevice(object):
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
                    self.parent = None
                    self.name = None
                    self.alias = None
                    self.type = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return self.parent._common_path +'/Cisco-IOS-XE-virtual-service-oper:attached-device[Cisco-IOS-XE-virtual-service-oper:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.alias is not None:
                        return True

                    if self.type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
                    return meta._meta_table['VirtualServices.VirtualService.AttachedDevices.AttachedDevice']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XE-virtual-service-oper:attached-devices'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.attached_device is not None:
                    for child_ref in self.attached_device:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
                return meta._meta_table['VirtualServices.VirtualService.AttachedDevices']['meta_info']


        class NetworkInterfaces(object):
            """
            Details for the network interfaces.
            
            .. attribute:: network_interface
            
            	Details for a network interface
            	**type**\: list of    :py:class:`NetworkInterface <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.NetworkInterfaces.NetworkInterface>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.network_interface = YList()
                self.network_interface.parent = self
                self.network_interface.name = 'network_interface'


            class NetworkInterface(object):
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
                    self.parent = None
                    self.mac_address = None
                    self.attached_interface = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.mac_address is None:
                        raise YPYModelError('Key property mac_address is None')

                    return self.parent._common_path +'/Cisco-IOS-XE-virtual-service-oper:network-interface[Cisco-IOS-XE-virtual-service-oper:mac-address = ' + str(self.mac_address) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.mac_address is not None:
                        return True

                    if self.attached_interface is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
                    return meta._meta_table['VirtualServices.VirtualService.NetworkInterfaces.NetworkInterface']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XE-virtual-service-oper:network-interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.network_interface is not None:
                    for child_ref in self.network_interface:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
                return meta._meta_table['VirtualServices.VirtualService.NetworkInterfaces']['meta_info']


        class GuestRoutes(object):
            """
            Routes for the guest interface.
            
            .. attribute:: guest_route
            
            	List of guest routes for a guest interface
            	**type**\: list of    :py:class:`GuestRoute <ydk.models.cisco_ios_xe.Cisco_IOS_XE_virtual_service_oper.VirtualServices.VirtualService.GuestRoutes.GuestRoute>`
            
            

            """

            _prefix = 'virtual-service-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.guest_route = YList()
                self.guest_route.parent = self
                self.guest_route.name = 'guest_route'


            class GuestRoute(object):
                """
                List of guest routes for a guest interface.
                
                .. attribute:: route  <key>
                
                	A guest route for a guest interface
                	**type**\:  str
                
                

                """

                _prefix = 'virtual-service-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.route = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.route is None:
                        raise YPYModelError('Key property route is None')

                    return self.parent._common_path +'/Cisco-IOS-XE-virtual-service-oper:guest-route[Cisco-IOS-XE-virtual-service-oper:route = ' + str(self.route) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.route is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
                    return meta._meta_table['VirtualServices.VirtualService.GuestRoutes.GuestRoute']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XE-virtual-service-oper:guest-routes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.guest_route is not None:
                    for child_ref in self.guest_route:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
                return meta._meta_table['VirtualServices.VirtualService.GuestRoutes']['meta_info']

        @property
        def _common_path(self):
            if self.name is None:
                raise YPYModelError('Key property name is None')

            return '/Cisco-IOS-XE-virtual-service-oper:virtual-services/Cisco-IOS-XE-virtual-service-oper:virtual-service[Cisco-IOS-XE-virtual-service-oper:name = ' + str(self.name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.name is not None:
                return True

            if self.attached_devices is not None and self.attached_devices._has_data():
                return True

            if self.details is not None and self.details._has_data():
                return True

            if self.guest_routes is not None and self.guest_routes._has_data():
                return True

            if self.network_interfaces is not None and self.network_interfaces._has_data():
                return True

            if self.network_utils is not None and self.network_utils._has_data():
                return True

            if self.storage_utils is not None and self.storage_utils._has_data():
                return True

            if self.utilization is not None and self.utilization._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
            return meta._meta_table['VirtualServices.VirtualService']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-virtual-service-oper:virtual-services'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.virtual_service is not None:
            for child_ref in self.virtual_service:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_virtual_service_oper as meta
        return meta._meta_table['VirtualServices']['meta_info']



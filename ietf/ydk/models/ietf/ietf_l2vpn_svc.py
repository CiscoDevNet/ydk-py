""" ietf_l2vpn_svc 

The YANG module defines a generic service configuration
model for Layer 2 VPN services common across all of the
vendor implementations.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class ControlModeEnum(Enum):
    """
    ControlModeEnum

    Defining a type of the control mode

    .. data:: peer = 0

    	Peer mode

    .. data:: tunnel = 1

    	Tunnel mode

    .. data:: discard = 2

    	Discard mode

    """

    peer = 0

    tunnel = 1

    discard = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['ControlModeEnum']


class NegModeEnum(Enum):
    """
    NegModeEnum

    Defining a type of the negotiation mode

    .. data:: full_duplex = 0

    	Full duplex mode

    .. data:: auto_neg = 1

    	Auto negotiation mode

    """

    full_duplex = 0

    auto_neg = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['NegModeEnum']



class BwTypeIdentity(object):
    """
    Identity of bandwidth
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['BwTypeIdentity']['meta_info']


class LacpModeIdentity(object):
    """
    Identity of LACP mode
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['LacpModeIdentity']['meta_info']


class LacpStateIdentity(object):
    """
    Identity of LACP state
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['LacpStateIdentity']['meta_info']


class MacLearningModeIdentity(object):
    """
    MAC learning mode
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['MacLearningModeIdentity']['meta_info']


class PolicingIdentity(object):
    """
    Identity of policing type
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['PolicingIdentity']['meta_info']


class BumTypeIdentity(object):
    """
    Identity of BUM type
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['BumTypeIdentity']['meta_info']


class ColorTypeIdentity(object):
    """
    Identity of color types
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['ColorTypeIdentity']['meta_info']


class PlacementDiversityIdentity(object):
    """
    Base identity for site placement
    constraints
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['PlacementDiversityIdentity']['meta_info']


class PerfTierOptIdentity(object):
    """
    Identity of performance tier option.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['PerfTierOptIdentity']['meta_info']


class SiteTypeIdentity(object):
    """
    Identity of site type.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['SiteTypeIdentity']['meta_info']


class AddressFamilyIdentity(object):
    """
    Base identity for an address family.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['AddressFamilyIdentity']['meta_info']


class DataSvcFrameDeliveryIdentity(object):
    """
    Delivery types
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['DataSvcFrameDeliveryIdentity']['meta_info']


class LoopPreventionTypeIdentity(object):
    """
    Identity of loop prevention
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['LoopPreventionTypeIdentity']['meta_info']


class ColorIdIdentity(object):
    """
    Identity of color id
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['ColorIdIdentity']['meta_info']


class FaultAlarmDefectTypeIdentity(object):
    """
    Indicating the alarm priority defect
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['FaultAlarmDefectTypeIdentity']['meta_info']


class ManagementIdentity(object):
    """
    Base identity for site management scheme.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['ManagementIdentity']['meta_info']


class SvcTopoTypeIdentity(object):
    """
    Service topology Type
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['SvcTopoTypeIdentity']['meta_info']


class CosIdIdentity(object):
    """
    Identity of class of service id
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['CosIdIdentity']['meta_info']


class L2VpnTypeIdentity(object):
    """
    Layer 2 VPN types
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['L2VpnTypeIdentity']['meta_info']


class BundlingTypeIdentity(object):
    """
    Bundling type.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['BundlingTypeIdentity']['meta_info']


class VpnTopologyIdentity(object):
    """
    Base identity for VPN topology.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['VpnTopologyIdentity']['meta_info']


class SiteRoleIdentity(object):
    """
    Base identity for site type.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['SiteRoleIdentity']['meta_info']


class PmTypeIdentity(object):
    """
    Performance monitor type
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['PmTypeIdentity']['meta_info']


class L2AccessTypeIdentity(object):
    """
    This identify the access type
    of the vpn acccess interface
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['L2AccessTypeIdentity']['meta_info']


class VpnSignalingTypeIdentity(object):
    """
    Identity of VPN signaling types
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['VpnSignalingTypeIdentity']['meta_info']


class LacpSpeedIdentity(object):
    """
    Identity of LACP speed
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['LacpSpeedIdentity']['meta_info']


class ServiceTypeIdentity(object):
    """
    Identity of service type.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['ServiceTypeIdentity']['meta_info']


class L2VpnSvc(object):
    """
    Container for L2VPN service
    
    .. attribute:: customer_info
    
    	Container for customer information
    	**type**\:   :py:class:`CustomerInfo <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.CustomerInfo>`
    
    .. attribute:: sites
    
    	Container of site configurations
    	**type**\:   :py:class:`Sites <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites>`
    
    .. attribute:: vpn_services
    
    	Container for VPN services
    	**type**\:   :py:class:`VpnServices <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices>`
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        self.customer_info = L2VpnSvc.CustomerInfo()
        self.customer_info.parent = self
        self.sites = L2VpnSvc.Sites()
        self.sites.parent = self
        self.vpn_services = L2VpnSvc.VpnServices()
        self.vpn_services.parent = self


    class CustomerInfo(object):
        """
        Container for customer information.
        
        .. attribute:: customer_info
        
        	List of customer information
        	**type**\: list of    :py:class:`CustomerInfo_ <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.CustomerInfo.CustomerInfo_>`
        
        

        """

        _prefix = 'l2svc'
        _revision = '2017-02-13'

        def __init__(self):
            self.parent = None
            self.customer_info = YList()
            self.customer_info.parent = self
            self.customer_info.name = 'customer_info'


        class CustomerInfo_(object):
            """
            List of customer information
            
            .. attribute:: customer_account_number  <key>
            
            	Customer account number
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: customer_name  <key>
            
            	Customer name
            	**type**\:  str
            
            .. attribute:: customer_operation_center
            
            	Configuration of customer operation center
            	**type**\:   :py:class:`CustomerOperationCenter <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.CustomerInfo.CustomerInfo_.CustomerOperationCenter>`
            
            

            """

            _prefix = 'l2svc'
            _revision = '2017-02-13'

            def __init__(self):
                self.parent = None
                self.customer_account_number = None
                self.customer_name = None
                self.customer_operation_center = L2VpnSvc.CustomerInfo.CustomerInfo_.CustomerOperationCenter()
                self.customer_operation_center.parent = self


            class CustomerOperationCenter(object):
                """
                Configuration of customer operation center
                
                .. attribute:: customer_noc_phone_number
                
                	Configuration of customer NOCc phone number
                	**type**\:   :py:class:`CustomerNocPhoneNumber <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.CustomerInfo.CustomerInfo_.CustomerOperationCenter.CustomerNocPhoneNumber>`
                
                .. attribute:: customer_noc_street_address
                
                	Customer NOC street Address
                	**type**\:  str
                
                

                """

                _prefix = 'l2svc'
                _revision = '2017-02-13'

                def __init__(self):
                    self.parent = None
                    self.customer_noc_phone_number = L2VpnSvc.CustomerInfo.CustomerInfo_.CustomerOperationCenter.CustomerNocPhoneNumber()
                    self.customer_noc_phone_number.parent = self
                    self.customer_noc_street_address = None


                class CustomerNocPhoneNumber(object):
                    """
                    Configuration of customer NOCc phone number
                    
                    .. attribute:: extension_options
                    
                    	Extension or options
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: main_phone_num
                    
                    	Main phone number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'l2svc'
                    _revision = '2017-02-13'

                    def __init__(self):
                        self.parent = None
                        self.extension_options = None
                        self.main_phone_num = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-l2vpn-svc:customer-noc-phone-number'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.extension_options is not None:
                            return True

                        if self.main_phone_num is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                        return meta._meta_table['L2VpnSvc.CustomerInfo.CustomerInfo_.CustomerOperationCenter.CustomerNocPhoneNumber']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-l2vpn-svc:customer-operation-center'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.customer_noc_phone_number is not None and self.customer_noc_phone_number._has_data():
                        return True

                    if self.customer_noc_street_address is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                    return meta._meta_table['L2VpnSvc.CustomerInfo.CustomerInfo_.CustomerOperationCenter']['meta_info']

            @property
            def _common_path(self):
                if self.customer_account_number is None:
                    raise YPYModelError('Key property customer_account_number is None')
                if self.customer_name is None:
                    raise YPYModelError('Key property customer_name is None')

                return '/ietf-l2vpn-svc:l2vpn-svc/ietf-l2vpn-svc:customer-info/ietf-l2vpn-svc:customer-info[ietf-l2vpn-svc:customer-account-number = ' + str(self.customer_account_number) + '][ietf-l2vpn-svc:customer-name = ' + str(self.customer_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.customer_account_number is not None:
                    return True

                if self.customer_name is not None:
                    return True

                if self.customer_operation_center is not None and self.customer_operation_center._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                return meta._meta_table['L2VpnSvc.CustomerInfo.CustomerInfo_']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-l2vpn-svc:l2vpn-svc/ietf-l2vpn-svc:customer-info'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.customer_info is not None:
                for child_ref in self.customer_info:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
            return meta._meta_table['L2VpnSvc.CustomerInfo']['meta_info']


    class VpnServices(object):
        """
        Container for VPN services.
        
        .. attribute:: vpn_svc
        
        	List of vpn\-svc
        	**type**\: list of    :py:class:`VpnSvc <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc>`
        
        

        """

        _prefix = 'l2svc'
        _revision = '2017-02-13'

        def __init__(self):
            self.parent = None
            self.vpn_svc = YList()
            self.vpn_svc.parent = self
            self.vpn_svc.name = 'vpn_svc'


        class VpnSvc(object):
            """
            List of vpn\-svc
            
            .. attribute:: vpn_id  <key>
            
            	Defining a service id
            	**type**\:  str
            
            .. attribute:: ce_vlan_preservation
            
            	CE vlan preservation
            	**type**\:   :py:class:`CeVlanPreservation <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc.CeVlanPreservation>`
            
            .. attribute:: cloud_accesses
            
            	Container for cloud access configurations
            	**type**\:   :py:class:`CloudAccesses <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc.CloudAccesses>`
            
            .. attribute:: cvlan_id_to_evc_map
            
            	List for cvlan\-id to evc map configurations
            	**type**\: list of    :py:class:`CvlanIdToEvcMap <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc.CvlanIdToEvcMap>`
            
            .. attribute:: ethernet_svc_type
            
            	Container of Ethernet service type
            	**type**\:   :py:class:`EthernetSvcType <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc.EthernetSvcType>`
            
            .. attribute:: evc_type
            
            	Container for Ethernet virtual connection
            	**type**\:   :py:class:`EvcType <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc.EvcType>`
            
            .. attribute:: l2cp_control
            
            	Container of L2CP control configurations
            	**type**\:   :py:class:`L2CpControl <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc.L2CpControl>`
            
            .. attribute:: load_balance_options
            
            	Container for load balance options
            	**type**\:   :py:class:`LoadBalanceOptions <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc.LoadBalanceOptions>`
            
            .. attribute:: metro_network_id
            
            	Container of Metro\-Network ID configurations
            	**type**\:   :py:class:`MetroNetworkId <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc.MetroNetworkId>`
            
            .. attribute:: ovc_type
            
            	Container for OVC
            	**type**\:   :py:class:`OvcType <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc.OvcType>`
            
            .. attribute:: service_level_mac_limit
            
            	Service\-level MAC\-limit (E\-LAN only)
            	**type**\:  str
            
            .. attribute:: service_protection
            
            	Container of End\-to\-end Service Protection configurations
            	**type**\:   :py:class:`ServiceProtection <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc.ServiceProtection>`
            
            .. attribute:: sla_targets
            
            	Container for SLA targets
            	**type**\:   :py:class:`SlaTargets <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc.SlaTargets>`
            
            .. attribute:: svc_topo
            
            	Defining service topology, such as point to point, multipoint to multipoint, rooted multipoint, etc
            	**type**\:   :py:class:`SvcTopoTypeIdentity <ydk.models.ietf.ietf_l2vpn_svc.SvcTopoTypeIdentity>`
            
            .. attribute:: svc_type
            
            	Service type
            	**type**\:   :py:class:`ServiceTypeIdentity <ydk.models.ietf.ietf_l2vpn_svc.ServiceTypeIdentity>`
            
            .. attribute:: svlan_id_ethernet_tag
            
            	SVLAN\-ID/Ethernet Tag configurations
            	**type**\:  str
            
            

            """

            _prefix = 'l2svc'
            _revision = '2017-02-13'

            def __init__(self):
                self.parent = None
                self.vpn_id = None
                self.ce_vlan_preservation = L2VpnSvc.VpnServices.VpnSvc.CeVlanPreservation()
                self.ce_vlan_preservation.parent = self
                self.cloud_accesses = L2VpnSvc.VpnServices.VpnSvc.CloudAccesses()
                self.cloud_accesses.parent = self
                self.cvlan_id_to_evc_map = YList()
                self.cvlan_id_to_evc_map.parent = self
                self.cvlan_id_to_evc_map.name = 'cvlan_id_to_evc_map'
                self.ethernet_svc_type = L2VpnSvc.VpnServices.VpnSvc.EthernetSvcType()
                self.ethernet_svc_type.parent = self
                self.evc_type = L2VpnSvc.VpnServices.VpnSvc.EvcType()
                self.evc_type.parent = self
                self.l2cp_control = L2VpnSvc.VpnServices.VpnSvc.L2CpControl()
                self.l2cp_control.parent = self
                self.load_balance_options = L2VpnSvc.VpnServices.VpnSvc.LoadBalanceOptions()
                self.load_balance_options.parent = self
                self.metro_network_id = L2VpnSvc.VpnServices.VpnSvc.MetroNetworkId()
                self.metro_network_id.parent = self
                self.ovc_type = L2VpnSvc.VpnServices.VpnSvc.OvcType()
                self.ovc_type.parent = self
                self.service_level_mac_limit = None
                self.service_protection = L2VpnSvc.VpnServices.VpnSvc.ServiceProtection()
                self.service_protection.parent = self
                self.sla_targets = L2VpnSvc.VpnServices.VpnSvc.SlaTargets()
                self.sla_targets.parent = self
                self.svc_topo = None
                self.svc_type = None
                self.svlan_id_ethernet_tag = None


            class EvcType(object):
                """
                Container for Ethernet virtual connection.
                
                .. attribute:: evc_id
                
                	Ethernet Virtual Connection identifier
                	**type**\:  str
                
                .. attribute:: number_of_pe
                
                	Number of PE
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_site
                
                	Number of Sites
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: uni_list
                
                	Container for UNI List
                	**type**\:   :py:class:`UniList <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc.EvcType.UniList>`
                
                

                """

                _prefix = 'l2svc'
                _revision = '2017-02-13'

                def __init__(self):
                    self.parent = None
                    self.evc_id = None
                    self.number_of_pe = None
                    self.number_of_site = None
                    self.uni_list = L2VpnSvc.VpnServices.VpnSvc.EvcType.UniList()
                    self.uni_list.parent = self


                class UniList(object):
                    """
                    Container for UNI List
                    
                    .. attribute:: uni_list
                    
                    	List for UNIs
                    	**type**\: list of    :py:class:`UniList_ <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc.EvcType.UniList.UniList_>`
                    
                    

                    """

                    _prefix = 'l2svc'
                    _revision = '2017-02-13'

                    def __init__(self):
                        self.parent = None
                        self.uni_list = YList()
                        self.uni_list.parent = self
                        self.uni_list.name = 'uni_list'


                    class UniList_(object):
                        """
                        List for UNIs
                        
                        .. attribute:: network_access_id  <key>
                        
                        	Network Access Identifier
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'l2svc'
                        _revision = '2017-02-13'

                        def __init__(self):
                            self.parent = None
                            self.network_access_id = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.network_access_id is None:
                                raise YPYModelError('Key property network_access_id is None')

                            return self.parent._common_path +'/ietf-l2vpn-svc:uni-list[ietf-l2vpn-svc:network-access-id = ' + str(self.network_access_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.network_access_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                            return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc.EvcType.UniList.UniList_']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-l2vpn-svc:uni-list'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.uni_list is not None:
                            for child_ref in self.uni_list:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                        return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc.EvcType.UniList']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-l2vpn-svc:evc-type'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.evc_id is not None:
                        return True

                    if self.number_of_pe is not None:
                        return True

                    if self.number_of_site is not None:
                        return True

                    if self.uni_list is not None and self.uni_list._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                    return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc.EvcType']['meta_info']


            class OvcType(object):
                """
                Container for OVC
                
                .. attribute:: ovc_list
                
                	List for OVC
                	**type**\: list of    :py:class:`OvcList <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc.OvcType.OvcList>`
                
                

                """

                _prefix = 'l2svc'
                _revision = '2017-02-13'

                def __init__(self):
                    self.parent = None
                    self.ovc_list = YList()
                    self.ovc_list.parent = self
                    self.ovc_list.name = 'ovc_list'


                class OvcList(object):
                    """
                    List for OVC
                    
                    .. attribute:: ovc_id  <key>
                    
                    	OVC ID type
                    	**type**\:  str
                    
                    .. attribute:: off_net
                    
                    	Off net
                    	**type**\:  bool
                    
                    .. attribute:: on_net
                    
                    	On net
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'l2svc'
                    _revision = '2017-02-13'

                    def __init__(self):
                        self.parent = None
                        self.ovc_id = None
                        self.off_net = None
                        self.on_net = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.ovc_id is None:
                            raise YPYModelError('Key property ovc_id is None')

                        return self.parent._common_path +'/ietf-l2vpn-svc:ovc-list[ietf-l2vpn-svc:ovc-id = ' + str(self.ovc_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.ovc_id is not None:
                            return True

                        if self.off_net is not None:
                            return True

                        if self.on_net is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                        return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc.OvcType.OvcList']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-l2vpn-svc:ovc-type'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.ovc_list is not None:
                        for child_ref in self.ovc_list:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                    return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc.OvcType']['meta_info']


            class EthernetSvcType(object):
                """
                Container of Ethernet service type
                
                .. attribute:: access_epl
                
                	Access Ethernet virtual private line
                	**type**\:  bool
                
                .. attribute:: access_evpl
                
                	Access Ethernet virtual private line
                	**type**\:  bool
                
                .. attribute:: ep_lan
                
                	Ethernet private LAN
                	**type**\:  bool
                
                .. attribute:: epl
                
                	Ethernet private line
                	**type**\:  bool
                
                .. attribute:: evp_lan
                
                	Ethernet virtual private LAN
                	**type**\:  bool
                
                .. attribute:: evpl
                
                	Ethernet virtual private line
                	**type**\:  bool
                
                

                """

                _prefix = 'l2svc'
                _revision = '2017-02-13'

                def __init__(self):
                    self.parent = None
                    self.access_epl = None
                    self.access_evpl = None
                    self.ep_lan = None
                    self.epl = None
                    self.evp_lan = None
                    self.evpl = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-l2vpn-svc:ethernet-svc-type'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.access_epl is not None:
                        return True

                    if self.access_evpl is not None:
                        return True

                    if self.ep_lan is not None:
                        return True

                    if self.epl is not None:
                        return True

                    if self.evp_lan is not None:
                        return True

                    if self.evpl is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                    return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc.EthernetSvcType']['meta_info']


            class CloudAccesses(object):
                """
                Container for cloud access configurations
                
                .. attribute:: cloud_access
                
                	Cloud access configuration
                	**type**\: list of    :py:class:`CloudAccess <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess>`
                
                

                """

                _prefix = 'l2svc'
                _revision = '2017-02-13'

                def __init__(self):
                    self.parent = None
                    self.cloud_access = YList()
                    self.cloud_access.parent = self
                    self.cloud_access.name = 'cloud_access'


                class CloudAccess(object):
                    """
                    Cloud access configuration.
                    
                    .. attribute:: cloud_identifier  <key>
                    
                    	Identification of cloud service. Local admin meaning
                    	**type**\:  str
                    
                    .. attribute:: authorized_sites
                    
                    	Configuration of authorized sites
                    	**type**\:   :py:class:`AuthorizedSites <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.AuthorizedSites>`
                    
                    .. attribute:: denied_sites
                    
                    	Configuration of denied sites
                    	**type**\:   :py:class:`DeniedSites <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.DeniedSites>`
                    
                    .. attribute:: deny_site
                    
                    	Site ID to be denied
                    	**type**\:  list of str
                    
                    	**refers to**\:  :py:class:`site_id <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site>`
                    
                    .. attribute:: permit_any
                    
                    	Allow all sites
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: permit_site
                    
                    	Site ID to be authorized
                    	**type**\:  list of str
                    
                    	**refers to**\:  :py:class:`site_id <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site>`
                    
                    

                    """

                    _prefix = 'l2svc'
                    _revision = '2017-02-13'

                    def __init__(self):
                        self.parent = None
                        self.cloud_identifier = None
                        self.authorized_sites = L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.AuthorizedSites()
                        self.authorized_sites.parent = self
                        self.denied_sites = L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.DeniedSites()
                        self.denied_sites.parent = self
                        self.deny_site = YLeafList()
                        self.deny_site.parent = self
                        self.deny_site.name = 'deny_site'
                        self.permit_any = None
                        self.permit_site = YLeafList()
                        self.permit_site.parent = self
                        self.permit_site.name = 'permit_site'


                    class AuthorizedSites(object):
                        """
                        Configuration of authorized sites
                        
                        .. attribute:: authorized_site
                        
                        	List of authorized sites
                        	**type**\: list of    :py:class:`AuthorizedSite <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.AuthorizedSites.AuthorizedSite>`
                        
                        

                        """

                        _prefix = 'l2svc'
                        _revision = '2017-02-13'

                        def __init__(self):
                            self.parent = None
                            self.authorized_site = YList()
                            self.authorized_site.parent = self
                            self.authorized_site.name = 'authorized_site'


                        class AuthorizedSite(object):
                            """
                            List of authorized sites.
                            
                            .. attribute:: site_id  <key>
                            
                            	Site ID
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`site_id <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site>`
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.site_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.site_id is None:
                                    raise YPYModelError('Key property site_id is None')

                                return self.parent._common_path +'/ietf-l2vpn-svc:authorized-site[ietf-l2vpn-svc:site-id = ' + str(self.site_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.site_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.AuthorizedSites.AuthorizedSite']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-l2vpn-svc:authorized-sites'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.authorized_site is not None:
                                for child_ref in self.authorized_site:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                            return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.AuthorizedSites']['meta_info']


                    class DeniedSites(object):
                        """
                        Configuration of denied sites
                        
                        .. attribute:: denied_site
                        
                        	List of denied sites
                        	**type**\: list of    :py:class:`DeniedSite <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.DeniedSites.DeniedSite>`
                        
                        

                        """

                        _prefix = 'l2svc'
                        _revision = '2017-02-13'

                        def __init__(self):
                            self.parent = None
                            self.denied_site = YList()
                            self.denied_site.parent = self
                            self.denied_site.name = 'denied_site'


                        class DeniedSite(object):
                            """
                            List of denied sites.
                            
                            .. attribute:: site_id  <key>
                            
                            	Site ID
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`site_id <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site>`
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.site_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.site_id is None:
                                    raise YPYModelError('Key property site_id is None')

                                return self.parent._common_path +'/ietf-l2vpn-svc:denied-site[ietf-l2vpn-svc:site-id = ' + str(self.site_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.site_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.DeniedSites.DeniedSite']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-l2vpn-svc:denied-sites'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.denied_site is not None:
                                for child_ref in self.denied_site:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                            return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.DeniedSites']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.cloud_identifier is None:
                            raise YPYModelError('Key property cloud_identifier is None')

                        return self.parent._common_path +'/ietf-l2vpn-svc:cloud-access[ietf-l2vpn-svc:cloud-identifier = ' + str(self.cloud_identifier) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.cloud_identifier is not None:
                            return True

                        if self.authorized_sites is not None and self.authorized_sites._has_data():
                            return True

                        if self.denied_sites is not None and self.denied_sites._has_data():
                            return True

                        if self.deny_site is not None:
                            for child in self.deny_site:
                                if child is not None:
                                    return True

                        if self.permit_any is not None:
                            return True

                        if self.permit_site is not None:
                            for child in self.permit_site:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                        return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-l2vpn-svc:cloud-accesses'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.cloud_access is not None:
                        for child_ref in self.cloud_access:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                    return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc.CloudAccesses']['meta_info']


            class CeVlanPreservation(object):
                """
                CE vlan preservation
                
                

                """

                _prefix = 'l2svc'
                _revision = '2017-02-13'

                def __init__(self):
                    self.parent = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-l2vpn-svc:ce-vlan-preservation'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                    return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc.CeVlanPreservation']['meta_info']


            class MetroNetworkId(object):
                """
                Container of Metro\-Network ID configurations
                
                .. attribute:: inter_mkt_service
                
                	Indicate whether service is inter market service
                	**type**\:  bool
                
                .. attribute:: intra_mkt
                
                	List of intra\-MKT
                	**type**\: list of    :py:class:`IntraMkt <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc.MetroNetworkId.IntraMkt>`
                
                

                """

                _prefix = 'l2svc'
                _revision = '2017-02-13'

                def __init__(self):
                    self.parent = None
                    self.inter_mkt_service = None
                    self.intra_mkt = YList()
                    self.intra_mkt.parent = self
                    self.intra_mkt.name = 'intra_mkt'


                class IntraMkt(object):
                    """
                    List of intra\-MKT
                    
                    .. attribute:: metro_mkt_id  <key>
                    
                    	Metro MKT ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mkt_name  <key>
                    
                    	MKT Name
                    	**type**\:  str
                    
                    .. attribute:: ovc_id
                    
                    	OVC identifier
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'l2svc'
                    _revision = '2017-02-13'

                    def __init__(self):
                        self.parent = None
                        self.metro_mkt_id = None
                        self.mkt_name = None
                        self.ovc_id = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.metro_mkt_id is None:
                            raise YPYModelError('Key property metro_mkt_id is None')
                        if self.mkt_name is None:
                            raise YPYModelError('Key property mkt_name is None')

                        return self.parent._common_path +'/ietf-l2vpn-svc:intra-mkt[ietf-l2vpn-svc:metro-mkt-id = ' + str(self.metro_mkt_id) + '][ietf-l2vpn-svc:mkt-name = ' + str(self.mkt_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.metro_mkt_id is not None:
                            return True

                        if self.mkt_name is not None:
                            return True

                        if self.ovc_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                        return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc.MetroNetworkId.IntraMkt']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-l2vpn-svc:metro-network-id'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.inter_mkt_service is not None:
                        return True

                    if self.intra_mkt is not None:
                        for child_ref in self.intra_mkt:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                    return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc.MetroNetworkId']['meta_info']


            class L2CpControl(object):
                """
                Container of L2CP control configurations
                
                .. attribute:: lldp
                
                	LLDP
                	**type**\:  bool
                
                .. attribute:: pause
                
                	Pause
                	**type**\:   :py:class:`ControlModeEnum <ydk.models.ietf.ietf_l2vpn_svc.ControlModeEnum>`
                
                .. attribute:: stp_rstp_mstp
                
                	STP/RSTP/MSTP
                	**type**\:   :py:class:`ControlModeEnum <ydk.models.ietf.ietf_l2vpn_svc.ControlModeEnum>`
                
                

                """

                _prefix = 'l2svc'
                _revision = '2017-02-13'

                def __init__(self):
                    self.parent = None
                    self.lldp = None
                    self.pause = None
                    self.stp_rstp_mstp = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-l2vpn-svc:L2CP-control'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.lldp is not None:
                        return True

                    if self.pause is not None:
                        return True

                    if self.stp_rstp_mstp is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                    return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc.L2CpControl']['meta_info']


            class LoadBalanceOptions(object):
                """
                Container for load balance options
                
                .. attribute:: entropy_label
                
                	Entropy label is applied to IP forwarding, L2VPN or L3VPN across MPLS network
                	**type**\:  bool
                
                .. attribute:: fat_pw
                
                	Fat label is applied to Pseudowires across MPLS network
                	**type**\:  bool
                
                .. attribute:: vxlan_source_port
                
                	Vxlan source port
                	**type**\:  str
                
                

                """

                _prefix = 'l2svc'
                _revision = '2017-02-13'

                def __init__(self):
                    self.parent = None
                    self.entropy_label = None
                    self.fat_pw = None
                    self.vxlan_source_port = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-l2vpn-svc:load-balance-options'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.entropy_label is not None:
                        return True

                    if self.fat_pw is not None:
                        return True

                    if self.vxlan_source_port is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                    return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc.LoadBalanceOptions']['meta_info']


            class CvlanIdToEvcMap(object):
                """
                List for cvlan\-id to evc map configurations
                
                .. attribute:: evc_id  <key>
                
                	EVC ID
                	**type**\:  str
                
                	**refers to**\:  :py:class:`vpn_id <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc>`
                
                .. attribute:: type  <key>
                
                	Bundling type
                	**type**\:   :py:class:`BundlingTypeIdentity <ydk.models.ietf.ietf_l2vpn_svc.BundlingTypeIdentity>`
                
                .. attribute:: cvlan_id
                
                	List of CVLAN\-ID to EVC Map configurations
                	**type**\: list of    :py:class:`CvlanId <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc.CvlanIdToEvcMap.CvlanId>`
                
                

                """

                _prefix = 'l2svc'
                _revision = '2017-02-13'

                def __init__(self):
                    self.parent = None
                    self.evc_id = None
                    self.type = None
                    self.cvlan_id = YList()
                    self.cvlan_id.parent = self
                    self.cvlan_id.name = 'cvlan_id'


                class CvlanId(object):
                    """
                    List of CVLAN\-ID to EVC Map configurations
                    
                    .. attribute:: vid  <key>
                    
                    	CVLAN ID
                    	**type**\:   :py:class:`IanaInterfaceTypeIdentity <ydk.models.ietf.iana_if_type.IanaInterfaceTypeIdentity>`
                    
                    

                    """

                    _prefix = 'l2svc'
                    _revision = '2017-02-13'

                    def __init__(self):
                        self.parent = None
                        self.vid = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.vid is None:
                            raise YPYModelError('Key property vid is None')

                        return self.parent._common_path +'/ietf-l2vpn-svc:cvlan-id[ietf-l2vpn-svc:vid = ' + str(self.vid) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.vid is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                        return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc.CvlanIdToEvcMap.CvlanId']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.evc_id is None:
                        raise YPYModelError('Key property evc_id is None')
                    if self.type is None:
                        raise YPYModelError('Key property type is None')

                    return self.parent._common_path +'/ietf-l2vpn-svc:cvlan-id-to-evc-map[ietf-l2vpn-svc:evc-id = ' + str(self.evc_id) + '][ietf-l2vpn-svc:type = ' + str(self.type) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.evc_id is not None:
                        return True

                    if self.type is not None:
                        return True

                    if self.cvlan_id is not None:
                        for child_ref in self.cvlan_id:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                    return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc.CvlanIdToEvcMap']['meta_info']


            class ServiceProtection(object):
                """
                Container of End\-to\-end Service Protection
                configurations
                
                .. attribute:: peer_evc_id
                
                	Container of peer EVC ID configurations
                	**type**\:   :py:class:`PeerEvcId <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc.ServiceProtection.PeerEvcId>`
                
                .. attribute:: protection_model
                
                	Container of protection model configurations
                	**type**\:   :py:class:`ProtectionModel <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc.ServiceProtection.ProtectionModel>`
                
                

                """

                _prefix = 'l2svc'
                _revision = '2017-02-13'

                def __init__(self):
                    self.parent = None
                    self.peer_evc_id = L2VpnSvc.VpnServices.VpnSvc.ServiceProtection.PeerEvcId()
                    self.peer_evc_id.parent = self
                    self.protection_model = L2VpnSvc.VpnServices.VpnSvc.ServiceProtection.ProtectionModel()
                    self.protection_model.parent = self


                class ProtectionModel(object):
                    """
                    Container of protection model configurations
                    
                    

                    """

                    _prefix = 'l2svc'
                    _revision = '2017-02-13'

                    def __init__(self):
                        self.parent = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-l2vpn-svc:protection-model'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                        return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc.ServiceProtection.ProtectionModel']['meta_info']


                class PeerEvcId(object):
                    """
                    Container of peer EVC ID configurations
                    
                    

                    """

                    _prefix = 'l2svc'
                    _revision = '2017-02-13'

                    def __init__(self):
                        self.parent = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-l2vpn-svc:peer-evc-id'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                        return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc.ServiceProtection.PeerEvcId']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-l2vpn-svc:service-protection'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.peer_evc_id is not None and self.peer_evc_id._has_data():
                        return True

                    if self.protection_model is not None and self.protection_model._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                    return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc.ServiceProtection']['meta_info']


            class SlaTargets(object):
                """
                Container for SLA targets
                
                

                """

                _prefix = 'l2svc'
                _revision = '2017-02-13'

                def __init__(self):
                    self.parent = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-l2vpn-svc:sla-targets'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                    return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc.SlaTargets']['meta_info']

            @property
            def _common_path(self):
                if self.vpn_id is None:
                    raise YPYModelError('Key property vpn_id is None')

                return '/ietf-l2vpn-svc:l2vpn-svc/ietf-l2vpn-svc:vpn-services/ietf-l2vpn-svc:vpn-svc[ietf-l2vpn-svc:vpn-id = ' + str(self.vpn_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.vpn_id is not None:
                    return True

                if self.ce_vlan_preservation is not None and self.ce_vlan_preservation._has_data():
                    return True

                if self.cloud_accesses is not None and self.cloud_accesses._has_data():
                    return True

                if self.cvlan_id_to_evc_map is not None:
                    for child_ref in self.cvlan_id_to_evc_map:
                        if child_ref._has_data():
                            return True

                if self.ethernet_svc_type is not None and self.ethernet_svc_type._has_data():
                    return True

                if self.evc_type is not None and self.evc_type._has_data():
                    return True

                if self.l2cp_control is not None and self.l2cp_control._has_data():
                    return True

                if self.load_balance_options is not None and self.load_balance_options._has_data():
                    return True

                if self.metro_network_id is not None and self.metro_network_id._has_data():
                    return True

                if self.ovc_type is not None and self.ovc_type._has_data():
                    return True

                if self.service_level_mac_limit is not None:
                    return True

                if self.service_protection is not None and self.service_protection._has_data():
                    return True

                if self.sla_targets is not None and self.sla_targets._has_data():
                    return True

                if self.svc_topo is not None:
                    return True

                if self.svc_type is not None:
                    return True

                if self.svlan_id_ethernet_tag is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                return meta._meta_table['L2VpnSvc.VpnServices.VpnSvc']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-l2vpn-svc:l2vpn-svc/ietf-l2vpn-svc:vpn-services'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.vpn_svc is not None:
                for child_ref in self.vpn_svc:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
            return meta._meta_table['L2VpnSvc.VpnServices']['meta_info']


    class Sites(object):
        """
        Container of site configurations
        
        .. attribute:: site
        
        	List of sites
        	**type**\: list of    :py:class:`Site <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site>`
        
        

        """

        _prefix = 'l2svc'
        _revision = '2017-02-13'

        def __init__(self):
            self.parent = None
            self.site = YList()
            self.site.parent = self
            self.site.name = 'site'


        class Site(object):
            """
            List of sites
            
            .. attribute:: site_id  <key>
            
            	Site id
            	**type**\:  str
            
            .. attribute:: site_type  <key>
            
            	Site type
            	**type**\:   :py:class:`SiteTypeIdentity <ydk.models.ietf.ietf_l2vpn_svc.SiteTypeIdentity>`
            
            .. attribute:: actual_site_start
            
            	Optional leaf indicating actual date and time when the service at a particular site actually started
            	**type**\:  str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: actual_site_stop
            
            	Optional leaf indicating actual date and time when the service at a particular site actually stopped
            	**type**\:  str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: device
            
            	Devices configuration
            	**type**\:   :py:class:`Device <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Device>`
            
            .. attribute:: load_balance_options
            
            	Container for load balance options
            	**type**\:   :py:class:`LoadBalanceOptions <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.LoadBalanceOptions>`
            
            .. attribute:: location
            
            	Location of the site
            	**type**\:   :py:class:`Location <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Location>`
            
            .. attribute:: managemnt
            
            	Container for management
            	**type**\:   :py:class:`Managemnt <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Managemnt>`
            
            .. attribute:: ports
            
            	Container of port configurations
            	**type**\:   :py:class:`Ports <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports>`
            
            .. attribute:: signaling_option
            
            	Container for signaling option
            	**type**\:   :py:class:`SignalingOption <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.SignalingOption>`
            
            .. attribute:: site_diversity
            
            	Diversity constraint type
            	**type**\:   :py:class:`SiteDiversity <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.SiteDiversity>`
            
            .. attribute:: vpn_policies
            
            	VPN policy
            	**type**\:   :py:class:`VpnPolicies <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.VpnPolicies>`
            
            

            """

            _prefix = 'l2svc'
            _revision = '2017-02-13'

            def __init__(self):
                self.parent = None
                self.site_id = None
                self.site_type = None
                self.actual_site_start = None
                self.actual_site_stop = None
                self.device = L2VpnSvc.Sites.Site.Device()
                self.device.parent = self
                self.load_balance_options = L2VpnSvc.Sites.Site.LoadBalanceOptions()
                self.load_balance_options.parent = self
                self.location = L2VpnSvc.Sites.Site.Location()
                self.location.parent = self
                self.managemnt = L2VpnSvc.Sites.Site.Managemnt()
                self.managemnt.parent = self
                self.ports = L2VpnSvc.Sites.Site.Ports()
                self.ports.parent = self
                self.signaling_option = L2VpnSvc.Sites.Site.SignalingOption()
                self.signaling_option.parent = self
                self.site_diversity = L2VpnSvc.Sites.Site.SiteDiversity()
                self.site_diversity.parent = self
                self.vpn_policies = L2VpnSvc.Sites.Site.VpnPolicies()
                self.vpn_policies.parent = self


            class Device(object):
                """
                Devices configuration
                
                .. attribute:: devices
                
                	List of devices
                	**type**\: list of    :py:class:`Devices <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Device.Devices>`
                
                

                """

                _prefix = 'l2svc'
                _revision = '2017-02-13'

                def __init__(self):
                    self.parent = None
                    self.devices = YList()
                    self.devices.parent = self
                    self.devices.name = 'devices'


                class Devices(object):
                    """
                    List of devices
                    
                    .. attribute:: device_id  <key>
                    
                    	Device ID
                    	**type**\:  str
                    
                    .. attribute:: management
                    
                    	Container for management
                    	**type**\:   :py:class:`Management <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Device.Devices.Management>`
                    
                    .. attribute:: site_name
                    
                    	Site name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'l2svc'
                    _revision = '2017-02-13'

                    def __init__(self):
                        self.parent = None
                        self.device_id = None
                        self.management = L2VpnSvc.Sites.Site.Device.Devices.Management()
                        self.management.parent = self
                        self.site_name = None


                    class Management(object):
                        """
                        Container for management
                        
                        .. attribute:: address
                        
                        	Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: management_transport
                        
                        	Transport protocol used for management
                        	**type**\:   :py:class:`AddressFamilyIdentity <ydk.models.ietf.ietf_l2vpn_svc.AddressFamilyIdentity>`
                        
                        

                        """

                        _prefix = 'l2svc'
                        _revision = '2017-02-13'

                        def __init__(self):
                            self.parent = None
                            self.address = None
                            self.management_transport = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-l2vpn-svc:management'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.address is not None:
                                return True

                            if self.management_transport is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                            return meta._meta_table['L2VpnSvc.Sites.Site.Device.Devices.Management']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.device_id is None:
                            raise YPYModelError('Key property device_id is None')

                        return self.parent._common_path +'/ietf-l2vpn-svc:devices[ietf-l2vpn-svc:device-id = ' + str(self.device_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.device_id is not None:
                            return True

                        if self.management is not None and self.management._has_data():
                            return True

                        if self.site_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                        return meta._meta_table['L2VpnSvc.Sites.Site.Device.Devices']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-l2vpn-svc:device'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.devices is not None:
                        for child_ref in self.devices:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                    return meta._meta_table['L2VpnSvc.Sites.Site.Device']['meta_info']


            class Managemnt(object):
                """
                Container for management
                
                .. attribute:: type
                
                	Management type of the connection
                	**type**\:   :py:class:`ManagementIdentity <ydk.models.ietf.ietf_l2vpn_svc.ManagementIdentity>`
                
                

                """

                _prefix = 'l2svc'
                _revision = '2017-02-13'

                def __init__(self):
                    self.parent = None
                    self.type = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-l2vpn-svc:managemnt'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                    return meta._meta_table['L2VpnSvc.Sites.Site.Managemnt']['meta_info']


            class Location(object):
                """
                Location of the site.
                
                .. attribute:: address
                
                	Address (number and street) of the site
                	**type**\:  str
                
                .. attribute:: city
                
                	City of the site
                	**type**\:  str
                
                .. attribute:: country_code
                
                	Country of the site
                	**type**\:  str
                
                .. attribute:: state
                
                	State of the site. This leaf can also be used to describe a region for country who does not have states
                	**type**\:  str
                
                .. attribute:: zip_code
                
                	ZIP code of the site
                	**type**\:  str
                
                

                """

                _prefix = 'l2svc'
                _revision = '2017-02-13'

                def __init__(self):
                    self.parent = None
                    self.address = None
                    self.city = None
                    self.country_code = None
                    self.state = None
                    self.zip_code = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-l2vpn-svc:location'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.address is not None:
                        return True

                    if self.city is not None:
                        return True

                    if self.country_code is not None:
                        return True

                    if self.state is not None:
                        return True

                    if self.zip_code is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                    return meta._meta_table['L2VpnSvc.Sites.Site.Location']['meta_info']


            class SiteDiversity(object):
                """
                Diversity constraint type.
                
                .. attribute:: groups
                
                	Groups the site is belonging to. All site network accesses will inherit those group values
                	**type**\:   :py:class:`Groups <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.SiteDiversity.Groups>`
                
                

                """

                _prefix = 'l2svc'
                _revision = '2017-02-13'

                def __init__(self):
                    self.parent = None
                    self.groups = L2VpnSvc.Sites.Site.SiteDiversity.Groups()
                    self.groups.parent = self


                class Groups(object):
                    """
                    Groups the site is belonging to.
                    All site network accesses will inherit those group
                    values.
                    
                    .. attribute:: group
                    
                    	List of group\-id
                    	**type**\: list of    :py:class:`Group <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.SiteDiversity.Groups.Group>`
                    
                    

                    """

                    _prefix = 'l2svc'
                    _revision = '2017-02-13'

                    def __init__(self):
                        self.parent = None
                        self.group = YList()
                        self.group.parent = self
                        self.group.name = 'group'


                    class Group(object):
                        """
                        List of group\-id
                        
                        .. attribute:: group_id  <key>
                        
                        	Group\-id the site is belonging to
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'l2svc'
                        _revision = '2017-02-13'

                        def __init__(self):
                            self.parent = None
                            self.group_id = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.group_id is None:
                                raise YPYModelError('Key property group_id is None')

                            return self.parent._common_path +'/ietf-l2vpn-svc:group[ietf-l2vpn-svc:group-id = ' + str(self.group_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.group_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                            return meta._meta_table['L2VpnSvc.Sites.Site.SiteDiversity.Groups.Group']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-l2vpn-svc:groups'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.group is not None:
                            for child_ref in self.group:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                        return meta._meta_table['L2VpnSvc.Sites.Site.SiteDiversity.Groups']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-l2vpn-svc:site-diversity'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.groups is not None and self.groups._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                    return meta._meta_table['L2VpnSvc.Sites.Site.SiteDiversity']['meta_info']


            class VpnPolicies(object):
                """
                VPN policy.
                
                .. attribute:: vpn_policy
                
                	List of VPN policies
                	**type**\: list of    :py:class:`VpnPolicy <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy>`
                
                

                """

                _prefix = 'l2svc'
                _revision = '2017-02-13'

                def __init__(self):
                    self.parent = None
                    self.vpn_policy = YList()
                    self.vpn_policy.parent = self
                    self.vpn_policy.name = 'vpn_policy'


                class VpnPolicy(object):
                    """
                    List of VPN policies.
                    
                    .. attribute:: vpn_policy_id  <key>
                    
                    	Unique identifier for the VPN policy
                    	**type**\:  str
                    
                    .. attribute:: entries
                    
                    	List of entries for export policy
                    	**type**\: list of    :py:class:`Entries <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy.Entries>`
                    
                    

                    """

                    _prefix = 'l2svc'
                    _revision = '2017-02-13'

                    def __init__(self):
                        self.parent = None
                        self.vpn_policy_id = None
                        self.entries = YList()
                        self.entries.parent = self
                        self.entries.name = 'entries'


                    class Entries(object):
                        """
                        List of entries for export policy.
                        
                        .. attribute:: id  <key>
                        
                        	Unique identifier for the policy entry
                        	**type**\:  str
                        
                        .. attribute:: filter
                        
                        	If used, it permit to split site LANs among multiple VPNs. If no filter used, all the LANs will be part of the same VPNs with the same role
                        	**type**\:   :py:class:`Filter <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy.Entries.Filter>`
                        
                        .. attribute:: vpn
                        
                        	List of VPNs the LAN is associated to
                        	**type**\:   :py:class:`Vpn <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy.Entries.Vpn>`
                        
                        

                        """

                        _prefix = 'l2svc'
                        _revision = '2017-02-13'

                        def __init__(self):
                            self.parent = None
                            self.id = None
                            self.filter = L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy.Entries.Filter()
                            self.filter.parent = self
                            self.vpn = L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy.Entries.Vpn()
                            self.vpn.parent = self


                        class Filter(object):
                            """
                            If used, it permit to split site LANs
                            among multiple VPNs.
                            If no filter used, all the LANs will be
                            part of the same VPNs with the same
                            role.
                            
                            .. attribute:: lan_tag
                            
                            	List of lan\-tags to be matched
                            	**type**\:  list of str
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.lan_tag = YLeafList()
                                self.lan_tag.parent = self
                                self.lan_tag.name = 'lan_tag'

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-l2vpn-svc:filter'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.lan_tag is not None:
                                    for child in self.lan_tag:
                                        if child is not None:
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy.Entries.Filter']['meta_info']


                        class Vpn(object):
                            """
                            List of VPNs the LAN is associated to.
                            
                            .. attribute:: site_role
                            
                            	Role of the site in the IPVPN
                            	**type**\:   :py:class:`SiteRoleIdentity <ydk.models.ietf.ietf_l2vpn_svc.SiteRoleIdentity>`
                            
                            	**default value**\: any-to-any-role
                            
                            .. attribute:: vpn_id
                            
                            	Reference to an IPVPN
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`vpn_id <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.site_role = None
                                self.vpn_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-l2vpn-svc:vpn'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.site_role is not None:
                                    return True

                                if self.vpn_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy.Entries.Vpn']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.id is None:
                                raise YPYModelError('Key property id is None')

                            return self.parent._common_path +'/ietf-l2vpn-svc:entries[ietf-l2vpn-svc:id = ' + str(self.id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.id is not None:
                                return True

                            if self.filter is not None and self.filter._has_data():
                                return True

                            if self.vpn is not None and self.vpn._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                            return meta._meta_table['L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy.Entries']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.vpn_policy_id is None:
                            raise YPYModelError('Key property vpn_policy_id is None')

                        return self.parent._common_path +'/ietf-l2vpn-svc:vpn-policy[ietf-l2vpn-svc:vpn-policy-id = ' + str(self.vpn_policy_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.vpn_policy_id is not None:
                            return True

                        if self.entries is not None:
                            for child_ref in self.entries:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                        return meta._meta_table['L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-l2vpn-svc:vpn-policies'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.vpn_policy is not None:
                        for child_ref in self.vpn_policy:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                    return meta._meta_table['L2VpnSvc.Sites.Site.VpnPolicies']['meta_info']


            class SignalingOption(object):
                """
                Container for signaling option
                
                .. attribute:: signaling_option
                
                	List of VPN Signaling Option
                	**type**\: list of    :py:class:`SignalingOption_ <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_>`
                
                

                """

                _prefix = 'l2svc'
                _revision = '2017-02-13'

                def __init__(self):
                    self.parent = None
                    self.signaling_option = YList()
                    self.signaling_option.parent = self
                    self.signaling_option.name = 'signaling_option'


                class SignalingOption_(object):
                    """
                    List of VPN Signaling Option.
                    
                    .. attribute:: type  <key>
                    
                    	VPN signaling types
                    	**type**\:   :py:class:`VpnSignalingTypeIdentity <ydk.models.ietf.ietf_l2vpn_svc.VpnSignalingTypeIdentity>`
                    
                    .. attribute:: control_word
                    
                    	Container of control word configurations
                    	**type**\:   :py:class:`ControlWord <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.ControlWord>`
                    
                    .. attribute:: mp_bgp_evpn
                    
                    	Container for MP BGP L2VPN
                    	**type**\:   :py:class:`MpBgpEvpn <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.MpBgpEvpn>`
                    
                    .. attribute:: mp_bgp_l2vpn
                    
                    	Container for MP BGP L2VPN
                    	**type**\:   :py:class:`MpBgpL2Vpn <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.MpBgpL2Vpn>`
                    
                    .. attribute:: pwe_encapsulation_type
                    
                    	Container of PWE Encapsulation Type configurations
                    	**type**\:   :py:class:`PweEncapsulationType <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.PweEncapsulationType>`
                    
                    .. attribute:: pwe_mtu
                    
                    	Container of PWE MTU configurations
                    	**type**\:   :py:class:`PweMtu <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.PweMtu>`
                    
                    .. attribute:: t_ldp_pwe
                    
                    	Container of T\-LDP PWE configurations
                    	**type**\:   :py:class:`TLdpPwe <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.TLdpPwe>`
                    
                    

                    """

                    _prefix = 'l2svc'
                    _revision = '2017-02-13'

                    def __init__(self):
                        self.parent = None
                        self.type = None
                        self.control_word = L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.ControlWord()
                        self.control_word.parent = self
                        self.mp_bgp_evpn = L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.MpBgpEvpn()
                        self.mp_bgp_evpn.parent = self
                        self.mp_bgp_l2vpn = L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.MpBgpL2Vpn()
                        self.mp_bgp_l2vpn.parent = self
                        self.pwe_encapsulation_type = L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.PweEncapsulationType()
                        self.pwe_encapsulation_type.parent = self
                        self.pwe_mtu = L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.PweMtu()
                        self.pwe_mtu.parent = self
                        self.t_ldp_pwe = L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.TLdpPwe()
                        self.t_ldp_pwe.parent = self


                    class MpBgpL2Vpn(object):
                        """
                        Container for MP BGP L2VPN
                        
                        .. attribute:: type
                        
                        	L2VPN types
                        	**type**\:   :py:class:`L2VpnTypeIdentity <ydk.models.ietf.ietf_l2vpn_svc.L2VpnTypeIdentity>`
                        
                        .. attribute:: vpn_id
                        
                        	Identifies the target VPN
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'l2svc'
                        _revision = '2017-02-13'

                        def __init__(self):
                            self.parent = None
                            self.type = None
                            self.vpn_id = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-l2vpn-svc:mp-bgp-l2vpn'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.type is not None:
                                return True

                            if self.vpn_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                            return meta._meta_table['L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.MpBgpL2Vpn']['meta_info']


                    class MpBgpEvpn(object):
                        """
                        Container for MP BGP L2VPN
                        
                        .. attribute:: arp_suppress
                        
                        	Indicates whether to suppress ARP broadcast
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        .. attribute:: mac_learning_mode
                        
                        	Indicates through which plane MAC addresses are advertised
                        	**type**\:   :py:class:`MacLearningModeIdentity <ydk.models.ietf.ietf_l2vpn_svc.MacLearningModeIdentity>`
                        
                        .. attribute:: type
                        
                        	L2VPN types
                        	**type**\:   :py:class:`L2VpnTypeIdentity <ydk.models.ietf.ietf_l2vpn_svc.L2VpnTypeIdentity>`
                        
                        .. attribute:: vpn_id
                        
                        	Identifies the target VPN
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'l2svc'
                        _revision = '2017-02-13'

                        def __init__(self):
                            self.parent = None
                            self.arp_suppress = None
                            self.mac_learning_mode = None
                            self.type = None
                            self.vpn_id = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-l2vpn-svc:mp-bgp-evpn'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.arp_suppress is not None:
                                return True

                            if self.mac_learning_mode is not None:
                                return True

                            if self.type is not None:
                                return True

                            if self.vpn_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                            return meta._meta_table['L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.MpBgpEvpn']['meta_info']


                    class TLdpPwe(object):
                        """
                        Container of T\-LDP PWE configurations
                        
                        .. attribute:: pe_eg_list
                        
                        	List of PE/EG
                        	**type**\: list of    :py:class:`PeEgList <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.TLdpPwe.PeEgList>`
                        
                        

                        """

                        _prefix = 'l2svc'
                        _revision = '2017-02-13'

                        def __init__(self):
                            self.parent = None
                            self.pe_eg_list = YList()
                            self.pe_eg_list.parent = self
                            self.pe_eg_list.name = 'pe_eg_list'


                        class PeEgList(object):
                            """
                            List of PE/EG
                            
                            .. attribute:: service_ip_lo_addr  <key>
                            
                            	Service ip lo address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: vc_id  <key>
                            
                            	VC id
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.service_ip_lo_addr = None
                                self.vc_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.service_ip_lo_addr is None:
                                    raise YPYModelError('Key property service_ip_lo_addr is None')
                                if self.vc_id is None:
                                    raise YPYModelError('Key property vc_id is None')

                                return self.parent._common_path +'/ietf-l2vpn-svc:PE-EG-list[ietf-l2vpn-svc:service-ip-lo-addr = ' + str(self.service_ip_lo_addr) + '][ietf-l2vpn-svc:vc-id = ' + str(self.vc_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.service_ip_lo_addr is not None:
                                    return True

                                if self.vc_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.TLdpPwe.PeEgList']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-l2vpn-svc:t-ldp-pwe'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.pe_eg_list is not None:
                                for child_ref in self.pe_eg_list:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                            return meta._meta_table['L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.TLdpPwe']['meta_info']


                    class PweEncapsulationType(object):
                        """
                        Container of PWE Encapsulation Type configurations
                        
                        .. attribute:: ethernet
                        
                        	Ethernet
                        	**type**\:  bool
                        
                        .. attribute:: vlan
                        
                        	VLAN
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'l2svc'
                        _revision = '2017-02-13'

                        def __init__(self):
                            self.parent = None
                            self.ethernet = None
                            self.vlan = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-l2vpn-svc:pwe-encapsulation-type'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.ethernet is not None:
                                return True

                            if self.vlan is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                            return meta._meta_table['L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.PweEncapsulationType']['meta_info']


                    class PweMtu(object):
                        """
                        Container of PWE MTU configurations
                        
                        .. attribute:: allow_mtu_mismatch
                        
                        	Allow MTU mismatch
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'l2svc'
                        _revision = '2017-02-13'

                        def __init__(self):
                            self.parent = None
                            self.allow_mtu_mismatch = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-l2vpn-svc:pwe-mtu'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.allow_mtu_mismatch is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                            return meta._meta_table['L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.PweMtu']['meta_info']


                    class ControlWord(object):
                        """
                        Container of control word configurations
                        
                        

                        """

                        _prefix = 'l2svc'
                        _revision = '2017-02-13'

                        def __init__(self):
                            self.parent = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-l2vpn-svc:control-word'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                            return meta._meta_table['L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.ControlWord']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.type is None:
                            raise YPYModelError('Key property type is None')

                        return self.parent._common_path +'/ietf-l2vpn-svc:signaling-option[ietf-l2vpn-svc:type = ' + str(self.type) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.type is not None:
                            return True

                        if self.control_word is not None and self.control_word._has_data():
                            return True

                        if self.mp_bgp_evpn is not None and self.mp_bgp_evpn._has_data():
                            return True

                        if self.mp_bgp_l2vpn is not None and self.mp_bgp_l2vpn._has_data():
                            return True

                        if self.pwe_encapsulation_type is not None and self.pwe_encapsulation_type._has_data():
                            return True

                        if self.pwe_mtu is not None and self.pwe_mtu._has_data():
                            return True

                        if self.t_ldp_pwe is not None and self.t_ldp_pwe._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                        return meta._meta_table['L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-l2vpn-svc:signaling-option'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.signaling_option is not None:
                        for child_ref in self.signaling_option:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                    return meta._meta_table['L2VpnSvc.Sites.Site.SignalingOption']['meta_info']


            class LoadBalanceOptions(object):
                """
                Container for load balance options
                
                .. attribute:: entropy_label
                
                	Entropy label is applied to IP forwarding, L2VPN or L3VPN across MPLS network
                	**type**\:  bool
                
                .. attribute:: fat_pw
                
                	Fat label is applied to Pseudowires across MPLS network
                	**type**\:  bool
                
                .. attribute:: vxlan_source_port
                
                	Vxlan source port
                	**type**\:  str
                
                

                """

                _prefix = 'l2svc'
                _revision = '2017-02-13'

                def __init__(self):
                    self.parent = None
                    self.entropy_label = None
                    self.fat_pw = None
                    self.vxlan_source_port = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-l2vpn-svc:load-balance-options'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.entropy_label is not None:
                        return True

                    if self.fat_pw is not None:
                        return True

                    if self.vxlan_source_port is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                    return meta._meta_table['L2VpnSvc.Sites.Site.LoadBalanceOptions']['meta_info']


            class Ports(object):
                """
                Container of port configurations
                
                .. attribute:: port
                
                	List of ports
                	**type**\: list of    :py:class:`Port <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port>`
                
                

                """

                _prefix = 'l2svc'
                _revision = '2017-02-13'

                def __init__(self):
                    self.parent = None
                    self.port = YList()
                    self.port.parent = self
                    self.port.name = 'port'


                class Port(object):
                    """
                    List of ports
                    
                    .. attribute:: network_access_id  <key>
                    
                    	Identifier of network access
                    	**type**\:  str
                    
                    .. attribute:: access_diversity
                    
                    	Diversity parameters
                    	**type**\:   :py:class:`AccessDiversity <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity>`
                    
                    .. attribute:: availability
                    
                    	Container of availability optional configurations
                    	**type**\:   :py:class:`Availability <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.Availability>`
                    
                    .. attribute:: bearer
                    
                    	Bearer specific parameters. To be augmented
                    	**type**\:   :py:class:`Bearer <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.Bearer>`
                    
                    .. attribute:: ethernet_connection
                    
                    	Container for bearer
                    	**type**\:   :py:class:`EthernetConnection <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection>`
                    
                    .. attribute:: ethernet_service_oam
                    
                    	Container for Ethernet service OAM
                    	**type**\:   :py:class:`EthernetServiceOam <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam>`
                    
                    .. attribute:: evc_mtu
                    
                    	EVC MTU
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: l2cp_control
                    
                    	Container of L2CP control configurations
                    	**type**\:   :py:class:`L2CpControl <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.L2CpControl>`
                    
                    .. attribute:: remote_carrier_name
                    
                    	Remote carrier name
                    	**type**\:  str
                    
                    .. attribute:: security_filtering
                    
                    	Security parameters
                    	**type**\:   :py:class:`SecurityFiltering <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering>`
                    
                    .. attribute:: service
                    
                    	Container for service
                    	**type**\:   :py:class:`Service <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.Service>`
                    
                    .. attribute:: vpn_attachment
                    
                    	Defines VPN attachment of a site
                    	**type**\:   :py:class:`VpnAttachment <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.VpnAttachment>`
                    
                    

                    """

                    _prefix = 'l2svc'
                    _revision = '2017-02-13'

                    def __init__(self):
                        self.parent = None
                        self.network_access_id = None
                        self.access_diversity = L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity()
                        self.access_diversity.parent = self
                        self.availability = L2VpnSvc.Sites.Site.Ports.Port.Availability()
                        self.availability.parent = self
                        self.bearer = L2VpnSvc.Sites.Site.Ports.Port.Bearer()
                        self.bearer.parent = self
                        self.ethernet_connection = L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection()
                        self.ethernet_connection.parent = self
                        self.ethernet_service_oam = L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam()
                        self.ethernet_service_oam.parent = self
                        self.evc_mtu = None
                        self.l2cp_control = L2VpnSvc.Sites.Site.Ports.Port.L2CpControl()
                        self.l2cp_control.parent = self
                        self.remote_carrier_name = None
                        self.security_filtering = L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering()
                        self.security_filtering.parent = self
                        self.service = L2VpnSvc.Sites.Site.Ports.Port.Service()
                        self.service.parent = self
                        self.vpn_attachment = L2VpnSvc.Sites.Site.Ports.Port.VpnAttachment()
                        self.vpn_attachment.parent = self


                    class AccessDiversity(object):
                        """
                        Diversity parameters.
                        
                        .. attribute:: constraints
                        
                        	Constraints for placing this site  network access
                        	**type**\:   :py:class:`Constraints <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints>`
                        
                        .. attribute:: groups
                        
                        	Groups the fate sharing group member is belonging to
                        	**type**\:   :py:class:`Groups <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Groups>`
                        
                        

                        """

                        _prefix = 'l2svc'
                        _revision = '2017-02-13'

                        def __init__(self):
                            self.parent = None
                            self.constraints = L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints()
                            self.constraints.parent = self
                            self.groups = L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Groups()
                            self.groups.parent = self


                        class Groups(object):
                            """
                            Groups the fate sharing group member
                            is belonging to
                            
                            .. attribute:: fate_sharing_group_size
                            
                            	Fate sharing group size
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: group
                            
                            	List of group\-id
                            	**type**\: list of    :py:class:`Group <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Groups.Group>`
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.fate_sharing_group_size = None
                                self.group = YList()
                                self.group.parent = self
                                self.group.name = 'group'


                            class Group(object):
                                """
                                List of group\-id
                                
                                .. attribute:: group_id  <key>
                                
                                	Group\-id the site network access is belonging to
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'l2svc'
                                _revision = '2017-02-13'

                                def __init__(self):
                                    self.parent = None
                                    self.group_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.group_id is None:
                                        raise YPYModelError('Key property group_id is None')

                                    return self.parent._common_path +'/ietf-l2vpn-svc:group[ietf-l2vpn-svc:group-id = ' + str(self.group_id) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.group_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                    return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Groups.Group']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-l2vpn-svc:groups'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.fate_sharing_group_size is not None:
                                    return True

                                if self.group is not None:
                                    for child_ref in self.group:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Groups']['meta_info']


                        class Constraints(object):
                            """
                            Constraints for placing this site
                             network access
                            
                            .. attribute:: constraint
                            
                            	List of constraints
                            	**type**\: list of    :py:class:`Constraint <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints.Constraint>`
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.constraint = YList()
                                self.constraint.parent = self
                                self.constraint.name = 'constraint'


                            class Constraint(object):
                                """
                                List of constraints
                                
                                .. attribute:: constraint_type  <key>
                                
                                	Diversity constraint type
                                	**type**\:   :py:class:`PlacementDiversityIdentity <ydk.models.ietf.ietf_l2vpn_svc.PlacementDiversityIdentity>`
                                
                                .. attribute:: target
                                
                                	The constraint will apply against this list of groups
                                	**type**\:   :py:class:`Target <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints.Constraint.Target>`
                                
                                

                                """

                                _prefix = 'l2svc'
                                _revision = '2017-02-13'

                                def __init__(self):
                                    self.parent = None
                                    self.constraint_type = None
                                    self.target = L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints.Constraint.Target()
                                    self.target.parent = self


                                class Target(object):
                                    """
                                    The constraint will apply against
                                    this list of groups
                                    
                                    .. attribute:: all_other_accesses
                                    
                                    	The constraint will apply against all other site network access of this site
                                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: all_other_groups
                                    
                                    	The constraint will apply against all other groups the customer is managing
                                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: group
                                    
                                    	List of groups
                                    	**type**\: list of    :py:class:`Group <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints.Constraint.Target.Group>`
                                    
                                    

                                    """

                                    _prefix = 'l2svc'
                                    _revision = '2017-02-13'

                                    def __init__(self):
                                        self.parent = None
                                        self.all_other_accesses = None
                                        self.all_other_groups = None
                                        self.group = YList()
                                        self.group.parent = self
                                        self.group.name = 'group'


                                    class Group(object):
                                        """
                                        List of groups
                                        
                                        .. attribute:: group_id  <key>
                                        
                                        	The constraint will apply against this particular group\-id
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'l2svc'
                                        _revision = '2017-02-13'

                                        def __init__(self):
                                            self.parent = None
                                            self.group_id = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.group_id is None:
                                                raise YPYModelError('Key property group_id is None')

                                            return self.parent._common_path +'/ietf-l2vpn-svc:group[ietf-l2vpn-svc:group-id = ' + str(self.group_id) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.group_id is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                            return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints.Constraint.Target.Group']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-l2vpn-svc:target'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.all_other_accesses is not None:
                                            return True

                                        if self.all_other_groups is not None:
                                            return True

                                        if self.group is not None:
                                            for child_ref in self.group:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                        return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints.Constraint.Target']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.constraint_type is None:
                                        raise YPYModelError('Key property constraint_type is None')

                                    return self.parent._common_path +'/ietf-l2vpn-svc:constraint[ietf-l2vpn-svc:constraint-type = ' + str(self.constraint_type) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.constraint_type is not None:
                                        return True

                                    if self.target is not None and self.target._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                    return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints.Constraint']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-l2vpn-svc:constraints'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.constraint is not None:
                                    for child_ref in self.constraint:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-l2vpn-svc:access-diversity'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.constraints is not None and self.constraints._has_data():
                                return True

                            if self.groups is not None and self.groups._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                            return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity']['meta_info']


                    class Bearer(object):
                        """
                        Bearer specific parameters.
                        To be augmented.
                        
                        .. attribute:: always_on
                        
                        	Request for an always on access type. This means no Dial access type for example
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        .. attribute:: bearer_reference
                        
                        	This is an internal reference for the service provider
                        	**type**\:  str
                        
                        .. attribute:: requested_type
                        
                        	Container for requested type
                        	**type**\:   :py:class:`RequestedType <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.Bearer.RequestedType>`
                        
                        

                        """

                        _prefix = 'l2svc'
                        _revision = '2017-02-13'

                        def __init__(self):
                            self.parent = None
                            self.always_on = None
                            self.bearer_reference = None
                            self.requested_type = L2VpnSvc.Sites.Site.Ports.Port.Bearer.RequestedType()
                            self.requested_type.parent = self


                        class RequestedType(object):
                            """
                            Container for requested type.
                            
                            .. attribute:: request_type_profile
                            
                            	Container for request type profile
                            	**type**\:   :py:class:`RequestTypeProfile <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.Bearer.RequestedType.RequestTypeProfile>`
                            
                            .. attribute:: requested_type
                            
                            	Type of requested bearer Ethernet, DSL, Wireless ... Operator specific
                            	**type**\:  str
                            
                            .. attribute:: strict
                            
                            	Define if the requested\-type is a preference or a strict requirement
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.request_type_profile = L2VpnSvc.Sites.Site.Ports.Port.Bearer.RequestedType.RequestTypeProfile()
                                self.request_type_profile.parent = self
                                self.requested_type = None
                                self.strict = None


                            class RequestTypeProfile(object):
                                """
                                Container for request type profile.
                                
                                .. attribute:: circuit_id
                                
                                	Circuit ID
                                	**type**\:  str
                                
                                .. attribute:: dot1q
                                
                                	Container for dot1q
                                	**type**\:   :py:class:`Dot1Q <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.Bearer.RequestedType.RequestTypeProfile.Dot1Q>`
                                
                                .. attribute:: physical_if
                                
                                	Physical interface
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'l2svc'
                                _revision = '2017-02-13'

                                def __init__(self):
                                    self.parent = None
                                    self.circuit_id = None
                                    self.dot1q = L2VpnSvc.Sites.Site.Ports.Port.Bearer.RequestedType.RequestTypeProfile.Dot1Q()
                                    self.dot1q.parent = self
                                    self.physical_if = None


                                class Dot1Q(object):
                                    """
                                    Container for dot1q.
                                    
                                    .. attribute:: physical_if
                                    
                                    	Physical interface
                                    	**type**\:  str
                                    
                                    .. attribute:: vlan_id
                                    
                                    	VLAN ID
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'l2svc'
                                    _revision = '2017-02-13'

                                    def __init__(self):
                                        self.parent = None
                                        self.physical_if = None
                                        self.vlan_id = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-l2vpn-svc:dot1q'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.physical_if is not None:
                                            return True

                                        if self.vlan_id is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                        return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.Bearer.RequestedType.RequestTypeProfile.Dot1Q']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/ietf-l2vpn-svc:request-type-profile'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.circuit_id is not None:
                                        return True

                                    if self.dot1q is not None and self.dot1q._has_data():
                                        return True

                                    if self.physical_if is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                    return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.Bearer.RequestedType.RequestTypeProfile']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-l2vpn-svc:requested-type'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.request_type_profile is not None and self.request_type_profile._has_data():
                                    return True

                                if self.requested_type is not None:
                                    return True

                                if self.strict is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.Bearer.RequestedType']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-l2vpn-svc:bearer'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.always_on is not None:
                                return True

                            if self.bearer_reference is not None:
                                return True

                            if self.requested_type is not None and self.requested_type._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                            return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.Bearer']['meta_info']


                    class EthernetConnection(object):
                        """
                        Container for bearer
                        
                        .. attribute:: dot1q
                        
                        	Qot1q
                        	**type**\:   :py:class:`Dot1Q <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Dot1Q>`
                        
                        .. attribute:: esi
                        
                        	Ethernet segment id
                        	**type**\:  str
                        
                        .. attribute:: interface_description
                        
                        	Interface description
                        	**type**\:  str
                        
                        .. attribute:: lag_interface
                        
                        	Container of LAG interface attributes configuration
                        	**type**\:   :py:class:`LagInterface <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface>`
                        
                        .. attribute:: phy_interface
                        
                        	Container of PHY Interface Attributes configurations
                        	**type**\:   :py:class:`PhyInterface <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.PhyInterface>`
                        
                        .. attribute:: qinq
                        
                        	QinQ
                        	**type**\:   :py:class:`Qinq <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Qinq>`
                        
                        .. attribute:: sub_if_id
                        
                        	Sub interface ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: vlan
                        
                        	Abstract container for VLAN
                        	**type**\:   :py:class:`Vlan <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Vlan>`
                        
                        .. attribute:: vxlan
                        
                        	QinQ
                        	**type**\:   :py:class:`Vxlan <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Vxlan>`
                        
                        

                        """

                        _prefix = 'l2svc'
                        _revision = '2017-02-13'

                        def __init__(self):
                            self.parent = None
                            self.dot1q = L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Dot1Q()
                            self.dot1q.parent = self
                            self.esi = None
                            self.interface_description = None
                            self.lag_interface = L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface()
                            self.lag_interface.parent = self
                            self.phy_interface = L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.PhyInterface()
                            self.phy_interface.parent = self
                            self.qinq = L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Qinq()
                            self.qinq.parent = self
                            self.sub_if_id = None
                            self.vlan = L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Vlan()
                            self.vlan.parent = self
                            self.vxlan = L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Vxlan()
                            self.vxlan.parent = self


                        class Vlan(object):
                            """
                            Abstract container for VLAN
                            
                            .. attribute:: vlan_id
                            
                            	VLAN\-ID/Ethernet Tag configurations
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.vlan_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-l2vpn-svc:vlan'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.vlan_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Vlan']['meta_info']


                        class Dot1Q(object):
                            """
                            Qot1q
                            
                            .. attribute:: physical_inf
                            
                            	Physical Interface
                            	**type**\:  str
                            
                            .. attribute:: vlan_id
                            
                            	VLAN identifier
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.physical_inf = None
                                self.vlan_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-l2vpn-svc:dot1q'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.physical_inf is not None:
                                    return True

                                if self.vlan_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Dot1Q']['meta_info']


                        class Qinq(object):
                            """
                            QinQ
                            
                            .. attribute:: c_vlan_id
                            
                            	C\-VLAN Identifier
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: s_vlan_id
                            
                            	S\-VLAN Identifier
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.c_vlan_id = None
                                self.s_vlan_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-l2vpn-svc:qinq'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.c_vlan_id is not None:
                                    return True

                                if self.s_vlan_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Qinq']['meta_info']


                        class Vxlan(object):
                            """
                            QinQ
                            
                            .. attribute:: peer_list
                            
                            	List for peer IP
                            	**type**\: list of    :py:class:`PeerList <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Vxlan.PeerList>`
                            
                            .. attribute:: vni_id
                            
                            	VNI Identifier
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.peer_list = YList()
                                self.peer_list.parent = self
                                self.peer_list.name = 'peer_list'
                                self.vni_id = None


                            class PeerList(object):
                                """
                                List for peer IP
                                
                                .. attribute:: peer_ip  <key>
                                
                                	Peer IP
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                

                                """

                                _prefix = 'l2svc'
                                _revision = '2017-02-13'

                                def __init__(self):
                                    self.parent = None
                                    self.peer_ip = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.peer_ip is None:
                                        raise YPYModelError('Key property peer_ip is None')

                                    return self.parent._common_path +'/ietf-l2vpn-svc:peer-list[ietf-l2vpn-svc:peer-ip = ' + str(self.peer_ip) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.peer_ip is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                    return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Vxlan.PeerList']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-l2vpn-svc:vxlan'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.peer_list is not None:
                                    for child_ref in self.peer_list:
                                        if child_ref._has_data():
                                            return True

                                if self.vni_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Vxlan']['meta_info']


                        class PhyInterface(object):
                            """
                            Container of PHY Interface Attributes configurations
                            
                            .. attribute:: encapsulation_type
                            
                            	Encapsulation\-type
                            	**type**\:   :py:class:`EncapsulationTypeEnum <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.PhyInterface.EncapsulationTypeEnum>`
                            
                            .. attribute:: ethertype
                            
                            	Ethertype
                            	**type**\:  str
                            
                            .. attribute:: flow_control
                            
                            	Flow control
                            	**type**\:  str
                            
                            .. attribute:: lldp
                            
                            	LLDP
                            	**type**\:  bool
                            
                            .. attribute:: mode
                            
                            	Negotiation mode
                            	**type**\:   :py:class:`NegModeEnum <ydk.models.ietf.ietf_l2vpn_svc.NegModeEnum>`
                            
                            .. attribute:: oam_802_3ah_link
                            
                            	Container for oam 802.3 ah link
                            	**type**\:   :py:class:`Oam802__Dot__3AhLink <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.PhyInterface.Oam802__Dot__3AhLink>`
                            
                            .. attribute:: phy_mtu
                            
                            	PHY MTU
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: port_number
                            
                            	Port number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: port_speed
                            
                            	Port speed
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: uni_loop_prevention
                            
                            	If this leaf set to truth that the port automatically goes down when a physical loopback is detect
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.encapsulation_type = None
                                self.ethertype = None
                                self.flow_control = None
                                self.lldp = None
                                self.mode = None
                                self.oam_802_3ah_link = L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.PhyInterface.Oam802__Dot__3AhLink()
                                self.oam_802_3ah_link.parent = self
                                self.phy_mtu = None
                                self.port_number = None
                                self.port_speed = None
                                self.uni_loop_prevention = None

                            class EncapsulationTypeEnum(Enum):
                                """
                                EncapsulationTypeEnum

                                Encapsulation\-type

                                .. data:: VLAN = 0

                                	VLAN

                                .. data:: Ethernet = 1

                                	Ethernet

                                """

                                VLAN = 0

                                Ethernet = 1


                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                    return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.PhyInterface.EncapsulationTypeEnum']



                            class Oam802__Dot__3AhLink(object):
                                """
                                Container for oam 802.3 ah link.
                                
                                .. attribute:: enable
                                
                                	Indicate whether support oam 802.3 ah link
                                	**type**\:  bool
                                
                                

                                """

                                _prefix = 'l2svc'
                                _revision = '2017-02-13'

                                def __init__(self):
                                    self.parent = None
                                    self.enable = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/ietf-l2vpn-svc:oam-802.3AH-link'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.enable is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                    return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.PhyInterface.Oam802__Dot__3AhLink']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-l2vpn-svc:phy-interface'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.encapsulation_type is not None:
                                    return True

                                if self.ethertype is not None:
                                    return True

                                if self.flow_control is not None:
                                    return True

                                if self.lldp is not None:
                                    return True

                                if self.mode is not None:
                                    return True

                                if self.oam_802_3ah_link is not None and self.oam_802_3ah_link._has_data():
                                    return True

                                if self.phy_mtu is not None:
                                    return True

                                if self.port_number is not None:
                                    return True

                                if self.port_speed is not None:
                                    return True

                                if self.uni_loop_prevention is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.PhyInterface']['meta_info']


                        class LagInterface(object):
                            """
                            Container of LAG interface attributes configuration
                            
                            .. attribute:: lag_interface
                            
                            	List of LAG interfaces
                            	**type**\: list of    :py:class:`LagInterface_ <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_>`
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.lag_interface = YList()
                                self.lag_interface.parent = self
                                self.lag_interface.name = 'lag_interface'


                            class LagInterface_(object):
                                """
                                List of LAG interfaces
                                
                                .. attribute:: lag_interface_number  <key>
                                
                                	LAG interface number
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lacp
                                
                                	LACP
                                	**type**\:   :py:class:`Lacp <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp>`
                                
                                

                                """

                                _prefix = 'l2svc'
                                _revision = '2017-02-13'

                                def __init__(self):
                                    self.parent = None
                                    self.lag_interface_number = None
                                    self.lacp = L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp()
                                    self.lacp.parent = self


                                class Lacp(object):
                                    """
                                    LACP
                                    
                                    .. attribute:: bfd
                                    
                                    	Container for BFD
                                    	**type**\:   :py:class:`Bfd <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.Bfd>`
                                    
                                    .. attribute:: encapsulation_type
                                    
                                    	Encapsulation type
                                    	**type**\:   :py:class:`EncapsulationTypeEnum <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.EncapsulationTypeEnum>`
                                    
                                    .. attribute:: ethertype
                                    
                                    	Ether type
                                    	**type**\:  str
                                    
                                    .. attribute:: flow_control
                                    
                                    	Flow control
                                    	**type**\:  str
                                    
                                    .. attribute:: lacp_mode
                                    
                                    	LACP mode
                                    	**type**\:  bool
                                    
                                    .. attribute:: lacp_speed
                                    
                                    	LACP speed
                                    	**type**\:  bool
                                    
                                    .. attribute:: lacp_state
                                    
                                    	LACP on/off
                                    	**type**\:  bool
                                    
                                    .. attribute:: lldp
                                    
                                    	LLDP
                                    	**type**\:  bool
                                    
                                    .. attribute:: member_link_list
                                    
                                    	Container of Member link list
                                    	**type**\:   :py:class:`MemberLinkList <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MemberLinkList>`
                                    
                                    .. attribute:: micro_bfd
                                    
                                    	Container of Micro\-BFD configurations
                                    	**type**\:   :py:class:`MicroBfd <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MicroBfd>`
                                    
                                    .. attribute:: mini_link
                                    
                                    	Mini link
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: system_priority
                                    
                                    	Indicates the LACP priority for the system. The range is from 0 to 65535. The default is 32768
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'l2svc'
                                    _revision = '2017-02-13'

                                    def __init__(self):
                                        self.parent = None
                                        self.bfd = L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.Bfd()
                                        self.bfd.parent = self
                                        self.encapsulation_type = None
                                        self.ethertype = None
                                        self.flow_control = None
                                        self.lacp_mode = None
                                        self.lacp_speed = None
                                        self.lacp_state = None
                                        self.lldp = None
                                        self.member_link_list = L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MemberLinkList()
                                        self.member_link_list.parent = self
                                        self.micro_bfd = L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MicroBfd()
                                        self.micro_bfd.parent = self
                                        self.mini_link = None
                                        self.system_priority = None

                                    class EncapsulationTypeEnum(Enum):
                                        """
                                        EncapsulationTypeEnum

                                        Encapsulation type

                                        .. data:: VLAN = 0

                                        	VLAN

                                        .. data:: ether = 1

                                        	Ethernet

                                        """

                                        VLAN = 0

                                        ether = 1


                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                            return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.EncapsulationTypeEnum']



                                    class MicroBfd(object):
                                        """
                                        Container of Micro\-BFD configurations
                                        
                                        .. attribute:: bfd_hold_timer
                                        
                                        	BFD hold timer
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: bfd_interval
                                        
                                        	BFD interval
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: micro_bfd_on_off
                                        
                                        	Micro BFD ON/OFF
                                        	**type**\:   :py:class:`MicroBfdOnOffEnum <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MicroBfd.MicroBfdOnOffEnum>`
                                        
                                        

                                        """

                                        _prefix = 'l2svc'
                                        _revision = '2017-02-13'

                                        def __init__(self):
                                            self.parent = None
                                            self.bfd_hold_timer = None
                                            self.bfd_interval = None
                                            self.micro_bfd_on_off = None

                                        class MicroBfdOnOffEnum(Enum):
                                            """
                                            MicroBfdOnOffEnum

                                            Micro BFD ON/OFF

                                            .. data:: on = 0

                                            	Micro-bfd on

                                            .. data:: off = 1

                                            	Micro-bfd off

                                            """

                                            on = 0

                                            off = 1


                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MicroBfd.MicroBfdOnOffEnum']


                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/ietf-l2vpn-svc:Micro-BFD'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.bfd_hold_timer is not None:
                                                return True

                                            if self.bfd_interval is not None:
                                                return True

                                            if self.micro_bfd_on_off is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                            return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MicroBfd']['meta_info']


                                    class Bfd(object):
                                        """
                                        Container for BFD.
                                        
                                        .. attribute:: bfd_enabled
                                        
                                        	BFD activation
                                        	**type**\:  bool
                                        
                                        .. attribute:: fixed_value
                                        
                                        	Expected hold time expressed in msec
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**units**\: msec
                                        
                                        .. attribute:: profile_name
                                        
                                        	Service provider well known profile
                                        	**type**\:  str
                                        
                                        

                                        """

                                        _prefix = 'l2svc'
                                        _revision = '2017-02-13'

                                        def __init__(self):
                                            self.parent = None
                                            self.bfd_enabled = None
                                            self.fixed_value = None
                                            self.profile_name = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/ietf-l2vpn-svc:bfd'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.bfd_enabled is not None:
                                                return True

                                            if self.fixed_value is not None:
                                                return True

                                            if self.profile_name is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                            return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.Bfd']['meta_info']


                                    class MemberLinkList(object):
                                        """
                                        Container of Member link list
                                        
                                        .. attribute:: member_link
                                        
                                        	Member link
                                        	**type**\: list of    :py:class:`MemberLink <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MemberLinkList.MemberLink>`
                                        
                                        

                                        """

                                        _prefix = 'l2svc'
                                        _revision = '2017-02-13'

                                        def __init__(self):
                                            self.parent = None
                                            self.member_link = YList()
                                            self.member_link.parent = self
                                            self.member_link.name = 'member_link'


                                        class MemberLink(object):
                                            """
                                            Member link
                                            
                                            .. attribute:: name  <key>
                                            
                                            	Member link name
                                            	**type**\:  str
                                            
                                            .. attribute:: mode
                                            
                                            	Negotiation mode
                                            	**type**\:   :py:class:`NegModeEnum <ydk.models.ietf.ietf_l2vpn_svc.NegModeEnum>`
                                            
                                            .. attribute:: mtu
                                            
                                            	MTU
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: oam_802_3ah_link
                                            
                                            	Container for oam 802.3 ah link
                                            	**type**\:   :py:class:`Oam802__Dot__3AhLink <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MemberLinkList.MemberLink.Oam802__Dot__3AhLink>`
                                            
                                            .. attribute:: port_speed
                                            
                                            	Port speed
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'l2svc'
                                            _revision = '2017-02-13'

                                            def __init__(self):
                                                self.parent = None
                                                self.name = None
                                                self.mode = None
                                                self.mtu = None
                                                self.oam_802_3ah_link = L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MemberLinkList.MemberLink.Oam802__Dot__3AhLink()
                                                self.oam_802_3ah_link.parent = self
                                                self.port_speed = None


                                            class Oam802__Dot__3AhLink(object):
                                                """
                                                Container for oam 802.3 ah link.
                                                
                                                .. attribute:: enable
                                                
                                                	Indicate whether support oam 802.3 ah link
                                                	**type**\:  bool
                                                
                                                

                                                """

                                                _prefix = 'l2svc'
                                                _revision = '2017-02-13'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.enable = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/ietf-l2vpn-svc:oam-802.3AH-link'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return True

                                                def _has_data(self):
                                                    if not self.is_config():
                                                        return False
                                                    if self.enable is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                                    return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MemberLinkList.MemberLink.Oam802__Dot__3AhLink']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.name is None:
                                                    raise YPYModelError('Key property name is None')

                                                return self.parent._common_path +'/ietf-l2vpn-svc:member-link[ietf-l2vpn-svc:name = ' + str(self.name) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.name is not None:
                                                    return True

                                                if self.mode is not None:
                                                    return True

                                                if self.mtu is not None:
                                                    return True

                                                if self.oam_802_3ah_link is not None and self.oam_802_3ah_link._has_data():
                                                    return True

                                                if self.port_speed is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MemberLinkList.MemberLink']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/ietf-l2vpn-svc:Member-link-list'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.member_link is not None:
                                                for child_ref in self.member_link:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                            return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MemberLinkList']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-l2vpn-svc:LACP'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.bfd is not None and self.bfd._has_data():
                                            return True

                                        if self.encapsulation_type is not None:
                                            return True

                                        if self.ethertype is not None:
                                            return True

                                        if self.flow_control is not None:
                                            return True

                                        if self.lacp_mode is not None:
                                            return True

                                        if self.lacp_speed is not None:
                                            return True

                                        if self.lacp_state is not None:
                                            return True

                                        if self.lldp is not None:
                                            return True

                                        if self.member_link_list is not None and self.member_link_list._has_data():
                                            return True

                                        if self.micro_bfd is not None and self.micro_bfd._has_data():
                                            return True

                                        if self.mini_link is not None:
                                            return True

                                        if self.system_priority is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                        return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.lag_interface_number is None:
                                        raise YPYModelError('Key property lag_interface_number is None')

                                    return self.parent._common_path +'/ietf-l2vpn-svc:LAG-interface[ietf-l2vpn-svc:LAG-interface-number = ' + str(self.lag_interface_number) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.lag_interface_number is not None:
                                        return True

                                    if self.lacp is not None and self.lacp._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                    return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-l2vpn-svc:LAG-interface'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.lag_interface is not None:
                                    for child_ref in self.lag_interface:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-l2vpn-svc:ethernet-connection'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.dot1q is not None and self.dot1q._has_data():
                                return True

                            if self.esi is not None:
                                return True

                            if self.interface_description is not None:
                                return True

                            if self.lag_interface is not None and self.lag_interface._has_data():
                                return True

                            if self.phy_interface is not None and self.phy_interface._has_data():
                                return True

                            if self.qinq is not None and self.qinq._has_data():
                                return True

                            if self.sub_if_id is not None:
                                return True

                            if self.vlan is not None and self.vlan._has_data():
                                return True

                            if self.vxlan is not None and self.vxlan._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                            return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection']['meta_info']


                    class L2CpControl(object):
                        """
                        Container of L2CP control configurations
                        
                        .. attribute:: e_lmi
                        
                        	E\-LMI
                        	**type**\:   :py:class:`ControlModeEnum <ydk.models.ietf.ietf_l2vpn_svc.ControlModeEnum>`
                        
                        .. attribute:: esmc
                        
                        	ESMC
                        	**type**\:   :py:class:`ControlModeEnum <ydk.models.ietf.ietf_l2vpn_svc.ControlModeEnum>`
                        
                        .. attribute:: garp_mrp
                        
                        	GARP/MRP
                        	**type**\:   :py:class:`ControlModeEnum <ydk.models.ietf.ietf_l2vpn_svc.ControlModeEnum>`
                        
                        .. attribute:: l2cp_802_1x
                        
                        	802.x
                        	**type**\:   :py:class:`ControlModeEnum <ydk.models.ietf.ietf_l2vpn_svc.ControlModeEnum>`
                        
                        .. attribute:: lacp_lamp
                        
                        	LACP/LAMP
                        	**type**\:   :py:class:`ControlModeEnum <ydk.models.ietf.ietf_l2vpn_svc.ControlModeEnum>`
                        
                        .. attribute:: link_oam
                        
                        	Link OAM
                        	**type**\:   :py:class:`ControlModeEnum <ydk.models.ietf.ietf_l2vpn_svc.ControlModeEnum>`
                        
                        .. attribute:: lldp
                        
                        	LLDP
                        	**type**\:  bool
                        
                        .. attribute:: pause
                        
                        	Pause
                        	**type**\:   :py:class:`ControlModeEnum <ydk.models.ietf.ietf_l2vpn_svc.ControlModeEnum>`
                        
                        .. attribute:: provider_bridge_group
                        
                        	Provider bridge group reserved MAC address 01\-80\-C2\-00\-00\-08
                        	**type**\:   :py:class:`ControlModeEnum <ydk.models.ietf.ietf_l2vpn_svc.ControlModeEnum>`
                        
                        .. attribute:: provider_bridge_mvrp
                        
                        	Provider bridge MVRP reserved MAC address 01\-80\-C2\-00\-00\-0D
                        	**type**\:   :py:class:`ControlModeEnum <ydk.models.ietf.ietf_l2vpn_svc.ControlModeEnum>`
                        
                        .. attribute:: ptp_peer_delay
                        
                        	PTP peer delay
                        	**type**\:   :py:class:`ControlModeEnum <ydk.models.ietf.ietf_l2vpn_svc.ControlModeEnum>`
                        
                        .. attribute:: stp_rstp_mstp
                        
                        	STP/RSTP/MSTP
                        	**type**\:   :py:class:`ControlModeEnum <ydk.models.ietf.ietf_l2vpn_svc.ControlModeEnum>`
                        
                        

                        """

                        _prefix = 'l2svc'
                        _revision = '2017-02-13'

                        def __init__(self):
                            self.parent = None
                            self.e_lmi = None
                            self.esmc = None
                            self.garp_mrp = None
                            self.l2cp_802_1x = None
                            self.lacp_lamp = None
                            self.link_oam = None
                            self.lldp = None
                            self.pause = None
                            self.provider_bridge_group = None
                            self.provider_bridge_mvrp = None
                            self.ptp_peer_delay = None
                            self.stp_rstp_mstp = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-l2vpn-svc:L2CP-control'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.e_lmi is not None:
                                return True

                            if self.esmc is not None:
                                return True

                            if self.garp_mrp is not None:
                                return True

                            if self.l2cp_802_1x is not None:
                                return True

                            if self.lacp_lamp is not None:
                                return True

                            if self.link_oam is not None:
                                return True

                            if self.lldp is not None:
                                return True

                            if self.pause is not None:
                                return True

                            if self.provider_bridge_group is not None:
                                return True

                            if self.provider_bridge_mvrp is not None:
                                return True

                            if self.ptp_peer_delay is not None:
                                return True

                            if self.stp_rstp_mstp is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                            return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.L2CpControl']['meta_info']


                    class Availability(object):
                        """
                        Container of availability optional configurations
                        
                        .. attribute:: all_active
                        
                        	All active
                        	**type**\:  bool
                        
                        .. attribute:: single_active
                        
                        	Single active
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'l2svc'
                        _revision = '2017-02-13'

                        def __init__(self):
                            self.parent = None
                            self.all_active = None
                            self.single_active = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-l2vpn-svc:availability'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.all_active is not None:
                                return True

                            if self.single_active is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                            return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.Availability']['meta_info']


                    class VpnAttachment(object):
                        """
                        Defines VPN attachment of a site.
                        
                        .. attribute:: device_id
                        
                        	Device ID
                        	**type**\:  str
                        
                        .. attribute:: management
                        
                        	Management configuration.
                        	**type**\:   :py:class:`Management <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.VpnAttachment.Management>`
                        
                        .. attribute:: site_role
                        
                        	Role of the site in the IPVPN
                        	**type**\:   :py:class:`SiteRoleIdentity <ydk.models.ietf.ietf_l2vpn_svc.SiteRoleIdentity>`
                        
                        	**default value**\: any-to-any-role
                        
                        .. attribute:: vpn_id
                        
                        	Reference to a VPN
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`vpn_id <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc>`
                        
                        

                        """

                        _prefix = 'l2svc'
                        _revision = '2017-02-13'

                        def __init__(self):
                            self.parent = None
                            self.device_id = None
                            self.management = L2VpnSvc.Sites.Site.Ports.Port.VpnAttachment.Management()
                            self.management.parent = self
                            self.site_role = None
                            self.vpn_id = None


                        class Management(object):
                            """
                            Management configuration..
                            
                            .. attribute:: address
                            
                            	Management address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: address_family
                            
                            	Address family used for management
                            	**type**\:   :py:class:`AddressFamilyIdentity <ydk.models.ietf.ietf_l2vpn_svc.AddressFamilyIdentity>`
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.address = None
                                self.address_family = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-l2vpn-svc:management'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.address is not None:
                                    return True

                                if self.address_family is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.VpnAttachment.Management']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-l2vpn-svc:vpn-attachment'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.device_id is not None:
                                return True

                            if self.management is not None and self.management._has_data():
                                return True

                            if self.site_role is not None:
                                return True

                            if self.vpn_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                            return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.VpnAttachment']['meta_info']


                    class Service(object):
                        """
                        Container for service
                        
                        .. attribute:: cvlan_id_to_evc_map
                        
                        	List for cvlan\-id to evc map configurations
                        	**type**\: list of    :py:class:`CvlanIdToEvcMap <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.Service.CvlanIdToEvcMap>`
                        
                        .. attribute:: qos
                        
                        	QoS configuration
                        	**type**\:   :py:class:`Qos <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.Service.Qos>`
                        
                        .. attribute:: service_level_mac_limit
                        
                        	Service\-level MAC\-limit (E\-LAN only)
                        	**type**\:  str
                        
                        .. attribute:: service_multiplexing
                        
                        	Service multiplexing
                        	**type**\:  bool
                        
                        .. attribute:: svc_input_bandwidth
                        
                        	From the PE perspective, the service input bandwidth of the connection
                        	**type**\:   :py:class:`SvcInputBandwidth <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.Service.SvcInputBandwidth>`
                        
                        .. attribute:: svc_output_bandwidth
                        
                        	From the PE perspective, the service output bandwidth of the connection
                        	**type**\:   :py:class:`SvcOutputBandwidth <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.Service.SvcOutputBandwidth>`
                        
                        .. attribute:: svlan_id_ethernet_tag
                        
                        	SVLAN\-ID/Ethernet Tag configurations
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'l2svc'
                        _revision = '2017-02-13'

                        def __init__(self):
                            self.parent = None
                            self.cvlan_id_to_evc_map = YList()
                            self.cvlan_id_to_evc_map.parent = self
                            self.cvlan_id_to_evc_map.name = 'cvlan_id_to_evc_map'
                            self.qos = L2VpnSvc.Sites.Site.Ports.Port.Service.Qos()
                            self.qos.parent = self
                            self.service_level_mac_limit = None
                            self.service_multiplexing = None
                            self.svc_input_bandwidth = L2VpnSvc.Sites.Site.Ports.Port.Service.SvcInputBandwidth()
                            self.svc_input_bandwidth.parent = self
                            self.svc_output_bandwidth = L2VpnSvc.Sites.Site.Ports.Port.Service.SvcOutputBandwidth()
                            self.svc_output_bandwidth.parent = self
                            self.svlan_id_ethernet_tag = None


                        class SvcInputBandwidth(object):
                            """
                            From the PE perspective, the service input
                            bandwidth of the connection.
                            
                            .. attribute:: input_bandwidth
                            
                            	List for input bandwidth
                            	**type**\: list of    :py:class:`InputBandwidth <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.Service.SvcInputBandwidth.InputBandwidth>`
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.input_bandwidth = YList()
                                self.input_bandwidth.parent = self
                                self.input_bandwidth.name = 'input_bandwidth'


                            class InputBandwidth(object):
                                """
                                List for input bandwidth
                                
                                .. attribute:: id  <key>
                                
                                	ID
                                	**type**\:  str
                                
                                .. attribute:: type  <key>
                                
                                	Bandwidth Type
                                	**type**\:   :py:class:`BwTypeIdentity <ydk.models.ietf.ietf_l2vpn_svc.BwTypeIdentity>`
                                
                                .. attribute:: cbs
                                
                                	Committed Burst Size
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: cir
                                
                                	Committed Information Rate
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: cm
                                
                                	Color Mode
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ebs
                                
                                	Excess Burst Size
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: eir
                                
                                	Excess Information Rate
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: evc_id
                                
                                	EVC ID
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'l2svc'
                                _revision = '2017-02-13'

                                def __init__(self):
                                    self.parent = None
                                    self.id = None
                                    self.type = None
                                    self.cbs = None
                                    self.cir = None
                                    self.cm = None
                                    self.ebs = None
                                    self.eir = None
                                    self.evc_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.id is None:
                                        raise YPYModelError('Key property id is None')
                                    if self.type is None:
                                        raise YPYModelError('Key property type is None')

                                    return self.parent._common_path +'/ietf-l2vpn-svc:input-bandwidth[ietf-l2vpn-svc:id = ' + str(self.id) + '][ietf-l2vpn-svc:type = ' + str(self.type) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.id is not None:
                                        return True

                                    if self.type is not None:
                                        return True

                                    if self.cbs is not None:
                                        return True

                                    if self.cir is not None:
                                        return True

                                    if self.cm is not None:
                                        return True

                                    if self.ebs is not None:
                                        return True

                                    if self.eir is not None:
                                        return True

                                    if self.evc_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                    return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.SvcInputBandwidth.InputBandwidth']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-l2vpn-svc:svc-input-bandwidth'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.input_bandwidth is not None:
                                    for child_ref in self.input_bandwidth:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.SvcInputBandwidth']['meta_info']


                        class SvcOutputBandwidth(object):
                            """
                            From the PE perspective, the service output
                            bandwidth of the connection.
                            
                            .. attribute:: output_bandwidth
                            
                            	List for output bandwidth
                            	**type**\: list of    :py:class:`OutputBandwidth <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.Service.SvcOutputBandwidth.OutputBandwidth>`
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.output_bandwidth = YList()
                                self.output_bandwidth.parent = self
                                self.output_bandwidth.name = 'output_bandwidth'


                            class OutputBandwidth(object):
                                """
                                List for output bandwidth
                                
                                .. attribute:: id  <key>
                                
                                	ID
                                	**type**\:  str
                                
                                .. attribute:: type  <key>
                                
                                	Bandwidth Type
                                	**type**\:   :py:class:`BwTypeIdentity <ydk.models.ietf.ietf_l2vpn_svc.BwTypeIdentity>`
                                
                                .. attribute:: cbs
                                
                                	Committed Burst Size
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: cir
                                
                                	Committed Information Rate
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: cm
                                
                                	Color Mode
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ebs
                                
                                	Excess Burst Size
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: eir
                                
                                	Excess Information Rate
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: evc_id
                                
                                	EVC ID
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'l2svc'
                                _revision = '2017-02-13'

                                def __init__(self):
                                    self.parent = None
                                    self.id = None
                                    self.type = None
                                    self.cbs = None
                                    self.cir = None
                                    self.cm = None
                                    self.ebs = None
                                    self.eir = None
                                    self.evc_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.id is None:
                                        raise YPYModelError('Key property id is None')
                                    if self.type is None:
                                        raise YPYModelError('Key property type is None')

                                    return self.parent._common_path +'/ietf-l2vpn-svc:output-bandwidth[ietf-l2vpn-svc:id = ' + str(self.id) + '][ietf-l2vpn-svc:type = ' + str(self.type) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.id is not None:
                                        return True

                                    if self.type is not None:
                                        return True

                                    if self.cbs is not None:
                                        return True

                                    if self.cir is not None:
                                        return True

                                    if self.cm is not None:
                                        return True

                                    if self.ebs is not None:
                                        return True

                                    if self.eir is not None:
                                        return True

                                    if self.evc_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                    return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.SvcOutputBandwidth.OutputBandwidth']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-l2vpn-svc:svc-output-bandwidth'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.output_bandwidth is not None:
                                    for child_ref in self.output_bandwidth:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.SvcOutputBandwidth']['meta_info']


                        class CvlanIdToEvcMap(object):
                            """
                            List for cvlan\-id to evc map configurations
                            
                            .. attribute:: evc_id  <key>
                            
                            	EVC ID
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`vpn_id <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.VpnServices.VpnSvc>`
                            
                            .. attribute:: type  <key>
                            
                            	Bundling type
                            	**type**\:   :py:class:`BundlingTypeIdentity <ydk.models.ietf.ietf_l2vpn_svc.BundlingTypeIdentity>`
                            
                            .. attribute:: cvlan_id
                            
                            	List of CVLAN\-ID to EVC Map configurations
                            	**type**\: list of    :py:class:`CvlanId <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.Service.CvlanIdToEvcMap.CvlanId>`
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.evc_id = None
                                self.type = None
                                self.cvlan_id = YList()
                                self.cvlan_id.parent = self
                                self.cvlan_id.name = 'cvlan_id'


                            class CvlanId(object):
                                """
                                List of CVLAN\-ID to EVC Map configurations
                                
                                .. attribute:: vid  <key>
                                
                                	CVLAN ID
                                	**type**\:   :py:class:`IanaInterfaceTypeIdentity <ydk.models.ietf.iana_if_type.IanaInterfaceTypeIdentity>`
                                
                                

                                """

                                _prefix = 'l2svc'
                                _revision = '2017-02-13'

                                def __init__(self):
                                    self.parent = None
                                    self.vid = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.vid is None:
                                        raise YPYModelError('Key property vid is None')

                                    return self.parent._common_path +'/ietf-l2vpn-svc:cvlan-id[ietf-l2vpn-svc:vid = ' + str(self.vid) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.vid is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                    return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.CvlanIdToEvcMap.CvlanId']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.evc_id is None:
                                    raise YPYModelError('Key property evc_id is None')
                                if self.type is None:
                                    raise YPYModelError('Key property type is None')

                                return self.parent._common_path +'/ietf-l2vpn-svc:cvlan-id-to-evc-map[ietf-l2vpn-svc:evc-id = ' + str(self.evc_id) + '][ietf-l2vpn-svc:type = ' + str(self.type) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.evc_id is not None:
                                    return True

                                if self.type is not None:
                                    return True

                                if self.cvlan_id is not None:
                                    for child_ref in self.cvlan_id:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.CvlanIdToEvcMap']['meta_info']


                        class Qos(object):
                            """
                            QoS configuration.
                            
                            .. attribute:: qos_classification_policy
                            
                            	Need to express marking rules ..
                            	**type**\:   :py:class:`QosClassificationPolicy <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy>`
                            
                            .. attribute:: qos_profile
                            
                            	Qos profile configuration
                            	**type**\:   :py:class:`QosProfile <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile>`
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.qos_classification_policy = L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy()
                                self.qos_classification_policy.parent = self
                                self.qos_profile = L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile()
                                self.qos_profile.parent = self


                            class QosClassificationPolicy(object):
                                """
                                Need to express marking rules ...
                                
                                .. attribute:: rule
                                
                                	List of marking rules
                                	**type**\: list of    :py:class:`Rule <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy.Rule>`
                                
                                

                                """

                                _prefix = 'l2svc'
                                _revision = '2017-02-13'

                                def __init__(self):
                                    self.parent = None
                                    self.rule = YList()
                                    self.rule.parent = self
                                    self.rule.name = 'rule'


                                class Rule(object):
                                    """
                                    List of marking rules.
                                    
                                    .. attribute:: id  <key>
                                    
                                    	ID of the rule
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: match_flow
                                    
                                    	Describe flow matching criterions
                                    	**type**\:   :py:class:`MatchFlow <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy.Rule.MatchFlow>`
                                    
                                    .. attribute:: match_phy_port
                                    
                                    	Defines the physical port to match
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: target_class_id
                                    
                                    	Identification of the class of service. This identifier is internal to the administration
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'l2svc'
                                    _revision = '2017-02-13'

                                    def __init__(self):
                                        self.parent = None
                                        self.id = None
                                        self.match_flow = L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy.Rule.MatchFlow()
                                        self.match_flow.parent = self
                                        self.match_phy_port = None
                                        self.target_class_id = None


                                    class MatchFlow(object):
                                        """
                                        Describe flow matching criterions.
                                        
                                        .. attribute:: color_type
                                        
                                        	Color Types
                                        	**type**\:   :py:class:`ColorTypeIdentity <ydk.models.ietf.ietf_l2vpn_svc.ColorTypeIdentity>`
                                        
                                        .. attribute:: cos_color_id
                                        
                                        	Container for cos color id
                                        	**type**\:   :py:class:`CosColorId <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy.Rule.MatchFlow.CosColorId>`
                                        
                                        .. attribute:: dot1p
                                        
                                        	802.1p matching
                                        	**type**\:  int
                                        
                                        	**range:** 0..7
                                        
                                        .. attribute:: dscp
                                        
                                        	DSCP value
                                        	**type**\:  int
                                        
                                        	**range:** 0..63
                                        
                                        .. attribute:: dst_mac
                                        
                                        	Destination MAC
                                        	**type**\:  str
                                        
                                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                        
                                        .. attribute:: pcp
                                        
                                        	PCP value
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: src_mac
                                        
                                        	Source MAC
                                        	**type**\:  str
                                        
                                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                        
                                        .. attribute:: target_sites
                                        
                                        	Identify a site as traffic destination
                                        	**type**\:  list of str
                                        
                                        

                                        """

                                        _prefix = 'l2svc'
                                        _revision = '2017-02-13'

                                        def __init__(self):
                                            self.parent = None
                                            self.color_type = None
                                            self.cos_color_id = L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy.Rule.MatchFlow.CosColorId()
                                            self.cos_color_id.parent = self
                                            self.dot1p = None
                                            self.dscp = None
                                            self.dst_mac = None
                                            self.pcp = None
                                            self.src_mac = None
                                            self.target_sites = YLeafList()
                                            self.target_sites.parent = self
                                            self.target_sites.name = 'target_sites'


                                        class CosColorId(object):
                                            """
                                            Container for cos color id
                                            
                                            .. attribute:: cos_label
                                            
                                            	COS label
                                            	**type**\:   :py:class:`CosIdIdentity <ydk.models.ietf.ietf_l2vpn_svc.CosIdIdentity>`
                                            
                                            .. attribute:: device_id
                                            
                                            	Device ID
                                            	**type**\:  str
                                            
                                            .. attribute:: dscp
                                            
                                            	DSCP value
                                            	**type**\:  int
                                            
                                            	**range:** 0..63
                                            
                                            .. attribute:: pcp
                                            
                                            	PCP value
                                            	**type**\:  int
                                            
                                            	**range:** 0..255
                                            
                                            

                                            """

                                            _prefix = 'l2svc'
                                            _revision = '2017-02-13'

                                            def __init__(self):
                                                self.parent = None
                                                self.cos_label = None
                                                self.device_id = None
                                                self.dscp = None
                                                self.pcp = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-l2vpn-svc:cos-color-id'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.cos_label is not None:
                                                    return True

                                                if self.device_id is not None:
                                                    return True

                                                if self.dscp is not None:
                                                    return True

                                                if self.pcp is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy.Rule.MatchFlow.CosColorId']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/ietf-l2vpn-svc:match-flow'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.color_type is not None:
                                                return True

                                            if self.cos_color_id is not None and self.cos_color_id._has_data():
                                                return True

                                            if self.dot1p is not None:
                                                return True

                                            if self.dscp is not None:
                                                return True

                                            if self.dst_mac is not None:
                                                return True

                                            if self.pcp is not None:
                                                return True

                                            if self.src_mac is not None:
                                                return True

                                            if self.target_sites is not None:
                                                for child in self.target_sites:
                                                    if child is not None:
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                            return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy.Rule.MatchFlow']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.id is None:
                                            raise YPYModelError('Key property id is None')

                                        return self.parent._common_path +'/ietf-l2vpn-svc:rule[ietf-l2vpn-svc:id = ' + str(self.id) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.id is not None:
                                            return True

                                        if self.match_flow is not None and self.match_flow._has_data():
                                            return True

                                        if self.match_phy_port is not None:
                                            return True

                                        if self.target_class_id is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                        return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy.Rule']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/ietf-l2vpn-svc:qos-classification-policy'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.rule is not None:
                                        for child_ref in self.rule:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                    return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy']['meta_info']


                            class QosProfile(object):
                                """
                                Qos profile configuration.
                                
                                .. attribute:: classes
                                
                                	Container for list of class of services
                                	**type**\:   :py:class:`Classes <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes>`
                                
                                .. attribute:: egress_profile
                                
                                	Egress QoS Profile to be used
                                	**type**\:  str
                                
                                .. attribute:: ingress_profile
                                
                                	Ingress QoS Profile to be used
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'l2svc'
                                _revision = '2017-02-13'

                                def __init__(self):
                                    self.parent = None
                                    self.classes = L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes()
                                    self.classes.parent = self
                                    self.egress_profile = None
                                    self.ingress_profile = None


                                class Classes(object):
                                    """
                                    Container for list of class of services.
                                    
                                    .. attribute:: class_
                                    
                                    	List of class of services
                                    	**type**\: list of    :py:class:`Class_ <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_>`
                                    
                                    

                                    """

                                    _prefix = 'l2svc'
                                    _revision = '2017-02-13'

                                    def __init__(self):
                                        self.parent = None
                                        self.class_ = YList()
                                        self.class_.parent = self
                                        self.class_.name = 'class_'


                                    class Class_(object):
                                        """
                                        List of class of services.
                                        
                                        .. attribute:: class_id  <key>
                                        
                                        	Identification of the class of service. This identifier is internal to the administration
                                        	**type**\:  str
                                        
                                        .. attribute:: byte_offset
                                        
                                        	For not including extra VLAN tags in the QoS calculation
                                        	**type**\:  int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: direction
                                        
                                        	Direction type
                                        	**type**\:  str
                                        
                                        .. attribute:: discard_percentage
                                        
                                        	The value of the discard\-percentage, Expressed as pecentage of the svc\-bw 
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        	**default value**\: 100
                                        
                                        .. attribute:: frame_delay
                                        
                                        	Delay constraint on the traffic class
                                        	**type**\:   :py:class:`FrameDelay <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_.FrameDelay>`
                                        
                                        .. attribute:: frame_jitter
                                        
                                        	Jitter constraint on the traffic class
                                        	**type**\:   :py:class:`FrameJitter <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_.FrameJitter>`
                                        
                                        .. attribute:: frame_loss
                                        
                                        	Container for frame loss
                                        	**type**\:   :py:class:`FrameLoss <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_.FrameLoss>`
                                        
                                        .. attribute:: perf_tier_opt
                                        
                                        	Performance tier option
                                        	**type**\:   :py:class:`PerfTierOptIdentity <ydk.models.ietf.ietf_l2vpn_svc.PerfTierOptIdentity>`
                                        
                                        .. attribute:: policing
                                        
                                        	The policing can be either one\-rate, two\-color (1R2C) or two\-rate, three\-color (2R3C)
                                        	**type**\:   :py:class:`PolicingIdentity <ydk.models.ietf.ietf_l2vpn_svc.PolicingIdentity>`
                                        
                                        .. attribute:: rate_limit
                                        
                                        	To be used if class must be rate limited. Expressed as percentage of the svc\-bw
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        	**units**\: percent
                                        
                                        

                                        """

                                        _prefix = 'l2svc'
                                        _revision = '2017-02-13'

                                        def __init__(self):
                                            self.parent = None
                                            self.class_id = None
                                            self.byte_offset = None
                                            self.direction = None
                                            self.discard_percentage = None
                                            self.frame_delay = L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_.FrameDelay()
                                            self.frame_delay.parent = self
                                            self.frame_jitter = L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_.FrameJitter()
                                            self.frame_jitter.parent = self
                                            self.frame_loss = L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_.FrameLoss()
                                            self.frame_loss.parent = self
                                            self.perf_tier_opt = None
                                            self.policing = None
                                            self.rate_limit = None


                                        class FrameDelay(object):
                                            """
                                            Delay constraint on the traffic
                                            class
                                            
                                            .. attribute:: delay_bound
                                            
                                            	The traffic class should use a path with a defined maximum delay
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            	**units**\: msec
                                            
                                            .. attribute:: use_low_del
                                            
                                            	The traffic class should use the lowest delay path
                                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                            
                                            

                                            """

                                            _prefix = 'l2svc'
                                            _revision = '2017-02-13'

                                            def __init__(self):
                                                self.parent = None
                                                self.delay_bound = None
                                                self.use_low_del = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-l2vpn-svc:frame-delay'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.delay_bound is not None:
                                                    return True

                                                if self.use_low_del is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_.FrameDelay']['meta_info']


                                        class FrameJitter(object):
                                            """
                                            Jitter constraint on the traffic
                                            class
                                            
                                            .. attribute:: delay_bound
                                            
                                            	The traffic class should use a path with a defined maximum jitter
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**units**\: usec
                                            
                                            .. attribute:: use_low_jit
                                            
                                            	The traffic class should use the lowest jitter path
                                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                            
                                            

                                            """

                                            _prefix = 'l2svc'
                                            _revision = '2017-02-13'

                                            def __init__(self):
                                                self.parent = None
                                                self.delay_bound = None
                                                self.use_low_jit = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-l2vpn-svc:frame-jitter'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.delay_bound is not None:
                                                    return True

                                                if self.use_low_jit is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_.FrameJitter']['meta_info']


                                        class FrameLoss(object):
                                            """
                                            Container for frame loss
                                            
                                            .. attribute:: fr_loss_rate
                                            
                                            	Loss constraint on the traffic class
                                            	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                                            
                                            	**range:** \-92233720368547758.08..92233720368547758.07
                                            
                                            

                                            """

                                            _prefix = 'l2svc'
                                            _revision = '2017-02-13'

                                            def __init__(self):
                                                self.parent = None
                                                self.fr_loss_rate = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-l2vpn-svc:frame-loss'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.fr_loss_rate is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_.FrameLoss']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.class_id is None:
                                                raise YPYModelError('Key property class_id is None')

                                            return self.parent._common_path +'/ietf-l2vpn-svc:class[ietf-l2vpn-svc:class-id = ' + str(self.class_id) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.class_id is not None:
                                                return True

                                            if self.byte_offset is not None:
                                                return True

                                            if self.direction is not None:
                                                return True

                                            if self.discard_percentage is not None:
                                                return True

                                            if self.frame_delay is not None and self.frame_delay._has_data():
                                                return True

                                            if self.frame_jitter is not None and self.frame_jitter._has_data():
                                                return True

                                            if self.frame_loss is not None and self.frame_loss._has_data():
                                                return True

                                            if self.perf_tier_opt is not None:
                                                return True

                                            if self.policing is not None:
                                                return True

                                            if self.rate_limit is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                            return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-l2vpn-svc:classes'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.class_ is not None:
                                            for child_ref in self.class_:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                        return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/ietf-l2vpn-svc:qos-profile'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.classes is not None and self.classes._has_data():
                                        return True

                                    if self.egress_profile is not None:
                                        return True

                                    if self.ingress_profile is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                    return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-l2vpn-svc:qos'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.qos_classification_policy is not None and self.qos_classification_policy._has_data():
                                    return True

                                if self.qos_profile is not None and self.qos_profile._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-l2vpn-svc:service'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.cvlan_id_to_evc_map is not None:
                                for child_ref in self.cvlan_id_to_evc_map:
                                    if child_ref._has_data():
                                        return True

                            if self.qos is not None and self.qos._has_data():
                                return True

                            if self.service_level_mac_limit is not None:
                                return True

                            if self.service_multiplexing is not None:
                                return True

                            if self.svc_input_bandwidth is not None and self.svc_input_bandwidth._has_data():
                                return True

                            if self.svc_output_bandwidth is not None and self.svc_output_bandwidth._has_data():
                                return True

                            if self.svlan_id_ethernet_tag is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                            return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service']['meta_info']


                    class EthernetServiceOam(object):
                        """
                        Container for Ethernet service OAM.
                        
                        .. attribute:: cfm_802_1_ag
                        
                        	Container of 802.1ag CFM configurations
                        	**type**\:   :py:class:`Cfm802__Dot__1Ag <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag>`
                        
                        .. attribute:: md_level
                        
                        	Maintenance domain level
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: md_name
                        
                        	Maintenance domain name
                        	**type**\:  str
                        
                        .. attribute:: y_1731
                        
                        	List for y\-1731
                        	**type**\: list of    :py:class:`Y1731 <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Y1731>`
                        
                        

                        """

                        _prefix = 'l2svc'
                        _revision = '2017-02-13'

                        def __init__(self):
                            self.parent = None
                            self.cfm_802_1_ag = L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag()
                            self.cfm_802_1_ag.parent = self
                            self.md_level = None
                            self.md_name = None
                            self.y_1731 = YList()
                            self.y_1731.parent = self
                            self.y_1731.name = 'y_1731'


                        class Cfm802__Dot__1Ag(object):
                            """
                            Container of 802.1ag CFM configurations.
                            
                            .. attribute:: n2_uni_c
                            
                            	List of UNI\-N to UNI\-C
                            	**type**\: list of    :py:class:`N2UniC <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag.N2UniC>`
                            
                            .. attribute:: n2_uni_n
                            
                            	List of UNI\-N to UNI\-N
                            	**type**\: list of    :py:class:`N2UniN <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag.N2UniN>`
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.n2_uni_c = YList()
                                self.n2_uni_c.parent = self
                                self.n2_uni_c.name = 'n2_uni_c'
                                self.n2_uni_n = YList()
                                self.n2_uni_n.parent = self
                                self.n2_uni_n.name = 'n2_uni_n'


                            class N2UniC(object):
                                """
                                List of UNI\-N to UNI\-C
                                
                                .. attribute:: maid  <key>
                                
                                	MA ID
                                	**type**\:  str
                                
                                .. attribute:: alarm_priority_defect
                                
                                	The lowest priority defect that is allowed to generate a Fault Alarm. The non\-existence of this leaf means that no defects are to be reported
                                	**type**\:   :py:class:`FaultAlarmDefectTypeIdentity <ydk.models.ietf.ietf_l2vpn_svc.FaultAlarmDefectTypeIdentity>`
                                
                                .. attribute:: ccm_holdtime
                                
                                	CCM hold time
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ccm_interval
                                
                                	CCM interval
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ccm_p_bits_pri
                                
                                	The priority parameter for CCMs transmitted by the MEP
                                	**type**\:  int
                                
                                	**range:** 0..7
                                
                                .. attribute:: cos_for_cfm_pdus
                                
                                	COS for CFM PDUs
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: mep_id
                                
                                	Local MEP ID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: mep_level
                                
                                	MEP level
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: mep_up_down
                                
                                	MEP up/down
                                	**type**\:   :py:class:`MepUpDownEnum <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag.N2UniC.MepUpDownEnum>`
                                
                                .. attribute:: remote_mep_id
                                
                                	Remote MEP ID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'l2svc'
                                _revision = '2017-02-13'

                                def __init__(self):
                                    self.parent = None
                                    self.maid = None
                                    self.alarm_priority_defect = None
                                    self.ccm_holdtime = None
                                    self.ccm_interval = None
                                    self.ccm_p_bits_pri = None
                                    self.cos_for_cfm_pdus = None
                                    self.mep_id = None
                                    self.mep_level = None
                                    self.mep_up_down = None
                                    self.remote_mep_id = None

                                class MepUpDownEnum(Enum):
                                    """
                                    MepUpDownEnum

                                    MEP up/down

                                    .. data:: up = 0

                                    	MEP up

                                    .. data:: down = 1

                                    	MEP down

                                    """

                                    up = 0

                                    down = 1


                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                        return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag.N2UniC.MepUpDownEnum']


                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.maid is None:
                                        raise YPYModelError('Key property maid is None')

                                    return self.parent._common_path +'/ietf-l2vpn-svc:n2-uni-c[ietf-l2vpn-svc:MAID = ' + str(self.maid) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.maid is not None:
                                        return True

                                    if self.alarm_priority_defect is not None:
                                        return True

                                    if self.ccm_holdtime is not None:
                                        return True

                                    if self.ccm_interval is not None:
                                        return True

                                    if self.ccm_p_bits_pri is not None:
                                        return True

                                    if self.cos_for_cfm_pdus is not None:
                                        return True

                                    if self.mep_id is not None:
                                        return True

                                    if self.mep_level is not None:
                                        return True

                                    if self.mep_up_down is not None:
                                        return True

                                    if self.remote_mep_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                    return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag.N2UniC']['meta_info']


                            class N2UniN(object):
                                """
                                List of UNI\-N to UNI\-N
                                
                                .. attribute:: maid  <key>
                                
                                	MA ID
                                	**type**\:  str
                                
                                .. attribute:: alarm_priority_defect
                                
                                	The lowest priority defect that is allowed to generate a Fault Alarm. The non\-existence of this leaf means that no defects are to be reported
                                	**type**\:   :py:class:`FaultAlarmDefectTypeIdentity <ydk.models.ietf.ietf_l2vpn_svc.FaultAlarmDefectTypeIdentity>`
                                
                                .. attribute:: ccm_holdtime
                                
                                	CCM hold time
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ccm_interval
                                
                                	CCM interval
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ccm_p_bits_pri
                                
                                	The priority parameter for CCMs transmitted by the MEP
                                	**type**\:  int
                                
                                	**range:** 0..7
                                
                                .. attribute:: cos_for_cfm_pdus
                                
                                	COS for CFM PDUs
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: mep_id
                                
                                	Local MEP ID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: mep_level
                                
                                	MEP level
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: mep_up_down
                                
                                	MEP up/down
                                	**type**\:   :py:class:`MepUpDownEnum <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag.N2UniN.MepUpDownEnum>`
                                
                                .. attribute:: remote_mep_id
                                
                                	Remote MEP ID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'l2svc'
                                _revision = '2017-02-13'

                                def __init__(self):
                                    self.parent = None
                                    self.maid = None
                                    self.alarm_priority_defect = None
                                    self.ccm_holdtime = None
                                    self.ccm_interval = None
                                    self.ccm_p_bits_pri = None
                                    self.cos_for_cfm_pdus = None
                                    self.mep_id = None
                                    self.mep_level = None
                                    self.mep_up_down = None
                                    self.remote_mep_id = None

                                class MepUpDownEnum(Enum):
                                    """
                                    MepUpDownEnum

                                    MEP up/down

                                    .. data:: up = 0

                                    	MEP up

                                    .. data:: down = 1

                                    	MEP down

                                    """

                                    up = 0

                                    down = 1


                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                        return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag.N2UniN.MepUpDownEnum']


                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.maid is None:
                                        raise YPYModelError('Key property maid is None')

                                    return self.parent._common_path +'/ietf-l2vpn-svc:n2-uni-n[ietf-l2vpn-svc:MAID = ' + str(self.maid) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.maid is not None:
                                        return True

                                    if self.alarm_priority_defect is not None:
                                        return True

                                    if self.ccm_holdtime is not None:
                                        return True

                                    if self.ccm_interval is not None:
                                        return True

                                    if self.ccm_p_bits_pri is not None:
                                        return True

                                    if self.cos_for_cfm_pdus is not None:
                                        return True

                                    if self.mep_id is not None:
                                        return True

                                    if self.mep_level is not None:
                                        return True

                                    if self.mep_up_down is not None:
                                        return True

                                    if self.remote_mep_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                    return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag.N2UniN']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-l2vpn-svc:cfm-802.1-ag'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.n2_uni_c is not None:
                                    for child_ref in self.n2_uni_c:
                                        if child_ref._has_data():
                                            return True

                                if self.n2_uni_n is not None:
                                    for child_ref in self.n2_uni_n:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag']['meta_info']


                        class Y1731(object):
                            """
                            List for y\-1731.
                            
                            .. attribute:: maid  <key>
                            
                            	MA ID 
                            	**type**\:  str
                            
                            .. attribute:: cos
                            
                            	Class of service
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: delay_measurement
                            
                            	Container for delay measurement
                            	**type**\:   :py:class:`DelayMeasurement <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Y1731.DelayMeasurement>`
                            
                            .. attribute:: frame_size
                            
                            	Frame size
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: loss_measurement
                            
                            	Whether enable loss measurement
                            	**type**\:  bool
                            
                            .. attribute:: measurement_interval
                            
                            	Specifies the measurement interval for statistics. The measurement interval is expressed in seconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mep_id
                            
                            	Local MEP ID
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: message_period
                            
                            	Defines the interval between OAM messages. The message period is expressed in milliseconds
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: remote_mep_id
                            
                            	Remote MEP ID
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_type
                            
                            	Session type
                            	**type**\:   :py:class:`SessionTypeEnum <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Y1731.SessionTypeEnum>`
                            
                            .. attribute:: synthethic_loss_measurement
                            
                            	Indicate whether enable synthetic loss measurement
                            	**type**\:  bool
                            
                            .. attribute:: type
                            
                            	Performance monitor types
                            	**type**\:   :py:class:`PmTypeIdentity <ydk.models.ietf.ietf_l2vpn_svc.PmTypeIdentity>`
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.maid = None
                                self.cos = None
                                self.delay_measurement = L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Y1731.DelayMeasurement()
                                self.delay_measurement.parent = self
                                self.frame_size = None
                                self.loss_measurement = None
                                self.measurement_interval = None
                                self.mep_id = None
                                self.message_period = None
                                self.remote_mep_id = None
                                self.session_type = None
                                self.synthethic_loss_measurement = None
                                self.type = None

                            class SessionTypeEnum(Enum):
                                """
                                SessionTypeEnum

                                Session type

                                .. data:: proactive = 0

                                	Proactive mode

                                .. data:: on_demand = 1

                                	On demand mode

                                """

                                proactive = 0

                                on_demand = 1


                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                    return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Y1731.SessionTypeEnum']



                            class DelayMeasurement(object):
                                """
                                Container for delay measurement
                                
                                .. attribute:: enable_dm
                                
                                	Whether to enable delay measurement
                                	**type**\:  bool
                                
                                .. attribute:: two_way
                                
                                	Whether delay measurement is two\-way (true) of one\- way (false)
                                	**type**\:  bool
                                
                                

                                """

                                _prefix = 'l2svc'
                                _revision = '2017-02-13'

                                def __init__(self):
                                    self.parent = None
                                    self.enable_dm = None
                                    self.two_way = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/ietf-l2vpn-svc:delay-measurement'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.enable_dm is not None:
                                        return True

                                    if self.two_way is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                    return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Y1731.DelayMeasurement']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.maid is None:
                                    raise YPYModelError('Key property maid is None')

                                return self.parent._common_path +'/ietf-l2vpn-svc:y-1731[ietf-l2vpn-svc:MAID = ' + str(self.maid) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.maid is not None:
                                    return True

                                if self.cos is not None:
                                    return True

                                if self.delay_measurement is not None and self.delay_measurement._has_data():
                                    return True

                                if self.frame_size is not None:
                                    return True

                                if self.loss_measurement is not None:
                                    return True

                                if self.measurement_interval is not None:
                                    return True

                                if self.mep_id is not None:
                                    return True

                                if self.message_period is not None:
                                    return True

                                if self.remote_mep_id is not None:
                                    return True

                                if self.session_type is not None:
                                    return True

                                if self.synthethic_loss_measurement is not None:
                                    return True

                                if self.type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Y1731']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-l2vpn-svc:Ethernet-Service-OAM'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.cfm_802_1_ag is not None and self.cfm_802_1_ag._has_data():
                                return True

                            if self.md_level is not None:
                                return True

                            if self.md_name is not None:
                                return True

                            if self.y_1731 is not None:
                                for child_ref in self.y_1731:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                            return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam']['meta_info']


                    class SecurityFiltering(object):
                        """
                        Security parameters
                        
                        .. attribute:: access_control_list
                        
                        	Container for access control
                        	**type**\:   :py:class:`AccessControlList <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.AccessControlList>`
                        
                        .. attribute:: b_u_m_storm_control
                        
                        	Container of B\-U\-M\-strom\-control configurations
                        	**type**\:   :py:class:`BUMStormControl <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.BUMStormControl>`
                        
                        .. attribute:: mac_addr_limit
                        
                        	Container of MAC\-Addr limit configurations
                        	**type**\:   :py:class:`MacAddrLimit <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.MacAddrLimit>`
                        
                        .. attribute:: mac_loop_prevention
                        
                        	Container of MAC loop prevention
                        	**type**\:   :py:class:`MacLoopPrevention <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.MacLoopPrevention>`
                        
                        

                        """

                        _prefix = 'l2svc'
                        _revision = '2017-02-13'

                        def __init__(self):
                            self.parent = None
                            self.access_control_list = L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.AccessControlList()
                            self.access_control_list.parent = self
                            self.b_u_m_storm_control = L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.BUMStormControl()
                            self.b_u_m_storm_control.parent = self
                            self.mac_addr_limit = L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.MacAddrLimit()
                            self.mac_addr_limit.parent = self
                            self.mac_loop_prevention = L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.MacLoopPrevention()
                            self.mac_loop_prevention.parent = self


                        class MacLoopPrevention(object):
                            """
                            Container of MAC loop prevention.
                            
                            .. attribute:: frequency
                            
                            	Frequency
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: number_retries
                            
                            	Number of retries
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: protection_type
                            
                            	Protection type
                            	**type**\:   :py:class:`LoopPreventionTypeIdentity <ydk.models.ietf.ietf_l2vpn_svc.LoopPreventionTypeIdentity>`
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.frequency = None
                                self.number_retries = None
                                self.protection_type = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-l2vpn-svc:mac-loop-prevention'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.frequency is not None:
                                    return True

                                if self.number_retries is not None:
                                    return True

                                if self.protection_type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.MacLoopPrevention']['meta_info']


                        class AccessControlList(object):
                            """
                            Container for access control
                            
                            .. attribute:: mac
                            
                            	List for MAC
                            	**type**\: list of    :py:class:`Mac <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.AccessControlList.Mac>`
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.mac = YList()
                                self.mac.parent = self
                                self.mac.name = 'mac'


                            class Mac(object):
                                """
                                List for MAC
                                
                                .. attribute:: mac_address  <key>
                                
                                	MAC address
                                	**type**\:  str
                                
                                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                                
                                

                                """

                                _prefix = 'l2svc'
                                _revision = '2017-02-13'

                                def __init__(self):
                                    self.parent = None
                                    self.mac_address = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.mac_address is None:
                                        raise YPYModelError('Key property mac_address is None')

                                    return self.parent._common_path +'/ietf-l2vpn-svc:mac[ietf-l2vpn-svc:mac-address = ' + str(self.mac_address) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.mac_address is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                    return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.AccessControlList.Mac']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-l2vpn-svc:access-control-list'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.mac is not None:
                                    for child_ref in self.mac:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.AccessControlList']['meta_info']


                        class MacAddrLimit(object):
                            """
                            Container of MAC\-Addr limit configurations
                            
                            .. attribute:: exceeding_option
                            
                            	Exceeding option
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.exceeding_option = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-l2vpn-svc:mac-addr-limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.exceeding_option is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.MacAddrLimit']['meta_info']


                        class BUMStormControl(object):
                            """
                            Container of B\-U\-M\-strom\-control configurations
                            
                            .. attribute:: bum_overall_rate
                            
                            	overall rate for BUM
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bum_rate_per_type
                            
                            	List of rate per type
                            	**type**\: list of    :py:class:`BumRatePerType <ydk.models.ietf.ietf_l2vpn_svc.L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.BUMStormControl.BumRatePerType>`
                            
                            

                            """

                            _prefix = 'l2svc'
                            _revision = '2017-02-13'

                            def __init__(self):
                                self.parent = None
                                self.bum_overall_rate = None
                                self.bum_rate_per_type = YList()
                                self.bum_rate_per_type.parent = self
                                self.bum_rate_per_type.name = 'bum_rate_per_type'


                            class BumRatePerType(object):
                                """
                                List of rate per type
                                
                                .. attribute:: type  <key>
                                
                                	BUM type
                                	**type**\:   :py:class:`BumTypeIdentity <ydk.models.ietf.ietf_l2vpn_svc.BumTypeIdentity>`
                                
                                .. attribute:: rate
                                
                                	rate for BUM
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'l2svc'
                                _revision = '2017-02-13'

                                def __init__(self):
                                    self.parent = None
                                    self.type = None
                                    self.rate = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.type is None:
                                        raise YPYModelError('Key property type is None')

                                    return self.parent._common_path +'/ietf-l2vpn-svc:BUM-rate-per-type[ietf-l2vpn-svc:type = ' + str(self.type) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.type is not None:
                                        return True

                                    if self.rate is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                    return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.BUMStormControl.BumRatePerType']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-l2vpn-svc:B-U-M-storm-control'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.bum_overall_rate is not None:
                                    return True

                                if self.bum_rate_per_type is not None:
                                    for child_ref in self.bum_rate_per_type:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                                return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.BUMStormControl']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-l2vpn-svc:security-filtering'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.access_control_list is not None and self.access_control_list._has_data():
                                return True

                            if self.b_u_m_storm_control is not None and self.b_u_m_storm_control._has_data():
                                return True

                            if self.mac_addr_limit is not None and self.mac_addr_limit._has_data():
                                return True

                            if self.mac_loop_prevention is not None and self.mac_loop_prevention._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                            return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.network_access_id is None:
                            raise YPYModelError('Key property network_access_id is None')

                        return self.parent._common_path +'/ietf-l2vpn-svc:port[ietf-l2vpn-svc:network-access-id = ' + str(self.network_access_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.network_access_id is not None:
                            return True

                        if self.access_diversity is not None and self.access_diversity._has_data():
                            return True

                        if self.availability is not None and self.availability._has_data():
                            return True

                        if self.bearer is not None and self.bearer._has_data():
                            return True

                        if self.ethernet_connection is not None and self.ethernet_connection._has_data():
                            return True

                        if self.ethernet_service_oam is not None and self.ethernet_service_oam._has_data():
                            return True

                        if self.evc_mtu is not None:
                            return True

                        if self.l2cp_control is not None and self.l2cp_control._has_data():
                            return True

                        if self.remote_carrier_name is not None:
                            return True

                        if self.security_filtering is not None and self.security_filtering._has_data():
                            return True

                        if self.service is not None and self.service._has_data():
                            return True

                        if self.vpn_attachment is not None and self.vpn_attachment._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                        return meta._meta_table['L2VpnSvc.Sites.Site.Ports.Port']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-l2vpn-svc:ports'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.port is not None:
                        for child_ref in self.port:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                    return meta._meta_table['L2VpnSvc.Sites.Site.Ports']['meta_info']

            @property
            def _common_path(self):
                if self.site_id is None:
                    raise YPYModelError('Key property site_id is None')
                if self.site_type is None:
                    raise YPYModelError('Key property site_type is None')

                return '/ietf-l2vpn-svc:l2vpn-svc/ietf-l2vpn-svc:sites/ietf-l2vpn-svc:site[ietf-l2vpn-svc:site-id = ' + str(self.site_id) + '][ietf-l2vpn-svc:site-type = ' + str(self.site_type) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.site_id is not None:
                    return True

                if self.site_type is not None:
                    return True

                if self.actual_site_start is not None:
                    return True

                if self.actual_site_stop is not None:
                    return True

                if self.device is not None and self.device._has_data():
                    return True

                if self.load_balance_options is not None and self.load_balance_options._has_data():
                    return True

                if self.location is not None and self.location._has_data():
                    return True

                if self.managemnt is not None and self.managemnt._has_data():
                    return True

                if self.ports is not None and self.ports._has_data():
                    return True

                if self.signaling_option is not None and self.signaling_option._has_data():
                    return True

                if self.site_diversity is not None and self.site_diversity._has_data():
                    return True

                if self.vpn_policies is not None and self.vpn_policies._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
                return meta._meta_table['L2VpnSvc.Sites.Site']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-l2vpn-svc:l2vpn-svc/ietf-l2vpn-svc:sites'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.site is not None:
                for child_ref in self.site:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
            return meta._meta_table['L2VpnSvc.Sites']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-l2vpn-svc:l2vpn-svc'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.customer_info is not None and self.customer_info._has_data():
            return True

        if self.sites is not None and self.sites._has_data():
            return True

        if self.vpn_services is not None and self.vpn_services._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['L2VpnSvc']['meta_info']


class DataPlaneIdentity(MacLearningModeIdentity):
    """
    User MAC addresses are learned through ARP broadcast.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        MacLearningModeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['DataPlaneIdentity']['meta_info']


class GlobalIdentity(PerfTierOptIdentity):
    """
    Identity of global
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        PerfTierOptIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['GlobalIdentity']['meta_info']


class CosIdEvcDscpIdentity(CosIdIdentity):
    """
    Identity of cos id based on EVC and DSCP
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        CosIdIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['CosIdEvcDscpIdentity']['meta_info']


class BwPerCosIdentity(BwTypeIdentity):
    """
    Bandwidth is per cos
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        BwTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['BwPerCosIdentity']['meta_info']


class ProviderManagedIdentity(ManagementIdentity):
    """
    Base identity for provider managed site.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        ManagementIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['ProviderManagedIdentity']['meta_info']


class EnniIdentity(SiteTypeIdentity):
    """
    Identity of External Network to Network Interface
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        SiteTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['EnniIdentity']['meta_info']


class LacpOnIdentity(LacpStateIdentity):
    """
    Identity of LCAP on
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        LacpStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['LacpOnIdentity']['meta_info']


class VxlanIdentity(L2AccessTypeIdentity):
    """
    Vxlan access into the vpn
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        L2AccessTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['VxlanIdentity']['meta_info']


class LacpSlowIdentity(LacpSpeedIdentity):
    """
    Identity of LACP slow
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        LacpSpeedIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['LacpSlowIdentity']['meta_info']


class EviIdentity(VpnSignalingTypeIdentity):
    """
    Ethernet virtual interconnect.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        VpnSignalingTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['EviIdentity']['meta_info']


class RegionalIdentity(PerfTierOptIdentity):
    """
    Identity of regional
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        PerfTierOptIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['RegionalIdentity']['meta_info']


class CoManagedIdentity(ManagementIdentity):
    """
    Base identity for co\-managed site.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        ManagementIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['CoManagedIdentity']['meta_info']


class HubRoleIdentity(SiteRoleIdentity):
    """
    Hub Site in a Hub &amp Spoke IPVPN.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        SiteRoleIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['HubRoleIdentity']['meta_info']


class YellowIdentity(ColorTypeIdentity):
    """
    Identity of yellow type
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        ColorTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['YellowIdentity']['meta_info']


class RootedMultipointIdentity(SvcTopoTypeIdentity):
    """
    Rooted Multipoint.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        SvcTopoTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['RootedMultipointIdentity']['meta_info']


class EvpnIdentity(L2VpnTypeIdentity):
    """
    Ethernet VPN
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        L2VpnTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['EvpnIdentity']['meta_info']


class LossIdentity(PmTypeIdentity):
    """
    Loss measurement
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        PmTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['LossIdentity']['meta_info']


class MultipointToMultipointIdentity(SvcTopoTypeIdentity):
    """
    Multipoint to Multipoint.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        SvcTopoTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['MultipointToMultipointIdentity']['meta_info']


class EvcIdentity(ServiceTypeIdentity):
    """
    EVC type.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        ServiceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['EvcIdentity']['meta_info']


class RemoteMacErrorIdentity(FaultAlarmDefectTypeIdentity):
    """
    Indicates that one or more of the remote MEPs is
    reporting a failure in its Port Status TLV or
    Interface Status TLV.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        FaultAlarmDefectTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['RemoteMacErrorIdentity']['meta_info']


class VpwsIdentity(L2VpnTypeIdentity):
    """
    Virtual Private Wire Service
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        L2VpnTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['VpwsIdentity']['meta_info']


class TrapIdentity(LoopPreventionTypeIdentity):
    """
    Identity of trap protection
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        LoopPreventionTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['TrapIdentity']['meta_info']


class OneRateTwoColorIdentity(PolicingIdentity):
    """
    Identity of one\-rate, two\-color (1R2C)
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        PolicingIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['OneRateTwoColorIdentity']['meta_info']


class HubSpokeIdentity(VpnTopologyIdentity):
    """
    Identity for Hub'n'Spoke VPN topology.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        VpnTopologyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['HubSpokeIdentity']['meta_info']


class BundlingIdentity(BundlingTypeIdentity):
    """
    Identity for bundling
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        BundlingTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['BundlingIdentity']['meta_info']


class ConditionalIdentity(DataSvcFrameDeliveryIdentity):
    """
    Service Frame are conditionally
    delivered to the destination UNI.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        DataSvcFrameDeliveryIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['ConditionalIdentity']['meta_info']


class CosIdEvcPcpIdentity(CosIdIdentity):
    """
    Identity of cos id based on EVC and PCP
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        CosIdIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['CosIdEvcPcpIdentity']['meta_info']


class HubSpokeDisjointIdentity(VpnTopologyIdentity):
    """
    Identity for Hub'n'Spoke VPN topology
    where Hubs cannot talk between each other.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        VpnTopologyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['HubSpokeDisjointIdentity']['meta_info']


class PortIdentity(L2AccessTypeIdentity):
    """
    Port
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        L2AccessTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['PortIdentity']['meta_info']


class ColorIdEvcIdentity(ColorIdIdentity):
    """
    Identity of color id base on EVC
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        ColorIdIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['ColorIdEvcIdentity']['meta_info']


class InvalidCcmIdentity(FaultAlarmDefectTypeIdentity):
    """
    Indicates that one or more invalid CCMs has been
    received and that 3.5 times that CCMs transmission
    interval has not yet expired.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        FaultAlarmDefectTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['InvalidCcmIdentity']['meta_info']


class OpaqueIdentity(BwTypeIdentity):
    """
    Opaque
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        BwTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['OpaqueIdentity']['meta_info']


class PeDiverseIdentity(PlacementDiversityIdentity):
    """
    Identity for PE diversity
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        PlacementDiversityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['PeDiverseIdentity']['meta_info']


class SamePeIdentity(PlacementDiversityIdentity):
    """
    Identity for having sites connected
    on the same PE
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        PlacementDiversityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['SamePeIdentity']['meta_info']


class RedIdentity(ColorTypeIdentity):
    """
    Identity of red type
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        ColorTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['RedIdentity']['meta_info']


class ShutIdentity(LoopPreventionTypeIdentity):
    """
    Identity of shut protection
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        LoopPreventionTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['ShutIdentity']['meta_info']


class LinecardDiverseIdentity(PlacementDiversityIdentity):
    """
    Identity for linecard diversity
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        PlacementDiversityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['LinecardDiverseIdentity']['meta_info']


class BearerDiverseIdentity(PlacementDiversityIdentity):
    """
    Identity for bearer diversity.
    The bearers should not use common elements.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        PlacementDiversityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['BearerDiverseIdentity']['meta_info']


class AnyToAnyIdentity(VpnTopologyIdentity):
    """
    Identity for any to any VPN topology.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        VpnTopologyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['AnyToAnyIdentity']['meta_info']


class VrfIdentity(VpnSignalingTypeIdentity):
    """
    Virtual routing and forwarding (VRF).
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        VpnSignalingTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['VrfIdentity']['meta_info']


class AnyToAnyRoleIdentity(SiteRoleIdentity):
    """
    Site in an any to any IPVPN.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        SiteRoleIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['AnyToAnyRoleIdentity']['meta_info']


class LacpActiveIdentity(LacpModeIdentity):
    """
    Identity of LACP active
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        LacpModeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['LacpActiveIdentity']['meta_info']


class MetroIdentity(PerfTierOptIdentity):
    """
    Identity of metro
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        PerfTierOptIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['MetroIdentity']['meta_info']


class PopDiverseIdentity(PlacementDiversityIdentity):
    """
    Identity for POP diversity
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        PlacementDiversityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['PopDiverseIdentity']['meta_info']


class MulticastIdentity(BumTypeIdentity):
    """
    Identity of multicast
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        BumTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['MulticastIdentity']['meta_info']


class RemoteInvalidCcmIdentity(FaultAlarmDefectTypeIdentity):
    """
    Indicates that at least one of the Remote MEP
    state machines is not receiving valid CCMs
    from its remote MEP.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        FaultAlarmDefectTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['RemoteInvalidCcmIdentity']['meta_info']


class DiscardIdentity(DataSvcFrameDeliveryIdentity):
    """
    Service Frames are discarded.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        DataSvcFrameDeliveryIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['DiscardIdentity']['meta_info']


class TwoRateThreeColorIdentity(PolicingIdentity):
    """
    Identity of two\-rate, three\-color (2R3C)
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        PolicingIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['TwoRateThreeColorIdentity']['meta_info']


class LacpPassiveIdentity(LacpModeIdentity):
    """
    Identity of LACP passive
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        LacpModeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['LacpPassiveIdentity']['meta_info']


class ContinentalIdentity(PerfTierOptIdentity):
    """
    Identity of continental
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        PerfTierOptIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['ContinentalIdentity']['meta_info']


class ControlPlaneIdentity(MacLearningModeIdentity):
    """
    User MAC addresses are advertised through EVPN\-BGP
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        MacLearningModeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['ControlPlaneIdentity']['meta_info']


class Ipv4Identity(AddressFamilyIdentity):
    """
    Identity for IPv4 address family.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['Ipv4Identity']['meta_info']


class Ipv6Identity(AddressFamilyIdentity):
    """
    Identity for IPv6 address family.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['Ipv6Identity']['meta_info']


class SubInterfaceIdentity(L2AccessTypeIdentity):
    """
    Create a default sub\-interface and keep vlan
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        L2AccessTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['SubInterfaceIdentity']['meta_info']


class BroadcastIdentity(BumTypeIdentity):
    """
    Identity of broadcast
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        BumTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['BroadcastIdentity']['meta_info']


class UniIdentity(SiteTypeIdentity):
    """
    Identity of User Network Interface 
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        SiteTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['UniIdentity']['meta_info']


class UntagIdentity(L2AccessTypeIdentity):
    """
    Untag
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        L2AccessTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['UntagIdentity']['meta_info']


class CustomerManagedIdentity(ManagementIdentity):
    """
    Base identity for customer managed site.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        ManagementIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['CustomerManagedIdentity']['meta_info']


class Dot1QIdentity(L2AccessTypeIdentity):
    """
    Qot1q
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        L2AccessTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['Dot1QIdentity']['meta_info']


class LacpOffIdentity(LacpStateIdentity):
    """
    Identity of LACP off
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        LacpStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['LacpOffIdentity']['meta_info']


class UnconditionalIdentity(DataSvcFrameDeliveryIdentity):
    """
    Service Frames are unconditionally
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        DataSvcFrameDeliveryIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['UnconditionalIdentity']['meta_info']


class UnicastIdentity(BumTypeIdentity):
    """
    Identity of unicast
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        BumTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['UnicastIdentity']['meta_info']


class LacpFastIdentity(LacpSpeedIdentity):
    """
    Identity of LACP fast
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        LacpSpeedIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['LacpFastIdentity']['meta_info']


class DelayIdentity(PmTypeIdentity):
    """
    Delay measurement
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        PmTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['DelayIdentity']['meta_info']


class ColorIdEvcCvlanIdentity(ColorIdIdentity):
    """
    Identity of color id base on EVC and CVLAN 
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        ColorIdIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['ColorIdEvcCvlanIdentity']['meta_info']


class GreenIdentity(ColorTypeIdentity):
    """
    Identity of green type
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        ColorTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['GreenIdentity']['meta_info']


class SpokeRoleIdentity(SiteRoleIdentity):
    """
    Spoke Site in a Hub &amp; Spoke IPVPN.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        SiteRoleIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['SpokeRoleIdentity']['meta_info']


class QinqIdentity(L2AccessTypeIdentity):
    """
    QinQ
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        L2AccessTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['QinqIdentity']['meta_info']


class PointToPointIdentity(SvcTopoTypeIdentity):
    """
    Point to Point.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        SvcTopoTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['PointToPointIdentity']['meta_info']


class CrossConnectCcmIdentity(FaultAlarmDefectTypeIdentity):
    """
    Indicates that one or more cross connect CCMs has been
    received and that 3.5 times of at least one of those
    CCMs transmission interval has not yet expired.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        FaultAlarmDefectTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['CrossConnectCcmIdentity']['meta_info']


class SameBearerIdentity(PlacementDiversityIdentity):
    """
    Identity for having sites connected
    using the same bearer
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        PlacementDiversityIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['SameBearerIdentity']['meta_info']


class All2OneBundlingIdentity(BundlingTypeIdentity):
    """
    Identity for all to one bundling
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        BundlingTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['All2OneBundlingIdentity']['meta_info']


class OvcIdentity(ServiceTypeIdentity):
    """
    OVC type.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        ServiceTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['OvcIdentity']['meta_info']


class VplsIdentity(L2VpnTypeIdentity):
    """
    Virtual Private LAN Service
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        L2VpnTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['VplsIdentity']['meta_info']


class CosIdEvcIdentity(CosIdIdentity):
    """
    Identity of cos id based on EVC
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        CosIdIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['CosIdEvcIdentity']['meta_info']


class VfiIdentity(VpnSignalingTypeIdentity):
    """
    Virtual forwarder interface
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        VpnSignalingTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['VfiIdentity']['meta_info']


class CosIdOvcEpIdentity(CosIdIdentity):
    """
    Identity of cos id based on OVC EP
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        CosIdIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['CosIdOvcEpIdentity']['meta_info']


class RemoteRdiIdentity(FaultAlarmDefectTypeIdentity):
    """
    Indicates the aggregate health of the remote MEPs.
    
    

    """

    _prefix = 'l2svc'
    _revision = '2017-02-13'

    def __init__(self):
        FaultAlarmDefectTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_l2vpn_svc as meta
        return meta._meta_table['RemoteRdiIdentity']['meta_info']



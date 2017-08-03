""" Cisco_IOS_XR_ip_mobileip_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-mobileip package configuration.

This module contains definitions
for the following management objects\:
  mobile\-ip\: MobileIP configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class EncapOpt(Enum):
    """
    EncapOpt

    Encap opt

    .. data:: greipv4 = 4

    	GRE IPv4 tunnel encap

    .. data:: greipv6 = 5

    	GRE IPv6 tunnel encap

    .. data:: mgreipv4 = 7

    	mGRE IPv4 tunnel encap

    .. data:: mgreipv6 = 8

    	mGRE IPv6 tunnel encap

    """

    greipv4 = Enum.YLeaf(4, "greipv4")

    greipv6 = Enum.YLeaf(5, "greipv6")

    mgreipv4 = Enum.YLeaf(7, "mgreipv4")

    mgreipv6 = Enum.YLeaf(8, "mgreipv6")


class GreKeyType(Enum):
    """
    GreKeyType

    Gre key type

    .. data:: symmetric = 1

    	Symmetric GRE Key (same Uplink and Downlink

    	key)

    """

    symmetric = Enum.YLeaf(1, "symmetric")


class LmaRat(Enum):
    """
    LmaRat

    Lma rat

    .. data:: virtual = 0

    	VIRTUAL rat

    .. data:: ppp = 1

    	PPP rat

    .. data:: ethernet = 2

    	ETHERNET rat

    .. data:: wlan = 3

    	WLAN rat

    .. data:: wi_max = 4

    	WIMAX rat

    .. data:: Y_3gppgeran = 5

    	3GPP_GERAN rat

    .. data:: Y_3gpputran = 6

    	3GPP_UTRAN rat

    .. data:: Y_3gppeutran = 7

    	3GPP_E_UTRAN rat

    .. data:: Y_3gpp2ehrpd = 8

    	3GPP2_EHRPD rat

    .. data:: Y_3gpp2hrpd = 9

    	3GPP2_HRPD rat

    .. data:: Y_3gpp21rtt = 10

    	3GPP2_1RTT rat

    .. data:: Y_3gpp2umb = 11

    	3GPP2_UMB rat

    """

    virtual = Enum.YLeaf(0, "virtual")

    ppp = Enum.YLeaf(1, "ppp")

    ethernet = Enum.YLeaf(2, "ethernet")

    wlan = Enum.YLeaf(3, "wlan")

    wi_max = Enum.YLeaf(4, "wi-max")

    Y_3gppgeran = Enum.YLeaf(5, "3gppgeran")

    Y_3gpputran = Enum.YLeaf(6, "3gpputran")

    Y_3gppeutran = Enum.YLeaf(7, "3gppeutran")

    Y_3gpp2ehrpd = Enum.YLeaf(8, "3gpp2ehrpd")

    Y_3gpp2hrpd = Enum.YLeaf(9, "3gpp2hrpd")

    Y_3gpp21rtt = Enum.YLeaf(10, "3gpp21rtt")

    Y_3gpp2umb = Enum.YLeaf(11, "3gpp2umb")


class LmaRole(Enum):
    """
    LmaRole

    Lma role

    .. data:: Y_3gma = 0

    	3GMA mode

    """

    Y_3gma = Enum.YLeaf(0, "3gma")


class LmaService(Enum):
    """
    LmaService

    Lma service

    .. data:: service_mll = 1

    	Wireless Private Routing service

    """

    service_mll = Enum.YLeaf(1, "service-mll")


class RedistSubType(Enum):
    """
    RedistSubType

    Redist sub type

    .. data:: host_prefix = 1

    	Redistribute HoA/HNP host prefix routes

    .. data:: disable = 2

    	Disable redistribution of HoA/HNP host and pool

    	refix routes

    """

    host_prefix = Enum.YLeaf(1, "host-prefix")

    disable = Enum.YLeaf(2, "disable")


class RedistType(Enum):
    """
    RedistType

    Redist type

    .. data:: home_address = 1

    	Redistribute HoA/HNP routes

    """

    home_address = Enum.YLeaf(1, "home-address")


class ServiceType(Enum):
    """
    ServiceType

    Service type

    .. data:: ipv4 = 1

    	ipv4 service type

    .. data:: ipv6 = 2

    	ipv6 service type

    .. data:: dual = 3

    	dual service type

    """

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")

    dual = Enum.YLeaf(3, "dual")



class MobileIp(Entity):
    """
    MobileIP configuration
    
    .. attribute:: domains
    
    	Table of Domain
    	**type**\:   :py:class:`Domains <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains>`
    
    .. attribute:: lmas
    
    	Table of LMA
    	**type**\:   :py:class:`Lmas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas>`
    
    

    """

    _prefix = 'ip-mobileip-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(MobileIp, self).__init__()
        self._top_entity = None

        self.yang_name = "mobile-ip"
        self.yang_parent_name = "Cisco-IOS-XR-ip-mobileip-cfg"

        self.domains = MobileIp.Domains()
        self.domains.parent = self
        self._children_name_map["domains"] = "domains"
        self._children_yang_names.add("domains")

        self.lmas = MobileIp.Lmas()
        self.lmas.parent = self
        self._children_name_map["lmas"] = "lmas"
        self._children_yang_names.add("lmas")


    class Domains(Entity):
        """
        Table of Domain
        
        .. attribute:: domain
        
        	PMIPv6 domain configuration
        	**type**\: list of    :py:class:`Domain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain>`
        
        

        """

        _prefix = 'ip-mobileip-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(MobileIp.Domains, self).__init__()

            self.yang_name = "domains"
            self.yang_parent_name = "mobile-ip"

            self.domain = YList(self)

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
                        super(MobileIp.Domains, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MobileIp.Domains, self).__setattr__(name, value)


        class Domain(Entity):
            """
            PMIPv6 domain configuration
            
            .. attribute:: domain_name  <key>
            
            	Domain Name
            	**type**\:  str
            
            	**length:** 1..125
            
            .. attribute:: authenticate_option
            
            	Authentication option between PMIPV6 entities
            	**type**\:   :py:class:`AuthenticateOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain.AuthenticateOption>`
            
            .. attribute:: enable
            
            	Enable PMIPv6 domain configuration. Deletion of this object also causes deletion of all associated objects under Domain
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: lmas
            
            	Table of LMA
            	**type**\:   :py:class:`Lmas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain.Lmas>`
            
            .. attribute:: mags
            
            	Table of MAG
            	**type**\:   :py:class:`Mags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain.Mags>`
            
            .. attribute:: nais
            
            	Table of NAI
            	**type**\:   :py:class:`Nais <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain.Nais>`
            
            

            """

            _prefix = 'ip-mobileip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(MobileIp.Domains.Domain, self).__init__()

                self.yang_name = "domain"
                self.yang_parent_name = "domains"

                self.domain_name = YLeaf(YType.str, "domain-name")

                self.enable = YLeaf(YType.empty, "enable")

                self.authenticate_option = MobileIp.Domains.Domain.AuthenticateOption()
                self.authenticate_option.parent = self
                self._children_name_map["authenticate_option"] = "authenticate-option"
                self._children_yang_names.add("authenticate-option")

                self.lmas = MobileIp.Domains.Domain.Lmas()
                self.lmas.parent = self
                self._children_name_map["lmas"] = "lmas"
                self._children_yang_names.add("lmas")

                self.mags = MobileIp.Domains.Domain.Mags()
                self.mags.parent = self
                self._children_name_map["mags"] = "mags"
                self._children_yang_names.add("mags")

                self.nais = MobileIp.Domains.Domain.Nais()
                self.nais.parent = self
                self._children_name_map["nais"] = "nais"
                self._children_yang_names.add("nais")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("domain_name",
                                "enable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MobileIp.Domains.Domain, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MobileIp.Domains.Domain, self).__setattr__(name, value)


            class Mags(Entity):
                """
                Table of MAG
                
                .. attribute:: mag
                
                	MAG within domain
                	**type**\: list of    :py:class:`Mag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain.Mags.Mag>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Domains.Domain.Mags, self).__init__()

                    self.yang_name = "mags"
                    self.yang_parent_name = "domain"

                    self.mag = YList(self)

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
                                super(MobileIp.Domains.Domain.Mags, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MobileIp.Domains.Domain.Mags, self).__setattr__(name, value)


                class Mag(Entity):
                    """
                    MAG within domain
                    
                    .. attribute:: mag_name  <key>
                    
                    	MAG Identifier
                    	**type**\:  str
                    
                    	**length:** 1..125
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MobileIp.Domains.Domain.Mags.Mag, self).__init__()

                        self.yang_name = "mag"
                        self.yang_parent_name = "mags"

                        self.mag_name = YLeaf(YType.str, "mag-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("mag_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MobileIp.Domains.Domain.Mags.Mag, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MobileIp.Domains.Domain.Mags.Mag, self).__setattr__(name, value)

                    def has_data(self):
                        return self.mag_name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.mag_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "mag" + "[mag-name='" + self.mag_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.mag_name.is_set or self.mag_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mag_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "mag-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "mag-name"):
                            self.mag_name = value
                            self.mag_name.value_namespace = name_space
                            self.mag_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.mag:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.mag:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "mags" + path_buffer

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

                    if (child_yang_name == "mag"):
                        for c in self.mag:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = MobileIp.Domains.Domain.Mags.Mag()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.mag.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "mag"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Nais(Entity):
                """
                Table of NAI
                
                .. attribute:: nai
                
                	Network access identifier or Realm
                	**type**\: list of    :py:class:`Nai <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain.Nais.Nai>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Domains.Domain.Nais, self).__init__()

                    self.yang_name = "nais"
                    self.yang_parent_name = "domain"

                    self.nai = YList(self)

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
                                super(MobileIp.Domains.Domain.Nais, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MobileIp.Domains.Domain.Nais, self).__setattr__(name, value)


                class Nai(Entity):
                    """
                    Network access identifier or Realm
                    
                    .. attribute:: nai_name  <key>
                    
                    	MN Identifier
                    	**type**\:  str
                    
                    	**length:** 1..125
                    
                    .. attribute:: apn
                    
                    	Access point network for this MN
                    	**type**\:  str
                    
                    	**length:** 1..125
                    
                    .. attribute:: customer
                    
                    	Customer name for this MN
                    	**type**\:  str
                    
                    	**length:** 1..125
                    
                    .. attribute:: lma
                    
                    	LMA for this MN
                    	**type**\:  str
                    
                    	**length:** 1..125
                    
                    .. attribute:: network
                    
                    	Network name (Address pool) for this MN
                    	**type**\:  str
                    
                    	**length:** 1..125
                    
                    .. attribute:: service
                    
                    	Service type for this MN
                    	**type**\:   :py:class:`ServiceType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.ServiceType>`
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MobileIp.Domains.Domain.Nais.Nai, self).__init__()

                        self.yang_name = "nai"
                        self.yang_parent_name = "nais"

                        self.nai_name = YLeaf(YType.str, "nai-name")

                        self.apn = YLeaf(YType.str, "apn")

                        self.customer = YLeaf(YType.str, "customer")

                        self.lma = YLeaf(YType.str, "lma")

                        self.network = YLeaf(YType.str, "network")

                        self.service = YLeaf(YType.enumeration, "service")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("nai_name",
                                        "apn",
                                        "customer",
                                        "lma",
                                        "network",
                                        "service") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MobileIp.Domains.Domain.Nais.Nai, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MobileIp.Domains.Domain.Nais.Nai, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.nai_name.is_set or
                            self.apn.is_set or
                            self.customer.is_set or
                            self.lma.is_set or
                            self.network.is_set or
                            self.service.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.nai_name.yfilter != YFilter.not_set or
                            self.apn.yfilter != YFilter.not_set or
                            self.customer.yfilter != YFilter.not_set or
                            self.lma.yfilter != YFilter.not_set or
                            self.network.yfilter != YFilter.not_set or
                            self.service.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "nai" + "[nai-name='" + self.nai_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.nai_name.is_set or self.nai_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nai_name.get_name_leafdata())
                        if (self.apn.is_set or self.apn.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.apn.get_name_leafdata())
                        if (self.customer.is_set or self.customer.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.customer.get_name_leafdata())
                        if (self.lma.is_set or self.lma.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lma.get_name_leafdata())
                        if (self.network.is_set or self.network.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.network.get_name_leafdata())
                        if (self.service.is_set or self.service.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.service.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "nai-name" or name == "apn" or name == "customer" or name == "lma" or name == "network" or name == "service"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "nai-name"):
                            self.nai_name = value
                            self.nai_name.value_namespace = name_space
                            self.nai_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "apn"):
                            self.apn = value
                            self.apn.value_namespace = name_space
                            self.apn.value_namespace_prefix = name_space_prefix
                        if(value_path == "customer"):
                            self.customer = value
                            self.customer.value_namespace = name_space
                            self.customer.value_namespace_prefix = name_space_prefix
                        if(value_path == "lma"):
                            self.lma = value
                            self.lma.value_namespace = name_space
                            self.lma.value_namespace_prefix = name_space_prefix
                        if(value_path == "network"):
                            self.network = value
                            self.network.value_namespace = name_space
                            self.network.value_namespace_prefix = name_space_prefix
                        if(value_path == "service"):
                            self.service = value
                            self.service.value_namespace = name_space
                            self.service.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.nai:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.nai:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "nais" + path_buffer

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

                    if (child_yang_name == "nai"):
                        for c in self.nai:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = MobileIp.Domains.Domain.Nais.Nai()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.nai.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "nai"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class AuthenticateOption(Entity):
                """
                Authentication option between PMIPV6 entities
                
                .. attribute:: key
                
                	ASCII string
                	**type**\:  str
                
                	**length:** 1..125
                
                .. attribute:: spi
                
                	SPI in hex value
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Domains.Domain.AuthenticateOption, self).__init__()

                    self.yang_name = "authenticate-option"
                    self.yang_parent_name = "domain"

                    self.key = YLeaf(YType.str, "key")

                    self.spi = YLeaf(YType.str, "spi")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("key",
                                    "spi") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MobileIp.Domains.Domain.AuthenticateOption, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MobileIp.Domains.Domain.AuthenticateOption, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.key.is_set or
                        self.spi.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.key.yfilter != YFilter.not_set or
                        self.spi.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "authenticate-option" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.key.is_set or self.key.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.key.get_name_leafdata())
                    if (self.spi.is_set or self.spi.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.spi.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "key" or name == "spi"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "key"):
                        self.key = value
                        self.key.value_namespace = name_space
                        self.key.value_namespace_prefix = name_space_prefix
                    if(value_path == "spi"):
                        self.spi = value
                        self.spi.value_namespace = name_space
                        self.spi.value_namespace_prefix = name_space_prefix


            class Lmas(Entity):
                """
                Table of LMA
                
                .. attribute:: lma
                
                	LMA within domain
                	**type**\: list of    :py:class:`Lma <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Domains.Domain.Lmas.Lma>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Domains.Domain.Lmas, self).__init__()

                    self.yang_name = "lmas"
                    self.yang_parent_name = "domain"

                    self.lma = YList(self)

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
                                super(MobileIp.Domains.Domain.Lmas, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MobileIp.Domains.Domain.Lmas, self).__setattr__(name, value)


                class Lma(Entity):
                    """
                    LMA within domain
                    
                    .. attribute:: lma_name  <key>
                    
                    	LMA Identifier
                    	**type**\:  str
                    
                    	**length:** 1..125
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MobileIp.Domains.Domain.Lmas.Lma, self).__init__()

                        self.yang_name = "lma"
                        self.yang_parent_name = "lmas"

                        self.lma_name = YLeaf(YType.str, "lma-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("lma_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MobileIp.Domains.Domain.Lmas.Lma, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MobileIp.Domains.Domain.Lmas.Lma, self).__setattr__(name, value)

                    def has_data(self):
                        return self.lma_name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.lma_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "lma" + "[lma-name='" + self.lma_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.lma_name.is_set or self.lma_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lma_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "lma-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "lma-name"):
                            self.lma_name = value
                            self.lma_name.value_namespace = name_space
                            self.lma_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.lma:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.lma:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "lmas" + path_buffer

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

                    if (child_yang_name == "lma"):
                        for c in self.lma:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = MobileIp.Domains.Domain.Lmas.Lma()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.lma.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "lma"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.domain_name.is_set or
                    self.enable.is_set or
                    (self.authenticate_option is not None and self.authenticate_option.has_data()) or
                    (self.lmas is not None and self.lmas.has_data()) or
                    (self.mags is not None and self.mags.has_data()) or
                    (self.nais is not None and self.nais.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.domain_name.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set or
                    (self.authenticate_option is not None and self.authenticate_option.has_operation()) or
                    (self.lmas is not None and self.lmas.has_operation()) or
                    (self.mags is not None and self.mags.has_operation()) or
                    (self.nais is not None and self.nais.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "domain" + "[domain-name='" + self.domain_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-mobileip-cfg:mobile-ip/domains/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.domain_name.is_set or self.domain_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.domain_name.get_name_leafdata())
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "authenticate-option"):
                    if (self.authenticate_option is None):
                        self.authenticate_option = MobileIp.Domains.Domain.AuthenticateOption()
                        self.authenticate_option.parent = self
                        self._children_name_map["authenticate_option"] = "authenticate-option"
                    return self.authenticate_option

                if (child_yang_name == "lmas"):
                    if (self.lmas is None):
                        self.lmas = MobileIp.Domains.Domain.Lmas()
                        self.lmas.parent = self
                        self._children_name_map["lmas"] = "lmas"
                    return self.lmas

                if (child_yang_name == "mags"):
                    if (self.mags is None):
                        self.mags = MobileIp.Domains.Domain.Mags()
                        self.mags.parent = self
                        self._children_name_map["mags"] = "mags"
                    return self.mags

                if (child_yang_name == "nais"):
                    if (self.nais is None):
                        self.nais = MobileIp.Domains.Domain.Nais()
                        self.nais.parent = self
                        self._children_name_map["nais"] = "nais"
                    return self.nais

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "authenticate-option" or name == "lmas" or name == "mags" or name == "nais" or name == "domain-name" or name == "enable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "domain-name"):
                    self.domain_name = value
                    self.domain_name.value_namespace = name_space
                    self.domain_name.value_namespace_prefix = name_space_prefix
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.domain:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.domain:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "domains" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-mobileip-cfg:mobile-ip/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "domain"):
                for c in self.domain:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MobileIp.Domains.Domain()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.domain.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "domain"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Lmas(Entity):
        """
        Table of LMA
        
        .. attribute:: lma
        
        	PMIPv6 LMA configuration
        	**type**\: list of    :py:class:`Lma <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma>`
        
        

        """

        _prefix = 'ip-mobileip-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(MobileIp.Lmas, self).__init__()

            self.yang_name = "lmas"
            self.yang_parent_name = "mobile-ip"

            self.lma = YList(self)

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
                        super(MobileIp.Lmas, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MobileIp.Lmas, self).__setattr__(name, value)


        class Lma(Entity):
            """
            PMIPv6 LMA configuration
            
            .. attribute:: lma_name  <key>
            
            	LMA name
            	**type**\:  str
            
            	**length:** 1..125
            
            .. attribute:: domain_name  <key>
            
            	Domain name
            	**type**\:  str
            
            	**length:** 1..125
            
            .. attribute:: aaa
            
            	AAA configuration for this LMA
            	**type**\:   :py:class:`Aaa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Aaa>`
            
            .. attribute:: ani
            
            	enable ani option processing in LMA
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: binding_attributes
            
            	LMA binding attributes
            	**type**\:   :py:class:`BindingAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.BindingAttributes>`
            
            .. attribute:: binding_revocation_attributes
            
            	LMA Binding Revocation Attributes
            	**type**\:   :py:class:`BindingRevocationAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.BindingRevocationAttributes>`
            
            .. attribute:: default_profile
            
            	Default MN profile for LMA
            	**type**\:  str
            
            	**length:** 1..125
            
            .. attribute:: dscp
            
            	DSCP for packets originating from this LMA
            	**type**\:   :py:class:`Dscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Dscp>`
            
            .. attribute:: dynamic
            
            	enable dynamic mag learning for LMA
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enforce
            
            	enforce heartbeat values to MAG
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: generate
            
            	generate gre key for LMA bindings
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: heart_beat_attributes
            
            	heartbeat config for this LMA
            	**type**\:   :py:class:`HeartBeatAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.HeartBeatAttributes>`
            
            .. attribute:: hnp
            
            	LMA HNP options
            	**type**\:   :py:class:`Hnp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Hnp>`
            
            .. attribute:: interface
            
            	CN facing interface name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: lmaipv4_addresses
            
            	Table of LMAIPv4Address
            	**type**\:   :py:class:`Lmaipv4Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Lmaipv4Addresses>`
            
            .. attribute:: lmaipv6_addresses
            
            	Table of LMAIPv6Address
            	**type**\:   :py:class:`Lmaipv6Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Lmaipv6Addresses>`
            
            .. attribute:: mags
            
            	Table of MAG
            	**type**\:   :py:class:`Mags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Mags>`
            
            .. attribute:: mobile_map
            
            	Mobile Map for this LMA
            	**type**\:  str
            
            	**length:** 1..125
            
            .. attribute:: mobile_route_ad
            
            	Specify the Admin Distance value
            	**type**\:  int
            
            	**range:** 1..254
            
            .. attribute:: multipath
            
            	enable multipath support for LMA
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: networks
            
            	Table of Network
            	**type**\:   :py:class:`Networks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks>`
            
            .. attribute:: pgw_subs_cont
            
            	Feature related to interface with PGW
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: rat_attributes
            
            	Radio access technology type config  this LMA
            	**type**\:   :py:class:`RatAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.RatAttributes>`
            
            .. attribute:: redistribute
            
            	Redistribute routes
            	**type**\:   :py:class:`Redistribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Redistribute>`
            
            .. attribute:: replay_protection
            
            	Replay Protection Method
            	**type**\:   :py:class:`ReplayProtection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.ReplayProtection>`
            
            .. attribute:: roles
            
            	Table of Role
            	**type**\:   :py:class:`Roles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Roles>`
            
            .. attribute:: services
            
            	Table of Service
            	**type**\:   :py:class:`Services <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services>`
            
            .. attribute:: tunnel_attributes
            
            	tunnel attributes
            	**type**\:   :py:class:`TunnelAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.TunnelAttributes>`
            
            

            """

            _prefix = 'ip-mobileip-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(MobileIp.Lmas.Lma, self).__init__()

                self.yang_name = "lma"
                self.yang_parent_name = "lmas"

                self.lma_name = YLeaf(YType.str, "lma-name")

                self.domain_name = YLeaf(YType.str, "domain-name")

                self.ani = YLeaf(YType.empty, "ani")

                self.default_profile = YLeaf(YType.str, "default-profile")

                self.dynamic = YLeaf(YType.empty, "dynamic")

                self.enforce = YLeaf(YType.empty, "enforce")

                self.generate = YLeaf(YType.empty, "generate")

                self.interface = YLeaf(YType.str, "interface")

                self.mobile_map = YLeaf(YType.str, "mobile-map")

                self.mobile_route_ad = YLeaf(YType.uint32, "mobile-route-ad")

                self.multipath = YLeaf(YType.empty, "multipath")

                self.pgw_subs_cont = YLeaf(YType.empty, "pgw-subs-cont")

                self.aaa = MobileIp.Lmas.Lma.Aaa()
                self.aaa.parent = self
                self._children_name_map["aaa"] = "aaa"
                self._children_yang_names.add("aaa")

                self.binding_attributes = MobileIp.Lmas.Lma.BindingAttributes()
                self.binding_attributes.parent = self
                self._children_name_map["binding_attributes"] = "binding-attributes"
                self._children_yang_names.add("binding-attributes")

                self.binding_revocation_attributes = MobileIp.Lmas.Lma.BindingRevocationAttributes()
                self.binding_revocation_attributes.parent = self
                self._children_name_map["binding_revocation_attributes"] = "binding-revocation-attributes"
                self._children_yang_names.add("binding-revocation-attributes")

                self.dscp = MobileIp.Lmas.Lma.Dscp()
                self.dscp.parent = self
                self._children_name_map["dscp"] = "dscp"
                self._children_yang_names.add("dscp")

                self.heart_beat_attributes = MobileIp.Lmas.Lma.HeartBeatAttributes()
                self.heart_beat_attributes.parent = self
                self._children_name_map["heart_beat_attributes"] = "heart-beat-attributes"
                self._children_yang_names.add("heart-beat-attributes")

                self.hnp = MobileIp.Lmas.Lma.Hnp()
                self.hnp.parent = self
                self._children_name_map["hnp"] = "hnp"
                self._children_yang_names.add("hnp")

                self.lmaipv4_addresses = MobileIp.Lmas.Lma.Lmaipv4Addresses()
                self.lmaipv4_addresses.parent = self
                self._children_name_map["lmaipv4_addresses"] = "lmaipv4-addresses"
                self._children_yang_names.add("lmaipv4-addresses")

                self.lmaipv6_addresses = MobileIp.Lmas.Lma.Lmaipv6Addresses()
                self.lmaipv6_addresses.parent = self
                self._children_name_map["lmaipv6_addresses"] = "lmaipv6-addresses"
                self._children_yang_names.add("lmaipv6-addresses")

                self.mags = MobileIp.Lmas.Lma.Mags()
                self.mags.parent = self
                self._children_name_map["mags"] = "mags"
                self._children_yang_names.add("mags")

                self.networks = MobileIp.Lmas.Lma.Networks()
                self.networks.parent = self
                self._children_name_map["networks"] = "networks"
                self._children_yang_names.add("networks")

                self.rat_attributes = MobileIp.Lmas.Lma.RatAttributes()
                self.rat_attributes.parent = self
                self._children_name_map["rat_attributes"] = "rat-attributes"
                self._children_yang_names.add("rat-attributes")

                self.redistribute = MobileIp.Lmas.Lma.Redistribute()
                self.redistribute.parent = self
                self._children_name_map["redistribute"] = "redistribute"
                self._children_yang_names.add("redistribute")

                self.replay_protection = MobileIp.Lmas.Lma.ReplayProtection()
                self.replay_protection.parent = self
                self._children_name_map["replay_protection"] = "replay-protection"
                self._children_yang_names.add("replay-protection")

                self.roles = MobileIp.Lmas.Lma.Roles()
                self.roles.parent = self
                self._children_name_map["roles"] = "roles"
                self._children_yang_names.add("roles")

                self.services = MobileIp.Lmas.Lma.Services()
                self.services.parent = self
                self._children_name_map["services"] = "services"
                self._children_yang_names.add("services")

                self.tunnel_attributes = MobileIp.Lmas.Lma.TunnelAttributes()
                self.tunnel_attributes.parent = self
                self._children_name_map["tunnel_attributes"] = "tunnel-attributes"
                self._children_yang_names.add("tunnel-attributes")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("lma_name",
                                "domain_name",
                                "ani",
                                "default_profile",
                                "dynamic",
                                "enforce",
                                "generate",
                                "interface",
                                "mobile_map",
                                "mobile_route_ad",
                                "multipath",
                                "pgw_subs_cont") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MobileIp.Lmas.Lma, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MobileIp.Lmas.Lma, self).__setattr__(name, value)


            class BindingRevocationAttributes(Entity):
                """
                LMA Binding Revocation Attributes
                
                .. attribute:: delay
                
                	Time to wait before Retransmitting BRI Message
                	**type**\:   :py:class:`Delay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.BindingRevocationAttributes.Delay>`
                
                .. attribute:: retry
                
                	Number of Retransmissons Allowed for BRI Message
                	**type**\:  int
                
                	**range:** 1..10
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.BindingRevocationAttributes, self).__init__()

                    self.yang_name = "binding-revocation-attributes"
                    self.yang_parent_name = "lma"

                    self.retry = YLeaf(YType.uint32, "retry")

                    self.delay = MobileIp.Lmas.Lma.BindingRevocationAttributes.Delay()
                    self.delay.parent = self
                    self._children_name_map["delay"] = "delay"
                    self._children_yang_names.add("delay")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("retry") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MobileIp.Lmas.Lma.BindingRevocationAttributes, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MobileIp.Lmas.Lma.BindingRevocationAttributes, self).__setattr__(name, value)


                class Delay(Entity):
                    """
                    Time to wait before Retransmitting BRI
                    Message
                    
                    .. attribute:: br_max
                    
                    	Specify in millisec
                    	**type**\:  int
                    
                    	**range:** 500..65535
                    
                    .. attribute:: br_min
                    
                    	Specify in millisec
                    	**type**\:  int
                    
                    	**range:** 500..65535
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MobileIp.Lmas.Lma.BindingRevocationAttributes.Delay, self).__init__()

                        self.yang_name = "delay"
                        self.yang_parent_name = "binding-revocation-attributes"

                        self.br_max = YLeaf(YType.uint32, "br-max")

                        self.br_min = YLeaf(YType.uint32, "br-min")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("br_max",
                                        "br_min") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MobileIp.Lmas.Lma.BindingRevocationAttributes.Delay, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MobileIp.Lmas.Lma.BindingRevocationAttributes.Delay, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.br_max.is_set or
                            self.br_min.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.br_max.yfilter != YFilter.not_set or
                            self.br_min.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "delay" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.br_max.is_set or self.br_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.br_max.get_name_leafdata())
                        if (self.br_min.is_set or self.br_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.br_min.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "br-max" or name == "br-min"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "br-max"):
                            self.br_max = value
                            self.br_max.value_namespace = name_space
                            self.br_max.value_namespace_prefix = name_space_prefix
                        if(value_path == "br-min"):
                            self.br_min = value
                            self.br_min.value_namespace = name_space
                            self.br_min.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.retry.is_set or
                        (self.delay is not None and self.delay.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.retry.yfilter != YFilter.not_set or
                        (self.delay is not None and self.delay.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "binding-revocation-attributes" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.retry.is_set or self.retry.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.retry.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "delay"):
                        if (self.delay is None):
                            self.delay = MobileIp.Lmas.Lma.BindingRevocationAttributes.Delay()
                            self.delay.parent = self
                            self._children_name_map["delay"] = "delay"
                        return self.delay

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "delay" or name == "retry"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "retry"):
                        self.retry = value
                        self.retry.value_namespace = name_space
                        self.retry.value_namespace_prefix = name_space_prefix


            class RatAttributes(Entity):
                """
                Radio access technology type config  this LMA
                
                .. attribute:: lma_rat
                
                	LMA rat type
                	**type**\:   :py:class:`LmaRat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.LmaRat>`
                
                .. attribute:: priority_value
                
                	Specify the priority value
                	**type**\:  int
                
                	**range:** 1..255
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.RatAttributes, self).__init__()

                    self.yang_name = "rat-attributes"
                    self.yang_parent_name = "lma"

                    self.lma_rat = YLeaf(YType.enumeration, "lma-rat")

                    self.priority_value = YLeaf(YType.uint32, "priority-value")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("lma_rat",
                                    "priority_value") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MobileIp.Lmas.Lma.RatAttributes, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MobileIp.Lmas.Lma.RatAttributes, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.lma_rat.is_set or
                        self.priority_value.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.lma_rat.yfilter != YFilter.not_set or
                        self.priority_value.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "rat-attributes" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.lma_rat.is_set or self.lma_rat.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.lma_rat.get_name_leafdata())
                    if (self.priority_value.is_set or self.priority_value.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.priority_value.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "lma-rat" or name == "priority-value"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "lma-rat"):
                        self.lma_rat = value
                        self.lma_rat.value_namespace = name_space
                        self.lma_rat.value_namespace_prefix = name_space_prefix
                    if(value_path == "priority-value"):
                        self.priority_value = value
                        self.priority_value.value_namespace = name_space
                        self.priority_value.value_namespace_prefix = name_space_prefix


            class HeartBeatAttributes(Entity):
                """
                heartbeat config for this LMA
                
                .. attribute:: interval
                
                	Specify the interval value in second
                	**type**\:  int
                
                	**range:** 10..3600
                
                .. attribute:: retries
                
                	Specify the retry value
                	**type**\:  int
                
                	**range:** 1..10
                
                .. attribute:: timeout
                
                	Specify the timeout value
                	**type**\:  int
                
                	**range:** 1..3600
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.HeartBeatAttributes, self).__init__()

                    self.yang_name = "heart-beat-attributes"
                    self.yang_parent_name = "lma"

                    self.interval = YLeaf(YType.uint32, "interval")

                    self.retries = YLeaf(YType.uint32, "retries")

                    self.timeout = YLeaf(YType.uint32, "timeout")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interval",
                                    "retries",
                                    "timeout") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MobileIp.Lmas.Lma.HeartBeatAttributes, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MobileIp.Lmas.Lma.HeartBeatAttributes, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.interval.is_set or
                        self.retries.is_set or
                        self.timeout.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interval.yfilter != YFilter.not_set or
                        self.retries.yfilter != YFilter.not_set or
                        self.timeout.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "heart-beat-attributes" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interval.is_set or self.interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interval.get_name_leafdata())
                    if (self.retries.is_set or self.retries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.retries.get_name_leafdata())
                    if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.timeout.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interval" or name == "retries" or name == "timeout"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interval"):
                        self.interval = value
                        self.interval.value_namespace = name_space
                        self.interval.value_namespace_prefix = name_space_prefix
                    if(value_path == "retries"):
                        self.retries = value
                        self.retries.value_namespace = name_space
                        self.retries.value_namespace_prefix = name_space_prefix
                    if(value_path == "timeout"):
                        self.timeout = value
                        self.timeout.value_namespace = name_space
                        self.timeout.value_namespace_prefix = name_space_prefix


            class Lmaipv6Addresses(Entity):
                """
                Table of LMAIPv6Address
                
                .. attribute:: lmaipv6_address
                
                	Configure IPv6 address for this LMA
                	**type**\: list of    :py:class:`Lmaipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Lmaipv6Addresses.Lmaipv6Address>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.Lmaipv6Addresses, self).__init__()

                    self.yang_name = "lmaipv6-addresses"
                    self.yang_parent_name = "lma"

                    self.lmaipv6_address = YList(self)

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
                                super(MobileIp.Lmas.Lma.Lmaipv6Addresses, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MobileIp.Lmas.Lma.Lmaipv6Addresses, self).__setattr__(name, value)


                class Lmaipv6Address(Entity):
                    """
                    Configure IPv6 address for this LMA
                    
                    .. attribute:: address  <key>
                    
                    	LMA IPv6 address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MobileIp.Lmas.Lma.Lmaipv6Addresses.Lmaipv6Address, self).__init__()

                        self.yang_name = "lmaipv6-address"
                        self.yang_parent_name = "lmaipv6-addresses"

                        self.address = YLeaf(YType.str, "address")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("address") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MobileIp.Lmas.Lma.Lmaipv6Addresses.Lmaipv6Address, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MobileIp.Lmas.Lma.Lmaipv6Addresses.Lmaipv6Address, self).__setattr__(name, value)

                    def has_data(self):
                        return self.address.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "lmaipv6-address" + "[address='" + self.address.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address"):
                            self.address = value
                            self.address.value_namespace = name_space
                            self.address.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.lmaipv6_address:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.lmaipv6_address:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "lmaipv6-addresses" + path_buffer

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

                    if (child_yang_name == "lmaipv6-address"):
                        for c in self.lmaipv6_address:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = MobileIp.Lmas.Lma.Lmaipv6Addresses.Lmaipv6Address()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.lmaipv6_address.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "lmaipv6-address"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Hnp(Entity):
                """
                LMA HNP options
                
                .. attribute:: maximum
                
                	maximum HNPs allowed per MN interface
                	**type**\:  int
                
                	**range:** 1..3
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.Hnp, self).__init__()

                    self.yang_name = "hnp"
                    self.yang_parent_name = "lma"

                    self.maximum = YLeaf(YType.uint32, "maximum")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("maximum") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MobileIp.Lmas.Lma.Hnp, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MobileIp.Lmas.Lma.Hnp, self).__setattr__(name, value)

                def has_data(self):
                    return self.maximum.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.maximum.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "hnp" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.maximum.is_set or self.maximum.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.maximum.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "maximum"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "maximum"):
                        self.maximum = value
                        self.maximum.value_namespace = name_space
                        self.maximum.value_namespace_prefix = name_space_prefix


            class Redistribute(Entity):
                """
                Redistribute routes
                
                .. attribute:: redist_sub_type
                
                	Redistribute sub\-type
                	**type**\:   :py:class:`RedistSubType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.RedistSubType>`
                
                .. attribute:: redist_type
                
                	Redistribute type
                	**type**\:   :py:class:`RedistType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.RedistType>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.Redistribute, self).__init__()

                    self.yang_name = "redistribute"
                    self.yang_parent_name = "lma"

                    self.redist_sub_type = YLeaf(YType.enumeration, "redist-sub-type")

                    self.redist_type = YLeaf(YType.enumeration, "redist-type")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("redist_sub_type",
                                    "redist_type") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MobileIp.Lmas.Lma.Redistribute, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MobileIp.Lmas.Lma.Redistribute, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.redist_sub_type.is_set or
                        self.redist_type.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.redist_sub_type.yfilter != YFilter.not_set or
                        self.redist_type.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "redistribute" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.redist_sub_type.is_set or self.redist_sub_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.redist_sub_type.get_name_leafdata())
                    if (self.redist_type.is_set or self.redist_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.redist_type.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "redist-sub-type" or name == "redist-type"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "redist-sub-type"):
                        self.redist_sub_type = value
                        self.redist_sub_type.value_namespace = name_space
                        self.redist_sub_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "redist-type"):
                        self.redist_type = value
                        self.redist_type.value_namespace = name_space
                        self.redist_type.value_namespace_prefix = name_space_prefix


            class Aaa(Entity):
                """
                AAA configuration for this LMA
                
                .. attribute:: accounting
                
                	AAA accounting for this LMA
                	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Aaa.Accounting>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.Aaa, self).__init__()

                    self.yang_name = "aaa"
                    self.yang_parent_name = "lma"

                    self.accounting = MobileIp.Lmas.Lma.Aaa.Accounting()
                    self.accounting.parent = self
                    self._children_name_map["accounting"] = "accounting"
                    self._children_yang_names.add("accounting")


                class Accounting(Entity):
                    """
                    AAA accounting for this LMA
                    
                    .. attribute:: enable
                    
                    	Set constant integer
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: interim_interval
                    
                    	Interim acounting interval (in minutes)
                    	**type**\:  int
                    
                    	**range:** 1..86400
                    
                    	**units**\: minute
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MobileIp.Lmas.Lma.Aaa.Accounting, self).__init__()

                        self.yang_name = "accounting"
                        self.yang_parent_name = "aaa"

                        self.enable = YLeaf(YType.empty, "enable")

                        self.interim_interval = YLeaf(YType.uint32, "interim-interval")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("enable",
                                        "interim_interval") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MobileIp.Lmas.Lma.Aaa.Accounting, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MobileIp.Lmas.Lma.Aaa.Accounting, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.enable.is_set or
                            self.interim_interval.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.enable.yfilter != YFilter.not_set or
                            self.interim_interval.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "accounting" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enable.get_name_leafdata())
                        if (self.interim_interval.is_set or self.interim_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interim_interval.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "enable" or name == "interim-interval"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "enable"):
                            self.enable = value
                            self.enable.value_namespace = name_space
                            self.enable.value_namespace_prefix = name_space_prefix
                        if(value_path == "interim-interval"):
                            self.interim_interval = value
                            self.interim_interval.value_namespace = name_space
                            self.interim_interval.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.accounting is not None and self.accounting.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.accounting is not None and self.accounting.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "aaa" + path_buffer

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

                    if (child_yang_name == "accounting"):
                        if (self.accounting is None):
                            self.accounting = MobileIp.Lmas.Lma.Aaa.Accounting()
                            self.accounting.parent = self
                            self._children_name_map["accounting"] = "accounting"
                        return self.accounting

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "accounting"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Dscp(Entity):
                """
                DSCP for packets originating from this LMA
                
                .. attribute:: force
                
                	Set constant integer
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: value
                
                	Specify the DSCP value
                	**type**\:  int
                
                	**range:** 1..63
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.Dscp, self).__init__()

                    self.yang_name = "dscp"
                    self.yang_parent_name = "lma"

                    self.force = YLeaf(YType.empty, "force")

                    self.value = YLeaf(YType.uint32, "value")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("force",
                                    "value") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MobileIp.Lmas.Lma.Dscp, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MobileIp.Lmas.Lma.Dscp, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.force.is_set or
                        self.value.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.force.yfilter != YFilter.not_set or
                        self.value.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "dscp" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.force.is_set or self.force.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.force.get_name_leafdata())
                    if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.value.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "force" or name == "value"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "force"):
                        self.force = value
                        self.force.value_namespace = name_space
                        self.force.value_namespace_prefix = name_space_prefix
                    if(value_path == "value"):
                        self.value = value
                        self.value.value_namespace = name_space
                        self.value.value_namespace_prefix = name_space_prefix


            class Lmaipv4Addresses(Entity):
                """
                Table of LMAIPv4Address
                
                .. attribute:: lmaipv4_address
                
                	Configure IPv4 address for this LMA
                	**type**\: list of    :py:class:`Lmaipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Lmaipv4Addresses.Lmaipv4Address>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.Lmaipv4Addresses, self).__init__()

                    self.yang_name = "lmaipv4-addresses"
                    self.yang_parent_name = "lma"

                    self.lmaipv4_address = YList(self)

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
                                super(MobileIp.Lmas.Lma.Lmaipv4Addresses, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MobileIp.Lmas.Lma.Lmaipv4Addresses, self).__setattr__(name, value)


                class Lmaipv4Address(Entity):
                    """
                    Configure IPv4 address for this LMA
                    
                    .. attribute:: address  <key>
                    
                    	LMA IPv4 address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MobileIp.Lmas.Lma.Lmaipv4Addresses.Lmaipv4Address, self).__init__()

                        self.yang_name = "lmaipv4-address"
                        self.yang_parent_name = "lmaipv4-addresses"

                        self.address = YLeaf(YType.str, "address")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("address") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MobileIp.Lmas.Lma.Lmaipv4Addresses.Lmaipv4Address, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MobileIp.Lmas.Lma.Lmaipv4Addresses.Lmaipv4Address, self).__setattr__(name, value)

                    def has_data(self):
                        return self.address.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "lmaipv4-address" + "[address='" + self.address.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address"):
                            self.address = value
                            self.address.value_namespace = name_space
                            self.address.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.lmaipv4_address:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.lmaipv4_address:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "lmaipv4-addresses" + path_buffer

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

                    if (child_yang_name == "lmaipv4-address"):
                        for c in self.lmaipv4_address:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = MobileIp.Lmas.Lma.Lmaipv4Addresses.Lmaipv4Address()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.lmaipv4_address.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "lmaipv4-address"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Roles(Entity):
                """
                Table of Role
                
                .. attribute:: role
                
                	Role of this LMA
                	**type**\: list of    :py:class:`Role <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Roles.Role>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.Roles, self).__init__()

                    self.yang_name = "roles"
                    self.yang_parent_name = "lma"

                    self.role = YList(self)

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
                                super(MobileIp.Lmas.Lma.Roles, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MobileIp.Lmas.Lma.Roles, self).__setattr__(name, value)


                class Role(Entity):
                    """
                    Role of this LMA
                    
                    .. attribute:: lma_role  <key>
                    
                    	LMA role mode
                    	**type**\:   :py:class:`LmaRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.LmaRole>`
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MobileIp.Lmas.Lma.Roles.Role, self).__init__()

                        self.yang_name = "role"
                        self.yang_parent_name = "roles"

                        self.lma_role = YLeaf(YType.enumeration, "lma-role")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("lma_role") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MobileIp.Lmas.Lma.Roles.Role, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MobileIp.Lmas.Lma.Roles.Role, self).__setattr__(name, value)

                    def has_data(self):
                        return self.lma_role.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.lma_role.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "role" + "[lma-role='" + self.lma_role.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.lma_role.is_set or self.lma_role.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lma_role.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "lma-role"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "lma-role"):
                            self.lma_role = value
                            self.lma_role.value_namespace = name_space
                            self.lma_role.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.role:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.role:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "roles" + path_buffer

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

                    if (child_yang_name == "role"):
                        for c in self.role:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = MobileIp.Lmas.Lma.Roles.Role()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.role.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "role"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class BindingAttributes(Entity):
                """
                LMA binding attributes
                
                .. attribute:: create_wait_interval
                
                	bce create wait time interval
                	**type**\:  int
                
                	**range:** 100..65535
                
                .. attribute:: delete_wait_interval
                
                	bce delete wait time interval
                	**type**\:  int
                
                	**range:** 100..65535
                
                .. attribute:: max_life_time
                
                	Maximum bce lifetime permitted
                	**type**\:  int
                
                	**range:** 10..65535
                
                	**units**\: second
                
                .. attribute:: maximum
                
                	Specify max. number of bindings
                	**type**\:  int
                
                	**range:** 1..128000
                
                .. attribute:: refresh_time
                
                	Specify in seconds, (multiples of 4)
                	**type**\:  int
                
                	**range:** 4..65000
                
                	**units**\: second
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.BindingAttributes, self).__init__()

                    self.yang_name = "binding-attributes"
                    self.yang_parent_name = "lma"

                    self.create_wait_interval = YLeaf(YType.uint32, "create-wait-interval")

                    self.delete_wait_interval = YLeaf(YType.uint32, "delete-wait-interval")

                    self.max_life_time = YLeaf(YType.uint32, "max-life-time")

                    self.maximum = YLeaf(YType.uint32, "maximum")

                    self.refresh_time = YLeaf(YType.uint32, "refresh-time")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("create_wait_interval",
                                    "delete_wait_interval",
                                    "max_life_time",
                                    "maximum",
                                    "refresh_time") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MobileIp.Lmas.Lma.BindingAttributes, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MobileIp.Lmas.Lma.BindingAttributes, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.create_wait_interval.is_set or
                        self.delete_wait_interval.is_set or
                        self.max_life_time.is_set or
                        self.maximum.is_set or
                        self.refresh_time.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.create_wait_interval.yfilter != YFilter.not_set or
                        self.delete_wait_interval.yfilter != YFilter.not_set or
                        self.max_life_time.yfilter != YFilter.not_set or
                        self.maximum.yfilter != YFilter.not_set or
                        self.refresh_time.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "binding-attributes" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.create_wait_interval.is_set or self.create_wait_interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.create_wait_interval.get_name_leafdata())
                    if (self.delete_wait_interval.is_set or self.delete_wait_interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.delete_wait_interval.get_name_leafdata())
                    if (self.max_life_time.is_set or self.max_life_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max_life_time.get_name_leafdata())
                    if (self.maximum.is_set or self.maximum.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.maximum.get_name_leafdata())
                    if (self.refresh_time.is_set or self.refresh_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.refresh_time.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "create-wait-interval" or name == "delete-wait-interval" or name == "max-life-time" or name == "maximum" or name == "refresh-time"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "create-wait-interval"):
                        self.create_wait_interval = value
                        self.create_wait_interval.value_namespace = name_space
                        self.create_wait_interval.value_namespace_prefix = name_space_prefix
                    if(value_path == "delete-wait-interval"):
                        self.delete_wait_interval = value
                        self.delete_wait_interval.value_namespace = name_space
                        self.delete_wait_interval.value_namespace_prefix = name_space_prefix
                    if(value_path == "max-life-time"):
                        self.max_life_time = value
                        self.max_life_time.value_namespace = name_space
                        self.max_life_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "maximum"):
                        self.maximum = value
                        self.maximum.value_namespace = name_space
                        self.maximum.value_namespace_prefix = name_space_prefix
                    if(value_path == "refresh-time"):
                        self.refresh_time = value
                        self.refresh_time.value_namespace = name_space
                        self.refresh_time.value_namespace_prefix = name_space_prefix


            class Mags(Entity):
                """
                Table of MAG
                
                .. attribute:: mag
                
                	MAG within LMA
                	**type**\: list of    :py:class:`Mag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Mags.Mag>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.Mags, self).__init__()

                    self.yang_name = "mags"
                    self.yang_parent_name = "lma"

                    self.mag = YList(self)

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
                                super(MobileIp.Lmas.Lma.Mags, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MobileIp.Lmas.Lma.Mags, self).__setattr__(name, value)


                class Mag(Entity):
                    """
                    MAG within LMA
                    
                    .. attribute:: mag_name  <key>
                    
                    	MAG identifier
                    	**type**\:  str
                    
                    	**length:** 1..125
                    
                    .. attribute:: domain_name  <key>
                    
                    	Domain name
                    	**type**\:  str
                    
                    	**length:** 1..125
                    
                    .. attribute:: authenticate_option
                    
                    	Authentication option between PMIPV6 entities
                    	**type**\:   :py:class:`AuthenticateOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Mags.Mag.AuthenticateOption>`
                    
                    .. attribute:: dscp
                    
                    	DSCP for packets originating from this MAG
                    	**type**\:   :py:class:`Dscp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Mags.Mag.Dscp>`
                    
                    .. attribute:: encap_option
                    
                    	Encapsulation option between PMIPV6 entities
                    	**type**\:   :py:class:`EncapOpt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.EncapOpt>`
                    
                    .. attribute:: ipv4_address
                    
                    	Configure IPv4 address for this MAG
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6_address
                    
                    	Configure IPv6 address for this MAG
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: tunnel
                    
                    	static tunnel for this peer MAG
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MobileIp.Lmas.Lma.Mags.Mag, self).__init__()

                        self.yang_name = "mag"
                        self.yang_parent_name = "mags"

                        self.mag_name = YLeaf(YType.str, "mag-name")

                        self.domain_name = YLeaf(YType.str, "domain-name")

                        self.encap_option = YLeaf(YType.enumeration, "encap-option")

                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                        self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                        self.tunnel = YLeaf(YType.str, "tunnel")

                        self.authenticate_option = MobileIp.Lmas.Lma.Mags.Mag.AuthenticateOption()
                        self.authenticate_option.parent = self
                        self._children_name_map["authenticate_option"] = "authenticate-option"
                        self._children_yang_names.add("authenticate-option")

                        self.dscp = MobileIp.Lmas.Lma.Mags.Mag.Dscp()
                        self.dscp.parent = self
                        self._children_name_map["dscp"] = "dscp"
                        self._children_yang_names.add("dscp")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("mag_name",
                                        "domain_name",
                                        "encap_option",
                                        "ipv4_address",
                                        "ipv6_address",
                                        "tunnel") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MobileIp.Lmas.Lma.Mags.Mag, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MobileIp.Lmas.Lma.Mags.Mag, self).__setattr__(name, value)


                    class AuthenticateOption(Entity):
                        """
                        Authentication option between PMIPV6
                        entities
                        
                        .. attribute:: key
                        
                        	ASCII string
                        	**type**\:  str
                        
                        	**length:** 1..125
                        
                        .. attribute:: spi
                        
                        	SPI in hex value
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        

                        """

                        _prefix = 'ip-mobileip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MobileIp.Lmas.Lma.Mags.Mag.AuthenticateOption, self).__init__()

                            self.yang_name = "authenticate-option"
                            self.yang_parent_name = "mag"

                            self.key = YLeaf(YType.str, "key")

                            self.spi = YLeaf(YType.str, "spi")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("key",
                                            "spi") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MobileIp.Lmas.Lma.Mags.Mag.AuthenticateOption, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MobileIp.Lmas.Lma.Mags.Mag.AuthenticateOption, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.key.is_set or
                                self.spi.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.key.yfilter != YFilter.not_set or
                                self.spi.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "authenticate-option" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.key.is_set or self.key.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.key.get_name_leafdata())
                            if (self.spi.is_set or self.spi.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.spi.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "key" or name == "spi"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "key"):
                                self.key = value
                                self.key.value_namespace = name_space
                                self.key.value_namespace_prefix = name_space_prefix
                            if(value_path == "spi"):
                                self.spi = value
                                self.spi.value_namespace = name_space
                                self.spi.value_namespace_prefix = name_space_prefix


                    class Dscp(Entity):
                        """
                        DSCP for packets originating from this MAG
                        
                        .. attribute:: force
                        
                        	Set constant integer
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: value
                        
                        	Specify the DSCP value
                        	**type**\:  int
                        
                        	**range:** 1..63
                        
                        

                        """

                        _prefix = 'ip-mobileip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MobileIp.Lmas.Lma.Mags.Mag.Dscp, self).__init__()

                            self.yang_name = "dscp"
                            self.yang_parent_name = "mag"

                            self.force = YLeaf(YType.empty, "force")

                            self.value = YLeaf(YType.uint32, "value")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("force",
                                            "value") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MobileIp.Lmas.Lma.Mags.Mag.Dscp, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MobileIp.Lmas.Lma.Mags.Mag.Dscp, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.force.is_set or
                                self.value.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.force.yfilter != YFilter.not_set or
                                self.value.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "dscp" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.force.is_set or self.force.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.force.get_name_leafdata())
                            if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.value.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "force" or name == "value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "force"):
                                self.force = value
                                self.force.value_namespace = name_space
                                self.force.value_namespace_prefix = name_space_prefix
                            if(value_path == "value"):
                                self.value = value
                                self.value.value_namespace = name_space
                                self.value.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.mag_name.is_set or
                            self.domain_name.is_set or
                            self.encap_option.is_set or
                            self.ipv4_address.is_set or
                            self.ipv6_address.is_set or
                            self.tunnel.is_set or
                            (self.authenticate_option is not None and self.authenticate_option.has_data()) or
                            (self.dscp is not None and self.dscp.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.mag_name.yfilter != YFilter.not_set or
                            self.domain_name.yfilter != YFilter.not_set or
                            self.encap_option.yfilter != YFilter.not_set or
                            self.ipv4_address.yfilter != YFilter.not_set or
                            self.ipv6_address.yfilter != YFilter.not_set or
                            self.tunnel.yfilter != YFilter.not_set or
                            (self.authenticate_option is not None and self.authenticate_option.has_operation()) or
                            (self.dscp is not None and self.dscp.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "mag" + "[mag-name='" + self.mag_name.get() + "']" + "[domain-name='" + self.domain_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.mag_name.is_set or self.mag_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mag_name.get_name_leafdata())
                        if (self.domain_name.is_set or self.domain_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.domain_name.get_name_leafdata())
                        if (self.encap_option.is_set or self.encap_option.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.encap_option.get_name_leafdata())
                        if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                        if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6_address.get_name_leafdata())
                        if (self.tunnel.is_set or self.tunnel.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tunnel.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "authenticate-option"):
                            if (self.authenticate_option is None):
                                self.authenticate_option = MobileIp.Lmas.Lma.Mags.Mag.AuthenticateOption()
                                self.authenticate_option.parent = self
                                self._children_name_map["authenticate_option"] = "authenticate-option"
                            return self.authenticate_option

                        if (child_yang_name == "dscp"):
                            if (self.dscp is None):
                                self.dscp = MobileIp.Lmas.Lma.Mags.Mag.Dscp()
                                self.dscp.parent = self
                                self._children_name_map["dscp"] = "dscp"
                            return self.dscp

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "authenticate-option" or name == "dscp" or name == "mag-name" or name == "domain-name" or name == "encap-option" or name == "ipv4-address" or name == "ipv6-address" or name == "tunnel"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "mag-name"):
                            self.mag_name = value
                            self.mag_name.value_namespace = name_space
                            self.mag_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "domain-name"):
                            self.domain_name = value
                            self.domain_name.value_namespace = name_space
                            self.domain_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "encap-option"):
                            self.encap_option = value
                            self.encap_option.value_namespace = name_space
                            self.encap_option.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv4-address"):
                            self.ipv4_address = value
                            self.ipv4_address.value_namespace = name_space
                            self.ipv4_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6-address"):
                            self.ipv6_address = value
                            self.ipv6_address.value_namespace = name_space
                            self.ipv6_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "tunnel"):
                            self.tunnel = value
                            self.tunnel.value_namespace = name_space
                            self.tunnel.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.mag:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.mag:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "mags" + path_buffer

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

                    if (child_yang_name == "mag"):
                        for c in self.mag:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = MobileIp.Lmas.Lma.Mags.Mag()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.mag.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "mag"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class TunnelAttributes(Entity):
                """
                tunnel attributes
                
                .. attribute:: acl
                
                	access list to apply for tunnel
                	**type**\:  str
                
                	**length:** 1..125
                
                .. attribute:: mtu
                
                	maximum transmission unit for tunnel
                	**type**\:  int
                
                	**range:** 68..17916
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.TunnelAttributes, self).__init__()

                    self.yang_name = "tunnel-attributes"
                    self.yang_parent_name = "lma"

                    self.acl = YLeaf(YType.str, "acl")

                    self.mtu = YLeaf(YType.uint32, "mtu")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("acl",
                                    "mtu") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MobileIp.Lmas.Lma.TunnelAttributes, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MobileIp.Lmas.Lma.TunnelAttributes, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.acl.is_set or
                        self.mtu.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.acl.yfilter != YFilter.not_set or
                        self.mtu.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "tunnel-attributes" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.acl.is_set or self.acl.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.acl.get_name_leafdata())
                    if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mtu.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "acl" or name == "mtu"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "acl"):
                        self.acl = value
                        self.acl.value_namespace = name_space
                        self.acl.value_namespace_prefix = name_space_prefix
                    if(value_path == "mtu"):
                        self.mtu = value
                        self.mtu.value_namespace = name_space
                        self.mtu.value_namespace_prefix = name_space_prefix


            class Services(Entity):
                """
                Table of Service
                
                .. attribute:: service
                
                	Service of this LMA
                	**type**\: list of    :py:class:`Service <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.Services, self).__init__()

                    self.yang_name = "services"
                    self.yang_parent_name = "lma"

                    self.service = YList(self)

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
                                super(MobileIp.Lmas.Lma.Services, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MobileIp.Lmas.Lma.Services, self).__setattr__(name, value)


                class Service(Entity):
                    """
                    Service of this LMA
                    
                    .. attribute:: lma_service  <key>
                    
                    	LMA service mode
                    	**type**\:   :py:class:`LmaService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.LmaService>`
                    
                    .. attribute:: customers
                    
                    	Table of Customer
                    	**type**\:   :py:class:`Customers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers>`
                    
                    .. attribute:: ignore_home_address
                    
                    	Ignore HoA/HNP option
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: mnp_customer
                    
                    	mnp limit config for all customer's
                    	**type**\:  int
                    
                    	**range:** 1..4000000
                    
                    .. attribute:: mnp_ipv4_customer
                    
                    	mnp limit config for all customer's
                    	**type**\:  int
                    
                    	**range:** 1..4000000
                    
                    .. attribute:: mnp_ipv4_lmn
                    
                    	mnp limit config for all logical mn's
                    	**type**\:  int
                    
                    	**range:** 1..32
                    
                    .. attribute:: mnp_ipv6_customer
                    
                    	mnp limit config for all customer's
                    	**type**\:  int
                    
                    	**range:** 1..4000000
                    
                    .. attribute:: mnp_ipv6_lmn
                    
                    	mnp limit config for all logical mn's
                    	**type**\:  int
                    
                    	**range:** 1..32
                    
                    .. attribute:: mnp_lmn
                    
                    	mnp limit config for all logical mn's
                    	**type**\:  int
                    
                    	**range:** 1..32
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MobileIp.Lmas.Lma.Services.Service, self).__init__()

                        self.yang_name = "service"
                        self.yang_parent_name = "services"

                        self.lma_service = YLeaf(YType.enumeration, "lma-service")

                        self.ignore_home_address = YLeaf(YType.empty, "ignore-home-address")

                        self.mnp_customer = YLeaf(YType.uint32, "mnp-customer")

                        self.mnp_ipv4_customer = YLeaf(YType.uint32, "mnp-ipv4-customer")

                        self.mnp_ipv4_lmn = YLeaf(YType.uint32, "mnp-ipv4-lmn")

                        self.mnp_ipv6_customer = YLeaf(YType.uint32, "mnp-ipv6-customer")

                        self.mnp_ipv6_lmn = YLeaf(YType.uint32, "mnp-ipv6-lmn")

                        self.mnp_lmn = YLeaf(YType.uint32, "mnp-lmn")

                        self.customers = MobileIp.Lmas.Lma.Services.Service.Customers()
                        self.customers.parent = self
                        self._children_name_map["customers"] = "customers"
                        self._children_yang_names.add("customers")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("lma_service",
                                        "ignore_home_address",
                                        "mnp_customer",
                                        "mnp_ipv4_customer",
                                        "mnp_ipv4_lmn",
                                        "mnp_ipv6_customer",
                                        "mnp_ipv6_lmn",
                                        "mnp_lmn") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MobileIp.Lmas.Lma.Services.Service, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MobileIp.Lmas.Lma.Services.Service, self).__setattr__(name, value)


                    class Customers(Entity):
                        """
                        Table of Customer
                        
                        .. attribute:: customer
                        
                        	customer configuration on this mobile local loop service
                        	**type**\: list of    :py:class:`Customer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer>`
                        
                        

                        """

                        _prefix = 'ip-mobileip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MobileIp.Lmas.Lma.Services.Service.Customers, self).__init__()

                            self.yang_name = "customers"
                            self.yang_parent_name = "service"

                            self.customer = YList(self)

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
                                        super(MobileIp.Lmas.Lma.Services.Service.Customers, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MobileIp.Lmas.Lma.Services.Service.Customers, self).__setattr__(name, value)


                        class Customer(Entity):
                            """
                            customer configuration on this mobile local
                            loop service
                            
                            .. attribute:: customer_name  <key>
                            
                            	Customer name
                            	**type**\:  str
                            
                            	**length:** 1..32
                            
                            .. attribute:: vrf_name  <key>
                            
                            	VRF name
                            	**type**\:  str
                            
                            	**length:** 1..32
                            
                            .. attribute:: authenticate_option
                            
                            	Authentication option between PMIPV6 entities
                            	**type**\:   :py:class:`AuthenticateOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.AuthenticateOption>`
                            
                            .. attribute:: bandwidth_aggregate
                            
                            	Aggregate bandwidth across all logical MNs
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: binding_attributes
                            
                            	Customer specific binding attributes
                            	**type**\:   :py:class:`BindingAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.BindingAttributes>`
                            
                            .. attribute:: gre_key
                            
                            	Customer specific GRE key
                            	**type**\:   :py:class:`GreKey <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.GreKey>`
                            
                            .. attribute:: heart_beat_attributes
                            
                            	heartbeat config for this Customer
                            	**type**\:   :py:class:`HeartBeatAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.HeartBeatAttributes>`
                            
                            .. attribute:: mnp_customer
                            
                            	mnp limit config for customer
                            	**type**\:  int
                            
                            	**range:** 1..4000000
                            
                            .. attribute:: mnp_ipv4_customer
                            
                            	mnp limit config for customer
                            	**type**\:  int
                            
                            	**range:** 1..4000000
                            
                            .. attribute:: mnp_ipv4_lmn
                            
                            	mnp limit config for customer specific logical mn
                            	**type**\:  int
                            
                            	**range:** 1..32
                            
                            .. attribute:: mnp_ipv6_customer
                            
                            	mnp limit config for customer
                            	**type**\:  int
                            
                            	**range:** 1..4000000
                            
                            .. attribute:: mnp_ipv6_lmn
                            
                            	mnp limit config for customer specific logical mn
                            	**type**\:  int
                            
                            	**range:** 1..32
                            
                            .. attribute:: mnp_lmn
                            
                            	mnp limit config for customer specific logical mn
                            	**type**\:  int
                            
                            	**range:** 1..32
                            
                            .. attribute:: mobile_route_ad
                            
                            	Specify the Admin Distance value
                            	**type**\:  int
                            
                            	**range:** 1..254
                            
                            .. attribute:: network_attributes
                            
                            	network parameters for the customer
                            	**type**\:   :py:class:`NetworkAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes>`
                            
                            .. attribute:: transports
                            
                            	Table of Transport
                            	**type**\:   :py:class:`Transports <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports>`
                            
                            

                            """

                            _prefix = 'ip-mobileip-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer, self).__init__()

                                self.yang_name = "customer"
                                self.yang_parent_name = "customers"

                                self.customer_name = YLeaf(YType.str, "customer-name")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")

                                self.bandwidth_aggregate = YLeaf(YType.int32, "bandwidth-aggregate")

                                self.mnp_customer = YLeaf(YType.uint32, "mnp-customer")

                                self.mnp_ipv4_customer = YLeaf(YType.uint32, "mnp-ipv4-customer")

                                self.mnp_ipv4_lmn = YLeaf(YType.uint32, "mnp-ipv4-lmn")

                                self.mnp_ipv6_customer = YLeaf(YType.uint32, "mnp-ipv6-customer")

                                self.mnp_ipv6_lmn = YLeaf(YType.uint32, "mnp-ipv6-lmn")

                                self.mnp_lmn = YLeaf(YType.uint32, "mnp-lmn")

                                self.mobile_route_ad = YLeaf(YType.uint32, "mobile-route-ad")

                                self.authenticate_option = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.AuthenticateOption()
                                self.authenticate_option.parent = self
                                self._children_name_map["authenticate_option"] = "authenticate-option"
                                self._children_yang_names.add("authenticate-option")

                                self.binding_attributes = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.BindingAttributes()
                                self.binding_attributes.parent = self
                                self._children_name_map["binding_attributes"] = "binding-attributes"
                                self._children_yang_names.add("binding-attributes")

                                self.gre_key = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.GreKey()
                                self.gre_key.parent = self
                                self._children_name_map["gre_key"] = "gre-key"
                                self._children_yang_names.add("gre-key")

                                self.heart_beat_attributes = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.HeartBeatAttributes()
                                self.heart_beat_attributes.parent = self
                                self._children_name_map["heart_beat_attributes"] = "heart-beat-attributes"
                                self._children_yang_names.add("heart-beat-attributes")

                                self.network_attributes = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes()
                                self.network_attributes.parent = self
                                self._children_name_map["network_attributes"] = "network-attributes"
                                self._children_yang_names.add("network-attributes")

                                self.transports = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports()
                                self.transports.parent = self
                                self._children_name_map["transports"] = "transports"
                                self._children_yang_names.add("transports")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("customer_name",
                                                "vrf_name",
                                                "bandwidth_aggregate",
                                                "mnp_customer",
                                                "mnp_ipv4_customer",
                                                "mnp_ipv4_lmn",
                                                "mnp_ipv6_customer",
                                                "mnp_ipv6_lmn",
                                                "mnp_lmn",
                                                "mobile_route_ad") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer, self).__setattr__(name, value)


                            class AuthenticateOption(Entity):
                                """
                                Authentication option between PMIPV6
                                entities
                                
                                .. attribute:: key
                                
                                	ASCII string
                                	**type**\:  str
                                
                                	**length:** 1..125
                                
                                .. attribute:: spi
                                
                                	SPI in hex value
                                	**type**\:  str
                                
                                	**pattern:** [0\-9a\-fA\-F]{1,8}
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.AuthenticateOption, self).__init__()

                                    self.yang_name = "authenticate-option"
                                    self.yang_parent_name = "customer"

                                    self.key = YLeaf(YType.str, "key")

                                    self.spi = YLeaf(YType.str, "spi")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("key",
                                                    "spi") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.AuthenticateOption, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.AuthenticateOption, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.key.is_set or
                                        self.spi.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.key.yfilter != YFilter.not_set or
                                        self.spi.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "authenticate-option" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.key.is_set or self.key.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.key.get_name_leafdata())
                                    if (self.spi.is_set or self.spi.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.spi.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "key" or name == "spi"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "key"):
                                        self.key = value
                                        self.key.value_namespace = name_space
                                        self.key.value_namespace_prefix = name_space_prefix
                                    if(value_path == "spi"):
                                        self.spi = value
                                        self.spi.value_namespace = name_space
                                        self.spi.value_namespace_prefix = name_space_prefix


                            class HeartBeatAttributes(Entity):
                                """
                                heartbeat config for this Customer
                                
                                .. attribute:: interval
                                
                                	Specify the interval value in second
                                	**type**\:  int
                                
                                	**range:** 10..3600
                                
                                .. attribute:: retries
                                
                                	Specify the retry value
                                	**type**\:  int
                                
                                	**range:** 1..10
                                
                                .. attribute:: timeout
                                
                                	Specify the timeout value
                                	**type**\:  int
                                
                                	**range:** 1..3600
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.HeartBeatAttributes, self).__init__()

                                    self.yang_name = "heart-beat-attributes"
                                    self.yang_parent_name = "customer"

                                    self.interval = YLeaf(YType.uint32, "interval")

                                    self.retries = YLeaf(YType.uint32, "retries")

                                    self.timeout = YLeaf(YType.uint32, "timeout")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("interval",
                                                    "retries",
                                                    "timeout") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.HeartBeatAttributes, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.HeartBeatAttributes, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.interval.is_set or
                                        self.retries.is_set or
                                        self.timeout.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.interval.yfilter != YFilter.not_set or
                                        self.retries.yfilter != YFilter.not_set or
                                        self.timeout.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "heart-beat-attributes" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.interval.is_set or self.interval.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.interval.get_name_leafdata())
                                    if (self.retries.is_set or self.retries.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.retries.get_name_leafdata())
                                    if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.timeout.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "interval" or name == "retries" or name == "timeout"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "interval"):
                                        self.interval = value
                                        self.interval.value_namespace = name_space
                                        self.interval.value_namespace_prefix = name_space_prefix
                                    if(value_path == "retries"):
                                        self.retries = value
                                        self.retries.value_namespace = name_space
                                        self.retries.value_namespace_prefix = name_space_prefix
                                    if(value_path == "timeout"):
                                        self.timeout = value
                                        self.timeout.value_namespace = name_space
                                        self.timeout.value_namespace_prefix = name_space_prefix


                            class Transports(Entity):
                                """
                                Table of Transport
                                
                                .. attribute:: transport
                                
                                	Customer transport attributes
                                	**type**\: list of    :py:class:`Transport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports.Transport>`
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports, self).__init__()

                                    self.yang_name = "transports"
                                    self.yang_parent_name = "customer"

                                    self.transport = YList(self)

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
                                                super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports, self).__setattr__(name, value)


                                class Transport(Entity):
                                    """
                                    Customer transport attributes
                                    
                                    .. attribute:: vrf_name  <key>
                                    
                                    	VRF Name
                                    	**type**\:  str
                                    
                                    	**length:** 1..125
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	Configure IPv4 address for this LMA
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	Configure IPv6 address for this LMA
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ip-mobileip-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports.Transport, self).__init__()

                                        self.yang_name = "transport"
                                        self.yang_parent_name = "transports"

                                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                        self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("vrf_name",
                                                        "ipv4_address",
                                                        "ipv6_address") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports.Transport, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports.Transport, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.vrf_name.is_set or
                                            self.ipv4_address.is_set or
                                            self.ipv6_address.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.vrf_name.yfilter != YFilter.not_set or
                                            self.ipv4_address.yfilter != YFilter.not_set or
                                            self.ipv6_address.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "transport" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.vrf_name.get_name_leafdata())
                                        if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                                        if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "vrf-name" or name == "ipv4-address" or name == "ipv6-address"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "vrf-name"):
                                            self.vrf_name = value
                                            self.vrf_name.value_namespace = name_space
                                            self.vrf_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ipv4-address"):
                                            self.ipv4_address = value
                                            self.ipv4_address.value_namespace = name_space
                                            self.ipv4_address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ipv6-address"):
                                            self.ipv6_address = value
                                            self.ipv6_address.value_namespace = name_space
                                            self.ipv6_address.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.transport:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.transport:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "transports" + path_buffer

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

                                    if (child_yang_name == "transport"):
                                        for c in self.transport:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports.Transport()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.transport.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "transport"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class NetworkAttributes(Entity):
                                """
                                network parameters for the customer
                                
                                .. attribute:: authorizes
                                
                                	Table of Authorize
                                	**type**\:   :py:class:`Authorizes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes>`
                                
                                .. attribute:: unauthorize
                                
                                	not authorize the network prefixes
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes, self).__init__()

                                    self.yang_name = "network-attributes"
                                    self.yang_parent_name = "customer"

                                    self.unauthorize = YLeaf(YType.empty, "unauthorize")

                                    self.authorizes = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes()
                                    self.authorizes.parent = self
                                    self._children_name_map["authorizes"] = "authorizes"
                                    self._children_yang_names.add("authorizes")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("unauthorize") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes, self).__setattr__(name, value)


                                class Authorizes(Entity):
                                    """
                                    Table of Authorize
                                    
                                    .. attribute:: authorize
                                    
                                    	not authorize the network prefixes
                                    	**type**\: list of    :py:class:`Authorize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize>`
                                    
                                    

                                    """

                                    _prefix = 'ip-mobileip-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes, self).__init__()

                                        self.yang_name = "authorizes"
                                        self.yang_parent_name = "network-attributes"

                                        self.authorize = YList(self)

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
                                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes, self).__setattr__(name, value)


                                    class Authorize(Entity):
                                        """
                                        not authorize the network prefixes
                                        
                                        .. attribute:: name  <key>
                                        
                                        	ASCII string
                                        	**type**\:  str
                                        
                                        	**length:** 1..125
                                        
                                        .. attribute:: pool_attributes
                                        
                                        	Pool configs for this network
                                        	**type**\:   :py:class:`PoolAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes>`
                                        
                                        

                                        """

                                        _prefix = 'ip-mobileip-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize, self).__init__()

                                            self.yang_name = "authorize"
                                            self.yang_parent_name = "authorizes"

                                            self.name = YLeaf(YType.str, "name")

                                            self.pool_attributes = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes()
                                            self.pool_attributes.parent = self
                                            self._children_name_map["pool_attributes"] = "pool-attributes"
                                            self._children_yang_names.add("pool-attributes")

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
                                                        super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize, self).__setattr__(name, value)


                                        class PoolAttributes(Entity):
                                            """
                                            Pool configs for this network
                                            
                                            .. attribute:: mobile_network
                                            
                                            	pool configs for the mobile network
                                            	**type**\:   :py:class:`MobileNetwork <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork>`
                                            
                                            .. attribute:: mobile_node
                                            
                                            	pool configs for the mobile nodes
                                            	**type**\:   :py:class:`MobileNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode>`
                                            
                                            

                                            """

                                            _prefix = 'ip-mobileip-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes, self).__init__()

                                                self.yang_name = "pool-attributes"
                                                self.yang_parent_name = "authorize"

                                                self.mobile_network = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork()
                                                self.mobile_network.parent = self
                                                self._children_name_map["mobile_network"] = "mobile-network"
                                                self._children_yang_names.add("mobile-network")

                                                self.mobile_node = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode()
                                                self.mobile_node.parent = self
                                                self._children_name_map["mobile_node"] = "mobile-node"
                                                self._children_yang_names.add("mobile-node")


                                            class MobileNode(Entity):
                                                """
                                                pool configs for the mobile nodes
                                                
                                                .. attribute:: ipv4_pool
                                                
                                                	None
                                                	**type**\:   :py:class:`Ipv4Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv4Pool>`
                                                
                                                .. attribute:: ipv6_pool
                                                
                                                	None
                                                	**type**\:   :py:class:`Ipv6Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv6Pool>`
                                                
                                                

                                                """

                                                _prefix = 'ip-mobileip-cfg'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode, self).__init__()

                                                    self.yang_name = "mobile-node"
                                                    self.yang_parent_name = "pool-attributes"

                                                    self.ipv4_pool = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv4Pool()
                                                    self.ipv4_pool.parent = self
                                                    self._children_name_map["ipv4_pool"] = "ipv4-pool"
                                                    self._children_yang_names.add("ipv4-pool")

                                                    self.ipv6_pool = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv6Pool()
                                                    self.ipv6_pool.parent = self
                                                    self._children_name_map["ipv6_pool"] = "ipv6-pool"
                                                    self._children_yang_names.add("ipv6-pool")


                                                class Ipv4Pool(Entity):
                                                    """
                                                    None
                                                    
                                                    .. attribute:: pool_prefix
                                                    
                                                    	IPv4 Pool Prefix value
                                                    	**type**\:  int
                                                    
                                                    	**range:** 8..30
                                                    
                                                    .. attribute:: start_address
                                                    
                                                    	Pool IPv4 start address
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    

                                                    """

                                                    _prefix = 'ip-mobileip-cfg'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv4Pool, self).__init__()

                                                        self.yang_name = "ipv4-pool"
                                                        self.yang_parent_name = "mobile-node"

                                                        self.pool_prefix = YLeaf(YType.uint32, "pool-prefix")

                                                        self.start_address = YLeaf(YType.str, "start-address")

                                                    def __setattr__(self, name, value):
                                                        self._check_monkey_patching_error(name, value)
                                                        with _handle_type_error():
                                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                    "Please use list append or extend method."
                                                                                    .format(value))
                                                            if isinstance(value, Enum.YLeaf):
                                                                value = value.name
                                                            if name in ("pool_prefix",
                                                                        "start_address") and name in self.__dict__:
                                                                if isinstance(value, YLeaf):
                                                                    self.__dict__[name].set(value.get())
                                                                elif isinstance(value, YLeafList):
                                                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv4Pool, self).__setattr__(name, value)
                                                                else:
                                                                    self.__dict__[name].set(value)
                                                            else:
                                                                if hasattr(value, "parent") and name != "parent":
                                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                        value.parent = self
                                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                        value.parent = self
                                                                super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv4Pool, self).__setattr__(name, value)

                                                    def has_data(self):
                                                        return (
                                                            self.pool_prefix.is_set or
                                                            self.start_address.is_set)

                                                    def has_operation(self):
                                                        return (
                                                            self.yfilter != YFilter.not_set or
                                                            self.pool_prefix.yfilter != YFilter.not_set or
                                                            self.start_address.yfilter != YFilter.not_set)

                                                    def get_segment_path(self):
                                                        path_buffer = ""
                                                        path_buffer = "ipv4-pool" + path_buffer

                                                        return path_buffer

                                                    def get_entity_path(self, ancestor):
                                                        path_buffer = ""
                                                        if (ancestor is None):
                                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                        else:
                                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                        leaf_name_data = LeafDataList()
                                                        if (self.pool_prefix.is_set or self.pool_prefix.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.pool_prefix.get_name_leafdata())
                                                        if (self.start_address.is_set or self.start_address.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.start_address.get_name_leafdata())

                                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                                        return entity_path

                                                    def get_child_by_name(self, child_yang_name, segment_path):
                                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                        if child is not None:
                                                            return child

                                                        return None

                                                    def has_leaf_or_child_of_name(self, name):
                                                        if(name == "pool-prefix" or name == "start-address"):
                                                            return True
                                                        return False

                                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                                        if(value_path == "pool-prefix"):
                                                            self.pool_prefix = value
                                                            self.pool_prefix.value_namespace = name_space
                                                            self.pool_prefix.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "start-address"):
                                                            self.start_address = value
                                                            self.start_address.value_namespace = name_space
                                                            self.start_address.value_namespace_prefix = name_space_prefix


                                                class Ipv6Pool(Entity):
                                                    """
                                                    None
                                                    
                                                    .. attribute:: pool_prefix
                                                    
                                                    	IPv6 Pool Prefix value
                                                    	**type**\:  int
                                                    
                                                    	**range:** 8..62
                                                    
                                                    .. attribute:: start_address
                                                    
                                                    	Pool IPv6 start address
                                                    	**type**\:  str
                                                    
                                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                    
                                                    

                                                    """

                                                    _prefix = 'ip-mobileip-cfg'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv6Pool, self).__init__()

                                                        self.yang_name = "ipv6-pool"
                                                        self.yang_parent_name = "mobile-node"

                                                        self.pool_prefix = YLeaf(YType.uint32, "pool-prefix")

                                                        self.start_address = YLeaf(YType.str, "start-address")

                                                    def __setattr__(self, name, value):
                                                        self._check_monkey_patching_error(name, value)
                                                        with _handle_type_error():
                                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                    "Please use list append or extend method."
                                                                                    .format(value))
                                                            if isinstance(value, Enum.YLeaf):
                                                                value = value.name
                                                            if name in ("pool_prefix",
                                                                        "start_address") and name in self.__dict__:
                                                                if isinstance(value, YLeaf):
                                                                    self.__dict__[name].set(value.get())
                                                                elif isinstance(value, YLeafList):
                                                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv6Pool, self).__setattr__(name, value)
                                                                else:
                                                                    self.__dict__[name].set(value)
                                                            else:
                                                                if hasattr(value, "parent") and name != "parent":
                                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                        value.parent = self
                                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                        value.parent = self
                                                                super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv6Pool, self).__setattr__(name, value)

                                                    def has_data(self):
                                                        return (
                                                            self.pool_prefix.is_set or
                                                            self.start_address.is_set)

                                                    def has_operation(self):
                                                        return (
                                                            self.yfilter != YFilter.not_set or
                                                            self.pool_prefix.yfilter != YFilter.not_set or
                                                            self.start_address.yfilter != YFilter.not_set)

                                                    def get_segment_path(self):
                                                        path_buffer = ""
                                                        path_buffer = "ipv6-pool" + path_buffer

                                                        return path_buffer

                                                    def get_entity_path(self, ancestor):
                                                        path_buffer = ""
                                                        if (ancestor is None):
                                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                        else:
                                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                        leaf_name_data = LeafDataList()
                                                        if (self.pool_prefix.is_set or self.pool_prefix.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.pool_prefix.get_name_leafdata())
                                                        if (self.start_address.is_set or self.start_address.yfilter != YFilter.not_set):
                                                            leaf_name_data.append(self.start_address.get_name_leafdata())

                                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                                        return entity_path

                                                    def get_child_by_name(self, child_yang_name, segment_path):
                                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                        if child is not None:
                                                            return child

                                                        return None

                                                    def has_leaf_or_child_of_name(self, name):
                                                        if(name == "pool-prefix" or name == "start-address"):
                                                            return True
                                                        return False

                                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                                        if(value_path == "pool-prefix"):
                                                            self.pool_prefix = value
                                                            self.pool_prefix.value_namespace = name_space
                                                            self.pool_prefix.value_namespace_prefix = name_space_prefix
                                                        if(value_path == "start-address"):
                                                            self.start_address = value
                                                            self.start_address.value_namespace = name_space
                                                            self.start_address.value_namespace_prefix = name_space_prefix

                                                def has_data(self):
                                                    return (
                                                        (self.ipv4_pool is not None and self.ipv4_pool.has_data()) or
                                                        (self.ipv6_pool is not None and self.ipv6_pool.has_data()))

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        (self.ipv4_pool is not None and self.ipv4_pool.has_operation()) or
                                                        (self.ipv6_pool is not None and self.ipv6_pool.has_operation()))

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "mobile-node" + path_buffer

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

                                                    if (child_yang_name == "ipv4-pool"):
                                                        if (self.ipv4_pool is None):
                                                            self.ipv4_pool = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv4Pool()
                                                            self.ipv4_pool.parent = self
                                                            self._children_name_map["ipv4_pool"] = "ipv4-pool"
                                                        return self.ipv4_pool

                                                    if (child_yang_name == "ipv6-pool"):
                                                        if (self.ipv6_pool is None):
                                                            self.ipv6_pool = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode.Ipv6Pool()
                                                            self.ipv6_pool.parent = self
                                                            self._children_name_map["ipv6_pool"] = "ipv6-pool"
                                                        return self.ipv6_pool

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "ipv4-pool" or name == "ipv6-pool"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    pass


                                            class MobileNetwork(Entity):
                                                """
                                                pool configs for the mobile network
                                                
                                                .. attribute:: mripv4_pools
                                                
                                                	Table of MRIPV4Pool
                                                	**type**\:   :py:class:`Mripv4Pools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools>`
                                                
                                                .. attribute:: mripv6_pools
                                                
                                                	Table of MRIPV6Pool
                                                	**type**\:   :py:class:`Mripv6Pools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools>`
                                                
                                                

                                                """

                                                _prefix = 'ip-mobileip-cfg'
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork, self).__init__()

                                                    self.yang_name = "mobile-network"
                                                    self.yang_parent_name = "pool-attributes"

                                                    self.mripv4_pools = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools()
                                                    self.mripv4_pools.parent = self
                                                    self._children_name_map["mripv4_pools"] = "mripv4-pools"
                                                    self._children_yang_names.add("mripv4-pools")

                                                    self.mripv6_pools = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools()
                                                    self.mripv6_pools.parent = self
                                                    self._children_name_map["mripv6_pools"] = "mripv6-pools"
                                                    self._children_yang_names.add("mripv6-pools")


                                                class Mripv6Pools(Entity):
                                                    """
                                                    Table of MRIPV6Pool
                                                    
                                                    .. attribute:: mripv6_pool
                                                    
                                                    	ipv6 pool
                                                    	**type**\: list of    :py:class:`Mripv6Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'ip-mobileip-cfg'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools, self).__init__()

                                                        self.yang_name = "mripv6-pools"
                                                        self.yang_parent_name = "mobile-network"

                                                        self.mripv6_pool = YList(self)

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
                                                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools, self).__setattr__(name, value)
                                                                else:
                                                                    self.__dict__[name].set(value)
                                                            else:
                                                                if hasattr(value, "parent") and name != "parent":
                                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                        value.parent = self
                                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                        value.parent = self
                                                                super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools, self).__setattr__(name, value)


                                                    class Mripv6Pool(Entity):
                                                        """
                                                        ipv6 pool
                                                        
                                                        .. attribute:: start_address  <key>
                                                        
                                                        	Pool IPv6 start address
                                                        	**type**\:  str
                                                        
                                                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                        
                                                        .. attribute:: network_prefix
                                                        
                                                        	IPv4 Network Prefix value
                                                        	**type**\:  int
                                                        
                                                        	**range:** 8..64
                                                        
                                                        .. attribute:: pool_prefix
                                                        
                                                        	IPv6 Pool Prefix value
                                                        	**type**\:  int
                                                        
                                                        	**range:** 8..64
                                                        
                                                        

                                                        """

                                                        _prefix = 'ip-mobileip-cfg'
                                                        _revision = '2015-11-09'

                                                        def __init__(self):
                                                            super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool, self).__init__()

                                                            self.yang_name = "mripv6-pool"
                                                            self.yang_parent_name = "mripv6-pools"

                                                            self.start_address = YLeaf(YType.str, "start-address")

                                                            self.network_prefix = YLeaf(YType.uint32, "network-prefix")

                                                            self.pool_prefix = YLeaf(YType.uint32, "pool-prefix")

                                                        def __setattr__(self, name, value):
                                                            self._check_monkey_patching_error(name, value)
                                                            with _handle_type_error():
                                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                        "Please use list append or extend method."
                                                                                        .format(value))
                                                                if isinstance(value, Enum.YLeaf):
                                                                    value = value.name
                                                                if name in ("start_address",
                                                                            "network_prefix",
                                                                            "pool_prefix") and name in self.__dict__:
                                                                    if isinstance(value, YLeaf):
                                                                        self.__dict__[name].set(value.get())
                                                                    elif isinstance(value, YLeafList):
                                                                        super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool, self).__setattr__(name, value)
                                                                    else:
                                                                        self.__dict__[name].set(value)
                                                                else:
                                                                    if hasattr(value, "parent") and name != "parent":
                                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                            value.parent = self
                                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                            value.parent = self
                                                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool, self).__setattr__(name, value)

                                                        def has_data(self):
                                                            return (
                                                                self.start_address.is_set or
                                                                self.network_prefix.is_set or
                                                                self.pool_prefix.is_set)

                                                        def has_operation(self):
                                                            return (
                                                                self.yfilter != YFilter.not_set or
                                                                self.start_address.yfilter != YFilter.not_set or
                                                                self.network_prefix.yfilter != YFilter.not_set or
                                                                self.pool_prefix.yfilter != YFilter.not_set)

                                                        def get_segment_path(self):
                                                            path_buffer = ""
                                                            path_buffer = "mripv6-pool" + "[start-address='" + self.start_address.get() + "']" + path_buffer

                                                            return path_buffer

                                                        def get_entity_path(self, ancestor):
                                                            path_buffer = ""
                                                            if (ancestor is None):
                                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                            else:
                                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                            leaf_name_data = LeafDataList()
                                                            if (self.start_address.is_set or self.start_address.yfilter != YFilter.not_set):
                                                                leaf_name_data.append(self.start_address.get_name_leafdata())
                                                            if (self.network_prefix.is_set or self.network_prefix.yfilter != YFilter.not_set):
                                                                leaf_name_data.append(self.network_prefix.get_name_leafdata())
                                                            if (self.pool_prefix.is_set or self.pool_prefix.yfilter != YFilter.not_set):
                                                                leaf_name_data.append(self.pool_prefix.get_name_leafdata())

                                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                                            return entity_path

                                                        def get_child_by_name(self, child_yang_name, segment_path):
                                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                            if child is not None:
                                                                return child

                                                            return None

                                                        def has_leaf_or_child_of_name(self, name):
                                                            if(name == "start-address" or name == "network-prefix" or name == "pool-prefix"):
                                                                return True
                                                            return False

                                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                                            if(value_path == "start-address"):
                                                                self.start_address = value
                                                                self.start_address.value_namespace = name_space
                                                                self.start_address.value_namespace_prefix = name_space_prefix
                                                            if(value_path == "network-prefix"):
                                                                self.network_prefix = value
                                                                self.network_prefix.value_namespace = name_space
                                                                self.network_prefix.value_namespace_prefix = name_space_prefix
                                                            if(value_path == "pool-prefix"):
                                                                self.pool_prefix = value
                                                                self.pool_prefix.value_namespace = name_space
                                                                self.pool_prefix.value_namespace_prefix = name_space_prefix

                                                    def has_data(self):
                                                        for c in self.mripv6_pool:
                                                            if (c.has_data()):
                                                                return True
                                                        return False

                                                    def has_operation(self):
                                                        for c in self.mripv6_pool:
                                                            if (c.has_operation()):
                                                                return True
                                                        return self.yfilter != YFilter.not_set

                                                    def get_segment_path(self):
                                                        path_buffer = ""
                                                        path_buffer = "mripv6-pools" + path_buffer

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

                                                        if (child_yang_name == "mripv6-pool"):
                                                            for c in self.mripv6_pool:
                                                                segment = c.get_segment_path()
                                                                if (segment_path == segment):
                                                                    return c
                                                            c = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool()
                                                            c.parent = self
                                                            local_reference_key = "ydk::seg::%s" % segment_path
                                                            self._local_refs[local_reference_key] = c
                                                            self.mripv6_pool.append(c)
                                                            return c

                                                        return None

                                                    def has_leaf_or_child_of_name(self, name):
                                                        if(name == "mripv6-pool"):
                                                            return True
                                                        return False

                                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                                        pass


                                                class Mripv4Pools(Entity):
                                                    """
                                                    Table of MRIPV4Pool
                                                    
                                                    .. attribute:: mripv4_pool
                                                    
                                                    	ipv4 pool
                                                    	**type**\: list of    :py:class:`Mripv4Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'ip-mobileip-cfg'
                                                    _revision = '2015-11-09'

                                                    def __init__(self):
                                                        super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools, self).__init__()

                                                        self.yang_name = "mripv4-pools"
                                                        self.yang_parent_name = "mobile-network"

                                                        self.mripv4_pool = YList(self)

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
                                                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools, self).__setattr__(name, value)
                                                                else:
                                                                    self.__dict__[name].set(value)
                                                            else:
                                                                if hasattr(value, "parent") and name != "parent":
                                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                        value.parent = self
                                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                        value.parent = self
                                                                super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools, self).__setattr__(name, value)


                                                    class Mripv4Pool(Entity):
                                                        """
                                                        ipv4 pool
                                                        
                                                        .. attribute:: start_address  <key>
                                                        
                                                        	Pool IPv4 start address
                                                        	**type**\:  str
                                                        
                                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                        
                                                        .. attribute:: network_prefix
                                                        
                                                        	IPv4 Network Prefix value
                                                        	**type**\:  int
                                                        
                                                        	**range:** 8..32
                                                        
                                                        .. attribute:: pool_prefix
                                                        
                                                        	IPv4 Pool Prefix value
                                                        	**type**\:  int
                                                        
                                                        	**range:** 8..30
                                                        
                                                        

                                                        """

                                                        _prefix = 'ip-mobileip-cfg'
                                                        _revision = '2015-11-09'

                                                        def __init__(self):
                                                            super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool, self).__init__()

                                                            self.yang_name = "mripv4-pool"
                                                            self.yang_parent_name = "mripv4-pools"

                                                            self.start_address = YLeaf(YType.str, "start-address")

                                                            self.network_prefix = YLeaf(YType.uint32, "network-prefix")

                                                            self.pool_prefix = YLeaf(YType.uint32, "pool-prefix")

                                                        def __setattr__(self, name, value):
                                                            self._check_monkey_patching_error(name, value)
                                                            with _handle_type_error():
                                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                        "Please use list append or extend method."
                                                                                        .format(value))
                                                                if isinstance(value, Enum.YLeaf):
                                                                    value = value.name
                                                                if name in ("start_address",
                                                                            "network_prefix",
                                                                            "pool_prefix") and name in self.__dict__:
                                                                    if isinstance(value, YLeaf):
                                                                        self.__dict__[name].set(value.get())
                                                                    elif isinstance(value, YLeafList):
                                                                        super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool, self).__setattr__(name, value)
                                                                    else:
                                                                        self.__dict__[name].set(value)
                                                                else:
                                                                    if hasattr(value, "parent") and name != "parent":
                                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                            value.parent = self
                                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                            value.parent = self
                                                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool, self).__setattr__(name, value)

                                                        def has_data(self):
                                                            return (
                                                                self.start_address.is_set or
                                                                self.network_prefix.is_set or
                                                                self.pool_prefix.is_set)

                                                        def has_operation(self):
                                                            return (
                                                                self.yfilter != YFilter.not_set or
                                                                self.start_address.yfilter != YFilter.not_set or
                                                                self.network_prefix.yfilter != YFilter.not_set or
                                                                self.pool_prefix.yfilter != YFilter.not_set)

                                                        def get_segment_path(self):
                                                            path_buffer = ""
                                                            path_buffer = "mripv4-pool" + "[start-address='" + self.start_address.get() + "']" + path_buffer

                                                            return path_buffer

                                                        def get_entity_path(self, ancestor):
                                                            path_buffer = ""
                                                            if (ancestor is None):
                                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                            else:
                                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                            leaf_name_data = LeafDataList()
                                                            if (self.start_address.is_set or self.start_address.yfilter != YFilter.not_set):
                                                                leaf_name_data.append(self.start_address.get_name_leafdata())
                                                            if (self.network_prefix.is_set or self.network_prefix.yfilter != YFilter.not_set):
                                                                leaf_name_data.append(self.network_prefix.get_name_leafdata())
                                                            if (self.pool_prefix.is_set or self.pool_prefix.yfilter != YFilter.not_set):
                                                                leaf_name_data.append(self.pool_prefix.get_name_leafdata())

                                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                                            return entity_path

                                                        def get_child_by_name(self, child_yang_name, segment_path):
                                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                            if child is not None:
                                                                return child

                                                            return None

                                                        def has_leaf_or_child_of_name(self, name):
                                                            if(name == "start-address" or name == "network-prefix" or name == "pool-prefix"):
                                                                return True
                                                            return False

                                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                                            if(value_path == "start-address"):
                                                                self.start_address = value
                                                                self.start_address.value_namespace = name_space
                                                                self.start_address.value_namespace_prefix = name_space_prefix
                                                            if(value_path == "network-prefix"):
                                                                self.network_prefix = value
                                                                self.network_prefix.value_namespace = name_space
                                                                self.network_prefix.value_namespace_prefix = name_space_prefix
                                                            if(value_path == "pool-prefix"):
                                                                self.pool_prefix = value
                                                                self.pool_prefix.value_namespace = name_space
                                                                self.pool_prefix.value_namespace_prefix = name_space_prefix

                                                    def has_data(self):
                                                        for c in self.mripv4_pool:
                                                            if (c.has_data()):
                                                                return True
                                                        return False

                                                    def has_operation(self):
                                                        for c in self.mripv4_pool:
                                                            if (c.has_operation()):
                                                                return True
                                                        return self.yfilter != YFilter.not_set

                                                    def get_segment_path(self):
                                                        path_buffer = ""
                                                        path_buffer = "mripv4-pools" + path_buffer

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

                                                        if (child_yang_name == "mripv4-pool"):
                                                            for c in self.mripv4_pool:
                                                                segment = c.get_segment_path()
                                                                if (segment_path == segment):
                                                                    return c
                                                            c = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool()
                                                            c.parent = self
                                                            local_reference_key = "ydk::seg::%s" % segment_path
                                                            self._local_refs[local_reference_key] = c
                                                            self.mripv4_pool.append(c)
                                                            return c

                                                        return None

                                                    def has_leaf_or_child_of_name(self, name):
                                                        if(name == "mripv4-pool"):
                                                            return True
                                                        return False

                                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                                        pass

                                                def has_data(self):
                                                    return (
                                                        (self.mripv4_pools is not None and self.mripv4_pools.has_data()) or
                                                        (self.mripv6_pools is not None and self.mripv6_pools.has_data()))

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        (self.mripv4_pools is not None and self.mripv4_pools.has_operation()) or
                                                        (self.mripv6_pools is not None and self.mripv6_pools.has_operation()))

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "mobile-network" + path_buffer

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

                                                    if (child_yang_name == "mripv4-pools"):
                                                        if (self.mripv4_pools is None):
                                                            self.mripv4_pools = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv4Pools()
                                                            self.mripv4_pools.parent = self
                                                            self._children_name_map["mripv4_pools"] = "mripv4-pools"
                                                        return self.mripv4_pools

                                                    if (child_yang_name == "mripv6-pools"):
                                                        if (self.mripv6_pools is None):
                                                            self.mripv6_pools = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork.Mripv6Pools()
                                                            self.mripv6_pools.parent = self
                                                            self._children_name_map["mripv6_pools"] = "mripv6-pools"
                                                        return self.mripv6_pools

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "mripv4-pools" or name == "mripv6-pools"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    pass

                                            def has_data(self):
                                                return (
                                                    (self.mobile_network is not None and self.mobile_network.has_data()) or
                                                    (self.mobile_node is not None and self.mobile_node.has_data()))

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    (self.mobile_network is not None and self.mobile_network.has_operation()) or
                                                    (self.mobile_node is not None and self.mobile_node.has_operation()))

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "pool-attributes" + path_buffer

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

                                                if (child_yang_name == "mobile-network"):
                                                    if (self.mobile_network is None):
                                                        self.mobile_network = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNetwork()
                                                        self.mobile_network.parent = self
                                                        self._children_name_map["mobile_network"] = "mobile-network"
                                                    return self.mobile_network

                                                if (child_yang_name == "mobile-node"):
                                                    if (self.mobile_node is None):
                                                        self.mobile_node = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes.MobileNode()
                                                        self.mobile_node.parent = self
                                                        self._children_name_map["mobile_node"] = "mobile-node"
                                                    return self.mobile_node

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "mobile-network" or name == "mobile-node"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                pass

                                        def has_data(self):
                                            return (
                                                self.name.is_set or
                                                (self.pool_attributes is not None and self.pool_attributes.has_data()))

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.name.yfilter != YFilter.not_set or
                                                (self.pool_attributes is not None and self.pool_attributes.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "authorize" + "[name='" + self.name.get() + "']" + path_buffer

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

                                            if (child_yang_name == "pool-attributes"):
                                                if (self.pool_attributes is None):
                                                    self.pool_attributes = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize.PoolAttributes()
                                                    self.pool_attributes.parent = self
                                                    self._children_name_map["pool_attributes"] = "pool-attributes"
                                                return self.pool_attributes

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "pool-attributes" or name == "name"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "name"):
                                                self.name = value
                                                self.name.value_namespace = name_space
                                                self.name.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.authorize:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.authorize:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "authorizes" + path_buffer

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

                                        if (child_yang_name == "authorize"):
                                            for c in self.authorize:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes.Authorize()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.authorize.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "authorize"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass

                                def has_data(self):
                                    return (
                                        self.unauthorize.is_set or
                                        (self.authorizes is not None and self.authorizes.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.unauthorize.yfilter != YFilter.not_set or
                                        (self.authorizes is not None and self.authorizes.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "network-attributes" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.unauthorize.is_set or self.unauthorize.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.unauthorize.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "authorizes"):
                                        if (self.authorizes is None):
                                            self.authorizes = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes.Authorizes()
                                            self.authorizes.parent = self
                                            self._children_name_map["authorizes"] = "authorizes"
                                        return self.authorizes

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "authorizes" or name == "unauthorize"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "unauthorize"):
                                        self.unauthorize = value
                                        self.unauthorize.value_namespace = name_space
                                        self.unauthorize.value_namespace_prefix = name_space_prefix


                            class GreKey(Entity):
                                """
                                Customer specific GRE key
                                
                                .. attribute:: gre_key_type
                                
                                	GRE key type
                                	**type**\:   :py:class:`GreKeyType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.GreKeyType>`
                                
                                .. attribute:: gre_key_value
                                
                                	GRE key value
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.GreKey, self).__init__()

                                    self.yang_name = "gre-key"
                                    self.yang_parent_name = "customer"

                                    self.gre_key_type = YLeaf(YType.enumeration, "gre-key-type")

                                    self.gre_key_value = YLeaf(YType.int32, "gre-key-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("gre_key_type",
                                                    "gre_key_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.GreKey, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.GreKey, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.gre_key_type.is_set or
                                        self.gre_key_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.gre_key_type.yfilter != YFilter.not_set or
                                        self.gre_key_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "gre-key" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.gre_key_type.is_set or self.gre_key_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.gre_key_type.get_name_leafdata())
                                    if (self.gre_key_value.is_set or self.gre_key_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.gre_key_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "gre-key-type" or name == "gre-key-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "gre-key-type"):
                                        self.gre_key_type = value
                                        self.gre_key_type.value_namespace = name_space
                                        self.gre_key_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "gre-key-value"):
                                        self.gre_key_value = value
                                        self.gre_key_value.value_namespace = name_space
                                        self.gre_key_value.value_namespace_prefix = name_space_prefix


                            class BindingAttributes(Entity):
                                """
                                Customer specific binding attributes
                                
                                .. attribute:: max_life_time
                                
                                	Maximum bce lifetime permitted
                                	**type**\:  int
                                
                                	**range:** 10..65535
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.BindingAttributes, self).__init__()

                                    self.yang_name = "binding-attributes"
                                    self.yang_parent_name = "customer"

                                    self.max_life_time = YLeaf(YType.uint32, "max-life-time")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("max_life_time") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.BindingAttributes, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MobileIp.Lmas.Lma.Services.Service.Customers.Customer.BindingAttributes, self).__setattr__(name, value)

                                def has_data(self):
                                    return self.max_life_time.is_set

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.max_life_time.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "binding-attributes" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.max_life_time.is_set or self.max_life_time.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.max_life_time.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "max-life-time"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "max-life-time"):
                                        self.max_life_time = value
                                        self.max_life_time.value_namespace = name_space
                                        self.max_life_time.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.customer_name.is_set or
                                    self.vrf_name.is_set or
                                    self.bandwidth_aggregate.is_set or
                                    self.mnp_customer.is_set or
                                    self.mnp_ipv4_customer.is_set or
                                    self.mnp_ipv4_lmn.is_set or
                                    self.mnp_ipv6_customer.is_set or
                                    self.mnp_ipv6_lmn.is_set or
                                    self.mnp_lmn.is_set or
                                    self.mobile_route_ad.is_set or
                                    (self.authenticate_option is not None and self.authenticate_option.has_data()) or
                                    (self.binding_attributes is not None and self.binding_attributes.has_data()) or
                                    (self.gre_key is not None and self.gre_key.has_data()) or
                                    (self.heart_beat_attributes is not None and self.heart_beat_attributes.has_data()) or
                                    (self.network_attributes is not None and self.network_attributes.has_data()) or
                                    (self.transports is not None and self.transports.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.customer_name.yfilter != YFilter.not_set or
                                    self.vrf_name.yfilter != YFilter.not_set or
                                    self.bandwidth_aggregate.yfilter != YFilter.not_set or
                                    self.mnp_customer.yfilter != YFilter.not_set or
                                    self.mnp_ipv4_customer.yfilter != YFilter.not_set or
                                    self.mnp_ipv4_lmn.yfilter != YFilter.not_set or
                                    self.mnp_ipv6_customer.yfilter != YFilter.not_set or
                                    self.mnp_ipv6_lmn.yfilter != YFilter.not_set or
                                    self.mnp_lmn.yfilter != YFilter.not_set or
                                    self.mobile_route_ad.yfilter != YFilter.not_set or
                                    (self.authenticate_option is not None and self.authenticate_option.has_operation()) or
                                    (self.binding_attributes is not None and self.binding_attributes.has_operation()) or
                                    (self.gre_key is not None and self.gre_key.has_operation()) or
                                    (self.heart_beat_attributes is not None and self.heart_beat_attributes.has_operation()) or
                                    (self.network_attributes is not None and self.network_attributes.has_operation()) or
                                    (self.transports is not None and self.transports.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "customer" + "[customer-name='" + self.customer_name.get() + "']" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.customer_name.is_set or self.customer_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.customer_name.get_name_leafdata())
                                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vrf_name.get_name_leafdata())
                                if (self.bandwidth_aggregate.is_set or self.bandwidth_aggregate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bandwidth_aggregate.get_name_leafdata())
                                if (self.mnp_customer.is_set or self.mnp_customer.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mnp_customer.get_name_leafdata())
                                if (self.mnp_ipv4_customer.is_set or self.mnp_ipv4_customer.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mnp_ipv4_customer.get_name_leafdata())
                                if (self.mnp_ipv4_lmn.is_set or self.mnp_ipv4_lmn.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mnp_ipv4_lmn.get_name_leafdata())
                                if (self.mnp_ipv6_customer.is_set or self.mnp_ipv6_customer.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mnp_ipv6_customer.get_name_leafdata())
                                if (self.mnp_ipv6_lmn.is_set or self.mnp_ipv6_lmn.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mnp_ipv6_lmn.get_name_leafdata())
                                if (self.mnp_lmn.is_set or self.mnp_lmn.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mnp_lmn.get_name_leafdata())
                                if (self.mobile_route_ad.is_set or self.mobile_route_ad.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mobile_route_ad.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "authenticate-option"):
                                    if (self.authenticate_option is None):
                                        self.authenticate_option = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.AuthenticateOption()
                                        self.authenticate_option.parent = self
                                        self._children_name_map["authenticate_option"] = "authenticate-option"
                                    return self.authenticate_option

                                if (child_yang_name == "binding-attributes"):
                                    if (self.binding_attributes is None):
                                        self.binding_attributes = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.BindingAttributes()
                                        self.binding_attributes.parent = self
                                        self._children_name_map["binding_attributes"] = "binding-attributes"
                                    return self.binding_attributes

                                if (child_yang_name == "gre-key"):
                                    if (self.gre_key is None):
                                        self.gre_key = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.GreKey()
                                        self.gre_key.parent = self
                                        self._children_name_map["gre_key"] = "gre-key"
                                    return self.gre_key

                                if (child_yang_name == "heart-beat-attributes"):
                                    if (self.heart_beat_attributes is None):
                                        self.heart_beat_attributes = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.HeartBeatAttributes()
                                        self.heart_beat_attributes.parent = self
                                        self._children_name_map["heart_beat_attributes"] = "heart-beat-attributes"
                                    return self.heart_beat_attributes

                                if (child_yang_name == "network-attributes"):
                                    if (self.network_attributes is None):
                                        self.network_attributes = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.NetworkAttributes()
                                        self.network_attributes.parent = self
                                        self._children_name_map["network_attributes"] = "network-attributes"
                                    return self.network_attributes

                                if (child_yang_name == "transports"):
                                    if (self.transports is None):
                                        self.transports = MobileIp.Lmas.Lma.Services.Service.Customers.Customer.Transports()
                                        self.transports.parent = self
                                        self._children_name_map["transports"] = "transports"
                                    return self.transports

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "authenticate-option" or name == "binding-attributes" or name == "gre-key" or name == "heart-beat-attributes" or name == "network-attributes" or name == "transports" or name == "customer-name" or name == "vrf-name" or name == "bandwidth-aggregate" or name == "mnp-customer" or name == "mnp-ipv4-customer" or name == "mnp-ipv4-lmn" or name == "mnp-ipv6-customer" or name == "mnp-ipv6-lmn" or name == "mnp-lmn" or name == "mobile-route-ad"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "customer-name"):
                                    self.customer_name = value
                                    self.customer_name.value_namespace = name_space
                                    self.customer_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "vrf-name"):
                                    self.vrf_name = value
                                    self.vrf_name.value_namespace = name_space
                                    self.vrf_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "bandwidth-aggregate"):
                                    self.bandwidth_aggregate = value
                                    self.bandwidth_aggregate.value_namespace = name_space
                                    self.bandwidth_aggregate.value_namespace_prefix = name_space_prefix
                                if(value_path == "mnp-customer"):
                                    self.mnp_customer = value
                                    self.mnp_customer.value_namespace = name_space
                                    self.mnp_customer.value_namespace_prefix = name_space_prefix
                                if(value_path == "mnp-ipv4-customer"):
                                    self.mnp_ipv4_customer = value
                                    self.mnp_ipv4_customer.value_namespace = name_space
                                    self.mnp_ipv4_customer.value_namespace_prefix = name_space_prefix
                                if(value_path == "mnp-ipv4-lmn"):
                                    self.mnp_ipv4_lmn = value
                                    self.mnp_ipv4_lmn.value_namespace = name_space
                                    self.mnp_ipv4_lmn.value_namespace_prefix = name_space_prefix
                                if(value_path == "mnp-ipv6-customer"):
                                    self.mnp_ipv6_customer = value
                                    self.mnp_ipv6_customer.value_namespace = name_space
                                    self.mnp_ipv6_customer.value_namespace_prefix = name_space_prefix
                                if(value_path == "mnp-ipv6-lmn"):
                                    self.mnp_ipv6_lmn = value
                                    self.mnp_ipv6_lmn.value_namespace = name_space
                                    self.mnp_ipv6_lmn.value_namespace_prefix = name_space_prefix
                                if(value_path == "mnp-lmn"):
                                    self.mnp_lmn = value
                                    self.mnp_lmn.value_namespace = name_space
                                    self.mnp_lmn.value_namespace_prefix = name_space_prefix
                                if(value_path == "mobile-route-ad"):
                                    self.mobile_route_ad = value
                                    self.mobile_route_ad.value_namespace = name_space
                                    self.mobile_route_ad.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.customer:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.customer:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "customers" + path_buffer

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

                            if (child_yang_name == "customer"):
                                for c in self.customer:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = MobileIp.Lmas.Lma.Services.Service.Customers.Customer()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.customer.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "customer"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.lma_service.is_set or
                            self.ignore_home_address.is_set or
                            self.mnp_customer.is_set or
                            self.mnp_ipv4_customer.is_set or
                            self.mnp_ipv4_lmn.is_set or
                            self.mnp_ipv6_customer.is_set or
                            self.mnp_ipv6_lmn.is_set or
                            self.mnp_lmn.is_set or
                            (self.customers is not None and self.customers.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.lma_service.yfilter != YFilter.not_set or
                            self.ignore_home_address.yfilter != YFilter.not_set or
                            self.mnp_customer.yfilter != YFilter.not_set or
                            self.mnp_ipv4_customer.yfilter != YFilter.not_set or
                            self.mnp_ipv4_lmn.yfilter != YFilter.not_set or
                            self.mnp_ipv6_customer.yfilter != YFilter.not_set or
                            self.mnp_ipv6_lmn.yfilter != YFilter.not_set or
                            self.mnp_lmn.yfilter != YFilter.not_set or
                            (self.customers is not None and self.customers.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "service" + "[lma-service='" + self.lma_service.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.lma_service.is_set or self.lma_service.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lma_service.get_name_leafdata())
                        if (self.ignore_home_address.is_set or self.ignore_home_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ignore_home_address.get_name_leafdata())
                        if (self.mnp_customer.is_set or self.mnp_customer.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mnp_customer.get_name_leafdata())
                        if (self.mnp_ipv4_customer.is_set or self.mnp_ipv4_customer.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mnp_ipv4_customer.get_name_leafdata())
                        if (self.mnp_ipv4_lmn.is_set or self.mnp_ipv4_lmn.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mnp_ipv4_lmn.get_name_leafdata())
                        if (self.mnp_ipv6_customer.is_set or self.mnp_ipv6_customer.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mnp_ipv6_customer.get_name_leafdata())
                        if (self.mnp_ipv6_lmn.is_set or self.mnp_ipv6_lmn.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mnp_ipv6_lmn.get_name_leafdata())
                        if (self.mnp_lmn.is_set or self.mnp_lmn.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mnp_lmn.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "customers"):
                            if (self.customers is None):
                                self.customers = MobileIp.Lmas.Lma.Services.Service.Customers()
                                self.customers.parent = self
                                self._children_name_map["customers"] = "customers"
                            return self.customers

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "customers" or name == "lma-service" or name == "ignore-home-address" or name == "mnp-customer" or name == "mnp-ipv4-customer" or name == "mnp-ipv4-lmn" or name == "mnp-ipv6-customer" or name == "mnp-ipv6-lmn" or name == "mnp-lmn"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "lma-service"):
                            self.lma_service = value
                            self.lma_service.value_namespace = name_space
                            self.lma_service.value_namespace_prefix = name_space_prefix
                        if(value_path == "ignore-home-address"):
                            self.ignore_home_address = value
                            self.ignore_home_address.value_namespace = name_space
                            self.ignore_home_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "mnp-customer"):
                            self.mnp_customer = value
                            self.mnp_customer.value_namespace = name_space
                            self.mnp_customer.value_namespace_prefix = name_space_prefix
                        if(value_path == "mnp-ipv4-customer"):
                            self.mnp_ipv4_customer = value
                            self.mnp_ipv4_customer.value_namespace = name_space
                            self.mnp_ipv4_customer.value_namespace_prefix = name_space_prefix
                        if(value_path == "mnp-ipv4-lmn"):
                            self.mnp_ipv4_lmn = value
                            self.mnp_ipv4_lmn.value_namespace = name_space
                            self.mnp_ipv4_lmn.value_namespace_prefix = name_space_prefix
                        if(value_path == "mnp-ipv6-customer"):
                            self.mnp_ipv6_customer = value
                            self.mnp_ipv6_customer.value_namespace = name_space
                            self.mnp_ipv6_customer.value_namespace_prefix = name_space_prefix
                        if(value_path == "mnp-ipv6-lmn"):
                            self.mnp_ipv6_lmn = value
                            self.mnp_ipv6_lmn.value_namespace = name_space
                            self.mnp_ipv6_lmn.value_namespace_prefix = name_space_prefix
                        if(value_path == "mnp-lmn"):
                            self.mnp_lmn = value
                            self.mnp_lmn.value_namespace = name_space
                            self.mnp_lmn.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.service:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.service:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "services" + path_buffer

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

                    if (child_yang_name == "service"):
                        for c in self.service:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = MobileIp.Lmas.Lma.Services.Service()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.service.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "service"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Networks(Entity):
                """
                Table of Network
                
                .. attribute:: network
                
                	network for this LMA
                	**type**\: list of    :py:class:`Network <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network>`
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.Networks, self).__init__()

                    self.yang_name = "networks"
                    self.yang_parent_name = "lma"

                    self.network = YList(self)

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
                                super(MobileIp.Lmas.Lma.Networks, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MobileIp.Lmas.Lma.Networks, self).__setattr__(name, value)


                class Network(Entity):
                    """
                    network for this LMA
                    
                    .. attribute:: lma_network  <key>
                    
                    	Network name
                    	**type**\:  str
                    
                    	**length:** 1..125
                    
                    .. attribute:: pool_attributes
                    
                    	Pool configs for this network
                    	**type**\:   :py:class:`PoolAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes>`
                    
                    

                    """

                    _prefix = 'ip-mobileip-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MobileIp.Lmas.Lma.Networks.Network, self).__init__()

                        self.yang_name = "network"
                        self.yang_parent_name = "networks"

                        self.lma_network = YLeaf(YType.str, "lma-network")

                        self.pool_attributes = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes()
                        self.pool_attributes.parent = self
                        self._children_name_map["pool_attributes"] = "pool-attributes"
                        self._children_yang_names.add("pool-attributes")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("lma_network") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MobileIp.Lmas.Lma.Networks.Network, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MobileIp.Lmas.Lma.Networks.Network, self).__setattr__(name, value)


                    class PoolAttributes(Entity):
                        """
                        Pool configs for this network
                        
                        .. attribute:: mobile_network
                        
                        	pool configs for the mobile network
                        	**type**\:   :py:class:`MobileNetwork <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork>`
                        
                        .. attribute:: mobile_node
                        
                        	pool configs for the mobile nodes
                        	**type**\:   :py:class:`MobileNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode>`
                        
                        

                        """

                        _prefix = 'ip-mobileip-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes, self).__init__()

                            self.yang_name = "pool-attributes"
                            self.yang_parent_name = "network"

                            self.mobile_network = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork()
                            self.mobile_network.parent = self
                            self._children_name_map["mobile_network"] = "mobile-network"
                            self._children_yang_names.add("mobile-network")

                            self.mobile_node = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode()
                            self.mobile_node.parent = self
                            self._children_name_map["mobile_node"] = "mobile-node"
                            self._children_yang_names.add("mobile-node")


                        class MobileNode(Entity):
                            """
                            pool configs for the mobile nodes
                            
                            .. attribute:: ipv4_pool
                            
                            	None
                            	**type**\:   :py:class:`Ipv4Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv4Pool>`
                            
                            .. attribute:: ipv6_pool
                            
                            	None
                            	**type**\:   :py:class:`Ipv6Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv6Pool>`
                            
                            

                            """

                            _prefix = 'ip-mobileip-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode, self).__init__()

                                self.yang_name = "mobile-node"
                                self.yang_parent_name = "pool-attributes"

                                self.ipv4_pool = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv4Pool()
                                self.ipv4_pool.parent = self
                                self._children_name_map["ipv4_pool"] = "ipv4-pool"
                                self._children_yang_names.add("ipv4-pool")

                                self.ipv6_pool = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv6Pool()
                                self.ipv6_pool.parent = self
                                self._children_name_map["ipv6_pool"] = "ipv6-pool"
                                self._children_yang_names.add("ipv6-pool")


                            class Ipv4Pool(Entity):
                                """
                                None
                                
                                .. attribute:: pool_prefix
                                
                                	IPv4 Pool Prefix value
                                	**type**\:  int
                                
                                	**range:** 8..30
                                
                                .. attribute:: start_address
                                
                                	Pool IPv4 start address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv4Pool, self).__init__()

                                    self.yang_name = "ipv4-pool"
                                    self.yang_parent_name = "mobile-node"

                                    self.pool_prefix = YLeaf(YType.uint32, "pool-prefix")

                                    self.start_address = YLeaf(YType.str, "start-address")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("pool_prefix",
                                                    "start_address") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv4Pool, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv4Pool, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.pool_prefix.is_set or
                                        self.start_address.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.pool_prefix.yfilter != YFilter.not_set or
                                        self.start_address.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "ipv4-pool" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.pool_prefix.is_set or self.pool_prefix.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.pool_prefix.get_name_leafdata())
                                    if (self.start_address.is_set or self.start_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.start_address.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "pool-prefix" or name == "start-address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "pool-prefix"):
                                        self.pool_prefix = value
                                        self.pool_prefix.value_namespace = name_space
                                        self.pool_prefix.value_namespace_prefix = name_space_prefix
                                    if(value_path == "start-address"):
                                        self.start_address = value
                                        self.start_address.value_namespace = name_space
                                        self.start_address.value_namespace_prefix = name_space_prefix


                            class Ipv6Pool(Entity):
                                """
                                None
                                
                                .. attribute:: pool_prefix
                                
                                	IPv6 Pool Prefix value
                                	**type**\:  int
                                
                                	**range:** 8..62
                                
                                .. attribute:: start_address
                                
                                	Pool IPv6 start address
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv6Pool, self).__init__()

                                    self.yang_name = "ipv6-pool"
                                    self.yang_parent_name = "mobile-node"

                                    self.pool_prefix = YLeaf(YType.uint32, "pool-prefix")

                                    self.start_address = YLeaf(YType.str, "start-address")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("pool_prefix",
                                                    "start_address") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv6Pool, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv6Pool, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.pool_prefix.is_set or
                                        self.start_address.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.pool_prefix.yfilter != YFilter.not_set or
                                        self.start_address.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "ipv6-pool" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.pool_prefix.is_set or self.pool_prefix.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.pool_prefix.get_name_leafdata())
                                    if (self.start_address.is_set or self.start_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.start_address.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "pool-prefix" or name == "start-address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "pool-prefix"):
                                        self.pool_prefix = value
                                        self.pool_prefix.value_namespace = name_space
                                        self.pool_prefix.value_namespace_prefix = name_space_prefix
                                    if(value_path == "start-address"):
                                        self.start_address = value
                                        self.start_address.value_namespace = name_space
                                        self.start_address.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    (self.ipv4_pool is not None and self.ipv4_pool.has_data()) or
                                    (self.ipv6_pool is not None and self.ipv6_pool.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.ipv4_pool is not None and self.ipv4_pool.has_operation()) or
                                    (self.ipv6_pool is not None and self.ipv6_pool.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "mobile-node" + path_buffer

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

                                if (child_yang_name == "ipv4-pool"):
                                    if (self.ipv4_pool is None):
                                        self.ipv4_pool = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv4Pool()
                                        self.ipv4_pool.parent = self
                                        self._children_name_map["ipv4_pool"] = "ipv4-pool"
                                    return self.ipv4_pool

                                if (child_yang_name == "ipv6-pool"):
                                    if (self.ipv6_pool is None):
                                        self.ipv6_pool = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode.Ipv6Pool()
                                        self.ipv6_pool.parent = self
                                        self._children_name_map["ipv6_pool"] = "ipv6-pool"
                                    return self.ipv6_pool

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ipv4-pool" or name == "ipv6-pool"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class MobileNetwork(Entity):
                            """
                            pool configs for the mobile network
                            
                            .. attribute:: mripv4_pools
                            
                            	Table of MRIPV4Pool
                            	**type**\:   :py:class:`Mripv4Pools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools>`
                            
                            .. attribute:: mripv6_pools
                            
                            	Table of MRIPV6Pool
                            	**type**\:   :py:class:`Mripv6Pools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools>`
                            
                            

                            """

                            _prefix = 'ip-mobileip-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork, self).__init__()

                                self.yang_name = "mobile-network"
                                self.yang_parent_name = "pool-attributes"

                                self.mripv4_pools = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools()
                                self.mripv4_pools.parent = self
                                self._children_name_map["mripv4_pools"] = "mripv4-pools"
                                self._children_yang_names.add("mripv4-pools")

                                self.mripv6_pools = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools()
                                self.mripv6_pools.parent = self
                                self._children_name_map["mripv6_pools"] = "mripv6-pools"
                                self._children_yang_names.add("mripv6-pools")


                            class Mripv6Pools(Entity):
                                """
                                Table of MRIPV6Pool
                                
                                .. attribute:: mripv6_pool
                                
                                	ipv6 pool
                                	**type**\: list of    :py:class:`Mripv6Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool>`
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools, self).__init__()

                                    self.yang_name = "mripv6-pools"
                                    self.yang_parent_name = "mobile-network"

                                    self.mripv6_pool = YList(self)

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
                                                super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools, self).__setattr__(name, value)


                                class Mripv6Pool(Entity):
                                    """
                                    ipv6 pool
                                    
                                    .. attribute:: start_address  <key>
                                    
                                    	Pool IPv6 start address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: network_prefix
                                    
                                    	IPv4 Network Prefix value
                                    	**type**\:  int
                                    
                                    	**range:** 8..64
                                    
                                    .. attribute:: pool_prefix
                                    
                                    	IPv6 Pool Prefix value
                                    	**type**\:  int
                                    
                                    	**range:** 8..64
                                    
                                    

                                    """

                                    _prefix = 'ip-mobileip-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool, self).__init__()

                                        self.yang_name = "mripv6-pool"
                                        self.yang_parent_name = "mripv6-pools"

                                        self.start_address = YLeaf(YType.str, "start-address")

                                        self.network_prefix = YLeaf(YType.uint32, "network-prefix")

                                        self.pool_prefix = YLeaf(YType.uint32, "pool-prefix")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("start_address",
                                                        "network_prefix",
                                                        "pool_prefix") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.start_address.is_set or
                                            self.network_prefix.is_set or
                                            self.pool_prefix.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.start_address.yfilter != YFilter.not_set or
                                            self.network_prefix.yfilter != YFilter.not_set or
                                            self.pool_prefix.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "mripv6-pool" + "[start-address='" + self.start_address.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.start_address.is_set or self.start_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.start_address.get_name_leafdata())
                                        if (self.network_prefix.is_set or self.network_prefix.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.network_prefix.get_name_leafdata())
                                        if (self.pool_prefix.is_set or self.pool_prefix.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.pool_prefix.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "start-address" or name == "network-prefix" or name == "pool-prefix"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "start-address"):
                                            self.start_address = value
                                            self.start_address.value_namespace = name_space
                                            self.start_address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "network-prefix"):
                                            self.network_prefix = value
                                            self.network_prefix.value_namespace = name_space
                                            self.network_prefix.value_namespace_prefix = name_space_prefix
                                        if(value_path == "pool-prefix"):
                                            self.pool_prefix = value
                                            self.pool_prefix.value_namespace = name_space
                                            self.pool_prefix.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.mripv6_pool:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.mripv6_pool:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "mripv6-pools" + path_buffer

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

                                    if (child_yang_name == "mripv6-pool"):
                                        for c in self.mripv6_pool:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools.Mripv6Pool()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.mripv6_pool.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "mripv6-pool"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class Mripv4Pools(Entity):
                                """
                                Table of MRIPV4Pool
                                
                                .. attribute:: mripv4_pool
                                
                                	ipv4 pool
                                	**type**\: list of    :py:class:`Mripv4Pool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_mobileip_cfg.MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool>`
                                
                                

                                """

                                _prefix = 'ip-mobileip-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools, self).__init__()

                                    self.yang_name = "mripv4-pools"
                                    self.yang_parent_name = "mobile-network"

                                    self.mripv4_pool = YList(self)

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
                                                super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools, self).__setattr__(name, value)


                                class Mripv4Pool(Entity):
                                    """
                                    ipv4 pool
                                    
                                    .. attribute:: start_address  <key>
                                    
                                    	Pool IPv4 start address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: network_prefix
                                    
                                    	IPv4 Network Prefix value
                                    	**type**\:  int
                                    
                                    	**range:** 8..32
                                    
                                    .. attribute:: pool_prefix
                                    
                                    	IPv4 Pool Prefix value
                                    	**type**\:  int
                                    
                                    	**range:** 8..30
                                    
                                    

                                    """

                                    _prefix = 'ip-mobileip-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool, self).__init__()

                                        self.yang_name = "mripv4-pool"
                                        self.yang_parent_name = "mripv4-pools"

                                        self.start_address = YLeaf(YType.str, "start-address")

                                        self.network_prefix = YLeaf(YType.uint32, "network-prefix")

                                        self.pool_prefix = YLeaf(YType.uint32, "pool-prefix")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("start_address",
                                                        "network_prefix",
                                                        "pool_prefix") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.start_address.is_set or
                                            self.network_prefix.is_set or
                                            self.pool_prefix.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.start_address.yfilter != YFilter.not_set or
                                            self.network_prefix.yfilter != YFilter.not_set or
                                            self.pool_prefix.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "mripv4-pool" + "[start-address='" + self.start_address.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.start_address.is_set or self.start_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.start_address.get_name_leafdata())
                                        if (self.network_prefix.is_set or self.network_prefix.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.network_prefix.get_name_leafdata())
                                        if (self.pool_prefix.is_set or self.pool_prefix.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.pool_prefix.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "start-address" or name == "network-prefix" or name == "pool-prefix"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "start-address"):
                                            self.start_address = value
                                            self.start_address.value_namespace = name_space
                                            self.start_address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "network-prefix"):
                                            self.network_prefix = value
                                            self.network_prefix.value_namespace = name_space
                                            self.network_prefix.value_namespace_prefix = name_space_prefix
                                        if(value_path == "pool-prefix"):
                                            self.pool_prefix = value
                                            self.pool_prefix.value_namespace = name_space
                                            self.pool_prefix.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.mripv4_pool:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.mripv4_pool:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "mripv4-pools" + path_buffer

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

                                    if (child_yang_name == "mripv4-pool"):
                                        for c in self.mripv4_pool:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools.Mripv4Pool()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.mripv4_pool.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "mripv4-pool"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    (self.mripv4_pools is not None and self.mripv4_pools.has_data()) or
                                    (self.mripv6_pools is not None and self.mripv6_pools.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.mripv4_pools is not None and self.mripv4_pools.has_operation()) or
                                    (self.mripv6_pools is not None and self.mripv6_pools.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "mobile-network" + path_buffer

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

                                if (child_yang_name == "mripv4-pools"):
                                    if (self.mripv4_pools is None):
                                        self.mripv4_pools = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv4Pools()
                                        self.mripv4_pools.parent = self
                                        self._children_name_map["mripv4_pools"] = "mripv4-pools"
                                    return self.mripv4_pools

                                if (child_yang_name == "mripv6-pools"):
                                    if (self.mripv6_pools is None):
                                        self.mripv6_pools = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork.Mripv6Pools()
                                        self.mripv6_pools.parent = self
                                        self._children_name_map["mripv6_pools"] = "mripv6-pools"
                                    return self.mripv6_pools

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "mripv4-pools" or name == "mripv6-pools"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                (self.mobile_network is not None and self.mobile_network.has_data()) or
                                (self.mobile_node is not None and self.mobile_node.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.mobile_network is not None and self.mobile_network.has_operation()) or
                                (self.mobile_node is not None and self.mobile_node.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "pool-attributes" + path_buffer

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

                            if (child_yang_name == "mobile-network"):
                                if (self.mobile_network is None):
                                    self.mobile_network = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNetwork()
                                    self.mobile_network.parent = self
                                    self._children_name_map["mobile_network"] = "mobile-network"
                                return self.mobile_network

                            if (child_yang_name == "mobile-node"):
                                if (self.mobile_node is None):
                                    self.mobile_node = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes.MobileNode()
                                    self.mobile_node.parent = self
                                    self._children_name_map["mobile_node"] = "mobile-node"
                                return self.mobile_node

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "mobile-network" or name == "mobile-node"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.lma_network.is_set or
                            (self.pool_attributes is not None and self.pool_attributes.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.lma_network.yfilter != YFilter.not_set or
                            (self.pool_attributes is not None and self.pool_attributes.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "network" + "[lma-network='" + self.lma_network.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.lma_network.is_set or self.lma_network.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lma_network.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "pool-attributes"):
                            if (self.pool_attributes is None):
                                self.pool_attributes = MobileIp.Lmas.Lma.Networks.Network.PoolAttributes()
                                self.pool_attributes.parent = self
                                self._children_name_map["pool_attributes"] = "pool-attributes"
                            return self.pool_attributes

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "pool-attributes" or name == "lma-network"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "lma-network"):
                            self.lma_network = value
                            self.lma_network.value_namespace = name_space
                            self.lma_network.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.network:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.network:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "networks" + path_buffer

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

                    if (child_yang_name == "network"):
                        for c in self.network:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = MobileIp.Lmas.Lma.Networks.Network()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.network.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "network"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class ReplayProtection(Entity):
                """
                Replay Protection Method
                
                .. attribute:: timestamp_window
                
                	Specify timestamp window value in seconds
                	**type**\:  int
                
                	**range:** 1..255
                
                	**units**\: second
                
                

                """

                _prefix = 'ip-mobileip-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MobileIp.Lmas.Lma.ReplayProtection, self).__init__()

                    self.yang_name = "replay-protection"
                    self.yang_parent_name = "lma"

                    self.timestamp_window = YLeaf(YType.uint32, "timestamp-window")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("timestamp_window") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MobileIp.Lmas.Lma.ReplayProtection, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MobileIp.Lmas.Lma.ReplayProtection, self).__setattr__(name, value)

                def has_data(self):
                    return self.timestamp_window.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.timestamp_window.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "replay-protection" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.timestamp_window.is_set or self.timestamp_window.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.timestamp_window.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "timestamp-window"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "timestamp-window"):
                        self.timestamp_window = value
                        self.timestamp_window.value_namespace = name_space
                        self.timestamp_window.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.lma_name.is_set or
                    self.domain_name.is_set or
                    self.ani.is_set or
                    self.default_profile.is_set or
                    self.dynamic.is_set or
                    self.enforce.is_set or
                    self.generate.is_set or
                    self.interface.is_set or
                    self.mobile_map.is_set or
                    self.mobile_route_ad.is_set or
                    self.multipath.is_set or
                    self.pgw_subs_cont.is_set or
                    (self.aaa is not None and self.aaa.has_data()) or
                    (self.binding_attributes is not None and self.binding_attributes.has_data()) or
                    (self.binding_revocation_attributes is not None and self.binding_revocation_attributes.has_data()) or
                    (self.dscp is not None and self.dscp.has_data()) or
                    (self.heart_beat_attributes is not None and self.heart_beat_attributes.has_data()) or
                    (self.hnp is not None and self.hnp.has_data()) or
                    (self.lmaipv4_addresses is not None and self.lmaipv4_addresses.has_data()) or
                    (self.lmaipv6_addresses is not None and self.lmaipv6_addresses.has_data()) or
                    (self.mags is not None and self.mags.has_data()) or
                    (self.networks is not None and self.networks.has_data()) or
                    (self.rat_attributes is not None and self.rat_attributes.has_data()) or
                    (self.redistribute is not None and self.redistribute.has_data()) or
                    (self.replay_protection is not None and self.replay_protection.has_data()) or
                    (self.roles is not None and self.roles.has_data()) or
                    (self.services is not None and self.services.has_data()) or
                    (self.tunnel_attributes is not None and self.tunnel_attributes.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.lma_name.yfilter != YFilter.not_set or
                    self.domain_name.yfilter != YFilter.not_set or
                    self.ani.yfilter != YFilter.not_set or
                    self.default_profile.yfilter != YFilter.not_set or
                    self.dynamic.yfilter != YFilter.not_set or
                    self.enforce.yfilter != YFilter.not_set or
                    self.generate.yfilter != YFilter.not_set or
                    self.interface.yfilter != YFilter.not_set or
                    self.mobile_map.yfilter != YFilter.not_set or
                    self.mobile_route_ad.yfilter != YFilter.not_set or
                    self.multipath.yfilter != YFilter.not_set or
                    self.pgw_subs_cont.yfilter != YFilter.not_set or
                    (self.aaa is not None and self.aaa.has_operation()) or
                    (self.binding_attributes is not None and self.binding_attributes.has_operation()) or
                    (self.binding_revocation_attributes is not None and self.binding_revocation_attributes.has_operation()) or
                    (self.dscp is not None and self.dscp.has_operation()) or
                    (self.heart_beat_attributes is not None and self.heart_beat_attributes.has_operation()) or
                    (self.hnp is not None and self.hnp.has_operation()) or
                    (self.lmaipv4_addresses is not None and self.lmaipv4_addresses.has_operation()) or
                    (self.lmaipv6_addresses is not None and self.lmaipv6_addresses.has_operation()) or
                    (self.mags is not None and self.mags.has_operation()) or
                    (self.networks is not None and self.networks.has_operation()) or
                    (self.rat_attributes is not None and self.rat_attributes.has_operation()) or
                    (self.redistribute is not None and self.redistribute.has_operation()) or
                    (self.replay_protection is not None and self.replay_protection.has_operation()) or
                    (self.roles is not None and self.roles.has_operation()) or
                    (self.services is not None and self.services.has_operation()) or
                    (self.tunnel_attributes is not None and self.tunnel_attributes.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "lma" + "[lma-name='" + self.lma_name.get() + "']" + "[domain-name='" + self.domain_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-mobileip-cfg:mobile-ip/lmas/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.lma_name.is_set or self.lma_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.lma_name.get_name_leafdata())
                if (self.domain_name.is_set or self.domain_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.domain_name.get_name_leafdata())
                if (self.ani.is_set or self.ani.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ani.get_name_leafdata())
                if (self.default_profile.is_set or self.default_profile.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.default_profile.get_name_leafdata())
                if (self.dynamic.is_set or self.dynamic.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dynamic.get_name_leafdata())
                if (self.enforce.is_set or self.enforce.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enforce.get_name_leafdata())
                if (self.generate.is_set or self.generate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.generate.get_name_leafdata())
                if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface.get_name_leafdata())
                if (self.mobile_map.is_set or self.mobile_map.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mobile_map.get_name_leafdata())
                if (self.mobile_route_ad.is_set or self.mobile_route_ad.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mobile_route_ad.get_name_leafdata())
                if (self.multipath.is_set or self.multipath.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.multipath.get_name_leafdata())
                if (self.pgw_subs_cont.is_set or self.pgw_subs_cont.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pgw_subs_cont.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "aaa"):
                    if (self.aaa is None):
                        self.aaa = MobileIp.Lmas.Lma.Aaa()
                        self.aaa.parent = self
                        self._children_name_map["aaa"] = "aaa"
                    return self.aaa

                if (child_yang_name == "binding-attributes"):
                    if (self.binding_attributes is None):
                        self.binding_attributes = MobileIp.Lmas.Lma.BindingAttributes()
                        self.binding_attributes.parent = self
                        self._children_name_map["binding_attributes"] = "binding-attributes"
                    return self.binding_attributes

                if (child_yang_name == "binding-revocation-attributes"):
                    if (self.binding_revocation_attributes is None):
                        self.binding_revocation_attributes = MobileIp.Lmas.Lma.BindingRevocationAttributes()
                        self.binding_revocation_attributes.parent = self
                        self._children_name_map["binding_revocation_attributes"] = "binding-revocation-attributes"
                    return self.binding_revocation_attributes

                if (child_yang_name == "dscp"):
                    if (self.dscp is None):
                        self.dscp = MobileIp.Lmas.Lma.Dscp()
                        self.dscp.parent = self
                        self._children_name_map["dscp"] = "dscp"
                    return self.dscp

                if (child_yang_name == "heart-beat-attributes"):
                    if (self.heart_beat_attributes is None):
                        self.heart_beat_attributes = MobileIp.Lmas.Lma.HeartBeatAttributes()
                        self.heart_beat_attributes.parent = self
                        self._children_name_map["heart_beat_attributes"] = "heart-beat-attributes"
                    return self.heart_beat_attributes

                if (child_yang_name == "hnp"):
                    if (self.hnp is None):
                        self.hnp = MobileIp.Lmas.Lma.Hnp()
                        self.hnp.parent = self
                        self._children_name_map["hnp"] = "hnp"
                    return self.hnp

                if (child_yang_name == "lmaipv4-addresses"):
                    if (self.lmaipv4_addresses is None):
                        self.lmaipv4_addresses = MobileIp.Lmas.Lma.Lmaipv4Addresses()
                        self.lmaipv4_addresses.parent = self
                        self._children_name_map["lmaipv4_addresses"] = "lmaipv4-addresses"
                    return self.lmaipv4_addresses

                if (child_yang_name == "lmaipv6-addresses"):
                    if (self.lmaipv6_addresses is None):
                        self.lmaipv6_addresses = MobileIp.Lmas.Lma.Lmaipv6Addresses()
                        self.lmaipv6_addresses.parent = self
                        self._children_name_map["lmaipv6_addresses"] = "lmaipv6-addresses"
                    return self.lmaipv6_addresses

                if (child_yang_name == "mags"):
                    if (self.mags is None):
                        self.mags = MobileIp.Lmas.Lma.Mags()
                        self.mags.parent = self
                        self._children_name_map["mags"] = "mags"
                    return self.mags

                if (child_yang_name == "networks"):
                    if (self.networks is None):
                        self.networks = MobileIp.Lmas.Lma.Networks()
                        self.networks.parent = self
                        self._children_name_map["networks"] = "networks"
                    return self.networks

                if (child_yang_name == "rat-attributes"):
                    if (self.rat_attributes is None):
                        self.rat_attributes = MobileIp.Lmas.Lma.RatAttributes()
                        self.rat_attributes.parent = self
                        self._children_name_map["rat_attributes"] = "rat-attributes"
                    return self.rat_attributes

                if (child_yang_name == "redistribute"):
                    if (self.redistribute is None):
                        self.redistribute = MobileIp.Lmas.Lma.Redistribute()
                        self.redistribute.parent = self
                        self._children_name_map["redistribute"] = "redistribute"
                    return self.redistribute

                if (child_yang_name == "replay-protection"):
                    if (self.replay_protection is None):
                        self.replay_protection = MobileIp.Lmas.Lma.ReplayProtection()
                        self.replay_protection.parent = self
                        self._children_name_map["replay_protection"] = "replay-protection"
                    return self.replay_protection

                if (child_yang_name == "roles"):
                    if (self.roles is None):
                        self.roles = MobileIp.Lmas.Lma.Roles()
                        self.roles.parent = self
                        self._children_name_map["roles"] = "roles"
                    return self.roles

                if (child_yang_name == "services"):
                    if (self.services is None):
                        self.services = MobileIp.Lmas.Lma.Services()
                        self.services.parent = self
                        self._children_name_map["services"] = "services"
                    return self.services

                if (child_yang_name == "tunnel-attributes"):
                    if (self.tunnel_attributes is None):
                        self.tunnel_attributes = MobileIp.Lmas.Lma.TunnelAttributes()
                        self.tunnel_attributes.parent = self
                        self._children_name_map["tunnel_attributes"] = "tunnel-attributes"
                    return self.tunnel_attributes

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "aaa" or name == "binding-attributes" or name == "binding-revocation-attributes" or name == "dscp" or name == "heart-beat-attributes" or name == "hnp" or name == "lmaipv4-addresses" or name == "lmaipv6-addresses" or name == "mags" or name == "networks" or name == "rat-attributes" or name == "redistribute" or name == "replay-protection" or name == "roles" or name == "services" or name == "tunnel-attributes" or name == "lma-name" or name == "domain-name" or name == "ani" or name == "default-profile" or name == "dynamic" or name == "enforce" or name == "generate" or name == "interface" or name == "mobile-map" or name == "mobile-route-ad" or name == "multipath" or name == "pgw-subs-cont"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "lma-name"):
                    self.lma_name = value
                    self.lma_name.value_namespace = name_space
                    self.lma_name.value_namespace_prefix = name_space_prefix
                if(value_path == "domain-name"):
                    self.domain_name = value
                    self.domain_name.value_namespace = name_space
                    self.domain_name.value_namespace_prefix = name_space_prefix
                if(value_path == "ani"):
                    self.ani = value
                    self.ani.value_namespace = name_space
                    self.ani.value_namespace_prefix = name_space_prefix
                if(value_path == "default-profile"):
                    self.default_profile = value
                    self.default_profile.value_namespace = name_space
                    self.default_profile.value_namespace_prefix = name_space_prefix
                if(value_path == "dynamic"):
                    self.dynamic = value
                    self.dynamic.value_namespace = name_space
                    self.dynamic.value_namespace_prefix = name_space_prefix
                if(value_path == "enforce"):
                    self.enforce = value
                    self.enforce.value_namespace = name_space
                    self.enforce.value_namespace_prefix = name_space_prefix
                if(value_path == "generate"):
                    self.generate = value
                    self.generate.value_namespace = name_space
                    self.generate.value_namespace_prefix = name_space_prefix
                if(value_path == "interface"):
                    self.interface = value
                    self.interface.value_namespace = name_space
                    self.interface.value_namespace_prefix = name_space_prefix
                if(value_path == "mobile-map"):
                    self.mobile_map = value
                    self.mobile_map.value_namespace = name_space
                    self.mobile_map.value_namespace_prefix = name_space_prefix
                if(value_path == "mobile-route-ad"):
                    self.mobile_route_ad = value
                    self.mobile_route_ad.value_namespace = name_space
                    self.mobile_route_ad.value_namespace_prefix = name_space_prefix
                if(value_path == "multipath"):
                    self.multipath = value
                    self.multipath.value_namespace = name_space
                    self.multipath.value_namespace_prefix = name_space_prefix
                if(value_path == "pgw-subs-cont"):
                    self.pgw_subs_cont = value
                    self.pgw_subs_cont.value_namespace = name_space
                    self.pgw_subs_cont.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.lma:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.lma:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "lmas" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-mobileip-cfg:mobile-ip/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "lma"):
                for c in self.lma:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MobileIp.Lmas.Lma()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.lma.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "lma"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.domains is not None and self.domains.has_data()) or
            (self.lmas is not None and self.lmas.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.domains is not None and self.domains.has_operation()) or
            (self.lmas is not None and self.lmas.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ip-mobileip-cfg:mobile-ip" + path_buffer

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

        if (child_yang_name == "domains"):
            if (self.domains is None):
                self.domains = MobileIp.Domains()
                self.domains.parent = self
                self._children_name_map["domains"] = "domains"
            return self.domains

        if (child_yang_name == "lmas"):
            if (self.lmas is None):
                self.lmas = MobileIp.Lmas()
                self.lmas.parent = self
                self._children_name_map["lmas"] = "lmas"
            return self.lmas

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "domains" or name == "lmas"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = MobileIp()
        return self._top_entity


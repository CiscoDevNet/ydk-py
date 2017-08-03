""" Cisco_IOS_XR_icpe_infra_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR icpe\-infra package configuration.

This module contains definitions
for the following management objects\:
  nv\-satellite\-global\: nV Satellite Global configuration
  nv\-satellites\: nv satellites

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-rgmgr\-cfg,
modules with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class NvSatelliteGlobal(Entity):
    """
    nV Satellite Global configuration
    
    .. attribute:: chassis_mac
    
    	Chassis MAC address
    	**type**\:   :py:class:`ChassisMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatelliteGlobal.ChassisMac>`
    
    

    """

    _prefix = 'icpe-infra-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(NvSatelliteGlobal, self).__init__()
        self._top_entity = None

        self.yang_name = "nv-satellite-global"
        self.yang_parent_name = "Cisco-IOS-XR-icpe-infra-cfg"

        self.chassis_mac = NvSatelliteGlobal.ChassisMac()
        self.chassis_mac.parent = self
        self._children_name_map["chassis_mac"] = "chassis-mac"
        self._children_yang_names.add("chassis-mac")


    class ChassisMac(Entity):
        """
        Chassis MAC address
        
        .. attribute:: mac1
        
        	First two bytes of MAC address
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        	**units**\: byte
        
        .. attribute:: mac2
        
        	Second two bytes of MAC address
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        	**units**\: byte
        
        .. attribute:: mac3
        
        	Third two bytes of MAC address
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        	**units**\: byte
        
        

        """

        _prefix = 'icpe-infra-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatelliteGlobal.ChassisMac, self).__init__()

            self.yang_name = "chassis-mac"
            self.yang_parent_name = "nv-satellite-global"

            self.mac1 = YLeaf(YType.uint32, "mac1")

            self.mac2 = YLeaf(YType.uint32, "mac2")

            self.mac3 = YLeaf(YType.uint32, "mac3")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("mac1",
                            "mac2",
                            "mac3") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NvSatelliteGlobal.ChassisMac, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NvSatelliteGlobal.ChassisMac, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.mac1.is_set or
                self.mac2.is_set or
                self.mac3.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.mac1.yfilter != YFilter.not_set or
                self.mac2.yfilter != YFilter.not_set or
                self.mac3.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "chassis-mac" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-icpe-infra-cfg:nv-satellite-global/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.mac1.is_set or self.mac1.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mac1.get_name_leafdata())
            if (self.mac2.is_set or self.mac2.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mac2.get_name_leafdata())
            if (self.mac3.is_set or self.mac3.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mac3.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mac1" or name == "mac2" or name == "mac3"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "mac1"):
                self.mac1 = value
                self.mac1.value_namespace = name_space
                self.mac1.value_namespace_prefix = name_space_prefix
            if(value_path == "mac2"):
                self.mac2 = value
                self.mac2.value_namespace = name_space
                self.mac2.value_namespace_prefix = name_space_prefix
            if(value_path == "mac3"):
                self.mac3 = value
                self.mac3.value_namespace = name_space
                self.mac3.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.chassis_mac is not None and self.chassis_mac.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.chassis_mac is not None and self.chassis_mac.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-icpe-infra-cfg:nv-satellite-global" + path_buffer

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

        if (child_yang_name == "chassis-mac"):
            if (self.chassis_mac is None):
                self.chassis_mac = NvSatelliteGlobal.ChassisMac()
                self.chassis_mac.parent = self
                self._children_name_map["chassis_mac"] = "chassis-mac"
            return self.chassis_mac

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "chassis-mac"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = NvSatelliteGlobal()
        return self._top_entity

class NvSatellites(Entity):
    """
    nv satellites
    
    .. attribute:: nv_satellite
    
    	Satellite Configuration
    	**type**\: list of    :py:class:`NvSatellite <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite>`
    
    

    """

    _prefix = 'icpe-infra-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(NvSatellites, self).__init__()
        self._top_entity = None

        self.yang_name = "nv-satellites"
        self.yang_parent_name = "Cisco-IOS-XR-icpe-infra-cfg"

        self.nv_satellite = YList(self)

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
                    super(NvSatellites, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(NvSatellites, self).__setattr__(name, value)


    class NvSatellite(Entity):
        """
        Satellite Configuration
        
        .. attribute:: satellite_id  <key>
        
        	Satellite ID
        	**type**\:  int
        
        	**range:** 100..65534
        
        .. attribute:: candidate_fabric_ports
        
        	Enable interfaces on the satellite to be used as fabric ports table
        	**type**\:   :py:class:`CandidateFabricPorts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite.CandidateFabricPorts>`
        
        .. attribute:: connection_info
        
        	Satellite User
        	**type**\:   :py:class:`ConnectionInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite.ConnectionInfo>`
        
        .. attribute:: delayed_switchback
        
        	Timer (in seconds) for delaying switchback in a dual home setup
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: second
        
        .. attribute:: description
        
        	Satellite Description
        	**type**\:  str
        
        .. attribute:: device_name
        
        	Satellite Name
        	**type**\:  str
        
        .. attribute:: disc_timeout
        
        	Discovery timeout for the satellite
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: enable
        
        	Enable
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: ip_address
        
        	Satellite IP Address
        	**type**\: one of the below types:
        
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        
        ----
        	**type**\:  str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        
        ----
        .. attribute:: redundancy
        
        	Redundancy submode
        	**type**\:   :py:class:`Redundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite.Redundancy>`
        
        .. attribute:: secret
        
        	Encrypted password for the Satellite
        	**type**\:  str
        
        	**pattern:** (!.+)\|([^!].+)
        
        .. attribute:: serial_number
        
        	Satellite Serial Number
        	**type**\:  str
        
        .. attribute:: timeout_warning
        
        	Discovery timeout warning for the satellite
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: type
        
        	Satellite Type
        	**type**\:  str
        
        .. attribute:: upgrade_on_connect
        
        	Satellite auto\-upgrade capability
        	**type**\:   :py:class:`UpgradeOnConnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite.UpgradeOnConnect>`
        
        .. attribute:: vrf
        
        	VRF for Satellite IP Address
        	**type**\:  str
        
        

        """

        _prefix = 'icpe-infra-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(NvSatellites.NvSatellite, self).__init__()

            self.yang_name = "nv-satellite"
            self.yang_parent_name = "nv-satellites"

            self.satellite_id = YLeaf(YType.uint32, "satellite-id")

            self.delayed_switchback = YLeaf(YType.uint32, "delayed-switchback")

            self.description = YLeaf(YType.str, "description")

            self.device_name = YLeaf(YType.str, "device-name")

            self.disc_timeout = YLeaf(YType.uint32, "disc-timeout")

            self.enable = YLeaf(YType.empty, "enable")

            self.ip_address = YLeaf(YType.str, "ip-address")

            self.secret = YLeaf(YType.str, "secret")

            self.serial_number = YLeaf(YType.str, "serial-number")

            self.timeout_warning = YLeaf(YType.uint32, "timeout-warning")

            self.type = YLeaf(YType.str, "type")

            self.vrf = YLeaf(YType.str, "vrf")

            self.candidate_fabric_ports = NvSatellites.NvSatellite.CandidateFabricPorts()
            self.candidate_fabric_ports.parent = self
            self._children_name_map["candidate_fabric_ports"] = "candidate-fabric-ports"
            self._children_yang_names.add("candidate-fabric-ports")

            self.connection_info = NvSatellites.NvSatellite.ConnectionInfo()
            self.connection_info.parent = self
            self._children_name_map["connection_info"] = "connection-info"
            self._children_yang_names.add("connection-info")

            self.redundancy = NvSatellites.NvSatellite.Redundancy()
            self.redundancy.parent = self
            self._children_name_map["redundancy"] = "redundancy"
            self._children_yang_names.add("redundancy")

            self.upgrade_on_connect = NvSatellites.NvSatellite.UpgradeOnConnect()
            self.upgrade_on_connect.parent = self
            self._children_name_map["upgrade_on_connect"] = "upgrade-on-connect"
            self._children_yang_names.add("upgrade-on-connect")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("satellite_id",
                            "delayed_switchback",
                            "description",
                            "device_name",
                            "disc_timeout",
                            "enable",
                            "ip_address",
                            "secret",
                            "serial_number",
                            "timeout_warning",
                            "type",
                            "vrf") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NvSatellites.NvSatellite, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NvSatellites.NvSatellite, self).__setattr__(name, value)


        class UpgradeOnConnect(Entity):
            """
            Satellite auto\-upgrade capability
            
            .. attribute:: connect_type
            
            	When to upgrade the satellite
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: reference
            
            	Reference name
            	**type**\:  str
            
            

            """

            _prefix = 'icpe-infra-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellites.NvSatellite.UpgradeOnConnect, self).__init__()

                self.yang_name = "upgrade-on-connect"
                self.yang_parent_name = "nv-satellite"

                self.connect_type = YLeaf(YType.uint32, "connect-type")

                self.reference = YLeaf(YType.str, "reference")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("connect_type",
                                "reference") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NvSatellites.NvSatellite.UpgradeOnConnect, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NvSatellites.NvSatellite.UpgradeOnConnect, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.connect_type.is_set or
                    self.reference.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.connect_type.yfilter != YFilter.not_set or
                    self.reference.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "upgrade-on-connect" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.connect_type.is_set or self.connect_type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.connect_type.get_name_leafdata())
                if (self.reference.is_set or self.reference.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.reference.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "connect-type" or name == "reference"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "connect-type"):
                    self.connect_type = value
                    self.connect_type.value_namespace = name_space
                    self.connect_type.value_namespace_prefix = name_space_prefix
                if(value_path == "reference"):
                    self.reference = value
                    self.reference.value_namespace = name_space
                    self.reference.value_namespace_prefix = name_space_prefix


        class CandidateFabricPorts(Entity):
            """
            Enable interfaces on the satellite to be used
            as fabric ports table
            
            .. attribute:: candidate_fabric_port
            
            	Enable interfaces on the satellite to be used as fabric ports
            	**type**\: list of    :py:class:`CandidateFabricPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg.NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort>`
            
            

            """

            _prefix = 'icpe-infra-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellites.NvSatellite.CandidateFabricPorts, self).__init__()

                self.yang_name = "candidate-fabric-ports"
                self.yang_parent_name = "nv-satellite"

                self.candidate_fabric_port = YList(self)

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
                            super(NvSatellites.NvSatellite.CandidateFabricPorts, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NvSatellites.NvSatellite.CandidateFabricPorts, self).__setattr__(name, value)


            class CandidateFabricPort(Entity):
                """
                Enable interfaces on the satellite to be used
                as fabric ports
                
                .. attribute:: port_type  <key>
                
                	Port type
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: slot  <key>
                
                	Slot
                	**type**\:  int
                
                	**range:** 0..8
                
                .. attribute:: sub_slot  <key>
                
                	Sub slot
                	**type**\:  int
                
                	**range:** 0..8
                
                .. attribute:: port_range
                
                	Port range
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'icpe-infra-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort, self).__init__()

                    self.yang_name = "candidate-fabric-port"
                    self.yang_parent_name = "candidate-fabric-ports"

                    self.port_type = YLeaf(YType.str, "port-type")

                    self.slot = YLeaf(YType.uint32, "slot")

                    self.sub_slot = YLeaf(YType.uint32, "sub-slot")

                    self.port_range = YLeaf(YType.str, "port-range")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("port_type",
                                    "slot",
                                    "sub_slot",
                                    "port_range") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.port_type.is_set or
                        self.slot.is_set or
                        self.sub_slot.is_set or
                        self.port_range.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.port_type.yfilter != YFilter.not_set or
                        self.slot.yfilter != YFilter.not_set or
                        self.sub_slot.yfilter != YFilter.not_set or
                        self.port_range.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "candidate-fabric-port" + "[port-type='" + self.port_type.get() + "']" + "[slot='" + self.slot.get() + "']" + "[sub-slot='" + self.sub_slot.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.port_type.is_set or self.port_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port_type.get_name_leafdata())
                    if (self.slot.is_set or self.slot.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.slot.get_name_leafdata())
                    if (self.sub_slot.is_set or self.sub_slot.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sub_slot.get_name_leafdata())
                    if (self.port_range.is_set or self.port_range.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port_range.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "port-type" or name == "slot" or name == "sub-slot" or name == "port-range"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "port-type"):
                        self.port_type = value
                        self.port_type.value_namespace = name_space
                        self.port_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "slot"):
                        self.slot = value
                        self.slot.value_namespace = name_space
                        self.slot.value_namespace_prefix = name_space_prefix
                    if(value_path == "sub-slot"):
                        self.sub_slot = value
                        self.sub_slot.value_namespace = name_space
                        self.sub_slot.value_namespace_prefix = name_space_prefix
                    if(value_path == "port-range"):
                        self.port_range = value
                        self.port_range.value_namespace = name_space
                        self.port_range.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.candidate_fabric_port:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.candidate_fabric_port:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "candidate-fabric-ports" + path_buffer

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

                if (child_yang_name == "candidate-fabric-port"):
                    for c in self.candidate_fabric_port:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.candidate_fabric_port.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "candidate-fabric-port"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class ConnectionInfo(Entity):
            """
            Satellite User
            
            .. attribute:: password
            
            	Encrypted password for the user
            	**type**\:  str
            
            	**pattern:** (!.+)\|([^!].+)
            
            .. attribute:: username
            
            	Satellite Username
            	**type**\:  str
            
            

            """

            _prefix = 'icpe-infra-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellites.NvSatellite.ConnectionInfo, self).__init__()

                self.yang_name = "connection-info"
                self.yang_parent_name = "nv-satellite"

                self.password = YLeaf(YType.str, "password")

                self.username = YLeaf(YType.str, "username")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("password",
                                "username") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NvSatellites.NvSatellite.ConnectionInfo, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NvSatellites.NvSatellite.ConnectionInfo, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.password.is_set or
                    self.username.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.password.yfilter != YFilter.not_set or
                    self.username.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "connection-info" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.password.is_set or self.password.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.password.get_name_leafdata())
                if (self.username.is_set or self.username.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.username.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "password" or name == "username"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "password"):
                    self.password = value
                    self.password.value_namespace = name_space
                    self.password.value_namespace_prefix = name_space_prefix
                if(value_path == "username"):
                    self.username = value
                    self.username.value_namespace = name_space
                    self.username.value_namespace_prefix = name_space_prefix


        class Redundancy(Entity):
            """
            Redundancy submode
            
            .. attribute:: host_priority
            
            	Priority for this host for the given satellite
            	**type**\:  int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'icpe-infra-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(NvSatellites.NvSatellite.Redundancy, self).__init__()

                self.yang_name = "redundancy"
                self.yang_parent_name = "nv-satellite"

                self.host_priority = YLeaf(YType.uint32, "host-priority")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("host_priority") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NvSatellites.NvSatellite.Redundancy, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NvSatellites.NvSatellite.Redundancy, self).__setattr__(name, value)

            def has_data(self):
                return self.host_priority.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.host_priority.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "redundancy" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.host_priority.is_set or self.host_priority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.host_priority.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "host-priority"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "host-priority"):
                    self.host_priority = value
                    self.host_priority.value_namespace = name_space
                    self.host_priority.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.satellite_id.is_set or
                self.delayed_switchback.is_set or
                self.description.is_set or
                self.device_name.is_set or
                self.disc_timeout.is_set or
                self.enable.is_set or
                self.ip_address.is_set or
                self.secret.is_set or
                self.serial_number.is_set or
                self.timeout_warning.is_set or
                self.type.is_set or
                self.vrf.is_set or
                (self.candidate_fabric_ports is not None and self.candidate_fabric_ports.has_data()) or
                (self.connection_info is not None and self.connection_info.has_data()) or
                (self.redundancy is not None and self.redundancy.has_data()) or
                (self.upgrade_on_connect is not None and self.upgrade_on_connect.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.satellite_id.yfilter != YFilter.not_set or
                self.delayed_switchback.yfilter != YFilter.not_set or
                self.description.yfilter != YFilter.not_set or
                self.device_name.yfilter != YFilter.not_set or
                self.disc_timeout.yfilter != YFilter.not_set or
                self.enable.yfilter != YFilter.not_set or
                self.ip_address.yfilter != YFilter.not_set or
                self.secret.yfilter != YFilter.not_set or
                self.serial_number.yfilter != YFilter.not_set or
                self.timeout_warning.yfilter != YFilter.not_set or
                self.type.yfilter != YFilter.not_set or
                self.vrf.yfilter != YFilter.not_set or
                (self.candidate_fabric_ports is not None and self.candidate_fabric_ports.has_operation()) or
                (self.connection_info is not None and self.connection_info.has_operation()) or
                (self.redundancy is not None and self.redundancy.has_operation()) or
                (self.upgrade_on_connect is not None and self.upgrade_on_connect.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nv-satellite" + "[satellite-id='" + self.satellite_id.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-icpe-infra-cfg:nv-satellites/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.satellite_id.is_set or self.satellite_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.satellite_id.get_name_leafdata())
            if (self.delayed_switchback.is_set or self.delayed_switchback.yfilter != YFilter.not_set):
                leaf_name_data.append(self.delayed_switchback.get_name_leafdata())
            if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                leaf_name_data.append(self.description.get_name_leafdata())
            if (self.device_name.is_set or self.device_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.device_name.get_name_leafdata())
            if (self.disc_timeout.is_set or self.disc_timeout.yfilter != YFilter.not_set):
                leaf_name_data.append(self.disc_timeout.get_name_leafdata())
            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enable.get_name_leafdata())
            if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ip_address.get_name_leafdata())
            if (self.secret.is_set or self.secret.yfilter != YFilter.not_set):
                leaf_name_data.append(self.secret.get_name_leafdata())
            if (self.serial_number.is_set or self.serial_number.yfilter != YFilter.not_set):
                leaf_name_data.append(self.serial_number.get_name_leafdata())
            if (self.timeout_warning.is_set or self.timeout_warning.yfilter != YFilter.not_set):
                leaf_name_data.append(self.timeout_warning.get_name_leafdata())
            if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                leaf_name_data.append(self.type.get_name_leafdata())
            if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vrf.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "candidate-fabric-ports"):
                if (self.candidate_fabric_ports is None):
                    self.candidate_fabric_ports = NvSatellites.NvSatellite.CandidateFabricPorts()
                    self.candidate_fabric_ports.parent = self
                    self._children_name_map["candidate_fabric_ports"] = "candidate-fabric-ports"
                return self.candidate_fabric_ports

            if (child_yang_name == "connection-info"):
                if (self.connection_info is None):
                    self.connection_info = NvSatellites.NvSatellite.ConnectionInfo()
                    self.connection_info.parent = self
                    self._children_name_map["connection_info"] = "connection-info"
                return self.connection_info

            if (child_yang_name == "redundancy"):
                if (self.redundancy is None):
                    self.redundancy = NvSatellites.NvSatellite.Redundancy()
                    self.redundancy.parent = self
                    self._children_name_map["redundancy"] = "redundancy"
                return self.redundancy

            if (child_yang_name == "upgrade-on-connect"):
                if (self.upgrade_on_connect is None):
                    self.upgrade_on_connect = NvSatellites.NvSatellite.UpgradeOnConnect()
                    self.upgrade_on_connect.parent = self
                    self._children_name_map["upgrade_on_connect"] = "upgrade-on-connect"
                return self.upgrade_on_connect

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "candidate-fabric-ports" or name == "connection-info" or name == "redundancy" or name == "upgrade-on-connect" or name == "satellite-id" or name == "delayed-switchback" or name == "description" or name == "device-name" or name == "disc-timeout" or name == "enable" or name == "ip-address" or name == "secret" or name == "serial-number" or name == "timeout-warning" or name == "type" or name == "vrf"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "satellite-id"):
                self.satellite_id = value
                self.satellite_id.value_namespace = name_space
                self.satellite_id.value_namespace_prefix = name_space_prefix
            if(value_path == "delayed-switchback"):
                self.delayed_switchback = value
                self.delayed_switchback.value_namespace = name_space
                self.delayed_switchback.value_namespace_prefix = name_space_prefix
            if(value_path == "description"):
                self.description = value
                self.description.value_namespace = name_space
                self.description.value_namespace_prefix = name_space_prefix
            if(value_path == "device-name"):
                self.device_name = value
                self.device_name.value_namespace = name_space
                self.device_name.value_namespace_prefix = name_space_prefix
            if(value_path == "disc-timeout"):
                self.disc_timeout = value
                self.disc_timeout.value_namespace = name_space
                self.disc_timeout.value_namespace_prefix = name_space_prefix
            if(value_path == "enable"):
                self.enable = value
                self.enable.value_namespace = name_space
                self.enable.value_namespace_prefix = name_space_prefix
            if(value_path == "ip-address"):
                self.ip_address = value
                self.ip_address.value_namespace = name_space
                self.ip_address.value_namespace_prefix = name_space_prefix
            if(value_path == "secret"):
                self.secret = value
                self.secret.value_namespace = name_space
                self.secret.value_namespace_prefix = name_space_prefix
            if(value_path == "serial-number"):
                self.serial_number = value
                self.serial_number.value_namespace = name_space
                self.serial_number.value_namespace_prefix = name_space_prefix
            if(value_path == "timeout-warning"):
                self.timeout_warning = value
                self.timeout_warning.value_namespace = name_space
                self.timeout_warning.value_namespace_prefix = name_space_prefix
            if(value_path == "type"):
                self.type = value
                self.type.value_namespace = name_space
                self.type.value_namespace_prefix = name_space_prefix
            if(value_path == "vrf"):
                self.vrf = value
                self.vrf.value_namespace = name_space
                self.vrf.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.nv_satellite:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.nv_satellite:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-icpe-infra-cfg:nv-satellites" + path_buffer

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

        if (child_yang_name == "nv-satellite"):
            for c in self.nv_satellite:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = NvSatellites.NvSatellite()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.nv_satellite.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nv-satellite"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = NvSatellites()
        return self._top_entity


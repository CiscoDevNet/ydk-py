""" Cisco_IOS_XR_ip_sbfd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-sbfd package operational data.

This module contains definitions
for the following management objects\:
  sbfd\: Seamless BFD (S\-BFD) operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BfdAfId(Enum):
    """
    BfdAfId

    Bfd af id

    .. data:: bfd_af_id_none = 0

    	No Address

    .. data:: bfd_af_id_ipv4 = 2

    	IPv4 AFI

    .. data:: bfd_af_id_ipv6 = 10

    	IPv6 AFI

    """

    bfd_af_id_none = Enum.YLeaf(0, "bfd-af-id-none")

    bfd_af_id_ipv4 = Enum.YLeaf(2, "bfd-af-id-ipv4")

    bfd_af_id_ipv6 = Enum.YLeaf(10, "bfd-af-id-ipv6")


class SbfdAddressFamily(Enum):
    """
    SbfdAddressFamily

    Sbfd address family

    .. data:: ipv4 = 1

    	ipv4

    .. data:: ipv6 = 2

    	ipv6

    """

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")



class Sbfd(Entity):
    """
    Seamless BFD (S\-BFD) operational data
    
    .. attribute:: target_identifier
    
    	Target\-identifier information
    	**type**\:   :py:class:`TargetIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier>`
    
    

    """

    _prefix = 'ip-sbfd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Sbfd, self).__init__()
        self._top_entity = None

        self.yang_name = "sbfd"
        self.yang_parent_name = "Cisco-IOS-XR-ip-sbfd-oper"

        self.target_identifier = Sbfd.TargetIdentifier()
        self.target_identifier.parent = self
        self._children_name_map["target_identifier"] = "target-identifier"
        self._children_yang_names.add("target-identifier")


    class TargetIdentifier(Entity):
        """
        Target\-identifier information
        
        .. attribute:: local_vrfs
        
        	SBFD local discriminator  data
        	**type**\:   :py:class:`LocalVrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier.LocalVrfs>`
        
        .. attribute:: remote_vrfs
        
        	SBFD remote discriminator data
        	**type**\:   :py:class:`RemoteVrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier.RemoteVrfs>`
        
        

        """

        _prefix = 'ip-sbfd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Sbfd.TargetIdentifier, self).__init__()

            self.yang_name = "target-identifier"
            self.yang_parent_name = "sbfd"

            self.local_vrfs = Sbfd.TargetIdentifier.LocalVrfs()
            self.local_vrfs.parent = self
            self._children_name_map["local_vrfs"] = "local-vrfs"
            self._children_yang_names.add("local-vrfs")

            self.remote_vrfs = Sbfd.TargetIdentifier.RemoteVrfs()
            self.remote_vrfs.parent = self
            self._children_name_map["remote_vrfs"] = "remote-vrfs"
            self._children_yang_names.add("remote-vrfs")


        class RemoteVrfs(Entity):
            """
            SBFD remote discriminator data
            
            .. attribute:: remote_vrf
            
            	Table of remote discriminator data per VRF
            	**type**\: list of    :py:class:`RemoteVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf>`
            
            

            """

            _prefix = 'ip-sbfd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Sbfd.TargetIdentifier.RemoteVrfs, self).__init__()

                self.yang_name = "remote-vrfs"
                self.yang_parent_name = "target-identifier"

                self.remote_vrf = YList(self)

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
                            super(Sbfd.TargetIdentifier.RemoteVrfs, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Sbfd.TargetIdentifier.RemoteVrfs, self).__setattr__(name, value)


            class RemoteVrf(Entity):
                """
                Table of remote discriminator data per VRF
                
                .. attribute:: vrf_name  <key>
                
                	VRF name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: remote_discriminator
                
                	SBFD remote discriminator 
                	**type**\: list of    :py:class:`RemoteDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator>`
                
                

                """

                _prefix = 'ip-sbfd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf, self).__init__()

                    self.yang_name = "remote-vrf"
                    self.yang_parent_name = "remote-vrfs"

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.remote_discriminator = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("vrf_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf, self).__setattr__(name, value)


                class RemoteDiscriminator(Entity):
                    """
                    SBFD remote discriminator 
                    
                    .. attribute:: address
                    
                    	Address
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: discr
                    
                    	Remote discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: discr_src
                    
                    	Discriminator source name
                    	**type**\:  str
                    
                    .. attribute:: ip_address
                    
                    	IP address
                    	**type**\:   :py:class:`IpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator.IpAddress>`
                    
                    .. attribute:: remote_discriminator
                    
                    	Remote Discriminator
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: status
                    
                    	Status
                    	**type**\:  str
                    
                    .. attribute:: tid_type
                    
                    	Target identifier for sbfd
                    	**type**\:   :py:class:`SbfdAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.SbfdAddressFamily>`
                    
                    .. attribute:: vrf_name
                    
                    	VRF Name 
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: vrf_name_xr
                    
                    	VRF Name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ip-sbfd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator, self).__init__()

                        self.yang_name = "remote-discriminator"
                        self.yang_parent_name = "remote-vrf"

                        self.address = YLeaf(YType.str, "address")

                        self.discr = YLeaf(YType.uint32, "discr")

                        self.discr_src = YLeaf(YType.str, "discr-src")

                        self.remote_discriminator = YLeaf(YType.int32, "remote-discriminator")

                        self.status = YLeaf(YType.str, "status")

                        self.tid_type = YLeaf(YType.enumeration, "tid-type")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.vrf_name_xr = YLeaf(YType.str, "vrf-name-xr")

                        self.ip_address = Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator.IpAddress()
                        self.ip_address.parent = self
                        self._children_name_map["ip_address"] = "ip-address"
                        self._children_yang_names.add("ip-address")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("address",
                                        "discr",
                                        "discr_src",
                                        "remote_discriminator",
                                        "status",
                                        "tid_type",
                                        "vrf_name",
                                        "vrf_name_xr") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator, self).__setattr__(name, value)


                    class IpAddress(Entity):
                        """
                        IP address
                        
                        .. attribute:: afi
                        
                        	AFI
                        	**type**\:   :py:class:`BfdAfId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.BfdAfId>`
                        
                        .. attribute:: dummy
                        
                        	No Address
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: ipv4
                        
                        	IPv4 address type
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6
                        
                        	IPv6 address type
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-sbfd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator.IpAddress, self).__init__()

                            self.yang_name = "ip-address"
                            self.yang_parent_name = "remote-discriminator"

                            self.afi = YLeaf(YType.enumeration, "afi")

                            self.dummy = YLeaf(YType.uint8, "dummy")

                            self.ipv4 = YLeaf(YType.str, "ipv4")

                            self.ipv6 = YLeaf(YType.str, "ipv6")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("afi",
                                            "dummy",
                                            "ipv4",
                                            "ipv6") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator.IpAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator.IpAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.afi.is_set or
                                self.dummy.is_set or
                                self.ipv4.is_set or
                                self.ipv6.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.afi.yfilter != YFilter.not_set or
                                self.dummy.yfilter != YFilter.not_set or
                                self.ipv4.yfilter != YFilter.not_set or
                                self.ipv6.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ip-address" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.afi.is_set or self.afi.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.afi.get_name_leafdata())
                            if (self.dummy.is_set or self.dummy.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dummy.get_name_leafdata())
                            if (self.ipv4.is_set or self.ipv4.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4.get_name_leafdata())
                            if (self.ipv6.is_set or self.ipv6.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "afi" or name == "dummy" or name == "ipv4" or name == "ipv6"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "afi"):
                                self.afi = value
                                self.afi.value_namespace = name_space
                                self.afi.value_namespace_prefix = name_space_prefix
                            if(value_path == "dummy"):
                                self.dummy = value
                                self.dummy.value_namespace = name_space
                                self.dummy.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv4"):
                                self.ipv4 = value
                                self.ipv4.value_namespace = name_space
                                self.ipv4.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv6"):
                                self.ipv6 = value
                                self.ipv6.value_namespace = name_space
                                self.ipv6.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.address.is_set or
                            self.discr.is_set or
                            self.discr_src.is_set or
                            self.remote_discriminator.is_set or
                            self.status.is_set or
                            self.tid_type.is_set or
                            self.vrf_name.is_set or
                            self.vrf_name_xr.is_set or
                            (self.ip_address is not None and self.ip_address.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set or
                            self.discr.yfilter != YFilter.not_set or
                            self.discr_src.yfilter != YFilter.not_set or
                            self.remote_discriminator.yfilter != YFilter.not_set or
                            self.status.yfilter != YFilter.not_set or
                            self.tid_type.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set or
                            self.vrf_name_xr.yfilter != YFilter.not_set or
                            (self.ip_address is not None and self.ip_address.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "remote-discriminator" + path_buffer

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
                        if (self.discr.is_set or self.discr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.discr.get_name_leafdata())
                        if (self.discr_src.is_set or self.discr_src.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.discr_src.get_name_leafdata())
                        if (self.remote_discriminator.is_set or self.remote_discriminator.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.remote_discriminator.get_name_leafdata())
                        if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.status.get_name_leafdata())
                        if (self.tid_type.is_set or self.tid_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tid_type.get_name_leafdata())
                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name.get_name_leafdata())
                        if (self.vrf_name_xr.is_set or self.vrf_name_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name_xr.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "ip-address"):
                            if (self.ip_address is None):
                                self.ip_address = Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator.IpAddress()
                                self.ip_address.parent = self
                                self._children_name_map["ip_address"] = "ip-address"
                            return self.ip_address

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ip-address" or name == "address" or name == "discr" or name == "discr-src" or name == "remote-discriminator" or name == "status" or name == "tid-type" or name == "vrf-name" or name == "vrf-name-xr"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address"):
                            self.address = value
                            self.address.value_namespace = name_space
                            self.address.value_namespace_prefix = name_space_prefix
                        if(value_path == "discr"):
                            self.discr = value
                            self.discr.value_namespace = name_space
                            self.discr.value_namespace_prefix = name_space_prefix
                        if(value_path == "discr-src"):
                            self.discr_src = value
                            self.discr_src.value_namespace = name_space
                            self.discr_src.value_namespace_prefix = name_space_prefix
                        if(value_path == "remote-discriminator"):
                            self.remote_discriminator = value
                            self.remote_discriminator.value_namespace = name_space
                            self.remote_discriminator.value_namespace_prefix = name_space_prefix
                        if(value_path == "status"):
                            self.status = value
                            self.status.value_namespace = name_space
                            self.status.value_namespace_prefix = name_space_prefix
                        if(value_path == "tid-type"):
                            self.tid_type = value
                            self.tid_type.value_namespace = name_space
                            self.tid_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf-name-xr"):
                            self.vrf_name_xr = value
                            self.vrf_name_xr.value_namespace = name_space
                            self.vrf_name_xr.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.remote_discriminator:
                        if (c.has_data()):
                            return True
                    return self.vrf_name.is_set

                def has_operation(self):
                    for c in self.remote_discriminator:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.vrf_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "remote-vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-sbfd-oper:sbfd/target-identifier/remote-vrfs/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "remote-discriminator"):
                        for c in self.remote_discriminator:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf.RemoteDiscriminator()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.remote_discriminator.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "remote-discriminator" or name == "vrf-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "vrf-name"):
                        self.vrf_name = value
                        self.vrf_name.value_namespace = name_space
                        self.vrf_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.remote_vrf:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.remote_vrf:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "remote-vrfs" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-sbfd-oper:sbfd/target-identifier/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "remote-vrf"):
                    for c in self.remote_vrf:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Sbfd.TargetIdentifier.RemoteVrfs.RemoteVrf()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.remote_vrf.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "remote-vrf"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class LocalVrfs(Entity):
            """
            SBFD local discriminator  data
            
            .. attribute:: local_vrf
            
            	Table of local discriminator data per VRF
            	**type**\: list of    :py:class:`LocalVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier.LocalVrfs.LocalVrf>`
            
            

            """

            _prefix = 'ip-sbfd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Sbfd.TargetIdentifier.LocalVrfs, self).__init__()

                self.yang_name = "local-vrfs"
                self.yang_parent_name = "target-identifier"

                self.local_vrf = YList(self)

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
                            super(Sbfd.TargetIdentifier.LocalVrfs, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Sbfd.TargetIdentifier.LocalVrfs, self).__setattr__(name, value)


            class LocalVrf(Entity):
                """
                Table of local discriminator data per VRF
                
                .. attribute:: vrf_name  <key>
                
                	VRF name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: local_discriminator
                
                	SBFD local discriminator 
                	**type**\: list of    :py:class:`LocalDiscriminator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_oper.Sbfd.TargetIdentifier.LocalVrfs.LocalVrf.LocalDiscriminator>`
                
                

                """

                _prefix = 'ip-sbfd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Sbfd.TargetIdentifier.LocalVrfs.LocalVrf, self).__init__()

                    self.yang_name = "local-vrf"
                    self.yang_parent_name = "local-vrfs"

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.local_discriminator = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("vrf_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Sbfd.TargetIdentifier.LocalVrfs.LocalVrf, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Sbfd.TargetIdentifier.LocalVrfs.LocalVrf, self).__setattr__(name, value)


                class LocalDiscriminator(Entity):
                    """
                    SBFD local discriminator 
                    
                    .. attribute:: discr
                    
                    	Local discriminator
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: discr_src
                    
                    	Discriminator source name
                    	**type**\:  str
                    
                    .. attribute:: flags
                    
                    	MODE name
                    	**type**\:  str
                    
                    .. attribute:: local_discriminator
                    
                    	Local discriminator
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: status
                    
                    	Status
                    	**type**\:  str
                    
                    .. attribute:: vrf_name
                    
                    	VRF Name 
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: vrf_name_xr
                    
                    	VRF Name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'ip-sbfd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Sbfd.TargetIdentifier.LocalVrfs.LocalVrf.LocalDiscriminator, self).__init__()

                        self.yang_name = "local-discriminator"
                        self.yang_parent_name = "local-vrf"

                        self.discr = YLeaf(YType.uint32, "discr")

                        self.discr_src = YLeaf(YType.str, "discr-src")

                        self.flags = YLeaf(YType.str, "flags")

                        self.local_discriminator = YLeaf(YType.int32, "local-discriminator")

                        self.status = YLeaf(YType.str, "status")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.vrf_name_xr = YLeaf(YType.str, "vrf-name-xr")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("discr",
                                        "discr_src",
                                        "flags",
                                        "local_discriminator",
                                        "status",
                                        "vrf_name",
                                        "vrf_name_xr") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Sbfd.TargetIdentifier.LocalVrfs.LocalVrf.LocalDiscriminator, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Sbfd.TargetIdentifier.LocalVrfs.LocalVrf.LocalDiscriminator, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.discr.is_set or
                            self.discr_src.is_set or
                            self.flags.is_set or
                            self.local_discriminator.is_set or
                            self.status.is_set or
                            self.vrf_name.is_set or
                            self.vrf_name_xr.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.discr.yfilter != YFilter.not_set or
                            self.discr_src.yfilter != YFilter.not_set or
                            self.flags.yfilter != YFilter.not_set or
                            self.local_discriminator.yfilter != YFilter.not_set or
                            self.status.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set or
                            self.vrf_name_xr.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "local-discriminator" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.discr.is_set or self.discr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.discr.get_name_leafdata())
                        if (self.discr_src.is_set or self.discr_src.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.discr_src.get_name_leafdata())
                        if (self.flags.is_set or self.flags.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flags.get_name_leafdata())
                        if (self.local_discriminator.is_set or self.local_discriminator.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_discriminator.get_name_leafdata())
                        if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.status.get_name_leafdata())
                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name.get_name_leafdata())
                        if (self.vrf_name_xr.is_set or self.vrf_name_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name_xr.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "discr" or name == "discr-src" or name == "flags" or name == "local-discriminator" or name == "status" or name == "vrf-name" or name == "vrf-name-xr"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "discr"):
                            self.discr = value
                            self.discr.value_namespace = name_space
                            self.discr.value_namespace_prefix = name_space_prefix
                        if(value_path == "discr-src"):
                            self.discr_src = value
                            self.discr_src.value_namespace = name_space
                            self.discr_src.value_namespace_prefix = name_space_prefix
                        if(value_path == "flags"):
                            self.flags = value
                            self.flags.value_namespace = name_space
                            self.flags.value_namespace_prefix = name_space_prefix
                        if(value_path == "local-discriminator"):
                            self.local_discriminator = value
                            self.local_discriminator.value_namespace = name_space
                            self.local_discriminator.value_namespace_prefix = name_space_prefix
                        if(value_path == "status"):
                            self.status = value
                            self.status.value_namespace = name_space
                            self.status.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf-name-xr"):
                            self.vrf_name_xr = value
                            self.vrf_name_xr.value_namespace = name_space
                            self.vrf_name_xr.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.local_discriminator:
                        if (c.has_data()):
                            return True
                    return self.vrf_name.is_set

                def has_operation(self):
                    for c in self.local_discriminator:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.vrf_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "local-vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ip-sbfd-oper:sbfd/target-identifier/local-vrfs/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "local-discriminator"):
                        for c in self.local_discriminator:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Sbfd.TargetIdentifier.LocalVrfs.LocalVrf.LocalDiscriminator()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.local_discriminator.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "local-discriminator" or name == "vrf-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "vrf-name"):
                        self.vrf_name = value
                        self.vrf_name.value_namespace = name_space
                        self.vrf_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.local_vrf:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.local_vrf:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "local-vrfs" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-sbfd-oper:sbfd/target-identifier/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "local-vrf"):
                    for c in self.local_vrf:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Sbfd.TargetIdentifier.LocalVrfs.LocalVrf()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.local_vrf.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "local-vrf"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.local_vrfs is not None and self.local_vrfs.has_data()) or
                (self.remote_vrfs is not None and self.remote_vrfs.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.local_vrfs is not None and self.local_vrfs.has_operation()) or
                (self.remote_vrfs is not None and self.remote_vrfs.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "target-identifier" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-sbfd-oper:sbfd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "local-vrfs"):
                if (self.local_vrfs is None):
                    self.local_vrfs = Sbfd.TargetIdentifier.LocalVrfs()
                    self.local_vrfs.parent = self
                    self._children_name_map["local_vrfs"] = "local-vrfs"
                return self.local_vrfs

            if (child_yang_name == "remote-vrfs"):
                if (self.remote_vrfs is None):
                    self.remote_vrfs = Sbfd.TargetIdentifier.RemoteVrfs()
                    self.remote_vrfs.parent = self
                    self._children_name_map["remote_vrfs"] = "remote-vrfs"
                return self.remote_vrfs

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "local-vrfs" or name == "remote-vrfs"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.target_identifier is not None and self.target_identifier.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.target_identifier is not None and self.target_identifier.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ip-sbfd-oper:sbfd" + path_buffer

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

        if (child_yang_name == "target-identifier"):
            if (self.target_identifier is None):
                self.target_identifier = Sbfd.TargetIdentifier()
                self.target_identifier.parent = self
                self._children_name_map["target_identifier"] = "target-identifier"
            return self.target_identifier

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "target-identifier"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Sbfd()
        return self._top_entity


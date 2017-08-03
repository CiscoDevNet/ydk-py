""" Cisco_IOS_XR_ipv4_autorp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-autorp package operational data.

This module contains definitions
for the following management objects\:
  auto\-rp\: AutoRP operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AutorpProtocolMode(Enum):
    """
    AutorpProtocolMode

    Autorp protocol mode

    .. data:: sparse = 0

    	sparse

    .. data:: bidirectional = 1

    	bidirectional

    """

    sparse = Enum.YLeaf(0, "sparse")

    bidirectional = Enum.YLeaf(1, "bidirectional")



class AutoRp(Entity):
    """
    AutoRP operational data
    
    .. attribute:: active
    
    	Active Process
    	**type**\:   :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active>`
    
    .. attribute:: standby
    
    	Standby Process
    	**type**\:   :py:class:`Standby <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby>`
    
    

    """

    _prefix = 'ipv4-autorp-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(AutoRp, self).__init__()
        self._top_entity = None

        self.yang_name = "auto-rp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-autorp-oper"

        self.active = AutoRp.Active()
        self.active.parent = self
        self._children_name_map["active"] = "active"
        self._children_yang_names.add("active")

        self.standby = AutoRp.Standby()
        self.standby.parent = self
        self._children_name_map["standby"] = "standby"
        self._children_yang_names.add("standby")


    class Standby(Entity):
        """
        Standby Process
        
        .. attribute:: candidate_rp
        
        	AutoRP Candidate RP
        	**type**\:   :py:class:`CandidateRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.CandidateRp>`
        
        .. attribute:: mapping_agent
        
        	AutoRP Mapping Agent Table
        	**type**\:   :py:class:`MappingAgent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.MappingAgent>`
        
        

        """

        _prefix = 'ipv4-autorp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(AutoRp.Standby, self).__init__()

            self.yang_name = "standby"
            self.yang_parent_name = "auto-rp"

            self.candidate_rp = AutoRp.Standby.CandidateRp()
            self.candidate_rp.parent = self
            self._children_name_map["candidate_rp"] = "candidate-rp"
            self._children_yang_names.add("candidate-rp")

            self.mapping_agent = AutoRp.Standby.MappingAgent()
            self.mapping_agent.parent = self
            self._children_name_map["mapping_agent"] = "mapping-agent"
            self._children_yang_names.add("mapping-agent")


        class CandidateRp(Entity):
            """
            AutoRP Candidate RP
            
            .. attribute:: rps
            
            	AutoRP Candidate RP Table
            	**type**\:   :py:class:`Rps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.CandidateRp.Rps>`
            
            .. attribute:: traffic
            
            	AutoRP Candidate Traffic Counters
            	**type**\:   :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.CandidateRp.Traffic>`
            
            

            """

            _prefix = 'ipv4-autorp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(AutoRp.Standby.CandidateRp, self).__init__()

                self.yang_name = "candidate-rp"
                self.yang_parent_name = "standby"

                self.rps = AutoRp.Standby.CandidateRp.Rps()
                self.rps.parent = self
                self._children_name_map["rps"] = "rps"
                self._children_yang_names.add("rps")

                self.traffic = AutoRp.Standby.CandidateRp.Traffic()
                self.traffic.parent = self
                self._children_name_map["traffic"] = "traffic"
                self._children_yang_names.add("traffic")


            class Traffic(Entity):
                """
                AutoRP Candidate Traffic Counters
                
                .. attribute:: active_sent_packets
                
                	Number of packets sent in active role
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: standby_sent_packets
                
                	Number of packets dropped in send path in standby role
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AutoRp.Standby.CandidateRp.Traffic, self).__init__()

                    self.yang_name = "traffic"
                    self.yang_parent_name = "candidate-rp"

                    self.active_sent_packets = YLeaf(YType.uint32, "active-sent-packets")

                    self.standby_sent_packets = YLeaf(YType.uint32, "standby-sent-packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("active_sent_packets",
                                    "standby_sent_packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(AutoRp.Standby.CandidateRp.Traffic, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AutoRp.Standby.CandidateRp.Traffic, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.active_sent_packets.is_set or
                        self.standby_sent_packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.active_sent_packets.yfilter != YFilter.not_set or
                        self.standby_sent_packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "traffic" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/candidate-rp/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.active_sent_packets.is_set or self.active_sent_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_sent_packets.get_name_leafdata())
                    if (self.standby_sent_packets.is_set or self.standby_sent_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby_sent_packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "active-sent-packets" or name == "standby-sent-packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "active-sent-packets"):
                        self.active_sent_packets = value
                        self.active_sent_packets.value_namespace = name_space
                        self.active_sent_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby-sent-packets"):
                        self.standby_sent_packets = value
                        self.standby_sent_packets.value_namespace = name_space
                        self.standby_sent_packets.value_namespace_prefix = name_space_prefix


            class Rps(Entity):
                """
                AutoRP Candidate RP Table
                
                .. attribute:: rp
                
                	AutoRP Candidate RP Entry
                	**type**\: list of    :py:class:`Rp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.CandidateRp.Rps.Rp>`
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AutoRp.Standby.CandidateRp.Rps, self).__init__()

                    self.yang_name = "rps"
                    self.yang_parent_name = "candidate-rp"

                    self.rp = YList(self)

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
                                super(AutoRp.Standby.CandidateRp.Rps, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AutoRp.Standby.CandidateRp.Rps, self).__setattr__(name, value)


                class Rp(Entity):
                    """
                    AutoRP Candidate RP Entry
                    
                    .. attribute:: access_list_name
                    
                    	ACL Name
                    	**type**\:  str
                    
                    .. attribute:: announce_period
                    
                    	Announce Period
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: candidate_rp_address
                    
                    	Candidate RP IP Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: protocol_mode
                    
                    	Protocol Mode
                    	**type**\:   :py:class:`AutoRpProtocolMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_datatypes.AutoRpProtocolMode>`
                    
                    .. attribute:: protocol_mode_xr
                    
                    	Protocol Mode
                    	**type**\:   :py:class:`AutorpProtocolMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutorpProtocolMode>`
                    
                    .. attribute:: ttl
                    
                    	TTL
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'ipv4-autorp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(AutoRp.Standby.CandidateRp.Rps.Rp, self).__init__()

                        self.yang_name = "rp"
                        self.yang_parent_name = "rps"

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                        self.announce_period = YLeaf(YType.int32, "announce-period")

                        self.candidate_rp_address = YLeaf(YType.str, "candidate-rp-address")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.protocol_mode = YLeaf(YType.enumeration, "protocol-mode")

                        self.protocol_mode_xr = YLeaf(YType.enumeration, "protocol-mode-xr")

                        self.ttl = YLeaf(YType.int32, "ttl")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("access_list_name",
                                        "announce_period",
                                        "candidate_rp_address",
                                        "interface_name",
                                        "protocol_mode",
                                        "protocol_mode_xr",
                                        "ttl") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(AutoRp.Standby.CandidateRp.Rps.Rp, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(AutoRp.Standby.CandidateRp.Rps.Rp, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.access_list_name.is_set or
                            self.announce_period.is_set or
                            self.candidate_rp_address.is_set or
                            self.interface_name.is_set or
                            self.protocol_mode.is_set or
                            self.protocol_mode_xr.is_set or
                            self.ttl.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.access_list_name.yfilter != YFilter.not_set or
                            self.announce_period.yfilter != YFilter.not_set or
                            self.candidate_rp_address.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.protocol_mode.yfilter != YFilter.not_set or
                            self.protocol_mode_xr.yfilter != YFilter.not_set or
                            self.ttl.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "rp" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/candidate-rp/rps/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_list_name.get_name_leafdata())
                        if (self.announce_period.is_set or self.announce_period.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.announce_period.get_name_leafdata())
                        if (self.candidate_rp_address.is_set or self.candidate_rp_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.candidate_rp_address.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.protocol_mode.is_set or self.protocol_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.protocol_mode.get_name_leafdata())
                        if (self.protocol_mode_xr.is_set or self.protocol_mode_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.protocol_mode_xr.get_name_leafdata())
                        if (self.ttl.is_set or self.ttl.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ttl.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "access-list-name" or name == "announce-period" or name == "candidate-rp-address" or name == "interface-name" or name == "protocol-mode" or name == "protocol-mode-xr" or name == "ttl"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "access-list-name"):
                            self.access_list_name = value
                            self.access_list_name.value_namespace = name_space
                            self.access_list_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "announce-period"):
                            self.announce_period = value
                            self.announce_period.value_namespace = name_space
                            self.announce_period.value_namespace_prefix = name_space_prefix
                        if(value_path == "candidate-rp-address"):
                            self.candidate_rp_address = value
                            self.candidate_rp_address.value_namespace = name_space
                            self.candidate_rp_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "protocol-mode"):
                            self.protocol_mode = value
                            self.protocol_mode.value_namespace = name_space
                            self.protocol_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "protocol-mode-xr"):
                            self.protocol_mode_xr = value
                            self.protocol_mode_xr.value_namespace = name_space
                            self.protocol_mode_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "ttl"):
                            self.ttl = value
                            self.ttl.value_namespace = name_space
                            self.ttl.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.rp:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.rp:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "rps" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/candidate-rp/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "rp"):
                        for c in self.rp:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = AutoRp.Standby.CandidateRp.Rps.Rp()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.rp.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "rp"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.rps is not None and self.rps.has_data()) or
                    (self.traffic is not None and self.traffic.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.rps is not None and self.rps.has_operation()) or
                    (self.traffic is not None and self.traffic.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "candidate-rp" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "rps"):
                    if (self.rps is None):
                        self.rps = AutoRp.Standby.CandidateRp.Rps()
                        self.rps.parent = self
                        self._children_name_map["rps"] = "rps"
                    return self.rps

                if (child_yang_name == "traffic"):
                    if (self.traffic is None):
                        self.traffic = AutoRp.Standby.CandidateRp.Traffic()
                        self.traffic.parent = self
                        self._children_name_map["traffic"] = "traffic"
                    return self.traffic

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rps" or name == "traffic"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class MappingAgent(Entity):
            """
            AutoRP Mapping Agent Table
            
            .. attribute:: rp_addresses
            
            	AutoRP Mapping Agent Table Entries
            	**type**\:   :py:class:`RpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.MappingAgent.RpAddresses>`
            
            .. attribute:: summary
            
            	AutoRP Mapping Agent Summary Information
            	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.MappingAgent.Summary>`
            
            .. attribute:: traffic
            
            	AutoRP Mapping Agent Traffic Counters
            	**type**\:   :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.MappingAgent.Traffic>`
            
            

            """

            _prefix = 'ipv4-autorp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(AutoRp.Standby.MappingAgent, self).__init__()

                self.yang_name = "mapping-agent"
                self.yang_parent_name = "standby"

                self.rp_addresses = AutoRp.Standby.MappingAgent.RpAddresses()
                self.rp_addresses.parent = self
                self._children_name_map["rp_addresses"] = "rp-addresses"
                self._children_yang_names.add("rp-addresses")

                self.summary = AutoRp.Standby.MappingAgent.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
                self._children_yang_names.add("summary")

                self.traffic = AutoRp.Standby.MappingAgent.Traffic()
                self.traffic.parent = self
                self._children_name_map["traffic"] = "traffic"
                self._children_yang_names.add("traffic")


            class Traffic(Entity):
                """
                AutoRP Mapping Agent Traffic Counters
                
                .. attribute:: active_received_packets
                
                	Number of packets received in active role
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: active_sent_packets
                
                	Number of packets sent in active role
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: standby_received_packets
                
                	Number of packets dropped in receive path in standby role
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: standby_sent_packets
                
                	Number of packets dropped in send path in standby role
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AutoRp.Standby.MappingAgent.Traffic, self).__init__()

                    self.yang_name = "traffic"
                    self.yang_parent_name = "mapping-agent"

                    self.active_received_packets = YLeaf(YType.uint32, "active-received-packets")

                    self.active_sent_packets = YLeaf(YType.uint32, "active-sent-packets")

                    self.standby_received_packets = YLeaf(YType.uint32, "standby-received-packets")

                    self.standby_sent_packets = YLeaf(YType.uint32, "standby-sent-packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("active_received_packets",
                                    "active_sent_packets",
                                    "standby_received_packets",
                                    "standby_sent_packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(AutoRp.Standby.MappingAgent.Traffic, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AutoRp.Standby.MappingAgent.Traffic, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.active_received_packets.is_set or
                        self.active_sent_packets.is_set or
                        self.standby_received_packets.is_set or
                        self.standby_sent_packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.active_received_packets.yfilter != YFilter.not_set or
                        self.active_sent_packets.yfilter != YFilter.not_set or
                        self.standby_received_packets.yfilter != YFilter.not_set or
                        self.standby_sent_packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "traffic" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/mapping-agent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.active_received_packets.is_set or self.active_received_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_received_packets.get_name_leafdata())
                    if (self.active_sent_packets.is_set or self.active_sent_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_sent_packets.get_name_leafdata())
                    if (self.standby_received_packets.is_set or self.standby_received_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby_received_packets.get_name_leafdata())
                    if (self.standby_sent_packets.is_set or self.standby_sent_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby_sent_packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "active-received-packets" or name == "active-sent-packets" or name == "standby-received-packets" or name == "standby-sent-packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "active-received-packets"):
                        self.active_received_packets = value
                        self.active_received_packets.value_namespace = name_space
                        self.active_received_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "active-sent-packets"):
                        self.active_sent_packets = value
                        self.active_sent_packets.value_namespace = name_space
                        self.active_sent_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby-received-packets"):
                        self.standby_received_packets = value
                        self.standby_received_packets.value_namespace = name_space
                        self.standby_received_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby-sent-packets"):
                        self.standby_sent_packets = value
                        self.standby_sent_packets.value_namespace = name_space
                        self.standby_sent_packets.value_namespace_prefix = name_space_prefix


            class RpAddresses(Entity):
                """
                AutoRP Mapping Agent Table Entries
                
                .. attribute:: rp_address
                
                	AutoRP Mapping Agent Entry
                	**type**\: list of    :py:class:`RpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.MappingAgent.RpAddresses.RpAddress>`
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AutoRp.Standby.MappingAgent.RpAddresses, self).__init__()

                    self.yang_name = "rp-addresses"
                    self.yang_parent_name = "mapping-agent"

                    self.rp_address = YList(self)

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
                                super(AutoRp.Standby.MappingAgent.RpAddresses, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AutoRp.Standby.MappingAgent.RpAddresses, self).__setattr__(name, value)


                class RpAddress(Entity):
                    """
                    AutoRP Mapping Agent Entry
                    
                    .. attribute:: rp_address  <key>
                    
                    	RP Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: expiry_time
                    
                    	Time for expiration in seconds
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: second
                    
                    .. attribute:: pim_version
                    
                    	PIM version of the CRP
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: range
                    
                    	Array of ranges
                    	**type**\: list of    :py:class:`Range <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.MappingAgent.RpAddresses.RpAddress.Range>`
                    
                    .. attribute:: rp_address_xr
                    
                    	Candidate\-RP address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ipv4-autorp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(AutoRp.Standby.MappingAgent.RpAddresses.RpAddress, self).__init__()

                        self.yang_name = "rp-address"
                        self.yang_parent_name = "rp-addresses"

                        self.rp_address = YLeaf(YType.str, "rp-address")

                        self.expiry_time = YLeaf(YType.uint64, "expiry-time")

                        self.pim_version = YLeaf(YType.uint8, "pim-version")

                        self.rp_address_xr = YLeaf(YType.str, "rp-address-xr")

                        self.range = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("rp_address",
                                        "expiry_time",
                                        "pim_version",
                                        "rp_address_xr") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(AutoRp.Standby.MappingAgent.RpAddresses.RpAddress, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(AutoRp.Standby.MappingAgent.RpAddresses.RpAddress, self).__setattr__(name, value)


                    class Range(Entity):
                        """
                        Array of ranges
                        
                        .. attribute:: check_point_object_id
                        
                        	Checkpoint object id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: create_type
                        
                        	Source of the entry
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_advertised
                        
                        	Is this entry advertised ?
                        	**type**\:  bool
                        
                        .. attribute:: prefix
                        
                        	Prefix of the range
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length
                        
                        	Prefix length of the range
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: protocol_mode
                        
                        	Protocol Mode
                        	**type**\:   :py:class:`AutorpProtocolMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutorpProtocolMode>`
                        
                        .. attribute:: uptime
                        
                        	Uptime in seconds
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'ipv4-autorp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(AutoRp.Standby.MappingAgent.RpAddresses.RpAddress.Range, self).__init__()

                            self.yang_name = "range"
                            self.yang_parent_name = "rp-address"

                            self.check_point_object_id = YLeaf(YType.uint32, "check-point-object-id")

                            self.create_type = YLeaf(YType.uint8, "create-type")

                            self.is_advertised = YLeaf(YType.boolean, "is-advertised")

                            self.prefix = YLeaf(YType.str, "prefix")

                            self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                            self.protocol_mode = YLeaf(YType.enumeration, "protocol-mode")

                            self.uptime = YLeaf(YType.uint64, "uptime")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("check_point_object_id",
                                            "create_type",
                                            "is_advertised",
                                            "prefix",
                                            "prefix_length",
                                            "protocol_mode",
                                            "uptime") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(AutoRp.Standby.MappingAgent.RpAddresses.RpAddress.Range, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(AutoRp.Standby.MappingAgent.RpAddresses.RpAddress.Range, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.check_point_object_id.is_set or
                                self.create_type.is_set or
                                self.is_advertised.is_set or
                                self.prefix.is_set or
                                self.prefix_length.is_set or
                                self.protocol_mode.is_set or
                                self.uptime.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.check_point_object_id.yfilter != YFilter.not_set or
                                self.create_type.yfilter != YFilter.not_set or
                                self.is_advertised.yfilter != YFilter.not_set or
                                self.prefix.yfilter != YFilter.not_set or
                                self.prefix_length.yfilter != YFilter.not_set or
                                self.protocol_mode.yfilter != YFilter.not_set or
                                self.uptime.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "range" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.check_point_object_id.is_set or self.check_point_object_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.check_point_object_id.get_name_leafdata())
                            if (self.create_type.is_set or self.create_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.create_type.get_name_leafdata())
                            if (self.is_advertised.is_set or self.is_advertised.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_advertised.get_name_leafdata())
                            if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix.get_name_leafdata())
                            if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix_length.get_name_leafdata())
                            if (self.protocol_mode.is_set or self.protocol_mode.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.protocol_mode.get_name_leafdata())
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
                            if(name == "check-point-object-id" or name == "create-type" or name == "is-advertised" or name == "prefix" or name == "prefix-length" or name == "protocol-mode" or name == "uptime"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "check-point-object-id"):
                                self.check_point_object_id = value
                                self.check_point_object_id.value_namespace = name_space
                                self.check_point_object_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "create-type"):
                                self.create_type = value
                                self.create_type.value_namespace = name_space
                                self.create_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-advertised"):
                                self.is_advertised = value
                                self.is_advertised.value_namespace = name_space
                                self.is_advertised.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix"):
                                self.prefix = value
                                self.prefix.value_namespace = name_space
                                self.prefix.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix-length"):
                                self.prefix_length = value
                                self.prefix_length.value_namespace = name_space
                                self.prefix_length.value_namespace_prefix = name_space_prefix
                            if(value_path == "protocol-mode"):
                                self.protocol_mode = value
                                self.protocol_mode.value_namespace = name_space
                                self.protocol_mode.value_namespace_prefix = name_space_prefix
                            if(value_path == "uptime"):
                                self.uptime = value
                                self.uptime.value_namespace = name_space
                                self.uptime.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.range:
                            if (c.has_data()):
                                return True
                        return (
                            self.rp_address.is_set or
                            self.expiry_time.is_set or
                            self.pim_version.is_set or
                            self.rp_address_xr.is_set)

                    def has_operation(self):
                        for c in self.range:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.rp_address.yfilter != YFilter.not_set or
                            self.expiry_time.yfilter != YFilter.not_set or
                            self.pim_version.yfilter != YFilter.not_set or
                            self.rp_address_xr.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "rp-address" + "[rp-address='" + self.rp_address.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/mapping-agent/rp-addresses/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.rp_address.is_set or self.rp_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rp_address.get_name_leafdata())
                        if (self.expiry_time.is_set or self.expiry_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.expiry_time.get_name_leafdata())
                        if (self.pim_version.is_set or self.pim_version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pim_version.get_name_leafdata())
                        if (self.rp_address_xr.is_set or self.rp_address_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rp_address_xr.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "range"):
                            for c in self.range:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = AutoRp.Standby.MappingAgent.RpAddresses.RpAddress.Range()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.range.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "range" or name == "rp-address" or name == "expiry-time" or name == "pim-version" or name == "rp-address-xr"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "rp-address"):
                            self.rp_address = value
                            self.rp_address.value_namespace = name_space
                            self.rp_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "expiry-time"):
                            self.expiry_time = value
                            self.expiry_time.value_namespace = name_space
                            self.expiry_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "pim-version"):
                            self.pim_version = value
                            self.pim_version.value_namespace = name_space
                            self.pim_version.value_namespace_prefix = name_space_prefix
                        if(value_path == "rp-address-xr"):
                            self.rp_address_xr = value
                            self.rp_address_xr.value_namespace = name_space
                            self.rp_address_xr.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.rp_address:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.rp_address:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "rp-addresses" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/mapping-agent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "rp-address"):
                        for c in self.rp_address:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = AutoRp.Standby.MappingAgent.RpAddresses.RpAddress()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.rp_address.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "rp-address"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Summary(Entity):
                """
                AutoRP Mapping Agent Summary Information
                
                .. attribute:: cache_count
                
                	Number of group to RP mapping entries in the cache
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: cache_limit
                
                	Maximum group to RP mapping entries allowed
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_maximum_disabled
                
                	Is maximum enforcement disabled ?
                	**type**\:  bool
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AutoRp.Standby.MappingAgent.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "mapping-agent"

                    self.cache_count = YLeaf(YType.uint32, "cache-count")

                    self.cache_limit = YLeaf(YType.uint32, "cache-limit")

                    self.is_maximum_disabled = YLeaf(YType.boolean, "is-maximum-disabled")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("cache_count",
                                    "cache_limit",
                                    "is_maximum_disabled") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(AutoRp.Standby.MappingAgent.Summary, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AutoRp.Standby.MappingAgent.Summary, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.cache_count.is_set or
                        self.cache_limit.is_set or
                        self.is_maximum_disabled.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.cache_count.yfilter != YFilter.not_set or
                        self.cache_limit.yfilter != YFilter.not_set or
                        self.is_maximum_disabled.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "summary" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/mapping-agent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.cache_count.is_set or self.cache_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cache_count.get_name_leafdata())
                    if (self.cache_limit.is_set or self.cache_limit.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cache_limit.get_name_leafdata())
                    if (self.is_maximum_disabled.is_set or self.is_maximum_disabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_maximum_disabled.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "cache-count" or name == "cache-limit" or name == "is-maximum-disabled"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "cache-count"):
                        self.cache_count = value
                        self.cache_count.value_namespace = name_space
                        self.cache_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "cache-limit"):
                        self.cache_limit = value
                        self.cache_limit.value_namespace = name_space
                        self.cache_limit.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-maximum-disabled"):
                        self.is_maximum_disabled = value
                        self.is_maximum_disabled.value_namespace = name_space
                        self.is_maximum_disabled.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    (self.rp_addresses is not None and self.rp_addresses.has_data()) or
                    (self.summary is not None and self.summary.has_data()) or
                    (self.traffic is not None and self.traffic.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.rp_addresses is not None and self.rp_addresses.has_operation()) or
                    (self.summary is not None and self.summary.has_operation()) or
                    (self.traffic is not None and self.traffic.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mapping-agent" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "rp-addresses"):
                    if (self.rp_addresses is None):
                        self.rp_addresses = AutoRp.Standby.MappingAgent.RpAddresses()
                        self.rp_addresses.parent = self
                        self._children_name_map["rp_addresses"] = "rp-addresses"
                    return self.rp_addresses

                if (child_yang_name == "summary"):
                    if (self.summary is None):
                        self.summary = AutoRp.Standby.MappingAgent.Summary()
                        self.summary.parent = self
                        self._children_name_map["summary"] = "summary"
                    return self.summary

                if (child_yang_name == "traffic"):
                    if (self.traffic is None):
                        self.traffic = AutoRp.Standby.MappingAgent.Traffic()
                        self.traffic.parent = self
                        self._children_name_map["traffic"] = "traffic"
                    return self.traffic

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rp-addresses" or name == "summary" or name == "traffic"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.candidate_rp is not None and self.candidate_rp.has_data()) or
                (self.mapping_agent is not None and self.mapping_agent.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.candidate_rp is not None and self.candidate_rp.has_operation()) or
                (self.mapping_agent is not None and self.mapping_agent.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "standby" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "candidate-rp"):
                if (self.candidate_rp is None):
                    self.candidate_rp = AutoRp.Standby.CandidateRp()
                    self.candidate_rp.parent = self
                    self._children_name_map["candidate_rp"] = "candidate-rp"
                return self.candidate_rp

            if (child_yang_name == "mapping-agent"):
                if (self.mapping_agent is None):
                    self.mapping_agent = AutoRp.Standby.MappingAgent()
                    self.mapping_agent.parent = self
                    self._children_name_map["mapping_agent"] = "mapping-agent"
                return self.mapping_agent

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "candidate-rp" or name == "mapping-agent"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Active(Entity):
        """
        Active Process
        
        .. attribute:: candidate_rp
        
        	AutoRP Candidate RP
        	**type**\:   :py:class:`CandidateRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.CandidateRp>`
        
        .. attribute:: mapping_agent
        
        	AutoRP Mapping Agent Table
        	**type**\:   :py:class:`MappingAgent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.MappingAgent>`
        
        

        """

        _prefix = 'ipv4-autorp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(AutoRp.Active, self).__init__()

            self.yang_name = "active"
            self.yang_parent_name = "auto-rp"

            self.candidate_rp = AutoRp.Active.CandidateRp()
            self.candidate_rp.parent = self
            self._children_name_map["candidate_rp"] = "candidate-rp"
            self._children_yang_names.add("candidate-rp")

            self.mapping_agent = AutoRp.Active.MappingAgent()
            self.mapping_agent.parent = self
            self._children_name_map["mapping_agent"] = "mapping-agent"
            self._children_yang_names.add("mapping-agent")


        class CandidateRp(Entity):
            """
            AutoRP Candidate RP
            
            .. attribute:: rps
            
            	AutoRP Candidate RP Table
            	**type**\:   :py:class:`Rps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.CandidateRp.Rps>`
            
            .. attribute:: traffic
            
            	AutoRP Candidate Traffic Counters
            	**type**\:   :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.CandidateRp.Traffic>`
            
            

            """

            _prefix = 'ipv4-autorp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(AutoRp.Active.CandidateRp, self).__init__()

                self.yang_name = "candidate-rp"
                self.yang_parent_name = "active"

                self.rps = AutoRp.Active.CandidateRp.Rps()
                self.rps.parent = self
                self._children_name_map["rps"] = "rps"
                self._children_yang_names.add("rps")

                self.traffic = AutoRp.Active.CandidateRp.Traffic()
                self.traffic.parent = self
                self._children_name_map["traffic"] = "traffic"
                self._children_yang_names.add("traffic")


            class Traffic(Entity):
                """
                AutoRP Candidate Traffic Counters
                
                .. attribute:: active_sent_packets
                
                	Number of packets sent in active role
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: standby_sent_packets
                
                	Number of packets dropped in send path in standby role
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AutoRp.Active.CandidateRp.Traffic, self).__init__()

                    self.yang_name = "traffic"
                    self.yang_parent_name = "candidate-rp"

                    self.active_sent_packets = YLeaf(YType.uint32, "active-sent-packets")

                    self.standby_sent_packets = YLeaf(YType.uint32, "standby-sent-packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("active_sent_packets",
                                    "standby_sent_packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(AutoRp.Active.CandidateRp.Traffic, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AutoRp.Active.CandidateRp.Traffic, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.active_sent_packets.is_set or
                        self.standby_sent_packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.active_sent_packets.yfilter != YFilter.not_set or
                        self.standby_sent_packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "traffic" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/candidate-rp/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.active_sent_packets.is_set or self.active_sent_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_sent_packets.get_name_leafdata())
                    if (self.standby_sent_packets.is_set or self.standby_sent_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby_sent_packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "active-sent-packets" or name == "standby-sent-packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "active-sent-packets"):
                        self.active_sent_packets = value
                        self.active_sent_packets.value_namespace = name_space
                        self.active_sent_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby-sent-packets"):
                        self.standby_sent_packets = value
                        self.standby_sent_packets.value_namespace = name_space
                        self.standby_sent_packets.value_namespace_prefix = name_space_prefix


            class Rps(Entity):
                """
                AutoRP Candidate RP Table
                
                .. attribute:: rp
                
                	AutoRP Candidate RP Entry
                	**type**\: list of    :py:class:`Rp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.CandidateRp.Rps.Rp>`
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AutoRp.Active.CandidateRp.Rps, self).__init__()

                    self.yang_name = "rps"
                    self.yang_parent_name = "candidate-rp"

                    self.rp = YList(self)

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
                                super(AutoRp.Active.CandidateRp.Rps, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AutoRp.Active.CandidateRp.Rps, self).__setattr__(name, value)


                class Rp(Entity):
                    """
                    AutoRP Candidate RP Entry
                    
                    .. attribute:: access_list_name
                    
                    	ACL Name
                    	**type**\:  str
                    
                    .. attribute:: announce_period
                    
                    	Announce Period
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: candidate_rp_address
                    
                    	Candidate RP IP Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: protocol_mode
                    
                    	Protocol Mode
                    	**type**\:   :py:class:`AutoRpProtocolMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_datatypes.AutoRpProtocolMode>`
                    
                    .. attribute:: protocol_mode_xr
                    
                    	Protocol Mode
                    	**type**\:   :py:class:`AutorpProtocolMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutorpProtocolMode>`
                    
                    .. attribute:: ttl
                    
                    	TTL
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'ipv4-autorp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(AutoRp.Active.CandidateRp.Rps.Rp, self).__init__()

                        self.yang_name = "rp"
                        self.yang_parent_name = "rps"

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                        self.announce_period = YLeaf(YType.int32, "announce-period")

                        self.candidate_rp_address = YLeaf(YType.str, "candidate-rp-address")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.protocol_mode = YLeaf(YType.enumeration, "protocol-mode")

                        self.protocol_mode_xr = YLeaf(YType.enumeration, "protocol-mode-xr")

                        self.ttl = YLeaf(YType.int32, "ttl")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("access_list_name",
                                        "announce_period",
                                        "candidate_rp_address",
                                        "interface_name",
                                        "protocol_mode",
                                        "protocol_mode_xr",
                                        "ttl") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(AutoRp.Active.CandidateRp.Rps.Rp, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(AutoRp.Active.CandidateRp.Rps.Rp, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.access_list_name.is_set or
                            self.announce_period.is_set or
                            self.candidate_rp_address.is_set or
                            self.interface_name.is_set or
                            self.protocol_mode.is_set or
                            self.protocol_mode_xr.is_set or
                            self.ttl.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.access_list_name.yfilter != YFilter.not_set or
                            self.announce_period.yfilter != YFilter.not_set or
                            self.candidate_rp_address.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.protocol_mode.yfilter != YFilter.not_set or
                            self.protocol_mode_xr.yfilter != YFilter.not_set or
                            self.ttl.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "rp" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/candidate-rp/rps/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.access_list_name.is_set or self.access_list_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_list_name.get_name_leafdata())
                        if (self.announce_period.is_set or self.announce_period.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.announce_period.get_name_leafdata())
                        if (self.candidate_rp_address.is_set or self.candidate_rp_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.candidate_rp_address.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.protocol_mode.is_set or self.protocol_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.protocol_mode.get_name_leafdata())
                        if (self.protocol_mode_xr.is_set or self.protocol_mode_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.protocol_mode_xr.get_name_leafdata())
                        if (self.ttl.is_set or self.ttl.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ttl.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "access-list-name" or name == "announce-period" or name == "candidate-rp-address" or name == "interface-name" or name == "protocol-mode" or name == "protocol-mode-xr" or name == "ttl"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "access-list-name"):
                            self.access_list_name = value
                            self.access_list_name.value_namespace = name_space
                            self.access_list_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "announce-period"):
                            self.announce_period = value
                            self.announce_period.value_namespace = name_space
                            self.announce_period.value_namespace_prefix = name_space_prefix
                        if(value_path == "candidate-rp-address"):
                            self.candidate_rp_address = value
                            self.candidate_rp_address.value_namespace = name_space
                            self.candidate_rp_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "protocol-mode"):
                            self.protocol_mode = value
                            self.protocol_mode.value_namespace = name_space
                            self.protocol_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "protocol-mode-xr"):
                            self.protocol_mode_xr = value
                            self.protocol_mode_xr.value_namespace = name_space
                            self.protocol_mode_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "ttl"):
                            self.ttl = value
                            self.ttl.value_namespace = name_space
                            self.ttl.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.rp:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.rp:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "rps" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/candidate-rp/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "rp"):
                        for c in self.rp:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = AutoRp.Active.CandidateRp.Rps.Rp()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.rp.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "rp"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.rps is not None and self.rps.has_data()) or
                    (self.traffic is not None and self.traffic.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.rps is not None and self.rps.has_operation()) or
                    (self.traffic is not None and self.traffic.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "candidate-rp" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "rps"):
                    if (self.rps is None):
                        self.rps = AutoRp.Active.CandidateRp.Rps()
                        self.rps.parent = self
                        self._children_name_map["rps"] = "rps"
                    return self.rps

                if (child_yang_name == "traffic"):
                    if (self.traffic is None):
                        self.traffic = AutoRp.Active.CandidateRp.Traffic()
                        self.traffic.parent = self
                        self._children_name_map["traffic"] = "traffic"
                    return self.traffic

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rps" or name == "traffic"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class MappingAgent(Entity):
            """
            AutoRP Mapping Agent Table
            
            .. attribute:: rp_addresses
            
            	AutoRP Mapping Agent Table Entries
            	**type**\:   :py:class:`RpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.MappingAgent.RpAddresses>`
            
            .. attribute:: summary
            
            	AutoRP Mapping Agent Summary Information
            	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.MappingAgent.Summary>`
            
            .. attribute:: traffic
            
            	AutoRP Mapping Agent Traffic Counters
            	**type**\:   :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.MappingAgent.Traffic>`
            
            

            """

            _prefix = 'ipv4-autorp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(AutoRp.Active.MappingAgent, self).__init__()

                self.yang_name = "mapping-agent"
                self.yang_parent_name = "active"

                self.rp_addresses = AutoRp.Active.MappingAgent.RpAddresses()
                self.rp_addresses.parent = self
                self._children_name_map["rp_addresses"] = "rp-addresses"
                self._children_yang_names.add("rp-addresses")

                self.summary = AutoRp.Active.MappingAgent.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
                self._children_yang_names.add("summary")

                self.traffic = AutoRp.Active.MappingAgent.Traffic()
                self.traffic.parent = self
                self._children_name_map["traffic"] = "traffic"
                self._children_yang_names.add("traffic")


            class Traffic(Entity):
                """
                AutoRP Mapping Agent Traffic Counters
                
                .. attribute:: active_received_packets
                
                	Number of packets received in active role
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: active_sent_packets
                
                	Number of packets sent in active role
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: standby_received_packets
                
                	Number of packets dropped in receive path in standby role
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: standby_sent_packets
                
                	Number of packets dropped in send path in standby role
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AutoRp.Active.MappingAgent.Traffic, self).__init__()

                    self.yang_name = "traffic"
                    self.yang_parent_name = "mapping-agent"

                    self.active_received_packets = YLeaf(YType.uint32, "active-received-packets")

                    self.active_sent_packets = YLeaf(YType.uint32, "active-sent-packets")

                    self.standby_received_packets = YLeaf(YType.uint32, "standby-received-packets")

                    self.standby_sent_packets = YLeaf(YType.uint32, "standby-sent-packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("active_received_packets",
                                    "active_sent_packets",
                                    "standby_received_packets",
                                    "standby_sent_packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(AutoRp.Active.MappingAgent.Traffic, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AutoRp.Active.MappingAgent.Traffic, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.active_received_packets.is_set or
                        self.active_sent_packets.is_set or
                        self.standby_received_packets.is_set or
                        self.standby_sent_packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.active_received_packets.yfilter != YFilter.not_set or
                        self.active_sent_packets.yfilter != YFilter.not_set or
                        self.standby_received_packets.yfilter != YFilter.not_set or
                        self.standby_sent_packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "traffic" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/mapping-agent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.active_received_packets.is_set or self.active_received_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_received_packets.get_name_leafdata())
                    if (self.active_sent_packets.is_set or self.active_sent_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_sent_packets.get_name_leafdata())
                    if (self.standby_received_packets.is_set or self.standby_received_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby_received_packets.get_name_leafdata())
                    if (self.standby_sent_packets.is_set or self.standby_sent_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby_sent_packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "active-received-packets" or name == "active-sent-packets" or name == "standby-received-packets" or name == "standby-sent-packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "active-received-packets"):
                        self.active_received_packets = value
                        self.active_received_packets.value_namespace = name_space
                        self.active_received_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "active-sent-packets"):
                        self.active_sent_packets = value
                        self.active_sent_packets.value_namespace = name_space
                        self.active_sent_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby-received-packets"):
                        self.standby_received_packets = value
                        self.standby_received_packets.value_namespace = name_space
                        self.standby_received_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby-sent-packets"):
                        self.standby_sent_packets = value
                        self.standby_sent_packets.value_namespace = name_space
                        self.standby_sent_packets.value_namespace_prefix = name_space_prefix


            class RpAddresses(Entity):
                """
                AutoRP Mapping Agent Table Entries
                
                .. attribute:: rp_address
                
                	AutoRP Mapping Agent Entry
                	**type**\: list of    :py:class:`RpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.MappingAgent.RpAddresses.RpAddress>`
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AutoRp.Active.MappingAgent.RpAddresses, self).__init__()

                    self.yang_name = "rp-addresses"
                    self.yang_parent_name = "mapping-agent"

                    self.rp_address = YList(self)

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
                                super(AutoRp.Active.MappingAgent.RpAddresses, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AutoRp.Active.MappingAgent.RpAddresses, self).__setattr__(name, value)


                class RpAddress(Entity):
                    """
                    AutoRP Mapping Agent Entry
                    
                    .. attribute:: rp_address  <key>
                    
                    	RP Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: expiry_time
                    
                    	Time for expiration in seconds
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: second
                    
                    .. attribute:: pim_version
                    
                    	PIM version of the CRP
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: range
                    
                    	Array of ranges
                    	**type**\: list of    :py:class:`Range <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.MappingAgent.RpAddresses.RpAddress.Range>`
                    
                    .. attribute:: rp_address_xr
                    
                    	Candidate\-RP address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ipv4-autorp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(AutoRp.Active.MappingAgent.RpAddresses.RpAddress, self).__init__()

                        self.yang_name = "rp-address"
                        self.yang_parent_name = "rp-addresses"

                        self.rp_address = YLeaf(YType.str, "rp-address")

                        self.expiry_time = YLeaf(YType.uint64, "expiry-time")

                        self.pim_version = YLeaf(YType.uint8, "pim-version")

                        self.rp_address_xr = YLeaf(YType.str, "rp-address-xr")

                        self.range = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("rp_address",
                                        "expiry_time",
                                        "pim_version",
                                        "rp_address_xr") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(AutoRp.Active.MappingAgent.RpAddresses.RpAddress, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(AutoRp.Active.MappingAgent.RpAddresses.RpAddress, self).__setattr__(name, value)


                    class Range(Entity):
                        """
                        Array of ranges
                        
                        .. attribute:: check_point_object_id
                        
                        	Checkpoint object id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: create_type
                        
                        	Source of the entry
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_advertised
                        
                        	Is this entry advertised ?
                        	**type**\:  bool
                        
                        .. attribute:: prefix
                        
                        	Prefix of the range
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length
                        
                        	Prefix length of the range
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: protocol_mode
                        
                        	Protocol Mode
                        	**type**\:   :py:class:`AutorpProtocolMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutorpProtocolMode>`
                        
                        .. attribute:: uptime
                        
                        	Uptime in seconds
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'ipv4-autorp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(AutoRp.Active.MappingAgent.RpAddresses.RpAddress.Range, self).__init__()

                            self.yang_name = "range"
                            self.yang_parent_name = "rp-address"

                            self.check_point_object_id = YLeaf(YType.uint32, "check-point-object-id")

                            self.create_type = YLeaf(YType.uint8, "create-type")

                            self.is_advertised = YLeaf(YType.boolean, "is-advertised")

                            self.prefix = YLeaf(YType.str, "prefix")

                            self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                            self.protocol_mode = YLeaf(YType.enumeration, "protocol-mode")

                            self.uptime = YLeaf(YType.uint64, "uptime")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("check_point_object_id",
                                            "create_type",
                                            "is_advertised",
                                            "prefix",
                                            "prefix_length",
                                            "protocol_mode",
                                            "uptime") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(AutoRp.Active.MappingAgent.RpAddresses.RpAddress.Range, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(AutoRp.Active.MappingAgent.RpAddresses.RpAddress.Range, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.check_point_object_id.is_set or
                                self.create_type.is_set or
                                self.is_advertised.is_set or
                                self.prefix.is_set or
                                self.prefix_length.is_set or
                                self.protocol_mode.is_set or
                                self.uptime.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.check_point_object_id.yfilter != YFilter.not_set or
                                self.create_type.yfilter != YFilter.not_set or
                                self.is_advertised.yfilter != YFilter.not_set or
                                self.prefix.yfilter != YFilter.not_set or
                                self.prefix_length.yfilter != YFilter.not_set or
                                self.protocol_mode.yfilter != YFilter.not_set or
                                self.uptime.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "range" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.check_point_object_id.is_set or self.check_point_object_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.check_point_object_id.get_name_leafdata())
                            if (self.create_type.is_set or self.create_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.create_type.get_name_leafdata())
                            if (self.is_advertised.is_set or self.is_advertised.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_advertised.get_name_leafdata())
                            if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix.get_name_leafdata())
                            if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix_length.get_name_leafdata())
                            if (self.protocol_mode.is_set or self.protocol_mode.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.protocol_mode.get_name_leafdata())
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
                            if(name == "check-point-object-id" or name == "create-type" or name == "is-advertised" or name == "prefix" or name == "prefix-length" or name == "protocol-mode" or name == "uptime"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "check-point-object-id"):
                                self.check_point_object_id = value
                                self.check_point_object_id.value_namespace = name_space
                                self.check_point_object_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "create-type"):
                                self.create_type = value
                                self.create_type.value_namespace = name_space
                                self.create_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-advertised"):
                                self.is_advertised = value
                                self.is_advertised.value_namespace = name_space
                                self.is_advertised.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix"):
                                self.prefix = value
                                self.prefix.value_namespace = name_space
                                self.prefix.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix-length"):
                                self.prefix_length = value
                                self.prefix_length.value_namespace = name_space
                                self.prefix_length.value_namespace_prefix = name_space_prefix
                            if(value_path == "protocol-mode"):
                                self.protocol_mode = value
                                self.protocol_mode.value_namespace = name_space
                                self.protocol_mode.value_namespace_prefix = name_space_prefix
                            if(value_path == "uptime"):
                                self.uptime = value
                                self.uptime.value_namespace = name_space
                                self.uptime.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.range:
                            if (c.has_data()):
                                return True
                        return (
                            self.rp_address.is_set or
                            self.expiry_time.is_set or
                            self.pim_version.is_set or
                            self.rp_address_xr.is_set)

                    def has_operation(self):
                        for c in self.range:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.rp_address.yfilter != YFilter.not_set or
                            self.expiry_time.yfilter != YFilter.not_set or
                            self.pim_version.yfilter != YFilter.not_set or
                            self.rp_address_xr.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "rp-address" + "[rp-address='" + self.rp_address.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/mapping-agent/rp-addresses/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.rp_address.is_set or self.rp_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rp_address.get_name_leafdata())
                        if (self.expiry_time.is_set or self.expiry_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.expiry_time.get_name_leafdata())
                        if (self.pim_version.is_set or self.pim_version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pim_version.get_name_leafdata())
                        if (self.rp_address_xr.is_set or self.rp_address_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rp_address_xr.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "range"):
                            for c in self.range:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = AutoRp.Active.MappingAgent.RpAddresses.RpAddress.Range()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.range.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "range" or name == "rp-address" or name == "expiry-time" or name == "pim-version" or name == "rp-address-xr"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "rp-address"):
                            self.rp_address = value
                            self.rp_address.value_namespace = name_space
                            self.rp_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "expiry-time"):
                            self.expiry_time = value
                            self.expiry_time.value_namespace = name_space
                            self.expiry_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "pim-version"):
                            self.pim_version = value
                            self.pim_version.value_namespace = name_space
                            self.pim_version.value_namespace_prefix = name_space_prefix
                        if(value_path == "rp-address-xr"):
                            self.rp_address_xr = value
                            self.rp_address_xr.value_namespace = name_space
                            self.rp_address_xr.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.rp_address:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.rp_address:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "rp-addresses" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/mapping-agent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "rp-address"):
                        for c in self.rp_address:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = AutoRp.Active.MappingAgent.RpAddresses.RpAddress()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.rp_address.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "rp-address"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Summary(Entity):
                """
                AutoRP Mapping Agent Summary Information
                
                .. attribute:: cache_count
                
                	Number of group to RP mapping entries in the cache
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: cache_limit
                
                	Maximum group to RP mapping entries allowed
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_maximum_disabled
                
                	Is maximum enforcement disabled ?
                	**type**\:  bool
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AutoRp.Active.MappingAgent.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "mapping-agent"

                    self.cache_count = YLeaf(YType.uint32, "cache-count")

                    self.cache_limit = YLeaf(YType.uint32, "cache-limit")

                    self.is_maximum_disabled = YLeaf(YType.boolean, "is-maximum-disabled")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("cache_count",
                                    "cache_limit",
                                    "is_maximum_disabled") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(AutoRp.Active.MappingAgent.Summary, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(AutoRp.Active.MappingAgent.Summary, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.cache_count.is_set or
                        self.cache_limit.is_set or
                        self.is_maximum_disabled.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.cache_count.yfilter != YFilter.not_set or
                        self.cache_limit.yfilter != YFilter.not_set or
                        self.is_maximum_disabled.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "summary" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/mapping-agent/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.cache_count.is_set or self.cache_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cache_count.get_name_leafdata())
                    if (self.cache_limit.is_set or self.cache_limit.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cache_limit.get_name_leafdata())
                    if (self.is_maximum_disabled.is_set or self.is_maximum_disabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_maximum_disabled.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "cache-count" or name == "cache-limit" or name == "is-maximum-disabled"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "cache-count"):
                        self.cache_count = value
                        self.cache_count.value_namespace = name_space
                        self.cache_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "cache-limit"):
                        self.cache_limit = value
                        self.cache_limit.value_namespace = name_space
                        self.cache_limit.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-maximum-disabled"):
                        self.is_maximum_disabled = value
                        self.is_maximum_disabled.value_namespace = name_space
                        self.is_maximum_disabled.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    (self.rp_addresses is not None and self.rp_addresses.has_data()) or
                    (self.summary is not None and self.summary.has_data()) or
                    (self.traffic is not None and self.traffic.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.rp_addresses is not None and self.rp_addresses.has_operation()) or
                    (self.summary is not None and self.summary.has_operation()) or
                    (self.traffic is not None and self.traffic.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mapping-agent" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "rp-addresses"):
                    if (self.rp_addresses is None):
                        self.rp_addresses = AutoRp.Active.MappingAgent.RpAddresses()
                        self.rp_addresses.parent = self
                        self._children_name_map["rp_addresses"] = "rp-addresses"
                    return self.rp_addresses

                if (child_yang_name == "summary"):
                    if (self.summary is None):
                        self.summary = AutoRp.Active.MappingAgent.Summary()
                        self.summary.parent = self
                        self._children_name_map["summary"] = "summary"
                    return self.summary

                if (child_yang_name == "traffic"):
                    if (self.traffic is None):
                        self.traffic = AutoRp.Active.MappingAgent.Traffic()
                        self.traffic.parent = self
                        self._children_name_map["traffic"] = "traffic"
                    return self.traffic

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rp-addresses" or name == "summary" or name == "traffic"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.candidate_rp is not None and self.candidate_rp.has_data()) or
                (self.mapping_agent is not None and self.mapping_agent.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.candidate_rp is not None and self.candidate_rp.has_operation()) or
                (self.mapping_agent is not None and self.mapping_agent.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "active" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "candidate-rp"):
                if (self.candidate_rp is None):
                    self.candidate_rp = AutoRp.Active.CandidateRp()
                    self.candidate_rp.parent = self
                    self._children_name_map["candidate_rp"] = "candidate-rp"
                return self.candidate_rp

            if (child_yang_name == "mapping-agent"):
                if (self.mapping_agent is None):
                    self.mapping_agent = AutoRp.Active.MappingAgent()
                    self.mapping_agent.parent = self
                    self._children_name_map["mapping_agent"] = "mapping-agent"
                return self.mapping_agent

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "candidate-rp" or name == "mapping-agent"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.active is not None and self.active.has_data()) or
            (self.standby is not None and self.standby.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.active is not None and self.active.has_operation()) or
            (self.standby is not None and self.standby.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp" + path_buffer

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

        if (child_yang_name == "active"):
            if (self.active is None):
                self.active = AutoRp.Active()
                self.active.parent = self
                self._children_name_map["active"] = "active"
            return self.active

        if (child_yang_name == "standby"):
            if (self.standby is None):
                self.standby = AutoRp.Standby()
                self.standby.parent = self
                self._children_name_map["standby"] = "standby"
            return self.standby

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "active" or name == "standby"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = AutoRp()
        return self._top_entity


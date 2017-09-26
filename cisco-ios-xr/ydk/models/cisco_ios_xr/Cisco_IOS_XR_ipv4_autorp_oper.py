""" Cisco_IOS_XR_ipv4_autorp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-autorp package operational data.

This module contains definitions
for the following management objects\:
  auto\-rp\: AutoRP operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
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
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"active" : ("active", AutoRp.Active), "standby" : ("standby", AutoRp.Standby)}
        self._child_list_classes = {}

        self.active = AutoRp.Active()
        self.active.parent = self
        self._children_name_map["active"] = "active"
        self._children_yang_names.add("active")

        self.standby = AutoRp.Standby()
        self.standby.parent = self
        self._children_name_map["standby"] = "standby"
        self._children_yang_names.add("standby")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp"


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"candidate-rp" : ("candidate_rp", AutoRp.Active.CandidateRp), "mapping-agent" : ("mapping_agent", AutoRp.Active.MappingAgent)}
            self._child_list_classes = {}

            self.candidate_rp = AutoRp.Active.CandidateRp()
            self.candidate_rp.parent = self
            self._children_name_map["candidate_rp"] = "candidate-rp"
            self._children_yang_names.add("candidate-rp")

            self.mapping_agent = AutoRp.Active.MappingAgent()
            self.mapping_agent.parent = self
            self._children_name_map["mapping_agent"] = "mapping-agent"
            self._children_yang_names.add("mapping-agent")
            self._segment_path = lambda: "active"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/%s" % self._segment_path()


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"rps" : ("rps", AutoRp.Active.CandidateRp.Rps), "traffic" : ("traffic", AutoRp.Active.CandidateRp.Traffic)}
                self._child_list_classes = {}

                self.rps = AutoRp.Active.CandidateRp.Rps()
                self.rps.parent = self
                self._children_name_map["rps"] = "rps"
                self._children_yang_names.add("rps")

                self.traffic = AutoRp.Active.CandidateRp.Traffic()
                self.traffic.parent = self
                self._children_name_map["traffic"] = "traffic"
                self._children_yang_names.add("traffic")
                self._segment_path = lambda: "candidate-rp"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/%s" % self._segment_path()


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"rp" : ("rp", AutoRp.Active.CandidateRp.Rps.Rp)}

                    self.rp = YList(self)
                    self._segment_path = lambda: "rps"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/candidate-rp/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(AutoRp.Active.CandidateRp.Rps, [], name, value)


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
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                        self.announce_period = YLeaf(YType.int32, "announce-period")

                        self.candidate_rp_address = YLeaf(YType.str, "candidate-rp-address")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.protocol_mode = YLeaf(YType.enumeration, "protocol-mode")

                        self.protocol_mode_xr = YLeaf(YType.enumeration, "protocol-mode-xr")

                        self.ttl = YLeaf(YType.int32, "ttl")
                        self._segment_path = lambda: "rp"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/candidate-rp/rps/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(AutoRp.Active.CandidateRp.Rps.Rp, ['access_list_name', 'announce_period', 'candidate_rp_address', 'interface_name', 'protocol_mode', 'protocol_mode_xr', 'ttl'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.active_sent_packets = YLeaf(YType.uint32, "active-sent-packets")

                    self.standby_sent_packets = YLeaf(YType.uint32, "standby-sent-packets")
                    self._segment_path = lambda: "traffic"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/candidate-rp/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(AutoRp.Active.CandidateRp.Traffic, ['active_sent_packets', 'standby_sent_packets'], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"rp-addresses" : ("rp_addresses", AutoRp.Active.MappingAgent.RpAddresses), "summary" : ("summary", AutoRp.Active.MappingAgent.Summary), "traffic" : ("traffic", AutoRp.Active.MappingAgent.Traffic)}
                self._child_list_classes = {}

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
                self._segment_path = lambda: "mapping-agent"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/%s" % self._segment_path()


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"rp-address" : ("rp_address", AutoRp.Active.MappingAgent.RpAddresses.RpAddress)}

                    self.rp_address = YList(self)
                    self._segment_path = lambda: "rp-addresses"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/mapping-agent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(AutoRp.Active.MappingAgent.RpAddresses, [], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {"range" : ("range", AutoRp.Active.MappingAgent.RpAddresses.RpAddress.Range)}

                        self.rp_address = YLeaf(YType.str, "rp-address")

                        self.expiry_time = YLeaf(YType.uint64, "expiry-time")

                        self.pim_version = YLeaf(YType.uint8, "pim-version")

                        self.rp_address_xr = YLeaf(YType.str, "rp-address-xr")

                        self.range = YList(self)
                        self._segment_path = lambda: "rp-address" + "[rp-address='" + self.rp_address.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/mapping-agent/rp-addresses/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(AutoRp.Active.MappingAgent.RpAddresses.RpAddress, ['rp_address', 'expiry_time', 'pim_version', 'rp_address_xr'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.check_point_object_id = YLeaf(YType.uint32, "check-point-object-id")

                            self.create_type = YLeaf(YType.uint8, "create-type")

                            self.is_advertised = YLeaf(YType.boolean, "is-advertised")

                            self.prefix = YLeaf(YType.str, "prefix")

                            self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                            self.protocol_mode = YLeaf(YType.enumeration, "protocol-mode")

                            self.uptime = YLeaf(YType.uint64, "uptime")
                            self._segment_path = lambda: "range"

                        def __setattr__(self, name, value):
                            self._perform_setattr(AutoRp.Active.MappingAgent.RpAddresses.RpAddress.Range, ['check_point_object_id', 'create_type', 'is_advertised', 'prefix', 'prefix_length', 'protocol_mode', 'uptime'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.cache_count = YLeaf(YType.uint32, "cache-count")

                    self.cache_limit = YLeaf(YType.uint32, "cache-limit")

                    self.is_maximum_disabled = YLeaf(YType.boolean, "is-maximum-disabled")
                    self._segment_path = lambda: "summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/mapping-agent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(AutoRp.Active.MappingAgent.Summary, ['cache_count', 'cache_limit', 'is_maximum_disabled'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.active_received_packets = YLeaf(YType.uint32, "active-received-packets")

                    self.active_sent_packets = YLeaf(YType.uint32, "active-sent-packets")

                    self.standby_received_packets = YLeaf(YType.uint32, "standby-received-packets")

                    self.standby_sent_packets = YLeaf(YType.uint32, "standby-sent-packets")
                    self._segment_path = lambda: "traffic"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/mapping-agent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(AutoRp.Active.MappingAgent.Traffic, ['active_received_packets', 'active_sent_packets', 'standby_received_packets', 'standby_sent_packets'], name, value)


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"candidate-rp" : ("candidate_rp", AutoRp.Standby.CandidateRp), "mapping-agent" : ("mapping_agent", AutoRp.Standby.MappingAgent)}
            self._child_list_classes = {}

            self.candidate_rp = AutoRp.Standby.CandidateRp()
            self.candidate_rp.parent = self
            self._children_name_map["candidate_rp"] = "candidate-rp"
            self._children_yang_names.add("candidate-rp")

            self.mapping_agent = AutoRp.Standby.MappingAgent()
            self.mapping_agent.parent = self
            self._children_name_map["mapping_agent"] = "mapping-agent"
            self._children_yang_names.add("mapping-agent")
            self._segment_path = lambda: "standby"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/%s" % self._segment_path()


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"rps" : ("rps", AutoRp.Standby.CandidateRp.Rps), "traffic" : ("traffic", AutoRp.Standby.CandidateRp.Traffic)}
                self._child_list_classes = {}

                self.rps = AutoRp.Standby.CandidateRp.Rps()
                self.rps.parent = self
                self._children_name_map["rps"] = "rps"
                self._children_yang_names.add("rps")

                self.traffic = AutoRp.Standby.CandidateRp.Traffic()
                self.traffic.parent = self
                self._children_name_map["traffic"] = "traffic"
                self._children_yang_names.add("traffic")
                self._segment_path = lambda: "candidate-rp"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/%s" % self._segment_path()


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"rp" : ("rp", AutoRp.Standby.CandidateRp.Rps.Rp)}

                    self.rp = YList(self)
                    self._segment_path = lambda: "rps"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/candidate-rp/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(AutoRp.Standby.CandidateRp.Rps, [], name, value)


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
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.access_list_name = YLeaf(YType.str, "access-list-name")

                        self.announce_period = YLeaf(YType.int32, "announce-period")

                        self.candidate_rp_address = YLeaf(YType.str, "candidate-rp-address")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.protocol_mode = YLeaf(YType.enumeration, "protocol-mode")

                        self.protocol_mode_xr = YLeaf(YType.enumeration, "protocol-mode-xr")

                        self.ttl = YLeaf(YType.int32, "ttl")
                        self._segment_path = lambda: "rp"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/candidate-rp/rps/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(AutoRp.Standby.CandidateRp.Rps.Rp, ['access_list_name', 'announce_period', 'candidate_rp_address', 'interface_name', 'protocol_mode', 'protocol_mode_xr', 'ttl'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.active_sent_packets = YLeaf(YType.uint32, "active-sent-packets")

                    self.standby_sent_packets = YLeaf(YType.uint32, "standby-sent-packets")
                    self._segment_path = lambda: "traffic"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/candidate-rp/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(AutoRp.Standby.CandidateRp.Traffic, ['active_sent_packets', 'standby_sent_packets'], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"rp-addresses" : ("rp_addresses", AutoRp.Standby.MappingAgent.RpAddresses), "summary" : ("summary", AutoRp.Standby.MappingAgent.Summary), "traffic" : ("traffic", AutoRp.Standby.MappingAgent.Traffic)}
                self._child_list_classes = {}

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
                self._segment_path = lambda: "mapping-agent"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/%s" % self._segment_path()


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"rp-address" : ("rp_address", AutoRp.Standby.MappingAgent.RpAddresses.RpAddress)}

                    self.rp_address = YList(self)
                    self._segment_path = lambda: "rp-addresses"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/mapping-agent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(AutoRp.Standby.MappingAgent.RpAddresses, [], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {"range" : ("range", AutoRp.Standby.MappingAgent.RpAddresses.RpAddress.Range)}

                        self.rp_address = YLeaf(YType.str, "rp-address")

                        self.expiry_time = YLeaf(YType.uint64, "expiry-time")

                        self.pim_version = YLeaf(YType.uint8, "pim-version")

                        self.rp_address_xr = YLeaf(YType.str, "rp-address-xr")

                        self.range = YList(self)
                        self._segment_path = lambda: "rp-address" + "[rp-address='" + self.rp_address.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/mapping-agent/rp-addresses/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(AutoRp.Standby.MappingAgent.RpAddresses.RpAddress, ['rp_address', 'expiry_time', 'pim_version', 'rp_address_xr'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.check_point_object_id = YLeaf(YType.uint32, "check-point-object-id")

                            self.create_type = YLeaf(YType.uint8, "create-type")

                            self.is_advertised = YLeaf(YType.boolean, "is-advertised")

                            self.prefix = YLeaf(YType.str, "prefix")

                            self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                            self.protocol_mode = YLeaf(YType.enumeration, "protocol-mode")

                            self.uptime = YLeaf(YType.uint64, "uptime")
                            self._segment_path = lambda: "range"

                        def __setattr__(self, name, value):
                            self._perform_setattr(AutoRp.Standby.MappingAgent.RpAddresses.RpAddress.Range, ['check_point_object_id', 'create_type', 'is_advertised', 'prefix', 'prefix_length', 'protocol_mode', 'uptime'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.cache_count = YLeaf(YType.uint32, "cache-count")

                    self.cache_limit = YLeaf(YType.uint32, "cache-limit")

                    self.is_maximum_disabled = YLeaf(YType.boolean, "is-maximum-disabled")
                    self._segment_path = lambda: "summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/mapping-agent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(AutoRp.Standby.MappingAgent.Summary, ['cache_count', 'cache_limit', 'is_maximum_disabled'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.active_received_packets = YLeaf(YType.uint32, "active-received-packets")

                    self.active_sent_packets = YLeaf(YType.uint32, "active-sent-packets")

                    self.standby_received_packets = YLeaf(YType.uint32, "standby-received-packets")

                    self.standby_sent_packets = YLeaf(YType.uint32, "standby-sent-packets")
                    self._segment_path = lambda: "traffic"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/mapping-agent/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(AutoRp.Standby.MappingAgent.Traffic, ['active_received_packets', 'active_sent_packets', 'standby_received_packets', 'standby_sent_packets'], name, value)

    def clone_ptr(self):
        self._top_entity = AutoRp()
        return self._top_entity


""" Cisco_IOS_XR_ipv4_autorp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-autorp package operational data.

This module contains definitions
for the following management objects\:
  auto\-rp\: AutoRP operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AutorpProtocolMode(Enum):
    """
    AutorpProtocolMode (Enum Class)

    Autorp protocol mode

    .. data:: sparse = 0

    	sparse

    .. data:: bidirectional = 1

    	bidirectional

    """

    sparse = Enum.YLeaf(0, "sparse")

    bidirectional = Enum.YLeaf(1, "bidirectional")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
        return meta._meta_table['AutorpProtocolMode']



class AutoRp(_Entity_):
    """
    AutoRP operational data
    
    .. attribute:: standby
    
    	Standby Process
    	**type**\:  :py:class:`Standby <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby>`
    
    	**config**\: False
    
    .. attribute:: active
    
    	Active Process
    	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active>`
    
    	**config**\: False
    
    

    """

    _prefix = 'ipv4-autorp-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(AutoRp, self).__init__()
        self._top_entity = None

        self.yang_name = "auto-rp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-autorp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("standby", ("standby", AutoRp.Standby)), ("active", ("active", AutoRp.Active))])
        self._leafs = OrderedDict()

        self.standby = AutoRp.Standby()
        self.standby.parent = self
        self._children_name_map["standby"] = "standby"

        self.active = AutoRp.Active()
        self.active.parent = self
        self._children_name_map["active"] = "active"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(AutoRp, [], name, value)


    class Standby(_Entity_):
        """
        Standby Process
        
        .. attribute:: candidate_rp
        
        	AutoRP Candidate RP
        	**type**\:  :py:class:`CandidateRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.CandidateRp>`
        
        	**config**\: False
        
        .. attribute:: mapping_agent
        
        	AutoRP Mapping Agent Table
        	**type**\:  :py:class:`MappingAgent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.MappingAgent>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ipv4-autorp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(AutoRp.Standby, self).__init__()

            self.yang_name = "standby"
            self.yang_parent_name = "auto-rp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("candidate-rp", ("candidate_rp", AutoRp.Standby.CandidateRp)), ("mapping-agent", ("mapping_agent", AutoRp.Standby.MappingAgent))])
            self._leafs = OrderedDict()

            self.candidate_rp = AutoRp.Standby.CandidateRp()
            self.candidate_rp.parent = self
            self._children_name_map["candidate_rp"] = "candidate-rp"

            self.mapping_agent = AutoRp.Standby.MappingAgent()
            self.mapping_agent.parent = self
            self._children_name_map["mapping_agent"] = "mapping-agent"
            self._segment_path = lambda: "standby"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(AutoRp.Standby, [], name, value)


        class CandidateRp(_Entity_):
            """
            AutoRP Candidate RP
            
            .. attribute:: traffic
            
            	AutoRP Candidate Traffic Counters
            	**type**\:  :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.CandidateRp.Traffic>`
            
            	**config**\: False
            
            .. attribute:: rps
            
            	AutoRP Candidate RP Table
            	**type**\:  :py:class:`Rps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.CandidateRp.Rps>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ipv4-autorp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(AutoRp.Standby.CandidateRp, self).__init__()

                self.yang_name = "candidate-rp"
                self.yang_parent_name = "standby"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("traffic", ("traffic", AutoRp.Standby.CandidateRp.Traffic)), ("rps", ("rps", AutoRp.Standby.CandidateRp.Rps))])
                self._leafs = OrderedDict()

                self.traffic = AutoRp.Standby.CandidateRp.Traffic()
                self.traffic.parent = self
                self._children_name_map["traffic"] = "traffic"

                self.rps = AutoRp.Standby.CandidateRp.Rps()
                self.rps.parent = self
                self._children_name_map["rps"] = "rps"
                self._segment_path = lambda: "candidate-rp"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AutoRp.Standby.CandidateRp, [], name, value)


            class Traffic(_Entity_):
                """
                AutoRP Candidate Traffic Counters
                
                .. attribute:: active_sent_packets
                
                	Number of packets sent in active role
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: standby_sent_packets
                
                	Number of packets dropped in send path in standby role
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AutoRp.Standby.CandidateRp.Traffic, self).__init__()

                    self.yang_name = "traffic"
                    self.yang_parent_name = "candidate-rp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('active_sent_packets', (YLeaf(YType.uint32, 'active-sent-packets'), ['int'])),
                        ('standby_sent_packets', (YLeaf(YType.uint32, 'standby-sent-packets'), ['int'])),
                    ])
                    self.active_sent_packets = None
                    self.standby_sent_packets = None
                    self._segment_path = lambda: "traffic"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/candidate-rp/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AutoRp.Standby.CandidateRp.Traffic, ['active_sent_packets', 'standby_sent_packets'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                    return meta._meta_table['AutoRp.Standby.CandidateRp.Traffic']['meta_info']


            class Rps(_Entity_):
                """
                AutoRP Candidate RP Table
                
                .. attribute:: rp
                
                	AutoRP Candidate RP Entry
                	**type**\: list of  		 :py:class:`Rp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.CandidateRp.Rps.Rp>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AutoRp.Standby.CandidateRp.Rps, self).__init__()

                    self.yang_name = "rps"
                    self.yang_parent_name = "candidate-rp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("rp", ("rp", AutoRp.Standby.CandidateRp.Rps.Rp))])
                    self._leafs = OrderedDict()

                    self.rp = YList(self)
                    self._segment_path = lambda: "rps"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/candidate-rp/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AutoRp.Standby.CandidateRp.Rps, [], name, value)


                class Rp(_Entity_):
                    """
                    AutoRP Candidate RP Entry
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: protocol_mode
                    
                    	Protocol Mode
                    	**type**\:  :py:class:`AutoRpProtocolMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_datatypes.AutoRpProtocolMode>`
                    
                    	**config**\: False
                    
                    .. attribute:: access_list_name
                    
                    	ACL Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: candidate_rp_address
                    
                    	Candidate RP IP Address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: ttl
                    
                    	TTL
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: announce_period
                    
                    	Announce Period
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: protocol_mode_xr
                    
                    	Protocol Mode
                    	**type**\:  :py:class:`AutorpProtocolMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutorpProtocolMode>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv4-autorp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(AutoRp.Standby.CandidateRp.Rps.Rp, self).__init__()

                        self.yang_name = "rp"
                        self.yang_parent_name = "rps"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('protocol_mode', (YLeaf(YType.enumeration, 'protocol-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_datatypes', 'AutoRpProtocolMode', '')])),
                            ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                            ('candidate_rp_address', (YLeaf(YType.str, 'candidate-rp-address'), ['str'])),
                            ('ttl', (YLeaf(YType.int32, 'ttl'), ['int'])),
                            ('announce_period', (YLeaf(YType.int32, 'announce-period'), ['int'])),
                            ('protocol_mode_xr', (YLeaf(YType.enumeration, 'protocol-mode-xr'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutorpProtocolMode', '')])),
                        ])
                        self.interface_name = None
                        self.protocol_mode = None
                        self.access_list_name = None
                        self.candidate_rp_address = None
                        self.ttl = None
                        self.announce_period = None
                        self.protocol_mode_xr = None
                        self._segment_path = lambda: "rp"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/candidate-rp/rps/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AutoRp.Standby.CandidateRp.Rps.Rp, ['interface_name', 'protocol_mode', 'access_list_name', 'candidate_rp_address', 'ttl', 'announce_period', 'protocol_mode_xr'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                        return meta._meta_table['AutoRp.Standby.CandidateRp.Rps.Rp']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                    return meta._meta_table['AutoRp.Standby.CandidateRp.Rps']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                return meta._meta_table['AutoRp.Standby.CandidateRp']['meta_info']


        class MappingAgent(_Entity_):
            """
            AutoRP Mapping Agent Table
            
            .. attribute:: traffic
            
            	AutoRP Mapping Agent Traffic Counters
            	**type**\:  :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.MappingAgent.Traffic>`
            
            	**config**\: False
            
            .. attribute:: rp_addresses
            
            	AutoRP Mapping Agent Table Entries
            	**type**\:  :py:class:`RpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.MappingAgent.RpAddresses>`
            
            	**config**\: False
            
            .. attribute:: summary
            
            	AutoRP Mapping Agent Summary Information
            	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.MappingAgent.Summary>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ipv4-autorp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(AutoRp.Standby.MappingAgent, self).__init__()

                self.yang_name = "mapping-agent"
                self.yang_parent_name = "standby"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("traffic", ("traffic", AutoRp.Standby.MappingAgent.Traffic)), ("rp-addresses", ("rp_addresses", AutoRp.Standby.MappingAgent.RpAddresses)), ("summary", ("summary", AutoRp.Standby.MappingAgent.Summary))])
                self._leafs = OrderedDict()

                self.traffic = AutoRp.Standby.MappingAgent.Traffic()
                self.traffic.parent = self
                self._children_name_map["traffic"] = "traffic"

                self.rp_addresses = AutoRp.Standby.MappingAgent.RpAddresses()
                self.rp_addresses.parent = self
                self._children_name_map["rp_addresses"] = "rp-addresses"

                self.summary = AutoRp.Standby.MappingAgent.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
                self._segment_path = lambda: "mapping-agent"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AutoRp.Standby.MappingAgent, [], name, value)


            class Traffic(_Entity_):
                """
                AutoRP Mapping Agent Traffic Counters
                
                .. attribute:: active_sent_packets
                
                	Number of packets sent in active role
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: standby_sent_packets
                
                	Number of packets dropped in send path in standby role
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: active_received_packets
                
                	Number of packets received in active role
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: standby_received_packets
                
                	Number of packets dropped in receive path in standby role
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AutoRp.Standby.MappingAgent.Traffic, self).__init__()

                    self.yang_name = "traffic"
                    self.yang_parent_name = "mapping-agent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('active_sent_packets', (YLeaf(YType.uint32, 'active-sent-packets'), ['int'])),
                        ('standby_sent_packets', (YLeaf(YType.uint32, 'standby-sent-packets'), ['int'])),
                        ('active_received_packets', (YLeaf(YType.uint32, 'active-received-packets'), ['int'])),
                        ('standby_received_packets', (YLeaf(YType.uint32, 'standby-received-packets'), ['int'])),
                    ])
                    self.active_sent_packets = None
                    self.standby_sent_packets = None
                    self.active_received_packets = None
                    self.standby_received_packets = None
                    self._segment_path = lambda: "traffic"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/mapping-agent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AutoRp.Standby.MappingAgent.Traffic, ['active_sent_packets', 'standby_sent_packets', 'active_received_packets', 'standby_received_packets'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                    return meta._meta_table['AutoRp.Standby.MappingAgent.Traffic']['meta_info']


            class RpAddresses(_Entity_):
                """
                AutoRP Mapping Agent Table Entries
                
                .. attribute:: rp_address
                
                	AutoRP Mapping Agent Entry
                	**type**\: list of  		 :py:class:`RpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.MappingAgent.RpAddresses.RpAddress>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AutoRp.Standby.MappingAgent.RpAddresses, self).__init__()

                    self.yang_name = "rp-addresses"
                    self.yang_parent_name = "mapping-agent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("rp-address", ("rp_address", AutoRp.Standby.MappingAgent.RpAddresses.RpAddress))])
                    self._leafs = OrderedDict()

                    self.rp_address = YList(self)
                    self._segment_path = lambda: "rp-addresses"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/mapping-agent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AutoRp.Standby.MappingAgent.RpAddresses, [], name, value)


                class RpAddress(_Entity_):
                    """
                    AutoRP Mapping Agent Entry
                    
                    .. attribute:: rp_address  (key)
                    
                    	RP Address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: rp_address_xr
                    
                    	Candidate\-RP address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: expiry_time
                    
                    	Time for expiration in seconds
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: pim_version
                    
                    	PIM version of the CRP
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: range
                    
                    	Array of ranges
                    	**type**\: list of  		 :py:class:`Range <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.MappingAgent.RpAddresses.RpAddress.Range>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv4-autorp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(AutoRp.Standby.MappingAgent.RpAddresses.RpAddress, self).__init__()

                        self.yang_name = "rp-address"
                        self.yang_parent_name = "rp-addresses"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['rp_address']
                        self._child_classes = OrderedDict([("range", ("range", AutoRp.Standby.MappingAgent.RpAddresses.RpAddress.Range))])
                        self._leafs = OrderedDict([
                            ('rp_address', (YLeaf(YType.str, 'rp-address'), ['str'])),
                            ('rp_address_xr', (YLeaf(YType.str, 'rp-address-xr'), ['str'])),
                            ('expiry_time', (YLeaf(YType.uint64, 'expiry-time'), ['int'])),
                            ('pim_version', (YLeaf(YType.uint8, 'pim-version'), ['int'])),
                        ])
                        self.rp_address = None
                        self.rp_address_xr = None
                        self.expiry_time = None
                        self.pim_version = None

                        self.range = YList(self)
                        self._segment_path = lambda: "rp-address" + "[rp-address='" + str(self.rp_address) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/mapping-agent/rp-addresses/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AutoRp.Standby.MappingAgent.RpAddresses.RpAddress, ['rp_address', 'rp_address_xr', 'expiry_time', 'pim_version'], name, value)


                    class Range(_Entity_):
                        """
                        Array of ranges
                        
                        .. attribute:: prefix
                        
                        	Prefix of the range
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: prefix_length
                        
                        	Prefix length of the range
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: protocol_mode
                        
                        	Protocol Mode
                        	**type**\:  :py:class:`AutorpProtocolMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutorpProtocolMode>`
                        
                        	**config**\: False
                        
                        .. attribute:: is_advertised
                        
                        	Is this entry advertised ?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: create_type
                        
                        	Source of the entry
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: check_point_object_id
                        
                        	Checkpoint object id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: uptime
                        
                        	Uptime in seconds
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'ipv4-autorp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(AutoRp.Standby.MappingAgent.RpAddresses.RpAddress.Range, self).__init__()

                            self.yang_name = "range"
                            self.yang_parent_name = "rp-address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                                ('protocol_mode', (YLeaf(YType.enumeration, 'protocol-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutorpProtocolMode', '')])),
                                ('is_advertised', (YLeaf(YType.boolean, 'is-advertised'), ['bool'])),
                                ('create_type', (YLeaf(YType.uint8, 'create-type'), ['int'])),
                                ('check_point_object_id', (YLeaf(YType.uint32, 'check-point-object-id'), ['int'])),
                                ('uptime', (YLeaf(YType.uint64, 'uptime'), ['int'])),
                            ])
                            self.prefix = None
                            self.prefix_length = None
                            self.protocol_mode = None
                            self.is_advertised = None
                            self.create_type = None
                            self.check_point_object_id = None
                            self.uptime = None
                            self._segment_path = lambda: "range"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(AutoRp.Standby.MappingAgent.RpAddresses.RpAddress.Range, ['prefix', 'prefix_length', 'protocol_mode', 'is_advertised', 'create_type', 'check_point_object_id', 'uptime'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                            return meta._meta_table['AutoRp.Standby.MappingAgent.RpAddresses.RpAddress.Range']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                        return meta._meta_table['AutoRp.Standby.MappingAgent.RpAddresses.RpAddress']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                    return meta._meta_table['AutoRp.Standby.MappingAgent.RpAddresses']['meta_info']


            class Summary(_Entity_):
                """
                AutoRP Mapping Agent Summary Information
                
                .. attribute:: is_maximum_disabled
                
                	Is maximum enforcement disabled ?
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: cache_limit
                
                	Maximum group to RP mapping entries allowed
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: cache_count
                
                	Number of group to RP mapping entries in the cache
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AutoRp.Standby.MappingAgent.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "mapping-agent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('is_maximum_disabled', (YLeaf(YType.boolean, 'is-maximum-disabled'), ['bool'])),
                        ('cache_limit', (YLeaf(YType.uint32, 'cache-limit'), ['int'])),
                        ('cache_count', (YLeaf(YType.uint32, 'cache-count'), ['int'])),
                    ])
                    self.is_maximum_disabled = None
                    self.cache_limit = None
                    self.cache_count = None
                    self._segment_path = lambda: "summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/standby/mapping-agent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AutoRp.Standby.MappingAgent.Summary, ['is_maximum_disabled', 'cache_limit', 'cache_count'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                    return meta._meta_table['AutoRp.Standby.MappingAgent.Summary']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                return meta._meta_table['AutoRp.Standby.MappingAgent']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
            return meta._meta_table['AutoRp.Standby']['meta_info']


    class Active(_Entity_):
        """
        Active Process
        
        .. attribute:: candidate_rp
        
        	AutoRP Candidate RP
        	**type**\:  :py:class:`CandidateRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.CandidateRp>`
        
        	**config**\: False
        
        .. attribute:: mapping_agent
        
        	AutoRP Mapping Agent Table
        	**type**\:  :py:class:`MappingAgent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.MappingAgent>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ipv4-autorp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(AutoRp.Active, self).__init__()

            self.yang_name = "active"
            self.yang_parent_name = "auto-rp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("candidate-rp", ("candidate_rp", AutoRp.Active.CandidateRp)), ("mapping-agent", ("mapping_agent", AutoRp.Active.MappingAgent))])
            self._leafs = OrderedDict()

            self.candidate_rp = AutoRp.Active.CandidateRp()
            self.candidate_rp.parent = self
            self._children_name_map["candidate_rp"] = "candidate-rp"

            self.mapping_agent = AutoRp.Active.MappingAgent()
            self.mapping_agent.parent = self
            self._children_name_map["mapping_agent"] = "mapping-agent"
            self._segment_path = lambda: "active"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(AutoRp.Active, [], name, value)


        class CandidateRp(_Entity_):
            """
            AutoRP Candidate RP
            
            .. attribute:: traffic
            
            	AutoRP Candidate Traffic Counters
            	**type**\:  :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.CandidateRp.Traffic>`
            
            	**config**\: False
            
            .. attribute:: rps
            
            	AutoRP Candidate RP Table
            	**type**\:  :py:class:`Rps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.CandidateRp.Rps>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ipv4-autorp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(AutoRp.Active.CandidateRp, self).__init__()

                self.yang_name = "candidate-rp"
                self.yang_parent_name = "active"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("traffic", ("traffic", AutoRp.Active.CandidateRp.Traffic)), ("rps", ("rps", AutoRp.Active.CandidateRp.Rps))])
                self._leafs = OrderedDict()

                self.traffic = AutoRp.Active.CandidateRp.Traffic()
                self.traffic.parent = self
                self._children_name_map["traffic"] = "traffic"

                self.rps = AutoRp.Active.CandidateRp.Rps()
                self.rps.parent = self
                self._children_name_map["rps"] = "rps"
                self._segment_path = lambda: "candidate-rp"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AutoRp.Active.CandidateRp, [], name, value)


            class Traffic(_Entity_):
                """
                AutoRP Candidate Traffic Counters
                
                .. attribute:: active_sent_packets
                
                	Number of packets sent in active role
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: standby_sent_packets
                
                	Number of packets dropped in send path in standby role
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AutoRp.Active.CandidateRp.Traffic, self).__init__()

                    self.yang_name = "traffic"
                    self.yang_parent_name = "candidate-rp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('active_sent_packets', (YLeaf(YType.uint32, 'active-sent-packets'), ['int'])),
                        ('standby_sent_packets', (YLeaf(YType.uint32, 'standby-sent-packets'), ['int'])),
                    ])
                    self.active_sent_packets = None
                    self.standby_sent_packets = None
                    self._segment_path = lambda: "traffic"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/candidate-rp/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AutoRp.Active.CandidateRp.Traffic, ['active_sent_packets', 'standby_sent_packets'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                    return meta._meta_table['AutoRp.Active.CandidateRp.Traffic']['meta_info']


            class Rps(_Entity_):
                """
                AutoRP Candidate RP Table
                
                .. attribute:: rp
                
                	AutoRP Candidate RP Entry
                	**type**\: list of  		 :py:class:`Rp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.CandidateRp.Rps.Rp>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AutoRp.Active.CandidateRp.Rps, self).__init__()

                    self.yang_name = "rps"
                    self.yang_parent_name = "candidate-rp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("rp", ("rp", AutoRp.Active.CandidateRp.Rps.Rp))])
                    self._leafs = OrderedDict()

                    self.rp = YList(self)
                    self._segment_path = lambda: "rps"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/candidate-rp/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AutoRp.Active.CandidateRp.Rps, [], name, value)


                class Rp(_Entity_):
                    """
                    AutoRP Candidate RP Entry
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: protocol_mode
                    
                    	Protocol Mode
                    	**type**\:  :py:class:`AutoRpProtocolMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_datatypes.AutoRpProtocolMode>`
                    
                    	**config**\: False
                    
                    .. attribute:: access_list_name
                    
                    	ACL Name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: candidate_rp_address
                    
                    	Candidate RP IP Address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: ttl
                    
                    	TTL
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: announce_period
                    
                    	Announce Period
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    .. attribute:: protocol_mode_xr
                    
                    	Protocol Mode
                    	**type**\:  :py:class:`AutorpProtocolMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutorpProtocolMode>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv4-autorp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(AutoRp.Active.CandidateRp.Rps.Rp, self).__init__()

                        self.yang_name = "rp"
                        self.yang_parent_name = "rps"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('protocol_mode', (YLeaf(YType.enumeration, 'protocol-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_datatypes', 'AutoRpProtocolMode', '')])),
                            ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                            ('candidate_rp_address', (YLeaf(YType.str, 'candidate-rp-address'), ['str'])),
                            ('ttl', (YLeaf(YType.int32, 'ttl'), ['int'])),
                            ('announce_period', (YLeaf(YType.int32, 'announce-period'), ['int'])),
                            ('protocol_mode_xr', (YLeaf(YType.enumeration, 'protocol-mode-xr'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutorpProtocolMode', '')])),
                        ])
                        self.interface_name = None
                        self.protocol_mode = None
                        self.access_list_name = None
                        self.candidate_rp_address = None
                        self.ttl = None
                        self.announce_period = None
                        self.protocol_mode_xr = None
                        self._segment_path = lambda: "rp"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/candidate-rp/rps/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AutoRp.Active.CandidateRp.Rps.Rp, ['interface_name', 'protocol_mode', 'access_list_name', 'candidate_rp_address', 'ttl', 'announce_period', 'protocol_mode_xr'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                        return meta._meta_table['AutoRp.Active.CandidateRp.Rps.Rp']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                    return meta._meta_table['AutoRp.Active.CandidateRp.Rps']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                return meta._meta_table['AutoRp.Active.CandidateRp']['meta_info']


        class MappingAgent(_Entity_):
            """
            AutoRP Mapping Agent Table
            
            .. attribute:: traffic
            
            	AutoRP Mapping Agent Traffic Counters
            	**type**\:  :py:class:`Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.MappingAgent.Traffic>`
            
            	**config**\: False
            
            .. attribute:: rp_addresses
            
            	AutoRP Mapping Agent Table Entries
            	**type**\:  :py:class:`RpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.MappingAgent.RpAddresses>`
            
            	**config**\: False
            
            .. attribute:: summary
            
            	AutoRP Mapping Agent Summary Information
            	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.MappingAgent.Summary>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ipv4-autorp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(AutoRp.Active.MappingAgent, self).__init__()

                self.yang_name = "mapping-agent"
                self.yang_parent_name = "active"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("traffic", ("traffic", AutoRp.Active.MappingAgent.Traffic)), ("rp-addresses", ("rp_addresses", AutoRp.Active.MappingAgent.RpAddresses)), ("summary", ("summary", AutoRp.Active.MappingAgent.Summary))])
                self._leafs = OrderedDict()

                self.traffic = AutoRp.Active.MappingAgent.Traffic()
                self.traffic.parent = self
                self._children_name_map["traffic"] = "traffic"

                self.rp_addresses = AutoRp.Active.MappingAgent.RpAddresses()
                self.rp_addresses.parent = self
                self._children_name_map["rp_addresses"] = "rp-addresses"

                self.summary = AutoRp.Active.MappingAgent.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
                self._segment_path = lambda: "mapping-agent"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AutoRp.Active.MappingAgent, [], name, value)


            class Traffic(_Entity_):
                """
                AutoRP Mapping Agent Traffic Counters
                
                .. attribute:: active_sent_packets
                
                	Number of packets sent in active role
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: standby_sent_packets
                
                	Number of packets dropped in send path in standby role
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: active_received_packets
                
                	Number of packets received in active role
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: standby_received_packets
                
                	Number of packets dropped in receive path in standby role
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AutoRp.Active.MappingAgent.Traffic, self).__init__()

                    self.yang_name = "traffic"
                    self.yang_parent_name = "mapping-agent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('active_sent_packets', (YLeaf(YType.uint32, 'active-sent-packets'), ['int'])),
                        ('standby_sent_packets', (YLeaf(YType.uint32, 'standby-sent-packets'), ['int'])),
                        ('active_received_packets', (YLeaf(YType.uint32, 'active-received-packets'), ['int'])),
                        ('standby_received_packets', (YLeaf(YType.uint32, 'standby-received-packets'), ['int'])),
                    ])
                    self.active_sent_packets = None
                    self.standby_sent_packets = None
                    self.active_received_packets = None
                    self.standby_received_packets = None
                    self._segment_path = lambda: "traffic"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/mapping-agent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AutoRp.Active.MappingAgent.Traffic, ['active_sent_packets', 'standby_sent_packets', 'active_received_packets', 'standby_received_packets'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                    return meta._meta_table['AutoRp.Active.MappingAgent.Traffic']['meta_info']


            class RpAddresses(_Entity_):
                """
                AutoRP Mapping Agent Table Entries
                
                .. attribute:: rp_address
                
                	AutoRP Mapping Agent Entry
                	**type**\: list of  		 :py:class:`RpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.MappingAgent.RpAddresses.RpAddress>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AutoRp.Active.MappingAgent.RpAddresses, self).__init__()

                    self.yang_name = "rp-addresses"
                    self.yang_parent_name = "mapping-agent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("rp-address", ("rp_address", AutoRp.Active.MappingAgent.RpAddresses.RpAddress))])
                    self._leafs = OrderedDict()

                    self.rp_address = YList(self)
                    self._segment_path = lambda: "rp-addresses"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/mapping-agent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AutoRp.Active.MappingAgent.RpAddresses, [], name, value)


                class RpAddress(_Entity_):
                    """
                    AutoRP Mapping Agent Entry
                    
                    .. attribute:: rp_address  (key)
                    
                    	RP Address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: rp_address_xr
                    
                    	Candidate\-RP address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: expiry_time
                    
                    	Time for expiration in seconds
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: pim_version
                    
                    	PIM version of the CRP
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: range
                    
                    	Array of ranges
                    	**type**\: list of  		 :py:class:`Range <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.MappingAgent.RpAddresses.RpAddress.Range>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ipv4-autorp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(AutoRp.Active.MappingAgent.RpAddresses.RpAddress, self).__init__()

                        self.yang_name = "rp-address"
                        self.yang_parent_name = "rp-addresses"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['rp_address']
                        self._child_classes = OrderedDict([("range", ("range", AutoRp.Active.MappingAgent.RpAddresses.RpAddress.Range))])
                        self._leafs = OrderedDict([
                            ('rp_address', (YLeaf(YType.str, 'rp-address'), ['str'])),
                            ('rp_address_xr', (YLeaf(YType.str, 'rp-address-xr'), ['str'])),
                            ('expiry_time', (YLeaf(YType.uint64, 'expiry-time'), ['int'])),
                            ('pim_version', (YLeaf(YType.uint8, 'pim-version'), ['int'])),
                        ])
                        self.rp_address = None
                        self.rp_address_xr = None
                        self.expiry_time = None
                        self.pim_version = None

                        self.range = YList(self)
                        self._segment_path = lambda: "rp-address" + "[rp-address='" + str(self.rp_address) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/mapping-agent/rp-addresses/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AutoRp.Active.MappingAgent.RpAddresses.RpAddress, ['rp_address', 'rp_address_xr', 'expiry_time', 'pim_version'], name, value)


                    class Range(_Entity_):
                        """
                        Array of ranges
                        
                        .. attribute:: prefix
                        
                        	Prefix of the range
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: prefix_length
                        
                        	Prefix length of the range
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: protocol_mode
                        
                        	Protocol Mode
                        	**type**\:  :py:class:`AutorpProtocolMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutorpProtocolMode>`
                        
                        	**config**\: False
                        
                        .. attribute:: is_advertised
                        
                        	Is this entry advertised ?
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: create_type
                        
                        	Source of the entry
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: check_point_object_id
                        
                        	Checkpoint object id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: uptime
                        
                        	Uptime in seconds
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'ipv4-autorp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(AutoRp.Active.MappingAgent.RpAddresses.RpAddress.Range, self).__init__()

                            self.yang_name = "range"
                            self.yang_parent_name = "rp-address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                                ('protocol_mode', (YLeaf(YType.enumeration, 'protocol-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutorpProtocolMode', '')])),
                                ('is_advertised', (YLeaf(YType.boolean, 'is-advertised'), ['bool'])),
                                ('create_type', (YLeaf(YType.uint8, 'create-type'), ['int'])),
                                ('check_point_object_id', (YLeaf(YType.uint32, 'check-point-object-id'), ['int'])),
                                ('uptime', (YLeaf(YType.uint64, 'uptime'), ['int'])),
                            ])
                            self.prefix = None
                            self.prefix_length = None
                            self.protocol_mode = None
                            self.is_advertised = None
                            self.create_type = None
                            self.check_point_object_id = None
                            self.uptime = None
                            self._segment_path = lambda: "range"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(AutoRp.Active.MappingAgent.RpAddresses.RpAddress.Range, ['prefix', 'prefix_length', 'protocol_mode', 'is_advertised', 'create_type', 'check_point_object_id', 'uptime'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                            return meta._meta_table['AutoRp.Active.MappingAgent.RpAddresses.RpAddress.Range']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                        return meta._meta_table['AutoRp.Active.MappingAgent.RpAddresses.RpAddress']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                    return meta._meta_table['AutoRp.Active.MappingAgent.RpAddresses']['meta_info']


            class Summary(_Entity_):
                """
                AutoRP Mapping Agent Summary Information
                
                .. attribute:: is_maximum_disabled
                
                	Is maximum enforcement disabled ?
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: cache_limit
                
                	Maximum group to RP mapping entries allowed
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: cache_count
                
                	Number of group to RP mapping entries in the cache
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(AutoRp.Active.MappingAgent.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "mapping-agent"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('is_maximum_disabled', (YLeaf(YType.boolean, 'is-maximum-disabled'), ['bool'])),
                        ('cache_limit', (YLeaf(YType.uint32, 'cache-limit'), ['int'])),
                        ('cache_count', (YLeaf(YType.uint32, 'cache-count'), ['int'])),
                    ])
                    self.is_maximum_disabled = None
                    self.cache_limit = None
                    self.cache_count = None
                    self._segment_path = lambda: "summary"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/active/mapping-agent/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AutoRp.Active.MappingAgent.Summary, ['is_maximum_disabled', 'cache_limit', 'cache_count'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                    return meta._meta_table['AutoRp.Active.MappingAgent.Summary']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                return meta._meta_table['AutoRp.Active.MappingAgent']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
            return meta._meta_table['AutoRp.Active']['meta_info']

    def clone_ptr(self):
        self._top_entity = AutoRp()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
        return meta._meta_table['AutoRp']['meta_info']



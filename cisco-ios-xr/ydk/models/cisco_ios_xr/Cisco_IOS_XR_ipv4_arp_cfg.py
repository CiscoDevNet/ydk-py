""" Cisco_IOS_XR_ipv4_arp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-arp package configuration.

This module contains definitions
for the following management objects\:
  arp\: ARP configuraiton
  iedge\-cfg\: iedge cfg
  arpgmp\: arpgmp
  arp\-redundancy\: arp redundancy

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ArpEncap(Enum):
    """
    ArpEncap (Enum Class)

    Arp encap

    .. data:: arpa = 1

    	Encapsulation type ARPA

    .. data:: srp = 4

    	Encapsulation type SRP

    .. data:: srpa = 5

    	Encapsulation type SRPA

    .. data:: srpb = 6

    	Encapsulation type SRPB

    """

    arpa = Enum.YLeaf(1, "arpa")

    srp = Enum.YLeaf(4, "srp")

    srpa = Enum.YLeaf(5, "srpa")

    srpb = Enum.YLeaf(6, "srpb")


class ArpEntry(Enum):
    """
    ArpEntry (Enum Class)

    Arp entry

    .. data:: static = 0

    	Static ARP entry type

    .. data:: alias = 1

    	Alias ARP entry type

    """

    static = Enum.YLeaf(0, "static")

    alias = Enum.YLeaf(1, "alias")



class Arp(Entity):
    """
    ARP configuraiton
    
    .. attribute:: max_entries
    
    	Configure maximum number of safe ARP entries per line card
    	**type**\: int
    
    	**range:** 1..256000
    
    .. attribute:: inner_cos
    
    	Configure inner cos values for arp packets
    	**type**\: int
    
    	**range:** 0..7
    
    .. attribute:: outer_cos
    
    	Configure outer cos values for arp packets
    	**type**\: int
    
    	**range:** 0..7
    
    

    """

    _prefix = 'ipv4-arp-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(Arp, self).__init__()
        self._top_entity = None

        self.yang_name = "arp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-arp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('max_entries', (YLeaf(YType.uint32, 'max-entries'), ['int'])),
            ('inner_cos', (YLeaf(YType.uint32, 'inner-cos'), ['int'])),
            ('outer_cos', (YLeaf(YType.uint32, 'outer-cos'), ['int'])),
        ])
        self.max_entries = None
        self.inner_cos = None
        self.outer_cos = None
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-arp-cfg:arp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Arp, ['max_entries', 'inner_cos', 'outer_cos'], name, value)

    def clone_ptr(self):
        self._top_entity = Arp()
        return self._top_entity

class IedgeCfg(Entity):
    """
    iedge cfg
    
    .. attribute:: subscriber_uncond_proxy
    
    	ARP Subscriber Enable Unconditional Proxy ARP
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: subscriber_scale_mode
    
    	ARP Subscriber Scale Mode Configuration
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'ipv4-arp-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(IedgeCfg, self).__init__()
        self._top_entity = None

        self.yang_name = "iedge-cfg"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-arp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('subscriber_uncond_proxy', (YLeaf(YType.empty, 'subscriber-uncond-proxy'), ['Empty'])),
            ('subscriber_scale_mode', (YLeaf(YType.empty, 'subscriber-scale-mode'), ['Empty'])),
        ])
        self.subscriber_uncond_proxy = None
        self.subscriber_scale_mode = None
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-arp-cfg:iedge-cfg"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(IedgeCfg, ['subscriber_uncond_proxy', 'subscriber_scale_mode'], name, value)

    def clone_ptr(self):
        self._top_entity = IedgeCfg()
        return self._top_entity

class Arpgmp(Entity):
    """
    arpgmp
    
    .. attribute:: vrf
    
    	Per VRF configuration, for the default VRF use 'default'
    	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.Arpgmp.Vrf>`
    
    

    """

    _prefix = 'ipv4-arp-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(Arpgmp, self).__init__()
        self._top_entity = None

        self.yang_name = "arpgmp"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-arp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vrf", ("vrf", Arpgmp.Vrf))])
        self._leafs = OrderedDict()

        self.vrf = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-arp-cfg:arpgmp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Arpgmp, [], name, value)


    class Vrf(Entity):
        """
        Per VRF configuration, for the default VRF use
        'default'
        
        .. attribute:: vrf_name  (key)
        
        	VRF name
        	**type**\: str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: entries
        
        	ARP static and alias entry configuration
        	**type**\:  :py:class:`Entries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.Arpgmp.Vrf.Entries>`
        
        

        """

        _prefix = 'ipv4-arp-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Arpgmp.Vrf, self).__init__()

            self.yang_name = "vrf"
            self.yang_parent_name = "arpgmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['vrf_name']
            self._child_classes = OrderedDict([("entries", ("entries", Arpgmp.Vrf.Entries))])
            self._leafs = OrderedDict([
                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
            ])
            self.vrf_name = None

            self.entries = Arpgmp.Vrf.Entries()
            self.entries.parent = self
            self._children_name_map["entries"] = "entries"
            self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-arp-cfg:arpgmp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Arpgmp.Vrf, ['vrf_name'], name, value)


        class Entries(Entity):
            """
            ARP static and alias entry configuration
            
            .. attribute:: entry
            
            	ARP static and alias entry configuration item
            	**type**\: list of  		 :py:class:`Entry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.Arpgmp.Vrf.Entries.Entry>`
            
            

            """

            _prefix = 'ipv4-arp-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Arpgmp.Vrf.Entries, self).__init__()

                self.yang_name = "entries"
                self.yang_parent_name = "vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("entry", ("entry", Arpgmp.Vrf.Entries.Entry))])
                self._leafs = OrderedDict()

                self.entry = YList(self)
                self._segment_path = lambda: "entries"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Arpgmp.Vrf.Entries, [], name, value)


            class Entry(Entity):
                """
                ARP static and alias entry configuration item
                
                .. attribute:: address  (key)
                
                	IP Address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: mac_address
                
                	MAC Address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: encapsulation
                
                	Encapsulation type
                	**type**\:  :py:class:`ArpEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpEncap>`
                
                .. attribute:: entry_type
                
                	Entry type
                	**type**\:  :py:class:`ArpEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpEntry>`
                
                .. attribute:: interface
                
                	Interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                

                """

                _prefix = 'ipv4-arp-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Arpgmp.Vrf.Entries.Entry, self).__init__()

                    self.yang_name = "entry"
                    self.yang_parent_name = "entries"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['address']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                        ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                        ('encapsulation', (YLeaf(YType.enumeration, 'encapsulation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpEncap', '')])),
                        ('entry_type', (YLeaf(YType.enumeration, 'entry-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg', 'ArpEntry', '')])),
                        ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                    ])
                    self.address = None
                    self.mac_address = None
                    self.encapsulation = None
                    self.entry_type = None
                    self.interface = None
                    self._segment_path = lambda: "entry" + "[address='" + str(self.address) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Arpgmp.Vrf.Entries.Entry, ['address', 'mac_address', 'encapsulation', 'entry_type', 'interface'], name, value)

    def clone_ptr(self):
        self._top_entity = Arpgmp()
        return self._top_entity

class ArpRedundancy(Entity):
    """
    arp redundancy
    
    .. attribute:: redundancy
    
    	Configure parameter for ARP Geo redundancy
    	**type**\:  :py:class:`Redundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'ipv4-arp-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(ArpRedundancy, self).__init__()
        self._top_entity = None

        self.yang_name = "arp-redundancy"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-arp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("redundancy", ("redundancy", ArpRedundancy.Redundancy))])
        self._leafs = OrderedDict()

        self.redundancy = None
        self._children_name_map["redundancy"] = "redundancy"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-arp-cfg:arp-redundancy"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ArpRedundancy, [], name, value)


    class Redundancy(Entity):
        """
        Configure parameter for ARP Geo redundancy
        
        .. attribute:: groups
        
        	Table of Group
        	**type**\:  :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups>`
        
        .. attribute:: enable
        
        	Enable Configure parameter for ARP Geo redundancy. Deletion of this object also causes deletion of all associated objects under ArpRedundancy
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-arp-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(ArpRedundancy.Redundancy, self).__init__()

            self.yang_name = "redundancy"
            self.yang_parent_name = "arp-redundancy"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("groups", ("groups", ArpRedundancy.Redundancy.Groups))])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ])
            self.enable = None

            self.groups = ArpRedundancy.Redundancy.Groups()
            self.groups.parent = self
            self._children_name_map["groups"] = "groups"
            self._segment_path = lambda: "redundancy"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-arp-cfg:arp-redundancy/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ArpRedundancy.Redundancy, ['enable'], name, value)


        class Groups(Entity):
            """
            Table of Group
            
            .. attribute:: group
            
            	None
            	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group>`
            
            

            """

            _prefix = 'ipv4-arp-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(ArpRedundancy.Redundancy.Groups, self).__init__()

                self.yang_name = "groups"
                self.yang_parent_name = "redundancy"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("group", ("group", ArpRedundancy.Redundancy.Groups.Group))])
                self._leafs = OrderedDict()

                self.group = YList(self)
                self._segment_path = lambda: "groups"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-arp-cfg:arp-redundancy/redundancy/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ArpRedundancy.Redundancy.Groups, [], name, value)


            class Group(Entity):
                """
                None
                
                .. attribute:: group_id  (key)
                
                	Group ID
                	**type**\: int
                
                	**range:** 1..32
                
                .. attribute:: peers
                
                	Table of Peer
                	**type**\:  :py:class:`Peers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group.Peers>`
                
                .. attribute:: interface_list
                
                	List of Interfaces for this Group
                	**type**\:  :py:class:`InterfaceList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group.InterfaceList>`
                
                	**presence node**\: True
                
                .. attribute:: source_interface
                
                	Interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                

                """

                _prefix = 'ipv4-arp-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(ArpRedundancy.Redundancy.Groups.Group, self).__init__()

                    self.yang_name = "group"
                    self.yang_parent_name = "groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['group_id']
                    self._child_classes = OrderedDict([("peers", ("peers", ArpRedundancy.Redundancy.Groups.Group.Peers)), ("interface-list", ("interface_list", ArpRedundancy.Redundancy.Groups.Group.InterfaceList))])
                    self._leafs = OrderedDict([
                        ('group_id', (YLeaf(YType.uint32, 'group-id'), ['int'])),
                        ('source_interface', (YLeaf(YType.str, 'source-interface'), ['str'])),
                    ])
                    self.group_id = None
                    self.source_interface = None

                    self.peers = ArpRedundancy.Redundancy.Groups.Group.Peers()
                    self.peers.parent = self
                    self._children_name_map["peers"] = "peers"

                    self.interface_list = None
                    self._children_name_map["interface_list"] = "interface-list"
                    self._segment_path = lambda: "group" + "[group-id='" + str(self.group_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-arp-cfg:arp-redundancy/redundancy/groups/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ArpRedundancy.Redundancy.Groups.Group, ['group_id', 'source_interface'], name, value)


                class Peers(Entity):
                    """
                    Table of Peer
                    
                    .. attribute:: peer
                    
                    	None
                    	**type**\: list of  		 :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group.Peers.Peer>`
                    
                    

                    """

                    _prefix = 'ipv4-arp-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ArpRedundancy.Redundancy.Groups.Group.Peers, self).__init__()

                        self.yang_name = "peers"
                        self.yang_parent_name = "group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("peer", ("peer", ArpRedundancy.Redundancy.Groups.Group.Peers.Peer))])
                        self._leafs = OrderedDict()

                        self.peer = YList(self)
                        self._segment_path = lambda: "peers"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ArpRedundancy.Redundancy.Groups.Group.Peers, [], name, value)


                    class Peer(Entity):
                        """
                        None
                        
                        .. attribute:: prefix_string  (key)
                        
                        	Neighbor IPv4 address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv4-arp-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ArpRedundancy.Redundancy.Groups.Group.Peers.Peer, self).__init__()

                            self.yang_name = "peer"
                            self.yang_parent_name = "peers"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['prefix_string']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('prefix_string', (YLeaf(YType.str, 'prefix-string'), ['str','str'])),
                            ])
                            self.prefix_string = None
                            self._segment_path = lambda: "peer" + "[prefix-string='" + str(self.prefix_string) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ArpRedundancy.Redundancy.Groups.Group.Peers.Peer, ['prefix_string'], name, value)


                class InterfaceList(Entity):
                    """
                    List of Interfaces for this Group
                    
                    .. attribute:: interfaces
                    
                    	Table of Interface
                    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces>`
                    
                    .. attribute:: enable
                    
                    	Enable List of Interfaces for this Group. Deletion of this object also causes deletion of all associated objects under InterfaceList
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-arp-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ArpRedundancy.Redundancy.Groups.Group.InterfaceList, self).__init__()

                        self.yang_name = "interface-list"
                        self.yang_parent_name = "group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interfaces", ("interfaces", ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces))])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ])
                        self.enable = None

                        self.interfaces = ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                        self._segment_path = lambda: "interface-list"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ArpRedundancy.Redundancy.Groups.Group.InterfaceList, ['enable'], name, value)


                    class Interfaces(Entity):
                        """
                        Table of Interface
                        
                        .. attribute:: interface
                        
                        	Interface for this Group
                        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces.Interface>`
                        
                        

                        """

                        _prefix = 'ipv4-arp-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces, self).__init__()

                            self.yang_name = "interfaces"
                            self.yang_parent_name = "interface-list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("interface", ("interface", ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces.Interface))])
                            self._leafs = OrderedDict()

                            self.interface = YList(self)
                            self._segment_path = lambda: "interfaces"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces, [], name, value)


                        class Interface(Entity):
                            """
                            Interface for this Group
                            
                            .. attribute:: interface_name  (key)
                            
                            	Interface name
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: interface_id
                            
                            	Interface Id for the interface
                            	**type**\: int
                            
                            	**range:** 1..65535
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'ipv4-arp-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces.Interface, self).__init__()

                                self.yang_name = "interface"
                                self.yang_parent_name = "interfaces"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['interface_name']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('interface_id', (YLeaf(YType.uint32, 'interface-id'), ['int'])),
                                ])
                                self.interface_name = None
                                self.interface_id = None
                                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces.Interface, ['interface_name', 'interface_id'], name, value)

    def clone_ptr(self):
        self._top_entity = ArpRedundancy()
        return self._top_entity


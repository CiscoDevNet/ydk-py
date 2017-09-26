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

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class ArpEncap(Enum):
    """
    ArpEncap

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
    ArpEntry

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
    
    .. attribute:: inner_cos
    
    	Configure inner cos values for arp packets
    	**type**\:  int
    
    	**range:** 0..7
    
    .. attribute:: max_entries
    
    	Configure maximum number of safe ARP entries per line card
    	**type**\:  int
    
    	**range:** 1..256000
    
    .. attribute:: outer_cos
    
    	Configure outer cos values for arp packets
    	**type**\:  int
    
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
        self._child_container_classes = {}
        self._child_list_classes = {}

        self.inner_cos = YLeaf(YType.uint32, "inner-cos")

        self.max_entries = YLeaf(YType.uint32, "max-entries")

        self.outer_cos = YLeaf(YType.uint32, "outer-cos")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-arp-cfg:arp"

    def __setattr__(self, name, value):
        self._perform_setattr(Arp, ['inner_cos', 'max_entries', 'outer_cos'], name, value)

    def clone_ptr(self):
        self._top_entity = Arp()
        return self._top_entity

class ArpRedundancy(Entity):
    """
    arp redundancy
    
    .. attribute:: redundancy
    
    	Configure parameter for ARP Geo redundancy
    	**type**\:   :py:class:`Redundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy>`
    
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
        self._child_container_classes = {"redundancy" : ("redundancy", ArpRedundancy.Redundancy)}
        self._child_list_classes = {}

        self.redundancy = None
        self._children_name_map["redundancy"] = "redundancy"
        self._children_yang_names.add("redundancy")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-arp-cfg:arp-redundancy"


    class Redundancy(Entity):
        """
        Configure parameter for ARP Geo redundancy
        
        .. attribute:: enable
        
        	Enable Configure parameter for ARP Geo redundancy. Deletion of this object also causes deletion of all associated objects under ArpRedundancy
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        .. attribute:: groups
        
        	Table of Group
        	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups>`
        
        

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
            self._child_container_classes = {"groups" : ("groups", ArpRedundancy.Redundancy.Groups)}
            self._child_list_classes = {}
            self.is_presence_container = True

            self.enable = YLeaf(YType.empty, "enable")

            self.groups = ArpRedundancy.Redundancy.Groups()
            self.groups.parent = self
            self._children_name_map["groups"] = "groups"
            self._children_yang_names.add("groups")
            self._segment_path = lambda: "redundancy"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-arp-cfg:arp-redundancy/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ArpRedundancy.Redundancy, ['enable'], name, value)


        class Groups(Entity):
            """
            Table of Group
            
            .. attribute:: group
            
            	None
            	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group>`
            
            

            """

            _prefix = 'ipv4-arp-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(ArpRedundancy.Redundancy.Groups, self).__init__()

                self.yang_name = "groups"
                self.yang_parent_name = "redundancy"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"group" : ("group", ArpRedundancy.Redundancy.Groups.Group)}

                self.group = YList(self)
                self._segment_path = lambda: "groups"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-arp-cfg:arp-redundancy/redundancy/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ArpRedundancy.Redundancy.Groups, [], name, value)


            class Group(Entity):
                """
                None
                
                .. attribute:: group_id  <key>
                
                	Group ID
                	**type**\:  int
                
                	**range:** 1..32
                
                .. attribute:: interface_list
                
                	List of Interfaces for this Group
                	**type**\:   :py:class:`InterfaceList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group.InterfaceList>`
                
                	**presence node**\: True
                
                .. attribute:: peers
                
                	Table of Peer
                	**type**\:   :py:class:`Peers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group.Peers>`
                
                .. attribute:: source_interface
                
                	Interface name
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                

                """

                _prefix = 'ipv4-arp-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(ArpRedundancy.Redundancy.Groups.Group, self).__init__()

                    self.yang_name = "group"
                    self.yang_parent_name = "groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"interface-list" : ("interface_list", ArpRedundancy.Redundancy.Groups.Group.InterfaceList), "peers" : ("peers", ArpRedundancy.Redundancy.Groups.Group.Peers)}
                    self._child_list_classes = {}

                    self.group_id = YLeaf(YType.uint32, "group-id")

                    self.source_interface = YLeaf(YType.str, "source-interface")

                    self.interface_list = None
                    self._children_name_map["interface_list"] = "interface-list"
                    self._children_yang_names.add("interface-list")

                    self.peers = ArpRedundancy.Redundancy.Groups.Group.Peers()
                    self.peers.parent = self
                    self._children_name_map["peers"] = "peers"
                    self._children_yang_names.add("peers")
                    self._segment_path = lambda: "group" + "[group-id='" + self.group_id.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-arp-cfg:arp-redundancy/redundancy/groups/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ArpRedundancy.Redundancy.Groups.Group, ['group_id', 'source_interface'], name, value)


                class InterfaceList(Entity):
                    """
                    List of Interfaces for this Group
                    
                    .. attribute:: enable
                    
                    	Enable List of Interfaces for this Group. Deletion of this object also causes deletion of all associated objects under InterfaceList
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: interfaces
                    
                    	Table of Interface
                    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces>`
                    
                    

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
                        self._child_container_classes = {"interfaces" : ("interfaces", ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces)}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.enable = YLeaf(YType.empty, "enable")

                        self.interfaces = ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                        self._children_yang_names.add("interfaces")
                        self._segment_path = lambda: "interface-list"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ArpRedundancy.Redundancy.Groups.Group.InterfaceList, ['enable'], name, value)


                    class Interfaces(Entity):
                        """
                        Table of Interface
                        
                        .. attribute:: interface
                        
                        	Interface for this Group
                        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces.Interface>`
                        
                        

                        """

                        _prefix = 'ipv4-arp-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces, self).__init__()

                            self.yang_name = "interfaces"
                            self.yang_parent_name = "interface-list"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"interface" : ("interface", ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces.Interface)}

                            self.interface = YList(self)
                            self._segment_path = lambda: "interfaces"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces, [], name, value)


                        class Interface(Entity):
                            """
                            Interface for this Group
                            
                            .. attribute:: interface_name  <key>
                            
                            	Interface name
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: interface_id
                            
                            	Interface Id for the interface
                            	**type**\:  int
                            
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
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.interface_id = YLeaf(YType.uint32, "interface-id")
                                self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(ArpRedundancy.Redundancy.Groups.Group.InterfaceList.Interfaces.Interface, ['interface_name', 'interface_id'], name, value)


                class Peers(Entity):
                    """
                    Table of Peer
                    
                    .. attribute:: peer
                    
                    	None
                    	**type**\: list of    :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpRedundancy.Redundancy.Groups.Group.Peers.Peer>`
                    
                    

                    """

                    _prefix = 'ipv4-arp-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ArpRedundancy.Redundancy.Groups.Group.Peers, self).__init__()

                        self.yang_name = "peers"
                        self.yang_parent_name = "group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"peer" : ("peer", ArpRedundancy.Redundancy.Groups.Group.Peers.Peer)}

                        self.peer = YList(self)
                        self._segment_path = lambda: "peers"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ArpRedundancy.Redundancy.Groups.Group.Peers, [], name, value)


                    class Peer(Entity):
                        """
                        None
                        
                        .. attribute:: prefix_string  <key>
                        
                        	Neighbor IPv4 address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        

                        """

                        _prefix = 'ipv4-arp-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ArpRedundancy.Redundancy.Groups.Group.Peers.Peer, self).__init__()

                            self.yang_name = "peer"
                            self.yang_parent_name = "peers"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.prefix_string = YLeaf(YType.str, "prefix-string")
                            self._segment_path = lambda: "peer" + "[prefix-string='" + self.prefix_string.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ArpRedundancy.Redundancy.Groups.Group.Peers.Peer, ['prefix_string'], name, value)

    def clone_ptr(self):
        self._top_entity = ArpRedundancy()
        return self._top_entity

class Arpgmp(Entity):
    """
    arpgmp
    
    .. attribute:: vrf
    
    	Per VRF configuration, for the default VRF use 'default'
    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.Arpgmp.Vrf>`
    
    

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
        self._child_container_classes = {}
        self._child_list_classes = {"vrf" : ("vrf", Arpgmp.Vrf)}

        self.vrf = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-arp-cfg:arpgmp"

    def __setattr__(self, name, value):
        self._perform_setattr(Arpgmp, [], name, value)


    class Vrf(Entity):
        """
        Per VRF configuration, for the default VRF use
        'default'
        
        .. attribute:: vrf_name  <key>
        
        	VRF name
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: entries
        
        	ARP static and alias entry configuration
        	**type**\:   :py:class:`Entries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.Arpgmp.Vrf.Entries>`
        
        

        """

        _prefix = 'ipv4-arp-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(Arpgmp.Vrf, self).__init__()

            self.yang_name = "vrf"
            self.yang_parent_name = "arpgmp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"entries" : ("entries", Arpgmp.Vrf.Entries)}
            self._child_list_classes = {}

            self.vrf_name = YLeaf(YType.str, "vrf-name")

            self.entries = Arpgmp.Vrf.Entries()
            self.entries.parent = self
            self._children_name_map["entries"] = "entries"
            self._children_yang_names.add("entries")
            self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-arp-cfg:arpgmp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Arpgmp.Vrf, ['vrf_name'], name, value)


        class Entries(Entity):
            """
            ARP static and alias entry configuration
            
            .. attribute:: entry
            
            	ARP static and alias entry configuration item
            	**type**\: list of    :py:class:`Entry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.Arpgmp.Vrf.Entries.Entry>`
            
            

            """

            _prefix = 'ipv4-arp-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(Arpgmp.Vrf.Entries, self).__init__()

                self.yang_name = "entries"
                self.yang_parent_name = "vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"entry" : ("entry", Arpgmp.Vrf.Entries.Entry)}

                self.entry = YList(self)
                self._segment_path = lambda: "entries"

            def __setattr__(self, name, value):
                self._perform_setattr(Arpgmp.Vrf.Entries, [], name, value)


            class Entry(Entity):
                """
                ARP static and alias entry configuration item
                
                .. attribute:: address  <key>
                
                	IP Address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: encapsulation
                
                	Encapsulation type
                	**type**\:   :py:class:`ArpEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpEncap>`
                
                .. attribute:: entry_type
                
                	Entry type
                	**type**\:   :py:class:`ArpEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_arp_cfg.ArpEntry>`
                
                .. attribute:: interface
                
                	Interface name
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: mac_address
                
                	MAC Address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                

                """

                _prefix = 'ipv4-arp-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Arpgmp.Vrf.Entries.Entry, self).__init__()

                    self.yang_name = "entry"
                    self.yang_parent_name = "entries"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.address = YLeaf(YType.str, "address")

                    self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                    self.entry_type = YLeaf(YType.enumeration, "entry-type")

                    self.interface = YLeaf(YType.str, "interface")

                    self.mac_address = YLeaf(YType.str, "mac-address")
                    self._segment_path = lambda: "entry" + "[address='" + self.address.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Arpgmp.Vrf.Entries.Entry, ['address', 'encapsulation', 'entry_type', 'interface', 'mac_address'], name, value)

    def clone_ptr(self):
        self._top_entity = Arpgmp()
        return self._top_entity

class IedgeCfg(Entity):
    """
    iedge cfg
    
    .. attribute:: subscriber_scale_mode
    
    	ARP Subscriber Scale Mode Configuration
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: subscriber_uncond_proxy
    
    	ARP Subscriber Enable Unconditional Proxy ARP
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    

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
        self._child_container_classes = {}
        self._child_list_classes = {}

        self.subscriber_scale_mode = YLeaf(YType.empty, "subscriber-scale-mode")

        self.subscriber_uncond_proxy = YLeaf(YType.empty, "subscriber-uncond-proxy")
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-arp-cfg:iedge-cfg"

    def __setattr__(self, name, value):
        self._perform_setattr(IedgeCfg, ['subscriber_scale_mode', 'subscriber_uncond_proxy'], name, value)

    def clone_ptr(self):
        self._top_entity = IedgeCfg()
        return self._top_entity


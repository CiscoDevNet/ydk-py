""" Cisco_IOS_XR_ip_tcp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-tcp package configuration.

This module contains definitions
for the following management objects\:
  ip\-tcp\: Global IP TCP configuration
  ip\: ip

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class IpTcp(Entity):
    """
    Global IP TCP configuration
    
    .. attribute:: directory
    
    	TCP directory details
    	**type**\:  :py:class:`Directory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.IpTcp.Directory>`
    
    	**presence node**\: True
    
    .. attribute:: throttle
    
    	Throttle TCP receive buffer (in percentage)
    	**type**\:  :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.IpTcp.Throttle>`
    
    	**presence node**\: True
    
    .. attribute:: ao
    
    	TCP authentication option configuration mode
    	**type**\:  :py:class:`Ao <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.IpTcp.Ao>`
    
    .. attribute:: num_thread
    
    	TCP InQueue and OutQueue threads
    	**type**\:  :py:class:`NumThread <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.IpTcp.NumThread>`
    
    	**presence node**\: True
    
    .. attribute:: accept_rate
    
    	TCP connection accept rate
    	**type**\: int
    
    	**range:** 1..1000
    
    	**default value**\: 500
    
    .. attribute:: selective_ack
    
    	Enable TCP selective\-ACK
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: window_size
    
    	TCP receive window size (bytes)
    	**type**\: int
    
    	**range:** 2048..65535
    
    	**units**\: byte
    
    .. attribute:: receive_q
    
    	TCP receive Queue Size
    	**type**\: int
    
    	**range:** 40..800
    
    .. attribute:: maximum_segment_size
    
    	TCP initial maximum segment size
    	**type**\: int
    
    	**range:** 68..10000
    
    .. attribute:: syn_wait_time
    
    	Time to wait on new TCP connections in seconds
    	**type**\: int
    
    	**range:** 5..30
    
    	**units**\: second
    
    .. attribute:: timestamp
    
    	Enable TCP timestamp option
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: path_mtu_discovery
    
    	Aging time; 0 for infinite, and range be (10,30)
    	**type**\: int
    
    	**range:** 0..4294967295
    
    	**units**\: minute
    
    	**default value**\: 10
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'ip-tcp-cfg'
    _revision = '2018-02-14'

    def __init__(self):
        super(IpTcp, self).__init__()
        self._top_entity = None

        self.yang_name = "ip-tcp"
        self.yang_parent_name = "Cisco-IOS-XR-ip-tcp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("directory", ("directory", IpTcp.Directory)), ("throttle", ("throttle", IpTcp.Throttle)), ("ao", ("ao", IpTcp.Ao)), ("num-thread", ("num_thread", IpTcp.NumThread))])
        self.is_presence_container = True
        self._leafs = OrderedDict([
            ('accept_rate', (YLeaf(YType.uint32, 'accept-rate'), ['int'])),
            ('selective_ack', (YLeaf(YType.empty, 'selective-ack'), ['Empty'])),
            ('window_size', (YLeaf(YType.uint32, 'window-size'), ['int'])),
            ('receive_q', (YLeaf(YType.uint32, 'receive-q'), ['int'])),
            ('maximum_segment_size', (YLeaf(YType.uint32, 'maximum-segment-size'), ['int'])),
            ('syn_wait_time', (YLeaf(YType.uint32, 'syn-wait-time'), ['int'])),
            ('timestamp', (YLeaf(YType.empty, 'timestamp'), ['Empty'])),
            ('path_mtu_discovery', (YLeaf(YType.uint32, 'path-mtu-discovery'), ['int'])),
        ])
        self.accept_rate = None
        self.selective_ack = None
        self.window_size = None
        self.receive_q = None
        self.maximum_segment_size = None
        self.syn_wait_time = None
        self.timestamp = None
        self.path_mtu_discovery = None

        self.directory = None
        self._children_name_map["directory"] = "directory"

        self.throttle = None
        self._children_name_map["throttle"] = "throttle"

        self.ao = IpTcp.Ao()
        self.ao.parent = self
        self._children_name_map["ao"] = "ao"

        self.num_thread = None
        self._children_name_map["num_thread"] = "num-thread"
        self._segment_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip-tcp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(IpTcp, ['accept_rate', 'selective_ack', 'window_size', 'receive_q', 'maximum_segment_size', 'syn_wait_time', 'timestamp', 'path_mtu_discovery'], name, value)


    class Directory(Entity):
        """
        TCP directory details
        
        .. attribute:: directoryname
        
        	Directory name 
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: max_debug_files
        
        	Set number of Debug files
        	**type**\: int
        
        	**range:** 1..10000
        
        	**default value**\: 256
        
        .. attribute:: max_file_size_files
        
        	Set size of debug files in bytes
        	**type**\: int
        
        	**range:** 1024..4294967295
        
        	**units**\: byte
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ip-tcp-cfg'
        _revision = '2018-02-14'

        def __init__(self):
            super(IpTcp.Directory, self).__init__()

            self.yang_name = "directory"
            self.yang_parent_name = "ip-tcp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('directoryname', (YLeaf(YType.str, 'directoryname'), ['str'])),
                ('max_debug_files', (YLeaf(YType.uint32, 'max-debug-files'), ['int'])),
                ('max_file_size_files', (YLeaf(YType.uint32, 'max-file-size-files'), ['int'])),
            ])
            self.directoryname = None
            self.max_debug_files = None
            self.max_file_size_files = None
            self._segment_path = lambda: "directory"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip-tcp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(IpTcp.Directory, ['directoryname', 'max_debug_files', 'max_file_size_files'], name, value)


    class Throttle(Entity):
        """
        Throttle TCP receive buffer (in percentage)
        
        .. attribute:: tcpmin_throttle
        
        	Min throttle
        	**type**\: int
        
        	**range:** 0..100
        
        	**mandatory**\: True
        
        .. attribute:: tcpmaxthrottle
        
        	Max throttle
        	**type**\: int
        
        	**range:** 0..100
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ip-tcp-cfg'
        _revision = '2018-02-14'

        def __init__(self):
            super(IpTcp.Throttle, self).__init__()

            self.yang_name = "throttle"
            self.yang_parent_name = "ip-tcp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('tcpmin_throttle', (YLeaf(YType.uint32, 'tcpmin-throttle'), ['int'])),
                ('tcpmaxthrottle', (YLeaf(YType.uint32, 'tcpmaxthrottle'), ['int'])),
            ])
            self.tcpmin_throttle = None
            self.tcpmaxthrottle = None
            self._segment_path = lambda: "throttle"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip-tcp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(IpTcp.Throttle, ['tcpmin_throttle', 'tcpmaxthrottle'], name, value)


    class Ao(Entity):
        """
        TCP authentication option configuration mode
        
        .. attribute:: keychains
        
        	Configure a Key Chain
        	**type**\:  :py:class:`Keychains <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.IpTcp.Ao.Keychains>`
        
        .. attribute:: enable
        
        	Create TCP\-AO submode
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ip-tcp-cfg'
        _revision = '2018-02-14'

        def __init__(self):
            super(IpTcp.Ao, self).__init__()

            self.yang_name = "ao"
            self.yang_parent_name = "ip-tcp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("keychains", ("keychains", IpTcp.Ao.Keychains))])
            self._leafs = OrderedDict([
                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ])
            self.enable = None

            self.keychains = IpTcp.Ao.Keychains()
            self.keychains.parent = self
            self._children_name_map["keychains"] = "keychains"
            self._segment_path = lambda: "ao"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip-tcp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(IpTcp.Ao, ['enable'], name, value)


        class Keychains(Entity):
            """
            Configure a Key Chain
            
            .. attribute:: keychain
            
            	Name of the key chain
            	**type**\: list of  		 :py:class:`Keychain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.IpTcp.Ao.Keychains.Keychain>`
            
            

            """

            _prefix = 'ip-tcp-cfg'
            _revision = '2018-02-14'

            def __init__(self):
                super(IpTcp.Ao.Keychains, self).__init__()

                self.yang_name = "keychains"
                self.yang_parent_name = "ao"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("keychain", ("keychain", IpTcp.Ao.Keychains.Keychain))])
                self._leafs = OrderedDict()

                self.keychain = YList(self)
                self._segment_path = lambda: "keychains"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip-tcp/ao/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(IpTcp.Ao.Keychains, [], name, value)


            class Keychain(Entity):
                """
                Name of the key chain
                
                .. attribute:: name  (key)
                
                	Name of the key chain
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: keys
                
                	Configure a Key
                	**type**\:  :py:class:`Keys <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.IpTcp.Ao.Keychains.Keychain.Keys>`
                
                .. attribute:: create
                
                	Create keychain
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ip-tcp-cfg'
                _revision = '2018-02-14'

                def __init__(self):
                    super(IpTcp.Ao.Keychains.Keychain, self).__init__()

                    self.yang_name = "keychain"
                    self.yang_parent_name = "keychains"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("keys", ("keys", IpTcp.Ao.Keychains.Keychain.Keys))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('create', (YLeaf(YType.empty, 'create'), ['Empty'])),
                    ])
                    self.name = None
                    self.create = None

                    self.keys = IpTcp.Ao.Keychains.Keychain.Keys()
                    self.keys.parent = self
                    self._children_name_map["keys"] = "keys"
                    self._segment_path = lambda: "keychain" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip-tcp/ao/keychains/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(IpTcp.Ao.Keychains.Keychain, ['name', 'create'], name, value)


                class Keys(Entity):
                    """
                    Configure a Key
                    
                    .. attribute:: key
                    
                    	Key identifier
                    	**type**\: list of  		 :py:class:`Key <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.IpTcp.Ao.Keychains.Keychain.Keys.Key>`
                    
                    

                    """

                    _prefix = 'ip-tcp-cfg'
                    _revision = '2018-02-14'

                    def __init__(self):
                        super(IpTcp.Ao.Keychains.Keychain.Keys, self).__init__()

                        self.yang_name = "keys"
                        self.yang_parent_name = "keychain"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("key", ("key", IpTcp.Ao.Keychains.Keychain.Keys.Key))])
                        self._leafs = OrderedDict()

                        self.key = YList(self)
                        self._segment_path = lambda: "keys"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpTcp.Ao.Keychains.Keychain.Keys, [], name, value)


                    class Key(Entity):
                        """
                        Key identifier
                        
                        .. attribute:: key_id  (key)
                        
                        	48\-bit Key identifier in range [0 \- 281474976710655]
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: send_id
                        
                        	Send ID
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**mandatory**\: True
                        
                        .. attribute:: receive_id
                        
                        	Receive ID
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ip-tcp-cfg'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(IpTcp.Ao.Keychains.Keychain.Keys.Key, self).__init__()

                            self.yang_name = "key"
                            self.yang_parent_name = "keys"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['key_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('key_id', (YLeaf(YType.str, 'key-id'), ['str'])),
                                ('send_id', (YLeaf(YType.uint32, 'send-id'), ['int'])),
                                ('receive_id', (YLeaf(YType.uint32, 'receive-id'), ['int'])),
                            ])
                            self.key_id = None
                            self.send_id = None
                            self.receive_id = None
                            self._segment_path = lambda: "key" + "[key-id='" + str(self.key_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(IpTcp.Ao.Keychains.Keychain.Keys.Key, ['key_id', 'send_id', 'receive_id'], name, value)


    class NumThread(Entity):
        """
        TCP InQueue and OutQueue threads
        
        .. attribute:: tcp_in_q_threads
        
        	InQ Threads
        	**type**\: int
        
        	**range:** 1..16
        
        	**mandatory**\: True
        
        .. attribute:: tcp_out_q_threads
        
        	OutQ Threads
        	**type**\: int
        
        	**range:** 1..16
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ip-tcp-cfg'
        _revision = '2018-02-14'

        def __init__(self):
            super(IpTcp.NumThread, self).__init__()

            self.yang_name = "num-thread"
            self.yang_parent_name = "ip-tcp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('tcp_in_q_threads', (YLeaf(YType.uint32, 'tcp-in-q-threads'), ['int'])),
                ('tcp_out_q_threads', (YLeaf(YType.uint32, 'tcp-out-q-threads'), ['int'])),
            ])
            self.tcp_in_q_threads = None
            self.tcp_out_q_threads = None
            self._segment_path = lambda: "num-thread"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip-tcp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(IpTcp.NumThread, ['tcp_in_q_threads', 'tcp_out_q_threads'], name, value)

    def clone_ptr(self):
        self._top_entity = IpTcp()
        return self._top_entity

class Ip(Entity):
    """
    ip
    
    .. attribute:: cinetd
    
    	Cinetd configuration data
    	**type**\:  :py:class:`Cinetd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd>`
    
    .. attribute:: forward_protocol
    
    	Controls forwarding of physical and directed IP broadcasts
    	**type**\:  :py:class:`ForwardProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.ForwardProtocol>`
    
    

    """

    _prefix = 'ip-tcp-cfg'
    _revision = '2018-02-14'

    def __init__(self):
        super(Ip, self).__init__()
        self._top_entity = None

        self.yang_name = "ip"
        self.yang_parent_name = "Cisco-IOS-XR-ip-tcp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cinetd", ("cinetd", Ip.Cinetd)), ("Cisco-IOS-XR-ip-udp-cfg:forward-protocol", ("forward_protocol", Ip.ForwardProtocol))])
        self._leafs = OrderedDict()

        self.cinetd = Ip.Cinetd()
        self.cinetd.parent = self
        self._children_name_map["cinetd"] = "cinetd"

        self.forward_protocol = Ip.ForwardProtocol()
        self.forward_protocol.parent = self
        self._children_name_map["forward_protocol"] = "Cisco-IOS-XR-ip-udp-cfg:forward-protocol"
        self._segment_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ip, [], name, value)


    class Cinetd(Entity):
        """
        Cinetd configuration data
        
        .. attribute:: services
        
        	Describing services of cinetd
        	**type**\:  :py:class:`Services <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services>`
        
        .. attribute:: rate_limit
        
        	Number of service requests accepted per second
        	**type**\: int
        
        	**range:** 1..100
        
        	**default value**\: 1
        
        

        """

        _prefix = 'ip-tcp-cfg'
        _revision = '2018-02-14'

        def __init__(self):
            super(Ip.Cinetd, self).__init__()

            self.yang_name = "cinetd"
            self.yang_parent_name = "ip"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("services", ("services", Ip.Cinetd.Services))])
            self._leafs = OrderedDict([
                ('rate_limit', (YLeaf(YType.uint32, 'Cisco-IOS-XR-ipv4-cinetd-cfg:rate-limit'), ['int'])),
            ])
            self.rate_limit = None

            self.services = Ip.Cinetd.Services()
            self.services.parent = self
            self._children_name_map["services"] = "services"
            self._segment_path = lambda: "cinetd"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ip.Cinetd, ['rate_limit'], name, value)


        class Services(Entity):
            """
            Describing services of cinetd
            
            .. attribute:: ipv4
            
            	IPV4 related services
            	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv4>`
            
            .. attribute:: vrfs
            
            	VRF table
            	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs>`
            
            .. attribute:: ipv6
            
            	IPV6 related services
            	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv6>`
            
            

            """

            _prefix = 'ip-tcp-cfg'
            _revision = '2018-02-14'

            def __init__(self):
                super(Ip.Cinetd.Services, self).__init__()

                self.yang_name = "services"
                self.yang_parent_name = "cinetd"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ipv4", ("ipv4", Ip.Cinetd.Services.Ipv4)), ("vrfs", ("vrfs", Ip.Cinetd.Services.Vrfs)), ("ipv6", ("ipv6", Ip.Cinetd.Services.Ipv6))])
                self._leafs = OrderedDict()

                self.ipv4 = Ip.Cinetd.Services.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"

                self.vrfs = Ip.Cinetd.Services.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"

                self.ipv6 = Ip.Cinetd.Services.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"
                self._segment_path = lambda: "services"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip/cinetd/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ip.Cinetd.Services, [], name, value)


            class Ipv4(Entity):
                """
                IPV4 related services
                
                .. attribute:: small_servers
                
                	Describing IPV4 and IPV6 small servers
                	**type**\:  :py:class:`SmallServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv4.SmallServers>`
                
                

                """

                _prefix = 'ip-tcp-cfg'
                _revision = '2018-02-14'

                def __init__(self):
                    super(Ip.Cinetd.Services.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "services"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("small-servers", ("small_servers", Ip.Cinetd.Services.Ipv4.SmallServers))])
                    self._leafs = OrderedDict()

                    self.small_servers = Ip.Cinetd.Services.Ipv4.SmallServers()
                    self.small_servers.parent = self
                    self._children_name_map["small_servers"] = "small-servers"
                    self._segment_path = lambda: "ipv4"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip/cinetd/services/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ip.Cinetd.Services.Ipv4, [], name, value)


                class SmallServers(Entity):
                    """
                    Describing IPV4 and IPV6 small servers
                    
                    .. attribute:: tcp_small_servers
                    
                    	Describing TCP related IPV4 and IPV6 small servers
                    	**type**\:  :py:class:`TcpSmallServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv4.SmallServers.TcpSmallServers>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: udp_small_servers
                    
                    	UDP small servers configuration
                    	**type**\:  :py:class:`UdpSmallServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'ip-tcp-cfg'
                    _revision = '2018-02-14'

                    def __init__(self):
                        super(Ip.Cinetd.Services.Ipv4.SmallServers, self).__init__()

                        self.yang_name = "small-servers"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("tcp-small-servers", ("tcp_small_servers", Ip.Cinetd.Services.Ipv4.SmallServers.TcpSmallServers)), ("Cisco-IOS-XR-ip-udp-cfg:udp-small-servers", ("udp_small_servers", Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers))])
                        self._leafs = OrderedDict()

                        self.tcp_small_servers = None
                        self._children_name_map["tcp_small_servers"] = "tcp-small-servers"

                        self.udp_small_servers = None
                        self._children_name_map["udp_small_servers"] = "Cisco-IOS-XR-ip-udp-cfg:udp-small-servers"
                        self._segment_path = lambda: "small-servers"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip/cinetd/services/ipv4/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ip.Cinetd.Services.Ipv4.SmallServers, [], name, value)


                    class TcpSmallServers(Entity):
                        """
                        Describing TCP related IPV4 and IPV6 small
                        servers
                        
                        .. attribute:: access_control_list_name
                        
                        	Specify the access list
                        	**type**\: str
                        
                        .. attribute:: small_server
                        
                        	Set number of allowable TCP small servers, specify 0 for no\-limit
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`SmallServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers.SmallServer>`
                        
                        		**type**\: int
                        
                        			**range:** 0..2147483647
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ip-tcp-cfg'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(Ip.Cinetd.Services.Ipv4.SmallServers.TcpSmallServers, self).__init__()

                            self.yang_name = "tcp-small-servers"
                            self.yang_parent_name = "small-servers"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('access_control_list_name', (YLeaf(YType.str, 'access-control-list-name'), ['str'])),
                                ('small_server', (YLeaf(YType.str, 'small-server'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip', 'Cinetd.Services.Ipv6.SmallServers.TcpSmallServers.SmallServer'),'int'])),
                            ])
                            self.access_control_list_name = None
                            self.small_server = None
                            self._segment_path = lambda: "tcp-small-servers"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip/cinetd/services/ipv4/small-servers/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ip.Cinetd.Services.Ipv4.SmallServers.TcpSmallServers, ['access_control_list_name', 'small_server'], name, value)

                        class SmallServer(Enum):
                            """
                            SmallServer (Enum Class)

                            Set number of allowable TCP small servers,

                            specify 0 for no\-limit

                            .. data:: no_limit = 0

                            	Unlimited Servers

                            """

                            no_limit = Enum.YLeaf(0, "no-limit")



                    class UdpSmallServers(Entity):
                        """
                        UDP small servers configuration
                        
                        .. attribute:: access_control_list_name
                        
                        	Specify the access list
                        	**type**\: str
                        
                        .. attribute:: small_server
                        
                        	Set number of allowable small servers, specify 0 for no\-limit
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`SmallServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers.SmallServer>`
                        
                        		**type**\: int
                        
                        			**range:** 0..2147483647
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ip-udp-cfg'
                        _revision = '2017-09-30'

                        def __init__(self):
                            super(Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers, self).__init__()

                            self.yang_name = "udp-small-servers"
                            self.yang_parent_name = "small-servers"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('access_control_list_name', (YLeaf(YType.str, 'access-control-list-name'), ['str'])),
                                ('small_server', (YLeaf(YType.str, 'small-server'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip', 'Cinetd.Services.Ipv4.SmallServers.UdpSmallServers.SmallServer'),'int'])),
                            ])
                            self.access_control_list_name = None
                            self.small_server = None
                            self._segment_path = lambda: "Cisco-IOS-XR-ip-udp-cfg:udp-small-servers"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip/cinetd/services/ipv4/small-servers/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ip.Cinetd.Services.Ipv4.SmallServers.UdpSmallServers, ['access_control_list_name', 'small_server'], name, value)

                        class SmallServer(Enum):
                            """
                            SmallServer (Enum Class)

                            Set number of allowable small servers, specify

                            0 for no\-limit

                            .. data:: no_limit = 0

                            	Unlimited Servers

                            """

                            no_limit = Enum.YLeaf(0, "no-limit")



            class Vrfs(Entity):
                """
                VRF table
                
                .. attribute:: vrf
                
                	VRF specific data
                	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf>`
                
                

                """

                _prefix = 'ip-tcp-cfg'
                _revision = '2018-02-14'

                def __init__(self):
                    super(Ip.Cinetd.Services.Vrfs, self).__init__()

                    self.yang_name = "vrfs"
                    self.yang_parent_name = "services"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("vrf", ("vrf", Ip.Cinetd.Services.Vrfs.Vrf))])
                    self._leafs = OrderedDict()

                    self.vrf = YList(self)
                    self._segment_path = lambda: "vrfs"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip/cinetd/services/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ip.Cinetd.Services.Vrfs, [], name, value)


                class Vrf(Entity):
                    """
                    VRF specific data
                    
                    .. attribute:: vrf_name  (key)
                    
                    	Name of the VRF instance
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: ipv6
                    
                    	IPV6 related services
                    	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv6>`
                    
                    .. attribute:: ipv4
                    
                    	IPV4 related services
                    	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv4>`
                    
                    

                    """

                    _prefix = 'ip-tcp-cfg'
                    _revision = '2018-02-14'

                    def __init__(self):
                        super(Ip.Cinetd.Services.Vrfs.Vrf, self).__init__()

                        self.yang_name = "vrf"
                        self.yang_parent_name = "vrfs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['vrf_name']
                        self._child_classes = OrderedDict([("ipv6", ("ipv6", Ip.Cinetd.Services.Vrfs.Vrf.Ipv6)), ("ipv4", ("ipv4", Ip.Cinetd.Services.Vrfs.Vrf.Ipv4))])
                        self._leafs = OrderedDict([
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                        ])
                        self.vrf_name = None

                        self.ipv6 = Ip.Cinetd.Services.Vrfs.Vrf.Ipv6()
                        self.ipv6.parent = self
                        self._children_name_map["ipv6"] = "ipv6"

                        self.ipv4 = Ip.Cinetd.Services.Vrfs.Vrf.Ipv4()
                        self.ipv4.parent = self
                        self._children_name_map["ipv4"] = "ipv4"
                        self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip/cinetd/services/vrfs/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ip.Cinetd.Services.Vrfs.Vrf, ['vrf_name'], name, value)


                    class Ipv6(Entity):
                        """
                        IPV6 related services
                        
                        .. attribute:: telnet
                        
                        	TELNET server configuration commands
                        	**type**\:  :py:class:`Telnet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet>`
                        
                        .. attribute:: tftp
                        
                        	TFTP server configuration commands
                        	**type**\:  :py:class:`Tftp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp>`
                        
                        

                        """

                        _prefix = 'ip-tcp-cfg'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv6, self).__init__()

                            self.yang_name = "ipv6"
                            self.yang_parent_name = "vrf"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("telnet", ("telnet", Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet)), ("tftp", ("tftp", Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp))])
                            self._leafs = OrderedDict()

                            self.telnet = Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet()
                            self.telnet.parent = self
                            self._children_name_map["telnet"] = "telnet"

                            self.tftp = Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp()
                            self.tftp.parent = self
                            self._children_name_map["tftp"] = "tftp"
                            self._segment_path = lambda: "ipv6"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ip.Cinetd.Services.Vrfs.Vrf.Ipv6, [], name, value)


                        class Telnet(Entity):
                            """
                            TELNET server configuration commands
                            
                            .. attribute:: tcp
                            
                            	TCP details
                            	**type**\:  :py:class:`Tcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet.Tcp>`
                            
                            	**presence node**\: True
                            
                            

                            """

                            _prefix = 'ip-tcp-cfg'
                            _revision = '2018-02-14'

                            def __init__(self):
                                super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet, self).__init__()

                                self.yang_name = "telnet"
                                self.yang_parent_name = "ipv6"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("tcp", ("tcp", Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet.Tcp))])
                                self._leafs = OrderedDict()

                                self.tcp = None
                                self._children_name_map["tcp"] = "tcp"
                                self._segment_path = lambda: "telnet"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet, [], name, value)


                            class Tcp(Entity):
                                """
                                TCP details
                                
                                .. attribute:: access_list_name
                                
                                	Access list
                                	**type**\: str
                                
                                .. attribute:: maximum_server
                                
                                	Set number of allowable servers
                                	**type**\: int
                                
                                	**range:** 1..100
                                
                                	**mandatory**\: True
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'ip-tcp-cfg'
                                _revision = '2018-02-14'

                                def __init__(self):
                                    super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet.Tcp, self).__init__()

                                    self.yang_name = "tcp"
                                    self.yang_parent_name = "telnet"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self.is_presence_container = True
                                    self._leafs = OrderedDict([
                                        ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                                        ('maximum_server', (YLeaf(YType.uint32, 'maximum-server'), ['int'])),
                                    ])
                                    self.access_list_name = None
                                    self.maximum_server = None
                                    self._segment_path = lambda: "tcp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Telnet.Tcp, ['access_list_name', 'maximum_server'], name, value)


                        class Tftp(Entity):
                            """
                            TFTP server configuration commands
                            
                            .. attribute:: udp
                            
                            	UDP details
                            	**type**\:  :py:class:`Udp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp.Udp>`
                            
                            	**presence node**\: True
                            
                            

                            """

                            _prefix = 'ip-tcp-cfg'
                            _revision = '2018-02-14'

                            def __init__(self):
                                super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp, self).__init__()

                                self.yang_name = "tftp"
                                self.yang_parent_name = "ipv6"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("udp", ("udp", Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp.Udp))])
                                self._leafs = OrderedDict()

                                self.udp = None
                                self._children_name_map["udp"] = "udp"
                                self._segment_path = lambda: "tftp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp, [], name, value)


                            class Udp(Entity):
                                """
                                UDP details
                                
                                .. attribute:: access_list_name
                                
                                	Access list
                                	**type**\: str
                                
                                .. attribute:: maximum_server
                                
                                	Set number of allowable servers, 0 for no\-limit
                                	**type**\: int
                                
                                	**range:** 0..2147483647
                                
                                .. attribute:: home_directory
                                
                                	Specify device name where file is read from (e .g. flash\:)
                                	**type**\: str
                                
                                	**mandatory**\: True
                                
                                .. attribute:: dscp_value
                                
                                	Set IP DSCP (DiffServ CodePoint) for TFTP Server Packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'ip-tcp-cfg'
                                _revision = '2018-02-14'

                                def __init__(self):
                                    super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp.Udp, self).__init__()

                                    self.yang_name = "udp"
                                    self.yang_parent_name = "tftp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self.is_presence_container = True
                                    self._leafs = OrderedDict([
                                        ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                                        ('maximum_server', (YLeaf(YType.uint32, 'maximum-server'), ['int'])),
                                        ('home_directory', (YLeaf(YType.str, 'home-directory'), ['str'])),
                                        ('dscp_value', (YLeaf(YType.uint32, 'dscp-value'), ['int'])),
                                    ])
                                    self.access_list_name = None
                                    self.maximum_server = None
                                    self.home_directory = None
                                    self.dscp_value = None
                                    self._segment_path = lambda: "udp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ip.Cinetd.Services.Vrfs.Vrf.Ipv6.Tftp.Udp, ['access_list_name', 'maximum_server', 'home_directory', 'dscp_value'], name, value)


                    class Ipv4(Entity):
                        """
                        IPV4 related services
                        
                        .. attribute:: telnet
                        
                        	TELNET server configuration commands
                        	**type**\:  :py:class:`Telnet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet>`
                        
                        .. attribute:: tftp
                        
                        	TFTP server configuration commands
                        	**type**\:  :py:class:`Tftp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp>`
                        
                        

                        """

                        _prefix = 'ip-tcp-cfg'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv4, self).__init__()

                            self.yang_name = "ipv4"
                            self.yang_parent_name = "vrf"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("telnet", ("telnet", Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet)), ("tftp", ("tftp", Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp))])
                            self._leafs = OrderedDict()

                            self.telnet = Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet()
                            self.telnet.parent = self
                            self._children_name_map["telnet"] = "telnet"

                            self.tftp = Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp()
                            self.tftp.parent = self
                            self._children_name_map["tftp"] = "tftp"
                            self._segment_path = lambda: "ipv4"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ip.Cinetd.Services.Vrfs.Vrf.Ipv4, [], name, value)


                        class Telnet(Entity):
                            """
                            TELNET server configuration commands
                            
                            .. attribute:: tcp
                            
                            	TCP details
                            	**type**\:  :py:class:`Tcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet.Tcp>`
                            
                            	**presence node**\: True
                            
                            

                            """

                            _prefix = 'ip-tcp-cfg'
                            _revision = '2018-02-14'

                            def __init__(self):
                                super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet, self).__init__()

                                self.yang_name = "telnet"
                                self.yang_parent_name = "ipv4"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("tcp", ("tcp", Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet.Tcp))])
                                self._leafs = OrderedDict()

                                self.tcp = None
                                self._children_name_map["tcp"] = "tcp"
                                self._segment_path = lambda: "telnet"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet, [], name, value)


                            class Tcp(Entity):
                                """
                                TCP details
                                
                                .. attribute:: access_list_name
                                
                                	Access list
                                	**type**\: str
                                
                                .. attribute:: maximum_server
                                
                                	Set number of allowable servers
                                	**type**\: int
                                
                                	**range:** 1..100
                                
                                	**mandatory**\: True
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'ip-tcp-cfg'
                                _revision = '2018-02-14'

                                def __init__(self):
                                    super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet.Tcp, self).__init__()

                                    self.yang_name = "tcp"
                                    self.yang_parent_name = "telnet"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self.is_presence_container = True
                                    self._leafs = OrderedDict([
                                        ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                                        ('maximum_server', (YLeaf(YType.uint32, 'maximum-server'), ['int'])),
                                    ])
                                    self.access_list_name = None
                                    self.maximum_server = None
                                    self._segment_path = lambda: "tcp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Telnet.Tcp, ['access_list_name', 'maximum_server'], name, value)


                        class Tftp(Entity):
                            """
                            TFTP server configuration commands
                            
                            .. attribute:: udp
                            
                            	UDP details
                            	**type**\:  :py:class:`Udp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp.Udp>`
                            
                            	**presence node**\: True
                            
                            

                            """

                            _prefix = 'ip-tcp-cfg'
                            _revision = '2018-02-14'

                            def __init__(self):
                                super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp, self).__init__()

                                self.yang_name = "tftp"
                                self.yang_parent_name = "ipv4"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("udp", ("udp", Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp.Udp))])
                                self._leafs = OrderedDict()

                                self.udp = None
                                self._children_name_map["udp"] = "udp"
                                self._segment_path = lambda: "tftp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp, [], name, value)


                            class Udp(Entity):
                                """
                                UDP details
                                
                                .. attribute:: access_list_name
                                
                                	Access list
                                	**type**\: str
                                
                                .. attribute:: maximum_server
                                
                                	Set number of allowable servers, 0 for no\-limit
                                	**type**\: int
                                
                                	**range:** 0..2147483647
                                
                                .. attribute:: home_directory
                                
                                	Specify device name where file is read from (e .g. flash\:)
                                	**type**\: str
                                
                                	**mandatory**\: True
                                
                                .. attribute:: dscp_value
                                
                                	Set IP DSCP (DiffServ CodePoint) for TFTP Server Packets
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'ip-tcp-cfg'
                                _revision = '2018-02-14'

                                def __init__(self):
                                    super(Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp.Udp, self).__init__()

                                    self.yang_name = "udp"
                                    self.yang_parent_name = "tftp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self.is_presence_container = True
                                    self._leafs = OrderedDict([
                                        ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                                        ('maximum_server', (YLeaf(YType.uint32, 'maximum-server'), ['int'])),
                                        ('home_directory', (YLeaf(YType.str, 'home-directory'), ['str'])),
                                        ('dscp_value', (YLeaf(YType.uint32, 'dscp-value'), ['int'])),
                                    ])
                                    self.access_list_name = None
                                    self.maximum_server = None
                                    self.home_directory = None
                                    self.dscp_value = None
                                    self._segment_path = lambda: "udp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ip.Cinetd.Services.Vrfs.Vrf.Ipv4.Tftp.Udp, ['access_list_name', 'maximum_server', 'home_directory', 'dscp_value'], name, value)


            class Ipv6(Entity):
                """
                IPV6 related services
                
                .. attribute:: small_servers
                
                	Describing IPV4 and IPV6 small servers
                	**type**\:  :py:class:`SmallServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv6.SmallServers>`
                
                

                """

                _prefix = 'ip-tcp-cfg'
                _revision = '2018-02-14'

                def __init__(self):
                    super(Ip.Cinetd.Services.Ipv6, self).__init__()

                    self.yang_name = "ipv6"
                    self.yang_parent_name = "services"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("small-servers", ("small_servers", Ip.Cinetd.Services.Ipv6.SmallServers))])
                    self._leafs = OrderedDict()

                    self.small_servers = Ip.Cinetd.Services.Ipv6.SmallServers()
                    self.small_servers.parent = self
                    self._children_name_map["small_servers"] = "small-servers"
                    self._segment_path = lambda: "ipv6"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip/cinetd/services/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ip.Cinetd.Services.Ipv6, [], name, value)


                class SmallServers(Entity):
                    """
                    Describing IPV4 and IPV6 small servers
                    
                    .. attribute:: tcp_small_servers
                    
                    	Describing TCP related IPV4 and IPV6 small servers
                    	**type**\:  :py:class:`TcpSmallServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: udp_small_servers
                    
                    	UDP small servers configuration
                    	**type**\:  :py:class:`UdpSmallServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv6.SmallServers.UdpSmallServers>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'ip-tcp-cfg'
                    _revision = '2018-02-14'

                    def __init__(self):
                        super(Ip.Cinetd.Services.Ipv6.SmallServers, self).__init__()

                        self.yang_name = "small-servers"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("tcp-small-servers", ("tcp_small_servers", Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers)), ("Cisco-IOS-XR-ip-udp-cfg:udp-small-servers", ("udp_small_servers", Ip.Cinetd.Services.Ipv6.SmallServers.UdpSmallServers))])
                        self._leafs = OrderedDict()

                        self.tcp_small_servers = None
                        self._children_name_map["tcp_small_servers"] = "tcp-small-servers"

                        self.udp_small_servers = None
                        self._children_name_map["udp_small_servers"] = "Cisco-IOS-XR-ip-udp-cfg:udp-small-servers"
                        self._segment_path = lambda: "small-servers"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip/cinetd/services/ipv6/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ip.Cinetd.Services.Ipv6.SmallServers, [], name, value)


                    class TcpSmallServers(Entity):
                        """
                        Describing TCP related IPV4 and IPV6 small
                        servers
                        
                        .. attribute:: access_control_list_name
                        
                        	Specify the access list
                        	**type**\: str
                        
                        .. attribute:: small_server
                        
                        	Set number of allowable TCP small servers, specify 0 for no\-limit
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`SmallServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers.SmallServer>`
                        
                        		**type**\: int
                        
                        			**range:** 0..2147483647
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ip-tcp-cfg'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers, self).__init__()

                            self.yang_name = "tcp-small-servers"
                            self.yang_parent_name = "small-servers"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('access_control_list_name', (YLeaf(YType.str, 'access-control-list-name'), ['str'])),
                                ('small_server', (YLeaf(YType.str, 'small-server'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip', 'Cinetd.Services.Ipv6.SmallServers.TcpSmallServers.SmallServer'),'int'])),
                            ])
                            self.access_control_list_name = None
                            self.small_server = None
                            self._segment_path = lambda: "tcp-small-servers"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip/cinetd/services/ipv6/small-servers/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ip.Cinetd.Services.Ipv6.SmallServers.TcpSmallServers, ['access_control_list_name', 'small_server'], name, value)

                        class SmallServer(Enum):
                            """
                            SmallServer (Enum Class)

                            Set number of allowable TCP small servers,

                            specify 0 for no\-limit

                            .. data:: no_limit = 0

                            	Unlimited Servers

                            """

                            no_limit = Enum.YLeaf(0, "no-limit")



                    class UdpSmallServers(Entity):
                        """
                        UDP small servers configuration
                        
                        .. attribute:: access_control_list_name
                        
                        	Specify the access list
                        	**type**\: str
                        
                        .. attribute:: small_server
                        
                        	Set number of allowable small servers, specify 0 for no\-limit
                        	**type**\: union of the below types:
                        
                        		**type**\:  :py:class:`SmallServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.Cinetd.Services.Ipv6.SmallServers.UdpSmallServers.SmallServer>`
                        
                        		**type**\: int
                        
                        			**range:** 0..2147483647
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ip-udp-cfg'
                        _revision = '2017-09-30'

                        def __init__(self):
                            super(Ip.Cinetd.Services.Ipv6.SmallServers.UdpSmallServers, self).__init__()

                            self.yang_name = "udp-small-servers"
                            self.yang_parent_name = "small-servers"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('access_control_list_name', (YLeaf(YType.str, 'access-control-list-name'), ['str'])),
                                ('small_server', (YLeaf(YType.str, 'small-server'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg', 'Ip', 'Cinetd.Services.Ipv6.SmallServers.UdpSmallServers.SmallServer'),'int'])),
                            ])
                            self.access_control_list_name = None
                            self.small_server = None
                            self._segment_path = lambda: "Cisco-IOS-XR-ip-udp-cfg:udp-small-servers"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip/cinetd/services/ipv6/small-servers/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ip.Cinetd.Services.Ipv6.SmallServers.UdpSmallServers, ['access_control_list_name', 'small_server'], name, value)

                        class SmallServer(Enum):
                            """
                            SmallServer (Enum Class)

                            Set number of allowable small servers, specify

                            0 for no\-limit

                            .. data:: no_limit = 0

                            	Unlimited Servers

                            """

                            no_limit = Enum.YLeaf(0, "no-limit")



    class ForwardProtocol(Entity):
        """
        Controls forwarding of physical and directed IP
        broadcasts
        
        .. attribute:: udp
        
        	Packets to a specific UDP port
        	**type**\:  :py:class:`Udp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.ForwardProtocol.Udp>`
        
        

        """

        _prefix = 'ip-udp-cfg'
        _revision = '2017-09-30'

        def __init__(self):
            super(Ip.ForwardProtocol, self).__init__()

            self.yang_name = "forward-protocol"
            self.yang_parent_name = "ip"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("udp", ("udp", Ip.ForwardProtocol.Udp))])
            self._leafs = OrderedDict()

            self.udp = Ip.ForwardProtocol.Udp()
            self.udp.parent = self
            self._children_name_map["udp"] = "udp"
            self._segment_path = lambda: "Cisco-IOS-XR-ip-udp-cfg:forward-protocol"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ip.ForwardProtocol, [], name, value)


        class Udp(Entity):
            """
            Packets to a specific UDP port
            
            .. attribute:: ports
            
            	Port configuration
            	**type**\:  :py:class:`Ports <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.ForwardProtocol.Udp.Ports>`
            
            .. attribute:: disable
            
            	Disable IP Forward Protocol UDP
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-udp-cfg'
            _revision = '2017-09-30'

            def __init__(self):
                super(Ip.ForwardProtocol.Udp, self).__init__()

                self.yang_name = "udp"
                self.yang_parent_name = "forward-protocol"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ports", ("ports", Ip.ForwardProtocol.Udp.Ports))])
                self._leafs = OrderedDict([
                    ('disable', (YLeaf(YType.empty, 'disable'), ['Empty'])),
                ])
                self.disable = None

                self.ports = Ip.ForwardProtocol.Udp.Ports()
                self.ports.parent = self
                self._children_name_map["ports"] = "ports"
                self._segment_path = lambda: "udp"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip/Cisco-IOS-XR-ip-udp-cfg:forward-protocol/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ip.ForwardProtocol.Udp, ['disable'], name, value)


            class Ports(Entity):
                """
                Port configuration
                
                .. attribute:: port
                
                	Well\-known ports are enabled by default and non well\-known ports are disabled by default. It is not allowed to configure the default
                	**type**\: list of  		 :py:class:`Port <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_cfg.Ip.ForwardProtocol.Udp.Ports.Port>`
                
                

                """

                _prefix = 'ip-udp-cfg'
                _revision = '2017-09-30'

                def __init__(self):
                    super(Ip.ForwardProtocol.Udp.Ports, self).__init__()

                    self.yang_name = "ports"
                    self.yang_parent_name = "udp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("port", ("port", Ip.ForwardProtocol.Udp.Ports.Port))])
                    self._leafs = OrderedDict()

                    self.port = YList(self)
                    self._segment_path = lambda: "ports"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip/Cisco-IOS-XR-ip-udp-cfg:forward-protocol/udp/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ip.ForwardProtocol.Udp.Ports, [], name, value)


                class Port(Entity):
                    """
                    Well\-known ports are enabled by default and
                    non well\-known ports are disabled by default.
                    It is not allowed to configure the default.
                    
                    .. attribute:: port_id  (key)
                    
                    	Port number
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: enable
                    
                    	Specify 'false' to disable well\-known ports Domain (53), TFTP (69), NameServer (42), TACACS (49), NetBiosNameService (137), or NetBiosDatagramService (138).  Specify 'true' to enable non well\-known ports
                    	**type**\: bool
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ip-udp-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(Ip.ForwardProtocol.Udp.Ports.Port, self).__init__()

                        self.yang_name = "port"
                        self.yang_parent_name = "ports"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['port_id']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('port_id', (YLeaf(YType.uint16, 'port-id'), ['int'])),
                            ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                        ])
                        self.port_id = None
                        self.enable = None
                        self._segment_path = lambda: "port" + "[port-id='" + str(self.port_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-cfg:ip/Cisco-IOS-XR-ip-udp-cfg:forward-protocol/udp/ports/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ip.ForwardProtocol.Udp.Ports.Port, ['port_id', 'enable'], name, value)

    def clone_ptr(self):
        self._top_entity = Ip()
        return self._top_entity


""" Cisco_IOS_XR_ip_udp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-udp package configuration.

This module contains definitions
for the following management objects\:
  ip\-udp\: Global IP UDP configuration

This YANG module augments the
  Cisco\-IOS\-XR\-ip\-tcp\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class IpUdp(Entity):
    """
    Global IP UDP configuration
    
    .. attribute:: num_thread
    
    	UDP InQueue and OutQueue threads
    	**type**\:  :py:class:`NumThread <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_cfg.IpUdp.NumThread>`
    
    	**presence node**\: True
    
    .. attribute:: directory
    
    	UDP directory details
    	**type**\:  :py:class:`Directory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_cfg.IpUdp.Directory>`
    
    	**presence node**\: True
    
    .. attribute:: receive_q
    
    	UDP receive Queue Size
    	**type**\: int
    
    	**range:** 40..800
    
    

    """

    _prefix = 'ip-udp-cfg'
    _revision = '2017-09-30'

    def __init__(self):
        super(IpUdp, self).__init__()
        self._top_entity = None

        self.yang_name = "ip-udp"
        self.yang_parent_name = "Cisco-IOS-XR-ip-udp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("num-thread", ("num_thread", IpUdp.NumThread)), ("directory", ("directory", IpUdp.Directory))])
        self._leafs = OrderedDict([
            ('receive_q', (YLeaf(YType.uint32, 'receive-q'), ['int'])),
        ])
        self.receive_q = None

        self.num_thread = None
        self._children_name_map["num_thread"] = "num-thread"

        self.directory = None
        self._children_name_map["directory"] = "directory"
        self._segment_path = lambda: "Cisco-IOS-XR-ip-udp-cfg:ip-udp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(IpUdp, ['receive_q'], name, value)


    class NumThread(Entity):
        """
        UDP InQueue and OutQueue threads
        
        .. attribute:: udp_in_q_threads
        
        	InQ Threads
        	**type**\: int
        
        	**range:** 1..16
        
        	**mandatory**\: True
        
        .. attribute:: udp_out_q_threads
        
        	OutQ Threads
        	**type**\: int
        
        	**range:** 1..16
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ip-udp-cfg'
        _revision = '2017-09-30'

        def __init__(self):
            super(IpUdp.NumThread, self).__init__()

            self.yang_name = "num-thread"
            self.yang_parent_name = "ip-udp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('udp_in_q_threads', (YLeaf(YType.uint32, 'udp-in-q-threads'), ['int'])),
                ('udp_out_q_threads', (YLeaf(YType.uint32, 'udp-out-q-threads'), ['int'])),
            ])
            self.udp_in_q_threads = None
            self.udp_out_q_threads = None
            self._segment_path = lambda: "num-thread"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-udp-cfg:ip-udp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(IpUdp.NumThread, ['udp_in_q_threads', 'udp_out_q_threads'], name, value)


    class Directory(Entity):
        """
        UDP directory details
        
        .. attribute:: directoryname
        
        	Directory name
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: max_udp_debug_files
        
        	Set number of Debug files
        	**type**\: int
        
        	**range:** 1..5000
        
        	**default value**\: 256
        
        .. attribute:: max_file_size_files
        
        	Set size of debug files in bytes
        	**type**\: int
        
        	**range:** 1024..4294967295
        
        	**units**\: byte
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ip-udp-cfg'
        _revision = '2017-09-30'

        def __init__(self):
            super(IpUdp.Directory, self).__init__()

            self.yang_name = "directory"
            self.yang_parent_name = "ip-udp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('directoryname', (YLeaf(YType.str, 'directoryname'), ['str'])),
                ('max_udp_debug_files', (YLeaf(YType.uint32, 'max-udp-debug-files'), ['int'])),
                ('max_file_size_files', (YLeaf(YType.uint32, 'max-file-size-files'), ['int'])),
            ])
            self.directoryname = None
            self.max_udp_debug_files = None
            self.max_file_size_files = None
            self._segment_path = lambda: "directory"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-udp-cfg:ip-udp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(IpUdp.Directory, ['directoryname', 'max_udp_debug_files', 'max_file_size_files'], name, value)

    def clone_ptr(self):
        self._top_entity = IpUdp()
        return self._top_entity


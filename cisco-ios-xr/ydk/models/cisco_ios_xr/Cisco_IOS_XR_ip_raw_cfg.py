""" Cisco_IOS_XR_ip_raw_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-raw package configuration.

This module contains definitions
for the following management objects\:
  ip\-raw\: Global IP RAW configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class IpRaw(Entity):
    """
    Global IP RAW configuration
    
    .. attribute:: num_thread
    
    	RAW InQueue and OutQueue threads
    	**type**\:  :py:class:`NumThread <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_raw_cfg.IpRaw.NumThread>`
    
    	**presence node**\: True
    
    .. attribute:: directory
    
    	RAW directory details
    	**type**\:  :py:class:`Directory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_raw_cfg.IpRaw.Directory>`
    
    	**presence node**\: True
    
    .. attribute:: receive_q
    
    	RAW receive Queue Size
    	**type**\: int
    
    	**range:** 40..800
    
    

    """

    _prefix = 'ip-raw-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(IpRaw, self).__init__()
        self._top_entity = None

        self.yang_name = "ip-raw"
        self.yang_parent_name = "Cisco-IOS-XR-ip-raw-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("num-thread", ("num_thread", IpRaw.NumThread)), ("directory", ("directory", IpRaw.Directory))])
        self._leafs = OrderedDict([
            ('receive_q', (YLeaf(YType.uint32, 'receive-q'), ['int'])),
        ])
        self.receive_q = None

        self.num_thread = None
        self._children_name_map["num_thread"] = "num-thread"

        self.directory = None
        self._children_name_map["directory"] = "directory"
        self._segment_path = lambda: "Cisco-IOS-XR-ip-raw-cfg:ip-raw"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(IpRaw, ['receive_q'], name, value)


    class NumThread(Entity):
        """
        RAW InQueue and OutQueue threads
        
        .. attribute:: raw_in_q_threads
        
        	InQ Threads
        	**type**\: int
        
        	**range:** 1..16
        
        	**mandatory**\: True
        
        .. attribute:: raw_out_q_threads
        
        	OutQ Threads
        	**type**\: int
        
        	**range:** 1..16
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ip-raw-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(IpRaw.NumThread, self).__init__()

            self.yang_name = "num-thread"
            self.yang_parent_name = "ip-raw"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('raw_in_q_threads', (YLeaf(YType.uint32, 'raw-in-q-threads'), ['int'])),
                ('raw_out_q_threads', (YLeaf(YType.uint32, 'raw-out-q-threads'), ['int'])),
            ])
            self.raw_in_q_threads = None
            self.raw_out_q_threads = None
            self._segment_path = lambda: "num-thread"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-raw-cfg:ip-raw/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(IpRaw.NumThread, ['raw_in_q_threads', 'raw_out_q_threads'], name, value)


    class Directory(Entity):
        """
        RAW directory details
        
        .. attribute:: directoryname
        
        	Directory name
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: max_raw_debug_files
        
        	Set number of Debug files
        	**type**\: int
        
        	**range:** 1..18000
        
        	**default value**\: 256
        
        .. attribute:: max_file_size_files
        
        	Set size of debug files in bytes
        	**type**\: int
        
        	**range:** 1024..4294967295
        
        	**units**\: byte
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ip-raw-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(IpRaw.Directory, self).__init__()

            self.yang_name = "directory"
            self.yang_parent_name = "ip-raw"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('directoryname', (YLeaf(YType.str, 'directoryname'), ['str'])),
                ('max_raw_debug_files', (YLeaf(YType.uint32, 'max-raw-debug-files'), ['int'])),
                ('max_file_size_files', (YLeaf(YType.uint32, 'max-file-size-files'), ['int'])),
            ])
            self.directoryname = None
            self.max_raw_debug_files = None
            self.max_file_size_files = None
            self._segment_path = lambda: "directory"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-raw-cfg:ip-raw/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(IpRaw.Directory, ['directoryname', 'max_raw_debug_files', 'max_file_size_files'], name, value)

    def clone_ptr(self):
        self._top_entity = IpRaw()
        return self._top_entity


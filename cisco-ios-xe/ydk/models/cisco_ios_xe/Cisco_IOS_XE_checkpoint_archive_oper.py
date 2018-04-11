""" Cisco_IOS_XE_checkpoint_archive_oper 

This module contains a collection of YANG definitions for
monitoring the checkpoint archives in a Network Element.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CheckpointArchives(Entity):
    """
    Contents of the checkpoint archive information base
    
    .. attribute:: max
    
    	The maxium number of archives
    	**type**\: int
    
    	**range:** 0..255
    
    .. attribute:: current
    
    	The current number of archives
    	**type**\: int
    
    	**range:** 0..255
    
    .. attribute:: recent
    
    	The most recent archive
    	**type**\: str
    
    .. attribute:: archives
    
    	Archive information
    	**type**\:  :py:class:`Archives <ydk.models.cisco_ios_xe.Cisco_IOS_XE_checkpoint_archive_oper.CheckpointArchives.Archives>`
    
    

    """

    _prefix = 'checkpoint-archive-ios-xe-oper'
    _revision = '2017-04-01'

    def __init__(self):
        super(CheckpointArchives, self).__init__()
        self._top_entity = None

        self.yang_name = "checkpoint-archives"
        self.yang_parent_name = "Cisco-IOS-XE-checkpoint-archive-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("archives", ("archives", CheckpointArchives.Archives))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('max', YLeaf(YType.uint8, 'max')),
            ('current', YLeaf(YType.uint8, 'current')),
            ('recent', YLeaf(YType.str, 'recent')),
        ])
        self.max = None
        self.current = None
        self.recent = None

        self.archives = CheckpointArchives.Archives()
        self.archives.parent = self
        self._children_name_map["archives"] = "archives"
        self._children_yang_names.add("archives")
        self._segment_path = lambda: "Cisco-IOS-XE-checkpoint-archive-oper:checkpoint-archives"

    def __setattr__(self, name, value):
        self._perform_setattr(CheckpointArchives, ['max', 'current', 'recent'], name, value)


    class Archives(Entity):
        """
        Archive information
        
        .. attribute:: archive
        
        	List of archives
        	**type**\: list of  		 :py:class:`Archive <ydk.models.cisco_ios_xe.Cisco_IOS_XE_checkpoint_archive_oper.CheckpointArchives.Archives.Archive>`
        
        

        """

        _prefix = 'checkpoint-archive-ios-xe-oper'
        _revision = '2017-04-01'

        def __init__(self):
            super(CheckpointArchives.Archives, self).__init__()

            self.yang_name = "archives"
            self.yang_parent_name = "checkpoint-archives"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("archive", ("archive", CheckpointArchives.Archives.Archive))])
            self._leafs = OrderedDict()

            self.archive = YList(self)
            self._segment_path = lambda: "archives"
            self._absolute_path = lambda: "Cisco-IOS-XE-checkpoint-archive-oper:checkpoint-archives/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CheckpointArchives.Archives, [], name, value)


        class Archive(Entity):
            """
            List of archives
            
            .. attribute:: number  (key)
            
            	The archive number
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: name
            
            	The name of the archive
            	**type**\: str
            
            

            """

            _prefix = 'checkpoint-archive-ios-xe-oper'
            _revision = '2017-04-01'

            def __init__(self):
                super(CheckpointArchives.Archives.Archive, self).__init__()

                self.yang_name = "archive"
                self.yang_parent_name = "archives"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['number']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('number', YLeaf(YType.uint16, 'number')),
                    ('name', YLeaf(YType.str, 'name')),
                ])
                self.number = None
                self.name = None
                self._segment_path = lambda: "archive" + "[number='" + str(self.number) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-checkpoint-archive-oper:checkpoint-archives/archives/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CheckpointArchives.Archives.Archive, ['number', 'name'], name, value)

    def clone_ptr(self):
        self._top_entity = CheckpointArchives()
        return self._top_entity


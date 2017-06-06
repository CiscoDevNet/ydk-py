""" Cisco_IOS_XR_shellutil_filesystem_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR shellutil\-filesystem package operational data.

This module contains definitions
for the following management objects\:
  file\-system\: List of filesystems

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class FileSystem(object):
    """
    List of filesystems
    
    .. attribute:: node
    
    	Node ID
    	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_filesystem_oper.FileSystem.Node>`
    
    

    """

    _prefix = 'shellutil-filesystem-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.node = YList()
        self.node.parent = self
        self.node.name = 'node'


    class Node(object):
        """
        Node ID
        
        .. attribute:: node_name  <key>
        
        	Node name
        	**type**\:  str
        
        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
        
        .. attribute:: file_system
        
        	Available file systems
        	**type**\: list of    :py:class:`FileSystem_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_filesystem_oper.FileSystem.Node.FileSystem_>`
        
        

        """

        _prefix = 'shellutil-filesystem-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node_name = None
            self.file_system = YList()
            self.file_system.parent = self
            self.file_system.name = 'file_system'


        class FileSystem_(object):
            """
            Available file systems
            
            .. attribute:: flags
            
            	Flags of file system
            	**type**\:  str
            
            .. attribute:: free
            
            	Free space in the file system in bytes
            	**type**\:  str
            
            	**units**\: byte
            
            .. attribute:: prefixes
            
            	Prefixes of file system
            	**type**\:  str
            
            .. attribute:: size
            
            	Size of the file system in bytes
            	**type**\:  str
            
            	**units**\: byte
            
            .. attribute:: type
            
            	Type of file system
            	**type**\:  str
            
            

            """

            _prefix = 'shellutil-filesystem-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.flags = None
                self.free = None
                self.prefixes = None
                self.size = None
                self.type = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-shellutil-filesystem-oper:file-system'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.flags is not None:
                    return True

                if self.free is not None:
                    return True

                if self.prefixes is not None:
                    return True

                if self.size is not None:
                    return True

                if self.type is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_shellutil_filesystem_oper as meta
                return meta._meta_table['FileSystem.Node.FileSystem_']['meta_info']

        @property
        def _common_path(self):
            if self.node_name is None:
                raise YPYModelError('Key property node_name is None')

            return '/Cisco-IOS-XR-shellutil-filesystem-oper:file-system/Cisco-IOS-XR-shellutil-filesystem-oper:node[Cisco-IOS-XR-shellutil-filesystem-oper:node-name = ' + str(self.node_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node_name is not None:
                return True

            if self.file_system is not None:
                for child_ref in self.file_system:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_shellutil_filesystem_oper as meta
            return meta._meta_table['FileSystem.Node']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-shellutil-filesystem-oper:file-system'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.node is not None:
            for child_ref in self.node:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_shellutil_filesystem_oper as meta
        return meta._meta_table['FileSystem']['meta_info']



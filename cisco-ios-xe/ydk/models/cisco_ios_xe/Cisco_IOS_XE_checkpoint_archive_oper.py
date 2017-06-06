""" Cisco_IOS_XE_checkpoint_archive_oper 

This module contains a collection of YANG definitions for
monitoring the checkpoint archives in a Network Element.Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class CheckpointArchive(object):
    """
    Contents of the show archive cli
    
    .. attribute:: archives
    
    	
    	**type**\:   :py:class:`Archives <ydk.models.cisco_ios_xe.Cisco_IOS_XE_checkpoint_archive_oper.CheckpointArchive.Archives>`
    
    .. attribute:: current
    
    	The current number of archives
    	**type**\:  int
    
    	**range:** 0..255
    
    .. attribute:: max
    
    	The maxium number of archives
    	**type**\:  int
    
    	**range:** 0..255
    
    .. attribute:: recent
    
    	The most recent archive
    	**type**\:  str
    
    

    """

    _prefix = 'checkpoint-archive-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        self.archives = CheckpointArchive.Archives()
        self.archives.parent = self
        self.current = None
        self.max = None
        self.recent = None


    class Archives(object):
        """
        
        
        .. attribute:: archive
        
        	Archive information
        	**type**\: list of    :py:class:`Archive <ydk.models.cisco_ios_xe.Cisco_IOS_XE_checkpoint_archive_oper.CheckpointArchive.Archives.Archive>`
        
        

        """

        _prefix = 'checkpoint-archive-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.archive = YList()
            self.archive.parent = self
            self.archive.name = 'archive'


        class Archive(object):
            """
            Archive information
            
            .. attribute:: number  <key>
            
            	The archive number
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: name
            
            	the name of the archive
            	**type**\:  str
            
            

            """

            _prefix = 'checkpoint-archive-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.number = None
                self.name = None

            @property
            def _common_path(self):
                if self.number is None:
                    raise YPYModelError('Key property number is None')

                return '/Cisco-IOS-XE-checkpoint-archive-oper:checkpoint-archive/Cisco-IOS-XE-checkpoint-archive-oper:archives/Cisco-IOS-XE-checkpoint-archive-oper:archive[Cisco-IOS-XE-checkpoint-archive-oper:number = ' + str(self.number) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.number is not None:
                    return True

                if self.name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_checkpoint_archive_oper as meta
                return meta._meta_table['CheckpointArchive.Archives.Archive']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-checkpoint-archive-oper:checkpoint-archive/Cisco-IOS-XE-checkpoint-archive-oper:archives'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.archive is not None:
                for child_ref in self.archive:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_checkpoint_archive_oper as meta
            return meta._meta_table['CheckpointArchive.Archives']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-checkpoint-archive-oper:checkpoint-archive'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.archives is not None and self.archives._has_data():
            return True

        if self.current is not None:
            return True

        if self.max is not None:
            return True

        if self.recent is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_checkpoint_archive_oper as meta
        return meta._meta_table['CheckpointArchive']['meta_info']



""" Cisco_IOS_XR_linux_os_reboot_history_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR linux\-os\-reboot\-history package operational data.

This module contains definitions
for the following management objects\:
  reboot\-history\: Reboot History information

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class RebootHistory(object):
    """
    Reboot History information
    
    .. attribute:: node
    
    	Node ID
    	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_reboot_history_oper.RebootHistory.Node>`
    
    

    """

    _prefix = 'linux-os-reboot-history-oper'
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
        
        .. attribute:: reboot_history
        
        	Last Reboots
        	**type**\: list of    :py:class:`RebootHistory_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_reboot_history_oper.RebootHistory.Node.RebootHistory_>`
        
        

        """

        _prefix = 'linux-os-reboot-history-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node_name = None
            self.reboot_history = YList()
            self.reboot_history.parent = self
            self.reboot_history.name = 'reboot_history'


        class RebootHistory_(object):
            """
            Last Reboots
            
            .. attribute:: cause_code
            
            	Cause code for reboot
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: no
            
            	Number count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: reason
            
            	Reason for reboot
            	**type**\:  str
            
            .. attribute:: time
            
            	Time of reboot
            	**type**\:  str
            
            

            """

            _prefix = 'linux-os-reboot-history-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.cause_code = None
                self.no = None
                self.reason = None
                self.time = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-linux-os-reboot-history-oper:reboot-history'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.cause_code is not None:
                    return True

                if self.no is not None:
                    return True

                if self.reason is not None:
                    return True

                if self.time is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_linux_os_reboot_history_oper as meta
                return meta._meta_table['RebootHistory.Node.RebootHistory_']['meta_info']

        @property
        def _common_path(self):
            if self.node_name is None:
                raise YPYModelError('Key property node_name is None')

            return '/Cisco-IOS-XR-linux-os-reboot-history-oper:reboot-history/Cisco-IOS-XR-linux-os-reboot-history-oper:node[Cisco-IOS-XR-linux-os-reboot-history-oper:node-name = ' + str(self.node_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node_name is not None:
                return True

            if self.reboot_history is not None:
                for child_ref in self.reboot_history:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_linux_os_reboot_history_oper as meta
            return meta._meta_table['RebootHistory.Node']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-linux-os-reboot-history-oper:reboot-history'

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_linux_os_reboot_history_oper as meta
        return meta._meta_table['RebootHistory']['meta_info']



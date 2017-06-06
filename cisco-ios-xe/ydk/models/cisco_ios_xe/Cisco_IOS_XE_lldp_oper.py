""" Cisco_IOS_XE_lldp_oper 

This module contains a collection of YANG definitions for
monitoring LLDP state information.Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class LldpEntries(object):
    """
    Data nodes for LLDP entries.
    
    .. attribute:: lldp_entry
    
    	The list of LLDP entries
    	**type**\: list of    :py:class:`LldpEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lldp_oper.LldpEntries.LldpEntry>`
    
    

    """

    _prefix = 'lldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        self.lldp_entry = YList()
        self.lldp_entry.parent = self
        self.lldp_entry.name = 'lldp_entry'


    class LldpEntry(object):
        """
        The list of LLDP entries.
        
        .. attribute:: device_id  <key>
        
        	The device ID of the link
        	**type**\:  str
        
        .. attribute:: local_interface  <key>
        
        	The name of the local interface on the current device
        	**type**\:  str
        
        .. attribute:: connecting_interface  <key>
        
        	The name of the connected interface to 'local\-interface'
        	**type**\:  str
        
        .. attribute:: capabilities
        
        	
        	**type**\:   :py:class:`Capabilities <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lldp_oper.LldpEntries.LldpEntry.Capabilities>`
        
        .. attribute:: ttl
        
        	TTL denoting hold\-time of this link entry
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'lldp-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.device_id = None
            self.local_interface = None
            self.connecting_interface = None
            self.capabilities = LldpEntries.LldpEntry.Capabilities()
            self.capabilities.parent = self
            self.ttl = None


        class Capabilities(object):
            """
            
            
            .. attribute:: access_point
            
            	
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: bridge
            
            	
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: docsis
            
            	
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: other
            
            	
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: repeater
            
            	
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: router
            
            	
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: station
            
            	
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: telephone
            
            	
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'lldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.access_point = None
                self.bridge = None
                self.docsis = None
                self.other = None
                self.repeater = None
                self.router = None
                self.station = None
                self.telephone = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XE-lldp-oper:capabilities'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.access_point is not None:
                    return True

                if self.bridge is not None:
                    return True

                if self.docsis is not None:
                    return True

                if self.other is not None:
                    return True

                if self.repeater is not None:
                    return True

                if self.router is not None:
                    return True

                if self.station is not None:
                    return True

                if self.telephone is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_lldp_oper as meta
                return meta._meta_table['LldpEntries.LldpEntry.Capabilities']['meta_info']

        @property
        def _common_path(self):
            if self.device_id is None:
                raise YPYModelError('Key property device_id is None')
            if self.local_interface is None:
                raise YPYModelError('Key property local_interface is None')
            if self.connecting_interface is None:
                raise YPYModelError('Key property connecting_interface is None')

            return '/Cisco-IOS-XE-lldp-oper:lldp-entries/Cisco-IOS-XE-lldp-oper:lldp-entry[Cisco-IOS-XE-lldp-oper:device-id = ' + str(self.device_id) + '][Cisco-IOS-XE-lldp-oper:local-interface = ' + str(self.local_interface) + '][Cisco-IOS-XE-lldp-oper:connecting-interface = ' + str(self.connecting_interface) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.device_id is not None:
                return True

            if self.local_interface is not None:
                return True

            if self.connecting_interface is not None:
                return True

            if self.capabilities is not None and self.capabilities._has_data():
                return True

            if self.ttl is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_lldp_oper as meta
            return meta._meta_table['LldpEntries.LldpEntry']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-lldp-oper:lldp-entries'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.lldp_entry is not None:
            for child_ref in self.lldp_entry:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_lldp_oper as meta
        return meta._meta_table['LldpEntries']['meta_info']



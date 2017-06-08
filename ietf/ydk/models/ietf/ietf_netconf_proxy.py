""" ietf_netconf_proxy 

NETCONF Protocol Data Types and Protocol Operations.

Copyright (c) 2011 IETF Trust and the persons identified as
the document authors.  All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

This YANG module describe how to define a netconf proxy

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Proxy(object):
    """
    Container for NETCONF Proxy
    
    .. attribute:: proxy_name
    
    	Proxy name
    	**type**\:  str
    
    .. attribute:: target_list
    
    	List for target information
    	**type**\: list of    :py:class:`TargetList <ydk.models.ietf.ietf_netconf_proxy.Proxy.TargetList>`
    
    

    """

    _prefix = 'np'
    _revision = '2017-03-09'

    def __init__(self):
        self.proxy_name = None
        self.target_list = YList()
        self.target_list.parent = self
        self.target_list.name = 'target_list'


    class TargetList(object):
        """
        List for target information
        
        .. attribute:: target_id  <key>
        
        	Target ID
        	**type**\:  str
        
        .. attribute:: authentication
        
        	Authentication
        	**type**\:  str
        
        .. attribute:: protocol
        
        	Support protocols
        	**type**\:  str
        
        

        """

        _prefix = 'np'
        _revision = '2017-03-09'

        def __init__(self):
            self.parent = None
            self.target_id = None
            self.authentication = None
            self.protocol = None

        @property
        def _common_path(self):
            if self.target_id is None:
                raise YPYModelError('Key property target_id is None')

            return '/ietf-netconf-proxy:proxy/ietf-netconf-proxy:target-list[ietf-netconf-proxy:target-id = ' + str(self.target_id) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.target_id is not None:
                return True

            if self.authentication is not None:
                return True

            if self.protocol is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_netconf_proxy as meta
            return meta._meta_table['Proxy.TargetList']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-netconf-proxy:proxy'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.proxy_name is not None:
            return True

        if self.target_list is not None:
            for child_ref in self.target_list:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_netconf_proxy as meta
        return meta._meta_table['Proxy']['meta_info']



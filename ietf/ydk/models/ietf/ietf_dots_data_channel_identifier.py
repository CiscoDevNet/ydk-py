""" ietf_dots_data_channel_identifier 

This module contains YANG definition for
configuring identifiers for resources using DOTS data channel

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Identifier(object):
    """
    top level container for identifiers
    
    .. attribute:: alias
    
    	list of identifiers
    	**type**\: list of    :py:class:`Alias <ydk.models.ietf.ietf_dots_data_channel_identifier.Identifier.Alias>`
    
    

    """

    _prefix = 'alias'
    _revision = '2016-11-28'

    def __init__(self):
        self.alias = YList()
        self.alias.parent = self
        self.alias.name = 'alias'


    class Alias(object):
        """
        list of identifiers
        
        .. attribute:: alias_name  <key>
        
        	alias name
        	**type**\:  str
        
        .. attribute:: e_164
        
        	E.164 number
        	**type**\:  list of str
        
        .. attribute:: fqdn
        
        	FQDN
        	**type**\:  list of str
        
        	**pattern:** ((([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.)\*([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.?)\|\\.
        
        .. attribute:: ip
        
        	IP address
        	**type**\: one of the below types:
        
        	**type**\:  list of str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        
        ----
        	**type**\:  list of str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        
        ----
        .. attribute:: port_range
        
        	Port range. When only lower\-port is present, it represents a single port
        	**type**\: list of    :py:class:`PortRange <ydk.models.ietf.ietf_dots_data_channel_identifier.Identifier.Alias.PortRange>`
        
        .. attribute:: prefix
        
        	prefix
        	**type**\: one of the below types:
        
        	**type**\:  list of str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
        
        
        ----
        	**type**\:  list of str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
        
        
        ----
        .. attribute:: traffic_protocol
        
        	Internet Protocol number
        	**type**\:  list of int
        
        	**range:** 0..255
        
        .. attribute:: uri
        
        	URI
        	**type**\:  list of str
        
        

        """

        _prefix = 'alias'
        _revision = '2016-11-28'

        def __init__(self):
            self.parent = None
            self.alias_name = None
            self.e_164 = YLeafList()
            self.e_164.parent = self
            self.e_164.name = 'e_164'
            self.fqdn = YLeafList()
            self.fqdn.parent = self
            self.fqdn.name = 'fqdn'
            self.ip = YLeafList()
            self.ip.parent = self
            self.ip.name = 'ip'
            self.port_range = YList()
            self.port_range.parent = self
            self.port_range.name = 'port_range'
            self.prefix = YLeafList()
            self.prefix.parent = self
            self.prefix.name = 'prefix'
            self.traffic_protocol = YLeafList()
            self.traffic_protocol.parent = self
            self.traffic_protocol.name = 'traffic_protocol'
            self.uri = YLeafList()
            self.uri.parent = self
            self.uri.name = 'uri'


        class PortRange(object):
            """
            Port range. When only lower\-port is present,
            it represents a single port.
            
            .. attribute:: lower_port  <key>
            
            	lower port
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**mandatory**\: True
            
            .. attribute:: upper_port  <key>
            
            	upper port
            	**type**\:  int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'alias'
            _revision = '2016-11-28'

            def __init__(self):
                self.parent = None
                self.lower_port = None
                self.upper_port = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')
                if self.lower_port is None:
                    raise YPYModelError('Key property lower_port is None')
                if self.upper_port is None:
                    raise YPYModelError('Key property upper_port is None')

                return self.parent._common_path +'/ietf-dots-data-channel-identifier:port-range[ietf-dots-data-channel-identifier:lower-port = ' + str(self.lower_port) + '][ietf-dots-data-channel-identifier:upper-port = ' + str(self.upper_port) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.lower_port is not None:
                    return True

                if self.upper_port is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_dots_data_channel_identifier as meta
                return meta._meta_table['Identifier.Alias.PortRange']['meta_info']

        @property
        def _common_path(self):
            if self.alias_name is None:
                raise YPYModelError('Key property alias_name is None')

            return '/ietf-dots-data-channel-identifier:identifier/ietf-dots-data-channel-identifier:alias[ietf-dots-data-channel-identifier:alias-name = ' + str(self.alias_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.alias_name is not None:
                return True

            if self.e_164 is not None:
                for child in self.e_164:
                    if child is not None:
                        return True

            if self.fqdn is not None:
                for child in self.fqdn:
                    if child is not None:
                        return True

            if self.ip is not None:
                for child in self.ip:
                    if child is not None:
                        return True

            if self.port_range is not None:
                for child_ref in self.port_range:
                    if child_ref._has_data():
                        return True

            if self.prefix is not None:
                for child in self.prefix:
                    if child is not None:
                        return True

            if self.traffic_protocol is not None:
                for child in self.traffic_protocol:
                    if child is not None:
                        return True

            if self.uri is not None:
                for child in self.uri:
                    if child is not None:
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_dots_data_channel_identifier as meta
            return meta._meta_table['Identifier.Alias']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-dots-data-channel-identifier:identifier'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.alias is not None:
            for child_ref in self.alias:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dots_data_channel_identifier as meta
        return meta._meta_table['Identifier']['meta_info']



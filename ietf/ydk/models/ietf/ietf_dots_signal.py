""" ietf_dots_signal 

This module contains YANG definition for DOTS
signal sent by the DOTS client to the DOTS server

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class MitigationScope(object):
    """
    top level container for mitigation request
    
    .. attribute:: scope
    
    	Identifier for the mitigation request
    	**type**\: list of    :py:class:`Scope <ydk.models.ietf.ietf_dots_signal.MitigationScope.Scope>`
    
    

    """

    _prefix = 'signal'
    _revision = '2016-11-28'

    def __init__(self):
        self.scope = YList()
        self.scope.parent = self
        self.scope.name = 'scope'


    class Scope(object):
        """
        Identifier for the mitigation request
        
        .. attribute:: policy_id  <key>
        
        	policy identifier
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: alias
        
        	alias name
        	**type**\:  list of str
        
        .. attribute:: e_164
        
        	E.164 number
        	**type**\:  list of str
        
        .. attribute:: fqdn
        
        	FQDN
        	**type**\:  list of str
        
        	**pattern:** ((([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.)\*([a\-zA\-Z0\-9\_]([a\-zA\-Z0\-9\\\-\_]){0,61})?[a\-zA\-Z0\-9]\\.?)\|\\.
        
        .. attribute:: lifetime
        
        	lifetime
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: target_ip
        
        	IP address
        	**type**\: one of the below types:
        
        	**type**\:  list of str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        
        ----
        	**type**\:  list of str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        
        ----
        .. attribute:: target_port_range
        
        	Port range. When only lower\-port is present, it represents a single port
        	**type**\: list of    :py:class:`TargetPortRange <ydk.models.ietf.ietf_dots_signal.MitigationScope.Scope.TargetPortRange>`
        
        .. attribute:: target_prefix
        
        	prefix
        	**type**\: one of the below types:
        
        	**type**\:  list of str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
        
        
        ----
        	**type**\:  list of str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
        
        
        ----
        .. attribute:: target_protocol
        
        	Internet Protocol number
        	**type**\:  list of int
        
        	**range:** 0..255
        
        .. attribute:: uri
        
        	URI
        	**type**\:  list of str
        
        

        """

        _prefix = 'signal'
        _revision = '2016-11-28'

        def __init__(self):
            self.parent = None
            self.policy_id = None
            self.alias = YLeafList()
            self.alias.parent = self
            self.alias.name = 'alias'
            self.e_164 = YLeafList()
            self.e_164.parent = self
            self.e_164.name = 'e_164'
            self.fqdn = YLeafList()
            self.fqdn.parent = self
            self.fqdn.name = 'fqdn'
            self.lifetime = None
            self.target_ip = YLeafList()
            self.target_ip.parent = self
            self.target_ip.name = 'target_ip'
            self.target_port_range = YList()
            self.target_port_range.parent = self
            self.target_port_range.name = 'target_port_range'
            self.target_prefix = YLeafList()
            self.target_prefix.parent = self
            self.target_prefix.name = 'target_prefix'
            self.target_protocol = YLeafList()
            self.target_protocol.parent = self
            self.target_protocol.name = 'target_protocol'
            self.uri = YLeafList()
            self.uri.parent = self
            self.uri.name = 'uri'


        class TargetPortRange(object):
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

            _prefix = 'signal'
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

                return self.parent._common_path +'/ietf-dots-signal:target-port-range[ietf-dots-signal:lower-port = ' + str(self.lower_port) + '][ietf-dots-signal:upper-port = ' + str(self.upper_port) + ']'

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
                from ydk.models.ietf._meta import _ietf_dots_signal as meta
                return meta._meta_table['MitigationScope.Scope.TargetPortRange']['meta_info']

        @property
        def _common_path(self):
            if self.policy_id is None:
                raise YPYModelError('Key property policy_id is None')

            return '/ietf-dots-signal:mitigation-scope/ietf-dots-signal:scope[ietf-dots-signal:policy-id = ' + str(self.policy_id) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.policy_id is not None:
                return True

            if self.alias is not None:
                for child in self.alias:
                    if child is not None:
                        return True

            if self.e_164 is not None:
                for child in self.e_164:
                    if child is not None:
                        return True

            if self.fqdn is not None:
                for child in self.fqdn:
                    if child is not None:
                        return True

            if self.lifetime is not None:
                return True

            if self.target_ip is not None:
                for child in self.target_ip:
                    if child is not None:
                        return True

            if self.target_port_range is not None:
                for child_ref in self.target_port_range:
                    if child_ref._has_data():
                        return True

            if self.target_prefix is not None:
                for child in self.target_prefix:
                    if child is not None:
                        return True

            if self.target_protocol is not None:
                for child in self.target_protocol:
                    if child is not None:
                        return True

            if self.uri is not None:
                for child in self.uri:
                    if child is not None:
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_dots_signal as meta
            return meta._meta_table['MitigationScope.Scope']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-dots-signal:mitigation-scope'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.scope is not None:
            for child_ref in self.scope:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_dots_signal as meta
        return meta._meta_table['MitigationScope']['meta_info']



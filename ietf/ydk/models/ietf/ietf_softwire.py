""" ietf_softwire 

This document defines a YANG data model for the configuration and
management of A+P Softwire Border Routers (BRs) and Customer
Premises Equipment (CEs). It covers Lightweight 4over6,
MAP\-E and MAP\-T mechanisms.

Copyright (c) 2016 IETF Trust and the persons identified
as authors of the code. All rights reserved.
This version of this YANG module is part of RFC XXX; see the RFC
itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class SoftwireConfig(object):
    """
    The configuration data for Softwire instances. And the shared
    data describes the softwire data model which is common to all of
    the different softwire mechanisms, such as description.
    
    .. attribute:: algorithm
    
    	Indicate the instances support the MAP\-E and MAP\-T function. The instances advertise the map\-e feature through the capability exchange mechanism when a NETCONF session is established
    	**type**\:   :py:class:`Algorithm <ydk.models.ietf.ietf_softwire.SoftwireConfig.Algorithm>`
    
    .. attribute:: binding
    
    	lw4over6 (binding) configuration
    	**type**\:   :py:class:`Binding <ydk.models.ietf.ietf_softwire.SoftwireConfig.Binding>`
    
    .. attribute:: description
    
    	A textual description of Softwire
    	**type**\:  str
    
    

    """

    _prefix = 'softwire'
    _revision = '2016-06-04'

    def __init__(self):
        self.algorithm = SoftwireConfig.Algorithm()
        self.algorithm.parent = self
        self.binding = SoftwireConfig.Binding()
        self.binding.parent = self
        self.description = None


    class Binding(object):
        """
        lw4over6 (binding) configuration.
        
        .. attribute:: br
        
        	Indicate this instance supports the lwAFTR (BR) function. The instances advertise the BR feature through the capability exchange mechanism when a NETCONF session is established
        	**type**\:   :py:class:`Br <ydk.models.ietf.ietf_softwire.SoftwireConfig.Binding.Br>`
        
        .. attribute:: ce
        
        	Indicate this instance supports the lwB4 (CE) function. The instances advertise the CE feature through the capability exchange mechanism when a NETCONF session is established
        	**type**\:   :py:class:`Ce <ydk.models.ietf.ietf_softwire.SoftwireConfig.Binding.Ce>`
        
        

        """

        _prefix = 'softwire'
        _revision = '2016-06-04'

        def __init__(self):
            self.parent = None
            self.br = SoftwireConfig.Binding.Br()
            self.br.parent = self
            self.ce = SoftwireConfig.Binding.Ce()
            self.ce.parent = self


        class Br(object):
            """
            Indicate this instance supports the lwAFTR (BR) function.
            The instances advertise the BR feature through the
            capability exchange mechanism when a NETCONF session is
            established.
            
            .. attribute:: br_instances
            
            	A set of BRs to be configured
            	**type**\:   :py:class:`BrInstances <ydk.models.ietf.ietf_softwire.SoftwireConfig.Binding.Br.BrInstances>`
            
            .. attribute:: enable
            
            	Enable/disable the lwAFTR (BR) function
            	**type**\:  bool
            
            

            """

            _prefix = 'softwire'
            _revision = '2016-06-04'

            def __init__(self):
                self.parent = None
                self.br_instances = SoftwireConfig.Binding.Br.BrInstances()
                self.br_instances.parent = self
                self.enable = None


            class BrInstances(object):
                """
                A set of BRs to be configured.
                
                .. attribute:: br_instance
                
                	A set of lwAFTRs to be configured
                	**type**\: list of    :py:class:`BrInstance <ydk.models.ietf.ietf_softwire.SoftwireConfig.Binding.Br.BrInstances.BrInstance>`
                
                

                """

                _prefix = 'softwire'
                _revision = '2016-06-04'

                def __init__(self):
                    self.parent = None
                    self.br_instance = YList()
                    self.br_instance.parent = self
                    self.br_instance.name = 'br_instance'


                class BrInstance(object):
                    """
                    A set of lwAFTRs to be configured.
                    
                    .. attribute:: id  <key>
                    
                    	An instance identifier
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    .. attribute:: binding_table
                    
                    	binding table
                    	**type**\:   :py:class:`BindingTable <ydk.models.ietf.ietf_softwire.SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTable>`
                    
                    .. attribute:: binding_table_version
                    
                    	binding table's version
                    	**type**\:   :py:class:`BindingTableVersion <ydk.models.ietf.ietf_softwire.SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTableVersion>`
                    
                    .. attribute:: name
                    
                    	The name for the lwaftr
                    	**type**\:  str
                    
                    .. attribute:: softwire_num_threshold
                    
                    	The maximum number of tunnels that can be created on the lwAFTR
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    .. attribute:: tunnel_path_mru
                    
                    	The path MRU for Lightweight 4over6 tunnel
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: tunnel_payload_mtu
                    
                    	The payload MTU for Lightweight 4over6 tunnel
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'softwire'
                    _revision = '2016-06-04'

                    def __init__(self):
                        self.parent = None
                        self.id = None
                        self.binding_table = SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTable()
                        self.binding_table.parent = self
                        self.binding_table_version = SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTableVersion()
                        self.binding_table_version.parent = self
                        self.name = None
                        self.softwire_num_threshold = None
                        self.tunnel_path_mru = None
                        self.tunnel_payload_mtu = None


                    class BindingTableVersion(object):
                        """
                        binding table's version
                        
                        .. attribute:: binding_table_date
                        
                        	Timestamp to the binding table
                        	**type**\:  str
                        
                        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                        
                        .. attribute:: binding_table_version
                        
                        	Incremental version number to the binding table
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'softwire'
                        _revision = '2016-06-04'

                        def __init__(self):
                            self.parent = None
                            self.binding_table_date = None
                            self.binding_table_version = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-softwire:binding-table-version'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.binding_table_date is not None:
                                return True

                            if self.binding_table_version is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_softwire as meta
                            return meta._meta_table['SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTableVersion']['meta_info']


                    class BindingTable(object):
                        """
                        binding table
                        
                        .. attribute:: binding_entry
                        
                        	binding entry
                        	**type**\: list of    :py:class:`BindingEntry <ydk.models.ietf.ietf_softwire.SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTable.BindingEntry>`
                        
                        

                        """

                        _prefix = 'softwire'
                        _revision = '2016-06-04'

                        def __init__(self):
                            self.parent = None
                            self.binding_entry = YList()
                            self.binding_entry.parent = self
                            self.binding_entry.name = 'binding_entry'


                        class BindingEntry(object):
                            """
                            binding entry
                            
                            .. attribute:: binding_ipv6info  <key>
                            
                            	The IPv6 information for a binding entry. If this is an IPv6 prefix, it indicates that the IPv6 source address of the lwB4 is constructed according to the description in RFC7596; if it is an IPv6 address, it means the lwB4 uses any /128 address from the assigned IPv6 prefix. 
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                            
                            	**mandatory**\: True
                            
                            
                            ----
                            .. attribute:: binding_ipv4_addr
                            
                            	The IPv4 address assigned to the lwB4, which is used as the IPv4 external address for lwB4 local NAPT44
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: br_ipv6_addr
                            
                            	The IPv6 address for lwaftr
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            .. attribute:: lifetime
                            
                            	The lifetime for the binding entry
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: seconds
                            
                            .. attribute:: port_set
                            
                            	For Lightweight 4over6, the default value of offset should be 0, to configure one contiguous port range
                            	**type**\:   :py:class:`PortSet <ydk.models.ietf.ietf_softwire.SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTable.BindingEntry.PortSet>`
                            
                            

                            """

                            _prefix = 'softwire'
                            _revision = '2016-06-04'

                            def __init__(self):
                                self.parent = None
                                self.binding_ipv6info = None
                                self.binding_ipv4_addr = None
                                self.br_ipv6_addr = None
                                self.lifetime = None
                                self.port_set = SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTable.BindingEntry.PortSet()
                                self.port_set.parent = self


                            class PortSet(object):
                                """
                                For Lightweight 4over6, the default value
                                of offset should be 0, to configure one contiguous
                                port range.
                                
                                .. attribute:: psid
                                
                                	Port Set Identifier (PSID) value, which identifies a set of ports algorithmically
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                	**mandatory**\: True
                                
                                .. attribute:: psid_len
                                
                                	The length of PSID, representing the sharing ratio for an IPv4 address
                                	**type**\:  int
                                
                                	**range:** 0..15
                                
                                	**mandatory**\: True
                                
                                .. attribute:: psid_offset
                                
                                	The number of offset bits. In Lightweight 4over6, the default value is 0 for assigning one contiguous port range. In MAP\-E/T, the default value is 6, which excludes system ports by default and assigns port ranges distribute across the entire port space. If the this parameter is larger than 0, the value of offset MUST be greater than 0
                                	**type**\:  int
                                
                                	**range:** 0..16
                                
                                	**default value**\: 0
                                
                                

                                """

                                _prefix = 'softwire'
                                _revision = '2016-06-04'

                                def __init__(self):
                                    self.parent = None
                                    self.psid = None
                                    self.psid_len = None
                                    self.psid_offset = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/ietf-softwire:port-set'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.psid is not None:
                                        return True

                                    if self.psid_len is not None:
                                        return True

                                    if self.psid_offset is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_softwire as meta
                                    return meta._meta_table['SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTable.BindingEntry.PortSet']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.binding_ipv6info is None:
                                    raise YPYModelError('Key property binding_ipv6info is None')

                                return self.parent._common_path +'/ietf-softwire:binding-entry[ietf-softwire:binding-ipv6info = ' + str(self.binding_ipv6info) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.binding_ipv6info is not None:
                                    return True

                                if self.binding_ipv4_addr is not None:
                                    return True

                                if self.br_ipv6_addr is not None:
                                    return True

                                if self.lifetime is not None:
                                    return True

                                if self.port_set is not None and self.port_set._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_softwire as meta
                                return meta._meta_table['SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTable.BindingEntry']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-softwire:binding-table'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.binding_entry is not None:
                                for child_ref in self.binding_entry:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_softwire as meta
                            return meta._meta_table['SoftwireConfig.Binding.Br.BrInstances.BrInstance.BindingTable']['meta_info']

                    @property
                    def _common_path(self):
                        if self.id is None:
                            raise YPYModelError('Key property id is None')

                        return '/ietf-softwire:softwire-config/ietf-softwire:binding/ietf-softwire:br/ietf-softwire:br-instances/ietf-softwire:br-instance[ietf-softwire:id = ' + str(self.id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.id is not None:
                            return True

                        if self.binding_table is not None and self.binding_table._has_data():
                            return True

                        if self.binding_table_version is not None and self.binding_table_version._has_data():
                            return True

                        if self.name is not None:
                            return True

                        if self.softwire_num_threshold is not None:
                            return True

                        if self.tunnel_path_mru is not None:
                            return True

                        if self.tunnel_payload_mtu is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_softwire as meta
                        return meta._meta_table['SoftwireConfig.Binding.Br.BrInstances.BrInstance']['meta_info']

                @property
                def _common_path(self):

                    return '/ietf-softwire:softwire-config/ietf-softwire:binding/ietf-softwire:br/ietf-softwire:br-instances'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.br_instance is not None:
                        for child_ref in self.br_instance:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_softwire as meta
                    return meta._meta_table['SoftwireConfig.Binding.Br.BrInstances']['meta_info']

            @property
            def _common_path(self):

                return '/ietf-softwire:softwire-config/ietf-softwire:binding/ietf-softwire:br'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.br_instances is not None and self.br_instances._has_data():
                    return True

                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_softwire as meta
                return meta._meta_table['SoftwireConfig.Binding.Br']['meta_info']


        class Ce(object):
            """
            Indicate this instance supports the lwB4 (CE) function.
            The instances advertise the CE feature through the
            capability exchange mechanism when a NETCONF session is
            established.
            
            .. attribute:: ce_instances
            
            	A set of CEs to be configured
            	**type**\:   :py:class:`CeInstances <ydk.models.ietf.ietf_softwire.SoftwireConfig.Binding.Ce.CeInstances>`
            
            .. attribute:: enable
            
            	Enable/disable the lwB4 (CE) function
            	**type**\:  bool
            
            

            """

            _prefix = 'softwire'
            _revision = '2016-06-04'

            def __init__(self):
                self.parent = None
                self.ce_instances = SoftwireConfig.Binding.Ce.CeInstances()
                self.ce_instances.parent = self
                self.enable = None


            class CeInstances(object):
                """
                A set of CEs to be configured.
                
                .. attribute:: ce_instance
                
                	instances for CE
                	**type**\: list of    :py:class:`CeInstance <ydk.models.ietf.ietf_softwire.SoftwireConfig.Binding.Ce.CeInstances.CeInstance>`
                
                

                """

                _prefix = 'softwire'
                _revision = '2016-06-04'

                def __init__(self):
                    self.parent = None
                    self.ce_instance = YList()
                    self.ce_instance.parent = self
                    self.ce_instance.name = 'ce_instance'


                class CeInstance(object):
                    """
                    instances for CE
                    
                    .. attribute:: binding_ipv6info  <key>
                    
                    	The IPv6 information for a binding entry. If this is an IPv6 prefix, it indicates that the IPv6 source address of the lwB4 is constructed according to the description in RFC7596; if it is an IPv6 address, it means the lwB4 uses any /128 address from the assigned IPv6 prefix. 
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**mandatory**\: True
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                    
                    	**mandatory**\: True
                    
                    
                    ----
                    .. attribute:: b4_ipv6_addr_format
                    
                    	The format of lwB4 (CE) IPv6 address. If set to true, it indicates that the IPv6 source address of the lwB4 is constructed according to the description in [RFC7596]; if set to false, the lwB4 (CE) can use any /128 address from the assigned IPv6 prefix
                    	**type**\:  bool
                    
                    	**mandatory**\: True
                    
                    .. attribute:: binding_ipv4_addr
                    
                    	The IPv4 address assigned to the lwB4, which is used as the IPv4 external address for lwB4 local NAPT44
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**mandatory**\: True
                    
                    .. attribute:: br_ipv6_addr
                    
                    	The IPv6 address for lwaftr
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**mandatory**\: True
                    
                    .. attribute:: lifetime
                    
                    	The lifetime for the binding entry
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: seconds
                    
                    .. attribute:: name
                    
                    	The CE's name
                    	**type**\:  str
                    
                    .. attribute:: port_set
                    
                    	For Lightweight 4over6, the default value of offset should be 0, to configure one contiguous port range
                    	**type**\:   :py:class:`PortSet <ydk.models.ietf.ietf_softwire.SoftwireConfig.Binding.Ce.CeInstances.CeInstance.PortSet>`
                    
                    .. attribute:: tunnel_path_mru
                    
                    	The path MRU for Lightweight 4over6 tunnel
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: tunnel_payload_mtu
                    
                    	The payload MTU for Lightweight 4over6 tunnel
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'softwire'
                    _revision = '2016-06-04'

                    def __init__(self):
                        self.parent = None
                        self.binding_ipv6info = None
                        self.b4_ipv6_addr_format = None
                        self.binding_ipv4_addr = None
                        self.br_ipv6_addr = None
                        self.lifetime = None
                        self.name = None
                        self.port_set = SoftwireConfig.Binding.Ce.CeInstances.CeInstance.PortSet()
                        self.port_set.parent = self
                        self.tunnel_path_mru = None
                        self.tunnel_payload_mtu = None


                    class PortSet(object):
                        """
                        For Lightweight 4over6, the default value
                        of offset should be 0, to configure one contiguous
                        port range.
                        
                        .. attribute:: psid
                        
                        	Port Set Identifier (PSID) value, which identifies a set of ports algorithmically
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        	**mandatory**\: True
                        
                        .. attribute:: psid_len
                        
                        	The length of PSID, representing the sharing ratio for an IPv4 address
                        	**type**\:  int
                        
                        	**range:** 0..15
                        
                        	**mandatory**\: True
                        
                        .. attribute:: psid_offset
                        
                        	The number of offset bits. In Lightweight 4over6, the default value is 0 for assigning one contiguous port range. In MAP\-E/T, the default value is 6, which excludes system ports by default and assigns port ranges distribute across the entire port space. If the this parameter is larger than 0, the value of offset MUST be greater than 0
                        	**type**\:  int
                        
                        	**range:** 0..16
                        
                        	**default value**\: 0
                        
                        

                        """

                        _prefix = 'softwire'
                        _revision = '2016-06-04'

                        def __init__(self):
                            self.parent = None
                            self.psid = None
                            self.psid_len = None
                            self.psid_offset = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-softwire:port-set'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.psid is not None:
                                return True

                            if self.psid_len is not None:
                                return True

                            if self.psid_offset is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_softwire as meta
                            return meta._meta_table['SoftwireConfig.Binding.Ce.CeInstances.CeInstance.PortSet']['meta_info']

                    @property
                    def _common_path(self):
                        if self.binding_ipv6info is None:
                            raise YPYModelError('Key property binding_ipv6info is None')

                        return '/ietf-softwire:softwire-config/ietf-softwire:binding/ietf-softwire:ce/ietf-softwire:ce-instances/ietf-softwire:ce-instance[ietf-softwire:binding-ipv6info = ' + str(self.binding_ipv6info) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.binding_ipv6info is not None:
                            return True

                        if self.b4_ipv6_addr_format is not None:
                            return True

                        if self.binding_ipv4_addr is not None:
                            return True

                        if self.br_ipv6_addr is not None:
                            return True

                        if self.lifetime is not None:
                            return True

                        if self.name is not None:
                            return True

                        if self.port_set is not None and self.port_set._has_data():
                            return True

                        if self.tunnel_path_mru is not None:
                            return True

                        if self.tunnel_payload_mtu is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_softwire as meta
                        return meta._meta_table['SoftwireConfig.Binding.Ce.CeInstances.CeInstance']['meta_info']

                @property
                def _common_path(self):

                    return '/ietf-softwire:softwire-config/ietf-softwire:binding/ietf-softwire:ce/ietf-softwire:ce-instances'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.ce_instance is not None:
                        for child_ref in self.ce_instance:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_softwire as meta
                    return meta._meta_table['SoftwireConfig.Binding.Ce.CeInstances']['meta_info']

            @property
            def _common_path(self):

                return '/ietf-softwire:softwire-config/ietf-softwire:binding/ietf-softwire:ce'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.ce_instances is not None and self.ce_instances._has_data():
                    return True

                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_softwire as meta
                return meta._meta_table['SoftwireConfig.Binding.Ce']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-softwire:softwire-config/ietf-softwire:binding'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.br is not None and self.br._has_data():
                return True

            if self.ce is not None and self.ce._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_softwire as meta
            return meta._meta_table['SoftwireConfig.Binding']['meta_info']


    class Algorithm(object):
        """
        Indicate the instances support the MAP\-E and MAP\-T function.
        The instances advertise the map\-e feature through the
        capability exchange mechanism when a NETCONF session is
        established.
        
        .. attribute:: algo_instances
        
        	A set of MAP\-E or MAP\-T instances to be configured, applying to BRs and CEs. A MAP\-E/T instance defines a MAP domain comprising one or more MAP\-CE and MAP\-BR
        	**type**\:   :py:class:`AlgoInstances <ydk.models.ietf.ietf_softwire.SoftwireConfig.Algorithm.AlgoInstances>`
        
        .. attribute:: enable
        
        	Enable/disable the MAP\-E or MAP\-T function
        	**type**\:  bool
        
        

        """

        _prefix = 'softwire'
        _revision = '2016-06-04'

        def __init__(self):
            self.parent = None
            self.algo_instances = SoftwireConfig.Algorithm.AlgoInstances()
            self.algo_instances.parent = self
            self.enable = None


        class AlgoInstances(object):
            """
            A set of MAP\-E or MAP\-T instances to be configured,
            applying to BRs and CEs. A MAP\-E/T instance defines a MAP
            domain comprising one or more MAP\-CE and MAP\-BR
            
            .. attribute:: algo_instance
            
            	instance for MAP\-E/MAP\-T
            	**type**\: list of    :py:class:`AlgoInstance <ydk.models.ietf.ietf_softwire.SoftwireConfig.Algorithm.AlgoInstances.AlgoInstance>`
            
            

            """

            _prefix = 'softwire'
            _revision = '2016-06-04'

            def __init__(self):
                self.parent = None
                self.algo_instance = YList()
                self.algo_instance.parent = self
                self.algo_instance.name = 'algo_instance'


            class AlgoInstance(object):
                """
                instance for MAP\-E/MAP\-T
                
                .. attribute:: id  <key>
                
                	Algorithm Instance ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**mandatory**\: True
                
                .. attribute:: algo_versioning
                
                	algorithm's version
                	**type**\:   :py:class:`AlgoVersioning <ydk.models.ietf.ietf_softwire.SoftwireConfig.Algorithm.AlgoInstances.AlgoInstance.AlgoVersioning>`
                
                .. attribute:: br_ipv6_addr
                
                	The IPv6 address of the MAP\-E BR
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                .. attribute:: data_plane
                
                	Encapsulation is for MAP\-E while translation is for MAP\-T
                	**type**\:   :py:class:`DataPlaneEnum <ydk.models.ietf.ietf_softwire.SoftwireConfig.Algorithm.AlgoInstances.AlgoInstance.DataPlaneEnum>`
                
                .. attribute:: dmr_ipv6_prefix
                
                	The IPv6 prefix of the MAP\-T BR. 
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                .. attribute:: ea_len
                
                	Embedded Address (EA) bits are the IPv4 EA\-bits in the IPv6 address identify an IPv4 prefix/address (or part thereof) or a shared IPv4 address (or part thereof) and a port\-set identifier. The length of the EA\-bits is defined as part of a MAP rule for a MAP domain
                	**type**\:  int
                
                	**range:** 0..255
                
                	**mandatory**\: True
                
                .. attribute:: forwarding
                
                	This parameter specifies whether the rule may be used for forwarding (FMR). If set, this rule is used as an FMR; if not set, this rule is a BMR only and must not be used for forwarding
                	**type**\:  bool
                
                	**mandatory**\: True
                
                .. attribute:: name
                
                	The name for the instance
                	**type**\:  str
                
                .. attribute:: psid_len
                
                	The length of PSID, representing the sharing ratio for an IPv4 address
                	**type**\:  int
                
                	**range:** 0..15
                
                	**mandatory**\: True
                
                .. attribute:: psid_offset
                
                	The number of offset bits. In Lightweight 4over6, the default value is 0 for assigning one contiguous port range. In MAP\-E/T, the default value is 6, which excludes system ports by default and assigns distributed port ranges. If the this parameter is larger than 0, the value of offset MUST be greater than 0
                	**type**\:  int
                
                	**range:** 0..16
                
                	**mandatory**\: True
                
                .. attribute:: rule_ipv4_prefix
                
                	The Rule IPv4 prefix defined in the mapping rule
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                	**mandatory**\: True
                
                .. attribute:: rule_ipv6_prefix
                
                	The Rule IPv6 prefix defined in the mapping rule
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                	**mandatory**\: True
                
                .. attribute:: tunnel_path_mru
                
                	The path MRU for MAP\-E tunnel
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: tunnel_payload_mtu
                
                	The payload MTU for MAP\-E tunnel
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'softwire'
                _revision = '2016-06-04'

                def __init__(self):
                    self.parent = None
                    self.id = None
                    self.algo_versioning = SoftwireConfig.Algorithm.AlgoInstances.AlgoInstance.AlgoVersioning()
                    self.algo_versioning.parent = self
                    self.br_ipv6_addr = None
                    self.data_plane = None
                    self.dmr_ipv6_prefix = None
                    self.ea_len = None
                    self.forwarding = None
                    self.name = None
                    self.psid_len = None
                    self.psid_offset = None
                    self.rule_ipv4_prefix = None
                    self.rule_ipv6_prefix = None
                    self.tunnel_path_mru = None
                    self.tunnel_payload_mtu = None

                class DataPlaneEnum(Enum):
                    """
                    DataPlaneEnum

                    Encapsulation is for MAP\-E while translation is

                    for MAP\-T

                    .. data:: encapsulation = 0

                    	encapsulation for MAP-E

                    .. data:: translation = 1

                    	translation for MAP-T

                    """

                    encapsulation = 0

                    translation = 1


                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_softwire as meta
                        return meta._meta_table['SoftwireConfig.Algorithm.AlgoInstances.AlgoInstance.DataPlaneEnum']



                class AlgoVersioning(object):
                    """
                    algorithm's version
                    
                    .. attribute:: algo_date
                    
                    	Timestamp to the algorithm
                    	**type**\:  str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: algo_version
                    
                    	Incremental version number to the algorithm
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'softwire'
                    _revision = '2016-06-04'

                    def __init__(self):
                        self.parent = None
                        self.algo_date = None
                        self.algo_version = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-softwire:algo-versioning'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.algo_date is not None:
                            return True

                        if self.algo_version is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_softwire as meta
                        return meta._meta_table['SoftwireConfig.Algorithm.AlgoInstances.AlgoInstance.AlgoVersioning']['meta_info']

                @property
                def _common_path(self):
                    if self.id is None:
                        raise YPYModelError('Key property id is None')

                    return '/ietf-softwire:softwire-config/ietf-softwire:algorithm/ietf-softwire:algo-instances/ietf-softwire:algo-instance[ietf-softwire:id = ' + str(self.id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.id is not None:
                        return True

                    if self.algo_versioning is not None and self.algo_versioning._has_data():
                        return True

                    if self.br_ipv6_addr is not None:
                        return True

                    if self.data_plane is not None:
                        return True

                    if self.dmr_ipv6_prefix is not None:
                        return True

                    if self.ea_len is not None:
                        return True

                    if self.forwarding is not None:
                        return True

                    if self.name is not None:
                        return True

                    if self.psid_len is not None:
                        return True

                    if self.psid_offset is not None:
                        return True

                    if self.rule_ipv4_prefix is not None:
                        return True

                    if self.rule_ipv6_prefix is not None:
                        return True

                    if self.tunnel_path_mru is not None:
                        return True

                    if self.tunnel_payload_mtu is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_softwire as meta
                    return meta._meta_table['SoftwireConfig.Algorithm.AlgoInstances.AlgoInstance']['meta_info']

            @property
            def _common_path(self):

                return '/ietf-softwire:softwire-config/ietf-softwire:algorithm/ietf-softwire:algo-instances'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.algo_instance is not None:
                    for child_ref in self.algo_instance:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_softwire as meta
                return meta._meta_table['SoftwireConfig.Algorithm.AlgoInstances']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-softwire:softwire-config/ietf-softwire:algorithm'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.algo_instances is not None and self.algo_instances._has_data():
                return True

            if self.enable is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_softwire as meta
            return meta._meta_table['SoftwireConfig.Algorithm']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-softwire:softwire-config'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.algorithm is not None and self.algorithm._has_data():
            return True

        if self.binding is not None and self.binding._has_data():
            return True

        if self.description is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_softwire as meta
        return meta._meta_table['SoftwireConfig']['meta_info']


class SoftwireState(object):
    """
    The operational state data for Softwire instances. 
    
    .. attribute:: algorithm
    
    	Indicate the instances support the MAP\-E and MAP\-T function. The instances advertise the map\-e/map\-t feature through the capability exchange mechanism when a NETCONF session is established
    	**type**\:   :py:class:`Algorithm <ydk.models.ietf.ietf_softwire.SoftwireState.Algorithm>`
    
    .. attribute:: binding
    
    	lw4over6 (binding) state
    	**type**\:   :py:class:`Binding <ydk.models.ietf.ietf_softwire.SoftwireState.Binding>`
    
    .. attribute:: description
    
    	A textual description of the softwire instances
    	**type**\:  str
    
    

    """

    _prefix = 'softwire'
    _revision = '2016-06-04'

    def __init__(self):
        self.algorithm = SoftwireState.Algorithm()
        self.algorithm.parent = self
        self.binding = SoftwireState.Binding()
        self.binding.parent = self
        self.description = None


    class Binding(object):
        """
        lw4over6 (binding) state.
        
        .. attribute:: br
        
        	Indicate this instance supports the lwAFTR (BR) function. The instances advertise the lwaftr (BR) feature through the capability exchange mechanism when a NETCONF session is established
        	**type**\:   :py:class:`Br <ydk.models.ietf.ietf_softwire.SoftwireState.Binding.Br>`
        
        .. attribute:: ce
        
        	Indicate this instance supports the lwB4 (CE) function. The instances advertise the lwb4 (CE) feature through the capability exchange mechanism when a NETCONF session is established
        	**type**\:   :py:class:`Ce <ydk.models.ietf.ietf_softwire.SoftwireState.Binding.Ce>`
        
        

        """

        _prefix = 'softwire'
        _revision = '2016-06-04'

        def __init__(self):
            self.parent = None
            self.br = SoftwireState.Binding.Br()
            self.br.parent = self
            self.ce = SoftwireState.Binding.Ce()
            self.ce.parent = self


        class Br(object):
            """
            Indicate this instance supports the lwAFTR (BR) function.
            The instances advertise the lwaftr (BR) feature through the
            capability exchange mechanism when a NETCONF session is
            established.
            
            .. attribute:: br_instances
            
            	A set of BRs
            	**type**\:   :py:class:`BrInstances <ydk.models.ietf.ietf_softwire.SoftwireState.Binding.Br.BrInstances>`
            
            

            """

            _prefix = 'softwire'
            _revision = '2016-06-04'

            def __init__(self):
                self.parent = None
                self.br_instances = SoftwireState.Binding.Br.BrInstances()
                self.br_instances.parent = self


            class BrInstances(object):
                """
                A set of BRs.
                
                .. attribute:: br_instance
                
                	instances for BR
                	**type**\: list of    :py:class:`BrInstance <ydk.models.ietf.ietf_softwire.SoftwireState.Binding.Br.BrInstances.BrInstance>`
                
                

                """

                _prefix = 'softwire'
                _revision = '2016-06-04'

                def __init__(self):
                    self.parent = None
                    self.br_instance = YList()
                    self.br_instance.parent = self
                    self.br_instance.name = 'br_instance'


                class BrInstance(object):
                    """
                    instances for BR
                    
                    .. attribute:: id  <key>
                    
                    	id
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    .. attribute:: active_softwire_num
                    
                    	The number of currently active tunnels on the lw4over6 (binding) instance
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: binding_table
                    
                    	id
                    	**type**\:   :py:class:`BindingTable <ydk.models.ietf.ietf_softwire.SoftwireState.Binding.Br.BrInstances.BrInstance.BindingTable>`
                    
                    .. attribute:: droppedbyte
                    
                    	Traffic dropped, in bytes
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: droppedpacket
                    
                    	Number of packets dropped
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: name
                    
                    	The name for this lwaftr
                    	**type**\:  str
                    
                    .. attribute:: rcvdbyte
                    
                    	Traffic received, in bytes
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: rcvdpacket
                    
                    	Number of packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sentbyte
                    
                    	Traffic sent, in bytes
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sentpacket
                    
                    	Number of packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'softwire'
                    _revision = '2016-06-04'

                    def __init__(self):
                        self.parent = None
                        self.id = None
                        self.active_softwire_num = None
                        self.binding_table = SoftwireState.Binding.Br.BrInstances.BrInstance.BindingTable()
                        self.binding_table.parent = self
                        self.droppedbyte = None
                        self.droppedpacket = None
                        self.name = None
                        self.rcvdbyte = None
                        self.rcvdpacket = None
                        self.sentbyte = None
                        self.sentpacket = None


                    class BindingTable(object):
                        """
                        id
                        
                        .. attribute:: binding_entry
                        
                        	An identifier of the binding entry
                        	**type**\: list of    :py:class:`BindingEntry <ydk.models.ietf.ietf_softwire.SoftwireState.Binding.Br.BrInstances.BrInstance.BindingTable.BindingEntry>`
                        
                        

                        """

                        _prefix = 'softwire'
                        _revision = '2016-06-04'

                        def __init__(self):
                            self.parent = None
                            self.binding_entry = YList()
                            self.binding_entry.parent = self
                            self.binding_entry.name = 'binding_entry'


                        class BindingEntry(object):
                            """
                            An identifier of the binding entry.
                            
                            .. attribute:: binding_ipv6info  <key>
                            
                            	The IPv6 information used to identify  a binding entry. 
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**mandatory**\: True
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                            
                            	**mandatory**\: True
                            
                            
                            ----
                            .. attribute:: active
                            
                            	Status of a specific tunnel
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'softwire'
                            _revision = '2016-06-04'

                            def __init__(self):
                                self.parent = None
                                self.binding_ipv6info = None
                                self.active = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.binding_ipv6info is None:
                                    raise YPYModelError('Key property binding_ipv6info is None')

                                return self.parent._common_path +'/ietf-softwire:binding-entry[ietf-softwire:binding-ipv6info = ' + str(self.binding_ipv6info) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.binding_ipv6info is not None:
                                    return True

                                if self.active is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_softwire as meta
                                return meta._meta_table['SoftwireState.Binding.Br.BrInstances.BrInstance.BindingTable.BindingEntry']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-softwire:binding-table'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.binding_entry is not None:
                                for child_ref in self.binding_entry:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_softwire as meta
                            return meta._meta_table['SoftwireState.Binding.Br.BrInstances.BrInstance.BindingTable']['meta_info']

                    @property
                    def _common_path(self):
                        if self.id is None:
                            raise YPYModelError('Key property id is None')

                        return '/ietf-softwire:softwire-state/ietf-softwire:binding/ietf-softwire:br/ietf-softwire:br-instances/ietf-softwire:br-instance[ietf-softwire:id = ' + str(self.id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.id is not None:
                            return True

                        if self.active_softwire_num is not None:
                            return True

                        if self.binding_table is not None and self.binding_table._has_data():
                            return True

                        if self.droppedbyte is not None:
                            return True

                        if self.droppedpacket is not None:
                            return True

                        if self.name is not None:
                            return True

                        if self.rcvdbyte is not None:
                            return True

                        if self.rcvdpacket is not None:
                            return True

                        if self.sentbyte is not None:
                            return True

                        if self.sentpacket is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_softwire as meta
                        return meta._meta_table['SoftwireState.Binding.Br.BrInstances.BrInstance']['meta_info']

                @property
                def _common_path(self):

                    return '/ietf-softwire:softwire-state/ietf-softwire:binding/ietf-softwire:br/ietf-softwire:br-instances'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.br_instance is not None:
                        for child_ref in self.br_instance:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_softwire as meta
                    return meta._meta_table['SoftwireState.Binding.Br.BrInstances']['meta_info']

            @property
            def _common_path(self):

                return '/ietf-softwire:softwire-state/ietf-softwire:binding/ietf-softwire:br'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.br_instances is not None and self.br_instances._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_softwire as meta
                return meta._meta_table['SoftwireState.Binding.Br']['meta_info']


        class Ce(object):
            """
            Indicate this instance supports the lwB4 (CE) function.
            The instances advertise the lwb4 (CE) feature through the
            capability exchange mechanism when a NETCONF session is
            established.
            
            .. attribute:: ce_instances
            
            	Status of the configured CEs
            	**type**\:   :py:class:`CeInstances <ydk.models.ietf.ietf_softwire.SoftwireState.Binding.Ce.CeInstances>`
            
            

            """

            _prefix = 'softwire'
            _revision = '2016-06-04'

            def __init__(self):
                self.parent = None
                self.ce_instances = SoftwireState.Binding.Ce.CeInstances()
                self.ce_instances.parent = self


            class CeInstances(object):
                """
                Status of the configured CEs.
                
                .. attribute:: ce_instance
                
                	a lwB4 (CE) instance
                	**type**\: list of    :py:class:`CeInstance <ydk.models.ietf.ietf_softwire.SoftwireState.Binding.Ce.CeInstances.CeInstance>`
                
                

                """

                _prefix = 'softwire'
                _revision = '2016-06-04'

                def __init__(self):
                    self.parent = None
                    self.ce_instance = YList()
                    self.ce_instance.parent = self
                    self.ce_instance.name = 'ce_instance'


                class CeInstance(object):
                    """
                    a lwB4 (CE) instance.
                    
                    .. attribute:: binding_ipv6info  <key>
                    
                    	The IPv6 information used to identify a binding entry. 
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**mandatory**\: True
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                    
                    	**mandatory**\: True
                    
                    
                    ----
                    .. attribute:: droppedbyte
                    
                    	Traffic dropped, in bytes
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: droppedpacket
                    
                    	Number of packets dropped
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: name
                    
                    	The CE's name
                    	**type**\:  str
                    
                    .. attribute:: rcvdbyte
                    
                    	Traffic received, in bytes
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: rcvdpacket
                    
                    	Number of packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sentbyte
                    
                    	Traffic sent, in bytes
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sentpacket
                    
                    	Number of packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'softwire'
                    _revision = '2016-06-04'

                    def __init__(self):
                        self.parent = None
                        self.binding_ipv6info = None
                        self.droppedbyte = None
                        self.droppedpacket = None
                        self.name = None
                        self.rcvdbyte = None
                        self.rcvdpacket = None
                        self.sentbyte = None
                        self.sentpacket = None

                    @property
                    def _common_path(self):
                        if self.binding_ipv6info is None:
                            raise YPYModelError('Key property binding_ipv6info is None')

                        return '/ietf-softwire:softwire-state/ietf-softwire:binding/ietf-softwire:ce/ietf-softwire:ce-instances/ietf-softwire:ce-instance[ietf-softwire:binding-ipv6info = ' + str(self.binding_ipv6info) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.binding_ipv6info is not None:
                            return True

                        if self.droppedbyte is not None:
                            return True

                        if self.droppedpacket is not None:
                            return True

                        if self.name is not None:
                            return True

                        if self.rcvdbyte is not None:
                            return True

                        if self.rcvdpacket is not None:
                            return True

                        if self.sentbyte is not None:
                            return True

                        if self.sentpacket is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_softwire as meta
                        return meta._meta_table['SoftwireState.Binding.Ce.CeInstances.CeInstance']['meta_info']

                @property
                def _common_path(self):

                    return '/ietf-softwire:softwire-state/ietf-softwire:binding/ietf-softwire:ce/ietf-softwire:ce-instances'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.ce_instance is not None:
                        for child_ref in self.ce_instance:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_softwire as meta
                    return meta._meta_table['SoftwireState.Binding.Ce.CeInstances']['meta_info']

            @property
            def _common_path(self):

                return '/ietf-softwire:softwire-state/ietf-softwire:binding/ietf-softwire:ce'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.ce_instances is not None and self.ce_instances._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_softwire as meta
                return meta._meta_table['SoftwireState.Binding.Ce']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-softwire:softwire-state/ietf-softwire:binding'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.br is not None and self.br._has_data():
                return True

            if self.ce is not None and self.ce._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_softwire as meta
            return meta._meta_table['SoftwireState.Binding']['meta_info']


    class Algorithm(object):
        """
        Indicate the instances support the MAP\-E and MAP\-T function.
        The instances advertise the map\-e/map\-t feature through the
        capability exchange mechanism when a NETCONF session is
        established.
        
        .. attribute:: algo_instances
        
        	Status of MAP\-E instance(s)
        	**type**\:   :py:class:`AlgoInstances <ydk.models.ietf.ietf_softwire.SoftwireState.Algorithm.AlgoInstances>`
        
        

        """

        _prefix = 'softwire'
        _revision = '2016-06-04'

        def __init__(self):
            self.parent = None
            self.algo_instances = SoftwireState.Algorithm.AlgoInstances()
            self.algo_instances.parent = self


        class AlgoInstances(object):
            """
            Status of MAP\-E instance(s).
            
            .. attribute:: algo_instance
            
            	Instances for algorithm
            	**type**\: list of    :py:class:`AlgoInstance <ydk.models.ietf.ietf_softwire.SoftwireState.Algorithm.AlgoInstances.AlgoInstance>`
            
            

            """

            _prefix = 'softwire'
            _revision = '2016-06-04'

            def __init__(self):
                self.parent = None
                self.algo_instance = YList()
                self.algo_instance.parent = self
                self.algo_instance.name = 'algo_instance'


            class AlgoInstance(object):
                """
                Instances for algorithm
                
                .. attribute:: id  <key>
                
                	id
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**mandatory**\: True
                
                .. attribute:: droppedbyte
                
                	Traffic dropped, in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: droppedpacket
                
                	Number of packets dropped
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: name
                
                	The map\-e instance name
                	**type**\:  str
                
                .. attribute:: rcvdbyte
                
                	Traffic received, in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rcvdpacket
                
                	Number of packets received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sentbyte
                
                	Traffic sent, in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sentpacket
                
                	Number of packets sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'softwire'
                _revision = '2016-06-04'

                def __init__(self):
                    self.parent = None
                    self.id = None
                    self.droppedbyte = None
                    self.droppedpacket = None
                    self.name = None
                    self.rcvdbyte = None
                    self.rcvdpacket = None
                    self.sentbyte = None
                    self.sentpacket = None

                @property
                def _common_path(self):
                    if self.id is None:
                        raise YPYModelError('Key property id is None')

                    return '/ietf-softwire:softwire-state/ietf-softwire:algorithm/ietf-softwire:algo-instances/ietf-softwire:algo-instance[ietf-softwire:id = ' + str(self.id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.id is not None:
                        return True

                    if self.droppedbyte is not None:
                        return True

                    if self.droppedpacket is not None:
                        return True

                    if self.name is not None:
                        return True

                    if self.rcvdbyte is not None:
                        return True

                    if self.rcvdpacket is not None:
                        return True

                    if self.sentbyte is not None:
                        return True

                    if self.sentpacket is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_softwire as meta
                    return meta._meta_table['SoftwireState.Algorithm.AlgoInstances.AlgoInstance']['meta_info']

            @property
            def _common_path(self):

                return '/ietf-softwire:softwire-state/ietf-softwire:algorithm/ietf-softwire:algo-instances'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.algo_instance is not None:
                    for child_ref in self.algo_instance:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_softwire as meta
                return meta._meta_table['SoftwireState.Algorithm.AlgoInstances']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-softwire:softwire-state/ietf-softwire:algorithm'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.algo_instances is not None and self.algo_instances._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_softwire as meta
            return meta._meta_table['SoftwireState.Algorithm']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-softwire:softwire-state'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.algorithm is not None and self.algorithm._has_data():
            return True

        if self.binding is not None and self.binding._has_data():
            return True

        if self.description is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_softwire as meta
        return meta._meta_table['SoftwireState']['meta_info']



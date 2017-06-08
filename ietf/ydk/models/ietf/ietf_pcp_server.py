""" ietf_pcp_server 

This module contains a collection of YANG definitions for
 PCP server implementations.

 Copyright (c) 2016 IETF Trust and the persons identified as
 authors of the code.  All rights reserved.

 Redistribution and use in source and binary forms, with or
 without modification, is permitted pursuant to, and subject
 to the license terms contained in, the Simplified BSD License
 set forth in Section 4.c of the IETF Trust's Legal Provisions
 Relating to IETF Documents
 (http\://trustee.ietf.org/license\-info).

 This version of this YANG module is part of RFC XXXX; see
 the RFC itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class PcpServerConfig(object):
    """
    PCP server
    
    .. attribute:: enable
    
    	Enable/Disable PCP server function
    	**type**\:  bool
    
    .. attribute:: pcp_server_instances
    
    	PCP server instances
    	**type**\:   :py:class:`PcpServerInstances <ydk.models.ietf.ietf_pcp_server.PcpServerConfig.PcpServerInstances>`
    
    

    """

    _prefix = 'pcp-server'
    _revision = '2015-08-05'

    def __init__(self):
        self.enable = None
        self.pcp_server_instances = PcpServerConfig.PcpServerInstances()
        self.pcp_server_instances.parent = self


    class PcpServerInstances(object):
        """
        PCP server instances
        
        .. attribute:: pcp_server_instance
        
        	a PCP server instance
        	**type**\: list of    :py:class:`PcpServerInstance <ydk.models.ietf.ietf_pcp_server.PcpServerConfig.PcpServerInstances.PcpServerInstance>`
        
        

        """

        _prefix = 'pcp-server'
        _revision = '2015-08-05'

        def __init__(self):
            self.parent = None
            self.pcp_server_instance = YList()
            self.pcp_server_instance.parent = self
            self.pcp_server_instance.name = 'pcp_server_instance'


        class PcpServerInstance(object):
            """
            a PCP server instance.
            
            .. attribute:: id  <key>
            
            	PCP server instance identifier
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authentication_enable
            
            	Enable/disable PCP authentication
            	**type**\:  bool
            
            .. attribute:: epoch_set
            
            	Set the Epoch parameter
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: error_lifetime
            
            	Configure values for the error lifetime to be returned to requesting PCP clients
            	**type**\:   :py:class:`ErrorLifetime <ydk.models.ietf.ietf_pcp_server.PcpServerConfig.PcpServerInstances.PcpServerInstance.ErrorLifetime>`
            
            .. attribute:: exclude_ports
            
            	The set of ports not to be assigned  by the server
            	**type**\: list of    :py:class:`ExcludePorts <ydk.models.ietf.ietf_pcp_server.PcpServerConfig.PcpServerInstances.PcpServerInstance.ExcludePorts>`
            
            .. attribute:: lifetime
            
            	Configure values for the lifetime to be assigned to requesting PCP clients.  The client requests a certain lifetime, and the server responds with the assigned lifetime.  The server may grant a lifetime smaller or larger than the requested lifetime.  The minimum value should be 120 seconds.  The maximum value should be the remaining lifetime of the IP address assigned to the PCP client if that information is available, or half the lifetime of IP address assignments, or 24 hours.  Excessively long lifetimes can cause consumption of ports even if the internal host is no longer interested in receiving the traffic or is no longer connected to the network. (Section 15 [RFC6877]
            	**type**\:   :py:class:`Lifetime <ydk.models.ietf.ietf_pcp_server.PcpServerConfig.PcpServerInstances.PcpServerInstance.Lifetime>`
            
            .. attribute:: mapping_table
            
            	PCP mapping table as maintained by  the PCP server
            	**type**\:   :py:class:`MappingTable <ydk.models.ietf.ietf_pcp_server.PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable>`
            
            .. attribute:: name
            
            	A name associated with the PCP server instance
            	**type**\:  str
            
            .. attribute:: nonce_validation_checks_enable
            
            	Indicates whether the PCP server has to  disable/enable Nonce validation checks
            	**type**\:  bool
            
            .. attribute:: opcode_configuration
            
            	Opcode\-related configuration
            	**type**\:   :py:class:`OpcodeConfiguration <ydk.models.ietf.ietf_pcp_server.PcpServerConfig.PcpServerInstances.PcpServerInstance.OpcodeConfiguration>`
            
            .. attribute:: option_configuration
            
            	Option\-related configuration
            	**type**\:   :py:class:`OptionConfiguration <ydk.models.ietf.ietf_pcp_server.PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration>`
            
            .. attribute:: pcp_server_ip_address
            
            	set one or multiple IP addresses for the PCP server
            	**type**\: list of    :py:class:`PcpServerIpAddress <ydk.models.ietf.ietf_pcp_server.PcpServerConfig.PcpServerInstances.PcpServerInstance.PcpServerIpAddress>`
            
            .. attribute:: port_parity_preservation_enable
            
            	Indicates whether the PCP server should  preserve the port parity of the  internal port number
            	**type**\:  bool
            
            .. attribute:: port_preservation_enable
            
            	Indicates whether the PCP server should  preserve the internal port number
            	**type**\:  bool
            
            .. attribute:: port_quota
            
            	configure a port quota to be assigned per  PCP client/subscriber
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: port_randomization_enable
            
            	Enable/disable port randomization  feature
            	**type**\:  bool
            
            .. attribute:: protocol
            
            	set of protocols supported by  the PCP\-controlled function
            	**type**\: list of    :py:class:`Protocol <ydk.models.ietf.ietf_pcp_server.PcpServerConfig.PcpServerInstances.PcpServerInstance.Protocol>`
            
            .. attribute:: subscriber_mask
            
            	The subscriber\-mask is an integer that indicates the length of significant bits to be applied on the source IPv6 address (internal side) to identify unambiguously a CPE.  Subscriber\-mask is a system\-wide configuration parameter that is used to enforce generic per\-subscriber policies (e.g., port\-quota).  Applying these generic policies does not require configuring every subscriber's prefix.  Example\: suppose the 2001\:db8\:100\:100\:\:/56 prefix is assigned to a DS\-Lite enabled CPE. Suppose also that the 2001\:db8\:100\:100\:\:1 is the IPv6 address used by the client that resides in that CPE. When the server receives a packet from this client, the server applies the subscriber\-mask (e.g., 56) on the source IPv6 address to compute the associated prefix for this client (that is 2001\:db8\:100\:100\:\:/56).  Then, the server enforces policies based on that prefix (2001\:db8\:100\:100\:\:/56), not on the exact source IPv6 address
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: version
            
            	Indicates the PCP version(s) supported by the  PCP server.  Current supported versions are 0, 1, and 2
            	**type**\: list of    :py:class:`Version <ydk.models.ietf.ietf_pcp_server.PcpServerConfig.PcpServerInstances.PcpServerInstance.Version>`
            
            

            """

            _prefix = 'pcp-server'
            _revision = '2015-08-05'

            def __init__(self):
                self.parent = None
                self.id = None
                self.authentication_enable = None
                self.epoch_set = None
                self.error_lifetime = PcpServerConfig.PcpServerInstances.PcpServerInstance.ErrorLifetime()
                self.error_lifetime.parent = self
                self.exclude_ports = YList()
                self.exclude_ports.parent = self
                self.exclude_ports.name = 'exclude_ports'
                self.lifetime = PcpServerConfig.PcpServerInstances.PcpServerInstance.Lifetime()
                self.lifetime.parent = self
                self.mapping_table = PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable()
                self.mapping_table.parent = self
                self.name = None
                self.nonce_validation_checks_enable = None
                self.opcode_configuration = PcpServerConfig.PcpServerInstances.PcpServerInstance.OpcodeConfiguration()
                self.opcode_configuration.parent = self
                self.option_configuration = PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration()
                self.option_configuration.parent = self
                self.pcp_server_ip_address = YList()
                self.pcp_server_ip_address.parent = self
                self.pcp_server_ip_address.name = 'pcp_server_ip_address'
                self.port_parity_preservation_enable = None
                self.port_preservation_enable = None
                self.port_quota = None
                self.port_randomization_enable = None
                self.protocol = YList()
                self.protocol.parent = self
                self.protocol.name = 'protocol'
                self.subscriber_mask = None
                self.version = YList()
                self.version.parent = self
                self.version.name = 'version'


            class Version(object):
                """
                Indicates the PCP version(s) supported by the
                 PCP server.
                 Current supported versions are 0, 1, and 2.
                
                .. attribute:: version  <key>
                
                	Indicates a PCP server.  Current versions are\: 0, 1, and 2
                	**type**\:  int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.version = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.version is None:
                        raise YPYModelError('Key property version is None')

                    return self.parent._common_path +'/ietf-pcp-server:version[ietf-pcp-server:version = ' + str(self.version) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.version is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.Version']['meta_info']


            class PcpServerIpAddress(object):
                """
                set one or multiple IP addresses for
                the PCP server
                
                .. attribute:: address_id  <key>
                
                	The identifier of the address
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ip_address
                
                	IP (v4/v6) address of the PCP server
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.address_id = None
                    self.ip_address = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.address_id is None:
                        raise YPYModelError('Key property address_id is None')

                    return self.parent._common_path +'/ietf-pcp-server:pcp-server-ip-address[ietf-pcp-server:address-id = ' + str(self.address_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.address_id is not None:
                        return True

                    if self.ip_address is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.PcpServerIpAddress']['meta_info']


            class OpcodeConfiguration(object):
                """
                Opcode\-related configuration
                
                .. attribute:: announce
                
                	ANNOUNCE opcode
                	**type**\:  bool
                
                .. attribute:: map
                
                	MAP opcode
                	**type**\:  bool
                
                .. attribute:: peer
                
                	PEER opcode
                	**type**\:  bool
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.announce = None
                    self.map = None
                    self.peer = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-pcp-server:opcode-configuration'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.announce is not None:
                        return True

                    if self.map is not None:
                        return True

                    if self.peer is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.OpcodeConfiguration']['meta_info']


            class OptionConfiguration(object):
                """
                Option\-related configuration
                
                .. attribute:: description
                
                	enable/disable DESCRIPTION option
                	**type**\:   :py:class:`Description <ydk.models.ietf.ietf_pcp_server.PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Description>`
                
                .. attribute:: filter
                
                	enable/disable FILTER option
                	**type**\:   :py:class:`Filter <ydk.models.ietf.ietf_pcp_server.PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Filter>`
                
                .. attribute:: port_set_option
                
                	enable/disable PORT\_SET option
                	**type**\:   :py:class:`PortSetOption <ydk.models.ietf.ietf_pcp_server.PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.PortSetOption>`
                
                .. attribute:: prefer_failure
                
                	enable/disable PREFER\_FAILURE option
                	**type**\:  bool
                
                .. attribute:: prefix64_option
                
                	enable/disable PREFIX64 option
                	**type**\:   :py:class:`Prefix64Option <ydk.models.ietf.ietf_pcp_server.PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option>`
                
                .. attribute:: third_party
                
                	enable/disable THIRD\_PARTY option
                	**type**\:  bool
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.description = PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Description()
                    self.description.parent = self
                    self.filter = PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Filter()
                    self.filter.parent = self
                    self.port_set_option = PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.PortSetOption()
                    self.port_set_option.parent = self
                    self.prefer_failure = None
                    self.prefix64_option = PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option()
                    self.prefix64_option.parent = self
                    self.third_party = None


                class Filter(object):
                    """
                    enable/disable FILTER option.
                    
                    .. attribute:: filter_enabled
                    
                    	Enable/disable FILTER option
                    	**type**\:  bool
                    
                    .. attribute:: max_filters
                    
                    	Indicates the maximum number of filters  associated with a mapping
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pcp-server'
                    _revision = '2015-08-05'

                    def __init__(self):
                        self.parent = None
                        self.filter_enabled = None
                        self.max_filters = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-pcp-server:filter'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.filter_enabled is not None:
                            return True

                        if self.max_filters is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_pcp_server as meta
                        return meta._meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Filter']['meta_info']


                class PortSetOption(object):
                    """
                    enable/disable PORT\_SET option.
                    
                    .. attribute:: default_port_set_size
                    
                    	Indicates the default size of a port set
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: maximum_port_set_size
                    
                    	Indicates the maximum size of a port set
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: port_set_enable
                    
                    	Enable/disable PORT\_SET option
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'pcp-server'
                    _revision = '2015-08-05'

                    def __init__(self):
                        self.parent = None
                        self.default_port_set_size = None
                        self.maximum_port_set_size = None
                        self.port_set_enable = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-pcp-server:port-set-option'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.default_port_set_size is not None:
                            return True

                        if self.maximum_port_set_size is not None:
                            return True

                        if self.port_set_enable is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_pcp_server as meta
                        return meta._meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.PortSetOption']['meta_info']


                class Description(object):
                    """
                    enable/disable DESCRIPTION option.
                    
                    .. attribute:: description_enabled
                    
                    	Enable/disable DESCRIPTION option
                    	**type**\:  bool
                    
                    .. attribute:: max_description
                    
                    	Indicates the maximum length of the description  associated with a mapping
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pcp-server'
                    _revision = '2015-08-05'

                    def __init__(self):
                        self.parent = None
                        self.description_enabled = None
                        self.max_description = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-pcp-server:description'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.description_enabled is not None:
                            return True

                        if self.max_description is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_pcp_server as meta
                        return meta._meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Description']['meta_info']


                class Prefix64Option(object):
                    """
                    enable/disable PREFIX64 option.
                    
                    .. attribute:: prefix64
                    
                    	maintains a list of Prefix64s
                    	**type**\: list of    :py:class:`Prefix64 <ydk.models.ietf.ietf_pcp_server.PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64>`
                    
                    .. attribute:: prefix64_option_enable
                    
                    	Indicates whether the option is enabled/disabled
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'pcp-server'
                    _revision = '2015-08-05'

                    def __init__(self):
                        self.parent = None
                        self.prefix64 = YList()
                        self.prefix64.parent = self
                        self.prefix64.name = 'prefix64'
                        self.prefix64_option_enable = None


                    class Prefix64(object):
                        """
                        maintains a list of Prefix64s.
                        
                        .. attribute:: prefix64_id  <key>
                        
                        	An identifier of a Prefix64
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dest_ipv4_prefix
                        
                        	used to solve the destination\-dependent  Pref64\:\:/n discovery problem discussed in  Section 5.1 of [RFC7050]
                        	**type**\: list of    :py:class:`DestIpv4Prefix <ydk.models.ietf.ietf_pcp_server.PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64.DestIpv4Prefix>`
                        
                        .. attribute:: prefix64
                        
                        	A Prefix64
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                        
                        .. attribute:: suffix
                        
                        	The suffix is used for constructing an  IPv4\-converted IPv6 address from an IPv4 address as  specified in Section 2.2 of [RFC6052]. No suffix is  included if a /96 Prefix64 is used
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'pcp-server'
                        _revision = '2015-08-05'

                        def __init__(self):
                            self.parent = None
                            self.prefix64_id = None
                            self.dest_ipv4_prefix = YList()
                            self.dest_ipv4_prefix.parent = self
                            self.dest_ipv4_prefix.name = 'dest_ipv4_prefix'
                            self.prefix64 = None
                            self.suffix = None


                        class DestIpv4Prefix(object):
                            """
                            used to solve the destination\-dependent
                             Pref64\:\:/n discovery problem discussed in
                             Section 5.1 of [RFC7050].
                            
                            .. attribute:: ipv4_prefix_id  <key>
                            
                            	An identifier of a destination IPv4 prefix
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv4_prefix
                            
                            	an IPv4 prefix
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                            
                            

                            """

                            _prefix = 'pcp-server'
                            _revision = '2015-08-05'

                            def __init__(self):
                                self.parent = None
                                self.ipv4_prefix_id = None
                                self.ipv4_prefix = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.ipv4_prefix_id is None:
                                    raise YPYModelError('Key property ipv4_prefix_id is None')

                                return self.parent._common_path +'/ietf-pcp-server:dest-ipv4-prefix[ietf-pcp-server:ipv4-prefix-id = ' + str(self.ipv4_prefix_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ipv4_prefix_id is not None:
                                    return True

                                if self.ipv4_prefix is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_pcp_server as meta
                                return meta._meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64.DestIpv4Prefix']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.prefix64_id is None:
                                raise YPYModelError('Key property prefix64_id is None')

                            return self.parent._common_path +'/ietf-pcp-server:prefix64[ietf-pcp-server:prefix64-id = ' + str(self.prefix64_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix64_id is not None:
                                return True

                            if self.dest_ipv4_prefix is not None:
                                for child_ref in self.dest_ipv4_prefix:
                                    if child_ref._has_data():
                                        return True

                            if self.prefix64 is not None:
                                return True

                            if self.suffix is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_pcp_server as meta
                            return meta._meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-pcp-server:prefix64-option'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.prefix64 is not None:
                            for child_ref in self.prefix64:
                                if child_ref._has_data():
                                    return True

                        if self.prefix64_option_enable is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_pcp_server as meta
                        return meta._meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-pcp-server:option-configuration'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.description is not None and self.description._has_data():
                        return True

                    if self.filter is not None and self.filter._has_data():
                        return True

                    if self.port_set_option is not None and self.port_set_option._has_data():
                        return True

                    if self.prefer_failure is not None:
                        return True

                    if self.prefix64_option is not None and self.prefix64_option._has_data():
                        return True

                    if self.third_party is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.OptionConfiguration']['meta_info']


            class ExcludePorts(object):
                """
                The set of ports not to be assigned
                 by the server.
                
                .. attribute:: id  <key>
                
                	An identifier
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: end_port_number
                
                	End of the port range
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: single_port_number
                
                	used for single port numbers
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: start_port_number
                
                	Begining of the port range
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.id = None
                    self.end_port_number = None
                    self.single_port_number = None
                    self.start_port_number = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.id is None:
                        raise YPYModelError('Key property id is None')

                    return self.parent._common_path +'/ietf-pcp-server:exclude-ports[ietf-pcp-server:id = ' + str(self.id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.id is not None:
                        return True

                    if self.end_port_number is not None:
                        return True

                    if self.single_port_number is not None:
                        return True

                    if self.start_port_number is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.ExcludePorts']['meta_info']


            class Protocol(object):
                """
                set of protocols supported by
                 the PCP\-controlled function.
                
                .. attribute:: protocol_id  <key>
                
                	identifier of the protocol
                	**type**\:  int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.protocol_id = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.protocol_id is None:
                        raise YPYModelError('Key property protocol_id is None')

                    return self.parent._common_path +'/ietf-pcp-server:protocol[ietf-pcp-server:protocol-id = ' + str(self.protocol_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.protocol_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.Protocol']['meta_info']


            class Lifetime(object):
                """
                Configure values for the lifetime to be
                assigned to requesting PCP clients.
                
                The client requests a certain lifetime, and the server
                responds with the assigned lifetime.
                
                The server may grant a lifetime smaller or larger than
                the requested lifetime.
                
                The minimum value should be 120 seconds.
                
                The maximum value should be the remaining
                lifetime of the IP address assigned to
                the PCP client if that information is available,
                or half the lifetime of IP address
                assignments, or 24 hours.
                
                Excessively long lifetimes can cause consumption
                of ports even if the internal host is no longer
                interested in receiving the traffic or is no
                longer connected to the network.
                (Section 15 [RFC6877].
                
                .. attribute:: maximum_lifetime
                
                	Maximum lifetime
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**default value**\: 86400
                
                .. attribute:: minimum_lifetime
                
                	Minimum lifetime
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**default value**\: 120
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.maximum_lifetime = None
                    self.minimum_lifetime = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-pcp-server:lifetime'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.maximum_lifetime is not None:
                        return True

                    if self.minimum_lifetime is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.Lifetime']['meta_info']


            class ErrorLifetime(object):
                """
                Configure values for the error lifetime to be
                returned to requesting PCP clients.
                
                .. attribute:: maximum_error_lifetime
                
                	Maximum error lifetime, in seconds.  [RFC6877] recommends that long lifetime errors use a 30\-minute lifetime
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**default value**\: 1800
                
                .. attribute:: minimum_error_lifetime
                
                	Minimum error lifetime, in seconds.  [RFC6877] recommends that short lifetime errors use a 30\-second lifetime
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**default value**\: 30
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.maximum_error_lifetime = None
                    self.minimum_error_lifetime = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-pcp-server:error-lifetime'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.maximum_error_lifetime is not None:
                        return True

                    if self.minimum_error_lifetime is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.ErrorLifetime']['meta_info']


            class MappingTable(object):
                """
                PCP mapping table as maintained by
                 the PCP server
                
                .. attribute:: mapping_entry
                
                	PCP mapping entry
                	**type**\: list of    :py:class:`MappingEntry <ydk.models.ietf.ietf_pcp_server.PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry>`
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.mapping_entry = YList()
                    self.mapping_entry.parent = self
                    self.mapping_entry.name = 'mapping_entry'


                class MappingEntry(object):
                    """
                    PCP mapping entry
                    
                    .. attribute:: index  <key>
                    
                    	A unique identifier of a mapping entry
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: description
                    
                    	a description string associated with the mapping
                    	**type**\:  str
                    
                    .. attribute:: external_ip_address
                    
                    	External IP address. Can be 'Suggested' or 'Assigned'.  It can be set by a client to stale\-ip\-address, if available or to (\:\:) (for requesting external IPv6 addresses) or (\:\:ffff\:0\:0) (for requesting external IPv4 addresses)
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                    
                    .. attribute:: external_port
                    
                    	External port number. Can be 'Suggested' or 'Assigned'
                    	**type**\:   :py:class:`ExternalPort <ydk.models.ietf.ietf_pcp_server.PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.ExternalPort>`
                    
                    .. attribute:: filter
                    
                    	a list of filters associated with the mapping
                    	**type**\: list of    :py:class:`Filter <ydk.models.ietf.ietf_pcp_server.PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.Filter>`
                    
                    .. attribute:: internal_ip_address
                    
                    	Corresponds to the PCP Client's IP Address defined in [RFC6887]
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                    
                    .. attribute:: internal_port
                    
                    	Internal port for the mapping. Value 0 indicates 'all ports', and is legal when the lifetime is zero (a delete request), if the protocol does not use 16\-bit port numbers, or the client is requesting 'all ports'.  If the protocol is zero (meaning 'all protocols'), then internal port is set to zero
                    	**type**\:   :py:class:`InternalPort <ydk.models.ietf.ietf_pcp_server.PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.InternalPort>`
                    
                    .. attribute:: lifetime
                    
                    	Lifetime of the mapping.  Can be requested/assigned/remaining
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mapping_nonce
                    
                    	A random value chosen by the PCP client
                    	**type**\:  str
                    
                    .. attribute:: prefer_failure_tagged
                    
                    	a tag which indicates whether PREFER\_FAILURE  is (to be) used
                    	**type**\:  bool
                    
                    .. attribute:: protocol
                    
                    	Upper\-layer protocol associated with this Opcode. Values are taken from the IANA protocol registry. For example, this field contains 6 (TCP) if the Opcode is intended to create a TCP mapping.  This field contains 17 (UDP) if the Opcode is intended to create a UDP mapping. The value 0 has a special meaning for 'all protocols'
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: status
                    
                    	Indicates the status of a mapping entry
                    	**type**\:   :py:class:`StatusEnum <ydk.models.ietf.ietf_pcp_server.PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.StatusEnum>`
                    
                    .. attribute:: third_party_address
                    
                    	used to indicate the internal IP address  when THIRD\_PARTY is in use
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                    
                    

                    """

                    _prefix = 'pcp-server'
                    _revision = '2015-08-05'

                    def __init__(self):
                        self.parent = None
                        self.index = None
                        self.description = None
                        self.external_ip_address = None
                        self.external_port = PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.ExternalPort()
                        self.external_port.parent = self
                        self.filter = YList()
                        self.filter.parent = self
                        self.filter.name = 'filter'
                        self.internal_ip_address = None
                        self.internal_port = PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.InternalPort()
                        self.internal_port.parent = self
                        self.lifetime = None
                        self.mapping_nonce = None
                        self.prefer_failure_tagged = None
                        self.protocol = None
                        self.status = None
                        self.third_party_address = None

                    class StatusEnum(Enum):
                        """
                        StatusEnum

                        Indicates the status of a mapping entry.

                        .. data:: disabled = 0

                        	The mapping entry is not in use (Disabled).

                        .. data:: requested = 1

                        	A PCP request has been sent for this mapping.

                        	Still waiting for a response from the server.

                        .. data:: assigned = 2

                        	This mapping has been granted by the server.

                        .. data:: stale = 3

                        	This is a stale mapping (case of reboot).

                        """

                        disabled = 0

                        requested = 1

                        assigned = 2

                        stale = 3


                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_pcp_server as meta
                            return meta._meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.StatusEnum']



                    class InternalPort(object):
                        """
                        Internal port for the mapping. Value 0 indicates
                        'all ports', and is legal when the lifetime is zero
                        (a delete request), if the protocol does not use
                        16\-bit port numbers, or the client is requesting
                        'all ports'.  If the protocol is zero
                        (meaning 'all protocols'), then internal port
                        is set to zero.
                        
                        .. attribute:: end_port_number
                        
                        	End of the port range
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: single_port_number
                        
                        	used for single port numbers
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: start_port_number
                        
                        	Begining of the port range
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'pcp-server'
                        _revision = '2015-08-05'

                        def __init__(self):
                            self.parent = None
                            self.end_port_number = None
                            self.single_port_number = None
                            self.start_port_number = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-pcp-server:internal-port'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.end_port_number is not None:
                                return True

                            if self.single_port_number is not None:
                                return True

                            if self.start_port_number is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_pcp_server as meta
                            return meta._meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.InternalPort']['meta_info']


                    class ExternalPort(object):
                        """
                        External port number. Can be 'Suggested' or 'Assigned'.
                        
                        .. attribute:: end_port_number
                        
                        	End of the port range
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: single_port_number
                        
                        	used for single port numbers
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: start_port_number
                        
                        	Begining of the port range
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'pcp-server'
                        _revision = '2015-08-05'

                        def __init__(self):
                            self.parent = None
                            self.end_port_number = None
                            self.single_port_number = None
                            self.start_port_number = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-pcp-server:external-port'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.end_port_number is not None:
                                return True

                            if self.single_port_number is not None:
                                return True

                            if self.start_port_number is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_pcp_server as meta
                            return meta._meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.ExternalPort']['meta_info']


                    class Filter(object):
                        """
                        a list of filters associated with the mapping.
                        
                        .. attribute:: filter_id  <key>
                        
                        	An identifier of the filter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_ip_prefix
                        
                        	The IP address of the remote peer
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                        
                        .. attribute:: remote_port_number
                        
                        	The port number of the remote peer. Value 0 indicates 'all ports'
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'pcp-server'
                        _revision = '2015-08-05'

                        def __init__(self):
                            self.parent = None
                            self.filter_id = None
                            self.remote_ip_prefix = None
                            self.remote_port_number = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.filter_id is None:
                                raise YPYModelError('Key property filter_id is None')

                            return self.parent._common_path +'/ietf-pcp-server:filter[ietf-pcp-server:filter-id = ' + str(self.filter_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.filter_id is not None:
                                return True

                            if self.remote_ip_prefix is not None:
                                return True

                            if self.remote_port_number is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_pcp_server as meta
                            return meta._meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.Filter']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.index is None:
                            raise YPYModelError('Key property index is None')

                        return self.parent._common_path +'/ietf-pcp-server:mapping-entry[ietf-pcp-server:index = ' + str(self.index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.index is not None:
                            return True

                        if self.description is not None:
                            return True

                        if self.external_ip_address is not None:
                            return True

                        if self.external_port is not None and self.external_port._has_data():
                            return True

                        if self.filter is not None:
                            for child_ref in self.filter:
                                if child_ref._has_data():
                                    return True

                        if self.internal_ip_address is not None:
                            return True

                        if self.internal_port is not None and self.internal_port._has_data():
                            return True

                        if self.lifetime is not None:
                            return True

                        if self.mapping_nonce is not None:
                            return True

                        if self.prefer_failure_tagged is not None:
                            return True

                        if self.protocol is not None:
                            return True

                        if self.status is not None:
                            return True

                        if self.third_party_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_pcp_server as meta
                        return meta._meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-pcp-server:mapping-table'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.mapping_entry is not None:
                        for child_ref in self.mapping_entry:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance.MappingTable']['meta_info']

            @property
            def _common_path(self):
                if self.id is None:
                    raise YPYModelError('Key property id is None')

                return '/ietf-pcp-server:pcp-server-config/ietf-pcp-server:pcp-server-instances/ietf-pcp-server:pcp-server-instance[ietf-pcp-server:id = ' + str(self.id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.id is not None:
                    return True

                if self.authentication_enable is not None:
                    return True

                if self.epoch_set is not None:
                    return True

                if self.error_lifetime is not None and self.error_lifetime._has_data():
                    return True

                if self.exclude_ports is not None:
                    for child_ref in self.exclude_ports:
                        if child_ref._has_data():
                            return True

                if self.lifetime is not None and self.lifetime._has_data():
                    return True

                if self.mapping_table is not None and self.mapping_table._has_data():
                    return True

                if self.name is not None:
                    return True

                if self.nonce_validation_checks_enable is not None:
                    return True

                if self.opcode_configuration is not None and self.opcode_configuration._has_data():
                    return True

                if self.option_configuration is not None and self.option_configuration._has_data():
                    return True

                if self.pcp_server_ip_address is not None:
                    for child_ref in self.pcp_server_ip_address:
                        if child_ref._has_data():
                            return True

                if self.port_parity_preservation_enable is not None:
                    return True

                if self.port_preservation_enable is not None:
                    return True

                if self.port_quota is not None:
                    return True

                if self.port_randomization_enable is not None:
                    return True

                if self.protocol is not None:
                    for child_ref in self.protocol:
                        if child_ref._has_data():
                            return True

                if self.subscriber_mask is not None:
                    return True

                if self.version is not None:
                    for child_ref in self.version:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_pcp_server as meta
                return meta._meta_table['PcpServerConfig.PcpServerInstances.PcpServerInstance']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-pcp-server:pcp-server-config/ietf-pcp-server:pcp-server-instances'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.pcp_server_instance is not None:
                for child_ref in self.pcp_server_instance:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_pcp_server as meta
            return meta._meta_table['PcpServerConfig.PcpServerInstances']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-pcp-server:pcp-server-config'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.enable is not None:
            return True

        if self.pcp_server_instances is not None and self.pcp_server_instances._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pcp_server as meta
        return meta._meta_table['PcpServerConfig']['meta_info']


class PcpServerState(object):
    """
    PCP server
    
    .. attribute:: pcp_server_instances
    
    	PCP server instances
    	**type**\:   :py:class:`PcpServerInstances <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances>`
    
    

    """

    _prefix = 'pcp-server'
    _revision = '2015-08-05'

    def __init__(self):
        self.pcp_server_instances = PcpServerState.PcpServerInstances()
        self.pcp_server_instances.parent = self


    class PcpServerInstances(object):
        """
        PCP server instances
        
        .. attribute:: pcp_server_instance
        
        	PCP server instance
        	**type**\: list of    :py:class:`PcpServerInstance <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance>`
        
        

        """

        _prefix = 'pcp-server'
        _revision = '2015-08-05'

        def __init__(self):
            self.parent = None
            self.pcp_server_instance = YList()
            self.pcp_server_instance.parent = self
            self.pcp_server_instance.name = 'pcp_server_instance'


        class PcpServerInstance(object):
            """
            PCP server instance
            
            .. attribute:: id  <key>
            
            	The identifier of the PCP server instance
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: authentication_enabled
            
            	Indicates whether PCP authentication  is enabled/disabled
            	**type**\:  bool
            
            .. attribute:: authentication_support
            
            	Status of the support of PCP authentication
            	**type**\:  bool
            
            .. attribute:: configured_pcp_server_ip_address
            
            	List of PCP server IP addresses
            	**type**\: list of    :py:class:`ConfiguredPcpServerIpAddress <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.ConfiguredPcpServerIpAddress>`
            
            .. attribute:: enabled_protocol
            
            	Indicates the set of enabled transport protocols
            	**type**\: list of    :py:class:`EnabledProtocol <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.EnabledProtocol>`
            
            .. attribute:: epoch
            
            	value of the current server's epoch
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: error_lifetime
            
            	Vvalues for the error lifetime to be returned to requesting PCP clients
            	**type**\:   :py:class:`ErrorLifetime <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.ErrorLifetime>`
            
            .. attribute:: exclude_ports
            
            	Indicates ports that are excluded from  dynamic assignment
            	**type**\: list of    :py:class:`ExcludePorts <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.ExcludePorts>`
            
            .. attribute:: external_ip_address_pool
            
            	Pool of external IP addresses used to service requesting clients
            	**type**\: list of    :py:class:`ExternalIpAddressPool <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.ExternalIpAddressPool>`
            
            .. attribute:: lifetime
            
            	lifetime\-related configuration
            	**type**\:   :py:class:`Lifetime <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.Lifetime>`
            
            .. attribute:: mapping_table
            
            	Mapping table
            	**type**\:   :py:class:`MappingTable <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable>`
            
            .. attribute:: name
            
            	The name of the PCP server instance
            	**type**\:  str
            
            .. attribute:: nonce_validation_checks_enable
            
            	Indicates whether NONCE validation checks are  enabled/disabled
            	**type**\:  bool
            
            .. attribute:: opcode_capability
            
            	Opcode\-related capabilities
            	**type**\:   :py:class:`OpcodeCapability <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.OpcodeCapability>`
            
            .. attribute:: opcode_configuration
            
            	Opcode\-related configuration
            	**type**\:   :py:class:`OpcodeConfiguration <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.OpcodeConfiguration>`
            
            .. attribute:: option_capability
            
            	Option\-related capabilities
            	**type**\:   :py:class:`OptionCapability <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.OptionCapability>`
            
            .. attribute:: option_configuration
            
            	Option\-related configuration
            	**type**\:   :py:class:`OptionConfiguration <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration>`
            
            .. attribute:: pcp_controlled_function_capability
            
            	list of controlled functions
            	**type**\:   :py:class:`PcpControlledFunctionCapability <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.PcpControlledFunctionCapability>`
            
            .. attribute:: port_parity_preservation_enable
            
            	Indicates whether port parity preservation  is enabled/disabled
            	**type**\:  bool
            
            .. attribute:: port_parity_preservation_support
            
            	Indicates whether port parity preservation is  supported
            	**type**\:  bool
            
            .. attribute:: port_preservation_enable
            
            	Indicates whether port preservation  is enabled/disabled
            	**type**\:  bool
            
            .. attribute:: port_preservation_suport
            
            	Indicates whether port preservation  is supported
            	**type**\:  bool
            
            .. attribute:: port_quota
            
            	Indicates the configured port quota
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: port_randomization_enable
            
            	Indicates whether port randomization  is enabled/disabled
            	**type**\:  bool
            
            .. attribute:: port_randomization_support
            
            	Indicates whether port randomization is  supported
            	**type**\:  bool
            
            .. attribute:: preferred_version
            
            	List of preferred version.  Mainly used for unsolicited messages
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: protocol_capabilities
            
            	A set of supported transported protocols
            	**type**\: list of    :py:class:`ProtocolCapabilities <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.ProtocolCapabilities>`
            
            .. attribute:: subscriber_mask
            
            	Indicates the configured subscriber\-mask
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: subscriber_mask_support
            
            	Indicates if the subscriber\-mask feature is supported
            	**type**\:  bool
            
            .. attribute:: supported_version
            
            	List of supported PCP versions
            	**type**\: list of    :py:class:`SupportedVersion <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.SupportedVersion>`
            
            .. attribute:: traffic_statistics
            
            	traffic statistics
            	**type**\:   :py:class:`TrafficStatistics <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics>`
            
            

            """

            _prefix = 'pcp-server'
            _revision = '2015-08-05'

            def __init__(self):
                self.parent = None
                self.id = None
                self.authentication_enabled = None
                self.authentication_support = None
                self.configured_pcp_server_ip_address = YList()
                self.configured_pcp_server_ip_address.parent = self
                self.configured_pcp_server_ip_address.name = 'configured_pcp_server_ip_address'
                self.enabled_protocol = YList()
                self.enabled_protocol.parent = self
                self.enabled_protocol.name = 'enabled_protocol'
                self.epoch = None
                self.error_lifetime = PcpServerState.PcpServerInstances.PcpServerInstance.ErrorLifetime()
                self.error_lifetime.parent = self
                self.exclude_ports = YList()
                self.exclude_ports.parent = self
                self.exclude_ports.name = 'exclude_ports'
                self.external_ip_address_pool = YList()
                self.external_ip_address_pool.parent = self
                self.external_ip_address_pool.name = 'external_ip_address_pool'
                self.lifetime = PcpServerState.PcpServerInstances.PcpServerInstance.Lifetime()
                self.lifetime.parent = self
                self.mapping_table = PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable()
                self.mapping_table.parent = self
                self.name = None
                self.nonce_validation_checks_enable = None
                self.opcode_capability = PcpServerState.PcpServerInstances.PcpServerInstance.OpcodeCapability()
                self.opcode_capability.parent = self
                self.opcode_configuration = PcpServerState.PcpServerInstances.PcpServerInstance.OpcodeConfiguration()
                self.opcode_configuration.parent = self
                self.option_capability = PcpServerState.PcpServerInstances.PcpServerInstance.OptionCapability()
                self.option_capability.parent = self
                self.option_configuration = PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration()
                self.option_configuration.parent = self
                self.pcp_controlled_function_capability = PcpServerState.PcpServerInstances.PcpServerInstance.PcpControlledFunctionCapability()
                self.pcp_controlled_function_capability.parent = self
                self.port_parity_preservation_enable = None
                self.port_parity_preservation_support = None
                self.port_preservation_enable = None
                self.port_preservation_suport = None
                self.port_quota = None
                self.port_randomization_enable = None
                self.port_randomization_support = None
                self.preferred_version = None
                self.protocol_capabilities = YList()
                self.protocol_capabilities.parent = self
                self.protocol_capabilities.name = 'protocol_capabilities'
                self.subscriber_mask = None
                self.subscriber_mask_support = None
                self.supported_version = YList()
                self.supported_version.parent = self
                self.supported_version.name = 'supported_version'
                self.traffic_statistics = PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics()
                self.traffic_statistics.parent = self


            class SupportedVersion(object):
                """
                List of supported PCP versions.
                
                .. attribute:: version  <key>
                
                	Indicates a PCP server.  Current versions are\: 0, 1, and 2
                	**type**\:  int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.version = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.version is None:
                        raise YPYModelError('Key property version is None')

                    return self.parent._common_path +'/ietf-pcp-server:supported-version[ietf-pcp-server:version = ' + str(self.version) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.version is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.SupportedVersion']['meta_info']


            class ConfiguredPcpServerIpAddress(object):
                """
                List of PCP server IP addresses
                
                .. attribute:: address_id  <key>
                
                	The identifier of the address
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ip_address
                
                	IP address of the PCP server
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.address_id = None
                    self.ip_address = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.address_id is None:
                        raise YPYModelError('Key property address_id is None')

                    return self.parent._common_path +'/ietf-pcp-server:configured-pcp-server-ip-address[ietf-pcp-server:address-id = ' + str(self.address_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.address_id is not None:
                        return True

                    if self.ip_address is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.ConfiguredPcpServerIpAddress']['meta_info']


            class ExternalIpAddressPool(object):
                """
                Pool of external IP addresses used to service
                requesting clients.
                
                .. attribute:: address_id  <key>
                
                	An identifier
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: external_ip_pool
                
                	An address or prefix
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.address_id = None
                    self.external_ip_pool = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.address_id is None:
                        raise YPYModelError('Key property address_id is None')

                    return self.parent._common_path +'/ietf-pcp-server:external-ip-address-pool[ietf-pcp-server:address-id = ' + str(self.address_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.address_id is not None:
                        return True

                    if self.external_ip_pool is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.ExternalIpAddressPool']['meta_info']


            class OpcodeCapability(object):
                """
                Opcode\-related capabilities
                
                .. attribute:: announce
                
                	ANNOUNCE opcode
                	**type**\:  bool
                
                .. attribute:: map
                
                	MAP opcode
                	**type**\:  bool
                
                .. attribute:: peer
                
                	PEER opcode
                	**type**\:  bool
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.announce = None
                    self.map = None
                    self.peer = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-pcp-server:opcode-capability'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.announce is not None:
                        return True

                    if self.map is not None:
                        return True

                    if self.peer is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OpcodeCapability']['meta_info']


            class OptionCapability(object):
                """
                Option\-related capabilities
                
                .. attribute:: description
                
                	Associates a description with a mapping [RFC7220]
                	**type**\:   :py:class:`Description <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.OptionCapability.Description>`
                
                .. attribute:: filter
                
                	This option indicates that filtering incoming packets is desired
                	**type**\:   :py:class:`Filter <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.OptionCapability.Filter>`
                
                .. attribute:: port_set
                
                	Indicates whether PORT\_SET is supported/enabled
                	**type**\:  bool
                
                .. attribute:: prefer_failure
                
                	This option indicates that if the PCP server is unable to map both the suggested external port and suggested external address, the PCP server should not create a mapping.  This differs from the behavior without this option, which is to create a mapping.  PREFER\_FAILURE is never necessary for a PCP client to manage mappings for itself, and its use causes additional work in the PCP client and in the PCP server. See Section 13.2 of [RFC6887]
                	**type**\:  bool
                
                .. attribute:: prefix64
                
                	PREFIX64 PCP option [RFC7225]
                	**type**\:  bool
                
                .. attribute:: third_party
                
                	THIRD\_PARTY option is used when a PCP client wants  to control a mapping to an internal host other  than itself [RFC6887]
                	**type**\:  bool
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.description = PcpServerState.PcpServerInstances.PcpServerInstance.OptionCapability.Description()
                    self.description.parent = self
                    self.filter = PcpServerState.PcpServerInstances.PcpServerInstance.OptionCapability.Filter()
                    self.filter.parent = self
                    self.port_set = None
                    self.prefer_failure = None
                    self.prefix64 = None
                    self.third_party = None


                class Filter(object):
                    """
                    This option indicates that filtering incoming packets
                    is desired.
                    
                    .. attribute:: filter_enabled
                    
                    	Enable/disable FILTER option
                    	**type**\:  bool
                    
                    .. attribute:: max_filters
                    
                    	Indicates the maximum number of filters  associated with a mapping
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pcp-server'
                    _revision = '2015-08-05'

                    def __init__(self):
                        self.parent = None
                        self.filter_enabled = None
                        self.max_filters = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-pcp-server:filter'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.filter_enabled is not None:
                            return True

                        if self.max_filters is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_pcp_server as meta
                        return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionCapability.Filter']['meta_info']


                class Description(object):
                    """
                    Associates a description with a mapping [RFC7220].
                    
                    .. attribute:: description_enabled
                    
                    	Enable/disable DESCRIPTION option
                    	**type**\:  bool
                    
                    .. attribute:: max_description
                    
                    	Indicates the maximum length of the description  associated with a mapping
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pcp-server'
                    _revision = '2015-08-05'

                    def __init__(self):
                        self.parent = None
                        self.description_enabled = None
                        self.max_description = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-pcp-server:description'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.description_enabled is not None:
                            return True

                        if self.max_description is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_pcp_server as meta
                        return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionCapability.Description']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-pcp-server:option-capability'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.description is not None and self.description._has_data():
                        return True

                    if self.filter is not None and self.filter._has_data():
                        return True

                    if self.port_set is not None:
                        return True

                    if self.prefer_failure is not None:
                        return True

                    if self.prefix64 is not None:
                        return True

                    if self.third_party is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionCapability']['meta_info']


            class ProtocolCapabilities(object):
                """
                A set of supported transported protocols
                
                .. attribute:: protocol_id  <key>
                
                	transport protocol
                	**type**\:  int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.protocol_id = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.protocol_id is None:
                        raise YPYModelError('Key property protocol_id is None')

                    return self.parent._common_path +'/ietf-pcp-server:protocol-capabilities[ietf-pcp-server:protocol-id = ' + str(self.protocol_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.protocol_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.ProtocolCapabilities']['meta_info']


            class PcpControlledFunctionCapability(object):
                """
                list of controlled functions.
                
                .. attribute:: ds_lite
                
                	DS\-Lite
                	**type**\:  bool
                
                .. attribute:: ipv4_firewall
                
                	IPv4 firewall
                	**type**\:  bool
                
                .. attribute:: ipv6_firewall
                
                	IPv6 firewall
                	**type**\:  bool
                
                .. attribute:: nat44
                
                	NAT44
                	**type**\:  bool
                
                .. attribute:: nat64
                
                	NAT64
                	**type**\:  bool
                
                .. attribute:: nptv6
                
                	NPTv6
                	**type**\:  bool
                
                .. attribute:: port_range_router
                
                	Port Range Router
                	**type**\:  bool
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.ds_lite = None
                    self.ipv4_firewall = None
                    self.ipv6_firewall = None
                    self.nat44 = None
                    self.nat64 = None
                    self.nptv6 = None
                    self.port_range_router = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-pcp-server:pcp-controlled-function-capability'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.ds_lite is not None:
                        return True

                    if self.ipv4_firewall is not None:
                        return True

                    if self.ipv6_firewall is not None:
                        return True

                    if self.nat44 is not None:
                        return True

                    if self.nat64 is not None:
                        return True

                    if self.nptv6 is not None:
                        return True

                    if self.port_range_router is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.PcpControlledFunctionCapability']['meta_info']


            class OpcodeConfiguration(object):
                """
                Opcode\-related configuration
                
                .. attribute:: announce
                
                	ANNOUNCE opcode
                	**type**\:  bool
                
                .. attribute:: map
                
                	MAP opcode
                	**type**\:  bool
                
                .. attribute:: peer
                
                	PEER opcode
                	**type**\:  bool
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.announce = None
                    self.map = None
                    self.peer = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-pcp-server:opcode-configuration'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.announce is not None:
                        return True

                    if self.map is not None:
                        return True

                    if self.peer is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OpcodeConfiguration']['meta_info']


            class OptionConfiguration(object):
                """
                Option\-related configuration
                
                .. attribute:: description
                
                	enable/disable DESCRIPTION option
                	**type**\:   :py:class:`Description <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Description>`
                
                .. attribute:: filter
                
                	enable/disable FILTER option
                	**type**\:   :py:class:`Filter <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Filter>`
                
                .. attribute:: port_set_option
                
                	enable/disable PORT\_SET option
                	**type**\:   :py:class:`PortSetOption <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.PortSetOption>`
                
                .. attribute:: prefer_failure
                
                	enable/disable PREFER\_FAILURE option
                	**type**\:  bool
                
                .. attribute:: prefix64_option
                
                	enable/disable PREFIX64 option
                	**type**\:   :py:class:`Prefix64Option <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option>`
                
                .. attribute:: third_party
                
                	enable/disable THIRD\_PARTY option
                	**type**\:  bool
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.description = PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Description()
                    self.description.parent = self
                    self.filter = PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Filter()
                    self.filter.parent = self
                    self.port_set_option = PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.PortSetOption()
                    self.port_set_option.parent = self
                    self.prefer_failure = None
                    self.prefix64_option = PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option()
                    self.prefix64_option.parent = self
                    self.third_party = None


                class Filter(object):
                    """
                    enable/disable FILTER option.
                    
                    .. attribute:: filter_enabled
                    
                    	Enable/disable FILTER option
                    	**type**\:  bool
                    
                    .. attribute:: max_filters
                    
                    	Indicates the maximum number of filters  associated with a mapping
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pcp-server'
                    _revision = '2015-08-05'

                    def __init__(self):
                        self.parent = None
                        self.filter_enabled = None
                        self.max_filters = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-pcp-server:filter'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.filter_enabled is not None:
                            return True

                        if self.max_filters is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_pcp_server as meta
                        return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Filter']['meta_info']


                class PortSetOption(object):
                    """
                    enable/disable PORT\_SET option.
                    
                    .. attribute:: default_port_set_size
                    
                    	Indicates the default size of a port set
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: maximum_port_set_size
                    
                    	Indicates the maximum size of a port set
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: port_set_enable
                    
                    	Enable/disable PORT\_SET option
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'pcp-server'
                    _revision = '2015-08-05'

                    def __init__(self):
                        self.parent = None
                        self.default_port_set_size = None
                        self.maximum_port_set_size = None
                        self.port_set_enable = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-pcp-server:port-set-option'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.default_port_set_size is not None:
                            return True

                        if self.maximum_port_set_size is not None:
                            return True

                        if self.port_set_enable is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_pcp_server as meta
                        return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.PortSetOption']['meta_info']


                class Description(object):
                    """
                    enable/disable DESCRIPTION option.
                    
                    .. attribute:: description_enabled
                    
                    	Enable/disable DESCRIPTION option
                    	**type**\:  bool
                    
                    .. attribute:: max_description
                    
                    	Indicates the maximum length of the description  associated with a mapping
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pcp-server'
                    _revision = '2015-08-05'

                    def __init__(self):
                        self.parent = None
                        self.description_enabled = None
                        self.max_description = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-pcp-server:description'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.description_enabled is not None:
                            return True

                        if self.max_description is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_pcp_server as meta
                        return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Description']['meta_info']


                class Prefix64Option(object):
                    """
                    enable/disable PREFIX64 option.
                    
                    .. attribute:: prefix64
                    
                    	maintains a list of Prefix64s
                    	**type**\: list of    :py:class:`Prefix64 <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64>`
                    
                    .. attribute:: prefix64_option_enable
                    
                    	Indicates whether the option is enabled/disabled
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'pcp-server'
                    _revision = '2015-08-05'

                    def __init__(self):
                        self.parent = None
                        self.prefix64 = YList()
                        self.prefix64.parent = self
                        self.prefix64.name = 'prefix64'
                        self.prefix64_option_enable = None


                    class Prefix64(object):
                        """
                        maintains a list of Prefix64s.
                        
                        .. attribute:: prefix64_id  <key>
                        
                        	An identifier of a Prefix64
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dest_ipv4_prefix
                        
                        	used to solve the destination\-dependent  Pref64\:\:/n discovery problem discussed in  Section 5.1 of [RFC7050]
                        	**type**\: list of    :py:class:`DestIpv4Prefix <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64.DestIpv4Prefix>`
                        
                        .. attribute:: prefix64
                        
                        	A Prefix64
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                        
                        .. attribute:: suffix
                        
                        	The suffix is used for constructing an  IPv4\-converted IPv6 address from an IPv4 address as  specified in Section 2.2 of [RFC6052]. No suffix is  included if a /96 Prefix64 is used
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'pcp-server'
                        _revision = '2015-08-05'

                        def __init__(self):
                            self.parent = None
                            self.prefix64_id = None
                            self.dest_ipv4_prefix = YList()
                            self.dest_ipv4_prefix.parent = self
                            self.dest_ipv4_prefix.name = 'dest_ipv4_prefix'
                            self.prefix64 = None
                            self.suffix = None


                        class DestIpv4Prefix(object):
                            """
                            used to solve the destination\-dependent
                             Pref64\:\:/n discovery problem discussed in
                             Section 5.1 of [RFC7050].
                            
                            .. attribute:: ipv4_prefix_id  <key>
                            
                            	An identifier of a destination IPv4 prefix
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv4_prefix
                            
                            	an IPv4 prefix
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                            
                            

                            """

                            _prefix = 'pcp-server'
                            _revision = '2015-08-05'

                            def __init__(self):
                                self.parent = None
                                self.ipv4_prefix_id = None
                                self.ipv4_prefix = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.ipv4_prefix_id is None:
                                    raise YPYModelError('Key property ipv4_prefix_id is None')

                                return self.parent._common_path +'/ietf-pcp-server:dest-ipv4-prefix[ietf-pcp-server:ipv4-prefix-id = ' + str(self.ipv4_prefix_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ipv4_prefix_id is not None:
                                    return True

                                if self.ipv4_prefix is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_pcp_server as meta
                                return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64.DestIpv4Prefix']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.prefix64_id is None:
                                raise YPYModelError('Key property prefix64_id is None')

                            return self.parent._common_path +'/ietf-pcp-server:prefix64[ietf-pcp-server:prefix64-id = ' + str(self.prefix64_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix64_id is not None:
                                return True

                            if self.dest_ipv4_prefix is not None:
                                for child_ref in self.dest_ipv4_prefix:
                                    if child_ref._has_data():
                                        return True

                            if self.prefix64 is not None:
                                return True

                            if self.suffix is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_pcp_server as meta
                            return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option.Prefix64']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-pcp-server:prefix64-option'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.prefix64 is not None:
                            for child_ref in self.prefix64:
                                if child_ref._has_data():
                                    return True

                        if self.prefix64_option_enable is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_pcp_server as meta
                        return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration.Prefix64Option']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-pcp-server:option-configuration'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.description is not None and self.description._has_data():
                        return True

                    if self.filter is not None and self.filter._has_data():
                        return True

                    if self.port_set_option is not None and self.port_set_option._has_data():
                        return True

                    if self.prefer_failure is not None:
                        return True

                    if self.prefix64_option is not None and self.prefix64_option._has_data():
                        return True

                    if self.third_party is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.OptionConfiguration']['meta_info']


            class EnabledProtocol(object):
                """
                Indicates the set of enabled transport protocols.
                
                .. attribute:: protocol_id  <key>
                
                	A transport protocol
                	**type**\:  int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.protocol_id = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.protocol_id is None:
                        raise YPYModelError('Key property protocol_id is None')

                    return self.parent._common_path +'/ietf-pcp-server:enabled-protocol[ietf-pcp-server:protocol-id = ' + str(self.protocol_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.protocol_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.EnabledProtocol']['meta_info']


            class ExcludePorts(object):
                """
                Indicates ports that are excluded from
                 dynamic assignment.
                
                .. attribute:: id  <key>
                
                	identifier
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: end_port_number
                
                	End of the port range
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: single_port_number
                
                	used for single port numbers
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: start_port_number
                
                	Begining of the port range
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.id = None
                    self.end_port_number = None
                    self.single_port_number = None
                    self.start_port_number = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.id is None:
                        raise YPYModelError('Key property id is None')

                    return self.parent._common_path +'/ietf-pcp-server:exclude-ports[ietf-pcp-server:id = ' + str(self.id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.id is not None:
                        return True

                    if self.end_port_number is not None:
                        return True

                    if self.single_port_number is not None:
                        return True

                    if self.start_port_number is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.ExcludePorts']['meta_info']


            class Lifetime(object):
                """
                lifetime\-related configuration
                
                .. attribute:: maximum_lifetime
                
                	configured maximum\-lifetime
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: minimum_lifetime
                
                	configured minimum lifetime
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.maximum_lifetime = None
                    self.minimum_lifetime = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-pcp-server:lifetime'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.maximum_lifetime is not None:
                        return True

                    if self.minimum_lifetime is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.Lifetime']['meta_info']


            class ErrorLifetime(object):
                """
                Vvalues for the error lifetime to be
                returned to requesting PCP clients.
                
                .. attribute:: maximum_error_lifetime
                
                	Configured maximum error lifetime, in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: minimum_error_lifetime
                
                	Configured minimum error lifetime, in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.maximum_error_lifetime = None
                    self.minimum_error_lifetime = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-pcp-server:error-lifetime'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.maximum_error_lifetime is not None:
                        return True

                    if self.minimum_error_lifetime is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.ErrorLifetime']['meta_info']


            class MappingTable(object):
                """
                Mapping table
                
                .. attribute:: mapping_entry
                
                	mapping entry
                	**type**\: list of    :py:class:`MappingEntry <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry>`
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.mapping_entry = YList()
                    self.mapping_entry.parent = self
                    self.mapping_entry.name = 'mapping_entry'


                class MappingEntry(object):
                    """
                    mapping entry
                    
                    .. attribute:: index  <key>
                    
                    	A unique identifier of a mapping entry
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: description
                    
                    	a description string associated with the mapping
                    	**type**\:  str
                    
                    .. attribute:: external_ip_address
                    
                    	External IP address. Can be 'Suggested' or 'Assigned'.  It can be set by a client to stale\-ip\-address, if available or to (\:\:) (for requesting external IPv6 addresses) or (\:\:ffff\:0\:0) (for requesting external IPv4 addresses)
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                    
                    .. attribute:: external_port
                    
                    	External port number. Can be 'Suggested' or 'Assigned'
                    	**type**\:   :py:class:`ExternalPort <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.ExternalPort>`
                    
                    .. attribute:: filter
                    
                    	a list of filters associated with the mapping
                    	**type**\: list of    :py:class:`Filter <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.Filter>`
                    
                    .. attribute:: internal_ip_address
                    
                    	Corresponds to the PCP Client's IP Address defined in [RFC6887]
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                    
                    .. attribute:: internal_port
                    
                    	Internal port for the mapping. Value 0 indicates 'all ports', and is legal when the lifetime is zero (a delete request), if the protocol does not use 16\-bit port numbers, or the client is requesting 'all ports'.  If the protocol is zero (meaning 'all protocols'), then internal port is set to zero
                    	**type**\:   :py:class:`InternalPort <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.InternalPort>`
                    
                    .. attribute:: lifetime
                    
                    	Lifetime of the mapping.  Can be requested/assigned/remaining
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mapping_nonce
                    
                    	A random value chosen by the PCP client
                    	**type**\:  str
                    
                    .. attribute:: prefer_failure_tagged
                    
                    	a tag which indicates whether PREFER\_FAILURE  is (to be) used
                    	**type**\:  bool
                    
                    .. attribute:: protocol
                    
                    	Upper\-layer protocol associated with this Opcode. Values are taken from the IANA protocol registry. For example, this field contains 6 (TCP) if the Opcode is intended to create a TCP mapping.  This field contains 17 (UDP) if the Opcode is intended to create a UDP mapping. The value 0 has a special meaning for 'all protocols'
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: status
                    
                    	Indicates the status of a mapping entry
                    	**type**\:   :py:class:`StatusEnum <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.StatusEnum>`
                    
                    .. attribute:: status_code
                    
                    	result status code
                    	**type**\:   :py:class:`StatusCodeEnum <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.StatusCodeEnum>`
                    
                    .. attribute:: third_party_address
                    
                    	used to indicate the internal IP address  when THIRD\_PARTY is in use
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                    
                    

                    """

                    _prefix = 'pcp-server'
                    _revision = '2015-08-05'

                    def __init__(self):
                        self.parent = None
                        self.index = None
                        self.description = None
                        self.external_ip_address = None
                        self.external_port = PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.ExternalPort()
                        self.external_port.parent = self
                        self.filter = YList()
                        self.filter.parent = self
                        self.filter.name = 'filter'
                        self.internal_ip_address = None
                        self.internal_port = PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.InternalPort()
                        self.internal_port.parent = self
                        self.lifetime = None
                        self.mapping_nonce = None
                        self.prefer_failure_tagged = None
                        self.protocol = None
                        self.status = None
                        self.status_code = None
                        self.third_party_address = None

                    class StatusCodeEnum(Enum):
                        """
                        StatusCodeEnum

                        result status code.

                        .. data:: SUCCESS = 0

                        	Success

                        .. data:: unsupported_version = 1

                        	The version number at the start of the PCP Request

                        	header is not recognized by this PCP server.

                        	This is a long lifetime error.

                        .. data:: not_authorized = 2

                        	The requested operation is disabled for this PCP

                        	client, or the PCP client requested an operation

                        	that cannot be fulfilled by the PCP server's

                        	security policy.

                        	This is a long lifetime error.

                        .. data:: malformed_request = 3

                        	The request could not be successfully parsed.

                        	This is a long lifetime error.

                        .. data:: unsupported_opcode = 4

                        	Unsupported Opcode.

                        	This is a long lifetime error.

                        .. data:: unsupported_option = 5

                        	Unsupported option.  This error only occurs if

                        	the option is in the mandatory-to-process range.

                        	This is a long lifetime error.

                        .. data:: malformed_option = 6

                        	Malformed option (e.g., appears too many times,

                        	invalid length).

                        	This is a long lifetime error.

                        .. data:: network_failure = 7

                        	The PCP server or the device it controls is

                        	experiencing a network failure of some sort

                        	(e.g., has not yet obtained an external

                        	IP address).

                        	This is a short lifetime error.

                        .. data:: no_resources = 8

                        	Request is well-formed and valid, but the server

                        	has insufficient resources to complete

                        	the requested operation at this time.

                        	For example, the NAT device cannot create more

                        	mappings at this time, is short of CPU cycles

                        	or memory, or is unable to handle the request

                        	due to some other temporary condition.

                        	The same request may succeed in the future.

                        	This is a system-wide error, different from

                        	USER_EX_QUOTA.  This can be used as a

                        	catch-all error, should no other error

                        	message be suitable.

                        	This is a short lifetime error.

                        .. data:: unsupported_protocol = 9

                        	Unsupported transport protocol, e.g.,

                        	SCTP in a  NAT that handles only UDP and TCP.

                        	This is a long lifetime error.

                        .. data:: ex_quota = 10

                        	This attempt to create a new mapping would

                        	exceed this subscriber's port quota.

                        	This is a short lifetime error.

                        .. data:: cannot_provide_external = 11

                        	The suggested external port and/or

                        	external address cannot be provided.

                        	This error must only be returned for:

                        	 *  MAP requests that included the

                        	    PREFER_FAILURE option

                        	 *  MAP requests for the SCTP protocol

                        	   (PREFER_FAILURE is implied)

                        	 *  PEER requests.

                        .. data:: address_mismatch = 12

                        	The source IP address of the request

                        	packet does not match the contents of the

                        	PCP Client's IP Address field, due to an

                        	unexpected NAT on the path between the PCP

                        	client and the PCP-controlled NAT or firewall.

                        	This is a long lifetime error.

                        .. data:: extensive_remote_peer = 13

                        	The PCP server was not able to create the

                        	filters in this request.  This result code must

                        	only be returned if the MAP request contained

                        	the FILTER option.

                        	This is a long lifetime error.

                        """

                        SUCCESS = 0

                        unsupported_version = 1

                        not_authorized = 2

                        malformed_request = 3

                        unsupported_opcode = 4

                        unsupported_option = 5

                        malformed_option = 6

                        network_failure = 7

                        no_resources = 8

                        unsupported_protocol = 9

                        ex_quota = 10

                        cannot_provide_external = 11

                        address_mismatch = 12

                        extensive_remote_peer = 13


                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_pcp_server as meta
                            return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.StatusCodeEnum']


                    class StatusEnum(Enum):
                        """
                        StatusEnum

                        Indicates the status of a mapping entry.

                        .. data:: disabled = 0

                        	The mapping entry is not in use (Disabled).

                        .. data:: requested = 1

                        	A PCP request has been sent for this mapping.

                        	Still waiting for a response from the server.

                        .. data:: assigned = 2

                        	This mapping has been granted by the server.

                        .. data:: stale = 3

                        	This is a stale mapping (case of reboot).

                        """

                        disabled = 0

                        requested = 1

                        assigned = 2

                        stale = 3


                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_pcp_server as meta
                            return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.StatusEnum']



                    class InternalPort(object):
                        """
                        Internal port for the mapping. Value 0 indicates
                        'all ports', and is legal when the lifetime is zero
                        (a delete request), if the protocol does not use
                        16\-bit port numbers, or the client is requesting
                        'all ports'.  If the protocol is zero
                        (meaning 'all protocols'), then internal port
                        is set to zero.
                        
                        .. attribute:: end_port_number
                        
                        	End of the port range
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: single_port_number
                        
                        	used for single port numbers
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: start_port_number
                        
                        	Begining of the port range
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'pcp-server'
                        _revision = '2015-08-05'

                        def __init__(self):
                            self.parent = None
                            self.end_port_number = None
                            self.single_port_number = None
                            self.start_port_number = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-pcp-server:internal-port'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.end_port_number is not None:
                                return True

                            if self.single_port_number is not None:
                                return True

                            if self.start_port_number is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_pcp_server as meta
                            return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.InternalPort']['meta_info']


                    class ExternalPort(object):
                        """
                        External port number. Can be 'Suggested' or 'Assigned'.
                        
                        .. attribute:: end_port_number
                        
                        	End of the port range
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: single_port_number
                        
                        	used for single port numbers
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: start_port_number
                        
                        	Begining of the port range
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'pcp-server'
                        _revision = '2015-08-05'

                        def __init__(self):
                            self.parent = None
                            self.end_port_number = None
                            self.single_port_number = None
                            self.start_port_number = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-pcp-server:external-port'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.end_port_number is not None:
                                return True

                            if self.single_port_number is not None:
                                return True

                            if self.start_port_number is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_pcp_server as meta
                            return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.ExternalPort']['meta_info']


                    class Filter(object):
                        """
                        a list of filters associated with the mapping.
                        
                        .. attribute:: filter_id  <key>
                        
                        	An identifier of the filter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_ip_prefix
                        
                        	The IP address of the remote peer
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                        
                        .. attribute:: remote_port_number
                        
                        	The port number of the remote peer. Value 0 indicates 'all ports'
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'pcp-server'
                        _revision = '2015-08-05'

                        def __init__(self):
                            self.parent = None
                            self.filter_id = None
                            self.remote_ip_prefix = None
                            self.remote_port_number = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.filter_id is None:
                                raise YPYModelError('Key property filter_id is None')

                            return self.parent._common_path +'/ietf-pcp-server:filter[ietf-pcp-server:filter-id = ' + str(self.filter_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.filter_id is not None:
                                return True

                            if self.remote_ip_prefix is not None:
                                return True

                            if self.remote_port_number is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_pcp_server as meta
                            return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry.Filter']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.index is None:
                            raise YPYModelError('Key property index is None')

                        return self.parent._common_path +'/ietf-pcp-server:mapping-entry[ietf-pcp-server:index = ' + str(self.index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.index is not None:
                            return True

                        if self.description is not None:
                            return True

                        if self.external_ip_address is not None:
                            return True

                        if self.external_port is not None and self.external_port._has_data():
                            return True

                        if self.filter is not None:
                            for child_ref in self.filter:
                                if child_ref._has_data():
                                    return True

                        if self.internal_ip_address is not None:
                            return True

                        if self.internal_port is not None and self.internal_port._has_data():
                            return True

                        if self.lifetime is not None:
                            return True

                        if self.mapping_nonce is not None:
                            return True

                        if self.prefer_failure_tagged is not None:
                            return True

                        if self.protocol is not None:
                            return True

                        if self.status is not None:
                            return True

                        if self.status_code is not None:
                            return True

                        if self.third_party_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_pcp_server as meta
                        return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable.MappingEntry']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-pcp-server:mapping-table'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.mapping_entry is not None:
                        for child_ref in self.mapping_entry:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.MappingTable']['meta_info']


            class TrafficStatistics(object):
                """
                traffic statistics
                
                .. attribute:: mapping_table
                
                	mapping table statistics
                	**type**\:   :py:class:`MappingTable <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics.MappingTable>`
                
                .. attribute:: opcode_statistics
                
                	Opcode\-related statistics
                	**type**\:   :py:class:`OpcodeStatistics <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics.OpcodeStatistics>`
                
                .. attribute:: port_in_use
                
                	ratio of the port usage
                	**type**\:  int
                
                	**range:** 0..100
                
                .. attribute:: traffic_statistics
                
                	Generic traffic statistics
                	**type**\:   :py:class:`TrafficStatistics_ <ydk.models.ietf.ietf_pcp_server.PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics.TrafficStatistics_>`
                
                

                """

                _prefix = 'pcp-server'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.mapping_table = PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics.MappingTable()
                    self.mapping_table.parent = self
                    self.opcode_statistics = PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics.OpcodeStatistics()
                    self.opcode_statistics.parent = self
                    self.port_in_use = None
                    self.traffic_statistics = PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics.TrafficStatistics_()
                    self.traffic_statistics.parent = self


                class TrafficStatistics_(object):
                    """
                    Generic traffic statistics.
                    
                    .. attribute:: dropped_byte
                    
                    	Counter for dropped traffic in bytes
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: dropped_packet
                    
                    	Counter for dropped packets
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: rcvd_byte
                    
                    	Counter for received traffic in bytes
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: rcvd_packet
                    
                    	Counter for received packets
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sent_byte
                    
                    	Counter for sent traffic in bytes
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sent_packet
                    
                    	Packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'pcp-server'
                    _revision = '2015-08-05'

                    def __init__(self):
                        self.parent = None
                        self.dropped_byte = None
                        self.dropped_packet = None
                        self.rcvd_byte = None
                        self.rcvd_packet = None
                        self.sent_byte = None
                        self.sent_packet = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-pcp-server:traffic-statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.dropped_byte is not None:
                            return True

                        if self.dropped_packet is not None:
                            return True

                        if self.rcvd_byte is not None:
                            return True

                        if self.rcvd_packet is not None:
                            return True

                        if self.sent_byte is not None:
                            return True

                        if self.sent_packet is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_pcp_server as meta
                        return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics.TrafficStatistics_']['meta_info']


                class OpcodeStatistics(object):
                    """
                    Opcode\-related statistics.
                    
                    .. attribute:: rcvd_announce
                    
                    	Counter for received ANNOUNCED messages
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: rcvd_malformed
                    
                    	Counter for received malformed opcodes
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: rcvd_map
                    
                    	Counter for received MAP messages
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: rcvd_peer
                    
                    	Counter for received PEER messages
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: rcvd_unknown
                    
                    	Counter for received unknown opcodes
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sent_annonce
                    
                    	Counter for sent ANNOUNCE messages
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sent_map
                    
                    	Counter for sent MAP messages
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sent_peer
                    
                    	Counter for sent PEER messages
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'pcp-server'
                    _revision = '2015-08-05'

                    def __init__(self):
                        self.parent = None
                        self.rcvd_announce = None
                        self.rcvd_malformed = None
                        self.rcvd_map = None
                        self.rcvd_peer = None
                        self.rcvd_unknown = None
                        self.sent_annonce = None
                        self.sent_map = None
                        self.sent_peer = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-pcp-server:opcode-statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.rcvd_announce is not None:
                            return True

                        if self.rcvd_malformed is not None:
                            return True

                        if self.rcvd_map is not None:
                            return True

                        if self.rcvd_peer is not None:
                            return True

                        if self.rcvd_unknown is not None:
                            return True

                        if self.sent_annonce is not None:
                            return True

                        if self.sent_map is not None:
                            return True

                        if self.sent_peer is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_pcp_server as meta
                        return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics.OpcodeStatistics']['meta_info']


                class MappingTable(object):
                    """
                    mapping table statistics
                    
                    .. attribute:: current_mt_size
                    
                    	Size of the mapping table
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: max_mt_size
                    
                    	Maximum configured size of the mapping table
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pcp-server'
                    _revision = '2015-08-05'

                    def __init__(self):
                        self.parent = None
                        self.current_mt_size = None
                        self.max_mt_size = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-pcp-server:mapping-table'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.current_mt_size is not None:
                            return True

                        if self.max_mt_size is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_pcp_server as meta
                        return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics.MappingTable']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-pcp-server:traffic-statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.mapping_table is not None and self.mapping_table._has_data():
                        return True

                    if self.opcode_statistics is not None and self.opcode_statistics._has_data():
                        return True

                    if self.port_in_use is not None:
                        return True

                    if self.traffic_statistics is not None and self.traffic_statistics._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_server as meta
                    return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance.TrafficStatistics']['meta_info']

            @property
            def _common_path(self):
                if self.id is None:
                    raise YPYModelError('Key property id is None')

                return '/ietf-pcp-server:pcp-server-state/ietf-pcp-server:pcp-server-instances/ietf-pcp-server:pcp-server-instance[ietf-pcp-server:id = ' + str(self.id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.id is not None:
                    return True

                if self.authentication_enabled is not None:
                    return True

                if self.authentication_support is not None:
                    return True

                if self.configured_pcp_server_ip_address is not None:
                    for child_ref in self.configured_pcp_server_ip_address:
                        if child_ref._has_data():
                            return True

                if self.enabled_protocol is not None:
                    for child_ref in self.enabled_protocol:
                        if child_ref._has_data():
                            return True

                if self.epoch is not None:
                    return True

                if self.error_lifetime is not None and self.error_lifetime._has_data():
                    return True

                if self.exclude_ports is not None:
                    for child_ref in self.exclude_ports:
                        if child_ref._has_data():
                            return True

                if self.external_ip_address_pool is not None:
                    for child_ref in self.external_ip_address_pool:
                        if child_ref._has_data():
                            return True

                if self.lifetime is not None and self.lifetime._has_data():
                    return True

                if self.mapping_table is not None and self.mapping_table._has_data():
                    return True

                if self.name is not None:
                    return True

                if self.nonce_validation_checks_enable is not None:
                    return True

                if self.opcode_capability is not None and self.opcode_capability._has_data():
                    return True

                if self.opcode_configuration is not None and self.opcode_configuration._has_data():
                    return True

                if self.option_capability is not None and self.option_capability._has_data():
                    return True

                if self.option_configuration is not None and self.option_configuration._has_data():
                    return True

                if self.pcp_controlled_function_capability is not None and self.pcp_controlled_function_capability._has_data():
                    return True

                if self.port_parity_preservation_enable is not None:
                    return True

                if self.port_parity_preservation_support is not None:
                    return True

                if self.port_preservation_enable is not None:
                    return True

                if self.port_preservation_suport is not None:
                    return True

                if self.port_quota is not None:
                    return True

                if self.port_randomization_enable is not None:
                    return True

                if self.port_randomization_support is not None:
                    return True

                if self.preferred_version is not None:
                    return True

                if self.protocol_capabilities is not None:
                    for child_ref in self.protocol_capabilities:
                        if child_ref._has_data():
                            return True

                if self.subscriber_mask is not None:
                    return True

                if self.subscriber_mask_support is not None:
                    return True

                if self.supported_version is not None:
                    for child_ref in self.supported_version:
                        if child_ref._has_data():
                            return True

                if self.traffic_statistics is not None and self.traffic_statistics._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_pcp_server as meta
                return meta._meta_table['PcpServerState.PcpServerInstances.PcpServerInstance']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-pcp-server:pcp-server-state/ietf-pcp-server:pcp-server-instances'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.pcp_server_instance is not None:
                for child_ref in self.pcp_server_instance:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_pcp_server as meta
            return meta._meta_table['PcpServerState.PcpServerInstances']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-pcp-server:pcp-server-state'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.pcp_server_instances is not None and self.pcp_server_instances._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pcp_server as meta
        return meta._meta_table['PcpServerState']['meta_info']



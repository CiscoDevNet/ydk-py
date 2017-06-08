""" ietf_pcp_iwf 

This module contains a collection of YANG definitions for
UPnP IGD/PCP Interworking implementations.

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




class PcpIwfConfig(object):
    """
    UPnP IGD/PCP Interworking Function
    
    .. attribute:: enable
    
    	Enable/Disable the UPnP IGD\-PCP IWF
    	**type**\:  bool
    
    .. attribute:: pcp_igd_iwf_instances
    
    	UPnP IGD/PCP Interworking Function instances
    	**type**\:   :py:class:`PcpIgdIwfInstances <ydk.models.ietf.ietf_pcp_iwf.PcpIwfConfig.PcpIgdIwfInstances>`
    
    

    """

    _prefix = 'pcp-iwf'
    _revision = '2015-08-05'

    def __init__(self):
        self.enable = None
        self.pcp_igd_iwf_instances = PcpIwfConfig.PcpIgdIwfInstances()
        self.pcp_igd_iwf_instances.parent = self


    class PcpIgdIwfInstances(object):
        """
        UPnP IGD/PCP Interworking Function instances
        
        .. attribute:: pcp_igd_iwf_instance
        
        	UPnP IGD/PCP Interworking Function instance
        	**type**\: list of    :py:class:`PcpIgdIwfInstance <ydk.models.ietf.ietf_pcp_iwf.PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance>`
        
        

        """

        _prefix = 'pcp-iwf'
        _revision = '2015-08-05'

        def __init__(self):
            self.parent = None
            self.pcp_igd_iwf_instance = YList()
            self.pcp_igd_iwf_instance.parent = self
            self.pcp_igd_iwf_instance.name = 'pcp_igd_iwf_instance'


        class PcpIgdIwfInstance(object):
            """
            UPnP IGD/PCP Interworking Function instance
            
            .. attribute:: id  <key>
            
            	An identifier of the IWF instance
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authentication_enable
            
            	Enable/disable PCP authentication
            	**type**\:  bool
            
            .. attribute:: igd_version
            
            	Configure UPnP IGD version(s)
            	**type**\:   :py:class:`IgdVersion <ydk.models.ietf.ietf_pcp_iwf.PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.IgdVersion>`
            
            .. attribute:: mapping_table
            
            	Mapping table as maintained by a  UPnP IGD\-PCP IWF instance
            	**type**\:   :py:class:`MappingTable <ydk.models.ietf.ietf_pcp_iwf.PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable>`
            
            .. attribute:: name
            
            	A name of the UPnP IGD\-PCP IWF instance
            	**type**\:  str
            
            .. attribute:: pcp_servers
            
            	List of configured PCP servers
            	**type**\: list of    :py:class:`PcpServers <ydk.models.ietf.ietf_pcp_iwf.PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServers>`
            
            .. attribute:: version
            
            	configures one or several PCP versions
            	**type**\: list of    :py:class:`Version <ydk.models.ietf.ietf_pcp_iwf.PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.Version>`
            
            

            """

            _prefix = 'pcp-iwf'
            _revision = '2015-08-05'

            def __init__(self):
                self.parent = None
                self.id = None
                self.authentication_enable = None
                self.igd_version = PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.IgdVersion()
                self.igd_version.parent = self
                self.mapping_table = PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable()
                self.mapping_table.parent = self
                self.name = None
                self.pcp_servers = YList()
                self.pcp_servers.parent = self
                self.pcp_servers.name = 'pcp_servers'
                self.version = YList()
                self.version.parent = self
                self.version.name = 'version'


            class Version(object):
                """
                configures one or several PCP versions.
                
                .. attribute:: version  <key>
                
                	Indicates a PCP server.  Current versions are\: 0, 1, and 2
                	**type**\:  int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'pcp-iwf'
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

                    return self.parent._common_path +'/ietf-pcp-iwf:version[ietf-pcp-iwf:version = ' + str(self.version) + ']'

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
                    from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                    return meta._meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.Version']['meta_info']


            class PcpServers(object):
                """
                List of configured PCP servers.
                
                .. attribute:: pcp_server_id  <key>
                
                	A unique identifier
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: external_address_familly
                
                	The address family of the external address(es) managed by the PCP server. Can be IPv4, IPv6 or both
                	**type**\:   :py:class:`IpVersionEnum <ydk.models.ietf.ietf_inet_types.IpVersionEnum>`
                
                .. attribute:: pcp_server_ip_address
                
                	a list of IP addresses of a PCP server
                	**type**\: list of    :py:class:`PcpServerIpAddress <ydk.models.ietf.ietf_pcp_iwf.PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServers.PcpServerIpAddress>`
                
                .. attribute:: stale_external_ip_address
                
                	A stale address that can be used by the PCP client to be assigned the same address upon reboot or other failure events
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                

                """

                _prefix = 'pcp-iwf'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.pcp_server_id = None
                    self.external_address_familly = None
                    self.pcp_server_ip_address = YList()
                    self.pcp_server_ip_address.parent = self
                    self.pcp_server_ip_address.name = 'pcp_server_ip_address'
                    self.stale_external_ip_address = None


                class PcpServerIpAddress(object):
                    """
                    a list of IP addresses of a PCP server
                    
                    .. attribute:: address_id  <key>
                    
                    	An identifier
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ip_address
                    
                    	An IP address of a PCP server
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'pcp-iwf'
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

                        return self.parent._common_path +'/ietf-pcp-iwf:pcp-server-ip-address[ietf-pcp-iwf:address-id = ' + str(self.address_id) + ']'

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
                        from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                        return meta._meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServers.PcpServerIpAddress']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.pcp_server_id is None:
                        raise YPYModelError('Key property pcp_server_id is None')

                    return self.parent._common_path +'/ietf-pcp-iwf:pcp-servers[ietf-pcp-iwf:pcp-server-id = ' + str(self.pcp_server_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.pcp_server_id is not None:
                        return True

                    if self.external_address_familly is not None:
                        return True

                    if self.pcp_server_ip_address is not None:
                        for child_ref in self.pcp_server_ip_address:
                            if child_ref._has_data():
                                return True

                    if self.stale_external_ip_address is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                    return meta._meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServers']['meta_info']


            class IgdVersion(object):
                """
                Configure UPnP IGD version(s).
                
                .. attribute:: igd_version
                
                	UPnP IGD Version
                	**type**\:   :py:class:`IgdVersionEnum <ydk.models.ietf.ietf_pcp_iwf.PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.IgdVersion.IgdVersionEnum>`
                
                

                """

                _prefix = 'pcp-iwf'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.igd_version = None

                class IgdVersionEnum(Enum):
                    """
                    IgdVersionEnum

                    UPnP IGD Version

                    .. data:: igd__COLON__1 = 0

                    	UPnP IGD:1

                    .. data:: igd__COLON__2 = 1

                    	UPnP IGD:2

                    .. data:: both = 2

                    	UPnP IGD:1 and UPnP IGD:2

                    """

                    igd__COLON__1 = 0

                    igd__COLON__2 = 1

                    both = 2


                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                        return meta._meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.IgdVersion.IgdVersionEnum']


                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-pcp-iwf:igd-version'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.igd_version is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                    return meta._meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.IgdVersion']['meta_info']


            class MappingTable(object):
                """
                Mapping table as maintained by a
                 UPnP IGD\-PCP IWF instance
                
                .. attribute:: mapping_entry
                
                	PCP Mapping Entry
                	**type**\: list of    :py:class:`MappingEntry <ydk.models.ietf.ietf_pcp_iwf.PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry>`
                
                

                """

                _prefix = 'pcp-iwf'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.mapping_entry = YList()
                    self.mapping_entry.parent = self
                    self.mapping_entry.name = 'mapping_entry'


                class MappingEntry(object):
                    """
                    PCP Mapping Entry.
                    
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
                    	**type**\:   :py:class:`ExternalPort <ydk.models.ietf.ietf_pcp_iwf.PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.ExternalPort>`
                    
                    .. attribute:: filter
                    
                    	a list of filters associated with the mapping
                    	**type**\: list of    :py:class:`Filter <ydk.models.ietf.ietf_pcp_iwf.PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.Filter>`
                    
                    .. attribute:: igd_control_point_address
                    
                    	IP address of the UPnP Control Point
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: igd_control_point_port
                    
                    	Port number
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: internal_ip_address
                    
                    	Corresponds to the PCP Client's IP Address defined in [RFC6887]
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                    
                    .. attribute:: internal_port
                    
                    	Internal port for the mapping. Value 0 indicates 'all ports', and is legal when the lifetime is zero (a delete request), if the protocol does not use 16\-bit port numbers, or the client is requesting 'all ports'.  If the protocol is zero (meaning 'all protocols'), then internal port is set to zero
                    	**type**\:   :py:class:`InternalPort <ydk.models.ietf.ietf_pcp_iwf.PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.InternalPort>`
                    
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
                    	**type**\:   :py:class:`StatusEnum <ydk.models.ietf.ietf_pcp_iwf.PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.StatusEnum>`
                    
                    .. attribute:: third_party_address
                    
                    	used to indicate the internal IP address  when THIRD\_PARTY is in use
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                    
                    

                    """

                    _prefix = 'pcp-iwf'
                    _revision = '2015-08-05'

                    def __init__(self):
                        self.parent = None
                        self.index = None
                        self.description = None
                        self.external_ip_address = None
                        self.external_port = PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.ExternalPort()
                        self.external_port.parent = self
                        self.filter = YList()
                        self.filter.parent = self
                        self.filter.name = 'filter'
                        self.igd_control_point_address = None
                        self.igd_control_point_port = None
                        self.internal_ip_address = None
                        self.internal_port = PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.InternalPort()
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
                            from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                            return meta._meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.StatusEnum']



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

                        _prefix = 'pcp-iwf'
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

                            return self.parent._common_path +'/ietf-pcp-iwf:internal-port'

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
                            from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                            return meta._meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.InternalPort']['meta_info']


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

                        _prefix = 'pcp-iwf'
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

                            return self.parent._common_path +'/ietf-pcp-iwf:external-port'

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
                            from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                            return meta._meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.ExternalPort']['meta_info']


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

                        _prefix = 'pcp-iwf'
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

                            return self.parent._common_path +'/ietf-pcp-iwf:filter[ietf-pcp-iwf:filter-id = ' + str(self.filter_id) + ']'

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
                            from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                            return meta._meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.Filter']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.index is None:
                            raise YPYModelError('Key property index is None')

                        return self.parent._common_path +'/ietf-pcp-iwf:mapping-entry[ietf-pcp-iwf:index = ' + str(self.index) + ']'

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

                        if self.igd_control_point_address is not None:
                            return True

                        if self.igd_control_point_port is not None:
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
                        from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                        return meta._meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-pcp-iwf:mapping-table'

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
                    from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                    return meta._meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable']['meta_info']

            @property
            def _common_path(self):
                if self.id is None:
                    raise YPYModelError('Key property id is None')

                return '/ietf-pcp-iwf:pcp-iwf-config/ietf-pcp-iwf:pcp-igd-iwf-instances/ietf-pcp-iwf:pcp-igd-iwf-instance[ietf-pcp-iwf:id = ' + str(self.id) + ']'

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

                if self.igd_version is not None and self.igd_version._has_data():
                    return True

                if self.mapping_table is not None and self.mapping_table._has_data():
                    return True

                if self.name is not None:
                    return True

                if self.pcp_servers is not None:
                    for child_ref in self.pcp_servers:
                        if child_ref._has_data():
                            return True

                if self.version is not None:
                    for child_ref in self.version:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                return meta._meta_table['PcpIwfConfig.PcpIgdIwfInstances.PcpIgdIwfInstance']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-pcp-iwf:pcp-iwf-config/ietf-pcp-iwf:pcp-igd-iwf-instances'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.pcp_igd_iwf_instance is not None:
                for child_ref in self.pcp_igd_iwf_instance:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
            return meta._meta_table['PcpIwfConfig.PcpIgdIwfInstances']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-pcp-iwf:pcp-iwf-config'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.enable is not None:
            return True

        if self.pcp_igd_iwf_instances is not None and self.pcp_igd_iwf_instances._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
        return meta._meta_table['PcpIwfConfig']['meta_info']


class PcpIwfState(object):
    """
    UPnP IGD/PCP Interworking Function
    
    .. attribute:: pcp_igd_iwf_instances
    
    	UPnP IGD/PCP Interworking Function instances
    	**type**\:   :py:class:`PcpIgdIwfInstances <ydk.models.ietf.ietf_pcp_iwf.PcpIwfState.PcpIgdIwfInstances>`
    
    

    """

    _prefix = 'pcp-iwf'
    _revision = '2015-08-05'

    def __init__(self):
        self.pcp_igd_iwf_instances = PcpIwfState.PcpIgdIwfInstances()
        self.pcp_igd_iwf_instances.parent = self


    class PcpIgdIwfInstances(object):
        """
        UPnP IGD/PCP Interworking Function instances
        
        .. attribute:: pcp_igd_iwf_instance
        
        	UPnP IGD/PCP Interworking Function instance
        	**type**\: list of    :py:class:`PcpIgdIwfInstance <ydk.models.ietf.ietf_pcp_iwf.PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance>`
        
        

        """

        _prefix = 'pcp-iwf'
        _revision = '2015-08-05'

        def __init__(self):
            self.parent = None
            self.pcp_igd_iwf_instance = YList()
            self.pcp_igd_iwf_instance.parent = self
            self.pcp_igd_iwf_instance.name = 'pcp_igd_iwf_instance'


        class PcpIgdIwfInstance(object):
            """
            UPnP IGD/PCP Interworking Function instance
            
            .. attribute:: id  <key>
            
            	the identifier of the instance
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: authentication_enabled
            
            	Indicates whether PCP authentication  is enabled
            	**type**\:  bool
            
            .. attribute:: authentication_support
            
            	Indicates whether PCP authentication is  supported
            	**type**\:  bool
            
            .. attribute:: enabled_igd_version
            
            	Configured UPnP IGD versions
            	**type**\:   :py:class:`EnabledIgdVersion <ydk.models.ietf.ietf_pcp_iwf.PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.EnabledIgdVersion>`
            
            .. attribute:: igd_version_capability
            
            	List of supported UPnP IGD versions
            	**type**\:   :py:class:`IgdVersionCapability <ydk.models.ietf.ietf_pcp_iwf.PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.IgdVersionCapability>`
            
            .. attribute:: mapping_table
            
            	PCP Mapping table
            	**type**\:   :py:class:`MappingTable <ydk.models.ietf.ietf_pcp_iwf.PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable>`
            
            .. attribute:: name
            
            	the name of the instance
            	**type**\:  str
            
            .. attribute:: pcp_igd_iwf_ip_address
            
            	local IP addresses of the UPnP IGD\-PCP IWF
            	**type**\: list of    :py:class:`PcpIgdIwfIpAddress <ydk.models.ietf.ietf_pcp_iwf.PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpIgdIwfIpAddress>`
            
            .. attribute:: pcp_server_address
            
            	List of provisioned PCP servers
            	**type**\: list of    :py:class:`PcpServerAddress <ydk.models.ietf.ietf_pcp_iwf.PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServerAddress>`
            
            .. attribute:: preferred_version
            
            	Preferred version
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: supported_version
            
            	list of supported PCP versions
            	**type**\: list of    :py:class:`SupportedVersion <ydk.models.ietf.ietf_pcp_iwf.PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.SupportedVersion>`
            
            .. attribute:: traffic_statistics
            
            	traffic statistics
            	**type**\:   :py:class:`TrafficStatistics <ydk.models.ietf.ietf_pcp_iwf.PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics>`
            
            

            """

            _prefix = 'pcp-iwf'
            _revision = '2015-08-05'

            def __init__(self):
                self.parent = None
                self.id = None
                self.authentication_enabled = None
                self.authentication_support = None
                self.enabled_igd_version = PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.EnabledIgdVersion()
                self.enabled_igd_version.parent = self
                self.igd_version_capability = PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.IgdVersionCapability()
                self.igd_version_capability.parent = self
                self.mapping_table = PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable()
                self.mapping_table.parent = self
                self.name = None
                self.pcp_igd_iwf_ip_address = YList()
                self.pcp_igd_iwf_ip_address.parent = self
                self.pcp_igd_iwf_ip_address.name = 'pcp_igd_iwf_ip_address'
                self.pcp_server_address = YList()
                self.pcp_server_address.parent = self
                self.pcp_server_address.name = 'pcp_server_address'
                self.preferred_version = None
                self.supported_version = YList()
                self.supported_version.parent = self
                self.supported_version.name = 'supported_version'
                self.traffic_statistics = PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics()
                self.traffic_statistics.parent = self


            class SupportedVersion(object):
                """
                list of supported PCP versions.
                
                .. attribute:: version  <key>
                
                	Indicates a PCP server.  Current versions are\: 0, 1, and 2
                	**type**\:  int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'pcp-iwf'
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

                    return self.parent._common_path +'/ietf-pcp-iwf:supported-version[ietf-pcp-iwf:version = ' + str(self.version) + ']'

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
                    from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                    return meta._meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.SupportedVersion']['meta_info']


            class PcpIgdIwfIpAddress(object):
                """
                local IP addresses of the UPnP IGD\-PCP IWF
                
                .. attribute:: address_id  <key>
                
                	An identifier of the address
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ip_address
                
                	An address of the UPnP IGD\-PCP IWF
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'pcp-iwf'
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

                    return self.parent._common_path +'/ietf-pcp-iwf:pcp-igd-iwf-ip-address[ietf-pcp-iwf:address-id = ' + str(self.address_id) + ']'

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
                    from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                    return meta._meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpIgdIwfIpAddress']['meta_info']


            class IgdVersionCapability(object):
                """
                List of supported UPnP IGD versions.
                
                .. attribute:: igd_version
                
                	UPnP IGD Version
                	**type**\:   :py:class:`IgdVersionEnum <ydk.models.ietf.ietf_pcp_iwf.PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.IgdVersionCapability.IgdVersionEnum>`
                
                

                """

                _prefix = 'pcp-iwf'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.igd_version = None

                class IgdVersionEnum(Enum):
                    """
                    IgdVersionEnum

                    UPnP IGD Version

                    .. data:: igd__COLON__1 = 0

                    	UPnP IGD:1

                    .. data:: igd__COLON__2 = 1

                    	UPnP IGD:2

                    .. data:: both = 2

                    	UPnP IGD:1 and UPnP IGD:2

                    """

                    igd__COLON__1 = 0

                    igd__COLON__2 = 1

                    both = 2


                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                        return meta._meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.IgdVersionCapability.IgdVersionEnum']


                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-pcp-iwf:igd-version-capability'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.igd_version is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                    return meta._meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.IgdVersionCapability']['meta_info']


            class EnabledIgdVersion(object):
                """
                Configured UPnP IGD versions
                
                .. attribute:: igd_version
                
                	UPnP IGD Version
                	**type**\:   :py:class:`IgdVersionEnum <ydk.models.ietf.ietf_pcp_iwf.PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.EnabledIgdVersion.IgdVersionEnum>`
                
                

                """

                _prefix = 'pcp-iwf'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.igd_version = None

                class IgdVersionEnum(Enum):
                    """
                    IgdVersionEnum

                    UPnP IGD Version

                    .. data:: igd__COLON__1 = 0

                    	UPnP IGD:1

                    .. data:: igd__COLON__2 = 1

                    	UPnP IGD:2

                    .. data:: both = 2

                    	UPnP IGD:1 and UPnP IGD:2

                    """

                    igd__COLON__1 = 0

                    igd__COLON__2 = 1

                    both = 2


                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                        return meta._meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.EnabledIgdVersion.IgdVersionEnum']


                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-pcp-iwf:enabled-igd-version'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.igd_version is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                    return meta._meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.EnabledIgdVersion']['meta_info']


            class PcpServerAddress(object):
                """
                List of provisioned PCP servers
                
                .. attribute:: pcp_server_id  <key>
                
                	A unique identifier
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: client_epoch
                
                	The PCP client's Epoch
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_version
                
                	The version that is selected as per the version negotiation procedure specified in Section 9 of [RFC6877]
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: external_address_familly
                
                	The address family of the external address(es) managed by the PCP server. Can be IPv4, IPv6 or both
                	**type**\:   :py:class:`IpVersionEnum <ydk.models.ietf.ietf_inet_types.IpVersionEnum>`
                
                .. attribute:: in_use
                
                	Indicates whether this in\-use instance of the server is the result of the selection process defined in [RFC7488]
                	**type**\:  bool
                
                .. attribute:: pcp_server_ip_address
                
                	a list of IP addresses of a PCP server
                	**type**\: list of    :py:class:`PcpServerIpAddress <ydk.models.ietf.ietf_pcp_iwf.PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServerAddress.PcpServerIpAddress>`
                
                .. attribute:: server_epoch
                
                	The PCP server's Epoch
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: source
                
                	source of the PCP server reachability information
                	**type**\:   :py:class:`SourceEnum <ydk.models.ietf.ietf_pcp_iwf.PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServerAddress.SourceEnum>`
                
                .. attribute:: stale_external_ip_address
                
                	A stale address that can be used by the PCP client to be assigned the same address upon reboot or other failure events
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                

                """

                _prefix = 'pcp-iwf'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.pcp_server_id = None
                    self.client_epoch = None
                    self.current_version = None
                    self.external_address_familly = None
                    self.in_use = None
                    self.pcp_server_ip_address = YList()
                    self.pcp_server_ip_address.parent = self
                    self.pcp_server_ip_address.name = 'pcp_server_ip_address'
                    self.server_epoch = None
                    self.source = None
                    self.stale_external_ip_address = None

                class SourceEnum(Enum):
                    """
                    SourceEnum

                    source of the PCP server reachability information.

                    .. data:: manual_configuration = 0

                    	The server has been manually configured.

                    .. data:: dhcpv6 = 1

                    	Retrieved from DHCPv6 [RFC7291].

                    .. data:: dhcpv4 = 2

                    	Retrieved from DHCPv4 [RFC7291].

                    .. data:: else_ = 3

                    	Else (e.g., TR-96.)

                    """

                    manual_configuration = 0

                    dhcpv6 = 1

                    dhcpv4 = 2

                    else_ = 3


                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                        return meta._meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServerAddress.SourceEnum']



                class PcpServerIpAddress(object):
                    """
                    a list of IP addresses of a PCP server
                    
                    .. attribute:: address_id  <key>
                    
                    	An identifier
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ip_address
                    
                    	An IP address of a PCP server
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'pcp-iwf'
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

                        return self.parent._common_path +'/ietf-pcp-iwf:pcp-server-ip-address[ietf-pcp-iwf:address-id = ' + str(self.address_id) + ']'

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
                        from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                        return meta._meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServerAddress.PcpServerIpAddress']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.pcp_server_id is None:
                        raise YPYModelError('Key property pcp_server_id is None')

                    return self.parent._common_path +'/ietf-pcp-iwf:pcp-server-address[ietf-pcp-iwf:pcp-server-id = ' + str(self.pcp_server_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.pcp_server_id is not None:
                        return True

                    if self.client_epoch is not None:
                        return True

                    if self.current_version is not None:
                        return True

                    if self.external_address_familly is not None:
                        return True

                    if self.in_use is not None:
                        return True

                    if self.pcp_server_ip_address is not None:
                        for child_ref in self.pcp_server_ip_address:
                            if child_ref._has_data():
                                return True

                    if self.server_epoch is not None:
                        return True

                    if self.source is not None:
                        return True

                    if self.stale_external_ip_address is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                    return meta._meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.PcpServerAddress']['meta_info']


            class MappingTable(object):
                """
                PCP Mapping table
                
                .. attribute:: mapping_entry
                
                	PCP mapping entry
                	**type**\: list of    :py:class:`MappingEntry <ydk.models.ietf.ietf_pcp_iwf.PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry>`
                
                

                """

                _prefix = 'pcp-iwf'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.mapping_entry = YList()
                    self.mapping_entry.parent = self
                    self.mapping_entry.name = 'mapping_entry'


                class MappingEntry(object):
                    """
                    PCP mapping entry.
                    
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
                    	**type**\:   :py:class:`ExternalPort <ydk.models.ietf.ietf_pcp_iwf.PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.ExternalPort>`
                    
                    .. attribute:: filter
                    
                    	a list of filters associated with the mapping
                    	**type**\: list of    :py:class:`Filter <ydk.models.ietf.ietf_pcp_iwf.PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.Filter>`
                    
                    .. attribute:: igd_control_point_address
                    
                    	The IP address of a UPnP Control Point
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: igd_control_point_port
                    
                    	The port number of a UPnP Control Point
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: internal_ip_address
                    
                    	Corresponds to the PCP Client's IP Address defined in [RFC6887]
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                    
                    .. attribute:: internal_port
                    
                    	Internal port for the mapping. Value 0 indicates 'all ports', and is legal when the lifetime is zero (a delete request), if the protocol does not use 16\-bit port numbers, or the client is requesting 'all ports'.  If the protocol is zero (meaning 'all protocols'), then internal port is set to zero
                    	**type**\:   :py:class:`InternalPort <ydk.models.ietf.ietf_pcp_iwf.PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.InternalPort>`
                    
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
                    	**type**\:   :py:class:`StatusEnum <ydk.models.ietf.ietf_pcp_iwf.PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.StatusEnum>`
                    
                    .. attribute:: status_code
                    
                    	result status code
                    	**type**\:   :py:class:`StatusCodeEnum <ydk.models.ietf.ietf_pcp_iwf.PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.StatusCodeEnum>`
                    
                    .. attribute:: third_party_address
                    
                    	used to indicate the internal IP address  when THIRD\_PARTY is in use
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                    
                    

                    """

                    _prefix = 'pcp-iwf'
                    _revision = '2015-08-05'

                    def __init__(self):
                        self.parent = None
                        self.index = None
                        self.description = None
                        self.external_ip_address = None
                        self.external_port = PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.ExternalPort()
                        self.external_port.parent = self
                        self.filter = YList()
                        self.filter.parent = self
                        self.filter.name = 'filter'
                        self.igd_control_point_address = None
                        self.igd_control_point_port = None
                        self.internal_ip_address = None
                        self.internal_port = PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.InternalPort()
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
                            from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                            return meta._meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.StatusCodeEnum']


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
                            from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                            return meta._meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.StatusEnum']



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

                        _prefix = 'pcp-iwf'
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

                            return self.parent._common_path +'/ietf-pcp-iwf:internal-port'

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
                            from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                            return meta._meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.InternalPort']['meta_info']


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

                        _prefix = 'pcp-iwf'
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

                            return self.parent._common_path +'/ietf-pcp-iwf:external-port'

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
                            from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                            return meta._meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.ExternalPort']['meta_info']


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

                        _prefix = 'pcp-iwf'
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

                            return self.parent._common_path +'/ietf-pcp-iwf:filter[ietf-pcp-iwf:filter-id = ' + str(self.filter_id) + ']'

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
                            from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                            return meta._meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry.Filter']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.index is None:
                            raise YPYModelError('Key property index is None')

                        return self.parent._common_path +'/ietf-pcp-iwf:mapping-entry[ietf-pcp-iwf:index = ' + str(self.index) + ']'

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

                        if self.igd_control_point_address is not None:
                            return True

                        if self.igd_control_point_port is not None:
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
                        from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                        return meta._meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable.MappingEntry']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-pcp-iwf:mapping-table'

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
                    from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                    return meta._meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.MappingTable']['meta_info']


            class TrafficStatistics(object):
                """
                traffic statistics
                
                .. attribute:: mapping_table
                
                	Mapping table related statistics
                	**type**\:   :py:class:`MappingTable <ydk.models.ietf.ietf_pcp_iwf.PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics.MappingTable>`
                
                .. attribute:: opcode_statistics
                
                	Opcode\-related statistics
                	**type**\:   :py:class:`OpcodeStatistics <ydk.models.ietf.ietf_pcp_iwf.PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics.OpcodeStatistics>`
                
                .. attribute:: traffic_statistics
                
                	Generic traffic statistics
                	**type**\:   :py:class:`TrafficStatistics_ <ydk.models.ietf.ietf_pcp_iwf.PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics.TrafficStatistics_>`
                
                

                """

                _prefix = 'pcp-iwf'
                _revision = '2015-08-05'

                def __init__(self):
                    self.parent = None
                    self.mapping_table = PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics.MappingTable()
                    self.mapping_table.parent = self
                    self.opcode_statistics = PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics.OpcodeStatistics()
                    self.opcode_statistics.parent = self
                    self.traffic_statistics = PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics.TrafficStatistics_()
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

                    _prefix = 'pcp-iwf'
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

                        return self.parent._common_path +'/ietf-pcp-iwf:traffic-statistics'

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
                        from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                        return meta._meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics.TrafficStatistics_']['meta_info']


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

                    _prefix = 'pcp-iwf'
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

                        return self.parent._common_path +'/ietf-pcp-iwf:opcode-statistics'

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
                        from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                        return meta._meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics.OpcodeStatistics']['meta_info']


                class MappingTable(object):
                    """
                    Mapping table related statistics
                    
                    .. attribute:: current_mt_size
                    
                    	Size of the mapping table
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: max_mt_size
                    
                    	Maximum configured size of the mapping table
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'pcp-iwf'
                    _revision = '2015-08-05'

                    def __init__(self):
                        self.parent = None
                        self.current_mt_size = None
                        self.max_mt_size = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-pcp-iwf:mapping-table'

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
                        from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                        return meta._meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics.MappingTable']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/ietf-pcp-iwf:traffic-statistics'

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

                    if self.traffic_statistics is not None and self.traffic_statistics._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                    return meta._meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance.TrafficStatistics']['meta_info']

            @property
            def _common_path(self):
                if self.id is None:
                    raise YPYModelError('Key property id is None')

                return '/ietf-pcp-iwf:pcp-iwf-state/ietf-pcp-iwf:pcp-igd-iwf-instances/ietf-pcp-iwf:pcp-igd-iwf-instance[ietf-pcp-iwf:id = ' + str(self.id) + ']'

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

                if self.enabled_igd_version is not None and self.enabled_igd_version._has_data():
                    return True

                if self.igd_version_capability is not None and self.igd_version_capability._has_data():
                    return True

                if self.mapping_table is not None and self.mapping_table._has_data():
                    return True

                if self.name is not None:
                    return True

                if self.pcp_igd_iwf_ip_address is not None:
                    for child_ref in self.pcp_igd_iwf_ip_address:
                        if child_ref._has_data():
                            return True

                if self.pcp_server_address is not None:
                    for child_ref in self.pcp_server_address:
                        if child_ref._has_data():
                            return True

                if self.preferred_version is not None:
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
                from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
                return meta._meta_table['PcpIwfState.PcpIgdIwfInstances.PcpIgdIwfInstance']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-pcp-iwf:pcp-iwf-state/ietf-pcp-iwf:pcp-igd-iwf-instances'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.pcp_igd_iwf_instance is not None:
                for child_ref in self.pcp_igd_iwf_instance:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
            return meta._meta_table['PcpIwfState.PcpIgdIwfInstances']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-pcp-iwf:pcp-iwf-state'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.pcp_igd_iwf_instances is not None and self.pcp_igd_iwf_instances._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_pcp_iwf as meta
        return meta._meta_table['PcpIwfState']['meta_info']



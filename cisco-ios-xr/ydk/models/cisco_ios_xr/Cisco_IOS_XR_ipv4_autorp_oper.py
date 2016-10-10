""" Cisco_IOS_XR_ipv4_autorp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-autorp package operational data.

This module contains definitions
for the following management objects\:
  auto\-rp\: AutoRP operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AutorpProtocolModeEnum(Enum):
    """
    AutorpProtocolModeEnum

    Autorp protocol mode

    .. data:: SPARSE = 0

    	sparse

    .. data:: BIDIRECTIONAL = 1

    	bidirectional

    """

    SPARSE = 0

    BIDIRECTIONAL = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
        return meta._meta_table['AutorpProtocolModeEnum']



class AutoRp(object):
    """
    AutoRP operational data
    
    .. attribute:: active
    
    	Active Process
    	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active>`
    
    .. attribute:: standby
    
    	Standby Process
    	**type**\:  :py:class:`Standby <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby>`
    
    

    """

    _prefix = 'ipv4-autorp-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.active = AutoRp.Active()
        self.active.parent = self
        self.standby = AutoRp.Standby()
        self.standby.parent = self


    class Standby(object):
        """
        Standby Process
        
        .. attribute:: candidate_rps
        
        	AutoRP Candidate RP Table
        	**type**\:  :py:class:`CandidateRps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.CandidateRps>`
        
        .. attribute:: mapping_agent
        
        	AutoRP Mapping Agent Table
        	**type**\:  :py:class:`MappingAgent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.MappingAgent>`
        
        

        """

        _prefix = 'ipv4-autorp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.candidate_rps = AutoRp.Standby.CandidateRps()
            self.candidate_rps.parent = self
            self.mapping_agent = AutoRp.Standby.MappingAgent()
            self.mapping_agent.parent = self


        class CandidateRps(object):
            """
            AutoRP Candidate RP Table
            
            .. attribute:: candidate_rp
            
            	AutoRP Candidate RP Entry
            	**type**\: list of  :py:class:`CandidateRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.CandidateRps.CandidateRp>`
            
            

            """

            _prefix = 'ipv4-autorp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.candidate_rp = YList()
                self.candidate_rp.parent = self
                self.candidate_rp.name = 'candidate_rp'


            class CandidateRp(object):
                """
                AutoRP Candidate RP Entry
                
                .. attribute:: access_list_name
                
                	ACL Name
                	**type**\:  str
                
                .. attribute:: announce_period
                
                	Announce Period
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: candidate_rp_address
                
                	Candidate RP IP Address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: interface_name
                
                	Interface Name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: protocol_mode
                
                	Protocol Mode
                	**type**\:  :py:class:`AutoRpProtocolModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_datatypes.AutoRpProtocolModeEnum>`
                
                .. attribute:: protocol_mode_xr
                
                	Protocol Mode
                	**type**\:  :py:class:`AutorpProtocolModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutorpProtocolModeEnum>`
                
                .. attribute:: ttl
                
                	TTL
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.access_list_name = None
                    self.announce_period = None
                    self.candidate_rp_address = None
                    self.interface_name = None
                    self.protocol_mode = None
                    self.protocol_mode_xr = None
                    self.ttl = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/Cisco-IOS-XR-ipv4-autorp-oper:standby/Cisco-IOS-XR-ipv4-autorp-oper:candidate-rps/Cisco-IOS-XR-ipv4-autorp-oper:candidate-rp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.access_list_name is not None:
                        return True

                    if self.announce_period is not None:
                        return True

                    if self.candidate_rp_address is not None:
                        return True

                    if self.interface_name is not None:
                        return True

                    if self.protocol_mode is not None:
                        return True

                    if self.protocol_mode_xr is not None:
                        return True

                    if self.ttl is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                    return meta._meta_table['AutoRp.Standby.CandidateRps.CandidateRp']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/Cisco-IOS-XR-ipv4-autorp-oper:standby/Cisco-IOS-XR-ipv4-autorp-oper:candidate-rps'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.candidate_rp is not None:
                    for child_ref in self.candidate_rp:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                return meta._meta_table['AutoRp.Standby.CandidateRps']['meta_info']


        class MappingAgent(object):
            """
            AutoRP Mapping Agent Table
            
            .. attribute:: rp_addresses
            
            	AutoRP Mapping Agent Table Entries
            	**type**\:  :py:class:`RpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.MappingAgent.RpAddresses>`
            
            .. attribute:: summary
            
            	AutoRP Mapping Agent Summary Information
            	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.MappingAgent.Summary>`
            
            

            """

            _prefix = 'ipv4-autorp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.rp_addresses = AutoRp.Standby.MappingAgent.RpAddresses()
                self.rp_addresses.parent = self
                self.summary = AutoRp.Standby.MappingAgent.Summary()
                self.summary.parent = self


            class RpAddresses(object):
                """
                AutoRP Mapping Agent Table Entries
                
                .. attribute:: rp_address
                
                	AutoRP Mapping Agent Entry
                	**type**\: list of  :py:class:`RpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.MappingAgent.RpAddresses.RpAddress>`
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.rp_address = YList()
                    self.rp_address.parent = self
                    self.rp_address.name = 'rp_address'


                class RpAddress(object):
                    """
                    AutoRP Mapping Agent Entry
                    
                    .. attribute:: rp_address  <key>
                    
                    	RP Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: expiry_time
                    
                    	Time for expiration in seconds
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: pim_version
                    
                    	PIM version of the CRP
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: range
                    
                    	Array of ranges
                    	**type**\: list of  :py:class:`Range <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Standby.MappingAgent.RpAddresses.RpAddress.Range>`
                    
                    .. attribute:: rp_address_xr
                    
                    	Candidate\-RP address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ipv4-autorp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.rp_address = None
                        self.expiry_time = None
                        self.pim_version = None
                        self.range = YList()
                        self.range.parent = self
                        self.range.name = 'range'
                        self.rp_address_xr = None


                    class Range(object):
                        """
                        Array of ranges
                        
                        .. attribute:: check_point_object_id
                        
                        	Checkpoint object id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: create_type
                        
                        	Source of the entry
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_advertised
                        
                        	Is this entry advertised ?
                        	**type**\:  bool
                        
                        .. attribute:: prefix
                        
                        	Prefix of the range
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length
                        
                        	Prefix length of the range
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: protocol_mode
                        
                        	Protocol Mode
                        	**type**\:  :py:class:`AutorpProtocolModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutorpProtocolModeEnum>`
                        
                        .. attribute:: uptime
                        
                        	Uptime in seconds
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'ipv4-autorp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.check_point_object_id = None
                            self.create_type = None
                            self.is_advertised = None
                            self.prefix = None
                            self.prefix_length = None
                            self.protocol_mode = None
                            self.uptime = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-autorp-oper:range'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.check_point_object_id is not None:
                                return True

                            if self.create_type is not None:
                                return True

                            if self.is_advertised is not None:
                                return True

                            if self.prefix is not None:
                                return True

                            if self.prefix_length is not None:
                                return True

                            if self.protocol_mode is not None:
                                return True

                            if self.uptime is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                            return meta._meta_table['AutoRp.Standby.MappingAgent.RpAddresses.RpAddress.Range']['meta_info']

                    @property
                    def _common_path(self):
                        if self.rp_address is None:
                            raise YPYModelError('Key property rp_address is None')

                        return '/Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/Cisco-IOS-XR-ipv4-autorp-oper:standby/Cisco-IOS-XR-ipv4-autorp-oper:mapping-agent/Cisco-IOS-XR-ipv4-autorp-oper:rp-addresses/Cisco-IOS-XR-ipv4-autorp-oper:rp-address[Cisco-IOS-XR-ipv4-autorp-oper:rp-address = ' + str(self.rp_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.rp_address is not None:
                            return True

                        if self.expiry_time is not None:
                            return True

                        if self.pim_version is not None:
                            return True

                        if self.range is not None:
                            for child_ref in self.range:
                                if child_ref._has_data():
                                    return True

                        if self.rp_address_xr is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                        return meta._meta_table['AutoRp.Standby.MappingAgent.RpAddresses.RpAddress']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/Cisco-IOS-XR-ipv4-autorp-oper:standby/Cisco-IOS-XR-ipv4-autorp-oper:mapping-agent/Cisco-IOS-XR-ipv4-autorp-oper:rp-addresses'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.rp_address is not None:
                        for child_ref in self.rp_address:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                    return meta._meta_table['AutoRp.Standby.MappingAgent.RpAddresses']['meta_info']


            class Summary(object):
                """
                AutoRP Mapping Agent Summary Information
                
                .. attribute:: cache_count
                
                	Number of group to RP mapping entries in the cache
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: cache_limit
                
                	Maximum group to RP mapping entries allowed
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_maximum_disabled
                
                	Is maximum enforcement disabled ?
                	**type**\:  bool
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.cache_count = None
                    self.cache_limit = None
                    self.is_maximum_disabled = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/Cisco-IOS-XR-ipv4-autorp-oper:standby/Cisco-IOS-XR-ipv4-autorp-oper:mapping-agent/Cisco-IOS-XR-ipv4-autorp-oper:summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.cache_count is not None:
                        return True

                    if self.cache_limit is not None:
                        return True

                    if self.is_maximum_disabled is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                    return meta._meta_table['AutoRp.Standby.MappingAgent.Summary']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/Cisco-IOS-XR-ipv4-autorp-oper:standby/Cisco-IOS-XR-ipv4-autorp-oper:mapping-agent'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.rp_addresses is not None and self.rp_addresses._has_data():
                    return True

                if self.summary is not None and self.summary._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                return meta._meta_table['AutoRp.Standby.MappingAgent']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/Cisco-IOS-XR-ipv4-autorp-oper:standby'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.candidate_rps is not None and self.candidate_rps._has_data():
                return True

            if self.mapping_agent is not None and self.mapping_agent._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
            return meta._meta_table['AutoRp.Standby']['meta_info']


    class Active(object):
        """
        Active Process
        
        .. attribute:: candidate_rps
        
        	AutoRP Candidate RP Table
        	**type**\:  :py:class:`CandidateRps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.CandidateRps>`
        
        .. attribute:: mapping_agent
        
        	AutoRP Mapping Agent Table
        	**type**\:  :py:class:`MappingAgent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.MappingAgent>`
        
        

        """

        _prefix = 'ipv4-autorp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.candidate_rps = AutoRp.Active.CandidateRps()
            self.candidate_rps.parent = self
            self.mapping_agent = AutoRp.Active.MappingAgent()
            self.mapping_agent.parent = self


        class CandidateRps(object):
            """
            AutoRP Candidate RP Table
            
            .. attribute:: candidate_rp
            
            	AutoRP Candidate RP Entry
            	**type**\: list of  :py:class:`CandidateRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.CandidateRps.CandidateRp>`
            
            

            """

            _prefix = 'ipv4-autorp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.candidate_rp = YList()
                self.candidate_rp.parent = self
                self.candidate_rp.name = 'candidate_rp'


            class CandidateRp(object):
                """
                AutoRP Candidate RP Entry
                
                .. attribute:: access_list_name
                
                	ACL Name
                	**type**\:  str
                
                .. attribute:: announce_period
                
                	Announce Period
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: candidate_rp_address
                
                	Candidate RP IP Address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: interface_name
                
                	Interface Name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: protocol_mode
                
                	Protocol Mode
                	**type**\:  :py:class:`AutoRpProtocolModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_datatypes.AutoRpProtocolModeEnum>`
                
                .. attribute:: protocol_mode_xr
                
                	Protocol Mode
                	**type**\:  :py:class:`AutorpProtocolModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutorpProtocolModeEnum>`
                
                .. attribute:: ttl
                
                	TTL
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.access_list_name = None
                    self.announce_period = None
                    self.candidate_rp_address = None
                    self.interface_name = None
                    self.protocol_mode = None
                    self.protocol_mode_xr = None
                    self.ttl = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/Cisco-IOS-XR-ipv4-autorp-oper:active/Cisco-IOS-XR-ipv4-autorp-oper:candidate-rps/Cisco-IOS-XR-ipv4-autorp-oper:candidate-rp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.access_list_name is not None:
                        return True

                    if self.announce_period is not None:
                        return True

                    if self.candidate_rp_address is not None:
                        return True

                    if self.interface_name is not None:
                        return True

                    if self.protocol_mode is not None:
                        return True

                    if self.protocol_mode_xr is not None:
                        return True

                    if self.ttl is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                    return meta._meta_table['AutoRp.Active.CandidateRps.CandidateRp']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/Cisco-IOS-XR-ipv4-autorp-oper:active/Cisco-IOS-XR-ipv4-autorp-oper:candidate-rps'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.candidate_rp is not None:
                    for child_ref in self.candidate_rp:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                return meta._meta_table['AutoRp.Active.CandidateRps']['meta_info']


        class MappingAgent(object):
            """
            AutoRP Mapping Agent Table
            
            .. attribute:: rp_addresses
            
            	AutoRP Mapping Agent Table Entries
            	**type**\:  :py:class:`RpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.MappingAgent.RpAddresses>`
            
            .. attribute:: summary
            
            	AutoRP Mapping Agent Summary Information
            	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.MappingAgent.Summary>`
            
            

            """

            _prefix = 'ipv4-autorp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.rp_addresses = AutoRp.Active.MappingAgent.RpAddresses()
                self.rp_addresses.parent = self
                self.summary = AutoRp.Active.MappingAgent.Summary()
                self.summary.parent = self


            class RpAddresses(object):
                """
                AutoRP Mapping Agent Table Entries
                
                .. attribute:: rp_address
                
                	AutoRP Mapping Agent Entry
                	**type**\: list of  :py:class:`RpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.MappingAgent.RpAddresses.RpAddress>`
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.rp_address = YList()
                    self.rp_address.parent = self
                    self.rp_address.name = 'rp_address'


                class RpAddress(object):
                    """
                    AutoRP Mapping Agent Entry
                    
                    .. attribute:: rp_address  <key>
                    
                    	RP Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: expiry_time
                    
                    	Time for expiration in seconds
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: pim_version
                    
                    	PIM version of the CRP
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: range
                    
                    	Array of ranges
                    	**type**\: list of  :py:class:`Range <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutoRp.Active.MappingAgent.RpAddresses.RpAddress.Range>`
                    
                    .. attribute:: rp_address_xr
                    
                    	Candidate\-RP address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ipv4-autorp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.rp_address = None
                        self.expiry_time = None
                        self.pim_version = None
                        self.range = YList()
                        self.range.parent = self
                        self.range.name = 'range'
                        self.rp_address_xr = None


                    class Range(object):
                        """
                        Array of ranges
                        
                        .. attribute:: check_point_object_id
                        
                        	Checkpoint object id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: create_type
                        
                        	Source of the entry
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_advertised
                        
                        	Is this entry advertised ?
                        	**type**\:  bool
                        
                        .. attribute:: prefix
                        
                        	Prefix of the range
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length
                        
                        	Prefix length of the range
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: protocol_mode
                        
                        	Protocol Mode
                        	**type**\:  :py:class:`AutorpProtocolModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper.AutorpProtocolModeEnum>`
                        
                        .. attribute:: uptime
                        
                        	Uptime in seconds
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'ipv4-autorp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.check_point_object_id = None
                            self.create_type = None
                            self.is_advertised = None
                            self.prefix = None
                            self.prefix_length = None
                            self.protocol_mode = None
                            self.uptime = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-autorp-oper:range'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.check_point_object_id is not None:
                                return True

                            if self.create_type is not None:
                                return True

                            if self.is_advertised is not None:
                                return True

                            if self.prefix is not None:
                                return True

                            if self.prefix_length is not None:
                                return True

                            if self.protocol_mode is not None:
                                return True

                            if self.uptime is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                            return meta._meta_table['AutoRp.Active.MappingAgent.RpAddresses.RpAddress.Range']['meta_info']

                    @property
                    def _common_path(self):
                        if self.rp_address is None:
                            raise YPYModelError('Key property rp_address is None')

                        return '/Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/Cisco-IOS-XR-ipv4-autorp-oper:active/Cisco-IOS-XR-ipv4-autorp-oper:mapping-agent/Cisco-IOS-XR-ipv4-autorp-oper:rp-addresses/Cisco-IOS-XR-ipv4-autorp-oper:rp-address[Cisco-IOS-XR-ipv4-autorp-oper:rp-address = ' + str(self.rp_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.rp_address is not None:
                            return True

                        if self.expiry_time is not None:
                            return True

                        if self.pim_version is not None:
                            return True

                        if self.range is not None:
                            for child_ref in self.range:
                                if child_ref._has_data():
                                    return True

                        if self.rp_address_xr is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                        return meta._meta_table['AutoRp.Active.MappingAgent.RpAddresses.RpAddress']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/Cisco-IOS-XR-ipv4-autorp-oper:active/Cisco-IOS-XR-ipv4-autorp-oper:mapping-agent/Cisco-IOS-XR-ipv4-autorp-oper:rp-addresses'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.rp_address is not None:
                        for child_ref in self.rp_address:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                    return meta._meta_table['AutoRp.Active.MappingAgent.RpAddresses']['meta_info']


            class Summary(object):
                """
                AutoRP Mapping Agent Summary Information
                
                .. attribute:: cache_count
                
                	Number of group to RP mapping entries in the cache
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: cache_limit
                
                	Maximum group to RP mapping entries allowed
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_maximum_disabled
                
                	Is maximum enforcement disabled ?
                	**type**\:  bool
                
                

                """

                _prefix = 'ipv4-autorp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.cache_count = None
                    self.cache_limit = None
                    self.is_maximum_disabled = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/Cisco-IOS-XR-ipv4-autorp-oper:active/Cisco-IOS-XR-ipv4-autorp-oper:mapping-agent/Cisco-IOS-XR-ipv4-autorp-oper:summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.cache_count is not None:
                        return True

                    if self.cache_limit is not None:
                        return True

                    if self.is_maximum_disabled is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                    return meta._meta_table['AutoRp.Active.MappingAgent.Summary']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/Cisco-IOS-XR-ipv4-autorp-oper:active/Cisco-IOS-XR-ipv4-autorp-oper:mapping-agent'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.rp_addresses is not None and self.rp_addresses._has_data():
                    return True

                if self.summary is not None and self.summary._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
                return meta._meta_table['AutoRp.Active.MappingAgent']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-autorp-oper:auto-rp/Cisco-IOS-XR-ipv4-autorp-oper:active'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.candidate_rps is not None and self.candidate_rps._has_data():
                return True

            if self.mapping_agent is not None and self.mapping_agent._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
            return meta._meta_table['AutoRp.Active']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-autorp-oper:auto-rp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.active is not None and self.active._has_data():
            return True

        if self.standby is not None and self.standby._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_autorp_oper as meta
        return meta._meta_table['AutoRp']['meta_info']



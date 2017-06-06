""" Cisco_IOS_XR_vservice_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR vservice package configuration.

This module contains definitions
for the following management objects\:
  vservice\: configure vservice node

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class SfcMetadataAllocEnum(Enum):
    """
    SfcMetadataAllocEnum

    Sfc metadata alloc

    .. data:: type1 = 1

    	type 1 allocation

    """

    type1 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
        return meta._meta_table['SfcMetadataAllocEnum']


class SfcMetadataDispositionActionEnum(Enum):
    """
    SfcMetadataDispositionActionEnum

    Sfc metadata disposition action

    .. data:: redirect_nexthop = 1

    	redirect nexthop action

    """

    redirect_nexthop = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
        return meta._meta_table['SfcMetadataDispositionActionEnum']


class SfcMetadataDispositionMatchEnum(Enum):
    """
    SfcMetadataDispositionMatchEnum

    Sfc metadata disposition match

    .. data:: type1_dcalloc_tenant_id = 1

    	match type 1

    """

    type1_dcalloc_tenant_id = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
        return meta._meta_table['SfcMetadataDispositionMatchEnum']


class SfcMetadataType1AllocFormatEnum(Enum):
    """
    SfcMetadataType1AllocFormatEnum

    Sfc metadata type1 alloc format

    .. data:: dc_allocation = 1

    	data center allocation

    """

    dc_allocation = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
        return meta._meta_table['SfcMetadataType1AllocFormatEnum']


class SfcSfTransportEnum(Enum):
    """
    SfcSfTransportEnum

    Sfc sf transport

    .. data:: vxlan_gpe = 1

    	vxlan-gpe transport type

    """

    vxlan_gpe = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
        return meta._meta_table['SfcSfTransportEnum']



class Vservice(object):
    """
    configure vservice node
    
    .. attribute:: metadata_dispositions
    
    	Configure metadata disposition
    	**type**\:   :py:class:`MetadataDispositions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.MetadataDispositions>`
    
    .. attribute:: metadata_templates
    
    	configure metadata imposition
    	**type**\:   :py:class:`MetadataTemplates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.MetadataTemplates>`
    
    .. attribute:: service_function_forward_locator
    
    	configure service function forward locator
    	**type**\:   :py:class:`ServiceFunctionForwardLocator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionForwardLocator>`
    
    .. attribute:: service_function_locator
    
    	configure service function locator
    	**type**\:   :py:class:`ServiceFunctionLocator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionLocator>`
    
    .. attribute:: service_function_path
    
    	service function path
    	**type**\:   :py:class:`ServiceFunctionPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath>`
    
    

    """

    _prefix = 'vservice-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.metadata_dispositions = Vservice.MetadataDispositions()
        self.metadata_dispositions.parent = self
        self.metadata_templates = Vservice.MetadataTemplates()
        self.metadata_templates.parent = self
        self.service_function_forward_locator = Vservice.ServiceFunctionForwardLocator()
        self.service_function_forward_locator.parent = self
        self.service_function_locator = Vservice.ServiceFunctionLocator()
        self.service_function_locator.parent = self
        self.service_function_path = Vservice.ServiceFunctionPath()
        self.service_function_path.parent = self


    class ServiceFunctionLocator(object):
        """
        configure service function locator
        
        .. attribute:: names
        
        	Mention the sf/sff name
        	**type**\:   :py:class:`Names <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionLocator.Names>`
        
        

        """

        _prefix = 'vservice-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.names = Vservice.ServiceFunctionLocator.Names()
            self.names.parent = self


        class Names(object):
            """
            Mention the sf/sff name
            
            .. attribute:: name
            
            	service function name
            	**type**\: list of    :py:class:`Name <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionLocator.Names.Name>`
            
            

            """

            _prefix = 'vservice-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.name = YList()
                self.name.parent = self
                self.name.name = 'name'


            class Name(object):
                """
                service function name
                
                .. attribute:: function_name  <key>
                
                	Service function/forwarder name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: locator_id  <key>
                
                	Specify locator id
                	**type**\:  int
                
                	**range:** 1..255
                
                .. attribute:: node
                
                	configure sff/sffl
                	**type**\:   :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionLocator.Names.Name.Node>`
                
                

                """

                _prefix = 'vservice-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.function_name = None
                    self.locator_id = None
                    self.node = Vservice.ServiceFunctionLocator.Names.Name.Node()
                    self.node.parent = self


                class Node(object):
                    """
                    configure sff/sffl
                    
                    .. attribute:: ipv4_destination_address
                    
                    	IPv4 destination address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4_source_address
                    
                    	IPv4 source address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: transport
                    
                    	Transport type
                    	**type**\:   :py:class:`SfcSfTransportEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.SfcSfTransportEnum>`
                    
                    .. attribute:: vni
                    
                    	VNI
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'vservice-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ipv4_destination_address = None
                        self.ipv4_source_address = None
                        self.transport = None
                        self.vni = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-vservice-cfg:node'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.ipv4_destination_address is not None:
                            return True

                        if self.ipv4_source_address is not None:
                            return True

                        if self.transport is not None:
                            return True

                        if self.vni is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
                        return meta._meta_table['Vservice.ServiceFunctionLocator.Names.Name.Node']['meta_info']

                @property
                def _common_path(self):
                    if self.function_name is None:
                        raise YPYModelError('Key property function_name is None')
                    if self.locator_id is None:
                        raise YPYModelError('Key property locator_id is None')

                    return '/Cisco-IOS-XR-vservice-cfg:vservice/Cisco-IOS-XR-vservice-cfg:service-function-locator/Cisco-IOS-XR-vservice-cfg:names/Cisco-IOS-XR-vservice-cfg:name[Cisco-IOS-XR-vservice-cfg:function-name = ' + str(self.function_name) + '][Cisco-IOS-XR-vservice-cfg:locator-id = ' + str(self.locator_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.function_name is not None:
                        return True

                    if self.locator_id is not None:
                        return True

                    if self.node is not None and self.node._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
                    return meta._meta_table['Vservice.ServiceFunctionLocator.Names.Name']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-vservice-cfg:vservice/Cisco-IOS-XR-vservice-cfg:service-function-locator/Cisco-IOS-XR-vservice-cfg:names'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    for child_ref in self.name:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
                return meta._meta_table['Vservice.ServiceFunctionLocator.Names']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-vservice-cfg:vservice/Cisco-IOS-XR-vservice-cfg:service-function-locator'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.names is not None and self.names._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
            return meta._meta_table['Vservice.ServiceFunctionLocator']['meta_info']


    class MetadataDispositions(object):
        """
        Configure metadata disposition
        
        .. attribute:: metadata_disposition
        
        	metadata disposition name
        	**type**\: list of    :py:class:`MetadataDisposition <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.MetadataDispositions.MetadataDisposition>`
        
        

        """

        _prefix = 'vservice-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.metadata_disposition = YList()
            self.metadata_disposition.parent = self
            self.metadata_disposition.name = 'metadata_disposition'


        class MetadataDisposition(object):
            """
            metadata disposition name
            
            .. attribute:: disposition_name  <key>
            
            	disposition name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: format  <key>
            
            	Specify Format
            	**type**\:   :py:class:`SfcMetadataType1AllocFormatEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.SfcMetadataType1AllocFormatEnum>`
            
            .. attribute:: match_entry
            
            	match entry name
            	**type**\: list of    :py:class:`MatchEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.MetadataDispositions.MetadataDisposition.MatchEntry>`
            
            

            """

            _prefix = 'vservice-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.disposition_name = None
                self.format = None
                self.match_entry = YList()
                self.match_entry.parent = self
                self.match_entry.name = 'match_entry'


            class MatchEntry(object):
                """
                match entry name
                
                .. attribute:: match_entry_name  <key>
                
                	match entry name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: node
                
                	configure disposition data
                	**type**\:   :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.MetadataDispositions.MetadataDisposition.MatchEntry.Node>`
                
                

                """

                _prefix = 'vservice-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.match_entry_name = None
                    self.node = Vservice.MetadataDispositions.MetadataDisposition.MatchEntry.Node()
                    self.node.parent = self


                class Node(object):
                    """
                    configure disposition data
                    
                    .. attribute:: action_type
                    
                    	action type
                    	**type**\:   :py:class:`SfcMetadataDispositionActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.SfcMetadataDispositionActionEnum>`
                    
                    .. attribute:: match_type
                    
                    	match type
                    	**type**\:   :py:class:`SfcMetadataDispositionMatchEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.SfcMetadataDispositionMatchEnum>`
                    
                    .. attribute:: nexthop_ipv4_address
                    
                    	IPv4 nexthop address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: tenant_id
                    
                    	24\-bit tenant id
                    	**type**\:  list of int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: vrf
                    
                    	VRF name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'vservice-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.action_type = None
                        self.match_type = None
                        self.nexthop_ipv4_address = None
                        self.tenant_id = YLeafList()
                        self.tenant_id.parent = self
                        self.tenant_id.name = 'tenant_id'
                        self.vrf = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-vservice-cfg:node'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.action_type is not None:
                            return True

                        if self.match_type is not None:
                            return True

                        if self.nexthop_ipv4_address is not None:
                            return True

                        if self.tenant_id is not None:
                            for child in self.tenant_id:
                                if child is not None:
                                    return True

                        if self.vrf is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
                        return meta._meta_table['Vservice.MetadataDispositions.MetadataDisposition.MatchEntry.Node']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.match_entry_name is None:
                        raise YPYModelError('Key property match_entry_name is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-vservice-cfg:match-entry[Cisco-IOS-XR-vservice-cfg:match-entry-name = ' + str(self.match_entry_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.match_entry_name is not None:
                        return True

                    if self.node is not None and self.node._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
                    return meta._meta_table['Vservice.MetadataDispositions.MetadataDisposition.MatchEntry']['meta_info']

            @property
            def _common_path(self):
                if self.disposition_name is None:
                    raise YPYModelError('Key property disposition_name is None')
                if self.format is None:
                    raise YPYModelError('Key property format is None')

                return '/Cisco-IOS-XR-vservice-cfg:vservice/Cisco-IOS-XR-vservice-cfg:metadata-dispositions/Cisco-IOS-XR-vservice-cfg:metadata-disposition[Cisco-IOS-XR-vservice-cfg:disposition-name = ' + str(self.disposition_name) + '][Cisco-IOS-XR-vservice-cfg:format = ' + str(self.format) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.disposition_name is not None:
                    return True

                if self.format is not None:
                    return True

                if self.match_entry is not None:
                    for child_ref in self.match_entry:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
                return meta._meta_table['Vservice.MetadataDispositions.MetadataDisposition']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-vservice-cfg:vservice/Cisco-IOS-XR-vservice-cfg:metadata-dispositions'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.metadata_disposition is not None:
                for child_ref in self.metadata_disposition:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
            return meta._meta_table['Vservice.MetadataDispositions']['meta_info']


    class ServiceFunctionForwardLocator(object):
        """
        configure service function forward locator
        
        .. attribute:: names
        
        	Mention the sf/sff name
        	**type**\:   :py:class:`Names <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionForwardLocator.Names>`
        
        

        """

        _prefix = 'vservice-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.names = Vservice.ServiceFunctionForwardLocator.Names()
            self.names.parent = self


        class Names(object):
            """
            Mention the sf/sff name
            
            .. attribute:: name
            
            	service function name
            	**type**\: list of    :py:class:`Name <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionForwardLocator.Names.Name>`
            
            

            """

            _prefix = 'vservice-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.name = YList()
                self.name.parent = self
                self.name.name = 'name'


            class Name(object):
                """
                service function name
                
                .. attribute:: function_name  <key>
                
                	Service function/forwarder name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: locator_id  <key>
                
                	Specify locator id
                	**type**\:  int
                
                	**range:** 1..255
                
                .. attribute:: node
                
                	configure sff/sffl
                	**type**\:   :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionForwardLocator.Names.Name.Node>`
                
                

                """

                _prefix = 'vservice-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.function_name = None
                    self.locator_id = None
                    self.node = Vservice.ServiceFunctionForwardLocator.Names.Name.Node()
                    self.node.parent = self


                class Node(object):
                    """
                    configure sff/sffl
                    
                    .. attribute:: ipv4_destination_address
                    
                    	IPv4 destination address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv4_source_address
                    
                    	IPv4 source address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: transport
                    
                    	Transport type
                    	**type**\:   :py:class:`SfcSfTransportEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.SfcSfTransportEnum>`
                    
                    .. attribute:: vni
                    
                    	VNI
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'vservice-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ipv4_destination_address = None
                        self.ipv4_source_address = None
                        self.transport = None
                        self.vni = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-vservice-cfg:node'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.ipv4_destination_address is not None:
                            return True

                        if self.ipv4_source_address is not None:
                            return True

                        if self.transport is not None:
                            return True

                        if self.vni is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
                        return meta._meta_table['Vservice.ServiceFunctionForwardLocator.Names.Name.Node']['meta_info']

                @property
                def _common_path(self):
                    if self.function_name is None:
                        raise YPYModelError('Key property function_name is None')
                    if self.locator_id is None:
                        raise YPYModelError('Key property locator_id is None')

                    return '/Cisco-IOS-XR-vservice-cfg:vservice/Cisco-IOS-XR-vservice-cfg:service-function-forward-locator/Cisco-IOS-XR-vservice-cfg:names/Cisco-IOS-XR-vservice-cfg:name[Cisco-IOS-XR-vservice-cfg:function-name = ' + str(self.function_name) + '][Cisco-IOS-XR-vservice-cfg:locator-id = ' + str(self.locator_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.function_name is not None:
                        return True

                    if self.locator_id is not None:
                        return True

                    if self.node is not None and self.node._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
                    return meta._meta_table['Vservice.ServiceFunctionForwardLocator.Names.Name']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-vservice-cfg:vservice/Cisco-IOS-XR-vservice-cfg:service-function-forward-locator/Cisco-IOS-XR-vservice-cfg:names'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    for child_ref in self.name:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
                return meta._meta_table['Vservice.ServiceFunctionForwardLocator.Names']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-vservice-cfg:vservice/Cisco-IOS-XR-vservice-cfg:service-function-forward-locator'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.names is not None and self.names._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
            return meta._meta_table['Vservice.ServiceFunctionForwardLocator']['meta_info']


    class MetadataTemplates(object):
        """
        configure metadata imposition
        
        .. attribute:: metadata_template
        
        	metadata name, type and format
        	**type**\: list of    :py:class:`MetadataTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.MetadataTemplates.MetadataTemplate>`
        
        

        """

        _prefix = 'vservice-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.metadata_template = YList()
            self.metadata_template.parent = self
            self.metadata_template.name = 'metadata_template'


        class MetadataTemplate(object):
            """
            metadata name, type and format
            
            .. attribute:: metadata_name  <key>
            
            	metadata name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: type  <key>
            
            	Specify Type 
            	**type**\:   :py:class:`SfcMetadataAllocEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.SfcMetadataAllocEnum>`
            
            .. attribute:: format  <key>
            
            	Specify Format
            	**type**\:   :py:class:`SfcMetadataType1AllocFormatEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.SfcMetadataType1AllocFormatEnum>`
            
            .. attribute:: tenant_id
            
            	Enter 24\-bit tenant id
            	**type**\:  int
            
            	**range:** 1..16777215
            
            

            """

            _prefix = 'vservice-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.metadata_name = None
                self.type = None
                self.format = None
                self.tenant_id = None

            @property
            def _common_path(self):
                if self.metadata_name is None:
                    raise YPYModelError('Key property metadata_name is None')
                if self.type is None:
                    raise YPYModelError('Key property type is None')
                if self.format is None:
                    raise YPYModelError('Key property format is None')

                return '/Cisco-IOS-XR-vservice-cfg:vservice/Cisco-IOS-XR-vservice-cfg:metadata-templates/Cisco-IOS-XR-vservice-cfg:metadata-template[Cisco-IOS-XR-vservice-cfg:metadata-name = ' + str(self.metadata_name) + '][Cisco-IOS-XR-vservice-cfg:type = ' + str(self.type) + '][Cisco-IOS-XR-vservice-cfg:format = ' + str(self.format) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.metadata_name is not None:
                    return True

                if self.type is not None:
                    return True

                if self.format is not None:
                    return True

                if self.tenant_id is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
                return meta._meta_table['Vservice.MetadataTemplates.MetadataTemplate']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-vservice-cfg:vservice/Cisco-IOS-XR-vservice-cfg:metadata-templates'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.metadata_template is not None:
                for child_ref in self.metadata_template:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
            return meta._meta_table['Vservice.MetadataTemplates']['meta_info']


    class ServiceFunctionPath(object):
        """
        service function path
        
        .. attribute:: paths
        
        	service function path id
        	**type**\:   :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath.Paths>`
        
        

        """

        _prefix = 'vservice-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.paths = Vservice.ServiceFunctionPath.Paths()
            self.paths.parent = self


        class Paths(object):
            """
            service function path id
            
            .. attribute:: path
            
            	specify the service function path id
            	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath.Paths.Path>`
            
            

            """

            _prefix = 'vservice-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.path = YList()
                self.path.parent = self
                self.path.name = 'path'


            class Path(object):
                """
                specify the service function path id
                
                .. attribute:: path_id  <key>
                
                	Specify the service function path id
                	**type**\:  int
                
                	**range:** 1..16777215
                
                .. attribute:: service_index
                
                	specify the service index
                	**type**\: list of    :py:class:`ServiceIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex>`
                
                

                """

                _prefix = 'vservice-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.path_id = None
                    self.service_index = YList()
                    self.service_index.parent = self
                    self.service_index.name = 'service_index'


                class ServiceIndex(object):
                    """
                    specify the service index
                    
                    .. attribute:: index  <key>
                    
                    	Specify the id of service function
                    	**type**\:  int
                    
                    	**range:** 1..255
                    
                    .. attribute:: sf_names
                    
                    	service function 
                    	**type**\:   :py:class:`SfNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames>`
                    
                    .. attribute:: sff_names
                    
                    	service function forwarder 
                    	**type**\:   :py:class:`SffNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames>`
                    
                    .. attribute:: terminate
                    
                    	configure terminate
                    	**type**\:   :py:class:`Terminate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate>`
                    
                    

                    """

                    _prefix = 'vservice-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.index = None
                        self.sf_names = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames()
                        self.sf_names.parent = self
                        self.sff_names = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames()
                        self.sff_names.parent = self
                        self.terminate = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate()
                        self.terminate.parent = self


                    class Terminate(object):
                        """
                        configure terminate
                        
                        .. attribute:: node
                        
                        	configure default terminate action
                        	**type**\:   :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate.Node>`
                        
                        

                        """

                        _prefix = 'vservice-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.node = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate.Node()
                            self.node.parent = self


                        class Node(object):
                            """
                            configure default terminate action
                            
                            .. attribute:: action
                            
                            	default action enum
                            	**type**\:   :py:class:`SfcMetadataDispositionActionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.SfcMetadataDispositionActionEnum>`
                            
                            .. attribute:: metatdata_disposition
                            
                            	metadata\-disposition name
                            	**type**\:  str
                            
                            .. attribute:: nexthop_ipv4_address
                            
                            	IPv4 nexthop address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf
                            
                            	nexthop vrf name
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'vservice-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.action = None
                                self.metatdata_disposition = None
                                self.nexthop_ipv4_address = None
                                self.vrf = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-vservice-cfg:node'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.action is not None:
                                    return True

                                if self.metatdata_disposition is not None:
                                    return True

                                if self.nexthop_ipv4_address is not None:
                                    return True

                                if self.vrf is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
                                return meta._meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate.Node']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-vservice-cfg:terminate'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.node is not None and self.node._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
                            return meta._meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.Terminate']['meta_info']


                    class SffNames(object):
                        """
                        service function forwarder 
                        
                        .. attribute:: sff_name
                        
                        	service function forwarder name
                        	**type**\: list of    :py:class:`SffName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName>`
                        
                        

                        """

                        _prefix = 'vservice-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sff_name = YList()
                            self.sff_name.parent = self
                            self.sff_name.name = 'sff_name'


                        class SffName(object):
                            """
                            service function forwarder name
                            
                            .. attribute:: name  <key>
                            
                            	SFF Name
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: node
                            
                            	configure SFP
                            	**type**\:   :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName.Node>`
                            
                            

                            """

                            _prefix = 'vservice-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.name = None
                                self.node = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName.Node()
                                self.node.parent = self


                            class Node(object):
                                """
                                configure SFP
                                
                                .. attribute:: enable
                                
                                	Enable Service function path
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: reserved
                                
                                	Dummy
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'vservice-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.enable = None
                                    self.reserved = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-vservice-cfg:node'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.enable is not None:
                                        return True

                                    if self.reserved is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
                                    return meta._meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName.Node']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.name is None:
                                    raise YPYModelError('Key property name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-vservice-cfg:sff-name[Cisco-IOS-XR-vservice-cfg:name = ' + str(self.name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.name is not None:
                                    return True

                                if self.node is not None and self.node._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
                                return meta._meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames.SffName']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-vservice-cfg:sff-names'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.sff_name is not None:
                                for child_ref in self.sff_name:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
                            return meta._meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SffNames']['meta_info']


                    class SfNames(object):
                        """
                        service function 
                        
                        .. attribute:: sf_name
                        
                        	service function name
                        	**type**\: list of    :py:class:`SfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName>`
                        
                        

                        """

                        _prefix = 'vservice-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sf_name = YList()
                            self.sf_name.parent = self
                            self.sf_name.name = 'sf_name'


                        class SfName(object):
                            """
                            service function name
                            
                            .. attribute:: name  <key>
                            
                            	SF Name
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: node
                            
                            	configure SFP
                            	**type**\:   :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_vservice_cfg.Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName.Node>`
                            
                            

                            """

                            _prefix = 'vservice-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.name = None
                                self.node = Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName.Node()
                                self.node.parent = self


                            class Node(object):
                                """
                                configure SFP
                                
                                .. attribute:: enable
                                
                                	Enable Service function path
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: reserved
                                
                                	Dummy
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'vservice-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.enable = None
                                    self.reserved = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-vservice-cfg:node'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.enable is not None:
                                        return True

                                    if self.reserved is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
                                    return meta._meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName.Node']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.name is None:
                                    raise YPYModelError('Key property name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-vservice-cfg:sf-name[Cisco-IOS-XR-vservice-cfg:name = ' + str(self.name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.name is not None:
                                    return True

                                if self.node is not None and self.node._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
                                return meta._meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames.SfName']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-vservice-cfg:sf-names'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.sf_name is not None:
                                for child_ref in self.sf_name:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
                            return meta._meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex.SfNames']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.index is None:
                            raise YPYModelError('Key property index is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-vservice-cfg:service-index[Cisco-IOS-XR-vservice-cfg:index = ' + str(self.index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.index is not None:
                            return True

                        if self.sf_names is not None and self.sf_names._has_data():
                            return True

                        if self.sff_names is not None and self.sff_names._has_data():
                            return True

                        if self.terminate is not None and self.terminate._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
                        return meta._meta_table['Vservice.ServiceFunctionPath.Paths.Path.ServiceIndex']['meta_info']

                @property
                def _common_path(self):
                    if self.path_id is None:
                        raise YPYModelError('Key property path_id is None')

                    return '/Cisco-IOS-XR-vservice-cfg:vservice/Cisco-IOS-XR-vservice-cfg:service-function-path/Cisco-IOS-XR-vservice-cfg:paths/Cisco-IOS-XR-vservice-cfg:path[Cisco-IOS-XR-vservice-cfg:path-id = ' + str(self.path_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.path_id is not None:
                        return True

                    if self.service_index is not None:
                        for child_ref in self.service_index:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
                    return meta._meta_table['Vservice.ServiceFunctionPath.Paths.Path']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-vservice-cfg:vservice/Cisco-IOS-XR-vservice-cfg:service-function-path/Cisco-IOS-XR-vservice-cfg:paths'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.path is not None:
                    for child_ref in self.path:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
                return meta._meta_table['Vservice.ServiceFunctionPath.Paths']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-vservice-cfg:vservice/Cisco-IOS-XR-vservice-cfg:service-function-path'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.paths is not None and self.paths._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
            return meta._meta_table['Vservice.ServiceFunctionPath']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-vservice-cfg:vservice'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.metadata_dispositions is not None and self.metadata_dispositions._has_data():
            return True

        if self.metadata_templates is not None and self.metadata_templates._has_data():
            return True

        if self.service_function_forward_locator is not None and self.service_function_forward_locator._has_data():
            return True

        if self.service_function_locator is not None and self.service_function_locator._has_data():
            return True

        if self.service_function_path is not None and self.service_function_path._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_vservice_cfg as meta
        return meta._meta_table['Vservice']['meta_info']



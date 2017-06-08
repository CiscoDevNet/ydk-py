""" ietf_qos_policy 

This module contains a collection of YANG definitions for
configuring qos specification implementations.
Copyright (c) 2014 IETF Trust and the persons identified as
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




class ActionTypeIdentity(object):
    """
    This base identity type defines action\-types
    
    

    """

    _prefix = 'policy'
    _revision = '2016-03-03'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_policy as meta
        return meta._meta_table['ActionTypeIdentity']['meta_info']


class PolicyTypeIdentity(object):
    """
    This base identity type defines policy\-types
    
    

    """

    _prefix = 'policy'
    _revision = '2016-03-03'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_policy as meta
        return meta._meta_table['PolicyTypeIdentity']['meta_info']


class Policies(object):
    """
    list of policy templates
    
    .. attribute:: policy_entry
    
    	policy template
    	**type**\: list of    :py:class:`PolicyEntry <ydk.models.ietf.ietf_qos_policy.Policies.PolicyEntry>`
    
    

    """

    _prefix = 'policy'
    _revision = '2016-03-03'

    def __init__(self):
        self.policy_entry = YList()
        self.policy_entry.parent = self
        self.policy_entry.name = 'policy_entry'


    class PolicyEntry(object):
        """
        policy template
        
        .. attribute:: policy_name  <key>
        
        	policy name
        	**type**\:  str
        
        .. attribute:: policy_type  <key>
        
        	policy type
        	**type**\:   :py:class:`PolicyTypeIdentity <ydk.models.ietf.ietf_qos_policy.PolicyTypeIdentity>`
        
        .. attribute:: classifier_entry
        
        	Classifier entry configuration in a policy
        	**type**\: list of    :py:class:`ClassifierEntry <ydk.models.ietf.ietf_qos_policy.Policies.PolicyEntry.ClassifierEntry>`
        
        .. attribute:: policy_descr
        
        	policy description
        	**type**\:  str
        
        

        """

        _prefix = 'policy'
        _revision = '2016-03-03'

        def __init__(self):
            self.parent = None
            self.policy_name = None
            self.policy_type = None
            self.classifier_entry = YList()
            self.classifier_entry.parent = self
            self.classifier_entry.name = 'classifier_entry'
            self.policy_descr = None


        class ClassifierEntry(object):
            """
            Classifier entry configuration in a policy
            
            .. attribute:: classifier_entry_name  <key>
            
            	classifier entry name
            	**type**\:  str
            
            .. attribute:: classifier_action_entry_cfg
            
            	Configuration of classifier & associated actions
            	**type**\: list of    :py:class:`ClassifierActionEntryCfg <ydk.models.ietf.ietf_qos_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg>`
            
            .. attribute:: classifier_entry_filter_oper
            
            	Filters are applicable as match\-any or match\-all filters
            	**type**\:   :py:class:`ClassifierEntryFilterOperationTypeIdentity <ydk.models.ietf.ietf_qos_classifier.ClassifierEntryFilterOperationTypeIdentity>`
            
            	**default value**\: match-all-filter
            
            .. attribute:: classifier_entry_inline
            
            	Indication of inline classifier entry
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: filter_entry
            
            	Filters configured inline in a policy
            	**type**\: list of    :py:class:`FilterEntry <ydk.models.ietf.ietf_qos_policy.Policies.PolicyEntry.ClassifierEntry.FilterEntry>`
            
            

            """

            _prefix = 'policy'
            _revision = '2016-03-03'

            def __init__(self):
                self.parent = None
                self.classifier_entry_name = None
                self.classifier_action_entry_cfg = YList()
                self.classifier_action_entry_cfg.parent = self
                self.classifier_action_entry_cfg.name = 'classifier_action_entry_cfg'
                self.classifier_entry_filter_oper = None
                self.classifier_entry_inline = None
                self.filter_entry = YList()
                self.filter_entry.parent = self
                self.filter_entry.name = 'filter_entry'


            class FilterEntry(object):
                """
                Filters configured inline in a policy
                
                .. attribute:: filter_logical_not  <key>
                
                	 This is logical\-not operator for a filter. When true, it indicates filter looks for absence of a pattern defined by the filter 
                	**type**\:  bool
                
                .. attribute:: filter_type  <key>
                
                	This leaf defines type of the filter
                	**type**\:   :py:class:`FilterTypeIdentity <ydk.models.ietf.ietf_qos_classifier.FilterTypeIdentity>`
                
                .. attribute:: destination_ip_address_cfg
                
                	list of destination ipv4 or ipv6 address
                	**type**\: list of    :py:class:`DestinationIpAddressCfg <ydk.models.ietf.ietf_qos_policy.Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationIpAddressCfg>`
                
                .. attribute:: destination_port_cfg
                
                	list of ranges of destination port
                	**type**\: list of    :py:class:`DestinationPortCfg <ydk.models.ietf.ietf_qos_policy.Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationPortCfg>`
                
                .. attribute:: dscp_cfg
                
                	list of dscp ranges
                	**type**\: list of    :py:class:`DscpCfg <ydk.models.ietf.ietf_qos_policy.Policies.PolicyEntry.ClassifierEntry.FilterEntry.DscpCfg>`
                
                .. attribute:: protocol_cfg
                
                	list of ranges of protocol values
                	**type**\: list of    :py:class:`ProtocolCfg <ydk.models.ietf.ietf_qos_policy.Policies.PolicyEntry.ClassifierEntry.FilterEntry.ProtocolCfg>`
                
                .. attribute:: source_ip_address_cfg
                
                	list of source ipv4 or ipv6 address
                	**type**\: list of    :py:class:`SourceIpAddressCfg <ydk.models.ietf.ietf_qos_policy.Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourceIpAddressCfg>`
                
                .. attribute:: source_port_cfg
                
                	list of ranges of source port
                	**type**\: list of    :py:class:`SourcePortCfg <ydk.models.ietf.ietf_qos_policy.Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourcePortCfg>`
                
                

                """

                _prefix = 'policy'
                _revision = '2016-03-03'

                def __init__(self):
                    self.parent = None
                    self.filter_logical_not = None
                    self.filter_type = None
                    self.destination_ip_address_cfg = YList()
                    self.destination_ip_address_cfg.parent = self
                    self.destination_ip_address_cfg.name = 'destination_ip_address_cfg'
                    self.destination_port_cfg = YList()
                    self.destination_port_cfg.parent = self
                    self.destination_port_cfg.name = 'destination_port_cfg'
                    self.dscp_cfg = YList()
                    self.dscp_cfg.parent = self
                    self.dscp_cfg.name = 'dscp_cfg'
                    self.protocol_cfg = YList()
                    self.protocol_cfg.parent = self
                    self.protocol_cfg.name = 'protocol_cfg'
                    self.source_ip_address_cfg = YList()
                    self.source_ip_address_cfg.parent = self
                    self.source_ip_address_cfg.name = 'source_ip_address_cfg'
                    self.source_port_cfg = YList()
                    self.source_port_cfg.parent = self
                    self.source_port_cfg.name = 'source_port_cfg'


                class DscpCfg(object):
                    """
                    list of dscp ranges
                    
                    .. attribute:: dscp_max  <key>
                    
                    	maximum value of dscp min\-max range
                    	**type**\:  int
                    
                    	**range:** 0..63
                    
                    .. attribute:: dscp_min  <key>
                    
                    	Minimum value of dscp min\-max range
                    	**type**\:  int
                    
                    	**range:** 0..63
                    
                    

                    """

                    _prefix = 'diffserv'
                    _revision = '2016-06-15'

                    def __init__(self):
                        self.parent = None
                        self.dscp_max = None
                        self.dscp_min = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.dscp_max is None:
                            raise YPYModelError('Key property dscp_max is None')
                        if self.dscp_min is None:
                            raise YPYModelError('Key property dscp_min is None')

                        return self.parent._common_path +'/ietf-diffserv:dscp-cfg[ietf-diffserv:dscp-max = ' + str(self.dscp_max) + '][ietf-diffserv:dscp-min = ' + str(self.dscp_min) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.dscp_max is not None:
                            return True

                        if self.dscp_min is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_qos_policy as meta
                        return meta._meta_table['Policies.PolicyEntry.ClassifierEntry.FilterEntry.DscpCfg']['meta_info']


                class SourceIpAddressCfg(object):
                    """
                    list of source ipv4 or ipv6 address
                    
                    .. attribute:: source_ip_addr  <key>
                    
                    	source ipv4 or ipv6 prefix
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                    
                    
                    ----
                    

                    """

                    _prefix = 'diffserv'
                    _revision = '2016-06-15'

                    def __init__(self):
                        self.parent = None
                        self.source_ip_addr = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.source_ip_addr is None:
                            raise YPYModelError('Key property source_ip_addr is None')

                        return self.parent._common_path +'/ietf-diffserv:source-ip-address-cfg[ietf-diffserv:source-ip-addr = ' + str(self.source_ip_addr) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.source_ip_addr is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_qos_policy as meta
                        return meta._meta_table['Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourceIpAddressCfg']['meta_info']


                class DestinationIpAddressCfg(object):
                    """
                    list of destination ipv4 or ipv6 address
                    
                    .. attribute:: destination_ip_addr  <key>
                    
                    	destination ipv4 or ipv6 prefix
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                    
                    
                    ----
                    

                    """

                    _prefix = 'diffserv'
                    _revision = '2016-06-15'

                    def __init__(self):
                        self.parent = None
                        self.destination_ip_addr = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.destination_ip_addr is None:
                            raise YPYModelError('Key property destination_ip_addr is None')

                        return self.parent._common_path +'/ietf-diffserv:destination-ip-address-cfg[ietf-diffserv:destination-ip-addr = ' + str(self.destination_ip_addr) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.destination_ip_addr is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_qos_policy as meta
                        return meta._meta_table['Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationIpAddressCfg']['meta_info']


                class SourcePortCfg(object):
                    """
                    list of ranges of source port
                    
                    .. attribute:: source_port_max  <key>
                    
                    	maximum value of source port range
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: source_port_min  <key>
                    
                    	minimum value of source port range
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'diffserv'
                    _revision = '2016-06-15'

                    def __init__(self):
                        self.parent = None
                        self.source_port_max = None
                        self.source_port_min = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.source_port_max is None:
                            raise YPYModelError('Key property source_port_max is None')
                        if self.source_port_min is None:
                            raise YPYModelError('Key property source_port_min is None')

                        return self.parent._common_path +'/ietf-diffserv:source-port-cfg[ietf-diffserv:source-port-max = ' + str(self.source_port_max) + '][ietf-diffserv:source-port-min = ' + str(self.source_port_min) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.source_port_max is not None:
                            return True

                        if self.source_port_min is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_qos_policy as meta
                        return meta._meta_table['Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourcePortCfg']['meta_info']


                class DestinationPortCfg(object):
                    """
                    list of ranges of destination port
                    
                    .. attribute:: destination_port_max  <key>
                    
                    	maximum value of destination port range
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: destination_port_min  <key>
                    
                    	minimum value of destination port range
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'diffserv'
                    _revision = '2016-06-15'

                    def __init__(self):
                        self.parent = None
                        self.destination_port_max = None
                        self.destination_port_min = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.destination_port_max is None:
                            raise YPYModelError('Key property destination_port_max is None')
                        if self.destination_port_min is None:
                            raise YPYModelError('Key property destination_port_min is None')

                        return self.parent._common_path +'/ietf-diffserv:destination-port-cfg[ietf-diffserv:destination-port-max = ' + str(self.destination_port_max) + '][ietf-diffserv:destination-port-min = ' + str(self.destination_port_min) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.destination_port_max is not None:
                            return True

                        if self.destination_port_min is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_qos_policy as meta
                        return meta._meta_table['Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationPortCfg']['meta_info']


                class ProtocolCfg(object):
                    """
                    list of ranges of protocol values
                    
                    .. attribute:: protocol_max  <key>
                    
                    	maximum value of protocol range
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: protocol_min  <key>
                    
                    	minimum value of protocol range
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'diffserv'
                    _revision = '2016-06-15'

                    def __init__(self):
                        self.parent = None
                        self.protocol_max = None
                        self.protocol_min = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.protocol_max is None:
                            raise YPYModelError('Key property protocol_max is None')
                        if self.protocol_min is None:
                            raise YPYModelError('Key property protocol_min is None')

                        return self.parent._common_path +'/ietf-diffserv:protocol-cfg[ietf-diffserv:protocol-max = ' + str(self.protocol_max) + '][ietf-diffserv:protocol-min = ' + str(self.protocol_min) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.protocol_max is not None:
                            return True

                        if self.protocol_min is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_qos_policy as meta
                        return meta._meta_table['Policies.PolicyEntry.ClassifierEntry.FilterEntry.ProtocolCfg']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.filter_logical_not is None:
                        raise YPYModelError('Key property filter_logical_not is None')
                    if self.filter_type is None:
                        raise YPYModelError('Key property filter_type is None')

                    return self.parent._common_path +'/ietf-qos-policy:filter-entry[ietf-qos-policy:filter-logical-not = ' + str(self.filter_logical_not) + '][ietf-qos-policy:filter-type = ' + str(self.filter_type) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.filter_logical_not is not None:
                        return True

                    if self.filter_type is not None:
                        return True

                    if self.destination_ip_address_cfg is not None:
                        for child_ref in self.destination_ip_address_cfg:
                            if child_ref._has_data():
                                return True

                    if self.destination_port_cfg is not None:
                        for child_ref in self.destination_port_cfg:
                            if child_ref._has_data():
                                return True

                    if self.dscp_cfg is not None:
                        for child_ref in self.dscp_cfg:
                            if child_ref._has_data():
                                return True

                    if self.protocol_cfg is not None:
                        for child_ref in self.protocol_cfg:
                            if child_ref._has_data():
                                return True

                    if self.source_ip_address_cfg is not None:
                        for child_ref in self.source_ip_address_cfg:
                            if child_ref._has_data():
                                return True

                    if self.source_port_cfg is not None:
                        for child_ref in self.source_port_cfg:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_qos_policy as meta
                    return meta._meta_table['Policies.PolicyEntry.ClassifierEntry.FilterEntry']['meta_info']


            class ClassifierActionEntryCfg(object):
                """
                Configuration of classifier & associated actions
                
                .. attribute:: action_type  <key>
                
                	This defines action type 
                	**type**\:   :py:class:`ActionTypeIdentity <ydk.models.ietf.ietf_qos_policy.ActionTypeIdentity>`
                
                .. attribute:: dscp_cfg
                
                	dscp marking container
                	**type**\:   :py:class:`DscpCfg <ydk.models.ietf.ietf_qos_policy.Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.DscpCfg>`
                
                

                """

                _prefix = 'policy'
                _revision = '2016-03-03'

                def __init__(self):
                    self.parent = None
                    self.action_type = None
                    self.dscp_cfg = Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.DscpCfg()
                    self.dscp_cfg.parent = self


                class DscpCfg(object):
                    """
                    dscp marking container
                    
                    .. attribute:: dscp
                    
                    	dscp marking
                    	**type**\:  int
                    
                    	**range:** 0..63
                    
                    

                    """

                    _prefix = 'diffserv'
                    _revision = '2016-06-15'

                    def __init__(self):
                        self.parent = None
                        self.dscp = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-diffserv:dscp-cfg'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.dscp is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_qos_policy as meta
                        return meta._meta_table['Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg.DscpCfg']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.action_type is None:
                        raise YPYModelError('Key property action_type is None')

                    return self.parent._common_path +'/ietf-qos-policy:classifier-action-entry-cfg[ietf-qos-policy:action-type = ' + str(self.action_type) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.action_type is not None:
                        return True

                    if self.dscp_cfg is not None and self.dscp_cfg._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_qos_policy as meta
                    return meta._meta_table['Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')
                if self.classifier_entry_name is None:
                    raise YPYModelError('Key property classifier_entry_name is None')

                return self.parent._common_path +'/ietf-qos-policy:classifier-entry[ietf-qos-policy:classifier-entry-name = ' + str(self.classifier_entry_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.classifier_entry_name is not None:
                    return True

                if self.classifier_action_entry_cfg is not None:
                    for child_ref in self.classifier_action_entry_cfg:
                        if child_ref._has_data():
                            return True

                if self.classifier_entry_filter_oper is not None:
                    return True

                if self.classifier_entry_inline is not None:
                    return True

                if self.filter_entry is not None:
                    for child_ref in self.filter_entry:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_qos_policy as meta
                return meta._meta_table['Policies.PolicyEntry.ClassifierEntry']['meta_info']

        @property
        def _common_path(self):
            if self.policy_name is None:
                raise YPYModelError('Key property policy_name is None')
            if self.policy_type is None:
                raise YPYModelError('Key property policy_type is None')

            return '/ietf-qos-policy:policies/ietf-qos-policy:policy-entry[ietf-qos-policy:policy-name = ' + str(self.policy_name) + '][ietf-qos-policy:policy-type = ' + str(self.policy_type) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.policy_name is not None:
                return True

            if self.policy_type is not None:
                return True

            if self.classifier_entry is not None:
                for child_ref in self.classifier_entry:
                    if child_ref._has_data():
                        return True

            if self.policy_descr is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_qos_policy as meta
            return meta._meta_table['Policies.PolicyEntry']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-qos-policy:policies'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.policy_entry is not None:
            for child_ref in self.policy_entry:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_qos_policy as meta
        return meta._meta_table['Policies']['meta_info']



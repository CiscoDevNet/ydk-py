""" ietf_diffserv_classifier 

This module contains a collection of YANG definitions for
configuring diffserv specification implementations.

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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class FilterType(Identity):
    """
     This is identity of base filter\-type
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(FilterType, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:filter-type")


class ClassifierEntryFilterOperationType(Identity):
    """
    Classifier entry filter logical operation
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(ClassifierEntryFilterOperationType, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:classifier-entry-filter-operation-type")


class Classifiers(Entity):
    """
    list of classifier entry
    
    .. attribute:: classifier_entry
    
    	classifier entry template
    	**type**\: list of  		 :py:class:`ClassifierEntry <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry>`
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(Classifiers, self).__init__()
        self._top_entity = None

        self.yang_name = "classifiers"
        self.yang_parent_name = "ietf-diffserv-classifier"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("classifier-entry", ("classifier_entry", Classifiers.ClassifierEntry))])
        self._leafs = OrderedDict()

        self.classifier_entry = YList(self)
        self._segment_path = lambda: "ietf-diffserv-classifier:classifiers"

    def __setattr__(self, name, value):
        self._perform_setattr(Classifiers, [], name, value)


    class ClassifierEntry(Entity):
        """
        classifier entry template
        
        .. attribute:: classifier_entry_name  (key)
        
        	Diffserv classifier name
        	**type**\: str
        
        .. attribute:: classifier_entry_descr
        
        	Description of the class template
        	**type**\: str
        
        .. attribute:: classifier_entry_filter_operation
        
        	Filters are applicable as any or all filters
        	**type**\:  :py:class:`ClassifierEntryFilterOperationType <ydk.models.ietf.ietf_diffserv_classifier.ClassifierEntryFilterOperationType>`
        
        	**default value**\: match-any-filter
        
        .. attribute:: filter_entry
        
        	Filter configuration
        	**type**\: list of  		 :py:class:`FilterEntry <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry>`
        
        

        """

        _prefix = 'classifier'
        _revision = '2015-04-07'

        def __init__(self):
            super(Classifiers.ClassifierEntry, self).__init__()

            self.yang_name = "classifier-entry"
            self.yang_parent_name = "classifiers"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['classifier_entry_name']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("filter-entry", ("filter_entry", Classifiers.ClassifierEntry.FilterEntry))])
            self._leafs = OrderedDict([
                ('classifier_entry_name', YLeaf(YType.str, 'classifier-entry-name')),
                ('classifier_entry_descr', YLeaf(YType.str, 'classifier-entry-descr')),
                ('classifier_entry_filter_operation', YLeaf(YType.identityref, 'classifier-entry-filter-operation')),
            ])
            self.classifier_entry_name = None
            self.classifier_entry_descr = None
            self.classifier_entry_filter_operation = None

            self.filter_entry = YList(self)
            self._segment_path = lambda: "classifier-entry" + "[classifier-entry-name='" + str(self.classifier_entry_name) + "']"
            self._absolute_path = lambda: "ietf-diffserv-classifier:classifiers/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Classifiers.ClassifierEntry, ['classifier_entry_name', 'classifier_entry_descr', 'classifier_entry_filter_operation'], name, value)


        class FilterEntry(Entity):
            """
            Filter configuration
            
            .. attribute:: filter_type  (key)
            
            	This leaf defines type of the filter
            	**type**\:  :py:class:`FilterType <ydk.models.ietf.ietf_diffserv_classifier.FilterType>`
            
            .. attribute:: filter_logical_not  (key)
            
            	 This is logical\-not operator for a filter. When true, it  indicates filter looks for absence of a pattern defined  by the filter 
            	**type**\: bool
            
            .. attribute:: dscp_cfg
            
            	list of dscp ranges
            	**type**\: list of  		 :py:class:`DscpCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.DscpCfg>`
            
            .. attribute:: source_ip_address_cfg
            
            	list of source ip address
            	**type**\: list of  		 :py:class:`SourceIpAddressCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.SourceIpAddressCfg>`
            
            .. attribute:: destination_ip_address_cfg
            
            	list of destination ip address
            	**type**\: list of  		 :py:class:`DestinationIpAddressCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.DestinationIpAddressCfg>`
            
            .. attribute:: source_port_cfg
            
            	list of ranges of source port
            	**type**\: list of  		 :py:class:`SourcePortCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.SourcePortCfg>`
            
            .. attribute:: destination_port_cfg
            
            	list of ranges of destination port
            	**type**\: list of  		 :py:class:`DestinationPortCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.DestinationPortCfg>`
            
            .. attribute:: protocol_cfg
            
            	list of ranges of protocol values
            	**type**\: list of  		 :py:class:`ProtocolCfg <ydk.models.ietf.ietf_diffserv_classifier.Classifiers.ClassifierEntry.FilterEntry.ProtocolCfg>`
            
            

            """

            _prefix = 'classifier'
            _revision = '2015-04-07'

            def __init__(self):
                super(Classifiers.ClassifierEntry.FilterEntry, self).__init__()

                self.yang_name = "filter-entry"
                self.yang_parent_name = "classifier-entry"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['filter_type','filter_logical_not']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("dscp-cfg", ("dscp_cfg", Classifiers.ClassifierEntry.FilterEntry.DscpCfg)), ("source-ip-address-cfg", ("source_ip_address_cfg", Classifiers.ClassifierEntry.FilterEntry.SourceIpAddressCfg)), ("destination-ip-address-cfg", ("destination_ip_address_cfg", Classifiers.ClassifierEntry.FilterEntry.DestinationIpAddressCfg)), ("source-port-cfg", ("source_port_cfg", Classifiers.ClassifierEntry.FilterEntry.SourcePortCfg)), ("destination-port-cfg", ("destination_port_cfg", Classifiers.ClassifierEntry.FilterEntry.DestinationPortCfg)), ("protocol-cfg", ("protocol_cfg", Classifiers.ClassifierEntry.FilterEntry.ProtocolCfg))])
                self._leafs = OrderedDict([
                    ('filter_type', YLeaf(YType.identityref, 'filter-type')),
                    ('filter_logical_not', YLeaf(YType.boolean, 'filter-logical-not')),
                ])
                self.filter_type = None
                self.filter_logical_not = None

                self.dscp_cfg = YList(self)
                self.source_ip_address_cfg = YList(self)
                self.destination_ip_address_cfg = YList(self)
                self.source_port_cfg = YList(self)
                self.destination_port_cfg = YList(self)
                self.protocol_cfg = YList(self)
                self._segment_path = lambda: "filter-entry" + "[filter-type='" + str(self.filter_type) + "']" + "[filter-logical-not='" + str(self.filter_logical_not) + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(Classifiers.ClassifierEntry.FilterEntry, ['filter_type', 'filter_logical_not'], name, value)


            class DscpCfg(Entity):
                """
                list of dscp ranges
                
                .. attribute:: dscp_min  (key)
                
                	Minimum value of dscp range
                	**type**\: int
                
                	**range:** 0..63
                
                .. attribute:: dscp_max  (key)
                
                	maximum value of dscp range
                	**type**\: int
                
                	**range:** 0..63
                
                

                """

                _prefix = 'classifier'
                _revision = '2015-04-07'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.DscpCfg, self).__init__()

                    self.yang_name = "dscp-cfg"
                    self.yang_parent_name = "filter-entry"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['dscp_min','dscp_max']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('dscp_min', YLeaf(YType.uint8, 'dscp-min')),
                        ('dscp_max', YLeaf(YType.uint8, 'dscp-max')),
                    ])
                    self.dscp_min = None
                    self.dscp_max = None
                    self._segment_path = lambda: "dscp-cfg" + "[dscp-min='" + str(self.dscp_min) + "']" + "[dscp-max='" + str(self.dscp_max) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Classifiers.ClassifierEntry.FilterEntry.DscpCfg, ['dscp_min', 'dscp_max'], name, value)


            class SourceIpAddressCfg(Entity):
                """
                list of source ip address
                
                .. attribute:: source_ip_addr  (key)
                
                	source ip prefix
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                

                """

                _prefix = 'classifier'
                _revision = '2015-04-07'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.SourceIpAddressCfg, self).__init__()

                    self.yang_name = "source-ip-address-cfg"
                    self.yang_parent_name = "filter-entry"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['source_ip_addr']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('source_ip_addr', YLeaf(YType.str, 'source-ip-addr')),
                    ])
                    self.source_ip_addr = None
                    self._segment_path = lambda: "source-ip-address-cfg" + "[source-ip-addr='" + str(self.source_ip_addr) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Classifiers.ClassifierEntry.FilterEntry.SourceIpAddressCfg, ['source_ip_addr'], name, value)


            class DestinationIpAddressCfg(Entity):
                """
                list of destination ip address
                
                .. attribute:: destination_ip_addr  (key)
                
                	destination ip prefix
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                

                """

                _prefix = 'classifier'
                _revision = '2015-04-07'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.DestinationIpAddressCfg, self).__init__()

                    self.yang_name = "destination-ip-address-cfg"
                    self.yang_parent_name = "filter-entry"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['destination_ip_addr']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('destination_ip_addr', YLeaf(YType.str, 'destination-ip-addr')),
                    ])
                    self.destination_ip_addr = None
                    self._segment_path = lambda: "destination-ip-address-cfg" + "[destination-ip-addr='" + str(self.destination_ip_addr) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Classifiers.ClassifierEntry.FilterEntry.DestinationIpAddressCfg, ['destination_ip_addr'], name, value)


            class SourcePortCfg(Entity):
                """
                list of ranges of source port
                
                .. attribute:: source_port_min  (key)
                
                	minimum value of source port range
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: source_port_max  (key)
                
                	maximum value of source port range
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'classifier'
                _revision = '2015-04-07'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.SourcePortCfg, self).__init__()

                    self.yang_name = "source-port-cfg"
                    self.yang_parent_name = "filter-entry"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['source_port_min','source_port_max']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('source_port_min', YLeaf(YType.uint16, 'source-port-min')),
                        ('source_port_max', YLeaf(YType.uint16, 'source-port-max')),
                    ])
                    self.source_port_min = None
                    self.source_port_max = None
                    self._segment_path = lambda: "source-port-cfg" + "[source-port-min='" + str(self.source_port_min) + "']" + "[source-port-max='" + str(self.source_port_max) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Classifiers.ClassifierEntry.FilterEntry.SourcePortCfg, ['source_port_min', 'source_port_max'], name, value)


            class DestinationPortCfg(Entity):
                """
                list of ranges of destination port
                
                .. attribute:: destination_port_min  (key)
                
                	minimum value of destination port range
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: destination_port_max  (key)
                
                	maximum value of destination port range
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'classifier'
                _revision = '2015-04-07'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.DestinationPortCfg, self).__init__()

                    self.yang_name = "destination-port-cfg"
                    self.yang_parent_name = "filter-entry"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['destination_port_min','destination_port_max']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('destination_port_min', YLeaf(YType.uint16, 'destination-port-min')),
                        ('destination_port_max', YLeaf(YType.uint16, 'destination-port-max')),
                    ])
                    self.destination_port_min = None
                    self.destination_port_max = None
                    self._segment_path = lambda: "destination-port-cfg" + "[destination-port-min='" + str(self.destination_port_min) + "']" + "[destination-port-max='" + str(self.destination_port_max) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Classifiers.ClassifierEntry.FilterEntry.DestinationPortCfg, ['destination_port_min', 'destination_port_max'], name, value)


            class ProtocolCfg(Entity):
                """
                list of ranges of protocol values
                
                .. attribute:: protocol_min  (key)
                
                	minimum value of protocol range
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: protocol_max  (key)
                
                	maximum value of protocol range
                	**type**\: int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'classifier'
                _revision = '2015-04-07'

                def __init__(self):
                    super(Classifiers.ClassifierEntry.FilterEntry.ProtocolCfg, self).__init__()

                    self.yang_name = "protocol-cfg"
                    self.yang_parent_name = "filter-entry"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['protocol_min','protocol_max']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('protocol_min', YLeaf(YType.uint8, 'protocol-min')),
                        ('protocol_max', YLeaf(YType.uint8, 'protocol-max')),
                    ])
                    self.protocol_min = None
                    self.protocol_max = None
                    self._segment_path = lambda: "protocol-cfg" + "[protocol-min='" + str(self.protocol_min) + "']" + "[protocol-max='" + str(self.protocol_max) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Classifiers.ClassifierEntry.FilterEntry.ProtocolCfg, ['protocol_min', 'protocol_max'], name, value)

    def clone_ptr(self):
        self._top_entity = Classifiers()
        return self._top_entity

class Dscp(Identity):
    """
    DSCP filter\-type
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(Dscp, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:dscp")


class SourceIpAddress(Identity):
    """
    source\-ip\-address filter\-type
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(SourceIpAddress, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:source-ip-address")


class DestinationIpAddress(Identity):
    """
    destination\-ip\-address filter\-type
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(DestinationIpAddress, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:destination-ip-address")


class SourcePort(Identity):
    """
    source\-port filter\-type
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(SourcePort, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:source-port")


class DestinationPort(Identity):
    """
    destination\-port filter\-type
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(DestinationPort, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:destination-port")


class Protocol(Identity):
    """
    protocol filter\-type
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(Protocol, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:protocol")


class MatchAnyFilter(Identity):
    """
    Classifier entry filter logical OR operation
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(MatchAnyFilter, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:match-any-filter")


class MatchAllFilter(Identity):
    """
    Classifier entry filter logical AND operation
    
    

    """

    _prefix = 'classifier'
    _revision = '2015-04-07'

    def __init__(self):
        super(MatchAllFilter, self).__init__("urn:ietf:params:xml:ns:yang:ietf-diffserv-classifier", "ietf-diffserv-classifier", "ietf-diffserv-classifier:match-all-filter")



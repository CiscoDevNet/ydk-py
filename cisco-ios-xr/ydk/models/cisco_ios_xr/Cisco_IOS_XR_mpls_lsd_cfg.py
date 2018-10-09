""" Cisco_IOS_XR_mpls_lsd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-lsd package configuration.

This module contains definitions
for the following management objects\:
  mpls\-lsd\: MPLS LSD configuration data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MplsIpTtlPropagateDisable(Enum):
    """
    MplsIpTtlPropagateDisable (Enum Class)

    Mpls ip ttl propagate disable

    .. data:: all = 0

    	Disable IP TTL propagation for all MPLS packets

    .. data:: forward = 1

    	Disable IP TTL propagation for only forwarded

    	MPLS packets

    .. data:: local = 2

    	Disable IP TTL propagation for only locally

    	generated MPLS packets

    """

    all = Enum.YLeaf(0, "all")

    forward = Enum.YLeaf(1, "forward")

    local = Enum.YLeaf(2, "local")



class MplsLsd(Entity):
    """
    MPLS LSD configuration data
    
    .. attribute:: ipv6
    
    	Configure IPv6 parameters
    	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg.MplsLsd.Ipv6>`
    
    .. attribute:: ipv4
    
    	Configure IPv4 parameters
    	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg.MplsLsd.Ipv4>`
    
    .. attribute:: label_databases
    
    	Table of label databases
    	**type**\:  :py:class:`LabelDatabases <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg.MplsLsd.LabelDatabases>`
    
    .. attribute:: ltrace_multiplier
    
    	Multiply the MPLS LSD Ltrace buffer length
    	**type**\: int
    
    	**range:** 2..5
    
    .. attribute:: app_reg_delay_disable
    
    	Disable LSD application reg delay
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: mpls_entropy_label
    
    	Enable MPLS Entropy Label
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: mpls_ip_ttl_propagate_disable
    
    	Disable Propagation of IP TTL onto the label stack
    	**type**\:  :py:class:`MplsIpTtlPropagateDisable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg.MplsIpTtlPropagateDisable>`
    
    

    """

    _prefix = 'mpls-lsd-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(MplsLsd, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls-lsd"
        self.yang_parent_name = "Cisco-IOS-XR-mpls-lsd-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ipv6", ("ipv6", MplsLsd.Ipv6)), ("ipv4", ("ipv4", MplsLsd.Ipv4)), ("label-databases", ("label_databases", MplsLsd.LabelDatabases))])
        self._leafs = OrderedDict([
            ('ltrace_multiplier', (YLeaf(YType.uint32, 'ltrace-multiplier'), ['int'])),
            ('app_reg_delay_disable', (YLeaf(YType.empty, 'app-reg-delay-disable'), ['Empty'])),
            ('mpls_entropy_label', (YLeaf(YType.empty, 'mpls-entropy-label'), ['Empty'])),
            ('mpls_ip_ttl_propagate_disable', (YLeaf(YType.enumeration, 'mpls-ip-ttl-propagate-disable'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg', 'MplsIpTtlPropagateDisable', '')])),
        ])
        self.ltrace_multiplier = None
        self.app_reg_delay_disable = None
        self.mpls_entropy_label = None
        self.mpls_ip_ttl_propagate_disable = None

        self.ipv6 = MplsLsd.Ipv6()
        self.ipv6.parent = self
        self._children_name_map["ipv6"] = "ipv6"

        self.ipv4 = MplsLsd.Ipv4()
        self.ipv4.parent = self
        self._children_name_map["ipv4"] = "ipv4"

        self.label_databases = MplsLsd.LabelDatabases()
        self.label_databases.parent = self
        self._children_name_map["label_databases"] = "label-databases"
        self._segment_path = lambda: "Cisco-IOS-XR-mpls-lsd-cfg:mpls-lsd"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(MplsLsd, ['ltrace_multiplier', 'app_reg_delay_disable', 'mpls_entropy_label', 'mpls_ip_ttl_propagate_disable'], name, value)


    class Ipv6(Entity):
        """
        Configure IPv6 parameters
        
        .. attribute:: ttl_expiration_pop
        
        	Number of labels to pop upon MPLS IP TTL expiry
        	**type**\: int
        
        	**range:** 1..10
        
        

        """

        _prefix = 'mpls-lsd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(MplsLsd.Ipv6, self).__init__()

            self.yang_name = "ipv6"
            self.yang_parent_name = "mpls-lsd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ttl_expiration_pop', (YLeaf(YType.uint32, 'ttl-expiration-pop'), ['int'])),
            ])
            self.ttl_expiration_pop = None
            self._segment_path = lambda: "ipv6"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-lsd-cfg:mpls-lsd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MplsLsd.Ipv6, ['ttl_expiration_pop'], name, value)


    class Ipv4(Entity):
        """
        Configure IPv4 parameters
        
        .. attribute:: ttl_expiration_pop
        
        	Number of labels to pop upon MPLS IP TTL expiry
        	**type**\: int
        
        	**range:** 1..10
        
        

        """

        _prefix = 'mpls-lsd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(MplsLsd.Ipv4, self).__init__()

            self.yang_name = "ipv4"
            self.yang_parent_name = "mpls-lsd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ttl_expiration_pop', (YLeaf(YType.uint32, 'ttl-expiration-pop'), ['int'])),
            ])
            self.ttl_expiration_pop = None
            self._segment_path = lambda: "ipv4"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-lsd-cfg:mpls-lsd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MplsLsd.Ipv4, ['ttl_expiration_pop'], name, value)


    class LabelDatabases(Entity):
        """
        Table of label databases
        
        .. attribute:: label_database
        
        	A label database
        	**type**\: list of  		 :py:class:`LabelDatabase <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg.MplsLsd.LabelDatabases.LabelDatabase>`
        
        

        """

        _prefix = 'mpls-lsd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(MplsLsd.LabelDatabases, self).__init__()

            self.yang_name = "label-databases"
            self.yang_parent_name = "mpls-lsd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("label-database", ("label_database", MplsLsd.LabelDatabases.LabelDatabase))])
            self._leafs = OrderedDict()

            self.label_database = YList(self)
            self._segment_path = lambda: "label-databases"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-lsd-cfg:mpls-lsd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MplsLsd.LabelDatabases, [], name, value)


        class LabelDatabase(Entity):
            """
            A label database
            
            .. attribute:: label_database_id  (key)
            
            	Label database identifier
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: label_range
            
            	Label range
            	**type**\:  :py:class:`LabelRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg.MplsLsd.LabelDatabases.LabelDatabase.LabelRange>`
            
            

            """

            _prefix = 'mpls-lsd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsLsd.LabelDatabases.LabelDatabase, self).__init__()

                self.yang_name = "label-database"
                self.yang_parent_name = "label-databases"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['label_database_id']
                self._child_classes = OrderedDict([("label-range", ("label_range", MplsLsd.LabelDatabases.LabelDatabase.LabelRange))])
                self._leafs = OrderedDict([
                    ('label_database_id', (YLeaf(YType.uint32, 'label-database-id'), ['int'])),
                ])
                self.label_database_id = None

                self.label_range = MplsLsd.LabelDatabases.LabelDatabase.LabelRange()
                self.label_range.parent = self
                self._children_name_map["label_range"] = "label-range"
                self._segment_path = lambda: "label-database" + "[label-database-id='" + str(self.label_database_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-lsd-cfg:mpls-lsd/label-databases/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLsd.LabelDatabases.LabelDatabase, ['label_database_id'], name, value)


            class LabelRange(Entity):
                """
                Label range
                
                .. attribute:: minvalue
                
                	Minimum label value
                	**type**\: int
                
                	**range:** 16000..1048575
                
                .. attribute:: max_value
                
                	Maximum label value
                	**type**\: int
                
                	**range:** 16000..1048575
                
                .. attribute:: min_static_value
                
                	Minimum static label value
                	**type**\: int
                
                	**range:** 0..1048575
                
                .. attribute:: max_static_value
                
                	Maximum static label value
                	**type**\: int
                
                	**range:** 0..1048575
                
                

                """

                _prefix = 'mpls-lsd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsLsd.LabelDatabases.LabelDatabase.LabelRange, self).__init__()

                    self.yang_name = "label-range"
                    self.yang_parent_name = "label-database"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('minvalue', (YLeaf(YType.uint32, 'minvalue'), ['int'])),
                        ('max_value', (YLeaf(YType.uint32, 'max-value'), ['int'])),
                        ('min_static_value', (YLeaf(YType.uint32, 'min-static-value'), ['int'])),
                        ('max_static_value', (YLeaf(YType.uint32, 'max-static-value'), ['int'])),
                    ])
                    self.minvalue = None
                    self.max_value = None
                    self.min_static_value = None
                    self.max_static_value = None
                    self._segment_path = lambda: "label-range"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLsd.LabelDatabases.LabelDatabase.LabelRange, ['minvalue', 'max_value', 'min_static_value', 'max_static_value'], name, value)

    def clone_ptr(self):
        self._top_entity = MplsLsd()
        return self._top_entity


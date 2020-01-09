""" Cisco_IOS_XR_mpls_lsd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-lsd package configuration.

This module contains definitions
for the following management objects\:
  mpls\-lsd\: MPLS LSD configuration data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class LabelBlock(Enum):
    """
    LabelBlock (Enum Class)

    Label block

    .. data:: cbf = 3

    	CBF block

    """

    cbf = Enum.YLeaf(3, "cbf")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_lsd_cfg as meta
        return meta._meta_table['LabelBlock']


class LabelRange(Enum):
    """
    LabelRange (Enum Class)

    Label range

    .. data:: lower_upper = 0

    	Start and end of block

    .. data:: lower_size = 1

    	Start and size of block

    """

    lower_upper = Enum.YLeaf(0, "lower-upper")

    lower_size = Enum.YLeaf(1, "lower-size")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_lsd_cfg as meta
        return meta._meta_table['LabelRange']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_lsd_cfg as meta
        return meta._meta_table['MplsIpTtlPropagateDisable']



class MplsLsd(_Entity_):
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
    _revision = '2019-08-20'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
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


    class Ipv6(_Entity_):
        """
        Configure IPv6 parameters
        
        .. attribute:: ttl_expiration_pop
        
        	Number of labels to pop upon MPLS IP TTL expiry
        	**type**\: int
        
        	**range:** 1..10
        
        

        """

        _prefix = 'mpls-lsd-cfg'
        _revision = '2019-08-20'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_lsd_cfg as meta
            return meta._meta_table['MplsLsd.Ipv6']['meta_info']


    class Ipv4(_Entity_):
        """
        Configure IPv4 parameters
        
        .. attribute:: ttl_expiration_pop
        
        	Number of labels to pop upon MPLS IP TTL expiry
        	**type**\: int
        
        	**range:** 1..10
        
        

        """

        _prefix = 'mpls-lsd-cfg'
        _revision = '2019-08-20'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_lsd_cfg as meta
            return meta._meta_table['MplsLsd.Ipv4']['meta_info']


    class LabelDatabases(_Entity_):
        """
        Table of label databases
        
        .. attribute:: label_database
        
        	A label database
        	**type**\: list of  		 :py:class:`LabelDatabase <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg.MplsLsd.LabelDatabases.LabelDatabase>`
        
        

        """

        _prefix = 'mpls-lsd-cfg'
        _revision = '2019-08-20'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
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


        class LabelDatabase(_Entity_):
            """
            A label database
            
            .. attribute:: label_database_id  (key)
            
            	Label database identifier
            	**type**\: int
            
            	**range:** 0..0
            
            .. attribute:: label_range
            
            	Label range
            	**type**\:  :py:class:`LabelRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg.MplsLsd.LabelDatabases.LabelDatabase.LabelRange>`
            
            .. attribute:: label_blocks
            
            	A label blocks database
            	**type**\:  :py:class:`LabelBlocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg.MplsLsd.LabelDatabases.LabelDatabase.LabelBlocks>`
            
            

            """

            _prefix = 'mpls-lsd-cfg'
            _revision = '2019-08-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(MplsLsd.LabelDatabases.LabelDatabase, self).__init__()

                self.yang_name = "label-database"
                self.yang_parent_name = "label-databases"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['label_database_id']
                self._child_classes = OrderedDict([("label-range", ("label_range", MplsLsd.LabelDatabases.LabelDatabase.LabelRange)), ("label-blocks", ("label_blocks", MplsLsd.LabelDatabases.LabelDatabase.LabelBlocks))])
                self._leafs = OrderedDict([
                    ('label_database_id', (YLeaf(YType.uint32, 'label-database-id'), ['int'])),
                ])
                self.label_database_id = None

                self.label_range = MplsLsd.LabelDatabases.LabelDatabase.LabelRange()
                self.label_range.parent = self
                self._children_name_map["label_range"] = "label-range"

                self.label_blocks = MplsLsd.LabelDatabases.LabelDatabase.LabelBlocks()
                self.label_blocks.parent = self
                self._children_name_map["label_blocks"] = "label-blocks"
                self._segment_path = lambda: "label-database" + "[label-database-id='" + str(self.label_database_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-lsd-cfg:mpls-lsd/label-databases/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLsd.LabelDatabases.LabelDatabase, ['label_database_id'], name, value)


            class LabelRange(_Entity_):
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
                _revision = '2019-08-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
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

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_lsd_cfg as meta
                    return meta._meta_table['MplsLsd.LabelDatabases.LabelDatabase.LabelRange']['meta_info']


            class LabelBlocks(_Entity_):
                """
                A label blocks database
                
                .. attribute:: label_block
                
                	Label block
                	**type**\: list of  		 :py:class:`LabelBlock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg.MplsLsd.LabelDatabases.LabelDatabase.LabelBlocks.LabelBlock>`
                
                

                """

                _prefix = 'mpls-lsd-cfg'
                _revision = '2019-08-20'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(MplsLsd.LabelDatabases.LabelDatabase.LabelBlocks, self).__init__()

                    self.yang_name = "label-blocks"
                    self.yang_parent_name = "label-database"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("label-block", ("label_block", MplsLsd.LabelDatabases.LabelDatabase.LabelBlocks.LabelBlock))])
                    self._leafs = OrderedDict()

                    self.label_block = YList(self)
                    self._segment_path = lambda: "label-blocks"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLsd.LabelDatabases.LabelDatabase.LabelBlocks, [], name, value)


                class LabelBlock(_Entity_):
                    """
                    Label block
                    
                    .. attribute:: block_name  (key)
                    
                    	Label block identifier
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: block_type
                    
                    	Label block type
                    	**type**\:  :py:class:`LabelBlock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg.LabelBlock>`
                    
                    	**default value**\: cbf
                    
                    .. attribute:: range_type
                    
                    	Label range type
                    	**type**\:  :py:class:`LabelRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg.LabelRange>`
                    
                    	**default value**\: lower-upper
                    
                    .. attribute:: lower_bound
                    
                    	Lower bound of block
                    	**type**\: int
                    
                    	**range:** 16000..1048575
                    
                    	**default value**\: 16000
                    
                    .. attribute:: upper_bound
                    
                    	Upper bound of block
                    	**type**\: int
                    
                    	**range:** 16000..1048575
                    
                    	**default value**\: 16000
                    
                    .. attribute:: block_size
                    
                    	Size of block
                    	**type**\: int
                    
                    	**range:** 1..1032576
                    
                    	**default value**\: 1
                    
                    .. attribute:: client_instance_name
                    
                    	Client instance name
                    	**type**\: str
                    
                    	**length:** 1..48
                    
                    	**default value**\: any
                    
                    

                    """

                    _prefix = 'mpls-lsd-cfg'
                    _revision = '2019-08-20'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(MplsLsd.LabelDatabases.LabelDatabase.LabelBlocks.LabelBlock, self).__init__()

                        self.yang_name = "label-block"
                        self.yang_parent_name = "label-blocks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['block_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('block_name', (YLeaf(YType.str, 'block-name'), ['str'])),
                            ('block_type', (YLeaf(YType.enumeration, 'block-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg', 'LabelBlock', '')])),
                            ('range_type', (YLeaf(YType.enumeration, 'range-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_lsd_cfg', 'LabelRange', '')])),
                            ('lower_bound', (YLeaf(YType.uint32, 'lower-bound'), ['int'])),
                            ('upper_bound', (YLeaf(YType.uint32, 'upper-bound'), ['int'])),
                            ('block_size', (YLeaf(YType.uint32, 'block-size'), ['int'])),
                            ('client_instance_name', (YLeaf(YType.str, 'client-instance-name'), ['str'])),
                        ])
                        self.block_name = None
                        self.block_type = None
                        self.range_type = None
                        self.lower_bound = None
                        self.upper_bound = None
                        self.block_size = None
                        self.client_instance_name = None
                        self._segment_path = lambda: "label-block" + "[block-name='" + str(self.block_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLsd.LabelDatabases.LabelDatabase.LabelBlocks.LabelBlock, ['block_name', 'block_type', 'range_type', 'lower_bound', 'upper_bound', 'block_size', 'client_instance_name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_lsd_cfg as meta
                        return meta._meta_table['MplsLsd.LabelDatabases.LabelDatabase.LabelBlocks.LabelBlock']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_lsd_cfg as meta
                    return meta._meta_table['MplsLsd.LabelDatabases.LabelDatabase.LabelBlocks']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_lsd_cfg as meta
                return meta._meta_table['MplsLsd.LabelDatabases.LabelDatabase']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_lsd_cfg as meta
            return meta._meta_table['MplsLsd.LabelDatabases']['meta_info']

    def clone_ptr(self):
        self._top_entity = MplsLsd()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_lsd_cfg as meta
        return meta._meta_table['MplsLsd']['meta_info']



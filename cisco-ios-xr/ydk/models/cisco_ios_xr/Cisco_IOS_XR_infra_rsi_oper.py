""" Cisco_IOS_XR_infra_rsi_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-rsi package operational data.

This module contains definitions
for the following management objects\:
  vrf\-group\: VRF group operational data
  srlg\: srlg
  selective\-vrf\-download\: selective vrf download

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



class Priority(Enum):
    """
    Priority (Enum Class)

    Priority

    .. data:: critical = 0

    	Critical

    .. data:: high = 1

    	High

    .. data:: medium = 2

    	Medium

    .. data:: low = 3

    	Low

    .. data:: very_low = 4

    	Very low

    .. data:: invald = 5

    	Invalid

    """

    critical = Enum.YLeaf(0, "critical")

    high = Enum.YLeaf(1, "high")

    medium = Enum.YLeaf(2, "medium")

    low = Enum.YLeaf(3, "low")

    very_low = Enum.YLeaf(4, "very-low")

    invald = Enum.YLeaf(5, "invald")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
        return meta._meta_table['Priority']


class Source(Enum):
    """
    Source (Enum Class)

    Source

    .. data:: configured = 1

    	Configured

    .. data:: from_group = 2

    	From group

    .. data:: inherited = 4

    	Inherited

    .. data:: from_optical = 8

    	From optical

    .. data:: configured_and_notified = 17

    	Configured and notified

    .. data:: from_group_and_notified = 18

    	From group and notified

    .. data:: inherited_and_notified = 20

    	Inherited and notified

    .. data:: from_optical_and_notified = 24

    	From optical and notified

    """

    configured = Enum.YLeaf(1, "configured")

    from_group = Enum.YLeaf(2, "from-group")

    inherited = Enum.YLeaf(4, "inherited")

    from_optical = Enum.YLeaf(8, "from-optical")

    configured_and_notified = Enum.YLeaf(17, "configured-and-notified")

    from_group_and_notified = Enum.YLeaf(18, "from-group-and-notified")

    inherited_and_notified = Enum.YLeaf(20, "inherited-and-notified")

    from_optical_and_notified = Enum.YLeaf(24, "from-optical-and-notified")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
        return meta._meta_table['Source']



class VrfGroup(_Entity_):
    """
    VRF group operational data
    
    .. attribute:: nodes
    
    	Node operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.VrfGroup.Nodes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'infra-rsi-oper'
    _revision = '2017-09-07'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(VrfGroup, self).__init__()
        self._top_entity = None

        self.yang_name = "vrf-group"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", VrfGroup.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = VrfGroup.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:vrf-group"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(VrfGroup, [], name, value)


    class Nodes(_Entity_):
        """
        Node operational data
        
        .. attribute:: node
        
        	Node details
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.VrfGroup.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(VrfGroup.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "vrf-group"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", VrfGroup.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:vrf-group/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(VrfGroup.Nodes, [], name, value)


        class Node(_Entity_):
            """
            Node details
            
            .. attribute:: node_name  (key)
            
            	Node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: groups
            
            	Group operational data
            	**type**\:  :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.VrfGroup.Nodes.Node.Groups>`
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-rsi-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(VrfGroup.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("groups", ("groups", VrfGroup.Nodes.Node.Groups))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.groups = VrfGroup.Nodes.Node.Groups()
                self.groups.parent = self
                self._children_name_map["groups"] = "groups"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:vrf-group/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(VrfGroup.Nodes.Node, ['node_name'], name, value)


            class Groups(_Entity_):
                """
                Group operational data
                
                .. attribute:: group
                
                	Group details
                	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.VrfGroup.Nodes.Node.Groups.Group>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(VrfGroup.Nodes.Node.Groups, self).__init__()

                    self.yang_name = "groups"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("group", ("group", VrfGroup.Nodes.Node.Groups.Group))])
                    self._leafs = OrderedDict()

                    self.group = YList(self)
                    self._segment_path = lambda: "groups"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(VrfGroup.Nodes.Node.Groups, [], name, value)


                class Group(_Entity_):
                    """
                    Group details
                    
                    .. attribute:: group_name  (key)
                    
                    	Group name
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    	**config**\: False
                    
                    .. attribute:: vr_fs
                    
                    	Number of VRFs in this VRF group
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: forward_reference
                    
                    	VRF group not present but used
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: vrf
                    
                    	VRF group's VRF
                    	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.VrfGroup.Nodes.Node.Groups.Group.Vrf>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(VrfGroup.Nodes.Node.Groups.Group, self).__init__()

                        self.yang_name = "group"
                        self.yang_parent_name = "groups"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['group_name']
                        self._child_classes = OrderedDict([("vrf", ("vrf", VrfGroup.Nodes.Node.Groups.Group.Vrf))])
                        self._leafs = OrderedDict([
                            ('group_name', (YLeaf(YType.str, 'group-name'), ['str'])),
                            ('vr_fs', (YLeaf(YType.uint32, 'vr-fs'), ['int'])),
                            ('forward_reference', (YLeaf(YType.boolean, 'forward-reference'), ['bool'])),
                        ])
                        self.group_name = None
                        self.vr_fs = None
                        self.forward_reference = None

                        self.vrf = YList(self)
                        self._segment_path = lambda: "group" + "[group-name='" + str(self.group_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(VrfGroup.Nodes.Node.Groups.Group, ['group_name', 'vr_fs', 'forward_reference'], name, value)


                    class Vrf(_Entity_):
                        """
                        VRF group's VRF
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-rsi-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(VrfGroup.Nodes.Node.Groups.Group.Vrf, self).__init__()

                            self.yang_name = "vrf"
                            self.yang_parent_name = "group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ])
                            self.vrf_name = None
                            self._segment_path = lambda: "vrf"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(VrfGroup.Nodes.Node.Groups.Group.Vrf, ['vrf_name'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                            return meta._meta_table['VrfGroup.Nodes.Node.Groups.Group.Vrf']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                        return meta._meta_table['VrfGroup.Nodes.Node.Groups.Group']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                    return meta._meta_table['VrfGroup.Nodes.Node.Groups']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                return meta._meta_table['VrfGroup.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
            return meta._meta_table['VrfGroup.Nodes']['meta_info']

    def clone_ptr(self):
        self._top_entity = VrfGroup()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
        return meta._meta_table['VrfGroup']['meta_info']


class Srlg(_Entity_):
    """
    srlg
    
    .. attribute:: groups
    
    	Set of Groups configured for SRLG
    	**type**\:  :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Groups>`
    
    	**config**\: False
    
    .. attribute:: interfaces
    
    	Set of interfaces configured for SRLG
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Interfaces>`
    
    	**config**\: False
    
    .. attribute:: rsips
    
    	Set of rsip configured for SRLG
    	**type**\:  :py:class:`Rsips <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Rsips>`
    
    	**config**\: False
    
    .. attribute:: srlg_maps
    
    	Set of SRLG name, value maps configured
    	**type**\:  :py:class:`SrlgMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.SrlgMaps>`
    
    	**config**\: False
    
    .. attribute:: nodes
    
    	RSI SRLG operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes>`
    
    	**config**\: False
    
    .. attribute:: interface_srlg_names
    
    	Set of SRLG names configured
    	**type**\:  :py:class:`InterfaceSrlgNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.InterfaceSrlgNames>`
    
    	**config**\: False
    
    .. attribute:: inherit_nodes
    
    	Set of inherit locations configured for SRLG
    	**type**\:  :py:class:`InheritNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.InheritNodes>`
    
    	**config**\: False
    
    .. attribute:: srlg_values
    
    	Set of SRLG values configured
    	**type**\:  :py:class:`SrlgValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.SrlgValues>`
    
    	**config**\: False
    
    .. attribute:: interface_details
    
    	Set of interfaces configured for SRLG
    	**type**\:  :py:class:`InterfaceDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.InterfaceDetails>`
    
    	**config**\: False
    
    

    """

    _prefix = 'infra-rsi-oper'
    _revision = '2017-09-07'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Srlg, self).__init__()
        self._top_entity = None

        self.yang_name = "srlg"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("groups", ("groups", Srlg.Groups)), ("interfaces", ("interfaces", Srlg.Interfaces)), ("rsips", ("rsips", Srlg.Rsips)), ("srlg-maps", ("srlg_maps", Srlg.SrlgMaps)), ("nodes", ("nodes", Srlg.Nodes)), ("interface-srlg-names", ("interface_srlg_names", Srlg.InterfaceSrlgNames)), ("inherit-nodes", ("inherit_nodes", Srlg.InheritNodes)), ("srlg-values", ("srlg_values", Srlg.SrlgValues)), ("interface-details", ("interface_details", Srlg.InterfaceDetails))])
        self._leafs = OrderedDict()

        self.groups = Srlg.Groups()
        self.groups.parent = self
        self._children_name_map["groups"] = "groups"

        self.interfaces = Srlg.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"

        self.rsips = Srlg.Rsips()
        self.rsips.parent = self
        self._children_name_map["rsips"] = "rsips"

        self.srlg_maps = Srlg.SrlgMaps()
        self.srlg_maps.parent = self
        self._children_name_map["srlg_maps"] = "srlg-maps"

        self.nodes = Srlg.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"

        self.interface_srlg_names = Srlg.InterfaceSrlgNames()
        self.interface_srlg_names.parent = self
        self._children_name_map["interface_srlg_names"] = "interface-srlg-names"

        self.inherit_nodes = Srlg.InheritNodes()
        self.inherit_nodes.parent = self
        self._children_name_map["inherit_nodes"] = "inherit-nodes"

        self.srlg_values = Srlg.SrlgValues()
        self.srlg_values.parent = self
        self._children_name_map["srlg_values"] = "srlg-values"

        self.interface_details = Srlg.InterfaceDetails()
        self.interface_details.parent = self
        self._children_name_map["interface_details"] = "interface-details"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Srlg, [], name, value)


    class Groups(_Entity_):
        """
        Set of Groups configured for SRLG
        
        .. attribute:: group
        
        	SRLG group details
        	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Groups.Group>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Srlg.Groups, self).__init__()

            self.yang_name = "groups"
            self.yang_parent_name = "srlg"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("group", ("group", Srlg.Groups.Group))])
            self._leafs = OrderedDict()

            self.group = YList(self)
            self._segment_path = lambda: "groups"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Srlg.Groups, [], name, value)


        class Group(_Entity_):
            """
            SRLG group details
            
            .. attribute:: group_name  (key)
            
            	Group name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            	**config**\: False
            
            .. attribute:: group_name_xr
            
            	Group name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: group_values
            
            	Group values
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: srlg_attribute
            
            	SRLG attribute
            	**type**\: list of  		 :py:class:`SrlgAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Groups.Group.SrlgAttribute>`
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-rsi-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Srlg.Groups.Group, self).__init__()

                self.yang_name = "group"
                self.yang_parent_name = "groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['group_name']
                self._child_classes = OrderedDict([("srlg-attribute", ("srlg_attribute", Srlg.Groups.Group.SrlgAttribute))])
                self._leafs = OrderedDict([
                    ('group_name', (YLeaf(YType.str, 'group-name'), ['str'])),
                    ('group_name_xr', (YLeaf(YType.str, 'group-name-xr'), ['str'])),
                    ('group_values', (YLeaf(YType.uint32, 'group-values'), ['int'])),
                ])
                self.group_name = None
                self.group_name_xr = None
                self.group_values = None

                self.srlg_attribute = YList(self)
                self._segment_path = lambda: "group" + "[group-name='" + str(self.group_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/groups/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srlg.Groups.Group, ['group_name', 'group_name_xr', 'group_values'], name, value)


            class SrlgAttribute(_Entity_):
                """
                SRLG attribute
                
                .. attribute:: srlg_value
                
                	SRLG value
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: priority
                
                	Priority
                	**type**\:  :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Priority>`
                
                	**config**\: False
                
                .. attribute:: srlg_index
                
                	Index
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srlg.Groups.Group.SrlgAttribute, self).__init__()

                    self.yang_name = "srlg-attribute"
                    self.yang_parent_name = "group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('srlg_value', (YLeaf(YType.uint32, 'srlg-value'), ['int'])),
                        ('priority', (YLeaf(YType.enumeration, 'priority'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Priority', '')])),
                        ('srlg_index', (YLeaf(YType.uint16, 'srlg-index'), ['int'])),
                    ])
                    self.srlg_value = None
                    self.priority = None
                    self.srlg_index = None
                    self._segment_path = lambda: "srlg-attribute"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Groups.Group.SrlgAttribute, ['srlg_value', 'priority', 'srlg_index'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                    return meta._meta_table['Srlg.Groups.Group.SrlgAttribute']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                return meta._meta_table['Srlg.Groups.Group']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
            return meta._meta_table['Srlg.Groups']['meta_info']


    class Interfaces(_Entity_):
        """
        Set of interfaces configured for SRLG
        
        .. attribute:: interface
        
        	SRLG interface summary
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Interfaces.Interface>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Srlg.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "srlg"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface", ("interface", Srlg.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Srlg.Interfaces, [], name, value)


        class Interface(_Entity_):
            """
            SRLG interface summary
            
            .. attribute:: interface_name  (key)
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            	**config**\: False
            
            .. attribute:: interface_name_xr
            
            	Interface name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: value_count
            
            	Values
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: registrations
            
            	Registrations
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: srlg_value
            
            	SRLG values
            	**type**\: list of int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-rsi-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Srlg.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('interface_name_xr', (YLeaf(YType.str, 'interface-name-xr'), ['str'])),
                    ('value_count', (YLeaf(YType.uint32, 'value-count'), ['int'])),
                    ('registrations', (YLeaf(YType.uint32, 'registrations'), ['int'])),
                    ('srlg_value', (YLeafList(YType.uint32, 'srlg-value'), ['int'])),
                ])
                self.interface_name = None
                self.interface_name_xr = None
                self.value_count = None
                self.registrations = None
                self.srlg_value = []
                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srlg.Interfaces.Interface, ['interface_name', 'interface_name_xr', 'value_count', 'registrations', 'srlg_value'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                return meta._meta_table['Srlg.Interfaces.Interface']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
            return meta._meta_table['Srlg.Interfaces']['meta_info']


    class Rsips(_Entity_):
        """
        Set of rsip configured for SRLG
        
        .. attribute:: rsip
        
        	SRLG rsip details
        	**type**\: list of  		 :py:class:`Rsip <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Rsips.Rsip>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Srlg.Rsips, self).__init__()

            self.yang_name = "rsips"
            self.yang_parent_name = "srlg"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rsip", ("rsip", Srlg.Rsips.Rsip))])
            self._leafs = OrderedDict()

            self.rsip = YList(self)
            self._segment_path = lambda: "rsips"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Srlg.Rsips, [], name, value)


        class Rsip(_Entity_):
            """
            SRLG rsip details
            
            .. attribute:: rsip_name  (key)
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            	**config**\: False
            
            .. attribute:: optical_layer_interface_name
            
            	Optical layer interface name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: registrations
            
            	Registrations
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: interface_values
            
            	Interface values
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: srlg_attribute
            
            	SRLG attribute
            	**type**\: list of  		 :py:class:`SrlgAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Rsips.Rsip.SrlgAttribute>`
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-rsi-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Srlg.Rsips.Rsip, self).__init__()

                self.yang_name = "rsip"
                self.yang_parent_name = "rsips"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rsip_name']
                self._child_classes = OrderedDict([("srlg-attribute", ("srlg_attribute", Srlg.Rsips.Rsip.SrlgAttribute))])
                self._leafs = OrderedDict([
                    ('rsip_name', (YLeaf(YType.str, 'rsip-name'), ['str'])),
                    ('optical_layer_interface_name', (YLeaf(YType.str, 'optical-layer-interface-name'), ['str'])),
                    ('registrations', (YLeaf(YType.uint32, 'registrations'), ['int'])),
                    ('interface_values', (YLeaf(YType.uint32, 'interface-values'), ['int'])),
                ])
                self.rsip_name = None
                self.optical_layer_interface_name = None
                self.registrations = None
                self.interface_values = None

                self.srlg_attribute = YList(self)
                self._segment_path = lambda: "rsip" + "[rsip-name='" + str(self.rsip_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/rsips/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srlg.Rsips.Rsip, ['rsip_name', 'optical_layer_interface_name', 'registrations', 'interface_values'], name, value)


            class SrlgAttribute(_Entity_):
                """
                SRLG attribute
                
                .. attribute:: srlg_value
                
                	SRLG value
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: priority
                
                	Priority
                	**type**\:  :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Priority>`
                
                	**config**\: False
                
                .. attribute:: srlg_index
                
                	Index
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srlg.Rsips.Rsip.SrlgAttribute, self).__init__()

                    self.yang_name = "srlg-attribute"
                    self.yang_parent_name = "rsip"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('srlg_value', (YLeaf(YType.uint32, 'srlg-value'), ['int'])),
                        ('priority', (YLeaf(YType.enumeration, 'priority'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Priority', '')])),
                        ('srlg_index', (YLeaf(YType.uint16, 'srlg-index'), ['int'])),
                    ])
                    self.srlg_value = None
                    self.priority = None
                    self.srlg_index = None
                    self._segment_path = lambda: "srlg-attribute"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Rsips.Rsip.SrlgAttribute, ['srlg_value', 'priority', 'srlg_index'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                    return meta._meta_table['Srlg.Rsips.Rsip.SrlgAttribute']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                return meta._meta_table['Srlg.Rsips.Rsip']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
            return meta._meta_table['Srlg.Rsips']['meta_info']


    class SrlgMaps(_Entity_):
        """
        Set of SRLG name, value maps configured
        
        .. attribute:: srlg_map
        
        	Configured SRLG name details 
        	**type**\: list of  		 :py:class:`SrlgMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.SrlgMaps.SrlgMap>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Srlg.SrlgMaps, self).__init__()

            self.yang_name = "srlg-maps"
            self.yang_parent_name = "srlg"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("srlg-map", ("srlg_map", Srlg.SrlgMaps.SrlgMap))])
            self._leafs = OrderedDict()

            self.srlg_map = YList(self)
            self._segment_path = lambda: "srlg-maps"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Srlg.SrlgMaps, [], name, value)


        class SrlgMap(_Entity_):
            """
            Configured SRLG name details 
            
            .. attribute:: srlg_name  (key)
            
            	SRLG name
            	**type**\: str
            
            	**length:** 1..64
            
            	**config**\: False
            
            .. attribute:: srlg_value
            
            	SRLG value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: srlg_name_xr
            
            	SRLG name
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-rsi-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Srlg.SrlgMaps.SrlgMap, self).__init__()

                self.yang_name = "srlg-map"
                self.yang_parent_name = "srlg-maps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['srlg_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('srlg_name', (YLeaf(YType.str, 'srlg-name'), ['str'])),
                    ('srlg_value', (YLeaf(YType.uint32, 'srlg-value'), ['int'])),
                    ('srlg_name_xr', (YLeaf(YType.str, 'srlg-name-xr'), ['str'])),
                ])
                self.srlg_name = None
                self.srlg_value = None
                self.srlg_name_xr = None
                self._segment_path = lambda: "srlg-map" + "[srlg-name='" + str(self.srlg_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/srlg-maps/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srlg.SrlgMaps.SrlgMap, ['srlg_name', 'srlg_value', 'srlg_name_xr'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                return meta._meta_table['Srlg.SrlgMaps.SrlgMap']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
            return meta._meta_table['Srlg.SrlgMaps']['meta_info']


    class Nodes(_Entity_):
        """
        RSI SRLG operational data
        
        .. attribute:: node
        
        	RSI SRLG operational data
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Srlg.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "srlg"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Srlg.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Srlg.Nodes, [], name, value)


        class Node(_Entity_):
            """
            RSI SRLG operational data
            
            .. attribute:: node_name  (key)
            
            	Node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: srlg_maps
            
            	Set of SRLG name, value maps configured
            	**type**\:  :py:class:`SrlgMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.SrlgMaps>`
            
            	**config**\: False
            
            .. attribute:: groups
            
            	Set of Groups configured for SRLG
            	**type**\:  :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.Groups>`
            
            	**config**\: False
            
            .. attribute:: inherit_nodes
            
            	Set of inherit locations configured for SRLG
            	**type**\:  :py:class:`InheritNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InheritNodes>`
            
            	**config**\: False
            
            .. attribute:: interfaces
            
            	Set of interfaces configured for SRLG
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.Interfaces>`
            
            	**config**\: False
            
            .. attribute:: interface_details
            
            	Set of interfaces configured for SRLG
            	**type**\:  :py:class:`InterfaceDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceDetails>`
            
            	**config**\: False
            
            .. attribute:: srlg_values
            
            	Set of SRLG values configured
            	**type**\:  :py:class:`SrlgValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.SrlgValues>`
            
            	**config**\: False
            
            .. attribute:: interface_srlg_names
            
            	Set of SRLG names configured
            	**type**\:  :py:class:`InterfaceSrlgNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceSrlgNames>`
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-rsi-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Srlg.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("srlg-maps", ("srlg_maps", Srlg.Nodes.Node.SrlgMaps)), ("groups", ("groups", Srlg.Nodes.Node.Groups)), ("inherit-nodes", ("inherit_nodes", Srlg.Nodes.Node.InheritNodes)), ("interfaces", ("interfaces", Srlg.Nodes.Node.Interfaces)), ("interface-details", ("interface_details", Srlg.Nodes.Node.InterfaceDetails)), ("srlg-values", ("srlg_values", Srlg.Nodes.Node.SrlgValues)), ("interface-srlg-names", ("interface_srlg_names", Srlg.Nodes.Node.InterfaceSrlgNames))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.srlg_maps = Srlg.Nodes.Node.SrlgMaps()
                self.srlg_maps.parent = self
                self._children_name_map["srlg_maps"] = "srlg-maps"

                self.groups = Srlg.Nodes.Node.Groups()
                self.groups.parent = self
                self._children_name_map["groups"] = "groups"

                self.inherit_nodes = Srlg.Nodes.Node.InheritNodes()
                self.inherit_nodes.parent = self
                self._children_name_map["inherit_nodes"] = "inherit-nodes"

                self.interfaces = Srlg.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"

                self.interface_details = Srlg.Nodes.Node.InterfaceDetails()
                self.interface_details.parent = self
                self._children_name_map["interface_details"] = "interface-details"

                self.srlg_values = Srlg.Nodes.Node.SrlgValues()
                self.srlg_values.parent = self
                self._children_name_map["srlg_values"] = "srlg-values"

                self.interface_srlg_names = Srlg.Nodes.Node.InterfaceSrlgNames()
                self.interface_srlg_names.parent = self
                self._children_name_map["interface_srlg_names"] = "interface-srlg-names"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srlg.Nodes.Node, ['node_name'], name, value)


            class SrlgMaps(_Entity_):
                """
                Set of SRLG name, value maps configured
                
                .. attribute:: srlg_map
                
                	Configured SRLG name details 
                	**type**\: list of  		 :py:class:`SrlgMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.SrlgMaps.SrlgMap>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srlg.Nodes.Node.SrlgMaps, self).__init__()

                    self.yang_name = "srlg-maps"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("srlg-map", ("srlg_map", Srlg.Nodes.Node.SrlgMaps.SrlgMap))])
                    self._leafs = OrderedDict()

                    self.srlg_map = YList(self)
                    self._segment_path = lambda: "srlg-maps"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Nodes.Node.SrlgMaps, [], name, value)


                class SrlgMap(_Entity_):
                    """
                    Configured SRLG name details 
                    
                    .. attribute:: srlg_name  (key)
                    
                    	SRLG name
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    	**config**\: False
                    
                    .. attribute:: srlg_value
                    
                    	SRLG value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: srlg_name_xr
                    
                    	SRLG name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srlg.Nodes.Node.SrlgMaps.SrlgMap, self).__init__()

                        self.yang_name = "srlg-map"
                        self.yang_parent_name = "srlg-maps"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['srlg_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('srlg_name', (YLeaf(YType.str, 'srlg-name'), ['str'])),
                            ('srlg_value', (YLeaf(YType.uint32, 'srlg-value'), ['int'])),
                            ('srlg_name_xr', (YLeaf(YType.str, 'srlg-name-xr'), ['str'])),
                        ])
                        self.srlg_name = None
                        self.srlg_value = None
                        self.srlg_name_xr = None
                        self._segment_path = lambda: "srlg-map" + "[srlg-name='" + str(self.srlg_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.Nodes.Node.SrlgMaps.SrlgMap, ['srlg_name', 'srlg_value', 'srlg_name_xr'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                        return meta._meta_table['Srlg.Nodes.Node.SrlgMaps.SrlgMap']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                    return meta._meta_table['Srlg.Nodes.Node.SrlgMaps']['meta_info']


            class Groups(_Entity_):
                """
                Set of Groups configured for SRLG
                
                .. attribute:: group
                
                	SRLG group details
                	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.Groups.Group>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srlg.Nodes.Node.Groups, self).__init__()

                    self.yang_name = "groups"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("group", ("group", Srlg.Nodes.Node.Groups.Group))])
                    self._leafs = OrderedDict()

                    self.group = YList(self)
                    self._segment_path = lambda: "groups"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Nodes.Node.Groups, [], name, value)


                class Group(_Entity_):
                    """
                    SRLG group details
                    
                    .. attribute:: group_name  (key)
                    
                    	Group name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: group_name_xr
                    
                    	Group name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: group_values
                    
                    	Group values
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: srlg_attribute
                    
                    	SRLG attribute
                    	**type**\: list of  		 :py:class:`SrlgAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.Groups.Group.SrlgAttribute>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srlg.Nodes.Node.Groups.Group, self).__init__()

                        self.yang_name = "group"
                        self.yang_parent_name = "groups"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['group_name']
                        self._child_classes = OrderedDict([("srlg-attribute", ("srlg_attribute", Srlg.Nodes.Node.Groups.Group.SrlgAttribute))])
                        self._leafs = OrderedDict([
                            ('group_name', (YLeaf(YType.str, 'group-name'), ['str'])),
                            ('group_name_xr', (YLeaf(YType.str, 'group-name-xr'), ['str'])),
                            ('group_values', (YLeaf(YType.uint32, 'group-values'), ['int'])),
                        ])
                        self.group_name = None
                        self.group_name_xr = None
                        self.group_values = None

                        self.srlg_attribute = YList(self)
                        self._segment_path = lambda: "group" + "[group-name='" + str(self.group_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.Nodes.Node.Groups.Group, ['group_name', 'group_name_xr', 'group_values'], name, value)


                    class SrlgAttribute(_Entity_):
                        """
                        SRLG attribute
                        
                        .. attribute:: srlg_value
                        
                        	SRLG value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: priority
                        
                        	Priority
                        	**type**\:  :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Priority>`
                        
                        	**config**\: False
                        
                        .. attribute:: srlg_index
                        
                        	Index
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-rsi-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srlg.Nodes.Node.Groups.Group.SrlgAttribute, self).__init__()

                            self.yang_name = "srlg-attribute"
                            self.yang_parent_name = "group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('srlg_value', (YLeaf(YType.uint32, 'srlg-value'), ['int'])),
                                ('priority', (YLeaf(YType.enumeration, 'priority'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Priority', '')])),
                                ('srlg_index', (YLeaf(YType.uint16, 'srlg-index'), ['int'])),
                            ])
                            self.srlg_value = None
                            self.priority = None
                            self.srlg_index = None
                            self._segment_path = lambda: "srlg-attribute"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srlg.Nodes.Node.Groups.Group.SrlgAttribute, ['srlg_value', 'priority', 'srlg_index'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                            return meta._meta_table['Srlg.Nodes.Node.Groups.Group.SrlgAttribute']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                        return meta._meta_table['Srlg.Nodes.Node.Groups.Group']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                    return meta._meta_table['Srlg.Nodes.Node.Groups']['meta_info']


            class InheritNodes(_Entity_):
                """
                Set of inherit locations configured for SRLG
                
                .. attribute:: inherit_node
                
                	SRLG inherit location details
                	**type**\: list of  		 :py:class:`InheritNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InheritNodes.InheritNode>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srlg.Nodes.Node.InheritNodes, self).__init__()

                    self.yang_name = "inherit-nodes"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("inherit-node", ("inherit_node", Srlg.Nodes.Node.InheritNodes.InheritNode))])
                    self._leafs = OrderedDict()

                    self.inherit_node = YList(self)
                    self._segment_path = lambda: "inherit-nodes"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Nodes.Node.InheritNodes, [], name, value)


                class InheritNode(_Entity_):
                    """
                    SRLG inherit location details
                    
                    .. attribute:: inherit_node_name  (key)
                    
                    	Inherit node
                    	**type**\: str
                    
                    	**pattern:** ((([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))/){2}(([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))
                    
                    	**config**\: False
                    
                    .. attribute:: node_name
                    
                    	Inherit node name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: node_values
                    
                    	Node values
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: srlg_attribute
                    
                    	SRLG attribute
                    	**type**\: list of  		 :py:class:`SrlgAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InheritNodes.InheritNode.SrlgAttribute>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srlg.Nodes.Node.InheritNodes.InheritNode, self).__init__()

                        self.yang_name = "inherit-node"
                        self.yang_parent_name = "inherit-nodes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['inherit_node_name']
                        self._child_classes = OrderedDict([("srlg-attribute", ("srlg_attribute", Srlg.Nodes.Node.InheritNodes.InheritNode.SrlgAttribute))])
                        self._leafs = OrderedDict([
                            ('inherit_node_name', (YLeaf(YType.str, 'inherit-node-name'), ['str'])),
                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                            ('node_values', (YLeaf(YType.uint32, 'node-values'), ['int'])),
                        ])
                        self.inherit_node_name = None
                        self.node_name = None
                        self.node_values = None

                        self.srlg_attribute = YList(self)
                        self._segment_path = lambda: "inherit-node" + "[inherit-node-name='" + str(self.inherit_node_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.Nodes.Node.InheritNodes.InheritNode, ['inherit_node_name', 'node_name', 'node_values'], name, value)


                    class SrlgAttribute(_Entity_):
                        """
                        SRLG attribute
                        
                        .. attribute:: srlg_value
                        
                        	SRLG value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: priority
                        
                        	Priority
                        	**type**\:  :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Priority>`
                        
                        	**config**\: False
                        
                        .. attribute:: srlg_index
                        
                        	Index
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-rsi-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srlg.Nodes.Node.InheritNodes.InheritNode.SrlgAttribute, self).__init__()

                            self.yang_name = "srlg-attribute"
                            self.yang_parent_name = "inherit-node"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('srlg_value', (YLeaf(YType.uint32, 'srlg-value'), ['int'])),
                                ('priority', (YLeaf(YType.enumeration, 'priority'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Priority', '')])),
                                ('srlg_index', (YLeaf(YType.uint16, 'srlg-index'), ['int'])),
                            ])
                            self.srlg_value = None
                            self.priority = None
                            self.srlg_index = None
                            self._segment_path = lambda: "srlg-attribute"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srlg.Nodes.Node.InheritNodes.InheritNode.SrlgAttribute, ['srlg_value', 'priority', 'srlg_index'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                            return meta._meta_table['Srlg.Nodes.Node.InheritNodes.InheritNode.SrlgAttribute']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                        return meta._meta_table['Srlg.Nodes.Node.InheritNodes.InheritNode']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                    return meta._meta_table['Srlg.Nodes.Node.InheritNodes']['meta_info']


            class Interfaces(_Entity_):
                """
                Set of interfaces configured for SRLG
                
                .. attribute:: interface
                
                	SRLG interface summary
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.Interfaces.Interface>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srlg.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", Srlg.Nodes.Node.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Nodes.Node.Interfaces, [], name, value)


                class Interface(_Entity_):
                    """
                    SRLG interface summary
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: interface_name_xr
                    
                    	Interface name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: value_count
                    
                    	Values
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: registrations
                    
                    	Registrations
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: srlg_value
                    
                    	SRLG values
                    	**type**\: list of int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srlg.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('interface_name_xr', (YLeaf(YType.str, 'interface-name-xr'), ['str'])),
                            ('value_count', (YLeaf(YType.uint32, 'value-count'), ['int'])),
                            ('registrations', (YLeaf(YType.uint32, 'registrations'), ['int'])),
                            ('srlg_value', (YLeafList(YType.uint32, 'srlg-value'), ['int'])),
                        ])
                        self.interface_name = None
                        self.interface_name_xr = None
                        self.value_count = None
                        self.registrations = None
                        self.srlg_value = []
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.Nodes.Node.Interfaces.Interface, ['interface_name', 'interface_name_xr', 'value_count', 'registrations', 'srlg_value'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                        return meta._meta_table['Srlg.Nodes.Node.Interfaces.Interface']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                    return meta._meta_table['Srlg.Nodes.Node.Interfaces']['meta_info']


            class InterfaceDetails(_Entity_):
                """
                Set of interfaces configured for SRLG
                
                .. attribute:: interface_detail
                
                	SRLG interface details
                	**type**\: list of  		 :py:class:`InterfaceDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srlg.Nodes.Node.InterfaceDetails, self).__init__()

                    self.yang_name = "interface-details"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-detail", ("interface_detail", Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail))])
                    self._leafs = OrderedDict()

                    self.interface_detail = YList(self)
                    self._segment_path = lambda: "interface-details"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Nodes.Node.InterfaceDetails, [], name, value)


                class InterfaceDetail(_Entity_):
                    """
                    SRLG interface details
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: groups
                    
                    	Groups
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: nodes
                    
                    	Nodes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: srlg_attribute
                    
                    	SRLG attributes
                    	**type**\: list of  		 :py:class:`SrlgAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.SrlgAttribute>`
                    
                    	**config**\: False
                    
                    .. attribute:: rsip
                    
                    	rsip list
                    	**type**\: list of  		 :py:class:`Rsip <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.Rsip>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail, self).__init__()

                        self.yang_name = "interface-detail"
                        self.yang_parent_name = "interface-details"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("srlg-attribute", ("srlg_attribute", Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.SrlgAttribute)), ("rsip", ("rsip", Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.Rsip))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('groups', (YLeaf(YType.uint32, 'groups'), ['int'])),
                            ('nodes', (YLeaf(YType.uint32, 'nodes'), ['int'])),
                        ])
                        self.interface_name = None
                        self.groups = None
                        self.nodes = None

                        self.srlg_attribute = YList(self)
                        self.rsip = YList(self)
                        self._segment_path = lambda: "interface-detail" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail, ['interface_name', 'groups', 'nodes'], name, value)


                    class SrlgAttribute(_Entity_):
                        """
                        SRLG attributes
                        
                        .. attribute:: srlg_value
                        
                        	SRLG value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: priority
                        
                        	Priority
                        	**type**\:  :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Priority>`
                        
                        	**config**\: False
                        
                        .. attribute:: source
                        
                        	Source
                        	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Source>`
                        
                        	**config**\: False
                        
                        .. attribute:: source_name
                        
                        	Source name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: srlg_index
                        
                        	Index
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-rsi-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.SrlgAttribute, self).__init__()

                            self.yang_name = "srlg-attribute"
                            self.yang_parent_name = "interface-detail"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('srlg_value', (YLeaf(YType.uint32, 'srlg-value'), ['int'])),
                                ('priority', (YLeaf(YType.enumeration, 'priority'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Priority', '')])),
                                ('source', (YLeaf(YType.enumeration, 'source'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Source', '')])),
                                ('source_name', (YLeaf(YType.str, 'source-name'), ['str'])),
                                ('srlg_index', (YLeaf(YType.uint16, 'srlg-index'), ['int'])),
                            ])
                            self.srlg_value = None
                            self.priority = None
                            self.source = None
                            self.source_name = None
                            self.srlg_index = None
                            self._segment_path = lambda: "srlg-attribute"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.SrlgAttribute, ['srlg_value', 'priority', 'source', 'source_name', 'srlg_index'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                            return meta._meta_table['Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.SrlgAttribute']['meta_info']


                    class Rsip(_Entity_):
                        """
                        rsip list
                        
                        .. attribute:: rsip_name
                        
                        	list of names matching rsip
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-rsi-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.Rsip, self).__init__()

                            self.yang_name = "rsip"
                            self.yang_parent_name = "interface-detail"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rsip_name', (YLeaf(YType.str, 'rsip-name'), ['str'])),
                            ])
                            self.rsip_name = None
                            self._segment_path = lambda: "rsip"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.Rsip, ['rsip_name'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                            return meta._meta_table['Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.Rsip']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                        return meta._meta_table['Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                    return meta._meta_table['Srlg.Nodes.Node.InterfaceDetails']['meta_info']


            class SrlgValues(_Entity_):
                """
                Set of SRLG values configured
                
                .. attribute:: srlg_value
                
                	Configured SRLG value details 
                	**type**\: list of  		 :py:class:`SrlgValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.SrlgValues.SrlgValue>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srlg.Nodes.Node.SrlgValues, self).__init__()

                    self.yang_name = "srlg-values"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("srlg-value", ("srlg_value", Srlg.Nodes.Node.SrlgValues.SrlgValue))])
                    self._leafs = OrderedDict()

                    self.srlg_value = YList(self)
                    self._segment_path = lambda: "srlg-values"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Nodes.Node.SrlgValues, [], name, value)


                class SrlgValue(_Entity_):
                    """
                    Configured SRLG value details 
                    
                    .. attribute:: value  (key)
                    
                    	SRLG value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\: list of str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srlg.Nodes.Node.SrlgValues.SrlgValue, self).__init__()

                        self.yang_name = "srlg-value"
                        self.yang_parent_name = "srlg-values"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['value']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                            ('interface_name', (YLeafList(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.value = None
                        self.interface_name = []
                        self._segment_path = lambda: "srlg-value" + "[value='" + str(self.value) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.Nodes.Node.SrlgValues.SrlgValue, ['value', 'interface_name'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                        return meta._meta_table['Srlg.Nodes.Node.SrlgValues.SrlgValue']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                    return meta._meta_table['Srlg.Nodes.Node.SrlgValues']['meta_info']


            class InterfaceSrlgNames(_Entity_):
                """
                Set of SRLG names configured
                
                .. attribute:: interface_srlg_name
                
                	Configured SRLG name details 
                	**type**\: list of  		 :py:class:`InterfaceSrlgName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName>`
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srlg.Nodes.Node.InterfaceSrlgNames, self).__init__()

                    self.yang_name = "interface-srlg-names"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-srlg-name", ("interface_srlg_name", Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName))])
                    self._leafs = OrderedDict()

                    self.interface_srlg_name = YList(self)
                    self._segment_path = lambda: "interface-srlg-names"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.Nodes.Node.InterfaceSrlgNames, [], name, value)


                class InterfaceSrlgName(_Entity_):
                    """
                    Configured SRLG name details 
                    
                    .. attribute:: srlg_name  (key)
                    
                    	SRLG name
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    	**config**\: False
                    
                    .. attribute:: interfaces
                    
                    	Interfaces information
                    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces>`
                    
                    	**config**\: False
                    
                    .. attribute:: srlg_name_xr
                    
                    	SRLG name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: srlg_value
                    
                    	SRLG value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName, self).__init__()

                        self.yang_name = "interface-srlg-name"
                        self.yang_parent_name = "interface-srlg-names"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['srlg_name']
                        self._child_classes = OrderedDict([("interfaces", ("interfaces", Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces))])
                        self._leafs = OrderedDict([
                            ('srlg_name', (YLeaf(YType.str, 'srlg-name'), ['str'])),
                            ('srlg_name_xr', (YLeaf(YType.str, 'srlg-name-xr'), ['str'])),
                            ('srlg_value', (YLeaf(YType.uint32, 'srlg-value'), ['int'])),
                        ])
                        self.srlg_name = None
                        self.srlg_name_xr = None
                        self.srlg_value = None

                        self.interfaces = Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                        self._segment_path = lambda: "interface-srlg-name" + "[srlg-name='" + str(self.srlg_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName, ['srlg_name', 'srlg_name_xr', 'srlg_value'], name, value)


                    class Interfaces(_Entity_):
                        """
                        Interfaces information
                        
                        .. attribute:: interface_name
                        
                        	Interface name
                        	**type**\: list of str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'infra-rsi-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces, self).__init__()

                            self.yang_name = "interfaces"
                            self.yang_parent_name = "interface-srlg-name"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeafList(YType.str, 'interface-name'), ['str'])),
                            ])
                            self.interface_name = []
                            self._segment_path = lambda: "interfaces"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces, ['interface_name'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                            return meta._meta_table['Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                        return meta._meta_table['Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                    return meta._meta_table['Srlg.Nodes.Node.InterfaceSrlgNames']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                return meta._meta_table['Srlg.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
            return meta._meta_table['Srlg.Nodes']['meta_info']


    class InterfaceSrlgNames(_Entity_):
        """
        Set of SRLG names configured
        
        .. attribute:: interface_srlg_name
        
        	Configured SRLG name details 
        	**type**\: list of  		 :py:class:`InterfaceSrlgName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.InterfaceSrlgNames.InterfaceSrlgName>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Srlg.InterfaceSrlgNames, self).__init__()

            self.yang_name = "interface-srlg-names"
            self.yang_parent_name = "srlg"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface-srlg-name", ("interface_srlg_name", Srlg.InterfaceSrlgNames.InterfaceSrlgName))])
            self._leafs = OrderedDict()

            self.interface_srlg_name = YList(self)
            self._segment_path = lambda: "interface-srlg-names"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Srlg.InterfaceSrlgNames, [], name, value)


        class InterfaceSrlgName(_Entity_):
            """
            Configured SRLG name details 
            
            .. attribute:: srlg_name  (key)
            
            	SRLG name
            	**type**\: str
            
            	**length:** 1..64
            
            	**config**\: False
            
            .. attribute:: interfaces
            
            	Interfaces information
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces>`
            
            	**config**\: False
            
            .. attribute:: srlg_name_xr
            
            	SRLG name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: srlg_value
            
            	SRLG value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-rsi-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Srlg.InterfaceSrlgNames.InterfaceSrlgName, self).__init__()

                self.yang_name = "interface-srlg-name"
                self.yang_parent_name = "interface-srlg-names"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['srlg_name']
                self._child_classes = OrderedDict([("interfaces", ("interfaces", Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces))])
                self._leafs = OrderedDict([
                    ('srlg_name', (YLeaf(YType.str, 'srlg-name'), ['str'])),
                    ('srlg_name_xr', (YLeaf(YType.str, 'srlg-name-xr'), ['str'])),
                    ('srlg_value', (YLeaf(YType.uint32, 'srlg-value'), ['int'])),
                ])
                self.srlg_name = None
                self.srlg_name_xr = None
                self.srlg_value = None

                self.interfaces = Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._segment_path = lambda: "interface-srlg-name" + "[srlg-name='" + str(self.srlg_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/interface-srlg-names/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srlg.InterfaceSrlgNames.InterfaceSrlgName, ['srlg_name', 'srlg_name_xr', 'srlg_value'], name, value)


            class Interfaces(_Entity_):
                """
                Interfaces information
                
                .. attribute:: interface_name
                
                	Interface name
                	**type**\: list of str
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "interface-srlg-name"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeafList(YType.str, 'interface-name'), ['str'])),
                    ])
                    self.interface_name = []
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces, ['interface_name'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                    return meta._meta_table['Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                return meta._meta_table['Srlg.InterfaceSrlgNames.InterfaceSrlgName']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
            return meta._meta_table['Srlg.InterfaceSrlgNames']['meta_info']


    class InheritNodes(_Entity_):
        """
        Set of inherit locations configured for SRLG
        
        .. attribute:: inherit_node
        
        	SRLG inherit location details
        	**type**\: list of  		 :py:class:`InheritNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.InheritNodes.InheritNode>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Srlg.InheritNodes, self).__init__()

            self.yang_name = "inherit-nodes"
            self.yang_parent_name = "srlg"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("inherit-node", ("inherit_node", Srlg.InheritNodes.InheritNode))])
            self._leafs = OrderedDict()

            self.inherit_node = YList(self)
            self._segment_path = lambda: "inherit-nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Srlg.InheritNodes, [], name, value)


        class InheritNode(_Entity_):
            """
            SRLG inherit location details
            
            .. attribute:: inherit_node_name  (key)
            
            	Inherit Locatio
            	**type**\: str
            
            	**pattern:** ((([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))/){2}(([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))
            
            	**config**\: False
            
            .. attribute:: node_name
            
            	Inherit node name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: node_values
            
            	Node values
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: srlg_attribute
            
            	SRLG attribute
            	**type**\: list of  		 :py:class:`SrlgAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.InheritNodes.InheritNode.SrlgAttribute>`
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-rsi-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Srlg.InheritNodes.InheritNode, self).__init__()

                self.yang_name = "inherit-node"
                self.yang_parent_name = "inherit-nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['inherit_node_name']
                self._child_classes = OrderedDict([("srlg-attribute", ("srlg_attribute", Srlg.InheritNodes.InheritNode.SrlgAttribute))])
                self._leafs = OrderedDict([
                    ('inherit_node_name', (YLeaf(YType.str, 'inherit-node-name'), ['str'])),
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                    ('node_values', (YLeaf(YType.uint32, 'node-values'), ['int'])),
                ])
                self.inherit_node_name = None
                self.node_name = None
                self.node_values = None

                self.srlg_attribute = YList(self)
                self._segment_path = lambda: "inherit-node" + "[inherit-node-name='" + str(self.inherit_node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/inherit-nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srlg.InheritNodes.InheritNode, ['inherit_node_name', 'node_name', 'node_values'], name, value)


            class SrlgAttribute(_Entity_):
                """
                SRLG attribute
                
                .. attribute:: srlg_value
                
                	SRLG value
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: priority
                
                	Priority
                	**type**\:  :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Priority>`
                
                	**config**\: False
                
                .. attribute:: srlg_index
                
                	Index
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srlg.InheritNodes.InheritNode.SrlgAttribute, self).__init__()

                    self.yang_name = "srlg-attribute"
                    self.yang_parent_name = "inherit-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('srlg_value', (YLeaf(YType.uint32, 'srlg-value'), ['int'])),
                        ('priority', (YLeaf(YType.enumeration, 'priority'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Priority', '')])),
                        ('srlg_index', (YLeaf(YType.uint16, 'srlg-index'), ['int'])),
                    ])
                    self.srlg_value = None
                    self.priority = None
                    self.srlg_index = None
                    self._segment_path = lambda: "srlg-attribute"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.InheritNodes.InheritNode.SrlgAttribute, ['srlg_value', 'priority', 'srlg_index'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                    return meta._meta_table['Srlg.InheritNodes.InheritNode.SrlgAttribute']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                return meta._meta_table['Srlg.InheritNodes.InheritNode']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
            return meta._meta_table['Srlg.InheritNodes']['meta_info']


    class SrlgValues(_Entity_):
        """
        Set of SRLG values configured
        
        .. attribute:: srlg_value
        
        	Configured SRLG value details 
        	**type**\: list of  		 :py:class:`SrlgValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.SrlgValues.SrlgValue>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Srlg.SrlgValues, self).__init__()

            self.yang_name = "srlg-values"
            self.yang_parent_name = "srlg"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("srlg-value", ("srlg_value", Srlg.SrlgValues.SrlgValue))])
            self._leafs = OrderedDict()

            self.srlg_value = YList(self)
            self._segment_path = lambda: "srlg-values"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Srlg.SrlgValues, [], name, value)


        class SrlgValue(_Entity_):
            """
            Configured SRLG value details 
            
            .. attribute:: value  (key)
            
            	SRLG value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: interface_name
            
            	Interface name
            	**type**\: list of str
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-rsi-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Srlg.SrlgValues.SrlgValue, self).__init__()

                self.yang_name = "srlg-value"
                self.yang_parent_name = "srlg-values"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['value']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                    ('interface_name', (YLeafList(YType.str, 'interface-name'), ['str'])),
                ])
                self.value = None
                self.interface_name = []
                self._segment_path = lambda: "srlg-value" + "[value='" + str(self.value) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/srlg-values/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srlg.SrlgValues.SrlgValue, ['value', 'interface_name'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                return meta._meta_table['Srlg.SrlgValues.SrlgValue']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
            return meta._meta_table['Srlg.SrlgValues']['meta_info']


    class InterfaceDetails(_Entity_):
        """
        Set of interfaces configured for SRLG
        
        .. attribute:: interface_detail
        
        	SRLG interface details
        	**type**\: list of  		 :py:class:`InterfaceDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.InterfaceDetails.InterfaceDetail>`
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Srlg.InterfaceDetails, self).__init__()

            self.yang_name = "interface-details"
            self.yang_parent_name = "srlg"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface-detail", ("interface_detail", Srlg.InterfaceDetails.InterfaceDetail))])
            self._leafs = OrderedDict()

            self.interface_detail = YList(self)
            self._segment_path = lambda: "interface-details"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Srlg.InterfaceDetails, [], name, value)


        class InterfaceDetail(_Entity_):
            """
            SRLG interface details
            
            .. attribute:: interface_name  (key)
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            	**config**\: False
            
            .. attribute:: groups
            
            	Groups
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: nodes
            
            	Nodes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: srlg_attribute
            
            	SRLG attributes
            	**type**\: list of  		 :py:class:`SrlgAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.InterfaceDetails.InterfaceDetail.SrlgAttribute>`
            
            	**config**\: False
            
            .. attribute:: rsip
            
            	rsip list
            	**type**\: list of  		 :py:class:`Rsip <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.InterfaceDetails.InterfaceDetail.Rsip>`
            
            	**config**\: False
            
            

            """

            _prefix = 'infra-rsi-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Srlg.InterfaceDetails.InterfaceDetail, self).__init__()

                self.yang_name = "interface-detail"
                self.yang_parent_name = "interface-details"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([("srlg-attribute", ("srlg_attribute", Srlg.InterfaceDetails.InterfaceDetail.SrlgAttribute)), ("rsip", ("rsip", Srlg.InterfaceDetails.InterfaceDetail.Rsip))])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('groups', (YLeaf(YType.uint32, 'groups'), ['int'])),
                    ('nodes', (YLeaf(YType.uint32, 'nodes'), ['int'])),
                ])
                self.interface_name = None
                self.groups = None
                self.nodes = None

                self.srlg_attribute = YList(self)
                self.rsip = YList(self)
                self._segment_path = lambda: "interface-detail" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:srlg/interface-details/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Srlg.InterfaceDetails.InterfaceDetail, ['interface_name', 'groups', 'nodes'], name, value)


            class SrlgAttribute(_Entity_):
                """
                SRLG attributes
                
                .. attribute:: srlg_value
                
                	SRLG value
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: priority
                
                	Priority
                	**type**\:  :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Priority>`
                
                	**config**\: False
                
                .. attribute:: source
                
                	Source
                	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Source>`
                
                	**config**\: False
                
                .. attribute:: source_name
                
                	Source name
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: srlg_index
                
                	Index
                	**type**\: int
                
                	**range:** 0..65535
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srlg.InterfaceDetails.InterfaceDetail.SrlgAttribute, self).__init__()

                    self.yang_name = "srlg-attribute"
                    self.yang_parent_name = "interface-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('srlg_value', (YLeaf(YType.uint32, 'srlg-value'), ['int'])),
                        ('priority', (YLeaf(YType.enumeration, 'priority'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Priority', '')])),
                        ('source', (YLeaf(YType.enumeration, 'source'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper', 'Source', '')])),
                        ('source_name', (YLeaf(YType.str, 'source-name'), ['str'])),
                        ('srlg_index', (YLeaf(YType.uint16, 'srlg-index'), ['int'])),
                    ])
                    self.srlg_value = None
                    self.priority = None
                    self.source = None
                    self.source_name = None
                    self.srlg_index = None
                    self._segment_path = lambda: "srlg-attribute"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.InterfaceDetails.InterfaceDetail.SrlgAttribute, ['srlg_value', 'priority', 'source', 'source_name', 'srlg_index'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                    return meta._meta_table['Srlg.InterfaceDetails.InterfaceDetail.SrlgAttribute']['meta_info']


            class Rsip(_Entity_):
                """
                rsip list
                
                .. attribute:: rsip_name
                
                	list of names matching rsip
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Srlg.InterfaceDetails.InterfaceDetail.Rsip, self).__init__()

                    self.yang_name = "rsip"
                    self.yang_parent_name = "interface-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('rsip_name', (YLeaf(YType.str, 'rsip-name'), ['str'])),
                    ])
                    self.rsip_name = None
                    self._segment_path = lambda: "rsip"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Srlg.InterfaceDetails.InterfaceDetail.Rsip, ['rsip_name'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                    return meta._meta_table['Srlg.InterfaceDetails.InterfaceDetail.Rsip']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                return meta._meta_table['Srlg.InterfaceDetails.InterfaceDetail']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
            return meta._meta_table['Srlg.InterfaceDetails']['meta_info']

    def clone_ptr(self):
        self._top_entity = Srlg()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
        return meta._meta_table['Srlg']['meta_info']


class SelectiveVrfDownload(_Entity_):
    """
    selective vrf download
    
    .. attribute:: state
    
    	Selective VRF Download feature state details
    	**type**\:  :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.SelectiveVrfDownload.State>`
    
    	**config**\: False
    
    

    """

    _prefix = 'infra-rsi-oper'
    _revision = '2017-09-07'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(SelectiveVrfDownload, self).__init__()
        self._top_entity = None

        self.yang_name = "selective-vrf-download"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rsi-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("state", ("state", SelectiveVrfDownload.State))])
        self._leafs = OrderedDict()

        self.state = SelectiveVrfDownload.State()
        self.state.parent = self
        self._children_name_map["state"] = "state"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:selective-vrf-download"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SelectiveVrfDownload, [], name, value)


    class State(_Entity_):
        """
        Selective VRF Download feature state details
        
        .. attribute:: is_svd_enabled
        
        	Is SVD Enabled Operational
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: is_svd_enabled_cfg
        
        	Is SVD Enabled Config
        	**type**\: bool
        
        	**config**\: False
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SelectiveVrfDownload.State, self).__init__()

            self.yang_name = "state"
            self.yang_parent_name = "selective-vrf-download"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('is_svd_enabled', (YLeaf(YType.boolean, 'is-svd-enabled'), ['bool'])),
                ('is_svd_enabled_cfg', (YLeaf(YType.boolean, 'is-svd-enabled-cfg'), ['bool'])),
            ])
            self.is_svd_enabled = None
            self.is_svd_enabled_cfg = None
            self._segment_path = lambda: "state"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-rsi-oper:selective-vrf-download/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SelectiveVrfDownload.State, ['is_svd_enabled', 'is_svd_enabled_cfg'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
            return meta._meta_table['SelectiveVrfDownload.State']['meta_info']

    def clone_ptr(self):
        self._top_entity = SelectiveVrfDownload()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
        return meta._meta_table['SelectiveVrfDownload']['meta_info']



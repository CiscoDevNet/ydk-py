""" Cisco_IOS_XR_infra_rsi_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-rsi package operational data.

This module contains definitions
for the following management objects\:
  vrf\-group\: VRF group operational data
  srlg\: srlg
  selective\-vrf\-download\: selective vrf download

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class PriorityEnum(Enum):
    """
    PriorityEnum

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

    """

    critical = 0

    high = 1

    medium = 2

    low = 3

    very_low = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
        return meta._meta_table['PriorityEnum']


class SourceEnum(Enum):
    """
    SourceEnum

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

    configured = 1

    from_group = 2

    inherited = 4

    from_optical = 8

    configured_and_notified = 17

    from_group_and_notified = 18

    inherited_and_notified = 20

    from_optical_and_notified = 24


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
        return meta._meta_table['SourceEnum']



class VrfGroup(object):
    """
    VRF group operational data
    
    .. attribute:: nodes
    
    	Node operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.VrfGroup.Nodes>`
    
    

    """

    _prefix = 'infra-rsi-oper'
    _revision = '2015-01-07'

    def __init__(self):
        self.nodes = VrfGroup.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Node operational data
        
        .. attribute:: node
        
        	Node details
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.VrfGroup.Nodes.Node>`
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2015-01-07'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Node details
            
            .. attribute:: node_name  <key>
            
            	Node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: groups
            
            	Group operational data
            	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.VrfGroup.Nodes.Node.Groups>`
            
            

            """

            _prefix = 'infra-rsi-oper'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.groups = VrfGroup.Nodes.Node.Groups()
                self.groups.parent = self


            class Groups(object):
                """
                Group operational data
                
                .. attribute:: group
                
                	Group details
                	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.VrfGroup.Nodes.Node.Groups.Group>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    self.parent = None
                    self.group = YList()
                    self.group.parent = self
                    self.group.name = 'group'


                class Group(object):
                    """
                    Group details
                    
                    .. attribute:: group_name  <key>
                    
                    	Group name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: forward_reference
                    
                    	VRF group not present but used
                    	**type**\:  bool
                    
                    .. attribute:: vr_fs
                    
                    	Number of VRFs in this VRF group
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf
                    
                    	VRF group's VRF
                    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.VrfGroup.Nodes.Node.Groups.Group.Vrf>`
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        self.parent = None
                        self.group_name = None
                        self.forward_reference = None
                        self.vr_fs = None
                        self.vrf = YList()
                        self.vrf.parent = self
                        self.vrf.name = 'vrf'


                    class Vrf(object):
                        """
                        VRF group's VRF
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'infra-rsi-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            self.parent = None
                            self.vrf_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-oper:vrf'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                            return meta._meta_table['VrfGroup.Nodes.Node.Groups.Group.Vrf']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.group_name is None:
                            raise YPYModelError('Key property group_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-oper:group[Cisco-IOS-XR-infra-rsi-oper:group-name = ' + str(self.group_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.group_name is not None:
                            return True

                        if self.forward_reference is not None:
                            return True

                        if self.vr_fs is not None:
                            return True

                        if self.vrf is not None:
                            for child_ref in self.vrf:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                        return meta._meta_table['VrfGroup.Nodes.Node.Groups.Group']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-oper:groups'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.group is not None:
                        for child_ref in self.group:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                    return meta._meta_table['VrfGroup.Nodes.Node.Groups']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-infra-rsi-oper:vrf-group/Cisco-IOS-XR-infra-rsi-oper:nodes/Cisco-IOS-XR-infra-rsi-oper:node[Cisco-IOS-XR-infra-rsi-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.groups is not None and self.groups._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                return meta._meta_table['VrfGroup.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-rsi-oper:vrf-group/Cisco-IOS-XR-infra-rsi-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
            return meta._meta_table['VrfGroup.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-rsi-oper:vrf-group'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
        return meta._meta_table['VrfGroup']['meta_info']


class Srlg(object):
    """
    srlg
    
    .. attribute:: interface_srlg_names
    
    	Set of SRLG names configured
    	**type**\:   :py:class:`InterfaceSrlgNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.InterfaceSrlgNames>`
    
    .. attribute:: nodes
    
    	RSI SRLG operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes>`
    
    .. attribute:: srlg_maps
    
    	Set of SRLG name, value maps configured
    	**type**\:   :py:class:`SrlgMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.SrlgMaps>`
    
    

    """

    _prefix = 'infra-rsi-oper'
    _revision = '2015-01-07'

    def __init__(self):
        self.interface_srlg_names = Srlg.InterfaceSrlgNames()
        self.interface_srlg_names.parent = self
        self.nodes = Srlg.Nodes()
        self.nodes.parent = self
        self.srlg_maps = Srlg.SrlgMaps()
        self.srlg_maps.parent = self


    class SrlgMaps(object):
        """
        Set of SRLG name, value maps configured
        
        .. attribute:: srlg_map
        
        	Configured SRLG name details 
        	**type**\: list of    :py:class:`SrlgMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.SrlgMaps.SrlgMap>`
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2015-01-07'

        def __init__(self):
            self.parent = None
            self.srlg_map = YList()
            self.srlg_map.parent = self
            self.srlg_map.name = 'srlg_map'


        class SrlgMap(object):
            """
            Configured SRLG name details 
            
            .. attribute:: srlg_name  <key>
            
            	SRLG name
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: srlg_name_xr
            
            	SRLG name
            	**type**\:  str
            
            .. attribute:: srlg_value
            
            	SRLG value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-rsi-oper'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.srlg_name = None
                self.srlg_name_xr = None
                self.srlg_value = None

            @property
            def _common_path(self):
                if self.srlg_name is None:
                    raise YPYModelError('Key property srlg_name is None')

                return '/Cisco-IOS-XR-infra-rsi-oper:srlg/Cisco-IOS-XR-infra-rsi-oper:srlg-maps/Cisco-IOS-XR-infra-rsi-oper:srlg-map[Cisco-IOS-XR-infra-rsi-oper:srlg-name = ' + str(self.srlg_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.srlg_name is not None:
                    return True

                if self.srlg_name_xr is not None:
                    return True

                if self.srlg_value is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                return meta._meta_table['Srlg.SrlgMaps.SrlgMap']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-rsi-oper:srlg/Cisco-IOS-XR-infra-rsi-oper:srlg-maps'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.srlg_map is not None:
                for child_ref in self.srlg_map:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
            return meta._meta_table['Srlg.SrlgMaps']['meta_info']


    class Nodes(object):
        """
        RSI SRLG operational data
        
        .. attribute:: node
        
        	RSI SRLG operational data
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node>`
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2015-01-07'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            RSI SRLG operational data
            
            .. attribute:: node_name  <key>
            
            	Node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: groups
            
            	Set of Groups configured for SRLG
            	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.Groups>`
            
            .. attribute:: inherit_nodes
            
            	Set of inherit locations configured for SRLG
            	**type**\:   :py:class:`InheritNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InheritNodes>`
            
            .. attribute:: interface_details
            
            	Set of interfaces configured for SRLG
            	**type**\:   :py:class:`InterfaceDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceDetails>`
            
            .. attribute:: interface_srlg_names
            
            	Set of SRLG names configured
            	**type**\:   :py:class:`InterfaceSrlgNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceSrlgNames>`
            
            .. attribute:: interfaces
            
            	Set of interfaces configured for SRLG
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.Interfaces>`
            
            .. attribute:: srlg_maps
            
            	Set of SRLG name, value maps configured
            	**type**\:   :py:class:`SrlgMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.SrlgMaps>`
            
            .. attribute:: srlg_values
            
            	Set of SRLG values configured
            	**type**\:   :py:class:`SrlgValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.SrlgValues>`
            
            

            """

            _prefix = 'infra-rsi-oper'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.groups = Srlg.Nodes.Node.Groups()
                self.groups.parent = self
                self.inherit_nodes = Srlg.Nodes.Node.InheritNodes()
                self.inherit_nodes.parent = self
                self.interface_details = Srlg.Nodes.Node.InterfaceDetails()
                self.interface_details.parent = self
                self.interface_srlg_names = Srlg.Nodes.Node.InterfaceSrlgNames()
                self.interface_srlg_names.parent = self
                self.interfaces = Srlg.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self.srlg_maps = Srlg.Nodes.Node.SrlgMaps()
                self.srlg_maps.parent = self
                self.srlg_values = Srlg.Nodes.Node.SrlgValues()
                self.srlg_values.parent = self


            class SrlgMaps(object):
                """
                Set of SRLG name, value maps configured
                
                .. attribute:: srlg_map
                
                	Configured SRLG name details 
                	**type**\: list of    :py:class:`SrlgMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.SrlgMaps.SrlgMap>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    self.parent = None
                    self.srlg_map = YList()
                    self.srlg_map.parent = self
                    self.srlg_map.name = 'srlg_map'


                class SrlgMap(object):
                    """
                    Configured SRLG name details 
                    
                    .. attribute:: srlg_name  <key>
                    
                    	SRLG name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: srlg_name_xr
                    
                    	SRLG name
                    	**type**\:  str
                    
                    .. attribute:: srlg_value
                    
                    	SRLG value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        self.parent = None
                        self.srlg_name = None
                        self.srlg_name_xr = None
                        self.srlg_value = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.srlg_name is None:
                            raise YPYModelError('Key property srlg_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-oper:srlg-map[Cisco-IOS-XR-infra-rsi-oper:srlg-name = ' + str(self.srlg_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.srlg_name is not None:
                            return True

                        if self.srlg_name_xr is not None:
                            return True

                        if self.srlg_value is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                        return meta._meta_table['Srlg.Nodes.Node.SrlgMaps.SrlgMap']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-oper:srlg-maps'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.srlg_map is not None:
                        for child_ref in self.srlg_map:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                    return meta._meta_table['Srlg.Nodes.Node.SrlgMaps']['meta_info']


            class Groups(object):
                """
                Set of Groups configured for SRLG
                
                .. attribute:: group
                
                	SRLG group details
                	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.Groups.Group>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    self.parent = None
                    self.group = YList()
                    self.group.parent = self
                    self.group.name = 'group'


                class Group(object):
                    """
                    SRLG group details
                    
                    .. attribute:: group_name  <key>
                    
                    	Group name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: group_name_xr
                    
                    	Group name
                    	**type**\:  str
                    
                    .. attribute:: group_values
                    
                    	Group values
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: srlg_attribute
                    
                    	SRLG attribute
                    	**type**\: list of    :py:class:`SrlgAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.Groups.Group.SrlgAttribute>`
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        self.parent = None
                        self.group_name = None
                        self.group_name_xr = None
                        self.group_values = None
                        self.srlg_attribute = YList()
                        self.srlg_attribute.parent = self
                        self.srlg_attribute.name = 'srlg_attribute'


                    class SrlgAttribute(object):
                        """
                        SRLG attribute
                        
                        .. attribute:: priority
                        
                        	Priority
                        	**type**\:   :py:class:`PriorityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.PriorityEnum>`
                        
                        .. attribute:: srlg_index
                        
                        	Index
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: srlg_value
                        
                        	SRLG value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-rsi-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            self.parent = None
                            self.priority = None
                            self.srlg_index = None
                            self.srlg_value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-oper:srlg-attribute'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.priority is not None:
                                return True

                            if self.srlg_index is not None:
                                return True

                            if self.srlg_value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                            return meta._meta_table['Srlg.Nodes.Node.Groups.Group.SrlgAttribute']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.group_name is None:
                            raise YPYModelError('Key property group_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-oper:group[Cisco-IOS-XR-infra-rsi-oper:group-name = ' + str(self.group_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.group_name is not None:
                            return True

                        if self.group_name_xr is not None:
                            return True

                        if self.group_values is not None:
                            return True

                        if self.srlg_attribute is not None:
                            for child_ref in self.srlg_attribute:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                        return meta._meta_table['Srlg.Nodes.Node.Groups.Group']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-oper:groups'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.group is not None:
                        for child_ref in self.group:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                    return meta._meta_table['Srlg.Nodes.Node.Groups']['meta_info']


            class InheritNodes(object):
                """
                Set of inherit locations configured for SRLG
                
                .. attribute:: inherit_node
                
                	SRLG inherit location details
                	**type**\: list of    :py:class:`InheritNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InheritNodes.InheritNode>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    self.parent = None
                    self.inherit_node = YList()
                    self.inherit_node.parent = self
                    self.inherit_node.name = 'inherit_node'


                class InheritNode(object):
                    """
                    SRLG inherit location details
                    
                    .. attribute:: inherit_node_name  <key>
                    
                    	Inherit node
                    	**type**\:  str
                    
                    	**pattern:** ((([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))/){2}(([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))
                    
                    .. attribute:: node_name
                    
                    	Inherit node name
                    	**type**\:  str
                    
                    .. attribute:: node_values
                    
                    	Node values
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: srlg_attribute
                    
                    	SRLG attribute
                    	**type**\: list of    :py:class:`SrlgAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InheritNodes.InheritNode.SrlgAttribute>`
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        self.parent = None
                        self.inherit_node_name = None
                        self.node_name = None
                        self.node_values = None
                        self.srlg_attribute = YList()
                        self.srlg_attribute.parent = self
                        self.srlg_attribute.name = 'srlg_attribute'


                    class SrlgAttribute(object):
                        """
                        SRLG attribute
                        
                        .. attribute:: priority
                        
                        	Priority
                        	**type**\:   :py:class:`PriorityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.PriorityEnum>`
                        
                        .. attribute:: srlg_index
                        
                        	Index
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: srlg_value
                        
                        	SRLG value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-rsi-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            self.parent = None
                            self.priority = None
                            self.srlg_index = None
                            self.srlg_value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-oper:srlg-attribute'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.priority is not None:
                                return True

                            if self.srlg_index is not None:
                                return True

                            if self.srlg_value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                            return meta._meta_table['Srlg.Nodes.Node.InheritNodes.InheritNode.SrlgAttribute']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.inherit_node_name is None:
                            raise YPYModelError('Key property inherit_node_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-oper:inherit-node[Cisco-IOS-XR-infra-rsi-oper:inherit-node-name = ' + str(self.inherit_node_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.inherit_node_name is not None:
                            return True

                        if self.node_name is not None:
                            return True

                        if self.node_values is not None:
                            return True

                        if self.srlg_attribute is not None:
                            for child_ref in self.srlg_attribute:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                        return meta._meta_table['Srlg.Nodes.Node.InheritNodes.InheritNode']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-oper:inherit-nodes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.inherit_node is not None:
                        for child_ref in self.inherit_node:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                    return meta._meta_table['Srlg.Nodes.Node.InheritNodes']['meta_info']


            class Interfaces(object):
                """
                Set of interfaces configured for SRLG
                
                .. attribute:: interface
                
                	SRLG interface summary
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    SRLG interface summary
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: interface_name_xr
                    
                    	Interface name
                    	**type**\:  str
                    
                    .. attribute:: registrations
                    
                    	Registrations
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: srlg_value
                    
                    	SRLG values
                    	**type**\:  list of int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: value_count
                    
                    	Values
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.interface_name_xr = None
                        self.registrations = None
                        self.srlg_value = YLeafList()
                        self.srlg_value.parent = self
                        self.srlg_value.name = 'srlg_value'
                        self.value_count = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-oper:interface[Cisco-IOS-XR-infra-rsi-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.interface_name_xr is not None:
                            return True

                        if self.registrations is not None:
                            return True

                        if self.srlg_value is not None:
                            for child in self.srlg_value:
                                if child is not None:
                                    return True

                        if self.value_count is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                        return meta._meta_table['Srlg.Nodes.Node.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-oper:interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface is not None:
                        for child_ref in self.interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                    return meta._meta_table['Srlg.Nodes.Node.Interfaces']['meta_info']


            class InterfaceDetails(object):
                """
                Set of interfaces configured for SRLG
                
                .. attribute:: interface_detail
                
                	SRLG interface details
                	**type**\: list of    :py:class:`InterfaceDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    self.parent = None
                    self.interface_detail = YList()
                    self.interface_detail.parent = self
                    self.interface_detail.name = 'interface_detail'


                class InterfaceDetail(object):
                    """
                    SRLG interface details
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: groups
                    
                    	Groups
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: nodes
                    
                    	Nodes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: srlg_attribute
                    
                    	SRLG attributes
                    	**type**\: list of    :py:class:`SrlgAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.SrlgAttribute>`
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.groups = None
                        self.nodes = None
                        self.srlg_attribute = YList()
                        self.srlg_attribute.parent = self
                        self.srlg_attribute.name = 'srlg_attribute'


                    class SrlgAttribute(object):
                        """
                        SRLG attributes
                        
                        .. attribute:: priority
                        
                        	Priority
                        	**type**\:   :py:class:`PriorityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.PriorityEnum>`
                        
                        .. attribute:: source
                        
                        	Source
                        	**type**\:   :py:class:`SourceEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.SourceEnum>`
                        
                        .. attribute:: source_name
                        
                        	Source name
                        	**type**\:  str
                        
                        .. attribute:: srlg_index
                        
                        	Index
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: srlg_value
                        
                        	SRLG value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-rsi-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            self.parent = None
                            self.priority = None
                            self.source = None
                            self.source_name = None
                            self.srlg_index = None
                            self.srlg_value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-oper:srlg-attribute'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.priority is not None:
                                return True

                            if self.source is not None:
                                return True

                            if self.source_name is not None:
                                return True

                            if self.srlg_index is not None:
                                return True

                            if self.srlg_value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                            return meta._meta_table['Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail.SrlgAttribute']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-oper:interface-detail[Cisco-IOS-XR-infra-rsi-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.groups is not None:
                            return True

                        if self.nodes is not None:
                            return True

                        if self.srlg_attribute is not None:
                            for child_ref in self.srlg_attribute:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                        return meta._meta_table['Srlg.Nodes.Node.InterfaceDetails.InterfaceDetail']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-oper:interface-details'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_detail is not None:
                        for child_ref in self.interface_detail:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                    return meta._meta_table['Srlg.Nodes.Node.InterfaceDetails']['meta_info']


            class SrlgValues(object):
                """
                Set of SRLG values configured
                
                .. attribute:: srlg_value
                
                	Configured SRLG value details 
                	**type**\: list of    :py:class:`SrlgValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.SrlgValues.SrlgValue>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    self.parent = None
                    self.srlg_value = YList()
                    self.srlg_value.parent = self
                    self.srlg_value.name = 'srlg_value'


                class SrlgValue(object):
                    """
                    Configured SRLG value details 
                    
                    .. attribute:: value  <key>
                    
                    	SRLG value
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: interface_name
                    
                    	Interface name
                    	**type**\:  list of str
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        self.parent = None
                        self.value = None
                        self.interface_name = YLeafList()
                        self.interface_name.parent = self
                        self.interface_name.name = 'interface_name'

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.value is None:
                            raise YPYModelError('Key property value is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-oper:srlg-value[Cisco-IOS-XR-infra-rsi-oper:value = ' + str(self.value) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.value is not None:
                            return True

                        if self.interface_name is not None:
                            for child in self.interface_name:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                        return meta._meta_table['Srlg.Nodes.Node.SrlgValues.SrlgValue']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-oper:srlg-values'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.srlg_value is not None:
                        for child_ref in self.srlg_value:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                    return meta._meta_table['Srlg.Nodes.Node.SrlgValues']['meta_info']


            class InterfaceSrlgNames(object):
                """
                Set of SRLG names configured
                
                .. attribute:: interface_srlg_name
                
                	Configured SRLG name details 
                	**type**\: list of    :py:class:`InterfaceSrlgName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName>`
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    self.parent = None
                    self.interface_srlg_name = YList()
                    self.interface_srlg_name.parent = self
                    self.interface_srlg_name.name = 'interface_srlg_name'


                class InterfaceSrlgName(object):
                    """
                    Configured SRLG name details 
                    
                    .. attribute:: srlg_name  <key>
                    
                    	SRLG name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: interfaces
                    
                    	Interfaces information
                    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces>`
                    
                    .. attribute:: srlg_name_xr
                    
                    	SRLG name
                    	**type**\:  str
                    
                    .. attribute:: srlg_value
                    
                    	SRLG value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-rsi-oper'
                    _revision = '2015-01-07'

                    def __init__(self):
                        self.parent = None
                        self.srlg_name = None
                        self.interfaces = Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces()
                        self.interfaces.parent = self
                        self.srlg_name_xr = None
                        self.srlg_value = None


                    class Interfaces(object):
                        """
                        Interfaces information
                        
                        .. attribute:: interface_name
                        
                        	Interface name
                        	**type**\:  list of str
                        
                        

                        """

                        _prefix = 'infra-rsi-oper'
                        _revision = '2015-01-07'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = YLeafList()
                            self.interface_name.parent = self
                            self.interface_name.name = 'interface_name'

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-oper:interfaces'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.interface_name is not None:
                                for child in self.interface_name:
                                    if child is not None:
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                            return meta._meta_table['Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName.Interfaces']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.srlg_name is None:
                            raise YPYModelError('Key property srlg_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-oper:interface-srlg-name[Cisco-IOS-XR-infra-rsi-oper:srlg-name = ' + str(self.srlg_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.srlg_name is not None:
                            return True

                        if self.interfaces is not None and self.interfaces._has_data():
                            return True

                        if self.srlg_name_xr is not None:
                            return True

                        if self.srlg_value is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                        return meta._meta_table['Srlg.Nodes.Node.InterfaceSrlgNames.InterfaceSrlgName']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-oper:interface-srlg-names'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_srlg_name is not None:
                        for child_ref in self.interface_srlg_name:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                    return meta._meta_table['Srlg.Nodes.Node.InterfaceSrlgNames']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-infra-rsi-oper:srlg/Cisco-IOS-XR-infra-rsi-oper:nodes/Cisco-IOS-XR-infra-rsi-oper:node[Cisco-IOS-XR-infra-rsi-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.groups is not None and self.groups._has_data():
                    return True

                if self.inherit_nodes is not None and self.inherit_nodes._has_data():
                    return True

                if self.interface_details is not None and self.interface_details._has_data():
                    return True

                if self.interface_srlg_names is not None and self.interface_srlg_names._has_data():
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                if self.srlg_maps is not None and self.srlg_maps._has_data():
                    return True

                if self.srlg_values is not None and self.srlg_values._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                return meta._meta_table['Srlg.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-rsi-oper:srlg/Cisco-IOS-XR-infra-rsi-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
            return meta._meta_table['Srlg.Nodes']['meta_info']


    class InterfaceSrlgNames(object):
        """
        Set of SRLG names configured
        
        .. attribute:: interface_srlg_name
        
        	Configured SRLG name details 
        	**type**\: list of    :py:class:`InterfaceSrlgName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.InterfaceSrlgNames.InterfaceSrlgName>`
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2015-01-07'

        def __init__(self):
            self.parent = None
            self.interface_srlg_name = YList()
            self.interface_srlg_name.parent = self
            self.interface_srlg_name.name = 'interface_srlg_name'


        class InterfaceSrlgName(object):
            """
            Configured SRLG name details 
            
            .. attribute:: srlg_name  <key>
            
            	SRLG name
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: interfaces
            
            	Interfaces information
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces>`
            
            .. attribute:: srlg_name_xr
            
            	SRLG name
            	**type**\:  str
            
            .. attribute:: srlg_value
            
            	SRLG value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-rsi-oper'
            _revision = '2015-01-07'

            def __init__(self):
                self.parent = None
                self.srlg_name = None
                self.interfaces = Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces()
                self.interfaces.parent = self
                self.srlg_name_xr = None
                self.srlg_value = None


            class Interfaces(object):
                """
                Interfaces information
                
                .. attribute:: interface_name
                
                	Interface name
                	**type**\:  list of str
                
                

                """

                _prefix = 'infra-rsi-oper'
                _revision = '2015-01-07'

                def __init__(self):
                    self.parent = None
                    self.interface_name = YLeafList()
                    self.interface_name.parent = self
                    self.interface_name.name = 'interface_name'

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-oper:interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        for child in self.interface_name:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                    return meta._meta_table['Srlg.InterfaceSrlgNames.InterfaceSrlgName.Interfaces']['meta_info']

            @property
            def _common_path(self):
                if self.srlg_name is None:
                    raise YPYModelError('Key property srlg_name is None')

                return '/Cisco-IOS-XR-infra-rsi-oper:srlg/Cisco-IOS-XR-infra-rsi-oper:interface-srlg-names/Cisco-IOS-XR-infra-rsi-oper:interface-srlg-name[Cisco-IOS-XR-infra-rsi-oper:srlg-name = ' + str(self.srlg_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.srlg_name is not None:
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                if self.srlg_name_xr is not None:
                    return True

                if self.srlg_value is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
                return meta._meta_table['Srlg.InterfaceSrlgNames.InterfaceSrlgName']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-rsi-oper:srlg/Cisco-IOS-XR-infra-rsi-oper:interface-srlg-names'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.interface_srlg_name is not None:
                for child_ref in self.interface_srlg_name:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
            return meta._meta_table['Srlg.InterfaceSrlgNames']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-rsi-oper:srlg'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.interface_srlg_names is not None and self.interface_srlg_names._has_data():
            return True

        if self.nodes is not None and self.nodes._has_data():
            return True

        if self.srlg_maps is not None and self.srlg_maps._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
        return meta._meta_table['Srlg']['meta_info']


class SelectiveVrfDownload(object):
    """
    selective vrf download
    
    .. attribute:: state
    
    	Selective VRF Download feature state details
    	**type**\:   :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_oper.SelectiveVrfDownload.State>`
    
    

    """

    _prefix = 'infra-rsi-oper'
    _revision = '2015-01-07'

    def __init__(self):
        self.state = SelectiveVrfDownload.State()
        self.state.parent = self


    class State(object):
        """
        Selective VRF Download feature state details
        
        .. attribute:: is_svd_enabled
        
        	Is SVD Enabled Operational
        	**type**\:  bool
        
        .. attribute:: is_svd_enabled_cfg
        
        	Is SVD Enabled Config
        	**type**\:  bool
        
        

        """

        _prefix = 'infra-rsi-oper'
        _revision = '2015-01-07'

        def __init__(self):
            self.parent = None
            self.is_svd_enabled = None
            self.is_svd_enabled_cfg = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-rsi-oper:selective-vrf-download/Cisco-IOS-XR-infra-rsi-oper:state'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.is_svd_enabled is not None:
                return True

            if self.is_svd_enabled_cfg is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
            return meta._meta_table['SelectiveVrfDownload.State']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-rsi-oper:selective-vrf-download'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.state is not None and self.state._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_oper as meta
        return meta._meta_table['SelectiveVrfDownload']['meta_info']



""" Cisco_IOS_XR_ip_iarm_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-iarm package configuration.

This module contains definitions
for the following management objects\:
  ip\-arm\: IP Address Repository Manager (IPv4/IPv6 ARM)
    configuration data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IpArmConflictPolicy(Enum):
    """
    IpArmConflictPolicy (Enum Class)

    Ip arm conflict policy

    .. data:: lowest_rack_slot = 0

    	Lowest Rack/Slot

    .. data:: static = 1

    	UP interfaces unaffected

    .. data:: longest_prefix = 2

    	Longest Prefix

    .. data:: highest_ip = 4

    	Highest IP

    """

    lowest_rack_slot = Enum.YLeaf(0, "lowest-rack-slot")

    static = Enum.YLeaf(1, "static")

    longest_prefix = Enum.YLeaf(2, "longest-prefix")

    highest_ip = Enum.YLeaf(4, "highest-ip")



class IpArm(Entity):
    """
    IP Address Repository Manager (IPv4/IPv6 ARM)
    configuration data
    
    .. attribute:: ipv4
    
    	IPv4 ARM configuration
    	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg.IpArm.Ipv4>`
    
    .. attribute:: ipv6
    
    	IPv6 ARM configuration
    	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg.IpArm.Ipv6>`
    
    

    """

    _prefix = 'ip-iarm-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(IpArm, self).__init__()
        self._top_entity = None

        self.yang_name = "ip-arm"
        self.yang_parent_name = "Cisco-IOS-XR-ip-iarm-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ipv4", ("ipv4", IpArm.Ipv4)), ("ipv6", ("ipv6", IpArm.Ipv6))])
        self._leafs = OrderedDict()

        self.ipv4 = IpArm.Ipv4()
        self.ipv4.parent = self
        self._children_name_map["ipv4"] = "ipv4"

        self.ipv6 = IpArm.Ipv6()
        self.ipv6.parent = self
        self._children_name_map["ipv6"] = "ipv6"
        self._segment_path = lambda: "Cisco-IOS-XR-ip-iarm-cfg:ip-arm"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(IpArm, [], name, value)


    class Ipv4(Entity):
        """
        IPv4 ARM configuration
        
        .. attribute:: conflict_policy_table
        
        	IP ARM conflict policy configuration
        	**type**\:  :py:class:`ConflictPolicyTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg.IpArm.Ipv4.ConflictPolicyTable>`
        
        .. attribute:: multicast_host
        
        	IP ARM Multicast Host configuration
        	**type**\:  :py:class:`MulticastHost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg.IpArm.Ipv4.MulticastHost>`
        
        

        """

        _prefix = 'ip-iarm-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(IpArm.Ipv4, self).__init__()

            self.yang_name = "ipv4"
            self.yang_parent_name = "ip-arm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("conflict-policy-table", ("conflict_policy_table", IpArm.Ipv4.ConflictPolicyTable)), ("multicast-host", ("multicast_host", IpArm.Ipv4.MulticastHost))])
            self._leafs = OrderedDict()

            self.conflict_policy_table = IpArm.Ipv4.ConflictPolicyTable()
            self.conflict_policy_table.parent = self
            self._children_name_map["conflict_policy_table"] = "conflict-policy-table"

            self.multicast_host = IpArm.Ipv4.MulticastHost()
            self.multicast_host.parent = self
            self._children_name_map["multicast_host"] = "multicast-host"
            self._segment_path = lambda: "ipv4"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-iarm-cfg:ip-arm/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(IpArm.Ipv4, [], name, value)


        class ConflictPolicyTable(Entity):
            """
            IP ARM conflict policy configuration
            
            .. attribute:: conflict_policy
            
            	IP ARM conflict policy value definitions
            	**type**\:  :py:class:`IpArmConflictPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg.IpArmConflictPolicy>`
            
            

            """

            _prefix = 'ip-iarm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(IpArm.Ipv4.ConflictPolicyTable, self).__init__()

                self.yang_name = "conflict-policy-table"
                self.yang_parent_name = "ipv4"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('conflict_policy', (YLeaf(YType.enumeration, 'conflict-policy'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg', 'IpArmConflictPolicy', '')])),
                ])
                self.conflict_policy = None
                self._segment_path = lambda: "conflict-policy-table"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-iarm-cfg:ip-arm/ipv4/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(IpArm.Ipv4.ConflictPolicyTable, ['conflict_policy'], name, value)


        class MulticastHost(Entity):
            """
            IP ARM Multicast Host configuration
            
            .. attribute:: multicast_host_interface
            
            	Default multicast host interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            

            """

            _prefix = 'ip-iarm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(IpArm.Ipv4.MulticastHost, self).__init__()

                self.yang_name = "multicast-host"
                self.yang_parent_name = "ipv4"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('multicast_host_interface', (YLeaf(YType.str, 'multicast-host-interface'), ['str'])),
                ])
                self.multicast_host_interface = None
                self._segment_path = lambda: "multicast-host"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-iarm-cfg:ip-arm/ipv4/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(IpArm.Ipv4.MulticastHost, ['multicast_host_interface'], name, value)


    class Ipv6(Entity):
        """
        IPv6 ARM configuration
        
        .. attribute:: conflict_policy_table
        
        	IP ARM conflict policy configuration
        	**type**\:  :py:class:`ConflictPolicyTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg.IpArm.Ipv6.ConflictPolicyTable>`
        
        .. attribute:: multicast_host
        
        	IP ARM Multicast Host configuration
        	**type**\:  :py:class:`MulticastHost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg.IpArm.Ipv6.MulticastHost>`
        
        

        """

        _prefix = 'ip-iarm-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(IpArm.Ipv6, self).__init__()

            self.yang_name = "ipv6"
            self.yang_parent_name = "ip-arm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("conflict-policy-table", ("conflict_policy_table", IpArm.Ipv6.ConflictPolicyTable)), ("multicast-host", ("multicast_host", IpArm.Ipv6.MulticastHost))])
            self._leafs = OrderedDict()

            self.conflict_policy_table = IpArm.Ipv6.ConflictPolicyTable()
            self.conflict_policy_table.parent = self
            self._children_name_map["conflict_policy_table"] = "conflict-policy-table"

            self.multicast_host = IpArm.Ipv6.MulticastHost()
            self.multicast_host.parent = self
            self._children_name_map["multicast_host"] = "multicast-host"
            self._segment_path = lambda: "ipv6"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-iarm-cfg:ip-arm/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(IpArm.Ipv6, [], name, value)


        class ConflictPolicyTable(Entity):
            """
            IP ARM conflict policy configuration
            
            .. attribute:: conflict_policy
            
            	IP ARM conflict policy value definitions
            	**type**\:  :py:class:`IpArmConflictPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg.IpArmConflictPolicy>`
            
            

            """

            _prefix = 'ip-iarm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(IpArm.Ipv6.ConflictPolicyTable, self).__init__()

                self.yang_name = "conflict-policy-table"
                self.yang_parent_name = "ipv6"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('conflict_policy', (YLeaf(YType.enumeration, 'conflict-policy'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_cfg', 'IpArmConflictPolicy', '')])),
                ])
                self.conflict_policy = None
                self._segment_path = lambda: "conflict-policy-table"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-iarm-cfg:ip-arm/ipv6/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(IpArm.Ipv6.ConflictPolicyTable, ['conflict_policy'], name, value)


        class MulticastHost(Entity):
            """
            IP ARM Multicast Host configuration
            
            .. attribute:: multicast_host_interface
            
            	Default multicast host interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            

            """

            _prefix = 'ip-iarm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(IpArm.Ipv6.MulticastHost, self).__init__()

                self.yang_name = "multicast-host"
                self.yang_parent_name = "ipv6"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('multicast_host_interface', (YLeaf(YType.str, 'multicast-host-interface'), ['str'])),
                ])
                self.multicast_host_interface = None
                self._segment_path = lambda: "multicast-host"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-iarm-cfg:ip-arm/ipv6/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(IpArm.Ipv6.MulticastHost, ['multicast_host_interface'], name, value)

    def clone_ptr(self):
        self._top_entity = IpArm()
        return self._top_entity


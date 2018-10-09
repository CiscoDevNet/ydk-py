""" Cisco_IOS_XR_lib_mpp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lib\-mpp package operational data.

This module contains definitions
for the following management objects\:
  management\-plane\-protection\: Management Plane Protection (MPP)
    operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MppAllow(Enum):
    """
    MppAllow (Enum Class)

    MPP protocol types

    .. data:: ssh = 0

    	SSH protocol

    .. data:: telnet = 1

    	TELNET protocol

    .. data:: snmp = 2

    	SNMP protocol

    .. data:: tftp = 3

    	TFTP protocol

    .. data:: http = 4

    	HTTP protocol

    .. data:: xr_xml = 5

    	XML

    .. data:: netconf = 6

    	NETCONF protocol

    .. data:: all = 7

    	All

    """

    ssh = Enum.YLeaf(0, "ssh")

    telnet = Enum.YLeaf(1, "telnet")

    snmp = Enum.YLeaf(2, "snmp")

    tftp = Enum.YLeaf(3, "tftp")

    http = Enum.YLeaf(4, "http")

    xr_xml = Enum.YLeaf(5, "xr-xml")

    netconf = Enum.YLeaf(6, "netconf")

    all = Enum.YLeaf(7, "all")



class MppAfIdBase(Identity):
    """
    Base identity for Mpp\-af\-id
    
    

    """

    _prefix = 'Cisco-IOS-XR-lib-mpp-oper'
    _revision = '2017-05-01'

    def __init__(self, ns="http://cisco.com/ns/yang/Cisco-IOS-XR-lib-mpp-oper", pref="Cisco-IOS-XR-lib-mpp-oper", tag="Cisco-IOS-XR-lib-mpp-oper:Mpp-af-id-base"):
        super(MppAfIdBase, self).__init__(ns, pref, tag)


class ManagementPlaneProtection(Entity):
    """
    Management Plane Protection (MPP) operational
    data
    
    .. attribute:: outband
    
    	Management Plane Protection (MPP) outband interface data
    	**type**\:  :py:class:`Outband <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband>`
    
    .. attribute:: inband
    
    	Management Plane Protection (MPP) inband interface data
    	**type**\:  :py:class:`Inband <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Inband>`
    
    

    """

    _prefix = 'lib-mpp-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(ManagementPlaneProtection, self).__init__()
        self._top_entity = None

        self.yang_name = "management-plane-protection"
        self.yang_parent_name = "Cisco-IOS-XR-lib-mpp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("outband", ("outband", ManagementPlaneProtection.Outband)), ("inband", ("inband", ManagementPlaneProtection.Inband))])
        self._leafs = OrderedDict()

        self.outband = ManagementPlaneProtection.Outband()
        self.outband.parent = self
        self._children_name_map["outband"] = "outband"

        self.inband = ManagementPlaneProtection.Inband()
        self.inband.parent = self
        self._children_name_map["inband"] = "inband"
        self._segment_path = lambda: "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ManagementPlaneProtection, [], name, value)


    class Outband(Entity):
        """
        Management Plane Protection (MPP) outband
        interface data
        
        .. attribute:: vrf
        
        	Outband VRF information
        	**type**\:  :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband.Vrf>`
        
        .. attribute:: interfaces
        
        	List of inband/outband interfaces
        	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband.Interfaces>`
        
        

        """

        _prefix = 'lib-mpp-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(ManagementPlaneProtection.Outband, self).__init__()

            self.yang_name = "outband"
            self.yang_parent_name = "management-plane-protection"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vrf", ("vrf", ManagementPlaneProtection.Outband.Vrf)), ("interfaces", ("interfaces", ManagementPlaneProtection.Outband.Interfaces))])
            self._leafs = OrderedDict()

            self.vrf = ManagementPlaneProtection.Outband.Vrf()
            self.vrf.parent = self
            self._children_name_map["vrf"] = "vrf"

            self.interfaces = ManagementPlaneProtection.Outband.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._segment_path = lambda: "outband"
            self._absolute_path = lambda: "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ManagementPlaneProtection.Outband, [], name, value)


        class Vrf(Entity):
            """
            Outband VRF information
            
            .. attribute:: vrf_name
            
            	Outband VRF name
            	**type**\: str
            
            

            """

            _prefix = 'lib-mpp-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(ManagementPlaneProtection.Outband.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "outband"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                ])
                self.vrf_name = None
                self._segment_path = lambda: "vrf"
                self._absolute_path = lambda: "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/outband/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ManagementPlaneProtection.Outband.Vrf, ['vrf_name'], name, value)


        class Interfaces(Entity):
            """
            List of inband/outband interfaces
            
            .. attribute:: interface
            
            	MPP interface information
            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband.Interfaces.Interface>`
            
            

            """

            _prefix = 'lib-mpp-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(ManagementPlaneProtection.Outband.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "outband"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interface", ("interface", ManagementPlaneProtection.Outband.Interfaces.Interface))])
                self._leafs = OrderedDict()

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/outband/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ManagementPlaneProtection.Outband.Interfaces, [], name, value)


            class Interface(Entity):
                """
                MPP interface information
                
                .. attribute:: interface_name  (key)
                
                	Interface name, specify 'all' for all interfaces
                	**type**\: str
                
                .. attribute:: protocol
                
                	MPP Interface protocols
                	**type**\: list of  		 :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol>`
                
                

                """

                _prefix = 'lib-mpp-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(ManagementPlaneProtection.Outband.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_name']
                    self._child_classes = OrderedDict([("protocol", ("protocol", ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol))])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ])
                    self.interface_name = None

                    self.protocol = YList(self)
                    self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/outband/interfaces/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ManagementPlaneProtection.Outband.Interfaces.Interface, ['interface_name'], name, value)


                class Protocol(Entity):
                    """
                    MPP Interface protocols
                    
                    .. attribute:: allow
                    
                    	MPP allow
                    	**type**\:  :py:class:`MppAllow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.MppAllow>`
                    
                    .. attribute:: is_all_peers_allowed
                    
                    	If TRUE, all peers are allowed
                    	**type**\: bool
                    
                    .. attribute:: peer_address
                    
                    	List of peer addresses
                    	**type**\: list of  		 :py:class:`PeerAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol.PeerAddress>`
                    
                    

                    """

                    _prefix = 'lib-mpp-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol, self).__init__()

                        self.yang_name = "protocol"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("peer-address", ("peer_address", ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol.PeerAddress))])
                        self._leafs = OrderedDict([
                            ('allow', (YLeaf(YType.enumeration, 'allow'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'MppAllow', '')])),
                            ('is_all_peers_allowed', (YLeaf(YType.boolean, 'is-all-peers-allowed'), ['bool'])),
                        ])
                        self.allow = None
                        self.is_all_peers_allowed = None

                        self.peer_address = YList(self)
                        self._segment_path = lambda: "protocol"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol, ['allow', 'is_all_peers_allowed'], name, value)


                    class PeerAddress(Entity):
                        """
                        List of peer addresses
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`MppAfIdBase <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.MppAfIdBase>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'lib-mpp-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol.PeerAddress, self).__init__()

                            self.yang_name = "peer-address"
                            self.yang_parent_name = "protocol"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.identityref, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'MppAfIdBase')])),
                                ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None
                            self._segment_path = lambda: "peer-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol.PeerAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)


    class Inband(Entity):
        """
        Management Plane Protection (MPP) inband
        interface data
        
        .. attribute:: interfaces
        
        	List of inband/outband interfaces
        	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Inband.Interfaces>`
        
        

        """

        _prefix = 'lib-mpp-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(ManagementPlaneProtection.Inband, self).__init__()

            self.yang_name = "inband"
            self.yang_parent_name = "management-plane-protection"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interfaces", ("interfaces", ManagementPlaneProtection.Inband.Interfaces))])
            self._leafs = OrderedDict()

            self.interfaces = ManagementPlaneProtection.Inband.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._segment_path = lambda: "inband"
            self._absolute_path = lambda: "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ManagementPlaneProtection.Inband, [], name, value)


        class Interfaces(Entity):
            """
            List of inband/outband interfaces
            
            .. attribute:: interface
            
            	MPP interface information
            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Inband.Interfaces.Interface>`
            
            

            """

            _prefix = 'lib-mpp-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(ManagementPlaneProtection.Inband.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "inband"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interface", ("interface", ManagementPlaneProtection.Inband.Interfaces.Interface))])
                self._leafs = OrderedDict()

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/inband/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ManagementPlaneProtection.Inband.Interfaces, [], name, value)


            class Interface(Entity):
                """
                MPP interface information
                
                .. attribute:: interface_name  (key)
                
                	Interface name, specify 'all' for all interfaces
                	**type**\: str
                
                .. attribute:: protocol
                
                	MPP Interface protocols
                	**type**\: list of  		 :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol>`
                
                

                """

                _prefix = 'lib-mpp-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(ManagementPlaneProtection.Inband.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['interface_name']
                    self._child_classes = OrderedDict([("protocol", ("protocol", ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol))])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ])
                    self.interface_name = None

                    self.protocol = YList(self)
                    self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/inband/interfaces/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ManagementPlaneProtection.Inband.Interfaces.Interface, ['interface_name'], name, value)


                class Protocol(Entity):
                    """
                    MPP Interface protocols
                    
                    .. attribute:: allow
                    
                    	MPP allow
                    	**type**\:  :py:class:`MppAllow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.MppAllow>`
                    
                    .. attribute:: is_all_peers_allowed
                    
                    	If TRUE, all peers are allowed
                    	**type**\: bool
                    
                    .. attribute:: peer_address
                    
                    	List of peer addresses
                    	**type**\: list of  		 :py:class:`PeerAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol.PeerAddress>`
                    
                    

                    """

                    _prefix = 'lib-mpp-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol, self).__init__()

                        self.yang_name = "protocol"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("peer-address", ("peer_address", ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol.PeerAddress))])
                        self._leafs = OrderedDict([
                            ('allow', (YLeaf(YType.enumeration, 'allow'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'MppAllow', '')])),
                            ('is_all_peers_allowed', (YLeaf(YType.boolean, 'is-all-peers-allowed'), ['bool'])),
                        ])
                        self.allow = None
                        self.is_all_peers_allowed = None

                        self.peer_address = YList(self)
                        self._segment_path = lambda: "protocol"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol, ['allow', 'is_all_peers_allowed'], name, value)


                    class PeerAddress(Entity):
                        """
                        List of peer addresses
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`MppAfIdBase <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.MppAfIdBase>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'lib-mpp-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol.PeerAddress, self).__init__()

                            self.yang_name = "peer-address"
                            self.yang_parent_name = "protocol"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.identityref, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'MppAfIdBase')])),
                                ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None
                            self._segment_path = lambda: "peer-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol.PeerAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)

    def clone_ptr(self):
        self._top_entity = ManagementPlaneProtection()
        return self._top_entity

class Ipv4(MppAfIdBase):
    """
    IPv4 address family
    
    

    """

    _prefix = 'Cisco-IOS-XR-lib-mpp-oper'
    _revision = '2017-05-01'

    def __init__(self, ns="http://cisco.com/ns/yang/Cisco-IOS-XR-lib-mpp-oper", pref="Cisco-IOS-XR-lib-mpp-oper", tag="Cisco-IOS-XR-lib-mpp-oper:ipv4"):
        super(Ipv4, self).__init__(ns, pref, tag)


class Ipv6(MppAfIdBase):
    """
    IPv6 address family
    
    

    """

    _prefix = 'Cisco-IOS-XR-lib-mpp-oper'
    _revision = '2017-05-01'

    def __init__(self, ns="http://cisco.com/ns/yang/Cisco-IOS-XR-lib-mpp-oper", pref="Cisco-IOS-XR-lib-mpp-oper", tag="Cisco-IOS-XR-lib-mpp-oper:ipv6"):
        super(Ipv6, self).__init__(ns, pref, tag)



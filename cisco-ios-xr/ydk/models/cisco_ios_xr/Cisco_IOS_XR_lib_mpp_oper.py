""" Cisco_IOS_XR_lib_mpp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lib\-mpp package operational data.

This module contains definitions
for the following management objects\:
  management\-plane\-protection\: Management Plane Protection (MPP)
    operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MppAllow(Enum):
    """
    MppAllow

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



class ManagementPlaneProtection(Entity):
    """
    Management Plane Protection (MPP) operational
    data
    
    .. attribute:: inband
    
    	Management Plane Protection (MPP) inband interface data
    	**type**\:   :py:class:`Inband <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Inband>`
    
    .. attribute:: outband
    
    	Management Plane Protection (MPP) outband interface data
    	**type**\:   :py:class:`Outband <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband>`
    
    

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
        self._child_container_classes = {"inband" : ("inband", ManagementPlaneProtection.Inband), "outband" : ("outband", ManagementPlaneProtection.Outband)}
        self._child_list_classes = {}

        self.inband = ManagementPlaneProtection.Inband()
        self.inband.parent = self
        self._children_name_map["inband"] = "inband"
        self._children_yang_names.add("inband")

        self.outband = ManagementPlaneProtection.Outband()
        self.outband.parent = self
        self._children_name_map["outband"] = "outband"
        self._children_yang_names.add("outband")
        self._segment_path = lambda: "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection"


    class Inband(Entity):
        """
        Management Plane Protection (MPP) inband
        interface data
        
        .. attribute:: interfaces
        
        	List of inband/outband interfaces
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Inband.Interfaces>`
        
        

        """

        _prefix = 'lib-mpp-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(ManagementPlaneProtection.Inband, self).__init__()

            self.yang_name = "inband"
            self.yang_parent_name = "management-plane-protection"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"interfaces" : ("interfaces", ManagementPlaneProtection.Inband.Interfaces)}
            self._child_list_classes = {}

            self.interfaces = ManagementPlaneProtection.Inband.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")
            self._segment_path = lambda: "inband"
            self._absolute_path = lambda: "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/%s" % self._segment_path()


        class Interfaces(Entity):
            """
            List of inband/outband interfaces
            
            .. attribute:: interface
            
            	MPP interface information
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Inband.Interfaces.Interface>`
            
            

            """

            _prefix = 'lib-mpp-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(ManagementPlaneProtection.Inband.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "inband"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"interface" : ("interface", ManagementPlaneProtection.Inband.Interfaces.Interface)}

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/inband/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ManagementPlaneProtection.Inband.Interfaces, [], name, value)


            class Interface(Entity):
                """
                MPP interface information
                
                .. attribute:: interface_name  <key>
                
                	Interface name, specify 'all' for all interfaces
                	**type**\:  str
                
                .. attribute:: protocol
                
                	MPP Interface protocols
                	**type**\: list of    :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol>`
                
                

                """

                _prefix = 'lib-mpp-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(ManagementPlaneProtection.Inband.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"protocol" : ("protocol", ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol)}

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.protocol = YList(self)
                    self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/inband/interfaces/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ManagementPlaneProtection.Inband.Interfaces.Interface, ['interface_name'], name, value)


                class Protocol(Entity):
                    """
                    MPP Interface protocols
                    
                    .. attribute:: allow
                    
                    	MPP allow
                    	**type**\:   :py:class:`MppAllow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.MppAllow>`
                    
                    .. attribute:: is_all_peers_allowed
                    
                    	If TRUE, all peers are allowed
                    	**type**\:  bool
                    
                    .. attribute:: peer_address
                    
                    	List of peer addresses
                    	**type**\: list of    :py:class:`PeerAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol.PeerAddress>`
                    
                    

                    """

                    _prefix = 'lib-mpp-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol, self).__init__()

                        self.yang_name = "protocol"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"peer-address" : ("peer_address", ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol.PeerAddress)}

                        self.allow = YLeaf(YType.enumeration, "allow")

                        self.is_all_peers_allowed = YLeaf(YType.boolean, "is-all-peers-allowed")

                        self.peer_address = YList(self)
                        self._segment_path = lambda: "protocol"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol, ['allow', 'is_all_peers_allowed'], name, value)


                    class PeerAddress(Entity):
                        """
                        List of peer addresses
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`MppAfIdBase <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.MppAfIdBase>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\:  str
                        
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
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.af_name = YLeaf(YType.identityref, "af-name")

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                            self._segment_path = lambda: "peer-address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol.PeerAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)


    class Outband(Entity):
        """
        Management Plane Protection (MPP) outband
        interface data
        
        .. attribute:: interfaces
        
        	List of inband/outband interfaces
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband.Interfaces>`
        
        .. attribute:: vrf
        
        	Outband VRF information
        	**type**\:   :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband.Vrf>`
        
        

        """

        _prefix = 'lib-mpp-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(ManagementPlaneProtection.Outband, self).__init__()

            self.yang_name = "outband"
            self.yang_parent_name = "management-plane-protection"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"interfaces" : ("interfaces", ManagementPlaneProtection.Outband.Interfaces), "vrf" : ("vrf", ManagementPlaneProtection.Outband.Vrf)}
            self._child_list_classes = {}

            self.interfaces = ManagementPlaneProtection.Outband.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")

            self.vrf = ManagementPlaneProtection.Outband.Vrf()
            self.vrf.parent = self
            self._children_name_map["vrf"] = "vrf"
            self._children_yang_names.add("vrf")
            self._segment_path = lambda: "outband"
            self._absolute_path = lambda: "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/%s" % self._segment_path()


        class Interfaces(Entity):
            """
            List of inband/outband interfaces
            
            .. attribute:: interface
            
            	MPP interface information
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband.Interfaces.Interface>`
            
            

            """

            _prefix = 'lib-mpp-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(ManagementPlaneProtection.Outband.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "outband"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"interface" : ("interface", ManagementPlaneProtection.Outband.Interfaces.Interface)}

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/outband/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ManagementPlaneProtection.Outband.Interfaces, [], name, value)


            class Interface(Entity):
                """
                MPP interface information
                
                .. attribute:: interface_name  <key>
                
                	Interface name, specify 'all' for all interfaces
                	**type**\:  str
                
                .. attribute:: protocol
                
                	MPP Interface protocols
                	**type**\: list of    :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol>`
                
                

                """

                _prefix = 'lib-mpp-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(ManagementPlaneProtection.Outband.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"protocol" : ("protocol", ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol)}

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.protocol = YList(self)
                    self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/outband/interfaces/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ManagementPlaneProtection.Outband.Interfaces.Interface, ['interface_name'], name, value)


                class Protocol(Entity):
                    """
                    MPP Interface protocols
                    
                    .. attribute:: allow
                    
                    	MPP allow
                    	**type**\:   :py:class:`MppAllow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.MppAllow>`
                    
                    .. attribute:: is_all_peers_allowed
                    
                    	If TRUE, all peers are allowed
                    	**type**\:  bool
                    
                    .. attribute:: peer_address
                    
                    	List of peer addresses
                    	**type**\: list of    :py:class:`PeerAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol.PeerAddress>`
                    
                    

                    """

                    _prefix = 'lib-mpp-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol, self).__init__()

                        self.yang_name = "protocol"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"peer-address" : ("peer_address", ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol.PeerAddress)}

                        self.allow = YLeaf(YType.enumeration, "allow")

                        self.is_all_peers_allowed = YLeaf(YType.boolean, "is-all-peers-allowed")

                        self.peer_address = YList(self)
                        self._segment_path = lambda: "protocol"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol, ['allow', 'is_all_peers_allowed'], name, value)


                    class PeerAddress(Entity):
                        """
                        List of peer addresses
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`MppAfIdBase <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper.MppAfIdBase>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\:  str
                        
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
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.af_name = YLeaf(YType.identityref, "af-name")

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                            self._segment_path = lambda: "peer-address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol.PeerAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)


        class Vrf(Entity):
            """
            Outband VRF information
            
            .. attribute:: vrf_name
            
            	Outband VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'lib-mpp-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(ManagementPlaneProtection.Outband.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "outband"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.vrf_name = YLeaf(YType.str, "vrf-name")
                self._segment_path = lambda: "vrf"
                self._absolute_path = lambda: "Cisco-IOS-XR-lib-mpp-oper:management-plane-protection/outband/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ManagementPlaneProtection.Outband.Vrf, ['vrf_name'], name, value)

    def clone_ptr(self):
        self._top_entity = ManagementPlaneProtection()
        return self._top_entity

class MppAfIdBase(Identity):
    """
    Base identity for Mpp\-af\-id
    
    

    """

    _prefix = 'Cisco-IOS-XR-lib-mpp-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(MppAfIdBase, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XR-lib-mpp-oper", "Cisco-IOS-XR-lib-mpp-oper", "Cisco-IOS-XR-lib-mpp-oper:Mpp-af-id-base")


class Ipv4(Identity):
    """
    IPv4 address family
    
    

    """

    _prefix = 'Cisco-IOS-XR-lib-mpp-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(Ipv4, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XR-lib-mpp-oper", "Cisco-IOS-XR-lib-mpp-oper", "Cisco-IOS-XR-lib-mpp-oper:ipv4")


class Ipv6(Identity):
    """
    IPv6 address family
    
    

    """

    _prefix = 'Cisco-IOS-XR-lib-mpp-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(Ipv6, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XR-lib-mpp-oper", "Cisco-IOS-XR-lib-mpp-oper", "Cisco-IOS-XR-lib-mpp-oper:ipv6")



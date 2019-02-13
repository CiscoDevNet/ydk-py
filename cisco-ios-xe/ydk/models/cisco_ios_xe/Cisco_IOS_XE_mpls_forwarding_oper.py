""" Cisco_IOS_XE_mpls_forwarding_oper 

This module contains a collection of YANG definitions
for mpls forwarding operational data.
Copyright (c) 2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ConnectionInfoType(Enum):
    """
    ConnectionInfoType (Enum Class)

    Describes connection information types

    .. data:: information_string = 0

    	Connection information string

    .. data:: ip_prefix = 1

    	IP prefix for the connection

    """

    information_string = Enum.YLeaf(0, "information-string")

    ip_prefix = Enum.YLeaf(1, "ip-prefix")


class ForwardingNextHopType(Enum):
    """
    ForwardingNextHopType (Enum Class)

    Describes supported next hop types

    .. data:: point2point = 0

    	Next hop is via a P2P link

    .. data:: next_hop_ip_address = 1

    	Next hop IP address

    """

    point2point = Enum.YLeaf(0, "point2point")

    next_hop_ip_address = Enum.YLeaf(1, "next-hop-ip-address")


class OutgoingInterfaceDescriptionType(Enum):
    """
    OutgoingInterfaceDescriptionType (Enum Class)

    Describes outgoing interface information types

    .. data:: interface_type = 0

    	Forwarding path's outgoing interface type

    .. data:: interface_value = 1

    	Forwarding path's outgoing interface value

    """

    interface_type = Enum.YLeaf(0, "interface-type")

    interface_value = Enum.YLeaf(1, "interface-value")


class OutgoingInterfaceType(Enum):
    """
    OutgoingInterfaceType (Enum Class)

    Describes supported outgoing interface types

    .. data:: drop = 0

    	Outgoing interface is not found

    .. data:: punt = 1

    	Punt packets to cpu

    .. data:: aggregate = 2

    	Aggregate interface (e.g., used for VPN label allocation)

    .. data:: exception = 3

    	Exception

    .. data:: none = 4

    	No outgoing interface

    """

    drop = Enum.YLeaf(0, "drop")

    punt = Enum.YLeaf(1, "punt")

    aggregate = Enum.YLeaf(2, "aggregate")

    exception = Enum.YLeaf(3, "exception")

    none = Enum.YLeaf(4, "none")


class OutgoingLabelType(Enum):
    """
    OutgoingLabelType (Enum Class)

    Describes supported outgoing label types

    .. data:: no_label = 0

    	A label is not present

    .. data:: pop_label = 1

    	Label is poped

    .. data:: ipv4_explicit_null = 2

    	IPv4 explicit NULL label is present

    .. data:: ipv6_explicit_null = 3

    	IPv6 explicit NULL label is present

    .. data:: regular_label = 4

    	A regular MPLS label is present

    .. data:: invalid_label = 5

    	An invalid label is present

    """

    no_label = Enum.YLeaf(0, "no-label")

    pop_label = Enum.YLeaf(1, "pop-label")

    ipv4_explicit_null = Enum.YLeaf(2, "ipv4-explicit-null")

    ipv6_explicit_null = Enum.YLeaf(3, "ipv6-explicit-null")

    regular_label = Enum.YLeaf(4, "regular-label")

    invalid_label = Enum.YLeaf(5, "invalid-label")



class MplsForwardingOperData(Entity):
    """
    MPLS forwarding operatinal data
    
    .. attribute:: mpls_local_label
    
    	Local label information
    	**type**\: list of  		 :py:class:`MplsLocalLabel <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_forwarding_oper.MplsForwardingOperData.MplsLocalLabel>`
    
    	**config**\: False
    
    .. attribute:: mpls_local_label_statistics
    
    	Statistics for forwarding paths of the local labels
    	**type**\: list of  		 :py:class:`MplsLocalLabelStatistics <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_forwarding_oper.MplsForwardingOperData.MplsLocalLabelStatistics>`
    
    	**config**\: False
    
    

    """

    _prefix = 'mpls-forwarding-ios-xe-oper'
    _revision = '2017-11-01'

    def __init__(self):
        super(MplsForwardingOperData, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls-forwarding-oper-data"
        self.yang_parent_name = "Cisco-IOS-XE-mpls-forwarding-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("mpls-local-label", ("mpls_local_label", MplsForwardingOperData.MplsLocalLabel)), ("mpls-local-label-statistics", ("mpls_local_label_statistics", MplsForwardingOperData.MplsLocalLabelStatistics))])
        self._leafs = OrderedDict()

        self.mpls_local_label = YList(self)
        self.mpls_local_label_statistics = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-mpls-forwarding-oper:mpls-forwarding-oper-data"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(MplsForwardingOperData, [], name, value)


    class MplsLocalLabel(Entity):
        """
        Local label information
        
        .. attribute:: local_label  (key)
        
        	Value of local label
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: connection_information
        
        	Connection information for the local label
        	**type**\:  :py:class:`ConnectionInformation <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_forwarding_oper.MplsForwardingOperData.MplsLocalLabel.ConnectionInformation>`
        
        	**config**\: False
        
        .. attribute:: forwarding_paths
        
        	ECMP paths for the local label
        	**type**\: list of  		 :py:class:`ForwardingPaths <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_forwarding_oper.MplsForwardingOperData.MplsLocalLabel.ForwardingPaths>`
        
        	**config**\: False
        
        

        """

        _prefix = 'mpls-forwarding-ios-xe-oper'
        _revision = '2017-11-01'

        def __init__(self):
            super(MplsForwardingOperData.MplsLocalLabel, self).__init__()

            self.yang_name = "mpls-local-label"
            self.yang_parent_name = "mpls-forwarding-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['local_label']
            self._child_classes = OrderedDict([("connection-information", ("connection_information", MplsForwardingOperData.MplsLocalLabel.ConnectionInformation)), ("forwarding-paths", ("forwarding_paths", MplsForwardingOperData.MplsLocalLabel.ForwardingPaths))])
            self._leafs = OrderedDict([
                ('local_label', (YLeaf(YType.uint32, 'local-label'), ['int'])),
            ])
            self.local_label = None

            self.connection_information = MplsForwardingOperData.MplsLocalLabel.ConnectionInformation()
            self.connection_information.parent = self
            self._children_name_map["connection_information"] = "connection-information"

            self.forwarding_paths = YList(self)
            self._segment_path = lambda: "mpls-local-label" + "[local-label='" + str(self.local_label) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-mpls-forwarding-oper:mpls-forwarding-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MplsForwardingOperData.MplsLocalLabel, ['local_label'], name, value)


        class ConnectionInformation(Entity):
            """
            Connection information for the local label
            
            .. attribute:: info_str
            
            	Connection information string
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: ip_prefix
            
            	IP prefix for the connection
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
            
            	**config**\: False
            
            

            """

            _prefix = 'mpls-forwarding-ios-xe-oper'
            _revision = '2017-11-01'

            def __init__(self):
                super(MplsForwardingOperData.MplsLocalLabel.ConnectionInformation, self).__init__()

                self.yang_name = "connection-information"
                self.yang_parent_name = "mpls-local-label"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('info_str', (YLeaf(YType.str, 'info-str'), ['str'])),
                    ('ip_prefix', (YLeaf(YType.str, 'ip-prefix'), ['str','str'])),
                ])
                self.info_str = None
                self.ip_prefix = None
                self._segment_path = lambda: "connection-information"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsForwardingOperData.MplsLocalLabel.ConnectionInformation, ['info_str', 'ip_prefix'], name, value)



        class ForwardingPaths(Entity):
            """
            ECMP paths for the local label
            
            .. attribute:: outgoing_interface
            
            	Outgoing interface information
            	**type**\:  :py:class:`OutgoingInterface <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_forwarding_oper.MplsForwardingOperData.MplsLocalLabel.ForwardingPaths.OutgoingInterface>`
            
            	**config**\: False
            
            .. attribute:: outgoing_label
            
            	Outgoing label information
            	**type**\:  :py:class:`OutgoingLabel <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_forwarding_oper.MplsForwardingOperData.MplsLocalLabel.ForwardingPaths.OutgoingLabel>`
            
            	**config**\: False
            
            .. attribute:: next_hop
            
            	Next hop information
            	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_forwarding_oper.MplsForwardingOperData.MplsLocalLabel.ForwardingPaths.NextHop>`
            
            	**config**\: False
            
            

            """

            _prefix = 'mpls-forwarding-ios-xe-oper'
            _revision = '2017-11-01'

            def __init__(self):
                super(MplsForwardingOperData.MplsLocalLabel.ForwardingPaths, self).__init__()

                self.yang_name = "forwarding-paths"
                self.yang_parent_name = "mpls-local-label"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("outgoing-interface", ("outgoing_interface", MplsForwardingOperData.MplsLocalLabel.ForwardingPaths.OutgoingInterface)), ("outgoing-label", ("outgoing_label", MplsForwardingOperData.MplsLocalLabel.ForwardingPaths.OutgoingLabel)), ("next-hop", ("next_hop", MplsForwardingOperData.MplsLocalLabel.ForwardingPaths.NextHop))])
                self._leafs = OrderedDict()

                self.outgoing_interface = MplsForwardingOperData.MplsLocalLabel.ForwardingPaths.OutgoingInterface()
                self.outgoing_interface.parent = self
                self._children_name_map["outgoing_interface"] = "outgoing-interface"

                self.outgoing_label = MplsForwardingOperData.MplsLocalLabel.ForwardingPaths.OutgoingLabel()
                self.outgoing_label.parent = self
                self._children_name_map["outgoing_label"] = "outgoing-label"

                self.next_hop = MplsForwardingOperData.MplsLocalLabel.ForwardingPaths.NextHop()
                self.next_hop.parent = self
                self._children_name_map["next_hop"] = "next-hop"
                self._segment_path = lambda: "forwarding-paths"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsForwardingOperData.MplsLocalLabel.ForwardingPaths, [], name, value)


            class OutgoingInterface(Entity):
                """
                Outgoing interface information
                
                .. attribute:: interface_type
                
                	Outgoing interface type
                	**type**\:  :py:class:`OutgoingInterfaceType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_forwarding_oper.OutgoingInterfaceType>`
                
                	**config**\: False
                
                .. attribute:: interface_value
                
                	Outgoing interface value
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'mpls-forwarding-ios-xe-oper'
                _revision = '2017-11-01'

                def __init__(self):
                    super(MplsForwardingOperData.MplsLocalLabel.ForwardingPaths.OutgoingInterface, self).__init__()

                    self.yang_name = "outgoing-interface"
                    self.yang_parent_name = "forwarding-paths"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_type', (YLeaf(YType.enumeration, 'interface-type'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_forwarding_oper', 'OutgoingInterfaceType', '')])),
                        ('interface_value', (YLeaf(YType.str, 'interface-value'), ['str'])),
                    ])
                    self.interface_type = None
                    self.interface_value = None
                    self._segment_path = lambda: "outgoing-interface"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsForwardingOperData.MplsLocalLabel.ForwardingPaths.OutgoingInterface, ['interface_type', 'interface_value'], name, value)



            class OutgoingLabel(Entity):
                """
                Outgoing label information
                
                .. attribute:: no_label
                
                	True if a label is not present
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: pop_label
                
                	Pop label value
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: ipv4_explicit_null
                
                	IPv4 explicit null label value
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: ipv6_explicit_null
                
                	IPv6 explicit null label value
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: regular_label
                
                	Regular label value
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: invalid_label
                
                	True if a label with a value that is outside IETF acceptable label range is present
                	**type**\: bool
                
                	**config**\: False
                
                

                """

                _prefix = 'mpls-forwarding-ios-xe-oper'
                _revision = '2017-11-01'

                def __init__(self):
                    super(MplsForwardingOperData.MplsLocalLabel.ForwardingPaths.OutgoingLabel, self).__init__()

                    self.yang_name = "outgoing-label"
                    self.yang_parent_name = "forwarding-paths"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('no_label', (YLeaf(YType.boolean, 'no-label'), ['bool'])),
                        ('pop_label', (YLeaf(YType.uint32, 'pop-label'), ['int'])),
                        ('ipv4_explicit_null', (YLeaf(YType.uint32, 'ipv4-explicit-null'), ['int'])),
                        ('ipv6_explicit_null', (YLeaf(YType.uint32, 'ipv6-explicit-null'), ['int'])),
                        ('regular_label', (YLeaf(YType.uint32, 'regular-label'), ['int'])),
                        ('invalid_label', (YLeaf(YType.boolean, 'invalid-label'), ['bool'])),
                    ])
                    self.no_label = None
                    self.pop_label = None
                    self.ipv4_explicit_null = None
                    self.ipv6_explicit_null = None
                    self.regular_label = None
                    self.invalid_label = None
                    self._segment_path = lambda: "outgoing-label"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsForwardingOperData.MplsLocalLabel.ForwardingPaths.OutgoingLabel, ['no_label', 'pop_label', 'ipv4_explicit_null', 'ipv6_explicit_null', 'regular_label', 'invalid_label'], name, value)



            class NextHop(Entity):
                """
                Next hop information
                
                .. attribute:: p2p
                
                	True if next hop is via a p2p link
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: ip_address
                
                	Next hop ip address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                

                """

                _prefix = 'mpls-forwarding-ios-xe-oper'
                _revision = '2017-11-01'

                def __init__(self):
                    super(MplsForwardingOperData.MplsLocalLabel.ForwardingPaths.NextHop, self).__init__()

                    self.yang_name = "next-hop"
                    self.yang_parent_name = "forwarding-paths"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('p2p', (YLeaf(YType.boolean, 'p2p'), ['bool'])),
                        ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
                    ])
                    self.p2p = None
                    self.ip_address = None
                    self._segment_path = lambda: "next-hop"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsForwardingOperData.MplsLocalLabel.ForwardingPaths.NextHop, ['p2p', 'ip_address'], name, value)





    class MplsLocalLabelStatistics(Entity):
        """
        Statistics for forwarding paths of the local labels
        
        .. attribute:: local_label  (key)
        
        	Value of local label
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: forwarding_path_index  (key)
        
        	Path index among ECMP paths for the same local label
        	**type**\: int
        
        	**range:** 0..255
        
        	**config**\: False
        
        .. attribute:: label_switched_bytes
        
        	Number of bytes switched to a particular ECMP path
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        .. attribute:: label_switched_packets
        
        	Number of packets switched to a particular ECMP path
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        	**config**\: False
        
        

        """

        _prefix = 'mpls-forwarding-ios-xe-oper'
        _revision = '2017-11-01'

        def __init__(self):
            super(MplsForwardingOperData.MplsLocalLabelStatistics, self).__init__()

            self.yang_name = "mpls-local-label-statistics"
            self.yang_parent_name = "mpls-forwarding-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['local_label','forwarding_path_index']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('local_label', (YLeaf(YType.uint32, 'local-label'), ['int'])),
                ('forwarding_path_index', (YLeaf(YType.uint8, 'forwarding-path-index'), ['int'])),
                ('label_switched_bytes', (YLeaf(YType.uint64, 'label-switched-bytes'), ['int'])),
                ('label_switched_packets', (YLeaf(YType.uint64, 'label-switched-packets'), ['int'])),
            ])
            self.local_label = None
            self.forwarding_path_index = None
            self.label_switched_bytes = None
            self.label_switched_packets = None
            self._segment_path = lambda: "mpls-local-label-statistics" + "[local-label='" + str(self.local_label) + "']" + "[forwarding-path-index='" + str(self.forwarding_path_index) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-mpls-forwarding-oper:mpls-forwarding-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MplsForwardingOperData.MplsLocalLabelStatistics, ['local_label', 'forwarding_path_index', 'label_switched_bytes', 'label_switched_packets'], name, value)


    def clone_ptr(self):
        self._top_entity = MplsForwardingOperData()
        return self._top_entity




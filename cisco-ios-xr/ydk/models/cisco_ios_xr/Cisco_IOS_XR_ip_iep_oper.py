""" Cisco_IOS_XR_ip_iep_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-iep package operational data.

This module contains definitions
for the following management objects\:
  explicit\-paths\: Configured IP explicit paths

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class IepAddress(Enum):
    """
    IepAddress

    Address types

    .. data:: next = 0

    	Address type is next

    .. data:: exclude = 1

    	Address type is exclude

    .. data:: exclude_srlg = 2

    	Address type is exclude SRLG

    """

    next = Enum.YLeaf(0, "next")

    exclude = Enum.YLeaf(1, "exclude")

    exclude_srlg = Enum.YLeaf(2, "exclude-srlg")


class IepHop(Enum):
    """
    IepHop

    Hop types of the next\-address configured

    .. data:: strict = 0

    	Hop type is strict

    .. data:: loose = 1

    	Hop type is loose

    """

    strict = Enum.YLeaf(0, "strict")

    loose = Enum.YLeaf(1, "loose")


class IepStatus(Enum):
    """
    IepStatus

    Status of the path

    .. data:: enabled = 0

    	Status is enabled

    .. data:: disabled = 1

    	Status is disabled

    """

    enabled = Enum.YLeaf(0, "enabled")

    disabled = Enum.YLeaf(1, "disabled")



class ExplicitPaths(Entity):
    """
    Configured IP explicit paths
    
    .. attribute:: identifiers
    
    	List of configured IP explicit path identifiers, this corresponds to mplsTunnelHopTable in TE MIB
    	**type**\:   :py:class:`Identifiers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.ExplicitPaths.Identifiers>`
    
    .. attribute:: names
    
    	List of configured IP explicit path names, this corresponds to mplsTunnelHopTable in TE MIB
    	**type**\:   :py:class:`Names <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.ExplicitPaths.Names>`
    
    

    """

    _prefix = 'ip-iep-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(ExplicitPaths, self).__init__()
        self._top_entity = None

        self.yang_name = "explicit-paths"
        self.yang_parent_name = "Cisco-IOS-XR-ip-iep-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"identifiers" : ("identifiers", ExplicitPaths.Identifiers), "names" : ("names", ExplicitPaths.Names)}
        self._child_list_classes = {}

        self.identifiers = ExplicitPaths.Identifiers()
        self.identifiers.parent = self
        self._children_name_map["identifiers"] = "identifiers"
        self._children_yang_names.add("identifiers")

        self.names = ExplicitPaths.Names()
        self.names.parent = self
        self._children_name_map["names"] = "names"
        self._children_yang_names.add("names")
        self._segment_path = lambda: "Cisco-IOS-XR-ip-iep-oper:explicit-paths"


    class Identifiers(Entity):
        """
        List of configured IP explicit path identifiers,
        this corresponds to mplsTunnelHopTable in TE MIB
        
        .. attribute:: identifier
        
        	IP explicit path configured for a particular identifier
        	**type**\: list of    :py:class:`Identifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.ExplicitPaths.Identifiers.Identifier>`
        
        

        """

        _prefix = 'ip-iep-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ExplicitPaths.Identifiers, self).__init__()

            self.yang_name = "identifiers"
            self.yang_parent_name = "explicit-paths"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"identifier" : ("identifier", ExplicitPaths.Identifiers.Identifier)}

            self.identifier = YList(self)
            self._segment_path = lambda: "identifiers"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-iep-oper:explicit-paths/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ExplicitPaths.Identifiers, [], name, value)


        class Identifier(Entity):
            """
            IP explicit path configured for a particular
            identifier
            
            .. attribute:: identifier_id  <key>
            
            	Identifier ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: address
            
            	List of IP addresses configured in the explicit path
            	**type**\: list of    :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.ExplicitPaths.Identifiers.Identifier.Address>`
            
            .. attribute:: status
            
            	Status of the path
            	**type**\:   :py:class:`IepStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.IepStatus>`
            
            

            """

            _prefix = 'ip-iep-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ExplicitPaths.Identifiers.Identifier, self).__init__()

                self.yang_name = "identifier"
                self.yang_parent_name = "identifiers"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"address" : ("address", ExplicitPaths.Identifiers.Identifier.Address)}

                self.identifier_id = YLeaf(YType.int32, "identifier-id")

                self.status = YLeaf(YType.enumeration, "status")

                self.address = YList(self)
                self._segment_path = lambda: "identifier" + "[identifier-id='" + self.identifier_id.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-iep-oper:explicit-paths/identifiers/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ExplicitPaths.Identifiers.Identifier, ['identifier_id', 'status'], name, value)


            class Address(Entity):
                """
                List of IP addresses configured in the explicit
                path
                
                .. attribute:: address
                
                	IPv4 unicast address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: address_type
                
                	Specifies the address type
                	**type**\:   :py:class:`IepAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.IepAddress>`
                
                .. attribute:: hop_type
                
                	Specifies the next unicast address in the path as a strict or loose hop
                	**type**\:   :py:class:`IepHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.IepHop>`
                
                .. attribute:: if_index
                
                	Interface Index of the path
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: index
                
                	Index number at which the path entry is inserted or modified
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: mpls_label
                
                	MPLS label
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-iep-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ExplicitPaths.Identifiers.Identifier.Address, self).__init__()

                    self.yang_name = "address"
                    self.yang_parent_name = "identifier"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.address = YLeaf(YType.str, "address")

                    self.address_type = YLeaf(YType.enumeration, "address-type")

                    self.hop_type = YLeaf(YType.enumeration, "hop-type")

                    self.if_index = YLeaf(YType.uint32, "if-index")

                    self.index = YLeaf(YType.uint32, "index")

                    self.mpls_label = YLeaf(YType.uint32, "mpls-label")
                    self._segment_path = lambda: "address"

                def __setattr__(self, name, value):
                    self._perform_setattr(ExplicitPaths.Identifiers.Identifier.Address, ['address', 'address_type', 'hop_type', 'if_index', 'index', 'mpls_label'], name, value)


    class Names(Entity):
        """
        List of configured IP explicit path names, this
        corresponds to mplsTunnelHopTable in TE MIB
        
        .. attribute:: name
        
        	IP explicit path configured for a particular path name
        	**type**\: list of    :py:class:`Name <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.ExplicitPaths.Names.Name>`
        
        

        """

        _prefix = 'ip-iep-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ExplicitPaths.Names, self).__init__()

            self.yang_name = "names"
            self.yang_parent_name = "explicit-paths"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"name" : ("name", ExplicitPaths.Names.Name)}

            self.name = YList(self)
            self._segment_path = lambda: "names"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-iep-oper:explicit-paths/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ExplicitPaths.Names, [], name, value)


        class Name(Entity):
            """
            IP explicit path configured for a particular
            path name
            
            .. attribute:: path_name  <key>
            
            	Path name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: address
            
            	List of IP addresses configured in the explicit path
            	**type**\: list of    :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.ExplicitPaths.Names.Name.Address>`
            
            .. attribute:: status
            
            	Status of the path
            	**type**\:   :py:class:`IepStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.IepStatus>`
            
            

            """

            _prefix = 'ip-iep-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ExplicitPaths.Names.Name, self).__init__()

                self.yang_name = "name"
                self.yang_parent_name = "names"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"address" : ("address", ExplicitPaths.Names.Name.Address)}

                self.path_name = YLeaf(YType.str, "path-name")

                self.status = YLeaf(YType.enumeration, "status")

                self.address = YList(self)
                self._segment_path = lambda: "name" + "[path-name='" + self.path_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-iep-oper:explicit-paths/names/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ExplicitPaths.Names.Name, ['path_name', 'status'], name, value)


            class Address(Entity):
                """
                List of IP addresses configured in the explicit
                path
                
                .. attribute:: address
                
                	IPv4 unicast address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: address_type
                
                	Specifies the address type
                	**type**\:   :py:class:`IepAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.IepAddress>`
                
                .. attribute:: hop_type
                
                	Specifies the next unicast address in the path as a strict or loose hop
                	**type**\:   :py:class:`IepHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.IepHop>`
                
                .. attribute:: if_index
                
                	Interface Index of the path
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: index
                
                	Index number at which the path entry is inserted or modified
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: mpls_label
                
                	MPLS label
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-iep-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ExplicitPaths.Names.Name.Address, self).__init__()

                    self.yang_name = "address"
                    self.yang_parent_name = "name"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.address = YLeaf(YType.str, "address")

                    self.address_type = YLeaf(YType.enumeration, "address-type")

                    self.hop_type = YLeaf(YType.enumeration, "hop-type")

                    self.if_index = YLeaf(YType.uint32, "if-index")

                    self.index = YLeaf(YType.uint32, "index")

                    self.mpls_label = YLeaf(YType.uint32, "mpls-label")
                    self._segment_path = lambda: "address"

                def __setattr__(self, name, value):
                    self._perform_setattr(ExplicitPaths.Names.Name.Address, ['address', 'address_type', 'hop_type', 'if_index', 'index', 'mpls_label'], name, value)

    def clone_ptr(self):
        self._top_entity = ExplicitPaths()
        return self._top_entity


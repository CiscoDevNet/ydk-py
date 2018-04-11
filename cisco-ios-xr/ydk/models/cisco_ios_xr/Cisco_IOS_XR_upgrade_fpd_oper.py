""" Cisco_IOS_XR_upgrade_fpd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR upgrade\-fpd package operational data.

This module contains definitions
for the following management objects\:
  fpd\: Field programmable device (FPD) operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Fpd(Enum):
    """
    Fpd (Enum Class)

    Fpd

    .. data:: spa = 0

    	SPA class of fpd

    .. data:: lc = 1

    	Linecard class of fpd

    .. data:: sam = 2

    	SAM class of fpd

    """

    spa = Enum.YLeaf(0, "spa")

    lc = Enum.YLeaf(1, "lc")

    sam = Enum.YLeaf(2, "sam")


class Fpd1(Enum):
    """
    Fpd1 (Enum Class)

    FPD types

    .. data:: spa = 0

    	Shared port adapter

    .. data:: lc = 1

    	Line card

    .. data:: sam = 2

    	Service acceleration module

    """

    spa = Enum.YLeaf(0, "spa")

    lc = Enum.YLeaf(1, "lc")

    sam = Enum.YLeaf(2, "sam")


class FpdSub(Enum):
    """
    FpdSub (Enum Class)

    Fpd sub

    .. data:: fpga1 = 0

    	FPGA device

    .. data:: rommon = 1

    	ROMMON device

    .. data:: rommona = 2

    	ROMMON device #A

    .. data:: fabldr = 3

    	Fabric loader

    .. data:: fpga2 = 4

    	FPGA device #2

    .. data:: fpga3 = 5

    	FPGA device #3

    .. data:: fpga4 = 6

    	FPGA device #4

    .. data:: fpga5 = 7

    	FPGA device #5

    .. data:: fpga6 = 8

    	FPGA device #6

    .. data:: fpga7 = 9

    	FPGA device #7

    .. data:: fpga8 = 10

    	FPGA device #8

    .. data:: fpga9 = 11

    	FPGA device #9

    .. data:: fpga10 = 12

    	FPGA device #10

    .. data:: fpga11 = 13

    	FPGA device #11

    .. data:: fpga12 = 14

    	FPGA device #12

    .. data:: fpga13 = 15

    	FPGA device #13

    .. data:: fpga14 = 16

    	FPGA device #14

    .. data:: cpld1 = 17

    	CPLD device #1

    .. data:: cpld2 = 18

    	CPLD device #2

    .. data:: cpld3 = 19

    	CPLD device #3

    .. data:: cpld4 = 20

    	CPLD device #4

    .. data:: cpld5 = 21

    	CPLD device #5

    .. data:: cpld6 = 22

    	CPLD device #6

    .. data:: cbc = 23

    	Can bus controller

    .. data:: hsbi = 24

    	HSBI image

    .. data:: txpod = 25

    	Fabric Tx POD

    .. data:: rxpod = 26

    	Fabric Rx POD

    .. data:: ibmc = 27

    	IBMC

    .. data:: fsbl = 28

    	FSBL

    .. data:: lnx = 29

    	Linux firmware

    .. data:: fpga15 = 30

    	FPGA device #15

    .. data:: fpga16 = 31

    	FPGA device #16

    .. data:: fc_fsbl = 32

    	FC FSBL

    .. data:: fc_lnx = 33

    	FC linux firmware

    """

    fpga1 = Enum.YLeaf(0, "fpga1")

    rommon = Enum.YLeaf(1, "rommon")

    rommona = Enum.YLeaf(2, "rommona")

    fabldr = Enum.YLeaf(3, "fabldr")

    fpga2 = Enum.YLeaf(4, "fpga2")

    fpga3 = Enum.YLeaf(5, "fpga3")

    fpga4 = Enum.YLeaf(6, "fpga4")

    fpga5 = Enum.YLeaf(7, "fpga5")

    fpga6 = Enum.YLeaf(8, "fpga6")

    fpga7 = Enum.YLeaf(9, "fpga7")

    fpga8 = Enum.YLeaf(10, "fpga8")

    fpga9 = Enum.YLeaf(11, "fpga9")

    fpga10 = Enum.YLeaf(12, "fpga10")

    fpga11 = Enum.YLeaf(13, "fpga11")

    fpga12 = Enum.YLeaf(14, "fpga12")

    fpga13 = Enum.YLeaf(15, "fpga13")

    fpga14 = Enum.YLeaf(16, "fpga14")

    cpld1 = Enum.YLeaf(17, "cpld1")

    cpld2 = Enum.YLeaf(18, "cpld2")

    cpld3 = Enum.YLeaf(19, "cpld3")

    cpld4 = Enum.YLeaf(20, "cpld4")

    cpld5 = Enum.YLeaf(21, "cpld5")

    cpld6 = Enum.YLeaf(22, "cpld6")

    cbc = Enum.YLeaf(23, "cbc")

    hsbi = Enum.YLeaf(24, "hsbi")

    txpod = Enum.YLeaf(25, "txpod")

    rxpod = Enum.YLeaf(26, "rxpod")

    ibmc = Enum.YLeaf(27, "ibmc")

    fsbl = Enum.YLeaf(28, "fsbl")

    lnx = Enum.YLeaf(29, "lnx")

    fpga15 = Enum.YLeaf(30, "fpga15")

    fpga16 = Enum.YLeaf(31, "fpga16")

    fc_fsbl = Enum.YLeaf(32, "fc-fsbl")

    fc_lnx = Enum.YLeaf(33, "fc-lnx")


class FpdSub1(Enum):
    """
    FpdSub1 (Enum Class)

    FPD sub types

    .. data:: fpga1 = 0

    	FPGA device

    .. data:: rommon = 1

    	ROMMON device

    .. data:: rommona = 2

    	ROMMONA device

    .. data:: fabric_loader = 3

    	Fabric loader

    .. data:: fpga2 = 4

    	FPGA device

    .. data:: fpga3 = 5

    	FPGA device

    .. data:: fpga4 = 6

    	FPGA device

    .. data:: fpga5 = 7

    	FPGA device

    .. data:: fpga6 = 8

    	FPGA device

    .. data:: fpga7 = 9

    	FPGA device

    .. data:: fpga8 = 10

    	FPGA device

    .. data:: fpga9 = 11

    	FPGA device

    .. data:: fpga10 = 12

    	FPGA device

    .. data:: fpga11 = 13

    	FPGA device

    .. data:: fpga12 = 14

    	FPGA device

    .. data:: fpga13 = 15

    	FPGA device

    .. data:: fpga14 = 16

    	FPGA device

    .. data:: cpld1 = 17

    	CPLD device

    .. data:: cpld2 = 18

    	CPLD device

    .. data:: cpld3 = 19

    	CPLD device

    .. data:: cpld4 = 20

    	CPLD device

    .. data:: cpld5 = 21

    	CPLD device

    .. data:: cpld6 = 22

    	CPLD device

    .. data:: cbc = 23

    	CAN bus controller

    .. data:: hsbi = 24

    	HSBI image

    .. data:: txpod = 25

    	Fabric Tx POD

    .. data:: rxpod = 26

    	Fabric Rx POD

    .. data:: ibmc = 27

    	IBMC

    .. data:: fsbl = 28

    	FSBL

    .. data:: lnx = 29

    	Linux firmware

    .. data:: fpga15 = 30

    	FPGA device

    .. data:: fpga16 = 31

    	FPGA device

    .. data:: fc_fsbl = 32

    	FC FSBL

    .. data:: fc_lnx = 33

    	FC linux firmware

    """

    fpga1 = Enum.YLeaf(0, "fpga1")

    rommon = Enum.YLeaf(1, "rommon")

    rommona = Enum.YLeaf(2, "rommona")

    fabric_loader = Enum.YLeaf(3, "fabric-loader")

    fpga2 = Enum.YLeaf(4, "fpga2")

    fpga3 = Enum.YLeaf(5, "fpga3")

    fpga4 = Enum.YLeaf(6, "fpga4")

    fpga5 = Enum.YLeaf(7, "fpga5")

    fpga6 = Enum.YLeaf(8, "fpga6")

    fpga7 = Enum.YLeaf(9, "fpga7")

    fpga8 = Enum.YLeaf(10, "fpga8")

    fpga9 = Enum.YLeaf(11, "fpga9")

    fpga10 = Enum.YLeaf(12, "fpga10")

    fpga11 = Enum.YLeaf(13, "fpga11")

    fpga12 = Enum.YLeaf(14, "fpga12")

    fpga13 = Enum.YLeaf(15, "fpga13")

    fpga14 = Enum.YLeaf(16, "fpga14")

    cpld1 = Enum.YLeaf(17, "cpld1")

    cpld2 = Enum.YLeaf(18, "cpld2")

    cpld3 = Enum.YLeaf(19, "cpld3")

    cpld4 = Enum.YLeaf(20, "cpld4")

    cpld5 = Enum.YLeaf(21, "cpld5")

    cpld6 = Enum.YLeaf(22, "cpld6")

    cbc = Enum.YLeaf(23, "cbc")

    hsbi = Enum.YLeaf(24, "hsbi")

    txpod = Enum.YLeaf(25, "txpod")

    rxpod = Enum.YLeaf(26, "rxpod")

    ibmc = Enum.YLeaf(27, "ibmc")

    fsbl = Enum.YLeaf(28, "fsbl")

    lnx = Enum.YLeaf(29, "lnx")

    fpga15 = Enum.YLeaf(30, "fpga15")

    fpga16 = Enum.YLeaf(31, "fpga16")

    fc_fsbl = Enum.YLeaf(32, "fc-fsbl")

    fc_lnx = Enum.YLeaf(33, "fc-lnx")



class Fpd_(Entity):
    """
    Field programmable device (FPD) operational data
    
    .. attribute:: nodes
    
    	List of FPD supported nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.Fpd_.Nodes>`
    
    .. attribute:: packages
    
    	FPD packages information
    	**type**\:  :py:class:`Packages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.Fpd_.Packages>`
    
    

    """

    _prefix = 'upgrade-fpd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Fpd_, self).__init__()
        self._top_entity = None

        self.yang_name = "fpd"
        self.yang_parent_name = "Cisco-IOS-XR-upgrade-fpd-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("nodes", ("nodes", Fpd_.Nodes)), ("packages", ("packages", Fpd_.Packages))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.nodes = Fpd_.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")

        self.packages = Fpd_.Packages()
        self.packages.parent = self
        self._children_name_map["packages"] = "packages"
        self._children_yang_names.add("packages")
        self._segment_path = lambda: "Cisco-IOS-XR-upgrade-fpd-oper:fpd"


    class Nodes(Entity):
        """
        List of FPD supported nodes
        
        .. attribute:: node
        
        	Information about a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.Fpd_.Nodes.Node>`
        
        

        """

        _prefix = 'upgrade-fpd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Fpd_.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "fpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", Fpd_.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-upgrade-fpd-oper:fpd/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Fpd_.Nodes, [], name, value)


        class Node(Entity):
            """
            Information about a particular node
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: devices
            
            	FPD information table
            	**type**\:  :py:class:`Devices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.Fpd_.Nodes.Node.Devices>`
            
            

            """

            _prefix = 'upgrade-fpd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Fpd_.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_container_classes = OrderedDict([("devices", ("devices", Fpd_.Nodes.Node.Devices))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_name', YLeaf(YType.str, 'node-name')),
                ])
                self.node_name = None

                self.devices = Fpd_.Nodes.Node.Devices()
                self.devices.parent = self
                self._children_name_map["devices"] = "devices"
                self._children_yang_names.add("devices")
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-upgrade-fpd-oper:fpd/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Fpd_.Nodes.Node, ['node_name'], name, value)


            class Devices(Entity):
                """
                FPD information table
                
                .. attribute:: device
                
                	FPD information for a particular fpd type
                	**type**\: list of  		 :py:class:`Device <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.Fpd_.Nodes.Node.Devices.Device>`
                
                

                """

                _prefix = 'upgrade-fpd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Fpd_.Nodes.Node.Devices, self).__init__()

                    self.yang_name = "devices"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("device", ("device", Fpd_.Nodes.Node.Devices.Device))])
                    self._leafs = OrderedDict()

                    self.device = YList(self)
                    self._segment_path = lambda: "devices"

                def __setattr__(self, name, value):
                    self._perform_setattr(Fpd_.Nodes.Node.Devices, [], name, value)


                class Device(Entity):
                    """
                    FPD information for a particular fpd type
                    
                    .. attribute:: fpd_type
                    
                    	FPD type
                    	**type**\:  :py:class:`Fpd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.Fpd>`
                    
                    .. attribute:: instance
                    
                    	Instance
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: sub_type
                    
                    	FPD sub type
                    	**type**\:  :py:class:`FpdSub <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.FpdSub>`
                    
                    .. attribute:: card_type
                    
                    	Card type containing FPD
                    	**type**\: str
                    
                    .. attribute:: hardware_version
                    
                    	FPD hardware version inX.Y format. X\-Major version, Y\-Minor version
                    	**type**\: str
                    
                    .. attribute:: software_version
                    
                    	FPD software version in X.Y format X\-Major version, Y\-Minor version Note\: 'Unknown' is returned in case the software version of the FPD cannot be determined
                    	**type**\: str
                    
                    .. attribute:: is_upgrade_downgrade
                    
                    	If true, upgrade or downgrade
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'upgrade-fpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Fpd_.Nodes.Node.Devices.Device, self).__init__()

                        self.yang_name = "device"
                        self.yang_parent_name = "devices"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('fpd_type', YLeaf(YType.enumeration, 'fpd-type')),
                            ('instance', YLeaf(YType.int32, 'instance')),
                            ('sub_type', YLeaf(YType.enumeration, 'sub-type')),
                            ('card_type', YLeaf(YType.str, 'card-type')),
                            ('hardware_version', YLeaf(YType.str, 'hardware-version')),
                            ('software_version', YLeaf(YType.str, 'software-version')),
                            ('is_upgrade_downgrade', YLeaf(YType.boolean, 'is-upgrade-downgrade')),
                        ])
                        self.fpd_type = None
                        self.instance = None
                        self.sub_type = None
                        self.card_type = None
                        self.hardware_version = None
                        self.software_version = None
                        self.is_upgrade_downgrade = None
                        self._segment_path = lambda: "device"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Fpd_.Nodes.Node.Devices.Device, ['fpd_type', 'instance', 'sub_type', 'card_type', 'hardware_version', 'software_version', 'is_upgrade_downgrade'], name, value)


    class Packages(Entity):
        """
        FPD packages information
        
        .. attribute:: all_package
        
        	List of packages
        	**type**\: list of  		 :py:class:`AllPackage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.Fpd_.Packages.AllPackage>`
        
        

        """

        _prefix = 'upgrade-fpd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Fpd_.Packages, self).__init__()

            self.yang_name = "packages"
            self.yang_parent_name = "fpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("all-package", ("all_package", Fpd_.Packages.AllPackage))])
            self._leafs = OrderedDict()

            self.all_package = YList(self)
            self._segment_path = lambda: "packages"
            self._absolute_path = lambda: "Cisco-IOS-XR-upgrade-fpd-oper:fpd/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Fpd_.Packages, [], name, value)


        class AllPackage(Entity):
            """
            List of packages
            
            .. attribute:: card_type
            
            	Card type containing FPD
            	**type**\: str
            
            .. attribute:: card_description
            
            	Card description
            	**type**\: str
            
            .. attribute:: fpd_type
            
            	FPD type
            	**type**\:  :py:class:`Fpd1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.Fpd1>`
            
            .. attribute:: fpd_sub_type
            
            	FPD sub type
            	**type**\:  :py:class:`FpdSub1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.FpdSub1>`
            
            .. attribute:: software_version
            
            	FPD software version in X.Y format X\-Major version, Y\-Minor version Note\: 'Unknown' is returned in case the software version of the FPD cannot be determined
            	**type**\: str
            
            .. attribute:: minimum_required_software_version
            
            	Minimum required FPD software version in X.Y format X\-Major version, Y\-Minor version Note\: 'Unknown' is returned in case the software version of the FPD cannot be determined
            	**type**\: str
            
            .. attribute:: minimum_required_hardware_version
            
            	Minimum required FPD hardware version in X.Y format X\-Major version, Y\-Minor version 
            	**type**\: str
            
            

            """

            _prefix = 'upgrade-fpd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Fpd_.Packages.AllPackage, self).__init__()

                self.yang_name = "all-package"
                self.yang_parent_name = "packages"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('card_type', YLeaf(YType.str, 'card-type')),
                    ('card_description', YLeaf(YType.str, 'card-description')),
                    ('fpd_type', YLeaf(YType.enumeration, 'fpd-type')),
                    ('fpd_sub_type', YLeaf(YType.enumeration, 'fpd-sub-type')),
                    ('software_version', YLeaf(YType.str, 'software-version')),
                    ('minimum_required_software_version', YLeaf(YType.str, 'minimum-required-software-version')),
                    ('minimum_required_hardware_version', YLeaf(YType.str, 'minimum-required-hardware-version')),
                ])
                self.card_type = None
                self.card_description = None
                self.fpd_type = None
                self.fpd_sub_type = None
                self.software_version = None
                self.minimum_required_software_version = None
                self.minimum_required_hardware_version = None
                self._segment_path = lambda: "all-package"
                self._absolute_path = lambda: "Cisco-IOS-XR-upgrade-fpd-oper:fpd/packages/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Fpd_.Packages.AllPackage, ['card_type', 'card_description', 'fpd_type', 'fpd_sub_type', 'software_version', 'minimum_required_software_version', 'minimum_required_hardware_version'], name, value)

    def clone_ptr(self):
        self._top_entity = Fpd_()
        return self._top_entity


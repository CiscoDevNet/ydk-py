""" Cisco_IOS_XR_upgrade_fpd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR upgrade\-fpd package operational data.

This module contains definitions
for the following management objects\:
  fpd\: Field programmable device (FPD) operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Fpd(Enum):
    """
    Fpd

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
    Fpd1

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
    FpdSub

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
    FpdSub1

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
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.Fpd_.Nodes>`
    
    .. attribute:: packages
    
    	FPD packages information
    	**type**\:   :py:class:`Packages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.Fpd_.Packages>`
    
    

    """

    _prefix = 'upgrade-fpd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Fpd_, self).__init__()
        self._top_entity = None

        self.yang_name = "fpd"
        self.yang_parent_name = "Cisco-IOS-XR-upgrade-fpd-oper"

        self.nodes = Fpd_.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")

        self.packages = Fpd_.Packages()
        self.packages.parent = self
        self._children_name_map["packages"] = "packages"
        self._children_yang_names.add("packages")


    class Nodes(Entity):
        """
        List of FPD supported nodes
        
        .. attribute:: node
        
        	Information about a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.Fpd_.Nodes.Node>`
        
        

        """

        _prefix = 'upgrade-fpd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Fpd_.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "fpd"

            self.node = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Fpd_.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Fpd_.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Information about a particular node
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: devices
            
            	FPD information table
            	**type**\:   :py:class:`Devices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.Fpd_.Nodes.Node.Devices>`
            
            

            """

            _prefix = 'upgrade-fpd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Fpd_.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.devices = Fpd_.Nodes.Node.Devices()
                self.devices.parent = self
                self._children_name_map["devices"] = "devices"
                self._children_yang_names.add("devices")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Fpd_.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Fpd_.Nodes.Node, self).__setattr__(name, value)


            class Devices(Entity):
                """
                FPD information table
                
                .. attribute:: device
                
                	FPD information for a particular fpd type
                	**type**\: list of    :py:class:`Device <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.Fpd_.Nodes.Node.Devices.Device>`
                
                

                """

                _prefix = 'upgrade-fpd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Fpd_.Nodes.Node.Devices, self).__init__()

                    self.yang_name = "devices"
                    self.yang_parent_name = "node"

                    self.device = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Fpd_.Nodes.Node.Devices, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Fpd_.Nodes.Node.Devices, self).__setattr__(name, value)


                class Device(Entity):
                    """
                    FPD information for a particular fpd type
                    
                    .. attribute:: card_type
                    
                    	Card type containing FPD
                    	**type**\:  str
                    
                    .. attribute:: fpd_type
                    
                    	FPD type
                    	**type**\:   :py:class:`Fpd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.Fpd>`
                    
                    .. attribute:: hardware_version
                    
                    	FPD hardware version inX.Y format. X\-Major version, Y\-Minor version
                    	**type**\:  str
                    
                    .. attribute:: instance
                    
                    	Instance
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: is_upgrade_downgrade
                    
                    	If true, upgrade or downgrade
                    	**type**\:  bool
                    
                    .. attribute:: software_version
                    
                    	FPD software version in X.Y format X\-Major version, Y\-Minor version Note\: 'Unknown' is returned in case the software version of the FPD cannot be determined
                    	**type**\:  str
                    
                    .. attribute:: sub_type
                    
                    	FPD sub type
                    	**type**\:   :py:class:`FpdSub <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.FpdSub>`
                    
                    

                    """

                    _prefix = 'upgrade-fpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Fpd_.Nodes.Node.Devices.Device, self).__init__()

                        self.yang_name = "device"
                        self.yang_parent_name = "devices"

                        self.card_type = YLeaf(YType.str, "card-type")

                        self.fpd_type = YLeaf(YType.enumeration, "fpd-type")

                        self.hardware_version = YLeaf(YType.str, "hardware-version")

                        self.instance = YLeaf(YType.int32, "instance")

                        self.is_upgrade_downgrade = YLeaf(YType.boolean, "is-upgrade-downgrade")

                        self.software_version = YLeaf(YType.str, "software-version")

                        self.sub_type = YLeaf(YType.enumeration, "sub-type")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("card_type",
                                        "fpd_type",
                                        "hardware_version",
                                        "instance",
                                        "is_upgrade_downgrade",
                                        "software_version",
                                        "sub_type") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Fpd_.Nodes.Node.Devices.Device, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Fpd_.Nodes.Node.Devices.Device, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.card_type.is_set or
                            self.fpd_type.is_set or
                            self.hardware_version.is_set or
                            self.instance.is_set or
                            self.is_upgrade_downgrade.is_set or
                            self.software_version.is_set or
                            self.sub_type.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.card_type.yfilter != YFilter.not_set or
                            self.fpd_type.yfilter != YFilter.not_set or
                            self.hardware_version.yfilter != YFilter.not_set or
                            self.instance.yfilter != YFilter.not_set or
                            self.is_upgrade_downgrade.yfilter != YFilter.not_set or
                            self.software_version.yfilter != YFilter.not_set or
                            self.sub_type.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "device" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.card_type.is_set or self.card_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.card_type.get_name_leafdata())
                        if (self.fpd_type.is_set or self.fpd_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.fpd_type.get_name_leafdata())
                        if (self.hardware_version.is_set or self.hardware_version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hardware_version.get_name_leafdata())
                        if (self.instance.is_set or self.instance.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.instance.get_name_leafdata())
                        if (self.is_upgrade_downgrade.is_set or self.is_upgrade_downgrade.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_upgrade_downgrade.get_name_leafdata())
                        if (self.software_version.is_set or self.software_version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.software_version.get_name_leafdata())
                        if (self.sub_type.is_set or self.sub_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sub_type.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "card-type" or name == "fpd-type" or name == "hardware-version" or name == "instance" or name == "is-upgrade-downgrade" or name == "software-version" or name == "sub-type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "card-type"):
                            self.card_type = value
                            self.card_type.value_namespace = name_space
                            self.card_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "fpd-type"):
                            self.fpd_type = value
                            self.fpd_type.value_namespace = name_space
                            self.fpd_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "hardware-version"):
                            self.hardware_version = value
                            self.hardware_version.value_namespace = name_space
                            self.hardware_version.value_namespace_prefix = name_space_prefix
                        if(value_path == "instance"):
                            self.instance = value
                            self.instance.value_namespace = name_space
                            self.instance.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-upgrade-downgrade"):
                            self.is_upgrade_downgrade = value
                            self.is_upgrade_downgrade.value_namespace = name_space
                            self.is_upgrade_downgrade.value_namespace_prefix = name_space_prefix
                        if(value_path == "software-version"):
                            self.software_version = value
                            self.software_version.value_namespace = name_space
                            self.software_version.value_namespace_prefix = name_space_prefix
                        if(value_path == "sub-type"):
                            self.sub_type = value
                            self.sub_type.value_namespace = name_space
                            self.sub_type.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.device:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.device:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "devices" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "device"):
                        for c in self.device:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Fpd_.Nodes.Node.Devices.Device()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.device.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "device"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.devices is not None and self.devices.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.devices is not None and self.devices.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-upgrade-fpd-oper:fpd/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "devices"):
                    if (self.devices is None):
                        self.devices = Fpd_.Nodes.Node.Devices()
                        self.devices.parent = self
                        self._children_name_map["devices"] = "devices"
                    return self.devices

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "devices" or name == "node-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-upgrade-fpd-oper:fpd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "node"):
                for c in self.node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Fpd_.Nodes.Node()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Packages(Entity):
        """
        FPD packages information
        
        .. attribute:: all_package
        
        	List of packages
        	**type**\: list of    :py:class:`AllPackage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.Fpd_.Packages.AllPackage>`
        
        

        """

        _prefix = 'upgrade-fpd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Fpd_.Packages, self).__init__()

            self.yang_name = "packages"
            self.yang_parent_name = "fpd"

            self.all_package = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Fpd_.Packages, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Fpd_.Packages, self).__setattr__(name, value)


        class AllPackage(Entity):
            """
            List of packages
            
            .. attribute:: card_description
            
            	Card description
            	**type**\:  str
            
            .. attribute:: card_type
            
            	Card type containing FPD
            	**type**\:  str
            
            .. attribute:: fpd_sub_type
            
            	FPD sub type
            	**type**\:   :py:class:`FpdSub1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.FpdSub1>`
            
            .. attribute:: fpd_type
            
            	FPD type
            	**type**\:   :py:class:`Fpd1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.Fpd1>`
            
            .. attribute:: minimum_required_hardware_version
            
            	Minimum required FPD hardware version in X.Y format X\-Major version, Y\-Minor version 
            	**type**\:  str
            
            .. attribute:: minimum_required_software_version
            
            	Minimum required FPD software version in X.Y format X\-Major version, Y\-Minor version Note\: 'Unknown' is returned in case the software version of the FPD cannot be determined
            	**type**\:  str
            
            .. attribute:: software_version
            
            	FPD software version in X.Y format X\-Major version, Y\-Minor version Note\: 'Unknown' is returned in case the software version of the FPD cannot be determined
            	**type**\:  str
            
            

            """

            _prefix = 'upgrade-fpd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Fpd_.Packages.AllPackage, self).__init__()

                self.yang_name = "all-package"
                self.yang_parent_name = "packages"

                self.card_description = YLeaf(YType.str, "card-description")

                self.card_type = YLeaf(YType.str, "card-type")

                self.fpd_sub_type = YLeaf(YType.enumeration, "fpd-sub-type")

                self.fpd_type = YLeaf(YType.enumeration, "fpd-type")

                self.minimum_required_hardware_version = YLeaf(YType.str, "minimum-required-hardware-version")

                self.minimum_required_software_version = YLeaf(YType.str, "minimum-required-software-version")

                self.software_version = YLeaf(YType.str, "software-version")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("card_description",
                                "card_type",
                                "fpd_sub_type",
                                "fpd_type",
                                "minimum_required_hardware_version",
                                "minimum_required_software_version",
                                "software_version") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Fpd_.Packages.AllPackage, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Fpd_.Packages.AllPackage, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.card_description.is_set or
                    self.card_type.is_set or
                    self.fpd_sub_type.is_set or
                    self.fpd_type.is_set or
                    self.minimum_required_hardware_version.is_set or
                    self.minimum_required_software_version.is_set or
                    self.software_version.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.card_description.yfilter != YFilter.not_set or
                    self.card_type.yfilter != YFilter.not_set or
                    self.fpd_sub_type.yfilter != YFilter.not_set or
                    self.fpd_type.yfilter != YFilter.not_set or
                    self.minimum_required_hardware_version.yfilter != YFilter.not_set or
                    self.minimum_required_software_version.yfilter != YFilter.not_set or
                    self.software_version.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "all-package" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-upgrade-fpd-oper:fpd/packages/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.card_description.is_set or self.card_description.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.card_description.get_name_leafdata())
                if (self.card_type.is_set or self.card_type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.card_type.get_name_leafdata())
                if (self.fpd_sub_type.is_set or self.fpd_sub_type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.fpd_sub_type.get_name_leafdata())
                if (self.fpd_type.is_set or self.fpd_type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.fpd_type.get_name_leafdata())
                if (self.minimum_required_hardware_version.is_set or self.minimum_required_hardware_version.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.minimum_required_hardware_version.get_name_leafdata())
                if (self.minimum_required_software_version.is_set or self.minimum_required_software_version.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.minimum_required_software_version.get_name_leafdata())
                if (self.software_version.is_set or self.software_version.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.software_version.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "card-description" or name == "card-type" or name == "fpd-sub-type" or name == "fpd-type" or name == "minimum-required-hardware-version" or name == "minimum-required-software-version" or name == "software-version"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "card-description"):
                    self.card_description = value
                    self.card_description.value_namespace = name_space
                    self.card_description.value_namespace_prefix = name_space_prefix
                if(value_path == "card-type"):
                    self.card_type = value
                    self.card_type.value_namespace = name_space
                    self.card_type.value_namespace_prefix = name_space_prefix
                if(value_path == "fpd-sub-type"):
                    self.fpd_sub_type = value
                    self.fpd_sub_type.value_namespace = name_space
                    self.fpd_sub_type.value_namespace_prefix = name_space_prefix
                if(value_path == "fpd-type"):
                    self.fpd_type = value
                    self.fpd_type.value_namespace = name_space
                    self.fpd_type.value_namespace_prefix = name_space_prefix
                if(value_path == "minimum-required-hardware-version"):
                    self.minimum_required_hardware_version = value
                    self.minimum_required_hardware_version.value_namespace = name_space
                    self.minimum_required_hardware_version.value_namespace_prefix = name_space_prefix
                if(value_path == "minimum-required-software-version"):
                    self.minimum_required_software_version = value
                    self.minimum_required_software_version.value_namespace = name_space
                    self.minimum_required_software_version.value_namespace_prefix = name_space_prefix
                if(value_path == "software-version"):
                    self.software_version = value
                    self.software_version.value_namespace = name_space
                    self.software_version.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.all_package:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.all_package:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "packages" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-upgrade-fpd-oper:fpd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "all-package"):
                for c in self.all_package:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Fpd_.Packages.AllPackage()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.all_package.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "all-package"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.nodes is not None and self.nodes.has_data()) or
            (self.packages is not None and self.packages.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nodes is not None and self.nodes.has_operation()) or
            (self.packages is not None and self.packages.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-upgrade-fpd-oper:fpd" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = Fpd_.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        if (child_yang_name == "packages"):
            if (self.packages is None):
                self.packages = Fpd_.Packages()
                self.packages.parent = self
                self._children_name_map["packages"] = "packages"
            return self.packages

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nodes" or name == "packages"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Fpd_()
        return self._top_entity


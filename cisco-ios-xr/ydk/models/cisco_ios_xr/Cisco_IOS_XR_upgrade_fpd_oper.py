""" Cisco_IOS_XR_upgrade_fpd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR upgrade\-fpd package operational data.

This module contains definitions
for the following management objects\:
  fpd\: Field programmable device (FPD) operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class Fpd1Enum(Enum):
    """
    Fpd1Enum

    FPD types

    .. data:: spa = 0

    	Shared port adapter

    .. data:: lc = 1

    	Line card

    .. data:: sam = 2

    	Service acceleration module

    """

    spa = 0

    lc = 1

    sam = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_upgrade_fpd_oper as meta
        return meta._meta_table['Fpd1Enum']


class FpdEnum(Enum):
    """
    FpdEnum

    Fpd

    .. data:: spa = 0

    	SPA class of fpd

    .. data:: lc = 1

    	Linecard class of fpd

    .. data:: sam = 2

    	SAM class of fpd

    """

    spa = 0

    lc = 1

    sam = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_upgrade_fpd_oper as meta
        return meta._meta_table['FpdEnum']


class FpdSub1Enum(Enum):
    """
    FpdSub1Enum

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

    fpga1 = 0

    rommon = 1

    rommona = 2

    fabric_loader = 3

    fpga2 = 4

    fpga3 = 5

    fpga4 = 6

    fpga5 = 7

    fpga6 = 8

    fpga7 = 9

    fpga8 = 10

    fpga9 = 11

    fpga10 = 12

    fpga11 = 13

    fpga12 = 14

    fpga13 = 15

    fpga14 = 16

    cpld1 = 17

    cpld2 = 18

    cpld3 = 19

    cpld4 = 20

    cpld5 = 21

    cpld6 = 22

    cbc = 23

    hsbi = 24

    txpod = 25

    rxpod = 26

    ibmc = 27

    fsbl = 28

    lnx = 29

    fpga15 = 30

    fpga16 = 31

    fc_fsbl = 32

    fc_lnx = 33


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_upgrade_fpd_oper as meta
        return meta._meta_table['FpdSub1Enum']


class FpdSubEnum(Enum):
    """
    FpdSubEnum

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

    fpga1 = 0

    rommon = 1

    rommona = 2

    fabldr = 3

    fpga2 = 4

    fpga3 = 5

    fpga4 = 6

    fpga5 = 7

    fpga6 = 8

    fpga7 = 9

    fpga8 = 10

    fpga9 = 11

    fpga10 = 12

    fpga11 = 13

    fpga12 = 14

    fpga13 = 15

    fpga14 = 16

    cpld1 = 17

    cpld2 = 18

    cpld3 = 19

    cpld4 = 20

    cpld5 = 21

    cpld6 = 22

    cbc = 23

    hsbi = 24

    txpod = 25

    rxpod = 26

    ibmc = 27

    fsbl = 28

    lnx = 29

    fpga15 = 30

    fpga16 = 31

    fc_fsbl = 32

    fc_lnx = 33


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_upgrade_fpd_oper as meta
        return meta._meta_table['FpdSubEnum']



class Fpd(object):
    """
    Field programmable device (FPD) operational data
    
    .. attribute:: nodes
    
    	List of FPD supported nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.Fpd.Nodes>`
    
    .. attribute:: packages
    
    	FPD packages information
    	**type**\:   :py:class:`Packages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.Fpd.Packages>`
    
    

    """

    _prefix = 'upgrade-fpd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = Fpd.Nodes()
        self.nodes.parent = self
        self.packages = Fpd.Packages()
        self.packages.parent = self


    class Nodes(object):
        """
        List of FPD supported nodes
        
        .. attribute:: node
        
        	Information about a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.Fpd.Nodes.Node>`
        
        

        """

        _prefix = 'upgrade-fpd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Information about a particular node
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: devices
            
            	FPD information table
            	**type**\:   :py:class:`Devices <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.Fpd.Nodes.Node.Devices>`
            
            

            """

            _prefix = 'upgrade-fpd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.devices = Fpd.Nodes.Node.Devices()
                self.devices.parent = self


            class Devices(object):
                """
                FPD information table
                
                .. attribute:: device
                
                	FPD information for a particular fpd type
                	**type**\: list of    :py:class:`Device <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.Fpd.Nodes.Node.Devices.Device>`
                
                

                """

                _prefix = 'upgrade-fpd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.device = YList()
                    self.device.parent = self
                    self.device.name = 'device'


                class Device(object):
                    """
                    FPD information for a particular fpd type
                    
                    .. attribute:: card_type
                    
                    	Card type containing FPD
                    	**type**\:  str
                    
                    .. attribute:: fpd_type
                    
                    	FPD type
                    	**type**\:   :py:class:`FpdEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.FpdEnum>`
                    
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
                    	**type**\:   :py:class:`FpdSubEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.FpdSubEnum>`
                    
                    

                    """

                    _prefix = 'upgrade-fpd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.card_type = None
                        self.fpd_type = None
                        self.hardware_version = None
                        self.instance = None
                        self.is_upgrade_downgrade = None
                        self.software_version = None
                        self.sub_type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-upgrade-fpd-oper:device'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.card_type is not None:
                            return True

                        if self.fpd_type is not None:
                            return True

                        if self.hardware_version is not None:
                            return True

                        if self.instance is not None:
                            return True

                        if self.is_upgrade_downgrade is not None:
                            return True

                        if self.software_version is not None:
                            return True

                        if self.sub_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_upgrade_fpd_oper as meta
                        return meta._meta_table['Fpd.Nodes.Node.Devices.Device']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-upgrade-fpd-oper:devices'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.device is not None:
                        for child_ref in self.device:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_upgrade_fpd_oper as meta
                    return meta._meta_table['Fpd.Nodes.Node.Devices']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-upgrade-fpd-oper:fpd/Cisco-IOS-XR-upgrade-fpd-oper:nodes/Cisco-IOS-XR-upgrade-fpd-oper:node[Cisco-IOS-XR-upgrade-fpd-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.devices is not None and self.devices._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_upgrade_fpd_oper as meta
                return meta._meta_table['Fpd.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-upgrade-fpd-oper:fpd/Cisco-IOS-XR-upgrade-fpd-oper:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_upgrade_fpd_oper as meta
            return meta._meta_table['Fpd.Nodes']['meta_info']


    class Packages(object):
        """
        FPD packages information
        
        .. attribute:: all_package
        
        	List of packages
        	**type**\: list of    :py:class:`AllPackage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.Fpd.Packages.AllPackage>`
        
        

        """

        _prefix = 'upgrade-fpd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.all_package = YList()
            self.all_package.parent = self
            self.all_package.name = 'all_package'


        class AllPackage(object):
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
            	**type**\:   :py:class:`FpdSub1Enum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.FpdSub1Enum>`
            
            .. attribute:: fpd_type
            
            	FPD type
            	**type**\:   :py:class:`Fpd1Enum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_upgrade_fpd_oper.Fpd1Enum>`
            
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
                self.parent = None
                self.card_description = None
                self.card_type = None
                self.fpd_sub_type = None
                self.fpd_type = None
                self.minimum_required_hardware_version = None
                self.minimum_required_software_version = None
                self.software_version = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-upgrade-fpd-oper:fpd/Cisco-IOS-XR-upgrade-fpd-oper:packages/Cisco-IOS-XR-upgrade-fpd-oper:all-package'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.card_description is not None:
                    return True

                if self.card_type is not None:
                    return True

                if self.fpd_sub_type is not None:
                    return True

                if self.fpd_type is not None:
                    return True

                if self.minimum_required_hardware_version is not None:
                    return True

                if self.minimum_required_software_version is not None:
                    return True

                if self.software_version is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_upgrade_fpd_oper as meta
                return meta._meta_table['Fpd.Packages.AllPackage']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-upgrade-fpd-oper:fpd/Cisco-IOS-XR-upgrade-fpd-oper:packages'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.all_package is not None:
                for child_ref in self.all_package:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_upgrade_fpd_oper as meta
            return meta._meta_table['Fpd.Packages']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-upgrade-fpd-oper:fpd'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        if self.packages is not None and self.packages._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_upgrade_fpd_oper as meta
        return meta._meta_table['Fpd']['meta_info']



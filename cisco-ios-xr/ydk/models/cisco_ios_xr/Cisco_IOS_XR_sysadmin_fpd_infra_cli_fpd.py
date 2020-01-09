""" Cisco_IOS_XR_sysadmin_fpd_infra_cli_fpd 

This module contains definitions
for the Calvados model objects.

FPD CLI support for both oper and config

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
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




class Fpd(_Entity_):
    """
    
    
    .. attribute:: config
    
    	fpd config mode
    	**type**\:  :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fpd_infra_cli_fpd.Fpd.Config>`
    
    

    """

    _prefix = 'fpd'
    _revision = '2017-05-01'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Fpd, self).__init__()
        self._top_entity = None

        self.yang_name = "fpd"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-fpd-infra-cli-fpd"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("config", ("config", Fpd.Config))])
        self._leafs = OrderedDict()

        self.config = Fpd.Config()
        self.config.parent = self
        self._children_name_map["config"] = "config"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-fpd-infra-cli-fpd:fpd"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Fpd, [], name, value)


    class Config(_Entity_):
        """
        fpd config mode
        
        .. attribute:: auto_upgrade
        
        	
        	**type**\:  :py:class:`AutoUpgrade <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fpd_infra_cli_fpd.Fpd.Config.AutoUpgrade>`
        
        	**default value**\: disable
        
        

        """

        _prefix = 'fpd'
        _revision = '2017-05-01'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Fpd.Config, self).__init__()

            self.yang_name = "config"
            self.yang_parent_name = "fpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('auto_upgrade', (YLeaf(YType.enumeration, 'auto-upgrade'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_fpd_infra_cli_fpd', 'Fpd', 'Config.AutoUpgrade')])),
            ])
            self.auto_upgrade = None
            self._segment_path = lambda: "config"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-fpd-infra-cli-fpd:fpd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Fpd.Config, ['auto_upgrade'], name, value)

        class AutoUpgrade(Enum):
            """
            AutoUpgrade (Enum Class)

            .. data:: enable = 0

            .. data:: disable = 1

            """

            enable = Enum.YLeaf(0, "enable")

            disable = Enum.YLeaf(1, "disable")


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fpd_infra_cli_fpd as meta
                return meta._meta_table['Fpd.Config.AutoUpgrade']


        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fpd_infra_cli_fpd as meta
            return meta._meta_table['Fpd.Config']['meta_info']

    def clone_ptr(self):
        self._top_entity = Fpd()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_fpd_infra_cli_fpd as meta
        return meta._meta_table['Fpd']['meta_info']



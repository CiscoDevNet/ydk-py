""" Cisco_IOS_XR_sysadmin_vm 

This module contains definitions
for the Calvados model objects.

This module contains the YANG definitions
for the Cisco IOS\-XR SysAdmin
'vm profile\|cpu\|memory' commands.

Copyright(c) 2018 by Cisco Systems, Inc.
All rights reserved.

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




class Vm(_Entity_):
    """
    
    
    .. attribute:: config
    
    	
    	**type**\:  :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm.Vm.Config>`
    
    

    """

    _prefix = 'vm'
    _revision = '2018-11-20'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Vm, self).__init__()
        self._top_entity = None

        self.yang_name = "vm"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-vm"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("config", ("config", Vm.Config))])
        self._leafs = OrderedDict()

        self.config = Vm.Config()
        self.config.parent = self
        self._children_name_map["config"] = "config"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-vm:vm"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Vm, [], name, value)


    class Config(_Entity_):
        """
        
        
        .. attribute:: hw_profile
        
        	
        	**type**\:  :py:class:`HwProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm.Vm.Config.HwProfile>`
        
        .. attribute:: memory
        
        	
        	**type**\:  :py:class:`Memory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm.Vm.Config.Memory>`
        
        .. attribute:: cpu
        
        	
        	**type**\:  :py:class:`Cpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm.Vm.Config.Cpu>`
        
        

        """

        _prefix = 'vm'
        _revision = '2018-11-20'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Vm.Config, self).__init__()

            self.yang_name = "config"
            self.yang_parent_name = "vm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("hw-profile", ("hw_profile", Vm.Config.HwProfile)), ("memory", ("memory", Vm.Config.Memory)), ("cpu", ("cpu", Vm.Config.Cpu))])
            self._leafs = OrderedDict()

            self.hw_profile = Vm.Config.HwProfile()
            self.hw_profile.parent = self
            self._children_name_map["hw_profile"] = "hw-profile"

            self.memory = Vm.Config.Memory()
            self.memory.parent = self
            self._children_name_map["memory"] = "memory"

            self.cpu = Vm.Config.Cpu()
            self.cpu.parent = self
            self._children_name_map["cpu"] = "cpu"
            self._segment_path = lambda: "config"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-vm:vm/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vm.Config, [], name, value)


        class HwProfile(_Entity_):
            """
            
            
            .. attribute:: profile
            
            	xrv9k profile vpe\|vrr
            	**type**\:  :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm.Vm.Config.HwProfile.Profile>`
            
            

            """

            _prefix = 'vm'
            _revision = '2018-11-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Vm.Config.HwProfile, self).__init__()

                self.yang_name = "hw-profile"
                self.yang_parent_name = "config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('profile', (YLeaf(YType.enumeration, 'profile'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_vm', 'Vm', 'Config.HwProfile.Profile')])),
                ])
                self.profile = None
                self._segment_path = lambda: "hw-profile"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-vm:vm/config/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vm.Config.HwProfile, ['profile'], name, value)

            class Profile(Enum):
                """
                Profile (Enum Class)

                xrv9k profile vpe\|vrr

                .. data:: vrr = 0

                """

                vrr = Enum.YLeaf(0, "vrr")


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_vm as meta
                    return meta._meta_table['Vm.Config.HwProfile.Profile']


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_vm as meta
                return meta._meta_table['Vm.Config.HwProfile']['meta_info']


        class Memory(_Entity_):
            """
            
            
            .. attribute:: admin
            
            	admin container memory in GB
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rp
            
            	rp container memory in GB
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: lc
            
            	lc container memory in GB
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'vm'
            _revision = '2018-11-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Vm.Config.Memory, self).__init__()

                self.yang_name = "memory"
                self.yang_parent_name = "config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('admin', (YLeaf(YType.uint32, 'admin'), ['int'])),
                    ('rp', (YLeaf(YType.uint32, 'rp'), ['int'])),
                    ('lc', (YLeaf(YType.uint32, 'lc'), ['int'])),
                ])
                self.admin = None
                self.rp = None
                self.lc = None
                self._segment_path = lambda: "memory"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-vm:vm/config/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vm.Config.Memory, ['admin', 'rp', 'lc'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_vm as meta
                return meta._meta_table['Vm.Config.Memory']['meta_info']


        class Cpu(_Entity_):
            """
            
            
            .. attribute:: assign
            
            	assign cpu cores to control/data plane
            	**type**\: str
            
            	**pattern:** 0(\-[0\-9]+)?/[0\-9]+(\-[0\-9]+)?
            
            

            """

            _prefix = 'vm'
            _revision = '2018-11-20'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Vm.Config.Cpu, self).__init__()

                self.yang_name = "cpu"
                self.yang_parent_name = "config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('assign', (YLeaf(YType.str, 'assign'), ['str'])),
                ])
                self.assign = None
                self._segment_path = lambda: "cpu"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-vm:vm/config/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vm.Config.Cpu, ['assign'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_vm as meta
                return meta._meta_table['Vm.Config.Cpu']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_vm as meta
            return meta._meta_table['Vm.Config']['meta_info']

    def clone_ptr(self):
        self._top_entity = Vm()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_vm as meta
        return meta._meta_table['Vm']['meta_info']



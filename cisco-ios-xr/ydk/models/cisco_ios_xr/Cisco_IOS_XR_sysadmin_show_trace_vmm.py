""" Cisco_IOS_XR_sysadmin_show_trace_vmm 

This module contains definitions
for the Calvados model objects.

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

Copyright(c) 2012\-2017 by Cisco Systems, Inc.
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




class Vmm(_Entity_):
    """
    
    
    .. attribute:: vm_manager
    
    	
    	**type**\:  :py:class:`VmManager <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_vmm.Vmm.VmManager>`
    
    	**config**\: False
    
    

    """

    _prefix = 'vm_managerh'
    _revision = '2017-04-12'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Vmm, self).__init__()
        self._top_entity = None

        self.yang_name = "vmm"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-show-trace-vmm"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vm_manager", ("vm_manager", Vmm.VmManager))])
        self._leafs = OrderedDict()

        self.vm_manager = Vmm.VmManager()
        self.vm_manager.parent = self
        self._children_name_map["vm_manager"] = "vm_manager"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-show-trace-vmm:vmm"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Vmm, [], name, value)


    class VmManager(_Entity_):
        """
        
        
        .. attribute:: trace
        
        	show traceable processes
        	**type**\: list of  		 :py:class:`Trace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_vmm.Vmm.VmManager.Trace>`
        
        	**config**\: False
        
        

        """

        _prefix = 'vm_managerh'
        _revision = '2017-04-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Vmm.VmManager, self).__init__()

            self.yang_name = "vm_manager"
            self.yang_parent_name = "vmm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("trace", ("trace", Vmm.VmManager.Trace))])
            self._leafs = OrderedDict()

            self.trace = YList(self)
            self._segment_path = lambda: "vm_manager"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-trace-vmm:vmm/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vmm.VmManager, [], name, value)


        class Trace(_Entity_):
            """
            show traceable processes
            
            .. attribute:: buffer  (key)
            
            	
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: location
            
            	
            	**type**\: list of  		 :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_vmm.Vmm.VmManager.Trace.Location>`
            
            	**config**\: False
            
            

            """

            _prefix = 'vm_managerh'
            _revision = '2017-04-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Vmm.VmManager.Trace, self).__init__()

                self.yang_name = "trace"
                self.yang_parent_name = "vm_manager"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['buffer']
                self._child_classes = OrderedDict([("location", ("location", Vmm.VmManager.Trace.Location))])
                self._leafs = OrderedDict([
                    ('buffer', (YLeaf(YType.str, 'buffer'), ['str'])),
                ])
                self.buffer = None

                self.location = YList(self)
                self._segment_path = lambda: "trace" + "[buffer='" + str(self.buffer) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-show-trace-vmm:vmm/vm_manager/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vmm.VmManager.Trace, ['buffer'], name, value)


            class Location(_Entity_):
                """
                
                
                .. attribute:: location_name  (key)
                
                	
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: all_options
                
                	
                	**type**\: list of  		 :py:class:`AllOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_vmm.Vmm.VmManager.Trace.Location.AllOptions>`
                
                	**config**\: False
                
                

                """

                _prefix = 'vm_managerh'
                _revision = '2017-04-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Vmm.VmManager.Trace.Location, self).__init__()

                    self.yang_name = "location"
                    self.yang_parent_name = "trace"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['location_name']
                    self._child_classes = OrderedDict([("all-options", ("all_options", Vmm.VmManager.Trace.Location.AllOptions))])
                    self._leafs = OrderedDict([
                        ('location_name', (YLeaf(YType.str, 'location_name'), ['str'])),
                    ])
                    self.location_name = None

                    self.all_options = YList(self)
                    self._segment_path = lambda: "location" + "[location_name='" + str(self.location_name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vmm.VmManager.Trace.Location, ['location_name'], name, value)


                class AllOptions(_Entity_):
                    """
                    
                    
                    .. attribute:: option  (key)
                    
                    	
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: trace_blocks
                    
                    	
                    	**type**\: list of  		 :py:class:`TraceBlocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_show_trace_vmm.Vmm.VmManager.Trace.Location.AllOptions.TraceBlocks>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'vm_managerh'
                    _revision = '2017-04-12'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Vmm.VmManager.Trace.Location.AllOptions, self).__init__()

                        self.yang_name = "all-options"
                        self.yang_parent_name = "location"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['option']
                        self._child_classes = OrderedDict([("trace-blocks", ("trace_blocks", Vmm.VmManager.Trace.Location.AllOptions.TraceBlocks))])
                        self._leafs = OrderedDict([
                            ('option', (YLeaf(YType.str, 'option'), ['str'])),
                        ])
                        self.option = None

                        self.trace_blocks = YList(self)
                        self._segment_path = lambda: "all-options" + "[option='" + str(self.option) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vmm.VmManager.Trace.Location.AllOptions, ['option'], name, value)


                    class TraceBlocks(_Entity_):
                        """
                        
                        
                        .. attribute:: data
                        
                        	Trace output block
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'vm_managerh'
                        _revision = '2017-04-12'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Vmm.VmManager.Trace.Location.AllOptions.TraceBlocks, self).__init__()

                            self.yang_name = "trace-blocks"
                            self.yang_parent_name = "all-options"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('data', (YLeaf(YType.str, 'data'), ['str'])),
                            ])
                            self.data = None
                            self._segment_path = lambda: "trace-blocks"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vmm.VmManager.Trace.Location.AllOptions.TraceBlocks, ['data'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_trace_vmm as meta
                            return meta._meta_table['Vmm.VmManager.Trace.Location.AllOptions.TraceBlocks']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_trace_vmm as meta
                        return meta._meta_table['Vmm.VmManager.Trace.Location.AllOptions']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_trace_vmm as meta
                    return meta._meta_table['Vmm.VmManager.Trace.Location']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_trace_vmm as meta
                return meta._meta_table['Vmm.VmManager.Trace']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_trace_vmm as meta
            return meta._meta_table['Vmm.VmManager']['meta_info']

    def clone_ptr(self):
        self._top_entity = Vmm()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_show_trace_vmm as meta
        return meta._meta_table['Vmm']['meta_info']



""" Cisco_IOS_XR_spirit_install_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR action package configuration.

Copyright (c) 2016\-2019 by Cisco Systems, Inc.
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




class InstallAdd(_Entity_):
    """
    Cli\-command install add source
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallAdd.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallAdd.Output>`
    
    

    """

    _prefix = 'install-act'
    _revision = '2018-09-10'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(InstallAdd, self).__init__()
        self._top_entity = None

        self.yang_name = "install-add"
        self.yang_parent_name = "Cisco-IOS-XR-spirit-install-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = InstallAdd.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"

        self.output = InstallAdd.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._segment_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-add"
        self._is_frozen = True


    class Input(_Entity_):
        """
        
        
        .. attribute:: packagepath
        
        	
        	**type**\: str
        
        .. attribute:: packagename
        
        	
        	**type**\: list of str
        
        

        """

        _prefix = 'install-act'
        _revision = '2018-09-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(InstallAdd.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "install-add"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('packagepath', (YLeaf(YType.str, 'packagepath'), ['str'])),
                ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
            ])
            self.packagepath = None
            self.packagename = []
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-add/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InstallAdd.Input, ['packagepath', 'packagename'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
            return meta._meta_table['InstallAdd.Input']['meta_info']


    class Output(_Entity_):
        """
        
        
        .. attribute:: op_id
        
        	operation id of the triggered action
        	**type**\: str
        
        .. attribute:: error
        
        	case when op\-id is not triggered
        	**type**\: str
        
        

        """

        _prefix = 'install-act'
        _revision = '2018-09-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(InstallAdd.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "install-add"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('op_id', (YLeaf(YType.str, 'op-id'), ['str'])),
                ('error', (YLeaf(YType.str, 'Error'), ['str'])),
            ])
            self.op_id = None
            self.error = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-add/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InstallAdd.Output, ['op_id', 'error'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
            return meta._meta_table['InstallAdd.Output']['meta_info']

    def clone_ptr(self):
        self._top_entity = InstallAdd()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
        return meta._meta_table['InstallAdd']['meta_info']


class InstallCommit(_Entity_):
    """
    Cli\-command install commit
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallCommit.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallCommit.Output>`
    
    

    """

    _prefix = 'install-act'
    _revision = '2018-09-10'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(InstallCommit, self).__init__()
        self._top_entity = None

        self.yang_name = "install-commit"
        self.yang_parent_name = "Cisco-IOS-XR-spirit-install-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = InstallCommit.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"

        self.output = InstallCommit.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._segment_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-commit"
        self._is_frozen = True


    class Input(_Entity_):
        """
        
        
        .. attribute:: sdr
        
        	commit packages in the system
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'install-act'
        _revision = '2018-09-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(InstallCommit.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "install-commit"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('sdr', (YLeaf(YType.empty, 'sdr'), ['Empty'])),
            ])
            self.sdr = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-commit/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InstallCommit.Input, ['sdr'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
            return meta._meta_table['InstallCommit.Input']['meta_info']


    class Output(_Entity_):
        """
        
        
        .. attribute:: op_id
        
        	operation id of the triggered action
        	**type**\: str
        
        .. attribute:: error
        
        	case when op\-id is not triggered
        	**type**\: str
        
        

        """

        _prefix = 'install-act'
        _revision = '2018-09-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(InstallCommit.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "install-commit"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('op_id', (YLeaf(YType.str, 'op-id'), ['str'])),
                ('error', (YLeaf(YType.str, 'Error'), ['str'])),
            ])
            self.op_id = None
            self.error = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-commit/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InstallCommit.Output, ['op_id', 'error'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
            return meta._meta_table['InstallCommit.Output']['meta_info']

    def clone_ptr(self):
        self._top_entity = InstallCommit()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
        return meta._meta_table['InstallCommit']['meta_info']


class InstallRemove(_Entity_):
    """
    Cli\-command remove
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallRemove.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallRemove.Output>`
    
    

    """

    _prefix = 'install-act'
    _revision = '2018-09-10'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(InstallRemove, self).__init__()
        self._top_entity = None

        self.yang_name = "install-remove"
        self.yang_parent_name = "Cisco-IOS-XR-spirit-install-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = InstallRemove.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"

        self.output = InstallRemove.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._segment_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-remove"
        self._is_frozen = True


    class Input(_Entity_):
        """
        
        
        .. attribute:: packages
        
        	
        	**type**\:  :py:class:`Packages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallRemove.Input.Packages>`
        
        .. attribute:: ids
        
        	
        	**type**\:  :py:class:`Ids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallRemove.Input.Ids>`
        
        .. attribute:: inactive
        
        	Remove inactive packages from XR repo
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: inactiveall
        
        	Remove inactive packages from Host,Sysadmin and XR repo
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'install-act'
        _revision = '2018-09-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(InstallRemove.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "install-remove"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("packages", ("packages", InstallRemove.Input.Packages)), ("ids", ("ids", InstallRemove.Input.Ids))])
            self._leafs = OrderedDict([
                ('inactive', (YLeaf(YType.empty, 'inactive'), ['Empty'])),
                ('inactiveall', (YLeaf(YType.empty, 'inactiveall'), ['Empty'])),
            ])
            self.inactive = None
            self.inactiveall = None

            self.packages = InstallRemove.Input.Packages()
            self.packages.parent = self
            self._children_name_map["packages"] = "packages"

            self.ids = InstallRemove.Input.Ids()
            self.ids.parent = self
            self._children_name_map["ids"] = "ids"
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-remove/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InstallRemove.Input, ['inactive', 'inactiveall'], name, value)


        class Packages(_Entity_):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallRemove.Input.Packages, self).__init__()

                self.yang_name = "packages"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                ])
                self.packagename = []
                self._segment_path = lambda: "packages"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-remove/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallRemove.Input.Packages, ['packagename'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallRemove.Input.Packages']['meta_info']


        class Ids(_Entity_):
            """
            
            
            .. attribute:: id_no
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallRemove.Input.Ids, self).__init__()

                self.yang_name = "ids"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('id_no', (YLeafList(YType.str, 'id-no'), ['str'])),
                ])
                self.id_no = []
                self._segment_path = lambda: "ids"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-remove/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallRemove.Input.Ids, ['id_no'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallRemove.Input.Ids']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
            return meta._meta_table['InstallRemove.Input']['meta_info']


    class Output(_Entity_):
        """
        
        
        .. attribute:: op_id
        
        	operation id of the triggered action
        	**type**\: str
        
        .. attribute:: error
        
        	case when op\-id is not triggered
        	**type**\: str
        
        

        """

        _prefix = 'install-act'
        _revision = '2018-09-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(InstallRemove.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "install-remove"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('op_id', (YLeaf(YType.str, 'op-id'), ['str'])),
                ('error', (YLeaf(YType.str, 'Error'), ['str'])),
            ])
            self.op_id = None
            self.error = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-remove/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InstallRemove.Output, ['op_id', 'error'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
            return meta._meta_table['InstallRemove.Output']['meta_info']

    def clone_ptr(self):
        self._top_entity = InstallRemove()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
        return meta._meta_table['InstallRemove']['meta_info']


class InstallPrepare(_Entity_):
    """
    Cli\-command prepare
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallPrepare.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallPrepare.Output>`
    
    

    """

    _prefix = 'install-act'
    _revision = '2018-09-10'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(InstallPrepare, self).__init__()
        self._top_entity = None

        self.yang_name = "install-prepare"
        self.yang_parent_name = "Cisco-IOS-XR-spirit-install-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = InstallPrepare.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"

        self.output = InstallPrepare.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._segment_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-prepare"
        self._is_frozen = True


    class Input(_Entity_):
        """
        
        
        .. attribute:: packages
        
        	
        	**type**\:  :py:class:`Packages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallPrepare.Input.Packages>`
        
        .. attribute:: ids
        
        	
        	**type**\:  :py:class:`Ids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallPrepare.Input.Ids>`
        
        .. attribute:: clean
        
        	Clean the prepared packages
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: prepare_force
        
        	
        	**type**\:  :py:class:`PrepareForce <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallPrepare.Input.PrepareForce>`
        
        

        """

        _prefix = 'install-act'
        _revision = '2018-09-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(InstallPrepare.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "install-prepare"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("packages", ("packages", InstallPrepare.Input.Packages)), ("ids", ("ids", InstallPrepare.Input.Ids)), ("prepare-force", ("prepare_force", InstallPrepare.Input.PrepareForce))])
            self._leafs = OrderedDict([
                ('clean', (YLeaf(YType.empty, 'clean'), ['Empty'])),
            ])
            self.clean = None

            self.packages = InstallPrepare.Input.Packages()
            self.packages.parent = self
            self._children_name_map["packages"] = "packages"

            self.ids = InstallPrepare.Input.Ids()
            self.ids.parent = self
            self._children_name_map["ids"] = "ids"

            self.prepare_force = InstallPrepare.Input.PrepareForce()
            self.prepare_force.parent = self
            self._children_name_map["prepare_force"] = "prepare-force"
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-prepare/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InstallPrepare.Input, ['clean'], name, value)


        class Packages(_Entity_):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallPrepare.Input.Packages, self).__init__()

                self.yang_name = "packages"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                ])
                self.packagename = []
                self._segment_path = lambda: "packages"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-prepare/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallPrepare.Input.Packages, ['packagename'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallPrepare.Input.Packages']['meta_info']


        class Ids(_Entity_):
            """
            
            
            .. attribute:: id_no
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallPrepare.Input.Ids, self).__init__()

                self.yang_name = "ids"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('id_no', (YLeafList(YType.str, 'id-no'), ['str'])),
                ])
                self.id_no = []
                self._segment_path = lambda: "ids"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-prepare/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallPrepare.Input.Ids, ['id_no'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallPrepare.Input.Ids']['meta_info']


        class PrepareForce(_Entity_):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            .. attribute:: ids
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallPrepare.Input.PrepareForce, self).__init__()

                self.yang_name = "prepare-force"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                    ('ids', (YLeafList(YType.str, 'ids'), ['str'])),
                ])
                self.packagename = []
                self.ids = []
                self._segment_path = lambda: "prepare-force"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-prepare/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallPrepare.Input.PrepareForce, ['packagename', 'ids'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallPrepare.Input.PrepareForce']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
            return meta._meta_table['InstallPrepare.Input']['meta_info']


    class Output(_Entity_):
        """
        
        
        .. attribute:: op_id
        
        	operation id of the triggered action
        	**type**\: str
        
        .. attribute:: error
        
        	case when op\-id is not triggered
        	**type**\: str
        
        

        """

        _prefix = 'install-act'
        _revision = '2018-09-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(InstallPrepare.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "install-prepare"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('op_id', (YLeaf(YType.str, 'op-id'), ['str'])),
                ('error', (YLeaf(YType.str, 'Error'), ['str'])),
            ])
            self.op_id = None
            self.error = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-prepare/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InstallPrepare.Output, ['op_id', 'error'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
            return meta._meta_table['InstallPrepare.Output']['meta_info']

    def clone_ptr(self):
        self._top_entity = InstallPrepare()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
        return meta._meta_table['InstallPrepare']['meta_info']


class InstallActivate(_Entity_):
    """
    Cli\-command activate
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallActivate.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallActivate.Output>`
    
    

    """

    _prefix = 'install-act'
    _revision = '2018-09-10'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(InstallActivate, self).__init__()
        self._top_entity = None

        self.yang_name = "install-activate"
        self.yang_parent_name = "Cisco-IOS-XR-spirit-install-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = InstallActivate.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"

        self.output = InstallActivate.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._segment_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-activate"
        self._is_frozen = True


    class Input(_Entity_):
        """
        
        
        .. attribute:: warm
        
        	
        	**type**\:  :py:class:`Warm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallActivate.Input.Warm>`
        
        .. attribute:: warm_force
        
        	
        	**type**\:  :py:class:`WarmForce <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallActivate.Input.WarmForce>`
        
        .. attribute:: warm_replace
        
        	
        	**type**\:  :py:class:`WarmReplace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallActivate.Input.WarmReplace>`
        
        .. attribute:: warm_replace_force
        
        	
        	**type**\:  :py:class:`WarmReplaceForce <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallActivate.Input.WarmReplaceForce>`
        
        .. attribute:: reload
        
        	
        	**type**\:  :py:class:`Reload <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallActivate.Input.Reload>`
        
        .. attribute:: reload_force
        
        	
        	**type**\:  :py:class:`ReloadForce <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallActivate.Input.ReloadForce>`
        
        .. attribute:: replace
        
        	
        	**type**\:  :py:class:`Replace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallActivate.Input.Replace>`
        
        .. attribute:: replace_force
        
        	
        	**type**\:  :py:class:`ReplaceForce <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallActivate.Input.ReplaceForce>`
        
        .. attribute:: activate_force
        
        	
        	**type**\:  :py:class:`ActivateForce <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallActivate.Input.ActivateForce>`
        
        .. attribute:: packages
        
        	
        	**type**\:  :py:class:`Packages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallActivate.Input.Packages>`
        
        .. attribute:: ids
        
        	
        	**type**\:  :py:class:`Ids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallActivate.Input.Ids>`
        
        .. attribute:: activate_prepared_pkg
        
        	Activate the prepared package
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: force
        
        	Activate the prepared package with force option
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: activate_reload
        
        	Activate the prepared package with reload option
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: activate_reload_force
        
        	Activate the prepared package with reload force option
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: activate_warm_prepared_pkg
        
        	Activate the prepared package with warm option
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: activate_warm_force_prepared_pkg
        
        	Activate the prepared package with warm force option
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: activate_warm_replace_prepared_pkg
        
        	Activate the prepared package with warm replace option
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: activate_warm_force_replace_prepared_pkg
        
        	Activate the prepared package with warm force replace option
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'install-act'
        _revision = '2018-09-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(InstallActivate.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "install-activate"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("warm", ("warm", InstallActivate.Input.Warm)), ("warm-force", ("warm_force", InstallActivate.Input.WarmForce)), ("warm-replace", ("warm_replace", InstallActivate.Input.WarmReplace)), ("warm-replace-force", ("warm_replace_force", InstallActivate.Input.WarmReplaceForce)), ("reload", ("reload", InstallActivate.Input.Reload)), ("reload-force", ("reload_force", InstallActivate.Input.ReloadForce)), ("replace", ("replace", InstallActivate.Input.Replace)), ("replace-force", ("replace_force", InstallActivate.Input.ReplaceForce)), ("activate-force", ("activate_force", InstallActivate.Input.ActivateForce)), ("packages", ("packages", InstallActivate.Input.Packages)), ("ids", ("ids", InstallActivate.Input.Ids))])
            self._leafs = OrderedDict([
                ('activate_prepared_pkg', (YLeaf(YType.empty, 'activate_prepared_pkg'), ['Empty'])),
                ('force', (YLeaf(YType.empty, 'force'), ['Empty'])),
                ('activate_reload', (YLeaf(YType.empty, 'activate-reload'), ['Empty'])),
                ('activate_reload_force', (YLeaf(YType.empty, 'activate-reload-force'), ['Empty'])),
                ('activate_warm_prepared_pkg', (YLeaf(YType.empty, 'activate_warm_prepared_pkg'), ['Empty'])),
                ('activate_warm_force_prepared_pkg', (YLeaf(YType.empty, 'activate_warm_force_prepared_pkg'), ['Empty'])),
                ('activate_warm_replace_prepared_pkg', (YLeaf(YType.empty, 'activate_warm_replace_prepared_pkg'), ['Empty'])),
                ('activate_warm_force_replace_prepared_pkg', (YLeaf(YType.empty, 'activate_warm_force_replace_prepared_pkg'), ['Empty'])),
            ])
            self.activate_prepared_pkg = None
            self.force = None
            self.activate_reload = None
            self.activate_reload_force = None
            self.activate_warm_prepared_pkg = None
            self.activate_warm_force_prepared_pkg = None
            self.activate_warm_replace_prepared_pkg = None
            self.activate_warm_force_replace_prepared_pkg = None

            self.warm = InstallActivate.Input.Warm()
            self.warm.parent = self
            self._children_name_map["warm"] = "warm"

            self.warm_force = InstallActivate.Input.WarmForce()
            self.warm_force.parent = self
            self._children_name_map["warm_force"] = "warm-force"

            self.warm_replace = InstallActivate.Input.WarmReplace()
            self.warm_replace.parent = self
            self._children_name_map["warm_replace"] = "warm-replace"

            self.warm_replace_force = InstallActivate.Input.WarmReplaceForce()
            self.warm_replace_force.parent = self
            self._children_name_map["warm_replace_force"] = "warm-replace-force"

            self.reload = InstallActivate.Input.Reload()
            self.reload.parent = self
            self._children_name_map["reload"] = "reload"

            self.reload_force = InstallActivate.Input.ReloadForce()
            self.reload_force.parent = self
            self._children_name_map["reload_force"] = "reload-force"

            self.replace = InstallActivate.Input.Replace()
            self.replace.parent = self
            self._children_name_map["replace"] = "replace"

            self.replace_force = InstallActivate.Input.ReplaceForce()
            self.replace_force.parent = self
            self._children_name_map["replace_force"] = "replace-force"

            self.activate_force = InstallActivate.Input.ActivateForce()
            self.activate_force.parent = self
            self._children_name_map["activate_force"] = "activate-force"

            self.packages = InstallActivate.Input.Packages()
            self.packages.parent = self
            self._children_name_map["packages"] = "packages"

            self.ids = InstallActivate.Input.Ids()
            self.ids.parent = self
            self._children_name_map["ids"] = "ids"
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-activate/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InstallActivate.Input, ['activate_prepared_pkg', 'force', 'activate_reload', 'activate_reload_force', 'activate_warm_prepared_pkg', 'activate_warm_force_prepared_pkg', 'activate_warm_replace_prepared_pkg', 'activate_warm_force_replace_prepared_pkg'], name, value)


        class Warm(_Entity_):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            .. attribute:: ids
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallActivate.Input.Warm, self).__init__()

                self.yang_name = "warm"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                    ('ids', (YLeafList(YType.str, 'ids'), ['str'])),
                ])
                self.packagename = []
                self.ids = []
                self._segment_path = lambda: "warm"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-activate/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallActivate.Input.Warm, ['packagename', 'ids'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallActivate.Input.Warm']['meta_info']


        class WarmForce(_Entity_):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            .. attribute:: ids
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallActivate.Input.WarmForce, self).__init__()

                self.yang_name = "warm-force"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                    ('ids', (YLeafList(YType.str, 'ids'), ['str'])),
                ])
                self.packagename = []
                self.ids = []
                self._segment_path = lambda: "warm-force"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-activate/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallActivate.Input.WarmForce, ['packagename', 'ids'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallActivate.Input.WarmForce']['meta_info']


        class WarmReplace(_Entity_):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            .. attribute:: ids
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallActivate.Input.WarmReplace, self).__init__()

                self.yang_name = "warm-replace"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                    ('ids', (YLeafList(YType.str, 'ids'), ['str'])),
                ])
                self.packagename = []
                self.ids = []
                self._segment_path = lambda: "warm-replace"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-activate/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallActivate.Input.WarmReplace, ['packagename', 'ids'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallActivate.Input.WarmReplace']['meta_info']


        class WarmReplaceForce(_Entity_):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            .. attribute:: ids
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallActivate.Input.WarmReplaceForce, self).__init__()

                self.yang_name = "warm-replace-force"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                    ('ids', (YLeafList(YType.str, 'ids'), ['str'])),
                ])
                self.packagename = []
                self.ids = []
                self._segment_path = lambda: "warm-replace-force"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-activate/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallActivate.Input.WarmReplaceForce, ['packagename', 'ids'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallActivate.Input.WarmReplaceForce']['meta_info']


        class Reload(_Entity_):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            .. attribute:: ids
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallActivate.Input.Reload, self).__init__()

                self.yang_name = "reload"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                    ('ids', (YLeafList(YType.str, 'ids'), ['str'])),
                ])
                self.packagename = []
                self.ids = []
                self._segment_path = lambda: "reload"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-activate/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallActivate.Input.Reload, ['packagename', 'ids'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallActivate.Input.Reload']['meta_info']


        class ReloadForce(_Entity_):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            .. attribute:: ids
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallActivate.Input.ReloadForce, self).__init__()

                self.yang_name = "reload-force"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                    ('ids', (YLeafList(YType.str, 'ids'), ['str'])),
                ])
                self.packagename = []
                self.ids = []
                self._segment_path = lambda: "reload-force"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-activate/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallActivate.Input.ReloadForce, ['packagename', 'ids'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallActivate.Input.ReloadForce']['meta_info']


        class Replace(_Entity_):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            .. attribute:: ids
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallActivate.Input.Replace, self).__init__()

                self.yang_name = "replace"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                    ('ids', (YLeafList(YType.str, 'ids'), ['str'])),
                ])
                self.packagename = []
                self.ids = []
                self._segment_path = lambda: "replace"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-activate/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallActivate.Input.Replace, ['packagename', 'ids'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallActivate.Input.Replace']['meta_info']


        class ReplaceForce(_Entity_):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            .. attribute:: ids
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallActivate.Input.ReplaceForce, self).__init__()

                self.yang_name = "replace-force"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                    ('ids', (YLeafList(YType.str, 'ids'), ['str'])),
                ])
                self.packagename = []
                self.ids = []
                self._segment_path = lambda: "replace-force"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-activate/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallActivate.Input.ReplaceForce, ['packagename', 'ids'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallActivate.Input.ReplaceForce']['meta_info']


        class ActivateForce(_Entity_):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            .. attribute:: ids
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallActivate.Input.ActivateForce, self).__init__()

                self.yang_name = "activate-force"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                    ('ids', (YLeafList(YType.str, 'ids'), ['str'])),
                ])
                self.packagename = []
                self.ids = []
                self._segment_path = lambda: "activate-force"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-activate/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallActivate.Input.ActivateForce, ['packagename', 'ids'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallActivate.Input.ActivateForce']['meta_info']


        class Packages(_Entity_):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallActivate.Input.Packages, self).__init__()

                self.yang_name = "packages"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                ])
                self.packagename = []
                self._segment_path = lambda: "packages"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-activate/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallActivate.Input.Packages, ['packagename'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallActivate.Input.Packages']['meta_info']


        class Ids(_Entity_):
            """
            
            
            .. attribute:: id_no
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallActivate.Input.Ids, self).__init__()

                self.yang_name = "ids"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('id_no', (YLeafList(YType.str, 'id-no'), ['str'])),
                ])
                self.id_no = []
                self._segment_path = lambda: "ids"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-activate/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallActivate.Input.Ids, ['id_no'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallActivate.Input.Ids']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
            return meta._meta_table['InstallActivate.Input']['meta_info']


    class Output(_Entity_):
        """
        
        
        .. attribute:: op_id
        
        	operation id of the triggered action
        	**type**\: str
        
        .. attribute:: error
        
        	case when op\-id is not triggered
        	**type**\: str
        
        

        """

        _prefix = 'install-act'
        _revision = '2018-09-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(InstallActivate.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "install-activate"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('op_id', (YLeaf(YType.str, 'op-id'), ['str'])),
                ('error', (YLeaf(YType.str, 'Error'), ['str'])),
            ])
            self.op_id = None
            self.error = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-activate/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InstallActivate.Output, ['op_id', 'error'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
            return meta._meta_table['InstallActivate.Output']['meta_info']

    def clone_ptr(self):
        self._top_entity = InstallActivate()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
        return meta._meta_table['InstallActivate']['meta_info']


class InstallDeactivate(_Entity_):
    """
    Cli\-command deactivate
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallDeactivate.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallDeactivate.Output>`
    
    

    """

    _prefix = 'install-act'
    _revision = '2018-09-10'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(InstallDeactivate, self).__init__()
        self._top_entity = None

        self.yang_name = "install-deactivate"
        self.yang_parent_name = "Cisco-IOS-XR-spirit-install-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = InstallDeactivate.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"

        self.output = InstallDeactivate.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._segment_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-deactivate"
        self._is_frozen = True


    class Input(_Entity_):
        """
        
        
        .. attribute:: reload
        
        	
        	**type**\:  :py:class:`Reload <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallDeactivate.Input.Reload>`
        
        .. attribute:: packages
        
        	
        	**type**\:  :py:class:`Packages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallDeactivate.Input.Packages>`
        
        .. attribute:: ids
        
        	
        	**type**\:  :py:class:`Ids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallDeactivate.Input.Ids>`
        
        .. attribute:: superseded
        
        	Deactivate all superseded packages
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'install-act'
        _revision = '2018-09-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(InstallDeactivate.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "install-deactivate"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("reload", ("reload", InstallDeactivate.Input.Reload)), ("packages", ("packages", InstallDeactivate.Input.Packages)), ("ids", ("ids", InstallDeactivate.Input.Ids))])
            self._leafs = OrderedDict([
                ('superseded', (YLeaf(YType.empty, 'superseded'), ['Empty'])),
            ])
            self.superseded = None

            self.reload = InstallDeactivate.Input.Reload()
            self.reload.parent = self
            self._children_name_map["reload"] = "reload"

            self.packages = InstallDeactivate.Input.Packages()
            self.packages.parent = self
            self._children_name_map["packages"] = "packages"

            self.ids = InstallDeactivate.Input.Ids()
            self.ids.parent = self
            self._children_name_map["ids"] = "ids"
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-deactivate/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InstallDeactivate.Input, ['superseded'], name, value)


        class Reload(_Entity_):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            .. attribute:: ids
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallDeactivate.Input.Reload, self).__init__()

                self.yang_name = "reload"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                    ('ids', (YLeafList(YType.str, 'ids'), ['str'])),
                ])
                self.packagename = []
                self.ids = []
                self._segment_path = lambda: "reload"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-deactivate/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallDeactivate.Input.Reload, ['packagename', 'ids'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallDeactivate.Input.Reload']['meta_info']


        class Packages(_Entity_):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallDeactivate.Input.Packages, self).__init__()

                self.yang_name = "packages"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                ])
                self.packagename = []
                self._segment_path = lambda: "packages"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-deactivate/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallDeactivate.Input.Packages, ['packagename'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallDeactivate.Input.Packages']['meta_info']


        class Ids(_Entity_):
            """
            
            
            .. attribute:: id_no
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallDeactivate.Input.Ids, self).__init__()

                self.yang_name = "ids"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('id_no', (YLeafList(YType.str, 'id-no'), ['str'])),
                ])
                self.id_no = []
                self._segment_path = lambda: "ids"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-deactivate/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallDeactivate.Input.Ids, ['id_no'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallDeactivate.Input.Ids']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
            return meta._meta_table['InstallDeactivate.Input']['meta_info']


    class Output(_Entity_):
        """
        
        
        .. attribute:: op_id
        
        	operation id of the triggered action
        	**type**\: str
        
        .. attribute:: error
        
        	case when op\-id is not triggered
        	**type**\: str
        
        

        """

        _prefix = 'install-act'
        _revision = '2018-09-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(InstallDeactivate.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "install-deactivate"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('op_id', (YLeaf(YType.str, 'op-id'), ['str'])),
                ('error', (YLeaf(YType.str, 'Error'), ['str'])),
            ])
            self.op_id = None
            self.error = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-deactivate/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InstallDeactivate.Output, ['op_id', 'error'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
            return meta._meta_table['InstallDeactivate.Output']['meta_info']

    def clone_ptr(self):
        self._top_entity = InstallDeactivate()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
        return meta._meta_table['InstallDeactivate']['meta_info']


class InstallExtract(_Entity_):
    """
    Cli\-command extract
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallExtract.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallExtract.Output>`
    
    

    """

    _prefix = 'install-act'
    _revision = '2018-09-10'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(InstallExtract, self).__init__()
        self._top_entity = None

        self.yang_name = "install-extract"
        self.yang_parent_name = "Cisco-IOS-XR-spirit-install-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = InstallExtract.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"

        self.output = InstallExtract.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._segment_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-extract"
        self._is_frozen = True


    class Input(_Entity_):
        """
        
        
        .. attribute:: packages
        
        	
        	**type**\:  :py:class:`Packages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallExtract.Input.Packages>`
        
        

        """

        _prefix = 'install-act'
        _revision = '2018-09-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(InstallExtract.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "install-extract"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("packages", ("packages", InstallExtract.Input.Packages))])
            self._leafs = OrderedDict()

            self.packages = InstallExtract.Input.Packages()
            self.packages.parent = self
            self._children_name_map["packages"] = "packages"
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-extract/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InstallExtract.Input, [], name, value)


        class Packages(_Entity_):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallExtract.Input.Packages, self).__init__()

                self.yang_name = "packages"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                ])
                self.packagename = []
                self._segment_path = lambda: "packages"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-extract/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallExtract.Input.Packages, ['packagename'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallExtract.Input.Packages']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
            return meta._meta_table['InstallExtract.Input']['meta_info']


    class Output(_Entity_):
        """
        
        
        .. attribute:: op_id
        
        	operation id of the triggered action
        	**type**\: str
        
        .. attribute:: error
        
        	case when op\-id is not triggered
        	**type**\: str
        
        

        """

        _prefix = 'install-act'
        _revision = '2018-09-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(InstallExtract.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "install-extract"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('op_id', (YLeaf(YType.str, 'op-id'), ['str'])),
                ('error', (YLeaf(YType.str, 'Error'), ['str'])),
            ])
            self.op_id = None
            self.error = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-extract/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InstallExtract.Output, ['op_id', 'error'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
            return meta._meta_table['InstallExtract.Output']['meta_info']

    def clone_ptr(self):
        self._top_entity = InstallExtract()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
        return meta._meta_table['InstallExtract']['meta_info']


class InstallVerify(_Entity_):
    """
    Cli\-command install verify packages
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallVerify.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallVerify.Output>`
    
    

    """

    _prefix = 'install-act'
    _revision = '2018-09-10'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(InstallVerify, self).__init__()
        self._top_entity = None

        self.yang_name = "install-verify"
        self.yang_parent_name = "Cisco-IOS-XR-spirit-install-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = InstallVerify.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"

        self.output = InstallVerify.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._segment_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-verify"
        self._is_frozen = True


    class Input(_Entity_):
        """
        
        
        .. attribute:: location
        
        	
        	**type**\: list of str
        
        

        """

        _prefix = 'install-act'
        _revision = '2018-09-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(InstallVerify.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "install-verify"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('location', (YLeafList(YType.str, 'location'), ['str'])),
            ])
            self.location = []
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-verify/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InstallVerify.Input, ['location'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
            return meta._meta_table['InstallVerify.Input']['meta_info']


    class Output(_Entity_):
        """
        
        
        .. attribute:: op_id
        
        	operation id of the triggered action
        	**type**\: str
        
        .. attribute:: error
        
        	case when op\-id is not triggered
        	**type**\: str
        
        

        """

        _prefix = 'install-act'
        _revision = '2018-09-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(InstallVerify.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "install-verify"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('op_id', (YLeaf(YType.str, 'op-id'), ['str'])),
                ('error', (YLeaf(YType.str, 'Error'), ['str'])),
            ])
            self.op_id = None
            self.error = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-verify/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InstallVerify.Output, ['op_id', 'error'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
            return meta._meta_table['InstallVerify.Output']['meta_info']

    def clone_ptr(self):
        self._top_entity = InstallVerify()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
        return meta._meta_table['InstallVerify']['meta_info']


class InstallUpdate(_Entity_):
    """
    Cli\-command install update
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallUpdate.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallUpdate.Output>`
    
    

    """

    _prefix = 'install-act'
    _revision = '2018-09-10'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(InstallUpdate, self).__init__()
        self._top_entity = None

        self.yang_name = "install-update"
        self.yang_parent_name = "Cisco-IOS-XR-spirit-install-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = InstallUpdate.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"

        self.output = InstallUpdate.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._segment_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-update"
        self._is_frozen = True


    class Input(_Entity_):
        """
        
        
        .. attribute:: packagepath
        
        	
        	**type**\: str
        
        .. attribute:: packagename
        
        	
        	**type**\: list of str
        
        .. attribute:: warm
        
        	
        	**type**\:  :py:class:`Warm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallUpdate.Input.Warm>`
        
        .. attribute:: warm_force
        
        	
        	**type**\:  :py:class:`WarmForce <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallUpdate.Input.WarmForce>`
        
        .. attribute:: warm_replace
        
        	
        	**type**\:  :py:class:`WarmReplace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallUpdate.Input.WarmReplace>`
        
        .. attribute:: warm_replace_force
        
        	
        	**type**\:  :py:class:`WarmReplaceForce <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallUpdate.Input.WarmReplaceForce>`
        
        .. attribute:: force
        
        	
        	**type**\:  :py:class:`Force <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallUpdate.Input.Force>`
        
        .. attribute:: replace
        
        	
        	**type**\:  :py:class:`Replace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallUpdate.Input.Replace>`
        
        .. attribute:: replace_force
        
        	
        	**type**\:  :py:class:`ReplaceForce <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallUpdate.Input.ReplaceForce>`
        
        .. attribute:: replace_commit
        
        	
        	**type**\:  :py:class:`ReplaceCommit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallUpdate.Input.ReplaceCommit>`
        
        .. attribute:: replace_commit_force
        
        	
        	**type**\:  :py:class:`ReplaceCommitForce <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallUpdate.Input.ReplaceCommitForce>`
        
        

        """

        _prefix = 'install-act'
        _revision = '2018-09-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(InstallUpdate.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "install-update"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("warm", ("warm", InstallUpdate.Input.Warm)), ("warm-force", ("warm_force", InstallUpdate.Input.WarmForce)), ("warm-replace", ("warm_replace", InstallUpdate.Input.WarmReplace)), ("warm-replace-force", ("warm_replace_force", InstallUpdate.Input.WarmReplaceForce)), ("force", ("force", InstallUpdate.Input.Force)), ("replace", ("replace", InstallUpdate.Input.Replace)), ("replace-force", ("replace_force", InstallUpdate.Input.ReplaceForce)), ("replace-commit", ("replace_commit", InstallUpdate.Input.ReplaceCommit)), ("replace-commit-force", ("replace_commit_force", InstallUpdate.Input.ReplaceCommitForce))])
            self._leafs = OrderedDict([
                ('packagepath', (YLeaf(YType.str, 'packagepath'), ['str'])),
                ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
            ])
            self.packagepath = None
            self.packagename = []

            self.warm = InstallUpdate.Input.Warm()
            self.warm.parent = self
            self._children_name_map["warm"] = "warm"

            self.warm_force = InstallUpdate.Input.WarmForce()
            self.warm_force.parent = self
            self._children_name_map["warm_force"] = "warm-force"

            self.warm_replace = InstallUpdate.Input.WarmReplace()
            self.warm_replace.parent = self
            self._children_name_map["warm_replace"] = "warm-replace"

            self.warm_replace_force = InstallUpdate.Input.WarmReplaceForce()
            self.warm_replace_force.parent = self
            self._children_name_map["warm_replace_force"] = "warm-replace-force"

            self.force = InstallUpdate.Input.Force()
            self.force.parent = self
            self._children_name_map["force"] = "force"

            self.replace = InstallUpdate.Input.Replace()
            self.replace.parent = self
            self._children_name_map["replace"] = "replace"

            self.replace_force = InstallUpdate.Input.ReplaceForce()
            self.replace_force.parent = self
            self._children_name_map["replace_force"] = "replace-force"

            self.replace_commit = InstallUpdate.Input.ReplaceCommit()
            self.replace_commit.parent = self
            self._children_name_map["replace_commit"] = "replace-commit"

            self.replace_commit_force = InstallUpdate.Input.ReplaceCommitForce()
            self.replace_commit_force.parent = self
            self._children_name_map["replace_commit_force"] = "replace-commit-force"
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-update/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InstallUpdate.Input, ['packagepath', 'packagename'], name, value)


        class Warm(_Entity_):
            """
            
            
            .. attribute:: packagepath
            
            	
            	**type**\: str
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallUpdate.Input.Warm, self).__init__()

                self.yang_name = "warm"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagepath', (YLeaf(YType.str, 'packagepath'), ['str'])),
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                ])
                self.packagepath = None
                self.packagename = []
                self._segment_path = lambda: "warm"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-update/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallUpdate.Input.Warm, ['packagepath', 'packagename'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallUpdate.Input.Warm']['meta_info']


        class WarmForce(_Entity_):
            """
            
            
            .. attribute:: packagepath
            
            	
            	**type**\: str
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallUpdate.Input.WarmForce, self).__init__()

                self.yang_name = "warm-force"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagepath', (YLeaf(YType.str, 'packagepath'), ['str'])),
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                ])
                self.packagepath = None
                self.packagename = []
                self._segment_path = lambda: "warm-force"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-update/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallUpdate.Input.WarmForce, ['packagepath', 'packagename'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallUpdate.Input.WarmForce']['meta_info']


        class WarmReplace(_Entity_):
            """
            
            
            .. attribute:: packagepath
            
            	
            	**type**\: str
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallUpdate.Input.WarmReplace, self).__init__()

                self.yang_name = "warm-replace"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagepath', (YLeaf(YType.str, 'packagepath'), ['str'])),
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                ])
                self.packagepath = None
                self.packagename = []
                self._segment_path = lambda: "warm-replace"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-update/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallUpdate.Input.WarmReplace, ['packagepath', 'packagename'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallUpdate.Input.WarmReplace']['meta_info']


        class WarmReplaceForce(_Entity_):
            """
            
            
            .. attribute:: packagepath
            
            	
            	**type**\: str
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallUpdate.Input.WarmReplaceForce, self).__init__()

                self.yang_name = "warm-replace-force"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagepath', (YLeaf(YType.str, 'packagepath'), ['str'])),
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                ])
                self.packagepath = None
                self.packagename = []
                self._segment_path = lambda: "warm-replace-force"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-update/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallUpdate.Input.WarmReplaceForce, ['packagepath', 'packagename'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallUpdate.Input.WarmReplaceForce']['meta_info']


        class Force(_Entity_):
            """
            
            
            .. attribute:: packagepath
            
            	
            	**type**\: str
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallUpdate.Input.Force, self).__init__()

                self.yang_name = "force"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagepath', (YLeaf(YType.str, 'packagepath'), ['str'])),
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                ])
                self.packagepath = None
                self.packagename = []
                self._segment_path = lambda: "force"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-update/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallUpdate.Input.Force, ['packagepath', 'packagename'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallUpdate.Input.Force']['meta_info']


        class Replace(_Entity_):
            """
            
            
            .. attribute:: packagepath
            
            	
            	**type**\: str
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallUpdate.Input.Replace, self).__init__()

                self.yang_name = "replace"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagepath', (YLeaf(YType.str, 'packagepath'), ['str'])),
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                ])
                self.packagepath = None
                self.packagename = []
                self._segment_path = lambda: "replace"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-update/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallUpdate.Input.Replace, ['packagepath', 'packagename'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallUpdate.Input.Replace']['meta_info']


        class ReplaceForce(_Entity_):
            """
            
            
            .. attribute:: packagepath
            
            	
            	**type**\: str
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallUpdate.Input.ReplaceForce, self).__init__()

                self.yang_name = "replace-force"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagepath', (YLeaf(YType.str, 'packagepath'), ['str'])),
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                ])
                self.packagepath = None
                self.packagename = []
                self._segment_path = lambda: "replace-force"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-update/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallUpdate.Input.ReplaceForce, ['packagepath', 'packagename'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallUpdate.Input.ReplaceForce']['meta_info']


        class ReplaceCommit(_Entity_):
            """
            
            
            .. attribute:: packagepath
            
            	
            	**type**\: str
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallUpdate.Input.ReplaceCommit, self).__init__()

                self.yang_name = "replace-commit"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagepath', (YLeaf(YType.str, 'packagepath'), ['str'])),
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                ])
                self.packagepath = None
                self.packagename = []
                self._segment_path = lambda: "replace-commit"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-update/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallUpdate.Input.ReplaceCommit, ['packagepath', 'packagename'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallUpdate.Input.ReplaceCommit']['meta_info']


        class ReplaceCommitForce(_Entity_):
            """
            
            
            .. attribute:: packagepath
            
            	
            	**type**\: str
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2018-09-10'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(InstallUpdate.Input.ReplaceCommitForce, self).__init__()

                self.yang_name = "replace-commit-force"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packagepath', (YLeaf(YType.str, 'packagepath'), ['str'])),
                    ('packagename', (YLeafList(YType.str, 'packagename'), ['str'])),
                ])
                self.packagepath = None
                self.packagename = []
                self._segment_path = lambda: "replace-commit-force"
                self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-update/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InstallUpdate.Input.ReplaceCommitForce, ['packagepath', 'packagename'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
                return meta._meta_table['InstallUpdate.Input.ReplaceCommitForce']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
            return meta._meta_table['InstallUpdate.Input']['meta_info']


    class Output(_Entity_):
        """
        
        
        .. attribute:: op_id
        
        	operation id of the triggered action
        	**type**\: str
        
        .. attribute:: error
        
        	case when op\-id is not triggered
        	**type**\: str
        
        

        """

        _prefix = 'install-act'
        _revision = '2018-09-10'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(InstallUpdate.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "install-update"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('op_id', (YLeaf(YType.str, 'op-id'), ['str'])),
                ('error', (YLeaf(YType.str, 'Error'), ['str'])),
            ])
            self.op_id = None
            self.error = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-update/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InstallUpdate.Output, ['op_id', 'error'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
            return meta._meta_table['InstallUpdate.Output']['meta_info']

    def clone_ptr(self):
        self._top_entity = InstallUpdate()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_spirit_install_act as meta
        return meta._meta_table['InstallUpdate']['meta_info']



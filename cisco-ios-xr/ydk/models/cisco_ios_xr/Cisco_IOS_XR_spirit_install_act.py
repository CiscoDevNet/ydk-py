""" Cisco_IOS_XR_spirit_install_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR action package configuration.

Copyright (c) 2016\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class InstallAdd(Entity):
    """
    Cli\-command install add source
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallAdd.Input>`
    
    

    """

    _prefix = 'install-act'
    _revision = '2017-10-23'

    def __init__(self):
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
        self._segment_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-add"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: packagepath
        
        	
        	**type**\: str
        
        .. attribute:: packagename
        
        	
        	**type**\: list of str
        
        

        """

        _prefix = 'install-act'
        _revision = '2017-10-23'

        def __init__(self):
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

    def clone_ptr(self):
        self._top_entity = InstallAdd()
        return self._top_entity

class InstallCommit(Entity):
    """
    Cli\-command install commit
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallCommit.Input>`
    
    

    """

    _prefix = 'install-act'
    _revision = '2017-10-23'

    def __init__(self):
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
        self._segment_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-commit"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: sdr
        
        	commit packages in the system
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'install-act'
        _revision = '2017-10-23'

        def __init__(self):
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

    def clone_ptr(self):
        self._top_entity = InstallCommit()
        return self._top_entity

class InstallRemove(Entity):
    """
    Cli\-command remove
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallRemove.Input>`
    
    

    """

    _prefix = 'install-act'
    _revision = '2017-10-23'

    def __init__(self):
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
        self._segment_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-remove"
        self._is_frozen = True


    class Input(Entity):
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
        _revision = '2017-10-23'

        def __init__(self):
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


        class Packages(Entity):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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


        class Ids(Entity):
            """
            
            
            .. attribute:: id_no
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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

    def clone_ptr(self):
        self._top_entity = InstallRemove()
        return self._top_entity

class InstallPrepare(Entity):
    """
    Cli\-command prepare
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallPrepare.Input>`
    
    

    """

    _prefix = 'install-act'
    _revision = '2017-10-23'

    def __init__(self):
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
        self._segment_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-prepare"
        self._is_frozen = True


    class Input(Entity):
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
        _revision = '2017-10-23'

        def __init__(self):
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


        class Packages(Entity):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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


        class Ids(Entity):
            """
            
            
            .. attribute:: id_no
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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


        class PrepareForce(Entity):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            .. attribute:: ids
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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

    def clone_ptr(self):
        self._top_entity = InstallPrepare()
        return self._top_entity

class InstallActivate(Entity):
    """
    Cli\-command activate
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallActivate.Input>`
    
    

    """

    _prefix = 'install-act'
    _revision = '2017-10-23'

    def __init__(self):
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
        self._segment_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-activate"
        self._is_frozen = True


    class Input(Entity):
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
        _revision = '2017-10-23'

        def __init__(self):
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


        class Warm(Entity):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            .. attribute:: ids
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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


        class WarmForce(Entity):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            .. attribute:: ids
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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


        class WarmReplace(Entity):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            .. attribute:: ids
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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


        class WarmReplaceForce(Entity):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            .. attribute:: ids
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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


        class Reload(Entity):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            .. attribute:: ids
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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


        class ReloadForce(Entity):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            .. attribute:: ids
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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


        class Replace(Entity):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            .. attribute:: ids
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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


        class ReplaceForce(Entity):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            .. attribute:: ids
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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


        class ActivateForce(Entity):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            .. attribute:: ids
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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


        class Packages(Entity):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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


        class Ids(Entity):
            """
            
            
            .. attribute:: id_no
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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

    def clone_ptr(self):
        self._top_entity = InstallActivate()
        return self._top_entity

class InstallDeactivate(Entity):
    """
    Cli\-command deactivate
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallDeactivate.Input>`
    
    

    """

    _prefix = 'install-act'
    _revision = '2017-10-23'

    def __init__(self):
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
        self._segment_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-deactivate"
        self._is_frozen = True


    class Input(Entity):
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
        _revision = '2017-10-23'

        def __init__(self):
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


        class Reload(Entity):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            .. attribute:: ids
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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


        class Packages(Entity):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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


        class Ids(Entity):
            """
            
            
            .. attribute:: id_no
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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

    def clone_ptr(self):
        self._top_entity = InstallDeactivate()
        return self._top_entity

class InstallExtract(Entity):
    """
    Cli\-command extract
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallExtract.Input>`
    
    

    """

    _prefix = 'install-act'
    _revision = '2017-10-23'

    def __init__(self):
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
        self._segment_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-extract"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: packages
        
        	
        	**type**\:  :py:class:`Packages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallExtract.Input.Packages>`
        
        

        """

        _prefix = 'install-act'
        _revision = '2017-10-23'

        def __init__(self):
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


        class Packages(Entity):
            """
            
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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

    def clone_ptr(self):
        self._top_entity = InstallExtract()
        return self._top_entity

class InstallVerify(Entity):
    """
    Cli\-command install verify packages
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallVerify.Input>`
    
    

    """

    _prefix = 'install-act'
    _revision = '2017-10-23'

    def __init__(self):
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
        self._segment_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-verify"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: location
        
        	
        	**type**\: list of str
        
        

        """

        _prefix = 'install-act'
        _revision = '2017-10-23'

        def __init__(self):
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

    def clone_ptr(self):
        self._top_entity = InstallVerify()
        return self._top_entity

class InstallUpdate(Entity):
    """
    Cli\-command install update
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_act.InstallUpdate.Input>`
    
    

    """

    _prefix = 'install-act'
    _revision = '2017-10-23'

    def __init__(self):
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
        self._segment_path = lambda: "Cisco-IOS-XR-spirit-install-act:install-update"
        self._is_frozen = True


    class Input(Entity):
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
        _revision = '2017-10-23'

        def __init__(self):
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


        class Warm(Entity):
            """
            
            
            .. attribute:: packagepath
            
            	
            	**type**\: str
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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


        class WarmForce(Entity):
            """
            
            
            .. attribute:: packagepath
            
            	
            	**type**\: str
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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


        class WarmReplace(Entity):
            """
            
            
            .. attribute:: packagepath
            
            	
            	**type**\: str
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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


        class WarmReplaceForce(Entity):
            """
            
            
            .. attribute:: packagepath
            
            	
            	**type**\: str
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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


        class Force(Entity):
            """
            
            
            .. attribute:: packagepath
            
            	
            	**type**\: str
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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


        class Replace(Entity):
            """
            
            
            .. attribute:: packagepath
            
            	
            	**type**\: str
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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


        class ReplaceForce(Entity):
            """
            
            
            .. attribute:: packagepath
            
            	
            	**type**\: str
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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


        class ReplaceCommit(Entity):
            """
            
            
            .. attribute:: packagepath
            
            	
            	**type**\: str
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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


        class ReplaceCommitForce(Entity):
            """
            
            
            .. attribute:: packagepath
            
            	
            	**type**\: str
            
            .. attribute:: packagename
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install-act'
            _revision = '2017-10-23'

            def __init__(self):
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

    def clone_ptr(self):
        self._top_entity = InstallUpdate()
        return self._top_entity


""" Cisco_IOS_XR_sysadmin_instmgr_oper 

This module contains a collection of YANG
definitions for Cisco IOS\-XR sysadmin\-instmgr 
operational model

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Install(Entity):
    """
    
    
    .. attribute:: version
    
    	Gives sysadmin version information
    	**type**\:  :py:class:`Version <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Version>`
    
    .. attribute:: inactive
    
    	Calvados inactive package(s) list for this node
    	**type**\:  :py:class:`Inactive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Inactive>`
    
    .. attribute:: prepare
    
    	Calvados prepared package(s) list for this node
    	**type**\:  :py:class:`Prepare <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Prepare>`
    
    .. attribute:: package
    
    	Package Name(s) to get info for
    	**type**\:  :py:class:`Package <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Package>`
    
    .. attribute:: active
    
    	Calvados active package(s) list for this node
    	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Active>`
    
    .. attribute:: superseded
    
    	Calvados superseded package(s) list for this node
    	**type**\:  :py:class:`Superseded <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Superseded>`
    
    .. attribute:: request
    
    	Sysadmin current install operation details
    	**type**\:  :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Request>`
    
    .. attribute:: repository
    
    	Shows information about the install software repository
    	**type**\:  :py:class:`Repository <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Repository>`
    
    .. attribute:: log
    
    	
    	**type**\:  :py:class:`Log <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Log>`
    
    .. attribute:: which
    
    	Filename to get info for
    	**type**\:  :py:class:`Which <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Which>`
    
    .. attribute:: committed
    
    	Calvados committed package(s) list for this node
    	**type**\:  :py:class:`Committed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Committed>`
    
    

    """

    _prefix = 'install'
    _revision = '2017-10-13'

    def __init__(self):
        super(Install, self).__init__()
        self._top_entity = None

        self.yang_name = "install"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-instmgr-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("version", ("version", Install.Version)), ("inactive", ("inactive", Install.Inactive)), ("prepare", ("prepare", Install.Prepare)), ("package", ("package", Install.Package)), ("active", ("active", Install.Active)), ("superseded", ("superseded", Install.Superseded)), ("request", ("request", Install.Request)), ("repository", ("repository", Install.Repository)), ("log", ("log", Install.Log)), ("which", ("which", Install.Which)), ("committed", ("committed", Install.Committed))])
        self._leafs = OrderedDict()

        self.version = Install.Version()
        self.version.parent = self
        self._children_name_map["version"] = "version"

        self.inactive = Install.Inactive()
        self.inactive.parent = self
        self._children_name_map["inactive"] = "inactive"

        self.prepare = Install.Prepare()
        self.prepare.parent = self
        self._children_name_map["prepare"] = "prepare"

        self.package = Install.Package()
        self.package.parent = self
        self._children_name_map["package"] = "package"

        self.active = Install.Active()
        self.active.parent = self
        self._children_name_map["active"] = "active"

        self.superseded = Install.Superseded()
        self.superseded.parent = self
        self._children_name_map["superseded"] = "superseded"

        self.request = Install.Request()
        self.request.parent = self
        self._children_name_map["request"] = "request"

        self.repository = Install.Repository()
        self.repository.parent = self
        self._children_name_map["repository"] = "repository"

        self.log = Install.Log()
        self.log.parent = self
        self._children_name_map["log"] = "log"

        self.which = Install.Which()
        self.which.parent = self
        self._children_name_map["which"] = "which"

        self.committed = Install.Committed()
        self.committed.parent = self
        self._children_name_map["committed"] = "committed"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-instmgr-oper:install"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Install, [], name, value)


    class Version(Entity):
        """
        Gives sysadmin version information
        
        .. attribute:: img_info
        
        	
        	**type**\: list of str
        
        

        """

        _prefix = 'install'
        _revision = '2017-10-13'

        def __init__(self):
            super(Install.Version, self).__init__()

            self.yang_name = "version"
            self.yang_parent_name = "install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('img_info', (YLeafList(YType.str, 'img_info'), ['str'])),
            ])
            self.img_info = []
            self._segment_path = lambda: "version"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-instmgr-oper:install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Install.Version, ['img_info'], name, value)


    class Inactive(Entity):
        """
        Calvados inactive package(s) list for this node
        
        .. attribute:: summary
        
        	shows summary information of the inactive install software
        	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Inactive.Summary>`
        
        .. attribute:: si_inactive_output
        
        	
        	**type**\: list of str
        
        

        """

        _prefix = 'install'
        _revision = '2017-10-13'

        def __init__(self):
            super(Install.Inactive, self).__init__()

            self.yang_name = "inactive"
            self.yang_parent_name = "install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("summary", ("summary", Install.Inactive.Summary))])
            self._leafs = OrderedDict([
                ('si_inactive_output', (YLeafList(YType.str, 'si_inactive_output'), ['str'])),
            ])
            self.si_inactive_output = []

            self.summary = Install.Inactive.Summary()
            self.summary.parent = self
            self._children_name_map["summary"] = "summary"
            self._segment_path = lambda: "inactive"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-instmgr-oper:install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Install.Inactive, ['si_inactive_output'], name, value)


        class Summary(Entity):
            """
            shows summary information of the inactive install software
            
            .. attribute:: si_inactive_summary_output
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install'
            _revision = '2017-10-13'

            def __init__(self):
                super(Install.Inactive.Summary, self).__init__()

                self.yang_name = "summary"
                self.yang_parent_name = "inactive"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('si_inactive_summary_output', (YLeafList(YType.str, 'si_inactive_summary_output'), ['str'])),
                ])
                self.si_inactive_summary_output = []
                self._segment_path = lambda: "summary"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-instmgr-oper:install/inactive/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Install.Inactive.Summary, ['si_inactive_summary_output'], name, value)


    class Prepare(Entity):
        """
        Calvados prepared package(s) list for this node
        
        .. attribute:: si_prepare_output
        
        	
        	**type**\: list of str
        
        

        """

        _prefix = 'install'
        _revision = '2017-10-13'

        def __init__(self):
            super(Install.Prepare, self).__init__()

            self.yang_name = "prepare"
            self.yang_parent_name = "install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('si_prepare_output', (YLeafList(YType.str, 'si_prepare_output'), ['str'])),
            ])
            self.si_prepare_output = []
            self._segment_path = lambda: "prepare"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-instmgr-oper:install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Install.Prepare, ['si_prepare_output'], name, value)


    class Package(Entity):
        """
        Package Name(s) to get info for
        
        .. attribute:: pkg_list
        
        	
        	**type**\: list of  		 :py:class:`PkgList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Package.PkgList>`
        
        

        """

        _prefix = 'install'
        _revision = '2017-10-13'

        def __init__(self):
            super(Install.Package, self).__init__()

            self.yang_name = "package"
            self.yang_parent_name = "install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("pkg_list", ("pkg_list", Install.Package.PkgList))])
            self._leafs = OrderedDict()

            self.pkg_list = YList(self)
            self._segment_path = lambda: "package"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-instmgr-oper:install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Install.Package, [], name, value)


        class PkgList(Entity):
            """
            
            
            .. attribute:: pkg_name  (key)
            
            	
            	**type**\: str
            
            .. attribute:: detail
            
            	
            	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Package.PkgList.Detail>`
            
            .. attribute:: verbose
            
            	
            	**type**\:  :py:class:`Verbose <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Package.PkgList.Verbose>`
            
            .. attribute:: si_package_output
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install'
            _revision = '2017-10-13'

            def __init__(self):
                super(Install.Package.PkgList, self).__init__()

                self.yang_name = "pkg_list"
                self.yang_parent_name = "package"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['pkg_name']
                self._child_classes = OrderedDict([("detail", ("detail", Install.Package.PkgList.Detail)), ("verbose", ("verbose", Install.Package.PkgList.Verbose))])
                self._leafs = OrderedDict([
                    ('pkg_name', (YLeaf(YType.str, 'pkg_name'), ['str'])),
                    ('si_package_output', (YLeafList(YType.str, 'si_package_output'), ['str'])),
                ])
                self.pkg_name = None
                self.si_package_output = []

                self.detail = Install.Package.PkgList.Detail()
                self.detail.parent = self
                self._children_name_map["detail"] = "detail"

                self.verbose = Install.Package.PkgList.Verbose()
                self.verbose.parent = self
                self._children_name_map["verbose"] = "verbose"
                self._segment_path = lambda: "pkg_list" + "[pkg_name='" + str(self.pkg_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-instmgr-oper:install/package/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Install.Package.PkgList, ['pkg_name', 'si_package_output'], name, value)


            class Detail(Entity):
                """
                
                
                .. attribute:: si_package_detail_output
                
                	
                	**type**\: list of str
                
                

                """

                _prefix = 'install'
                _revision = '2017-10-13'

                def __init__(self):
                    super(Install.Package.PkgList.Detail, self).__init__()

                    self.yang_name = "detail"
                    self.yang_parent_name = "pkg_list"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('si_package_detail_output', (YLeafList(YType.str, 'si_package_detail_output'), ['str'])),
                    ])
                    self.si_package_detail_output = []
                    self._segment_path = lambda: "detail"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.Package.PkgList.Detail, ['si_package_detail_output'], name, value)


            class Verbose(Entity):
                """
                
                
                .. attribute:: si_package_verbose_output
                
                	
                	**type**\: list of str
                
                

                """

                _prefix = 'install'
                _revision = '2017-10-13'

                def __init__(self):
                    super(Install.Package.PkgList.Verbose, self).__init__()

                    self.yang_name = "verbose"
                    self.yang_parent_name = "pkg_list"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('si_package_verbose_output', (YLeafList(YType.str, 'si_package_verbose_output'), ['str'])),
                    ])
                    self.si_package_verbose_output = []
                    self._segment_path = lambda: "verbose"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.Package.PkgList.Verbose, ['si_package_verbose_output'], name, value)


    class Active(Entity):
        """
        Calvados active package(s) list for this node
        
        .. attribute:: summary
        
        	shows summary information of the active install software
        	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Active.Summary>`
        
        .. attribute:: si_active_output
        
        	
        	**type**\: list of str
        
        

        """

        _prefix = 'install'
        _revision = '2017-10-13'

        def __init__(self):
            super(Install.Active, self).__init__()

            self.yang_name = "active"
            self.yang_parent_name = "install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("summary", ("summary", Install.Active.Summary))])
            self._leafs = OrderedDict([
                ('si_active_output', (YLeafList(YType.str, 'si_active_output'), ['str'])),
            ])
            self.si_active_output = []

            self.summary = Install.Active.Summary()
            self.summary.parent = self
            self._children_name_map["summary"] = "summary"
            self._segment_path = lambda: "active"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-instmgr-oper:install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Install.Active, ['si_active_output'], name, value)


        class Summary(Entity):
            """
            shows summary information of the active install software
            
            .. attribute:: si_active_summary_output
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install'
            _revision = '2017-10-13'

            def __init__(self):
                super(Install.Active.Summary, self).__init__()

                self.yang_name = "summary"
                self.yang_parent_name = "active"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('si_active_summary_output', (YLeafList(YType.str, 'si_active_summary_output'), ['str'])),
                ])
                self.si_active_summary_output = []
                self._segment_path = lambda: "summary"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-instmgr-oper:install/active/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Install.Active.Summary, ['si_active_summary_output'], name, value)


    class Superseded(Entity):
        """
        Calvados superseded package(s) list for this node
        
        .. attribute:: summary
        
        	shows summary information of the show install superseded
        	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Superseded.Summary>`
        
        .. attribute:: si_superseded_output
        
        	
        	**type**\: list of str
        
        

        """

        _prefix = 'install'
        _revision = '2017-10-13'

        def __init__(self):
            super(Install.Superseded, self).__init__()

            self.yang_name = "superseded"
            self.yang_parent_name = "install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("summary", ("summary", Install.Superseded.Summary))])
            self._leafs = OrderedDict([
                ('si_superseded_output', (YLeafList(YType.str, 'si_superseded_output'), ['str'])),
            ])
            self.si_superseded_output = []

            self.summary = Install.Superseded.Summary()
            self.summary.parent = self
            self._children_name_map["summary"] = "summary"
            self._segment_path = lambda: "superseded"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-instmgr-oper:install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Install.Superseded, ['si_superseded_output'], name, value)


        class Summary(Entity):
            """
            shows summary information of the show install superseded
            
            .. attribute:: si_superseded_summary_output
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install'
            _revision = '2017-10-13'

            def __init__(self):
                super(Install.Superseded.Summary, self).__init__()

                self.yang_name = "summary"
                self.yang_parent_name = "superseded"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('si_superseded_summary_output', (YLeafList(YType.str, 'si_superseded_summary_output'), ['str'])),
                ])
                self.si_superseded_summary_output = []
                self._segment_path = lambda: "summary"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-instmgr-oper:install/superseded/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Install.Superseded.Summary, ['si_superseded_summary_output'], name, value)


    class Request(Entity):
        """
        Sysadmin current install operation details
        
        .. attribute:: curr_inst_oper
        
        	
        	**type**\: list of str
        
        

        """

        _prefix = 'install'
        _revision = '2017-10-13'

        def __init__(self):
            super(Install.Request, self).__init__()

            self.yang_name = "request"
            self.yang_parent_name = "install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('curr_inst_oper', (YLeafList(YType.str, 'curr_inst_oper'), ['str'])),
            ])
            self.curr_inst_oper = []
            self._segment_path = lambda: "request"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-instmgr-oper:install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Install.Request, ['curr_inst_oper'], name, value)


    class Repository(Entity):
        """
        Shows information about the install software repository.
        
        .. attribute:: all
        
        	shows contents of all the install software repositories
        	**type**\:  :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Repository.All>`
        
        .. attribute:: si_repository_output
        
        	
        	**type**\: list of str
        
        

        """

        _prefix = 'install'
        _revision = '2017-10-13'

        def __init__(self):
            super(Install.Repository, self).__init__()

            self.yang_name = "repository"
            self.yang_parent_name = "install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("all", ("all", Install.Repository.All))])
            self._leafs = OrderedDict([
                ('si_repository_output', (YLeafList(YType.str, 'si_repository_output'), ['str'])),
            ])
            self.si_repository_output = []

            self.all = Install.Repository.All()
            self.all.parent = self
            self._children_name_map["all"] = "all"
            self._segment_path = lambda: "repository"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-instmgr-oper:install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Install.Repository, ['si_repository_output'], name, value)


        class All(Entity):
            """
            shows contents of all the install software repositories
            
            .. attribute:: si_repository_all_output
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install'
            _revision = '2017-10-13'

            def __init__(self):
                super(Install.Repository.All, self).__init__()

                self.yang_name = "all"
                self.yang_parent_name = "repository"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('si_repository_all_output', (YLeafList(YType.str, 'si_repository_all_output'), ['str'])),
                ])
                self.si_repository_all_output = []
                self._segment_path = lambda: "all"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-instmgr-oper:install/repository/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Install.Repository.All, ['si_repository_all_output'], name, value)


    class Log(Entity):
        """
        
        
        .. attribute:: id
        
        	
        	**type**\: list of  		 :py:class:`Id <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Log.Id>`
        
        .. attribute:: reverse
        
        	
        	**type**\:  :py:class:`Reverse <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Log.Reverse>`
        
        .. attribute:: detail
        
        	
        	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Log.Detail>`
        
        .. attribute:: si_log_output
        
        	
        	**type**\: list of str
        
        

        """

        _prefix = 'install'
        _revision = '2017-10-13'

        def __init__(self):
            super(Install.Log, self).__init__()

            self.yang_name = "log"
            self.yang_parent_name = "install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("id", ("id", Install.Log.Id)), ("reverse", ("reverse", Install.Log.Reverse)), ("detail", ("detail", Install.Log.Detail))])
            self._leafs = OrderedDict([
                ('si_log_output', (YLeafList(YType.str, 'si_log_output'), ['str'])),
            ])
            self.si_log_output = []

            self.reverse = Install.Log.Reverse()
            self.reverse.parent = self
            self._children_name_map["reverse"] = "reverse"

            self.detail = Install.Log.Detail()
            self.detail.parent = self
            self._children_name_map["detail"] = "detail"

            self.id = YList(self)
            self._segment_path = lambda: "log"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-instmgr-oper:install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Install.Log, ['si_log_output'], name, value)


        class Id(Entity):
            """
            
            
            .. attribute:: opid  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: detail
            
            	
            	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Log.Id.Detail>`
            
            .. attribute:: si_log_id_output
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install'
            _revision = '2017-10-13'

            def __init__(self):
                super(Install.Log.Id, self).__init__()

                self.yang_name = "id"
                self.yang_parent_name = "log"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['opid']
                self._child_classes = OrderedDict([("detail", ("detail", Install.Log.Id.Detail))])
                self._leafs = OrderedDict([
                    ('opid', (YLeaf(YType.uint32, 'opid'), ['int'])),
                    ('si_log_id_output', (YLeafList(YType.str, 'si_log_id_output'), ['str'])),
                ])
                self.opid = None
                self.si_log_id_output = []

                self.detail = Install.Log.Id.Detail()
                self.detail.parent = self
                self._children_name_map["detail"] = "detail"
                self._segment_path = lambda: "id" + "[opid='" + str(self.opid) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-instmgr-oper:install/log/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Install.Log.Id, ['opid', 'si_log_id_output'], name, value)


            class Detail(Entity):
                """
                
                
                .. attribute:: si_log_id_detail_output
                
                	
                	**type**\: list of str
                
                

                """

                _prefix = 'install'
                _revision = '2017-10-13'

                def __init__(self):
                    super(Install.Log.Id.Detail, self).__init__()

                    self.yang_name = "detail"
                    self.yang_parent_name = "id"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('si_log_id_detail_output', (YLeafList(YType.str, 'si_log_id_detail_output'), ['str'])),
                    ])
                    self.si_log_id_detail_output = []
                    self._segment_path = lambda: "detail"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.Log.Id.Detail, ['si_log_id_detail_output'], name, value)


        class Reverse(Entity):
            """
            
            
            .. attribute:: detail
            
            	
            	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Log.Reverse.Detail>`
            
            .. attribute:: si_log_reverse_output
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install'
            _revision = '2017-10-13'

            def __init__(self):
                super(Install.Log.Reverse, self).__init__()

                self.yang_name = "reverse"
                self.yang_parent_name = "log"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("detail", ("detail", Install.Log.Reverse.Detail))])
                self._leafs = OrderedDict([
                    ('si_log_reverse_output', (YLeafList(YType.str, 'si_log_reverse_output'), ['str'])),
                ])
                self.si_log_reverse_output = []

                self.detail = Install.Log.Reverse.Detail()
                self.detail.parent = self
                self._children_name_map["detail"] = "detail"
                self._segment_path = lambda: "reverse"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-instmgr-oper:install/log/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Install.Log.Reverse, ['si_log_reverse_output'], name, value)


            class Detail(Entity):
                """
                
                
                .. attribute:: si_log_reverse_detail_output
                
                	
                	**type**\: list of str
                
                

                """

                _prefix = 'install'
                _revision = '2017-10-13'

                def __init__(self):
                    super(Install.Log.Reverse.Detail, self).__init__()

                    self.yang_name = "detail"
                    self.yang_parent_name = "reverse"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('si_log_reverse_detail_output', (YLeafList(YType.str, 'si_log_reverse_detail_output'), ['str'])),
                    ])
                    self.si_log_reverse_detail_output = []
                    self._segment_path = lambda: "detail"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-instmgr-oper:install/log/reverse/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.Log.Reverse.Detail, ['si_log_reverse_detail_output'], name, value)


        class Detail(Entity):
            """
            
            
            .. attribute:: si_log_detail_output
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install'
            _revision = '2017-10-13'

            def __init__(self):
                super(Install.Log.Detail, self).__init__()

                self.yang_name = "detail"
                self.yang_parent_name = "log"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('si_log_detail_output', (YLeafList(YType.str, 'si_log_detail_output'), ['str'])),
                ])
                self.si_log_detail_output = []
                self._segment_path = lambda: "detail"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-instmgr-oper:install/log/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Install.Log.Detail, ['si_log_detail_output'], name, value)


    class Which(Entity):
        """
        Filename to get info for
        
        .. attribute:: file_list
        
        	
        	**type**\: list of  		 :py:class:`FileList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Which.FileList>`
        
        

        """

        _prefix = 'install'
        _revision = '2017-10-13'

        def __init__(self):
            super(Install.Which, self).__init__()

            self.yang_name = "which"
            self.yang_parent_name = "install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("file_list", ("file_list", Install.Which.FileList))])
            self._leafs = OrderedDict()

            self.file_list = YList(self)
            self._segment_path = lambda: "which"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-instmgr-oper:install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Install.Which, [], name, value)


        class FileList(Entity):
            """
            
            
            .. attribute:: file_name  (key)
            
            	
            	**type**\: str
            
            .. attribute:: detail
            
            	
            	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Which.FileList.Detail>`
            
            .. attribute:: si_which_output
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install'
            _revision = '2017-10-13'

            def __init__(self):
                super(Install.Which.FileList, self).__init__()

                self.yang_name = "file_list"
                self.yang_parent_name = "which"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['file_name']
                self._child_classes = OrderedDict([("detail", ("detail", Install.Which.FileList.Detail))])
                self._leafs = OrderedDict([
                    ('file_name', (YLeaf(YType.str, 'file_name'), ['str'])),
                    ('si_which_output', (YLeafList(YType.str, 'si_which_output'), ['str'])),
                ])
                self.file_name = None
                self.si_which_output = []

                self.detail = Install.Which.FileList.Detail()
                self.detail.parent = self
                self._children_name_map["detail"] = "detail"
                self._segment_path = lambda: "file_list" + "[file_name='" + str(self.file_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-instmgr-oper:install/which/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Install.Which.FileList, ['file_name', 'si_which_output'], name, value)


            class Detail(Entity):
                """
                
                
                .. attribute:: si_which_detail_output
                
                	
                	**type**\: list of str
                
                

                """

                _prefix = 'install'
                _revision = '2017-10-13'

                def __init__(self):
                    super(Install.Which.FileList.Detail, self).__init__()

                    self.yang_name = "detail"
                    self.yang_parent_name = "file_list"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('si_which_detail_output', (YLeafList(YType.str, 'si_which_detail_output'), ['str'])),
                    ])
                    self.si_which_detail_output = []
                    self._segment_path = lambda: "detail"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Install.Which.FileList.Detail, ['si_which_detail_output'], name, value)


    class Committed(Entity):
        """
        Calvados committed package(s) list for this node
        
        .. attribute:: summary
        
        	shows summary information of the committed install software
        	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_instmgr_oper.Install.Committed.Summary>`
        
        .. attribute:: si_committed_output
        
        	
        	**type**\: list of str
        
        

        """

        _prefix = 'install'
        _revision = '2017-10-13'

        def __init__(self):
            super(Install.Committed, self).__init__()

            self.yang_name = "committed"
            self.yang_parent_name = "install"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("summary", ("summary", Install.Committed.Summary))])
            self._leafs = OrderedDict([
                ('si_committed_output', (YLeafList(YType.str, 'si_committed_output'), ['str'])),
            ])
            self.si_committed_output = []

            self.summary = Install.Committed.Summary()
            self.summary.parent = self
            self._children_name_map["summary"] = "summary"
            self._segment_path = lambda: "committed"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-instmgr-oper:install/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Install.Committed, ['si_committed_output'], name, value)


        class Summary(Entity):
            """
            shows summary information of the committed install software
            
            .. attribute:: si_committed_summary_output
            
            	
            	**type**\: list of str
            
            

            """

            _prefix = 'install'
            _revision = '2017-10-13'

            def __init__(self):
                super(Install.Committed.Summary, self).__init__()

                self.yang_name = "summary"
                self.yang_parent_name = "committed"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('si_committed_summary_output', (YLeafList(YType.str, 'si_committed_summary_output'), ['str'])),
                ])
                self.si_committed_summary_output = []
                self._segment_path = lambda: "summary"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-instmgr-oper:install/committed/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Install.Committed.Summary, ['si_committed_summary_output'], name, value)

    def clone_ptr(self):
        self._top_entity = Install()
        return self._top_entity


""" tailf_aaa 

This module defines the Tail\-f AAA data model.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Action(Enum):
    """
    Action (Enum Class)

    .. data:: accept = 0

    .. data:: reject = 1

    .. data:: accept_log = 2

    """

    accept = Enum.YLeaf(0, "accept")

    reject = Enum.YLeaf(1, "reject")

    accept_log = Enum.YLeaf(2, "accept_log")


class Builtinmodes(Enum):
    """
    Builtinmodes (Enum Class)

    .. data:: exec_ = 0

    .. data:: configure = 1

    """

    exec_ = Enum.YLeaf(0, "exec")

    configure = Enum.YLeaf(1, "configure")


class Builtinmodes_(Enum):
    """
    Builtinmodes\_ (Enum Class)

    .. data:: exec_ = 0

    .. data:: configure = 1

    """

    exec_ = Enum.YLeaf(0, "exec")

    configure = Enum.YLeaf(1, "configure")


class Cmdoperationtype(Enum):
    """
    Cmdoperationtype (Enum Class)

    .. data:: r = 0

    .. data:: rx = 1

    .. data:: x = 2

    """

    r = Enum.YLeaf(0, "r")

    rx = Enum.YLeaf(1, "rx")

    x = Enum.YLeaf(2, "x")


class Dataoperationtype(Enum):
    """
    Dataoperationtype (Enum Class)

    .. data:: r = 0

    .. data:: rx = 1

    .. data:: x = 2

    .. data:: rw = 3

    .. data:: rwx = 4

    .. data:: wx = 5

    .. data:: w = 6

    .. data:: c = 7

    .. data:: cr = 8

    .. data:: cu = 9

    .. data:: cd = 10

    .. data:: cx = 11

    .. data:: cru = 12

    .. data:: crd = 13

    .. data:: crx = 14

    .. data:: cud = 15

    .. data:: cux = 16

    .. data:: cdx = 17

    .. data:: crud = 18

    .. data:: crux = 19

    .. data:: crdx = 20

    .. data:: cudx = 21

    .. data:: crudx = 22

    .. data:: ru = 23

    .. data:: rd = 24

    .. data:: rud = 25

    .. data:: rux = 26

    .. data:: rdx = 27

    .. data:: u = 28

    .. data:: ud = 29

    .. data:: ux = 30

    .. data:: d = 31

    .. data:: dx = 32

    """

    r = Enum.YLeaf(0, "r")

    rx = Enum.YLeaf(1, "rx")

    x = Enum.YLeaf(2, "x")

    rw = Enum.YLeaf(3, "rw")

    rwx = Enum.YLeaf(4, "rwx")

    wx = Enum.YLeaf(5, "wx")

    w = Enum.YLeaf(6, "w")

    c = Enum.YLeaf(7, "c")

    cr = Enum.YLeaf(8, "cr")

    cu = Enum.YLeaf(9, "cu")

    cd = Enum.YLeaf(10, "cd")

    cx = Enum.YLeaf(11, "cx")

    cru = Enum.YLeaf(12, "cru")

    crd = Enum.YLeaf(13, "crd")

    crx = Enum.YLeaf(14, "crx")

    cud = Enum.YLeaf(15, "cud")

    cux = Enum.YLeaf(16, "cux")

    cdx = Enum.YLeaf(17, "cdx")

    crud = Enum.YLeaf(18, "crud")

    crux = Enum.YLeaf(19, "crux")

    crdx = Enum.YLeaf(20, "crdx")

    cudx = Enum.YLeaf(21, "cudx")

    crudx = Enum.YLeaf(22, "crudx")

    ru = Enum.YLeaf(23, "ru")

    rd = Enum.YLeaf(24, "rd")

    rud = Enum.YLeaf(25, "rud")

    rux = Enum.YLeaf(26, "rux")

    rdx = Enum.YLeaf(27, "rdx")

    u = Enum.YLeaf(28, "u")

    ud = Enum.YLeaf(29, "ud")

    ux = Enum.YLeaf(30, "ux")

    d = Enum.YLeaf(31, "d")

    dx = Enum.YLeaf(32, "dx")



class Aaa(Entity):
    """
    
    
    .. attribute:: authentication
    
    	
    	**type**\:  :py:class:`Authentication <ydk.models.cisco_ios_xr.tailf_aaa.Aaa.Authentication>`
    
    .. attribute:: authorization
    
    	
    	**type**\:  :py:class:`Authorization <ydk.models.cisco_ios_xr.tailf_aaa.Aaa.Authorization>`
    
    .. attribute:: ios
    
    	
    	**type**\:  :py:class:`Ios <ydk.models.cisco_ios_xr.tailf_aaa.Aaa.Ios>`
    
    	**presence node**\: True
    
    .. attribute:: privileged_access
    
    	
    	**type**\:  :py:class:`PrivilegedAccess <ydk.models.cisco_ios_xr.tailf_aaa.Aaa.PrivilegedAccess>`
    
    .. attribute:: accounting
    
    	
    	**type**\:  :py:class:`Accounting <ydk.models.cisco_ios_xr.tailf_aaa.Aaa.Accounting>`
    
    .. attribute:: user_group
    
    	
    	**type**\:  :py:class:`UserGroup <ydk.models.cisco_ios_xr.tailf_aaa.Aaa.UserGroup>`
    
    .. attribute:: disaster_recovery
    
    	
    	**type**\:  :py:class:`DisasterRecovery <ydk.models.cisco_ios_xr.tailf_aaa.Aaa.DisasterRecovery>`
    
    

    """

    _prefix = 'aaa'
    _revision = '2011-09-22'

    def __init__(self):
        super(Aaa, self).__init__()
        self._top_entity = None

        self.yang_name = "aaa"
        self.yang_parent_name = "tailf-aaa"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("authentication", ("authentication", Aaa.Authentication)), ("authorization", ("authorization", Aaa.Authorization)), ("ios", ("ios", Aaa.Ios)), ("Cisco-IOS-XR-sysadmin-aaa-aaa-show:privileged-access", ("privileged_access", Aaa.PrivilegedAccess)), ("Cisco-IOS-XR-sysadmin-aaa-aaa-show:accounting", ("accounting", Aaa.Accounting)), ("Cisco-IOS-XR-sysadmin-aaa-aaa-show:user-group", ("user_group", Aaa.UserGroup)), ("Cisco-IOS-XR-sysadmin-aaa-disaster-recovery:disaster-recovery", ("disaster_recovery", Aaa.DisasterRecovery))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.authentication = Aaa.Authentication()
        self.authentication.parent = self
        self._children_name_map["authentication"] = "authentication"
        self._children_yang_names.add("authentication")

        self.authorization = Aaa.Authorization()
        self.authorization.parent = self
        self._children_name_map["authorization"] = "authorization"
        self._children_yang_names.add("authorization")

        self.ios = None
        self._children_name_map["ios"] = "ios"
        self._children_yang_names.add("ios")

        self.privileged_access = Aaa.PrivilegedAccess()
        self.privileged_access.parent = self
        self._children_name_map["privileged_access"] = "Cisco-IOS-XR-sysadmin-aaa-aaa-show:privileged-access"
        self._children_yang_names.add("Cisco-IOS-XR-sysadmin-aaa-aaa-show:privileged-access")

        self.accounting = Aaa.Accounting()
        self.accounting.parent = self
        self._children_name_map["accounting"] = "Cisco-IOS-XR-sysadmin-aaa-aaa-show:accounting"
        self._children_yang_names.add("Cisco-IOS-XR-sysadmin-aaa-aaa-show:accounting")

        self.user_group = Aaa.UserGroup()
        self.user_group.parent = self
        self._children_name_map["user_group"] = "Cisco-IOS-XR-sysadmin-aaa-aaa-show:user-group"
        self._children_yang_names.add("Cisco-IOS-XR-sysadmin-aaa-aaa-show:user-group")

        self.disaster_recovery = Aaa.DisasterRecovery()
        self.disaster_recovery.parent = self
        self._children_name_map["disaster_recovery"] = "Cisco-IOS-XR-sysadmin-aaa-disaster-recovery:disaster-recovery"
        self._children_yang_names.add("Cisco-IOS-XR-sysadmin-aaa-disaster-recovery:disaster-recovery")
        self._segment_path = lambda: "tailf-aaa:aaa"


    class Authentication(Entity):
        """
        
        
        .. attribute:: users
        
        	
        	**type**\:  :py:class:`Users <ydk.models.cisco_ios_xr.tailf_aaa.Aaa.Authentication.Users>`
        
        .. attribute:: groups
        
        	
        	**type**\:  :py:class:`Groups <ydk.models.cisco_ios_xr.tailf_aaa.Aaa.Authentication.Groups>`
        
        

        """

        _prefix = 'aaa'
        _revision = '2011-09-22'

        def __init__(self):
            super(Aaa.Authentication, self).__init__()

            self.yang_name = "authentication"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("users", ("users", Aaa.Authentication.Users)), ("groups", ("groups", Aaa.Authentication.Groups))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.users = Aaa.Authentication.Users()
            self.users.parent = self
            self._children_name_map["users"] = "users"
            self._children_yang_names.add("users")

            self.groups = Aaa.Authentication.Groups()
            self.groups.parent = self
            self._children_name_map["groups"] = "groups"
            self._children_yang_names.add("groups")
            self._segment_path = lambda: "authentication"
            self._absolute_path = lambda: "tailf-aaa:aaa/%s" % self._segment_path()


        class Users(Entity):
            """
            
            
            .. attribute:: user
            
            	
            	**type**\: list of  		 :py:class:`User <ydk.models.cisco_ios_xr.tailf_aaa.Aaa.Authentication.Users.User>`
            
            

            """

            _prefix = 'aaa'
            _revision = '2011-09-22'

            def __init__(self):
                super(Aaa.Authentication.Users, self).__init__()

                self.yang_name = "users"
                self.yang_parent_name = "authentication"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("user", ("user", Aaa.Authentication.Users.User))])
                self._leafs = OrderedDict()

                self.user = YList(self)
                self._segment_path = lambda: "users"
                self._absolute_path = lambda: "tailf-aaa:aaa/authentication/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Authentication.Users, [], name, value)


            class User(Entity):
                """
                
                
                .. attribute:: name  (key)
                
                	
                	**type**\: str
                
                .. attribute:: uid
                
                	
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                	**mandatory**\: True
                
                .. attribute:: gid
                
                	
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                	**mandatory**\: True
                
                .. attribute:: password
                
                	
                	**type**\: str
                
                	**mandatory**\: True
                
                .. attribute:: ssh_keydir
                
                	
                	**type**\: str
                
                	**mandatory**\: True
                
                .. attribute:: homedir
                
                	
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'aaa'
                _revision = '2011-09-22'

                def __init__(self):
                    super(Aaa.Authentication.Users.User, self).__init__()

                    self.yang_name = "user"
                    self.yang_parent_name = "users"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                        ('uid', YLeaf(YType.int32, 'uid')),
                        ('gid', YLeaf(YType.int32, 'gid')),
                        ('password', YLeaf(YType.str, 'password')),
                        ('ssh_keydir', YLeaf(YType.str, 'ssh_keydir')),
                        ('homedir', YLeaf(YType.str, 'homedir')),
                    ])
                    self.name = None
                    self.uid = None
                    self.gid = None
                    self.password = None
                    self.ssh_keydir = None
                    self.homedir = None
                    self._segment_path = lambda: "user" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "tailf-aaa:aaa/authentication/users/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Authentication.Users.User, ['name', 'uid', 'gid', 'password', 'ssh_keydir', 'homedir'], name, value)


        class Groups(Entity):
            """
            
            
            .. attribute:: group
            
            	
            	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.tailf_aaa.Aaa.Authentication.Groups.Group>`
            
            

            """

            _prefix = 'aaa'
            _revision = '2011-09-22'

            def __init__(self):
                super(Aaa.Authentication.Groups, self).__init__()

                self.yang_name = "groups"
                self.yang_parent_name = "authentication"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("group", ("group", Aaa.Authentication.Groups.Group))])
                self._leafs = OrderedDict()

                self.group = YList(self)
                self._segment_path = lambda: "groups"
                self._absolute_path = lambda: "tailf-aaa:aaa/authentication/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Authentication.Groups, [], name, value)


            class Group(Entity):
                """
                
                
                .. attribute:: name  (key)
                
                	
                	**type**\: str
                
                .. attribute:: gid
                
                	
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: users
                
                	
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'aaa'
                _revision = '2011-09-22'

                def __init__(self):
                    super(Aaa.Authentication.Groups.Group, self).__init__()

                    self.yang_name = "group"
                    self.yang_parent_name = "groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                        ('gid', YLeaf(YType.int32, 'gid')),
                        ('users', YLeaf(YType.str, 'users')),
                    ])
                    self.name = None
                    self.gid = None
                    self.users = None
                    self._segment_path = lambda: "group" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "tailf-aaa:aaa/authentication/groups/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Authentication.Groups.Group, ['name', 'gid', 'users'], name, value)


    class Authorization(Entity):
        """
        
        
        .. attribute:: cmdrules
        
        	
        	**type**\:  :py:class:`Cmdrules <ydk.models.cisco_ios_xr.tailf_aaa.Aaa.Authorization.Cmdrules>`
        
        .. attribute:: datarules
        
        	
        	**type**\:  :py:class:`Datarules <ydk.models.cisco_ios_xr.tailf_aaa.Aaa.Authorization.Datarules>`
        
        

        """

        _prefix = 'aaa'
        _revision = '2011-09-22'

        def __init__(self):
            super(Aaa.Authorization, self).__init__()

            self.yang_name = "authorization"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("cmdrules", ("cmdrules", Aaa.Authorization.Cmdrules)), ("datarules", ("datarules", Aaa.Authorization.Datarules))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.cmdrules = Aaa.Authorization.Cmdrules()
            self.cmdrules.parent = self
            self._children_name_map["cmdrules"] = "cmdrules"
            self._children_yang_names.add("cmdrules")

            self.datarules = Aaa.Authorization.Datarules()
            self.datarules.parent = self
            self._children_name_map["datarules"] = "datarules"
            self._children_yang_names.add("datarules")
            self._segment_path = lambda: "authorization"
            self._absolute_path = lambda: "tailf-aaa:aaa/%s" % self._segment_path()


        class Cmdrules(Entity):
            """
            
            
            .. attribute:: cmdrule
            
            	
            	**type**\: list of  		 :py:class:`Cmdrule <ydk.models.cisco_ios_xr.tailf_aaa.Aaa.Authorization.Cmdrules.Cmdrule>`
            
            

            """

            _prefix = 'aaa'
            _revision = '2011-09-22'

            def __init__(self):
                super(Aaa.Authorization.Cmdrules, self).__init__()

                self.yang_name = "cmdrules"
                self.yang_parent_name = "authorization"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("cmdrule", ("cmdrule", Aaa.Authorization.Cmdrules.Cmdrule))])
                self._leafs = OrderedDict()

                self.cmdrule = YList(self)
                self._segment_path = lambda: "cmdrules"
                self._absolute_path = lambda: "tailf-aaa:aaa/authorization/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Authorization.Cmdrules, [], name, value)


            class Cmdrule(Entity):
                """
                
                
                .. attribute:: index  (key)
                
                	
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: context
                
                	
                	**type**\: str
                
                	**mandatory**\: True
                
                .. attribute:: command
                
                	
                	**type**\: str
                
                	**mandatory**\: True
                
                .. attribute:: group
                
                	
                	**type**\: str
                
                	**mandatory**\: True
                
                .. attribute:: ops
                
                	
                	**type**\:  :py:class:`Cmdoperationtype <ydk.models.cisco_ios_xr.tailf_aaa.Cmdoperationtype>`
                
                	**mandatory**\: True
                
                .. attribute:: action
                
                	
                	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.tailf_aaa.Action>`
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'aaa'
                _revision = '2011-09-22'

                def __init__(self):
                    super(Aaa.Authorization.Cmdrules.Cmdrule, self).__init__()

                    self.yang_name = "cmdrule"
                    self.yang_parent_name = "cmdrules"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['index']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('index', YLeaf(YType.uint32, 'index')),
                        ('context', YLeaf(YType.str, 'context')),
                        ('command', YLeaf(YType.str, 'command')),
                        ('group', YLeaf(YType.str, 'group')),
                        ('ops', YLeaf(YType.enumeration, 'ops')),
                        ('action', YLeaf(YType.enumeration, 'action')),
                    ])
                    self.index = None
                    self.context = None
                    self.command = None
                    self.group = None
                    self.ops = None
                    self.action = None
                    self._segment_path = lambda: "cmdrule" + "[index='" + str(self.index) + "']"
                    self._absolute_path = lambda: "tailf-aaa:aaa/authorization/cmdrules/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Authorization.Cmdrules.Cmdrule, ['index', 'context', 'command', 'group', 'ops', 'action'], name, value)


        class Datarules(Entity):
            """
            
            
            .. attribute:: datarule
            
            	
            	**type**\: list of  		 :py:class:`Datarule <ydk.models.cisco_ios_xr.tailf_aaa.Aaa.Authorization.Datarules.Datarule>`
            
            

            """

            _prefix = 'aaa'
            _revision = '2011-09-22'

            def __init__(self):
                super(Aaa.Authorization.Datarules, self).__init__()

                self.yang_name = "datarules"
                self.yang_parent_name = "authorization"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("datarule", ("datarule", Aaa.Authorization.Datarules.Datarule))])
                self._leafs = OrderedDict()

                self.datarule = YList(self)
                self._segment_path = lambda: "datarules"
                self._absolute_path = lambda: "tailf-aaa:aaa/authorization/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Authorization.Datarules, [], name, value)


            class Datarule(Entity):
                """
                
                
                .. attribute:: index  (key)
                
                	
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: namespace
                
                	
                	**type**\: str
                
                	**mandatory**\: True
                
                .. attribute:: context
                
                	
                	**type**\: str
                
                	**default value**\: *
                
                .. attribute:: keypath
                
                	
                	**type**\: str
                
                	**mandatory**\: True
                
                .. attribute:: group
                
                	
                	**type**\: str
                
                	**mandatory**\: True
                
                .. attribute:: ops
                
                	
                	**type**\:  :py:class:`Dataoperationtype <ydk.models.cisco_ios_xr.tailf_aaa.Dataoperationtype>`
                
                	**mandatory**\: True
                
                .. attribute:: action
                
                	
                	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.tailf_aaa.Action>`
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'aaa'
                _revision = '2011-09-22'

                def __init__(self):
                    super(Aaa.Authorization.Datarules.Datarule, self).__init__()

                    self.yang_name = "datarule"
                    self.yang_parent_name = "datarules"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['index']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('index', YLeaf(YType.uint32, 'index')),
                        ('namespace', YLeaf(YType.str, 'namespace')),
                        ('context', YLeaf(YType.str, 'context')),
                        ('keypath', YLeaf(YType.str, 'keypath')),
                        ('group', YLeaf(YType.str, 'group')),
                        ('ops', YLeaf(YType.enumeration, 'ops')),
                        ('action', YLeaf(YType.enumeration, 'action')),
                    ])
                    self.index = None
                    self.namespace = None
                    self.context = None
                    self.keypath = None
                    self.group = None
                    self.ops = None
                    self.action = None
                    self._segment_path = lambda: "datarule" + "[index='" + str(self.index) + "']"
                    self._absolute_path = lambda: "tailf-aaa:aaa/authorization/datarules/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Authorization.Datarules.Datarule, ['index', 'namespace', 'context', 'keypath', 'group', 'ops', 'action'], name, value)


    class Ios(Entity):
        """
        
        
        .. attribute:: level
        
        	
        	**type**\: list of  		 :py:class:`Level <ydk.models.cisco_ios_xr.tailf_aaa.Aaa.Ios.Level>`
        
        .. attribute:: privilege
        
        	
        	**type**\: list of  		 :py:class:`Privilege <ydk.models.cisco_ios_xr.tailf_aaa.Aaa.Ios.Privilege>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'aaa'
        _revision = '2011-09-22'

        def __init__(self):
            super(Aaa.Ios, self).__init__()

            self.yang_name = "ios"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("level", ("level", Aaa.Ios.Level)), ("privilege", ("privilege", Aaa.Ios.Privilege))])
            self.is_presence_container = True
            self._leafs = OrderedDict()

            self.level = YList(self)
            self.privilege = YList(self)
            self._segment_path = lambda: "ios"
            self._absolute_path = lambda: "tailf-aaa:aaa/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.Ios, [], name, value)


        class Level(Entity):
            """
            
            
            .. attribute:: nr  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..15
            
            .. attribute:: secret
            
            	
            	**type**\: str
            
            .. attribute:: password
            
            	
            	**type**\: str
            
            .. attribute:: prompt
            
            	
            	**type**\: str
            
            	**default value**\: \h# 
            
            

            """

            _prefix = 'aaa'
            _revision = '2011-09-22'

            def __init__(self):
                super(Aaa.Ios.Level, self).__init__()

                self.yang_name = "level"
                self.yang_parent_name = "ios"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['nr']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('nr', YLeaf(YType.int32, 'nr')),
                    ('secret', YLeaf(YType.str, 'secret')),
                    ('password', YLeaf(YType.str, 'password')),
                    ('prompt', YLeaf(YType.str, 'prompt')),
                ])
                self.nr = None
                self.secret = None
                self.password = None
                self.prompt = None
                self._segment_path = lambda: "level" + "[nr='" + str(self.nr) + "']"
                self._absolute_path = lambda: "tailf-aaa:aaa/ios/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Ios.Level, ['nr', 'secret', 'password', 'prompt'], name, value)


        class Privilege(Entity):
            """
            
            
            .. attribute:: mode  (key)
            
            	
            	**type**\: union of the below types:
            
            		**type**\: str
            
            		**type**\:  :py:class:`Builtinmodes_ <ydk.models.cisco_ios_xr.tailf_aaa.Builtinmodes_>`
            
            .. attribute:: level
            
            	
            	**type**\: list of  		 :py:class:`Level <ydk.models.cisco_ios_xr.tailf_aaa.Aaa.Ios.Privilege.Level>`
            
            

            """

            _prefix = 'aaa'
            _revision = '2011-09-22'

            def __init__(self):
                super(Aaa.Ios.Privilege, self).__init__()

                self.yang_name = "privilege"
                self.yang_parent_name = "ios"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mode']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("level", ("level", Aaa.Ios.Privilege.Level))])
                self._leafs = OrderedDict([
                    ('mode', YLeaf(YType.str, 'mode')),
                ])
                self.mode = None

                self.level = YList(self)
                self._segment_path = lambda: "privilege" + "[mode='" + str(self.mode) + "']"
                self._absolute_path = lambda: "tailf-aaa:aaa/ios/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Ios.Privilege, ['mode'], name, value)


            class Level(Entity):
                """
                
                
                .. attribute:: nr  (key)
                
                	
                	**type**\: int
                
                	**range:** 0..15
                
                .. attribute:: command
                
                	
                	**type**\: list of  		 :py:class:`Command <ydk.models.cisco_ios_xr.tailf_aaa.Aaa.Ios.Privilege.Level.Command>`
                
                

                """

                _prefix = 'aaa'
                _revision = '2011-09-22'

                def __init__(self):
                    super(Aaa.Ios.Privilege.Level, self).__init__()

                    self.yang_name = "level"
                    self.yang_parent_name = "privilege"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['nr']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("command", ("command", Aaa.Ios.Privilege.Level.Command))])
                    self._leafs = OrderedDict([
                        ('nr', YLeaf(YType.int32, 'nr')),
                    ])
                    self.nr = None

                    self.command = YList(self)
                    self._segment_path = lambda: "level" + "[nr='" + str(self.nr) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Ios.Privilege.Level, ['nr'], name, value)


                class Command(Entity):
                    """
                    
                    
                    .. attribute:: name  (key)
                    
                    	
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'aaa'
                    _revision = '2011-09-22'

                    def __init__(self):
                        super(Aaa.Ios.Privilege.Level.Command, self).__init__()

                        self.yang_name = "command"
                        self.yang_parent_name = "level"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', YLeaf(YType.str, 'name')),
                        ])
                        self.name = None
                        self._segment_path = lambda: "command" + "[name='" + str(self.name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Ios.Privilege.Level.Command, ['name'], name, value)


    class PrivilegedAccess(Entity):
        """
        
        
        .. attribute:: shell_access
        
        	
        	**type**\: str
        
        .. attribute:: first_user
        
        	
        	**type**\: str
        
        .. attribute:: first_user_change
        
        	
        	**type**\: str
        
        .. attribute:: current_disaster_recovery_user
        
        	
        	**type**\: str
        
        

        """

        _prefix = 'aaa_show'
        _revision = '2017-05-10'

        def __init__(self):
            super(Aaa.PrivilegedAccess, self).__init__()

            self.yang_name = "privileged-access"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('shell_access', YLeaf(YType.str, 'shell-access')),
                ('first_user', YLeaf(YType.str, 'first-user')),
                ('first_user_change', YLeaf(YType.str, 'first-user-change')),
                ('current_disaster_recovery_user', YLeaf(YType.str, 'current-disaster-recovery-user')),
            ])
            self.shell_access = None
            self.first_user = None
            self.first_user_change = None
            self.current_disaster_recovery_user = None
            self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-aaa-aaa-show:privileged-access"
            self._absolute_path = lambda: "tailf-aaa:aaa/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.PrivilegedAccess, ['shell_access', 'first_user', 'first_user_change', 'current_disaster_recovery_user'], name, value)


    class Accounting(Entity):
        """
        
        
        .. attribute:: log_data
        
        	
        	**type**\: str
        
        

        """

        _prefix = 'aaa_show'
        _revision = '2017-05-10'

        def __init__(self):
            super(Aaa.Accounting, self).__init__()

            self.yang_name = "accounting"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('log_data', YLeaf(YType.str, 'log-data')),
            ])
            self.log_data = None
            self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-aaa-aaa-show:accounting"
            self._absolute_path = lambda: "tailf-aaa:aaa/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.Accounting, ['log_data'], name, value)


    class UserGroup(Entity):
        """
        
        
        .. attribute:: grp_data
        
        	
        	**type**\: str
        
        

        """

        _prefix = 'aaa_show'
        _revision = '2017-05-10'

        def __init__(self):
            super(Aaa.UserGroup, self).__init__()

            self.yang_name = "user-group"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('grp_data', YLeaf(YType.str, 'grp-data')),
            ])
            self.grp_data = None
            self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-aaa-aaa-show:user-group"
            self._absolute_path = lambda: "tailf-aaa:aaa/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.UserGroup, ['grp_data'], name, value)


    class DisasterRecovery(Entity):
        """
        
        
        .. attribute:: username
        
        	
        	**type**\: str
        
        	**refers to**\:  :py:class:`name <ydk.models.cisco_ios_xr.tailf_aaa.Aaa.Authentication.Users.User>`
        
        .. attribute:: password
        
        	
        	**type**\: str
        
        

        """

        _prefix = 'disaster-recovery'
        _revision = '2017-05-10'

        def __init__(self):
            super(Aaa.DisasterRecovery, self).__init__()

            self.yang_name = "disaster-recovery"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('username', YLeaf(YType.str, 'username')),
                ('password', YLeaf(YType.str, 'password')),
            ])
            self.username = None
            self.password = None
            self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-aaa-disaster-recovery:disaster-recovery"
            self._absolute_path = lambda: "tailf-aaa:aaa/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.DisasterRecovery, ['username', 'password'], name, value)

    def clone_ptr(self):
        self._top_entity = Aaa()
        return self._top_entity

class Alias(Entity):
    """
    
    
    .. attribute:: name  (key)
    
    	
    	**type**\: str
    
    .. attribute:: expansion
    
    	
    	**type**\: str
    
    	**mandatory**\: True
    
    

    """

    _prefix = 'aaa'
    _revision = '2011-09-22'

    def __init__(self):
        super(Alias, self).__init__()
        self._top_entity = None

        self.yang_name = "alias"
        self.yang_parent_name = "tailf-aaa"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = ['name']
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('name', YLeaf(YType.str, 'name')),
            ('expansion', YLeaf(YType.str, 'expansion')),
        ])
        self.name = None
        self.expansion = None
        self._segment_path = lambda: "tailf-aaa:alias" + "[name='" + str(self.name) + "']"

    def __setattr__(self, name, value):
        self._perform_setattr(Alias, ['name', 'expansion'], name, value)

    def clone_ptr(self):
        self._top_entity = Alias()
        return self._top_entity

class Session(Entity):
    """
    
    
    .. attribute:: complete_on_space
    
    	
    	**type**\: bool
    
    .. attribute:: ignore_leading_space
    
    	
    	**type**\: bool
    
    .. attribute:: idle_timeout
    
    	
    	**type**\: int
    
    	**range:** 0..8192
    
    .. attribute:: paginate
    
    	
    	**type**\: bool
    
    .. attribute:: history
    
    	
    	**type**\: int
    
    	**range:** 0..8192
    
    .. attribute:: autowizard
    
    	
    	**type**\: bool
    
    .. attribute:: show_defaults
    
    	
    	**type**\: bool
    
    .. attribute:: display_level
    
    	
    	**type**\: int
    
    	**range:** 1..64
    
    .. attribute:: prompt1
    
    	
    	**type**\: str
    
    .. attribute:: prompt2
    
    	
    	**type**\: str
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'aaa'
    _revision = '2011-09-22'

    def __init__(self):
        super(Session, self).__init__()
        self._top_entity = None

        self.yang_name = "session"
        self.yang_parent_name = "tailf-aaa"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self.is_presence_container = True
        self._leafs = OrderedDict([
            ('complete_on_space', YLeaf(YType.boolean, 'complete-on-space')),
            ('ignore_leading_space', YLeaf(YType.boolean, 'ignore-leading-space')),
            ('idle_timeout', YLeaf(YType.uint64, 'idle-timeout')),
            ('paginate', YLeaf(YType.boolean, 'paginate')),
            ('history', YLeaf(YType.uint64, 'history')),
            ('autowizard', YLeaf(YType.boolean, 'autowizard')),
            ('show_defaults', YLeaf(YType.boolean, 'show-defaults')),
            ('display_level', YLeaf(YType.uint64, 'display-level')),
            ('prompt1', YLeaf(YType.str, 'prompt1')),
            ('prompt2', YLeaf(YType.str, 'prompt2')),
        ])
        self.complete_on_space = None
        self.ignore_leading_space = None
        self.idle_timeout = None
        self.paginate = None
        self.history = None
        self.autowizard = None
        self.show_defaults = None
        self.display_level = None
        self.prompt1 = None
        self.prompt2 = None
        self._segment_path = lambda: "tailf-aaa:session"

    def __setattr__(self, name, value):
        self._perform_setattr(Session, ['complete_on_space', 'ignore_leading_space', 'idle_timeout', 'paginate', 'history', 'autowizard', 'show_defaults', 'display_level', 'prompt1', 'prompt2'], name, value)

    def clone_ptr(self):
        self._top_entity = Session()
        return self._top_entity

class User(Entity):
    """
    
    
    .. attribute:: name  (key)
    
    	
    	**type**\: str
    
    .. attribute:: description
    
    	
    	**type**\: str
    
    .. attribute:: alias
    
    	
    	**type**\: list of  		 :py:class:`Alias <ydk.models.cisco_ios_xr.tailf_aaa.User.Alias>`
    
    .. attribute:: session
    
    	
    	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.tailf_aaa.User.Session>`
    
    

    """

    _prefix = 'aaa'
    _revision = '2011-09-22'

    def __init__(self):
        super(User, self).__init__()
        self._top_entity = None

        self.yang_name = "user"
        self.yang_parent_name = "tailf-aaa"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = ['name']
        self._child_container_classes = OrderedDict([("session", ("session", User.Session))])
        self._child_list_classes = OrderedDict([("alias", ("alias", User.Alias))])
        self._leafs = OrderedDict([
            ('name', YLeaf(YType.str, 'name')),
            ('description', YLeaf(YType.str, 'description')),
        ])
        self.name = None
        self.description = None

        self.session = User.Session()
        self.session.parent = self
        self._children_name_map["session"] = "session"
        self._children_yang_names.add("session")

        self.alias = YList(self)
        self._segment_path = lambda: "tailf-aaa:user" + "[name='" + str(self.name) + "']"

    def __setattr__(self, name, value):
        self._perform_setattr(User, ['name', 'description'], name, value)


    class Alias(Entity):
        """
        
        
        .. attribute:: name  (key)
        
        	
        	**type**\: str
        
        .. attribute:: expansion
        
        	
        	**type**\: str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'aaa'
        _revision = '2011-09-22'

        def __init__(self):
            super(User.Alias, self).__init__()

            self.yang_name = "alias"
            self.yang_parent_name = "user"
            self.is_top_level_class = False
            self.has_list_ancestor = True
            self.ylist_key_names = ['name']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('name', YLeaf(YType.str, 'name')),
                ('expansion', YLeaf(YType.str, 'expansion')),
            ])
            self.name = None
            self.expansion = None
            self._segment_path = lambda: "alias" + "[name='" + str(self.name) + "']"

        def __setattr__(self, name, value):
            self._perform_setattr(User.Alias, ['name', 'expansion'], name, value)


    class Session(Entity):
        """
        
        
        .. attribute:: complete_on_space
        
        	
        	**type**\: bool
        
        .. attribute:: ignore_leading_space
        
        	
        	**type**\: bool
        
        .. attribute:: idle_timeout
        
        	
        	**type**\: int
        
        	**range:** 0..8192
        
        .. attribute:: paginate
        
        	
        	**type**\: bool
        
        .. attribute:: history
        
        	
        	**type**\: int
        
        	**range:** 0..8192
        
        .. attribute:: autowizard
        
        	
        	**type**\: bool
        
        .. attribute:: show_defaults
        
        	
        	**type**\: bool
        
        .. attribute:: display_level
        
        	
        	**type**\: int
        
        	**range:** 1..64
        
        .. attribute:: prompt1
        
        	
        	**type**\: str
        
        .. attribute:: prompt2
        
        	
        	**type**\: str
        
        

        """

        _prefix = 'aaa'
        _revision = '2011-09-22'

        def __init__(self):
            super(User.Session, self).__init__()

            self.yang_name = "session"
            self.yang_parent_name = "user"
            self.is_top_level_class = False
            self.has_list_ancestor = True
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('complete_on_space', YLeaf(YType.boolean, 'complete-on-space')),
                ('ignore_leading_space', YLeaf(YType.boolean, 'ignore-leading-space')),
                ('idle_timeout', YLeaf(YType.uint64, 'idle-timeout')),
                ('paginate', YLeaf(YType.boolean, 'paginate')),
                ('history', YLeaf(YType.uint64, 'history')),
                ('autowizard', YLeaf(YType.boolean, 'autowizard')),
                ('show_defaults', YLeaf(YType.boolean, 'show-defaults')),
                ('display_level', YLeaf(YType.uint64, 'display-level')),
                ('prompt1', YLeaf(YType.str, 'prompt1')),
                ('prompt2', YLeaf(YType.str, 'prompt2')),
            ])
            self.complete_on_space = None
            self.ignore_leading_space = None
            self.idle_timeout = None
            self.paginate = None
            self.history = None
            self.autowizard = None
            self.show_defaults = None
            self.display_level = None
            self.prompt1 = None
            self.prompt2 = None
            self._segment_path = lambda: "session"

        def __setattr__(self, name, value):
            self._perform_setattr(User.Session, ['complete_on_space', 'ignore_leading_space', 'idle_timeout', 'paginate', 'history', 'autowizard', 'show_defaults', 'display_level', 'prompt1', 'prompt2'], name, value)

    def clone_ptr(self):
        self._top_entity = User()
        return self._top_entity


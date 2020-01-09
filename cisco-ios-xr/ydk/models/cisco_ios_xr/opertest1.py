""" opertest1 

This module contains definitions
for the Calvados model objects.

This module holds a sample operational data store.

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




class Oper(_Entity_):
    """
    
    
    .. attribute:: fred
    
    	
    	**type**\: int
    
    	**range:** 0..9
    
    	**config**\: False
    
    .. attribute:: barney
    
    	
    	**type**\: int
    
    	**range:** 0..9999
    
    	**config**\: False
    
    .. attribute:: wilma
    
    	
    	**type**\: int
    
    	**range:** 0..9999
    
    	**config**\: False
    
    .. attribute:: betty
    
    	
    	**type**\: int
    
    	**range:** 0..9999
    
    	**config**\: False
    
    .. attribute:: slates
    
    	
    	**type**\: list of  		 :py:class:`Slates <ydk.models.cisco_ios_xr.opertest1.Oper.Slates>`
    
    	**config**\: False
    
    .. attribute:: uname
    
    	
    	**type**\:  :py:class:`Uname <ydk.models.cisco_ios_xr.opertest1.Oper.Uname>`
    
    	**config**\: False
    
    .. attribute:: uptime
    
    	
    	**type**\:  :py:class:`Uptime <ydk.models.cisco_ios_xr.opertest1.Oper.Uptime>`
    
    	**config**\: False
    
    .. attribute:: w
    
    	
    	**type**\:  :py:class:`W <ydk.models.cisco_ios_xr.opertest1.Oper.W>`
    
    	**config**\: False
    
    

    """

    _prefix = 'opertest1'
    _revision = '2016-10-12'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Oper, self).__init__()
        self._top_entity = None

        self.yang_name = "oper"
        self.yang_parent_name = "opertest1"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("slates", ("slates", Oper.Slates)), ("uname", ("uname", Oper.Uname)), ("uptime", ("uptime", Oper.Uptime)), ("w", ("w", Oper.W))])
        self._leafs = OrderedDict([
            ('fred', (YLeaf(YType.int32, 'fred'), ['int'])),
            ('barney', (YLeaf(YType.int32, 'barney'), ['int'])),
            ('wilma', (YLeaf(YType.int32, 'wilma'), ['int'])),
            ('betty', (YLeaf(YType.int32, 'betty'), ['int'])),
        ])
        self.fred = None
        self.barney = None
        self.wilma = None
        self.betty = None

        self.uname = Oper.Uname()
        self.uname.parent = self
        self._children_name_map["uname"] = "uname"

        self.uptime = Oper.Uptime()
        self.uptime.parent = self
        self._children_name_map["uptime"] = "uptime"

        self.w = Oper.W()
        self.w.parent = self
        self._children_name_map["w"] = "w"

        self.slates = YList(self)
        self._segment_path = lambda: "opertest1:oper"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Oper, ['fred', 'barney', 'wilma', 'betty'], name, value)


    class Slates(_Entity_):
        """
        
        
        .. attribute:: slatenum  (key)
        
        	
        	**type**\: int
        
        	**range:** 0..999
        
        	**config**\: False
        
        .. attribute:: mrslate
        
        	
        	**type**\: int
        
        	**range:** 0..99999999
        
        	**config**\: False
        
        

        """

        _prefix = 'opertest1'
        _revision = '2016-10-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Oper.Slates, self).__init__()

            self.yang_name = "slates"
            self.yang_parent_name = "oper"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['slatenum']
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('slatenum', (YLeaf(YType.int32, 'slatenum'), ['int'])),
                ('mrslate', (YLeaf(YType.int32, 'mrslate'), ['int'])),
            ])
            self.slatenum = None
            self.mrslate = None
            self._segment_path = lambda: "slates" + "[slatenum='" + str(self.slatenum) + "']"
            self._absolute_path = lambda: "opertest1:oper/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Oper.Slates, ['slatenum', 'mrslate'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _opertest1 as meta
            return meta._meta_table['Oper.Slates']['meta_info']


    class Uname(_Entity_):
        """
        
        
        .. attribute:: system
        
        	The operating system name
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: nodename
        
        	The hostname or nodename
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: release
        
        	The release level of the operating system implementation
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: version
        
        	The operating system implmentation version level
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: machine
        
        	The name of the hardware type the system is running on
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: all
        
        	All the fields
        	**type**\: str
        
        	**config**\: False
        
        

        """

        _prefix = 'opertest1'
        _revision = '2016-10-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Oper.Uname, self).__init__()

            self.yang_name = "uname"
            self.yang_parent_name = "oper"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('system', (YLeaf(YType.str, 'system'), ['str'])),
                ('nodename', (YLeaf(YType.str, 'nodename'), ['str'])),
                ('release', (YLeaf(YType.str, 'release'), ['str'])),
                ('version', (YLeaf(YType.str, 'version'), ['str'])),
                ('machine', (YLeaf(YType.str, 'machine'), ['str'])),
                ('all', (YLeaf(YType.str, 'all'), ['str'])),
            ])
            self.system = None
            self.nodename = None
            self.release = None
            self.version = None
            self.machine = None
            self.all = None
            self._segment_path = lambda: "uname"
            self._absolute_path = lambda: "opertest1:oper/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Oper.Uname, ['system', 'nodename', 'release', 'version', 'machine', 'all'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _opertest1 as meta
            return meta._meta_table['Oper.Uname']['meta_info']


    class Uptime(_Entity_):
        """
        
        
        .. attribute:: curtime
        
        	Current time
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: uptime
        
        	Time since boot
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: loadavg1min
        
        	Weighted Exponential One\-Minute Load Average
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: loadavg5min
        
        	Weighted Exponential Five\-Minute Load Average
        	**type**\: str
        
        	**config**\: False
        
        .. attribute:: loadavg15min
        
        	Weighted Exponential Fifteen\-Minute Load Average
        	**type**\: str
        
        	**config**\: False
        
        

        """

        _prefix = 'opertest1'
        _revision = '2016-10-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Oper.Uptime, self).__init__()

            self.yang_name = "uptime"
            self.yang_parent_name = "oper"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('curtime', (YLeaf(YType.str, 'curtime'), ['str'])),
                ('uptime', (YLeaf(YType.str, 'uptime'), ['str'])),
                ('loadavg1min', (YLeaf(YType.str, 'loadavg1min'), ['str'])),
                ('loadavg5min', (YLeaf(YType.str, 'loadavg5min'), ['str'])),
                ('loadavg15min', (YLeaf(YType.str, 'loadavg15min'), ['str'])),
            ])
            self.curtime = None
            self.uptime = None
            self.loadavg1min = None
            self.loadavg5min = None
            self.loadavg15min = None
            self._segment_path = lambda: "uptime"
            self._absolute_path = lambda: "opertest1:oper/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Oper.Uptime, ['curtime', 'uptime', 'loadavg1min', 'loadavg5min', 'loadavg15min'], name, value)

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _opertest1 as meta
            return meta._meta_table['Oper.Uptime']['meta_info']


    class W(_Entity_):
        """
        
        
        .. attribute:: header_info
        
        	
        	**type**\:  :py:class:`HeaderInfo <ydk.models.cisco_ios_xr.opertest1.Oper.W.HeaderInfo>`
        
        	**config**\: False
        
        .. attribute:: users
        
        	
        	**type**\:  :py:class:`Users <ydk.models.cisco_ios_xr.opertest1.Oper.W.Users>`
        
        	**config**\: False
        
        

        """

        _prefix = 'opertest1'
        _revision = '2016-10-12'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Oper.W, self).__init__()

            self.yang_name = "w"
            self.yang_parent_name = "oper"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("header-info", ("header_info", Oper.W.HeaderInfo)), ("users", ("users", Oper.W.Users))])
            self._leafs = OrderedDict()

            self.header_info = Oper.W.HeaderInfo()
            self.header_info.parent = self
            self._children_name_map["header_info"] = "header-info"

            self.users = Oper.W.Users()
            self.users.parent = self
            self._children_name_map["users"] = "users"
            self._segment_path = lambda: "w"
            self._absolute_path = lambda: "opertest1:oper/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Oper.W, [], name, value)


        class HeaderInfo(_Entity_):
            """
            
            
            .. attribute:: curtime
            
            	Current time
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: uptime
            
            	Time since boot
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: loadavg1min
            
            	Weighted Exponential One\-Minute Load Average
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: loadavg5min
            
            	Weighted Exponential Five\-Minute Load Average
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: loadavg15min
            
            	Weighted Exponential Fifteen\-Minute Load Average
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'opertest1'
            _revision = '2016-10-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Oper.W.HeaderInfo, self).__init__()

                self.yang_name = "header-info"
                self.yang_parent_name = "w"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('curtime', (YLeaf(YType.str, 'curtime'), ['str'])),
                    ('uptime', (YLeaf(YType.str, 'uptime'), ['str'])),
                    ('loadavg1min', (YLeaf(YType.str, 'loadavg1min'), ['str'])),
                    ('loadavg5min', (YLeaf(YType.str, 'loadavg5min'), ['str'])),
                    ('loadavg15min', (YLeaf(YType.str, 'loadavg15min'), ['str'])),
                ])
                self.curtime = None
                self.uptime = None
                self.loadavg1min = None
                self.loadavg5min = None
                self.loadavg15min = None
                self._segment_path = lambda: "header-info"
                self._absolute_path = lambda: "opertest1:oper/w/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Oper.W.HeaderInfo, ['curtime', 'uptime', 'loadavg1min', 'loadavg5min', 'loadavg15min'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _opertest1 as meta
                return meta._meta_table['Oper.W.HeaderInfo']['meta_info']


        class Users(_Entity_):
            """
            
            
            .. attribute:: user
            
            	
            	**type**\: list of  		 :py:class:`User <ydk.models.cisco_ios_xr.opertest1.Oper.W.Users.User>`
            
            	**config**\: False
            
            

            """

            _prefix = 'opertest1'
            _revision = '2016-10-12'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Oper.W.Users, self).__init__()

                self.yang_name = "users"
                self.yang_parent_name = "w"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("user", ("user", Oper.W.Users.User))])
                self._leafs = OrderedDict()

                self.user = YList(self)
                self._segment_path = lambda: "users"
                self._absolute_path = lambda: "opertest1:oper/w/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Oper.W.Users, [], name, value)


            class User(_Entity_):
                """
                
                
                .. attribute:: tty  (key)
                
                	
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: user
                
                	
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: from_
                
                	
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: login_at
                
                	
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: idle
                
                	
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: jcpu
                
                	
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: pcpu
                
                	
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: what
                
                	
                	**type**\: str
                
                	**config**\: False
                
                

                """

                _prefix = 'opertest1'
                _revision = '2016-10-12'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Oper.W.Users.User, self).__init__()

                    self.yang_name = "user"
                    self.yang_parent_name = "users"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['tty']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('tty', (YLeaf(YType.str, 'tty'), ['str'])),
                        ('user', (YLeaf(YType.str, 'user'), ['str'])),
                        ('from_', (YLeaf(YType.str, 'from'), ['str'])),
                        ('login_at', (YLeaf(YType.str, 'login-at'), ['str'])),
                        ('idle', (YLeaf(YType.str, 'idle'), ['str'])),
                        ('jcpu', (YLeaf(YType.str, 'jcpu'), ['str'])),
                        ('pcpu', (YLeaf(YType.str, 'pcpu'), ['str'])),
                        ('what', (YLeaf(YType.str, 'what'), ['str'])),
                    ])
                    self.tty = None
                    self.user = None
                    self.from_ = None
                    self.login_at = None
                    self.idle = None
                    self.jcpu = None
                    self.pcpu = None
                    self.what = None
                    self._segment_path = lambda: "user" + "[tty='" + str(self.tty) + "']"
                    self._absolute_path = lambda: "opertest1:oper/w/users/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Oper.W.Users.User, ['tty', 'user', 'from_', 'login_at', 'idle', 'jcpu', 'pcpu', 'what'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _opertest1 as meta
                    return meta._meta_table['Oper.W.Users.User']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _opertest1 as meta
                return meta._meta_table['Oper.W.Users']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _opertest1 as meta
            return meta._meta_table['Oper.W']['meta_info']

    def clone_ptr(self):
        self._top_entity = Oper()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _opertest1 as meta
        return meta._meta_table['Oper']['meta_info']


class Actions(_Entity_):
    """
    
    
    

    """

    _prefix = 'opertest1'
    _revision = '2016-10-12'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Actions, self).__init__()
        self._top_entity = None

        self.yang_name = "actions"
        self.yang_parent_name = "opertest1"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "opertest1:actions"
        self._is_frozen = True

    def clone_ptr(self):
        self._top_entity = Actions()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _opertest1 as meta
        return meta._meta_table['Actions']['meta_info']



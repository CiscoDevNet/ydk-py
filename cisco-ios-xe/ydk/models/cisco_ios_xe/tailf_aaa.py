""" tailf_aaa 

This module defines the Tail\-f AAA data model.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class BuiltinmodesEnum(Enum):
    """
    BuiltinmodesEnum

    .. data:: exec_ = 0

    .. data:: configure = 1

    """

    exec_ = 0

    configure = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _tailf_aaa as meta
        return meta._meta_table['BuiltinmodesEnum']


class BuiltinmodesEnum(Enum):
    """
    BuiltinmodesEnum

    .. data:: exec_ = 0

    .. data:: configure = 1

    """

    exec_ = 0

    configure = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _tailf_aaa as meta
        return meta._meta_table['BuiltinmodesEnum']



class Aaa(object):
    """
    
    
    .. attribute:: authentication
    
    	
    	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xe.tailf_aaa.Aaa.Authentication>`
    
    .. attribute:: ios
    
    	
    	**type**\:   :py:class:`Ios <ydk.models.cisco_ios_xe.tailf_aaa.Aaa.Ios>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'aaa'
    _revision = '2015-06-16'

    def __init__(self):
        self.authentication = Aaa.Authentication()
        self.authentication.parent = self
        self.ios = None


    class Authentication(object):
        """
        
        
        .. attribute:: users
        
        	
        	**type**\:   :py:class:`Users <ydk.models.cisco_ios_xe.tailf_aaa.Aaa.Authentication.Users>`
        
        

        """

        _prefix = 'aaa'
        _revision = '2015-06-16'

        def __init__(self):
            self.parent = None
            self.users = Aaa.Authentication.Users()
            self.users.parent = self


        class Users(object):
            """
            
            
            .. attribute:: user
            
            	
            	**type**\: list of    :py:class:`User <ydk.models.cisco_ios_xe.tailf_aaa.Aaa.Authentication.Users.User>`
            
            

            """

            _prefix = 'aaa'
            _revision = '2015-06-16'

            def __init__(self):
                self.parent = None
                self.user = YList()
                self.user.parent = self
                self.user.name = 'user'


            class User(object):
                """
                
                
                .. attribute:: name  <key>
                
                	
                	**type**\:  str
                
                .. attribute:: gid
                
                	
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**mandatory**\: True
                
                .. attribute:: homedir
                
                	
                	**type**\:  str
                
                	**mandatory**\: True
                
                .. attribute:: password
                
                	
                	**type**\:  str
                
                	**pattern:** $0$.\*\|$1$[a\-zA\-Z0\-9./]{1,8}$[a\-zA\-Z0\-9./]{22}\|$5$(rounds=\\d+$)?[a\-zA\-Z0\-9./]{1,16}$[a\-zA\-Z0\-9./]{43}\|$6$(rounds=\\d+$)?[a\-zA\-Z0\-9./]{1,16}$[a\-zA\-Z0\-9./]{86}
                
                	**mandatory**\: True
                
                .. attribute:: ssh_keydir
                
                	
                	**type**\:  str
                
                	**mandatory**\: True
                
                .. attribute:: uid
                
                	
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'aaa'
                _revision = '2015-06-16'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.gid = None
                    self.homedir = None
                    self.password = None
                    self.ssh_keydir = None
                    self.uid = None

                @property
                def _common_path(self):
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return '/tailf-aaa:aaa/tailf-aaa:authentication/tailf-aaa:users/tailf-aaa:user[tailf-aaa:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.gid is not None:
                        return True

                    if self.homedir is not None:
                        return True

                    if self.password is not None:
                        return True

                    if self.ssh_keydir is not None:
                        return True

                    if self.uid is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _tailf_aaa as meta
                    return meta._meta_table['Aaa.Authentication.Users.User']['meta_info']

            @property
            def _common_path(self):

                return '/tailf-aaa:aaa/tailf-aaa:authentication/tailf-aaa:users'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.user is not None:
                    for child_ref in self.user:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _tailf_aaa as meta
                return meta._meta_table['Aaa.Authentication.Users']['meta_info']

        @property
        def _common_path(self):

            return '/tailf-aaa:aaa/tailf-aaa:authentication'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.users is not None and self.users._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _tailf_aaa as meta
            return meta._meta_table['Aaa.Authentication']['meta_info']


    class Ios(object):
        """
        
        
        .. attribute:: level
        
        	
        	**type**\: list of    :py:class:`Level <ydk.models.cisco_ios_xe.tailf_aaa.Aaa.Ios.Level>`
        
        .. attribute:: privilege
        
        	
        	**type**\: list of    :py:class:`Privilege <ydk.models.cisco_ios_xe.tailf_aaa.Aaa.Ios.Privilege>`
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'aaa'
        _revision = '2015-06-16'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.level = YList()
            self.level.parent = self
            self.level.name = 'level'
            self.privilege = YList()
            self.privilege.parent = self
            self.privilege.name = 'privilege'


        class Level(object):
            """
            
            
            .. attribute:: nr  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..15
            
            .. attribute:: password
            
            	
            	**type**\:  str
            
            	**pattern:** $0$.\*\|$1$[a\-zA\-Z0\-9./]{1,8}$[a\-zA\-Z0\-9./]{22}\|$5$(rounds=\\d+$)?[a\-zA\-Z0\-9./]{1,16}$[a\-zA\-Z0\-9./]{43}\|$6$(rounds=\\d+$)?[a\-zA\-Z0\-9./]{1,16}$[a\-zA\-Z0\-9./]{86}
            
            .. attribute:: prompt
            
            	
            	**type**\:  str
            
            	**default value**\: \h# 
            
            .. attribute:: secret
            
            	
            	**type**\:  str
            
            	**pattern:** $0$.\*\|$1$[a\-zA\-Z0\-9./]{1,8}$[a\-zA\-Z0\-9./]{22}\|$5$(rounds=\\d+$)?[a\-zA\-Z0\-9./]{1,16}$[a\-zA\-Z0\-9./]{43}\|$6$(rounds=\\d+$)?[a\-zA\-Z0\-9./]{1,16}$[a\-zA\-Z0\-9./]{86}
            
            

            """

            _prefix = 'aaa'
            _revision = '2015-06-16'

            def __init__(self):
                self.parent = None
                self.nr = None
                self.password = None
                self.prompt = None
                self.secret = None

            @property
            def _common_path(self):
                if self.nr is None:
                    raise YPYModelError('Key property nr is None')

                return '/tailf-aaa:aaa/tailf-aaa:ios/tailf-aaa:level[tailf-aaa:nr = ' + str(self.nr) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.nr is not None:
                    return True

                if self.password is not None:
                    return True

                if self.prompt is not None:
                    return True

                if self.secret is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _tailf_aaa as meta
                return meta._meta_table['Aaa.Ios.Level']['meta_info']


        class Privilege(object):
            """
            
            
            .. attribute:: mode  <key>
            
            	
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            
            ----
            	**type**\:   :py:class:`BuiltinmodesEnum <ydk.models.cisco_ios_xe.tailf_aaa.BuiltinmodesEnum>`
            
            
            ----
            .. attribute:: level
            
            	
            	**type**\: list of    :py:class:`Level <ydk.models.cisco_ios_xe.tailf_aaa.Aaa.Ios.Privilege.Level>`
            
            

            """

            _prefix = 'aaa'
            _revision = '2015-06-16'

            def __init__(self):
                self.parent = None
                self.mode = None
                self.level = YList()
                self.level.parent = self
                self.level.name = 'level'


            class Level(object):
                """
                
                
                .. attribute:: nr  <key>
                
                	
                	**type**\:  int
                
                	**range:** 0..15
                
                .. attribute:: command
                
                	
                	**type**\: list of    :py:class:`Command <ydk.models.cisco_ios_xe.tailf_aaa.Aaa.Ios.Privilege.Level.Command>`
                
                

                """

                _prefix = 'aaa'
                _revision = '2015-06-16'

                def __init__(self):
                    self.parent = None
                    self.nr = None
                    self.command = YList()
                    self.command.parent = self
                    self.command.name = 'command'


                class Command(object):
                    """
                    
                    
                    .. attribute:: name  <key>
                    
                    	
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'aaa'
                    _revision = '2015-06-16'

                    def __init__(self):
                        self.parent = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.name is None:
                            raise YPYModelError('Key property name is None')

                        return self.parent._common_path +'/tailf-aaa:command[tailf-aaa:name = ' + str(self.name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _tailf_aaa as meta
                        return meta._meta_table['Aaa.Ios.Privilege.Level.Command']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.nr is None:
                        raise YPYModelError('Key property nr is None')

                    return self.parent._common_path +'/tailf-aaa:level[tailf-aaa:nr = ' + str(self.nr) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.nr is not None:
                        return True

                    if self.command is not None:
                        for child_ref in self.command:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _tailf_aaa as meta
                    return meta._meta_table['Aaa.Ios.Privilege.Level']['meta_info']

            @property
            def _common_path(self):
                if self.mode is None:
                    raise YPYModelError('Key property mode is None')

                return '/tailf-aaa:aaa/tailf-aaa:ios/tailf-aaa:privilege[tailf-aaa:mode = ' + str(self.mode) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.mode is not None:
                    return True

                if self.level is not None:
                    for child_ref in self.level:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _tailf_aaa as meta
                return meta._meta_table['Aaa.Ios.Privilege']['meta_info']

        @property
        def _common_path(self):

            return '/tailf-aaa:aaa/tailf-aaa:ios'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.level is not None:
                for child_ref in self.level:
                    if child_ref._has_data():
                        return True

            if self.privilege is not None:
                for child_ref in self.privilege:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _tailf_aaa as meta
            return meta._meta_table['Aaa.Ios']['meta_info']

    @property
    def _common_path(self):

        return '/tailf-aaa:aaa'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.authentication is not None and self.authentication._has_data():
            return True

        if self.ios is not None and self.ios._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _tailf_aaa as meta
        return meta._meta_table['Aaa']['meta_info']


class Alias(object):
    """
    
    
    .. attribute:: name  <key>
    
    	
    	**type**\:  str
    
    .. attribute:: expansion
    
    	
    	**type**\:  str
    
    	**mandatory**\: True
    
    

    """

    _prefix = 'aaa'
    _revision = '2015-06-16'

    def __init__(self):
        self.name = None
        self.expansion = None

    @property
    def _common_path(self):
        if self.name is None:
            raise YPYModelError('Key property name is None')

        return '/tailf-aaa:alias[tailf-aaa:name = ' + str(self.name) + ']'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.name is not None:
            return True

        if self.expansion is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _tailf_aaa as meta
        return meta._meta_table['Alias']['meta_info']


class Session(object):
    """
    
    
    .. attribute:: autowizard
    
    	
    	**type**\:  bool
    
    .. attribute:: complete_on_space
    
    	
    	**type**\:  bool
    
    .. attribute:: display_level
    
    	
    	**type**\:  int
    
    	**range:** 1..64
    
    .. attribute:: history
    
    	
    	**type**\:  int
    
    	**range:** 0..8192
    
    .. attribute:: idle_timeout
    
    	
    	**type**\:  int
    
    	**range:** 0..8192
    
    .. attribute:: ignore_leading_space
    
    	
    	**type**\:  bool
    
    .. attribute:: paginate
    
    	
    	**type**\:  bool
    
    .. attribute:: prompt1
    
    	
    	**type**\:  str
    
    .. attribute:: prompt2
    
    	
    	**type**\:  str
    
    .. attribute:: show_defaults
    
    	
    	**type**\:  bool
    
    .. attribute:: _is_presence
    
    	Is present if this instance represents presence container else not
    	**type**\: bool
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'aaa'
    _revision = '2015-06-16'

    def __init__(self):
        self._is_presence = True
        self.autowizard = None
        self.complete_on_space = None
        self.display_level = None
        self.history = None
        self.idle_timeout = None
        self.ignore_leading_space = None
        self.paginate = None
        self.prompt1 = None
        self.prompt2 = None
        self.show_defaults = None

    @property
    def _common_path(self):

        return '/tailf-aaa:session'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self._is_presence:
            return True
        if self.autowizard is not None:
            return True

        if self.complete_on_space is not None:
            return True

        if self.display_level is not None:
            return True

        if self.history is not None:
            return True

        if self.idle_timeout is not None:
            return True

        if self.ignore_leading_space is not None:
            return True

        if self.paginate is not None:
            return True

        if self.prompt1 is not None:
            return True

        if self.prompt2 is not None:
            return True

        if self.show_defaults is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _tailf_aaa as meta
        return meta._meta_table['Session']['meta_info']


class User(object):
    """
    
    
    .. attribute:: name  <key>
    
    	
    	**type**\:  str
    
    .. attribute:: alias
    
    	
    	**type**\: list of    :py:class:`Alias <ydk.models.cisco_ios_xe.tailf_aaa.User.Alias>`
    
    .. attribute:: description
    
    	
    	**type**\:  str
    
    .. attribute:: session
    
    	
    	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xe.tailf_aaa.User.Session>`
    
    

    """

    _prefix = 'aaa'
    _revision = '2015-06-16'

    def __init__(self):
        self.name = None
        self.alias = YList()
        self.alias.parent = self
        self.alias.name = 'alias'
        self.description = None
        self.session = User.Session()
        self.session.parent = self


    class Alias(object):
        """
        
        
        .. attribute:: name  <key>
        
        	
        	**type**\:  str
        
        .. attribute:: expansion
        
        	
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'aaa'
        _revision = '2015-06-16'

        def __init__(self):
            self.parent = None
            self.name = None
            self.expansion = None

        @property
        def _common_path(self):
            if self.parent is None:
                raise YPYModelError('parent is not set . Cannot derive path.')
            if self.name is None:
                raise YPYModelError('Key property name is None')

            return self.parent._common_path +'/tailf-aaa:alias[tailf-aaa:name = ' + str(self.name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.name is not None:
                return True

            if self.expansion is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _tailf_aaa as meta
            return meta._meta_table['User.Alias']['meta_info']


    class Session(object):
        """
        
        
        .. attribute:: autowizard
        
        	
        	**type**\:  bool
        
        .. attribute:: complete_on_space
        
        	
        	**type**\:  bool
        
        .. attribute:: display_level
        
        	
        	**type**\:  int
        
        	**range:** 1..64
        
        .. attribute:: history
        
        	
        	**type**\:  int
        
        	**range:** 0..8192
        
        .. attribute:: idle_timeout
        
        	
        	**type**\:  int
        
        	**range:** 0..8192
        
        .. attribute:: ignore_leading_space
        
        	
        	**type**\:  bool
        
        .. attribute:: paginate
        
        	
        	**type**\:  bool
        
        .. attribute:: prompt1
        
        	
        	**type**\:  str
        
        .. attribute:: prompt2
        
        	
        	**type**\:  str
        
        .. attribute:: show_defaults
        
        	
        	**type**\:  bool
        
        

        """

        _prefix = 'aaa'
        _revision = '2015-06-16'

        def __init__(self):
            self.parent = None
            self.autowizard = None
            self.complete_on_space = None
            self.display_level = None
            self.history = None
            self.idle_timeout = None
            self.ignore_leading_space = None
            self.paginate = None
            self.prompt1 = None
            self.prompt2 = None
            self.show_defaults = None

        @property
        def _common_path(self):
            if self.parent is None:
                raise YPYModelError('parent is not set . Cannot derive path.')

            return self.parent._common_path +'/tailf-aaa:session'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.autowizard is not None:
                return True

            if self.complete_on_space is not None:
                return True

            if self.display_level is not None:
                return True

            if self.history is not None:
                return True

            if self.idle_timeout is not None:
                return True

            if self.ignore_leading_space is not None:
                return True

            if self.paginate is not None:
                return True

            if self.prompt1 is not None:
                return True

            if self.prompt2 is not None:
                return True

            if self.show_defaults is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _tailf_aaa as meta
            return meta._meta_table['User.Session']['meta_info']

    @property
    def _common_path(self):
        if self.name is None:
            raise YPYModelError('Key property name is None')

        return '/tailf-aaa:user[tailf-aaa:name = ' + str(self.name) + ']'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.name is not None:
            return True

        if self.alias is not None:
            for child_ref in self.alias:
                if child_ref._has_data():
                    return True

        if self.description is not None:
            return True

        if self.session is not None and self.session._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _tailf_aaa as meta
        return meta._meta_table['User']['meta_info']



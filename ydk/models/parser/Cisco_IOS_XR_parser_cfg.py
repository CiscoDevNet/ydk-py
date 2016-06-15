""" Cisco_IOS_XR_parser_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR parser package configuration.

This module contains definitions
for the following management objects\:
  parser\: Parser configuration

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Parser(object):
    """
    Parser configuration
    
    .. attribute:: alias
    
    	Alias for command mapping
    	**type**\: :py:class:`Alias <ydk.models.parser.Cisco_IOS_XR_parser_cfg.Parser.Alias>`
    
    .. attribute:: configuration
    
    	cli configuration services
    	**type**\: :py:class:`Configuration <ydk.models.parser.Cisco_IOS_XR_parser_cfg.Parser.Configuration>`
    
    .. attribute:: history
    
    	cli commands history
    	**type**\: :py:class:`History <ydk.models.parser.Cisco_IOS_XR_parser_cfg.Parser.History>`
    
    .. attribute:: indentation
    
    	indentation tracking
    	**type**\: :py:class:`Indentation <ydk.models.parser.Cisco_IOS_XR_parser_cfg.Parser.Indentation>`
    
    .. attribute:: submode_exit
    
    	Exit submode when only '!' seen in interactive mode
    	**type**\: :py:class:`SubmodeExit <ydk.models.parser.Cisco_IOS_XR_parser_cfg.Parser.SubmodeExit>`
    
    

    """

    _prefix = 'parser-cfg'
    _revision = '2015-06-02'

    def __init__(self):
        self.alias = Parser.Alias()
        self.alias.parent = self
        self.configuration = Parser.Configuration()
        self.configuration.parent = self
        self.history = Parser.History()
        self.history.parent = self
        self.indentation = Parser.Indentation()
        self.indentation.parent = self
        self.submode_exit = Parser.SubmodeExit()
        self.submode_exit.parent = self


    class Indentation(object):
        """
        indentation tracking
        
        .. attribute:: indentation_disable
        
        	disable the indentation
        	**type**\: bool
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2015-06-02'

        def __init__(self):
            self.parent = None
            self.indentation_disable = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-parser-cfg:parser/Cisco-IOS-XR-parser-cfg:indentation'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.indentation_disable is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.parser._meta import _Cisco_IOS_XR_parser_cfg as meta
            return meta._meta_table['Parser.Indentation']['meta_info']


    class Alias(object):
        """
        Alias for command mapping
        
        .. attribute:: alls
        
        	Table of all aliases configured
        	**type**\: :py:class:`Alls <ydk.models.parser.Cisco_IOS_XR_parser_cfg.Parser.Alias.Alls>`
        
        .. attribute:: configurations
        
        	Configuration command alias
        	**type**\: :py:class:`Configurations <ydk.models.parser.Cisco_IOS_XR_parser_cfg.Parser.Alias.Configurations>`
        
        .. attribute:: execs
        
        	Exec command alias
        	**type**\: :py:class:`Execs <ydk.models.parser.Cisco_IOS_XR_parser_cfg.Parser.Alias.Execs>`
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2015-06-02'

        def __init__(self):
            self.parent = None
            self.alls = Parser.Alias.Alls()
            self.alls.parent = self
            self.configurations = Parser.Alias.Configurations()
            self.configurations.parent = self
            self.execs = Parser.Alias.Execs()
            self.execs.parent = self


        class Execs(object):
            """
            Exec command alias
            
            .. attribute:: exec_
            
            	Exec alias name
            	**type**\: list of :py:class:`Exec <ydk.models.parser.Cisco_IOS_XR_parser_cfg.Parser.Alias.Execs.Exec>`
            
            

            """

            _prefix = 'parser-cfg'
            _revision = '2015-06-02'

            def __init__(self):
                self.parent = None
                self.exec_ = YList()
                self.exec_.parent = self
                self.exec_.name = 'exec_'


            class Exec(object):
                """
                Exec alias name
                
                .. attribute:: identifier  <key>
                
                	Exec Alias name
                	**type**\: str
                
                	**range:** 0..30
                
                .. attribute:: identifier_xr
                
                	Aliased exec command
                	**type**\: str
                
                

                """

                _prefix = 'parser-cfg'
                _revision = '2015-06-02'

                def __init__(self):
                    self.parent = None
                    self.identifier = None
                    self.identifier_xr = None

                @property
                def _common_path(self):
                    if self.identifier is None:
                        raise YPYModelError('Key property identifier is None')

                    return '/Cisco-IOS-XR-parser-cfg:parser/Cisco-IOS-XR-parser-cfg:alias/Cisco-IOS-XR-parser-cfg:execs/Cisco-IOS-XR-parser-cfg:exec[Cisco-IOS-XR-parser-cfg:identifier = ' + str(self.identifier) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.identifier is not None:
                        return True

                    if self.identifier_xr is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.parser._meta import _Cisco_IOS_XR_parser_cfg as meta
                    return meta._meta_table['Parser.Alias.Execs.Exec']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-parser-cfg:parser/Cisco-IOS-XR-parser-cfg:alias/Cisco-IOS-XR-parser-cfg:execs'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.exec_ is not None:
                    for child_ref in self.exec_:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.parser._meta import _Cisco_IOS_XR_parser_cfg as meta
                return meta._meta_table['Parser.Alias.Execs']['meta_info']


        class Configurations(object):
            """
            Configuration command alias
            
            .. attribute:: configuration
            
            	Configuration Alias name
            	**type**\: list of :py:class:`Configuration <ydk.models.parser.Cisco_IOS_XR_parser_cfg.Parser.Alias.Configurations.Configuration>`
            
            

            """

            _prefix = 'parser-cfg'
            _revision = '2015-06-02'

            def __init__(self):
                self.parent = None
                self.configuration = YList()
                self.configuration.parent = self
                self.configuration.name = 'configuration'


            class Configuration(object):
                """
                Configuration Alias name
                
                .. attribute:: identifier  <key>
                
                	Configuration alias name
                	**type**\: str
                
                	**range:** 0..30
                
                .. attribute:: identifier_xr
                
                	Aliased config command
                	**type**\: str
                
                

                """

                _prefix = 'parser-cfg'
                _revision = '2015-06-02'

                def __init__(self):
                    self.parent = None
                    self.identifier = None
                    self.identifier_xr = None

                @property
                def _common_path(self):
                    if self.identifier is None:
                        raise YPYModelError('Key property identifier is None')

                    return '/Cisco-IOS-XR-parser-cfg:parser/Cisco-IOS-XR-parser-cfg:alias/Cisco-IOS-XR-parser-cfg:configurations/Cisco-IOS-XR-parser-cfg:configuration[Cisco-IOS-XR-parser-cfg:identifier = ' + str(self.identifier) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.identifier is not None:
                        return True

                    if self.identifier_xr is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.parser._meta import _Cisco_IOS_XR_parser_cfg as meta
                    return meta._meta_table['Parser.Alias.Configurations.Configuration']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-parser-cfg:parser/Cisco-IOS-XR-parser-cfg:alias/Cisco-IOS-XR-parser-cfg:configurations'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.configuration is not None:
                    for child_ref in self.configuration:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.parser._meta import _Cisco_IOS_XR_parser_cfg as meta
                return meta._meta_table['Parser.Alias.Configurations']['meta_info']


        class Alls(object):
            """
            Table of all aliases configured
            
            .. attribute:: all
            
            	Alias name to command mapping
            	**type**\: list of :py:class:`All <ydk.models.parser.Cisco_IOS_XR_parser_cfg.Parser.Alias.Alls.All>`
            
            

            """

            _prefix = 'parser-cfg'
            _revision = '2015-06-02'

            def __init__(self):
                self.parent = None
                self.all = YList()
                self.all.parent = self
                self.all.name = 'all'


            class All(object):
                """
                Alias name to command mapping
                
                .. attribute:: identifier  <key>
                
                	Alias name
                	**type**\: str
                
                	**range:** 0..30
                
                .. attribute:: identifier_xr
                
                	The actual command
                	**type**\: str
                
                

                """

                _prefix = 'parser-cfg'
                _revision = '2015-06-02'

                def __init__(self):
                    self.parent = None
                    self.identifier = None
                    self.identifier_xr = None

                @property
                def _common_path(self):
                    if self.identifier is None:
                        raise YPYModelError('Key property identifier is None')

                    return '/Cisco-IOS-XR-parser-cfg:parser/Cisco-IOS-XR-parser-cfg:alias/Cisco-IOS-XR-parser-cfg:alls/Cisco-IOS-XR-parser-cfg:all[Cisco-IOS-XR-parser-cfg:identifier = ' + str(self.identifier) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.identifier is not None:
                        return True

                    if self.identifier_xr is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.parser._meta import _Cisco_IOS_XR_parser_cfg as meta
                    return meta._meta_table['Parser.Alias.Alls.All']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-parser-cfg:parser/Cisco-IOS-XR-parser-cfg:alias/Cisco-IOS-XR-parser-cfg:alls'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.all is not None:
                    for child_ref in self.all:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.parser._meta import _Cisco_IOS_XR_parser_cfg as meta
                return meta._meta_table['Parser.Alias.Alls']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-parser-cfg:parser/Cisco-IOS-XR-parser-cfg:alias'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.alls is not None and self.alls._has_data():
                return True

            if self.configurations is not None and self.configurations._has_data():
                return True

            if self.execs is not None and self.execs._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.parser._meta import _Cisco_IOS_XR_parser_cfg as meta
            return meta._meta_table['Parser.Alias']['meta_info']


    class History(object):
        """
        cli commands history
        
        .. attribute:: size
        
        	maximum number of commands in history
        	**type**\: int
        
        	**range:** 1000..5000
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2015-06-02'

        def __init__(self):
            self.parent = None
            self.size = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-parser-cfg:parser/Cisco-IOS-XR-parser-cfg:history'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.size is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.parser._meta import _Cisco_IOS_XR_parser_cfg as meta
            return meta._meta_table['Parser.History']['meta_info']


    class Configuration(object):
        """
        cli configuration services
        
        .. attribute:: disable
        
        	disable for read\-only access users
        	**type**\: :py:class:`Disable <ydk.models.parser.Cisco_IOS_XR_parser_cfg.Parser.Configuration.Disable>`
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2015-06-02'

        def __init__(self):
            self.parent = None
            self.disable = Parser.Configuration.Disable()
            self.disable.parent = self


        class Disable(object):
            """
            disable for read\-only access users
            
            .. attribute:: usergroup
            
            	Disable config mode for usergroup
            	**type**\: str
            
            

            """

            _prefix = 'parser-cfg'
            _revision = '2015-06-02'

            def __init__(self):
                self.parent = None
                self.usergroup = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-parser-cfg:parser/Cisco-IOS-XR-parser-cfg:configuration/Cisco-IOS-XR-parser-cfg:disable'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.usergroup is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.parser._meta import _Cisco_IOS_XR_parser_cfg as meta
                return meta._meta_table['Parser.Configuration.Disable']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-parser-cfg:parser/Cisco-IOS-XR-parser-cfg:configuration'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.disable is not None and self.disable._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.parser._meta import _Cisco_IOS_XR_parser_cfg as meta
            return meta._meta_table['Parser.Configuration']['meta_info']


    class SubmodeExit(object):
        """
        Exit submode when only '!' seen in interactive
        mode
        
        .. attribute:: enable
        
        	Enable the feature
        	**type**\: bool
        
        

        """

        _prefix = 'parser-cfg'
        _revision = '2015-06-02'

        def __init__(self):
            self.parent = None
            self.enable = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-parser-cfg:parser/Cisco-IOS-XR-parser-cfg:submode-exit'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.enable is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.parser._meta import _Cisco_IOS_XR_parser_cfg as meta
            return meta._meta_table['Parser.SubmodeExit']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-parser-cfg:parser'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.alias is not None and self.alias._has_data():
            return True

        if self.configuration is not None and self.configuration._has_data():
            return True

        if self.history is not None and self.history._has_data():
            return True

        if self.indentation is not None and self.indentation._has_data():
            return True

        if self.submode_exit is not None and self.submode_exit._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.parser._meta import _Cisco_IOS_XR_parser_cfg as meta
        return meta._meta_table['Parser']['meta_info']



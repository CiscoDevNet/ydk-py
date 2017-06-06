""" Cisco_IOS_XE_rpc 

NED RPC YANG module for IOS
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class SwitchRpc(object):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.SwitchRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.SwitchRpc.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-02-07'

    def __init__(self):
        self.input = SwitchRpc.Input()
        self.input.parent = self
        self.output = SwitchRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: priority
        
        	<1\-15>  Switch Priority
        	**type**\:  int
        
        	**range:** 1..15
        
        .. attribute:: renumber
        
        	<1\-9>  New number of the Switch
        	**type**\:  int
        
        	**range:** 1..9
        
        .. attribute:: statck
        
        	
        	**type**\:   :py:class:`Statck <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.SwitchRpc.Input.Statck>`
        
        .. attribute:: switch_number
        
        	
        	**type**\:  int
        
        	**range:** 1..9
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.priority = None
            self.renumber = None
            self.statck = SwitchRpc.Input.Statck()
            self.statck.parent = self
            self.switch_number = None


        class Statck(object):
            """
            
            
            .. attribute:: port
            
            	<1\-2>  Stack port number to enable/disable
            	**type**\:  int
            
            	**range:** 1..2
            
            

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.port = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-rpc:switch/Cisco-IOS-XE-rpc:input/Cisco-IOS-XE-rpc:statck'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if self.port is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_rpc as meta
                return meta._meta_table['SwitchRpc.Input.Statck']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-rpc:switch/Cisco-IOS-XE-rpc:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.priority is not None:
                return True

            if self.renumber is not None:
                return True

            if self.statck is not None and self.statck._has_data():
                return True

            if self.switch_number is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_rpc as meta
            return meta._meta_table['SwitchRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\:  str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.result = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-rpc:switch/Cisco-IOS-XE-rpc:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.result is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_rpc as meta
            return meta._meta_table['SwitchRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-rpc:switch'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_rpc as meta
        return meta._meta_table['SwitchRpc']['meta_info']


class DefaultRpc(object):
    """
    Set a command to its defaults
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.DefaultRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.DefaultRpc.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-02-07'

    def __init__(self):
        self.input = DefaultRpc.Input()
        self.input.parent = self
        self.output = DefaultRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: interface
        
        	Select an interface to configure
        	**type**\:  str
        
        	**pattern:** ([0\-9a\-zA\-Z.]+)
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.interface = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-rpc:default/Cisco-IOS-XE-rpc:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.interface is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_rpc as meta
            return meta._meta_table['DefaultRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\:  str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.result = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-rpc:default/Cisco-IOS-XE-rpc:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.result is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_rpc as meta
            return meta._meta_table['DefaultRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-rpc:default'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_rpc as meta
        return meta._meta_table['DefaultRpc']['meta_info']


class ReloadRpc(object):
    """
    Halt and perform a cold restart
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.ReloadRpc.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-02-07'

    def __init__(self):
        self.output = ReloadRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Output(object):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\:  str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.result = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-rpc:reload/Cisco-IOS-XE-rpc:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.result is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_rpc as meta
            return meta._meta_table['ReloadRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-rpc:reload'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_rpc as meta
        return meta._meta_table['ReloadRpc']['meta_info']


class LicenseRpc(object):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.LicenseRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.LicenseRpc.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-02-07'

    def __init__(self):
        self.input = LicenseRpc.Input()
        self.input.parent = self
        self.output = LicenseRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: smart
        
        	
        	**type**\:   :py:class:`Smart <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.LicenseRpc.Input.Smart>`
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.smart = LicenseRpc.Input.Smart()
            self.smart.parent = self


        class Smart(object):
            """
            
            
            .. attribute:: deregister
            
            	
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: register
            
            	
            	**type**\:   :py:class:`Register <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.LicenseRpc.Input.Smart.Register>`
            
            .. attribute:: renew
            
            	
            	**type**\:   :py:class:`Renew <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.LicenseRpc.Input.Smart.Renew>`
            
            

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.deregister = None
                self.register = LicenseRpc.Input.Smart.Register()
                self.register.parent = self
                self.renew = LicenseRpc.Input.Smart.Renew()
                self.renew.parent = self


            class Register(object):
                """
                
                
                .. attribute:: idtoken
                
                	
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ios-xe-rpc'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.idtoken = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XE-rpc:license/Cisco-IOS-XE-rpc:input/Cisco-IOS-XE-rpc:smart/Cisco-IOS-XE-rpc:register'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    if self.parent is None:
                        raise YPYError('Parent reference is needed to determine if entity has configuration data')
                    return self.parent.is_config()

                def _has_data(self):
                    if self.idtoken is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_rpc as meta
                    return meta._meta_table['LicenseRpc.Input.Smart.Register']['meta_info']


            class Renew(object):
                """
                
                
                .. attribute:: auth
                
                	
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: id
                
                	
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ios-xe-rpc'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.auth = None
                    self.id = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XE-rpc:license/Cisco-IOS-XE-rpc:input/Cisco-IOS-XE-rpc:smart/Cisco-IOS-XE-rpc:renew'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    if self.parent is None:
                        raise YPYError('Parent reference is needed to determine if entity has configuration data')
                    return self.parent.is_config()

                def _has_data(self):
                    if self.auth is not None:
                        return True

                    if self.id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_rpc as meta
                    return meta._meta_table['LicenseRpc.Input.Smart.Renew']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-rpc:license/Cisco-IOS-XE-rpc:input/Cisco-IOS-XE-rpc:smart'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if self.deregister is not None:
                    return True

                if self.register is not None and self.register._has_data():
                    return True

                if self.renew is not None and self.renew._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_rpc as meta
                return meta._meta_table['LicenseRpc.Input.Smart']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-rpc:license/Cisco-IOS-XE-rpc:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.smart is not None and self.smart._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_rpc as meta
            return meta._meta_table['LicenseRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\:  str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.result = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-rpc:license/Cisco-IOS-XE-rpc:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.result is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_rpc as meta
            return meta._meta_table['LicenseRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-rpc:license'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_rpc as meta
        return meta._meta_table['LicenseRpc']['meta_info']



""" Cisco_IOS_XR_tunnel_l2tun_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tunnel\-l2tun package configuration.

This module contains definitions
for the following management objects\:
  l2tp\: L2TPv3 class used for L2VPNs

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class L2TpDigestHashMethodEnum(Enum):
    """
    L2TpDigestHashMethodEnum

    L2tp digest hash method

    .. data:: md5 = 1

    	MD5

    .. data:: sha1 = 2

    	SHA1

    """

    md5 = 1

    sha1 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_cfg as meta
        return meta._meta_table['L2TpDigestHashMethodEnum']


class L2TpHashMethodEnum(Enum):
    """
    L2TpHashMethodEnum

    L2tp hash method

    .. data:: md5 = 1

    	MD5

    .. data:: sha1 = 2

    	SHA1

    .. data:: none = 3

    	None

    """

    md5 = 1

    sha1 = 2

    none = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_cfg as meta
        return meta._meta_table['L2TpHashMethodEnum']



class L2Tp(object):
    """
    L2TPv3 class used for L2VPNs
    
    .. attribute:: classes
    
    	List of classes
    	**type**\:   :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes>`
    
    

    """

    _prefix = 'tunnel-l2tun-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.classes = L2Tp.Classes()
        self.classes.parent = self


    class Classes(object):
        """
        List of classes
        
        .. attribute:: class_
        
        	Configuration for a specific class
        	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_>`
        
        

        """

        _prefix = 'tunnel-l2tun-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.class_ = YList()
            self.class_.parent = self
            self.class_.name = 'class_'


        class Class_(object):
            """
            Configuration for a specific class
            
            .. attribute:: class_name  <key>
            
            	Specify the class name. Regexp\: ^[a\-z0\-9A\-Z][\-\_.a\-z0\-9A\-Z]\*$
            	**type**\:  str
            
            	**length:** 1..31
            
            .. attribute:: authentication
            
            	Authenticate the L2TP control connection
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: congestion_control
            
            	Congestion control enabled
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: digest
            
            	Message digest authentication for the L2TP control connection
            	**type**\:   :py:class:`Digest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_.Digest>`
            
            .. attribute:: enable
            
            	Enable L2TPv3 class used for L2VPNs
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: hello_interval
            
            	Specify interval (in seconds)
            	**type**\:  int
            
            	**range:** 0..1000
            
            	**units**\: second
            
            .. attribute:: hidden
            
            	Specify to hide AVPs in outgoing control messages
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: host_name
            
            	Local hostname for control connection authentication
            	**type**\:  str
            
            .. attribute:: ip
            
            	IP TOS value
            	**type**\:   :py:class:`Ip <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_.Ip>`
            
            .. attribute:: password
            
            	Specify the password for control channel authentication
            	**type**\:  str
            
            	**pattern:** (!.+)\|([^!].+)
            
            .. attribute:: receive_window
            
            	Receive window size for the control connection
            	**type**\:  int
            
            	**range:** 1..16384
            
            	**units**\: byte
            
            .. attribute:: retransmit
            
            	Control message retransmission parameters
            	**type**\:   :py:class:`Retransmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_.Retransmit>`
            
            .. attribute:: security
            
            	Security check
            	**type**\:   :py:class:`Security <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_.Security>`
            
            .. attribute:: timeout_no_user
            
            	Timeout value for no\-user in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: timeout_setup
            
            	Time permitted to set up a control connection
            	**type**\:  int
            
            	**range:** 60..6000
            
            	**units**\: second
            
            .. attribute:: tunnel
            
            	l2TP tunnel
            	**type**\:   :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_.Tunnel>`
            
            

            """

            _prefix = 'tunnel-l2tun-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.class_name = None
                self.authentication = None
                self.congestion_control = None
                self.digest = L2Tp.Classes.Class_.Digest()
                self.digest.parent = self
                self.enable = None
                self.hello_interval = None
                self.hidden = None
                self.host_name = None
                self.ip = L2Tp.Classes.Class_.Ip()
                self.ip.parent = self
                self.password = None
                self.receive_window = None
                self.retransmit = L2Tp.Classes.Class_.Retransmit()
                self.retransmit.parent = self
                self.security = L2Tp.Classes.Class_.Security()
                self.security.parent = self
                self.timeout_no_user = None
                self.timeout_setup = None
                self.tunnel = L2Tp.Classes.Class_.Tunnel()
                self.tunnel.parent = self


            class Security(object):
                """
                Security check
                
                .. attribute:: ip
                
                	Security check for IP
                	**type**\:   :py:class:`Ip <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_.Security.Ip>`
                
                

                """

                _prefix = 'tunnel-l2tun-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ip = L2Tp.Classes.Class_.Security.Ip()
                    self.ip.parent = self


                class Ip(object):
                    """
                    Security check for IP
                    
                    .. attribute:: address_check
                    
                    	Enable IP address check for L2TP packets
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.address_check = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-cfg:ip'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.address_check is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_cfg as meta
                        return meta._meta_table['L2Tp.Classes.Class_.Security.Ip']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-cfg:security'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ip is not None and self.ip._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_cfg as meta
                    return meta._meta_table['L2Tp.Classes.Class_.Security']['meta_info']


            class Retransmit(object):
                """
                Control message retransmission parameters
                
                .. attribute:: initial
                
                	Set retries and timeouts for initial
                	**type**\:   :py:class:`Initial <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_.Retransmit.Initial>`
                
                .. attribute:: retry
                
                	Specify retransmit retry count
                	**type**\:  int
                
                	**range:** 5..1000
                
                .. attribute:: timeout
                
                	Set timeout value range
                	**type**\:   :py:class:`Timeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_.Retransmit.Timeout>`
                
                

                """

                _prefix = 'tunnel-l2tun-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.initial = L2Tp.Classes.Class_.Retransmit.Initial()
                    self.initial.parent = self
                    self.retry = None
                    self.timeout = L2Tp.Classes.Class_.Retransmit.Timeout()
                    self.timeout.parent = self


                class Initial(object):
                    """
                    Set retries and timeouts for initial
                    
                    .. attribute:: retry
                    
                    	Specify the retry number
                    	**type**\:  int
                    
                    	**range:** 1..1000
                    
                    .. attribute:: timeout
                    
                    	Set timeout value range
                    	**type**\:   :py:class:`Timeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_.Retransmit.Initial.Timeout>`
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.retry = None
                        self.timeout = L2Tp.Classes.Class_.Retransmit.Initial.Timeout()
                        self.timeout.parent = self


                    class Timeout(object):
                        """
                        Set timeout value range
                        
                        .. attribute:: maximum
                        
                        	Specify maximum timeout
                        	**type**\:  int
                        
                        	**range:** 1..8
                        
                        .. attribute:: minimum
                        
                        	Specify minimum timeout
                        	**type**\:  int
                        
                        	**range:** 1..8
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.maximum = None
                            self.minimum = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-cfg:timeout'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.maximum is not None:
                                return True

                            if self.minimum is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_cfg as meta
                            return meta._meta_table['L2Tp.Classes.Class_.Retransmit.Initial.Timeout']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-cfg:initial'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.retry is not None:
                            return True

                        if self.timeout is not None and self.timeout._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_cfg as meta
                        return meta._meta_table['L2Tp.Classes.Class_.Retransmit.Initial']['meta_info']


                class Timeout(object):
                    """
                    Set timeout value range
                    
                    .. attribute:: maximum
                    
                    	Specify maximum timeout
                    	**type**\:  int
                    
                    	**range:** 1..8
                    
                    .. attribute:: minimum
                    
                    	Specify minimum timeout
                    	**type**\:  int
                    
                    	**range:** 1..8
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.maximum = None
                        self.minimum = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-cfg:timeout'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.maximum is not None:
                            return True

                        if self.minimum is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_cfg as meta
                        return meta._meta_table['L2Tp.Classes.Class_.Retransmit.Timeout']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-cfg:retransmit'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.initial is not None and self.initial._has_data():
                        return True

                    if self.retry is not None:
                        return True

                    if self.timeout is not None and self.timeout._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_cfg as meta
                    return meta._meta_table['L2Tp.Classes.Class_.Retransmit']['meta_info']


            class Tunnel(object):
                """
                l2TP tunnel
                
                .. attribute:: accounting
                
                	Tunnel accounting
                	**type**\:  str
                
                

                """

                _prefix = 'tunnel-l2tun-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.accounting = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-cfg:tunnel'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.accounting is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_cfg as meta
                    return meta._meta_table['L2Tp.Classes.Class_.Tunnel']['meta_info']


            class Digest(object):
                """
                Message digest authentication for the L2TP
                control connection
                
                .. attribute:: check_disable
                
                	Disable digest checking
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: hash
                
                	Specify hash method
                	**type**\:   :py:class:`L2TpDigestHashMethodEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2TpDigestHashMethodEnum>`
                
                .. attribute:: secrets
                
                	Set shared secret for message digest
                	**type**\:   :py:class:`Secrets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_.Digest.Secrets>`
                
                

                """

                _prefix = 'tunnel-l2tun-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.check_disable = None
                    self.hash = None
                    self.secrets = L2Tp.Classes.Class_.Digest.Secrets()
                    self.secrets.parent = self


                class Secrets(object):
                    """
                    Set shared secret for message digest
                    
                    .. attribute:: secret
                    
                    	The encrypted user secret and hash method
                    	**type**\: list of    :py:class:`Secret <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class_.Digest.Secrets.Secret>`
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.secret = YList()
                        self.secret.parent = self
                        self.secret.name = 'secret'


                    class Secret(object):
                        """
                        The encrypted user secret and hash method
                        
                        .. attribute:: secret_name  <key>
                        
                        	Specify the encrypted user secret
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: hash
                        
                        	Specify hash method
                        	**type**\:   :py:class:`L2TpHashMethodEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2TpHashMethodEnum>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.secret_name = None
                            self.hash = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.secret_name is None:
                                raise YPYModelError('Key property secret_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-cfg:secret[Cisco-IOS-XR-tunnel-l2tun-cfg:secret-name = ' + str(self.secret_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.secret_name is not None:
                                return True

                            if self.hash is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_cfg as meta
                            return meta._meta_table['L2Tp.Classes.Class_.Digest.Secrets.Secret']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-cfg:secrets'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.secret is not None:
                            for child_ref in self.secret:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_cfg as meta
                        return meta._meta_table['L2Tp.Classes.Class_.Digest.Secrets']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-cfg:digest'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.check_disable is not None:
                        return True

                    if self.hash is not None:
                        return True

                    if self.secrets is not None and self.secrets._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_cfg as meta
                    return meta._meta_table['L2Tp.Classes.Class_.Digest']['meta_info']


            class Ip(object):
                """
                IP TOS value
                
                .. attribute:: tos
                
                	IP TOS value (decimal)
                	**type**\:  int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'tunnel-l2tun-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.tos = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tunnel-l2tun-cfg:ip'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.tos is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_cfg as meta
                    return meta._meta_table['L2Tp.Classes.Class_.Ip']['meta_info']

            @property
            def _common_path(self):
                if self.class_name is None:
                    raise YPYModelError('Key property class_name is None')

                return '/Cisco-IOS-XR-tunnel-l2tun-cfg:l2tp/Cisco-IOS-XR-tunnel-l2tun-cfg:classes/Cisco-IOS-XR-tunnel-l2tun-cfg:class[Cisco-IOS-XR-tunnel-l2tun-cfg:class-name = ' + str(self.class_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.class_name is not None:
                    return True

                if self.authentication is not None:
                    return True

                if self.congestion_control is not None:
                    return True

                if self.digest is not None and self.digest._has_data():
                    return True

                if self.enable is not None:
                    return True

                if self.hello_interval is not None:
                    return True

                if self.hidden is not None:
                    return True

                if self.host_name is not None:
                    return True

                if self.ip is not None and self.ip._has_data():
                    return True

                if self.password is not None:
                    return True

                if self.receive_window is not None:
                    return True

                if self.retransmit is not None and self.retransmit._has_data():
                    return True

                if self.security is not None and self.security._has_data():
                    return True

                if self.timeout_no_user is not None:
                    return True

                if self.timeout_setup is not None:
                    return True

                if self.tunnel is not None and self.tunnel._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_cfg as meta
                return meta._meta_table['L2Tp.Classes.Class_']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-l2tun-cfg:l2tp/Cisco-IOS-XR-tunnel-l2tun-cfg:classes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.class_ is not None:
                for child_ref in self.class_:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_cfg as meta
            return meta._meta_table['L2Tp.Classes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-tunnel-l2tun-cfg:l2tp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.classes is not None and self.classes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_l2tun_cfg as meta
        return meta._meta_table['L2Tp']['meta_info']



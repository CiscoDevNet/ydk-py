""" Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-new\-dhcpv6d package configuration.

This module contains definitions
for the following management objects\:
  dhcpv6\: None

This YANG module augments the
  Cisco\-IOS\-XR\-subscriber\-infra\-tmplmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class InsertEnum(Enum):
    """
    InsertEnum

    Insert

    .. data:: LOCAL = 0

    	Insert locally generated/configured Interface

    	ID value

    .. data:: RECEIVED = 1

    	Insert received Interface ID value

    """

    LOCAL = 0

    RECEIVED = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
        return meta._meta_table['InsertEnum']



class Dhcpv6(object):
    """
    None
    
    .. attribute:: allow_duid_change
    
    	For BNG session, allow duid change for a client MAC
    	**type**\: :py:class:`Empty <ydk.types.Empty>`
    
    .. attribute:: _is_presence
    
    	Is present if this instance represents presence container else not
    	**type**\: bool
    
    .. attribute:: database
    
    	Enable DHCP binding database storage to file system
    	**type**\: :py:class:`Database <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Database>`
    
    .. attribute:: _is_presence
    
    	Is present if this instance represents presence container else not
    	**type**\: bool
    
    .. attribute:: enable
    
    	Enable None. Deletion of this object also causes deletion of all associated objects under DHCPv6
    	**type**\: :py:class:`Empty <ydk.types.Empty>`
    
    .. attribute:: _is_presence
    
    	Is present if this instance represents presence container else not
    	**type**\: bool
    
    .. attribute:: interfaces
    
    	Table of Interface
    	**type**\: :py:class:`Interfaces <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces>`
    
    .. attribute:: _is_presence
    
    	Is present if this instance represents presence container else not
    	**type**\: bool
    
    .. attribute:: profiles
    
    	Table of Profile
    	**type**\: :py:class:`Profiles <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles>`
    
    .. attribute:: _is_presence
    
    	Is present if this instance represents presence container else not
    	**type**\: bool
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'ipv6-new-dhcpv6d-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.allow_duid_change = None
        self.database = Dhcpv6.Database()
        self.database.parent = self
        self.enable = None
        self.interfaces = Dhcpv6.Interfaces()
        self.interfaces.parent = self
        self.profiles = Dhcpv6.Profiles()
        self.profiles.parent = self


    class Database(object):
        """
        Enable DHCP binding database storage to file
        system
        
        .. attribute:: full_write_interval
        
        	Full file write interval (default 10 minutes)
        	**type**\: int
        
        	**range:** 1..1440
        
        .. attribute:: incremental_write_interval
        
        	Incremental file write interval (default 1 minutes)
        	**type**\: int
        
        	**range:** 1..1440
        
        .. attribute:: proxy
        
        	Enable DHCP proxy binding database storage to file system
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: relay
        
        	Enable DHCP relay binding database storage to file system
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: server
        
        	Enable DHCP server binding database storage to file system
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        

        """

        _prefix = 'ipv6-new-dhcpv6d-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.full_write_interval = None
            self.incremental_write_interval = None
            self.proxy = None
            self.relay = None
            self.server = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:database'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.full_write_interval is not None:
                return True

            if self.incremental_write_interval is not None:
                return True

            if self.proxy is not None:
                return True

            if self.relay is not None:
                return True

            if self.server is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
            return meta._meta_table['Dhcpv6.Database']['meta_info']


    class Interfaces(object):
        """
        Table of Interface
        
        .. attribute:: interface
        
        	None
        	**type**\: list of :py:class:`Interface <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface>`
        
        

        """

        _prefix = 'ipv6-new-dhcpv6d-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.interface = YList()
            self.interface.parent = self
            self.interface.name = 'interface'


        class Interface(object):
            """
            None
            
            .. attribute:: interface_name
            
            	Interface to configure
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: pppoe
            
            	PPPoE subscriber interface
            	**type**\: :py:class:`Pppoe <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface.Pppoe>`
            
            .. attribute:: proxy
            
            	Assign a proxy profile to interface
            	**type**\: :py:class:`Proxy <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface.Proxy>`
            
            .. attribute:: relay
            
            	Assign a relay profile to interface
            	**type**\: :py:class:`Relay <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface.Relay>`
            
            .. attribute:: server
            
            	Assign a server profile to interface
            	**type**\: :py:class:`Server <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Interfaces.Interface.Server>`
            
            

            """

            _prefix = 'ipv6-new-dhcpv6d-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.pppoe = Dhcpv6.Interfaces.Interface.Pppoe()
                self.pppoe.parent = self
                self.proxy = Dhcpv6.Interfaces.Interface.Proxy()
                self.proxy.parent = self
                self.relay = Dhcpv6.Interfaces.Interface.Relay()
                self.relay.parent = self
                self.server = Dhcpv6.Interfaces.Interface.Server()
                self.server.parent = self


            class Pppoe(object):
                """
                PPPoE subscriber interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\: str
                
                	**range:** 0..64
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.profile = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:pppoe'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.profile is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                    return meta._meta_table['Dhcpv6.Interfaces.Interface.Pppoe']['meta_info']


            class Proxy(object):
                """
                Assign a proxy profile to interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\: str
                
                	**range:** 0..64
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.profile = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:proxy'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.profile is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                    return meta._meta_table['Dhcpv6.Interfaces.Interface.Proxy']['meta_info']


            class Relay(object):
                """
                Assign a relay profile to interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\: str
                
                	**range:** 0..64
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.profile = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:relay'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.profile is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                    return meta._meta_table['Dhcpv6.Interfaces.Interface.Relay']['meta_info']


            class Server(object):
                """
                Assign a server profile to interface
                
                .. attribute:: profile
                
                	Enter profile name
                	**type**\: str
                
                	**range:** 0..64
                
                

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.profile = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:server'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.profile is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                    return meta._meta_table['Dhcpv6.Interfaces.Interface.Server']['meta_info']

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYDataValidationError('Key property interface_name is None')

                return '/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:interfaces/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:interface[Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.interface_name is not None:
                    return True

                if self.pppoe is not None and self.pppoe._has_data():
                    return True

                if self.proxy is not None and self.proxy._has_data():
                    return True

                if self.relay is not None and self.relay._has_data():
                    return True

                if self.server is not None and self.server._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                return meta._meta_table['Dhcpv6.Interfaces.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.interface is not None:
                for child_ref in self.interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
            return meta._meta_table['Dhcpv6.Interfaces']['meta_info']


    class Profiles(object):
        """
        Table of Profile
        
        .. attribute:: profile
        
        	None
        	**type**\: list of :py:class:`Profile <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile>`
        
        

        """

        _prefix = 'ipv6-new-dhcpv6d-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.profile = YList()
            self.profile.parent = self
            self.profile.name = 'profile'


        class Profile(object):
            """
            None
            
            .. attribute:: profile_name
            
            	Profile name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: proxy
            
            	None
            	**type**\: :py:class:`Proxy <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy>`
            
            .. attribute:: relay
            
            	None
            	**type**\: :py:class:`Relay <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Relay>`
            
            .. attribute:: server
            
            	None
            	**type**\: :py:class:`Server <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server>`
            
            

            """

            _prefix = 'ipv6-new-dhcpv6d-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.profile_name = None
                self.proxy = None
                self.relay = None
                self.server = None


            class Proxy(object):
                """
                None
                
                .. attribute:: classes
                
                	Table of Class
                	**type**\: :py:class:`Classes <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Classes>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                .. attribute:: enable
                
                	Enable None. Deletion of this object also causes deletion of all associated objects under Proxy
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                .. attribute:: interfaces
                
                	Table of Interface
                	**type**\: :py:class:`Interfaces <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Interfaces>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                .. attribute:: link_address
                
                	IPv6 address to be filled in link\-address
                	**type**\: one of { str | str }
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                .. attribute:: relay
                
                	Specify relay configuration
                	**type**\: :py:class:`Relay <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Relay>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                .. attribute:: sessions
                
                	Change sessions configuration
                	**type**\: :py:class:`Sessions <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Sessions>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                .. attribute:: src_intf_name
                
                	Create or enter proxy profile Source Interface Name
                	**type**\: str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                .. attribute:: vrfs
                
                	VRF related configuration
                	**type**\: :py:class:`Vrfs <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Vrfs>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.classes = Dhcpv6.Profiles.Profile.Proxy.Classes()
                    self.classes.parent = self
                    self.enable = None
                    self.interfaces = Dhcpv6.Profiles.Profile.Proxy.Interfaces()
                    self.interfaces.parent = self
                    self.link_address = None
                    self.relay = Dhcpv6.Profiles.Profile.Proxy.Relay()
                    self.relay.parent = self
                    self.sessions = Dhcpv6.Profiles.Profile.Proxy.Sessions()
                    self.sessions.parent = self
                    self.src_intf_name = None
                    self.vrfs = Dhcpv6.Profiles.Profile.Proxy.Vrfs()
                    self.vrfs.parent = self


                class Classes(object):
                    """
                    Table of Class
                    
                    .. attribute:: class_
                    
                    	None
                    	**type**\: list of :py:class:`Class <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Classes.Class>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.class_ = YList()
                        self.class_.parent = self
                        self.class_.name = 'class_'


                    class Class(object):
                        """
                        None
                        
                        .. attribute:: class_name
                        
                        	Class name
                        	**type**\: str
                        
                        	**range:** 0..128
                        
                        .. attribute:: helper_addresses
                        
                        	Table of HelperAddress
                        	**type**\: :py:class:`HelperAddresses <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses>`
                        
                        .. attribute:: link_address
                        
                        	IPv6 address to be filled in link\-address
                        	**type**\: one of { str | str }
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.class_name = None
                            self.helper_addresses = Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses()
                            self.helper_addresses.parent = self
                            self.link_address = None


                        class HelperAddresses(object):
                            """
                            Table of HelperAddress
                            
                            .. attribute:: helper_address
                            
                            	Specify the server helper address
                            	**type**\: list of :py:class:`HelperAddress <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses.HelperAddress>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.helper_address = YList()
                                self.helper_address.parent = self
                                self.helper_address.name = 'helper_address'


                            class HelperAddress(object):
                                """
                                Specify the server helper address
                                
                                .. attribute:: helper_address
                                
                                	Server address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: vrf_name
                                
                                	VRF name
                                	**type**\: str
                                
                                	**range:** 0..32
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.helper_address = None
                                    self.vrf_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.helper_address is None:
                                        raise YPYDataValidationError('Key property helper_address is None')
                                    if self.vrf_name is None:
                                        raise YPYDataValidationError('Key property vrf_name is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:helper-address[Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:helper-address = ' + str(self.helper_address) + '][Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:vrf-name = ' + str(self.vrf_name) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.helper_address is not None:
                                        return True

                                    if self.vrf_name is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                    return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses.HelperAddress']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:helper-addresses'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.helper_address is not None:
                                    for child_ref in self.helper_address:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Classes.Class.HelperAddresses']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.class_name is None:
                                raise YPYDataValidationError('Key property class_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:class[Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:class-name = ' + str(self.class_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.class_name is not None:
                                return True

                            if self.helper_addresses is not None and self.helper_addresses._has_data():
                                return True

                            if self.link_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                            return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Classes.Class']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:classes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.class_ is not None:
                            for child_ref in self.class_:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Classes']['meta_info']


                class Interfaces(object):
                    """
                    Table of Interface
                    
                    .. attribute:: interface
                    
                    	None
                    	**type**\: list of :py:class:`Interface <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface = YList()
                        self.interface.parent = self
                        self.interface.name = 'interface'


                    class Interface(object):
                        """
                        None
                        
                        .. attribute:: interface_name
                        
                        	Interface to configure
                        	**type**\: str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: interface_id
                        
                        	Physical interface ID
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = None
                            self.interface_id = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.interface_name is None:
                                raise YPYDataValidationError('Key property interface_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:interface[Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:interface-name = ' + str(self.interface_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.interface_name is not None:
                                return True

                            if self.interface_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                            return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Interfaces.Interface']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:interfaces'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.interface is not None:
                            for child_ref in self.interface:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Interfaces']['meta_info']


                class Relay(object):
                    """
                    Specify relay configuration
                    
                    .. attribute:: option
                    
                    	Specify relay option configuration
                    	**type**\: :py:class:`Option <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Relay.Option>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.option = Dhcpv6.Profiles.Profile.Proxy.Relay.Option()
                        self.option.parent = self


                    class Option(object):
                        """
                        Specify relay option configuration
                        
                        .. attribute:: interface_id
                        
                        	Interface Id option
                        	**type**\: :py:class:`InterfaceId <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId>`
                        
                        .. attribute:: remote_id
                        
                        	Enter remote\-id value
                        	**type**\: str
                        
                        	**range:** 0..256
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface_id = Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId()
                            self.interface_id.parent = self
                            self.remote_id = None


                        class InterfaceId(object):
                            """
                            Interface Id option
                            
                            .. attribute:: insert
                            
                            	Configure InterfaceID insert type
                            	**type**\: :py:class:`InsertEnum <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.InsertEnum>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.insert = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:interface-id'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.insert is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Relay.Option.InterfaceId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:option'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.interface_id is not None and self.interface_id._has_data():
                                return True

                            if self.remote_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                            return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Relay.Option']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:relay'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.option is not None and self.option._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Relay']['meta_info']


                class Sessions(object):
                    """
                    Change sessions configuration
                    
                    .. attribute:: mac
                    
                    	Throttle DHCP sessions based on MAC address
                    	**type**\: :py:class:`Mac <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.mac = Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac()
                        self.mac.parent = self


                    class Mac(object):
                        """
                        Throttle DHCP sessions based on MAC address
                        
                        .. attribute:: throttle
                        
                        	Throttle DHCP sessions from any one MAC address
                        	**type**\: :py:class:`Throttle <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.throttle = Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle()
                            self.throttle.parent = self


                        class Throttle(object):
                            """
                            Throttle DHCP sessions from any one MAC
                            address
                            
                            .. attribute:: block
                            
                            	Throttle blocking period (in secs)
                            	**type**\: int
                            
                            	**range:** 1..100
                            
                            .. attribute:: limit
                            
                            	Number of solicits at which to throttle
                            	**type**\: int
                            
                            	**range:** 1..65535
                            
                            .. attribute:: request
                            
                            	Throttle request period (in secs)
                            	**type**\: int
                            
                            	**range:** 1..100
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.block = None
                                self.limit = None
                                self.request = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:throttle'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.block is not None:
                                    return True

                                if self.limit is not None:
                                    return True

                                if self.request is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac.Throttle']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:mac'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.throttle is not None and self.throttle._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                            return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Sessions.Mac']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:sessions'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.mac is not None and self.mac._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Sessions']['meta_info']


                class Vrfs(object):
                    """
                    VRF related configuration
                    
                    .. attribute:: vrf
                    
                    	IPv6 DHCP proxy VRF name
                    	**type**\: list of :py:class:`Vrf <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.vrf = YList()
                        self.vrf.parent = self
                        self.vrf.name = 'vrf'


                    class Vrf(object):
                        """
                        IPv6 DHCP proxy VRF name
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: helper_addresses
                        
                        	Table of HelperAddress
                        	**type**\: :py:class:`HelperAddresses <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.vrf_name = None
                            self.helper_addresses = Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses()
                            self.helper_addresses.parent = self


                        class HelperAddresses(object):
                            """
                            Table of HelperAddress
                            
                            .. attribute:: helper_address
                            
                            	DHCPv6 Helper Address
                            	**type**\: list of :py:class:`HelperAddress <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress>`
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.helper_address = YList()
                                self.helper_address.parent = self
                                self.helper_address.name = 'helper_address'


                            class HelperAddress(object):
                                """
                                DHCPv6 Helper Address
                                
                                .. attribute:: helper_address
                                
                                	DHCPv6 Helper Address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: any_out_interface
                                
                                	DHCPv6 HelperAddress Output Interface
                                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                                
                                .. attribute:: out_interface
                                
                                	DHCPv6 HelperAddress Specific Output Interface
                                	**type**\: str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                

                                """

                                _prefix = 'ipv6-new-dhcpv6d-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.helper_address = None
                                    self.any_out_interface = None
                                    self.out_interface = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.helper_address is None:
                                        raise YPYDataValidationError('Key property helper_address is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:helper-address[Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:helper-address = ' + str(self.helper_address) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.helper_address is not None:
                                        return True

                                    if self.any_out_interface is not None:
                                        return True

                                    if self.out_interface is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                    return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:helper-addresses'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.helper_address is not None:
                                    for child_ref in self.helper_address:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf.HelperAddresses']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.vrf_name is None:
                                raise YPYDataValidationError('Key property vrf_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:vrf[Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:vrf-name = ' + str(self.vrf_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.vrf_name is not None:
                                return True

                            if self.helper_addresses is not None and self.helper_addresses._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                            return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Vrfs.Vrf']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:vrfs'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.vrf is not None:
                            for child_ref in self.vrf:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy.Vrfs']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:proxy'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.classes is not None and self.classes._has_data():
                        return True

                    if self.enable is not None:
                        return True

                    if self.interfaces is not None and self.interfaces._has_data():
                        return True

                    if self.link_address is not None:
                        return True

                    if self.relay is not None and self.relay._has_data():
                        return True

                    if self.sessions is not None and self.sessions._has_data():
                        return True

                    if self.src_intf_name is not None:
                        return True

                    if self.vrfs is not None and self.vrfs._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                    return meta._meta_table['Dhcpv6.Profiles.Profile.Proxy']['meta_info']


            class Relay(object):
                """
                None
                
                .. attribute:: enable
                
                	Enable None. Deletion of this object also causes deletion of all associated objects under Relay
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                .. attribute:: helper_addresses
                
                	Table of HelperAddress
                	**type**\: :py:class:`HelperAddresses <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Relay.HelperAddresses>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                .. attribute:: iana_route_add
                
                	Enable route addition for IANA
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.enable = None
                    self.helper_addresses = Dhcpv6.Profiles.Profile.Relay.HelperAddresses()
                    self.helper_addresses.parent = self
                    self.iana_route_add = None


                class HelperAddresses(object):
                    """
                    Table of HelperAddress
                    
                    .. attribute:: helper_address
                    
                    	Specify the server helper address
                    	**type**\: list of :py:class:`HelperAddress <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.helper_address = YList()
                        self.helper_address.parent = self
                        self.helper_address.name = 'helper_address'


                    class HelperAddress(object):
                        """
                        Specify the server helper address
                        
                        .. attribute:: helper_address
                        
                        	Server Global unicast address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\: str
                        
                        	**range:** 0..32
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.helper_address = None
                            self.vrf_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.helper_address is None:
                                raise YPYDataValidationError('Key property helper_address is None')
                            if self.vrf_name is None:
                                raise YPYDataValidationError('Key property vrf_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:helper-address[Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:helper-address = ' + str(self.helper_address) + '][Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:vrf-name = ' + str(self.vrf_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.helper_address is not None:
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                            return meta._meta_table['Dhcpv6.Profiles.Profile.Relay.HelperAddresses.HelperAddress']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:helper-addresses'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.helper_address is not None:
                            for child_ref in self.helper_address:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Relay.HelperAddresses']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:relay'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.enable is not None:
                        return True

                    if self.helper_addresses is not None and self.helper_addresses._has_data():
                        return True

                    if self.iana_route_add is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                    return meta._meta_table['Dhcpv6.Profiles.Profile.Relay']['meta_info']


            class Server(object):
                """
                None
                
                .. attribute:: address_pool
                
                	Address pool name
                	**type**\: str
                
                	**range:** 0..64
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                .. attribute:: aftr_name
                
                	AFTR name
                	**type**\: str
                
                	**range:** 0..64
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                .. attribute:: classes
                
                	Table of Class
                	**type**\: :py:class:`Classes <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Classes>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                .. attribute:: dns_servers
                
                	DNS servers
                	**type**\: :py:class:`DnsServers <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.DnsServers>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                .. attribute:: domain_name
                
                	Domain name
                	**type**\: str
                
                	**range:** 0..64
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                .. attribute:: enable
                
                	Enable None. Deletion of this object also causes deletion of all associated objects under Server
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                .. attribute:: lease
                
                	lease
                	**type**\: :py:class:`Lease <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Lease>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                .. attribute:: preference
                
                	DHCP Server Preference
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                .. attribute:: prefix_pool
                
                	Prefix pool name
                	**type**\: str
                
                	**range:** 0..64
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                .. attribute:: rapid_commit
                
                	Allow RAPID Commit
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                .. attribute:: sessions
                
                	Change sessions configuration
                	**type**\: :py:class:`Sessions <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Sessions>`
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv6-new-dhcpv6d-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.address_pool = None
                    self.aftr_name = None
                    self.classes = Dhcpv6.Profiles.Profile.Server.Classes()
                    self.classes.parent = self
                    self.dns_servers = Dhcpv6.Profiles.Profile.Server.DnsServers()
                    self.dns_servers.parent = self
                    self.domain_name = None
                    self.enable = None
                    self.lease = Dhcpv6.Profiles.Profile.Server.Lease()
                    self.lease.parent = self
                    self.preference = None
                    self.prefix_pool = None
                    self.rapid_commit = None
                    self.sessions = Dhcpv6.Profiles.Profile.Server.Sessions()
                    self.sessions.parent = self


                class Classes(object):
                    """
                    Table of Class
                    
                    .. attribute:: class_
                    
                    	None
                    	**type**\: list of :py:class:`Class <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Classes.Class>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.class_ = YList()
                        self.class_.parent = self
                        self.class_.name = 'class_'


                    class Class(object):
                        """
                        None
                        
                        .. attribute:: class_name
                        
                        	class name
                        	**type**\: str
                        
                        	**range:** 0..128
                        
                        .. attribute:: address_pool
                        
                        	Address pool name
                        	**type**\: str
                        
                        	**range:** 0..64
                        
                        .. attribute:: dns_servers
                        
                        	DNS servers
                        	**type**\: :py:class:`DnsServers <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Classes.Class.DnsServers>`
                        
                        .. attribute:: domain_name
                        
                        	Domain name
                        	**type**\: str
                        
                        	**range:** 0..64
                        
                        .. attribute:: preference
                        
                        	DHCP Server Preference
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        .. attribute:: prefix_pool
                        
                        	Prefix pool name
                        	**type**\: str
                        
                        	**range:** 0..64
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.class_name = None
                            self.address_pool = None
                            self.dns_servers = Dhcpv6.Profiles.Profile.Server.Classes.Class.DnsServers()
                            self.dns_servers.parent = self
                            self.domain_name = None
                            self.preference = None
                            self.prefix_pool = None


                        class DnsServers(object):
                            """
                            DNS servers
                            
                            .. attribute:: dns_server
                            
                            	Server's IPv6 address
                            	**type**\: list of one of { list of str | list of str }
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.dns_server = []

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dns-servers'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.dns_server is not None:
                                    for child in self.dns_server:
                                        if child is not None:
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Classes.Class.DnsServers']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.class_name is None:
                                raise YPYDataValidationError('Key property class_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:class[Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:class-name = ' + str(self.class_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.class_name is not None:
                                return True

                            if self.address_pool is not None:
                                return True

                            if self.dns_servers is not None and self.dns_servers._has_data():
                                return True

                            if self.domain_name is not None:
                                return True

                            if self.preference is not None:
                                return True

                            if self.prefix_pool is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                            return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Classes.Class']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:classes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.class_ is not None:
                            for child_ref in self.class_:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Classes']['meta_info']


                class DnsServers(object):
                    """
                    DNS servers
                    
                    .. attribute:: dns_server
                    
                    	Server's IPv6 address
                    	**type**\: list of one of { list of str | list of str }
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.dns_server = []

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dns-servers'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.dns_server is not None:
                            for child in self.dns_server:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Server.DnsServers']['meta_info']


                class Lease(object):
                    """
                    lease
                    
                    .. attribute:: days
                    
                    	Days
                    	**type**\: int
                    
                    	**range:** 0..365
                    
                    .. attribute:: hours
                    
                    	Hours
                    	**type**\: int
                    
                    	**range:** 0..23
                    
                    .. attribute:: infinite
                    
                    	Set string
                    	**type**\: str
                    
                    .. attribute:: minutes
                    
                    	Minutes
                    	**type**\: int
                    
                    	**range:** 1..59
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.days = None
                        self.hours = None
                        self.infinite = None
                        self.minutes = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:lease'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.days is not None:
                            return True

                        if self.hours is not None:
                            return True

                        if self.infinite is not None:
                            return True

                        if self.minutes is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Lease']['meta_info']


                class Sessions(object):
                    """
                    Change sessions configuration
                    
                    .. attribute:: mac
                    
                    	Throttle DHCP sessions based on MAC address
                    	**type**\: :py:class:`Mac <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Sessions.Mac>`
                    
                    

                    """

                    _prefix = 'ipv6-new-dhcpv6d-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.mac = Dhcpv6.Profiles.Profile.Server.Sessions.Mac()
                        self.mac.parent = self


                    class Mac(object):
                        """
                        Throttle DHCP sessions based on MAC address
                        
                        .. attribute:: throttle
                        
                        	Throttle DHCP sessions from any one MAC address
                        	**type**\: :py:class:`Throttle <ydk.models.ipv6.Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg.Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle>`
                        
                        

                        """

                        _prefix = 'ipv6-new-dhcpv6d-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.throttle = Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle()
                            self.throttle.parent = self


                        class Throttle(object):
                            """
                            Throttle DHCP sessions from any one MAC
                            address
                            
                            .. attribute:: block
                            
                            	Throttle blocking period (in secs)
                            	**type**\: int
                            
                            	**range:** 1..100
                            
                            .. attribute:: limit
                            
                            	Number of solicits at which to throttle
                            	**type**\: int
                            
                            	**range:** 1..65535
                            
                            .. attribute:: request
                            
                            	Throttle request period (in secs)
                            	**type**\: int
                            
                            	**range:** 1..100
                            
                            

                            """

                            _prefix = 'ipv6-new-dhcpv6d-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.block = None
                                self.limit = None
                                self.request = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:throttle'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.block is not None:
                                    return True

                                if self.limit is not None:
                                    return True

                                if self.request is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                                return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Sessions.Mac.Throttle']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:mac'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.throttle is not None and self.throttle._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                            return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Sessions.Mac']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:sessions'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.mac is not None and self.mac._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                        return meta._meta_table['Dhcpv6.Profiles.Profile.Server.Sessions']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:server'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.address_pool is not None:
                        return True

                    if self.aftr_name is not None:
                        return True

                    if self.classes is not None and self.classes._has_data():
                        return True

                    if self.dns_servers is not None and self.dns_servers._has_data():
                        return True

                    if self.domain_name is not None:
                        return True

                    if self.enable is not None:
                        return True

                    if self.lease is not None and self.lease._has_data():
                        return True

                    if self.preference is not None:
                        return True

                    if self.prefix_pool is not None:
                        return True

                    if self.rapid_commit is not None:
                        return True

                    if self.sessions is not None and self.sessions._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                    return meta._meta_table['Dhcpv6.Profiles.Profile.Server']['meta_info']

            @property
            def _common_path(self):
                if self.profile_name is None:
                    raise YPYDataValidationError('Key property profile_name is None')

                return '/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:profiles/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:profile[Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:profile-name = ' + str(self.profile_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.profile_name is not None:
                    return True

                if self.proxy is not None and self.proxy._has_data():
                    return True

                if self.relay is not None and self.relay._has_data():
                    return True

                if self.server is not None and self.server._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
                return meta._meta_table['Dhcpv6.Profiles.Profile']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:profiles'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.profile is not None:
                for child_ref in self.profile:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
            return meta._meta_table['Dhcpv6.Profiles']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv6-new-dhcpv6d-cfg:dhcpv6'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.allow_duid_change is not None:
            return True

        if self.database is not None and self.database._has_data():
            return True

        if self.enable is not None:
            return True

        if self.interfaces is not None and self.interfaces._has_data():
            return True

        if self.profiles is not None and self.profiles._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_new_dhcpv6d_cfg as meta
        return meta._meta_table['Dhcpv6']['meta_info']



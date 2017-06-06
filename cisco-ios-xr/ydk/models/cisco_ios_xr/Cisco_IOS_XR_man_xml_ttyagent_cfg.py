""" Cisco_IOS_XR_man_xml_ttyagent_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR man\-xml\-ttyagent package configuration.

This module contains definitions
for the following management objects\:
  xr\-xml\: XML
  netconf\: netconf

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class XrXml(object):
    """
    XML
    
    .. attribute:: agent
    
    	XML agent
    	**type**\:   :py:class:`Agent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent>`
    
    

    """

    _prefix = 'man-xml-ttyagent-cfg'
    _revision = '2015-07-30'

    def __init__(self):
        self.agent = XrXml.Agent()
        self.agent.parent = self


    class Agent(object):
        """
        XML agent
        
        .. attribute:: default
        
        	XML default dedicated agent
        	**type**\:   :py:class:`Default <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Default>`
        
        .. attribute:: ssl
        
        	XML SSL agent
        	**type**\:   :py:class:`Ssl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Ssl>`
        
        .. attribute:: tty
        
        	XML TTY agent
        	**type**\:   :py:class:`Tty <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Tty>`
        
        

        """

        _prefix = 'man-xml-ttyagent-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.default = XrXml.Agent.Default()
            self.default.parent = self
            self.ssl = XrXml.Agent.Ssl()
            self.ssl.parent = self
            self.tty = XrXml.Agent.Tty()
            self.tty.parent = self


        class Default(object):
            """
            XML default dedicated agent
            
            .. attribute:: enable
            
            	Enable specified XML agent
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: ipv4_disable
            
            	TRUE to disable IPV4
            	**type**\:  bool
            
            .. attribute:: ipv6_enable
            
            	IPv6 Transport State
            	**type**\:  bool
            
            .. attribute:: iteration_size
            
            	Iterator size, in KBytes, of the XML response. Specify 0 to turn off the XML response iterator
            	**type**\:  int
            
            	**range:** 0..100000
            
            	**units**\: kilobyte
            
            	**default value**\: 48
            
            .. attribute:: session
            
            	Session attributes
            	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Default.Session>`
            
            .. attribute:: streaming_size
            
            	Streaming size, in KBytes, of the XML response
            	**type**\:  int
            
            	**range:** 1..100000
            
            	**units**\: kilobyte
            
            .. attribute:: throttle
            
            	XML agent throttling
            	**type**\:   :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Default.Throttle>`
            
            .. attribute:: vrfs
            
            	List of VRFs
            	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Default.Vrfs>`
            
            

            """

            _prefix = 'man-xml-ttyagent-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.enable = None
                self.ipv4_disable = None
                self.ipv6_enable = None
                self.iteration_size = None
                self.session = XrXml.Agent.Default.Session()
                self.session.parent = self
                self.streaming_size = None
                self.throttle = XrXml.Agent.Default.Throttle()
                self.throttle.parent = self
                self.vrfs = XrXml.Agent.Default.Vrfs()
                self.vrfs.parent = self


            class Session(object):
                """
                Session attributes
                
                .. attribute:: timeout
                
                	Timeout in minutes
                	**type**\:  int
                
                	**range:** 1..1440
                
                	**units**\: minute
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.timeout = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-cfg:agent/Cisco-IOS-XR-man-xml-ttyagent-cfg:default/Cisco-IOS-XR-man-xml-ttyagent-cfg:session'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.timeout is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_cfg as meta
                    return meta._meta_table['XrXml.Agent.Default.Session']['meta_info']


            class Throttle(object):
                """
                XML agent throttling
                
                .. attribute:: memory
                
                	Size of memory usage, in MBytes, per session
                	**type**\:  int
                
                	**range:** 100..600
                
                	**units**\: megabyte
                
                	**default value**\: 300
                
                .. attribute:: process_rate
                
                	Process rate in number of XML tags per second
                	**type**\:  int
                
                	**range:** 1000..30000
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.memory = None
                    self.process_rate = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-cfg:agent/Cisco-IOS-XR-man-xml-ttyagent-cfg:default/Cisco-IOS-XR-man-xml-ttyagent-cfg:throttle'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.memory is not None:
                        return True

                    if self.process_rate is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_cfg as meta
                    return meta._meta_table['XrXml.Agent.Default.Throttle']['meta_info']


            class Vrfs(object):
                """
                List of VRFs
                
                .. attribute:: vrf
                
                	A specific VRF
                	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Default.Vrfs.Vrf>`
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.vrf = YList()
                    self.vrf.parent = self
                    self.vrf.name = 'vrf'


                class Vrf(object):
                    """
                    A specific VRF
                    
                    .. attribute:: vrf_name  <key>
                    
                    	VRF name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: access_list
                    
                    	Access list for XML agent
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: ipv4_access_list
                    
                    	IPv4 Transport Access list for VRF
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: ipv6_access_list
                    
                    	IPv6 Transport Access list for VRF
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: shutdown
                    
                    	Shutdown default VRF. This is applicable only for VRF default
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'man-xml-ttyagent-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.vrf_name = None
                        self.access_list = None
                        self.ipv4_access_list = None
                        self.ipv6_access_list = None
                        self.shutdown = None

                    @property
                    def _common_path(self):
                        if self.vrf_name is None:
                            raise YPYModelError('Key property vrf_name is None')

                        return '/Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-cfg:agent/Cisco-IOS-XR-man-xml-ttyagent-cfg:default/Cisco-IOS-XR-man-xml-ttyagent-cfg:vrfs/Cisco-IOS-XR-man-xml-ttyagent-cfg:vrf[Cisco-IOS-XR-man-xml-ttyagent-cfg:vrf-name = ' + str(self.vrf_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.vrf_name is not None:
                            return True

                        if self.access_list is not None:
                            return True

                        if self.ipv4_access_list is not None:
                            return True

                        if self.ipv6_access_list is not None:
                            return True

                        if self.shutdown is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_cfg as meta
                        return meta._meta_table['XrXml.Agent.Default.Vrfs.Vrf']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-cfg:agent/Cisco-IOS-XR-man-xml-ttyagent-cfg:default/Cisco-IOS-XR-man-xml-ttyagent-cfg:vrfs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.vrf is not None:
                        for child_ref in self.vrf:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_cfg as meta
                    return meta._meta_table['XrXml.Agent.Default.Vrfs']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-cfg:agent/Cisco-IOS-XR-man-xml-ttyagent-cfg:default'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                if self.ipv4_disable is not None:
                    return True

                if self.ipv6_enable is not None:
                    return True

                if self.iteration_size is not None:
                    return True

                if self.session is not None and self.session._has_data():
                    return True

                if self.streaming_size is not None:
                    return True

                if self.throttle is not None and self.throttle._has_data():
                    return True

                if self.vrfs is not None and self.vrfs._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_cfg as meta
                return meta._meta_table['XrXml.Agent.Default']['meta_info']


        class Tty(object):
            """
            XML TTY agent
            
            .. attribute:: enable
            
            	Enable specified XML agent
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: iteration_size
            
            	Iterator size, in KBytes, of the XML response. Specify 0 to turn off the XML response iterator
            	**type**\:  int
            
            	**range:** 0..100000
            
            	**units**\: kilobyte
            
            	**default value**\: 48
            
            .. attribute:: session
            
            	Session attributes
            	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Tty.Session>`
            
            .. attribute:: streaming_size
            
            	Streaming size, in KBytes, of the XML response
            	**type**\:  int
            
            	**range:** 1..100000
            
            	**units**\: kilobyte
            
            .. attribute:: throttle
            
            	XML agent throttling
            	**type**\:   :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Tty.Throttle>`
            
            

            """

            _prefix = 'man-xml-ttyagent-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.enable = None
                self.iteration_size = None
                self.session = XrXml.Agent.Tty.Session()
                self.session.parent = self
                self.streaming_size = None
                self.throttle = XrXml.Agent.Tty.Throttle()
                self.throttle.parent = self


            class Session(object):
                """
                Session attributes
                
                .. attribute:: timeout
                
                	Timeout in minutes
                	**type**\:  int
                
                	**range:** 1..1440
                
                	**units**\: minute
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.timeout = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-cfg:agent/Cisco-IOS-XR-man-xml-ttyagent-cfg:tty/Cisco-IOS-XR-man-xml-ttyagent-cfg:session'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.timeout is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_cfg as meta
                    return meta._meta_table['XrXml.Agent.Tty.Session']['meta_info']


            class Throttle(object):
                """
                XML agent throttling
                
                .. attribute:: memory
                
                	Size of memory usage, in MBytes, per session
                	**type**\:  int
                
                	**range:** 100..600
                
                	**units**\: megabyte
                
                	**default value**\: 300
                
                .. attribute:: process_rate
                
                	Process rate in number of XML tags per second
                	**type**\:  int
                
                	**range:** 1000..30000
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.memory = None
                    self.process_rate = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-cfg:agent/Cisco-IOS-XR-man-xml-ttyagent-cfg:tty/Cisco-IOS-XR-man-xml-ttyagent-cfg:throttle'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.memory is not None:
                        return True

                    if self.process_rate is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_cfg as meta
                    return meta._meta_table['XrXml.Agent.Tty.Throttle']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-cfg:agent/Cisco-IOS-XR-man-xml-ttyagent-cfg:tty'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                if self.iteration_size is not None:
                    return True

                if self.session is not None and self.session._has_data():
                    return True

                if self.streaming_size is not None:
                    return True

                if self.throttle is not None and self.throttle._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_cfg as meta
                return meta._meta_table['XrXml.Agent.Tty']['meta_info']


        class Ssl(object):
            """
            XML SSL agent
            
            .. attribute:: enable
            
            	Enable specified XML agent
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: iteration_size
            
            	Iterator size, in KBytes, of the XML response. Specify 0 to turn off the XML response iterator
            	**type**\:  int
            
            	**range:** 0..100000
            
            	**units**\: kilobyte
            
            	**default value**\: 48
            
            .. attribute:: session
            
            	Session attributes
            	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Ssl.Session>`
            
            .. attribute:: streaming_size
            
            	Streaming size, in KBytes, of the XML response
            	**type**\:  int
            
            	**range:** 1..100000
            
            	**units**\: kilobyte
            
            .. attribute:: throttle
            
            	XML agent throttling
            	**type**\:   :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Ssl.Throttle>`
            
            .. attribute:: vrfs
            
            	List of VRFs
            	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Ssl.Vrfs>`
            
            

            """

            _prefix = 'man-xml-ttyagent-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.enable = None
                self.iteration_size = None
                self.session = XrXml.Agent.Ssl.Session()
                self.session.parent = self
                self.streaming_size = None
                self.throttle = XrXml.Agent.Ssl.Throttle()
                self.throttle.parent = self
                self.vrfs = XrXml.Agent.Ssl.Vrfs()
                self.vrfs.parent = self


            class Session(object):
                """
                Session attributes
                
                .. attribute:: timeout
                
                	Timeout in minutes
                	**type**\:  int
                
                	**range:** 1..1440
                
                	**units**\: minute
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.timeout = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-cfg:agent/Cisco-IOS-XR-man-xml-ttyagent-cfg:ssl/Cisco-IOS-XR-man-xml-ttyagent-cfg:session'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.timeout is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_cfg as meta
                    return meta._meta_table['XrXml.Agent.Ssl.Session']['meta_info']


            class Throttle(object):
                """
                XML agent throttling
                
                .. attribute:: memory
                
                	Size of memory usage, in MBytes, per session
                	**type**\:  int
                
                	**range:** 100..600
                
                	**units**\: megabyte
                
                	**default value**\: 300
                
                .. attribute:: process_rate
                
                	Process rate in number of XML tags per second
                	**type**\:  int
                
                	**range:** 1000..30000
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.memory = None
                    self.process_rate = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-cfg:agent/Cisco-IOS-XR-man-xml-ttyagent-cfg:ssl/Cisco-IOS-XR-man-xml-ttyagent-cfg:throttle'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.memory is not None:
                        return True

                    if self.process_rate is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_cfg as meta
                    return meta._meta_table['XrXml.Agent.Ssl.Throttle']['meta_info']


            class Vrfs(object):
                """
                List of VRFs
                
                .. attribute:: vrf
                
                	A specific VRF
                	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Ssl.Vrfs.Vrf>`
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.vrf = YList()
                    self.vrf.parent = self
                    self.vrf.name = 'vrf'


                class Vrf(object):
                    """
                    A specific VRF
                    
                    .. attribute:: vrf_name  <key>
                    
                    	VRF name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: access_list
                    
                    	Access list for XML agent
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: ipv4_access_list
                    
                    	IPv4 Transport Access list for VRF
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: ipv6_access_list
                    
                    	IPv6 Transport Access list for VRF
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: shutdown
                    
                    	Shutdown default VRF. This is applicable only for VRF default
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'man-xml-ttyagent-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.vrf_name = None
                        self.access_list = None
                        self.ipv4_access_list = None
                        self.ipv6_access_list = None
                        self.shutdown = None

                    @property
                    def _common_path(self):
                        if self.vrf_name is None:
                            raise YPYModelError('Key property vrf_name is None')

                        return '/Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-cfg:agent/Cisco-IOS-XR-man-xml-ttyagent-cfg:ssl/Cisco-IOS-XR-man-xml-ttyagent-cfg:vrfs/Cisco-IOS-XR-man-xml-ttyagent-cfg:vrf[Cisco-IOS-XR-man-xml-ttyagent-cfg:vrf-name = ' + str(self.vrf_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.vrf_name is not None:
                            return True

                        if self.access_list is not None:
                            return True

                        if self.ipv4_access_list is not None:
                            return True

                        if self.ipv6_access_list is not None:
                            return True

                        if self.shutdown is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_cfg as meta
                        return meta._meta_table['XrXml.Agent.Ssl.Vrfs.Vrf']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-cfg:agent/Cisco-IOS-XR-man-xml-ttyagent-cfg:ssl/Cisco-IOS-XR-man-xml-ttyagent-cfg:vrfs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.vrf is not None:
                        for child_ref in self.vrf:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_cfg as meta
                    return meta._meta_table['XrXml.Agent.Ssl.Vrfs']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-cfg:agent/Cisco-IOS-XR-man-xml-ttyagent-cfg:ssl'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                if self.iteration_size is not None:
                    return True

                if self.session is not None and self.session._has_data():
                    return True

                if self.streaming_size is not None:
                    return True

                if self.throttle is not None and self.throttle._has_data():
                    return True

                if self.vrfs is not None and self.vrfs._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_cfg as meta
                return meta._meta_table['XrXml.Agent.Ssl']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-cfg:agent'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.default is not None and self.default._has_data():
                return True

            if self.ssl is not None and self.ssl._has_data():
                return True

            if self.tty is not None and self.tty._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_cfg as meta
            return meta._meta_table['XrXml.Agent']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.agent is not None and self.agent._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_cfg as meta
        return meta._meta_table['XrXml']['meta_info']


class Netconf(object):
    """
    netconf
    
    .. attribute:: agent
    
    	XML agent
    	**type**\:   :py:class:`Agent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.Netconf.Agent>`
    
    

    """

    _prefix = 'man-xml-ttyagent-cfg'
    _revision = '2015-07-30'

    def __init__(self):
        self.agent = Netconf.Agent()
        self.agent.parent = self


    class Agent(object):
        """
        XML agent
        
        .. attribute:: tty
        
        	NETCONF agent over TTY
        	**type**\:   :py:class:`Tty <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.Netconf.Agent.Tty>`
        
        

        """

        _prefix = 'man-xml-ttyagent-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.tty = Netconf.Agent.Tty()
            self.tty.parent = self


        class Tty(object):
            """
            NETCONF agent over TTY
            
            .. attribute:: enable
            
            	Enable specified NETCONF agent
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: session
            
            	Session attributes
            	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.Netconf.Agent.Tty.Session>`
            
            .. attribute:: throttle
            
            	NETCONF agent throttling
            	**type**\:   :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.Netconf.Agent.Tty.Throttle>`
            
            

            """

            _prefix = 'man-xml-ttyagent-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.enable = None
                self.session = Netconf.Agent.Tty.Session()
                self.session.parent = self
                self.throttle = Netconf.Agent.Tty.Throttle()
                self.throttle.parent = self


            class Throttle(object):
                """
                NETCONF agent throttling
                
                .. attribute:: memory
                
                	Size of memory usage, in MBytes, per session
                	**type**\:  int
                
                	**range:** 100..600
                
                	**units**\: megabyte
                
                	**default value**\: 300
                
                .. attribute:: offload_memory
                
                	Size of memory usage, in MBytes, per session
                	**type**\:  int
                
                	**range:** 0..12000
                
                	**units**\: megabyte
                
                	**default value**\: 0
                
                .. attribute:: process_rate
                
                	Process rate in number of XML tags per second
                	**type**\:  int
                
                	**range:** 1000..30000
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.memory = None
                    self.offload_memory = None
                    self.process_rate = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-man-xml-ttyagent-cfg:netconf/Cisco-IOS-XR-man-xml-ttyagent-cfg:agent/Cisco-IOS-XR-man-xml-ttyagent-cfg:tty/Cisco-IOS-XR-man-xml-ttyagent-cfg:throttle'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.memory is not None:
                        return True

                    if self.offload_memory is not None:
                        return True

                    if self.process_rate is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_cfg as meta
                    return meta._meta_table['Netconf.Agent.Tty.Throttle']['meta_info']


            class Session(object):
                """
                Session attributes
                
                .. attribute:: timeout
                
                	Timeout in minutes
                	**type**\:  int
                
                	**range:** 1..1440
                
                	**units**\: minute
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.timeout = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-man-xml-ttyagent-cfg:netconf/Cisco-IOS-XR-man-xml-ttyagent-cfg:agent/Cisco-IOS-XR-man-xml-ttyagent-cfg:tty/Cisco-IOS-XR-man-xml-ttyagent-cfg:session'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.timeout is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_cfg as meta
                    return meta._meta_table['Netconf.Agent.Tty.Session']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-man-xml-ttyagent-cfg:netconf/Cisco-IOS-XR-man-xml-ttyagent-cfg:agent/Cisco-IOS-XR-man-xml-ttyagent-cfg:tty'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                if self.session is not None and self.session._has_data():
                    return True

                if self.throttle is not None and self.throttle._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_cfg as meta
                return meta._meta_table['Netconf.Agent.Tty']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-man-xml-ttyagent-cfg:netconf/Cisco-IOS-XR-man-xml-ttyagent-cfg:agent'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.tty is not None and self.tty._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_cfg as meta
            return meta._meta_table['Netconf.Agent']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-man-xml-ttyagent-cfg:netconf'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.agent is not None and self.agent._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_cfg as meta
        return meta._meta_table['Netconf']['meta_info']



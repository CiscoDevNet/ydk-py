""" Cisco_IOS_XR_traceroute_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ping action package configuration.

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class TracerouteRpc(object):
    """
    Trace route to destination
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.TracerouteRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.TracerouteRpc.Output>`
    
    

    """

    _prefix = 'traceroute-act'
    _revision = '2016-09-28'

    def __init__(self):
        self.input = TracerouteRpc.Input()
        self.input.parent = self
        self.output = TracerouteRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: destination
        
        	
        	**type**\:   :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.TracerouteRpc.Input.Destination>`
        
        .. attribute:: ipv4
        
        	
        	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.TracerouteRpc.Input.Ipv4>`
        
        .. attribute:: ipv6
        
        	
        	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.TracerouteRpc.Input.Ipv6>`
        
        

        """

        _prefix = 'traceroute-act'
        _revision = '2016-09-28'

        def __init__(self):
            self.parent = None
            self.destination = TracerouteRpc.Input.Destination()
            self.destination.parent = self
            self.ipv4 = TracerouteRpc.Input.Ipv4()
            self.ipv4.parent = self
            self.ipv6 = TracerouteRpc.Input.Ipv6()
            self.ipv6.parent = self


        class Destination(object):
            """
            
            
            .. attribute:: destination
            
            	Destination address or hostname
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: max_ttl
            
            	maximum time to live
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 30
            
            .. attribute:: min_ttl
            
            	minimum time to live
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 1
            
            .. attribute:: numeric
            
            	Numeric display only
            	**type**\:  bool
            
            .. attribute:: outgoing_interface
            
            	Outgoing interface, needed in case of traceroute to link local address
            	**type**\:  str
            
            .. attribute:: port
            
            	Port numbe
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: priority
            
            	Priority of hte packet
            	**type**\:  int
            
            	**range:** 0..15
            
            .. attribute:: probe
            
            	Probe count
            	**type**\:  int
            
            	**range:** 1..64
            
            	**default value**\: 3
            
            .. attribute:: source
            
            	Source address or interface
            	**type**\:  str
            
            .. attribute:: timeout
            
            	Timeout in seconds
            	**type**\:  int
            
            	**range:** 0..36
            
            	**default value**\: 3
            
            .. attribute:: verbose
            
            	verbose output
            	**type**\:  bool
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'traceroute-act'
            _revision = '2016-09-28'

            def __init__(self):
                self.parent = None
                self.destination = None
                self.max_ttl = None
                self.min_ttl = None
                self.numeric = None
                self.outgoing_interface = None
                self.port = None
                self.priority = None
                self.probe = None
                self.source = None
                self.timeout = None
                self.verbose = None
                self.vrf_name = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-traceroute-act:traceroute/Cisco-IOS-XR-traceroute-act:input/Cisco-IOS-XR-traceroute-act:destination'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if self.destination is not None:
                    return True

                if self.max_ttl is not None:
                    return True

                if self.min_ttl is not None:
                    return True

                if self.numeric is not None:
                    return True

                if self.outgoing_interface is not None:
                    return True

                if self.port is not None:
                    return True

                if self.priority is not None:
                    return True

                if self.probe is not None:
                    return True

                if self.source is not None:
                    return True

                if self.timeout is not None:
                    return True

                if self.verbose is not None:
                    return True

                if self.vrf_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                return meta._meta_table['TracerouteRpc.Input.Destination']['meta_info']


        class Ipv4(object):
            """
            
            
            .. attribute:: destination
            
            	Destination address or hostname
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: max_ttl
            
            	maximum time to live
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 30
            
            .. attribute:: min_ttl
            
            	minimum time to live
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 1
            
            .. attribute:: numeric
            
            	Numeric display only
            	**type**\:  bool
            
            .. attribute:: port
            
            	Port numbe
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: probe
            
            	Probe count
            	**type**\:  int
            
            	**range:** 1..64
            
            	**default value**\: 3
            
            .. attribute:: source
            
            	Source address or interface
            	**type**\:  str
            
            .. attribute:: timeout
            
            	Timeout in seconds
            	**type**\:  int
            
            	**range:** 0..36
            
            	**default value**\: 3
            
            .. attribute:: verbose
            
            	verbose output
            	**type**\:  bool
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'traceroute-act'
            _revision = '2016-09-28'

            def __init__(self):
                self.parent = None
                self.destination = None
                self.max_ttl = None
                self.min_ttl = None
                self.numeric = None
                self.port = None
                self.probe = None
                self.source = None
                self.timeout = None
                self.verbose = None
                self.vrf_name = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-traceroute-act:traceroute/Cisco-IOS-XR-traceroute-act:input/Cisco-IOS-XR-traceroute-act:ipv4'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if self.destination is not None:
                    return True

                if self.max_ttl is not None:
                    return True

                if self.min_ttl is not None:
                    return True

                if self.numeric is not None:
                    return True

                if self.port is not None:
                    return True

                if self.probe is not None:
                    return True

                if self.source is not None:
                    return True

                if self.timeout is not None:
                    return True

                if self.verbose is not None:
                    return True

                if self.vrf_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                return meta._meta_table['TracerouteRpc.Input.Ipv4']['meta_info']


        class Ipv6(object):
            """
            
            
            .. attribute:: destination
            
            	Destination address or hostname
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: max_ttl
            
            	maximum time to live
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 30
            
            .. attribute:: min_ttl
            
            	minimum time to live
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 1
            
            .. attribute:: numeric
            
            	Numeric display only
            	**type**\:  bool
            
            .. attribute:: outgoing_interface
            
            	Outgoing interface, needed in case of traceroute to link local address
            	**type**\:  str
            
            .. attribute:: port
            
            	Port numbe
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: priority
            
            	Priority of hte packet
            	**type**\:  int
            
            	**range:** 0..15
            
            .. attribute:: probe
            
            	Probe count
            	**type**\:  int
            
            	**range:** 1..64
            
            	**default value**\: 3
            
            .. attribute:: source
            
            	Source address or interface
            	**type**\:  str
            
            .. attribute:: timeout
            
            	Timeout in seconds
            	**type**\:  int
            
            	**range:** 0..36
            
            	**default value**\: 3
            
            .. attribute:: verbose
            
            	verbose output
            	**type**\:  bool
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'traceroute-act'
            _revision = '2016-09-28'

            def __init__(self):
                self.parent = None
                self.destination = None
                self.max_ttl = None
                self.min_ttl = None
                self.numeric = None
                self.outgoing_interface = None
                self.port = None
                self.priority = None
                self.probe = None
                self.source = None
                self.timeout = None
                self.verbose = None
                self.vrf_name = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-traceroute-act:traceroute/Cisco-IOS-XR-traceroute-act:input/Cisco-IOS-XR-traceroute-act:ipv6'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if self.destination is not None:
                    return True

                if self.max_ttl is not None:
                    return True

                if self.min_ttl is not None:
                    return True

                if self.numeric is not None:
                    return True

                if self.outgoing_interface is not None:
                    return True

                if self.port is not None:
                    return True

                if self.priority is not None:
                    return True

                if self.probe is not None:
                    return True

                if self.source is not None:
                    return True

                if self.timeout is not None:
                    return True

                if self.verbose is not None:
                    return True

                if self.vrf_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                return meta._meta_table['TracerouteRpc.Input.Ipv6']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-traceroute-act:traceroute/Cisco-IOS-XR-traceroute-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.destination is not None and self.destination._has_data():
                return True

            if self.ipv4 is not None and self.ipv4._has_data():
                return True

            if self.ipv6 is not None and self.ipv6._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
            return meta._meta_table['TracerouteRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: traceroute_response
        
        	
        	**type**\:   :py:class:`TracerouteResponse <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.TracerouteRpc.Output.TracerouteResponse>`
        
        

        """

        _prefix = 'traceroute-act'
        _revision = '2016-09-28'

        def __init__(self):
            self.parent = None
            self.traceroute_response = TracerouteRpc.Output.TracerouteResponse()
            self.traceroute_response.parent = self


        class TracerouteResponse(object):
            """
            
            
            .. attribute:: ipv4
            
            	
            	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.TracerouteRpc.Output.TracerouteResponse.Ipv4>`
            
            .. attribute:: ipv6
            
            	
            	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.TracerouteRpc.Output.TracerouteResponse.Ipv6>`
            
            

            """

            _prefix = 'traceroute-act'
            _revision = '2016-09-28'

            def __init__(self):
                self.parent = None
                self.ipv4 = TracerouteRpc.Output.TracerouteResponse.Ipv4()
                self.ipv4.parent = self
                self.ipv6 = TracerouteRpc.Output.TracerouteResponse.Ipv6()
                self.ipv6.parent = self


            class Ipv4(object):
                """
                
                
                .. attribute:: destination
                
                	Destination address or hostname
                	**type**\:  str
                
                .. attribute:: hops
                
                	
                	**type**\: list of    :py:class:`Hops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.TracerouteRpc.Output.TracerouteResponse.Ipv4.Hops>`
                
                .. attribute:: verbose_output
                
                	Verbose output
                	**type**\:  str
                
                

                """

                _prefix = 'traceroute-act'
                _revision = '2016-09-28'

                def __init__(self):
                    self.parent = None
                    self.destination = None
                    self.hops = YList()
                    self.hops.parent = self
                    self.hops.name = 'hops'
                    self.verbose_output = None


                class Hops(object):
                    """
                    
                    
                    .. attribute:: hop_index  <key>
                    
                    	Index of the hop
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hop_address
                    
                    	Address of the hop
                    	**type**\:  str
                    
                    .. attribute:: hop_hostname
                    
                    	Hostname of the hop
                    	**type**\:  str
                    
                    .. attribute:: probes
                    
                    	
                    	**type**\: list of    :py:class:`Probes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.TracerouteRpc.Output.TracerouteResponse.Ipv4.Hops.Probes>`
                    
                    

                    """

                    _prefix = 'traceroute-act'
                    _revision = '2016-09-28'

                    def __init__(self):
                        self.parent = None
                        self.hop_index = None
                        self.hop_address = None
                        self.hop_hostname = None
                        self.probes = YList()
                        self.probes.parent = self
                        self.probes.name = 'probes'


                    class Probes(object):
                        """
                        
                        
                        .. attribute:: probe_index  <key>
                        
                        	Index of the probe
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: delta_time
                        
                        	Delta time in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hop_address
                        
                        	Address of the hop
                        	**type**\:  str
                        
                        .. attribute:: hop_hostname
                        
                        	Hostname of the hop
                        	**type**\:  str
                        
                        .. attribute:: result
                        
                        	Response for each probe
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'traceroute-act'
                        _revision = '2016-09-28'

                        def __init__(self):
                            self.parent = None
                            self.probe_index = None
                            self.delta_time = None
                            self.hop_address = None
                            self.hop_hostname = None
                            self.result = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.probe_index is None:
                                raise YPYModelError('Key property probe_index is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-traceroute-act:probes[Cisco-IOS-XR-traceroute-act:probe-index = ' + str(self.probe_index) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            if self.parent is None:
                                raise YPYError('Parent reference is needed to determine if entity has configuration data')
                            return self.parent.is_config()

                        def _has_data(self):
                            if self.probe_index is not None:
                                return True

                            if self.delta_time is not None:
                                return True

                            if self.hop_address is not None:
                                return True

                            if self.hop_hostname is not None:
                                return True

                            if self.result is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                            return meta._meta_table['TracerouteRpc.Output.TracerouteResponse.Ipv4.Hops.Probes']['meta_info']

                    @property
                    def _common_path(self):
                        if self.hop_index is None:
                            raise YPYModelError('Key property hop_index is None')

                        return '/Cisco-IOS-XR-traceroute-act:traceroute/Cisco-IOS-XR-traceroute-act:output/Cisco-IOS-XR-traceroute-act:traceroute-response/Cisco-IOS-XR-traceroute-act:ipv4/Cisco-IOS-XR-traceroute-act:hops[Cisco-IOS-XR-traceroute-act:hop-index = ' + str(self.hop_index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        if self.parent is None:
                            raise YPYError('Parent reference is needed to determine if entity has configuration data')
                        return self.parent.is_config()

                    def _has_data(self):
                        if self.hop_index is not None:
                            return True

                        if self.hop_address is not None:
                            return True

                        if self.hop_hostname is not None:
                            return True

                        if self.probes is not None:
                            for child_ref in self.probes:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                        return meta._meta_table['TracerouteRpc.Output.TracerouteResponse.Ipv4.Hops']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-traceroute-act:traceroute/Cisco-IOS-XR-traceroute-act:output/Cisco-IOS-XR-traceroute-act:traceroute-response/Cisco-IOS-XR-traceroute-act:ipv4'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    if self.parent is None:
                        raise YPYError('Parent reference is needed to determine if entity has configuration data')
                    return self.parent.is_config()

                def _has_data(self):
                    if self.destination is not None:
                        return True

                    if self.hops is not None:
                        for child_ref in self.hops:
                            if child_ref._has_data():
                                return True

                    if self.verbose_output is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                    return meta._meta_table['TracerouteRpc.Output.TracerouteResponse.Ipv4']['meta_info']


            class Ipv6(object):
                """
                
                
                .. attribute:: destination
                
                	Destination address or hostname
                	**type**\:  str
                
                .. attribute:: hops
                
                	
                	**type**\: list of    :py:class:`Hops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.TracerouteRpc.Output.TracerouteResponse.Ipv6.Hops>`
                
                .. attribute:: verbose_output
                
                	Verbose output
                	**type**\:  str
                
                

                """

                _prefix = 'traceroute-act'
                _revision = '2016-09-28'

                def __init__(self):
                    self.parent = None
                    self.destination = None
                    self.hops = YList()
                    self.hops.parent = self
                    self.hops.name = 'hops'
                    self.verbose_output = None


                class Hops(object):
                    """
                    
                    
                    .. attribute:: hop_index  <key>
                    
                    	Index of the hop
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hop_address
                    
                    	Address of the hop
                    	**type**\:  str
                    
                    .. attribute:: hop_hostname
                    
                    	Hostname of the hop
                    	**type**\:  str
                    
                    .. attribute:: probes
                    
                    	
                    	**type**\: list of    :py:class:`Probes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.TracerouteRpc.Output.TracerouteResponse.Ipv6.Hops.Probes>`
                    
                    

                    """

                    _prefix = 'traceroute-act'
                    _revision = '2016-09-28'

                    def __init__(self):
                        self.parent = None
                        self.hop_index = None
                        self.hop_address = None
                        self.hop_hostname = None
                        self.probes = YList()
                        self.probes.parent = self
                        self.probes.name = 'probes'


                    class Probes(object):
                        """
                        
                        
                        .. attribute:: probe_index  <key>
                        
                        	Index of the probe
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: delta_time
                        
                        	Delta time in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hop_address
                        
                        	Address of the hop
                        	**type**\:  str
                        
                        .. attribute:: hop_hostname
                        
                        	Hostname of the hop
                        	**type**\:  str
                        
                        .. attribute:: result
                        
                        	Response for each probe
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'traceroute-act'
                        _revision = '2016-09-28'

                        def __init__(self):
                            self.parent = None
                            self.probe_index = None
                            self.delta_time = None
                            self.hop_address = None
                            self.hop_hostname = None
                            self.result = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.probe_index is None:
                                raise YPYModelError('Key property probe_index is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-traceroute-act:probes[Cisco-IOS-XR-traceroute-act:probe-index = ' + str(self.probe_index) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            if self.parent is None:
                                raise YPYError('Parent reference is needed to determine if entity has configuration data')
                            return self.parent.is_config()

                        def _has_data(self):
                            if self.probe_index is not None:
                                return True

                            if self.delta_time is not None:
                                return True

                            if self.hop_address is not None:
                                return True

                            if self.hop_hostname is not None:
                                return True

                            if self.result is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                            return meta._meta_table['TracerouteRpc.Output.TracerouteResponse.Ipv6.Hops.Probes']['meta_info']

                    @property
                    def _common_path(self):
                        if self.hop_index is None:
                            raise YPYModelError('Key property hop_index is None')

                        return '/Cisco-IOS-XR-traceroute-act:traceroute/Cisco-IOS-XR-traceroute-act:output/Cisco-IOS-XR-traceroute-act:traceroute-response/Cisco-IOS-XR-traceroute-act:ipv6/Cisco-IOS-XR-traceroute-act:hops[Cisco-IOS-XR-traceroute-act:hop-index = ' + str(self.hop_index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        if self.parent is None:
                            raise YPYError('Parent reference is needed to determine if entity has configuration data')
                        return self.parent.is_config()

                    def _has_data(self):
                        if self.hop_index is not None:
                            return True

                        if self.hop_address is not None:
                            return True

                        if self.hop_hostname is not None:
                            return True

                        if self.probes is not None:
                            for child_ref in self.probes:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                        return meta._meta_table['TracerouteRpc.Output.TracerouteResponse.Ipv6.Hops']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-traceroute-act:traceroute/Cisco-IOS-XR-traceroute-act:output/Cisco-IOS-XR-traceroute-act:traceroute-response/Cisco-IOS-XR-traceroute-act:ipv6'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    if self.parent is None:
                        raise YPYError('Parent reference is needed to determine if entity has configuration data')
                    return self.parent.is_config()

                def _has_data(self):
                    if self.destination is not None:
                        return True

                    if self.hops is not None:
                        for child_ref in self.hops:
                            if child_ref._has_data():
                                return True

                    if self.verbose_output is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                    return meta._meta_table['TracerouteRpc.Output.TracerouteResponse.Ipv6']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-traceroute-act:traceroute/Cisco-IOS-XR-traceroute-act:output/Cisco-IOS-XR-traceroute-act:traceroute-response'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if self.ipv4 is not None and self.ipv4._has_data():
                    return True

                if self.ipv6 is not None and self.ipv6._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
                return meta._meta_table['TracerouteRpc.Output.TracerouteResponse']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-traceroute-act:traceroute/Cisco-IOS-XR-traceroute-act:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.traceroute_response is not None and self.traceroute_response._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
            return meta._meta_table['TracerouteRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-traceroute-act:traceroute'

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_traceroute_act as meta
        return meta._meta_table['TracerouteRpc']['meta_info']



""" Cisco_IOS_XR_isis_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ISIS action package configuration.

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class ClearIsisProcessRpc(object):
    """
    Clear all IS\-IS data structures
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisProcessRpc.Input>`
    
    

    """

    _prefix = 'isis-act'
    _revision = '2016-06-30'

    def __init__(self):
        self.input = ClearIsisProcessRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: instance
        
        	Clear data from single IS\-IS instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisProcessRpc.Input.Instance>`
        
        .. attribute:: process
        
        	Clear all IS\-IS data structures
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'isis-act'
        _revision = '2016-06-30'

        def __init__(self):
            self.parent = None
            self.instance = ClearIsisProcessRpc.Input.Instance()
            self.instance.parent = self
            self.process = None


        class Instance(object):
            """
            Clear data from single IS\-IS instance
            
            .. attribute:: instance_identifier
            
            	IS\-IS process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'isis-act'
            _revision = '2016-06-30'

            def __init__(self):
                self.parent = None
                self.instance_identifier = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-isis-act:clear-isis-process/Cisco-IOS-XR-isis-act:input/Cisco-IOS-XR-isis-act:instance'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if self.instance_identifier is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_isis_act as meta
                return meta._meta_table['ClearIsisProcessRpc.Input.Instance']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-isis-act:clear-isis-process/Cisco-IOS-XR-isis-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.instance is not None and self.instance._has_data():
                return True

            if self.process is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_isis_act as meta
            return meta._meta_table['ClearIsisProcessRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-isis-act:clear-isis-process'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_isis_act as meta
        return meta._meta_table['ClearIsisProcessRpc']['meta_info']


class ClearIsisRouteRpc(object):
    """
    Clear IS\-IS routes
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisRouteRpc.Input>`
    
    

    """

    _prefix = 'isis-act'
    _revision = '2016-06-30'

    def __init__(self):
        self.input = ClearIsisRouteRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: instance
        
        	Clear data from single IS\-IS instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisRouteRpc.Input.Instance>`
        
        .. attribute:: route
        
        	Clear IS\-IS routes
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'isis-act'
        _revision = '2016-06-30'

        def __init__(self):
            self.parent = None
            self.instance = ClearIsisRouteRpc.Input.Instance()
            self.instance.parent = self
            self.route = None


        class Instance(object):
            """
            Clear data from single IS\-IS instance
            
            .. attribute:: instance_identifier
            
            	IS\-IS process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'isis-act'
            _revision = '2016-06-30'

            def __init__(self):
                self.parent = None
                self.instance_identifier = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-isis-act:clear-isis-route/Cisco-IOS-XR-isis-act:input/Cisco-IOS-XR-isis-act:instance'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if self.instance_identifier is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_isis_act as meta
                return meta._meta_table['ClearIsisRouteRpc.Input.Instance']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-isis-act:clear-isis-route/Cisco-IOS-XR-isis-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.instance is not None and self.instance._has_data():
                return True

            if self.route is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_isis_act as meta
            return meta._meta_table['ClearIsisRouteRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-isis-act:clear-isis-route'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_isis_act as meta
        return meta._meta_table['ClearIsisRouteRpc']['meta_info']


class ClearIsisStatRpc(object):
    """
    Clear IS\-IS protocol statistics
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisStatRpc.Input>`
    
    

    """

    _prefix = 'isis-act'
    _revision = '2016-06-30'

    def __init__(self):
        self.input = ClearIsisStatRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: instance
        
        	Clear data from single IS\-IS instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisStatRpc.Input.Instance>`
        
        .. attribute:: statistics
        
        	Clear IS\-IS protocol statistics
        	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisStatRpc.Input.Statistics>`
        
        

        """

        _prefix = 'isis-act'
        _revision = '2016-06-30'

        def __init__(self):
            self.parent = None
            self.instance = ClearIsisStatRpc.Input.Instance()
            self.instance.parent = self
            self.statistics = ClearIsisStatRpc.Input.Statistics()
            self.statistics.parent = self


        class Instance(object):
            """
            Clear data from single IS\-IS instance
            
            .. attribute:: instance_identifier
            
            	IS\-IS process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'isis-act'
            _revision = '2016-06-30'

            def __init__(self):
                self.parent = None
                self.instance_identifier = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-isis-act:clear-isis-stat/Cisco-IOS-XR-isis-act:input/Cisco-IOS-XR-isis-act:instance'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if self.instance_identifier is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_isis_act as meta
                return meta._meta_table['ClearIsisStatRpc.Input.Instance']['meta_info']


        class Statistics(object):
            """
            Clear IS\-IS protocol statistics
            
            .. attribute:: interface_name
            
            	Interface name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'isis-act'
            _revision = '2016-06-30'

            def __init__(self):
                self.parent = None
                self.interface_name = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-isis-act:clear-isis-stat/Cisco-IOS-XR-isis-act:input/Cisco-IOS-XR-isis-act:statistics'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if self.interface_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_isis_act as meta
                return meta._meta_table['ClearIsisStatRpc.Input.Statistics']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-isis-act:clear-isis-stat/Cisco-IOS-XR-isis-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.instance is not None and self.instance._has_data():
                return True

            if self.statistics is not None and self.statistics._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_isis_act as meta
            return meta._meta_table['ClearIsisStatRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-isis-act:clear-isis-stat'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_isis_act as meta
        return meta._meta_table['ClearIsisStatRpc']['meta_info']


class ClearIsisDistRpc(object):
    """
    Reset BGP\-LS topology distribution
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisDistRpc.Input>`
    
    

    """

    _prefix = 'isis-act'
    _revision = '2016-06-30'

    def __init__(self):
        self.input = ClearIsisDistRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: distribution
        
        	Reset BGP\-LS topology distribution
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: instance
        
        	Reset BGP\-LS topology from single IS\-IS instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisDistRpc.Input.Instance>`
        
        

        """

        _prefix = 'isis-act'
        _revision = '2016-06-30'

        def __init__(self):
            self.parent = None
            self.distribution = None
            self.instance = ClearIsisDistRpc.Input.Instance()
            self.instance.parent = self


        class Instance(object):
            """
            Reset BGP\-LS topology from single IS\-IS instance
            
            .. attribute:: instance_identifier
            
            	IS\-IS process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'isis-act'
            _revision = '2016-06-30'

            def __init__(self):
                self.parent = None
                self.instance_identifier = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-isis-act:clear-isis-dist/Cisco-IOS-XR-isis-act:input/Cisco-IOS-XR-isis-act:instance'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if self.instance_identifier is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_isis_act as meta
                return meta._meta_table['ClearIsisDistRpc.Input.Instance']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-isis-act:clear-isis-dist/Cisco-IOS-XR-isis-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.distribution is not None:
                return True

            if self.instance is not None and self.instance._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_isis_act as meta
            return meta._meta_table['ClearIsisDistRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-isis-act:clear-isis-dist'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_isis_act as meta
        return meta._meta_table['ClearIsisDistRpc']['meta_info']


class ClearIsisRpc(object):
    """
    Clear IS\-IS data structures
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisRpc.Input>`
    
    

    """

    _prefix = 'isis-act'
    _revision = '2016-06-30'

    def __init__(self):
        self.input = ClearIsisRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: instance
        
        	Clear data from single IS\-IS instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisRpc.Input.Instance>`
        
        .. attribute:: route
        
        	Clear IS\-IS routes
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: rt_type
        
        	Clear data for these route types
        	**type**\:   :py:class:`RtTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisRpc.Input.RtTypeEnum>`
        
        .. attribute:: topology
        
        	Topology table information
        	**type**\:  str
        
        

        """

        _prefix = 'isis-act'
        _revision = '2016-06-30'

        def __init__(self):
            self.parent = None
            self.instance = ClearIsisRpc.Input.Instance()
            self.instance.parent = self
            self.route = None
            self.rt_type = None
            self.topology = None

        class RtTypeEnum(Enum):
            """
            RtTypeEnum

            Clear data for these route types

            .. data:: AFI_ALL_MULTICAST = 0

            .. data:: AFI_ALL_SAFI_ALL = 1

            .. data:: AFI_ALL_UNICAST = 2

            .. data:: IPv4_MULTICAST = 3

            .. data:: IPv4_SAFI_ALL = 4

            .. data:: IPv4_UNICAST = 5

            .. data:: IPv6_MULTICAST = 6

            .. data:: IPv6_SAFI_ALL = 7

            .. data:: IPv6_UNICAST = 8

            """

            AFI_ALL_MULTICAST = 0

            AFI_ALL_SAFI_ALL = 1

            AFI_ALL_UNICAST = 2

            IPv4_MULTICAST = 3

            IPv4_SAFI_ALL = 4

            IPv4_UNICAST = 5

            IPv6_MULTICAST = 6

            IPv6_SAFI_ALL = 7

            IPv6_UNICAST = 8


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_isis_act as meta
                return meta._meta_table['ClearIsisRpc.Input.RtTypeEnum']



        class Instance(object):
            """
            Clear data from single IS\-IS instance
            
            .. attribute:: instance_identifier
            
            	IS\-IS process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'isis-act'
            _revision = '2016-06-30'

            def __init__(self):
                self.parent = None
                self.instance_identifier = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-isis-act:clear-isis/Cisco-IOS-XR-isis-act:input/Cisco-IOS-XR-isis-act:instance'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if self.instance_identifier is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_isis_act as meta
                return meta._meta_table['ClearIsisRpc.Input.Instance']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-isis-act:clear-isis/Cisco-IOS-XR-isis-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.instance is not None and self.instance._has_data():
                return True

            if self.route is not None:
                return True

            if self.rt_type is not None:
                return True

            if self.topology is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_isis_act as meta
            return meta._meta_table['ClearIsisRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-isis-act:clear-isis'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_isis_act as meta
        return meta._meta_table['ClearIsisRpc']['meta_info']



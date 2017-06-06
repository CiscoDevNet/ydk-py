""" Cisco_IOS_XR_ipv6_ospfv3_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR IPv6 OSPFv3 action package configuration.

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class ActOspfv3RoutesRpc(object):
    """
    Clear OSPFv3 Routes Table
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3RoutesRpc.Input>`
    
    

    """

    _prefix = 'ospfv3-act'
    _revision = '2016-09-14'

    def __init__(self):
        self.input = ActOspfv3RoutesRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPFv3 instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3RoutesRpc.Input.Instance>`
        
        .. attribute:: route
        
        	Clear OSPFv3 route table
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ospfv3-act'
        _revision = '2016-09-14'

        def __init__(self):
            self.parent = None
            self.instance = ActOspfv3RoutesRpc.Input.Instance()
            self.instance.parent = self
            self.route = None


        class Instance(object):
            """
            Clear data from OSPFv3 instance
            
            .. attribute:: instance_identifier
            
            	OSPFv3 process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospfv3-act'
            _revision = '2016-09-14'

            def __init__(self):
                self.parent = None
                self.instance_identifier = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-routes/Cisco-IOS-XR-ipv6-ospfv3-act:input/Cisco-IOS-XR-ipv6-ospfv3-act:instance'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
                return meta._meta_table['ActOspfv3RoutesRpc.Input.Instance']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-routes/Cisco-IOS-XR-ipv6-ospfv3-act:input'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
            return meta._meta_table['ActOspfv3RoutesRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-routes'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
        return meta._meta_table['ActOspfv3RoutesRpc']['meta_info']


class ActOspfv3RedistributionRpc(object):
    """
    Clear OSPFv3 Route Redistribution
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3RedistributionRpc.Input>`
    
    

    """

    _prefix = 'ospfv3-act'
    _revision = '2016-09-14'

    def __init__(self):
        self.input = ActOspfv3RedistributionRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPFv3 instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3RedistributionRpc.Input.Instance>`
        
        .. attribute:: redistribution
        
        	Clear OSPFv3 Route Redistribution
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ospfv3-act'
        _revision = '2016-09-14'

        def __init__(self):
            self.parent = None
            self.instance = ActOspfv3RedistributionRpc.Input.Instance()
            self.instance.parent = self
            self.redistribution = None


        class Instance(object):
            """
            Clear data from OSPFv3 instance
            
            .. attribute:: instance_identifier
            
            	OSPFv3 process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospfv3-act'
            _revision = '2016-09-14'

            def __init__(self):
                self.parent = None
                self.instance_identifier = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-redistribution/Cisco-IOS-XR-ipv6-ospfv3-act:input/Cisco-IOS-XR-ipv6-ospfv3-act:instance'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
                return meta._meta_table['ActOspfv3RedistributionRpc.Input.Instance']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-redistribution/Cisco-IOS-XR-ipv6-ospfv3-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.instance is not None and self.instance._has_data():
                return True

            if self.redistribution is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
            return meta._meta_table['ActOspfv3RedistributionRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-redistribution'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
        return meta._meta_table['ActOspfv3RedistributionRpc']['meta_info']


class ActOspfv3ProcessRpc(object):
    """
    Reset OSPFv3 Process
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3ProcessRpc.Input>`
    
    

    """

    _prefix = 'ospfv3-act'
    _revision = '2016-09-14'

    def __init__(self):
        self.input = ActOspfv3ProcessRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPFv3 instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3ProcessRpc.Input.Instance>`
        
        .. attribute:: process
        
        	Reset OSPFv3 process
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ospfv3-act'
        _revision = '2016-09-14'

        def __init__(self):
            self.parent = None
            self.instance = ActOspfv3ProcessRpc.Input.Instance()
            self.instance.parent = self
            self.process = None


        class Instance(object):
            """
            Clear data from OSPFv3 instance
            
            .. attribute:: instance_identifier
            
            	OSPFv3 process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospfv3-act'
            _revision = '2016-09-14'

            def __init__(self):
                self.parent = None
                self.instance_identifier = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-process/Cisco-IOS-XR-ipv6-ospfv3-act:input/Cisco-IOS-XR-ipv6-ospfv3-act:instance'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
                return meta._meta_table['ActOspfv3ProcessRpc.Input.Instance']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-process/Cisco-IOS-XR-ipv6-ospfv3-act:input'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
            return meta._meta_table['ActOspfv3ProcessRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-process'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
        return meta._meta_table['ActOspfv3ProcessRpc']['meta_info']


class ActOspfv3StatisticsNeighborRpc(object):
    """
    Neighbor statistics per neighbor id
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3StatisticsNeighborRpc.Input>`
    
    

    """

    _prefix = 'ospfv3-act'
    _revision = '2016-09-14'

    def __init__(self):
        self.input = ActOspfv3StatisticsNeighborRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPFv3 instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3StatisticsNeighborRpc.Input.Instance>`
        
        .. attribute:: neighbor
        
        	
        	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3StatisticsNeighborRpc.Input.Neighbor>`
        
        

        """

        _prefix = 'ospfv3-act'
        _revision = '2016-09-14'

        def __init__(self):
            self.parent = None
            self.instance = ActOspfv3StatisticsNeighborRpc.Input.Instance()
            self.instance.parent = self
            self.neighbor = ActOspfv3StatisticsNeighborRpc.Input.Neighbor()
            self.neighbor.parent = self


        class Instance(object):
            """
            Clear data from OSPFv3 instance
            
            .. attribute:: instance_identifier
            
            	OSPFv3 process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospfv3-act'
            _revision = '2016-09-14'

            def __init__(self):
                self.parent = None
                self.instance_identifier = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-statistics-neighbor/Cisco-IOS-XR-ipv6-ospfv3-act:input/Cisco-IOS-XR-ipv6-ospfv3-act:instance'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
                return meta._meta_table['ActOspfv3StatisticsNeighborRpc.Input.Instance']['meta_info']


        class Neighbor(object):
            """
            
            
            .. attribute:: interface_name
            
            	Interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: neighbor_id
            
            	Neighbor ID
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'ospfv3-act'
            _revision = '2016-09-14'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.neighbor_id = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-statistics-neighbor/Cisco-IOS-XR-ipv6-ospfv3-act:input/Cisco-IOS-XR-ipv6-ospfv3-act:neighbor'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if self.interface_name is not None:
                    return True

                if self.neighbor_id is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
                return meta._meta_table['ActOspfv3StatisticsNeighborRpc.Input.Neighbor']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-statistics-neighbor/Cisco-IOS-XR-ipv6-ospfv3-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.instance is not None and self.instance._has_data():
                return True

            if self.neighbor is not None and self.neighbor._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
            return meta._meta_table['ActOspfv3StatisticsNeighborRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-statistics-neighbor'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
        return meta._meta_table['ActOspfv3StatisticsNeighborRpc']['meta_info']


class ActOspfv3StatisticsRpc(object):
    """
    Clear OSPFv3 Counters And Statistics
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3StatisticsRpc.Input>`
    
    

    """

    _prefix = 'ospfv3-act'
    _revision = '2016-09-14'

    def __init__(self):
        self.input = ActOspfv3StatisticsRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPFv3 instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3StatisticsRpc.Input.Instance>`
        
        .. attribute:: neighbor
        
        	Neighbor statistics per neighbor id
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: prefix_priority
        
        	All OSPFv3 counters and statistics
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: spf
        
        	SPF statistics
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ospfv3-act'
        _revision = '2016-09-14'

        def __init__(self):
            self.parent = None
            self.instance = ActOspfv3StatisticsRpc.Input.Instance()
            self.instance.parent = self
            self.neighbor = None
            self.prefix_priority = None
            self.spf = None


        class Instance(object):
            """
            Clear data from OSPFv3 instance
            
            .. attribute:: instance_identifier
            
            	OSPFv3 process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospfv3-act'
            _revision = '2016-09-14'

            def __init__(self):
                self.parent = None
                self.instance_identifier = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-statistics/Cisco-IOS-XR-ipv6-ospfv3-act:input/Cisco-IOS-XR-ipv6-ospfv3-act:instance'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
                return meta._meta_table['ActOspfv3StatisticsRpc.Input.Instance']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-statistics/Cisco-IOS-XR-ipv6-ospfv3-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.instance is not None and self.instance._has_data():
                return True

            if self.neighbor is not None:
                return True

            if self.prefix_priority is not None:
                return True

            if self.spf is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
            return meta._meta_table['ActOspfv3StatisticsRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-statistics'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
        return meta._meta_table['ActOspfv3StatisticsRpc']['meta_info']


class ActOspfv3InstanceVrfRpc(object):
    """
    Clear one or more non\-default OSPFv3 VRFs in process
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrfRpc.Input>`
    
    

    """

    _prefix = 'ospfv3-act'
    _revision = '2016-09-14'

    def __init__(self):
        self.input = ActOspfv3InstanceVrfRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: instance
        
        	OSPFv3 instance name
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrfRpc.Input.Instance>`
        
        

        """

        _prefix = 'ospfv3-act'
        _revision = '2016-09-14'

        def __init__(self):
            self.parent = None
            self.instance = ActOspfv3InstanceVrfRpc.Input.Instance()
            self.instance.parent = self


        class Instance(object):
            """
            OSPFv3 instance name
            
            .. attribute:: all
            
            	Clear all non\-default OSPFv3 VRFs
            	**type**\:   :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrfRpc.Input.Instance.All>`
            
            .. attribute:: all_inclusive
            
            	Clear all non\-default and default OSPFv3 VRFs
            	**type**\:   :py:class:`AllInclusive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive>`
            
            .. attribute:: instance_identifier
            
            	OSPFv3 process instance identifier
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: vrf
            
            	Clear one or more non\-default OSPFv3 VRFs in process
            	**type**\:   :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrfRpc.Input.Instance.Vrf>`
            
            

            """

            _prefix = 'ospfv3-act'
            _revision = '2016-09-14'

            def __init__(self):
                self.parent = None
                self.all = ActOspfv3InstanceVrfRpc.Input.Instance.All()
                self.all.parent = self
                self.all_inclusive = ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive()
                self.all_inclusive.parent = self
                self.instance_identifier = None
                self.vrf = ActOspfv3InstanceVrfRpc.Input.Instance.Vrf()
                self.vrf.parent = self


            class Vrf(object):
                """
                Clear one or more non\-default OSPFv3 VRFs in process
                
                .. attribute:: process
                
                	Reset OSPFv3 process
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: redistribution
                
                	Clear OSPFv3 route redistrbution
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: route
                
                	Clear OSPFv3 route table
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: stats
                
                	OSPFv3 counters and statistics
                	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrfRpc.Input.Instance.Vrf.Stats>`
                
                .. attribute:: vrf_name
                
                	OSPFv3 VRF name
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ospfv3-act'
                _revision = '2016-09-14'

                def __init__(self):
                    self.parent = None
                    self.process = None
                    self.redistribution = None
                    self.route = None
                    self.stats = ActOspfv3InstanceVrfRpc.Input.Instance.Vrf.Stats()
                    self.stats.parent = self
                    self.vrf_name = None


                class Stats(object):
                    """
                    OSPFv3 counters and statistics
                    
                    .. attribute:: neighbor
                    
                    	Neighbor statistics per interface or neighbor id
                    	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor>`
                    
                    .. attribute:: prefix_priority
                    
                    	SPF Prefix Priority statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: spf
                    
                    	SPF statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ospfv3-act'
                    _revision = '2016-09-14'

                    def __init__(self):
                        self.parent = None
                        self.neighbor = ActOspfv3InstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor()
                        self.neighbor.parent = self
                        self.prefix_priority = None
                        self.spf = None


                    class Neighbor(object):
                        """
                        Neighbor statistics per interface or neighbor id
                        
                        .. attribute:: interface
                        
                        	
                        	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor.Interface>`
                        
                        .. attribute:: neighbor_id
                        
                        	Neighbor ID
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ospfv3-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            self.parent = None
                            self.interface = ActOspfv3InstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor.Interface()
                            self.interface.parent = self
                            self.neighbor_id = None


                        class Interface(object):
                            """
                            
                            
                            .. attribute:: interface_name
                            
                            	OSPFv3 interface statistics
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'ospfv3-act'
                            _revision = '2016-09-14'

                            def __init__(self):
                                self.parent = None
                                self.interface_name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/Cisco-IOS-XR-ipv6-ospfv3-act:input/Cisco-IOS-XR-ipv6-ospfv3-act:instance/Cisco-IOS-XR-ipv6-ospfv3-act:vrf/Cisco-IOS-XR-ipv6-ospfv3-act:stats/Cisco-IOS-XR-ipv6-ospfv3-act:neighbor/Cisco-IOS-XR-ipv6-ospfv3-act:interface'

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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
                                return meta._meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor.Interface']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/Cisco-IOS-XR-ipv6-ospfv3-act:input/Cisco-IOS-XR-ipv6-ospfv3-act:instance/Cisco-IOS-XR-ipv6-ospfv3-act:vrf/Cisco-IOS-XR-ipv6-ospfv3-act:stats/Cisco-IOS-XR-ipv6-ospfv3-act:neighbor'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            if self.parent is None:
                                raise YPYError('Parent reference is needed to determine if entity has configuration data')
                            return self.parent.is_config()

                        def _has_data(self):
                            if self.interface is not None and self.interface._has_data():
                                return True

                            if self.neighbor_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
                            return meta._meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/Cisco-IOS-XR-ipv6-ospfv3-act:input/Cisco-IOS-XR-ipv6-ospfv3-act:instance/Cisco-IOS-XR-ipv6-ospfv3-act:vrf/Cisco-IOS-XR-ipv6-ospfv3-act:stats'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        if self.parent is None:
                            raise YPYError('Parent reference is needed to determine if entity has configuration data')
                        return self.parent.is_config()

                    def _has_data(self):
                        if self.neighbor is not None and self.neighbor._has_data():
                            return True

                        if self.prefix_priority is not None:
                            return True

                        if self.spf is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
                        return meta._meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.Vrf.Stats']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/Cisco-IOS-XR-ipv6-ospfv3-act:input/Cisco-IOS-XR-ipv6-ospfv3-act:instance/Cisco-IOS-XR-ipv6-ospfv3-act:vrf'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    if self.parent is None:
                        raise YPYError('Parent reference is needed to determine if entity has configuration data')
                    return self.parent.is_config()

                def _has_data(self):
                    if self.process is not None:
                        return True

                    if self.redistribution is not None:
                        return True

                    if self.route is not None:
                        return True

                    if self.stats is not None and self.stats._has_data():
                        return True

                    if self.vrf_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
                    return meta._meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.Vrf']['meta_info']


            class All(object):
                """
                Clear all non\-default OSPFv3 VRFs
                
                .. attribute:: process
                
                	Reset OSPFv3 process
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: redistribution
                
                	Clear OSPFv3 route redistrbution
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: route
                
                	Clear OSPFv3 route table
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: stats
                
                	OSPFv3 counters and statistics
                	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrfRpc.Input.Instance.All.Stats>`
                
                

                """

                _prefix = 'ospfv3-act'
                _revision = '2016-09-14'

                def __init__(self):
                    self.parent = None
                    self.process = None
                    self.redistribution = None
                    self.route = None
                    self.stats = ActOspfv3InstanceVrfRpc.Input.Instance.All.Stats()
                    self.stats.parent = self


                class Stats(object):
                    """
                    OSPFv3 counters and statistics
                    
                    .. attribute:: neighbor
                    
                    	Neighbor statistics per interface or neighbor id
                    	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrfRpc.Input.Instance.All.Stats.Neighbor>`
                    
                    .. attribute:: prefix_priority
                    
                    	SPF Prefix Priority statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: spf
                    
                    	SPF statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ospfv3-act'
                    _revision = '2016-09-14'

                    def __init__(self):
                        self.parent = None
                        self.neighbor = ActOspfv3InstanceVrfRpc.Input.Instance.All.Stats.Neighbor()
                        self.neighbor.parent = self
                        self.prefix_priority = None
                        self.spf = None


                    class Neighbor(object):
                        """
                        Neighbor statistics per interface or neighbor id
                        
                        .. attribute:: interface
                        
                        	
                        	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrfRpc.Input.Instance.All.Stats.Neighbor.Interface>`
                        
                        .. attribute:: neighbor_id
                        
                        	Neighbor ID
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ospfv3-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            self.parent = None
                            self.interface = ActOspfv3InstanceVrfRpc.Input.Instance.All.Stats.Neighbor.Interface()
                            self.interface.parent = self
                            self.neighbor_id = None


                        class Interface(object):
                            """
                            
                            
                            .. attribute:: interface_name
                            
                            	OSPFv3 interface statistics
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'ospfv3-act'
                            _revision = '2016-09-14'

                            def __init__(self):
                                self.parent = None
                                self.interface_name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/Cisco-IOS-XR-ipv6-ospfv3-act:input/Cisco-IOS-XR-ipv6-ospfv3-act:instance/Cisco-IOS-XR-ipv6-ospfv3-act:all/Cisco-IOS-XR-ipv6-ospfv3-act:stats/Cisco-IOS-XR-ipv6-ospfv3-act:neighbor/Cisco-IOS-XR-ipv6-ospfv3-act:interface'

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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
                                return meta._meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.All.Stats.Neighbor.Interface']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/Cisco-IOS-XR-ipv6-ospfv3-act:input/Cisco-IOS-XR-ipv6-ospfv3-act:instance/Cisco-IOS-XR-ipv6-ospfv3-act:all/Cisco-IOS-XR-ipv6-ospfv3-act:stats/Cisco-IOS-XR-ipv6-ospfv3-act:neighbor'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            if self.parent is None:
                                raise YPYError('Parent reference is needed to determine if entity has configuration data')
                            return self.parent.is_config()

                        def _has_data(self):
                            if self.interface is not None and self.interface._has_data():
                                return True

                            if self.neighbor_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
                            return meta._meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.All.Stats.Neighbor']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/Cisco-IOS-XR-ipv6-ospfv3-act:input/Cisco-IOS-XR-ipv6-ospfv3-act:instance/Cisco-IOS-XR-ipv6-ospfv3-act:all/Cisco-IOS-XR-ipv6-ospfv3-act:stats'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        if self.parent is None:
                            raise YPYError('Parent reference is needed to determine if entity has configuration data')
                        return self.parent.is_config()

                    def _has_data(self):
                        if self.neighbor is not None and self.neighbor._has_data():
                            return True

                        if self.prefix_priority is not None:
                            return True

                        if self.spf is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
                        return meta._meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.All.Stats']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/Cisco-IOS-XR-ipv6-ospfv3-act:input/Cisco-IOS-XR-ipv6-ospfv3-act:instance/Cisco-IOS-XR-ipv6-ospfv3-act:all'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    if self.parent is None:
                        raise YPYError('Parent reference is needed to determine if entity has configuration data')
                    return self.parent.is_config()

                def _has_data(self):
                    if self.process is not None:
                        return True

                    if self.redistribution is not None:
                        return True

                    if self.route is not None:
                        return True

                    if self.stats is not None and self.stats._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
                    return meta._meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.All']['meta_info']


            class AllInclusive(object):
                """
                Clear all non\-default and default OSPFv3 VRFs
                
                .. attribute:: process
                
                	Reset OSPFv3 process
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: redistribution
                
                	Clear OSPFv3 route redistrbution
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: route
                
                	Clear OSPFv3 route table
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: stats
                
                	OSPFv3 counters and statistics
                	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive.Stats>`
                
                

                """

                _prefix = 'ospfv3-act'
                _revision = '2016-09-14'

                def __init__(self):
                    self.parent = None
                    self.process = None
                    self.redistribution = None
                    self.route = None
                    self.stats = ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive.Stats()
                    self.stats.parent = self


                class Stats(object):
                    """
                    OSPFv3 counters and statistics
                    
                    .. attribute:: neighbor
                    
                    	Neighbor statistics per interface or neighbor id
                    	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor>`
                    
                    .. attribute:: prefix_priority
                    
                    	SPF Prefix Priority statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: spf
                    
                    	SPF statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ospfv3-act'
                    _revision = '2016-09-14'

                    def __init__(self):
                        self.parent = None
                        self.neighbor = ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor()
                        self.neighbor.parent = self
                        self.prefix_priority = None
                        self.spf = None


                    class Neighbor(object):
                        """
                        Neighbor statistics per interface or neighbor id
                        
                        .. attribute:: interface
                        
                        	
                        	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor.Interface>`
                        
                        .. attribute:: neighbor_id
                        
                        	Neighbor ID
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ospfv3-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            self.parent = None
                            self.interface = ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor.Interface()
                            self.interface.parent = self
                            self.neighbor_id = None


                        class Interface(object):
                            """
                            
                            
                            .. attribute:: interface_name
                            
                            	OSPFv3 interface statistics
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'ospfv3-act'
                            _revision = '2016-09-14'

                            def __init__(self):
                                self.parent = None
                                self.interface_name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/Cisco-IOS-XR-ipv6-ospfv3-act:input/Cisco-IOS-XR-ipv6-ospfv3-act:instance/Cisco-IOS-XR-ipv6-ospfv3-act:all-inclusive/Cisco-IOS-XR-ipv6-ospfv3-act:stats/Cisco-IOS-XR-ipv6-ospfv3-act:neighbor/Cisco-IOS-XR-ipv6-ospfv3-act:interface'

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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
                                return meta._meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor.Interface']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/Cisco-IOS-XR-ipv6-ospfv3-act:input/Cisco-IOS-XR-ipv6-ospfv3-act:instance/Cisco-IOS-XR-ipv6-ospfv3-act:all-inclusive/Cisco-IOS-XR-ipv6-ospfv3-act:stats/Cisco-IOS-XR-ipv6-ospfv3-act:neighbor'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            if self.parent is None:
                                raise YPYError('Parent reference is needed to determine if entity has configuration data')
                            return self.parent.is_config()

                        def _has_data(self):
                            if self.interface is not None and self.interface._has_data():
                                return True

                            if self.neighbor_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
                            return meta._meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/Cisco-IOS-XR-ipv6-ospfv3-act:input/Cisco-IOS-XR-ipv6-ospfv3-act:instance/Cisco-IOS-XR-ipv6-ospfv3-act:all-inclusive/Cisco-IOS-XR-ipv6-ospfv3-act:stats'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        if self.parent is None:
                            raise YPYError('Parent reference is needed to determine if entity has configuration data')
                        return self.parent.is_config()

                    def _has_data(self):
                        if self.neighbor is not None and self.neighbor._has_data():
                            return True

                        if self.prefix_priority is not None:
                            return True

                        if self.spf is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
                        return meta._meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive.Stats']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/Cisco-IOS-XR-ipv6-ospfv3-act:input/Cisco-IOS-XR-ipv6-ospfv3-act:instance/Cisco-IOS-XR-ipv6-ospfv3-act:all-inclusive'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    if self.parent is None:
                        raise YPYError('Parent reference is needed to determine if entity has configuration data')
                    return self.parent.is_config()

                def _has_data(self):
                    if self.process is not None:
                        return True

                    if self.redistribution is not None:
                        return True

                    if self.route is not None:
                        return True

                    if self.stats is not None and self.stats._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
                    return meta._meta_table['ActOspfv3InstanceVrfRpc.Input.Instance.AllInclusive']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/Cisco-IOS-XR-ipv6-ospfv3-act:input/Cisco-IOS-XR-ipv6-ospfv3-act:instance'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if self.all is not None and self.all._has_data():
                    return True

                if self.all_inclusive is not None and self.all_inclusive._has_data():
                    return True

                if self.instance_identifier is not None:
                    return True

                if self.vrf is not None and self.vrf._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
                return meta._meta_table['ActOspfv3InstanceVrfRpc.Input.Instance']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/Cisco-IOS-XR-ipv6-ospfv3-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.instance is not None and self.instance._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
            return meta._meta_table['ActOspfv3InstanceVrfRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_ospfv3_act as meta
        return meta._meta_table['ActOspfv3InstanceVrfRpc']['meta_info']



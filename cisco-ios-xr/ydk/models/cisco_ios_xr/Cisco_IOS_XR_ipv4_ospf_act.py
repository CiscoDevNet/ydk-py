""" Cisco_IOS_XR_ipv4_ospf_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR OSPF action package configuration.

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class ActOspfRoutesRpc(object):
    """
    Clear OSPF Routes Table
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfRoutesRpc.Input>`
    
    

    """

    _prefix = 'ospf-act'
    _revision = '2016-09-14'

    def __init__(self):
        self.input = ActOspfRoutesRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPF instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfRoutesRpc.Input.Instance>`
        
        .. attribute:: route
        
        	Clear OSPF route table
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ospf-act'
        _revision = '2016-09-14'

        def __init__(self):
            self.parent = None
            self.instance = ActOspfRoutesRpc.Input.Instance()
            self.instance.parent = self
            self.route = None


        class Instance(object):
            """
            Clear data from OSPF instance
            
            .. attribute:: instance_identifier
            
            	OSPF process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                self.parent = None
                self.instance_identifier = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-routes/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:instance'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                return meta._meta_table['ActOspfRoutesRpc.Input.Instance']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-routes/Cisco-IOS-XR-ipv4-ospf-act:input'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
            return meta._meta_table['ActOspfRoutesRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-routes'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
        return meta._meta_table['ActOspfRoutesRpc']['meta_info']


class ActOspfRedistributionRpc(object):
    """
    Clear OSPF Route Redistribution
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfRedistributionRpc.Input>`
    
    

    """

    _prefix = 'ospf-act'
    _revision = '2016-09-14'

    def __init__(self):
        self.input = ActOspfRedistributionRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPF instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfRedistributionRpc.Input.Instance>`
        
        .. attribute:: redistribution
        
        	Clear OSPF Route Redistribution
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ospf-act'
        _revision = '2016-09-14'

        def __init__(self):
            self.parent = None
            self.instance = ActOspfRedistributionRpc.Input.Instance()
            self.instance.parent = self
            self.redistribution = None


        class Instance(object):
            """
            Clear data from OSPF instance
            
            .. attribute:: instance_identifier
            
            	OSPF process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                self.parent = None
                self.instance_identifier = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-redistribution/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:instance'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                return meta._meta_table['ActOspfRedistributionRpc.Input.Instance']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-redistribution/Cisco-IOS-XR-ipv4-ospf-act:input'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
            return meta._meta_table['ActOspfRedistributionRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-redistribution'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
        return meta._meta_table['ActOspfRedistributionRpc']['meta_info']


class ActOspfStatisticsRpc(object):
    """
    Clear OSPF Counters And Statistics
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfStatisticsRpc.Input>`
    
    

    """

    _prefix = 'ospf-act'
    _revision = '2016-09-14'

    def __init__(self):
        self.input = ActOspfStatisticsRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: all
        
        	All OSPF counters and statistics
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: instance
        
        	Clear data from OSPF instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfStatisticsRpc.Input.Instance>`
        
        .. attribute:: interface_name
        
        	OSPF interface statistics
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: message_queue
        
        	Message\-queue statistics
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: neighbor
        
        	Neighbor statistics per neighbor id
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: spf
        
        	SPF statistics
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ospf-act'
        _revision = '2016-09-14'

        def __init__(self):
            self.parent = None
            self.all = None
            self.instance = ActOspfStatisticsRpc.Input.Instance()
            self.instance.parent = self
            self.interface_name = None
            self.message_queue = None
            self.neighbor = None
            self.spf = None


        class Instance(object):
            """
            Clear data from OSPF instance
            
            .. attribute:: instance_identifier
            
            	OSPF process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                self.parent = None
                self.instance_identifier = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-statistics/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:instance'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                return meta._meta_table['ActOspfStatisticsRpc.Input.Instance']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-statistics/Cisco-IOS-XR-ipv4-ospf-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.all is not None:
                return True

            if self.instance is not None and self.instance._has_data():
                return True

            if self.interface_name is not None:
                return True

            if self.message_queue is not None:
                return True

            if self.neighbor is not None:
                return True

            if self.spf is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
            return meta._meta_table['ActOspfStatisticsRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-statistics'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
        return meta._meta_table['ActOspfStatisticsRpc']['meta_info']


class ActOspfStatisticsNeighborRpc(object):
    """
    Neighbor statistics per neighbor id
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfStatisticsNeighborRpc.Input>`
    
    

    """

    _prefix = 'ospf-act'
    _revision = '2016-09-14'

    def __init__(self):
        self.input = ActOspfStatisticsNeighborRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPF instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfStatisticsNeighborRpc.Input.Instance>`
        
        .. attribute:: neighbor
        
        	
        	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfStatisticsNeighborRpc.Input.Neighbor>`
        
        

        """

        _prefix = 'ospf-act'
        _revision = '2016-09-14'

        def __init__(self):
            self.parent = None
            self.instance = ActOspfStatisticsNeighborRpc.Input.Instance()
            self.instance.parent = self
            self.neighbor = ActOspfStatisticsNeighborRpc.Input.Neighbor()
            self.neighbor.parent = self


        class Instance(object):
            """
            Clear data from OSPF instance
            
            .. attribute:: instance_identifier
            
            	OSPF process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                self.parent = None
                self.instance_identifier = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-statistics-neighbor/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:instance'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                return meta._meta_table['ActOspfStatisticsNeighborRpc.Input.Instance']['meta_info']


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

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.neighbor_id = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-statistics-neighbor/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:neighbor'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                return meta._meta_table['ActOspfStatisticsNeighborRpc.Input.Neighbor']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-statistics-neighbor/Cisco-IOS-XR-ipv4-ospf-act:input'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
            return meta._meta_table['ActOspfStatisticsNeighborRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-statistics-neighbor'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
        return meta._meta_table['ActOspfStatisticsNeighborRpc']['meta_info']


class ActOspfStatisticsInterfaceRpc(object):
    """
    Neighbor statistics per interface
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfStatisticsInterfaceRpc.Input>`
    
    

    """

    _prefix = 'ospf-act'
    _revision = '2016-09-14'

    def __init__(self):
        self.input = ActOspfStatisticsInterfaceRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPF instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfStatisticsInterfaceRpc.Input.Instance>`
        
        .. attribute:: interface
        
        	
        	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfStatisticsInterfaceRpc.Input.Interface>`
        
        

        """

        _prefix = 'ospf-act'
        _revision = '2016-09-14'

        def __init__(self):
            self.parent = None
            self.instance = ActOspfStatisticsInterfaceRpc.Input.Instance()
            self.instance.parent = self
            self.interface = ActOspfStatisticsInterfaceRpc.Input.Interface()
            self.interface.parent = self


        class Instance(object):
            """
            Clear data from OSPF instance
            
            .. attribute:: instance_identifier
            
            	OSPF process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                self.parent = None
                self.instance_identifier = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-statistics-interface/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:instance'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                return meta._meta_table['ActOspfStatisticsInterfaceRpc.Input.Instance']['meta_info']


        class Interface(object):
            """
            
            
            .. attribute:: interface_name
            
            	OSPF interface statistics
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                self.parent = None
                self.interface_name = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-statistics-interface/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:interface'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                return meta._meta_table['ActOspfStatisticsInterfaceRpc.Input.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-statistics-interface/Cisco-IOS-XR-ipv4-ospf-act:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.instance is not None and self.instance._has_data():
                return True

            if self.interface is not None and self.interface._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
            return meta._meta_table['ActOspfStatisticsInterfaceRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-statistics-interface'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
        return meta._meta_table['ActOspfStatisticsInterfaceRpc']['meta_info']


class ActOspfProcessRpc(object):
    """
    Reset OSPF Process
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfProcessRpc.Input>`
    
    

    """

    _prefix = 'ospf-act'
    _revision = '2016-09-14'

    def __init__(self):
        self.input = ActOspfProcessRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPF instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfProcessRpc.Input.Instance>`
        
        .. attribute:: process
        
        	Reset OSPF process
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ospf-act'
        _revision = '2016-09-14'

        def __init__(self):
            self.parent = None
            self.instance = ActOspfProcessRpc.Input.Instance()
            self.instance.parent = self
            self.process = None


        class Instance(object):
            """
            Clear data from OSPF instance
            
            .. attribute:: instance_identifier
            
            	OSPF process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                self.parent = None
                self.instance_identifier = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-process/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:instance'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                return meta._meta_table['ActOspfProcessRpc.Input.Instance']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-process/Cisco-IOS-XR-ipv4-ospf-act:input'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
            return meta._meta_table['ActOspfProcessRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-process'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
        return meta._meta_table['ActOspfProcessRpc']['meta_info']


class ActOspfInstanceVrfRpc(object):
    """
    Clear one or more non\-default OSPF VRFs in process
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrfRpc.Input>`
    
    

    """

    _prefix = 'ospf-act'
    _revision = '2016-09-14'

    def __init__(self):
        self.input = ActOspfInstanceVrfRpc.Input()
        self.input.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: instance
        
        	OSPF instance name
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrfRpc.Input.Instance>`
        
        

        """

        _prefix = 'ospf-act'
        _revision = '2016-09-14'

        def __init__(self):
            self.parent = None
            self.instance = ActOspfInstanceVrfRpc.Input.Instance()
            self.instance.parent = self


        class Instance(object):
            """
            OSPF instance name
            
            .. attribute:: all
            
            	Clear all non\-default OSPF VRFs
            	**type**\:   :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrfRpc.Input.Instance.All>`
            
            .. attribute:: all_inclusive
            
            	Clear all non\-default and default OSPF VRFs
            	**type**\:   :py:class:`AllInclusive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrfRpc.Input.Instance.AllInclusive>`
            
            .. attribute:: instance_identifier
            
            	OSPF process instance identifier
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: vrf
            
            	Clear one or more non\-default OSPF VRFs in process
            	**type**\:   :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrfRpc.Input.Instance.Vrf>`
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                self.parent = None
                self.all = ActOspfInstanceVrfRpc.Input.Instance.All()
                self.all.parent = self
                self.all_inclusive = ActOspfInstanceVrfRpc.Input.Instance.AllInclusive()
                self.all_inclusive.parent = self
                self.instance_identifier = None
                self.vrf = ActOspfInstanceVrfRpc.Input.Instance.Vrf()
                self.vrf.parent = self


            class Vrf(object):
                """
                Clear one or more non\-default OSPF VRFs in process
                
                .. attribute:: process
                
                	Reset OSPF process
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: redistribution
                
                	Clear OSPF route redistrbution
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: route
                
                	Clear OSPF route table
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: stats
                
                	OSPF counters and statistics
                	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats>`
                
                .. attribute:: vrf_name
                
                	OSPF VRF name
                	**type**\:  str
                
                

                """

                _prefix = 'ospf-act'
                _revision = '2016-09-14'

                def __init__(self):
                    self.parent = None
                    self.process = None
                    self.redistribution = None
                    self.route = None
                    self.stats = ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats()
                    self.stats.parent = self
                    self.vrf_name = None


                class Stats(object):
                    """
                    OSPF counters and statistics
                    
                    .. attribute:: interface
                    
                    	OSPF interface statistics
                    	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats.Interface>`
                    
                    .. attribute:: message_queue
                    
                    	Message\-queue statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: neighbor
                    
                    	Neighbor statistics per interface or neighbor id
                    	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor>`
                    
                    .. attribute:: spf
                    
                    	SPF statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ospf-act'
                    _revision = '2016-09-14'

                    def __init__(self):
                        self.parent = None
                        self.interface = ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats.Interface()
                        self.interface.parent = self
                        self.message_queue = None
                        self.neighbor = ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor()
                        self.neighbor.parent = self
                        self.spf = None


                    class Interface(object):
                        """
                        OSPF interface statistics
                        
                        .. attribute:: interface_name
                        
                        	
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        

                        """

                        _prefix = 'ospf-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:instance/Cisco-IOS-XR-ipv4-ospf-act:vrf/Cisco-IOS-XR-ipv4-ospf-act:stats/Cisco-IOS-XR-ipv4-ospf-act:interface'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                            return meta._meta_table['ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats.Interface']['meta_info']


                    class Neighbor(object):
                        """
                        Neighbor statistics per interface or neighbor id
                        
                        .. attribute:: interface
                        
                        	
                        	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor.Interface>`
                        
                        .. attribute:: neighbor_id
                        
                        	Neighbor ID
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ospf-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            self.parent = None
                            self.interface = ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor.Interface()
                            self.interface.parent = self
                            self.neighbor_id = None


                        class Interface(object):
                            """
                            
                            
                            .. attribute:: interface_name
                            
                            	OSPF interface statistics
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'ospf-act'
                            _revision = '2016-09-14'

                            def __init__(self):
                                self.parent = None
                                self.interface_name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:instance/Cisco-IOS-XR-ipv4-ospf-act:vrf/Cisco-IOS-XR-ipv4-ospf-act:stats/Cisco-IOS-XR-ipv4-ospf-act:neighbor/Cisco-IOS-XR-ipv4-ospf-act:interface'

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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                                return meta._meta_table['ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor.Interface']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:instance/Cisco-IOS-XR-ipv4-ospf-act:vrf/Cisco-IOS-XR-ipv4-ospf-act:stats/Cisco-IOS-XR-ipv4-ospf-act:neighbor'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                            return meta._meta_table['ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats.Neighbor']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:instance/Cisco-IOS-XR-ipv4-ospf-act:vrf/Cisco-IOS-XR-ipv4-ospf-act:stats'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        if self.parent is None:
                            raise YPYError('Parent reference is needed to determine if entity has configuration data')
                        return self.parent.is_config()

                    def _has_data(self):
                        if self.interface is not None and self.interface._has_data():
                            return True

                        if self.message_queue is not None:
                            return True

                        if self.neighbor is not None and self.neighbor._has_data():
                            return True

                        if self.spf is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                        return meta._meta_table['ActOspfInstanceVrfRpc.Input.Instance.Vrf.Stats']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:instance/Cisco-IOS-XR-ipv4-ospf-act:vrf'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                    return meta._meta_table['ActOspfInstanceVrfRpc.Input.Instance.Vrf']['meta_info']


            class All(object):
                """
                Clear all non\-default OSPF VRFs
                
                .. attribute:: process
                
                	Reset OSPF process
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: redistribution
                
                	Clear OSPF route redistrbution
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: route
                
                	Clear OSPF route table
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: stats
                
                	OSPF counters and statistics
                	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrfRpc.Input.Instance.All.Stats>`
                
                

                """

                _prefix = 'ospf-act'
                _revision = '2016-09-14'

                def __init__(self):
                    self.parent = None
                    self.process = None
                    self.redistribution = None
                    self.route = None
                    self.stats = ActOspfInstanceVrfRpc.Input.Instance.All.Stats()
                    self.stats.parent = self


                class Stats(object):
                    """
                    OSPF counters and statistics
                    
                    .. attribute:: interface
                    
                    	OSPF interface statistics
                    	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrfRpc.Input.Instance.All.Stats.Interface>`
                    
                    .. attribute:: message_queue
                    
                    	Message\-queue statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: neighbor
                    
                    	Neighbor statistics per interface or neighbor id
                    	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrfRpc.Input.Instance.All.Stats.Neighbor>`
                    
                    .. attribute:: spf
                    
                    	SPF statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ospf-act'
                    _revision = '2016-09-14'

                    def __init__(self):
                        self.parent = None
                        self.interface = ActOspfInstanceVrfRpc.Input.Instance.All.Stats.Interface()
                        self.interface.parent = self
                        self.message_queue = None
                        self.neighbor = ActOspfInstanceVrfRpc.Input.Instance.All.Stats.Neighbor()
                        self.neighbor.parent = self
                        self.spf = None


                    class Interface(object):
                        """
                        OSPF interface statistics
                        
                        .. attribute:: interface_name
                        
                        	
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        

                        """

                        _prefix = 'ospf-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:instance/Cisco-IOS-XR-ipv4-ospf-act:all/Cisco-IOS-XR-ipv4-ospf-act:stats/Cisco-IOS-XR-ipv4-ospf-act:interface'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                            return meta._meta_table['ActOspfInstanceVrfRpc.Input.Instance.All.Stats.Interface']['meta_info']


                    class Neighbor(object):
                        """
                        Neighbor statistics per interface or neighbor id
                        
                        .. attribute:: interface
                        
                        	
                        	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrfRpc.Input.Instance.All.Stats.Neighbor.Interface>`
                        
                        .. attribute:: neighbor_id
                        
                        	Neighbor ID
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ospf-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            self.parent = None
                            self.interface = ActOspfInstanceVrfRpc.Input.Instance.All.Stats.Neighbor.Interface()
                            self.interface.parent = self
                            self.neighbor_id = None


                        class Interface(object):
                            """
                            
                            
                            .. attribute:: interface_name
                            
                            	OSPF interface statistics
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'ospf-act'
                            _revision = '2016-09-14'

                            def __init__(self):
                                self.parent = None
                                self.interface_name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:instance/Cisco-IOS-XR-ipv4-ospf-act:all/Cisco-IOS-XR-ipv4-ospf-act:stats/Cisco-IOS-XR-ipv4-ospf-act:neighbor/Cisco-IOS-XR-ipv4-ospf-act:interface'

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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                                return meta._meta_table['ActOspfInstanceVrfRpc.Input.Instance.All.Stats.Neighbor.Interface']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:instance/Cisco-IOS-XR-ipv4-ospf-act:all/Cisco-IOS-XR-ipv4-ospf-act:stats/Cisco-IOS-XR-ipv4-ospf-act:neighbor'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                            return meta._meta_table['ActOspfInstanceVrfRpc.Input.Instance.All.Stats.Neighbor']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:instance/Cisco-IOS-XR-ipv4-ospf-act:all/Cisco-IOS-XR-ipv4-ospf-act:stats'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        if self.parent is None:
                            raise YPYError('Parent reference is needed to determine if entity has configuration data')
                        return self.parent.is_config()

                    def _has_data(self):
                        if self.interface is not None and self.interface._has_data():
                            return True

                        if self.message_queue is not None:
                            return True

                        if self.neighbor is not None and self.neighbor._has_data():
                            return True

                        if self.spf is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                        return meta._meta_table['ActOspfInstanceVrfRpc.Input.Instance.All.Stats']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:instance/Cisco-IOS-XR-ipv4-ospf-act:all'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                    return meta._meta_table['ActOspfInstanceVrfRpc.Input.Instance.All']['meta_info']


            class AllInclusive(object):
                """
                Clear all non\-default and default OSPF VRFs
                
                .. attribute:: process
                
                	Reset OSPF process
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: redistribution
                
                	Clear OSPF route redistrbution
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: route
                
                	Clear OSPF route table
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: stats
                
                	OSPF counters and statistics
                	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats>`
                
                

                """

                _prefix = 'ospf-act'
                _revision = '2016-09-14'

                def __init__(self):
                    self.parent = None
                    self.process = None
                    self.redistribution = None
                    self.route = None
                    self.stats = ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats()
                    self.stats.parent = self


                class Stats(object):
                    """
                    OSPF counters and statistics
                    
                    .. attribute:: interface
                    
                    	OSPF interface statistics
                    	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats.Interface>`
                    
                    .. attribute:: message_queue
                    
                    	Message\-queue statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: neighbor
                    
                    	Neighbor statistics per interface or neighbor id
                    	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor>`
                    
                    .. attribute:: spf
                    
                    	SPF statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ospf-act'
                    _revision = '2016-09-14'

                    def __init__(self):
                        self.parent = None
                        self.interface = ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats.Interface()
                        self.interface.parent = self
                        self.message_queue = None
                        self.neighbor = ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor()
                        self.neighbor.parent = self
                        self.spf = None


                    class Interface(object):
                        """
                        OSPF interface statistics
                        
                        .. attribute:: interface_name
                        
                        	
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        

                        """

                        _prefix = 'ospf-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:instance/Cisco-IOS-XR-ipv4-ospf-act:all-inclusive/Cisco-IOS-XR-ipv4-ospf-act:stats/Cisco-IOS-XR-ipv4-ospf-act:interface'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                            return meta._meta_table['ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats.Interface']['meta_info']


                    class Neighbor(object):
                        """
                        Neighbor statistics per interface or neighbor id
                        
                        .. attribute:: interface
                        
                        	
                        	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor.Interface>`
                        
                        .. attribute:: neighbor_id
                        
                        	Neighbor ID
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ospf-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            self.parent = None
                            self.interface = ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor.Interface()
                            self.interface.parent = self
                            self.neighbor_id = None


                        class Interface(object):
                            """
                            
                            
                            .. attribute:: interface_name
                            
                            	OSPF interface statistics
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'ospf-act'
                            _revision = '2016-09-14'

                            def __init__(self):
                                self.parent = None
                                self.interface_name = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:instance/Cisco-IOS-XR-ipv4-ospf-act:all-inclusive/Cisco-IOS-XR-ipv4-ospf-act:stats/Cisco-IOS-XR-ipv4-ospf-act:neighbor/Cisco-IOS-XR-ipv4-ospf-act:interface'

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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                                return meta._meta_table['ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor.Interface']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:instance/Cisco-IOS-XR-ipv4-ospf-act:all-inclusive/Cisco-IOS-XR-ipv4-ospf-act:stats/Cisco-IOS-XR-ipv4-ospf-act:neighbor'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                            return meta._meta_table['ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats.Neighbor']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:instance/Cisco-IOS-XR-ipv4-ospf-act:all-inclusive/Cisco-IOS-XR-ipv4-ospf-act:stats'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        if self.parent is None:
                            raise YPYError('Parent reference is needed to determine if entity has configuration data')
                        return self.parent.is_config()

                    def _has_data(self):
                        if self.interface is not None and self.interface._has_data():
                            return True

                        if self.message_queue is not None:
                            return True

                        if self.neighbor is not None and self.neighbor._has_data():
                            return True

                        if self.spf is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                        return meta._meta_table['ActOspfInstanceVrfRpc.Input.Instance.AllInclusive.Stats']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:instance/Cisco-IOS-XR-ipv4-ospf-act:all-inclusive'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                    return meta._meta_table['ActOspfInstanceVrfRpc.Input.Instance.AllInclusive']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/Cisco-IOS-XR-ipv4-ospf-act:input/Cisco-IOS-XR-ipv4-ospf-act:instance'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
                return meta._meta_table['ActOspfInstanceVrfRpc.Input.Instance']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/Cisco-IOS-XR-ipv4-ospf-act:input'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
            return meta._meta_table['ActOspfInstanceVrfRpc.Input']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_ospf_act as meta
        return meta._meta_table['ActOspfInstanceVrfRpc']['meta_info']



""" Cisco_IOS_XR_iedge4710_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR iedge4710 package configuration.

This module contains definitions
for the following management objects\:
  subscriber\-manager\: iEdge subscriber manager configuration
  subscriber\-featurette\: subscriber featurette
  iedge\-license\-manager\: iedge license manager
  sub\-manager\: sub manager

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class SubscriberManager(object):
    """
    iEdge subscriber manager configuration
    
    .. attribute:: accounting
    
    	iEdge accounting feature
    	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.SubscriberManager.Accounting>`
    
    .. attribute:: srg
    
    	SRG specific config
    	**type**\:   :py:class:`Srg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.SubscriberManager.Srg>`
    
    

    """

    _prefix = 'iedge4710-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.accounting = SubscriberManager.Accounting()
        self.accounting.parent = self
        self.srg = SubscriberManager.Srg()
        self.srg.parent = self


    class Accounting(object):
        """
        iEdge accounting feature
        
        .. attribute:: interim
        
        	interim accounting related
        	**type**\:   :py:class:`Interim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.SubscriberManager.Accounting.Interim>`
        
        .. attribute:: send_stop
        
        	Accounting send stop feature
        	**type**\:   :py:class:`SendStop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.SubscriberManager.Accounting.SendStop>`
        
        

        """

        _prefix = 'iedge4710-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.interim = SubscriberManager.Accounting.Interim()
            self.interim.parent = self
            self.send_stop = SubscriberManager.Accounting.SendStop()
            self.send_stop.parent = self


        class SendStop(object):
            """
            Accounting send stop feature
            
            .. attribute:: setup_failure
            
            	Set up failure feature
            	**type**\:  str
            
            

            """

            _prefix = 'iedge4710-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.setup_failure = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-iedge4710-cfg:subscriber-manager/Cisco-IOS-XR-iedge4710-cfg:accounting/Cisco-IOS-XR-iedge4710-cfg:send-stop'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.setup_failure is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_cfg as meta
                return meta._meta_table['SubscriberManager.Accounting.SendStop']['meta_info']


        class Interim(object):
            """
            interim accounting related
            
            .. attribute:: variation
            
            	variation of first session or service interim record from configured timeout
            	**type**\:   :py:class:`Variation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.SubscriberManager.Accounting.Interim.Variation>`
            
            

            """

            _prefix = 'iedge4710-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.variation = SubscriberManager.Accounting.Interim.Variation()
                self.variation.parent = self


            class Variation(object):
                """
                variation of first session or service interim
                record from configured timeout
                
                .. attribute:: maximum_percentage_variation
                
                	maximum percentage variation (maximum absolute variation is 15 minutes)
                	**type**\:  int
                
                	**range:** 0..50
                
                	**units**\: percentage
                
                

                """

                _prefix = 'iedge4710-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.maximum_percentage_variation = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-iedge4710-cfg:subscriber-manager/Cisco-IOS-XR-iedge4710-cfg:accounting/Cisco-IOS-XR-iedge4710-cfg:interim/Cisco-IOS-XR-iedge4710-cfg:variation'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.maximum_percentage_variation is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_cfg as meta
                    return meta._meta_table['SubscriberManager.Accounting.Interim.Variation']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-iedge4710-cfg:subscriber-manager/Cisco-IOS-XR-iedge4710-cfg:accounting/Cisco-IOS-XR-iedge4710-cfg:interim'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.variation is not None and self.variation._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_cfg as meta
                return meta._meta_table['SubscriberManager.Accounting.Interim']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-iedge4710-cfg:subscriber-manager/Cisco-IOS-XR-iedge4710-cfg:accounting'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.interim is not None and self.interim._has_data():
                return True

            if self.send_stop is not None and self.send_stop._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_cfg as meta
            return meta._meta_table['SubscriberManager.Accounting']['meta_info']


    class Srg(object):
        """
        SRG specific config
        
        .. attribute:: sync_account_session_id
        
        	sync account session id from master to slave
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'iedge4710-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.sync_account_session_id = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-iedge4710-cfg:subscriber-manager/Cisco-IOS-XR-iedge4710-cfg:srg'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.sync_account_session_id is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_cfg as meta
            return meta._meta_table['SubscriberManager.Srg']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-iedge4710-cfg:subscriber-manager'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.accounting is not None and self.accounting._has_data():
            return True

        if self.srg is not None and self.srg._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_cfg as meta
        return meta._meta_table['SubscriberManager']['meta_info']


class SubscriberFeaturette(object):
    """
    subscriber featurette
    
    .. attribute:: identity_change
    
    	enable identity change processing
    	**type**\: list of    :py:class:`IdentityChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.SubscriberFeaturette.IdentityChange>`
    
    

    """

    _prefix = 'iedge4710-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.identity_change = YList()
        self.identity_change.parent = self
        self.identity_change.name = 'identity_change'


    class IdentityChange(object):
        """
        enable identity change processing
        
        .. attribute:: identity_change  <key>
        
        	identity change
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: enable
        
        	instance of identity\-change
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'iedge4710-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.identity_change = None
            self.enable = None

        @property
        def _common_path(self):
            if self.identity_change is None:
                raise YPYModelError('Key property identity_change is None')

            return '/Cisco-IOS-XR-iedge4710-cfg:subscriber-featurette/Cisco-IOS-XR-iedge4710-cfg:identity-change[Cisco-IOS-XR-iedge4710-cfg:identity-change = ' + str(self.identity_change) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.identity_change is not None:
                return True

            if self.enable is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_cfg as meta
            return meta._meta_table['SubscriberFeaturette.IdentityChange']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-iedge4710-cfg:subscriber-featurette'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.identity_change is not None:
            for child_ref in self.identity_change:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_cfg as meta
        return meta._meta_table['SubscriberFeaturette']['meta_info']


class IedgeLicenseManager(object):
    """
    iedge license manager
    
    .. attribute:: node
    
    	Location. For eg., 0/1/CPU0
    	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.IedgeLicenseManager.Node>`
    
    

    """

    _prefix = 'iedge4710-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.node = YList()
        self.node.parent = self
        self.node.name = 'node'


    class Node(object):
        """
        Location. For eg., 0/1/CPU0
        
        .. attribute:: node_name  <key>
        
        	The node id to filter on. For eg., 0/1/CPU0
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: session_limit
        
        	Session limit configured on linecard
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: session_threshold
        
        	Session threshold configured on linecard
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'iedge4710-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node_name = None
            self.session_limit = None
            self.session_threshold = None

        @property
        def _common_path(self):
            if self.node_name is None:
                raise YPYModelError('Key property node_name is None')

            return '/Cisco-IOS-XR-iedge4710-cfg:iedge-license-manager/Cisco-IOS-XR-iedge4710-cfg:node[Cisco-IOS-XR-iedge4710-cfg:node-name = ' + str(self.node_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.node_name is not None:
                return True

            if self.session_limit is not None:
                return True

            if self.session_threshold is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_cfg as meta
            return meta._meta_table['IedgeLicenseManager.Node']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-iedge4710-cfg:iedge-license-manager'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.node is not None:
            for child_ref in self.node:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_cfg as meta
        return meta._meta_table['IedgeLicenseManager']['meta_info']


class SubManager(object):
    """
    sub manager
    
    .. attribute:: location
    
    	Select location
    	**type**\: list of    :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.SubManager.Location>`
    
    

    """

    _prefix = 'iedge4710-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.location = YList()
        self.location.parent = self
        self.location.name = 'location'


    class Location(object):
        """
        Select location
        
        .. attribute:: location1  <key>
        
        	Specify location
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: history
        
        	Disable history for subscriber manager
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: trace
        
        	Subscriber manager trace
        	**type**\:   :py:class:`Trace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.SubManager.Location.Trace>`
        
        

        """

        _prefix = 'iedge4710-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.location1 = None
            self.history = None
            self.trace = SubManager.Location.Trace()
            self.trace.parent = self


        class Trace(object):
            """
            Subscriber manager trace
            
            .. attribute:: trace_level
            
            	Subscriber manager trace level
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'iedge4710-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.trace_level = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-cfg:trace'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.trace_level is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_cfg as meta
                return meta._meta_table['SubManager.Location.Trace']['meta_info']

        @property
        def _common_path(self):
            if self.location1 is None:
                raise YPYModelError('Key property location1 is None')

            return '/Cisco-IOS-XR-iedge4710-cfg:sub-manager/Cisco-IOS-XR-iedge4710-cfg:location[Cisco-IOS-XR-iedge4710-cfg:location1 = ' + str(self.location1) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.location1 is not None:
                return True

            if self.history is not None:
                return True

            if self.trace is not None and self.trace._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_cfg as meta
            return meta._meta_table['SubManager.Location']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-iedge4710-cfg:sub-manager'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.location is not None:
            for child_ref in self.location:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_cfg as meta
        return meta._meta_table['SubManager']['meta_info']



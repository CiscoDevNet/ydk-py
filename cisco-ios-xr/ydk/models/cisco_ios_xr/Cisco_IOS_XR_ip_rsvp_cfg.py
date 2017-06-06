""" Cisco_IOS_XR_ip_rsvp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-rsvp package configuration.

This module contains definitions
for the following management objects\:
  rsvp\: Global RSVP configuration commands

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class RsvpBc0Enum(Enum):
    """
    RsvpBc0Enum

    Rsvp bc0

    .. data:: bc0 = 1

    	Keyword is bc0

    .. data:: global_pool = 2

    	Keyword is global-pool

    .. data:: not_specified = 3

    	Keyword is not specified

    """

    bc0 = 1

    global_pool = 2

    not_specified = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
        return meta._meta_table['RsvpBc0Enum']


class RsvpBc1Enum(Enum):
    """
    RsvpBc1Enum

    Rsvp bc1

    .. data:: bc1 = 1

    	Keyword is bc1

    .. data:: sub_pool = 2

    	Keyword is sub-pool

    """

    bc1 = 1

    sub_pool = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
        return meta._meta_table['RsvpBc1Enum']


class RsvpBwCfgEnum(Enum):
    """
    RsvpBwCfgEnum

    Rsvp bw cfg

    .. data:: absolute = 0

    	Configuration is in absolute bandwidth values

    .. data:: percentage = 1

    	Configuration is in percentage of physical

    	bandwidth values

    """

    absolute = 0

    percentage = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
        return meta._meta_table['RsvpBwCfgEnum']


class RsvpRdmEnum(Enum):
    """
    RsvpRdmEnum

    Rsvp rdm

    .. data:: rdm = 1

    	RDM Keyword Specified

    .. data:: not_specified = 2

    	RDM Keyword Not Specified

    .. data:: use_default_bandwidth = 3

    	Use Default Bandwidth - 75% Link Bandwidth

    """

    rdm = 1

    not_specified = 2

    use_default_bandwidth = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
        return meta._meta_table['RsvpRdmEnum']



class Rsvp(object):
    """
    Global RSVP configuration commands
    
    .. attribute:: authentication
    
    	Configure RSVP authentication
    	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Authentication>`
    
    .. attribute:: controllers
    
    	Controller table
    	**type**\:   :py:class:`Controllers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Controllers>`
    
    .. attribute:: global_bandwidth
    
    	Configure Global Bandwidth Parameters
    	**type**\:   :py:class:`GlobalBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.GlobalBandwidth>`
    
    .. attribute:: global_logging
    
    	Global Logging
    	**type**\:   :py:class:`GlobalLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.GlobalLogging>`
    
    .. attribute:: interfaces
    
    	Interface table
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces>`
    
    .. attribute:: neighbors
    
    	RSVP Neighbor Table
    	**type**\:   :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Neighbors>`
    
    .. attribute:: signalling
    
    	Configure Global RSVP signalling parameters
    	**type**\:   :py:class:`Signalling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Signalling>`
    
    

    """

    _prefix = 'ip-rsvp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.authentication = Rsvp.Authentication()
        self.authentication.parent = self
        self.controllers = Rsvp.Controllers()
        self.controllers.parent = self
        self.global_bandwidth = Rsvp.GlobalBandwidth()
        self.global_bandwidth.parent = self
        self.global_logging = Rsvp.GlobalLogging()
        self.global_logging.parent = self
        self.interfaces = Rsvp.Interfaces()
        self.interfaces.parent = self
        self.neighbors = Rsvp.Neighbors()
        self.neighbors.parent = self
        self.signalling = Rsvp.Signalling()
        self.signalling.parent = self


    class Neighbors(object):
        """
        RSVP Neighbor Table
        
        .. attribute:: neighbor
        
        	RSVP neighbor configuration
        	**type**\: list of    :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Neighbors.Neighbor>`
        
        

        """

        _prefix = 'ip-rsvp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.neighbor = YList()
            self.neighbor.parent = self
            self.neighbor.name = 'neighbor'


        class Neighbor(object):
            """
            RSVP neighbor configuration
            
            .. attribute:: neighbor  <key>
            
            	Neighbor IP address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: authentication
            
            	Configure RSVP authentication
            	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Neighbors.Neighbor.Authentication>`
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.neighbor = None
                self.authentication = Rsvp.Neighbors.Neighbor.Authentication()
                self.authentication.parent = self


            class Authentication(object):
                """
                Configure RSVP authentication
                
                .. attribute:: enable
                
                	Enable or disable RSVP authentication
                	**type**\:  bool
                
                .. attribute:: key_chain
                
                	Key chain to authenticate RSVP signalling messages
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: life_time
                
                	Life time (in seconds) for each security association
                	**type**\:  int
                
                	**range:** 30..86400
                
                	**units**\: second
                
                .. attribute:: window_size
                
                	Window\-size to limit number of out\-of\-order messages
                	**type**\:  int
                
                	**range:** 1..64
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.enable = None
                    self.key_chain = None
                    self.life_time = None
                    self.window_size = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-rsvp-cfg:authentication'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.enable is not None:
                        return True

                    if self.key_chain is not None:
                        return True

                    if self.life_time is not None:
                        return True

                    if self.window_size is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
                    return meta._meta_table['Rsvp.Neighbors.Neighbor.Authentication']['meta_info']

            @property
            def _common_path(self):
                if self.neighbor is None:
                    raise YPYModelError('Key property neighbor is None')

                return '/Cisco-IOS-XR-ip-rsvp-cfg:rsvp/Cisco-IOS-XR-ip-rsvp-cfg:neighbors/Cisco-IOS-XR-ip-rsvp-cfg:neighbor[Cisco-IOS-XR-ip-rsvp-cfg:neighbor = ' + str(self.neighbor) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.neighbor is not None:
                    return True

                if self.authentication is not None and self.authentication._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
                return meta._meta_table['Rsvp.Neighbors.Neighbor']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-rsvp-cfg:rsvp/Cisco-IOS-XR-ip-rsvp-cfg:neighbors'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.neighbor is not None:
                for child_ref in self.neighbor:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
            return meta._meta_table['Rsvp.Neighbors']['meta_info']


    class Controllers(object):
        """
        Controller table
        
        .. attribute:: controller
        
        	Controller configuration
        	**type**\: list of    :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Controllers.Controller>`
        
        

        """

        _prefix = 'ip-rsvp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.controller = YList()
            self.controller.parent = self
            self.controller.name = 'controller'


        class Controller(object):
            """
            Controller configuration
            
            .. attribute:: controller_name  <key>
            
            	Name of controller
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: cntl_signalling
            
            	Configure RSVP signalling parameters
            	**type**\:   :py:class:`CntlSignalling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Controllers.Controller.CntlSignalling>`
            
            .. attribute:: enable
            
            	Enable RSVP on an interface
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.controller_name = None
                self.cntl_signalling = Rsvp.Controllers.Controller.CntlSignalling()
                self.cntl_signalling.parent = self
                self.enable = None


            class CntlSignalling(object):
                """
                Configure RSVP signalling parameters
                
                .. attribute:: out_of_band
                
                	Configure RSVP out\-of\-band signalling parameters
                	**type**\:   :py:class:`OutOfBand <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Controllers.Controller.CntlSignalling.OutOfBand>`
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.out_of_band = Rsvp.Controllers.Controller.CntlSignalling.OutOfBand()
                    self.out_of_band.parent = self


                class OutOfBand(object):
                    """
                    Configure RSVP out\-of\-band signalling parameters
                    
                    .. attribute:: missed_messages
                    
                    	Configure max number of consecutive missed messages for state expiry for out\-of\-band tunnels
                    	**type**\:  int
                    
                    	**range:** 1..110000
                    
                    	**default value**\: 38000
                    
                    .. attribute:: refresh_interval
                    
                    	Configure interval between successive refreshes for out\-of\-band tunnels
                    	**type**\:  int
                    
                    	**range:** 180..86400
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'ip-rsvp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.missed_messages = None
                        self.refresh_interval = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rsvp-cfg:out-of-band'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.missed_messages is not None:
                            return True

                        if self.refresh_interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
                        return meta._meta_table['Rsvp.Controllers.Controller.CntlSignalling.OutOfBand']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-rsvp-cfg:cntl-signalling'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.out_of_band is not None and self.out_of_band._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
                    return meta._meta_table['Rsvp.Controllers.Controller.CntlSignalling']['meta_info']

            @property
            def _common_path(self):
                if self.controller_name is None:
                    raise YPYModelError('Key property controller_name is None')

                return '/Cisco-IOS-XR-ip-rsvp-cfg:rsvp/Cisco-IOS-XR-ip-rsvp-cfg:controllers/Cisco-IOS-XR-ip-rsvp-cfg:controller[Cisco-IOS-XR-ip-rsvp-cfg:controller-name = ' + str(self.controller_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.controller_name is not None:
                    return True

                if self.cntl_signalling is not None and self.cntl_signalling._has_data():
                    return True

                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
                return meta._meta_table['Rsvp.Controllers.Controller']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-rsvp-cfg:rsvp/Cisco-IOS-XR-ip-rsvp-cfg:controllers'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.controller is not None:
                for child_ref in self.controller:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
            return meta._meta_table['Rsvp.Controllers']['meta_info']


    class GlobalLogging(object):
        """
        Global Logging
        
        .. attribute:: log_issu_status
        
        	Enable ISSU Status Logging
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: log_nsr_status
        
        	Enable NSR Status Logging
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ip-rsvp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.log_issu_status = None
            self.log_nsr_status = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-rsvp-cfg:rsvp/Cisco-IOS-XR-ip-rsvp-cfg:global-logging'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.log_issu_status is not None:
                return True

            if self.log_nsr_status is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
            return meta._meta_table['Rsvp.GlobalLogging']['meta_info']


    class GlobalBandwidth(object):
        """
        Configure Global Bandwidth Parameters
        
        .. attribute:: default_interface_percent
        
        	Configure Global RSVP signalling parameters
        	**type**\:   :py:class:`DefaultInterfacePercent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.GlobalBandwidth.DefaultInterfacePercent>`
        
        

        """

        _prefix = 'ip-rsvp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.default_interface_percent = Rsvp.GlobalBandwidth.DefaultInterfacePercent()
            self.default_interface_percent.parent = self


        class DefaultInterfacePercent(object):
            """
            Configure Global RSVP signalling parameters
            
            .. attribute:: mam
            
            	Configure global default MAM I/F percent bandwidth parameters
            	**type**\:   :py:class:`Mam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.GlobalBandwidth.DefaultInterfacePercent.Mam>`
            
            .. attribute:: rdm
            
            	Configure global default RDM I/F percent bandwidth parameters
            	**type**\:   :py:class:`Rdm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.GlobalBandwidth.DefaultInterfacePercent.Rdm>`
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.mam = Rsvp.GlobalBandwidth.DefaultInterfacePercent.Mam()
                self.mam.parent = self
                self.rdm = Rsvp.GlobalBandwidth.DefaultInterfacePercent.Rdm()
                self.rdm.parent = self


            class Mam(object):
                """
                Configure global default MAM I/F percent
                bandwidth parameters
                
                .. attribute:: bc0_percent
                
                	Default BC0 pool I/F % B/W 
                	**type**\:  int
                
                	**range:** 0..10000
                
                .. attribute:: bc1_percent
                
                	Default BC1 pool I/F % B/W 
                	**type**\:  int
                
                	**range:** 0..10000
                
                .. attribute:: max_res_percent
                
                	Default maximum reservable I/F % B/W 
                	**type**\:  int
                
                	**range:** 0..10000
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bc0_percent = None
                    self.bc1_percent = None
                    self.max_res_percent = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-rsvp-cfg:rsvp/Cisco-IOS-XR-ip-rsvp-cfg:global-bandwidth/Cisco-IOS-XR-ip-rsvp-cfg:default-interface-percent/Cisco-IOS-XR-ip-rsvp-cfg:mam'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.bc0_percent is not None:
                        return True

                    if self.bc1_percent is not None:
                        return True

                    if self.max_res_percent is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
                    return meta._meta_table['Rsvp.GlobalBandwidth.DefaultInterfacePercent.Mam']['meta_info']


            class Rdm(object):
                """
                Configure global default RDM I/F percent
                bandwidth parameters
                
                .. attribute:: bc0_percent
                
                	Default BC0 pool I/F % B/W 
                	**type**\:  int
                
                	**range:** 0..10000
                
                .. attribute:: bc1_percent
                
                	Default BC1 pool I/F % B/W 
                	**type**\:  int
                
                	**range:** 0..10000
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bc0_percent = None
                    self.bc1_percent = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-rsvp-cfg:rsvp/Cisco-IOS-XR-ip-rsvp-cfg:global-bandwidth/Cisco-IOS-XR-ip-rsvp-cfg:default-interface-percent/Cisco-IOS-XR-ip-rsvp-cfg:rdm'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.bc0_percent is not None:
                        return True

                    if self.bc1_percent is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
                    return meta._meta_table['Rsvp.GlobalBandwidth.DefaultInterfacePercent.Rdm']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-rsvp-cfg:rsvp/Cisco-IOS-XR-ip-rsvp-cfg:global-bandwidth/Cisco-IOS-XR-ip-rsvp-cfg:default-interface-percent'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.mam is not None and self.mam._has_data():
                    return True

                if self.rdm is not None and self.rdm._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
                return meta._meta_table['Rsvp.GlobalBandwidth.DefaultInterfacePercent']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-rsvp-cfg:rsvp/Cisco-IOS-XR-ip-rsvp-cfg:global-bandwidth'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.default_interface_percent is not None and self.default_interface_percent._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
            return meta._meta_table['Rsvp.GlobalBandwidth']['meta_info']


    class Interfaces(object):
        """
        Interface table
        
        .. attribute:: interface
        
        	Interface configuration
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface>`
        
        

        """

        _prefix = 'ip-rsvp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.interface = YList()
            self.interface.parent = self
            self.interface.name = 'interface'


        class Interface(object):
            """
            Interface configuration
            
            .. attribute:: name  <key>
            
            	Name of interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: authentication
            
            	Configure RSVP authentication
            	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.Authentication>`
            
            .. attribute:: bandwidth
            
            	Configure Bandwidth
            	**type**\:   :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.Bandwidth>`
            
            .. attribute:: enable
            
            	Enable RSVP on an interface
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: if_signalling
            
            	Configure RSVP signalling parameters
            	**type**\:   :py:class:`IfSignalling <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.IfSignalling>`
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.name = None
                self.authentication = Rsvp.Interfaces.Interface.Authentication()
                self.authentication.parent = self
                self.bandwidth = Rsvp.Interfaces.Interface.Bandwidth()
                self.bandwidth.parent = self
                self.enable = None
                self.if_signalling = Rsvp.Interfaces.Interface.IfSignalling()
                self.if_signalling.parent = self


            class IfSignalling(object):
                """
                Configure RSVP signalling parameters
                
                .. attribute:: dscp
                
                	Differentiated Services Code Point (DSCP)
                	**type**\:  int
                
                	**range:** 0..63
                
                .. attribute:: hello_graceful_restart_if_based
                
                	Enable IF\-based Hello adjacency on a RSVP interface
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: interval_rate
                
                	Configure number of messages to be sent per interval
                	**type**\:   :py:class:`IntervalRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.IfSignalling.IntervalRate>`
                
                .. attribute:: missed_messages
                
                	Configure max number of consecutive missed messages for state expiry
                	**type**\:  int
                
                	**range:** 1..8
                
                	**default value**\: 4
                
                .. attribute:: out_of_band
                
                	Configure RSVP out\-of\-band signalling parameters
                	**type**\:   :py:class:`OutOfBand <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.IfSignalling.OutOfBand>`
                
                .. attribute:: pacing
                
                	Enable rate\-limiting on the interface
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: refresh_interval
                
                	Configure interval between successive refreshes
                	**type**\:  int
                
                	**range:** 10..180
                
                	**units**\: second
                
                	**default value**\: 45
                
                .. attribute:: refresh_reduction
                
                	Configure RSVP Refresh Reduction parameters
                	**type**\:   :py:class:`RefreshReduction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.IfSignalling.RefreshReduction>`
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.dscp = None
                    self.hello_graceful_restart_if_based = None
                    self.interval_rate = Rsvp.Interfaces.Interface.IfSignalling.IntervalRate()
                    self.interval_rate.parent = self
                    self.missed_messages = None
                    self.out_of_band = Rsvp.Interfaces.Interface.IfSignalling.OutOfBand()
                    self.out_of_band.parent = self
                    self.pacing = None
                    self.refresh_interval = None
                    self.refresh_reduction = Rsvp.Interfaces.Interface.IfSignalling.RefreshReduction()
                    self.refresh_reduction.parent = self


                class RefreshReduction(object):
                    """
                    Configure RSVP Refresh Reduction parameters
                    
                    .. attribute:: bundle_message_max_size
                    
                    	Configure maximum size of a single RSVP Bundle message
                    	**type**\:  int
                    
                    	**range:** 512..65000
                    
                    	**units**\: byte
                    
                    	**default value**\: 4096
                    
                    .. attribute:: disable
                    
                    	Disable refresh reduction
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: reliable_ack_hold_time
                    
                    	Configure hold time for sending RSVP ACK message(s)
                    	**type**\:  int
                    
                    	**range:** 100..5000
                    
                    	**units**\: millisecond
                    
                    	**default value**\: 400
                    
                    .. attribute:: reliable_ack_max_size
                    
                    	Configure max size of a single RSVP ACK message
                    	**type**\:  int
                    
                    	**range:** 20..65000
                    
                    	**units**\: byte
                    
                    	**default value**\: 4096
                    
                    .. attribute:: reliable_retransmit_time
                    
                    	Configure min delay to wait for an ACK before a retransmit
                    	**type**\:  int
                    
                    	**range:** 100..10000
                    
                    	**units**\: millisecond
                    
                    	**default value**\: 2100
                    
                    .. attribute:: reliable_s_refresh
                    
                    	Configure use of reliable messaging for summary refresh
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: summary_max_size
                    
                    	Configure max size of a single RSVP summary refresh message
                    	**type**\:  int
                    
                    	**range:** 20..65000
                    
                    	**units**\: byte
                    
                    	**default value**\: 4096
                    
                    

                    """

                    _prefix = 'ip-rsvp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.bundle_message_max_size = None
                        self.disable = None
                        self.reliable_ack_hold_time = None
                        self.reliable_ack_max_size = None
                        self.reliable_retransmit_time = None
                        self.reliable_s_refresh = None
                        self.summary_max_size = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rsvp-cfg:refresh-reduction'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.bundle_message_max_size is not None:
                            return True

                        if self.disable is not None:
                            return True

                        if self.reliable_ack_hold_time is not None:
                            return True

                        if self.reliable_ack_max_size is not None:
                            return True

                        if self.reliable_retransmit_time is not None:
                            return True

                        if self.reliable_s_refresh is not None:
                            return True

                        if self.summary_max_size is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
                        return meta._meta_table['Rsvp.Interfaces.Interface.IfSignalling.RefreshReduction']['meta_info']


                class IntervalRate(object):
                    """
                    Configure number of messages to be sent per
                    interval
                    
                    .. attribute:: interval_size
                    
                    	Size of an interval (milliseconds)
                    	**type**\:  int
                    
                    	**range:** 250..2000
                    
                    	**units**\: millisecond
                    
                    	**default value**\: 1000
                    
                    .. attribute:: messages_per_interval
                    
                    	Number of messages to be sent per interval
                    	**type**\:  int
                    
                    	**range:** 1..500
                    
                    	**default value**\: 100
                    
                    

                    """

                    _prefix = 'ip-rsvp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interval_size = None
                        self.messages_per_interval = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rsvp-cfg:interval-rate'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.interval_size is not None:
                            return True

                        if self.messages_per_interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
                        return meta._meta_table['Rsvp.Interfaces.Interface.IfSignalling.IntervalRate']['meta_info']


                class OutOfBand(object):
                    """
                    Configure RSVP out\-of\-band signalling parameters
                    
                    .. attribute:: missed_messages
                    
                    	Configure max number of consecutive missed messages for state expiry for out\-of\-band tunnels
                    	**type**\:  int
                    
                    	**range:** 1..110000
                    
                    	**default value**\: 38000
                    
                    .. attribute:: refresh_interval
                    
                    	Configure interval between successive refreshes for out\-of\-band tunnels
                    	**type**\:  int
                    
                    	**range:** 180..86400
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'ip-rsvp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.missed_messages = None
                        self.refresh_interval = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rsvp-cfg:out-of-band'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.missed_messages is not None:
                            return True

                        if self.refresh_interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
                        return meta._meta_table['Rsvp.Interfaces.Interface.IfSignalling.OutOfBand']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-rsvp-cfg:if-signalling'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.dscp is not None:
                        return True

                    if self.hello_graceful_restart_if_based is not None:
                        return True

                    if self.interval_rate is not None and self.interval_rate._has_data():
                        return True

                    if self.missed_messages is not None:
                        return True

                    if self.out_of_band is not None and self.out_of_band._has_data():
                        return True

                    if self.pacing is not None:
                        return True

                    if self.refresh_interval is not None:
                        return True

                    if self.refresh_reduction is not None and self.refresh_reduction._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
                    return meta._meta_table['Rsvp.Interfaces.Interface.IfSignalling']['meta_info']


            class Bandwidth(object):
                """
                Configure Bandwidth
                
                .. attribute:: mam
                
                	Configure MAM bandwidth parameters
                	**type**\:   :py:class:`Mam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.Bandwidth.Mam>`
                
                .. attribute:: rdm
                
                	Configure RDM bandwidth parameters
                	**type**\:   :py:class:`Rdm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Interfaces.Interface.Bandwidth.Rdm>`
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.mam = Rsvp.Interfaces.Interface.Bandwidth.Mam()
                    self.mam.parent = self
                    self.rdm = Rsvp.Interfaces.Interface.Bandwidth.Rdm()
                    self.rdm.parent = self


                class Mam(object):
                    """
                    Configure MAM bandwidth parameters
                    
                    .. attribute:: bandwidth_mode
                    
                    	Absolute or Percentage bandwidth mode
                    	**type**\:   :py:class:`RsvpBwCfgEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.RsvpBwCfgEnum>`
                    
                    	**units**\: percentage
                    
                    .. attribute:: bc0_bandwidth
                    
                    	Reservable bandwidth in BC0 (Kbps or percent of physical bandwidth)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bc1_bandwidth
                    
                    	Reservable bandwidth in BC1 (Kbps or percent of physical bandwidth)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max_resv_bandwidth
                    
                    	Maximum reservable bandwidth (Kbps or percent of physical bandwidth)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max_resv_flow
                    
                    	Largest reservable flow (Kbps or percent of physical bandwidth)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-rsvp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.bandwidth_mode = None
                        self.bc0_bandwidth = None
                        self.bc1_bandwidth = None
                        self.max_resv_bandwidth = None
                        self.max_resv_flow = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rsvp-cfg:mam'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.bandwidth_mode is not None:
                            return True

                        if self.bc0_bandwidth is not None:
                            return True

                        if self.bc1_bandwidth is not None:
                            return True

                        if self.max_resv_bandwidth is not None:
                            return True

                        if self.max_resv_flow is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
                        return meta._meta_table['Rsvp.Interfaces.Interface.Bandwidth.Mam']['meta_info']


                class Rdm(object):
                    """
                    Configure RDM bandwidth parameters
                    
                    .. attribute:: bandwidth_mode
                    
                    	Absolute or Percentage bandwidth mode
                    	**type**\:   :py:class:`RsvpBwCfgEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.RsvpBwCfgEnum>`
                    
                    	**units**\: percentage
                    
                    .. attribute:: bc0_bandwidth
                    
                    	Reservable bandwidth in BC0 (Kbps or percent of physical bandwidth)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bc0_keyword
                    
                    	Set requests should always use BC0
                    	**type**\:   :py:class:`RsvpBc0Enum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.RsvpBc0Enum>`
                    
                    .. attribute:: bc1_bandwidth
                    
                    	Reservable bandwidth in BC1 (Kbps or percent of physical bandwidth)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bc1_keyword
                    
                    	Set requests should always use BC1
                    	**type**\:   :py:class:`RsvpBc1Enum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.RsvpBc1Enum>`
                    
                    .. attribute:: max_resv_flow
                    
                    	Largest reservable flow (Kbps or percent of physical bandwidth)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rdm_keyword
                    
                    	Set requests should always use RDM
                    	**type**\:   :py:class:`RsvpRdmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.RsvpRdmEnum>`
                    
                    

                    """

                    _prefix = 'ip-rsvp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.bandwidth_mode = None
                        self.bc0_bandwidth = None
                        self.bc0_keyword = None
                        self.bc1_bandwidth = None
                        self.bc1_keyword = None
                        self.max_resv_flow = None
                        self.rdm_keyword = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rsvp-cfg:rdm'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.bandwidth_mode is not None:
                            return True

                        if self.bc0_bandwidth is not None:
                            return True

                        if self.bc0_keyword is not None:
                            return True

                        if self.bc1_bandwidth is not None:
                            return True

                        if self.bc1_keyword is not None:
                            return True

                        if self.max_resv_flow is not None:
                            return True

                        if self.rdm_keyword is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
                        return meta._meta_table['Rsvp.Interfaces.Interface.Bandwidth.Rdm']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-rsvp-cfg:bandwidth'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.mam is not None and self.mam._has_data():
                        return True

                    if self.rdm is not None and self.rdm._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
                    return meta._meta_table['Rsvp.Interfaces.Interface.Bandwidth']['meta_info']


            class Authentication(object):
                """
                Configure RSVP authentication
                
                .. attribute:: enable
                
                	Enable or disable RSVP authentication
                	**type**\:  bool
                
                .. attribute:: key_chain
                
                	Key chain to authenticate RSVP signalling messages
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: life_time
                
                	Life time (in seconds) for each security association
                	**type**\:  int
                
                	**range:** 30..86400
                
                	**units**\: second
                
                .. attribute:: window_size
                
                	Window\-size to limit number of out\-of\-order messages
                	**type**\:  int
                
                	**range:** 1..64
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.enable = None
                    self.key_chain = None
                    self.life_time = None
                    self.window_size = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-rsvp-cfg:authentication'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.enable is not None:
                        return True

                    if self.key_chain is not None:
                        return True

                    if self.life_time is not None:
                        return True

                    if self.window_size is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
                    return meta._meta_table['Rsvp.Interfaces.Interface.Authentication']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-ip-rsvp-cfg:rsvp/Cisco-IOS-XR-ip-rsvp-cfg:interfaces/Cisco-IOS-XR-ip-rsvp-cfg:interface[Cisco-IOS-XR-ip-rsvp-cfg:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.authentication is not None and self.authentication._has_data():
                    return True

                if self.bandwidth is not None and self.bandwidth._has_data():
                    return True

                if self.enable is not None:
                    return True

                if self.if_signalling is not None and self.if_signalling._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
                return meta._meta_table['Rsvp.Interfaces.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-rsvp-cfg:rsvp/Cisco-IOS-XR-ip-rsvp-cfg:interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.interface is not None:
                for child_ref in self.interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
            return meta._meta_table['Rsvp.Interfaces']['meta_info']


    class Signalling(object):
        """
        Configure Global RSVP signalling parameters
        
        .. attribute:: checksum
        
        	RSVP message checksum computation
        	**type**\:   :py:class:`Checksum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Signalling.Checksum>`
        
        .. attribute:: global_out_of_band
        
        	Configure out\-of\-band signalling parameters
        	**type**\:   :py:class:`GlobalOutOfBand <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Signalling.GlobalOutOfBand>`
        
        .. attribute:: graceful_restart
        
        	Configure RSVP Graceful\-Restart parameters
        	**type**\:   :py:class:`GracefulRestart <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Signalling.GracefulRestart>`
        
        .. attribute:: hello_graceful_restart_interval
        
        	Configure interval between successive Hello messages
        	**type**\:  int
        
        	**range:** 3000..30000
        
        	**units**\: millisecond
        
        	**default value**\: 5000
        
        .. attribute:: hello_graceful_restart_misses
        
        	Configure max number of consecutive missed Hello messages
        	**type**\:  int
        
        	**range:** 1..10
        
        	**default value**\: 3
        
        .. attribute:: pesr
        
        	Sending Path Error with State\-Removal flag
        	**type**\:   :py:class:`Pesr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Signalling.Pesr>`
        
        .. attribute:: prefix_filtering
        
        	Configure prefix filtering parameters
        	**type**\:   :py:class:`PrefixFiltering <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Signalling.PrefixFiltering>`
        
        

        """

        _prefix = 'ip-rsvp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.checksum = Rsvp.Signalling.Checksum()
            self.checksum.parent = self
            self.global_out_of_band = Rsvp.Signalling.GlobalOutOfBand()
            self.global_out_of_band.parent = self
            self.graceful_restart = Rsvp.Signalling.GracefulRestart()
            self.graceful_restart.parent = self
            self.hello_graceful_restart_interval = None
            self.hello_graceful_restart_misses = None
            self.pesr = Rsvp.Signalling.Pesr()
            self.pesr.parent = self
            self.prefix_filtering = Rsvp.Signalling.PrefixFiltering()
            self.prefix_filtering.parent = self


        class GlobalOutOfBand(object):
            """
            Configure out\-of\-band signalling parameters
            
            .. attribute:: vrf
            
            	VRF used for out\-of\-band control signalling
            	**type**\:  str
            
            	**length:** 1..32
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.vrf = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-rsvp-cfg:rsvp/Cisco-IOS-XR-ip-rsvp-cfg:signalling/Cisco-IOS-XR-ip-rsvp-cfg:global-out-of-band'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.vrf is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
                return meta._meta_table['Rsvp.Signalling.GlobalOutOfBand']['meta_info']


        class GracefulRestart(object):
            """
            Configure RSVP Graceful\-Restart parameters
            
            .. attribute:: enable
            
            	Enable RSVP graceful restart
            	**type**\:  bool
            
            .. attribute:: recovery_time
            
            	Graceful restart recovery time (seconds)
            	**type**\:  int
            
            	**range:** 0..3600
            
            	**units**\: second
            
            	**default value**\: 120
            
            .. attribute:: restart_time
            
            	Graceful restart time (seconds)
            	**type**\:  int
            
            	**range:** 60..3600
            
            	**units**\: second
            
            	**default value**\: 120
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None
                self.recovery_time = None
                self.restart_time = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-rsvp-cfg:rsvp/Cisco-IOS-XR-ip-rsvp-cfg:signalling/Cisco-IOS-XR-ip-rsvp-cfg:graceful-restart'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                if self.recovery_time is not None:
                    return True

                if self.restart_time is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
                return meta._meta_table['Rsvp.Signalling.GracefulRestart']['meta_info']


        class PrefixFiltering(object):
            """
            Configure prefix filtering parameters
            
            .. attribute:: acl
            
            	Configure an ACL to perform prefix filtering of RSVP Router Alert messages
            	**type**\:  str
            
            	**length:** 1..65
            
            .. attribute:: default_deny_action
            
            	Configure RSVP behaviour for scenarios where ACL match yields a default (implicit) deny
            	**type**\:   :py:class:`DefaultDenyAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rsvp_cfg.Rsvp.Signalling.PrefixFiltering.DefaultDenyAction>`
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.acl = None
                self.default_deny_action = Rsvp.Signalling.PrefixFiltering.DefaultDenyAction()
                self.default_deny_action.parent = self


            class DefaultDenyAction(object):
                """
                Configure RSVP behaviour for scenarios where
                ACL match yields a default (implicit) deny
                
                .. attribute:: drop
                
                	Configure RSVP to drop packets when ACL match yields a default (implicit) deny
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ip-rsvp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.drop = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ip-rsvp-cfg:rsvp/Cisco-IOS-XR-ip-rsvp-cfg:signalling/Cisco-IOS-XR-ip-rsvp-cfg:prefix-filtering/Cisco-IOS-XR-ip-rsvp-cfg:default-deny-action'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.drop is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
                    return meta._meta_table['Rsvp.Signalling.PrefixFiltering.DefaultDenyAction']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-rsvp-cfg:rsvp/Cisco-IOS-XR-ip-rsvp-cfg:signalling/Cisco-IOS-XR-ip-rsvp-cfg:prefix-filtering'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.acl is not None:
                    return True

                if self.default_deny_action is not None and self.default_deny_action._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
                return meta._meta_table['Rsvp.Signalling.PrefixFiltering']['meta_info']


        class Pesr(object):
            """
            Sending Path Error with State\-Removal flag
            
            .. attribute:: disable
            
            	Disable RSVP PESR
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.disable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-rsvp-cfg:rsvp/Cisco-IOS-XR-ip-rsvp-cfg:signalling/Cisco-IOS-XR-ip-rsvp-cfg:pesr'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.disable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
                return meta._meta_table['Rsvp.Signalling.Pesr']['meta_info']


        class Checksum(object):
            """
            RSVP message checksum computation
            
            .. attribute:: disable
            
            	Disable RSVP message checksum computation
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ip-rsvp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.disable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ip-rsvp-cfg:rsvp/Cisco-IOS-XR-ip-rsvp-cfg:signalling/Cisco-IOS-XR-ip-rsvp-cfg:checksum'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.disable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
                return meta._meta_table['Rsvp.Signalling.Checksum']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-rsvp-cfg:rsvp/Cisco-IOS-XR-ip-rsvp-cfg:signalling'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.checksum is not None and self.checksum._has_data():
                return True

            if self.global_out_of_band is not None and self.global_out_of_band._has_data():
                return True

            if self.graceful_restart is not None and self.graceful_restart._has_data():
                return True

            if self.hello_graceful_restart_interval is not None:
                return True

            if self.hello_graceful_restart_misses is not None:
                return True

            if self.pesr is not None and self.pesr._has_data():
                return True

            if self.prefix_filtering is not None and self.prefix_filtering._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
            return meta._meta_table['Rsvp.Signalling']['meta_info']


    class Authentication(object):
        """
        Configure RSVP authentication
        
        .. attribute:: enable
        
        	Enable or disable RSVP authentication
        	**type**\:  bool
        
        .. attribute:: key_chain
        
        	Key chain to authenticate RSVP signalling messages
        	**type**\:  str
        
        	**length:** 1..32
        
        .. attribute:: life_time
        
        	Life time (in seconds) for each security association
        	**type**\:  int
        
        	**range:** 30..86400
        
        	**units**\: second
        
        .. attribute:: window_size
        
        	Window\-size to limit number of out\-of\-order messages
        	**type**\:  int
        
        	**range:** 1..64
        
        

        """

        _prefix = 'ip-rsvp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.enable = None
            self.key_chain = None
            self.life_time = None
            self.window_size = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-rsvp-cfg:rsvp/Cisco-IOS-XR-ip-rsvp-cfg:authentication'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.enable is not None:
                return True

            if self.key_chain is not None:
                return True

            if self.life_time is not None:
                return True

            if self.window_size is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
            return meta._meta_table['Rsvp.Authentication']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-rsvp-cfg:rsvp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.authentication is not None and self.authentication._has_data():
            return True

        if self.controllers is not None and self.controllers._has_data():
            return True

        if self.global_bandwidth is not None and self.global_bandwidth._has_data():
            return True

        if self.global_logging is not None and self.global_logging._has_data():
            return True

        if self.interfaces is not None and self.interfaces._has_data():
            return True

        if self.neighbors is not None and self.neighbors._has_data():
            return True

        if self.signalling is not None and self.signalling._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_rsvp_cfg as meta
        return meta._meta_table['Rsvp']['meta_info']



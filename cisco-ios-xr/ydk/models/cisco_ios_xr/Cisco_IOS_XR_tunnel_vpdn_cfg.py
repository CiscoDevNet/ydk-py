""" Cisco_IOS_XR_tunnel_vpdn_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tunnel\-vpdn package configuration.

This module contains definitions
for the following management objects\:
  vpdn\: VPDN configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class DfBitEnum(Enum):
    """
    DfBitEnum

    Df bit

    .. data:: clear = 0

    	Clear df bit

    .. data:: reflect = 1

    	Reflect df bit from inner ip header

    .. data:: set = 2

    	Set df bit

    """

    clear = 0

    reflect = 1

    set = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
        return meta._meta_table['DfBitEnum']


class OptionEnum(Enum):
    """
    OptionEnum

    Option

    .. data:: local = 1

    	Log VPDN events locally

    .. data:: user = 2

    	Log VPDN user events

    .. data:: dead_cache = 8

    	Log VPDN dead cache

    .. data:: tunnel_drop = 16

    	Log VPDN tunnel drops

    """

    local = 1

    user = 2

    dead_cache = 8

    tunnel_drop = 16


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
        return meta._meta_table['OptionEnum']



class Vpdn(object):
    """
    VPDN configuration
    
    .. attribute:: caller_id
    
    	Options to apply on calling station ID
    	**type**\:   :py:class:`CallerId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.CallerId>`
    
    .. attribute:: enable
    
    	Enable VPDN configuration. Deletion of this object also causes deletion of all associated objects under VPDN
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: history
    
    	VPDN history logging
    	**type**\:   :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.History>`
    
    .. attribute:: l2tp
    
    	L2TPv2 protocol commands
    	**type**\:   :py:class:`L2Tp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.L2Tp>`
    
    .. attribute:: local
    
    	VPDN Local radius process configuration
    	**type**\:   :py:class:`Local <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Local>`
    
    .. attribute:: loggings
    
    	Table of Logging
    	**type**\:   :py:class:`Loggings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Loggings>`
    
    .. attribute:: redundancy
    
    	Enable VPDN redundancy
    	**type**\:   :py:class:`Redundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Redundancy>`
    
    .. attribute:: session_limit
    
    	Maximum simultaneous VPDN sessions
    	**type**\:  int
    
    	**range:** 1..131072
    
    .. attribute:: soft_shut
    
    	New session no longer allowed
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: templates
    
    	Table of Template
    	**type**\:   :py:class:`Templates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates>`
    
    .. attribute:: vpd_ngroups
    
    	Table of VPDNgroup
    	**type**\:   :py:class:`VpdNgroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.VpdNgroups>`
    
    

    """

    _prefix = 'tunnel-vpdn-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.caller_id = Vpdn.CallerId()
        self.caller_id.parent = self
        self.enable = None
        self.history = Vpdn.History()
        self.history.parent = self
        self.l2tp = Vpdn.L2Tp()
        self.l2tp.parent = self
        self.local = Vpdn.Local()
        self.local.parent = self
        self.loggings = Vpdn.Loggings()
        self.loggings.parent = self
        self.redundancy = Vpdn.Redundancy()
        self.redundancy.parent = self
        self.session_limit = None
        self.soft_shut = None
        self.templates = Vpdn.Templates()
        self.templates.parent = self
        self.vpd_ngroups = Vpdn.VpdNgroups()
        self.vpd_ngroups.parent = self


    class History(object):
        """
        VPDN history logging
        
        .. attribute:: failure
        
        	User failure
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.failure = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/Cisco-IOS-XR-tunnel-vpdn-cfg:history'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.failure is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
            return meta._meta_table['Vpdn.History']['meta_info']


    class Redundancy(object):
        """
        Enable VPDN redundancy
        
        .. attribute:: enable
        
        	Enable Enable VPDN redundancy. Deletion of this object also causes deletion of all associated objects under Redundancy
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: process_failures
        
        	Process crash configuration
        	**type**\:   :py:class:`ProcessFailures <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Redundancy.ProcessFailures>`
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.enable = None
            self.process_failures = Vpdn.Redundancy.ProcessFailures()
            self.process_failures.parent = self


        class ProcessFailures(object):
            """
            Process crash configuration
            
            .. attribute:: switchover
            
            	Force a switchover if the process crashes
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'tunnel-vpdn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.switchover = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/Cisco-IOS-XR-tunnel-vpdn-cfg:redundancy/Cisco-IOS-XR-tunnel-vpdn-cfg:process-failures'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.switchover is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
                return meta._meta_table['Vpdn.Redundancy.ProcessFailures']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/Cisco-IOS-XR-tunnel-vpdn-cfg:redundancy'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.enable is not None:
                return True

            if self.process_failures is not None and self.process_failures._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
            return meta._meta_table['Vpdn.Redundancy']['meta_info']


    class Local(object):
        """
        VPDN Local radius process configuration
        
        .. attribute:: cache_disabled
        
        	Set constant integer
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: path
        
        	local path of the saved profile
        	**type**\:  str
        
        	**length:** 1..64
        
        .. attribute:: port
        
        	port value
        	**type**\:  int
        
        	**range:** 1..65535
        
        .. attribute:: secret_text
        
        	secret password
        	**type**\:  str
        
        	**length:** 1..32
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.cache_disabled = None
            self.path = None
            self.port = None
            self.secret_text = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/Cisco-IOS-XR-tunnel-vpdn-cfg:local'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.cache_disabled is not None:
                return True

            if self.path is not None:
                return True

            if self.port is not None:
                return True

            if self.secret_text is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
            return meta._meta_table['Vpdn.Local']['meta_info']


    class Templates(object):
        """
        Table of Template
        
        .. attribute:: template
        
        	VPDN template configuration
        	**type**\: list of    :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates.Template>`
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.template = YList()
            self.template.parent = self
            self.template.name = 'template'


        class Template(object):
            """
            VPDN template configuration
            
            .. attribute:: template_name  <key>
            
            	VPDN template name
            	**type**\:  str
            
            	**length:** 1..63
            
            .. attribute:: caller_id
            
            	Options to apply on calling station id
            	**type**\:   :py:class:`CallerId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates.Template.CallerId>`
            
            .. attribute:: description
            
            	Up to 100 characters describing this VPDN template
            	**type**\:  str
            
            	**length:** 1..100
            
            .. attribute:: dsl_line_forwarding
            
            	Forward DSL Line Info attributes
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: ip
            
            	Set IP TOS value
            	**type**\:   :py:class:`Ip <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates.Template.Ip>`
            
            .. attribute:: ipv4
            
            	IPv4 settings for tunnel
            	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates.Template.Ipv4>`
            
            .. attribute:: l2tp_class
            
            	L2TP class  command
            	**type**\:  str
            
            	**length:** 1..79
            
            .. attribute:: tunnel
            
            	L2TP tunnel commands
            	**type**\:   :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates.Template.Tunnel>`
            
            .. attribute:: vpn
            
            	VPN ID/VRF name
            	**type**\:   :py:class:`Vpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates.Template.Vpn>`
            
            

            """

            _prefix = 'tunnel-vpdn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.template_name = None
                self.caller_id = Vpdn.Templates.Template.CallerId()
                self.caller_id.parent = self
                self.description = None
                self.dsl_line_forwarding = None
                self.ip = Vpdn.Templates.Template.Ip()
                self.ip.parent = self
                self.ipv4 = Vpdn.Templates.Template.Ipv4()
                self.ipv4.parent = self
                self.l2tp_class = None
                self.tunnel = Vpdn.Templates.Template.Tunnel()
                self.tunnel.parent = self
                self.vpn = Vpdn.Templates.Template.Vpn()
                self.vpn.parent = self


            class CallerId(object):
                """
                Options to apply on calling station id
                
                .. attribute:: mask
                
                	Mask characters by method
                	**type**\:  str
                
                	**length:** 1..63
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.mask = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tunnel-vpdn-cfg:caller-id'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.mask is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
                    return meta._meta_table['Vpdn.Templates.Template.CallerId']['meta_info']


            class Vpn(object):
                """
                VPN ID/VRF name
                
                .. attribute:: id
                
                	VPN ID
                	**type**\:   :py:class:`Id <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates.Template.Vpn.Id>`
                
                .. attribute:: vrf
                
                	VRF name
                	**type**\:  str
                
                	**length:** 1..32
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.id = Vpdn.Templates.Template.Vpn.Id()
                    self.id.parent = self
                    self.vrf = None


                class Id(object):
                    """
                    VPN ID
                    
                    .. attribute:: index
                    
                    	VPN ID, (OUI\:VPN\-Index) format(hex), 4 bytes VPN\_Index Part
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                    
                    .. attribute:: oui
                    
                    	VPN ID, (OUI\:VPN\-Index) format(hex), 3 bytes OUI Part
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                    
                    

                    """

                    _prefix = 'tunnel-vpdn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.index = None
                        self.oui = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tunnel-vpdn-cfg:id'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.index is not None:
                            return True

                        if self.oui is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
                        return meta._meta_table['Vpdn.Templates.Template.Vpn.Id']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tunnel-vpdn-cfg:vpn'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.id is not None and self.id._has_data():
                        return True

                    if self.vrf is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
                    return meta._meta_table['Vpdn.Templates.Template.Vpn']['meta_info']


            class Tunnel(object):
                """
                L2TP tunnel commands
                
                .. attribute:: busy_timeout
                
                	Busy time out value in seconds
                	**type**\:  int
                
                	**range:** 60..65535
                
                	**units**\: second
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.busy_timeout = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tunnel-vpdn-cfg:tunnel'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.busy_timeout is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
                    return meta._meta_table['Vpdn.Templates.Template.Tunnel']['meta_info']


            class Ip(object):
                """
                Set IP TOS value
                
                .. attribute:: tos
                
                	Set constant integer
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.tos = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tunnel-vpdn-cfg:ip'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.tos is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
                    return meta._meta_table['Vpdn.Templates.Template.Ip']['meta_info']


            class Ipv4(object):
                """
                IPv4 settings for tunnel
                
                .. attribute:: df_bit
                
                	IPv4 don't fragment bit set/clear/reflect
                	**type**\:   :py:class:`DfBitEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.DfBitEnum>`
                
                .. attribute:: source
                
                	Enter an IP address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.df_bit = None
                    self.source = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tunnel-vpdn-cfg:ipv4'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.df_bit is not None:
                        return True

                    if self.source is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
                    return meta._meta_table['Vpdn.Templates.Template.Ipv4']['meta_info']

            @property
            def _common_path(self):
                if self.template_name is None:
                    raise YPYModelError('Key property template_name is None')

                return '/Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/Cisco-IOS-XR-tunnel-vpdn-cfg:templates/Cisco-IOS-XR-tunnel-vpdn-cfg:template[Cisco-IOS-XR-tunnel-vpdn-cfg:template-name = ' + str(self.template_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.template_name is not None:
                    return True

                if self.caller_id is not None and self.caller_id._has_data():
                    return True

                if self.description is not None:
                    return True

                if self.dsl_line_forwarding is not None:
                    return True

                if self.ip is not None and self.ip._has_data():
                    return True

                if self.ipv4 is not None and self.ipv4._has_data():
                    return True

                if self.l2tp_class is not None:
                    return True

                if self.tunnel is not None and self.tunnel._has_data():
                    return True

                if self.vpn is not None and self.vpn._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
                return meta._meta_table['Vpdn.Templates.Template']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/Cisco-IOS-XR-tunnel-vpdn-cfg:templates'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.template is not None:
                for child_ref in self.template:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
            return meta._meta_table['Vpdn.Templates']['meta_info']


    class CallerId(object):
        """
        Options to apply on calling station ID
        
        .. attribute:: mask
        
        	Mask characters by method
        	**type**\:  str
        
        	**length:** 1..63
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.mask = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/Cisco-IOS-XR-tunnel-vpdn-cfg:caller-id'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.mask is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
            return meta._meta_table['Vpdn.CallerId']['meta_info']


    class VpdNgroups(object):
        """
        Table of VPDNgroup
        
        .. attribute:: vpd_ngroup
        
        	vpdn\-group configuration
        	**type**\: list of    :py:class:`VpdNgroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.VpdNgroups.VpdNgroup>`
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.vpd_ngroup = YList()
            self.vpd_ngroup.parent = self
            self.vpd_ngroup.name = 'vpd_ngroup'


        class VpdNgroup(object):
            """
            vpdn\-group configuration
            
            .. attribute:: vpd_ngroupname  <key>
            
            	vpdn\-group name
            	**type**\:  str
            
            	**length:** 1..63
            
            .. attribute:: attribute
            
            	match substring
            	**type**\:  str
            
            	**length:** 1..63
            
            .. attribute:: desc
            
            	upto 100 characters describing this VPDN group
            	**type**\:  str
            
            	**length:** 1..100
            
            .. attribute:: dsl_line_forwarding
            
            	Forward DSL Line Info attributes
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: ip
            
            	set ip tos value
            	**type**\:   :py:class:`Ip <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.VpdNgroups.VpdNgroup.Ip>`
            
            .. attribute:: l2tp_class
            
            	l2tp class name
            	**type**\:  str
            
            	**length:** 1..79
            
            .. attribute:: sr_ctemplate
            
            	Source vpdn\-template
            	**type**\:  str
            
            	**length:** 1..63
            
            .. attribute:: tunnel_busy_timeout
            
            	Busy list timeout length
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: vpn_id
            
            	Vpn id
            	**type**\:   :py:class:`VpnId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.VpdNgroups.VpdNgroup.VpnId>`
            
            .. attribute:: vrf_name
            
            	Vrf name
            	**type**\:  str
            
            	**length:** 1..32
            
            

            """

            _prefix = 'tunnel-vpdn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.vpd_ngroupname = None
                self.attribute = None
                self.desc = None
                self.dsl_line_forwarding = None
                self.ip = Vpdn.VpdNgroups.VpdNgroup.Ip()
                self.ip.parent = self
                self.l2tp_class = None
                self.sr_ctemplate = None
                self.tunnel_busy_timeout = None
                self.vpn_id = Vpdn.VpdNgroups.VpdNgroup.VpnId()
                self.vpn_id.parent = self
                self.vrf_name = None


            class VpnId(object):
                """
                Vpn id
                
                .. attribute:: vpn_id_index
                
                	VPN ID, (OUI\:VPN\-Index) format(hex), 4 bytes VPN\_Index Part
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: vpn_id_oui
                
                	VPN ID, (OUI\:VPN\-Index) format(hex), 3 bytes OUI Part
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.vpn_id_index = None
                    self.vpn_id_oui = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tunnel-vpdn-cfg:vpn-id'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.vpn_id_index is not None:
                        return True

                    if self.vpn_id_oui is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
                    return meta._meta_table['Vpdn.VpdNgroups.VpdNgroup.VpnId']['meta_info']


            class Ip(object):
                """
                set ip tos value
                
                .. attribute:: tos
                
                	ip tos value
                	**type**\:  int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.tos = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tunnel-vpdn-cfg:ip'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.tos is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
                    return meta._meta_table['Vpdn.VpdNgroups.VpdNgroup.Ip']['meta_info']

            @property
            def _common_path(self):
                if self.vpd_ngroupname is None:
                    raise YPYModelError('Key property vpd_ngroupname is None')

                return '/Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/Cisco-IOS-XR-tunnel-vpdn-cfg:vpd-ngroups/Cisco-IOS-XR-tunnel-vpdn-cfg:vpd-ngroup[Cisco-IOS-XR-tunnel-vpdn-cfg:vpd-ngroupname = ' + str(self.vpd_ngroupname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.vpd_ngroupname is not None:
                    return True

                if self.attribute is not None:
                    return True

                if self.desc is not None:
                    return True

                if self.dsl_line_forwarding is not None:
                    return True

                if self.ip is not None and self.ip._has_data():
                    return True

                if self.l2tp_class is not None:
                    return True

                if self.sr_ctemplate is not None:
                    return True

                if self.tunnel_busy_timeout is not None:
                    return True

                if self.vpn_id is not None and self.vpn_id._has_data():
                    return True

                if self.vrf_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
                return meta._meta_table['Vpdn.VpdNgroups.VpdNgroup']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/Cisco-IOS-XR-tunnel-vpdn-cfg:vpd-ngroups'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.vpd_ngroup is not None:
                for child_ref in self.vpd_ngroup:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
            return meta._meta_table['Vpdn.VpdNgroups']['meta_info']


    class Loggings(object):
        """
        Table of Logging
        
        .. attribute:: logging
        
        	Configure logging for VPDN
        	**type**\: list of    :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Loggings.Logging>`
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.logging = YList()
            self.logging.parent = self
            self.logging.name = 'logging'


        class Logging(object):
            """
            Configure logging for VPDN
            
            .. attribute:: option  <key>
            
            	VPDN logging options
            	**type**\:   :py:class:`OptionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.OptionEnum>`
            
            

            """

            _prefix = 'tunnel-vpdn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.option = None

            @property
            def _common_path(self):
                if self.option is None:
                    raise YPYModelError('Key property option is None')

                return '/Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/Cisco-IOS-XR-tunnel-vpdn-cfg:loggings/Cisco-IOS-XR-tunnel-vpdn-cfg:logging[Cisco-IOS-XR-tunnel-vpdn-cfg:option = ' + str(self.option) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.option is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
                return meta._meta_table['Vpdn.Loggings.Logging']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/Cisco-IOS-XR-tunnel-vpdn-cfg:loggings'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.logging is not None:
                for child_ref in self.logging:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
            return meta._meta_table['Vpdn.Loggings']['meta_info']


    class L2Tp(object):
        """
        L2TPv2 protocol commands
        
        .. attribute:: reassembly
        
        	L2TP IP packet reassembly enable
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: session_id
        
        	Session ID commands
        	**type**\:   :py:class:`SessionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.L2Tp.SessionId>`
        
        .. attribute:: tcp_mss_adjust
        
        	TCP MSS adjust value. The acceptable values might be further limited depending on platform
        	**type**\:  int
        
        	**range:** 1280..1460
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.reassembly = None
            self.session_id = Vpdn.L2Tp.SessionId()
            self.session_id.parent = self
            self.tcp_mss_adjust = None


        class SessionId(object):
            """
            Session ID commands
            
            .. attribute:: space
            
            	Session ID space commands
            	**type**\:   :py:class:`Space <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.L2Tp.SessionId.Space>`
            
            

            """

            _prefix = 'tunnel-vpdn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.space = Vpdn.L2Tp.SessionId.Space()
                self.space.parent = self


            class Space(object):
                """
                Session ID space commands
                
                .. attribute:: hierarchy
                
                	Session ID space hierarchical command
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.hierarchy = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/Cisco-IOS-XR-tunnel-vpdn-cfg:l2tp/Cisco-IOS-XR-tunnel-vpdn-cfg:session-id/Cisco-IOS-XR-tunnel-vpdn-cfg:space'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.hierarchy is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
                    return meta._meta_table['Vpdn.L2Tp.SessionId.Space']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/Cisco-IOS-XR-tunnel-vpdn-cfg:l2tp/Cisco-IOS-XR-tunnel-vpdn-cfg:session-id'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.space is not None and self.space._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
                return meta._meta_table['Vpdn.L2Tp.SessionId']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/Cisco-IOS-XR-tunnel-vpdn-cfg:l2tp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.reassembly is not None:
                return True

            if self.session_id is not None and self.session_id._has_data():
                return True

            if self.tcp_mss_adjust is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
            return meta._meta_table['Vpdn.L2Tp']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.caller_id is not None and self.caller_id._has_data():
            return True

        if self.enable is not None:
            return True

        if self.history is not None and self.history._has_data():
            return True

        if self.l2tp is not None and self.l2tp._has_data():
            return True

        if self.local is not None and self.local._has_data():
            return True

        if self.loggings is not None and self.loggings._has_data():
            return True

        if self.redundancy is not None and self.redundancy._has_data():
            return True

        if self.session_limit is not None:
            return True

        if self.soft_shut is not None:
            return True

        if self.templates is not None and self.templates._has_data():
            return True

        if self.vpd_ngroups is not None and self.vpd_ngroups._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_cfg as meta
        return meta._meta_table['Vpdn']['meta_info']



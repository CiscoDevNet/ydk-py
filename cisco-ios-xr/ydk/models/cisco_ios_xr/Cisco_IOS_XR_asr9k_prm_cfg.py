""" Cisco_IOS_XR_asr9k_prm_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-prm package configuration.

This module contains definitions
for the following management objects\:
  hardware\-module\-qos\-mode\: QoS mode in hardware module port(s)
  hardware\-module\-tcp\-mss\-adjust\: hardware module tcp mss adjust
  hardware\-module\-load\-balance\: hardware module load balance
  hardware\-module\-tcam\: hardware module tcam
  hardware\-module\-efd\: hardware module efd

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class Asr9KEfdModeEnum(Enum):
    """
    Asr9KEfdModeEnum

    Asr9k efd mode

    .. data:: only_outer_encap = 0

    	Only check outer encap

    .. data:: include_inner_encap = 1

    	Check outer and inner encap

    """

    only_outer_encap = 0

    include_inner_encap = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
        return meta._meta_table['Asr9KEfdModeEnum']


class Asr9KEfdOperationEnum(Enum):
    """
    Asr9KEfdOperationEnum

    Asr9k efd operation

    .. data:: less_than = 2

    	Less than

    .. data:: greater_than_or_equal = 3

    	Greater than or equal

    """

    less_than = 2

    greater_than_or_equal = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
        return meta._meta_table['Asr9KEfdOperationEnum']


class PrmTcamProfileEnum(Enum):
    """
    PrmTcamProfileEnum

    Prm tcam profile

    .. data:: profile0 = 0

    	Profile 0

    .. data:: profile1 = 1

    	Profile 1

    .. data:: profile2 = 2

    	Profile 2

    """

    profile0 = 0

    profile1 = 1

    profile2 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
        return meta._meta_table['PrmTcamProfileEnum']



class HardwareModuleQosMode(object):
    """
    QoS mode in hardware module port(s)
    
    .. attribute:: nodes
    
    	QoS applicable nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleQosMode.Nodes>`
    
    

    """

    _prefix = 'asr9k-prm-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = HardwareModuleQosMode.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        QoS applicable nodes
        
        .. attribute:: node
        
        	A node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleQosMode.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-prm-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            A node
            
            .. attribute:: node_name  <key>
            
            	Node ID
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: child_shaping_disable
            
            	Disable child level/flat policy shaping
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: lowburst_enable
            
            	Enable low burst mode for TM entity
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.child_shaping_disable = None
                self.lowburst_enable = None

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-qos-mode/Cisco-IOS-XR-asr9k-prm-cfg:nodes/Cisco-IOS-XR-asr9k-prm-cfg:node[Cisco-IOS-XR-asr9k-prm-cfg:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.child_shaping_disable is not None:
                    return True

                if self.lowburst_enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
                return meta._meta_table['HardwareModuleQosMode.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-qos-mode/Cisco-IOS-XR-asr9k-prm-cfg:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
            return meta._meta_table['HardwareModuleQosMode.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-qos-mode'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
        return meta._meta_table['HardwareModuleQosMode']['meta_info']


class HardwareModuleTcpMssAdjust(object):
    """
    hardware module tcp mss adjust
    
    .. attribute:: nodes
    
    	TCP MSS Adjust applicable nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleTcpMssAdjust.Nodes>`
    
    

    """

    _prefix = 'asr9k-prm-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = HardwareModuleTcpMssAdjust.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        TCP MSS Adjust applicable nodes
        
        .. attribute:: node
        
        	A node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleTcpMssAdjust.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-prm-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            A node
            
            .. attribute:: node_name  <key>
            
            	Node ID
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: nps
            
            	TCP MSS Adjust NPs
            	**type**\:   :py:class:`Nps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleTcpMssAdjust.Nodes.Node.Nps>`
            
            

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.nps = HardwareModuleTcpMssAdjust.Nodes.Node.Nps()
                self.nps.parent = self


            class Nps(object):
                """
                TCP MSS Adjust NPs
                
                .. attribute:: np
                
                	NP number
                	**type**\: list of    :py:class:`Np <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleTcpMssAdjust.Nodes.Node.Nps.Np>`
                
                

                """

                _prefix = 'asr9k-prm-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.np = YList()
                    self.np.parent = self
                    self.np.name = 'np'


                class Np(object):
                    """
                    NP number
                    
                    .. attribute:: np_id  <key>
                    
                    	Number between 0\-7
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    .. attribute:: adjust_value
                    
                    	TCP MSS Adjust value
                    	**type**\:  int
                    
                    	**range:** 1280..1535
                    
                    	**units**\: byte
                    
                    

                    """

                    _prefix = 'asr9k-prm-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.np_id = None
                        self.adjust_value = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.np_id is None:
                            raise YPYModelError('Key property np_id is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-prm-cfg:np[Cisco-IOS-XR-asr9k-prm-cfg:np-id = ' + str(self.np_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.np_id is not None:
                            return True

                        if self.adjust_value is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
                        return meta._meta_table['HardwareModuleTcpMssAdjust.Nodes.Node.Nps.Np']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-prm-cfg:nps'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.np is not None:
                        for child_ref in self.np:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
                    return meta._meta_table['HardwareModuleTcpMssAdjust.Nodes.Node.Nps']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-tcp-mss-adjust/Cisco-IOS-XR-asr9k-prm-cfg:nodes/Cisco-IOS-XR-asr9k-prm-cfg:node[Cisco-IOS-XR-asr9k-prm-cfg:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.nps is not None and self.nps._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
                return meta._meta_table['HardwareModuleTcpMssAdjust.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-tcp-mss-adjust/Cisco-IOS-XR-asr9k-prm-cfg:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
            return meta._meta_table['HardwareModuleTcpMssAdjust.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-tcp-mss-adjust'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
        return meta._meta_table['HardwareModuleTcpMssAdjust']['meta_info']


class HardwareModuleLoadBalance(object):
    """
    hardware module load balance
    
    .. attribute:: bundle
    
    	Bundle load balance options
    	**type**\:   :py:class:`Bundle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleLoadBalance.Bundle>`
    
    

    """

    _prefix = 'asr9k-prm-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.bundle = HardwareModuleLoadBalance.Bundle()
        self.bundle.parent = self


    class Bundle(object):
        """
        Bundle load balance options
        
        .. attribute:: l2_service
        
        	Load balance for L2 services
        	**type**\:   :py:class:`L2Service <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleLoadBalance.Bundle.L2Service>`
        
        

        """

        _prefix = 'asr9k-prm-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.l2_service = HardwareModuleLoadBalance.Bundle.L2Service()
            self.l2_service.parent = self


        class L2Service(object):
            """
            Load balance for L2 services
            
            .. attribute:: l3_parameters
            
            	Load balance L2 services over bundle with L3 parameters
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.l3_parameters = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-load-balance/Cisco-IOS-XR-asr9k-prm-cfg:bundle/Cisco-IOS-XR-asr9k-prm-cfg:l2-service'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.l3_parameters is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
                return meta._meta_table['HardwareModuleLoadBalance.Bundle.L2Service']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-load-balance/Cisco-IOS-XR-asr9k-prm-cfg:bundle'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.l2_service is not None and self.l2_service._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
            return meta._meta_table['HardwareModuleLoadBalance.Bundle']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-load-balance'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.bundle is not None and self.bundle._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
        return meta._meta_table['HardwareModuleLoadBalance']['meta_info']


class HardwareModuleTcam(object):
    """
    hardware module tcam
    
    .. attribute:: global_profile
    
    	Global TCAM partition profile for all TCAM applicable nodes
    	**type**\:   :py:class:`PrmTcamProfileEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.PrmTcamProfileEnum>`
    
    	**default value**\: profile0
    
    .. attribute:: nodes
    
    	TCAM applicable nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleTcam.Nodes>`
    
    

    """

    _prefix = 'asr9k-prm-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.global_profile = None
        self.nodes = HardwareModuleTcam.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        TCAM applicable nodes
        
        .. attribute:: node
        
        	A TCAM applicable node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleTcam.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-prm-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            A TCAM applicable node
            
            .. attribute:: node_name  <key>
            
            	Node ID
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: profile
            
            	A TCAM partition profile
            	**type**\:   :py:class:`PrmTcamProfileEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.PrmTcamProfileEnum>`
            
            	**default value**\: profile0
            
            

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.profile = None

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-tcam/Cisco-IOS-XR-asr9k-prm-cfg:nodes/Cisco-IOS-XR-asr9k-prm-cfg:node[Cisco-IOS-XR-asr9k-prm-cfg:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.profile is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
                return meta._meta_table['HardwareModuleTcam.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-tcam/Cisco-IOS-XR-asr9k-prm-cfg:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
            return meta._meta_table['HardwareModuleTcam.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-tcam'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.global_profile is not None:
            return True

        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
        return meta._meta_table['HardwareModuleTcam']['meta_info']


class HardwareModuleEfd(object):
    """
    hardware module efd
    
    .. attribute:: node_all
    
    	All nodes
    	**type**\:   :py:class:`NodeAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.NodeAll>`
    
    .. attribute:: nodes
    
    	EFD applicable nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.Nodes>`
    
    

    """

    _prefix = 'asr9k-prm-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.node_all = HardwareModuleEfd.NodeAll()
        self.node_all.parent = self
        self.nodes = HardwareModuleEfd.Nodes()
        self.nodes.parent = self


    class NodeAll(object):
        """
        All nodes
        
        .. attribute:: enable
        
        	Enable EFD for this node
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: ip_precedence
        
        	EFD IP parameters
        	**type**\:   :py:class:`IpPrecedence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.NodeAll.IpPrecedence>`
        
        	**presence node**\: True
        
        .. attribute:: mode
        
        	EFD mode parameter
        	**type**\:   :py:class:`Asr9KEfdModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9KEfdModeEnum>`
        
        .. attribute:: mpls_exp
        
        	EFD MPLS parameters
        	**type**\:   :py:class:`MplsExp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.NodeAll.MplsExp>`
        
        	**presence node**\: True
        
        .. attribute:: vlan_cos
        
        	EFD VLAN parameters
        	**type**\:   :py:class:`VlanCos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.NodeAll.VlanCos>`
        
        	**presence node**\: True
        
        

        """

        _prefix = 'asr9k-prm-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.enable = None
            self.ip_precedence = None
            self.mode = None
            self.mpls_exp = None
            self.vlan_cos = None


        class IpPrecedence(object):
            """
            EFD IP parameters
            
            .. attribute:: operation
            
            	IP operation
            	**type**\:   :py:class:`Asr9KEfdOperationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9KEfdOperationEnum>`
            
            	**default value**\: greater-than-or-equal
            
            .. attribute:: precedence
            
            	IP TOS precedence threshold
            	**type**\:  int
            
            	**range:** 0..7
            
            	**mandatory**\: True
            
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self._is_presence = True
                self.operation = None
                self.precedence = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/Cisco-IOS-XR-asr9k-prm-cfg:node-all/Cisco-IOS-XR-asr9k-prm-cfg:ip-precedence'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self._is_presence:
                    return True
                if self.operation is not None:
                    return True

                if self.precedence is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
                return meta._meta_table['HardwareModuleEfd.NodeAll.IpPrecedence']['meta_info']


        class VlanCos(object):
            """
            EFD VLAN parameters
            
            .. attribute:: cos
            
            	VLAN COS threshold
            	**type**\:  int
            
            	**range:** 0..7
            
            	**mandatory**\: True
            
            .. attribute:: operation
            
            	VLAN operation
            	**type**\:   :py:class:`Asr9KEfdOperationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9KEfdOperationEnum>`
            
            	**default value**\: greater-than-or-equal
            
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self._is_presence = True
                self.cos = None
                self.operation = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/Cisco-IOS-XR-asr9k-prm-cfg:node-all/Cisco-IOS-XR-asr9k-prm-cfg:vlan-cos'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self._is_presence:
                    return True
                if self.cos is not None:
                    return True

                if self.operation is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
                return meta._meta_table['HardwareModuleEfd.NodeAll.VlanCos']['meta_info']


        class MplsExp(object):
            """
            EFD MPLS parameters
            
            .. attribute:: exp
            
            	MPLS EXP threshold
            	**type**\:  int
            
            	**range:** 0..7
            
            	**mandatory**\: True
            
            .. attribute:: operation
            
            	MPLS operation
            	**type**\:   :py:class:`Asr9KEfdOperationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9KEfdOperationEnum>`
            
            	**default value**\: greater-than-or-equal
            
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self._is_presence = True
                self.exp = None
                self.operation = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/Cisco-IOS-XR-asr9k-prm-cfg:node-all/Cisco-IOS-XR-asr9k-prm-cfg:mpls-exp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self._is_presence:
                    return True
                if self.exp is not None:
                    return True

                if self.operation is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
                return meta._meta_table['HardwareModuleEfd.NodeAll.MplsExp']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/Cisco-IOS-XR-asr9k-prm-cfg:node-all'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.enable is not None:
                return True

            if self.ip_precedence is not None and self.ip_precedence._has_data():
                return True

            if self.mode is not None:
                return True

            if self.mpls_exp is not None and self.mpls_exp._has_data():
                return True

            if self.vlan_cos is not None and self.vlan_cos._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
            return meta._meta_table['HardwareModuleEfd.NodeAll']['meta_info']


    class Nodes(object):
        """
        EFD applicable nodes
        
        .. attribute:: node
        
        	A node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-prm-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            A node
            
            .. attribute:: node_name  <key>
            
            	Node Name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: enable
            
            	Enable EFD for this node
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: ip_precedence
            
            	EFD IP parameters
            	**type**\:   :py:class:`IpPrecedence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.Nodes.Node.IpPrecedence>`
            
            	**presence node**\: True
            
            .. attribute:: mode
            
            	EFD mode parameter
            	**type**\:   :py:class:`Asr9KEfdModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9KEfdModeEnum>`
            
            .. attribute:: mpls_exp
            
            	EFD MPLS parameters
            	**type**\:   :py:class:`MplsExp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.Nodes.Node.MplsExp>`
            
            	**presence node**\: True
            
            .. attribute:: vlan_cos
            
            	EFD VLAN parameters
            	**type**\:   :py:class:`VlanCos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.HardwareModuleEfd.Nodes.Node.VlanCos>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'asr9k-prm-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.enable = None
                self.ip_precedence = None
                self.mode = None
                self.mpls_exp = None
                self.vlan_cos = None


            class IpPrecedence(object):
                """
                EFD IP parameters
                
                .. attribute:: operation
                
                	IP operation
                	**type**\:   :py:class:`Asr9KEfdOperationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9KEfdOperationEnum>`
                
                	**default value**\: greater-than-or-equal
                
                .. attribute:: precedence
                
                	IP TOS precedence threshold
                	**type**\:  int
                
                	**range:** 0..7
                
                	**mandatory**\: True
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'asr9k-prm-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.operation = None
                    self.precedence = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-prm-cfg:ip-precedence'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.operation is not None:
                        return True

                    if self.precedence is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
                    return meta._meta_table['HardwareModuleEfd.Nodes.Node.IpPrecedence']['meta_info']


            class VlanCos(object):
                """
                EFD VLAN parameters
                
                .. attribute:: cos
                
                	VLAN COS threshold
                	**type**\:  int
                
                	**range:** 0..7
                
                	**mandatory**\: True
                
                .. attribute:: operation
                
                	VLAN operation
                	**type**\:   :py:class:`Asr9KEfdOperationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9KEfdOperationEnum>`
                
                	**default value**\: greater-than-or-equal
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'asr9k-prm-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.cos = None
                    self.operation = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-prm-cfg:vlan-cos'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.cos is not None:
                        return True

                    if self.operation is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
                    return meta._meta_table['HardwareModuleEfd.Nodes.Node.VlanCos']['meta_info']


            class MplsExp(object):
                """
                EFD MPLS parameters
                
                .. attribute:: exp
                
                	MPLS EXP threshold
                	**type**\:  int
                
                	**range:** 0..7
                
                	**mandatory**\: True
                
                .. attribute:: operation
                
                	MPLS operation
                	**type**\:   :py:class:`Asr9KEfdOperationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_prm_cfg.Asr9KEfdOperationEnum>`
                
                	**default value**\: greater-than-or-equal
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'asr9k-prm-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.exp = None
                    self.operation = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-prm-cfg:mpls-exp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.exp is not None:
                        return True

                    if self.operation is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
                    return meta._meta_table['HardwareModuleEfd.Nodes.Node.MplsExp']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/Cisco-IOS-XR-asr9k-prm-cfg:nodes/Cisco-IOS-XR-asr9k-prm-cfg:node[Cisco-IOS-XR-asr9k-prm-cfg:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.enable is not None:
                    return True

                if self.ip_precedence is not None and self.ip_precedence._has_data():
                    return True

                if self.mode is not None:
                    return True

                if self.mpls_exp is not None and self.mpls_exp._has_data():
                    return True

                if self.vlan_cos is not None and self.vlan_cos._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
                return meta._meta_table['HardwareModuleEfd.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd/Cisco-IOS-XR-asr9k-prm-cfg:nodes'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
            return meta._meta_table['HardwareModuleEfd.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-asr9k-prm-cfg:hardware-module-efd'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.node_all is not None and self.node_all._has_data():
            return True

        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_prm_cfg as meta
        return meta._meta_table['HardwareModuleEfd']['meta_info']



""" Cisco_IOS_XR_man_netconf_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR man\-netconf package configuration.

This module contains definitions
for the following management objects\:
  netconf\-yang\: NETCONF YANG configuration commands

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class NetconfYang(_Entity_):
    """
    NETCONF YANG configuration commands
    
    .. attribute:: agent
    
    	NETCONF YANG agent configuration commands
    	**type**\:  :py:class:`Agent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg.NetconfYang.Agent>`
    
    

    """

    _prefix = 'man-netconf-cfg'
    _revision = '2018-05-04'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(NetconfYang, self).__init__()
        self._top_entity = None

        self.yang_name = "netconf-yang"
        self.yang_parent_name = "Cisco-IOS-XR-man-netconf-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("agent", ("agent", NetconfYang.Agent))])
        self._leafs = OrderedDict()

        self.agent = NetconfYang.Agent()
        self.agent.parent = self
        self._children_name_map["agent"] = "agent"
        self._segment_path = lambda: "Cisco-IOS-XR-man-netconf-cfg:netconf-yang"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(NetconfYang, [], name, value)


    class Agent(_Entity_):
        """
        NETCONF YANG agent configuration commands
        
        .. attribute:: models
        
        	Models to be disabled
        	**type**\:  :py:class:`Models <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg.NetconfYang.Agent.Models>`
        
        .. attribute:: ssh
        
        	NETCONF YANG agent over SSH connection
        	**type**\:  :py:class:`Ssh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg.NetconfYang.Agent.Ssh>`
        
        .. attribute:: session
        
        	Session settings
        	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg.NetconfYang.Agent.Session>`
        
        .. attribute:: rate_limit
        
        	Number of bytes to process per sec
        	**type**\: int
        
        	**range:** 4096..4294967295
        
        	**units**\: byte
        
        

        """

        _prefix = 'man-netconf-cfg'
        _revision = '2018-05-04'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(NetconfYang.Agent, self).__init__()

            self.yang_name = "agent"
            self.yang_parent_name = "netconf-yang"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("models", ("models", NetconfYang.Agent.Models)), ("ssh", ("ssh", NetconfYang.Agent.Ssh)), ("session", ("session", NetconfYang.Agent.Session))])
            self._leafs = OrderedDict([
                ('rate_limit', (YLeaf(YType.uint32, 'rate-limit'), ['int'])),
            ])
            self.rate_limit = None

            self.models = NetconfYang.Agent.Models()
            self.models.parent = self
            self._children_name_map["models"] = "models"

            self.ssh = NetconfYang.Agent.Ssh()
            self.ssh.parent = self
            self._children_name_map["ssh"] = "ssh"

            self.session = NetconfYang.Agent.Session()
            self.session.parent = self
            self._children_name_map["session"] = "session"
            self._segment_path = lambda: "agent"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-netconf-cfg:netconf-yang/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(NetconfYang.Agent, ['rate_limit'], name, value)


        class Models(_Entity_):
            """
            Models to be disabled
            
            .. attribute:: openconfig
            
            	Type of models\: openconfig
            	**type**\:  :py:class:`Openconfig <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg.NetconfYang.Agent.Models.Openconfig>`
            
            

            """

            _prefix = 'man-netconf-cfg'
            _revision = '2018-05-04'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(NetconfYang.Agent.Models, self).__init__()

                self.yang_name = "models"
                self.yang_parent_name = "agent"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("openconfig", ("openconfig", NetconfYang.Agent.Models.Openconfig))])
                self._leafs = OrderedDict()

                self.openconfig = NetconfYang.Agent.Models.Openconfig()
                self.openconfig.parent = self
                self._children_name_map["openconfig"] = "openconfig"
                self._segment_path = lambda: "models"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-netconf-cfg:netconf-yang/agent/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NetconfYang.Agent.Models, [], name, value)


            class Openconfig(_Entity_):
                """
                Type of models\: openconfig
                
                .. attribute:: disabled
                
                	Disable the specified model type
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'man-netconf-cfg'
                _revision = '2018-05-04'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(NetconfYang.Agent.Models.Openconfig, self).__init__()

                    self.yang_name = "openconfig"
                    self.yang_parent_name = "models"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('disabled', (YLeaf(YType.empty, 'disabled'), ['Empty'])),
                    ])
                    self.disabled = None
                    self._segment_path = lambda: "openconfig"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-netconf-cfg:netconf-yang/agent/models/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(NetconfYang.Agent.Models.Openconfig, ['disabled'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_netconf_cfg as meta
                    return meta._meta_table['NetconfYang.Agent.Models.Openconfig']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_netconf_cfg as meta
                return meta._meta_table['NetconfYang.Agent.Models']['meta_info']


        class Ssh(_Entity_):
            """
            NETCONF YANG agent over SSH connection
            
            .. attribute:: enable
            
            	Enable NETCONF YANG agent over SSH connection
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'man-netconf-cfg'
            _revision = '2018-05-04'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(NetconfYang.Agent.Ssh, self).__init__()

                self.yang_name = "ssh"
                self.yang_parent_name = "agent"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.enable = None
                self._segment_path = lambda: "ssh"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-netconf-cfg:netconf-yang/agent/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NetconfYang.Agent.Ssh, ['enable'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_netconf_cfg as meta
                return meta._meta_table['NetconfYang.Agent.Ssh']['meta_info']


        class Session(_Entity_):
            """
            Session settings
            
            .. attribute:: limit
            
            	Count of allowable concurrent netconf\-yang sessions
            	**type**\: int
            
            	**range:** 1..50
            
            	**default value**\: 50
            
            .. attribute:: absolute_timeout
            
            	Absolute timeout in minutes
            	**type**\: int
            
            	**range:** 1..1440
            
            	**units**\: minute
            
            .. attribute:: idle_timeout
            
            	Non\-active session lifetime
            	**type**\: int
            
            	**range:** 1..1440
            
            	**units**\: minute
            
            

            """

            _prefix = 'man-netconf-cfg'
            _revision = '2018-05-04'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(NetconfYang.Agent.Session, self).__init__()

                self.yang_name = "session"
                self.yang_parent_name = "agent"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('limit', (YLeaf(YType.uint32, 'limit'), ['int'])),
                    ('absolute_timeout', (YLeaf(YType.uint32, 'absolute-timeout'), ['int'])),
                    ('idle_timeout', (YLeaf(YType.uint32, 'idle-timeout'), ['int'])),
                ])
                self.limit = None
                self.absolute_timeout = None
                self.idle_timeout = None
                self._segment_path = lambda: "session"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-netconf-cfg:netconf-yang/agent/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(NetconfYang.Agent.Session, ['limit', 'absolute_timeout', 'idle_timeout'], name, value)

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_netconf_cfg as meta
                return meta._meta_table['NetconfYang.Agent.Session']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_netconf_cfg as meta
            return meta._meta_table['NetconfYang.Agent']['meta_info']

    def clone_ptr(self):
        self._top_entity = NetconfYang()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_netconf_cfg as meta
        return meta._meta_table['NetconfYang']['meta_info']



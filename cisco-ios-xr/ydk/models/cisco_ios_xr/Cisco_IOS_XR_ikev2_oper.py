""" Cisco_IOS_XR_ikev2_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ikev2 package operational data.

This module contains definitions
for the following management objects\:
  ik\-ev2\: IKEv2 operational data

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




class IkEv2(_Entity_):
    """
    IKEv2 operational data
    
    .. attribute:: nodes
    
    	Per node IKEv2 operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'ikev2-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(IkEv2, self).__init__()
        self._top_entity = None

        self.yang_name = "ik-ev2"
        self.yang_parent_name = "Cisco-IOS-XR-ikev2-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", IkEv2.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = IkEv2.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-ikev2-oper:ik-ev2"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(IkEv2, [], name, value)


    class Nodes(_Entity_):
        """
        Per node IKEv2 operational data
        
        .. attribute:: node
        
        	IKEv2 operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ikev2-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(IkEv2.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ik-ev2"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", IkEv2.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ikev2-oper:ik-ev2/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(IkEv2.Nodes, [], name, value)


        class Node(_Entity_):
            """
            IKEv2 operational data for a particular node
            
            .. attribute:: node_name  (key)
            
            	The identifier for the node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: session
            
            	IKEv2 Session data
            	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes.Node.Session>`
            
            	**config**\: False
            
            .. attribute:: sa
            
            	IKEv2 SA data
            	**type**\:  :py:class:`Sa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes.Node.Sa>`
            
            	**config**\: False
            
            .. attribute:: policies
            
            	IKEv2 policies on this node
            	**type**\:  :py:class:`Policies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes.Node.Policies>`
            
            	**config**\: False
            
            .. attribute:: proposals
            
            	IKEv2 proposals on this node
            	**type**\:  :py:class:`Proposals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes.Node.Proposals>`
            
            	**config**\: False
            
            .. attribute:: profiles
            
            	IKEv2 profiles on this node
            	**type**\:  :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes.Node.Profiles>`
            
            	**config**\: False
            
            .. attribute:: keyrings
            
            	IKEv2 keyrings on this node
            	**type**\:  :py:class:`Keyrings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes.Node.Keyrings>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ikev2-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(IkEv2.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("session", ("session", IkEv2.Nodes.Node.Session)), ("sa", ("sa", IkEv2.Nodes.Node.Sa)), ("policies", ("policies", IkEv2.Nodes.Node.Policies)), ("proposals", ("proposals", IkEv2.Nodes.Node.Proposals)), ("profiles", ("profiles", IkEv2.Nodes.Node.Profiles)), ("keyrings", ("keyrings", IkEv2.Nodes.Node.Keyrings))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.session = IkEv2.Nodes.Node.Session()
                self.session.parent = self
                self._children_name_map["session"] = "session"

                self.sa = IkEv2.Nodes.Node.Sa()
                self.sa.parent = self
                self._children_name_map["sa"] = "sa"

                self.policies = IkEv2.Nodes.Node.Policies()
                self.policies.parent = self
                self._children_name_map["policies"] = "policies"

                self.proposals = IkEv2.Nodes.Node.Proposals()
                self.proposals.parent = self
                self._children_name_map["proposals"] = "proposals"

                self.profiles = IkEv2.Nodes.Node.Profiles()
                self.profiles.parent = self
                self._children_name_map["profiles"] = "profiles"

                self.keyrings = IkEv2.Nodes.Node.Keyrings()
                self.keyrings.parent = self
                self._children_name_map["keyrings"] = "keyrings"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ikev2-oper:ik-ev2/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(IkEv2.Nodes.Node, ['node_name'], name, value)


            class Session(_Entity_):
                """
                IKEv2 Session data
                
                .. attribute:: session
                
                	Session List
                	**type**\: list of  		 :py:class:`Session_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes.Node.Session.Session_>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ikev2-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(IkEv2.Nodes.Node.Session, self).__init__()

                    self.yang_name = "session"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("session", ("session", IkEv2.Nodes.Node.Session.Session_))])
                    self._leafs = OrderedDict()

                    self.session = YList(self)
                    self._segment_path = lambda: "session"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(IkEv2.Nodes.Node.Session, [], name, value)


                class Session_(_Entity_):
                    """
                    Session List
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: session_status
                    
                    	Session Status
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: ike_cnt
                    
                    	IKE Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: child_cnt
                    
                    	Child Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sa
                    
                    	SA List
                    	**type**\: list of  		 :py:class:`Sa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes.Node.Session.Session_.Sa>`
                    
                    	**config**\: False
                    
                    .. attribute:: child_sa
                    
                    	Child SA List
                    	**type**\: list of  		 :py:class:`ChildSa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes.Node.Session.Session_.ChildSa>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ikev2-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(IkEv2.Nodes.Node.Session.Session_, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "session"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sa", ("sa", IkEv2.Nodes.Node.Session.Session_.Sa)), ("child-sa", ("child_sa", IkEv2.Nodes.Node.Session.Session_.ChildSa))])
                        self._leafs = OrderedDict([
                            ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                            ('session_status', (YLeaf(YType.str, 'session-status'), ['str'])),
                            ('ike_cnt', (YLeaf(YType.uint32, 'ike-cnt'), ['int'])),
                            ('child_cnt', (YLeaf(YType.uint32, 'child-cnt'), ['int'])),
                        ])
                        self.session_id = None
                        self.session_status = None
                        self.ike_cnt = None
                        self.child_cnt = None

                        self.sa = YList(self)
                        self.child_sa = YList(self)
                        self._segment_path = lambda: "session"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(IkEv2.Nodes.Node.Session.Session_, ['session_id', 'session_status', 'ike_cnt', 'child_cnt'], name, value)


                    class Sa(_Entity_):
                        """
                        SA List
                        
                        .. attribute:: tunnel_id
                        
                        	Tunnel ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: local_addr_port
                        
                        	Local Addr Port
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: remote_addr_port
                        
                        	Remote Addr Port
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: state
                        
                        	State
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: encr
                        
                        	Encryption
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: keysize
                        
                        	Keysize
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: prf
                        
                        	PRF
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: hash
                        
                        	Hash
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: dh_group
                        
                        	DH Group
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: auth_sign
                        
                        	Auth Sign
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: auth_verify
                        
                        	Auth Verify
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: life_active
                        
                        	Life\-Active Time
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: session_id
                        
                        	Session ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: status_desc
                        
                        	Status Description
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: local_spi
                        
                        	Local SPI
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: remote_spi
                        
                        	Remote SPI
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: local_id
                        
                        	Local ID
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: remote_id
                        
                        	Remote ID
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: sa_initiator
                        
                        	Sa Initiator
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ikev2-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(IkEv2.Nodes.Node.Session.Session_.Sa, self).__init__()

                            self.yang_name = "sa"
                            self.yang_parent_name = "session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('tunnel_id', (YLeaf(YType.uint32, 'tunnel-id'), ['int'])),
                                ('local_addr_port', (YLeaf(YType.str, 'local-addr-port'), ['str'])),
                                ('remote_addr_port', (YLeaf(YType.str, 'remote-addr-port'), ['str'])),
                                ('state', (YLeaf(YType.str, 'state'), ['str'])),
                                ('encr', (YLeaf(YType.str, 'encr'), ['str'])),
                                ('keysize', (YLeaf(YType.uint32, 'keysize'), ['int'])),
                                ('prf', (YLeaf(YType.str, 'prf'), ['str'])),
                                ('hash', (YLeaf(YType.str, 'hash'), ['str'])),
                                ('dh_group', (YLeaf(YType.uint32, 'dh-group'), ['int'])),
                                ('auth_sign', (YLeaf(YType.str, 'auth-sign'), ['str'])),
                                ('auth_verify', (YLeaf(YType.str, 'auth-verify'), ['str'])),
                                ('life_active', (YLeaf(YType.str, 'life-active'), ['str'])),
                                ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                                ('status_desc', (YLeaf(YType.str, 'status-desc'), ['str'])),
                                ('local_spi', (YLeaf(YType.str, 'local-spi'), ['str'])),
                                ('remote_spi', (YLeaf(YType.str, 'remote-spi'), ['str'])),
                                ('local_id', (YLeaf(YType.str, 'local-id'), ['str'])),
                                ('remote_id', (YLeaf(YType.str, 'remote-id'), ['str'])),
                                ('sa_initiator', (YLeaf(YType.boolean, 'sa-initiator'), ['bool'])),
                            ])
                            self.tunnel_id = None
                            self.local_addr_port = None
                            self.remote_addr_port = None
                            self.state = None
                            self.encr = None
                            self.keysize = None
                            self.prf = None
                            self.hash = None
                            self.dh_group = None
                            self.auth_sign = None
                            self.auth_verify = None
                            self.life_active = None
                            self.session_id = None
                            self.status_desc = None
                            self.local_spi = None
                            self.remote_spi = None
                            self.local_id = None
                            self.remote_id = None
                            self.sa_initiator = None
                            self._segment_path = lambda: "sa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(IkEv2.Nodes.Node.Session.Session_.Sa, ['tunnel_id', 'local_addr_port', 'remote_addr_port', 'state', 'encr', 'keysize', 'prf', 'hash', 'dh_group', 'auth_sign', 'auth_verify', 'life_active', 'session_id', 'status_desc', 'local_spi', 'remote_spi', 'local_id', 'remote_id', 'sa_initiator'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
                            return meta._meta_table['IkEv2.Nodes.Node.Session.Session_.Sa']['meta_info']


                    class ChildSa(_Entity_):
                        """
                        Child SA List
                        
                        .. attribute:: local_selector
                        
                        	Local Selector
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: remote_selector
                        
                        	Remote Selector
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: esp_spi_in_out
                        
                        	ESP SPI In Out
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: encr
                        
                        	Encryption
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: keysize
                        
                        	Keysize
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: hmac
                        
                        	ESP HMAC
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ikev2-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(IkEv2.Nodes.Node.Session.Session_.ChildSa, self).__init__()

                            self.yang_name = "child-sa"
                            self.yang_parent_name = "session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('local_selector', (YLeaf(YType.str, 'local-selector'), ['str'])),
                                ('remote_selector', (YLeaf(YType.str, 'remote-selector'), ['str'])),
                                ('esp_spi_in_out', (YLeaf(YType.str, 'esp-spi-in-out'), ['str'])),
                                ('encr', (YLeaf(YType.str, 'encr'), ['str'])),
                                ('keysize', (YLeaf(YType.uint32, 'keysize'), ['int'])),
                                ('hmac', (YLeaf(YType.str, 'hmac'), ['str'])),
                            ])
                            self.local_selector = None
                            self.remote_selector = None
                            self.esp_spi_in_out = None
                            self.encr = None
                            self.keysize = None
                            self.hmac = None
                            self._segment_path = lambda: "child-sa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(IkEv2.Nodes.Node.Session.Session_.ChildSa, ['local_selector', 'remote_selector', 'esp_spi_in_out', 'encr', 'keysize', 'hmac'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
                            return meta._meta_table['IkEv2.Nodes.Node.Session.Session_.ChildSa']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
                        return meta._meta_table['IkEv2.Nodes.Node.Session.Session_']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
                    return meta._meta_table['IkEv2.Nodes.Node.Session']['meta_info']


            class Sa(_Entity_):
                """
                IKEv2 SA data
                
                .. attribute:: local_v4
                
                	IKEv2 SA lookup on local IP
                	**type**\:  :py:class:`LocalV4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes.Node.Sa.LocalV4>`
                
                	**config**\: False
                
                .. attribute:: remote_v4
                
                	IKEv2 SA lookup on remote IP
                	**type**\:  :py:class:`RemoteV4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes.Node.Sa.RemoteV4>`
                
                	**config**\: False
                
                .. attribute:: all
                
                	IKEv2 SA all data
                	**type**\:  :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes.Node.Sa.All>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ikev2-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(IkEv2.Nodes.Node.Sa, self).__init__()

                    self.yang_name = "sa"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("local-v4", ("local_v4", IkEv2.Nodes.Node.Sa.LocalV4)), ("remote-v4", ("remote_v4", IkEv2.Nodes.Node.Sa.RemoteV4)), ("all", ("all", IkEv2.Nodes.Node.Sa.All))])
                    self._leafs = OrderedDict()

                    self.local_v4 = IkEv2.Nodes.Node.Sa.LocalV4()
                    self.local_v4.parent = self
                    self._children_name_map["local_v4"] = "local-v4"

                    self.remote_v4 = IkEv2.Nodes.Node.Sa.RemoteV4()
                    self.remote_v4.parent = self
                    self._children_name_map["remote_v4"] = "remote-v4"

                    self.all = IkEv2.Nodes.Node.Sa.All()
                    self.all.parent = self
                    self._children_name_map["all"] = "all"
                    self._segment_path = lambda: "sa"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(IkEv2.Nodes.Node.Sa, [], name, value)


                class LocalV4(_Entity_):
                    """
                    IKEv2 SA lookup on local IP
                    
                    .. attribute:: ip
                    
                    	IKEv2 SA data based on address
                    	**type**\: list of  		 :py:class:`Ip <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes.Node.Sa.LocalV4.Ip>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ikev2-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(IkEv2.Nodes.Node.Sa.LocalV4, self).__init__()

                        self.yang_name = "local-v4"
                        self.yang_parent_name = "sa"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ip", ("ip", IkEv2.Nodes.Node.Sa.LocalV4.Ip))])
                        self._leafs = OrderedDict()

                        self.ip = YList(self)
                        self._segment_path = lambda: "local-v4"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(IkEv2.Nodes.Node.Sa.LocalV4, [], name, value)


                    class Ip(_Entity_):
                        """
                        IKEv2 SA data based on address
                        
                        .. attribute:: address  (key)
                        
                        	Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: sa
                        
                        	SA list
                        	**type**\: list of  		 :py:class:`Sa_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes.Node.Sa.LocalV4.Ip.Sa_>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ikev2-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(IkEv2.Nodes.Node.Sa.LocalV4.Ip, self).__init__()

                            self.yang_name = "ip"
                            self.yang_parent_name = "local-v4"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['address']
                            self._child_classes = OrderedDict([("sa", ("sa", IkEv2.Nodes.Node.Sa.LocalV4.Ip.Sa_))])
                            self._leafs = OrderedDict([
                                ('address', (YLeaf(YType.str, 'address'), ['str'])),
                            ])
                            self.address = None

                            self.sa = YList(self)
                            self._segment_path = lambda: "ip" + "[address='" + str(self.address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(IkEv2.Nodes.Node.Sa.LocalV4.Ip, ['address'], name, value)


                        class Sa_(_Entity_):
                            """
                            SA list
                            
                            .. attribute:: tunnel_id
                            
                            	Tunnel ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: local_addr_port
                            
                            	Local Addr Port
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: remote_addr_port
                            
                            	Remote Addr Port
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: state
                            
                            	State
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: encr
                            
                            	Encryption
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: keysize
                            
                            	Keysize
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: prf
                            
                            	PRF
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: hash
                            
                            	Hash
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: dh_group
                            
                            	DH Group
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: auth_sign
                            
                            	Auth Sign
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: auth_verify
                            
                            	Auth Verify
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: life_active
                            
                            	Life\-Active Time
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: session_id
                            
                            	Session ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: status_desc
                            
                            	Status Description
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: local_spi
                            
                            	Local SPI
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: remote_spi
                            
                            	Remote SPI
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: local_id
                            
                            	Local ID
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: remote_id
                            
                            	Remote ID
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: sa_initiator
                            
                            	Sa Initiator
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ikev2-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(IkEv2.Nodes.Node.Sa.LocalV4.Ip.Sa_, self).__init__()

                                self.yang_name = "sa"
                                self.yang_parent_name = "ip"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('tunnel_id', (YLeaf(YType.uint32, 'tunnel-id'), ['int'])),
                                    ('local_addr_port', (YLeaf(YType.str, 'local-addr-port'), ['str'])),
                                    ('remote_addr_port', (YLeaf(YType.str, 'remote-addr-port'), ['str'])),
                                    ('state', (YLeaf(YType.str, 'state'), ['str'])),
                                    ('encr', (YLeaf(YType.str, 'encr'), ['str'])),
                                    ('keysize', (YLeaf(YType.uint32, 'keysize'), ['int'])),
                                    ('prf', (YLeaf(YType.str, 'prf'), ['str'])),
                                    ('hash', (YLeaf(YType.str, 'hash'), ['str'])),
                                    ('dh_group', (YLeaf(YType.uint32, 'dh-group'), ['int'])),
                                    ('auth_sign', (YLeaf(YType.str, 'auth-sign'), ['str'])),
                                    ('auth_verify', (YLeaf(YType.str, 'auth-verify'), ['str'])),
                                    ('life_active', (YLeaf(YType.str, 'life-active'), ['str'])),
                                    ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                                    ('status_desc', (YLeaf(YType.str, 'status-desc'), ['str'])),
                                    ('local_spi', (YLeaf(YType.str, 'local-spi'), ['str'])),
                                    ('remote_spi', (YLeaf(YType.str, 'remote-spi'), ['str'])),
                                    ('local_id', (YLeaf(YType.str, 'local-id'), ['str'])),
                                    ('remote_id', (YLeaf(YType.str, 'remote-id'), ['str'])),
                                    ('sa_initiator', (YLeaf(YType.boolean, 'sa-initiator'), ['bool'])),
                                ])
                                self.tunnel_id = None
                                self.local_addr_port = None
                                self.remote_addr_port = None
                                self.state = None
                                self.encr = None
                                self.keysize = None
                                self.prf = None
                                self.hash = None
                                self.dh_group = None
                                self.auth_sign = None
                                self.auth_verify = None
                                self.life_active = None
                                self.session_id = None
                                self.status_desc = None
                                self.local_spi = None
                                self.remote_spi = None
                                self.local_id = None
                                self.remote_id = None
                                self.sa_initiator = None
                                self._segment_path = lambda: "sa"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(IkEv2.Nodes.Node.Sa.LocalV4.Ip.Sa_, ['tunnel_id', 'local_addr_port', 'remote_addr_port', 'state', 'encr', 'keysize', 'prf', 'hash', 'dh_group', 'auth_sign', 'auth_verify', 'life_active', 'session_id', 'status_desc', 'local_spi', 'remote_spi', 'local_id', 'remote_id', 'sa_initiator'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
                                return meta._meta_table['IkEv2.Nodes.Node.Sa.LocalV4.Ip.Sa_']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
                            return meta._meta_table['IkEv2.Nodes.Node.Sa.LocalV4.Ip']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
                        return meta._meta_table['IkEv2.Nodes.Node.Sa.LocalV4']['meta_info']


                class RemoteV4(_Entity_):
                    """
                    IKEv2 SA lookup on remote IP
                    
                    .. attribute:: ip
                    
                    	IKEv2 SA data based on address
                    	**type**\: list of  		 :py:class:`Ip <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes.Node.Sa.RemoteV4.Ip>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ikev2-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(IkEv2.Nodes.Node.Sa.RemoteV4, self).__init__()

                        self.yang_name = "remote-v4"
                        self.yang_parent_name = "sa"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ip", ("ip", IkEv2.Nodes.Node.Sa.RemoteV4.Ip))])
                        self._leafs = OrderedDict()

                        self.ip = YList(self)
                        self._segment_path = lambda: "remote-v4"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(IkEv2.Nodes.Node.Sa.RemoteV4, [], name, value)


                    class Ip(_Entity_):
                        """
                        IKEv2 SA data based on address
                        
                        .. attribute:: address  (key)
                        
                        	Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: sa
                        
                        	SA list
                        	**type**\: list of  		 :py:class:`Sa_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes.Node.Sa.RemoteV4.Ip.Sa_>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ikev2-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(IkEv2.Nodes.Node.Sa.RemoteV4.Ip, self).__init__()

                            self.yang_name = "ip"
                            self.yang_parent_name = "remote-v4"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['address']
                            self._child_classes = OrderedDict([("sa", ("sa", IkEv2.Nodes.Node.Sa.RemoteV4.Ip.Sa_))])
                            self._leafs = OrderedDict([
                                ('address', (YLeaf(YType.str, 'address'), ['str'])),
                            ])
                            self.address = None

                            self.sa = YList(self)
                            self._segment_path = lambda: "ip" + "[address='" + str(self.address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(IkEv2.Nodes.Node.Sa.RemoteV4.Ip, ['address'], name, value)


                        class Sa_(_Entity_):
                            """
                            SA list
                            
                            .. attribute:: tunnel_id
                            
                            	Tunnel ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: local_addr_port
                            
                            	Local Addr Port
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: remote_addr_port
                            
                            	Remote Addr Port
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: state
                            
                            	State
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: encr
                            
                            	Encryption
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: keysize
                            
                            	Keysize
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: prf
                            
                            	PRF
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: hash
                            
                            	Hash
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: dh_group
                            
                            	DH Group
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: auth_sign
                            
                            	Auth Sign
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: auth_verify
                            
                            	Auth Verify
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: life_active
                            
                            	Life\-Active Time
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: session_id
                            
                            	Session ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: status_desc
                            
                            	Status Description
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: local_spi
                            
                            	Local SPI
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: remote_spi
                            
                            	Remote SPI
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: local_id
                            
                            	Local ID
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: remote_id
                            
                            	Remote ID
                            	**type**\: str
                            
                            	**config**\: False
                            
                            .. attribute:: sa_initiator
                            
                            	Sa Initiator
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ikev2-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(IkEv2.Nodes.Node.Sa.RemoteV4.Ip.Sa_, self).__init__()

                                self.yang_name = "sa"
                                self.yang_parent_name = "ip"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('tunnel_id', (YLeaf(YType.uint32, 'tunnel-id'), ['int'])),
                                    ('local_addr_port', (YLeaf(YType.str, 'local-addr-port'), ['str'])),
                                    ('remote_addr_port', (YLeaf(YType.str, 'remote-addr-port'), ['str'])),
                                    ('state', (YLeaf(YType.str, 'state'), ['str'])),
                                    ('encr', (YLeaf(YType.str, 'encr'), ['str'])),
                                    ('keysize', (YLeaf(YType.uint32, 'keysize'), ['int'])),
                                    ('prf', (YLeaf(YType.str, 'prf'), ['str'])),
                                    ('hash', (YLeaf(YType.str, 'hash'), ['str'])),
                                    ('dh_group', (YLeaf(YType.uint32, 'dh-group'), ['int'])),
                                    ('auth_sign', (YLeaf(YType.str, 'auth-sign'), ['str'])),
                                    ('auth_verify', (YLeaf(YType.str, 'auth-verify'), ['str'])),
                                    ('life_active', (YLeaf(YType.str, 'life-active'), ['str'])),
                                    ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                                    ('status_desc', (YLeaf(YType.str, 'status-desc'), ['str'])),
                                    ('local_spi', (YLeaf(YType.str, 'local-spi'), ['str'])),
                                    ('remote_spi', (YLeaf(YType.str, 'remote-spi'), ['str'])),
                                    ('local_id', (YLeaf(YType.str, 'local-id'), ['str'])),
                                    ('remote_id', (YLeaf(YType.str, 'remote-id'), ['str'])),
                                    ('sa_initiator', (YLeaf(YType.boolean, 'sa-initiator'), ['bool'])),
                                ])
                                self.tunnel_id = None
                                self.local_addr_port = None
                                self.remote_addr_port = None
                                self.state = None
                                self.encr = None
                                self.keysize = None
                                self.prf = None
                                self.hash = None
                                self.dh_group = None
                                self.auth_sign = None
                                self.auth_verify = None
                                self.life_active = None
                                self.session_id = None
                                self.status_desc = None
                                self.local_spi = None
                                self.remote_spi = None
                                self.local_id = None
                                self.remote_id = None
                                self.sa_initiator = None
                                self._segment_path = lambda: "sa"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(IkEv2.Nodes.Node.Sa.RemoteV4.Ip.Sa_, ['tunnel_id', 'local_addr_port', 'remote_addr_port', 'state', 'encr', 'keysize', 'prf', 'hash', 'dh_group', 'auth_sign', 'auth_verify', 'life_active', 'session_id', 'status_desc', 'local_spi', 'remote_spi', 'local_id', 'remote_id', 'sa_initiator'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
                                return meta._meta_table['IkEv2.Nodes.Node.Sa.RemoteV4.Ip.Sa_']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
                            return meta._meta_table['IkEv2.Nodes.Node.Sa.RemoteV4.Ip']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
                        return meta._meta_table['IkEv2.Nodes.Node.Sa.RemoteV4']['meta_info']


                class All(_Entity_):
                    """
                    IKEv2 SA all data
                    
                    .. attribute:: sa
                    
                    	SA list
                    	**type**\: list of  		 :py:class:`Sa_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes.Node.Sa.All.Sa_>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ikev2-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(IkEv2.Nodes.Node.Sa.All, self).__init__()

                        self.yang_name = "all"
                        self.yang_parent_name = "sa"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sa", ("sa", IkEv2.Nodes.Node.Sa.All.Sa_))])
                        self._leafs = OrderedDict()

                        self.sa = YList(self)
                        self._segment_path = lambda: "all"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(IkEv2.Nodes.Node.Sa.All, [], name, value)


                    class Sa_(_Entity_):
                        """
                        SA list
                        
                        .. attribute:: tunnel_id
                        
                        	Tunnel ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: local_addr_port
                        
                        	Local Addr Port
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: remote_addr_port
                        
                        	Remote Addr Port
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: state
                        
                        	State
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: encr
                        
                        	Encryption
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: keysize
                        
                        	Keysize
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: prf
                        
                        	PRF
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: hash
                        
                        	Hash
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: dh_group
                        
                        	DH Group
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: auth_sign
                        
                        	Auth Sign
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: auth_verify
                        
                        	Auth Verify
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: life_active
                        
                        	Life\-Active Time
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: session_id
                        
                        	Session ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: status_desc
                        
                        	Status Description
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: local_spi
                        
                        	Local SPI
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: remote_spi
                        
                        	Remote SPI
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: local_id
                        
                        	Local ID
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: remote_id
                        
                        	Remote ID
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: sa_initiator
                        
                        	Sa Initiator
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ikev2-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(IkEv2.Nodes.Node.Sa.All.Sa_, self).__init__()

                            self.yang_name = "sa"
                            self.yang_parent_name = "all"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('tunnel_id', (YLeaf(YType.uint32, 'tunnel-id'), ['int'])),
                                ('local_addr_port', (YLeaf(YType.str, 'local-addr-port'), ['str'])),
                                ('remote_addr_port', (YLeaf(YType.str, 'remote-addr-port'), ['str'])),
                                ('state', (YLeaf(YType.str, 'state'), ['str'])),
                                ('encr', (YLeaf(YType.str, 'encr'), ['str'])),
                                ('keysize', (YLeaf(YType.uint32, 'keysize'), ['int'])),
                                ('prf', (YLeaf(YType.str, 'prf'), ['str'])),
                                ('hash', (YLeaf(YType.str, 'hash'), ['str'])),
                                ('dh_group', (YLeaf(YType.uint32, 'dh-group'), ['int'])),
                                ('auth_sign', (YLeaf(YType.str, 'auth-sign'), ['str'])),
                                ('auth_verify', (YLeaf(YType.str, 'auth-verify'), ['str'])),
                                ('life_active', (YLeaf(YType.str, 'life-active'), ['str'])),
                                ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                                ('status_desc', (YLeaf(YType.str, 'status-desc'), ['str'])),
                                ('local_spi', (YLeaf(YType.str, 'local-spi'), ['str'])),
                                ('remote_spi', (YLeaf(YType.str, 'remote-spi'), ['str'])),
                                ('local_id', (YLeaf(YType.str, 'local-id'), ['str'])),
                                ('remote_id', (YLeaf(YType.str, 'remote-id'), ['str'])),
                                ('sa_initiator', (YLeaf(YType.boolean, 'sa-initiator'), ['bool'])),
                            ])
                            self.tunnel_id = None
                            self.local_addr_port = None
                            self.remote_addr_port = None
                            self.state = None
                            self.encr = None
                            self.keysize = None
                            self.prf = None
                            self.hash = None
                            self.dh_group = None
                            self.auth_sign = None
                            self.auth_verify = None
                            self.life_active = None
                            self.session_id = None
                            self.status_desc = None
                            self.local_spi = None
                            self.remote_spi = None
                            self.local_id = None
                            self.remote_id = None
                            self.sa_initiator = None
                            self._segment_path = lambda: "sa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(IkEv2.Nodes.Node.Sa.All.Sa_, ['tunnel_id', 'local_addr_port', 'remote_addr_port', 'state', 'encr', 'keysize', 'prf', 'hash', 'dh_group', 'auth_sign', 'auth_verify', 'life_active', 'session_id', 'status_desc', 'local_spi', 'remote_spi', 'local_id', 'remote_id', 'sa_initiator'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
                            return meta._meta_table['IkEv2.Nodes.Node.Sa.All.Sa_']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
                        return meta._meta_table['IkEv2.Nodes.Node.Sa.All']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
                    return meta._meta_table['IkEv2.Nodes.Node.Sa']['meta_info']


            class Policies(_Entity_):
                """
                IKEv2 policies on this node
                
                .. attribute:: policy
                
                	IKEv2 policy data
                	**type**\: list of  		 :py:class:`Policy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes.Node.Policies.Policy>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ikev2-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(IkEv2.Nodes.Node.Policies, self).__init__()

                    self.yang_name = "policies"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("policy", ("policy", IkEv2.Nodes.Node.Policies.Policy))])
                    self._leafs = OrderedDict()

                    self.policy = YList(self)
                    self._segment_path = lambda: "policies"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(IkEv2.Nodes.Node.Policies, [], name, value)


                class Policy(_Entity_):
                    """
                    IKEv2 policy data
                    
                    .. attribute:: name  (key)
                    
                    	Name of the IKEv2 policy
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    	**config**\: False
                    
                    .. attribute:: policy_name
                    
                    	Name of the policy
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: addr
                    
                    	Match address of peer
                    	**type**\: list of str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: proposal
                    
                    	List of proposals
                    	**type**\: list of str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ikev2-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(IkEv2.Nodes.Node.Policies.Policy, self).__init__()

                        self.yang_name = "policy"
                        self.yang_parent_name = "policies"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                            ('addr', (YLeafList(YType.str, 'addr'), ['str'])),
                            ('proposal', (YLeafList(YType.str, 'proposal'), ['str'])),
                        ])
                        self.name = None
                        self.policy_name = None
                        self.addr = []
                        self.proposal = []
                        self._segment_path = lambda: "policy" + "[name='" + str(self.name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(IkEv2.Nodes.Node.Policies.Policy, ['name', 'policy_name', 'addr', 'proposal'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
                        return meta._meta_table['IkEv2.Nodes.Node.Policies.Policy']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
                    return meta._meta_table['IkEv2.Nodes.Node.Policies']['meta_info']


            class Proposals(_Entity_):
                """
                IKEv2 proposals on this node
                
                .. attribute:: proposal
                
                	IKEv2 proposal data
                	**type**\: list of  		 :py:class:`Proposal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes.Node.Proposals.Proposal>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ikev2-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(IkEv2.Nodes.Node.Proposals, self).__init__()

                    self.yang_name = "proposals"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("proposal", ("proposal", IkEv2.Nodes.Node.Proposals.Proposal))])
                    self._leafs = OrderedDict()

                    self.proposal = YList(self)
                    self._segment_path = lambda: "proposals"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(IkEv2.Nodes.Node.Proposals, [], name, value)


                class Proposal(_Entity_):
                    """
                    IKEv2 proposal data
                    
                    .. attribute:: name  (key)
                    
                    	Name of the IKEv2 proposal
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    	**config**\: False
                    
                    .. attribute:: proposal_name
                    
                    	Name of the proposal
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: encryption_alg
                    
                    	Encryption Algorithm
                    	**type**\: list of str
                    
                    	**config**\: False
                    
                    .. attribute:: hash_alg
                    
                    	Integrity Algorithm
                    	**type**\: list of str
                    
                    	**config**\: False
                    
                    .. attribute:: prf_alg
                    
                    	PRF Algorithm
                    	**type**\: list of str
                    
                    	**config**\: False
                    
                    .. attribute:: group_alg
                    
                    	Group Algorithm
                    	**type**\: list of str
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ikev2-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(IkEv2.Nodes.Node.Proposals.Proposal, self).__init__()

                        self.yang_name = "proposal"
                        self.yang_parent_name = "proposals"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('proposal_name', (YLeaf(YType.str, 'proposal-name'), ['str'])),
                            ('encryption_alg', (YLeafList(YType.str, 'encryption-alg'), ['str'])),
                            ('hash_alg', (YLeafList(YType.str, 'hash-alg'), ['str'])),
                            ('prf_alg', (YLeafList(YType.str, 'prf-alg'), ['str'])),
                            ('group_alg', (YLeafList(YType.str, 'group-alg'), ['str'])),
                        ])
                        self.name = None
                        self.proposal_name = None
                        self.encryption_alg = []
                        self.hash_alg = []
                        self.prf_alg = []
                        self.group_alg = []
                        self._segment_path = lambda: "proposal" + "[name='" + str(self.name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(IkEv2.Nodes.Node.Proposals.Proposal, ['name', 'proposal_name', 'encryption_alg', 'hash_alg', 'prf_alg', 'group_alg'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
                        return meta._meta_table['IkEv2.Nodes.Node.Proposals.Proposal']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
                    return meta._meta_table['IkEv2.Nodes.Node.Proposals']['meta_info']


            class Profiles(_Entity_):
                """
                IKEv2 profiles on this node
                
                .. attribute:: profile
                
                	IKEv2 profile data
                	**type**\: list of  		 :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes.Node.Profiles.Profile>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ikev2-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(IkEv2.Nodes.Node.Profiles, self).__init__()

                    self.yang_name = "profiles"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("profile", ("profile", IkEv2.Nodes.Node.Profiles.Profile))])
                    self._leafs = OrderedDict()

                    self.profile = YList(self)
                    self._segment_path = lambda: "profiles"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(IkEv2.Nodes.Node.Profiles, [], name, value)


                class Profile(_Entity_):
                    """
                    IKEv2 profile data
                    
                    .. attribute:: name  (key)
                    
                    	Name of the IKEv2 profile
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    	**config**\: False
                    
                    .. attribute:: profile_name
                    
                    	Name of the Profile
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: keyring_name
                    
                    	Name of the keyring
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: match_any
                    
                    	Match Any Criteria
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: lifetime
                    
                    	Lifetime
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: dpd_interval
                    
                    	DPD Interval
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: dpd_retry
                    
                    	DPD Retry
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: addr
                    
                    	Match address of peer
                    	**type**\: list of str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: mask
                    
                    	Mask of peer
                    	**type**\: list of str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ikev2-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(IkEv2.Nodes.Node.Profiles.Profile, self).__init__()

                        self.yang_name = "profile"
                        self.yang_parent_name = "profiles"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                            ('keyring_name', (YLeaf(YType.str, 'keyring-name'), ['str'])),
                            ('match_any', (YLeaf(YType.boolean, 'match-any'), ['bool'])),
                            ('lifetime', (YLeaf(YType.uint32, 'lifetime'), ['int'])),
                            ('dpd_interval', (YLeaf(YType.uint32, 'dpd-interval'), ['int'])),
                            ('dpd_retry', (YLeaf(YType.uint32, 'dpd-retry'), ['int'])),
                            ('addr', (YLeafList(YType.str, 'addr'), ['str'])),
                            ('mask', (YLeafList(YType.str, 'mask'), ['str'])),
                        ])
                        self.name = None
                        self.profile_name = None
                        self.keyring_name = None
                        self.match_any = None
                        self.lifetime = None
                        self.dpd_interval = None
                        self.dpd_retry = None
                        self.addr = []
                        self.mask = []
                        self._segment_path = lambda: "profile" + "[name='" + str(self.name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(IkEv2.Nodes.Node.Profiles.Profile, ['name', 'profile_name', 'keyring_name', 'match_any', 'lifetime', 'dpd_interval', 'dpd_retry', 'addr', 'mask'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
                        return meta._meta_table['IkEv2.Nodes.Node.Profiles.Profile']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
                    return meta._meta_table['IkEv2.Nodes.Node.Profiles']['meta_info']


            class Keyrings(_Entity_):
                """
                IKEv2 keyrings on this node
                
                .. attribute:: keyring
                
                	IKEv2 keyring data
                	**type**\: list of  		 :py:class:`Keyring <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes.Node.Keyrings.Keyring>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ikev2-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(IkEv2.Nodes.Node.Keyrings, self).__init__()

                    self.yang_name = "keyrings"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("keyring", ("keyring", IkEv2.Nodes.Node.Keyrings.Keyring))])
                    self._leafs = OrderedDict()

                    self.keyring = YList(self)
                    self._segment_path = lambda: "keyrings"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(IkEv2.Nodes.Node.Keyrings, [], name, value)


                class Keyring(_Entity_):
                    """
                    IKEv2 keyring data
                    
                    .. attribute:: name  (key)
                    
                    	Name of the IKEv2 keyring
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    	**config**\: False
                    
                    .. attribute:: keyring_name
                    
                    	Name of the Keyring
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: peer
                    
                    	List of peers
                    	**type**\: list of  		 :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ikev2_oper.IkEv2.Nodes.Node.Keyrings.Keyring.Peer>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ikev2-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(IkEv2.Nodes.Node.Keyrings.Keyring, self).__init__()

                        self.yang_name = "keyring"
                        self.yang_parent_name = "keyrings"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name']
                        self._child_classes = OrderedDict([("peer", ("peer", IkEv2.Nodes.Node.Keyrings.Keyring.Peer))])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('keyring_name', (YLeaf(YType.str, 'keyring-name'), ['str'])),
                        ])
                        self.name = None
                        self.keyring_name = None

                        self.peer = YList(self)
                        self._segment_path = lambda: "keyring" + "[name='" + str(self.name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(IkEv2.Nodes.Node.Keyrings.Keyring, ['name', 'keyring_name'], name, value)


                    class Peer(_Entity_):
                        """
                        List of peers
                        
                        .. attribute:: peer_name
                        
                        	Name of the peer
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: ip_address
                        
                        	IP Address of the peer
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: subnet
                        
                        	Subnet mask of the peer
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: local_psk
                        
                        	Local PSK
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: remote_psk
                        
                        	Remote PSK
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ikev2-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(IkEv2.Nodes.Node.Keyrings.Keyring.Peer, self).__init__()

                            self.yang_name = "peer"
                            self.yang_parent_name = "keyring"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('peer_name', (YLeaf(YType.str, 'peer-name'), ['str'])),
                                ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                ('subnet', (YLeaf(YType.str, 'subnet'), ['str'])),
                                ('local_psk', (YLeaf(YType.str, 'local-psk'), ['str'])),
                                ('remote_psk', (YLeaf(YType.str, 'remote-psk'), ['str'])),
                            ])
                            self.peer_name = None
                            self.ip_address = None
                            self.subnet = None
                            self.local_psk = None
                            self.remote_psk = None
                            self._segment_path = lambda: "peer"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(IkEv2.Nodes.Node.Keyrings.Keyring.Peer, ['peer_name', 'ip_address', 'subnet', 'local_psk', 'remote_psk'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
                            return meta._meta_table['IkEv2.Nodes.Node.Keyrings.Keyring.Peer']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
                        return meta._meta_table['IkEv2.Nodes.Node.Keyrings.Keyring']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
                    return meta._meta_table['IkEv2.Nodes.Node.Keyrings']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
                return meta._meta_table['IkEv2.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
            return meta._meta_table['IkEv2.Nodes']['meta_info']

    def clone_ptr(self):
        self._top_entity = IkEv2()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ikev2_oper as meta
        return meta._meta_table['IkEv2']['meta_info']



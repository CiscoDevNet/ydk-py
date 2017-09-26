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

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IedgeLicenseManager(Entity):
    """
    iedge license manager
    
    .. attribute:: node
    
    	Location. For eg., 0/1/CPU0
    	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.IedgeLicenseManager.Node>`
    
    

    """

    _prefix = 'iedge4710-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(IedgeLicenseManager, self).__init__()
        self._top_entity = None

        self.yang_name = "iedge-license-manager"
        self.yang_parent_name = "Cisco-IOS-XR-iedge4710-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"node" : ("node", IedgeLicenseManager.Node)}

        self.node = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-iedge4710-cfg:iedge-license-manager"

    def __setattr__(self, name, value):
        self._perform_setattr(IedgeLicenseManager, [], name, value)


    class Node(Entity):
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
            super(IedgeLicenseManager.Node, self).__init__()

            self.yang_name = "node"
            self.yang_parent_name = "iedge-license-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.node_name = YLeaf(YType.str, "node-name")

            self.session_limit = YLeaf(YType.int32, "session-limit")

            self.session_threshold = YLeaf(YType.int32, "session-threshold")
            self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-iedge4710-cfg:iedge-license-manager/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IedgeLicenseManager.Node, ['node_name', 'session_limit', 'session_threshold'], name, value)

    def clone_ptr(self):
        self._top_entity = IedgeLicenseManager()
        return self._top_entity

class SubManager(Entity):
    """
    sub manager
    
    .. attribute:: location
    
    	Select location
    	**type**\: list of    :py:class:`Location <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.SubManager.Location>`
    
    

    """

    _prefix = 'iedge4710-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(SubManager, self).__init__()
        self._top_entity = None

        self.yang_name = "sub-manager"
        self.yang_parent_name = "Cisco-IOS-XR-iedge4710-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"location" : ("location", SubManager.Location)}

        self.location = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-iedge4710-cfg:sub-manager"

    def __setattr__(self, name, value):
        self._perform_setattr(SubManager, [], name, value)


    class Location(Entity):
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
            super(SubManager.Location, self).__init__()

            self.yang_name = "location"
            self.yang_parent_name = "sub-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"trace" : ("trace", SubManager.Location.Trace)}
            self._child_list_classes = {}

            self.location1 = YLeaf(YType.str, "location1")

            self.history = YLeaf(YType.empty, "history")

            self.trace = SubManager.Location.Trace()
            self.trace.parent = self
            self._children_name_map["trace"] = "trace"
            self._children_yang_names.add("trace")
            self._segment_path = lambda: "location" + "[location1='" + self.location1.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-iedge4710-cfg:sub-manager/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SubManager.Location, ['location1', 'history'], name, value)


        class Trace(Entity):
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
                super(SubManager.Location.Trace, self).__init__()

                self.yang_name = "trace"
                self.yang_parent_name = "location"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.trace_level = YLeaf(YType.int32, "trace-level")
                self._segment_path = lambda: "trace"

            def __setattr__(self, name, value):
                self._perform_setattr(SubManager.Location.Trace, ['trace_level'], name, value)

    def clone_ptr(self):
        self._top_entity = SubManager()
        return self._top_entity

class SubscriberFeaturette(Entity):
    """
    subscriber featurette
    
    .. attribute:: identity_change
    
    	enable identity change processing
    	**type**\: list of    :py:class:`IdentityChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.SubscriberFeaturette.IdentityChange>`
    
    

    """

    _prefix = 'iedge4710-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(SubscriberFeaturette, self).__init__()
        self._top_entity = None

        self.yang_name = "subscriber-featurette"
        self.yang_parent_name = "Cisco-IOS-XR-iedge4710-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"identity-change" : ("identity_change", SubscriberFeaturette.IdentityChange)}

        self.identity_change = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-iedge4710-cfg:subscriber-featurette"

    def __setattr__(self, name, value):
        self._perform_setattr(SubscriberFeaturette, [], name, value)


    class IdentityChange(Entity):
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
            super(SubscriberFeaturette.IdentityChange, self).__init__()

            self.yang_name = "identity-change"
            self.yang_parent_name = "subscriber-featurette"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.identity_change = YLeaf(YType.str, "identity-change")

            self.enable = YLeaf(YType.int32, "enable")
            self._segment_path = lambda: "identity-change" + "[identity-change='" + self.identity_change.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-iedge4710-cfg:subscriber-featurette/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SubscriberFeaturette.IdentityChange, ['identity_change', 'enable'], name, value)

    def clone_ptr(self):
        self._top_entity = SubscriberFeaturette()
        return self._top_entity

class SubscriberManager(Entity):
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
        super(SubscriberManager, self).__init__()
        self._top_entity = None

        self.yang_name = "subscriber-manager"
        self.yang_parent_name = "Cisco-IOS-XR-iedge4710-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"accounting" : ("accounting", SubscriberManager.Accounting), "srg" : ("srg", SubscriberManager.Srg)}
        self._child_list_classes = {}

        self.accounting = SubscriberManager.Accounting()
        self.accounting.parent = self
        self._children_name_map["accounting"] = "accounting"
        self._children_yang_names.add("accounting")

        self.srg = SubscriberManager.Srg()
        self.srg.parent = self
        self._children_name_map["srg"] = "srg"
        self._children_yang_names.add("srg")
        self._segment_path = lambda: "Cisco-IOS-XR-iedge4710-cfg:subscriber-manager"


    class Accounting(Entity):
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
            super(SubscriberManager.Accounting, self).__init__()

            self.yang_name = "accounting"
            self.yang_parent_name = "subscriber-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"interim" : ("interim", SubscriberManager.Accounting.Interim), "send-stop" : ("send_stop", SubscriberManager.Accounting.SendStop)}
            self._child_list_classes = {}

            self.interim = SubscriberManager.Accounting.Interim()
            self.interim.parent = self
            self._children_name_map["interim"] = "interim"
            self._children_yang_names.add("interim")

            self.send_stop = SubscriberManager.Accounting.SendStop()
            self.send_stop.parent = self
            self._children_name_map["send_stop"] = "send-stop"
            self._children_yang_names.add("send-stop")
            self._segment_path = lambda: "accounting"
            self._absolute_path = lambda: "Cisco-IOS-XR-iedge4710-cfg:subscriber-manager/%s" % self._segment_path()


        class Interim(Entity):
            """
            interim accounting related
            
            .. attribute:: variation
            
            	variation of first session or service interim record from configured timeout
            	**type**\:   :py:class:`Variation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.SubscriberManager.Accounting.Interim.Variation>`
            
            

            """

            _prefix = 'iedge4710-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(SubscriberManager.Accounting.Interim, self).__init__()

                self.yang_name = "interim"
                self.yang_parent_name = "accounting"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"variation" : ("variation", SubscriberManager.Accounting.Interim.Variation)}
                self._child_list_classes = {}

                self.variation = SubscriberManager.Accounting.Interim.Variation()
                self.variation.parent = self
                self._children_name_map["variation"] = "variation"
                self._children_yang_names.add("variation")
                self._segment_path = lambda: "interim"
                self._absolute_path = lambda: "Cisco-IOS-XR-iedge4710-cfg:subscriber-manager/accounting/%s" % self._segment_path()


            class Variation(Entity):
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
                    super(SubscriberManager.Accounting.Interim.Variation, self).__init__()

                    self.yang_name = "variation"
                    self.yang_parent_name = "interim"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.maximum_percentage_variation = YLeaf(YType.uint32, "maximum-percentage-variation")
                    self._segment_path = lambda: "variation"
                    self._absolute_path = lambda: "Cisco-IOS-XR-iedge4710-cfg:subscriber-manager/accounting/interim/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriberManager.Accounting.Interim.Variation, ['maximum_percentage_variation'], name, value)


        class SendStop(Entity):
            """
            Accounting send stop feature
            
            .. attribute:: setup_failure
            
            	Setup failure feature
            	**type**\:   :py:class:`SetupFailure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_cfg.SubscriberManager.Accounting.SendStop.SetupFailure>`
            
            

            """

            _prefix = 'iedge4710-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(SubscriberManager.Accounting.SendStop, self).__init__()

                self.yang_name = "send-stop"
                self.yang_parent_name = "accounting"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"setup-failure" : ("setup_failure", SubscriberManager.Accounting.SendStop.SetupFailure)}
                self._child_list_classes = {}

                self.setup_failure = SubscriberManager.Accounting.SendStop.SetupFailure()
                self.setup_failure.parent = self
                self._children_name_map["setup_failure"] = "setup-failure"
                self._children_yang_names.add("setup-failure")
                self._segment_path = lambda: "send-stop"
                self._absolute_path = lambda: "Cisco-IOS-XR-iedge4710-cfg:subscriber-manager/accounting/%s" % self._segment_path()


            class SetupFailure(Entity):
                """
                Setup failure feature
                
                .. attribute:: method_list_name
                
                	AAA List name either default or preconfigured
                	**type**\:  str
                
                

                """

                _prefix = 'iedge4710-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SubscriberManager.Accounting.SendStop.SetupFailure, self).__init__()

                    self.yang_name = "setup-failure"
                    self.yang_parent_name = "send-stop"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.method_list_name = YLeaf(YType.str, "method-list-name")
                    self._segment_path = lambda: "setup-failure"
                    self._absolute_path = lambda: "Cisco-IOS-XR-iedge4710-cfg:subscriber-manager/accounting/send-stop/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriberManager.Accounting.SendStop.SetupFailure, ['method_list_name'], name, value)


    class Srg(Entity):
        """
        SRG specific config
        
        .. attribute:: sync_account_session_id
        
        	sync account session id from master to slave
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'iedge4710-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(SubscriberManager.Srg, self).__init__()

            self.yang_name = "srg"
            self.yang_parent_name = "subscriber-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.sync_account_session_id = YLeaf(YType.empty, "sync-account-session-id")
            self._segment_path = lambda: "srg"
            self._absolute_path = lambda: "Cisco-IOS-XR-iedge4710-cfg:subscriber-manager/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SubscriberManager.Srg, ['sync_account_session_id'], name, value)

    def clone_ptr(self):
        self._top_entity = SubscriberManager()
        return self._top_entity


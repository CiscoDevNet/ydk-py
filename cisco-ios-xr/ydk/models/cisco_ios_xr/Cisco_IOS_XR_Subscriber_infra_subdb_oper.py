""" Cisco_IOS_XR_Subscriber_infra_subdb_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR Subscriber\-infra\-subdb package operational data.

This module contains definitions
for the following management objects\:
  subscriber\-database\: Subscriber database operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SessionState(Enum):
    """
    SessionState (Enum Class)

    Session states

    .. data:: init = 1

    	Initialisation

    .. data:: destroy = 2

    	Destroy

    .. data:: config_generate = 3

    	Config generate

    .. data:: feature_registration_wait = 4

    	Feature registration wait

    .. data:: config_apply = 5

    	Config apply

    .. data:: config_done = 6

    	Config done

    .. data:: config_removed = 7

    	Config removed

    .. data:: config_error = 8

    	Config error

    .. data:: error = 9

    	Error

    .. data:: sync = 11

    	Sync

    """

    init = Enum.YLeaf(1, "init")

    destroy = Enum.YLeaf(2, "destroy")

    config_generate = Enum.YLeaf(3, "config-generate")

    feature_registration_wait = Enum.YLeaf(4, "feature-registration-wait")

    config_apply = Enum.YLeaf(5, "config-apply")

    config_done = Enum.YLeaf(6, "config-done")

    config_removed = Enum.YLeaf(7, "config-removed")

    config_error = Enum.YLeaf(8, "config-error")

    error = Enum.YLeaf(9, "error")

    sync = Enum.YLeaf(11, "sync")


class SubdbObjectTypeData(Enum):
    """
    SubdbObjectTypeData (Enum Class)

    Template types

    .. data:: user_profile = 1

    	User profile

    .. data:: service_profile = 2

    	Service profile

    .. data:: subscriber_service = 3

    	Subscriber service template

    .. data:: ppp = 4

    	PPP template

    .. data:: ip_subscriber = 5

    	IP subscriber template

    """

    user_profile = Enum.YLeaf(1, "user-profile")

    service_profile = Enum.YLeaf(2, "service-profile")

    subscriber_service = Enum.YLeaf(3, "subscriber-service")

    ppp = Enum.YLeaf(4, "ppp")

    ip_subscriber = Enum.YLeaf(5, "ip-subscriber")



class SubscriberDatabase(Entity):
    """
    Subscriber database operational data
    
    .. attribute:: nodes
    
    	List of nodes for which subscriber data is collected
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper.SubscriberDatabase.Nodes>`
    
    

    """

    _prefix = 'subscriber-infra-subdb-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(SubscriberDatabase, self).__init__()
        self._top_entity = None

        self.yang_name = "subscriber-database"
        self.yang_parent_name = "Cisco-IOS-XR-Subscriber-infra-subdb-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", SubscriberDatabase.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = SubscriberDatabase.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-Subscriber-infra-subdb-oper:subscriber-database"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SubscriberDatabase, [], name, value)


    class Nodes(Entity):
        """
        List of nodes for which subscriber data is
        collected
        
        .. attribute:: node
        
        	Subscriber data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper.SubscriberDatabase.Nodes.Node>`
        
        

        """

        _prefix = 'subscriber-infra-subdb-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SubscriberDatabase.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "subscriber-database"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", SubscriberDatabase.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-Subscriber-infra-subdb-oper:subscriber-database/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SubscriberDatabase.Nodes, [], name, value)


        class Node(Entity):
            """
            Subscriber data for a particular node
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: association
            
            	Subscriber data for associated templates
            	**type**\:  :py:class:`Association <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper.SubscriberDatabase.Nodes.Node.Association>`
            
            .. attribute:: summary
            
            	Subscriber data for associated templates
            	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper.SubscriberDatabase.Nodes.Node.Summary>`
            
            .. attribute:: session
            
            	Subscriber management session information
            	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper.SubscriberDatabase.Nodes.Node.Session>`
            
            

            """

            _prefix = 'subscriber-infra-subdb-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SubscriberDatabase.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("association", ("association", SubscriberDatabase.Nodes.Node.Association)), ("summary", ("summary", SubscriberDatabase.Nodes.Node.Summary)), ("session", ("session", SubscriberDatabase.Nodes.Node.Session))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.association = SubscriberDatabase.Nodes.Node.Association()
                self.association.parent = self
                self._children_name_map["association"] = "association"

                self.summary = SubscriberDatabase.Nodes.Node.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"

                self.session = SubscriberDatabase.Nodes.Node.Session()
                self.session.parent = self
                self._children_name_map["session"] = "session"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-Subscriber-infra-subdb-oper:subscriber-database/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SubscriberDatabase.Nodes.Node, ['node_name'], name, value)


            class Association(Entity):
                """
                Subscriber data for associated templates
                
                .. attribute:: labels
                
                	List of associated subscriber labels
                	**type**\:  :py:class:`Labels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper.SubscriberDatabase.Nodes.Node.Association.Labels>`
                
                

                """

                _prefix = 'subscriber-infra-subdb-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SubscriberDatabase.Nodes.Node.Association, self).__init__()

                    self.yang_name = "association"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("labels", ("labels", SubscriberDatabase.Nodes.Node.Association.Labels))])
                    self._leafs = OrderedDict()

                    self.labels = SubscriberDatabase.Nodes.Node.Association.Labels()
                    self.labels.parent = self
                    self._children_name_map["labels"] = "labels"
                    self._segment_path = lambda: "association"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriberDatabase.Nodes.Node.Association, [], name, value)


                class Labels(Entity):
                    """
                    List of associated subscriber labels
                    
                    .. attribute:: label
                    
                    	Association for a given subscriber label
                    	**type**\: list of  		 :py:class:`Label <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper.SubscriberDatabase.Nodes.Node.Association.Labels.Label>`
                    
                    

                    """

                    _prefix = 'subscriber-infra-subdb-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SubscriberDatabase.Nodes.Node.Association.Labels, self).__init__()

                        self.yang_name = "labels"
                        self.yang_parent_name = "association"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("label", ("label", SubscriberDatabase.Nodes.Node.Association.Labels.Label))])
                        self._leafs = OrderedDict()

                        self.label = YList(self)
                        self._segment_path = lambda: "labels"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberDatabase.Nodes.Node.Association.Labels, [], name, value)


                    class Label(Entity):
                        """
                        Association for a given subscriber label
                        
                        .. attribute:: subscriber_label  (key)
                        
                        	Subscriber label
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: template
                        
                        	Subdb template
                        	**type**\:  :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper.SubscriberDatabase.Nodes.Node.Association.Labels.Label.Template>`
                        
                        .. attribute:: interface_name
                        
                        	Interface name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: associations
                        
                        	Association count which reflects number of entries in AssociatedTemplates
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: varlist_id
                        
                        	Varlist Id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-infra-subdb-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SubscriberDatabase.Nodes.Node.Association.Labels.Label, self).__init__()

                            self.yang_name = "label"
                            self.yang_parent_name = "labels"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['subscriber_label']
                            self._child_classes = OrderedDict([("template", ("template", SubscriberDatabase.Nodes.Node.Association.Labels.Label.Template))])
                            self._leafs = OrderedDict([
                                ('subscriber_label', (YLeaf(YType.str, 'subscriber-label'), ['str'])),
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('associations', (YLeaf(YType.uint32, 'associations'), ['int'])),
                                ('varlist_id', (YLeaf(YType.uint32, 'varlist-id'), ['int'])),
                            ])
                            self.subscriber_label = None
                            self.interface_name = None
                            self.associations = None
                            self.varlist_id = None

                            self.template = SubscriberDatabase.Nodes.Node.Association.Labels.Label.Template()
                            self.template.parent = self
                            self._children_name_map["template"] = "template"
                            self._segment_path = lambda: "label" + "[subscriber-label='" + str(self.subscriber_label) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SubscriberDatabase.Nodes.Node.Association.Labels.Label, ['subscriber_label', 'interface_name', 'associations', 'varlist_id'], name, value)


                        class Template(Entity):
                            """
                            Subdb template
                            
                            .. attribute:: associated_template
                            
                            	Associated templates
                            	**type**\: list of  		 :py:class:`AssociatedTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper.SubscriberDatabase.Nodes.Node.Association.Labels.Label.Template.AssociatedTemplate>`
                            
                            

                            """

                            _prefix = 'subscriber-infra-subdb-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SubscriberDatabase.Nodes.Node.Association.Labels.Label.Template, self).__init__()

                                self.yang_name = "template"
                                self.yang_parent_name = "label"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("associated-template", ("associated_template", SubscriberDatabase.Nodes.Node.Association.Labels.Label.Template.AssociatedTemplate))])
                                self._leafs = OrderedDict()

                                self.associated_template = YList(self)
                                self._segment_path = lambda: "template"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SubscriberDatabase.Nodes.Node.Association.Labels.Label.Template, [], name, value)


                            class AssociatedTemplate(Entity):
                                """
                                Associated templates
                                
                                .. attribute:: template_type
                                
                                	Template type
                                	**type**\:  :py:class:`SubdbObjectTypeData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper.SubdbObjectTypeData>`
                                
                                .. attribute:: template_name
                                
                                	Template name
                                	**type**\: str
                                
                                	**length:** 0..65
                                
                                .. attribute:: varlist
                                
                                	Varlist
                                	**type**\: str
                                
                                	**length:** 0..1000
                                
                                

                                """

                                _prefix = 'subscriber-infra-subdb-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(SubscriberDatabase.Nodes.Node.Association.Labels.Label.Template.AssociatedTemplate, self).__init__()

                                    self.yang_name = "associated-template"
                                    self.yang_parent_name = "template"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('template_type', (YLeaf(YType.enumeration, 'template-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper', 'SubdbObjectTypeData', '')])),
                                        ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                                        ('varlist', (YLeaf(YType.str, 'varlist'), ['str'])),
                                    ])
                                    self.template_type = None
                                    self.template_name = None
                                    self.varlist = None
                                    self._segment_path = lambda: "associated-template"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(SubscriberDatabase.Nodes.Node.Association.Labels.Label.Template.AssociatedTemplate, ['template_type', 'template_name', 'varlist'], name, value)


            class Summary(Entity):
                """
                Subscriber data for associated templates
                
                .. attribute:: assoc_db_entries
                
                	Number of Entries in Association DB
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: assoc_db_associations
                
                	Number of Associations in Association DB
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: derived_db_entries
                
                	Number of Entries in Derived DB
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: config_db_entries
                
                	Number of Entries in Configuration DB
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: interface_db_entries
                
                	Number of Entries in Interface DB
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: num_ipsub_dhcp
                
                	Number of IPSUB DHCP subscribers
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: num_ipsub_inband
                
                	Number of IPSUB Inband subscribers
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: num_pppoe
                
                	Number of PPPOE subscribers
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: subdb_obj_counts_by_type
                
                	The count of the various configuration objects by type
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: num_subscribers_in_state
                
                	Number of subscribers in the various states
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: num_transitions_through_state
                
                	Cumulative number of transitions through the various states
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'subscriber-infra-subdb-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SubscriberDatabase.Nodes.Node.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('assoc_db_entries', (YLeaf(YType.uint32, 'assoc-db-entries'), ['int'])),
                        ('assoc_db_associations', (YLeaf(YType.uint32, 'assoc-db-associations'), ['int'])),
                        ('derived_db_entries', (YLeaf(YType.uint32, 'derived-db-entries'), ['int'])),
                        ('config_db_entries', (YLeaf(YType.uint32, 'config-db-entries'), ['int'])),
                        ('interface_db_entries', (YLeaf(YType.uint32, 'interface-db-entries'), ['int'])),
                        ('num_ipsub_dhcp', (YLeaf(YType.uint32, 'num-ipsub-dhcp'), ['int'])),
                        ('num_ipsub_inband', (YLeaf(YType.uint32, 'num-ipsub-inband'), ['int'])),
                        ('num_pppoe', (YLeaf(YType.uint32, 'num-pppoe'), ['int'])),
                        ('subdb_obj_counts_by_type', (YLeafList(YType.uint32, 'subdb-obj-counts-by-type'), ['int'])),
                        ('num_subscribers_in_state', (YLeafList(YType.uint32, 'num-subscribers-in-state'), ['int'])),
                        ('num_transitions_through_state', (YLeafList(YType.uint32, 'num-transitions-through-state'), ['int'])),
                    ])
                    self.assoc_db_entries = None
                    self.assoc_db_associations = None
                    self.derived_db_entries = None
                    self.config_db_entries = None
                    self.interface_db_entries = None
                    self.num_ipsub_dhcp = None
                    self.num_ipsub_inband = None
                    self.num_pppoe = None
                    self.subdb_obj_counts_by_type = []
                    self.num_subscribers_in_state = []
                    self.num_transitions_through_state = []
                    self._segment_path = lambda: "summary"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriberDatabase.Nodes.Node.Summary, [u'assoc_db_entries', u'assoc_db_associations', u'derived_db_entries', u'config_db_entries', u'interface_db_entries', u'num_ipsub_dhcp', u'num_ipsub_inband', u'num_pppoe', u'subdb_obj_counts_by_type', u'num_subscribers_in_state', u'num_transitions_through_state'], name, value)


            class Session(Entity):
                """
                Subscriber management session information
                
                .. attribute:: labels
                
                	Subscriber management list of subscriber labels
                	**type**\:  :py:class:`Labels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper.SubscriberDatabase.Nodes.Node.Session.Labels>`
                
                

                """

                _prefix = 'subscriber-infra-subdb-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SubscriberDatabase.Nodes.Node.Session, self).__init__()

                    self.yang_name = "session"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("labels", ("labels", SubscriberDatabase.Nodes.Node.Session.Labels))])
                    self._leafs = OrderedDict()

                    self.labels = SubscriberDatabase.Nodes.Node.Session.Labels()
                    self.labels.parent = self
                    self._children_name_map["labels"] = "labels"
                    self._segment_path = lambda: "session"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SubscriberDatabase.Nodes.Node.Session, [], name, value)


                class Labels(Entity):
                    """
                    Subscriber management list of subscriber
                    labels
                    
                    .. attribute:: label
                    
                    	Session information for a subscriber label
                    	**type**\: list of  		 :py:class:`Label <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper.SubscriberDatabase.Nodes.Node.Session.Labels.Label>`
                    
                    

                    """

                    _prefix = 'subscriber-infra-subdb-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SubscriberDatabase.Nodes.Node.Session.Labels, self).__init__()

                        self.yang_name = "labels"
                        self.yang_parent_name = "session"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("label", ("label", SubscriberDatabase.Nodes.Node.Session.Labels.Label))])
                        self._leafs = OrderedDict()

                        self.label = YList(self)
                        self._segment_path = lambda: "labels"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SubscriberDatabase.Nodes.Node.Session.Labels, [], name, value)


                    class Label(Entity):
                        """
                        Session information for a subscriber label
                        
                        .. attribute:: subscriber_label  (key)
                        
                        	Subscriber label
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: session_state
                        
                        	Subscriber session state
                        	**type**\:  :py:class:`SessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper.SessionState>`
                        
                        .. attribute:: activate_request_id
                        
                        	Activate request identifier
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: transaction_id
                        
                        	Transaction identifier associated with a particular 'produce\_done' or 'produce\_all\_done' request  default value is 0xffffffff which represents 'None'
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: produce_done_request_id
                        
                        	Produce done request ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: destroy_req_received
                        
                        	Flags indicating if a destroy request is received
                        	**type**\: bool
                        
                        .. attribute:: destroy_request_id
                        
                        	Destroy request ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_config_changed
                        
                        	Is true if configuration change due to template change only and not due to a produce done request
                        	**type**\: bool
                        
                        .. attribute:: is_creator_gone
                        
                        	Is true if the creator of the connection is destroyed
                        	**type**\: bool
                        
                        .. attribute:: is_delete_notify_done
                        
                        	Is true if the deleted features have all been notified and all 'apply done' ack messages have been received
                        	**type**\: bool
                        
                        .. attribute:: add_modify_done
                        
                        	Is true if added/modified features have all been notified and all 'apply done' ack messages have been received
                        	**type**\: bool
                        
                        .. attribute:: is_rollback_needed
                        
                        	Is true if the subscriber should be rolled back to the configuration prior to this transaction when all the outstanding  backend programming interface requests are replied
                        	**type**\: bool
                        
                        .. attribute:: is_rollback_in_progress
                        
                        	Is true if subscriber's configuration is being rolled back
                        	**type**\: bool
                        
                        .. attribute:: is_server_restart_apply
                        
                        	Is true if the subscriber's configuration is being applied due to subscriber database server restart
                        	**type**\: bool
                        
                        .. attribute:: is_rollback_performed
                        
                        	Is true if rollback has previously been performed for this subscriber
                        	**type**\: bool
                        
                        .. attribute:: repl_pending
                        
                        	Flags indicating if there is pending replication
                        	**type**\: bool
                        
                        .. attribute:: activate_timer_running
                        
                        	Flags indicating if activate timer is running
                        	**type**\: bool
                        
                        .. attribute:: apply_timer_running
                        
                        	Flags indicating if apply timer is running
                        	**type**\: bool
                        
                        .. attribute:: event_queue_size
                        
                        	the current size of the event queue
                        	**type**\: bool
                        
                        .. attribute:: restarts
                        
                        	Restart vector to keep track of the restart state
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: template_interface_id
                        
                        	Template Interface Identifier
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'subscriber-infra-subdb-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SubscriberDatabase.Nodes.Node.Session.Labels.Label, self).__init__()

                            self.yang_name = "label"
                            self.yang_parent_name = "labels"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['subscriber_label']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('subscriber_label', (YLeaf(YType.str, 'subscriber-label'), ['str'])),
                                ('session_state', (YLeaf(YType.enumeration, 'session-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Subscriber_infra_subdb_oper', 'SessionState', '')])),
                                ('activate_request_id', (YLeaf(YType.uint32, 'activate-request-id'), ['int'])),
                                ('transaction_id', (YLeaf(YType.int32, 'transaction-id'), ['int'])),
                                ('produce_done_request_id', (YLeaf(YType.uint32, 'produce-done-request-id'), ['int'])),
                                ('destroy_req_received', (YLeaf(YType.boolean, 'destroy-req-received'), ['bool'])),
                                ('destroy_request_id', (YLeaf(YType.uint32, 'destroy-request-id'), ['int'])),
                                ('is_config_changed', (YLeaf(YType.boolean, 'is-config-changed'), ['bool'])),
                                ('is_creator_gone', (YLeaf(YType.boolean, 'is-creator-gone'), ['bool'])),
                                ('is_delete_notify_done', (YLeaf(YType.boolean, 'is-delete-notify-done'), ['bool'])),
                                ('add_modify_done', (YLeaf(YType.boolean, 'add-modify-done'), ['bool'])),
                                ('is_rollback_needed', (YLeaf(YType.boolean, 'is-rollback-needed'), ['bool'])),
                                ('is_rollback_in_progress', (YLeaf(YType.boolean, 'is-rollback-in-progress'), ['bool'])),
                                ('is_server_restart_apply', (YLeaf(YType.boolean, 'is-server-restart-apply'), ['bool'])),
                                ('is_rollback_performed', (YLeaf(YType.boolean, 'is-rollback-performed'), ['bool'])),
                                ('repl_pending', (YLeaf(YType.boolean, 'repl-pending'), ['bool'])),
                                ('activate_timer_running', (YLeaf(YType.boolean, 'activate-timer-running'), ['bool'])),
                                ('apply_timer_running', (YLeaf(YType.boolean, 'apply-timer-running'), ['bool'])),
                                ('event_queue_size', (YLeaf(YType.boolean, 'event-queue-size'), ['bool'])),
                                ('restarts', (YLeaf(YType.str, 'restarts'), ['str'])),
                                ('template_interface_id', (YLeaf(YType.uint32, 'template-interface-id'), ['int'])),
                            ])
                            self.subscriber_label = None
                            self.session_state = None
                            self.activate_request_id = None
                            self.transaction_id = None
                            self.produce_done_request_id = None
                            self.destroy_req_received = None
                            self.destroy_request_id = None
                            self.is_config_changed = None
                            self.is_creator_gone = None
                            self.is_delete_notify_done = None
                            self.add_modify_done = None
                            self.is_rollback_needed = None
                            self.is_rollback_in_progress = None
                            self.is_server_restart_apply = None
                            self.is_rollback_performed = None
                            self.repl_pending = None
                            self.activate_timer_running = None
                            self.apply_timer_running = None
                            self.event_queue_size = None
                            self.restarts = None
                            self.template_interface_id = None
                            self._segment_path = lambda: "label" + "[subscriber-label='" + str(self.subscriber_label) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SubscriberDatabase.Nodes.Node.Session.Labels.Label, ['subscriber_label', 'session_state', 'activate_request_id', 'transaction_id', 'produce_done_request_id', 'destroy_req_received', 'destroy_request_id', 'is_config_changed', 'is_creator_gone', 'is_delete_notify_done', 'add_modify_done', 'is_rollback_needed', 'is_rollback_in_progress', 'is_server_restart_apply', 'is_rollback_performed', 'repl_pending', 'activate_timer_running', 'apply_timer_running', 'event_queue_size', 'restarts', 'template_interface_id'], name, value)

    def clone_ptr(self):
        self._top_entity = SubscriberDatabase()
        return self._top_entity


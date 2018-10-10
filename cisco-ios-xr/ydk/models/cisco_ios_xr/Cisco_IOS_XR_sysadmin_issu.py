""" Cisco_IOS_XR_sysadmin_issu 

This module contains a collection of YANG
definitions for executing and monitoring Cisco IOS\-XR
sysadmin ISSU operations.

Copyright(c) 2016\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IssuNotif(Enum):
    """
    IssuNotif (Enum Class)

    Enumeration of notifications that features can be registered for

    .. data:: notif_sysadmin_op_start = 0

    	A sysadmin ISSU operation is beginning

    .. data:: notif_sysadmin_phase_start = 1

    	A sysadmin ISSU phase is beginning

    .. data:: notif_sysadmin_op_end = 2

    	A sysadmin ISSU operation is ending

    """

    notif_sysadmin_op_start = Enum.YLeaf(0, "notif-sysadmin-op-start")

    notif_sysadmin_phase_start = Enum.YLeaf(1, "notif-sysadmin-phase-start")

    notif_sysadmin_op_end = Enum.YLeaf(2, "notif-sysadmin-op-end")


class OpResult(Enum):
    """
    OpResult (Enum Class)

    Enumeration of errors that can be encountered during an ISSU operation

    .. data:: success = 0

    	Operation succeeded

    .. data:: error_input = 1

    	Part or all of the input was invalid

    .. data:: error_orchestration = 2

    	An internal error occurred during ISSU orchestration

    .. data:: error_install = 3

    	An error occured in the install infrastructure

    .. data:: error_node_redundancy = 4

    	Not all nodes in the system have the required redundancy to allow an ISSU to proceed

    """

    success = Enum.YLeaf(0, "success")

    error_input = Enum.YLeaf(1, "error-input")

    error_orchestration = Enum.YLeaf(2, "error-orchestration")

    error_install = Enum.YLeaf(3, "error-install")

    error_node_redundancy = Enum.YLeaf(4, "error-node-redundancy")


class OpStage(Enum):
    """
    OpStage (Enum Class)

    Enumeration of stages that the ISSU operation can be in

    .. data:: prepare_preamble = 0

    	Prechecks and preprocessing

    .. data:: prepare_host = 1

    	Host package preparation

    .. data:: prepare_sysadmin = 2

    	Sysadmin package preparation

    .. data:: prepare_aborting = 3

    	Aborting after encountering an error

    .. data:: prepare_postamble = 4

    	Operation post-processing

    .. data:: prepare_complete = 5

    	All preparation complete

    .. data:: activate_preamble = 6

    	Pre-checks and pre-processing

    .. data:: activate_sysadmin_phase_one = 7

    	Sysadmin activation on first subset of nodes

    .. data:: activate_sysadmin_phase_two = 8

    	Sysadmin activation on second subset of nodes

    .. data:: activate_host = 9

    	Host activation

    .. data:: activate_aborting = 10

    	Aborting after encountering an error, from which it is not possible to recover

    .. data:: activate_paused = 11

    	Paused after encountering an error from which it is possible to recover

    .. data:: activate_postamble = 12

    	Post-checks and post-processing

    .. data:: activate_complete = 13

    	All activation complete

    """

    prepare_preamble = Enum.YLeaf(0, "prepare-preamble")

    prepare_host = Enum.YLeaf(1, "prepare-host")

    prepare_sysadmin = Enum.YLeaf(2, "prepare-sysadmin")

    prepare_aborting = Enum.YLeaf(3, "prepare-aborting")

    prepare_postamble = Enum.YLeaf(4, "prepare-postamble")

    prepare_complete = Enum.YLeaf(5, "prepare-complete")

    activate_preamble = Enum.YLeaf(6, "activate-preamble")

    activate_sysadmin_phase_one = Enum.YLeaf(7, "activate-sysadmin-phase-one")

    activate_sysadmin_phase_two = Enum.YLeaf(8, "activate-sysadmin-phase-two")

    activate_host = Enum.YLeaf(9, "activate-host")

    activate_aborting = Enum.YLeaf(10, "activate-aborting")

    activate_paused = Enum.YLeaf(11, "activate-paused")

    activate_postamble = Enum.YLeaf(12, "activate-postamble")

    activate_complete = Enum.YLeaf(13, "activate-complete")


class OpStartResult(Enum):
    """
    OpStartResult (Enum Class)

    Enumeration of errors that can be encountered while attempting to begin an ISSU operation

    .. data:: start_success = 0

    	Operation was started successfully

    .. data:: error_operation_in_progress = 1

    	Another ISSU operation is already in progress

    .. data:: activate_error_no_prepare = 2

    	A request to activate the prepared software was made, but there is no successfully prepared software

    .. data:: prepare_error_previous_prepare = 3

    	A request to prepare software was made, but previously prepared software exists

    .. data:: recover_error_unrecoverable = 4

    	The system is in a state that makes in-service recovery impossible

    .. data:: start_error_internal = 5

    	An internal error occured while attempting to start the operation

    """

    start_success = Enum.YLeaf(0, "start-success")

    error_operation_in_progress = Enum.YLeaf(1, "error-operation-in-progress")

    activate_error_no_prepare = Enum.YLeaf(2, "activate-error-no-prepare")

    prepare_error_previous_prepare = Enum.YLeaf(3, "prepare-error-previous-prepare")

    recover_error_unrecoverable = Enum.YLeaf(4, "recover-error-unrecoverable")

    start_error_internal = Enum.YLeaf(5, "start-error-internal")



class Issu(Entity):
    """
    ISSU actions and operational state
    
    .. attribute:: status
    
    	Status of the in\-progress or last completed ISSU operation
    	**type**\:  :py:class:`Status <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Status>`
    
    .. attribute:: clients
    
    	Features registered for notifications of ISSU phases
    	**type**\:  :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Clients>`
    
    .. attribute:: internals
    
    	Internal infrastructure state
    	**type**\:  :py:class:`Internals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals>`
    
    

    """

    _prefix = 'issu'
    _revision = '2018-03-12'

    def __init__(self):
        super(Issu, self).__init__()
        self._top_entity = None

        self.yang_name = "issu"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-issu"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("status", ("status", Issu.Status)), ("clients", ("clients", Issu.Clients)), ("internals", ("internals", Issu.Internals))])
        self._leafs = OrderedDict()

        self.status = Issu.Status()
        self.status.parent = self
        self._children_name_map["status"] = "status"

        self.clients = Issu.Clients()
        self.clients.parent = self
        self._children_name_map["clients"] = "clients"

        self.internals = Issu.Internals()
        self.internals.parent = self
        self._children_name_map["internals"] = "internals"
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Issu, [], name, value)


    class Status(Entity):
        """
        Status of the in\-progress or last completed ISSU operation
        
        .. attribute:: operation_type
        
        	Whether the operation is an activate or deactivate. Both types of operation go through 'prepare' and 'activate' phases.The difference is the end result\: whether the target packages are made to run, or removed from the running software
        	**type**\:  :py:class:`OperationType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Status.OperationType>`
        
        .. attribute:: id
        
        	ID for the current/latest phase of the operation
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: prepare_id
        
        	ID for the prepare phase of the operation
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: activate_id
        
        	ID for the activate or deactivate phase of the operation
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: sysadmin_packages
        
        	Sysadmin packages that are part of the operation
        	**type**\: list of str
        
        .. attribute:: host_packages
        
        	Host OS packages that are part of the operation
        	**type**\: list of str
        
        .. attribute:: complete
        
        	Whether or not the operation has completed
        	**type**\: bool
        
        .. attribute:: result
        
        	Whether the operation succeeded or failed, and the error if any. If in progress, this reflects the current state
        	**type**\:  :py:class:`OpResult <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.OpResult>`
        
        .. attribute:: recover_result
        
        	If a recovery attempt has been completed, an indication of whether the recovery succeeded or failed, and the error if any
        	**type**\:  :py:class:`OpResult <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.OpResult>`
        
        .. attribute:: prepare
        
        	State specific to the prepare phase
        	**type**\:  :py:class:`Prepare <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Status.Prepare>`
        
        .. attribute:: activate
        
        	State specific to the activate phase
        	**type**\:  :py:class:`Activate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Status.Activate>`
        
        .. attribute:: error
        
        	Details of the first error that was encountered, if there were any
        	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Status.Error>`
        
        

        """

        _prefix = 'issu'
        _revision = '2018-03-12'

        def __init__(self):
            super(Issu.Status, self).__init__()

            self.yang_name = "status"
            self.yang_parent_name = "issu"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("prepare", ("prepare", Issu.Status.Prepare)), ("activate", ("activate", Issu.Status.Activate)), ("error", ("error", Issu.Status.Error))])
            self._leafs = OrderedDict([
                ('operation_type', (YLeaf(YType.enumeration, 'operation-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'Issu', 'Status.OperationType')])),
                ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                ('prepare_id', (YLeaf(YType.uint32, 'prepare-id'), ['int'])),
                ('activate_id', (YLeaf(YType.uint32, 'activate-id'), ['int'])),
                ('sysadmin_packages', (YLeafList(YType.str, 'sysadmin-packages'), ['str'])),
                ('host_packages', (YLeafList(YType.str, 'host-packages'), ['str'])),
                ('complete', (YLeaf(YType.boolean, 'complete'), ['bool'])),
                ('result', (YLeaf(YType.enumeration, 'result'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'OpResult', '')])),
                ('recover_result', (YLeaf(YType.enumeration, 'recover-result'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'OpResult', '')])),
            ])
            self.operation_type = None
            self.id = None
            self.prepare_id = None
            self.activate_id = None
            self.sysadmin_packages = []
            self.host_packages = []
            self.complete = None
            self.result = None
            self.recover_result = None

            self.prepare = Issu.Status.Prepare()
            self.prepare.parent = self
            self._children_name_map["prepare"] = "prepare"

            self.activate = Issu.Status.Activate()
            self.activate.parent = self
            self._children_name_map["activate"] = "activate"

            self.error = Issu.Status.Error()
            self.error.parent = self
            self._children_name_map["error"] = "error"
            self._segment_path = lambda: "status"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Issu.Status, ['operation_type', 'id', 'prepare_id', 'activate_id', 'sysadmin_packages', 'host_packages', 'complete', 'result', 'recover_result'], name, value)

        class OperationType(Enum):
            """
            OperationType (Enum Class)

            Whether the operation is an activate or deactivate. Both types of operation go through 'prepare' and 'activate' phases.The difference is the end result\: whether the target packages are made to run, or removed from the running software.

            .. data:: no_operation = 0

            	No ISSU operations have been attempted.

            .. data:: activate_operation = 1

            	Overall operation will add or upgrade packages in the running software

            .. data:: deactivate_operation = 2

            	Overall operation will remove packages from the running software

            """

            no_operation = Enum.YLeaf(0, "no-operation")

            activate_operation = Enum.YLeaf(1, "activate-operation")

            deactivate_operation = Enum.YLeaf(2, "deactivate-operation")



        class Prepare(Entity):
            """
            State specific to the prepare phase
            
            .. attribute:: stage
            
            	Progress of the prepare phase
            	**type**\:  :py:class:`OpStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.OpStage>`
            
            .. attribute:: start_time
            
            	When this ehase was started
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: activity
            
            	A description of the current orchestration activity being executed
            	**type**\: str
            
            .. attribute:: activity_start_time
            
            	When the current activity was started
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            

            """

            _prefix = 'issu'
            _revision = '2018-03-12'

            def __init__(self):
                super(Issu.Status.Prepare, self).__init__()

                self.yang_name = "prepare"
                self.yang_parent_name = "status"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stage', (YLeaf(YType.enumeration, 'stage'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'OpStage', '')])),
                    ('start_time', (YLeaf(YType.str, 'start-time'), ['str'])),
                    ('activity', (YLeaf(YType.str, 'activity'), ['str'])),
                    ('activity_start_time', (YLeaf(YType.str, 'activity-start-time'), ['str'])),
                ])
                self.stage = None
                self.start_time = None
                self.activity = None
                self.activity_start_time = None
                self._segment_path = lambda: "prepare"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/status/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Issu.Status.Prepare, ['stage', 'start_time', 'activity', 'activity_start_time'], name, value)


        class Activate(Entity):
            """
            State specific to the activate phase
            
            .. attribute:: stage
            
            	Progress of the activate phase
            	**type**\:  :py:class:`OpStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.OpStage>`
            
            .. attribute:: start_time
            
            	When this phase was started
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: activity
            
            	A description of the current orchestration activity being executed
            	**type**\: str
            
            .. attribute:: activity_nodes
            
            	Nodes on which the current orchestration activity is being executed
            	**type**\: list of str
            
            .. attribute:: activity_waiting_for
            
            	A description of what needs to happen before the next orchestration activity can be started
            	**type**\: str
            
            .. attribute:: activity_start_time
            
            	When the current activity was started
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            

            """

            _prefix = 'issu'
            _revision = '2018-03-12'

            def __init__(self):
                super(Issu.Status.Activate, self).__init__()

                self.yang_name = "activate"
                self.yang_parent_name = "status"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('stage', (YLeaf(YType.enumeration, 'stage'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'OpStage', '')])),
                    ('start_time', (YLeaf(YType.str, 'start-time'), ['str'])),
                    ('activity', (YLeaf(YType.str, 'activity'), ['str'])),
                    ('activity_nodes', (YLeafList(YType.str, 'activity-nodes'), ['str'])),
                    ('activity_waiting_for', (YLeaf(YType.str, 'activity-waiting-for'), ['str'])),
                    ('activity_start_time', (YLeaf(YType.str, 'activity-start-time'), ['str'])),
                ])
                self.stage = None
                self.start_time = None
                self.activity = None
                self.activity_nodes = []
                self.activity_waiting_for = None
                self.activity_start_time = None
                self._segment_path = lambda: "activate"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/status/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Issu.Status.Activate, ['stage', 'start_time', 'activity', 'activity_nodes', 'activity_waiting_for', 'activity_start_time'], name, value)


        class Error(Entity):
            """
            Details of the first error that was encountered, if there were any.
            
            .. attribute:: result
            
            	If the operation has completed, an indication of whether the operation succeeded or failed, and the error if any
            	**type**\:  :py:class:`OpResult <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.OpResult>`
            
            .. attribute:: stage
            
            	The stage during which the error was encountered
            	**type**\:  :py:class:`OpStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.OpStage>`
            
            .. attribute:: error_message
            
            	Message describing the error
            	**type**\: str
            
            .. attribute:: details
            
            	Details specific to the error. Contents are only filled in if it is relevant to the error that occured
            	**type**\:  :py:class:`Details <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Status.Error.Details>`
            
            

            """

            _prefix = 'issu'
            _revision = '2018-03-12'

            def __init__(self):
                super(Issu.Status.Error, self).__init__()

                self.yang_name = "error"
                self.yang_parent_name = "status"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("details", ("details", Issu.Status.Error.Details))])
                self._leafs = OrderedDict([
                    ('result', (YLeaf(YType.enumeration, 'result'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'OpResult', '')])),
                    ('stage', (YLeaf(YType.enumeration, 'stage'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'OpStage', '')])),
                    ('error_message', (YLeaf(YType.str, 'error-message'), ['str'])),
                ])
                self.result = None
                self.stage = None
                self.error_message = None

                self.details = Issu.Status.Error.Details()
                self.details.parent = self
                self._children_name_map["details"] = "details"
                self._segment_path = lambda: "error"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/status/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Issu.Status.Error, ['result', 'stage', 'error_message'], name, value)


            class Details(Entity):
                """
                Details specific to the error. Contents are only filled in if it is relevant to the error that occured.
                
                .. attribute:: nodes
                
                	A list of the nodes affected by or causing the error
                	**type**\: list of str
                
                .. attribute:: clients
                
                	A list of the registered features affected by or causing the error
                	**type**\: list of str
                
                .. attribute:: packages
                
                	A list of the packages affected by or causing the error
                	**type**\: list of str
                
                .. attribute:: operation_ids
                
                	A list of the operation IDs affected by or causing the error
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'issu'
                _revision = '2018-03-12'

                def __init__(self):
                    super(Issu.Status.Error.Details, self).__init__()

                    self.yang_name = "details"
                    self.yang_parent_name = "error"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('nodes', (YLeafList(YType.str, 'nodes'), ['str'])),
                        ('clients', (YLeafList(YType.str, 'clients'), ['str'])),
                        ('packages', (YLeafList(YType.str, 'packages'), ['str'])),
                        ('operation_ids', (YLeafList(YType.uint32, 'operation-ids'), ['int'])),
                    ])
                    self.nodes = []
                    self.clients = []
                    self.packages = []
                    self.operation_ids = []
                    self._segment_path = lambda: "details"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/status/error/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Issu.Status.Error.Details, ['nodes', 'clients', 'packages', 'operation_ids'], name, value)


    class Clients(Entity):
        """
        Features registered for notifications of ISSU phases
        
        .. attribute:: announcement
        
        	Type of most recent notification sent to clients
        	**type**\:  :py:class:`IssuNotif <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.IssuNotif>`
        
        .. attribute:: announcement_status
        
        	Status of most recent notification sent to clients
        	**type**\:  :py:class:`AnnouncementStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Clients.AnnouncementStatus>`
        
        .. attribute:: client
        
        	
        	**type**\: list of  		 :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Clients.Client>`
        
        

        """

        _prefix = 'issu'
        _revision = '2018-03-12'

        def __init__(self):
            super(Issu.Clients, self).__init__()

            self.yang_name = "clients"
            self.yang_parent_name = "issu"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("client", ("client", Issu.Clients.Client))])
            self._leafs = OrderedDict([
                ('announcement', (YLeaf(YType.enumeration, 'announcement'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'IssuNotif', '')])),
                ('announcement_status', (YLeaf(YType.enumeration, 'announcement-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'Issu', 'Clients.AnnouncementStatus')])),
            ])
            self.announcement = None
            self.announcement_status = None

            self.client = YList(self)
            self._segment_path = lambda: "clients"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Issu.Clients, ['announcement', 'announcement_status'], name, value)

        class AnnouncementStatus(Enum):
            """
            AnnouncementStatus (Enum Class)

            Status of most recent notification sent to clients

            .. data:: announce_no_notif = 0

            	No announcement has yet been sent

            .. data:: announce_in_progress = 1

            	Announcement is in progress, waiting for responses

            .. data:: announce_success = 2

            	The announcement has been acknowledged by all clients, ISSU may continue

            .. data:: announce_veto = 3

            	One or more features vetoed the ISSU operation

            .. data:: announce_disconnect = 4

            	One or more features disconnected during the announcement

            .. data:: announce_timeout = 5

            	One or more features timed out during the announcement

            .. data:: announce_send_error = 6

            	There was an error ending the announcement to one or more features

            .. data:: announce_client_error = 7

            	One or more features has returned an error during the ISSU operation

            """

            announce_no_notif = Enum.YLeaf(0, "announce-no-notif")

            announce_in_progress = Enum.YLeaf(1, "announce-in-progress")

            announce_success = Enum.YLeaf(2, "announce-success")

            announce_veto = Enum.YLeaf(3, "announce-veto")

            announce_disconnect = Enum.YLeaf(4, "announce-disconnect")

            announce_timeout = Enum.YLeaf(5, "announce-timeout")

            announce_send_error = Enum.YLeaf(6, "announce-send-error")

            announce_client_error = Enum.YLeaf(7, "announce-client-error")



        class Client(Entity):
            """
            
            
            .. attribute:: name  (key)
            
            	Name of the registered feature
            	**type**\: str
            
            .. attribute:: location  (key)
            
            	Node on which the feature process is running
            	**type**\: str
            
            .. attribute:: registered_for
            
            	Which notifications the feature is registered to receive
            	**type**\: list of   :py:class:`IssuNotif <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.IssuNotif>`
            
            .. attribute:: notif
            
            	Type of most recent notification
            	**type**\:  :py:class:`IssuNotif <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.IssuNotif>`
            
            .. attribute:: response
            
            	Response from this client to most recent notification sent to the client
            	**type**\:  :py:class:`Response <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Clients.Client.Response>`
            
            .. attribute:: aborted
            
            	Whether the feature has requested that the current operation be aborted
            	**type**\: bool
            
            .. attribute:: abort_reason
            
            	Description of the reason for requesting an abort, if applicable
            	**type**\: str
            
            

            """

            _prefix = 'issu'
            _revision = '2018-03-12'

            def __init__(self):
                super(Issu.Clients.Client, self).__init__()

                self.yang_name = "client"
                self.yang_parent_name = "clients"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name','location']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('location', (YLeaf(YType.str, 'location'), ['str'])),
                    ('registered_for', (YLeafList(YType.enumeration, 'registered-for'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'IssuNotif', '')])),
                    ('notif', (YLeaf(YType.enumeration, 'notif'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'IssuNotif', '')])),
                    ('response', (YLeaf(YType.enumeration, 'response'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'Issu', 'Clients.Client.Response')])),
                    ('aborted', (YLeaf(YType.boolean, 'aborted'), ['bool'])),
                    ('abort_reason', (YLeaf(YType.str, 'abort-reason'), ['str'])),
                ])
                self.name = None
                self.location = None
                self.registered_for = []
                self.notif = None
                self.response = None
                self.aborted = None
                self.abort_reason = None
                self._segment_path = lambda: "client" + "[name='" + str(self.name) + "']" + "[location='" + str(self.location) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/clients/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Issu.Clients.Client, ['name', 'location', 'registered_for', 'notif', 'response', 'aborted', 'abort_reason'], name, value)

            class Response(Enum):
                """
                Response (Enum Class)

                Response from this client to most recent notification sent to the client

                .. data:: notif_resp_no_notif = 0

                	No notification has yet been sent

                .. data:: notif_resp_pending = 1

                	No response has yet been sent

                .. data:: notif_resp_ack = 2

                	The notification has been acknowledged, ISSU may continue

                .. data:: notif_resp_veto = 3

                	The feature has vetoed the ISSU operation

                .. data:: notif_resp_disconnect = 4

                	The feature has disconnected during the notification

                .. data:: notif_resp_timeout = 5

                	The feature has timed out during the ISSU operation

                .. data:: notif_resp_send_error = 6

                	There was an error ending the announcement to the feature

                .. data:: notif_resp_client_error = 7

                	The feature has returned an error during the ISSU operation

                .. data:: notif_resp_client_abort = 8

                	The feature has aborted during the ISSU operation

                """

                notif_resp_no_notif = Enum.YLeaf(0, "notif-resp-no-notif")

                notif_resp_pending = Enum.YLeaf(1, "notif-resp-pending")

                notif_resp_ack = Enum.YLeaf(2, "notif-resp-ack")

                notif_resp_veto = Enum.YLeaf(3, "notif-resp-veto")

                notif_resp_disconnect = Enum.YLeaf(4, "notif-resp-disconnect")

                notif_resp_timeout = Enum.YLeaf(5, "notif-resp-timeout")

                notif_resp_send_error = Enum.YLeaf(6, "notif-resp-send-error")

                notif_resp_client_error = Enum.YLeaf(7, "notif-resp-client-error")

                notif_resp_client_abort = Enum.YLeaf(8, "notif-resp-client-abort")



    class Internals(Entity):
        """
        Internal infrastructure state
        
        .. attribute:: orchestrator
        
        	Orchestrator module internal state
        	**type**\:  :py:class:`Orchestrator <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.Orchestrator>`
        
        .. attribute:: agents
        
        	Agent module internal state
        	**type**\:  :py:class:`Agents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.Agents>`
        
        .. attribute:: inventory_monitor
        
        	Inventory monitor module internal state
        	**type**\:  :py:class:`InventoryMonitor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.InventoryMonitor>`
        
        

        """

        _prefix = 'issu'
        _revision = '2018-03-12'

        def __init__(self):
            super(Issu.Internals, self).__init__()

            self.yang_name = "internals"
            self.yang_parent_name = "issu"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("orchestrator", ("orchestrator", Issu.Internals.Orchestrator)), ("agents", ("agents", Issu.Internals.Agents)), ("inventory-monitor", ("inventory_monitor", Issu.Internals.InventoryMonitor))])
            self._leafs = OrderedDict()

            self.orchestrator = Issu.Internals.Orchestrator()
            self.orchestrator.parent = self
            self._children_name_map["orchestrator"] = "orchestrator"

            self.agents = Issu.Internals.Agents()
            self.agents.parent = self
            self._children_name_map["agents"] = "agents"

            self.inventory_monitor = Issu.Internals.InventoryMonitor()
            self.inventory_monitor.parent = self
            self._children_name_map["inventory_monitor"] = "inventory-monitor"
            self._segment_path = lambda: "internals"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Issu.Internals, [], name, value)

        class OpRequestType(Enum):
            """
            OpRequestType (Enum Class)

            Enumeration of requests that initiate (part of) an ISSU operation

            .. data:: operation_request_prepare = 0

            	Request to execute the prepare phase of an operation

            .. data:: operation_request_activate = 1

            	Request to activate prepared packages

            .. data:: operation_request_deactivate = 2

            	Request to execute both prepare and deactivate phases of an operation

            .. data:: operation_request_recover = 3

            	Recover the system from a failed activate or deactivate operation

            """

            operation_request_prepare = Enum.YLeaf(0, "operation-request-prepare")

            operation_request_activate = Enum.YLeaf(1, "operation-request-activate")

            operation_request_deactivate = Enum.YLeaf(2, "operation-request-deactivate")

            operation_request_recover = Enum.YLeaf(3, "operation-request-recover")


        class PhaseType(Enum):
            """
            PhaseType (Enum Class)

            Calvados activate phase

            .. data:: calvados_activate_phase_one = 0

            	Phase one of the Calvados activate operation

            .. data:: calvados_activate_phase_two = 1

            	Phase two of the Calvados activate operation

            """

            calvados_activate_phase_one = Enum.YLeaf(0, "calvados-activate-phase-one")

            calvados_activate_phase_two = Enum.YLeaf(1, "calvados-activate-phase-two")


        class StageType(Enum):
            """
            StageType (Enum Class)

            Enumeration of possible internal stages in an operation

            .. data:: start = 0

            	Start of operation

            .. data:: end = 1

            	End of operation

            .. data:: prepare_inventory_precheck = 2

            	Inventory precheck

            .. data:: prepare_expand_operation_ids = 3

            	Expand add operation IDs to packages

            .. data:: prepare_get_metadata = 4

            	Retrieve package metadata

            .. data:: prepare_extract_composite = 5

            	Extract constituent packages

            .. data:: prepare_verify_packages = 6

            	Verify package contents

            .. data:: prepare_host = 7

            	The host preparation

            .. data:: prepare_calvados = 8

            	The Calvados preparation

            .. data:: prepare_deactivate_verify_packages = 9

            	Verify package contents for deactivation

            .. data:: prepare_deactivate_calvados = 10

            	The Calvados preparation for deactivation

            .. data:: prepare_abort = 11

            	Abort the prepare operation

            .. data:: prepare_clean = 12

            	Clean-up of prepare operation

            .. data:: activate_preamble = 13

            	Activation preamble

            .. data:: deactivate_preamble = 14

            	Deactivation preamble

            .. data:: activate_calvados_preamble = 15

            	Calvados-specific activation preamble

            .. data:: activate_calvados_phase = 16

            	Activate the Calvados software

            .. data:: activate_calvados_phase_reload = 17

            	Reload Calvados VMs

            .. data:: activate_calvados_phase_postamble = 18

            	Post VM restart checks for Calvados

            .. data:: activate_calvados_postamble = 19

            	Post Calvados activation handling

            .. data:: activate_host = 20

            	Execute host ISSU

            .. data:: activate_postamble = 21

            	Post-processing for the activate operation

            .. data:: deactivate_calvados = 22

            	Deactivate the Calvados software

            .. data:: activate_abort_no_recovery = 23

            	Abort the activate operation, no recovery is necessary

            .. data:: activate_abort_unrecoverable = 24

            	Abort the activate operation, no recovery is possible

            .. data:: activate_error_pause = 25

            	Pause following an error

            .. data:: activate_calvados_recovery = 26

            	Rollback to committed Calvados

            .. data:: activate_recovery_postamble = 27

            	Post rollback to committed Calvados

            """

            start = Enum.YLeaf(0, "start")

            end = Enum.YLeaf(1, "end")

            prepare_inventory_precheck = Enum.YLeaf(2, "prepare-inventory-precheck")

            prepare_expand_operation_ids = Enum.YLeaf(3, "prepare-expand-operation-ids")

            prepare_get_metadata = Enum.YLeaf(4, "prepare-get-metadata")

            prepare_extract_composite = Enum.YLeaf(5, "prepare-extract-composite")

            prepare_verify_packages = Enum.YLeaf(6, "prepare-verify-packages")

            prepare_host = Enum.YLeaf(7, "prepare-host")

            prepare_calvados = Enum.YLeaf(8, "prepare-calvados")

            prepare_deactivate_verify_packages = Enum.YLeaf(9, "prepare-deactivate-verify-packages")

            prepare_deactivate_calvados = Enum.YLeaf(10, "prepare-deactivate-calvados")

            prepare_abort = Enum.YLeaf(11, "prepare-abort")

            prepare_clean = Enum.YLeaf(12, "prepare-clean")

            activate_preamble = Enum.YLeaf(13, "activate-preamble")

            deactivate_preamble = Enum.YLeaf(14, "deactivate-preamble")

            activate_calvados_preamble = Enum.YLeaf(15, "activate-calvados-preamble")

            activate_calvados_phase = Enum.YLeaf(16, "activate-calvados-phase")

            activate_calvados_phase_reload = Enum.YLeaf(17, "activate-calvados-phase-reload")

            activate_calvados_phase_postamble = Enum.YLeaf(18, "activate-calvados-phase-postamble")

            activate_calvados_postamble = Enum.YLeaf(19, "activate-calvados-postamble")

            activate_host = Enum.YLeaf(20, "activate-host")

            activate_postamble = Enum.YLeaf(21, "activate-postamble")

            deactivate_calvados = Enum.YLeaf(22, "deactivate-calvados")

            activate_abort_no_recovery = Enum.YLeaf(23, "activate-abort-no-recovery")

            activate_abort_unrecoverable = Enum.YLeaf(24, "activate-abort-unrecoverable")

            activate_error_pause = Enum.YLeaf(25, "activate-error-pause")

            activate_calvados_recovery = Enum.YLeaf(26, "activate-calvados-recovery")

            activate_recovery_postamble = Enum.YLeaf(27, "activate-recovery-postamble")



        class Orchestrator(Entity):
            """
            Orchestrator module internal state
            
            .. attribute:: command
            
            	Command issued
            	**type**\:  :py:class:`OpRequestType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.OpRequestType>`
            
            .. attribute:: operation_type
            
            	Type of operation\: activate or deactivate
            	**type**\:  :py:class:`OpRequestType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.OpRequestType>`
            
            .. attribute:: current_operation
            
            	Operation being performed
            	**type**\:  :py:class:`OpRequestType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.OpRequestType>`
            
            .. attribute:: issu_completed
            
            	True if the overall ISSU operation has been completed, false otherwise
            	**type**\: bool
            
            .. attribute:: operation_id
            
            	The ID for the operation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: in_progress
            
            	True if an operation is in progress
            	**type**\: bool
            
            .. attribute:: operation_start_details
            
            	
            	**type**\:  :py:class:`OperationStartDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.Orchestrator.OperationStartDetails>`
            
            .. attribute:: internal_prepare
            
            	
            	**type**\:  :py:class:`InternalPrepare <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.Orchestrator.InternalPrepare>`
            
            .. attribute:: internal_activate
            
            	
            	**type**\:  :py:class:`InternalActivate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.Orchestrator.InternalActivate>`
            
            .. attribute:: error
            
            	
            	**type**\:  :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.Orchestrator.Error>`
            
            

            """

            _prefix = 'issu'
            _revision = '2018-03-12'

            def __init__(self):
                super(Issu.Internals.Orchestrator, self).__init__()

                self.yang_name = "orchestrator"
                self.yang_parent_name = "internals"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("operation-start-details", ("operation_start_details", Issu.Internals.Orchestrator.OperationStartDetails)), ("internal-prepare", ("internal_prepare", Issu.Internals.Orchestrator.InternalPrepare)), ("internal-activate", ("internal_activate", Issu.Internals.Orchestrator.InternalActivate)), ("error", ("error", Issu.Internals.Orchestrator.Error))])
                self._leafs = OrderedDict([
                    ('command', (YLeaf(YType.enumeration, 'command'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'Issu', 'Internals.OpRequestType')])),
                    ('operation_type', (YLeaf(YType.enumeration, 'operation-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'Issu', 'Internals.OpRequestType')])),
                    ('current_operation', (YLeaf(YType.enumeration, 'current-operation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'Issu', 'Internals.OpRequestType')])),
                    ('issu_completed', (YLeaf(YType.boolean, 'issu-completed'), ['bool'])),
                    ('operation_id', (YLeaf(YType.uint32, 'operation-id'), ['int'])),
                    ('in_progress', (YLeaf(YType.boolean, 'in-progress'), ['bool'])),
                ])
                self.command = None
                self.operation_type = None
                self.current_operation = None
                self.issu_completed = None
                self.operation_id = None
                self.in_progress = None

                self.operation_start_details = Issu.Internals.Orchestrator.OperationStartDetails()
                self.operation_start_details.parent = self
                self._children_name_map["operation_start_details"] = "operation-start-details"

                self.internal_prepare = Issu.Internals.Orchestrator.InternalPrepare()
                self.internal_prepare.parent = self
                self._children_name_map["internal_prepare"] = "internal-prepare"

                self.internal_activate = Issu.Internals.Orchestrator.InternalActivate()
                self.internal_activate.parent = self
                self._children_name_map["internal_activate"] = "internal-activate"

                self.error = Issu.Internals.Orchestrator.Error()
                self.error.parent = self
                self._children_name_map["error"] = "error"
                self._segment_path = lambda: "orchestrator"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/internals/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Issu.Internals.Orchestrator, ['command', 'operation_type', 'current_operation', 'issu_completed', 'operation_id', 'in_progress'], name, value)


            class OperationStartDetails(Entity):
                """
                
                
                .. attribute:: input_package
                
                	Packages used to initiate the operation
                	**type**\: list of str
                
                .. attribute:: input_operation_id
                
                	Operation IDs used to initiate operation
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'issu'
                _revision = '2018-03-12'

                def __init__(self):
                    super(Issu.Internals.Orchestrator.OperationStartDetails, self).__init__()

                    self.yang_name = "operation-start-details"
                    self.yang_parent_name = "orchestrator"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('input_package', (YLeafList(YType.str, 'input-package'), ['str'])),
                        ('input_operation_id', (YLeafList(YType.uint32, 'input-operation-id'), ['int'])),
                    ])
                    self.input_package = []
                    self.input_operation_id = []
                    self._segment_path = lambda: "operation-start-details"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/internals/orchestrator/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Issu.Internals.Orchestrator.OperationStartDetails, ['input_package', 'input_operation_id'], name, value)


            class InternalPrepare(Entity):
                """
                
                
                .. attribute:: operation_id
                
                	ID of prepare operation
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: complete
                
                	True if prepare phase complete
                	**type**\: bool
                
                .. attribute:: current_stage
                
                	Current stage of prepare operation, if a stage is in progress
                	**type**\:  :py:class:`StageType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.StageType>`
                
                .. attribute:: host_package
                
                	Host packages to be used in the ISSU
                	**type**\: list of str
                
                .. attribute:: calvados_package
                
                	Calvados packages to be used in the ISSU
                	**type**\: list of str
                
                .. attribute:: prepare_stage_history
                
                	
                	**type**\:  :py:class:`PrepareStageHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.Orchestrator.InternalPrepare.PrepareStageHistory>`
                
                

                """

                _prefix = 'issu'
                _revision = '2018-03-12'

                def __init__(self):
                    super(Issu.Internals.Orchestrator.InternalPrepare, self).__init__()

                    self.yang_name = "internal-prepare"
                    self.yang_parent_name = "orchestrator"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("prepare-stage-history", ("prepare_stage_history", Issu.Internals.Orchestrator.InternalPrepare.PrepareStageHistory))])
                    self._leafs = OrderedDict([
                        ('operation_id', (YLeaf(YType.uint32, 'operation-id'), ['int'])),
                        ('complete', (YLeaf(YType.boolean, 'complete'), ['bool'])),
                        ('current_stage', (YLeaf(YType.enumeration, 'current-stage'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'Issu', 'Internals.StageType')])),
                        ('host_package', (YLeafList(YType.str, 'host-package'), ['str'])),
                        ('calvados_package', (YLeafList(YType.str, 'calvados-package'), ['str'])),
                    ])
                    self.operation_id = None
                    self.complete = None
                    self.current_stage = None
                    self.host_package = []
                    self.calvados_package = []

                    self.prepare_stage_history = Issu.Internals.Orchestrator.InternalPrepare.PrepareStageHistory()
                    self.prepare_stage_history.parent = self
                    self._children_name_map["prepare_stage_history"] = "prepare-stage-history"
                    self._segment_path = lambda: "internal-prepare"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/internals/orchestrator/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Issu.Internals.Orchestrator.InternalPrepare, ['operation_id', 'complete', 'current_stage', 'host_package', 'calvados_package'], name, value)


                class PrepareStageHistory(Entity):
                    """
                    
                    
                    .. attribute:: historical_stage
                    
                    	
                    	**type**\: list of  		 :py:class:`HistoricalStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.Orchestrator.InternalPrepare.PrepareStageHistory.HistoricalStage>`
                    
                    

                    """

                    _prefix = 'issu'
                    _revision = '2018-03-12'

                    def __init__(self):
                        super(Issu.Internals.Orchestrator.InternalPrepare.PrepareStageHistory, self).__init__()

                        self.yang_name = "prepare-stage-history"
                        self.yang_parent_name = "internal-prepare"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("historical-stage", ("historical_stage", Issu.Internals.Orchestrator.InternalPrepare.PrepareStageHistory.HistoricalStage))])
                        self._leafs = OrderedDict()

                        self.historical_stage = YList(self)
                        self._segment_path = lambda: "prepare-stage-history"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/internals/orchestrator/internal-prepare/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Issu.Internals.Orchestrator.InternalPrepare.PrepareStageHistory, [], name, value)


                    class HistoricalStage(Entity):
                        """
                        
                        
                        .. attribute:: stage_index  (key)
                        
                        	Integer stage index
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: external_stage
                        
                        	External stage of operation
                        	**type**\:  :py:class:`OpStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.OpStage>`
                        
                        .. attribute:: internal_stage_details
                        
                        	Details of the internal stage
                        	**type**\: str
                        
                        .. attribute:: status
                        
                        	Status of the stage
                        	**type**\: str
                        
                        .. attribute:: error_details
                        
                        	Further error details
                        	**type**\: str
                        
                        .. attribute:: start_time
                        
                        	Start time of stage
                        	**type**\: str
                        
                        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                        
                        .. attribute:: end_time
                        
                        	End time of stage
                        	**type**\: str
                        
                        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                        
                        .. attribute:: complete
                        
                        	Is the stage complete?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'issu'
                        _revision = '2018-03-12'

                        def __init__(self):
                            super(Issu.Internals.Orchestrator.InternalPrepare.PrepareStageHistory.HistoricalStage, self).__init__()

                            self.yang_name = "historical-stage"
                            self.yang_parent_name = "prepare-stage-history"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['stage_index']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('stage_index', (YLeaf(YType.uint32, 'stage-index'), ['int'])),
                                ('external_stage', (YLeaf(YType.enumeration, 'external-stage'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'OpStage', '')])),
                                ('internal_stage_details', (YLeaf(YType.str, 'internal-stage-details'), ['str'])),
                                ('status', (YLeaf(YType.str, 'status'), ['str'])),
                                ('error_details', (YLeaf(YType.str, 'error-details'), ['str'])),
                                ('start_time', (YLeaf(YType.str, 'start-time'), ['str'])),
                                ('end_time', (YLeaf(YType.str, 'end-time'), ['str'])),
                                ('complete', (YLeaf(YType.boolean, 'complete'), ['bool'])),
                            ])
                            self.stage_index = None
                            self.external_stage = None
                            self.internal_stage_details = None
                            self.status = None
                            self.error_details = None
                            self.start_time = None
                            self.end_time = None
                            self.complete = None
                            self._segment_path = lambda: "historical-stage" + "[stage-index='" + str(self.stage_index) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/internals/orchestrator/internal-prepare/prepare-stage-history/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Issu.Internals.Orchestrator.InternalPrepare.PrepareStageHistory.HistoricalStage, ['stage_index', 'external_stage', 'internal_stage_details', 'status', 'error_details', 'start_time', 'end_time', 'complete'], name, value)


            class InternalActivate(Entity):
                """
                
                
                .. attribute:: operation_id
                
                	ID of prepare operation
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: complete
                
                	True if activate phase complete
                	**type**\: bool
                
                .. attribute:: current_stage
                
                	Current stage of activate operation, if a stage is in progress
                	**type**\:  :py:class:`StageType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.StageType>`
                
                .. attribute:: current_phase
                
                	Current phase of activate operation, if phase is relevant
                	**type**\:  :py:class:`PhaseType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.PhaseType>`
                
                .. attribute:: host_prepared
                
                	Indicates whether any host packages have been prepared
                	**type**\: bool
                
                .. attribute:: calvados_prepared
                
                	Indicates whether any Calvados packages have been prepared
                	**type**\: bool
                
                .. attribute:: host_node
                
                	Nodes participating in host ISSU
                	**type**\: list of str
                
                .. attribute:: calvados_phase_one_node
                
                	Nodes participating in phase one of Calvados ISSU
                	**type**\: list of str
                
                .. attribute:: calvados_phase_two_node
                
                	Nodes participating in phase two of Calvados ISSU
                	**type**\: list of str
                
                .. attribute:: activate_stage_history
                
                	
                	**type**\:  :py:class:`ActivateStageHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.Orchestrator.InternalActivate.ActivateStageHistory>`
                
                

                """

                _prefix = 'issu'
                _revision = '2018-03-12'

                def __init__(self):
                    super(Issu.Internals.Orchestrator.InternalActivate, self).__init__()

                    self.yang_name = "internal-activate"
                    self.yang_parent_name = "orchestrator"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("activate-stage-history", ("activate_stage_history", Issu.Internals.Orchestrator.InternalActivate.ActivateStageHistory))])
                    self._leafs = OrderedDict([
                        ('operation_id', (YLeaf(YType.uint32, 'operation-id'), ['int'])),
                        ('complete', (YLeaf(YType.boolean, 'complete'), ['bool'])),
                        ('current_stage', (YLeaf(YType.enumeration, 'current-stage'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'Issu', 'Internals.StageType')])),
                        ('current_phase', (YLeaf(YType.enumeration, 'current-phase'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'Issu', 'Internals.PhaseType')])),
                        ('host_prepared', (YLeaf(YType.boolean, 'host-prepared'), ['bool'])),
                        ('calvados_prepared', (YLeaf(YType.boolean, 'calvados-prepared'), ['bool'])),
                        ('host_node', (YLeafList(YType.str, 'host-node'), ['str'])),
                        ('calvados_phase_one_node', (YLeafList(YType.str, 'calvados-phase-one-node'), ['str'])),
                        ('calvados_phase_two_node', (YLeafList(YType.str, 'calvados-phase-two-node'), ['str'])),
                    ])
                    self.operation_id = None
                    self.complete = None
                    self.current_stage = None
                    self.current_phase = None
                    self.host_prepared = None
                    self.calvados_prepared = None
                    self.host_node = []
                    self.calvados_phase_one_node = []
                    self.calvados_phase_two_node = []

                    self.activate_stage_history = Issu.Internals.Orchestrator.InternalActivate.ActivateStageHistory()
                    self.activate_stage_history.parent = self
                    self._children_name_map["activate_stage_history"] = "activate-stage-history"
                    self._segment_path = lambda: "internal-activate"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/internals/orchestrator/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Issu.Internals.Orchestrator.InternalActivate, ['operation_id', 'complete', 'current_stage', 'current_phase', 'host_prepared', 'calvados_prepared', 'host_node', 'calvados_phase_one_node', 'calvados_phase_two_node'], name, value)


                class ActivateStageHistory(Entity):
                    """
                    
                    
                    .. attribute:: historical_stage
                    
                    	
                    	**type**\: list of  		 :py:class:`HistoricalStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.Orchestrator.InternalActivate.ActivateStageHistory.HistoricalStage>`
                    
                    

                    """

                    _prefix = 'issu'
                    _revision = '2018-03-12'

                    def __init__(self):
                        super(Issu.Internals.Orchestrator.InternalActivate.ActivateStageHistory, self).__init__()

                        self.yang_name = "activate-stage-history"
                        self.yang_parent_name = "internal-activate"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("historical-stage", ("historical_stage", Issu.Internals.Orchestrator.InternalActivate.ActivateStageHistory.HistoricalStage))])
                        self._leafs = OrderedDict()

                        self.historical_stage = YList(self)
                        self._segment_path = lambda: "activate-stage-history"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/internals/orchestrator/internal-activate/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Issu.Internals.Orchestrator.InternalActivate.ActivateStageHistory, [], name, value)


                    class HistoricalStage(Entity):
                        """
                        
                        
                        .. attribute:: stage_index  (key)
                        
                        	Integer stage index
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: external_stage
                        
                        	External stage of operation
                        	**type**\:  :py:class:`OpStage <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.OpStage>`
                        
                        .. attribute:: internal_stage_details
                        
                        	Details of the internal stage
                        	**type**\: str
                        
                        .. attribute:: status
                        
                        	Status of the stage
                        	**type**\: str
                        
                        .. attribute:: error_details
                        
                        	Further error details
                        	**type**\: str
                        
                        .. attribute:: start_time
                        
                        	Start time of stage
                        	**type**\: str
                        
                        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                        
                        .. attribute:: end_time
                        
                        	End time of stage
                        	**type**\: str
                        
                        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                        
                        .. attribute:: complete
                        
                        	Is the stage complete?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'issu'
                        _revision = '2018-03-12'

                        def __init__(self):
                            super(Issu.Internals.Orchestrator.InternalActivate.ActivateStageHistory.HistoricalStage, self).__init__()

                            self.yang_name = "historical-stage"
                            self.yang_parent_name = "activate-stage-history"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['stage_index']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('stage_index', (YLeaf(YType.uint32, 'stage-index'), ['int'])),
                                ('external_stage', (YLeaf(YType.enumeration, 'external-stage'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'OpStage', '')])),
                                ('internal_stage_details', (YLeaf(YType.str, 'internal-stage-details'), ['str'])),
                                ('status', (YLeaf(YType.str, 'status'), ['str'])),
                                ('error_details', (YLeaf(YType.str, 'error-details'), ['str'])),
                                ('start_time', (YLeaf(YType.str, 'start-time'), ['str'])),
                                ('end_time', (YLeaf(YType.str, 'end-time'), ['str'])),
                                ('complete', (YLeaf(YType.boolean, 'complete'), ['bool'])),
                            ])
                            self.stage_index = None
                            self.external_stage = None
                            self.internal_stage_details = None
                            self.status = None
                            self.error_details = None
                            self.start_time = None
                            self.end_time = None
                            self.complete = None
                            self._segment_path = lambda: "historical-stage" + "[stage-index='" + str(self.stage_index) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/internals/orchestrator/internal-activate/activate-stage-history/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Issu.Internals.Orchestrator.InternalActivate.ActivateStageHistory.HistoricalStage, ['stage_index', 'external_stage', 'internal_stage_details', 'status', 'error_details', 'start_time', 'end_time', 'complete'], name, value)


            class Error(Entity):
                """
                
                
                .. attribute:: operation_status
                
                	Overall status of the operation
                	**type**\: str
                
                .. attribute:: failure_operation
                
                	Operation in progress when first error was encountered
                	**type**\:  :py:class:`OpRequestType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.OpRequestType>`
                
                .. attribute:: failure_external_stage
                
                	Stage being undertaken when first failure was encountered
                	**type**\:  :py:class:`StageType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.StageType>`
                
                .. attribute:: failure_internal_stage_details
                
                	Description of the internal state when first error encountered
                	**type**\: str
                
                .. attribute:: error_details
                
                	String describing error encountered
                	**type**\: str
                
                .. attribute:: failed_node
                
                	Nodes on which a failure occurred
                	**type**\: list of str
                
                .. attribute:: failed_package
                
                	Packages which caused a failure
                	**type**\: list of str
                
                .. attribute:: failed_operation_id
                
                	Operation IDs which caused a failure
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                .. attribute:: failed_client
                
                	Registered features which caused a failure
                	**type**\: list of str
                
                .. attribute:: recovery_attempted
                
                	True if a recovery has been attempted or is currently in progress
                	**type**\: bool
                
                .. attribute:: recovery_status
                
                	Status of the recovery operation
                	**type**\: str
                
                

                """

                _prefix = 'issu'
                _revision = '2018-03-12'

                def __init__(self):
                    super(Issu.Internals.Orchestrator.Error, self).__init__()

                    self.yang_name = "error"
                    self.yang_parent_name = "orchestrator"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('operation_status', (YLeaf(YType.str, 'operation-status'), ['str'])),
                        ('failure_operation', (YLeaf(YType.enumeration, 'failure-operation'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'Issu', 'Internals.OpRequestType')])),
                        ('failure_external_stage', (YLeaf(YType.enumeration, 'failure-external-stage'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'Issu', 'Internals.StageType')])),
                        ('failure_internal_stage_details', (YLeaf(YType.str, 'failure-internal-stage-details'), ['str'])),
                        ('error_details', (YLeaf(YType.str, 'error-details'), ['str'])),
                        ('failed_node', (YLeafList(YType.str, 'failed-node'), ['str'])),
                        ('failed_package', (YLeafList(YType.str, 'failed-package'), ['str'])),
                        ('failed_operation_id', (YLeafList(YType.uint32, 'failed-operation-id'), ['int'])),
                        ('failed_client', (YLeafList(YType.str, 'failed-client'), ['str'])),
                        ('recovery_attempted', (YLeaf(YType.boolean, 'recovery-attempted'), ['bool'])),
                        ('recovery_status', (YLeaf(YType.str, 'recovery-status'), ['str'])),
                    ])
                    self.operation_status = None
                    self.failure_operation = None
                    self.failure_external_stage = None
                    self.failure_internal_stage_details = None
                    self.error_details = None
                    self.failed_node = []
                    self.failed_package = []
                    self.failed_operation_id = []
                    self.failed_client = []
                    self.recovery_attempted = None
                    self.recovery_status = None
                    self._segment_path = lambda: "error"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/internals/orchestrator/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Issu.Internals.Orchestrator.Error, ['operation_status', 'failure_operation', 'failure_external_stage', 'failure_internal_stage_details', 'error_details', 'failed_node', 'failed_package', 'failed_operation_id', 'failed_client', 'recovery_attempted', 'recovery_status'], name, value)


        class Agents(Entity):
            """
            Agent module internal state
            
            .. attribute:: requests
            
            	Data on requests being processed by Agent module
            	**type**\:  :py:class:`Requests <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.Agents.Requests>`
            
            .. attribute:: inventory
            
            	Inventory of agents held by Agent module
            	**type**\:  :py:class:`Inventory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.Agents.Inventory>`
            
            .. attribute:: reload_tracking
            
            	Reload tracking performed by Agent module
            	**type**\:  :py:class:`ReloadTracking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.Agents.ReloadTracking>`
            
            

            """

            _prefix = 'issu'
            _revision = '2018-03-12'

            def __init__(self):
                super(Issu.Internals.Agents, self).__init__()

                self.yang_name = "agents"
                self.yang_parent_name = "internals"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("requests", ("requests", Issu.Internals.Agents.Requests)), ("inventory", ("inventory", Issu.Internals.Agents.Inventory)), ("reload-tracking", ("reload_tracking", Issu.Internals.Agents.ReloadTracking))])
                self._leafs = OrderedDict()

                self.requests = Issu.Internals.Agents.Requests()
                self.requests.parent = self
                self._children_name_map["requests"] = "requests"

                self.inventory = Issu.Internals.Agents.Inventory()
                self.inventory.parent = self
                self._children_name_map["inventory"] = "inventory"

                self.reload_tracking = Issu.Internals.Agents.ReloadTracking()
                self.reload_tracking.parent = self
                self._children_name_map["reload_tracking"] = "reload-tracking"
                self._segment_path = lambda: "agents"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/internals/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Issu.Internals.Agents, [], name, value)


            class Requests(Entity):
                """
                Data on requests being processed by Agent module
                
                .. attribute:: request
                
                	
                	**type**\: list of  		 :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.Agents.Requests.Request>`
                
                

                """

                _prefix = 'issu'
                _revision = '2018-03-12'

                def __init__(self):
                    super(Issu.Internals.Agents.Requests, self).__init__()

                    self.yang_name = "requests"
                    self.yang_parent_name = "agents"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("request", ("request", Issu.Internals.Agents.Requests.Request))])
                    self._leafs = OrderedDict()

                    self.request = YList(self)
                    self._segment_path = lambda: "requests"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/internals/agents/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Issu.Internals.Agents.Requests, [], name, value)


                class Request(Entity):
                    """
                    
                    
                    .. attribute:: request_index  (key)
                    
                    	Integer request index
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: request_type
                    
                    	Type of request
                    	**type**\:  :py:class:`RequestType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.Agents.Requests.Request.RequestType>`
                    
                    .. attribute:: checkpoint
                    
                    	
                    	**type**\:  :py:class:`Checkpoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.Agents.Requests.Request.Checkpoint>`
                    
                    .. attribute:: requests_sent
                    
                    	Number of requests sent. Equal to number of expected responses
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: responses_received
                    
                    	Number of responses received from agents
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: agents
                    
                    	
                    	**type**\:  :py:class:`Agents_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.Agents.Requests.Request.Agents_>`
                    
                    

                    """

                    _prefix = 'issu'
                    _revision = '2018-03-12'

                    def __init__(self):
                        super(Issu.Internals.Agents.Requests.Request, self).__init__()

                        self.yang_name = "request"
                        self.yang_parent_name = "requests"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['request_index']
                        self._child_classes = OrderedDict([("checkpoint", ("checkpoint", Issu.Internals.Agents.Requests.Request.Checkpoint)), ("agents", ("agents", Issu.Internals.Agents.Requests.Request.Agents_))])
                        self._leafs = OrderedDict([
                            ('request_index', (YLeaf(YType.uint32, 'request-index'), ['int'])),
                            ('request_type', (YLeaf(YType.enumeration, 'request-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'Issu', 'Internals.Agents.Requests.Request.RequestType')])),
                            ('requests_sent', (YLeaf(YType.uint32, 'requests-sent'), ['int'])),
                            ('responses_received', (YLeaf(YType.uint32, 'responses-received'), ['int'])),
                        ])
                        self.request_index = None
                        self.request_type = None
                        self.requests_sent = None
                        self.responses_received = None

                        self.checkpoint = Issu.Internals.Agents.Requests.Request.Checkpoint()
                        self.checkpoint.parent = self
                        self._children_name_map["checkpoint"] = "checkpoint"

                        self.agents = Issu.Internals.Agents.Requests.Request.Agents_()
                        self.agents.parent = self
                        self._children_name_map["agents"] = "agents"
                        self._segment_path = lambda: "request" + "[request-index='" + str(self.request_index) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/internals/agents/requests/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Issu.Internals.Agents.Requests.Request, ['request_index', 'request_type', 'requests_sent', 'responses_received'], name, value)

                    class RequestType(Enum):
                        """
                        RequestType (Enum Class)

                        Type of request

                        .. data:: requests_node_ready = 0

                        	Node ready request

                        .. data:: requests_checkpoint = 1

                        	Checkpoint request

                        .. data:: requests_post_upgrade_cleanup = 2

                        	Post-upgrade cleanup request

                        """

                        requests_node_ready = Enum.YLeaf(0, "requests-node-ready")

                        requests_checkpoint = Enum.YLeaf(1, "requests-checkpoint")

                        requests_post_upgrade_cleanup = Enum.YLeaf(2, "requests-post-upgrade-cleanup")



                    class Checkpoint(Entity):
                        """
                        
                        
                        .. attribute:: message_type
                        
                        	Checkpoint request type
                        	**type**\:  :py:class:`MessageType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.Agents.Requests.Request.Checkpoint.MessageType>`
                        
                        .. attribute:: data_length
                        
                        	Length of checkpoint data. 0 for start/end requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: filename
                        
                        	Filename of associated checkpoint file
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'issu'
                        _revision = '2018-03-12'

                        def __init__(self):
                            super(Issu.Internals.Agents.Requests.Request.Checkpoint, self).__init__()

                            self.yang_name = "checkpoint"
                            self.yang_parent_name = "request"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('message_type', (YLeaf(YType.enumeration, 'message-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'Issu', 'Internals.Agents.Requests.Request.Checkpoint.MessageType')])),
                                ('data_length', (YLeaf(YType.uint32, 'data-length'), ['int'])),
                                ('filename', (YLeaf(YType.str, 'filename'), ['str'])),
                            ])
                            self.message_type = None
                            self.data_length = None
                            self.filename = None
                            self._segment_path = lambda: "checkpoint"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Issu.Internals.Agents.Requests.Request.Checkpoint, ['message_type', 'data_length', 'filename'], name, value)

                        class MessageType(Enum):
                            """
                            MessageType (Enum Class)

                            Checkpoint request type

                            .. data:: requests_checkpoint_start = 0

                            	Start request

                            .. data:: requests_checkpoint_end = 1

                            	End request

                            .. data:: requests_checkpoint_update = 2

                            	Update request

                            """

                            requests_checkpoint_start = Enum.YLeaf(0, "requests-checkpoint-start")

                            requests_checkpoint_end = Enum.YLeaf(1, "requests-checkpoint-end")

                            requests_checkpoint_update = Enum.YLeaf(2, "requests-checkpoint-update")



                    class Agents_(Entity):
                        """
                        
                        
                        .. attribute:: agent
                        
                        	
                        	**type**\: list of  		 :py:class:`Agent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.Agents.Requests.Request.Agents_.Agent>`
                        
                        

                        """

                        _prefix = 'issu'
                        _revision = '2018-03-12'

                        def __init__(self):
                            super(Issu.Internals.Agents.Requests.Request.Agents_, self).__init__()

                            self.yang_name = "agents"
                            self.yang_parent_name = "request"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("agent", ("agent", Issu.Internals.Agents.Requests.Request.Agents_.Agent))])
                            self._leafs = OrderedDict()

                            self.agent = YList(self)
                            self._segment_path = lambda: "agents"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Issu.Internals.Agents.Requests.Request.Agents_, [], name, value)


                        class Agent(Entity):
                            """
                            
                            
                            .. attribute:: agent_index  (key)
                            
                            	Integer agent index
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: node
                            
                            	Node ID
                            	**type**\: str
                            
                            .. attribute:: waiting_for_response
                            
                            	Indicates whether this agent has responded
                            	**type**\: bool
                            
                            .. attribute:: response_contents
                            
                            	
                            	**type**\:  :py:class:`ResponseContents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.Agents.Requests.Request.Agents_.Agent.ResponseContents>`
                            
                            

                            """

                            _prefix = 'issu'
                            _revision = '2018-03-12'

                            def __init__(self):
                                super(Issu.Internals.Agents.Requests.Request.Agents_.Agent, self).__init__()

                                self.yang_name = "agent"
                                self.yang_parent_name = "agents"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['agent_index']
                                self._child_classes = OrderedDict([("response-contents", ("response_contents", Issu.Internals.Agents.Requests.Request.Agents_.Agent.ResponseContents))])
                                self._leafs = OrderedDict([
                                    ('agent_index', (YLeaf(YType.uint32, 'agent-index'), ['int'])),
                                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                                    ('waiting_for_response', (YLeaf(YType.boolean, 'waiting-for-response'), ['bool'])),
                                ])
                                self.agent_index = None
                                self.node = None
                                self.waiting_for_response = None

                                self.response_contents = Issu.Internals.Agents.Requests.Request.Agents_.Agent.ResponseContents()
                                self.response_contents.parent = self
                                self._children_name_map["response_contents"] = "response-contents"
                                self._segment_path = lambda: "agent" + "[agent-index='" + str(self.agent_index) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Issu.Internals.Agents.Requests.Request.Agents_.Agent, ['agent_index', 'node', 'waiting_for_response'], name, value)


                            class ResponseContents(Entity):
                                """
                                
                                
                                .. attribute:: agent_status
                                
                                	Enum indicating node status
                                	**type**\:  :py:class:`AgentStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.Agents.Requests.Request.Agents_.Agent.ResponseContents.AgentStatus>`
                                
                                .. attribute:: error_details
                                
                                	Further details of error occuring
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'issu'
                                _revision = '2018-03-12'

                                def __init__(self):
                                    super(Issu.Internals.Agents.Requests.Request.Agents_.Agent.ResponseContents, self).__init__()

                                    self.yang_name = "response-contents"
                                    self.yang_parent_name = "agent"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('agent_status', (YLeaf(YType.enumeration, 'agent-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu', 'Issu', 'Internals.Agents.Requests.Request.Agents_.Agent.ResponseContents.AgentStatus')])),
                                        ('error_details', (YLeaf(YType.str, 'error-details'), ['str'])),
                                    ])
                                    self.agent_status = None
                                    self.error_details = None
                                    self._segment_path = lambda: "response-contents"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Issu.Internals.Agents.Requests.Request.Agents_.Agent.ResponseContents, ['agent_status', 'error_details'], name, value)

                                class AgentStatus(Enum):
                                    """
                                    AgentStatus (Enum Class)

                                    Enum indicating node status

                                    .. data:: agent_response_ok = 0

                                    	Node is ready/operation successful

                                    .. data:: agent_response_error = 1

                                    	Otherwise undefined error

                                    .. data:: agent_response_timeout = 2

                                    	Timeout during request

                                    .. data:: agent_response_send_failure = 3

                                    	Failed to send request

                                    """

                                    agent_response_ok = Enum.YLeaf(0, "agent-response-ok")

                                    agent_response_error = Enum.YLeaf(1, "agent-response-error")

                                    agent_response_timeout = Enum.YLeaf(2, "agent-response-timeout")

                                    agent_response_send_failure = Enum.YLeaf(3, "agent-response-send-failure")



            class Inventory(Entity):
                """
                Inventory of agents held by Agent module
                
                .. attribute:: agent
                
                	
                	**type**\: list of  		 :py:class:`Agent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.Agents.Inventory.Agent>`
                
                

                """

                _prefix = 'issu'
                _revision = '2018-03-12'

                def __init__(self):
                    super(Issu.Internals.Agents.Inventory, self).__init__()

                    self.yang_name = "inventory"
                    self.yang_parent_name = "agents"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("agent", ("agent", Issu.Internals.Agents.Inventory.Agent))])
                    self._leafs = OrderedDict()

                    self.agent = YList(self)
                    self._segment_path = lambda: "inventory"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/internals/agents/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Issu.Internals.Agents.Inventory, [], name, value)


                class Agent(Entity):
                    """
                    
                    
                    .. attribute:: agent_index  (key)
                    
                    	Integer agent index
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: agent_node
                    
                    	Agent node ID
                    	**type**\: str
                    
                    .. attribute:: reloaded
                    
                    	True if node has been reloaded. False otherwise
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'issu'
                    _revision = '2018-03-12'

                    def __init__(self):
                        super(Issu.Internals.Agents.Inventory.Agent, self).__init__()

                        self.yang_name = "agent"
                        self.yang_parent_name = "inventory"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['agent_index']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('agent_index', (YLeaf(YType.uint32, 'agent-index'), ['int'])),
                            ('agent_node', (YLeaf(YType.str, 'agent-node'), ['str'])),
                            ('reloaded', (YLeaf(YType.boolean, 'reloaded'), ['bool'])),
                        ])
                        self.agent_index = None
                        self.agent_node = None
                        self.reloaded = None
                        self._segment_path = lambda: "agent" + "[agent-index='" + str(self.agent_index) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/internals/agents/inventory/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Issu.Internals.Agents.Inventory.Agent, ['agent_index', 'agent_node', 'reloaded'], name, value)


            class ReloadTracking(Entity):
                """
                Reload tracking performed by Agent module
                
                .. attribute:: in_progress
                
                	True if reload tracking in progress
                	**type**\: bool
                
                .. attribute:: remaining_nodes_count
                
                	Number of nodes which have not yet reloaded
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: node
                
                	
                	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.Agents.ReloadTracking.Node>`
                
                

                """

                _prefix = 'issu'
                _revision = '2018-03-12'

                def __init__(self):
                    super(Issu.Internals.Agents.ReloadTracking, self).__init__()

                    self.yang_name = "reload-tracking"
                    self.yang_parent_name = "agents"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("node", ("node", Issu.Internals.Agents.ReloadTracking.Node))])
                    self._leafs = OrderedDict([
                        ('in_progress', (YLeaf(YType.boolean, 'in-progress'), ['bool'])),
                        ('remaining_nodes_count', (YLeaf(YType.uint32, 'remaining-nodes-count'), ['int'])),
                    ])
                    self.in_progress = None
                    self.remaining_nodes_count = None

                    self.node = YList(self)
                    self._segment_path = lambda: "reload-tracking"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/internals/agents/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Issu.Internals.Agents.ReloadTracking, ['in_progress', 'remaining_nodes_count'], name, value)


                class Node(Entity):
                    """
                    
                    
                    .. attribute:: node_index  (key)
                    
                    	Integer node index
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: id
                    
                    	Node ID
                    	**type**\: str
                    
                    .. attribute:: reloaded
                    
                    	True if node has been reloaded. False otherwise
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'issu'
                    _revision = '2018-03-12'

                    def __init__(self):
                        super(Issu.Internals.Agents.ReloadTracking.Node, self).__init__()

                        self.yang_name = "node"
                        self.yang_parent_name = "reload-tracking"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['node_index']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('node_index', (YLeaf(YType.uint32, 'node-index'), ['int'])),
                            ('id', (YLeaf(YType.str, 'id'), ['str'])),
                            ('reloaded', (YLeaf(YType.boolean, 'reloaded'), ['bool'])),
                        ])
                        self.node_index = None
                        self.id = None
                        self.reloaded = None
                        self._segment_path = lambda: "node" + "[node-index='" + str(self.node_index) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/internals/agents/reload-tracking/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Issu.Internals.Agents.ReloadTracking.Node, ['node_index', 'id', 'reloaded'], name, value)


        class InventoryMonitor(Entity):
            """
            Inventory monitor module internal state
            
            .. attribute:: inventory
            
            	Inventory of nodes in the system held by ISSU Director
            	**type**\:  :py:class:`Inventory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.InventoryMonitor.Inventory>`
            
            

            """

            _prefix = 'issu'
            _revision = '2018-03-12'

            def __init__(self):
                super(Issu.Internals.InventoryMonitor, self).__init__()

                self.yang_name = "inventory-monitor"
                self.yang_parent_name = "internals"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("inventory", ("inventory", Issu.Internals.InventoryMonitor.Inventory))])
                self._leafs = OrderedDict()

                self.inventory = Issu.Internals.InventoryMonitor.Inventory()
                self.inventory.parent = self
                self._children_name_map["inventory"] = "inventory"
                self._segment_path = lambda: "inventory-monitor"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/internals/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Issu.Internals.InventoryMonitor, [], name, value)


            class Inventory(Entity):
                """
                Inventory of nodes in the system held by ISSU Director
                
                .. attribute:: node
                
                	The tree of nodes within the Inventory monitor module, keyed by node ID
                	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_issu.Issu.Internals.InventoryMonitor.Inventory.Node>`
                
                

                """

                _prefix = 'issu'
                _revision = '2018-03-12'

                def __init__(self):
                    super(Issu.Internals.InventoryMonitor.Inventory, self).__init__()

                    self.yang_name = "inventory"
                    self.yang_parent_name = "inventory-monitor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("node", ("node", Issu.Internals.InventoryMonitor.Inventory.Node))])
                    self._leafs = OrderedDict()

                    self.node = YList(self)
                    self._segment_path = lambda: "inventory"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/internals/inventory-monitor/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Issu.Internals.InventoryMonitor.Inventory, [], name, value)


                class Node(Entity):
                    """
                    The tree of nodes within the Inventory monitor module, keyed by node ID
                    
                    .. attribute:: node  (key)
                    
                    	Node ID
                    	**type**\: str
                    
                    .. attribute:: ip
                    
                    	Node IP address
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'issu'
                    _revision = '2018-03-12'

                    def __init__(self):
                        super(Issu.Internals.InventoryMonitor.Inventory.Node, self).__init__()

                        self.yang_name = "node"
                        self.yang_parent_name = "inventory"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['node']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('node', (YLeaf(YType.str, 'node'), ['str'])),
                            ('ip', (YLeaf(YType.str, 'ip'), ['str'])),
                        ])
                        self.node = None
                        self.ip = None
                        self._segment_path = lambda: "node" + "[node='" + str(self.node) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-issu:issu/internals/inventory-monitor/inventory/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Issu.Internals.InventoryMonitor.Inventory.Node, ['node', 'ip'], name, value)

    def clone_ptr(self):
        self._top_entity = Issu()
        return self._top_entity


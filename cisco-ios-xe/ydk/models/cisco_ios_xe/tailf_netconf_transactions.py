""" tailf_netconf_transactions 

This module introduces four new rpc methods that are used to
control a two\-phase commit transaction on the NETCONF server.
The normal <edit\-config> operation is used to write data in the
transaction, but the modifications are not applied until an
explicit <commit\-transaction> is sent.

A typical sequence of operations looks like this\:


          C                           S
          \|                           \|
          \|  capability exchange      \|
          \|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\->\|
          \|<\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\->\|
          \|                           \|
          \|   <start\-transaction>     \|
          \|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\->\|
          \|<\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|
          \|         <ok/>             \|
          \|                           \|
          \|     <edit\-config>         \|
          \|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\->\|
          \|<\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|
          \|         <ok/>             \|
          \|                           \|
          \|  <prepare\-transaction>    \|
          \|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\->\|
          \|<\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|
          \|         <ok/>             \|
          \|                           \|
          \|   <commit\-transaction>    \|
          \|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\->\|
          \|<\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|
          \|         <ok/>             \|
          \|                           \|


"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class StartTransaction(Entity):
    """
    Starts a transaction towards a configuration datastore.  There
    can be a single ongoing transaction per session at any time.
    
    When a transaction has been started, the client can send any
    NETCONF operation, but any <edit\-config> or <copy\-config>
    operation sent from the client MUST specify the same <target>
    as the <start\-transaction>, and any <get\-config> MUST specify
    the same <source> as <start\-transaction>.
    
    If the server receives an <edit\-config> or <copy\-config> with
    another <target>, or a <get\-config> with another <source>, an
    error MUST be returned with an <error\-tag> set to 'invalid\-value'.
    
    The modifications sent in the <edit\-config> operations are not
    immediately applied to the configuration datastore.  Instead
    they are kept in the transaction state of the server.  The
    transaction state is only applied when a <commit\-transaction>
    is received.
    
    The client sends a <prepare\-transaction> when all modifications
    have been sent.
    
    If there is an ongoing transaction for this session already, an
    error MUST be returned with <error\-app\-tag> set to 'bad\-state'.
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.tailf_netconf_transactions.StartTransaction.Input>`
    
    

    """

    _prefix = 'tr'

    def __init__(self):
        super(StartTransaction, self).__init__()
        self._top_entity = None

        self.yang_name = "start-transaction"
        self.yang_parent_name = "tailf-netconf-transactions"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = StartTransaction.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")
        self._segment_path = lambda: "tailf-netconf-transactions:start-transaction"


    class Input(Entity):
        """
        
        
        .. attribute:: target
        
        	Name of the configuration datastore towards which the transaction is started
        	**type**\:  :py:class:`Target <ydk.models.cisco_ios_xe.tailf_netconf_transactions.StartTransaction.Input.Target>`
        
        .. attribute:: with_inactive
        
        	If the parameter is present in <start\-transaction>, it MUST also be present in any <edit\-config>, <copy\-config>, <get>, or <get\-config> operations within the transaction.  If it is not present in <start\-transaction>, it MUST NOT be present in any <edit\-config> operation within the transaction
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'tr'

        def __init__(self):
            super(StartTransaction.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "start-transaction"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("target", ("target", StartTransaction.Input.Target))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('with_inactive', YLeaf(YType.empty, 'tailf-netconf-inactive:with-inactive')),
            ])
            self.with_inactive = None

            self.target = StartTransaction.Input.Target()
            self.target.parent = self
            self._children_name_map["target"] = "target"
            self._children_yang_names.add("target")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "tailf-netconf-transactions:start-transaction/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(StartTransaction.Input, ['with_inactive'], name, value)


        class Target(Entity):
            """
            Name of the configuration datastore towards which the
            transaction is started.
            
            .. attribute:: startup
            
            	
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: running
            
            	
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: candidate
            
            	
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'tr'

            def __init__(self):
                super(StartTransaction.Input.Target, self).__init__()

                self.yang_name = "target"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('startup', YLeaf(YType.empty, 'startup')),
                    ('running', YLeaf(YType.empty, 'running')),
                    ('candidate', YLeaf(YType.empty, 'candidate')),
                ])
                self.startup = None
                self.running = None
                self.candidate = None
                self._segment_path = lambda: "target"
                self._absolute_path = lambda: "tailf-netconf-transactions:start-transaction/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(StartTransaction.Input.Target, ['startup', 'running', 'candidate'], name, value)

    def clone_ptr(self):
        self._top_entity = StartTransaction()
        return self._top_entity

class PrepareTransaction(Entity):
    """
    Prepares the transaction state for commit.  The server may reject
    the prepare request for any reason, for example due to lack of
    resources or if the combined changes would result in an invalid
    configuration datastore.
    
    After a successful <prepare\-transaction>, the next transaction
    related rpc operation must be <commit\-transaction> or
    <abort\-transaction>.  Note that an <edit\-config> cannot be sent
    before the transaction is either committed or aborted.
    
    Care must be taken by the server to make sure that if
    <prepare\-transaction> succeeds then the <commit\-transaction>
    SHOULD not fail, since this might result in an inconsistent
    distributed state.  Thus, <prepare\-transaction> should allocate
    any resources needed to make sure the <commit\-transaction> will
    succeed.
    
    If there is no ongoing transaction in this session, or if the
    ongoing transaction already has been prepared, an error MUST be
    returned with <error\-app\-tag> set to 'bad\-state'.
    
    

    """

    _prefix = 'tr'

    def __init__(self):
        super(PrepareTransaction, self).__init__()
        self._top_entity = None

        self.yang_name = "prepare-transaction"
        self.yang_parent_name = "tailf-netconf-transactions"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "tailf-netconf-transactions:prepare-transaction"

    def clone_ptr(self):
        self._top_entity = PrepareTransaction()
        return self._top_entity

class CommitTransaction(Entity):
    """
    Applies the changes made in the transaction to the configuration
    datatore.  The transaction is closed after a <commit\-transaction>.
    
    If there is no ongoing transaction in this session, or if the
    ongoing transaction already has not been prepared, an error
    MUST be returned with <error\-app\-tag> set to 'bad\-state'.
    
    

    """

    _prefix = 'tr'

    def __init__(self):
        super(CommitTransaction, self).__init__()
        self._top_entity = None

        self.yang_name = "commit-transaction"
        self.yang_parent_name = "tailf-netconf-transactions"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "tailf-netconf-transactions:commit-transaction"

    def clone_ptr(self):
        self._top_entity = CommitTransaction()
        return self._top_entity

class AbortTransaction(Entity):
    """
    Aborts the ongoing transaction, and all pending changes are
    discarded.  <abort\-transaction> can be given at any time during an
    ongoing transaction.
    
    If there is no ongoing transaction in this session, an error MUST
    be returned with <error\-app\-tag> set to 'bad\-state'.
    
    

    """

    _prefix = 'tr'

    def __init__(self):
        super(AbortTransaction, self).__init__()
        self._top_entity = None

        self.yang_name = "abort-transaction"
        self.yang_parent_name = "tailf-netconf-transactions"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "tailf-netconf-transactions:abort-transaction"

    def clone_ptr(self):
        self._top_entity = AbortTransaction()
        return self._top_entity


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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
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
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.tailf_netconf_transactions.StartTransaction.Input>`
    
    

    """

    _prefix = 'tr'

    def __init__(self):
        super(StartTransaction, self).__init__()
        self._top_entity = None

        self.yang_name = "start-transaction"
        self.yang_parent_name = "tailf-netconf-transactions"

        self.input = StartTransaction.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: target
        
        	Name of the configuration datastore towards which the transaction is started
        	**type**\:   :py:class:`Target <ydk.models.cisco_ios_xe.tailf_netconf_transactions.StartTransaction.Input.Target>`
        
        .. attribute:: with_inactive
        
        	If the parameter is present in <start\-transaction>, it MUST also be present in any <edit\-config>, <copy\-config>, <get>, or <get\-config> operations within the transaction.  If it is not present in <start\-transaction>, it MUST NOT be present in any <edit\-config> operation within the transaction
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'tr'

        def __init__(self):
            super(StartTransaction.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "start-transaction"

            self.with_inactive = YLeaf(YType.empty, "tailf-netconf-inactive:with-inactive")

            self.target = StartTransaction.Input.Target()
            self.target.parent = self
            self._children_name_map["target"] = "target"
            self._children_yang_names.add("target")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("with_inactive") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(StartTransaction.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(StartTransaction.Input, self).__setattr__(name, value)


        class Target(Entity):
            """
            Name of the configuration datastore towards which the
            transaction is started.
            
            .. attribute:: candidate
            
            	
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: running
            
            	
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: startup
            
            	
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'tr'

            def __init__(self):
                super(StartTransaction.Input.Target, self).__init__()

                self.yang_name = "target"
                self.yang_parent_name = "input"

                self.candidate = YLeaf(YType.empty, "candidate")

                self.running = YLeaf(YType.empty, "running")

                self.startup = YLeaf(YType.empty, "startup")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("candidate",
                                "running",
                                "startup") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(StartTransaction.Input.Target, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(StartTransaction.Input.Target, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.candidate.is_set or
                    self.running.is_set or
                    self.startup.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.candidate.yfilter != YFilter.not_set or
                    self.running.yfilter != YFilter.not_set or
                    self.startup.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "target" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "tailf-netconf-transactions:start-transaction/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.candidate.is_set or self.candidate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.candidate.get_name_leafdata())
                if (self.running.is_set or self.running.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.running.get_name_leafdata())
                if (self.startup.is_set or self.startup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.startup.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "candidate" or name == "running" or name == "startup"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "candidate"):
                    self.candidate = value
                    self.candidate.value_namespace = name_space
                    self.candidate.value_namespace_prefix = name_space_prefix
                if(value_path == "running"):
                    self.running = value
                    self.running.value_namespace = name_space
                    self.running.value_namespace_prefix = name_space_prefix
                if(value_path == "startup"):
                    self.startup = value
                    self.startup.value_namespace = name_space
                    self.startup.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.with_inactive.is_set or
                (self.target is not None and self.target.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.with_inactive.yfilter != YFilter.not_set or
                (self.target is not None and self.target.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "tailf-netconf-transactions:start-transaction/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.with_inactive.is_set or self.with_inactive.yfilter != YFilter.not_set):
                leaf_name_data.append(self.with_inactive.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "target"):
                if (self.target is None):
                    self.target = StartTransaction.Input.Target()
                    self.target.parent = self
                    self._children_name_map["target"] = "target"
                return self.target

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "target" or name == "with-inactive"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "with-inactive"):
                self.with_inactive = value
                self.with_inactive.value_namespace = name_space
                self.with_inactive.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "tailf-netconf-transactions:start-transaction" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = StartTransaction.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

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

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "tailf-netconf-transactions:prepare-transaction" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

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

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "tailf-netconf-transactions:commit-transaction" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

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

    def has_data(self):
        return False

    def has_operation(self):
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "tailf-netconf-transactions:abort-transaction" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        return None

    def has_leaf_or_child_of_name(self, name):
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = AbortTransaction()
        return self._top_entity


""" INTEGRATED_SERVICES_MIB 

The MIB module to describe the Integrated Services
Protocol

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Qosservice(Enum):
    """
    Qosservice

    The class of service in use by a flow.

    .. data:: bestEffort = 1

    .. data:: guaranteedDelay = 2

    .. data:: controlledLoad = 5

    """

    bestEffort = Enum.YLeaf(1, "bestEffort")

    guaranteedDelay = Enum.YLeaf(2, "guaranteedDelay")

    controlledLoad = Enum.YLeaf(5, "controlledLoad")



class IntegratedServicesMib(Entity):
    """
    
    
    .. attribute:: intsrvflowtable
    
    	Information describing the reserved flows  us\- ing the system's interfaces
    	**type**\:   :py:class:`Intsrvflowtable <ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB.IntegratedServicesMib.Intsrvflowtable>`
    
    .. attribute:: intsrvgenobjects
    
    	
    	**type**\:   :py:class:`Intsrvgenobjects <ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB.IntegratedServicesMib.Intsrvgenobjects>`
    
    .. attribute:: intsrvifattribtable
    
    	The reservable attributes of the system's  in\- terfaces
    	**type**\:   :py:class:`Intsrvifattribtable <ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB.IntegratedServicesMib.Intsrvifattribtable>`
    
    

    """

    _prefix = 'INTEGRATED-SERVICES-MIB'
    _revision = '1995-11-03'

    def __init__(self):
        super(IntegratedServicesMib, self).__init__()
        self._top_entity = None

        self.yang_name = "INTEGRATED-SERVICES-MIB"
        self.yang_parent_name = "INTEGRATED-SERVICES-MIB"

        self.intsrvflowtable = IntegratedServicesMib.Intsrvflowtable()
        self.intsrvflowtable.parent = self
        self._children_name_map["intsrvflowtable"] = "intSrvFlowTable"
        self._children_yang_names.add("intSrvFlowTable")

        self.intsrvgenobjects = IntegratedServicesMib.Intsrvgenobjects()
        self.intsrvgenobjects.parent = self
        self._children_name_map["intsrvgenobjects"] = "intSrvGenObjects"
        self._children_yang_names.add("intSrvGenObjects")

        self.intsrvifattribtable = IntegratedServicesMib.Intsrvifattribtable()
        self.intsrvifattribtable.parent = self
        self._children_name_map["intsrvifattribtable"] = "intSrvIfAttribTable"
        self._children_yang_names.add("intSrvIfAttribTable")


    class Intsrvgenobjects(Entity):
        """
        
        
        .. attribute:: intsrvflownewindex
        
        	This  object  is  used  to  assign  values  to intSrvFlowNumber  as described in 'Textual Con\- ventions  for  SNMPv2'.   The  network  manager reads  the  object,  and  then writes the value back in the SET that creates a new instance  of intSrvFlowEntry.   If  the  SET  fails with the code 'inconsistentValue', then the process must be  repeated; If the SET succeeds, then the ob\- ject is incremented, and the  new  instance  is created according to the manager's directions
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'INTEGRATED-SERVICES-MIB'
        _revision = '1995-11-03'

        def __init__(self):
            super(IntegratedServicesMib.Intsrvgenobjects, self).__init__()

            self.yang_name = "intSrvGenObjects"
            self.yang_parent_name = "INTEGRATED-SERVICES-MIB"

            self.intsrvflownewindex = YLeaf(YType.int32, "intSrvFlowNewIndex")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("intsrvflownewindex") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(IntegratedServicesMib.Intsrvgenobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IntegratedServicesMib.Intsrvgenobjects, self).__setattr__(name, value)

        def has_data(self):
            return self.intsrvflownewindex.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.intsrvflownewindex.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "intSrvGenObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "INTEGRATED-SERVICES-MIB:INTEGRATED-SERVICES-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.intsrvflownewindex.is_set or self.intsrvflownewindex.yfilter != YFilter.not_set):
                leaf_name_data.append(self.intsrvflownewindex.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "intSrvFlowNewIndex"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "intSrvFlowNewIndex"):
                self.intsrvflownewindex = value
                self.intsrvflownewindex.value_namespace = name_space
                self.intsrvflownewindex.value_namespace_prefix = name_space_prefix


    class Intsrvifattribtable(Entity):
        """
        The reservable attributes of the system's  in\-
        terfaces.
        
        .. attribute:: intsrvifattribentry
        
        	The reservable attributes of  a  given  inter\- face
        	**type**\: list of    :py:class:`Intsrvifattribentry <ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB.IntegratedServicesMib.Intsrvifattribtable.Intsrvifattribentry>`
        
        

        """

        _prefix = 'INTEGRATED-SERVICES-MIB'
        _revision = '1995-11-03'

        def __init__(self):
            super(IntegratedServicesMib.Intsrvifattribtable, self).__init__()

            self.yang_name = "intSrvIfAttribTable"
            self.yang_parent_name = "INTEGRATED-SERVICES-MIB"

            self.intsrvifattribentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(IntegratedServicesMib.Intsrvifattribtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IntegratedServicesMib.Intsrvifattribtable, self).__setattr__(name, value)


        class Intsrvifattribentry(Entity):
            """
            The reservable attributes of  a  given  inter\-
            face.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: intsrvifattriballocatedbits
            
            	The number of bits/second currently  allocated to reserved sessions on the interface
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: Bits per second
            
            .. attribute:: intsrvifattriballocatedbuffer
            
            	The amount of buffer space  required  to  hold the simultaneous burst of all reserved flows on the interface
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: Bytes
            
            .. attribute:: intsrvifattribflows
            
            	The number of reserved flows currently  active on  this  interface.  A flow can be created ei\- ther from a reservation protocol (such as  RSVP or ST\-II) or via configuration information
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: intsrvifattribmaxallocatedbits
            
            	The maximum number of bits/second that may  be allocated  to  reserved  sessions on the inter\- face
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: Bits per second
            
            .. attribute:: intsrvifattribpropagationdelay
            
            	The amount of propagation delay that this  in\- terface  introduces  in addition to that intro\- diced by bit propagation delays
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: intsrvifattribstatus
            
            	'active' on interfaces that are configured for RSVP
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'INTEGRATED-SERVICES-MIB'
            _revision = '1995-11-03'

            def __init__(self):
                super(IntegratedServicesMib.Intsrvifattribtable.Intsrvifattribentry, self).__init__()

                self.yang_name = "intSrvIfAttribEntry"
                self.yang_parent_name = "intSrvIfAttribTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.intsrvifattriballocatedbits = YLeaf(YType.int32, "intSrvIfAttribAllocatedBits")

                self.intsrvifattriballocatedbuffer = YLeaf(YType.int32, "intSrvIfAttribAllocatedBuffer")

                self.intsrvifattribflows = YLeaf(YType.uint32, "intSrvIfAttribFlows")

                self.intsrvifattribmaxallocatedbits = YLeaf(YType.int32, "intSrvIfAttribMaxAllocatedBits")

                self.intsrvifattribpropagationdelay = YLeaf(YType.int32, "intSrvIfAttribPropagationDelay")

                self.intsrvifattribstatus = YLeaf(YType.enumeration, "intSrvIfAttribStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "intsrvifattriballocatedbits",
                                "intsrvifattriballocatedbuffer",
                                "intsrvifattribflows",
                                "intsrvifattribmaxallocatedbits",
                                "intsrvifattribpropagationdelay",
                                "intsrvifattribstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IntegratedServicesMib.Intsrvifattribtable.Intsrvifattribentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IntegratedServicesMib.Intsrvifattribtable.Intsrvifattribentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.intsrvifattriballocatedbits.is_set or
                    self.intsrvifattriballocatedbuffer.is_set or
                    self.intsrvifattribflows.is_set or
                    self.intsrvifattribmaxallocatedbits.is_set or
                    self.intsrvifattribpropagationdelay.is_set or
                    self.intsrvifattribstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.intsrvifattriballocatedbits.yfilter != YFilter.not_set or
                    self.intsrvifattriballocatedbuffer.yfilter != YFilter.not_set or
                    self.intsrvifattribflows.yfilter != YFilter.not_set or
                    self.intsrvifattribmaxallocatedbits.yfilter != YFilter.not_set or
                    self.intsrvifattribpropagationdelay.yfilter != YFilter.not_set or
                    self.intsrvifattribstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "intSrvIfAttribEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "INTEGRATED-SERVICES-MIB:INTEGRATED-SERVICES-MIB/intSrvIfAttribTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.intsrvifattriballocatedbits.is_set or self.intsrvifattriballocatedbits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvifattriballocatedbits.get_name_leafdata())
                if (self.intsrvifattriballocatedbuffer.is_set or self.intsrvifattriballocatedbuffer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvifattriballocatedbuffer.get_name_leafdata())
                if (self.intsrvifattribflows.is_set or self.intsrvifattribflows.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvifattribflows.get_name_leafdata())
                if (self.intsrvifattribmaxallocatedbits.is_set or self.intsrvifattribmaxallocatedbits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvifattribmaxallocatedbits.get_name_leafdata())
                if (self.intsrvifattribpropagationdelay.is_set or self.intsrvifattribpropagationdelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvifattribpropagationdelay.get_name_leafdata())
                if (self.intsrvifattribstatus.is_set or self.intsrvifattribstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvifattribstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "intSrvIfAttribAllocatedBits" or name == "intSrvIfAttribAllocatedBuffer" or name == "intSrvIfAttribFlows" or name == "intSrvIfAttribMaxAllocatedBits" or name == "intSrvIfAttribPropagationDelay" or name == "intSrvIfAttribStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvIfAttribAllocatedBits"):
                    self.intsrvifattriballocatedbits = value
                    self.intsrvifattriballocatedbits.value_namespace = name_space
                    self.intsrvifattriballocatedbits.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvIfAttribAllocatedBuffer"):
                    self.intsrvifattriballocatedbuffer = value
                    self.intsrvifattriballocatedbuffer.value_namespace = name_space
                    self.intsrvifattriballocatedbuffer.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvIfAttribFlows"):
                    self.intsrvifattribflows = value
                    self.intsrvifattribflows.value_namespace = name_space
                    self.intsrvifattribflows.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvIfAttribMaxAllocatedBits"):
                    self.intsrvifattribmaxallocatedbits = value
                    self.intsrvifattribmaxallocatedbits.value_namespace = name_space
                    self.intsrvifattribmaxallocatedbits.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvIfAttribPropagationDelay"):
                    self.intsrvifattribpropagationdelay = value
                    self.intsrvifattribpropagationdelay.value_namespace = name_space
                    self.intsrvifattribpropagationdelay.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvIfAttribStatus"):
                    self.intsrvifattribstatus = value
                    self.intsrvifattribstatus.value_namespace = name_space
                    self.intsrvifattribstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.intsrvifattribentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.intsrvifattribentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "intSrvIfAttribTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "INTEGRATED-SERVICES-MIB:INTEGRATED-SERVICES-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "intSrvIfAttribEntry"):
                for c in self.intsrvifattribentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IntegratedServicesMib.Intsrvifattribtable.Intsrvifattribentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.intsrvifattribentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "intSrvIfAttribEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Intsrvflowtable(Entity):
        """
        Information describing the reserved flows  us\-
        ing the system's interfaces.
        
        .. attribute:: intsrvflowentry
        
        	Information describing the use of a given  in\- terface   by   a   given   flow.   The  counter intSrvFlowPoliced starts counting  at  the  in\- stallation of the flow
        	**type**\: list of    :py:class:`Intsrvflowentry <ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB.IntegratedServicesMib.Intsrvflowtable.Intsrvflowentry>`
        
        

        """

        _prefix = 'INTEGRATED-SERVICES-MIB'
        _revision = '1995-11-03'

        def __init__(self):
            super(IntegratedServicesMib.Intsrvflowtable, self).__init__()

            self.yang_name = "intSrvFlowTable"
            self.yang_parent_name = "INTEGRATED-SERVICES-MIB"

            self.intsrvflowentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(IntegratedServicesMib.Intsrvflowtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IntegratedServicesMib.Intsrvflowtable, self).__setattr__(name, value)


        class Intsrvflowentry(Entity):
            """
            Information describing the use of a given  in\-
            terface   by   a   given   flow.   The  counter
            intSrvFlowPoliced starts counting  at  the  in\-
            stallation of the flow.
            
            .. attribute:: intsrvflownumber  <key>
            
            	The number of this flow.  This is for SNMP In\- dexing purposes only and has no relation to any protocol value
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: intsrvflowbesteffort
            
            	The number of packets that  were  remanded  to best effort service
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: intsrvflowburst
            
            	The size of the largest  burst  expected  from the sender at a time.  If this is less than  the  sender's  advertised burst  size, the receiver is asking the network to provide flow pacing  beyond  what  would  be provided  under normal circumstances. Such pac\- ing is at the network's option
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bytes
            
            .. attribute:: intsrvflowdestaddr
            
            	The destination address used by all senders in this  session.   This object may not be changed when the value of the RowStatus object is  'ac\- tive'
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: intsrvflowdestaddrlength
            
            	The length of the destination address in bits. This  is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: intsrvflowdestport
            
            	The UDP or TCP port number used as a  destina\- tion  port for all senders in this session.  If the  IP   protocol   in   use,   specified   by intSrvResvFwdProtocol,  is 50 (ESP) or 51 (AH), this  represents  a  virtual  destination  port number.   A value of zero indicates that the IP protocol in use does not have ports.  This  ob\- ject  may  not be changed when the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 2..4
            
            .. attribute:: intsrvflowdiscard
            
            	If 'true', the flow  is  to  incur  loss  when traffic is policed.  If 'false', policed traff\- ic is treated as best effort traffic
            	**type**\:  bool
            
            .. attribute:: intsrvflowflowid
            
            	The flow ID that  this  sender  is  using,  if this  is  an IPv6 session
            	**type**\:  int
            
            	**range:** 0..16777215
            
            .. attribute:: intsrvflowifaddr
            
            	The IP Address on the ifEntry  on  which  this reservation  exists.  This is present primarily to support those interfaces which layer  multi\- ple IP Addresses on the interface
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: intsrvflowinterface
            
            	The ifIndex value of the  interface  on  which this reservation exists
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: intsrvflowmaxtu
            
            	The maximum datagram size for this  flow  that will conform to the traffic specification. This value cannot exceed the MTU of the interface
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: intsrvflowmintu
            
            	The minimum message size for  this  flow.  The policing  algorithm will treat smaller messages as though they are this size
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: intsrvfloworder
            
            	In the event of ambiguity, the order in  which the  classifier  should  make  its comparisons. The row with intSrvFlowOrder=0 is tried  first, and  comparisons  proceed  in  the order of in\- creasing value.  Non\-serial implementations  of the classifier should emulate this behavior
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: intsrvflowowner
            
            	The process that installed this  flow  in  the queue policy database
            	**type**\:   :py:class:`Intsrvflowowner <ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB.IntegratedServicesMib.Intsrvflowtable.Intsrvflowentry.Intsrvflowowner>`
            
            .. attribute:: intsrvflowpoliced
            
            	The number of packets policed since the incep\- tion of the flow's service
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: intsrvflowport
            
            	The UDP or TCP port number used  as  a  source port  for  this sender in this session.  If the IP    protocol    in    use,    specified    by intSrvResvFwdProtocol  is  50 (ESP) or 51 (AH), this represents a generalized  port  identifier (GPI).   A  value of zero indicates that the IP protocol in use does not have ports.  This  ob\- ject  may  not be changed when the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 2..4
            
            .. attribute:: intsrvflowprotocol
            
            	The IP Protocol used by a session.   This  ob\- ject  may  not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: intsrvflowqueue
            
            	The number of the queue used by this  traffic. Note  that the interpretation of this object is implementation\-specific,   as   implementations vary in their use of queue identifiers
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: intsrvflowrate
            
            	The Reserved Rate of the sender's data stream. If this is a Controlled Load service flow, this rate is derived from the Tspec  rate  parameter (r).   If  this  is  a Guaranteed service flow, this rate is derived from  the  Rspec  clearing rate parameter (R)
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: intsrvflowsenderaddr
            
            	The source address of the sender  selected  by this  reservation.  The value of all zeroes in\- dicates 'all senders'.  This object may not  be changed  when the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: intsrvflowsenderaddrlength
            
            	The length of the sender's  address  in  bits. This  is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: intsrvflowservice
            
            	The QoS service being applied to this flow
            	**type**\:   :py:class:`Qosservice <ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB.Qosservice>`
            
            .. attribute:: intsrvflowstatus
            
            	'active' for all active  flows.   This  object may be used to install static classifier infor\- mation, delete classifier information,  or  au\- thorize such
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: intsrvflowtype
            
            	The type of session (IP4, IP6, IP6  with  flow information, etc)
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: intsrvflowweight
            
            	The weight used  to  prioritize  the  traffic. Note  that the interpretation of this object is implementation\-specific,   as   implementations vary in their use of weighting procedures
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'INTEGRATED-SERVICES-MIB'
            _revision = '1995-11-03'

            def __init__(self):
                super(IntegratedServicesMib.Intsrvflowtable.Intsrvflowentry, self).__init__()

                self.yang_name = "intSrvFlowEntry"
                self.yang_parent_name = "intSrvFlowTable"

                self.intsrvflownumber = YLeaf(YType.int32, "intSrvFlowNumber")

                self.intsrvflowbesteffort = YLeaf(YType.uint32, "intSrvFlowBestEffort")

                self.intsrvflowburst = YLeaf(YType.int32, "intSrvFlowBurst")

                self.intsrvflowdestaddr = YLeaf(YType.str, "intSrvFlowDestAddr")

                self.intsrvflowdestaddrlength = YLeaf(YType.int32, "intSrvFlowDestAddrLength")

                self.intsrvflowdestport = YLeaf(YType.str, "intSrvFlowDestPort")

                self.intsrvflowdiscard = YLeaf(YType.boolean, "intSrvFlowDiscard")

                self.intsrvflowflowid = YLeaf(YType.int32, "intSrvFlowFlowId")

                self.intsrvflowifaddr = YLeaf(YType.str, "intSrvFlowIfAddr")

                self.intsrvflowinterface = YLeaf(YType.int32, "intSrvFlowInterface")

                self.intsrvflowmaxtu = YLeaf(YType.int32, "intSrvFlowMaxTU")

                self.intsrvflowmintu = YLeaf(YType.int32, "intSrvFlowMinTU")

                self.intsrvfloworder = YLeaf(YType.int32, "intSrvFlowOrder")

                self.intsrvflowowner = YLeaf(YType.enumeration, "intSrvFlowOwner")

                self.intsrvflowpoliced = YLeaf(YType.uint32, "intSrvFlowPoliced")

                self.intsrvflowport = YLeaf(YType.str, "intSrvFlowPort")

                self.intsrvflowprotocol = YLeaf(YType.int32, "intSrvFlowProtocol")

                self.intsrvflowqueue = YLeaf(YType.int32, "intSrvFlowQueue")

                self.intsrvflowrate = YLeaf(YType.int32, "intSrvFlowRate")

                self.intsrvflowsenderaddr = YLeaf(YType.str, "intSrvFlowSenderAddr")

                self.intsrvflowsenderaddrlength = YLeaf(YType.int32, "intSrvFlowSenderAddrLength")

                self.intsrvflowservice = YLeaf(YType.enumeration, "intSrvFlowService")

                self.intsrvflowstatus = YLeaf(YType.enumeration, "intSrvFlowStatus")

                self.intsrvflowtype = YLeaf(YType.int32, "intSrvFlowType")

                self.intsrvflowweight = YLeaf(YType.int32, "intSrvFlowWeight")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("intsrvflownumber",
                                "intsrvflowbesteffort",
                                "intsrvflowburst",
                                "intsrvflowdestaddr",
                                "intsrvflowdestaddrlength",
                                "intsrvflowdestport",
                                "intsrvflowdiscard",
                                "intsrvflowflowid",
                                "intsrvflowifaddr",
                                "intsrvflowinterface",
                                "intsrvflowmaxtu",
                                "intsrvflowmintu",
                                "intsrvfloworder",
                                "intsrvflowowner",
                                "intsrvflowpoliced",
                                "intsrvflowport",
                                "intsrvflowprotocol",
                                "intsrvflowqueue",
                                "intsrvflowrate",
                                "intsrvflowsenderaddr",
                                "intsrvflowsenderaddrlength",
                                "intsrvflowservice",
                                "intsrvflowstatus",
                                "intsrvflowtype",
                                "intsrvflowweight") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IntegratedServicesMib.Intsrvflowtable.Intsrvflowentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IntegratedServicesMib.Intsrvflowtable.Intsrvflowentry, self).__setattr__(name, value)

            class Intsrvflowowner(Enum):
                """
                Intsrvflowowner

                The process that installed this  flow  in  the

                queue policy database.

                .. data:: other = 1

                .. data:: rsvp = 2

                .. data:: management = 3

                """

                other = Enum.YLeaf(1, "other")

                rsvp = Enum.YLeaf(2, "rsvp")

                management = Enum.YLeaf(3, "management")


            def has_data(self):
                return (
                    self.intsrvflownumber.is_set or
                    self.intsrvflowbesteffort.is_set or
                    self.intsrvflowburst.is_set or
                    self.intsrvflowdestaddr.is_set or
                    self.intsrvflowdestaddrlength.is_set or
                    self.intsrvflowdestport.is_set or
                    self.intsrvflowdiscard.is_set or
                    self.intsrvflowflowid.is_set or
                    self.intsrvflowifaddr.is_set or
                    self.intsrvflowinterface.is_set or
                    self.intsrvflowmaxtu.is_set or
                    self.intsrvflowmintu.is_set or
                    self.intsrvfloworder.is_set or
                    self.intsrvflowowner.is_set or
                    self.intsrvflowpoliced.is_set or
                    self.intsrvflowport.is_set or
                    self.intsrvflowprotocol.is_set or
                    self.intsrvflowqueue.is_set or
                    self.intsrvflowrate.is_set or
                    self.intsrvflowsenderaddr.is_set or
                    self.intsrvflowsenderaddrlength.is_set or
                    self.intsrvflowservice.is_set or
                    self.intsrvflowstatus.is_set or
                    self.intsrvflowtype.is_set or
                    self.intsrvflowweight.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.intsrvflownumber.yfilter != YFilter.not_set or
                    self.intsrvflowbesteffort.yfilter != YFilter.not_set or
                    self.intsrvflowburst.yfilter != YFilter.not_set or
                    self.intsrvflowdestaddr.yfilter != YFilter.not_set or
                    self.intsrvflowdestaddrlength.yfilter != YFilter.not_set or
                    self.intsrvflowdestport.yfilter != YFilter.not_set or
                    self.intsrvflowdiscard.yfilter != YFilter.not_set or
                    self.intsrvflowflowid.yfilter != YFilter.not_set or
                    self.intsrvflowifaddr.yfilter != YFilter.not_set or
                    self.intsrvflowinterface.yfilter != YFilter.not_set or
                    self.intsrvflowmaxtu.yfilter != YFilter.not_set or
                    self.intsrvflowmintu.yfilter != YFilter.not_set or
                    self.intsrvfloworder.yfilter != YFilter.not_set or
                    self.intsrvflowowner.yfilter != YFilter.not_set or
                    self.intsrvflowpoliced.yfilter != YFilter.not_set or
                    self.intsrvflowport.yfilter != YFilter.not_set or
                    self.intsrvflowprotocol.yfilter != YFilter.not_set or
                    self.intsrvflowqueue.yfilter != YFilter.not_set or
                    self.intsrvflowrate.yfilter != YFilter.not_set or
                    self.intsrvflowsenderaddr.yfilter != YFilter.not_set or
                    self.intsrvflowsenderaddrlength.yfilter != YFilter.not_set or
                    self.intsrvflowservice.yfilter != YFilter.not_set or
                    self.intsrvflowstatus.yfilter != YFilter.not_set or
                    self.intsrvflowtype.yfilter != YFilter.not_set or
                    self.intsrvflowweight.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "intSrvFlowEntry" + "[intSrvFlowNumber='" + self.intsrvflownumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "INTEGRATED-SERVICES-MIB:INTEGRATED-SERVICES-MIB/intSrvFlowTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.intsrvflownumber.is_set or self.intsrvflownumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflownumber.get_name_leafdata())
                if (self.intsrvflowbesteffort.is_set or self.intsrvflowbesteffort.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflowbesteffort.get_name_leafdata())
                if (self.intsrvflowburst.is_set or self.intsrvflowburst.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflowburst.get_name_leafdata())
                if (self.intsrvflowdestaddr.is_set or self.intsrvflowdestaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflowdestaddr.get_name_leafdata())
                if (self.intsrvflowdestaddrlength.is_set or self.intsrvflowdestaddrlength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflowdestaddrlength.get_name_leafdata())
                if (self.intsrvflowdestport.is_set or self.intsrvflowdestport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflowdestport.get_name_leafdata())
                if (self.intsrvflowdiscard.is_set or self.intsrvflowdiscard.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflowdiscard.get_name_leafdata())
                if (self.intsrvflowflowid.is_set or self.intsrvflowflowid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflowflowid.get_name_leafdata())
                if (self.intsrvflowifaddr.is_set or self.intsrvflowifaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflowifaddr.get_name_leafdata())
                if (self.intsrvflowinterface.is_set or self.intsrvflowinterface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflowinterface.get_name_leafdata())
                if (self.intsrvflowmaxtu.is_set or self.intsrvflowmaxtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflowmaxtu.get_name_leafdata())
                if (self.intsrvflowmintu.is_set or self.intsrvflowmintu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflowmintu.get_name_leafdata())
                if (self.intsrvfloworder.is_set or self.intsrvfloworder.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvfloworder.get_name_leafdata())
                if (self.intsrvflowowner.is_set or self.intsrvflowowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflowowner.get_name_leafdata())
                if (self.intsrvflowpoliced.is_set or self.intsrvflowpoliced.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflowpoliced.get_name_leafdata())
                if (self.intsrvflowport.is_set or self.intsrvflowport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflowport.get_name_leafdata())
                if (self.intsrvflowprotocol.is_set or self.intsrvflowprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflowprotocol.get_name_leafdata())
                if (self.intsrvflowqueue.is_set or self.intsrvflowqueue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflowqueue.get_name_leafdata())
                if (self.intsrvflowrate.is_set or self.intsrvflowrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflowrate.get_name_leafdata())
                if (self.intsrvflowsenderaddr.is_set or self.intsrvflowsenderaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflowsenderaddr.get_name_leafdata())
                if (self.intsrvflowsenderaddrlength.is_set or self.intsrvflowsenderaddrlength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflowsenderaddrlength.get_name_leafdata())
                if (self.intsrvflowservice.is_set or self.intsrvflowservice.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflowservice.get_name_leafdata())
                if (self.intsrvflowstatus.is_set or self.intsrvflowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflowstatus.get_name_leafdata())
                if (self.intsrvflowtype.is_set or self.intsrvflowtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflowtype.get_name_leafdata())
                if (self.intsrvflowweight.is_set or self.intsrvflowweight.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intsrvflowweight.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "intSrvFlowNumber" or name == "intSrvFlowBestEffort" or name == "intSrvFlowBurst" or name == "intSrvFlowDestAddr" or name == "intSrvFlowDestAddrLength" or name == "intSrvFlowDestPort" or name == "intSrvFlowDiscard" or name == "intSrvFlowFlowId" or name == "intSrvFlowIfAddr" or name == "intSrvFlowInterface" or name == "intSrvFlowMaxTU" or name == "intSrvFlowMinTU" or name == "intSrvFlowOrder" or name == "intSrvFlowOwner" or name == "intSrvFlowPoliced" or name == "intSrvFlowPort" or name == "intSrvFlowProtocol" or name == "intSrvFlowQueue" or name == "intSrvFlowRate" or name == "intSrvFlowSenderAddr" or name == "intSrvFlowSenderAddrLength" or name == "intSrvFlowService" or name == "intSrvFlowStatus" or name == "intSrvFlowType" or name == "intSrvFlowWeight"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "intSrvFlowNumber"):
                    self.intsrvflownumber = value
                    self.intsrvflownumber.value_namespace = name_space
                    self.intsrvflownumber.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowBestEffort"):
                    self.intsrvflowbesteffort = value
                    self.intsrvflowbesteffort.value_namespace = name_space
                    self.intsrvflowbesteffort.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowBurst"):
                    self.intsrvflowburst = value
                    self.intsrvflowburst.value_namespace = name_space
                    self.intsrvflowburst.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowDestAddr"):
                    self.intsrvflowdestaddr = value
                    self.intsrvflowdestaddr.value_namespace = name_space
                    self.intsrvflowdestaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowDestAddrLength"):
                    self.intsrvflowdestaddrlength = value
                    self.intsrvflowdestaddrlength.value_namespace = name_space
                    self.intsrvflowdestaddrlength.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowDestPort"):
                    self.intsrvflowdestport = value
                    self.intsrvflowdestport.value_namespace = name_space
                    self.intsrvflowdestport.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowDiscard"):
                    self.intsrvflowdiscard = value
                    self.intsrvflowdiscard.value_namespace = name_space
                    self.intsrvflowdiscard.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowFlowId"):
                    self.intsrvflowflowid = value
                    self.intsrvflowflowid.value_namespace = name_space
                    self.intsrvflowflowid.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowIfAddr"):
                    self.intsrvflowifaddr = value
                    self.intsrvflowifaddr.value_namespace = name_space
                    self.intsrvflowifaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowInterface"):
                    self.intsrvflowinterface = value
                    self.intsrvflowinterface.value_namespace = name_space
                    self.intsrvflowinterface.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowMaxTU"):
                    self.intsrvflowmaxtu = value
                    self.intsrvflowmaxtu.value_namespace = name_space
                    self.intsrvflowmaxtu.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowMinTU"):
                    self.intsrvflowmintu = value
                    self.intsrvflowmintu.value_namespace = name_space
                    self.intsrvflowmintu.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowOrder"):
                    self.intsrvfloworder = value
                    self.intsrvfloworder.value_namespace = name_space
                    self.intsrvfloworder.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowOwner"):
                    self.intsrvflowowner = value
                    self.intsrvflowowner.value_namespace = name_space
                    self.intsrvflowowner.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowPoliced"):
                    self.intsrvflowpoliced = value
                    self.intsrvflowpoliced.value_namespace = name_space
                    self.intsrvflowpoliced.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowPort"):
                    self.intsrvflowport = value
                    self.intsrvflowport.value_namespace = name_space
                    self.intsrvflowport.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowProtocol"):
                    self.intsrvflowprotocol = value
                    self.intsrvflowprotocol.value_namespace = name_space
                    self.intsrvflowprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowQueue"):
                    self.intsrvflowqueue = value
                    self.intsrvflowqueue.value_namespace = name_space
                    self.intsrvflowqueue.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowRate"):
                    self.intsrvflowrate = value
                    self.intsrvflowrate.value_namespace = name_space
                    self.intsrvflowrate.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowSenderAddr"):
                    self.intsrvflowsenderaddr = value
                    self.intsrvflowsenderaddr.value_namespace = name_space
                    self.intsrvflowsenderaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowSenderAddrLength"):
                    self.intsrvflowsenderaddrlength = value
                    self.intsrvflowsenderaddrlength.value_namespace = name_space
                    self.intsrvflowsenderaddrlength.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowService"):
                    self.intsrvflowservice = value
                    self.intsrvflowservice.value_namespace = name_space
                    self.intsrvflowservice.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowStatus"):
                    self.intsrvflowstatus = value
                    self.intsrvflowstatus.value_namespace = name_space
                    self.intsrvflowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowType"):
                    self.intsrvflowtype = value
                    self.intsrvflowtype.value_namespace = name_space
                    self.intsrvflowtype.value_namespace_prefix = name_space_prefix
                if(value_path == "intSrvFlowWeight"):
                    self.intsrvflowweight = value
                    self.intsrvflowweight.value_namespace = name_space
                    self.intsrvflowweight.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.intsrvflowentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.intsrvflowentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "intSrvFlowTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "INTEGRATED-SERVICES-MIB:INTEGRATED-SERVICES-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "intSrvFlowEntry"):
                for c in self.intsrvflowentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IntegratedServicesMib.Intsrvflowtable.Intsrvflowentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.intsrvflowentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "intSrvFlowEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.intsrvflowtable is not None and self.intsrvflowtable.has_data()) or
            (self.intsrvgenobjects is not None and self.intsrvgenobjects.has_data()) or
            (self.intsrvifattribtable is not None and self.intsrvifattribtable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.intsrvflowtable is not None and self.intsrvflowtable.has_operation()) or
            (self.intsrvgenobjects is not None and self.intsrvgenobjects.has_operation()) or
            (self.intsrvifattribtable is not None and self.intsrvifattribtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "INTEGRATED-SERVICES-MIB:INTEGRATED-SERVICES-MIB" + path_buffer

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

        if (child_yang_name == "intSrvFlowTable"):
            if (self.intsrvflowtable is None):
                self.intsrvflowtable = IntegratedServicesMib.Intsrvflowtable()
                self.intsrvflowtable.parent = self
                self._children_name_map["intsrvflowtable"] = "intSrvFlowTable"
            return self.intsrvflowtable

        if (child_yang_name == "intSrvGenObjects"):
            if (self.intsrvgenobjects is None):
                self.intsrvgenobjects = IntegratedServicesMib.Intsrvgenobjects()
                self.intsrvgenobjects.parent = self
                self._children_name_map["intsrvgenobjects"] = "intSrvGenObjects"
            return self.intsrvgenobjects

        if (child_yang_name == "intSrvIfAttribTable"):
            if (self.intsrvifattribtable is None):
                self.intsrvifattribtable = IntegratedServicesMib.Intsrvifattribtable()
                self.intsrvifattribtable.parent = self
                self._children_name_map["intsrvifattribtable"] = "intSrvIfAttribTable"
            return self.intsrvifattribtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "intSrvFlowTable" or name == "intSrvGenObjects" or name == "intSrvIfAttribTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = IntegratedServicesMib()
        return self._top_entity


""" Cisco_IOS_XR_fia_internal_tcam_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fia\-internal\-tcam package operational data.

This module contains definitions
for the following management objects\:
  controller\: Controller Resources

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Controller(Entity):
    """
    Controller Resources
    
    .. attribute:: dpa
    
    	Controller DPA operational data
    	**type**\:   :py:class:`Dpa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa>`
    
    

    """

    _prefix = 'fia-internal-tcam-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Controller, self).__init__()
        self._top_entity = None

        self.yang_name = "controller"
        self.yang_parent_name = "Cisco-IOS-XR-fia-internal-tcam-oper"

        self.dpa = Controller.Dpa()
        self.dpa.parent = self
        self._children_name_map["dpa"] = "dpa"
        self._children_yang_names.add("dpa")


    class Dpa(Entity):
        """
        Controller DPA operational data
        
        .. attribute:: nodes
        
        	DPA data for available nodes
        	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes>`
        
        

        """

        _prefix = 'fia-internal-tcam-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Controller.Dpa, self).__init__()

            self.yang_name = "dpa"
            self.yang_parent_name = "controller"

            self.nodes = Controller.Dpa.Nodes()
            self.nodes.parent = self
            self._children_name_map["nodes"] = "nodes"
            self._children_yang_names.add("nodes")


        class Nodes(Entity):
            """
            DPA data for available nodes
            
            .. attribute:: node
            
            	DPA operational data for a particular node
            	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes.Node>`
            
            

            """

            _prefix = 'fia-internal-tcam-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Controller.Dpa.Nodes, self).__init__()

                self.yang_name = "nodes"
                self.yang_parent_name = "dpa"

                self.node = YList(self)

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
                            super(Controller.Dpa.Nodes, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Controller.Dpa.Nodes, self).__setattr__(name, value)


            class Node(Entity):
                """
                DPA operational data for a particular node
                
                .. attribute:: node_name  <key>
                
                	Node ID
                	**type**\:  str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: external_tcam_resources
                
                	External TCAM Resource Information
                	**type**\:   :py:class:`ExternalTcamResources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes.Node.ExternalTcamResources>`
                
                .. attribute:: internal_tcam_resources
                
                	Internal TCAM Resource Information
                	**type**\:   :py:class:`InternalTcamResources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes.Node.InternalTcamResources>`
                
                

                """

                _prefix = 'fia-internal-tcam-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Controller.Dpa.Nodes.Node, self).__init__()

                    self.yang_name = "node"
                    self.yang_parent_name = "nodes"

                    self.node_name = YLeaf(YType.str, "node-name")

                    self.external_tcam_resources = Controller.Dpa.Nodes.Node.ExternalTcamResources()
                    self.external_tcam_resources.parent = self
                    self._children_name_map["external_tcam_resources"] = "external-tcam-resources"
                    self._children_yang_names.add("external-tcam-resources")

                    self.internal_tcam_resources = Controller.Dpa.Nodes.Node.InternalTcamResources()
                    self.internal_tcam_resources.parent = self
                    self._children_name_map["internal_tcam_resources"] = "internal-tcam-resources"
                    self._children_yang_names.add("internal-tcam-resources")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("node_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Controller.Dpa.Nodes.Node, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Controller.Dpa.Nodes.Node, self).__setattr__(name, value)


                class ExternalTcamResources(Entity):
                    """
                    External TCAM Resource Information
                    
                    .. attribute:: npu_tcam
                    
                    	npu tcam
                    	**type**\: list of    :py:class:`NpuTcam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam>`
                    
                    

                    """

                    _prefix = 'fia-internal-tcam-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Controller.Dpa.Nodes.Node.ExternalTcamResources, self).__init__()

                        self.yang_name = "external-tcam-resources"
                        self.yang_parent_name = "node"

                        self.npu_tcam = YList(self)

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
                                    super(Controller.Dpa.Nodes.Node.ExternalTcamResources, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Controller.Dpa.Nodes.Node.ExternalTcamResources, self).__setattr__(name, value)


                    class NpuTcam(Entity):
                        """
                        npu tcam
                        
                        .. attribute:: npu_id
                        
                        	npu id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: tcam_bank
                        
                        	tcam bank
                        	**type**\: list of    :py:class:`TcamBank <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam.TcamBank>`
                        
                        

                        """

                        _prefix = 'fia-internal-tcam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam, self).__init__()

                            self.yang_name = "npu-tcam"
                            self.yang_parent_name = "external-tcam-resources"

                            self.npu_id = YLeaf(YType.uint32, "npu-id")

                            self.tcam_bank = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("npu_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam, self).__setattr__(name, value)


                        class TcamBank(Entity):
                            """
                            tcam bank
                            
                            .. attribute:: bank_db
                            
                            	bank db
                            	**type**\: list of    :py:class:`BankDb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam.TcamBank.BankDb>`
                            
                            .. attribute:: bank_free_entries
                            
                            	bank free entries
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bank_id
                            
                            	bank id
                            	**type**\:  str
                            
                            .. attribute:: bank_inuse_entries
                            
                            	bank inuse entries
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bank_key_size
                            
                            	bank key size
                            	**type**\:  str
                            
                            .. attribute:: nof_dbs
                            
                            	nof dbs
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: owner
                            
                            	owner
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'fia-internal-tcam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam.TcamBank, self).__init__()

                                self.yang_name = "tcam-bank"
                                self.yang_parent_name = "npu-tcam"

                                self.bank_free_entries = YLeaf(YType.uint32, "bank-free-entries")

                                self.bank_id = YLeaf(YType.str, "bank-id")

                                self.bank_inuse_entries = YLeaf(YType.uint32, "bank-inuse-entries")

                                self.bank_key_size = YLeaf(YType.str, "bank-key-size")

                                self.nof_dbs = YLeaf(YType.uint32, "nof-dbs")

                                self.owner = YLeaf(YType.str, "owner")

                                self.bank_db = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bank_free_entries",
                                                "bank_id",
                                                "bank_inuse_entries",
                                                "bank_key_size",
                                                "nof_dbs",
                                                "owner") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam.TcamBank, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam.TcamBank, self).__setattr__(name, value)


                            class BankDb(Entity):
                                """
                                bank db
                                
                                .. attribute:: db_id
                                
                                	db id
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: db_inuse_entries
                                
                                	db inuse entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: db_prefix
                                
                                	db prefix
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'fia-internal-tcam-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam.TcamBank.BankDb, self).__init__()

                                    self.yang_name = "bank-db"
                                    self.yang_parent_name = "tcam-bank"

                                    self.db_id = YLeaf(YType.uint32, "db-id")

                                    self.db_inuse_entries = YLeaf(YType.uint32, "db-inuse-entries")

                                    self.db_prefix = YLeaf(YType.str, "db-prefix")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("db_id",
                                                    "db_inuse_entries",
                                                    "db_prefix") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam.TcamBank.BankDb, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam.TcamBank.BankDb, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.db_id.is_set or
                                        self.db_inuse_entries.is_set or
                                        self.db_prefix.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.db_id.yfilter != YFilter.not_set or
                                        self.db_inuse_entries.yfilter != YFilter.not_set or
                                        self.db_prefix.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "bank-db" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.db_id.is_set or self.db_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.db_id.get_name_leafdata())
                                    if (self.db_inuse_entries.is_set or self.db_inuse_entries.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.db_inuse_entries.get_name_leafdata())
                                    if (self.db_prefix.is_set or self.db_prefix.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.db_prefix.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "db-id" or name == "db-inuse-entries" or name == "db-prefix"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "db-id"):
                                        self.db_id = value
                                        self.db_id.value_namespace = name_space
                                        self.db_id.value_namespace_prefix = name_space_prefix
                                    if(value_path == "db-inuse-entries"):
                                        self.db_inuse_entries = value
                                        self.db_inuse_entries.value_namespace = name_space
                                        self.db_inuse_entries.value_namespace_prefix = name_space_prefix
                                    if(value_path == "db-prefix"):
                                        self.db_prefix = value
                                        self.db_prefix.value_namespace = name_space
                                        self.db_prefix.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.bank_db:
                                    if (c.has_data()):
                                        return True
                                return (
                                    self.bank_free_entries.is_set or
                                    self.bank_id.is_set or
                                    self.bank_inuse_entries.is_set or
                                    self.bank_key_size.is_set or
                                    self.nof_dbs.is_set or
                                    self.owner.is_set)

                            def has_operation(self):
                                for c in self.bank_db:
                                    if (c.has_operation()):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bank_free_entries.yfilter != YFilter.not_set or
                                    self.bank_id.yfilter != YFilter.not_set or
                                    self.bank_inuse_entries.yfilter != YFilter.not_set or
                                    self.bank_key_size.yfilter != YFilter.not_set or
                                    self.nof_dbs.yfilter != YFilter.not_set or
                                    self.owner.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "tcam-bank" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bank_free_entries.is_set or self.bank_free_entries.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bank_free_entries.get_name_leafdata())
                                if (self.bank_id.is_set or self.bank_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bank_id.get_name_leafdata())
                                if (self.bank_inuse_entries.is_set or self.bank_inuse_entries.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bank_inuse_entries.get_name_leafdata())
                                if (self.bank_key_size.is_set or self.bank_key_size.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bank_key_size.get_name_leafdata())
                                if (self.nof_dbs.is_set or self.nof_dbs.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.nof_dbs.get_name_leafdata())
                                if (self.owner.is_set or self.owner.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.owner.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "bank-db"):
                                    for c in self.bank_db:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam.TcamBank.BankDb()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.bank_db.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bank-db" or name == "bank-free-entries" or name == "bank-id" or name == "bank-inuse-entries" or name == "bank-key-size" or name == "nof-dbs" or name == "owner"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bank-free-entries"):
                                    self.bank_free_entries = value
                                    self.bank_free_entries.value_namespace = name_space
                                    self.bank_free_entries.value_namespace_prefix = name_space_prefix
                                if(value_path == "bank-id"):
                                    self.bank_id = value
                                    self.bank_id.value_namespace = name_space
                                    self.bank_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "bank-inuse-entries"):
                                    self.bank_inuse_entries = value
                                    self.bank_inuse_entries.value_namespace = name_space
                                    self.bank_inuse_entries.value_namespace_prefix = name_space_prefix
                                if(value_path == "bank-key-size"):
                                    self.bank_key_size = value
                                    self.bank_key_size.value_namespace = name_space
                                    self.bank_key_size.value_namespace_prefix = name_space_prefix
                                if(value_path == "nof-dbs"):
                                    self.nof_dbs = value
                                    self.nof_dbs.value_namespace = name_space
                                    self.nof_dbs.value_namespace_prefix = name_space_prefix
                                if(value_path == "owner"):
                                    self.owner = value
                                    self.owner.value_namespace = name_space
                                    self.owner.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.tcam_bank:
                                if (c.has_data()):
                                    return True
                            return self.npu_id.is_set

                        def has_operation(self):
                            for c in self.tcam_bank:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.npu_id.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "npu-tcam" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.npu_id.is_set or self.npu_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.npu_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "tcam-bank"):
                                for c in self.tcam_bank:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam.TcamBank()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.tcam_bank.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "tcam-bank" or name == "npu-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "npu-id"):
                                self.npu_id = value
                                self.npu_id.value_namespace = name_space
                                self.npu_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.npu_tcam:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.npu_tcam:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "external-tcam-resources" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "npu-tcam"):
                            for c in self.npu_tcam:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Controller.Dpa.Nodes.Node.ExternalTcamResources.NpuTcam()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.npu_tcam.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "npu-tcam"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class InternalTcamResources(Entity):
                    """
                    Internal TCAM Resource Information
                    
                    .. attribute:: npu_tcam
                    
                    	npu tcam
                    	**type**\: list of    :py:class:`NpuTcam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam>`
                    
                    

                    """

                    _prefix = 'fia-internal-tcam-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Controller.Dpa.Nodes.Node.InternalTcamResources, self).__init__()

                        self.yang_name = "internal-tcam-resources"
                        self.yang_parent_name = "node"

                        self.npu_tcam = YList(self)

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
                                    super(Controller.Dpa.Nodes.Node.InternalTcamResources, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Controller.Dpa.Nodes.Node.InternalTcamResources, self).__setattr__(name, value)


                    class NpuTcam(Entity):
                        """
                        npu tcam
                        
                        .. attribute:: npu_id
                        
                        	npu id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: tcam_bank
                        
                        	tcam bank
                        	**type**\: list of    :py:class:`TcamBank <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank>`
                        
                        

                        """

                        _prefix = 'fia-internal-tcam-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam, self).__init__()

                            self.yang_name = "npu-tcam"
                            self.yang_parent_name = "internal-tcam-resources"

                            self.npu_id = YLeaf(YType.uint32, "npu-id")

                            self.tcam_bank = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("npu_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam, self).__setattr__(name, value)


                        class TcamBank(Entity):
                            """
                            tcam bank
                            
                            .. attribute:: bank_db
                            
                            	bank db
                            	**type**\: list of    :py:class:`BankDb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper.Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank.BankDb>`
                            
                            .. attribute:: bank_free_entries
                            
                            	bank free entries
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bank_id
                            
                            	bank id
                            	**type**\:  str
                            
                            .. attribute:: bank_inuse_entries
                            
                            	bank inuse entries
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bank_key_size
                            
                            	bank key size
                            	**type**\:  str
                            
                            .. attribute:: nof_dbs
                            
                            	nof dbs
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: owner
                            
                            	owner
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'fia-internal-tcam-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank, self).__init__()

                                self.yang_name = "tcam-bank"
                                self.yang_parent_name = "npu-tcam"

                                self.bank_free_entries = YLeaf(YType.uint32, "bank-free-entries")

                                self.bank_id = YLeaf(YType.str, "bank-id")

                                self.bank_inuse_entries = YLeaf(YType.uint32, "bank-inuse-entries")

                                self.bank_key_size = YLeaf(YType.str, "bank-key-size")

                                self.nof_dbs = YLeaf(YType.uint32, "nof-dbs")

                                self.owner = YLeaf(YType.str, "owner")

                                self.bank_db = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("bank_free_entries",
                                                "bank_id",
                                                "bank_inuse_entries",
                                                "bank_key_size",
                                                "nof_dbs",
                                                "owner") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank, self).__setattr__(name, value)


                            class BankDb(Entity):
                                """
                                bank db
                                
                                .. attribute:: db_id
                                
                                	db id
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: db_inuse_entries
                                
                                	db inuse entries
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: db_prefix
                                
                                	db prefix
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'fia-internal-tcam-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank.BankDb, self).__init__()

                                    self.yang_name = "bank-db"
                                    self.yang_parent_name = "tcam-bank"

                                    self.db_id = YLeaf(YType.uint32, "db-id")

                                    self.db_inuse_entries = YLeaf(YType.uint32, "db-inuse-entries")

                                    self.db_prefix = YLeaf(YType.str, "db-prefix")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("db_id",
                                                    "db_inuse_entries",
                                                    "db_prefix") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank.BankDb, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank.BankDb, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.db_id.is_set or
                                        self.db_inuse_entries.is_set or
                                        self.db_prefix.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.db_id.yfilter != YFilter.not_set or
                                        self.db_inuse_entries.yfilter != YFilter.not_set or
                                        self.db_prefix.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "bank-db" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.db_id.is_set or self.db_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.db_id.get_name_leafdata())
                                    if (self.db_inuse_entries.is_set or self.db_inuse_entries.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.db_inuse_entries.get_name_leafdata())
                                    if (self.db_prefix.is_set or self.db_prefix.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.db_prefix.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "db-id" or name == "db-inuse-entries" or name == "db-prefix"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "db-id"):
                                        self.db_id = value
                                        self.db_id.value_namespace = name_space
                                        self.db_id.value_namespace_prefix = name_space_prefix
                                    if(value_path == "db-inuse-entries"):
                                        self.db_inuse_entries = value
                                        self.db_inuse_entries.value_namespace = name_space
                                        self.db_inuse_entries.value_namespace_prefix = name_space_prefix
                                    if(value_path == "db-prefix"):
                                        self.db_prefix = value
                                        self.db_prefix.value_namespace = name_space
                                        self.db_prefix.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.bank_db:
                                    if (c.has_data()):
                                        return True
                                return (
                                    self.bank_free_entries.is_set or
                                    self.bank_id.is_set or
                                    self.bank_inuse_entries.is_set or
                                    self.bank_key_size.is_set or
                                    self.nof_dbs.is_set or
                                    self.owner.is_set)

                            def has_operation(self):
                                for c in self.bank_db:
                                    if (c.has_operation()):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.bank_free_entries.yfilter != YFilter.not_set or
                                    self.bank_id.yfilter != YFilter.not_set or
                                    self.bank_inuse_entries.yfilter != YFilter.not_set or
                                    self.bank_key_size.yfilter != YFilter.not_set or
                                    self.nof_dbs.yfilter != YFilter.not_set or
                                    self.owner.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "tcam-bank" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.bank_free_entries.is_set or self.bank_free_entries.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bank_free_entries.get_name_leafdata())
                                if (self.bank_id.is_set or self.bank_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bank_id.get_name_leafdata())
                                if (self.bank_inuse_entries.is_set or self.bank_inuse_entries.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bank_inuse_entries.get_name_leafdata())
                                if (self.bank_key_size.is_set or self.bank_key_size.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bank_key_size.get_name_leafdata())
                                if (self.nof_dbs.is_set or self.nof_dbs.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.nof_dbs.get_name_leafdata())
                                if (self.owner.is_set or self.owner.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.owner.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "bank-db"):
                                    for c in self.bank_db:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank.BankDb()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.bank_db.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bank-db" or name == "bank-free-entries" or name == "bank-id" or name == "bank-inuse-entries" or name == "bank-key-size" or name == "nof-dbs" or name == "owner"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "bank-free-entries"):
                                    self.bank_free_entries = value
                                    self.bank_free_entries.value_namespace = name_space
                                    self.bank_free_entries.value_namespace_prefix = name_space_prefix
                                if(value_path == "bank-id"):
                                    self.bank_id = value
                                    self.bank_id.value_namespace = name_space
                                    self.bank_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "bank-inuse-entries"):
                                    self.bank_inuse_entries = value
                                    self.bank_inuse_entries.value_namespace = name_space
                                    self.bank_inuse_entries.value_namespace_prefix = name_space_prefix
                                if(value_path == "bank-key-size"):
                                    self.bank_key_size = value
                                    self.bank_key_size.value_namespace = name_space
                                    self.bank_key_size.value_namespace_prefix = name_space_prefix
                                if(value_path == "nof-dbs"):
                                    self.nof_dbs = value
                                    self.nof_dbs.value_namespace = name_space
                                    self.nof_dbs.value_namespace_prefix = name_space_prefix
                                if(value_path == "owner"):
                                    self.owner = value
                                    self.owner.value_namespace = name_space
                                    self.owner.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.tcam_bank:
                                if (c.has_data()):
                                    return True
                            return self.npu_id.is_set

                        def has_operation(self):
                            for c in self.tcam_bank:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.npu_id.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "npu-tcam" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.npu_id.is_set or self.npu_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.npu_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "tcam-bank"):
                                for c in self.tcam_bank:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.tcam_bank.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "tcam-bank" or name == "npu-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "npu-id"):
                                self.npu_id = value
                                self.npu_id.value_namespace = name_space
                                self.npu_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.npu_tcam:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.npu_tcam:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "internal-tcam-resources" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "npu-tcam"):
                            for c in self.npu_tcam:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.npu_tcam.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "npu-tcam"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.node_name.is_set or
                        (self.external_tcam_resources is not None and self.external_tcam_resources.has_data()) or
                        (self.internal_tcam_resources is not None and self.internal_tcam_resources.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.node_name.yfilter != YFilter.not_set or
                        (self.external_tcam_resources is not None and self.external_tcam_resources.has_operation()) or
                        (self.internal_tcam_resources is not None and self.internal_tcam_resources.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-fia-internal-tcam-oper:controller/dpa/nodes/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.node_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "external-tcam-resources"):
                        if (self.external_tcam_resources is None):
                            self.external_tcam_resources = Controller.Dpa.Nodes.Node.ExternalTcamResources()
                            self.external_tcam_resources.parent = self
                            self._children_name_map["external_tcam_resources"] = "external-tcam-resources"
                        return self.external_tcam_resources

                    if (child_yang_name == "internal-tcam-resources"):
                        if (self.internal_tcam_resources is None):
                            self.internal_tcam_resources = Controller.Dpa.Nodes.Node.InternalTcamResources()
                            self.internal_tcam_resources.parent = self
                            self._children_name_map["internal_tcam_resources"] = "internal-tcam-resources"
                        return self.internal_tcam_resources

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "external-tcam-resources" or name == "internal-tcam-resources" or name == "node-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "node-name"):
                        self.node_name = value
                        self.node_name.value_namespace = name_space
                        self.node_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.node:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.node:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nodes" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-fia-internal-tcam-oper:controller/dpa/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "node"):
                    for c in self.node:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Controller.Dpa.Nodes.Node()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.node.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "node"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.nodes is not None and self.nodes.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.nodes is not None and self.nodes.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dpa" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-fia-internal-tcam-oper:controller/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "nodes"):
                if (self.nodes is None):
                    self.nodes = Controller.Dpa.Nodes()
                    self.nodes.parent = self
                    self._children_name_map["nodes"] = "nodes"
                return self.nodes

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "nodes"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.dpa is not None and self.dpa.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.dpa is not None and self.dpa.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-fia-internal-tcam-oper:controller" + path_buffer

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

        if (child_yang_name == "dpa"):
            if (self.dpa is None):
                self.dpa = Controller.Dpa()
                self.dpa.parent = self
                self._children_name_map["dpa"] = "dpa"
            return self.dpa

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "dpa"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Controller()
        return self._top_entity


""" CISCO_IETF_MPLS_TE_EXT_STD_03_MIB 

Copyright (c) 2012 IETF Trust and the persons identified
as the document authors.  All rights reserved.
This MIB module contains generic object definitions for
MPLS Traffic Engineering in transport networks.This module is a
cisco\-ized version of the IETF draft\:
draft\-ietf\-mpls\-tp\-te\-mib\-03

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoIetfMplsTeExtStd03Mib(Entity):
    """
    
    
    .. attribute:: cmplsnodeconfigtable
    
    	This table allows the administrator to map a node or LSR Identifier (IP compatible [Global\_Node\_ID] or ICC) with a local identifier.   This table is created to reuse the existing mplsTunnelTable for MPLS based transport network tunnels also. Since the MPLS tunnel's Ingress/Egress LSR identifiers' size (Unsigned32) value is not compatible for MPLS\-TP tunnel i.e. Global\_Node\_Id of size 8 bytes and ICC of size 6 bytes, there exists a need to map the Global\_Node\_ID or ICC with the local identifier of size 4 bytes (Unsigned32) value in order to index (Ingress/Egress LSR identifier) the existing mplsTunnelTable
    	**type**\:   :py:class:`Cmplsnodeconfigtable <ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CiscoIetfMplsTeExtStd03Mib.Cmplsnodeconfigtable>`
    
    .. attribute:: cmplsnodeiccmaptable
    
    	This read\-only table allows the administrator to retrieve the local identifier for a given ICC operator in an ICC operator environment.  This table MAY be used in on\-demand and/or proactive OAM operations to get the Ingress/Egress LSR identifier (Local Identifier) from Src\-ICC or Dst\-ICC and the Ingress and Egress LSR identifiers are used to retrieve the tunnel entry. This table returns nothing when the associated entry is not defined in mplsNodeConfigTable
    	**type**\:   :py:class:`Cmplsnodeiccmaptable <ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CiscoIetfMplsTeExtStd03Mib.Cmplsnodeiccmaptable>`
    
    .. attribute:: cmplsnodeipmaptable
    
    	This read\-only table allows the administrator to retrieve the local identifier for a given Global\_Node\_ID in an IP compatible operator environment.  This table MAY be used in on\-demand and/or proactive OAM operations to get the Ingress/Egress LSR identifier (Local Identifier) from Src\-Global\_Node\_ID or Dst\-Global\_Node\_ID and the Ingress and Egress LSR identifiers are used to retrieve the tunnel entry.  This table returns nothing when the associated entry is not defined in mplsNodeConfigTable
    	**type**\:   :py:class:`Cmplsnodeipmaptable <ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CiscoIetfMplsTeExtStd03Mib.Cmplsnodeipmaptable>`
    
    .. attribute:: cmplstunnelexttable
    
    	This table represents MPLS\-TP specific extensions to mplsTunnelTable.  As per MPLS\-TP Identifiers [RFC6370], LSP\_ID for IP based co\-routed bidirectional tunnel,  A1\-{Global\_ID\:\:Node\_ID\:\:Tunnel\_Num}\:\:Z9\-{Global\_ID\:\: Node\_ID\:\:Tunnel\_Num}\:\:LSP\_Num  LSP\_ID for IP based associated bidirectional tunnel, A1\-{Global\_ID\:\:Node\_ID\:\:Tunnel\_Num\:\:LSP\_Num}\:\: Z9\-{Global\_ID\:\:Node\_ID\:\:Tunnel\_Num\:\:LSP\_Num}  mplsTunnelTable is reused for forming the LSP\_ID as follows,  Source Tunnel\_Num is mapped with mplsTunnelIndex, Source Node\_ID is mapped with mplsTunnelIngressLSRId, Destination Node\_ID is mapped with mplsTunnelEgressLSRId LSP\_Num is mapped with mplsTunnelInstance.  Source Global\_Node\_ID and/or ICC and Destination Global\_Node\_ID and/or ICC are maintained in the mplsNodeConfigTable and mplsNodeConfigLocalId is used to create an entry in mplsTunnelTable
    	**type**\:   :py:class:`Cmplstunnelexttable <ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CiscoIetfMplsTeExtStd03Mib.Cmplstunnelexttable>`
    
    .. attribute:: cmplstunnelreverseperftable
    
    	This table extends the mplsTunnelTable to provide per\-tunnel packet performance information for the reverse direction of a bidirectional tunnel.  It can be seen as supplementing the mplsTunnelPerfTable, which augments the mplsTunnelTable.  For links that do not transport packets, these packet counters cannot be maintained.  For such links, attempts to read the objects in this table will return noSuchInstance
    	**type**\:   :py:class:`Cmplstunnelreverseperftable <ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CiscoIetfMplsTeExtStd03Mib.Cmplstunnelreverseperftable>`
    
    

    """

    _prefix = 'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'
    _revision = '2012-06-06'

    def __init__(self):
        super(CiscoIetfMplsTeExtStd03Mib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB"
        self.yang_parent_name = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB"

        self.cmplsnodeconfigtable = CiscoIetfMplsTeExtStd03Mib.Cmplsnodeconfigtable()
        self.cmplsnodeconfigtable.parent = self
        self._children_name_map["cmplsnodeconfigtable"] = "cmplsNodeConfigTable"
        self._children_yang_names.add("cmplsNodeConfigTable")

        self.cmplsnodeiccmaptable = CiscoIetfMplsTeExtStd03Mib.Cmplsnodeiccmaptable()
        self.cmplsnodeiccmaptable.parent = self
        self._children_name_map["cmplsnodeiccmaptable"] = "cmplsNodeIccMapTable"
        self._children_yang_names.add("cmplsNodeIccMapTable")

        self.cmplsnodeipmaptable = CiscoIetfMplsTeExtStd03Mib.Cmplsnodeipmaptable()
        self.cmplsnodeipmaptable.parent = self
        self._children_name_map["cmplsnodeipmaptable"] = "cmplsNodeIpMapTable"
        self._children_yang_names.add("cmplsNodeIpMapTable")

        self.cmplstunnelexttable = CiscoIetfMplsTeExtStd03Mib.Cmplstunnelexttable()
        self.cmplstunnelexttable.parent = self
        self._children_name_map["cmplstunnelexttable"] = "cmplsTunnelExtTable"
        self._children_yang_names.add("cmplsTunnelExtTable")

        self.cmplstunnelreverseperftable = CiscoIetfMplsTeExtStd03Mib.Cmplstunnelreverseperftable()
        self.cmplstunnelreverseperftable.parent = self
        self._children_name_map["cmplstunnelreverseperftable"] = "cmplsTunnelReversePerfTable"
        self._children_yang_names.add("cmplsTunnelReversePerfTable")


    class Cmplsnodeconfigtable(Entity):
        """
        This table allows the administrator to map a node or
        LSR Identifier (IP compatible [Global\_Node\_ID] or ICC)
        with a local identifier.
        
        
        This table is created to reuse the existing
        mplsTunnelTable for MPLS based transport network
        tunnels also.
        Since the MPLS tunnel's Ingress/Egress LSR identifiers'
        size (Unsigned32) value is not compatible for
        MPLS\-TP tunnel i.e. Global\_Node\_Id of size 8 bytes and
        ICC of size 6 bytes, there exists a need to map the
        Global\_Node\_ID or ICC with the local identifier of size
        4 bytes (Unsigned32) value in order
        to index (Ingress/Egress LSR identifier)
        the existing mplsTunnelTable.
        
        .. attribute:: cmplsnodeconfigentry
        
        	An entry in this table represents a mapping identification for the operator or service provider with node or LSR.  As per [RFC6370], this mapping is  represented as Global\_Node\_ID or ICC.  Note\: Each entry in this table should have a unique Global\_ID and Node\_ID combination
        	**type**\: list of    :py:class:`Cmplsnodeconfigentry <ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CiscoIetfMplsTeExtStd03Mib.Cmplsnodeconfigtable.Cmplsnodeconfigentry>`
        
        

        """

        _prefix = 'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'
        _revision = '2012-06-06'

        def __init__(self):
            super(CiscoIetfMplsTeExtStd03Mib.Cmplsnodeconfigtable, self).__init__()

            self.yang_name = "cmplsNodeConfigTable"
            self.yang_parent_name = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB"

            self.cmplsnodeconfigentry = YList(self)

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
                        super(CiscoIetfMplsTeExtStd03Mib.Cmplsnodeconfigtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfMplsTeExtStd03Mib.Cmplsnodeconfigtable, self).__setattr__(name, value)


        class Cmplsnodeconfigentry(Entity):
            """
            An entry in this table represents a mapping
            identification for the operator or service provider
            with node or LSR.
            
            As per [RFC6370], this mapping is
            
            represented as Global\_Node\_ID or ICC.
            
            Note\: Each entry in this table should have a unique
            Global\_ID and Node\_ID combination.
            
            .. attribute:: cmplsnodeconfiglocalid  <key>
            
            	This object allows the administrator to assign a unique local identifier to map Global\_Node\_ID or ICC
            	**type**\:  int
            
            	**range:** 1..16777215
            
            .. attribute:: cmplsnodeconfigglobalid
            
            	This object indicates the Global Operator Identifier. This object value should be zero when mplsNodeConfigIccId is configured with non\-null value
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: cmplsnodeconfigiccid
            
            	This object allows the operator or service provider to configure a unique MPLS\-TP ITU\-T Carrier Code (ICC) either for Ingress ID or Egress ID.  This object value should be zero when mplsNodeConfigGlobalId and mplsNodeConfigNodeId are assigned with non\-zero value
            	**type**\:  str
            
            	**length:** 1..6
            
            .. attribute:: cmplsnodeconfignodeid
            
            	This object indicates the Node\_ID within the operator. This object value should be zero when mplsNodeConfigIccId is configured with non\-null value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsnodeconfigrowstatus
            
            	This object allows the administrator to create, modify, and/or delete a row in this table
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cmplsnodeconfigstoragetype
            
            	This variable indicates the storage type for this object. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'
            _revision = '2012-06-06'

            def __init__(self):
                super(CiscoIetfMplsTeExtStd03Mib.Cmplsnodeconfigtable.Cmplsnodeconfigentry, self).__init__()

                self.yang_name = "cmplsNodeConfigEntry"
                self.yang_parent_name = "cmplsNodeConfigTable"

                self.cmplsnodeconfiglocalid = YLeaf(YType.uint32, "cmplsNodeConfigLocalId")

                self.cmplsnodeconfigglobalid = YLeaf(YType.str, "cmplsNodeConfigGlobalId")

                self.cmplsnodeconfigiccid = YLeaf(YType.str, "cmplsNodeConfigIccId")

                self.cmplsnodeconfignodeid = YLeaf(YType.uint32, "cmplsNodeConfigNodeId")

                self.cmplsnodeconfigrowstatus = YLeaf(YType.enumeration, "cmplsNodeConfigRowStatus")

                self.cmplsnodeconfigstoragetype = YLeaf(YType.enumeration, "cmplsNodeConfigStorageType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cmplsnodeconfiglocalid",
                                "cmplsnodeconfigglobalid",
                                "cmplsnodeconfigiccid",
                                "cmplsnodeconfignodeid",
                                "cmplsnodeconfigrowstatus",
                                "cmplsnodeconfigstoragetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfMplsTeExtStd03Mib.Cmplsnodeconfigtable.Cmplsnodeconfigentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfMplsTeExtStd03Mib.Cmplsnodeconfigtable.Cmplsnodeconfigentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cmplsnodeconfiglocalid.is_set or
                    self.cmplsnodeconfigglobalid.is_set or
                    self.cmplsnodeconfigiccid.is_set or
                    self.cmplsnodeconfignodeid.is_set or
                    self.cmplsnodeconfigrowstatus.is_set or
                    self.cmplsnodeconfigstoragetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cmplsnodeconfiglocalid.yfilter != YFilter.not_set or
                    self.cmplsnodeconfigglobalid.yfilter != YFilter.not_set or
                    self.cmplsnodeconfigiccid.yfilter != YFilter.not_set or
                    self.cmplsnodeconfignodeid.yfilter != YFilter.not_set or
                    self.cmplsnodeconfigrowstatus.yfilter != YFilter.not_set or
                    self.cmplsnodeconfigstoragetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cmplsNodeConfigEntry" + "[cmplsNodeConfigLocalId='" + self.cmplsnodeconfiglocalid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/cmplsNodeConfigTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cmplsnodeconfiglocalid.is_set or self.cmplsnodeconfiglocalid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsnodeconfiglocalid.get_name_leafdata())
                if (self.cmplsnodeconfigglobalid.is_set or self.cmplsnodeconfigglobalid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsnodeconfigglobalid.get_name_leafdata())
                if (self.cmplsnodeconfigiccid.is_set or self.cmplsnodeconfigiccid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsnodeconfigiccid.get_name_leafdata())
                if (self.cmplsnodeconfignodeid.is_set or self.cmplsnodeconfignodeid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsnodeconfignodeid.get_name_leafdata())
                if (self.cmplsnodeconfigrowstatus.is_set or self.cmplsnodeconfigrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsnodeconfigrowstatus.get_name_leafdata())
                if (self.cmplsnodeconfigstoragetype.is_set or self.cmplsnodeconfigstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsnodeconfigstoragetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cmplsNodeConfigLocalId" or name == "cmplsNodeConfigGlobalId" or name == "cmplsNodeConfigIccId" or name == "cmplsNodeConfigNodeId" or name == "cmplsNodeConfigRowStatus" or name == "cmplsNodeConfigStorageType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cmplsNodeConfigLocalId"):
                    self.cmplsnodeconfiglocalid = value
                    self.cmplsnodeconfiglocalid.value_namespace = name_space
                    self.cmplsnodeconfiglocalid.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsNodeConfigGlobalId"):
                    self.cmplsnodeconfigglobalid = value
                    self.cmplsnodeconfigglobalid.value_namespace = name_space
                    self.cmplsnodeconfigglobalid.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsNodeConfigIccId"):
                    self.cmplsnodeconfigiccid = value
                    self.cmplsnodeconfigiccid.value_namespace = name_space
                    self.cmplsnodeconfigiccid.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsNodeConfigNodeId"):
                    self.cmplsnodeconfignodeid = value
                    self.cmplsnodeconfignodeid.value_namespace = name_space
                    self.cmplsnodeconfignodeid.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsNodeConfigRowStatus"):
                    self.cmplsnodeconfigrowstatus = value
                    self.cmplsnodeconfigrowstatus.value_namespace = name_space
                    self.cmplsnodeconfigrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsNodeConfigStorageType"):
                    self.cmplsnodeconfigstoragetype = value
                    self.cmplsnodeconfigstoragetype.value_namespace = name_space
                    self.cmplsnodeconfigstoragetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cmplsnodeconfigentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cmplsnodeconfigentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cmplsNodeConfigTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cmplsNodeConfigEntry"):
                for c in self.cmplsnodeconfigentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfMplsTeExtStd03Mib.Cmplsnodeconfigtable.Cmplsnodeconfigentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cmplsnodeconfigentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cmplsNodeConfigEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cmplsnodeipmaptable(Entity):
        """
        This read\-only table allows the administrator to retrieve
        the local identifier for a given Global\_Node\_ID in an IP
        compatible operator environment.
        
        This table MAY be used in on\-demand and/or proactive
        OAM operations to get the Ingress/Egress LSR identifier
        (Local Identifier) from Src\-Global\_Node\_ID
        or Dst\-Global\_Node\_ID and the Ingress and Egress LSR
        identifiers are used to retrieve the tunnel entry.
        
        This table returns nothing when the associated entry
        is not defined in mplsNodeConfigTable.
        
        .. attribute:: cmplsnodeipmapentry
        
        	An entry in this table represents a mapping of Global\_Node\_ID with the local identifier.  An entry in this table is created automatically when the Local identifier is associated with Global\_ID and Node\_Id in the mplsNodeConfigTable. Note\: Each entry in this table should have a unique Global\_ID and Node\_ID combination
        	**type**\: list of    :py:class:`Cmplsnodeipmapentry <ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CiscoIetfMplsTeExtStd03Mib.Cmplsnodeipmaptable.Cmplsnodeipmapentry>`
        
        

        """

        _prefix = 'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'
        _revision = '2012-06-06'

        def __init__(self):
            super(CiscoIetfMplsTeExtStd03Mib.Cmplsnodeipmaptable, self).__init__()

            self.yang_name = "cmplsNodeIpMapTable"
            self.yang_parent_name = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB"

            self.cmplsnodeipmapentry = YList(self)

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
                        super(CiscoIetfMplsTeExtStd03Mib.Cmplsnodeipmaptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfMplsTeExtStd03Mib.Cmplsnodeipmaptable, self).__setattr__(name, value)


        class Cmplsnodeipmapentry(Entity):
            """
            An entry in this table represents a mapping of
            Global\_Node\_ID with the local identifier.
            
            An entry in this table is created automatically when
            the Local identifier is associated with Global\_ID and
            Node\_Id in the mplsNodeConfigTable.
            Note\: Each entry in this table should have a unique
            Global\_ID and Node\_ID combination.
            
            .. attribute:: cmplsnodeipmapglobalid  <key>
            
            	This object indicates the Global\_ID
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: cmplsnodeipmapnodeid  <key>
            
            	This object indicates the Node\_ID within the operator
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsnodeipmaplocalid
            
            	This object contains an IP compatible local identifier which is defined in mplsNodeConfigTable
            	**type**\:  int
            
            	**range:** 1..16777215
            
            

            """

            _prefix = 'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'
            _revision = '2012-06-06'

            def __init__(self):
                super(CiscoIetfMplsTeExtStd03Mib.Cmplsnodeipmaptable.Cmplsnodeipmapentry, self).__init__()

                self.yang_name = "cmplsNodeIpMapEntry"
                self.yang_parent_name = "cmplsNodeIpMapTable"

                self.cmplsnodeipmapglobalid = YLeaf(YType.str, "cmplsNodeIpMapGlobalId")

                self.cmplsnodeipmapnodeid = YLeaf(YType.uint32, "cmplsNodeIpMapNodeId")

                self.cmplsnodeipmaplocalid = YLeaf(YType.uint32, "cmplsNodeIpMapLocalId")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cmplsnodeipmapglobalid",
                                "cmplsnodeipmapnodeid",
                                "cmplsnodeipmaplocalid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfMplsTeExtStd03Mib.Cmplsnodeipmaptable.Cmplsnodeipmapentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfMplsTeExtStd03Mib.Cmplsnodeipmaptable.Cmplsnodeipmapentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cmplsnodeipmapglobalid.is_set or
                    self.cmplsnodeipmapnodeid.is_set or
                    self.cmplsnodeipmaplocalid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cmplsnodeipmapglobalid.yfilter != YFilter.not_set or
                    self.cmplsnodeipmapnodeid.yfilter != YFilter.not_set or
                    self.cmplsnodeipmaplocalid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cmplsNodeIpMapEntry" + "[cmplsNodeIpMapGlobalId='" + self.cmplsnodeipmapglobalid.get() + "']" + "[cmplsNodeIpMapNodeId='" + self.cmplsnodeipmapnodeid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/cmplsNodeIpMapTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cmplsnodeipmapglobalid.is_set or self.cmplsnodeipmapglobalid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsnodeipmapglobalid.get_name_leafdata())
                if (self.cmplsnodeipmapnodeid.is_set or self.cmplsnodeipmapnodeid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsnodeipmapnodeid.get_name_leafdata())
                if (self.cmplsnodeipmaplocalid.is_set or self.cmplsnodeipmaplocalid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsnodeipmaplocalid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cmplsNodeIpMapGlobalId" or name == "cmplsNodeIpMapNodeId" or name == "cmplsNodeIpMapLocalId"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cmplsNodeIpMapGlobalId"):
                    self.cmplsnodeipmapglobalid = value
                    self.cmplsnodeipmapglobalid.value_namespace = name_space
                    self.cmplsnodeipmapglobalid.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsNodeIpMapNodeId"):
                    self.cmplsnodeipmapnodeid = value
                    self.cmplsnodeipmapnodeid.value_namespace = name_space
                    self.cmplsnodeipmapnodeid.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsNodeIpMapLocalId"):
                    self.cmplsnodeipmaplocalid = value
                    self.cmplsnodeipmaplocalid.value_namespace = name_space
                    self.cmplsnodeipmaplocalid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cmplsnodeipmapentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cmplsnodeipmapentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cmplsNodeIpMapTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cmplsNodeIpMapEntry"):
                for c in self.cmplsnodeipmapentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfMplsTeExtStd03Mib.Cmplsnodeipmaptable.Cmplsnodeipmapentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cmplsnodeipmapentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cmplsNodeIpMapEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cmplsnodeiccmaptable(Entity):
        """
        This read\-only table allows the administrator to retrieve
        the local identifier for a given ICC operator in an ICC
        operator environment.
        
        This table MAY be used in on\-demand and/or proactive
        OAM operations to get the Ingress/Egress LSR
        identifier (Local Identifier) from Src\-ICC
        or Dst\-ICC and the Ingress and Egress LSR
        identifiers are used to retrieve the tunnel entry.
        This table returns nothing when the associated entry
        is not defined in mplsNodeConfigTable.
        
        .. attribute:: cmplsnodeiccmapentry
        
        	An entry in this table represents a mapping of ICC with the local identifier.  An entry in this table is created automatically when the Local identifier is associated with ICC in the mplsNodeConfigTable
        	**type**\: list of    :py:class:`Cmplsnodeiccmapentry <ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CiscoIetfMplsTeExtStd03Mib.Cmplsnodeiccmaptable.Cmplsnodeiccmapentry>`
        
        

        """

        _prefix = 'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'
        _revision = '2012-06-06'

        def __init__(self):
            super(CiscoIetfMplsTeExtStd03Mib.Cmplsnodeiccmaptable, self).__init__()

            self.yang_name = "cmplsNodeIccMapTable"
            self.yang_parent_name = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB"

            self.cmplsnodeiccmapentry = YList(self)

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
                        super(CiscoIetfMplsTeExtStd03Mib.Cmplsnodeiccmaptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfMplsTeExtStd03Mib.Cmplsnodeiccmaptable, self).__setattr__(name, value)


        class Cmplsnodeiccmapentry(Entity):
            """
            An entry in this table represents a mapping of ICC with
            the local identifier.
            
            An entry in this table is created automatically when
            the Local identifier is associated with ICC in
            the mplsNodeConfigTable.
            
            .. attribute:: cmplsnodeiccmapiccid  <key>
            
            	This object allows the operator or service provider to configure a unique MPLS\-TP ITU\-T Carrier Code (ICC) either for Ingress or Egress LSR ID.  The ICC is a string of one to six characters, each character being either alphabetic (i.e.  A\-Z) or numeric (i.e. 0\-9) characters. Alphabetic characters in the ICC should be represented with upper case letters
            	**type**\:  str
            
            	**length:** 1..6
            
            .. attribute:: cmplsnodeiccmaplocalid
            
            	This object contains an ICC based local identifier which is defined in mplsNodeConfigTable
            	**type**\:  int
            
            	**range:** 1..16777215
            
            

            """

            _prefix = 'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'
            _revision = '2012-06-06'

            def __init__(self):
                super(CiscoIetfMplsTeExtStd03Mib.Cmplsnodeiccmaptable.Cmplsnodeiccmapentry, self).__init__()

                self.yang_name = "cmplsNodeIccMapEntry"
                self.yang_parent_name = "cmplsNodeIccMapTable"

                self.cmplsnodeiccmapiccid = YLeaf(YType.str, "cmplsNodeIccMapIccId")

                self.cmplsnodeiccmaplocalid = YLeaf(YType.uint32, "cmplsNodeIccMapLocalId")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cmplsnodeiccmapiccid",
                                "cmplsnodeiccmaplocalid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfMplsTeExtStd03Mib.Cmplsnodeiccmaptable.Cmplsnodeiccmapentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfMplsTeExtStd03Mib.Cmplsnodeiccmaptable.Cmplsnodeiccmapentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cmplsnodeiccmapiccid.is_set or
                    self.cmplsnodeiccmaplocalid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cmplsnodeiccmapiccid.yfilter != YFilter.not_set or
                    self.cmplsnodeiccmaplocalid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cmplsNodeIccMapEntry" + "[cmplsNodeIccMapIccId='" + self.cmplsnodeiccmapiccid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/cmplsNodeIccMapTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cmplsnodeiccmapiccid.is_set or self.cmplsnodeiccmapiccid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsnodeiccmapiccid.get_name_leafdata())
                if (self.cmplsnodeiccmaplocalid.is_set or self.cmplsnodeiccmaplocalid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsnodeiccmaplocalid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cmplsNodeIccMapIccId" or name == "cmplsNodeIccMapLocalId"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cmplsNodeIccMapIccId"):
                    self.cmplsnodeiccmapiccid = value
                    self.cmplsnodeiccmapiccid.value_namespace = name_space
                    self.cmplsnodeiccmapiccid.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsNodeIccMapLocalId"):
                    self.cmplsnodeiccmaplocalid = value
                    self.cmplsnodeiccmaplocalid.value_namespace = name_space
                    self.cmplsnodeiccmaplocalid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cmplsnodeiccmapentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cmplsnodeiccmapentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cmplsNodeIccMapTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cmplsNodeIccMapEntry"):
                for c in self.cmplsnodeiccmapentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfMplsTeExtStd03Mib.Cmplsnodeiccmaptable.Cmplsnodeiccmapentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cmplsnodeiccmapentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cmplsNodeIccMapEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cmplstunnelexttable(Entity):
        """
        This table represents MPLS\-TP specific extensions to
        mplsTunnelTable.
        
        As per MPLS\-TP Identifiers [RFC6370], LSP\_ID for IP based
        co\-routed bidirectional tunnel,
        
        A1\-{Global\_ID\:\:Node\_ID\:\:Tunnel\_Num}\:\:Z9\-{Global\_ID\:\:
        Node\_ID\:\:Tunnel\_Num}\:\:LSP\_Num
        
        LSP\_ID for IP based associated bidirectional tunnel,
        A1\-{Global\_ID\:\:Node\_ID\:\:Tunnel\_Num\:\:LSP\_Num}\:\:
        Z9\-{Global\_ID\:\:Node\_ID\:\:Tunnel\_Num\:\:LSP\_Num}
        
        mplsTunnelTable is reused for forming the LSP\_ID
        as follows,
        
        Source Tunnel\_Num is mapped with mplsTunnelIndex,
        Source Node\_ID is mapped with
        mplsTunnelIngressLSRId, Destination Node\_ID is
        mapped with mplsTunnelEgressLSRId LSP\_Num is mapped with
        mplsTunnelInstance.
        
        Source Global\_Node\_ID and/or ICC and Destination
        Global\_Node\_ID and/or ICC are maintained in the
        mplsNodeConfigTable and mplsNodeConfigLocalId is
        used to create an entry in mplsTunnelTable.
        
        .. attribute:: cmplstunnelextentry
        
        	An entry in this table represents MPLS\-TP specific additional tunnel configurations
        	**type**\: list of    :py:class:`Cmplstunnelextentry <ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CiscoIetfMplsTeExtStd03Mib.Cmplstunnelexttable.Cmplstunnelextentry>`
        
        

        """

        _prefix = 'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'
        _revision = '2012-06-06'

        def __init__(self):
            super(CiscoIetfMplsTeExtStd03Mib.Cmplstunnelexttable, self).__init__()

            self.yang_name = "cmplsTunnelExtTable"
            self.yang_parent_name = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB"

            self.cmplstunnelextentry = YList(self)

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
                        super(CiscoIetfMplsTeExtStd03Mib.Cmplstunnelexttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfMplsTeExtStd03Mib.Cmplstunnelexttable, self).__setattr__(name, value)


        class Cmplstunnelextentry(Entity):
            """
            An entry in this table represents MPLS\-TP
            specific additional tunnel configurations.
            
            .. attribute:: mplstunnelindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`mplstunnelindex <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunneltable.Mplstunnelentry>`
            
            .. attribute:: mplstunnelinstance  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`mplstunnelinstance <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunneltable.Mplstunnelentry>`
            
            .. attribute:: mplstunnelingresslsrid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`mplstunnelingresslsrid <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunneltable.Mplstunnelentry>`
            
            .. attribute:: mplstunnelegresslsrid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`mplstunnelegresslsrid <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunneltable.Mplstunnelentry>`
            
            .. attribute:: cmplstunnelextdesttnlindex
            
            	This object is applicable only for the bidirectional tunnel that has the forward and reverse LSPs in the same tunnel or in the different tunnels.  This object holds the same value as that of the mplsTunnelIndex of mplsTunnelEntry if the forward and reverse LSPs are in the same tunnel. Otherwise, this object holds the value of the other direction associated LSP's mplsTunnelIndex from a different tunnel.  The values of this object and the mplsTunnelExtDestTnlLspIndex object together can be used to identify an opposite direction LSP i.e. if the mplsTunnelIndex and mplsTunnelInstance hold the value for forward LSP, this object and mplsTunnelExtDestTnlLspIndex can be used to retrieve the reverse direction LSP and vice versa.  This object and mplsTunnelExtDestTnlLspIndex values provide the first two indices of tunnel entry and the remaining indices can be derived as follows, if both the forward and reverse LSPs are present in the same tunnel, the opposite direction LSP's Ingress and Egress Identifier will be same for both the LSPs, else the Ingress and Egress Identifiers should be swapped in order to index the other direction tunnel
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cmplstunnelextdesttnllspindex
            
            	This object is applicable only for the bidirectional tunnel that has the forward and reverse LSPs in the same tunnel or in the different tunnels.  This object should contain different value if both the forward and reverse LSPs present in the same tunnel.  This object can contain same value or different values if the forward and reverse LSPs present in the different tunnels
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplstunnelextdesttnlvalid
            
            	Denotes whether or not this tunnel uses mplsTunnelExtDestTnlIndex and mplsTunnelExtDestTnlLspIndex for identifying the opposite direction tunnel information. Note that if this variable is set to true then the mplsTunnelExtDestTnlIndex and mplsTunnelExtDestTnlLspIndex objects should have the valid opposite direction tunnel indices
            	**type**\:  bool
            
            .. attribute:: cmplstunnelextoppositedirtnlvalid
            
            	Denotes whether or not this tunnel uses mplsTunnelOppositeDirPtr for identifying the opposite direction tunnel information. Note that if this variable is set to true then the mplsTunnelOppositeDirPtr should point to the first accessible row of the opposite direction tunnel
            	**type**\:  bool
            
            .. attribute:: cmplstunneloppositedirptr
            
            	This object is applicable only for the bidirectional tunnel that has the forward and reverse LSPs in the same tunnel or in the different tunnels.  This object holds the opposite direction tunnel entry if the bidirectional tunnel is setup by configuring two tunnel entries in mplsTunnelTable.  The value of zeroDotZero indicates single tunnel entry is used for bidirectional tunnel setup
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'
            _revision = '2012-06-06'

            def __init__(self):
                super(CiscoIetfMplsTeExtStd03Mib.Cmplstunnelexttable.Cmplstunnelextentry, self).__init__()

                self.yang_name = "cmplsTunnelExtEntry"
                self.yang_parent_name = "cmplsTunnelExtTable"

                self.mplstunnelindex = YLeaf(YType.str, "mplsTunnelIndex")

                self.mplstunnelinstance = YLeaf(YType.str, "mplsTunnelInstance")

                self.mplstunnelingresslsrid = YLeaf(YType.str, "mplsTunnelIngressLSRId")

                self.mplstunnelegresslsrid = YLeaf(YType.str, "mplsTunnelEgressLSRId")

                self.cmplstunnelextdesttnlindex = YLeaf(YType.uint32, "cmplsTunnelExtDestTnlIndex")

                self.cmplstunnelextdesttnllspindex = YLeaf(YType.uint32, "cmplsTunnelExtDestTnlLspIndex")

                self.cmplstunnelextdesttnlvalid = YLeaf(YType.boolean, "cmplsTunnelExtDestTnlValid")

                self.cmplstunnelextoppositedirtnlvalid = YLeaf(YType.boolean, "cmplsTunnelExtOppositeDirTnlValid")

                self.cmplstunneloppositedirptr = YLeaf(YType.str, "cmplsTunnelOppositeDirPtr")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplstunnelindex",
                                "mplstunnelinstance",
                                "mplstunnelingresslsrid",
                                "mplstunnelegresslsrid",
                                "cmplstunnelextdesttnlindex",
                                "cmplstunnelextdesttnllspindex",
                                "cmplstunnelextdesttnlvalid",
                                "cmplstunnelextoppositedirtnlvalid",
                                "cmplstunneloppositedirptr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfMplsTeExtStd03Mib.Cmplstunnelexttable.Cmplstunnelextentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfMplsTeExtStd03Mib.Cmplstunnelexttable.Cmplstunnelextentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.mplstunnelindex.is_set or
                    self.mplstunnelinstance.is_set or
                    self.mplstunnelingresslsrid.is_set or
                    self.mplstunnelegresslsrid.is_set or
                    self.cmplstunnelextdesttnlindex.is_set or
                    self.cmplstunnelextdesttnllspindex.is_set or
                    self.cmplstunnelextdesttnlvalid.is_set or
                    self.cmplstunnelextoppositedirtnlvalid.is_set or
                    self.cmplstunneloppositedirptr.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplstunnelindex.yfilter != YFilter.not_set or
                    self.mplstunnelinstance.yfilter != YFilter.not_set or
                    self.mplstunnelingresslsrid.yfilter != YFilter.not_set or
                    self.mplstunnelegresslsrid.yfilter != YFilter.not_set or
                    self.cmplstunnelextdesttnlindex.yfilter != YFilter.not_set or
                    self.cmplstunnelextdesttnllspindex.yfilter != YFilter.not_set or
                    self.cmplstunnelextdesttnlvalid.yfilter != YFilter.not_set or
                    self.cmplstunnelextoppositedirtnlvalid.yfilter != YFilter.not_set or
                    self.cmplstunneloppositedirptr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cmplsTunnelExtEntry" + "[mplsTunnelIndex='" + self.mplstunnelindex.get() + "']" + "[mplsTunnelInstance='" + self.mplstunnelinstance.get() + "']" + "[mplsTunnelIngressLSRId='" + self.mplstunnelingresslsrid.get() + "']" + "[mplsTunnelEgressLSRId='" + self.mplstunnelegresslsrid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/cmplsTunnelExtTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplstunnelindex.is_set or self.mplstunnelindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelindex.get_name_leafdata())
                if (self.mplstunnelinstance.is_set or self.mplstunnelinstance.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelinstance.get_name_leafdata())
                if (self.mplstunnelingresslsrid.is_set or self.mplstunnelingresslsrid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelingresslsrid.get_name_leafdata())
                if (self.mplstunnelegresslsrid.is_set or self.mplstunnelegresslsrid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelegresslsrid.get_name_leafdata())
                if (self.cmplstunnelextdesttnlindex.is_set or self.cmplstunnelextdesttnlindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplstunnelextdesttnlindex.get_name_leafdata())
                if (self.cmplstunnelextdesttnllspindex.is_set or self.cmplstunnelextdesttnllspindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplstunnelextdesttnllspindex.get_name_leafdata())
                if (self.cmplstunnelextdesttnlvalid.is_set or self.cmplstunnelextdesttnlvalid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplstunnelextdesttnlvalid.get_name_leafdata())
                if (self.cmplstunnelextoppositedirtnlvalid.is_set or self.cmplstunnelextoppositedirtnlvalid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplstunnelextoppositedirtnlvalid.get_name_leafdata())
                if (self.cmplstunneloppositedirptr.is_set or self.cmplstunneloppositedirptr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplstunneloppositedirptr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsTunnelIndex" or name == "mplsTunnelInstance" or name == "mplsTunnelIngressLSRId" or name == "mplsTunnelEgressLSRId" or name == "cmplsTunnelExtDestTnlIndex" or name == "cmplsTunnelExtDestTnlLspIndex" or name == "cmplsTunnelExtDestTnlValid" or name == "cmplsTunnelExtOppositeDirTnlValid" or name == "cmplsTunnelOppositeDirPtr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsTunnelIndex"):
                    self.mplstunnelindex = value
                    self.mplstunnelindex.value_namespace = name_space
                    self.mplstunnelindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelInstance"):
                    self.mplstunnelinstance = value
                    self.mplstunnelinstance.value_namespace = name_space
                    self.mplstunnelinstance.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelIngressLSRId"):
                    self.mplstunnelingresslsrid = value
                    self.mplstunnelingresslsrid.value_namespace = name_space
                    self.mplstunnelingresslsrid.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelEgressLSRId"):
                    self.mplstunnelegresslsrid = value
                    self.mplstunnelegresslsrid.value_namespace = name_space
                    self.mplstunnelegresslsrid.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsTunnelExtDestTnlIndex"):
                    self.cmplstunnelextdesttnlindex = value
                    self.cmplstunnelextdesttnlindex.value_namespace = name_space
                    self.cmplstunnelextdesttnlindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsTunnelExtDestTnlLspIndex"):
                    self.cmplstunnelextdesttnllspindex = value
                    self.cmplstunnelextdesttnllspindex.value_namespace = name_space
                    self.cmplstunnelextdesttnllspindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsTunnelExtDestTnlValid"):
                    self.cmplstunnelextdesttnlvalid = value
                    self.cmplstunnelextdesttnlvalid.value_namespace = name_space
                    self.cmplstunnelextdesttnlvalid.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsTunnelExtOppositeDirTnlValid"):
                    self.cmplstunnelextoppositedirtnlvalid = value
                    self.cmplstunnelextoppositedirtnlvalid.value_namespace = name_space
                    self.cmplstunnelextoppositedirtnlvalid.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsTunnelOppositeDirPtr"):
                    self.cmplstunneloppositedirptr = value
                    self.cmplstunneloppositedirptr.value_namespace = name_space
                    self.cmplstunneloppositedirptr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cmplstunnelextentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cmplstunnelextentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cmplsTunnelExtTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cmplsTunnelExtEntry"):
                for c in self.cmplstunnelextentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfMplsTeExtStd03Mib.Cmplstunnelexttable.Cmplstunnelextentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cmplstunnelextentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cmplsTunnelExtEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cmplstunnelreverseperftable(Entity):
        """
        This table extends the mplsTunnelTable to provide
        per\-tunnel packet performance information for the reverse
        direction of a bidirectional tunnel.  It can be seen as
        supplementing the mplsTunnelPerfTable, which augments the
        mplsTunnelTable.
        
        For links that do not transport packets, these packet
        counters cannot be maintained.  For such links, attempts
        to read the objects in this table will return
        noSuchInstance.
        
        .. attribute:: cmplstunnelreverseperfentry
        
        	An entry in this table is created by the LSR for every bidirectional MPLS tunnel where packets are visible to the LSR
        	**type**\: list of    :py:class:`Cmplstunnelreverseperfentry <ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CiscoIetfMplsTeExtStd03Mib.Cmplstunnelreverseperftable.Cmplstunnelreverseperfentry>`
        
        

        """

        _prefix = 'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'
        _revision = '2012-06-06'

        def __init__(self):
            super(CiscoIetfMplsTeExtStd03Mib.Cmplstunnelreverseperftable, self).__init__()

            self.yang_name = "cmplsTunnelReversePerfTable"
            self.yang_parent_name = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB"

            self.cmplstunnelreverseperfentry = YList(self)

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
                        super(CiscoIetfMplsTeExtStd03Mib.Cmplstunnelreverseperftable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfMplsTeExtStd03Mib.Cmplstunnelreverseperftable, self).__setattr__(name, value)


        class Cmplstunnelreverseperfentry(Entity):
            """
            An entry in this table is created by the LSR for every
            bidirectional MPLS tunnel where packets are visible to the
            LSR.
            
            .. attribute:: mplstunnelindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`mplstunnelindex <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunneltable.Mplstunnelentry>`
            
            .. attribute:: mplstunnelinstance  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`mplstunnelinstance <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunneltable.Mplstunnelentry>`
            
            .. attribute:: mplstunnelingresslsrid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`mplstunnelingresslsrid <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunneltable.Mplstunnelentry>`
            
            .. attribute:: mplstunnelegresslsrid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`mplstunnelegresslsrid <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunneltable.Mplstunnelentry>`
            
            .. attribute:: cmplstunnelreverseperfbytes
            
            	Number of bytes forwarded on the tunnel in the reverse direction if it is bidirectional.  This object represents the 32\-bit value of the least significant part of the 64\-bit value if both mplsTunnelReversePerfHCBytes and this object are returned.  For links that do not transport packets, this packet counter cannot be maintained.  For such links, this value will return noSuchInstance
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplstunnelreverseperferrors
            
            	Number of errored packets received on the tunnel in the reverse direction if it is bidirectional.  For links that do not transport packets, this packet counter cannot be maintained.  For such links, this value will return noSuchInstance
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplstunnelreverseperfhcbytes
            
            	High\-capacity counter for number of bytes forwarded on the tunnel in the reverse direction if it is bidirectional.  For links that do not transport packets, this packet counter cannot be maintained.  For such links, this value will return noSuchInstance
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cmplstunnelreverseperfhcpackets
            
            	High\-capacity counter for number of packets forwarded on the tunnel in the reverse direction if it is bidirectional.  For links that do not transport packets, this packet counter cannot be maintained.  For such links, this value will return noSuchInstance
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cmplstunnelreverseperfpackets
            
            	Number of packets forwarded on the tunnel in the reverse direction if it is bidirectional.  This object represents the 32\-bit value of the least significant part of the 64\-bit value if both mplsTunnelReversePerfHCPackets and this object are returned.  For links that do not transport packets, this packet counter cannot be maintained.  For such links, this value will return noSuchInstance
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'
            _revision = '2012-06-06'

            def __init__(self):
                super(CiscoIetfMplsTeExtStd03Mib.Cmplstunnelreverseperftable.Cmplstunnelreverseperfentry, self).__init__()

                self.yang_name = "cmplsTunnelReversePerfEntry"
                self.yang_parent_name = "cmplsTunnelReversePerfTable"

                self.mplstunnelindex = YLeaf(YType.str, "mplsTunnelIndex")

                self.mplstunnelinstance = YLeaf(YType.str, "mplsTunnelInstance")

                self.mplstunnelingresslsrid = YLeaf(YType.str, "mplsTunnelIngressLSRId")

                self.mplstunnelegresslsrid = YLeaf(YType.str, "mplsTunnelEgressLSRId")

                self.cmplstunnelreverseperfbytes = YLeaf(YType.uint32, "cmplsTunnelReversePerfBytes")

                self.cmplstunnelreverseperferrors = YLeaf(YType.uint32, "cmplsTunnelReversePerfErrors")

                self.cmplstunnelreverseperfhcbytes = YLeaf(YType.uint64, "cmplsTunnelReversePerfHCBytes")

                self.cmplstunnelreverseperfhcpackets = YLeaf(YType.uint64, "cmplsTunnelReversePerfHCPackets")

                self.cmplstunnelreverseperfpackets = YLeaf(YType.uint32, "cmplsTunnelReversePerfPackets")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplstunnelindex",
                                "mplstunnelinstance",
                                "mplstunnelingresslsrid",
                                "mplstunnelegresslsrid",
                                "cmplstunnelreverseperfbytes",
                                "cmplstunnelreverseperferrors",
                                "cmplstunnelreverseperfhcbytes",
                                "cmplstunnelreverseperfhcpackets",
                                "cmplstunnelreverseperfpackets") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIetfMplsTeExtStd03Mib.Cmplstunnelreverseperftable.Cmplstunnelreverseperfentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIetfMplsTeExtStd03Mib.Cmplstunnelreverseperftable.Cmplstunnelreverseperfentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.mplstunnelindex.is_set or
                    self.mplstunnelinstance.is_set or
                    self.mplstunnelingresslsrid.is_set or
                    self.mplstunnelegresslsrid.is_set or
                    self.cmplstunnelreverseperfbytes.is_set or
                    self.cmplstunnelreverseperferrors.is_set or
                    self.cmplstunnelreverseperfhcbytes.is_set or
                    self.cmplstunnelreverseperfhcpackets.is_set or
                    self.cmplstunnelreverseperfpackets.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplstunnelindex.yfilter != YFilter.not_set or
                    self.mplstunnelinstance.yfilter != YFilter.not_set or
                    self.mplstunnelingresslsrid.yfilter != YFilter.not_set or
                    self.mplstunnelegresslsrid.yfilter != YFilter.not_set or
                    self.cmplstunnelreverseperfbytes.yfilter != YFilter.not_set or
                    self.cmplstunnelreverseperferrors.yfilter != YFilter.not_set or
                    self.cmplstunnelreverseperfhcbytes.yfilter != YFilter.not_set or
                    self.cmplstunnelreverseperfhcpackets.yfilter != YFilter.not_set or
                    self.cmplstunnelreverseperfpackets.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cmplsTunnelReversePerfEntry" + "[mplsTunnelIndex='" + self.mplstunnelindex.get() + "']" + "[mplsTunnelInstance='" + self.mplstunnelinstance.get() + "']" + "[mplsTunnelIngressLSRId='" + self.mplstunnelingresslsrid.get() + "']" + "[mplsTunnelEgressLSRId='" + self.mplstunnelegresslsrid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/cmplsTunnelReversePerfTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplstunnelindex.is_set or self.mplstunnelindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelindex.get_name_leafdata())
                if (self.mplstunnelinstance.is_set or self.mplstunnelinstance.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelinstance.get_name_leafdata())
                if (self.mplstunnelingresslsrid.is_set or self.mplstunnelingresslsrid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelingresslsrid.get_name_leafdata())
                if (self.mplstunnelegresslsrid.is_set or self.mplstunnelegresslsrid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelegresslsrid.get_name_leafdata())
                if (self.cmplstunnelreverseperfbytes.is_set or self.cmplstunnelreverseperfbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplstunnelreverseperfbytes.get_name_leafdata())
                if (self.cmplstunnelreverseperferrors.is_set or self.cmplstunnelreverseperferrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplstunnelreverseperferrors.get_name_leafdata())
                if (self.cmplstunnelreverseperfhcbytes.is_set or self.cmplstunnelreverseperfhcbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplstunnelreverseperfhcbytes.get_name_leafdata())
                if (self.cmplstunnelreverseperfhcpackets.is_set or self.cmplstunnelreverseperfhcpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplstunnelreverseperfhcpackets.get_name_leafdata())
                if (self.cmplstunnelreverseperfpackets.is_set or self.cmplstunnelreverseperfpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplstunnelreverseperfpackets.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsTunnelIndex" or name == "mplsTunnelInstance" or name == "mplsTunnelIngressLSRId" or name == "mplsTunnelEgressLSRId" or name == "cmplsTunnelReversePerfBytes" or name == "cmplsTunnelReversePerfErrors" or name == "cmplsTunnelReversePerfHCBytes" or name == "cmplsTunnelReversePerfHCPackets" or name == "cmplsTunnelReversePerfPackets"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsTunnelIndex"):
                    self.mplstunnelindex = value
                    self.mplstunnelindex.value_namespace = name_space
                    self.mplstunnelindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelInstance"):
                    self.mplstunnelinstance = value
                    self.mplstunnelinstance.value_namespace = name_space
                    self.mplstunnelinstance.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelIngressLSRId"):
                    self.mplstunnelingresslsrid = value
                    self.mplstunnelingresslsrid.value_namespace = name_space
                    self.mplstunnelingresslsrid.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelEgressLSRId"):
                    self.mplstunnelegresslsrid = value
                    self.mplstunnelegresslsrid.value_namespace = name_space
                    self.mplstunnelegresslsrid.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsTunnelReversePerfBytes"):
                    self.cmplstunnelreverseperfbytes = value
                    self.cmplstunnelreverseperfbytes.value_namespace = name_space
                    self.cmplstunnelreverseperfbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsTunnelReversePerfErrors"):
                    self.cmplstunnelreverseperferrors = value
                    self.cmplstunnelreverseperferrors.value_namespace = name_space
                    self.cmplstunnelreverseperferrors.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsTunnelReversePerfHCBytes"):
                    self.cmplstunnelreverseperfhcbytes = value
                    self.cmplstunnelreverseperfhcbytes.value_namespace = name_space
                    self.cmplstunnelreverseperfhcbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsTunnelReversePerfHCPackets"):
                    self.cmplstunnelreverseperfhcpackets = value
                    self.cmplstunnelreverseperfhcpackets.value_namespace = name_space
                    self.cmplstunnelreverseperfhcpackets.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsTunnelReversePerfPackets"):
                    self.cmplstunnelreverseperfpackets = value
                    self.cmplstunnelreverseperfpackets.value_namespace = name_space
                    self.cmplstunnelreverseperfpackets.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cmplstunnelreverseperfentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cmplstunnelreverseperfentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cmplsTunnelReversePerfTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cmplsTunnelReversePerfEntry"):
                for c in self.cmplstunnelreverseperfentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIetfMplsTeExtStd03Mib.Cmplstunnelreverseperftable.Cmplstunnelreverseperfentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cmplstunnelreverseperfentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cmplsTunnelReversePerfEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cmplsnodeconfigtable is not None and self.cmplsnodeconfigtable.has_data()) or
            (self.cmplsnodeiccmaptable is not None and self.cmplsnodeiccmaptable.has_data()) or
            (self.cmplsnodeipmaptable is not None and self.cmplsnodeipmaptable.has_data()) or
            (self.cmplstunnelexttable is not None and self.cmplstunnelexttable.has_data()) or
            (self.cmplstunnelreverseperftable is not None and self.cmplstunnelreverseperftable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cmplsnodeconfigtable is not None and self.cmplsnodeconfigtable.has_operation()) or
            (self.cmplsnodeiccmaptable is not None and self.cmplsnodeiccmaptable.has_operation()) or
            (self.cmplsnodeipmaptable is not None and self.cmplsnodeipmaptable.has_operation()) or
            (self.cmplstunnelexttable is not None and self.cmplstunnelexttable.has_operation()) or
            (self.cmplstunnelreverseperftable is not None and self.cmplstunnelreverseperftable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB" + path_buffer

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

        if (child_yang_name == "cmplsNodeConfigTable"):
            if (self.cmplsnodeconfigtable is None):
                self.cmplsnodeconfigtable = CiscoIetfMplsTeExtStd03Mib.Cmplsnodeconfigtable()
                self.cmplsnodeconfigtable.parent = self
                self._children_name_map["cmplsnodeconfigtable"] = "cmplsNodeConfigTable"
            return self.cmplsnodeconfigtable

        if (child_yang_name == "cmplsNodeIccMapTable"):
            if (self.cmplsnodeiccmaptable is None):
                self.cmplsnodeiccmaptable = CiscoIetfMplsTeExtStd03Mib.Cmplsnodeiccmaptable()
                self.cmplsnodeiccmaptable.parent = self
                self._children_name_map["cmplsnodeiccmaptable"] = "cmplsNodeIccMapTable"
            return self.cmplsnodeiccmaptable

        if (child_yang_name == "cmplsNodeIpMapTable"):
            if (self.cmplsnodeipmaptable is None):
                self.cmplsnodeipmaptable = CiscoIetfMplsTeExtStd03Mib.Cmplsnodeipmaptable()
                self.cmplsnodeipmaptable.parent = self
                self._children_name_map["cmplsnodeipmaptable"] = "cmplsNodeIpMapTable"
            return self.cmplsnodeipmaptable

        if (child_yang_name == "cmplsTunnelExtTable"):
            if (self.cmplstunnelexttable is None):
                self.cmplstunnelexttable = CiscoIetfMplsTeExtStd03Mib.Cmplstunnelexttable()
                self.cmplstunnelexttable.parent = self
                self._children_name_map["cmplstunnelexttable"] = "cmplsTunnelExtTable"
            return self.cmplstunnelexttable

        if (child_yang_name == "cmplsTunnelReversePerfTable"):
            if (self.cmplstunnelreverseperftable is None):
                self.cmplstunnelreverseperftable = CiscoIetfMplsTeExtStd03Mib.Cmplstunnelreverseperftable()
                self.cmplstunnelreverseperftable.parent = self
                self._children_name_map["cmplstunnelreverseperftable"] = "cmplsTunnelReversePerfTable"
            return self.cmplstunnelreverseperftable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cmplsNodeConfigTable" or name == "cmplsNodeIccMapTable" or name == "cmplsNodeIpMapTable" or name == "cmplsTunnelExtTable" or name == "cmplsTunnelReversePerfTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoIetfMplsTeExtStd03Mib()
        return self._top_entity


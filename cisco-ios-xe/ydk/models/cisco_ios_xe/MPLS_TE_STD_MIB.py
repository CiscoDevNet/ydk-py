""" MPLS_TE_STD_MIB 

Copyright (C) The Internet Society (2004). The
initial version of this MIB module was published
in RFC 3812. For full legal notices see the RFC
itself or see\: http\://www.ietf.org/copyrights/ianamib.html

This MIB module contains managed object definitions
 for MPLS Traffic Engineering (TE) as defined in\:
1. Extensions to RSVP for LSP Tunnels, Awduche et
 al, RFC 3209, December 2001
2. Constraint\-Based LSP Setup using LDP, Jamoussi
 (Editor), RFC 3212, January 2002
3. Requirements for Traffic Engineering Over MPLS,
 Awduche, D., Malcolm, J., Agogbua, J., O'Dell, M.,
 and J. McManus, [RFC2702], September 1999

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MplsTeStdMib(Entity):
    """
    
    
    .. attribute:: mplsteobjects
    
    	
    	**type**\:   :py:class:`Mplsteobjects <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplsteobjects>`
    
    .. attribute:: mplstescalars
    
    	
    	**type**\:   :py:class:`Mplstescalars <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstescalars>`
    
    .. attribute:: mplstunnelarhoptable
    
    	The mplsTunnelARHopTable is used to indicate the hops for an MPLS tunnel defined in mplsTunnelTable, as reported by the MPLS signalling protocol. Thus at a transit LSR, this table (if the table is supported and if the signaling protocol is recording actual route information) contains the actual route of the whole tunnel. If the signaling protocol is not recording the actual route, this table MAY report the information from the mplsTunnelHopTable or the mplsTunnelCHopTable.  Each row in this table is indexed by mplsTunnelARHopListIndex. Each row also has a secondary index mplsTunnelARHopIndex, corresponding to the next hop that this row corresponds to.  Please note that since the information necessary to build entries within this table is not provided by some MPLS signalling protocols, implementation of this table is optional. Furthermore, since the information in this table is actually provided by the MPLS signalling protocol after the path has been set\-up, the entries in this table are provided only for observation, and hence, all variables in this table are accessible exclusively as read\- only.  Note also that the contents of this table may change while it is being read because of re\-routing activities. A network administrator may verify that the actual route read is consistent by reference to the mplsTunnelLastPathChange object
    	**type**\:   :py:class:`Mplstunnelarhoptable <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelarhoptable>`
    
    .. attribute:: mplstunnelchoptable
    
    	The mplsTunnelCHopTable is used to indicate the hops, strict or loose, for an MPLS tunnel defined in mplsTunnelTable, as computed by a constraint\- based routing protocol, based on the mplsTunnelHopTable for the outgoing direction of the tunnel. Thus at a transit LSR, this table (if the table is supported) MAY contain the path computed by the CSPF engine on (or on behalf of) this LSR. Each row in this table is indexed by mplsTunnelCHopListIndex.  Each row also has a secondary index mplsTunnelCHopIndex, corresponding to the next hop that this row corresponds to. In case we want to specify a particular interface on the originating LSR of an outgoing tunnel by which we want packets to exit the LSR, we specify this as the first hop for this tunnel in mplsTunnelCHopTable.  Please note that since the information necessary to build entries within this table may not be supported by some LSRs, implementation of this table is optional. Furthermore, since the information in this table describes the path computed by the CSPF engine the entries in this table are read\-only
    	**type**\:   :py:class:`Mplstunnelchoptable <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelchoptable>`
    
    .. attribute:: mplstunnelcrldprestable
    
    	The mplsTunnelCRLDPResTable allows a manager to specify which CR\-LDP\-specific resources are desired for an MPLS tunnel if that tunnel is signaled using CR\-LDP. Note that these attributes are in addition to those specified in mplsTunnelResourceTable. This table also allows several tunnels to point to a single entry in this table, implying that these tunnels should share resources
    	**type**\:   :py:class:`Mplstunnelcrldprestable <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelcrldprestable>`
    
    .. attribute:: mplstunnelhoptable
    
    	The mplsTunnelHopTable is used to indicate the hops, strict or loose, for an instance of an MPLS tunnel defined in mplsTunnelTable, when it is established via signalling, for the outgoing direction of the tunnel. Thus at a transit LSR, this table contains the desired path of the tunnel from this LSR onwards. Each row in this table is indexed by mplsTunnelHopListIndex which corresponds to a group of hop lists or path options.  Each row also has a secondary index mplsTunnelHopIndex, which indicates a group of hops (also known as a path option). Finally, the third index, mplsTunnelHopIndex indicates the specific hop information for a path option. In case we want to specify a particular interface on the originating LSR of an outgoing tunnel by which we want packets to exit the LSR, we specify this as the first hop for this tunnel in mplsTunnelHopTable
    	**type**\:   :py:class:`Mplstunnelhoptable <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelhoptable>`
    
    .. attribute:: mplstunnelresourcetable
    
    	The mplsTunnelResourceTable allows a manager to specify which resources are desired for an MPLS tunnel.  This table also allows several tunnels to point to a single entry in this table, implying that these tunnels should share resources
    	**type**\:   :py:class:`Mplstunnelresourcetable <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelresourcetable>`
    
    .. attribute:: mplstunneltable
    
    	The mplsTunnelTable allows new MPLS tunnels to be created between an LSR and a remote endpoint, and existing tunnels to be reconfigured or removed. Note that only point\-to\-point tunnel segments are supported, although multipoint\-to\-point and point\- to\-multipoint connections are supported by an LSR acting as a cross\-connect.  Each MPLS tunnel can thus have one out\-segment originating at this LSR and/or one in\-segment terminating at this LSR
    	**type**\:   :py:class:`Mplstunneltable <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunneltable>`
    
    

    """

    _prefix = 'MPLS-TE-STD-MIB'
    _revision = '2004-06-03'

    def __init__(self):
        super(MplsTeStdMib, self).__init__()
        self._top_entity = None

        self.yang_name = "MPLS-TE-STD-MIB"
        self.yang_parent_name = "MPLS-TE-STD-MIB"

        self.mplsteobjects = MplsTeStdMib.Mplsteobjects()
        self.mplsteobjects.parent = self
        self._children_name_map["mplsteobjects"] = "mplsTeObjects"
        self._children_yang_names.add("mplsTeObjects")

        self.mplstescalars = MplsTeStdMib.Mplstescalars()
        self.mplstescalars.parent = self
        self._children_name_map["mplstescalars"] = "mplsTeScalars"
        self._children_yang_names.add("mplsTeScalars")

        self.mplstunnelarhoptable = MplsTeStdMib.Mplstunnelarhoptable()
        self.mplstunnelarhoptable.parent = self
        self._children_name_map["mplstunnelarhoptable"] = "mplsTunnelARHopTable"
        self._children_yang_names.add("mplsTunnelARHopTable")

        self.mplstunnelchoptable = MplsTeStdMib.Mplstunnelchoptable()
        self.mplstunnelchoptable.parent = self
        self._children_name_map["mplstunnelchoptable"] = "mplsTunnelCHopTable"
        self._children_yang_names.add("mplsTunnelCHopTable")

        self.mplstunnelcrldprestable = MplsTeStdMib.Mplstunnelcrldprestable()
        self.mplstunnelcrldprestable.parent = self
        self._children_name_map["mplstunnelcrldprestable"] = "mplsTunnelCRLDPResTable"
        self._children_yang_names.add("mplsTunnelCRLDPResTable")

        self.mplstunnelhoptable = MplsTeStdMib.Mplstunnelhoptable()
        self.mplstunnelhoptable.parent = self
        self._children_name_map["mplstunnelhoptable"] = "mplsTunnelHopTable"
        self._children_yang_names.add("mplsTunnelHopTable")

        self.mplstunnelresourcetable = MplsTeStdMib.Mplstunnelresourcetable()
        self.mplstunnelresourcetable.parent = self
        self._children_name_map["mplstunnelresourcetable"] = "mplsTunnelResourceTable"
        self._children_yang_names.add("mplsTunnelResourceTable")

        self.mplstunneltable = MplsTeStdMib.Mplstunneltable()
        self.mplstunneltable.parent = self
        self._children_name_map["mplstunneltable"] = "mplsTunnelTable"
        self._children_yang_names.add("mplsTunnelTable")


    class Mplstescalars(Entity):
        """
        
        
        .. attribute:: mplstunnelactive
        
        	The number of tunnels active on this device. A tunnel is considered active if the mplsTunnelOperStatus is up(1)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplstunnelconfigured
        
        	The number of tunnels configured on this device. A tunnel is considered configured if the mplsTunnelRowStatus is active(1)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplstunnelmaxhops
        
        	The maximum number of hops that can be specified for a tunnel on this device
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplstunnelnotificationmaxrate
        
        	This variable indicates the maximum number of notifications issued per second. If events occur more rapidly, the implementation may simply fail to emit these notifications during that period, or may queue them until an appropriate time. A value of 0 means no throttling is applied and events may be notified at the rate at which they occur
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplstunneltedistproto
        
        	The traffic engineering distribution protocol(s) used by this LSR. Note that an LSR may support more than one distribution protocol simultaneously
        	**type**\:   :py:class:`Mplstunneltedistproto <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstescalars.Mplstunneltedistproto>`
        
        

        """

        _prefix = 'MPLS-TE-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsTeStdMib.Mplstescalars, self).__init__()

            self.yang_name = "mplsTeScalars"
            self.yang_parent_name = "MPLS-TE-STD-MIB"

            self.mplstunnelactive = YLeaf(YType.uint32, "mplsTunnelActive")

            self.mplstunnelconfigured = YLeaf(YType.uint32, "mplsTunnelConfigured")

            self.mplstunnelmaxhops = YLeaf(YType.uint32, "mplsTunnelMaxHops")

            self.mplstunnelnotificationmaxrate = YLeaf(YType.uint32, "mplsTunnelNotificationMaxRate")

            self.mplstunneltedistproto = YLeaf(YType.bits, "mplsTunnelTEDistProto")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("mplstunnelactive",
                            "mplstunnelconfigured",
                            "mplstunnelmaxhops",
                            "mplstunnelnotificationmaxrate",
                            "mplstunneltedistproto") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MplsTeStdMib.Mplstescalars, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsTeStdMib.Mplstescalars, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.mplstunnelactive.is_set or
                self.mplstunnelconfigured.is_set or
                self.mplstunnelmaxhops.is_set or
                self.mplstunnelnotificationmaxrate.is_set or
                self.mplstunneltedistproto.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.mplstunnelactive.yfilter != YFilter.not_set or
                self.mplstunnelconfigured.yfilter != YFilter.not_set or
                self.mplstunnelmaxhops.yfilter != YFilter.not_set or
                self.mplstunnelnotificationmaxrate.yfilter != YFilter.not_set or
                self.mplstunneltedistproto.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsTeScalars" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.mplstunnelactive.is_set or self.mplstunnelactive.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplstunnelactive.get_name_leafdata())
            if (self.mplstunnelconfigured.is_set or self.mplstunnelconfigured.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplstunnelconfigured.get_name_leafdata())
            if (self.mplstunnelmaxhops.is_set or self.mplstunnelmaxhops.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplstunnelmaxhops.get_name_leafdata())
            if (self.mplstunnelnotificationmaxrate.is_set or self.mplstunnelnotificationmaxrate.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplstunnelnotificationmaxrate.get_name_leafdata())
            if (self.mplstunneltedistproto.is_set or self.mplstunneltedistproto.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplstunneltedistproto.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsTunnelActive" or name == "mplsTunnelConfigured" or name == "mplsTunnelMaxHops" or name == "mplsTunnelNotificationMaxRate" or name == "mplsTunnelTEDistProto"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "mplsTunnelActive"):
                self.mplstunnelactive = value
                self.mplstunnelactive.value_namespace = name_space
                self.mplstunnelactive.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsTunnelConfigured"):
                self.mplstunnelconfigured = value
                self.mplstunnelconfigured.value_namespace = name_space
                self.mplstunnelconfigured.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsTunnelMaxHops"):
                self.mplstunnelmaxhops = value
                self.mplstunnelmaxhops.value_namespace = name_space
                self.mplstunnelmaxhops.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsTunnelNotificationMaxRate"):
                self.mplstunnelnotificationmaxrate = value
                self.mplstunnelnotificationmaxrate.value_namespace = name_space
                self.mplstunnelnotificationmaxrate.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsTunnelTEDistProto"):
                self.mplstunneltedistproto[value] = True


    class Mplsteobjects(Entity):
        """
        
        
        .. attribute:: mplstunnelhoplistindexnext
        
        	This object contains an appropriate value to be used for mplsTunnelHopListIndex when creating entries in the mplsTunnelHopTable.  If the number of unassigned entries is exhausted, a retrieval operation will return a value of 0.  This object may also return a value of 0 when the LSR is unable to accept conceptual row creation, for example, if the mplsTunnelHopTable is implemented as read\-only. To obtain the value of mplsTunnelHopListIndex for a new entry in the mplsTunnelHopTable, the manager issues a management protocol retrieval operation to obtain the current value of mplsTunnelHopIndex.  When the SET is performed to create a row in the mplsTunnelHopTable, the Command Responder (agent) must determine whether the value is indeed still unused; Two Network Management Applications may attempt to create a row (configuration entry) simultaneously and use the same value. If it is currently unused, the SET succeeds and the Command Responder (agent) changes the value of this object, according to an implementation\-specific algorithm. If the value is in use, however, the SET fails.  The Network Management Application must then re\-read this variable to obtain a new usable value
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplstunnelindexnext
        
        	This object contains an unused value for mplsTunnelIndex, or a zero to indicate that none exist. Negative values are not allowed, as they do not correspond to valid values of mplsTunnelIndex.  Note that this object offers an unused value for an mplsTunnelIndex value at the ingress side of a tunnel. At other LSRs the value of mplsTunnelIndex SHOULD be taken from the value signaled by the MPLS signaling protocol
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: mplstunnelnotificationenable
        
        	If this object is true, then it enables the generation of mplsTunnelUp and mplsTunnelDown traps, otherwise these traps are not emitted
        	**type**\:  bool
        
        .. attribute:: mplstunnelresourceindexnext
        
        	This object contains the next appropriate value to be used for mplsTunnelResourceIndex when creating entries in the mplsTunnelResourceTable. If the number of unassigned entries is exhausted, a retrieval operation will return a value of 0.  This object may also return a value of 0 when the LSR is unable to accept conceptual row creation, for example, if the mplsTunnelTable is implemented as read\-only.  To obtain the mplsTunnelResourceIndex value for a new entry, the manager must first issue a management protocol retrieval operation to obtain the current value of this object.  When the SET is performed to create a row in the mplsTunnelResourceTable, the Command Responder (agent) must determine whether the value is indeed still unused; Two Network Management Applications may attempt to create a row (configuration entry) simultaneously and use the same value. If it is currently unused, the SET succeeds and the Command Responder (agent) changes the value of this object, according to an implementation\-specific algorithm. If the value is in use, however, the SET fails.  The Network Management Application must then re\-read this variable to obtain a new usable value
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'MPLS-TE-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsTeStdMib.Mplsteobjects, self).__init__()

            self.yang_name = "mplsTeObjects"
            self.yang_parent_name = "MPLS-TE-STD-MIB"

            self.mplstunnelhoplistindexnext = YLeaf(YType.uint32, "mplsTunnelHopListIndexNext")

            self.mplstunnelindexnext = YLeaf(YType.uint32, "mplsTunnelIndexNext")

            self.mplstunnelnotificationenable = YLeaf(YType.boolean, "mplsTunnelNotificationEnable")

            self.mplstunnelresourceindexnext = YLeaf(YType.uint32, "mplsTunnelResourceIndexNext")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("mplstunnelhoplistindexnext",
                            "mplstunnelindexnext",
                            "mplstunnelnotificationenable",
                            "mplstunnelresourceindexnext") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MplsTeStdMib.Mplsteobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsTeStdMib.Mplsteobjects, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.mplstunnelhoplistindexnext.is_set or
                self.mplstunnelindexnext.is_set or
                self.mplstunnelnotificationenable.is_set or
                self.mplstunnelresourceindexnext.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.mplstunnelhoplistindexnext.yfilter != YFilter.not_set or
                self.mplstunnelindexnext.yfilter != YFilter.not_set or
                self.mplstunnelnotificationenable.yfilter != YFilter.not_set or
                self.mplstunnelresourceindexnext.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsTeObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.mplstunnelhoplistindexnext.is_set or self.mplstunnelhoplistindexnext.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplstunnelhoplistindexnext.get_name_leafdata())
            if (self.mplstunnelindexnext.is_set or self.mplstunnelindexnext.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplstunnelindexnext.get_name_leafdata())
            if (self.mplstunnelnotificationenable.is_set or self.mplstunnelnotificationenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplstunnelnotificationenable.get_name_leafdata())
            if (self.mplstunnelresourceindexnext.is_set or self.mplstunnelresourceindexnext.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplstunnelresourceindexnext.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsTunnelHopListIndexNext" or name == "mplsTunnelIndexNext" or name == "mplsTunnelNotificationEnable" or name == "mplsTunnelResourceIndexNext"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "mplsTunnelHopListIndexNext"):
                self.mplstunnelhoplistindexnext = value
                self.mplstunnelhoplistindexnext.value_namespace = name_space
                self.mplstunnelhoplistindexnext.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsTunnelIndexNext"):
                self.mplstunnelindexnext = value
                self.mplstunnelindexnext.value_namespace = name_space
                self.mplstunnelindexnext.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsTunnelNotificationEnable"):
                self.mplstunnelnotificationenable = value
                self.mplstunnelnotificationenable.value_namespace = name_space
                self.mplstunnelnotificationenable.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsTunnelResourceIndexNext"):
                self.mplstunnelresourceindexnext = value
                self.mplstunnelresourceindexnext.value_namespace = name_space
                self.mplstunnelresourceindexnext.value_namespace_prefix = name_space_prefix


    class Mplstunneltable(Entity):
        """
        The mplsTunnelTable allows new MPLS tunnels to be
        created between an LSR and a remote endpoint, and
        existing tunnels to be reconfigured or removed.
        Note that only point\-to\-point tunnel segments are
        supported, although multipoint\-to\-point and point\-
        to\-multipoint connections are supported by an LSR
        acting as a cross\-connect.  Each MPLS tunnel can
        thus have one out\-segment originating at this LSR
        and/or one in\-segment terminating at this LSR.
        
        .. attribute:: mplstunnelentry
        
        	An entry in this table represents an MPLS tunnel. An entry can be created by a network administrator or by an SNMP agent as instructed by an MPLS signalling protocol. Whenever a new entry is created with mplsTunnelIsIf set to true(1), then a corresponding entry is created in ifTable as well (see RFC 2863). The ifType of this entry is mplsTunnel(150).  A tunnel entry needs to be uniquely identified across a MPLS network. Indices mplsTunnelIndex and mplsTunnelInstance uniquely identify a tunnel on the LSR originating the tunnel.  To uniquely identify a tunnel across an MPLS network requires index mplsTunnelIngressLSRId.  The last index mplsTunnelEgressLSRId is useful in identifying all instances of a tunnel that terminate on the same egress LSR
        	**type**\: list of    :py:class:`Mplstunnelentry <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunneltable.Mplstunnelentry>`
        
        

        """

        _prefix = 'MPLS-TE-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsTeStdMib.Mplstunneltable, self).__init__()

            self.yang_name = "mplsTunnelTable"
            self.yang_parent_name = "MPLS-TE-STD-MIB"

            self.mplstunnelentry = YList(self)

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
                        super(MplsTeStdMib.Mplstunneltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsTeStdMib.Mplstunneltable, self).__setattr__(name, value)


        class Mplstunnelentry(Entity):
            """
            An entry in this table represents an MPLS tunnel.
            An entry can be created by a network administrator
            or by an SNMP agent as instructed by an MPLS
            signalling protocol. Whenever a new entry is
            created with mplsTunnelIsIf set to true(1), then a
            corresponding entry is created in ifTable as well
            (see RFC 2863). The ifType of this entry is
            mplsTunnel(150).
            
            A tunnel entry needs to be uniquely identified across
            a MPLS network. Indices mplsTunnelIndex and
            mplsTunnelInstance uniquely identify a tunnel on
            the LSR originating the tunnel.  To uniquely
            identify a tunnel across an MPLS network requires
            index mplsTunnelIngressLSRId.  The last index
            mplsTunnelEgressLSRId is useful in identifying all
            instances of a tunnel that terminate on the same
            egress LSR.
            
            .. attribute:: mplstunnelindex  <key>
            
            	Uniquely identifies a set of tunnel instances between a pair of ingress and egress LSRs. Managers should obtain new values for row creation in this table by reading mplsTunnelIndexNext. When the MPLS signalling protocol is rsvp(2) this value SHOULD be equal to the value signaled in the Tunnel Id of the Session object. When the MPLS signalling protocol is crldp(3) this value SHOULD be equal to the value signaled in the LSP ID
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: mplstunnelinstance  <key>
            
            	Uniquely identifies a particular instance of a tunnel between a pair of ingress and egress LSRs. It is useful to identify multiple instances of tunnels for the purposes of backup and parallel tunnels. When the MPLS signaling protocol is rsvp(2) this value SHOULD be equal to the LSP Id of the Sender Template object. When the signaling protocol is crldp(3) there is no equivalent signaling object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelingresslsrid  <key>
            
            	Identity of the ingress LSR associated with this tunnel instance. When the MPLS signalling protocol is rsvp(2) this value SHOULD be equal to the Tunnel Sender Address in the Sender Template object and MAY be equal to the Extended Tunnel Id field in the SESSION object. When the MPLS signalling protocol is crldp(3) this value SHOULD be equal to the Ingress LSR Router ID field in the LSPID TLV object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelegresslsrid  <key>
            
            	Identity of the egress LSR associated with this tunnel instance
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunneladminstatus
            
            	Indicates the desired operational status of this tunnel
            	**type**\:   :py:class:`Mplstunneladminstatus <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunneltable.Mplstunnelentry.Mplstunneladminstatus>`
            
            .. attribute:: mplstunnelarhoptableindex
            
            	Index into the mplsTunnelARHopTable entry that specifies the actual hops traversed by the tunnel. This is automatically updated by the agent when the actual hops becomes available
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelchoptableindex
            
            	Index into the mplsTunnelCHopTable entry that specifies the computed hops traversed by the tunnel. This is automatically updated by the agent when computed hops become available or when computed hops get modified
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelcreationtime
            
            	Specifies the value of SysUpTime when the first instance of this tunnel came into existence. That is, when the value of mplsTunnelOperStatus was first set to up(1)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunneldescr
            
            	A textual string containing information about the tunnel.  If there is no description this object contains a zero length string. This object is may not be signaled by MPLS signaling protocols, consequentally the value of this object at transit and egress LSRs MAY be automatically generated or absent
            	**type**\:  str
            
            .. attribute:: mplstunnelexcludeanyaffinity
            
            	A link satisfies the exclude\-any constraint if and only if the link contains none of the administrative groups specified in the constraint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelholdingprio
            
            	Indicates the holding priority for this tunnel
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: mplstunnelhoptableindex
            
            	Index into the mplsTunnelHopTable entry that specifies the explicit route hops for this tunnel. This object is meaningful only at the head\-end of the tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelifindex
            
            	If mplsTunnelIsIf is set to true, then this value contains the LSR\-assigned ifIndex which corresponds to an entry in the interfaces table.  Otherwise this variable should contain the value of zero indicating that a valid ifIndex was not assigned to this tunnel interface
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplstunnelincludeallaffinity
            
            	A link satisfies the include\-all constraint if and only if the link contains all of the administrative groups specified in the constraint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelincludeanyaffinity
            
            	A link satisfies the include\-any constraint if and only if the constraint is zero, or the link and the constraint have a resource class in common
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelinstancepriority
            
            	This value indicates which priority, in descending order, with 0 indicating the lowest priority, within a group of tunnel instances. A group of tunnel instances is defined as a set of LSPs with the same mplsTunnelIndex in this table, but with a different mplsTunnelInstance. Tunnel instance priorities are used to denote the priority at which a particular tunnel instance will supercede another. Instances of tunnels containing the same mplsTunnelInstancePriority will be used for load sharing
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelinstanceuptime
            
            	This value identifies the total time that this tunnel instance's operStatus has been Up(1)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelisif
            
            	Denotes whether or not this tunnel corresponds to an interface represented in the interfaces group table. Note that if this variable is set to true then the ifName of the interface corresponding to this tunnel should have a value equal to mplsTunnelName.  Also see the description of ifName in RFC 2863.  This object is meaningful only at the ingress and egress LSRs
            	**type**\:  bool
            
            .. attribute:: mplstunnellastpathchange
            
            	Specifies the time since the last change to the actual path for this tunnel instance
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnellocalprotectinuse
            
            	Indicates that the local repair mechanism is in use to maintain this tunnel (usually in the face of an outage of the link it was previously routed over)
            	**type**\:  bool
            
            .. attribute:: mplstunnelname
            
            	The canonical name assigned to the tunnel. This name can be used to refer to the tunnel on the LSR's console port.  If mplsTunnelIsIf is set to true then the ifName of the interface corresponding to this tunnel should have a value equal to mplsTunnelName.  Also see the description of ifName in RFC 2863
            	**type**\:  str
            
            .. attribute:: mplstunneloperstatus
            
            	Indicates the actual operational status of this tunnel, which is typically but not limited to, a function of the state of individual segments of this tunnel
            	**type**\:   :py:class:`Mplstunneloperstatus <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunneltable.Mplstunnelentry.Mplstunneloperstatus>`
            
            .. attribute:: mplstunnelowner
            
            	Denotes the entity that created and is responsible for managing this tunnel. This column is automatically filled by the agent on creation of a row
            	**type**\:   :py:class:`Mplsowner <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.Mplsowner>`
            
            .. attribute:: mplstunnelpathchanges
            
            	Specifies the number of times the actual path for this tunnel instance has changed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelpathinuse
            
            	This value denotes the configured path that was chosen for this tunnel. This value reflects the secondary index into mplsTunnelHopTable. This path may not exactly match the one in mplsTunnelARHopTable due to the fact that some CSPF modification may have taken place. See mplsTunnelARHopTable for the actual path being taken by the tunnel. A value of zero denotes that no path is currently in use or available
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelperfbytes
            
            	Number of bytes forwarded by the tunnel. This object should represents the 32\-bit value of the least significant part of the 64\-bit value if both mplsTunnelPerfHCBytes is returned
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelperferrors
            
            	Number of packets dropped because of errors or for other reasons
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelperfhcbytes
            
            	High capacity counter for number of bytes forwarded by the tunnel
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: mplstunnelperfhcpackets
            
            	High capacity counter for number of packets forwarded by the tunnel. 
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: mplstunnelperfpackets
            
            	Number of packets forwarded by the tunnel. This object should represents the 32\-bit value of the least significant part of the 64\-bit value if both mplsTunnelPerfHCPackets is returned
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelprimaryinstance
            
            	Specifies the instance index of the primary instance of this tunnel. More details of the definition of tunnel instances and the primary tunnel instance can be found in the description of the TEXTUAL\-CONVENTION MplsTunnelInstanceIndex
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelprimaryuptime
            
            	Specifies the total time the primary instance of this tunnel has been active. The primary instance of this tunnel is defined in mplsTunnelPrimaryInstance
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelresourcepointer
            
            	This variable represents a pointer to the traffic parameter specification for this tunnel.  This value may point at an entry in the mplsTunnelResourceEntry to indicate which mplsTunnelResourceEntry is to be assigned to this LSP instance.  This value may optionally point at an externally defined traffic parameter specification table.  A value of zeroDotZero indicates best\-effort treatment.  By having the same value of this object, two or more LSPs can indicate resource sharing
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplstunnelrole
            
            	This value signifies the role that this tunnel entry/instance represents. This value MUST be set to head(1) at the originating point of the tunnel. This value MUST be set to transit(2) at transit points along the tunnel, if transit points are supported. This value MUST be set to tail(3) at the terminating point of the tunnel if tunnel tails are supported.  The value headTail(4) is provided for tunnels that begin and end on the same LSR
            	**type**\:   :py:class:`Mplstunnelrole <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunneltable.Mplstunnelentry.Mplstunnelrole>`
            
            .. attribute:: mplstunnelrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table.  When a row in this table is in active(1) state, no objects in that row can be modified by the agent except mplsTunnelAdminStatus, mplsTunnelRowStatus and mplsTunnelStorageType
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: mplstunnelsessionattributes
            
            	This bit mask indicates optional session values for this tunnel. The following describes these bit fields\:  fastRerouteThis flag indicates that the any tunnel hop may choose to reroute this tunnel without tearing it down.  This flag permits transit routers to use a local repair mechanism which may result in violation of the explicit routing of this tunnel. When a fault is detected on an adjacent downstream link or node, a transit router can re\-route traffic for fast service restoration.  mergingPermitted This flag permits transit routers to merge this session with other RSVP sessions for the purpose of reducing resource overhead on downstream transit routers, thereby providing better network scaling.  isPersistent  Indicates whether this tunnel should be restored automatically after a failure occurs.  isPinned   This flag indicates whether the loose\- routed hops of this tunnel are to be pinned.  recordRouteThis flag indicates whether or not the signalling protocol should remember the tunnel path after it has been signaled
            	**type**\:   :py:class:`Mplstunnelsessionattributes <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunneltable.Mplstunnelentry.Mplstunnelsessionattributes>`
            
            .. attribute:: mplstunnelsetupprio
            
            	Indicates the setup priority of this tunnel
            	**type**\:  int
            
            	**range:** 0..7
            
            .. attribute:: mplstunnelsignallingproto
            
            	The signalling protocol, if any, used to setup this tunnel
            	**type**\:   :py:class:`Mplstunnelsignallingproto <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunneltable.Mplstunnelentry.Mplstunnelsignallingproto>`
            
            .. attribute:: mplstunnelstatetransitions
            
            	Specifies the number of times the state (mplsTunnelOperStatus) of this tunnel instance has changed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelstoragetype
            
            	The storage type for this tunnel entry. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: mplstunneltotaluptime
            
            	This value represents the aggregate up time for all instances of this tunnel, if available. If this value is unavailable, it MUST return a value of 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplstunnelxcpointer
            
            	This variable points to a row in the mplsXCTable. This table identifies the segments that compose this tunnel, their characteristics, and relationships to each other. A value of zeroDotZero indicates that no LSP has been associated with this tunnel yet
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'MPLS-TE-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MplsTeStdMib.Mplstunneltable.Mplstunnelentry, self).__init__()

                self.yang_name = "mplsTunnelEntry"
                self.yang_parent_name = "mplsTunnelTable"

                self.mplstunnelindex = YLeaf(YType.uint32, "mplsTunnelIndex")

                self.mplstunnelinstance = YLeaf(YType.uint32, "mplsTunnelInstance")

                self.mplstunnelingresslsrid = YLeaf(YType.uint32, "mplsTunnelIngressLSRId")

                self.mplstunnelegresslsrid = YLeaf(YType.uint32, "mplsTunnelEgressLSRId")

                self.mplstunneladminstatus = YLeaf(YType.enumeration, "mplsTunnelAdminStatus")

                self.mplstunnelarhoptableindex = YLeaf(YType.uint32, "mplsTunnelARHopTableIndex")

                self.mplstunnelchoptableindex = YLeaf(YType.uint32, "mplsTunnelCHopTableIndex")

                self.mplstunnelcreationtime = YLeaf(YType.uint32, "mplsTunnelCreationTime")

                self.mplstunneldescr = YLeaf(YType.str, "mplsTunnelDescr")

                self.mplstunnelexcludeanyaffinity = YLeaf(YType.uint32, "mplsTunnelExcludeAnyAffinity")

                self.mplstunnelholdingprio = YLeaf(YType.int32, "mplsTunnelHoldingPrio")

                self.mplstunnelhoptableindex = YLeaf(YType.uint32, "mplsTunnelHopTableIndex")

                self.mplstunnelifindex = YLeaf(YType.int32, "mplsTunnelIfIndex")

                self.mplstunnelincludeallaffinity = YLeaf(YType.uint32, "mplsTunnelIncludeAllAffinity")

                self.mplstunnelincludeanyaffinity = YLeaf(YType.uint32, "mplsTunnelIncludeAnyAffinity")

                self.mplstunnelinstancepriority = YLeaf(YType.uint32, "mplsTunnelInstancePriority")

                self.mplstunnelinstanceuptime = YLeaf(YType.uint32, "mplsTunnelInstanceUpTime")

                self.mplstunnelisif = YLeaf(YType.boolean, "mplsTunnelIsIf")

                self.mplstunnellastpathchange = YLeaf(YType.uint32, "mplsTunnelLastPathChange")

                self.mplstunnellocalprotectinuse = YLeaf(YType.boolean, "mplsTunnelLocalProtectInUse")

                self.mplstunnelname = YLeaf(YType.str, "mplsTunnelName")

                self.mplstunneloperstatus = YLeaf(YType.enumeration, "mplsTunnelOperStatus")

                self.mplstunnelowner = YLeaf(YType.enumeration, "mplsTunnelOwner")

                self.mplstunnelpathchanges = YLeaf(YType.uint32, "mplsTunnelPathChanges")

                self.mplstunnelpathinuse = YLeaf(YType.uint32, "mplsTunnelPathInUse")

                self.mplstunnelperfbytes = YLeaf(YType.uint32, "mplsTunnelPerfBytes")

                self.mplstunnelperferrors = YLeaf(YType.uint32, "mplsTunnelPerfErrors")

                self.mplstunnelperfhcbytes = YLeaf(YType.uint64, "mplsTunnelPerfHCBytes")

                self.mplstunnelperfhcpackets = YLeaf(YType.uint64, "mplsTunnelPerfHCPackets")

                self.mplstunnelperfpackets = YLeaf(YType.uint32, "mplsTunnelPerfPackets")

                self.mplstunnelprimaryinstance = YLeaf(YType.uint32, "mplsTunnelPrimaryInstance")

                self.mplstunnelprimaryuptime = YLeaf(YType.uint32, "mplsTunnelPrimaryUpTime")

                self.mplstunnelresourcepointer = YLeaf(YType.str, "mplsTunnelResourcePointer")

                self.mplstunnelrole = YLeaf(YType.enumeration, "mplsTunnelRole")

                self.mplstunnelrowstatus = YLeaf(YType.enumeration, "mplsTunnelRowStatus")

                self.mplstunnelsessionattributes = YLeaf(YType.bits, "mplsTunnelSessionAttributes")

                self.mplstunnelsetupprio = YLeaf(YType.int32, "mplsTunnelSetupPrio")

                self.mplstunnelsignallingproto = YLeaf(YType.enumeration, "mplsTunnelSignallingProto")

                self.mplstunnelstatetransitions = YLeaf(YType.uint32, "mplsTunnelStateTransitions")

                self.mplstunnelstoragetype = YLeaf(YType.enumeration, "mplsTunnelStorageType")

                self.mplstunneltotaluptime = YLeaf(YType.uint32, "mplsTunnelTotalUpTime")

                self.mplstunnelxcpointer = YLeaf(YType.str, "mplsTunnelXCPointer")

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
                                "mplstunneladminstatus",
                                "mplstunnelarhoptableindex",
                                "mplstunnelchoptableindex",
                                "mplstunnelcreationtime",
                                "mplstunneldescr",
                                "mplstunnelexcludeanyaffinity",
                                "mplstunnelholdingprio",
                                "mplstunnelhoptableindex",
                                "mplstunnelifindex",
                                "mplstunnelincludeallaffinity",
                                "mplstunnelincludeanyaffinity",
                                "mplstunnelinstancepriority",
                                "mplstunnelinstanceuptime",
                                "mplstunnelisif",
                                "mplstunnellastpathchange",
                                "mplstunnellocalprotectinuse",
                                "mplstunnelname",
                                "mplstunneloperstatus",
                                "mplstunnelowner",
                                "mplstunnelpathchanges",
                                "mplstunnelpathinuse",
                                "mplstunnelperfbytes",
                                "mplstunnelperferrors",
                                "mplstunnelperfhcbytes",
                                "mplstunnelperfhcpackets",
                                "mplstunnelperfpackets",
                                "mplstunnelprimaryinstance",
                                "mplstunnelprimaryuptime",
                                "mplstunnelresourcepointer",
                                "mplstunnelrole",
                                "mplstunnelrowstatus",
                                "mplstunnelsessionattributes",
                                "mplstunnelsetupprio",
                                "mplstunnelsignallingproto",
                                "mplstunnelstatetransitions",
                                "mplstunnelstoragetype",
                                "mplstunneltotaluptime",
                                "mplstunnelxcpointer") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsTeStdMib.Mplstunneltable.Mplstunnelentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsTeStdMib.Mplstunneltable.Mplstunnelentry, self).__setattr__(name, value)

            class Mplstunneladminstatus(Enum):
                """
                Mplstunneladminstatus

                Indicates the desired operational status of this

                tunnel.

                .. data:: up = 1

                .. data:: down = 2

                .. data:: testing = 3

                """

                up = Enum.YLeaf(1, "up")

                down = Enum.YLeaf(2, "down")

                testing = Enum.YLeaf(3, "testing")


            class Mplstunneloperstatus(Enum):
                """
                Mplstunneloperstatus

                Indicates the actual operational status of this

                tunnel, which is typically but not limited to, a

                function of the state of individual segments of

                this tunnel.

                .. data:: up = 1

                .. data:: down = 2

                .. data:: testing = 3

                .. data:: unknown = 4

                .. data:: dormant = 5

                .. data:: notPresent = 6

                .. data:: lowerLayerDown = 7

                """

                up = Enum.YLeaf(1, "up")

                down = Enum.YLeaf(2, "down")

                testing = Enum.YLeaf(3, "testing")

                unknown = Enum.YLeaf(4, "unknown")

                dormant = Enum.YLeaf(5, "dormant")

                notPresent = Enum.YLeaf(6, "notPresent")

                lowerLayerDown = Enum.YLeaf(7, "lowerLayerDown")


            class Mplstunnelrole(Enum):
                """
                Mplstunnelrole

                This value signifies the role that this tunnel

                entry/instance represents. This value MUST be set

                to head(1) at the originating point of the tunnel.

                This value MUST be set to transit(2) at transit

                points along the tunnel, if transit points are

                supported. This value MUST be set to tail(3) at the

                terminating point of the tunnel if tunnel tails are

                supported.

                The value headTail(4) is provided for tunnels that

                begin and end on the same LSR.

                .. data:: head = 1

                .. data:: transit = 2

                .. data:: tail = 3

                .. data:: headTail = 4

                """

                head = Enum.YLeaf(1, "head")

                transit = Enum.YLeaf(2, "transit")

                tail = Enum.YLeaf(3, "tail")

                headTail = Enum.YLeaf(4, "headTail")


            class Mplstunnelsignallingproto(Enum):
                """
                Mplstunnelsignallingproto

                The signalling protocol, if any, used to setup this

                tunnel.

                .. data:: none = 1

                .. data:: rsvp = 2

                .. data:: crldp = 3

                .. data:: other = 4

                """

                none = Enum.YLeaf(1, "none")

                rsvp = Enum.YLeaf(2, "rsvp")

                crldp = Enum.YLeaf(3, "crldp")

                other = Enum.YLeaf(4, "other")


            def has_data(self):
                return (
                    self.mplstunnelindex.is_set or
                    self.mplstunnelinstance.is_set or
                    self.mplstunnelingresslsrid.is_set or
                    self.mplstunnelegresslsrid.is_set or
                    self.mplstunneladminstatus.is_set or
                    self.mplstunnelarhoptableindex.is_set or
                    self.mplstunnelchoptableindex.is_set or
                    self.mplstunnelcreationtime.is_set or
                    self.mplstunneldescr.is_set or
                    self.mplstunnelexcludeanyaffinity.is_set or
                    self.mplstunnelholdingprio.is_set or
                    self.mplstunnelhoptableindex.is_set or
                    self.mplstunnelifindex.is_set or
                    self.mplstunnelincludeallaffinity.is_set or
                    self.mplstunnelincludeanyaffinity.is_set or
                    self.mplstunnelinstancepriority.is_set or
                    self.mplstunnelinstanceuptime.is_set or
                    self.mplstunnelisif.is_set or
                    self.mplstunnellastpathchange.is_set or
                    self.mplstunnellocalprotectinuse.is_set or
                    self.mplstunnelname.is_set or
                    self.mplstunneloperstatus.is_set or
                    self.mplstunnelowner.is_set or
                    self.mplstunnelpathchanges.is_set or
                    self.mplstunnelpathinuse.is_set or
                    self.mplstunnelperfbytes.is_set or
                    self.mplstunnelperferrors.is_set or
                    self.mplstunnelperfhcbytes.is_set or
                    self.mplstunnelperfhcpackets.is_set or
                    self.mplstunnelperfpackets.is_set or
                    self.mplstunnelprimaryinstance.is_set or
                    self.mplstunnelprimaryuptime.is_set or
                    self.mplstunnelresourcepointer.is_set or
                    self.mplstunnelrole.is_set or
                    self.mplstunnelrowstatus.is_set or
                    self.mplstunnelsessionattributes.is_set or
                    self.mplstunnelsetupprio.is_set or
                    self.mplstunnelsignallingproto.is_set or
                    self.mplstunnelstatetransitions.is_set or
                    self.mplstunnelstoragetype.is_set or
                    self.mplstunneltotaluptime.is_set or
                    self.mplstunnelxcpointer.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplstunnelindex.yfilter != YFilter.not_set or
                    self.mplstunnelinstance.yfilter != YFilter.not_set or
                    self.mplstunnelingresslsrid.yfilter != YFilter.not_set or
                    self.mplstunnelegresslsrid.yfilter != YFilter.not_set or
                    self.mplstunneladminstatus.yfilter != YFilter.not_set or
                    self.mplstunnelarhoptableindex.yfilter != YFilter.not_set or
                    self.mplstunnelchoptableindex.yfilter != YFilter.not_set or
                    self.mplstunnelcreationtime.yfilter != YFilter.not_set or
                    self.mplstunneldescr.yfilter != YFilter.not_set or
                    self.mplstunnelexcludeanyaffinity.yfilter != YFilter.not_set or
                    self.mplstunnelholdingprio.yfilter != YFilter.not_set or
                    self.mplstunnelhoptableindex.yfilter != YFilter.not_set or
                    self.mplstunnelifindex.yfilter != YFilter.not_set or
                    self.mplstunnelincludeallaffinity.yfilter != YFilter.not_set or
                    self.mplstunnelincludeanyaffinity.yfilter != YFilter.not_set or
                    self.mplstunnelinstancepriority.yfilter != YFilter.not_set or
                    self.mplstunnelinstanceuptime.yfilter != YFilter.not_set or
                    self.mplstunnelisif.yfilter != YFilter.not_set or
                    self.mplstunnellastpathchange.yfilter != YFilter.not_set or
                    self.mplstunnellocalprotectinuse.yfilter != YFilter.not_set or
                    self.mplstunnelname.yfilter != YFilter.not_set or
                    self.mplstunneloperstatus.yfilter != YFilter.not_set or
                    self.mplstunnelowner.yfilter != YFilter.not_set or
                    self.mplstunnelpathchanges.yfilter != YFilter.not_set or
                    self.mplstunnelpathinuse.yfilter != YFilter.not_set or
                    self.mplstunnelperfbytes.yfilter != YFilter.not_set or
                    self.mplstunnelperferrors.yfilter != YFilter.not_set or
                    self.mplstunnelperfhcbytes.yfilter != YFilter.not_set or
                    self.mplstunnelperfhcpackets.yfilter != YFilter.not_set or
                    self.mplstunnelperfpackets.yfilter != YFilter.not_set or
                    self.mplstunnelprimaryinstance.yfilter != YFilter.not_set or
                    self.mplstunnelprimaryuptime.yfilter != YFilter.not_set or
                    self.mplstunnelresourcepointer.yfilter != YFilter.not_set or
                    self.mplstunnelrole.yfilter != YFilter.not_set or
                    self.mplstunnelrowstatus.yfilter != YFilter.not_set or
                    self.mplstunnelsessionattributes.yfilter != YFilter.not_set or
                    self.mplstunnelsetupprio.yfilter != YFilter.not_set or
                    self.mplstunnelsignallingproto.yfilter != YFilter.not_set or
                    self.mplstunnelstatetransitions.yfilter != YFilter.not_set or
                    self.mplstunnelstoragetype.yfilter != YFilter.not_set or
                    self.mplstunneltotaluptime.yfilter != YFilter.not_set or
                    self.mplstunnelxcpointer.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsTunnelEntry" + "[mplsTunnelIndex='" + self.mplstunnelindex.get() + "']" + "[mplsTunnelInstance='" + self.mplstunnelinstance.get() + "']" + "[mplsTunnelIngressLSRId='" + self.mplstunnelingresslsrid.get() + "']" + "[mplsTunnelEgressLSRId='" + self.mplstunnelegresslsrid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/mplsTunnelTable/%s" % self.get_segment_path()
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
                if (self.mplstunneladminstatus.is_set or self.mplstunneladminstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunneladminstatus.get_name_leafdata())
                if (self.mplstunnelarhoptableindex.is_set or self.mplstunnelarhoptableindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelarhoptableindex.get_name_leafdata())
                if (self.mplstunnelchoptableindex.is_set or self.mplstunnelchoptableindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelchoptableindex.get_name_leafdata())
                if (self.mplstunnelcreationtime.is_set or self.mplstunnelcreationtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelcreationtime.get_name_leafdata())
                if (self.mplstunneldescr.is_set or self.mplstunneldescr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunneldescr.get_name_leafdata())
                if (self.mplstunnelexcludeanyaffinity.is_set or self.mplstunnelexcludeanyaffinity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelexcludeanyaffinity.get_name_leafdata())
                if (self.mplstunnelholdingprio.is_set or self.mplstunnelholdingprio.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelholdingprio.get_name_leafdata())
                if (self.mplstunnelhoptableindex.is_set or self.mplstunnelhoptableindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelhoptableindex.get_name_leafdata())
                if (self.mplstunnelifindex.is_set or self.mplstunnelifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelifindex.get_name_leafdata())
                if (self.mplstunnelincludeallaffinity.is_set or self.mplstunnelincludeallaffinity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelincludeallaffinity.get_name_leafdata())
                if (self.mplstunnelincludeanyaffinity.is_set or self.mplstunnelincludeanyaffinity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelincludeanyaffinity.get_name_leafdata())
                if (self.mplstunnelinstancepriority.is_set or self.mplstunnelinstancepriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelinstancepriority.get_name_leafdata())
                if (self.mplstunnelinstanceuptime.is_set or self.mplstunnelinstanceuptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelinstanceuptime.get_name_leafdata())
                if (self.mplstunnelisif.is_set or self.mplstunnelisif.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelisif.get_name_leafdata())
                if (self.mplstunnellastpathchange.is_set or self.mplstunnellastpathchange.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnellastpathchange.get_name_leafdata())
                if (self.mplstunnellocalprotectinuse.is_set or self.mplstunnellocalprotectinuse.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnellocalprotectinuse.get_name_leafdata())
                if (self.mplstunnelname.is_set or self.mplstunnelname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelname.get_name_leafdata())
                if (self.mplstunneloperstatus.is_set or self.mplstunneloperstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunneloperstatus.get_name_leafdata())
                if (self.mplstunnelowner.is_set or self.mplstunnelowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelowner.get_name_leafdata())
                if (self.mplstunnelpathchanges.is_set or self.mplstunnelpathchanges.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelpathchanges.get_name_leafdata())
                if (self.mplstunnelpathinuse.is_set or self.mplstunnelpathinuse.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelpathinuse.get_name_leafdata())
                if (self.mplstunnelperfbytes.is_set or self.mplstunnelperfbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelperfbytes.get_name_leafdata())
                if (self.mplstunnelperferrors.is_set or self.mplstunnelperferrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelperferrors.get_name_leafdata())
                if (self.mplstunnelperfhcbytes.is_set or self.mplstunnelperfhcbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelperfhcbytes.get_name_leafdata())
                if (self.mplstunnelperfhcpackets.is_set or self.mplstunnelperfhcpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelperfhcpackets.get_name_leafdata())
                if (self.mplstunnelperfpackets.is_set or self.mplstunnelperfpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelperfpackets.get_name_leafdata())
                if (self.mplstunnelprimaryinstance.is_set or self.mplstunnelprimaryinstance.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelprimaryinstance.get_name_leafdata())
                if (self.mplstunnelprimaryuptime.is_set or self.mplstunnelprimaryuptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelprimaryuptime.get_name_leafdata())
                if (self.mplstunnelresourcepointer.is_set or self.mplstunnelresourcepointer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelresourcepointer.get_name_leafdata())
                if (self.mplstunnelrole.is_set or self.mplstunnelrole.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelrole.get_name_leafdata())
                if (self.mplstunnelrowstatus.is_set or self.mplstunnelrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelrowstatus.get_name_leafdata())
                if (self.mplstunnelsessionattributes.is_set or self.mplstunnelsessionattributes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelsessionattributes.get_name_leafdata())
                if (self.mplstunnelsetupprio.is_set or self.mplstunnelsetupprio.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelsetupprio.get_name_leafdata())
                if (self.mplstunnelsignallingproto.is_set or self.mplstunnelsignallingproto.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelsignallingproto.get_name_leafdata())
                if (self.mplstunnelstatetransitions.is_set or self.mplstunnelstatetransitions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelstatetransitions.get_name_leafdata())
                if (self.mplstunnelstoragetype.is_set or self.mplstunnelstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelstoragetype.get_name_leafdata())
                if (self.mplstunneltotaluptime.is_set or self.mplstunneltotaluptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunneltotaluptime.get_name_leafdata())
                if (self.mplstunnelxcpointer.is_set or self.mplstunnelxcpointer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelxcpointer.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsTunnelIndex" or name == "mplsTunnelInstance" or name == "mplsTunnelIngressLSRId" or name == "mplsTunnelEgressLSRId" or name == "mplsTunnelAdminStatus" or name == "mplsTunnelARHopTableIndex" or name == "mplsTunnelCHopTableIndex" or name == "mplsTunnelCreationTime" or name == "mplsTunnelDescr" or name == "mplsTunnelExcludeAnyAffinity" or name == "mplsTunnelHoldingPrio" or name == "mplsTunnelHopTableIndex" or name == "mplsTunnelIfIndex" or name == "mplsTunnelIncludeAllAffinity" or name == "mplsTunnelIncludeAnyAffinity" or name == "mplsTunnelInstancePriority" or name == "mplsTunnelInstanceUpTime" or name == "mplsTunnelIsIf" or name == "mplsTunnelLastPathChange" or name == "mplsTunnelLocalProtectInUse" or name == "mplsTunnelName" or name == "mplsTunnelOperStatus" or name == "mplsTunnelOwner" or name == "mplsTunnelPathChanges" or name == "mplsTunnelPathInUse" or name == "mplsTunnelPerfBytes" or name == "mplsTunnelPerfErrors" or name == "mplsTunnelPerfHCBytes" or name == "mplsTunnelPerfHCPackets" or name == "mplsTunnelPerfPackets" or name == "mplsTunnelPrimaryInstance" or name == "mplsTunnelPrimaryUpTime" or name == "mplsTunnelResourcePointer" or name == "mplsTunnelRole" or name == "mplsTunnelRowStatus" or name == "mplsTunnelSessionAttributes" or name == "mplsTunnelSetupPrio" or name == "mplsTunnelSignallingProto" or name == "mplsTunnelStateTransitions" or name == "mplsTunnelStorageType" or name == "mplsTunnelTotalUpTime" or name == "mplsTunnelXCPointer"):
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
                if(value_path == "mplsTunnelAdminStatus"):
                    self.mplstunneladminstatus = value
                    self.mplstunneladminstatus.value_namespace = name_space
                    self.mplstunneladminstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelARHopTableIndex"):
                    self.mplstunnelarhoptableindex = value
                    self.mplstunnelarhoptableindex.value_namespace = name_space
                    self.mplstunnelarhoptableindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelCHopTableIndex"):
                    self.mplstunnelchoptableindex = value
                    self.mplstunnelchoptableindex.value_namespace = name_space
                    self.mplstunnelchoptableindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelCreationTime"):
                    self.mplstunnelcreationtime = value
                    self.mplstunnelcreationtime.value_namespace = name_space
                    self.mplstunnelcreationtime.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelDescr"):
                    self.mplstunneldescr = value
                    self.mplstunneldescr.value_namespace = name_space
                    self.mplstunneldescr.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelExcludeAnyAffinity"):
                    self.mplstunnelexcludeanyaffinity = value
                    self.mplstunnelexcludeanyaffinity.value_namespace = name_space
                    self.mplstunnelexcludeanyaffinity.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelHoldingPrio"):
                    self.mplstunnelholdingprio = value
                    self.mplstunnelholdingprio.value_namespace = name_space
                    self.mplstunnelholdingprio.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelHopTableIndex"):
                    self.mplstunnelhoptableindex = value
                    self.mplstunnelhoptableindex.value_namespace = name_space
                    self.mplstunnelhoptableindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelIfIndex"):
                    self.mplstunnelifindex = value
                    self.mplstunnelifindex.value_namespace = name_space
                    self.mplstunnelifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelIncludeAllAffinity"):
                    self.mplstunnelincludeallaffinity = value
                    self.mplstunnelincludeallaffinity.value_namespace = name_space
                    self.mplstunnelincludeallaffinity.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelIncludeAnyAffinity"):
                    self.mplstunnelincludeanyaffinity = value
                    self.mplstunnelincludeanyaffinity.value_namespace = name_space
                    self.mplstunnelincludeanyaffinity.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelInstancePriority"):
                    self.mplstunnelinstancepriority = value
                    self.mplstunnelinstancepriority.value_namespace = name_space
                    self.mplstunnelinstancepriority.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelInstanceUpTime"):
                    self.mplstunnelinstanceuptime = value
                    self.mplstunnelinstanceuptime.value_namespace = name_space
                    self.mplstunnelinstanceuptime.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelIsIf"):
                    self.mplstunnelisif = value
                    self.mplstunnelisif.value_namespace = name_space
                    self.mplstunnelisif.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelLastPathChange"):
                    self.mplstunnellastpathchange = value
                    self.mplstunnellastpathchange.value_namespace = name_space
                    self.mplstunnellastpathchange.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelLocalProtectInUse"):
                    self.mplstunnellocalprotectinuse = value
                    self.mplstunnellocalprotectinuse.value_namespace = name_space
                    self.mplstunnellocalprotectinuse.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelName"):
                    self.mplstunnelname = value
                    self.mplstunnelname.value_namespace = name_space
                    self.mplstunnelname.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelOperStatus"):
                    self.mplstunneloperstatus = value
                    self.mplstunneloperstatus.value_namespace = name_space
                    self.mplstunneloperstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelOwner"):
                    self.mplstunnelowner = value
                    self.mplstunnelowner.value_namespace = name_space
                    self.mplstunnelowner.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelPathChanges"):
                    self.mplstunnelpathchanges = value
                    self.mplstunnelpathchanges.value_namespace = name_space
                    self.mplstunnelpathchanges.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelPathInUse"):
                    self.mplstunnelpathinuse = value
                    self.mplstunnelpathinuse.value_namespace = name_space
                    self.mplstunnelpathinuse.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelPerfBytes"):
                    self.mplstunnelperfbytes = value
                    self.mplstunnelperfbytes.value_namespace = name_space
                    self.mplstunnelperfbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelPerfErrors"):
                    self.mplstunnelperferrors = value
                    self.mplstunnelperferrors.value_namespace = name_space
                    self.mplstunnelperferrors.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelPerfHCBytes"):
                    self.mplstunnelperfhcbytes = value
                    self.mplstunnelperfhcbytes.value_namespace = name_space
                    self.mplstunnelperfhcbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelPerfHCPackets"):
                    self.mplstunnelperfhcpackets = value
                    self.mplstunnelperfhcpackets.value_namespace = name_space
                    self.mplstunnelperfhcpackets.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelPerfPackets"):
                    self.mplstunnelperfpackets = value
                    self.mplstunnelperfpackets.value_namespace = name_space
                    self.mplstunnelperfpackets.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelPrimaryInstance"):
                    self.mplstunnelprimaryinstance = value
                    self.mplstunnelprimaryinstance.value_namespace = name_space
                    self.mplstunnelprimaryinstance.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelPrimaryUpTime"):
                    self.mplstunnelprimaryuptime = value
                    self.mplstunnelprimaryuptime.value_namespace = name_space
                    self.mplstunnelprimaryuptime.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelResourcePointer"):
                    self.mplstunnelresourcepointer = value
                    self.mplstunnelresourcepointer.value_namespace = name_space
                    self.mplstunnelresourcepointer.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelRole"):
                    self.mplstunnelrole = value
                    self.mplstunnelrole.value_namespace = name_space
                    self.mplstunnelrole.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelRowStatus"):
                    self.mplstunnelrowstatus = value
                    self.mplstunnelrowstatus.value_namespace = name_space
                    self.mplstunnelrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelSessionAttributes"):
                    self.mplstunnelsessionattributes[value] = True
                if(value_path == "mplsTunnelSetupPrio"):
                    self.mplstunnelsetupprio = value
                    self.mplstunnelsetupprio.value_namespace = name_space
                    self.mplstunnelsetupprio.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelSignallingProto"):
                    self.mplstunnelsignallingproto = value
                    self.mplstunnelsignallingproto.value_namespace = name_space
                    self.mplstunnelsignallingproto.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelStateTransitions"):
                    self.mplstunnelstatetransitions = value
                    self.mplstunnelstatetransitions.value_namespace = name_space
                    self.mplstunnelstatetransitions.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelStorageType"):
                    self.mplstunnelstoragetype = value
                    self.mplstunnelstoragetype.value_namespace = name_space
                    self.mplstunnelstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelTotalUpTime"):
                    self.mplstunneltotaluptime = value
                    self.mplstunneltotaluptime.value_namespace = name_space
                    self.mplstunneltotaluptime.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelXCPointer"):
                    self.mplstunnelxcpointer = value
                    self.mplstunnelxcpointer.value_namespace = name_space
                    self.mplstunnelxcpointer.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplstunnelentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplstunnelentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsTunnelTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsTunnelEntry"):
                for c in self.mplstunnelentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsTeStdMib.Mplstunneltable.Mplstunnelentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplstunnelentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsTunnelEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplstunnelhoptable(Entity):
        """
        The mplsTunnelHopTable is used to indicate the hops,
        strict or loose, for an instance of an MPLS tunnel
        defined in mplsTunnelTable, when it is established
        via signalling, for the outgoing direction of the
        tunnel. Thus at a transit LSR, this table contains
        the desired path of the tunnel from this LSR
        onwards. Each row in this table is indexed by
        mplsTunnelHopListIndex which corresponds to a group
        of hop lists or path options.  Each row also has a
        secondary index mplsTunnelHopIndex, which indicates
        a group of hops (also known as a path option).
        Finally, the third index, mplsTunnelHopIndex
        indicates the specific hop information for a path
        option. In case we want to specify a particular
        interface on the originating LSR of an outgoing
        tunnel by which we want packets to exit the LSR,
        we specify this as the first hop for this tunnel in
        mplsTunnelHopTable.
        
        .. attribute:: mplstunnelhopentry
        
        	An entry in this table represents a tunnel hop.  An entry is created by a network administrator for signaled ERLSP set up by an MPLS signalling protocol
        	**type**\: list of    :py:class:`Mplstunnelhopentry <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelhoptable.Mplstunnelhopentry>`
        
        

        """

        _prefix = 'MPLS-TE-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsTeStdMib.Mplstunnelhoptable, self).__init__()

            self.yang_name = "mplsTunnelHopTable"
            self.yang_parent_name = "MPLS-TE-STD-MIB"

            self.mplstunnelhopentry = YList(self)

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
                        super(MplsTeStdMib.Mplstunnelhoptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsTeStdMib.Mplstunnelhoptable, self).__setattr__(name, value)


        class Mplstunnelhopentry(Entity):
            """
            An entry in this table represents a tunnel hop.  An
            entry is created by a network administrator for
            signaled ERLSP set up by an MPLS signalling
            protocol.
            
            .. attribute:: mplstunnelhoplistindex  <key>
            
            	Primary index into this table identifying a particular explicit route object
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplstunnelhoppathoptionindex  <key>
            
            	Secondary index into this table identifying a particular group of hops representing a particular configured path. This is otherwise known as a path option
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplstunnelhopindex  <key>
            
            	Tertiary index into this table identifying a particular hop
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplstunnelhopaddrtype
            
            	The Hop Address Type of this tunnel hop.  The value of this object cannot be changed if the value of the corresponding mplsTunnelHopRowStatus object is 'active'.  Note that lspid(5) is a valid option only for tunnels signaled via CRLDP
            	**type**\:   :py:class:`Tehopaddresstype <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.Tehopaddresstype>`
            
            .. attribute:: mplstunnelhopaddrunnum
            
            	If mplsTunnelHopAddrType is set to unnum(4), then this value will contain the interface identifier of the unnumbered interface for this hop. This object should be used in conjunction with mplsTunnelHopIpAddress which would contain the LSR Router ID in this case. Otherwise the agent should set this object to zero\-length string and the manager should ignore this
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: mplstunnelhopasnumber
            
            	If mplsTunnelHopAddrType is set to asnumber(3), then this value will contain the AS number of this hop. Otherwise the agent should set this object to zero\- length string and the manager should ignore this
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: mplstunnelhopentrypathcomp
            
            	If this value is set to dynamic, then the user should only specify the source and destination of the path and expect that the CSPF will calculate the remainder of the path.  If this value is set to explicit, the user should specify the entire path for the tunnel to take.  This path may contain strict or loose hops.  Each hop along a specific path SHOULD have this object set to the same value
            	**type**\:   :py:class:`Mplstunnelhopentrypathcomp <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelhoptable.Mplstunnelhopentry.Mplstunnelhopentrypathcomp>`
            
            .. attribute:: mplstunnelhopinclude
            
            	If this value is set to true, then this indicates that this hop must be included in the tunnel's path. If this value is set to 'false', then this hop must be avoided when calculating the path for this tunnel. The default value of this object is 'true', so that by default all indicated hops are included in the CSPF path computation. If this object is set to 'false' the value of mplsTunnelHopType should be ignored
            	**type**\:  bool
            
            .. attribute:: mplstunnelhopipaddr
            
            	The Tunnel Hop Address for this tunnel hop.  The type of this address is determined by the value of the corresponding mplsTunnelHopAddrType.  The value of this object cannot be changed if the value of the corresponding mplsTunnelHopRowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mplstunnelhopipprefixlen
            
            	If mplsTunnelHopAddrType is set to ipv4(1) or ipv6(2), then this value will contain an appropriate prefix length for the IP address in object mplsTunnelHopIpAddr. Otherwise this value is irrelevant and should be ignored
            	**type**\:  int
            
            	**range:** 0..2040
            
            .. attribute:: mplstunnelhoplspid
            
            	If mplsTunnelHopAddrType is set to lspid(5), then this value will contain the LSPID of a tunnel of this hop. The present tunnel being configured is tunneled through this hop (using label stacking). This object is otherwise insignificant and should contain a value of 0 to indicate this fact
            	**type**\:  str
            
            	**length:** 2 \| 6
            
            .. attribute:: mplstunnelhoppathoptionname
            
            	The description of this series of hops as they relate to the specified path option. The value of this object SHOULD be the same for each hop in the series that comprises a path option
            	**type**\:  str
            
            .. attribute:: mplstunnelhoprowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table.  When a row in this table is in active(1) state, no objects in that row can be modified by the agent except mplsTunnelHopRowStatus and mplsTunnelHopStorageType
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: mplstunnelhopstoragetype
            
            	The storage type for this Hop entry. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: mplstunnelhoptype
            
            	Denotes whether this tunnel hop is routed in a strict or loose fashion. The value of this object has no meaning if the mplsTunnelHopInclude object is set to 'false'
            	**type**\:   :py:class:`Mplstunnelhoptype <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelhoptable.Mplstunnelhopentry.Mplstunnelhoptype>`
            
            

            """

            _prefix = 'MPLS-TE-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MplsTeStdMib.Mplstunnelhoptable.Mplstunnelhopentry, self).__init__()

                self.yang_name = "mplsTunnelHopEntry"
                self.yang_parent_name = "mplsTunnelHopTable"

                self.mplstunnelhoplistindex = YLeaf(YType.uint32, "mplsTunnelHopListIndex")

                self.mplstunnelhoppathoptionindex = YLeaf(YType.uint32, "mplsTunnelHopPathOptionIndex")

                self.mplstunnelhopindex = YLeaf(YType.uint32, "mplsTunnelHopIndex")

                self.mplstunnelhopaddrtype = YLeaf(YType.enumeration, "mplsTunnelHopAddrType")

                self.mplstunnelhopaddrunnum = YLeaf(YType.str, "mplsTunnelHopAddrUnnum")

                self.mplstunnelhopasnumber = YLeaf(YType.str, "mplsTunnelHopAsNumber")

                self.mplstunnelhopentrypathcomp = YLeaf(YType.enumeration, "mplsTunnelHopEntryPathComp")

                self.mplstunnelhopinclude = YLeaf(YType.boolean, "mplsTunnelHopInclude")

                self.mplstunnelhopipaddr = YLeaf(YType.str, "mplsTunnelHopIpAddr")

                self.mplstunnelhopipprefixlen = YLeaf(YType.uint32, "mplsTunnelHopIpPrefixLen")

                self.mplstunnelhoplspid = YLeaf(YType.str, "mplsTunnelHopLspId")

                self.mplstunnelhoppathoptionname = YLeaf(YType.str, "mplsTunnelHopPathOptionName")

                self.mplstunnelhoprowstatus = YLeaf(YType.enumeration, "mplsTunnelHopRowStatus")

                self.mplstunnelhopstoragetype = YLeaf(YType.enumeration, "mplsTunnelHopStorageType")

                self.mplstunnelhoptype = YLeaf(YType.enumeration, "mplsTunnelHopType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplstunnelhoplistindex",
                                "mplstunnelhoppathoptionindex",
                                "mplstunnelhopindex",
                                "mplstunnelhopaddrtype",
                                "mplstunnelhopaddrunnum",
                                "mplstunnelhopasnumber",
                                "mplstunnelhopentrypathcomp",
                                "mplstunnelhopinclude",
                                "mplstunnelhopipaddr",
                                "mplstunnelhopipprefixlen",
                                "mplstunnelhoplspid",
                                "mplstunnelhoppathoptionname",
                                "mplstunnelhoprowstatus",
                                "mplstunnelhopstoragetype",
                                "mplstunnelhoptype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsTeStdMib.Mplstunnelhoptable.Mplstunnelhopentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsTeStdMib.Mplstunnelhoptable.Mplstunnelhopentry, self).__setattr__(name, value)

            class Mplstunnelhopentrypathcomp(Enum):
                """
                Mplstunnelhopentrypathcomp

                If this value is set to dynamic, then the user

                should only specify the source and destination of

                the path and expect that the CSPF will calculate

                the remainder of the path.  If this value is set to

                explicit, the user should specify the entire path

                for the tunnel to take.  This path may contain

                strict or loose hops.  Each hop along a specific

                path SHOULD have this object set to the same value

                .. data:: dynamic = 1

                .. data:: explicit = 2

                """

                dynamic = Enum.YLeaf(1, "dynamic")

                explicit = Enum.YLeaf(2, "explicit")


            class Mplstunnelhoptype(Enum):
                """
                Mplstunnelhoptype

                Denotes whether this tunnel hop is routed in a

                strict or loose fashion. The value of this object

                has no meaning if the mplsTunnelHopInclude object

                is set to 'false'.

                .. data:: strict = 1

                .. data:: loose = 2

                """

                strict = Enum.YLeaf(1, "strict")

                loose = Enum.YLeaf(2, "loose")


            def has_data(self):
                return (
                    self.mplstunnelhoplistindex.is_set or
                    self.mplstunnelhoppathoptionindex.is_set or
                    self.mplstunnelhopindex.is_set or
                    self.mplstunnelhopaddrtype.is_set or
                    self.mplstunnelhopaddrunnum.is_set or
                    self.mplstunnelhopasnumber.is_set or
                    self.mplstunnelhopentrypathcomp.is_set or
                    self.mplstunnelhopinclude.is_set or
                    self.mplstunnelhopipaddr.is_set or
                    self.mplstunnelhopipprefixlen.is_set or
                    self.mplstunnelhoplspid.is_set or
                    self.mplstunnelhoppathoptionname.is_set or
                    self.mplstunnelhoprowstatus.is_set or
                    self.mplstunnelhopstoragetype.is_set or
                    self.mplstunnelhoptype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplstunnelhoplistindex.yfilter != YFilter.not_set or
                    self.mplstunnelhoppathoptionindex.yfilter != YFilter.not_set or
                    self.mplstunnelhopindex.yfilter != YFilter.not_set or
                    self.mplstunnelhopaddrtype.yfilter != YFilter.not_set or
                    self.mplstunnelhopaddrunnum.yfilter != YFilter.not_set or
                    self.mplstunnelhopasnumber.yfilter != YFilter.not_set or
                    self.mplstunnelhopentrypathcomp.yfilter != YFilter.not_set or
                    self.mplstunnelhopinclude.yfilter != YFilter.not_set or
                    self.mplstunnelhopipaddr.yfilter != YFilter.not_set or
                    self.mplstunnelhopipprefixlen.yfilter != YFilter.not_set or
                    self.mplstunnelhoplspid.yfilter != YFilter.not_set or
                    self.mplstunnelhoppathoptionname.yfilter != YFilter.not_set or
                    self.mplstunnelhoprowstatus.yfilter != YFilter.not_set or
                    self.mplstunnelhopstoragetype.yfilter != YFilter.not_set or
                    self.mplstunnelhoptype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsTunnelHopEntry" + "[mplsTunnelHopListIndex='" + self.mplstunnelhoplistindex.get() + "']" + "[mplsTunnelHopPathOptionIndex='" + self.mplstunnelhoppathoptionindex.get() + "']" + "[mplsTunnelHopIndex='" + self.mplstunnelhopindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/mplsTunnelHopTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplstunnelhoplistindex.is_set or self.mplstunnelhoplistindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelhoplistindex.get_name_leafdata())
                if (self.mplstunnelhoppathoptionindex.is_set or self.mplstunnelhoppathoptionindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelhoppathoptionindex.get_name_leafdata())
                if (self.mplstunnelhopindex.is_set or self.mplstunnelhopindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelhopindex.get_name_leafdata())
                if (self.mplstunnelhopaddrtype.is_set or self.mplstunnelhopaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelhopaddrtype.get_name_leafdata())
                if (self.mplstunnelhopaddrunnum.is_set or self.mplstunnelhopaddrunnum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelhopaddrunnum.get_name_leafdata())
                if (self.mplstunnelhopasnumber.is_set or self.mplstunnelhopasnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelhopasnumber.get_name_leafdata())
                if (self.mplstunnelhopentrypathcomp.is_set or self.mplstunnelhopentrypathcomp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelhopentrypathcomp.get_name_leafdata())
                if (self.mplstunnelhopinclude.is_set or self.mplstunnelhopinclude.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelhopinclude.get_name_leafdata())
                if (self.mplstunnelhopipaddr.is_set or self.mplstunnelhopipaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelhopipaddr.get_name_leafdata())
                if (self.mplstunnelhopipprefixlen.is_set or self.mplstunnelhopipprefixlen.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelhopipprefixlen.get_name_leafdata())
                if (self.mplstunnelhoplspid.is_set or self.mplstunnelhoplspid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelhoplspid.get_name_leafdata())
                if (self.mplstunnelhoppathoptionname.is_set or self.mplstunnelhoppathoptionname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelhoppathoptionname.get_name_leafdata())
                if (self.mplstunnelhoprowstatus.is_set or self.mplstunnelhoprowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelhoprowstatus.get_name_leafdata())
                if (self.mplstunnelhopstoragetype.is_set or self.mplstunnelhopstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelhopstoragetype.get_name_leafdata())
                if (self.mplstunnelhoptype.is_set or self.mplstunnelhoptype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelhoptype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsTunnelHopListIndex" or name == "mplsTunnelHopPathOptionIndex" or name == "mplsTunnelHopIndex" or name == "mplsTunnelHopAddrType" or name == "mplsTunnelHopAddrUnnum" or name == "mplsTunnelHopAsNumber" or name == "mplsTunnelHopEntryPathComp" or name == "mplsTunnelHopInclude" or name == "mplsTunnelHopIpAddr" or name == "mplsTunnelHopIpPrefixLen" or name == "mplsTunnelHopLspId" or name == "mplsTunnelHopPathOptionName" or name == "mplsTunnelHopRowStatus" or name == "mplsTunnelHopStorageType" or name == "mplsTunnelHopType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsTunnelHopListIndex"):
                    self.mplstunnelhoplistindex = value
                    self.mplstunnelhoplistindex.value_namespace = name_space
                    self.mplstunnelhoplistindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelHopPathOptionIndex"):
                    self.mplstunnelhoppathoptionindex = value
                    self.mplstunnelhoppathoptionindex.value_namespace = name_space
                    self.mplstunnelhoppathoptionindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelHopIndex"):
                    self.mplstunnelhopindex = value
                    self.mplstunnelhopindex.value_namespace = name_space
                    self.mplstunnelhopindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelHopAddrType"):
                    self.mplstunnelhopaddrtype = value
                    self.mplstunnelhopaddrtype.value_namespace = name_space
                    self.mplstunnelhopaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelHopAddrUnnum"):
                    self.mplstunnelhopaddrunnum = value
                    self.mplstunnelhopaddrunnum.value_namespace = name_space
                    self.mplstunnelhopaddrunnum.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelHopAsNumber"):
                    self.mplstunnelhopasnumber = value
                    self.mplstunnelhopasnumber.value_namespace = name_space
                    self.mplstunnelhopasnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelHopEntryPathComp"):
                    self.mplstunnelhopentrypathcomp = value
                    self.mplstunnelhopentrypathcomp.value_namespace = name_space
                    self.mplstunnelhopentrypathcomp.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelHopInclude"):
                    self.mplstunnelhopinclude = value
                    self.mplstunnelhopinclude.value_namespace = name_space
                    self.mplstunnelhopinclude.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelHopIpAddr"):
                    self.mplstunnelhopipaddr = value
                    self.mplstunnelhopipaddr.value_namespace = name_space
                    self.mplstunnelhopipaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelHopIpPrefixLen"):
                    self.mplstunnelhopipprefixlen = value
                    self.mplstunnelhopipprefixlen.value_namespace = name_space
                    self.mplstunnelhopipprefixlen.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelHopLspId"):
                    self.mplstunnelhoplspid = value
                    self.mplstunnelhoplspid.value_namespace = name_space
                    self.mplstunnelhoplspid.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelHopPathOptionName"):
                    self.mplstunnelhoppathoptionname = value
                    self.mplstunnelhoppathoptionname.value_namespace = name_space
                    self.mplstunnelhoppathoptionname.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelHopRowStatus"):
                    self.mplstunnelhoprowstatus = value
                    self.mplstunnelhoprowstatus.value_namespace = name_space
                    self.mplstunnelhoprowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelHopStorageType"):
                    self.mplstunnelhopstoragetype = value
                    self.mplstunnelhopstoragetype.value_namespace = name_space
                    self.mplstunnelhopstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelHopType"):
                    self.mplstunnelhoptype = value
                    self.mplstunnelhoptype.value_namespace = name_space
                    self.mplstunnelhoptype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplstunnelhopentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplstunnelhopentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsTunnelHopTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsTunnelHopEntry"):
                for c in self.mplstunnelhopentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsTeStdMib.Mplstunnelhoptable.Mplstunnelhopentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplstunnelhopentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsTunnelHopEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplstunnelresourcetable(Entity):
        """
        The mplsTunnelResourceTable allows a manager to
        specify which resources are desired for an MPLS
        tunnel.  This table also allows several tunnels to
        point to a single entry in this table, implying
        that these tunnels should share resources.
        
        .. attribute:: mplstunnelresourceentry
        
        	An entry in this table represents a set of resources for an MPLS tunnel.  An entry can be created by a network administrator or by an SNMP agent as instructed by any MPLS signalling protocol. An entry in this table referenced by a tunnel instance with zero mplsTunnelInstance value indicates a configured set of resource parameter. An entry referenced by a tunnel instance with a non\-zero mplsTunnelInstance reflects the in\-use resource parameters for the tunnel instance which may have been negotiated or modified by the MPLS signaling protocols
        	**type**\: list of    :py:class:`Mplstunnelresourceentry <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelresourcetable.Mplstunnelresourceentry>`
        
        

        """

        _prefix = 'MPLS-TE-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsTeStdMib.Mplstunnelresourcetable, self).__init__()

            self.yang_name = "mplsTunnelResourceTable"
            self.yang_parent_name = "MPLS-TE-STD-MIB"

            self.mplstunnelresourceentry = YList(self)

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
                        super(MplsTeStdMib.Mplstunnelresourcetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsTeStdMib.Mplstunnelresourcetable, self).__setattr__(name, value)


        class Mplstunnelresourceentry(Entity):
            """
            An entry in this table represents a set of resources
            for an MPLS tunnel.  An entry can be created by a
            network administrator or by an SNMP agent as
            instructed by any MPLS signalling protocol.
            An entry in this table referenced by a tunnel instance
            with zero mplsTunnelInstance value indicates a
            configured set of resource parameter. An entry
            referenced by a tunnel instance with a non\-zero
            mplsTunnelInstance reflects the in\-use resource
            parameters for the tunnel instance which may have
            been negotiated or modified by the MPLS signaling
            protocols.
            
            .. attribute:: mplstunnelresourceindex  <key>
            
            	Uniquely identifies this row
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: mplstunnelresourceexburstsize
            
            	The Excess burst size in bytes.  The implementations which do not implement this variable must return noSuchObject exception for this object and must not allow a user to set this value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: mplstunnelresourcefrequency
            
            	The granularity of the availability of committed rate.  The implementations which do not implement this variable must return unspecified(1) for this value and must not allow a user to set this value
            	**type**\:   :py:class:`Mplstunnelresourcefrequency <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelresourcetable.Mplstunnelresourceentry.Mplstunnelresourcefrequency>`
            
            .. attribute:: mplstunnelresourcemaxburstsize
            
            	The maximum burst size in bytes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: mplstunnelresourcemaxrate
            
            	The maximum rate in bits/second.  Note that setting mplsTunnelResourceMaxRate, mplsTunnelResourceMeanRate, and mplsTunnelResourceMaxBurstSize to 0 indicates best\- effort treatment
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilobits per second
            
            .. attribute:: mplstunnelresourcemeanburstsize
            
            	The mean burst size in bytes.  The implementations which do not implement this variable must return a noSuchObject exception for this object and must not allow a user to set this object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: mplstunnelresourcemeanrate
            
            	This object is copied into an instance of mplsTrafficParamMeanRate in the mplsTrafficParamTable. The OID of this table entry is then copied into the corresponding mplsInSegmentTrafficParamPtr
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilobits per second
            
            .. attribute:: mplstunnelresourcerowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table.  When a row in this table is in active(1) state, no objects in that row can be modified by the agent except mplsTunnelResourceRowStatus and mplsTunnelResourceStorageType
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: mplstunnelresourcestoragetype
            
            	The storage type for this Hop entry. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: mplstunnelresourceweight
            
            	The relative weight for using excess bandwidth above its committed rate.  The value of 0 means that weight is not applicable for the CR\-LSP
            	**type**\:  int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'MPLS-TE-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MplsTeStdMib.Mplstunnelresourcetable.Mplstunnelresourceentry, self).__init__()

                self.yang_name = "mplsTunnelResourceEntry"
                self.yang_parent_name = "mplsTunnelResourceTable"

                self.mplstunnelresourceindex = YLeaf(YType.uint32, "mplsTunnelResourceIndex")

                self.mplstunnelresourceexburstsize = YLeaf(YType.uint32, "mplsTunnelResourceExBurstSize")

                self.mplstunnelresourcefrequency = YLeaf(YType.enumeration, "mplsTunnelResourceFrequency")

                self.mplstunnelresourcemaxburstsize = YLeaf(YType.uint32, "mplsTunnelResourceMaxBurstSize")

                self.mplstunnelresourcemaxrate = YLeaf(YType.uint32, "mplsTunnelResourceMaxRate")

                self.mplstunnelresourcemeanburstsize = YLeaf(YType.uint32, "mplsTunnelResourceMeanBurstSize")

                self.mplstunnelresourcemeanrate = YLeaf(YType.uint32, "mplsTunnelResourceMeanRate")

                self.mplstunnelresourcerowstatus = YLeaf(YType.enumeration, "mplsTunnelResourceRowStatus")

                self.mplstunnelresourcestoragetype = YLeaf(YType.enumeration, "mplsTunnelResourceStorageType")

                self.mplstunnelresourceweight = YLeaf(YType.uint32, "mplsTunnelResourceWeight")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplstunnelresourceindex",
                                "mplstunnelresourceexburstsize",
                                "mplstunnelresourcefrequency",
                                "mplstunnelresourcemaxburstsize",
                                "mplstunnelresourcemaxrate",
                                "mplstunnelresourcemeanburstsize",
                                "mplstunnelresourcemeanrate",
                                "mplstunnelresourcerowstatus",
                                "mplstunnelresourcestoragetype",
                                "mplstunnelresourceweight") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsTeStdMib.Mplstunnelresourcetable.Mplstunnelresourceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsTeStdMib.Mplstunnelresourcetable.Mplstunnelresourceentry, self).__setattr__(name, value)

            class Mplstunnelresourcefrequency(Enum):
                """
                Mplstunnelresourcefrequency

                The granularity of the availability of committed

                rate.  The implementations which do not implement

                this variable must return unspecified(1) for this

                value and must not allow a user to set this value.

                .. data:: unspecified = 1

                .. data:: frequent = 2

                .. data:: veryFrequent = 3

                """

                unspecified = Enum.YLeaf(1, "unspecified")

                frequent = Enum.YLeaf(2, "frequent")

                veryFrequent = Enum.YLeaf(3, "veryFrequent")


            def has_data(self):
                return (
                    self.mplstunnelresourceindex.is_set or
                    self.mplstunnelresourceexburstsize.is_set or
                    self.mplstunnelresourcefrequency.is_set or
                    self.mplstunnelresourcemaxburstsize.is_set or
                    self.mplstunnelresourcemaxrate.is_set or
                    self.mplstunnelresourcemeanburstsize.is_set or
                    self.mplstunnelresourcemeanrate.is_set or
                    self.mplstunnelresourcerowstatus.is_set or
                    self.mplstunnelresourcestoragetype.is_set or
                    self.mplstunnelresourceweight.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplstunnelresourceindex.yfilter != YFilter.not_set or
                    self.mplstunnelresourceexburstsize.yfilter != YFilter.not_set or
                    self.mplstunnelresourcefrequency.yfilter != YFilter.not_set or
                    self.mplstunnelresourcemaxburstsize.yfilter != YFilter.not_set or
                    self.mplstunnelresourcemaxrate.yfilter != YFilter.not_set or
                    self.mplstunnelresourcemeanburstsize.yfilter != YFilter.not_set or
                    self.mplstunnelresourcemeanrate.yfilter != YFilter.not_set or
                    self.mplstunnelresourcerowstatus.yfilter != YFilter.not_set or
                    self.mplstunnelresourcestoragetype.yfilter != YFilter.not_set or
                    self.mplstunnelresourceweight.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsTunnelResourceEntry" + "[mplsTunnelResourceIndex='" + self.mplstunnelresourceindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/mplsTunnelResourceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplstunnelresourceindex.is_set or self.mplstunnelresourceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelresourceindex.get_name_leafdata())
                if (self.mplstunnelresourceexburstsize.is_set or self.mplstunnelresourceexburstsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelresourceexburstsize.get_name_leafdata())
                if (self.mplstunnelresourcefrequency.is_set or self.mplstunnelresourcefrequency.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelresourcefrequency.get_name_leafdata())
                if (self.mplstunnelresourcemaxburstsize.is_set or self.mplstunnelresourcemaxburstsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelresourcemaxburstsize.get_name_leafdata())
                if (self.mplstunnelresourcemaxrate.is_set or self.mplstunnelresourcemaxrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelresourcemaxrate.get_name_leafdata())
                if (self.mplstunnelresourcemeanburstsize.is_set or self.mplstunnelresourcemeanburstsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelresourcemeanburstsize.get_name_leafdata())
                if (self.mplstunnelresourcemeanrate.is_set or self.mplstunnelresourcemeanrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelresourcemeanrate.get_name_leafdata())
                if (self.mplstunnelresourcerowstatus.is_set or self.mplstunnelresourcerowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelresourcerowstatus.get_name_leafdata())
                if (self.mplstunnelresourcestoragetype.is_set or self.mplstunnelresourcestoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelresourcestoragetype.get_name_leafdata())
                if (self.mplstunnelresourceweight.is_set or self.mplstunnelresourceweight.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelresourceweight.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsTunnelResourceIndex" or name == "mplsTunnelResourceExBurstSize" or name == "mplsTunnelResourceFrequency" or name == "mplsTunnelResourceMaxBurstSize" or name == "mplsTunnelResourceMaxRate" or name == "mplsTunnelResourceMeanBurstSize" or name == "mplsTunnelResourceMeanRate" or name == "mplsTunnelResourceRowStatus" or name == "mplsTunnelResourceStorageType" or name == "mplsTunnelResourceWeight"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsTunnelResourceIndex"):
                    self.mplstunnelresourceindex = value
                    self.mplstunnelresourceindex.value_namespace = name_space
                    self.mplstunnelresourceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelResourceExBurstSize"):
                    self.mplstunnelresourceexburstsize = value
                    self.mplstunnelresourceexburstsize.value_namespace = name_space
                    self.mplstunnelresourceexburstsize.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelResourceFrequency"):
                    self.mplstunnelresourcefrequency = value
                    self.mplstunnelresourcefrequency.value_namespace = name_space
                    self.mplstunnelresourcefrequency.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelResourceMaxBurstSize"):
                    self.mplstunnelresourcemaxburstsize = value
                    self.mplstunnelresourcemaxburstsize.value_namespace = name_space
                    self.mplstunnelresourcemaxburstsize.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelResourceMaxRate"):
                    self.mplstunnelresourcemaxrate = value
                    self.mplstunnelresourcemaxrate.value_namespace = name_space
                    self.mplstunnelresourcemaxrate.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelResourceMeanBurstSize"):
                    self.mplstunnelresourcemeanburstsize = value
                    self.mplstunnelresourcemeanburstsize.value_namespace = name_space
                    self.mplstunnelresourcemeanburstsize.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelResourceMeanRate"):
                    self.mplstunnelresourcemeanrate = value
                    self.mplstunnelresourcemeanrate.value_namespace = name_space
                    self.mplstunnelresourcemeanrate.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelResourceRowStatus"):
                    self.mplstunnelresourcerowstatus = value
                    self.mplstunnelresourcerowstatus.value_namespace = name_space
                    self.mplstunnelresourcerowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelResourceStorageType"):
                    self.mplstunnelresourcestoragetype = value
                    self.mplstunnelresourcestoragetype.value_namespace = name_space
                    self.mplstunnelresourcestoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelResourceWeight"):
                    self.mplstunnelresourceweight = value
                    self.mplstunnelresourceweight.value_namespace = name_space
                    self.mplstunnelresourceweight.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplstunnelresourceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplstunnelresourceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsTunnelResourceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsTunnelResourceEntry"):
                for c in self.mplstunnelresourceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsTeStdMib.Mplstunnelresourcetable.Mplstunnelresourceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplstunnelresourceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsTunnelResourceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplstunnelarhoptable(Entity):
        """
        The mplsTunnelARHopTable is used to indicate the
        hops for an MPLS tunnel defined in mplsTunnelTable,
        as reported by the MPLS signalling protocol. Thus at
        a transit LSR, this table (if the table is supported
        and if the signaling protocol is recording actual
        route information) contains the actual route of the
        whole tunnel. If the signaling protocol is not
        recording the actual route, this table MAY report
        the information from the mplsTunnelHopTable or the
        mplsTunnelCHopTable.
        
        Each row in this table is indexed by
        mplsTunnelARHopListIndex. Each row also has a
        secondary index mplsTunnelARHopIndex, corresponding
        to the next hop that this row corresponds to.
        
        Please note that since the information necessary to
        build entries within this table is not provided by
        some MPLS signalling protocols, implementation of
        this table is optional. Furthermore, since the
        information in this table is actually provided by
        the MPLS signalling protocol after the path has
        been set\-up, the entries in this table are provided
        only for observation, and hence, all variables in
        this table are accessible exclusively as read\-
        only.
        
        Note also that the contents of this table may change
        while it is being read because of re\-routing
        activities. A network administrator may verify that
        the actual route read is consistent by reference to
        the mplsTunnelLastPathChange object.
        
        .. attribute:: mplstunnelarhopentry
        
        	An entry in this table represents a tunnel hop.  An entry is created by the agent for signaled ERLSP set up by an MPLS signalling protocol
        	**type**\: list of    :py:class:`Mplstunnelarhopentry <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelarhoptable.Mplstunnelarhopentry>`
        
        

        """

        _prefix = 'MPLS-TE-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsTeStdMib.Mplstunnelarhoptable, self).__init__()

            self.yang_name = "mplsTunnelARHopTable"
            self.yang_parent_name = "MPLS-TE-STD-MIB"

            self.mplstunnelarhopentry = YList(self)

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
                        super(MplsTeStdMib.Mplstunnelarhoptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsTeStdMib.Mplstunnelarhoptable, self).__setattr__(name, value)


        class Mplstunnelarhopentry(Entity):
            """
            An entry in this table represents a tunnel hop.  An
            entry is created by the agent for signaled ERLSP
            set up by an MPLS signalling protocol.
            
            .. attribute:: mplstunnelarhoplistindex  <key>
            
            	Primary index into this table identifying a particular recorded hop list
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplstunnelarhopindex  <key>
            
            	Secondary index into this table identifying the particular hop
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplstunnelarhopaddrtype
            
            	The Hop Address Type of this tunnel hop.  Note that lspid(5) is a valid option only for tunnels signaled via CRLDP
            	**type**\:   :py:class:`Tehopaddresstype <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.Tehopaddresstype>`
            
            .. attribute:: mplstunnelarhopaddrunnum
            
            	If mplsTunnelARHopAddrType is set to unnum(4), then this value will contain the interface identifier of the unnumbered interface for this hop. This object should be used in conjunction with mplsTunnelARHopIpAddr which would contain the LSR Router ID in this case. Otherwise the agent should set this object to zero\-length string and the manager should ignore this
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: mplstunnelarhopipaddr
            
            	The Tunnel Hop Address for this tunnel hop.  The type of this address is determined by the value of the corresponding mplsTunnelARHopAddrType. If mplsTunnelARHopAddrType is set to unnum(4),  then this value contains the LSR Router ID of the  unnumbered interface. Otherwise the agent SHOULD  set this object to the zero\-length string and the  manager should ignore this object
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mplstunnelarhoplspid
            
            	If mplsTunnelARHopAddrType is set to lspid(5), then this value will contain the LSP ID of this hop. This object is otherwise insignificant and should contain a value of 0 to indicate this fact
            	**type**\:  str
            
            	**length:** 2 \| 6
            
            

            """

            _prefix = 'MPLS-TE-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MplsTeStdMib.Mplstunnelarhoptable.Mplstunnelarhopentry, self).__init__()

                self.yang_name = "mplsTunnelARHopEntry"
                self.yang_parent_name = "mplsTunnelARHopTable"

                self.mplstunnelarhoplistindex = YLeaf(YType.uint32, "mplsTunnelARHopListIndex")

                self.mplstunnelarhopindex = YLeaf(YType.uint32, "mplsTunnelARHopIndex")

                self.mplstunnelarhopaddrtype = YLeaf(YType.enumeration, "mplsTunnelARHopAddrType")

                self.mplstunnelarhopaddrunnum = YLeaf(YType.str, "mplsTunnelARHopAddrUnnum")

                self.mplstunnelarhopipaddr = YLeaf(YType.str, "mplsTunnelARHopIpAddr")

                self.mplstunnelarhoplspid = YLeaf(YType.str, "mplsTunnelARHopLspId")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplstunnelarhoplistindex",
                                "mplstunnelarhopindex",
                                "mplstunnelarhopaddrtype",
                                "mplstunnelarhopaddrunnum",
                                "mplstunnelarhopipaddr",
                                "mplstunnelarhoplspid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsTeStdMib.Mplstunnelarhoptable.Mplstunnelarhopentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsTeStdMib.Mplstunnelarhoptable.Mplstunnelarhopentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.mplstunnelarhoplistindex.is_set or
                    self.mplstunnelarhopindex.is_set or
                    self.mplstunnelarhopaddrtype.is_set or
                    self.mplstunnelarhopaddrunnum.is_set or
                    self.mplstunnelarhopipaddr.is_set or
                    self.mplstunnelarhoplspid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplstunnelarhoplistindex.yfilter != YFilter.not_set or
                    self.mplstunnelarhopindex.yfilter != YFilter.not_set or
                    self.mplstunnelarhopaddrtype.yfilter != YFilter.not_set or
                    self.mplstunnelarhopaddrunnum.yfilter != YFilter.not_set or
                    self.mplstunnelarhopipaddr.yfilter != YFilter.not_set or
                    self.mplstunnelarhoplspid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsTunnelARHopEntry" + "[mplsTunnelARHopListIndex='" + self.mplstunnelarhoplistindex.get() + "']" + "[mplsTunnelARHopIndex='" + self.mplstunnelarhopindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/mplsTunnelARHopTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplstunnelarhoplistindex.is_set or self.mplstunnelarhoplistindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelarhoplistindex.get_name_leafdata())
                if (self.mplstunnelarhopindex.is_set or self.mplstunnelarhopindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelarhopindex.get_name_leafdata())
                if (self.mplstunnelarhopaddrtype.is_set or self.mplstunnelarhopaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelarhopaddrtype.get_name_leafdata())
                if (self.mplstunnelarhopaddrunnum.is_set or self.mplstunnelarhopaddrunnum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelarhopaddrunnum.get_name_leafdata())
                if (self.mplstunnelarhopipaddr.is_set or self.mplstunnelarhopipaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelarhopipaddr.get_name_leafdata())
                if (self.mplstunnelarhoplspid.is_set or self.mplstunnelarhoplspid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelarhoplspid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsTunnelARHopListIndex" or name == "mplsTunnelARHopIndex" or name == "mplsTunnelARHopAddrType" or name == "mplsTunnelARHopAddrUnnum" or name == "mplsTunnelARHopIpAddr" or name == "mplsTunnelARHopLspId"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsTunnelARHopListIndex"):
                    self.mplstunnelarhoplistindex = value
                    self.mplstunnelarhoplistindex.value_namespace = name_space
                    self.mplstunnelarhoplistindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelARHopIndex"):
                    self.mplstunnelarhopindex = value
                    self.mplstunnelarhopindex.value_namespace = name_space
                    self.mplstunnelarhopindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelARHopAddrType"):
                    self.mplstunnelarhopaddrtype = value
                    self.mplstunnelarhopaddrtype.value_namespace = name_space
                    self.mplstunnelarhopaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelARHopAddrUnnum"):
                    self.mplstunnelarhopaddrunnum = value
                    self.mplstunnelarhopaddrunnum.value_namespace = name_space
                    self.mplstunnelarhopaddrunnum.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelARHopIpAddr"):
                    self.mplstunnelarhopipaddr = value
                    self.mplstunnelarhopipaddr.value_namespace = name_space
                    self.mplstunnelarhopipaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelARHopLspId"):
                    self.mplstunnelarhoplspid = value
                    self.mplstunnelarhoplspid.value_namespace = name_space
                    self.mplstunnelarhoplspid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplstunnelarhopentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplstunnelarhopentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsTunnelARHopTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsTunnelARHopEntry"):
                for c in self.mplstunnelarhopentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsTeStdMib.Mplstunnelarhoptable.Mplstunnelarhopentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplstunnelarhopentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsTunnelARHopEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplstunnelchoptable(Entity):
        """
        The mplsTunnelCHopTable is used to indicate the
        hops, strict or loose, for an MPLS tunnel defined
        in mplsTunnelTable, as computed by a constraint\-
        based routing protocol, based on the
        mplsTunnelHopTable for the outgoing direction of
        the tunnel. Thus at a transit LSR, this table (if
        the table is supported) MAY contain the path
        computed by the CSPF engine on (or on behalf of)
        this LSR. Each row in this table is indexed by
        mplsTunnelCHopListIndex.  Each row also has a
        secondary index mplsTunnelCHopIndex, corresponding
        to the next hop that this row corresponds to. In
        case we want to specify a particular interface on
        the originating LSR of an outgoing tunnel by which
        we want packets to exit the LSR, we specify this as
        the first hop for this tunnel in
        mplsTunnelCHopTable.
        
        Please note that since the information necessary to
        build entries within this table may not be
        supported by some LSRs, implementation of this
        table is optional. Furthermore, since the
        information in this table describes the path
        computed by the CSPF engine the entries in this
        table are read\-only.
        
        .. attribute:: mplstunnelchopentry
        
        	An entry in this table represents a tunnel hop.  An entry in this table is created by a path computation engine using CSPF techniques applied to the information collected by routing protocols and the hops specified in the corresponding mplsTunnelHopTable
        	**type**\: list of    :py:class:`Mplstunnelchopentry <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelchoptable.Mplstunnelchopentry>`
        
        

        """

        _prefix = 'MPLS-TE-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsTeStdMib.Mplstunnelchoptable, self).__init__()

            self.yang_name = "mplsTunnelCHopTable"
            self.yang_parent_name = "MPLS-TE-STD-MIB"

            self.mplstunnelchopentry = YList(self)

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
                        super(MplsTeStdMib.Mplstunnelchoptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsTeStdMib.Mplstunnelchoptable, self).__setattr__(name, value)


        class Mplstunnelchopentry(Entity):
            """
            An entry in this table represents a tunnel hop.  An
            entry in this table is created by a path
            computation engine using CSPF techniques applied to
            the information collected by routing protocols and
            the hops specified in the corresponding
            mplsTunnelHopTable.
            
            .. attribute:: mplstunnelchoplistindex  <key>
            
            	Primary index into this table identifying a particular computed hop list
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplstunnelchopindex  <key>
            
            	Secondary index into this table identifying the particular hop
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplstunnelchopaddrtype
            
            	The Hop Address Type of this tunnel hop.  Note that lspid(5) is a valid option only for tunnels signaled via CRLDP
            	**type**\:   :py:class:`Tehopaddresstype <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.Tehopaddresstype>`
            
            .. attribute:: mplstunnelchopaddrunnum
            
            	If mplsTunnelCHopAddrType is set to unnum(4), then this value will contain the unnumbered interface identifier of this hop. This object should be used in conjunction with mplsTunnelCHopIpAddr which would contain the LSR Router ID in this case. Otherwise the agent should set this object to zero\- length string and the manager should ignore this
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: mplstunnelchopasnumber
            
            	If mplsTunnelCHopAddrType is set to asnumber(3), then this value will contain the AS number of this hop. Otherwise the agent should set this object to zero\-length string and the manager should ignore this
            	**type**\:  str
            
            	**length:** 4
            
            .. attribute:: mplstunnelchopipaddr
            
            	The Tunnel Hop Address for this tunnel hop. The type of this address is determined by the  value of the corresponding mplsTunnelCHopAddrType.  If mplsTunnelCHopAddrType is set to unnum(4), then  this value will contain the LSR Router ID of the  unnumbered interface. Otherwise the agent should  set this object to the zero\-length string and the  manager SHOULD ignore this object
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: mplstunnelchopipprefixlen
            
            	If mplsTunnelCHopAddrType is set to ipv4(1) or ipv6(2), then this value will contain an appropriate prefix length for the IP address in object mplsTunnelCHopIpAddr. Otherwise this value is irrelevant and should be ignored
            	**type**\:  int
            
            	**range:** 0..2040
            
            .. attribute:: mplstunnelchoplspid
            
            	If mplsTunnelCHopAddrType is set to lspid(5), then this value will contain the LSP ID of this hop. This object is otherwise insignificant and should contain a value of 0 to indicate this fact
            	**type**\:  str
            
            	**length:** 2 \| 6
            
            .. attribute:: mplstunnelchoptype
            
            	Denotes whether this is tunnel hop is routed in a strict or loose fashion
            	**type**\:   :py:class:`Mplstunnelchoptype <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelchoptable.Mplstunnelchopentry.Mplstunnelchoptype>`
            
            

            """

            _prefix = 'MPLS-TE-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MplsTeStdMib.Mplstunnelchoptable.Mplstunnelchopentry, self).__init__()

                self.yang_name = "mplsTunnelCHopEntry"
                self.yang_parent_name = "mplsTunnelCHopTable"

                self.mplstunnelchoplistindex = YLeaf(YType.uint32, "mplsTunnelCHopListIndex")

                self.mplstunnelchopindex = YLeaf(YType.uint32, "mplsTunnelCHopIndex")

                self.mplstunnelchopaddrtype = YLeaf(YType.enumeration, "mplsTunnelCHopAddrType")

                self.mplstunnelchopaddrunnum = YLeaf(YType.str, "mplsTunnelCHopAddrUnnum")

                self.mplstunnelchopasnumber = YLeaf(YType.str, "mplsTunnelCHopAsNumber")

                self.mplstunnelchopipaddr = YLeaf(YType.str, "mplsTunnelCHopIpAddr")

                self.mplstunnelchopipprefixlen = YLeaf(YType.uint32, "mplsTunnelCHopIpPrefixLen")

                self.mplstunnelchoplspid = YLeaf(YType.str, "mplsTunnelCHopLspId")

                self.mplstunnelchoptype = YLeaf(YType.enumeration, "mplsTunnelCHopType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplstunnelchoplistindex",
                                "mplstunnelchopindex",
                                "mplstunnelchopaddrtype",
                                "mplstunnelchopaddrunnum",
                                "mplstunnelchopasnumber",
                                "mplstunnelchopipaddr",
                                "mplstunnelchopipprefixlen",
                                "mplstunnelchoplspid",
                                "mplstunnelchoptype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsTeStdMib.Mplstunnelchoptable.Mplstunnelchopentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsTeStdMib.Mplstunnelchoptable.Mplstunnelchopentry, self).__setattr__(name, value)

            class Mplstunnelchoptype(Enum):
                """
                Mplstunnelchoptype

                Denotes whether this is tunnel hop is routed in a

                strict or loose fashion.

                .. data:: strict = 1

                .. data:: loose = 2

                """

                strict = Enum.YLeaf(1, "strict")

                loose = Enum.YLeaf(2, "loose")


            def has_data(self):
                return (
                    self.mplstunnelchoplistindex.is_set or
                    self.mplstunnelchopindex.is_set or
                    self.mplstunnelchopaddrtype.is_set or
                    self.mplstunnelchopaddrunnum.is_set or
                    self.mplstunnelchopasnumber.is_set or
                    self.mplstunnelchopipaddr.is_set or
                    self.mplstunnelchopipprefixlen.is_set or
                    self.mplstunnelchoplspid.is_set or
                    self.mplstunnelchoptype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplstunnelchoplistindex.yfilter != YFilter.not_set or
                    self.mplstunnelchopindex.yfilter != YFilter.not_set or
                    self.mplstunnelchopaddrtype.yfilter != YFilter.not_set or
                    self.mplstunnelchopaddrunnum.yfilter != YFilter.not_set or
                    self.mplstunnelchopasnumber.yfilter != YFilter.not_set or
                    self.mplstunnelchopipaddr.yfilter != YFilter.not_set or
                    self.mplstunnelchopipprefixlen.yfilter != YFilter.not_set or
                    self.mplstunnelchoplspid.yfilter != YFilter.not_set or
                    self.mplstunnelchoptype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsTunnelCHopEntry" + "[mplsTunnelCHopListIndex='" + self.mplstunnelchoplistindex.get() + "']" + "[mplsTunnelCHopIndex='" + self.mplstunnelchopindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/mplsTunnelCHopTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplstunnelchoplistindex.is_set or self.mplstunnelchoplistindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelchoplistindex.get_name_leafdata())
                if (self.mplstunnelchopindex.is_set or self.mplstunnelchopindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelchopindex.get_name_leafdata())
                if (self.mplstunnelchopaddrtype.is_set or self.mplstunnelchopaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelchopaddrtype.get_name_leafdata())
                if (self.mplstunnelchopaddrunnum.is_set or self.mplstunnelchopaddrunnum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelchopaddrunnum.get_name_leafdata())
                if (self.mplstunnelchopasnumber.is_set or self.mplstunnelchopasnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelchopasnumber.get_name_leafdata())
                if (self.mplstunnelchopipaddr.is_set or self.mplstunnelchopipaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelchopipaddr.get_name_leafdata())
                if (self.mplstunnelchopipprefixlen.is_set or self.mplstunnelchopipprefixlen.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelchopipprefixlen.get_name_leafdata())
                if (self.mplstunnelchoplspid.is_set or self.mplstunnelchoplspid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelchoplspid.get_name_leafdata())
                if (self.mplstunnelchoptype.is_set or self.mplstunnelchoptype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelchoptype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsTunnelCHopListIndex" or name == "mplsTunnelCHopIndex" or name == "mplsTunnelCHopAddrType" or name == "mplsTunnelCHopAddrUnnum" or name == "mplsTunnelCHopAsNumber" or name == "mplsTunnelCHopIpAddr" or name == "mplsTunnelCHopIpPrefixLen" or name == "mplsTunnelCHopLspId" or name == "mplsTunnelCHopType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsTunnelCHopListIndex"):
                    self.mplstunnelchoplistindex = value
                    self.mplstunnelchoplistindex.value_namespace = name_space
                    self.mplstunnelchoplistindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelCHopIndex"):
                    self.mplstunnelchopindex = value
                    self.mplstunnelchopindex.value_namespace = name_space
                    self.mplstunnelchopindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelCHopAddrType"):
                    self.mplstunnelchopaddrtype = value
                    self.mplstunnelchopaddrtype.value_namespace = name_space
                    self.mplstunnelchopaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelCHopAddrUnnum"):
                    self.mplstunnelchopaddrunnum = value
                    self.mplstunnelchopaddrunnum.value_namespace = name_space
                    self.mplstunnelchopaddrunnum.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelCHopAsNumber"):
                    self.mplstunnelchopasnumber = value
                    self.mplstunnelchopasnumber.value_namespace = name_space
                    self.mplstunnelchopasnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelCHopIpAddr"):
                    self.mplstunnelchopipaddr = value
                    self.mplstunnelchopipaddr.value_namespace = name_space
                    self.mplstunnelchopipaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelCHopIpPrefixLen"):
                    self.mplstunnelchopipprefixlen = value
                    self.mplstunnelchopipprefixlen.value_namespace = name_space
                    self.mplstunnelchopipprefixlen.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelCHopLspId"):
                    self.mplstunnelchoplspid = value
                    self.mplstunnelchoplspid.value_namespace = name_space
                    self.mplstunnelchoplspid.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelCHopType"):
                    self.mplstunnelchoptype = value
                    self.mplstunnelchoptype.value_namespace = name_space
                    self.mplstunnelchoptype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplstunnelchopentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplstunnelchopentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsTunnelCHopTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsTunnelCHopEntry"):
                for c in self.mplstunnelchopentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsTeStdMib.Mplstunnelchoptable.Mplstunnelchopentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplstunnelchopentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsTunnelCHopEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplstunnelcrldprestable(Entity):
        """
        The mplsTunnelCRLDPResTable allows a manager to
        specify which CR\-LDP\-specific resources are desired
        for an MPLS tunnel if that tunnel is signaled using
        CR\-LDP. Note that these attributes are in addition
        to those specified in mplsTunnelResourceTable. This
        table also allows several tunnels to point to a
        single entry in this table, implying that these
        tunnels should share resources.
        
        .. attribute:: mplstunnelcrldpresentry
        
        	An entry in this table represents a set of resources for an MPLS tunnel established using CRLDP (mplsTunnelSignallingProto equal to crldp (3)). An entry can be created by a network administrator or by an SNMP agent as instructed by any MPLS signalling protocol
        	**type**\: list of    :py:class:`Mplstunnelcrldpresentry <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelcrldprestable.Mplstunnelcrldpresentry>`
        
        

        """

        _prefix = 'MPLS-TE-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsTeStdMib.Mplstunnelcrldprestable, self).__init__()

            self.yang_name = "mplsTunnelCRLDPResTable"
            self.yang_parent_name = "MPLS-TE-STD-MIB"

            self.mplstunnelcrldpresentry = YList(self)

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
                        super(MplsTeStdMib.Mplstunnelcrldprestable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsTeStdMib.Mplstunnelcrldprestable, self).__setattr__(name, value)


        class Mplstunnelcrldpresentry(Entity):
            """
            An entry in this table represents a set of resources
            for an MPLS tunnel established using CRLDP
            (mplsTunnelSignallingProto equal to crldp (3)). An
            entry can be created by a network administrator or
            by an SNMP agent as instructed by any MPLS
            signalling protocol.
            
            .. attribute:: mplstunnelresourceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`mplstunnelresourceindex <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelresourcetable.Mplstunnelresourceentry>`
            
            .. attribute:: mplstunnelcrldpresexburstsize
            
            	The Excess burst size in bytes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: mplstunnelcrldpresflags
            
            	The value of the 1 byte Flags conveyed as part of the traffic parameters during the establishment of the CRLSP. The bits in this object are to be interpreted as follows.  +\-\-+\-\-+\-\-+\-\-+\-\-+\-\-+\-\-+\-\-+ \| Res \|F6\|F5\|F4\|F3\|F2\|F1\| +\-\-+\-\-+\-\-+\-\-+\-\-+\-\-+\-\-+\-\-+  Res \- These bits are reserved. Zero on transmission. Ignored on receipt. F1 \- Corresponds to the PDR. F2 \- Corresponds to the PBS. F3 \- Corresponds to the CDR. F4 \- Corresponds to the CBS. F5 \- Corresponds to the EBS. F6 \- Corresponds to the Weight.  Each flag if is a Negotiable Flag corresponding to a Traffic Parameter. The Negotiable Flag value zero denotes Not Negotiable and value one denotes Negotiable
            	**type**\:  int
            
            	**range:** 0..63
            
            .. attribute:: mplstunnelcrldpresfrequency
            
            	The granularity of the availability of committed rate
            	**type**\:   :py:class:`Mplstunnelcrldpresfrequency <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MplsTeStdMib.Mplstunnelcrldprestable.Mplstunnelcrldpresentry.Mplstunnelcrldpresfrequency>`
            
            .. attribute:: mplstunnelcrldpresmeanburstsize
            
            	The mean burst size in bytes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: mplstunnelcrldpresrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table.  When a row in this table is in active(1) state, no objects in that row can be modified by the agent except mplsTunnelCRLDPResRowStatus and mplsTunnelCRLDPResStorageType
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: mplstunnelcrldpresstoragetype
            
            	The storage type for this CR\-LDP Resource entry. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: mplstunnelcrldpresweight
            
            	The relative weight for using excess bandwidth above its committed rate.  The value of 0 means that weight is not applicable for the CR\-LSP
            	**type**\:  int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'MPLS-TE-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MplsTeStdMib.Mplstunnelcrldprestable.Mplstunnelcrldpresentry, self).__init__()

                self.yang_name = "mplsTunnelCRLDPResEntry"
                self.yang_parent_name = "mplsTunnelCRLDPResTable"

                self.mplstunnelresourceindex = YLeaf(YType.str, "mplsTunnelResourceIndex")

                self.mplstunnelcrldpresexburstsize = YLeaf(YType.uint32, "mplsTunnelCRLDPResExBurstSize")

                self.mplstunnelcrldpresflags = YLeaf(YType.uint32, "mplsTunnelCRLDPResFlags")

                self.mplstunnelcrldpresfrequency = YLeaf(YType.enumeration, "mplsTunnelCRLDPResFrequency")

                self.mplstunnelcrldpresmeanburstsize = YLeaf(YType.uint32, "mplsTunnelCRLDPResMeanBurstSize")

                self.mplstunnelcrldpresrowstatus = YLeaf(YType.enumeration, "mplsTunnelCRLDPResRowStatus")

                self.mplstunnelcrldpresstoragetype = YLeaf(YType.enumeration, "mplsTunnelCRLDPResStorageType")

                self.mplstunnelcrldpresweight = YLeaf(YType.uint32, "mplsTunnelCRLDPResWeight")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplstunnelresourceindex",
                                "mplstunnelcrldpresexburstsize",
                                "mplstunnelcrldpresflags",
                                "mplstunnelcrldpresfrequency",
                                "mplstunnelcrldpresmeanburstsize",
                                "mplstunnelcrldpresrowstatus",
                                "mplstunnelcrldpresstoragetype",
                                "mplstunnelcrldpresweight") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsTeStdMib.Mplstunnelcrldprestable.Mplstunnelcrldpresentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsTeStdMib.Mplstunnelcrldprestable.Mplstunnelcrldpresentry, self).__setattr__(name, value)

            class Mplstunnelcrldpresfrequency(Enum):
                """
                Mplstunnelcrldpresfrequency

                The granularity of the availability of committed

                rate.

                .. data:: unspecified = 1

                .. data:: frequent = 2

                .. data:: veryFrequent = 3

                """

                unspecified = Enum.YLeaf(1, "unspecified")

                frequent = Enum.YLeaf(2, "frequent")

                veryFrequent = Enum.YLeaf(3, "veryFrequent")


            def has_data(self):
                return (
                    self.mplstunnelresourceindex.is_set or
                    self.mplstunnelcrldpresexburstsize.is_set or
                    self.mplstunnelcrldpresflags.is_set or
                    self.mplstunnelcrldpresfrequency.is_set or
                    self.mplstunnelcrldpresmeanburstsize.is_set or
                    self.mplstunnelcrldpresrowstatus.is_set or
                    self.mplstunnelcrldpresstoragetype.is_set or
                    self.mplstunnelcrldpresweight.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplstunnelresourceindex.yfilter != YFilter.not_set or
                    self.mplstunnelcrldpresexburstsize.yfilter != YFilter.not_set or
                    self.mplstunnelcrldpresflags.yfilter != YFilter.not_set or
                    self.mplstunnelcrldpresfrequency.yfilter != YFilter.not_set or
                    self.mplstunnelcrldpresmeanburstsize.yfilter != YFilter.not_set or
                    self.mplstunnelcrldpresrowstatus.yfilter != YFilter.not_set or
                    self.mplstunnelcrldpresstoragetype.yfilter != YFilter.not_set or
                    self.mplstunnelcrldpresweight.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsTunnelCRLDPResEntry" + "[mplsTunnelResourceIndex='" + self.mplstunnelresourceindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/mplsTunnelCRLDPResTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplstunnelresourceindex.is_set or self.mplstunnelresourceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelresourceindex.get_name_leafdata())
                if (self.mplstunnelcrldpresexburstsize.is_set or self.mplstunnelcrldpresexburstsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelcrldpresexburstsize.get_name_leafdata())
                if (self.mplstunnelcrldpresflags.is_set or self.mplstunnelcrldpresflags.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelcrldpresflags.get_name_leafdata())
                if (self.mplstunnelcrldpresfrequency.is_set or self.mplstunnelcrldpresfrequency.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelcrldpresfrequency.get_name_leafdata())
                if (self.mplstunnelcrldpresmeanburstsize.is_set or self.mplstunnelcrldpresmeanburstsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelcrldpresmeanburstsize.get_name_leafdata())
                if (self.mplstunnelcrldpresrowstatus.is_set or self.mplstunnelcrldpresrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelcrldpresrowstatus.get_name_leafdata())
                if (self.mplstunnelcrldpresstoragetype.is_set or self.mplstunnelcrldpresstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelcrldpresstoragetype.get_name_leafdata())
                if (self.mplstunnelcrldpresweight.is_set or self.mplstunnelcrldpresweight.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplstunnelcrldpresweight.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsTunnelResourceIndex" or name == "mplsTunnelCRLDPResExBurstSize" or name == "mplsTunnelCRLDPResFlags" or name == "mplsTunnelCRLDPResFrequency" or name == "mplsTunnelCRLDPResMeanBurstSize" or name == "mplsTunnelCRLDPResRowStatus" or name == "mplsTunnelCRLDPResStorageType" or name == "mplsTunnelCRLDPResWeight"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsTunnelResourceIndex"):
                    self.mplstunnelresourceindex = value
                    self.mplstunnelresourceindex.value_namespace = name_space
                    self.mplstunnelresourceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelCRLDPResExBurstSize"):
                    self.mplstunnelcrldpresexburstsize = value
                    self.mplstunnelcrldpresexburstsize.value_namespace = name_space
                    self.mplstunnelcrldpresexburstsize.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelCRLDPResFlags"):
                    self.mplstunnelcrldpresflags = value
                    self.mplstunnelcrldpresflags.value_namespace = name_space
                    self.mplstunnelcrldpresflags.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelCRLDPResFrequency"):
                    self.mplstunnelcrldpresfrequency = value
                    self.mplstunnelcrldpresfrequency.value_namespace = name_space
                    self.mplstunnelcrldpresfrequency.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelCRLDPResMeanBurstSize"):
                    self.mplstunnelcrldpresmeanburstsize = value
                    self.mplstunnelcrldpresmeanburstsize.value_namespace = name_space
                    self.mplstunnelcrldpresmeanburstsize.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelCRLDPResRowStatus"):
                    self.mplstunnelcrldpresrowstatus = value
                    self.mplstunnelcrldpresrowstatus.value_namespace = name_space
                    self.mplstunnelcrldpresrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelCRLDPResStorageType"):
                    self.mplstunnelcrldpresstoragetype = value
                    self.mplstunnelcrldpresstoragetype.value_namespace = name_space
                    self.mplstunnelcrldpresstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsTunnelCRLDPResWeight"):
                    self.mplstunnelcrldpresweight = value
                    self.mplstunnelcrldpresweight.value_namespace = name_space
                    self.mplstunnelcrldpresweight.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplstunnelcrldpresentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplstunnelcrldpresentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsTunnelCRLDPResTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-TE-STD-MIB:MPLS-TE-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsTunnelCRLDPResEntry"):
                for c in self.mplstunnelcrldpresentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsTeStdMib.Mplstunnelcrldprestable.Mplstunnelcrldpresentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplstunnelcrldpresentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsTunnelCRLDPResEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.mplsteobjects is not None and self.mplsteobjects.has_data()) or
            (self.mplstescalars is not None and self.mplstescalars.has_data()) or
            (self.mplstunnelarhoptable is not None and self.mplstunnelarhoptable.has_data()) or
            (self.mplstunnelchoptable is not None and self.mplstunnelchoptable.has_data()) or
            (self.mplstunnelcrldprestable is not None and self.mplstunnelcrldprestable.has_data()) or
            (self.mplstunnelhoptable is not None and self.mplstunnelhoptable.has_data()) or
            (self.mplstunnelresourcetable is not None and self.mplstunnelresourcetable.has_data()) or
            (self.mplstunneltable is not None and self.mplstunneltable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.mplsteobjects is not None and self.mplsteobjects.has_operation()) or
            (self.mplstescalars is not None and self.mplstescalars.has_operation()) or
            (self.mplstunnelarhoptable is not None and self.mplstunnelarhoptable.has_operation()) or
            (self.mplstunnelchoptable is not None and self.mplstunnelchoptable.has_operation()) or
            (self.mplstunnelcrldprestable is not None and self.mplstunnelcrldprestable.has_operation()) or
            (self.mplstunnelhoptable is not None and self.mplstunnelhoptable.has_operation()) or
            (self.mplstunnelresourcetable is not None and self.mplstunnelresourcetable.has_operation()) or
            (self.mplstunneltable is not None and self.mplstunneltable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "MPLS-TE-STD-MIB:MPLS-TE-STD-MIB" + path_buffer

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

        if (child_yang_name == "mplsTeObjects"):
            if (self.mplsteobjects is None):
                self.mplsteobjects = MplsTeStdMib.Mplsteobjects()
                self.mplsteobjects.parent = self
                self._children_name_map["mplsteobjects"] = "mplsTeObjects"
            return self.mplsteobjects

        if (child_yang_name == "mplsTeScalars"):
            if (self.mplstescalars is None):
                self.mplstescalars = MplsTeStdMib.Mplstescalars()
                self.mplstescalars.parent = self
                self._children_name_map["mplstescalars"] = "mplsTeScalars"
            return self.mplstescalars

        if (child_yang_name == "mplsTunnelARHopTable"):
            if (self.mplstunnelarhoptable is None):
                self.mplstunnelarhoptable = MplsTeStdMib.Mplstunnelarhoptable()
                self.mplstunnelarhoptable.parent = self
                self._children_name_map["mplstunnelarhoptable"] = "mplsTunnelARHopTable"
            return self.mplstunnelarhoptable

        if (child_yang_name == "mplsTunnelCHopTable"):
            if (self.mplstunnelchoptable is None):
                self.mplstunnelchoptable = MplsTeStdMib.Mplstunnelchoptable()
                self.mplstunnelchoptable.parent = self
                self._children_name_map["mplstunnelchoptable"] = "mplsTunnelCHopTable"
            return self.mplstunnelchoptable

        if (child_yang_name == "mplsTunnelCRLDPResTable"):
            if (self.mplstunnelcrldprestable is None):
                self.mplstunnelcrldprestable = MplsTeStdMib.Mplstunnelcrldprestable()
                self.mplstunnelcrldprestable.parent = self
                self._children_name_map["mplstunnelcrldprestable"] = "mplsTunnelCRLDPResTable"
            return self.mplstunnelcrldprestable

        if (child_yang_name == "mplsTunnelHopTable"):
            if (self.mplstunnelhoptable is None):
                self.mplstunnelhoptable = MplsTeStdMib.Mplstunnelhoptable()
                self.mplstunnelhoptable.parent = self
                self._children_name_map["mplstunnelhoptable"] = "mplsTunnelHopTable"
            return self.mplstunnelhoptable

        if (child_yang_name == "mplsTunnelResourceTable"):
            if (self.mplstunnelresourcetable is None):
                self.mplstunnelresourcetable = MplsTeStdMib.Mplstunnelresourcetable()
                self.mplstunnelresourcetable.parent = self
                self._children_name_map["mplstunnelresourcetable"] = "mplsTunnelResourceTable"
            return self.mplstunnelresourcetable

        if (child_yang_name == "mplsTunnelTable"):
            if (self.mplstunneltable is None):
                self.mplstunneltable = MplsTeStdMib.Mplstunneltable()
                self.mplstunneltable.parent = self
                self._children_name_map["mplstunneltable"] = "mplsTunnelTable"
            return self.mplstunneltable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "mplsTeObjects" or name == "mplsTeScalars" or name == "mplsTunnelARHopTable" or name == "mplsTunnelCHopTable" or name == "mplsTunnelCRLDPResTable" or name == "mplsTunnelHopTable" or name == "mplsTunnelResourceTable" or name == "mplsTunnelTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = MplsTeStdMib()
        return self._top_entity


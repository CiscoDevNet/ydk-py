""" CISCO_OSPF_MIB 

An extension to the MIB module defined in
RFC 1850 for managing OSPF implimentation. 
Most of the MIB definitions are based on
the IETF draft 
< draft\-ietf\-ospf\-mib\-update\-05.txt > . 
Support for OSPF Sham link is also added

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoOspfMib(Entity):
    """
    
    
    .. attribute:: cospfgeneralgroup
    
    	
    	**type**\:   :py:class:`Cospfgeneralgroup <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfgeneralgroup>`
    
    .. attribute:: cospflocallsdbtable
    
    	The OSPF Process's Link\-Local Link State Database for non\-virtual links
    	**type**\:   :py:class:`Cospflocallsdbtable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospflocallsdbtable>`
    
    .. attribute:: cospflsdbtable
    
    	The OSPF Process's Link State Database. This  table is meant for Opaque LSA's
    	**type**\:   :py:class:`Cospflsdbtable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospflsdbtable>`
    
    .. attribute:: cospfshamlinknbrtable
    
    	A table of sham link neighbor information
    	**type**\:   :py:class:`Cospfshamlinknbrtable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfshamlinknbrtable>`
    
    .. attribute:: cospfshamlinkstable
    
    	Information about this router's sham links
    	**type**\:   :py:class:`Cospfshamlinkstable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfshamlinkstable>`
    
    .. attribute:: cospfshamlinktable
    
    	Information about this router's sham links
    	**type**\:   :py:class:`Cospfshamlinktable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfshamlinktable>`
    
    	**status**\: deprecated
    
    .. attribute:: cospfvirtlocallsdbtable
    
    	The OSPF Process's Link\-Local Link State Database for virtual links
    	**type**\:   :py:class:`Cospfvirtlocallsdbtable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfvirtlocallsdbtable>`
    
    

    """

    _prefix = 'CISCO-OSPF-MIB'
    _revision = '2003-07-18'

    def __init__(self):
        super(CiscoOspfMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-OSPF-MIB"
        self.yang_parent_name = "CISCO-OSPF-MIB"

        self.cospfgeneralgroup = CiscoOspfMib.Cospfgeneralgroup()
        self.cospfgeneralgroup.parent = self
        self._children_name_map["cospfgeneralgroup"] = "cospfGeneralGroup"
        self._children_yang_names.add("cospfGeneralGroup")

        self.cospflocallsdbtable = CiscoOspfMib.Cospflocallsdbtable()
        self.cospflocallsdbtable.parent = self
        self._children_name_map["cospflocallsdbtable"] = "cospfLocalLsdbTable"
        self._children_yang_names.add("cospfLocalLsdbTable")

        self.cospflsdbtable = CiscoOspfMib.Cospflsdbtable()
        self.cospflsdbtable.parent = self
        self._children_name_map["cospflsdbtable"] = "cospfLsdbTable"
        self._children_yang_names.add("cospfLsdbTable")

        self.cospfshamlinknbrtable = CiscoOspfMib.Cospfshamlinknbrtable()
        self.cospfshamlinknbrtable.parent = self
        self._children_name_map["cospfshamlinknbrtable"] = "cospfShamLinkNbrTable"
        self._children_yang_names.add("cospfShamLinkNbrTable")

        self.cospfshamlinkstable = CiscoOspfMib.Cospfshamlinkstable()
        self.cospfshamlinkstable.parent = self
        self._children_name_map["cospfshamlinkstable"] = "cospfShamLinksTable"
        self._children_yang_names.add("cospfShamLinksTable")

        self.cospfshamlinktable = CiscoOspfMib.Cospfshamlinktable()
        self.cospfshamlinktable.parent = self
        self._children_name_map["cospfshamlinktable"] = "cospfShamLinkTable"
        self._children_yang_names.add("cospfShamLinkTable")

        self.cospfvirtlocallsdbtable = CiscoOspfMib.Cospfvirtlocallsdbtable()
        self.cospfvirtlocallsdbtable.parent = self
        self._children_name_map["cospfvirtlocallsdbtable"] = "cospfVirtLocalLsdbTable"
        self._children_yang_names.add("cospfVirtLocalLsdbTable")


    class Cospfgeneralgroup(Entity):
        """
        
        
        .. attribute:: cospfopaqueaslsacksumsum
        
        	The 32\-bit unsigned sum of the Opaque AS  link\-state advertisements' LS checksums contained link state database
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cospfopaqueaslsacount
        
        	The total number of Opaque AS link\-state advertisements in the link state database
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cospfopaquelsasupport
        
        	The router's support for Opaque LSA types
        	**type**\:  bool
        
        .. attribute:: cospfrfc1583compatibility
        
        	Indicates metrics used to choose among multiple AS\- external\-LSAs. When cospfRFC1583Compatibility is set to enabled, only cost will be used when choosing among multiple AS\-external\-LSAs advertising the same destination. When cospfRFC1583Compatibility is set to disabled, preference will be driven first by type of path using cost only to break ties
        	**type**\:  bool
        
        .. attribute:: cospftrafficengineeringsupport
        
        	The router's support for OSPF traffic engineering
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            super(CiscoOspfMib.Cospfgeneralgroup, self).__init__()

            self.yang_name = "cospfGeneralGroup"
            self.yang_parent_name = "CISCO-OSPF-MIB"

            self.cospfopaqueaslsacksumsum = YLeaf(YType.uint32, "cospfOpaqueASLsaCksumSum")

            self.cospfopaqueaslsacount = YLeaf(YType.uint32, "cospfOpaqueASLsaCount")

            self.cospfopaquelsasupport = YLeaf(YType.boolean, "cospfOpaqueLsaSupport")

            self.cospfrfc1583compatibility = YLeaf(YType.boolean, "cospfRFC1583Compatibility")

            self.cospftrafficengineeringsupport = YLeaf(YType.boolean, "cospfTrafficEngineeringSupport")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cospfopaqueaslsacksumsum",
                            "cospfopaqueaslsacount",
                            "cospfopaquelsasupport",
                            "cospfrfc1583compatibility",
                            "cospftrafficengineeringsupport") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoOspfMib.Cospfgeneralgroup, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoOspfMib.Cospfgeneralgroup, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cospfopaqueaslsacksumsum.is_set or
                self.cospfopaqueaslsacount.is_set or
                self.cospfopaquelsasupport.is_set or
                self.cospfrfc1583compatibility.is_set or
                self.cospftrafficengineeringsupport.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cospfopaqueaslsacksumsum.yfilter != YFilter.not_set or
                self.cospfopaqueaslsacount.yfilter != YFilter.not_set or
                self.cospfopaquelsasupport.yfilter != YFilter.not_set or
                self.cospfrfc1583compatibility.yfilter != YFilter.not_set or
                self.cospftrafficengineeringsupport.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cospfGeneralGroup" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-OSPF-MIB:CISCO-OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cospfopaqueaslsacksumsum.is_set or self.cospfopaqueaslsacksumsum.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cospfopaqueaslsacksumsum.get_name_leafdata())
            if (self.cospfopaqueaslsacount.is_set or self.cospfopaqueaslsacount.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cospfopaqueaslsacount.get_name_leafdata())
            if (self.cospfopaquelsasupport.is_set or self.cospfopaquelsasupport.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cospfopaquelsasupport.get_name_leafdata())
            if (self.cospfrfc1583compatibility.is_set or self.cospfrfc1583compatibility.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cospfrfc1583compatibility.get_name_leafdata())
            if (self.cospftrafficengineeringsupport.is_set or self.cospftrafficengineeringsupport.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cospftrafficengineeringsupport.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cospfOpaqueASLsaCksumSum" or name == "cospfOpaqueASLsaCount" or name == "cospfOpaqueLsaSupport" or name == "cospfRFC1583Compatibility" or name == "cospfTrafficEngineeringSupport"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cospfOpaqueASLsaCksumSum"):
                self.cospfopaqueaslsacksumsum = value
                self.cospfopaqueaslsacksumsum.value_namespace = name_space
                self.cospfopaqueaslsacksumsum.value_namespace_prefix = name_space_prefix
            if(value_path == "cospfOpaqueASLsaCount"):
                self.cospfopaqueaslsacount = value
                self.cospfopaqueaslsacount.value_namespace = name_space
                self.cospfopaqueaslsacount.value_namespace_prefix = name_space_prefix
            if(value_path == "cospfOpaqueLsaSupport"):
                self.cospfopaquelsasupport = value
                self.cospfopaquelsasupport.value_namespace = name_space
                self.cospfopaquelsasupport.value_namespace_prefix = name_space_prefix
            if(value_path == "cospfRFC1583Compatibility"):
                self.cospfrfc1583compatibility = value
                self.cospfrfc1583compatibility.value_namespace = name_space
                self.cospfrfc1583compatibility.value_namespace_prefix = name_space_prefix
            if(value_path == "cospfTrafficEngineeringSupport"):
                self.cospftrafficengineeringsupport = value
                self.cospftrafficengineeringsupport.value_namespace = name_space
                self.cospftrafficengineeringsupport.value_namespace_prefix = name_space_prefix


    class Cospflsdbtable(Entity):
        """
        The OSPF Process's Link State Database. This 
        table is meant for Opaque LSA's
        
        .. attribute:: cospflsdbentry
        
        	A single Link State Advertisement
        	**type**\: list of    :py:class:`Cospflsdbentry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospflsdbtable.Cospflsdbentry>`
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            super(CiscoOspfMib.Cospflsdbtable, self).__init__()

            self.yang_name = "cospfLsdbTable"
            self.yang_parent_name = "CISCO-OSPF-MIB"

            self.cospflsdbentry = YList(self)

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
                        super(CiscoOspfMib.Cospflsdbtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoOspfMib.Cospflsdbtable, self).__setattr__(name, value)


        class Cospflsdbentry(Entity):
            """
            A single Link State Advertisement.
            
            .. attribute:: ospflsdbareaid  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ospflsdbareaid <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospflsdbtable.Ospflsdbentry>`
            
            .. attribute:: cospflsdbtype  <key>
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\:   :py:class:`Cospflsdbtype <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospflsdbtable.Cospflsdbentry.Cospflsdbtype>`
            
            .. attribute:: ospflsdblsid  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ospflsdblsid <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospflsdbtable.Ospflsdbentry>`
            
            .. attribute:: ospflsdbrouterid  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ospflsdbrouterid <ydk.models.cisco_ios_xe.OSPF_MIB.OspfMib.Ospflsdbtable.Ospflsdbentry>`
            
            .. attribute:: cospflsdbadvertisement
            
            	The entire Link State Advertisement, including its header
            	**type**\:  str
            
            	**length:** 1..65535
            
            .. attribute:: cospflsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cospflsdbchecksum
            
            	This field is the  checksum  of  the  complete contents  of  the  advertisement, excepting the age field.  The age field is excepted  so  that an   advertisement's  age  can  be  incremented without updating the  checksum.   The  checksum used  is  the same that is used for ISO connectionless datagrams; it is commonly referred  to as the Fletcher checksum
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cospflsdbsequence
            
            	The sequence number field is a  signed  32\-bit integer.   It  is used to detect old and duplicate link state advertisements.  The  space  of sequence  numbers  is  linearly  ordered.   The larger the sequence number the more recent  the advertisement
            	**type**\:  int
            
            	**range:** 1..147483647
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                super(CiscoOspfMib.Cospflsdbtable.Cospflsdbentry, self).__init__()

                self.yang_name = "cospfLsdbEntry"
                self.yang_parent_name = "cospfLsdbTable"

                self.ospflsdbareaid = YLeaf(YType.str, "ospfLsdbAreaId")

                self.cospflsdbtype = YLeaf(YType.enumeration, "cospfLsdbType")

                self.ospflsdblsid = YLeaf(YType.str, "ospfLsdbLsid")

                self.ospflsdbrouterid = YLeaf(YType.str, "ospfLsdbRouterId")

                self.cospflsdbadvertisement = YLeaf(YType.str, "cospfLsdbAdvertisement")

                self.cospflsdbage = YLeaf(YType.int32, "cospfLsdbAge")

                self.cospflsdbchecksum = YLeaf(YType.int32, "cospfLsdbChecksum")

                self.cospflsdbsequence = YLeaf(YType.int32, "cospfLsdbSequence")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ospflsdbareaid",
                                "cospflsdbtype",
                                "ospflsdblsid",
                                "ospflsdbrouterid",
                                "cospflsdbadvertisement",
                                "cospflsdbage",
                                "cospflsdbchecksum",
                                "cospflsdbsequence") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoOspfMib.Cospflsdbtable.Cospflsdbentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoOspfMib.Cospflsdbtable.Cospflsdbentry, self).__setattr__(name, value)

            class Cospflsdbtype(Enum):
                """
                Cospflsdbtype

                The type of the link state advertisement.

                Each link state type has a separate advertisement format.

                .. data:: areaOpaqueLink = 10

                .. data:: asOpaqueLink = 11

                """

                areaOpaqueLink = Enum.YLeaf(10, "areaOpaqueLink")

                asOpaqueLink = Enum.YLeaf(11, "asOpaqueLink")


            def has_data(self):
                return (
                    self.ospflsdbareaid.is_set or
                    self.cospflsdbtype.is_set or
                    self.ospflsdblsid.is_set or
                    self.ospflsdbrouterid.is_set or
                    self.cospflsdbadvertisement.is_set or
                    self.cospflsdbage.is_set or
                    self.cospflsdbchecksum.is_set or
                    self.cospflsdbsequence.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ospflsdbareaid.yfilter != YFilter.not_set or
                    self.cospflsdbtype.yfilter != YFilter.not_set or
                    self.ospflsdblsid.yfilter != YFilter.not_set or
                    self.ospflsdbrouterid.yfilter != YFilter.not_set or
                    self.cospflsdbadvertisement.yfilter != YFilter.not_set or
                    self.cospflsdbage.yfilter != YFilter.not_set or
                    self.cospflsdbchecksum.yfilter != YFilter.not_set or
                    self.cospflsdbsequence.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cospfLsdbEntry" + "[ospfLsdbAreaId='" + self.ospflsdbareaid.get() + "']" + "[cospfLsdbType='" + self.cospflsdbtype.get() + "']" + "[ospfLsdbLsid='" + self.ospflsdblsid.get() + "']" + "[ospfLsdbRouterId='" + self.ospflsdbrouterid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-OSPF-MIB:CISCO-OSPF-MIB/cospfLsdbTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ospflsdbareaid.is_set or self.ospflsdbareaid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospflsdbareaid.get_name_leafdata())
                if (self.cospflsdbtype.is_set or self.cospflsdbtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospflsdbtype.get_name_leafdata())
                if (self.ospflsdblsid.is_set or self.ospflsdblsid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospflsdblsid.get_name_leafdata())
                if (self.ospflsdbrouterid.is_set or self.ospflsdbrouterid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ospflsdbrouterid.get_name_leafdata())
                if (self.cospflsdbadvertisement.is_set or self.cospflsdbadvertisement.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospflsdbadvertisement.get_name_leafdata())
                if (self.cospflsdbage.is_set or self.cospflsdbage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospflsdbage.get_name_leafdata())
                if (self.cospflsdbchecksum.is_set or self.cospflsdbchecksum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospflsdbchecksum.get_name_leafdata())
                if (self.cospflsdbsequence.is_set or self.cospflsdbsequence.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospflsdbsequence.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ospfLsdbAreaId" or name == "cospfLsdbType" or name == "ospfLsdbLsid" or name == "ospfLsdbRouterId" or name == "cospfLsdbAdvertisement" or name == "cospfLsdbAge" or name == "cospfLsdbChecksum" or name == "cospfLsdbSequence"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ospfLsdbAreaId"):
                    self.ospflsdbareaid = value
                    self.ospflsdbareaid.value_namespace = name_space
                    self.ospflsdbareaid.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfLsdbType"):
                    self.cospflsdbtype = value
                    self.cospflsdbtype.value_namespace = name_space
                    self.cospflsdbtype.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfLsdbLsid"):
                    self.ospflsdblsid = value
                    self.ospflsdblsid.value_namespace = name_space
                    self.ospflsdblsid.value_namespace_prefix = name_space_prefix
                if(value_path == "ospfLsdbRouterId"):
                    self.ospflsdbrouterid = value
                    self.ospflsdbrouterid.value_namespace = name_space
                    self.ospflsdbrouterid.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfLsdbAdvertisement"):
                    self.cospflsdbadvertisement = value
                    self.cospflsdbadvertisement.value_namespace = name_space
                    self.cospflsdbadvertisement.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfLsdbAge"):
                    self.cospflsdbage = value
                    self.cospflsdbage.value_namespace = name_space
                    self.cospflsdbage.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfLsdbChecksum"):
                    self.cospflsdbchecksum = value
                    self.cospflsdbchecksum.value_namespace = name_space
                    self.cospflsdbchecksum.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfLsdbSequence"):
                    self.cospflsdbsequence = value
                    self.cospflsdbsequence.value_namespace = name_space
                    self.cospflsdbsequence.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cospflsdbentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cospflsdbentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cospfLsdbTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-OSPF-MIB:CISCO-OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cospfLsdbEntry"):
                for c in self.cospflsdbentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoOspfMib.Cospflsdbtable.Cospflsdbentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cospflsdbentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cospfLsdbEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cospfshamlinktable(Entity):
        """
        Information about this router's sham links
        
        .. attribute:: cospfshamlinkentry
        
        	Information about a single sham link
        	**type**\: list of    :py:class:`Cospfshamlinkentry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfshamlinktable.Cospfshamlinkentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            super(CiscoOspfMib.Cospfshamlinktable, self).__init__()

            self.yang_name = "cospfShamLinkTable"
            self.yang_parent_name = "CISCO-OSPF-MIB"

            self.cospfshamlinkentry = YList(self)

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
                        super(CiscoOspfMib.Cospfshamlinktable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoOspfMib.Cospfshamlinktable, self).__setattr__(name, value)


        class Cospfshamlinkentry(Entity):
            """
            Information about a single sham link
            
            .. attribute:: cospfshamlinkareaid  <key>
            
            	The  Transit  Area  that  the   Virtual   Link traverses.  By definition, this is not 0.0.0.0
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinklocalipaddress  <key>
            
            	The Local IP address of the sham link
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkneighborid  <key>
            
            	The Router ID of the other end router of the sham link
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkevents
            
            	The number of state changes or error events on this sham link
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkhellointerval
            
            	The length of time, in  seconds,  between  the Hello  packets that the router sends on the sham link
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkmetric
            
            	The Metric to be advertised
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkretransinterval
            
            	The number of seconds between  link\-state  advertisement retransmissions,  for  adjacencies belonging to this  link.   This  value  is also used when retransmitting database description   and  link\-state  request  packets. This value   should  be well over the expected round trip time
            	**type**\:  int
            
            	**range:** 0..3600
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkrtrdeadinterval
            
            	The number of seconds that  a  router's  Hello packets  have  not been seen before it's neighbors declare the router down.  This  should  be some  multiple  of  the  Hello  interval
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkstate
            
            	OSPF sham link states
            	**type**\:   :py:class:`Cospfshamlinkstate <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfshamlinktable.Cospfshamlinkentry.Cospfshamlinkstate>`
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                super(CiscoOspfMib.Cospfshamlinktable.Cospfshamlinkentry, self).__init__()

                self.yang_name = "cospfShamLinkEntry"
                self.yang_parent_name = "cospfShamLinkTable"

                self.cospfshamlinkareaid = YLeaf(YType.str, "cospfShamLinkAreaId")

                self.cospfshamlinklocalipaddress = YLeaf(YType.str, "cospfShamLinkLocalIpAddress")

                self.cospfshamlinkneighborid = YLeaf(YType.str, "cospfShamLinkNeighborId")

                self.cospfshamlinkevents = YLeaf(YType.uint32, "cospfShamLinkEvents")

                self.cospfshamlinkhellointerval = YLeaf(YType.int32, "cospfShamLinkHelloInterval")

                self.cospfshamlinkmetric = YLeaf(YType.int32, "cospfShamLinkMetric")

                self.cospfshamlinkretransinterval = YLeaf(YType.int32, "cospfShamLinkRetransInterval")

                self.cospfshamlinkrtrdeadinterval = YLeaf(YType.int32, "cospfShamLinkRtrDeadInterval")

                self.cospfshamlinkstate = YLeaf(YType.enumeration, "cospfShamLinkState")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cospfshamlinkareaid",
                                "cospfshamlinklocalipaddress",
                                "cospfshamlinkneighborid",
                                "cospfshamlinkevents",
                                "cospfshamlinkhellointerval",
                                "cospfshamlinkmetric",
                                "cospfshamlinkretransinterval",
                                "cospfshamlinkrtrdeadinterval",
                                "cospfshamlinkstate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoOspfMib.Cospfshamlinktable.Cospfshamlinkentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoOspfMib.Cospfshamlinktable.Cospfshamlinkentry, self).__setattr__(name, value)

            class Cospfshamlinkstate(Enum):
                """
                Cospfshamlinkstate

                OSPF sham link states.

                .. data:: down = 1

                .. data:: pointToPoint = 4

                """

                down = Enum.YLeaf(1, "down")

                pointToPoint = Enum.YLeaf(4, "pointToPoint")


            def has_data(self):
                return (
                    self.cospfshamlinkareaid.is_set or
                    self.cospfshamlinklocalipaddress.is_set or
                    self.cospfshamlinkneighborid.is_set or
                    self.cospfshamlinkevents.is_set or
                    self.cospfshamlinkhellointerval.is_set or
                    self.cospfshamlinkmetric.is_set or
                    self.cospfshamlinkretransinterval.is_set or
                    self.cospfshamlinkrtrdeadinterval.is_set or
                    self.cospfshamlinkstate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cospfshamlinkareaid.yfilter != YFilter.not_set or
                    self.cospfshamlinklocalipaddress.yfilter != YFilter.not_set or
                    self.cospfshamlinkneighborid.yfilter != YFilter.not_set or
                    self.cospfshamlinkevents.yfilter != YFilter.not_set or
                    self.cospfshamlinkhellointerval.yfilter != YFilter.not_set or
                    self.cospfshamlinkmetric.yfilter != YFilter.not_set or
                    self.cospfshamlinkretransinterval.yfilter != YFilter.not_set or
                    self.cospfshamlinkrtrdeadinterval.yfilter != YFilter.not_set or
                    self.cospfshamlinkstate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cospfShamLinkEntry" + "[cospfShamLinkAreaId='" + self.cospfshamlinkareaid.get() + "']" + "[cospfShamLinkLocalIpAddress='" + self.cospfshamlinklocalipaddress.get() + "']" + "[cospfShamLinkNeighborId='" + self.cospfshamlinkneighborid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-OSPF-MIB:CISCO-OSPF-MIB/cospfShamLinkTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cospfshamlinkareaid.is_set or self.cospfshamlinkareaid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinkareaid.get_name_leafdata())
                if (self.cospfshamlinklocalipaddress.is_set or self.cospfshamlinklocalipaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinklocalipaddress.get_name_leafdata())
                if (self.cospfshamlinkneighborid.is_set or self.cospfshamlinkneighborid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinkneighborid.get_name_leafdata())
                if (self.cospfshamlinkevents.is_set or self.cospfshamlinkevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinkevents.get_name_leafdata())
                if (self.cospfshamlinkhellointerval.is_set or self.cospfshamlinkhellointerval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinkhellointerval.get_name_leafdata())
                if (self.cospfshamlinkmetric.is_set or self.cospfshamlinkmetric.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinkmetric.get_name_leafdata())
                if (self.cospfshamlinkretransinterval.is_set or self.cospfshamlinkretransinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinkretransinterval.get_name_leafdata())
                if (self.cospfshamlinkrtrdeadinterval.is_set or self.cospfshamlinkrtrdeadinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinkrtrdeadinterval.get_name_leafdata())
                if (self.cospfshamlinkstate.is_set or self.cospfshamlinkstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinkstate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cospfShamLinkAreaId" or name == "cospfShamLinkLocalIpAddress" or name == "cospfShamLinkNeighborId" or name == "cospfShamLinkEvents" or name == "cospfShamLinkHelloInterval" or name == "cospfShamLinkMetric" or name == "cospfShamLinkRetransInterval" or name == "cospfShamLinkRtrDeadInterval" or name == "cospfShamLinkState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cospfShamLinkAreaId"):
                    self.cospfshamlinkareaid = value
                    self.cospfshamlinkareaid.value_namespace = name_space
                    self.cospfshamlinkareaid.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinkLocalIpAddress"):
                    self.cospfshamlinklocalipaddress = value
                    self.cospfshamlinklocalipaddress.value_namespace = name_space
                    self.cospfshamlinklocalipaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinkNeighborId"):
                    self.cospfshamlinkneighborid = value
                    self.cospfshamlinkneighborid.value_namespace = name_space
                    self.cospfshamlinkneighborid.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinkEvents"):
                    self.cospfshamlinkevents = value
                    self.cospfshamlinkevents.value_namespace = name_space
                    self.cospfshamlinkevents.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinkHelloInterval"):
                    self.cospfshamlinkhellointerval = value
                    self.cospfshamlinkhellointerval.value_namespace = name_space
                    self.cospfshamlinkhellointerval.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinkMetric"):
                    self.cospfshamlinkmetric = value
                    self.cospfshamlinkmetric.value_namespace = name_space
                    self.cospfshamlinkmetric.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinkRetransInterval"):
                    self.cospfshamlinkretransinterval = value
                    self.cospfshamlinkretransinterval.value_namespace = name_space
                    self.cospfshamlinkretransinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinkRtrDeadInterval"):
                    self.cospfshamlinkrtrdeadinterval = value
                    self.cospfshamlinkrtrdeadinterval.value_namespace = name_space
                    self.cospfshamlinkrtrdeadinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinkState"):
                    self.cospfshamlinkstate = value
                    self.cospfshamlinkstate.value_namespace = name_space
                    self.cospfshamlinkstate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cospfshamlinkentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cospfshamlinkentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cospfShamLinkTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-OSPF-MIB:CISCO-OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cospfShamLinkEntry"):
                for c in self.cospfshamlinkentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoOspfMib.Cospfshamlinktable.Cospfshamlinkentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cospfshamlinkentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cospfShamLinkEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cospflocallsdbtable(Entity):
        """
        The OSPF Process's Link\-Local Link State Database
        for non\-virtual links.
        
        .. attribute:: cospflocallsdbentry
        
        	A single Link State Advertisement
        	**type**\: list of    :py:class:`Cospflocallsdbentry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospflocallsdbtable.Cospflocallsdbentry>`
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            super(CiscoOspfMib.Cospflocallsdbtable, self).__init__()

            self.yang_name = "cospfLocalLsdbTable"
            self.yang_parent_name = "CISCO-OSPF-MIB"

            self.cospflocallsdbentry = YList(self)

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
                        super(CiscoOspfMib.Cospflocallsdbtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoOspfMib.Cospflocallsdbtable, self).__setattr__(name, value)


        class Cospflocallsdbentry(Entity):
            """
            A single Link State Advertisement.
            
            .. attribute:: cospflocallsdbipaddress  <key>
            
            	The IP Address of the interface from which the LSA was received if the interface is numbered
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospflocallsdbaddresslessif  <key>
            
            	The Interface Index of the interface from which the LSA was received if the interface is unnumbered
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cospflocallsdbtype  <key>
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\:   :py:class:`Cospflocallsdbtype <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospflocallsdbtable.Cospflocallsdbentry.Cospflocallsdbtype>`
            
            .. attribute:: cospflocallsdblsid  <key>
            
            	The Link State ID is an LS Type Specific field containing a 32 bit identifier in IP address format; it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospflocallsdbrouterid  <key>
            
            	The 32 bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospflocallsdbadvertisement
            
            	The entire Link State Advertisement, including its header
            	**type**\:  str
            
            	**length:** 1..65535
            
            .. attribute:: cospflocallsdbage
            
            	This field is the age of the link state advertisement  in seconds
            	**type**\:  int
            
            	**range:** 0..3600
            
            .. attribute:: cospflocallsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field. The age field is excepted so that an advertisement's age can be incremented without updating the checksum. The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred  to as the Fletcher checksum
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospflocallsdbsequence
            
            	The sequence number field is a signed 32\-bit integer. It is used to detect old and duplicate link state advertisements. The space of sequence numbers is linearly ordered. The larger the sequence number the more recent the advertisement
            	**type**\:  int
            
            	**range:** \-2147483647..2147483647
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                super(CiscoOspfMib.Cospflocallsdbtable.Cospflocallsdbentry, self).__init__()

                self.yang_name = "cospfLocalLsdbEntry"
                self.yang_parent_name = "cospfLocalLsdbTable"

                self.cospflocallsdbipaddress = YLeaf(YType.str, "cospfLocalLsdbIpAddress")

                self.cospflocallsdbaddresslessif = YLeaf(YType.int32, "cospfLocalLsdbAddressLessIf")

                self.cospflocallsdbtype = YLeaf(YType.enumeration, "cospfLocalLsdbType")

                self.cospflocallsdblsid = YLeaf(YType.str, "cospfLocalLsdbLsid")

                self.cospflocallsdbrouterid = YLeaf(YType.str, "cospfLocalLsdbRouterId")

                self.cospflocallsdbadvertisement = YLeaf(YType.str, "cospfLocalLsdbAdvertisement")

                self.cospflocallsdbage = YLeaf(YType.int32, "cospfLocalLsdbAge")

                self.cospflocallsdbchecksum = YLeaf(YType.uint32, "cospfLocalLsdbChecksum")

                self.cospflocallsdbsequence = YLeaf(YType.int32, "cospfLocalLsdbSequence")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cospflocallsdbipaddress",
                                "cospflocallsdbaddresslessif",
                                "cospflocallsdbtype",
                                "cospflocallsdblsid",
                                "cospflocallsdbrouterid",
                                "cospflocallsdbadvertisement",
                                "cospflocallsdbage",
                                "cospflocallsdbchecksum",
                                "cospflocallsdbsequence") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoOspfMib.Cospflocallsdbtable.Cospflocallsdbentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoOspfMib.Cospflocallsdbtable.Cospflocallsdbentry, self).__setattr__(name, value)

            class Cospflocallsdbtype(Enum):
                """
                Cospflocallsdbtype

                The type of the link state advertisement.

                Each link state type has a separate advertisement format.

                .. data:: localOpaqueLink = 9

                """

                localOpaqueLink = Enum.YLeaf(9, "localOpaqueLink")


            def has_data(self):
                return (
                    self.cospflocallsdbipaddress.is_set or
                    self.cospflocallsdbaddresslessif.is_set or
                    self.cospflocallsdbtype.is_set or
                    self.cospflocallsdblsid.is_set or
                    self.cospflocallsdbrouterid.is_set or
                    self.cospflocallsdbadvertisement.is_set or
                    self.cospflocallsdbage.is_set or
                    self.cospflocallsdbchecksum.is_set or
                    self.cospflocallsdbsequence.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cospflocallsdbipaddress.yfilter != YFilter.not_set or
                    self.cospflocallsdbaddresslessif.yfilter != YFilter.not_set or
                    self.cospflocallsdbtype.yfilter != YFilter.not_set or
                    self.cospflocallsdblsid.yfilter != YFilter.not_set or
                    self.cospflocallsdbrouterid.yfilter != YFilter.not_set or
                    self.cospflocallsdbadvertisement.yfilter != YFilter.not_set or
                    self.cospflocallsdbage.yfilter != YFilter.not_set or
                    self.cospflocallsdbchecksum.yfilter != YFilter.not_set or
                    self.cospflocallsdbsequence.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cospfLocalLsdbEntry" + "[cospfLocalLsdbIpAddress='" + self.cospflocallsdbipaddress.get() + "']" + "[cospfLocalLsdbAddressLessIf='" + self.cospflocallsdbaddresslessif.get() + "']" + "[cospfLocalLsdbType='" + self.cospflocallsdbtype.get() + "']" + "[cospfLocalLsdbLsid='" + self.cospflocallsdblsid.get() + "']" + "[cospfLocalLsdbRouterId='" + self.cospflocallsdbrouterid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-OSPF-MIB:CISCO-OSPF-MIB/cospfLocalLsdbTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cospflocallsdbipaddress.is_set or self.cospflocallsdbipaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospflocallsdbipaddress.get_name_leafdata())
                if (self.cospflocallsdbaddresslessif.is_set or self.cospflocallsdbaddresslessif.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospflocallsdbaddresslessif.get_name_leafdata())
                if (self.cospflocallsdbtype.is_set or self.cospflocallsdbtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospflocallsdbtype.get_name_leafdata())
                if (self.cospflocallsdblsid.is_set or self.cospflocallsdblsid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospflocallsdblsid.get_name_leafdata())
                if (self.cospflocallsdbrouterid.is_set or self.cospflocallsdbrouterid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospflocallsdbrouterid.get_name_leafdata())
                if (self.cospflocallsdbadvertisement.is_set or self.cospflocallsdbadvertisement.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospflocallsdbadvertisement.get_name_leafdata())
                if (self.cospflocallsdbage.is_set or self.cospflocallsdbage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospflocallsdbage.get_name_leafdata())
                if (self.cospflocallsdbchecksum.is_set or self.cospflocallsdbchecksum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospflocallsdbchecksum.get_name_leafdata())
                if (self.cospflocallsdbsequence.is_set or self.cospflocallsdbsequence.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospflocallsdbsequence.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cospfLocalLsdbIpAddress" or name == "cospfLocalLsdbAddressLessIf" or name == "cospfLocalLsdbType" or name == "cospfLocalLsdbLsid" or name == "cospfLocalLsdbRouterId" or name == "cospfLocalLsdbAdvertisement" or name == "cospfLocalLsdbAge" or name == "cospfLocalLsdbChecksum" or name == "cospfLocalLsdbSequence"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cospfLocalLsdbIpAddress"):
                    self.cospflocallsdbipaddress = value
                    self.cospflocallsdbipaddress.value_namespace = name_space
                    self.cospflocallsdbipaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfLocalLsdbAddressLessIf"):
                    self.cospflocallsdbaddresslessif = value
                    self.cospflocallsdbaddresslessif.value_namespace = name_space
                    self.cospflocallsdbaddresslessif.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfLocalLsdbType"):
                    self.cospflocallsdbtype = value
                    self.cospflocallsdbtype.value_namespace = name_space
                    self.cospflocallsdbtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfLocalLsdbLsid"):
                    self.cospflocallsdblsid = value
                    self.cospflocallsdblsid.value_namespace = name_space
                    self.cospflocallsdblsid.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfLocalLsdbRouterId"):
                    self.cospflocallsdbrouterid = value
                    self.cospflocallsdbrouterid.value_namespace = name_space
                    self.cospflocallsdbrouterid.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfLocalLsdbAdvertisement"):
                    self.cospflocallsdbadvertisement = value
                    self.cospflocallsdbadvertisement.value_namespace = name_space
                    self.cospflocallsdbadvertisement.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfLocalLsdbAge"):
                    self.cospflocallsdbage = value
                    self.cospflocallsdbage.value_namespace = name_space
                    self.cospflocallsdbage.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfLocalLsdbChecksum"):
                    self.cospflocallsdbchecksum = value
                    self.cospflocallsdbchecksum.value_namespace = name_space
                    self.cospflocallsdbchecksum.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfLocalLsdbSequence"):
                    self.cospflocallsdbsequence = value
                    self.cospflocallsdbsequence.value_namespace = name_space
                    self.cospflocallsdbsequence.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cospflocallsdbentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cospflocallsdbentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cospfLocalLsdbTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-OSPF-MIB:CISCO-OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cospfLocalLsdbEntry"):
                for c in self.cospflocallsdbentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoOspfMib.Cospflocallsdbtable.Cospflocallsdbentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cospflocallsdbentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cospfLocalLsdbEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cospfvirtlocallsdbtable(Entity):
        """
        The OSPF Process's Link\-Local Link State Database
        for virtual links.
        
        .. attribute:: cospfvirtlocallsdbentry
        
        	A single Link State Advertisement
        	**type**\: list of    :py:class:`Cospfvirtlocallsdbentry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfvirtlocallsdbtable.Cospfvirtlocallsdbentry>`
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            super(CiscoOspfMib.Cospfvirtlocallsdbtable, self).__init__()

            self.yang_name = "cospfVirtLocalLsdbTable"
            self.yang_parent_name = "CISCO-OSPF-MIB"

            self.cospfvirtlocallsdbentry = YList(self)

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
                        super(CiscoOspfMib.Cospfvirtlocallsdbtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoOspfMib.Cospfvirtlocallsdbtable, self).__setattr__(name, value)


        class Cospfvirtlocallsdbentry(Entity):
            """
            A single Link State Advertisement.
            
            .. attribute:: cospfvirtlocallsdbtransitarea  <key>
            
            	The Transit Area that the Virtual Link traverses. By definition, this is not 0.0.0.0
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfvirtlocallsdbneighbor  <key>
            
            	The Router ID of the Virtual Neighbor
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfvirtlocallsdbtype  <key>
            
            	The type of the link state advertisement. Each  link state type has a separate advertisement format
            	**type**\:   :py:class:`Cospfvirtlocallsdbtype <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfvirtlocallsdbtable.Cospfvirtlocallsdbentry.Cospfvirtlocallsdbtype>`
            
            .. attribute:: cospfvirtlocallsdblsid  <key>
            
            	The Link State ID is an LS Type Specific field containing a 32 bit identifier in IP address format; it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfvirtlocallsdbrouterid  <key>
            
            	The 32 bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfvirtlocallsdbadvertisement
            
            	The entire Link State Advertisement, including its header
            	**type**\:  str
            
            	**length:** 1..65535
            
            .. attribute:: cospfvirtlocallsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\:  int
            
            	**range:** 0..3600
            
            .. attribute:: cospfvirtlocallsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field. The age field is excepted so that an advertisement's age can be incremented without updating the checksum. The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred  to as the Fletcher checksum
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfvirtlocallsdbsequence
            
            	The sequence number field is a  signed  32\-bit integer. It is used to detect old and duplicate link state advertisements. The space of sequence numbers is linearly ordered. The larger the sequence number the more recent the advertisement
            	**type**\:  int
            
            	**range:** \-2147483647..2147483647
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                super(CiscoOspfMib.Cospfvirtlocallsdbtable.Cospfvirtlocallsdbentry, self).__init__()

                self.yang_name = "cospfVirtLocalLsdbEntry"
                self.yang_parent_name = "cospfVirtLocalLsdbTable"

                self.cospfvirtlocallsdbtransitarea = YLeaf(YType.str, "cospfVirtLocalLsdbTransitArea")

                self.cospfvirtlocallsdbneighbor = YLeaf(YType.str, "cospfVirtLocalLsdbNeighbor")

                self.cospfvirtlocallsdbtype = YLeaf(YType.enumeration, "cospfVirtLocalLsdbType")

                self.cospfvirtlocallsdblsid = YLeaf(YType.str, "cospfVirtLocalLsdbLsid")

                self.cospfvirtlocallsdbrouterid = YLeaf(YType.str, "cospfVirtLocalLsdbRouterId")

                self.cospfvirtlocallsdbadvertisement = YLeaf(YType.str, "cospfVirtLocalLsdbAdvertisement")

                self.cospfvirtlocallsdbage = YLeaf(YType.int32, "cospfVirtLocalLsdbAge")

                self.cospfvirtlocallsdbchecksum = YLeaf(YType.uint32, "cospfVirtLocalLsdbChecksum")

                self.cospfvirtlocallsdbsequence = YLeaf(YType.int32, "cospfVirtLocalLsdbSequence")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cospfvirtlocallsdbtransitarea",
                                "cospfvirtlocallsdbneighbor",
                                "cospfvirtlocallsdbtype",
                                "cospfvirtlocallsdblsid",
                                "cospfvirtlocallsdbrouterid",
                                "cospfvirtlocallsdbadvertisement",
                                "cospfvirtlocallsdbage",
                                "cospfvirtlocallsdbchecksum",
                                "cospfvirtlocallsdbsequence") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoOspfMib.Cospfvirtlocallsdbtable.Cospfvirtlocallsdbentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoOspfMib.Cospfvirtlocallsdbtable.Cospfvirtlocallsdbentry, self).__setattr__(name, value)

            class Cospfvirtlocallsdbtype(Enum):
                """
                Cospfvirtlocallsdbtype

                The type of the link state advertisement.

                Each  link state type has a separate advertisement format.

                .. data:: localOpaqueLink = 9

                """

                localOpaqueLink = Enum.YLeaf(9, "localOpaqueLink")


            def has_data(self):
                return (
                    self.cospfvirtlocallsdbtransitarea.is_set or
                    self.cospfvirtlocallsdbneighbor.is_set or
                    self.cospfvirtlocallsdbtype.is_set or
                    self.cospfvirtlocallsdblsid.is_set or
                    self.cospfvirtlocallsdbrouterid.is_set or
                    self.cospfvirtlocallsdbadvertisement.is_set or
                    self.cospfvirtlocallsdbage.is_set or
                    self.cospfvirtlocallsdbchecksum.is_set or
                    self.cospfvirtlocallsdbsequence.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cospfvirtlocallsdbtransitarea.yfilter != YFilter.not_set or
                    self.cospfvirtlocallsdbneighbor.yfilter != YFilter.not_set or
                    self.cospfvirtlocallsdbtype.yfilter != YFilter.not_set or
                    self.cospfvirtlocallsdblsid.yfilter != YFilter.not_set or
                    self.cospfvirtlocallsdbrouterid.yfilter != YFilter.not_set or
                    self.cospfvirtlocallsdbadvertisement.yfilter != YFilter.not_set or
                    self.cospfvirtlocallsdbage.yfilter != YFilter.not_set or
                    self.cospfvirtlocallsdbchecksum.yfilter != YFilter.not_set or
                    self.cospfvirtlocallsdbsequence.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cospfVirtLocalLsdbEntry" + "[cospfVirtLocalLsdbTransitArea='" + self.cospfvirtlocallsdbtransitarea.get() + "']" + "[cospfVirtLocalLsdbNeighbor='" + self.cospfvirtlocallsdbneighbor.get() + "']" + "[cospfVirtLocalLsdbType='" + self.cospfvirtlocallsdbtype.get() + "']" + "[cospfVirtLocalLsdbLsid='" + self.cospfvirtlocallsdblsid.get() + "']" + "[cospfVirtLocalLsdbRouterId='" + self.cospfvirtlocallsdbrouterid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-OSPF-MIB:CISCO-OSPF-MIB/cospfVirtLocalLsdbTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cospfvirtlocallsdbtransitarea.is_set or self.cospfvirtlocallsdbtransitarea.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfvirtlocallsdbtransitarea.get_name_leafdata())
                if (self.cospfvirtlocallsdbneighbor.is_set or self.cospfvirtlocallsdbneighbor.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfvirtlocallsdbneighbor.get_name_leafdata())
                if (self.cospfvirtlocallsdbtype.is_set or self.cospfvirtlocallsdbtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfvirtlocallsdbtype.get_name_leafdata())
                if (self.cospfvirtlocallsdblsid.is_set or self.cospfvirtlocallsdblsid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfvirtlocallsdblsid.get_name_leafdata())
                if (self.cospfvirtlocallsdbrouterid.is_set or self.cospfvirtlocallsdbrouterid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfvirtlocallsdbrouterid.get_name_leafdata())
                if (self.cospfvirtlocallsdbadvertisement.is_set or self.cospfvirtlocallsdbadvertisement.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfvirtlocallsdbadvertisement.get_name_leafdata())
                if (self.cospfvirtlocallsdbage.is_set or self.cospfvirtlocallsdbage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfvirtlocallsdbage.get_name_leafdata())
                if (self.cospfvirtlocallsdbchecksum.is_set or self.cospfvirtlocallsdbchecksum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfvirtlocallsdbchecksum.get_name_leafdata())
                if (self.cospfvirtlocallsdbsequence.is_set or self.cospfvirtlocallsdbsequence.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfvirtlocallsdbsequence.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cospfVirtLocalLsdbTransitArea" or name == "cospfVirtLocalLsdbNeighbor" or name == "cospfVirtLocalLsdbType" or name == "cospfVirtLocalLsdbLsid" or name == "cospfVirtLocalLsdbRouterId" or name == "cospfVirtLocalLsdbAdvertisement" or name == "cospfVirtLocalLsdbAge" or name == "cospfVirtLocalLsdbChecksum" or name == "cospfVirtLocalLsdbSequence"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cospfVirtLocalLsdbTransitArea"):
                    self.cospfvirtlocallsdbtransitarea = value
                    self.cospfvirtlocallsdbtransitarea.value_namespace = name_space
                    self.cospfvirtlocallsdbtransitarea.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfVirtLocalLsdbNeighbor"):
                    self.cospfvirtlocallsdbneighbor = value
                    self.cospfvirtlocallsdbneighbor.value_namespace = name_space
                    self.cospfvirtlocallsdbneighbor.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfVirtLocalLsdbType"):
                    self.cospfvirtlocallsdbtype = value
                    self.cospfvirtlocallsdbtype.value_namespace = name_space
                    self.cospfvirtlocallsdbtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfVirtLocalLsdbLsid"):
                    self.cospfvirtlocallsdblsid = value
                    self.cospfvirtlocallsdblsid.value_namespace = name_space
                    self.cospfvirtlocallsdblsid.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfVirtLocalLsdbRouterId"):
                    self.cospfvirtlocallsdbrouterid = value
                    self.cospfvirtlocallsdbrouterid.value_namespace = name_space
                    self.cospfvirtlocallsdbrouterid.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfVirtLocalLsdbAdvertisement"):
                    self.cospfvirtlocallsdbadvertisement = value
                    self.cospfvirtlocallsdbadvertisement.value_namespace = name_space
                    self.cospfvirtlocallsdbadvertisement.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfVirtLocalLsdbAge"):
                    self.cospfvirtlocallsdbage = value
                    self.cospfvirtlocallsdbage.value_namespace = name_space
                    self.cospfvirtlocallsdbage.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfVirtLocalLsdbChecksum"):
                    self.cospfvirtlocallsdbchecksum = value
                    self.cospfvirtlocallsdbchecksum.value_namespace = name_space
                    self.cospfvirtlocallsdbchecksum.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfVirtLocalLsdbSequence"):
                    self.cospfvirtlocallsdbsequence = value
                    self.cospfvirtlocallsdbsequence.value_namespace = name_space
                    self.cospfvirtlocallsdbsequence.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cospfvirtlocallsdbentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cospfvirtlocallsdbentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cospfVirtLocalLsdbTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-OSPF-MIB:CISCO-OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cospfVirtLocalLsdbEntry"):
                for c in self.cospfvirtlocallsdbentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoOspfMib.Cospfvirtlocallsdbtable.Cospfvirtlocallsdbentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cospfvirtlocallsdbentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cospfVirtLocalLsdbEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cospfshamlinknbrtable(Entity):
        """
        A table of sham link neighbor information.
        
        .. attribute:: cospfshamlinknbrentry
        
        	Sham link neighbor information
        	**type**\: list of    :py:class:`Cospfshamlinknbrentry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfshamlinknbrtable.Cospfshamlinknbrentry>`
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            super(CiscoOspfMib.Cospfshamlinknbrtable, self).__init__()

            self.yang_name = "cospfShamLinkNbrTable"
            self.yang_parent_name = "CISCO-OSPF-MIB"

            self.cospfshamlinknbrentry = YList(self)

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
                        super(CiscoOspfMib.Cospfshamlinknbrtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoOspfMib.Cospfshamlinknbrtable, self).__setattr__(name, value)


        class Cospfshamlinknbrentry(Entity):
            """
            Sham link neighbor information.
            
            .. attribute:: cospfshamlinkslocalipaddrtype  <key>
            
            	
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cospfshamlinkslocalipaddr  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`cospfshamlinkslocalipaddr <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfshamlinkstable.Cospfshamlinksentry>`
            
            .. attribute:: cospfshamlinknbrarea  <key>
            
            	The area to which the sham link is part of
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfshamlinknbripaddrtype  <key>
            
            	The type of internet address of this sham link neighbor's IP address
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cospfshamlinknbripaddr  <key>
            
            	The IP address this sham link neighbor is using
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cospfshamlinknbrevents
            
            	The number of  times  this sham link has changed state or an error has occurred
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfshamlinknbrhellosuppressed
            
            	Indicates whether Hellos are being  suppressed to the neighbor
            	**type**\:  bool
            
            .. attribute:: cospfshamlinknbrlsretransqlen
            
            	The  current  length  of  the   retransmission queue. The retransmission queue is maintained for LSAs that have been flooded but not acknowledged on this adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfshamlinknbroptions
            
            	A Bit Mask corresponding to the neighbor's options field.  Bit 1, if set, indicates that the  system  will operate  on  Type of Service metrics other than TOS 0.  If zero, the neighbor will  ignore  all metrics except the TOS 0 metric.  Bit 2, if set, indicates  that  the  system  is Network  Multicast  capable; ie, that it implements  OSPF Multicast Routing
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: cospfshamlinknbrrtrid
            
            	A 32\-bit integer uniquely identifying the neighboring router
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfshamlinknbrstate
            
            	The state of this sham link neighbor relation\- ship
            	**type**\:   :py:class:`Cospfshamlinknbrstate <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfshamlinknbrtable.Cospfshamlinknbrentry.Cospfshamlinknbrstate>`
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                super(CiscoOspfMib.Cospfshamlinknbrtable.Cospfshamlinknbrentry, self).__init__()

                self.yang_name = "cospfShamLinkNbrEntry"
                self.yang_parent_name = "cospfShamLinkNbrTable"

                self.cospfshamlinkslocalipaddrtype = YLeaf(YType.enumeration, "cospfShamLinksLocalIpAddrType")

                self.cospfshamlinkslocalipaddr = YLeaf(YType.str, "cospfShamLinksLocalIpAddr")

                self.cospfshamlinknbrarea = YLeaf(YType.str, "cospfShamLinkNbrArea")

                self.cospfshamlinknbripaddrtype = YLeaf(YType.enumeration, "cospfShamLinkNbrIpAddrType")

                self.cospfshamlinknbripaddr = YLeaf(YType.str, "cospfShamLinkNbrIpAddr")

                self.cospfshamlinknbrevents = YLeaf(YType.uint32, "cospfShamLinkNbrEvents")

                self.cospfshamlinknbrhellosuppressed = YLeaf(YType.boolean, "cospfShamLinkNbrHelloSuppressed")

                self.cospfshamlinknbrlsretransqlen = YLeaf(YType.uint32, "cospfShamLinkNbrLsRetransQLen")

                self.cospfshamlinknbroptions = YLeaf(YType.int32, "cospfShamLinkNbrOptions")

                self.cospfshamlinknbrrtrid = YLeaf(YType.str, "cospfShamLinkNbrRtrId")

                self.cospfshamlinknbrstate = YLeaf(YType.enumeration, "cospfShamLinkNbrState")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cospfshamlinkslocalipaddrtype",
                                "cospfshamlinkslocalipaddr",
                                "cospfshamlinknbrarea",
                                "cospfshamlinknbripaddrtype",
                                "cospfshamlinknbripaddr",
                                "cospfshamlinknbrevents",
                                "cospfshamlinknbrhellosuppressed",
                                "cospfshamlinknbrlsretransqlen",
                                "cospfshamlinknbroptions",
                                "cospfshamlinknbrrtrid",
                                "cospfshamlinknbrstate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoOspfMib.Cospfshamlinknbrtable.Cospfshamlinknbrentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoOspfMib.Cospfshamlinknbrtable.Cospfshamlinknbrentry, self).__setattr__(name, value)

            class Cospfshamlinknbrstate(Enum):
                """
                Cospfshamlinknbrstate

                The state of this sham link neighbor relation\-

                ship.

                .. data:: down = 1

                .. data:: attempt = 2

                .. data:: init = 3

                .. data:: twoWay = 4

                .. data:: exchangeStart = 5

                .. data:: exchange = 6

                .. data:: loading = 7

                .. data:: full = 8

                """

                down = Enum.YLeaf(1, "down")

                attempt = Enum.YLeaf(2, "attempt")

                init = Enum.YLeaf(3, "init")

                twoWay = Enum.YLeaf(4, "twoWay")

                exchangeStart = Enum.YLeaf(5, "exchangeStart")

                exchange = Enum.YLeaf(6, "exchange")

                loading = Enum.YLeaf(7, "loading")

                full = Enum.YLeaf(8, "full")


            def has_data(self):
                return (
                    self.cospfshamlinkslocalipaddrtype.is_set or
                    self.cospfshamlinkslocalipaddr.is_set or
                    self.cospfshamlinknbrarea.is_set or
                    self.cospfshamlinknbripaddrtype.is_set or
                    self.cospfshamlinknbripaddr.is_set or
                    self.cospfshamlinknbrevents.is_set or
                    self.cospfshamlinknbrhellosuppressed.is_set or
                    self.cospfshamlinknbrlsretransqlen.is_set or
                    self.cospfshamlinknbroptions.is_set or
                    self.cospfshamlinknbrrtrid.is_set or
                    self.cospfshamlinknbrstate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cospfshamlinkslocalipaddrtype.yfilter != YFilter.not_set or
                    self.cospfshamlinkslocalipaddr.yfilter != YFilter.not_set or
                    self.cospfshamlinknbrarea.yfilter != YFilter.not_set or
                    self.cospfshamlinknbripaddrtype.yfilter != YFilter.not_set or
                    self.cospfshamlinknbripaddr.yfilter != YFilter.not_set or
                    self.cospfshamlinknbrevents.yfilter != YFilter.not_set or
                    self.cospfshamlinknbrhellosuppressed.yfilter != YFilter.not_set or
                    self.cospfshamlinknbrlsretransqlen.yfilter != YFilter.not_set or
                    self.cospfshamlinknbroptions.yfilter != YFilter.not_set or
                    self.cospfshamlinknbrrtrid.yfilter != YFilter.not_set or
                    self.cospfshamlinknbrstate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cospfShamLinkNbrEntry" + "[cospfShamLinksLocalIpAddrType='" + self.cospfshamlinkslocalipaddrtype.get() + "']" + "[cospfShamLinksLocalIpAddr='" + self.cospfshamlinkslocalipaddr.get() + "']" + "[cospfShamLinkNbrArea='" + self.cospfshamlinknbrarea.get() + "']" + "[cospfShamLinkNbrIpAddrType='" + self.cospfshamlinknbripaddrtype.get() + "']" + "[cospfShamLinkNbrIpAddr='" + self.cospfshamlinknbripaddr.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-OSPF-MIB:CISCO-OSPF-MIB/cospfShamLinkNbrTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cospfshamlinkslocalipaddrtype.is_set or self.cospfshamlinkslocalipaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinkslocalipaddrtype.get_name_leafdata())
                if (self.cospfshamlinkslocalipaddr.is_set or self.cospfshamlinkslocalipaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinkslocalipaddr.get_name_leafdata())
                if (self.cospfshamlinknbrarea.is_set or self.cospfshamlinknbrarea.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinknbrarea.get_name_leafdata())
                if (self.cospfshamlinknbripaddrtype.is_set or self.cospfshamlinknbripaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinknbripaddrtype.get_name_leafdata())
                if (self.cospfshamlinknbripaddr.is_set or self.cospfshamlinknbripaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinknbripaddr.get_name_leafdata())
                if (self.cospfshamlinknbrevents.is_set or self.cospfshamlinknbrevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinknbrevents.get_name_leafdata())
                if (self.cospfshamlinknbrhellosuppressed.is_set or self.cospfshamlinknbrhellosuppressed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinknbrhellosuppressed.get_name_leafdata())
                if (self.cospfshamlinknbrlsretransqlen.is_set or self.cospfshamlinknbrlsretransqlen.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinknbrlsretransqlen.get_name_leafdata())
                if (self.cospfshamlinknbroptions.is_set or self.cospfshamlinknbroptions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinknbroptions.get_name_leafdata())
                if (self.cospfshamlinknbrrtrid.is_set or self.cospfshamlinknbrrtrid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinknbrrtrid.get_name_leafdata())
                if (self.cospfshamlinknbrstate.is_set or self.cospfshamlinknbrstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinknbrstate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cospfShamLinksLocalIpAddrType" or name == "cospfShamLinksLocalIpAddr" or name == "cospfShamLinkNbrArea" or name == "cospfShamLinkNbrIpAddrType" or name == "cospfShamLinkNbrIpAddr" or name == "cospfShamLinkNbrEvents" or name == "cospfShamLinkNbrHelloSuppressed" or name == "cospfShamLinkNbrLsRetransQLen" or name == "cospfShamLinkNbrOptions" or name == "cospfShamLinkNbrRtrId" or name == "cospfShamLinkNbrState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cospfShamLinksLocalIpAddrType"):
                    self.cospfshamlinkslocalipaddrtype = value
                    self.cospfshamlinkslocalipaddrtype.value_namespace = name_space
                    self.cospfshamlinkslocalipaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinksLocalIpAddr"):
                    self.cospfshamlinkslocalipaddr = value
                    self.cospfshamlinkslocalipaddr.value_namespace = name_space
                    self.cospfshamlinkslocalipaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinkNbrArea"):
                    self.cospfshamlinknbrarea = value
                    self.cospfshamlinknbrarea.value_namespace = name_space
                    self.cospfshamlinknbrarea.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinkNbrIpAddrType"):
                    self.cospfshamlinknbripaddrtype = value
                    self.cospfshamlinknbripaddrtype.value_namespace = name_space
                    self.cospfshamlinknbripaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinkNbrIpAddr"):
                    self.cospfshamlinknbripaddr = value
                    self.cospfshamlinknbripaddr.value_namespace = name_space
                    self.cospfshamlinknbripaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinkNbrEvents"):
                    self.cospfshamlinknbrevents = value
                    self.cospfshamlinknbrevents.value_namespace = name_space
                    self.cospfshamlinknbrevents.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinkNbrHelloSuppressed"):
                    self.cospfshamlinknbrhellosuppressed = value
                    self.cospfshamlinknbrhellosuppressed.value_namespace = name_space
                    self.cospfshamlinknbrhellosuppressed.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinkNbrLsRetransQLen"):
                    self.cospfshamlinknbrlsretransqlen = value
                    self.cospfshamlinknbrlsretransqlen.value_namespace = name_space
                    self.cospfshamlinknbrlsretransqlen.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinkNbrOptions"):
                    self.cospfshamlinknbroptions = value
                    self.cospfshamlinknbroptions.value_namespace = name_space
                    self.cospfshamlinknbroptions.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinkNbrRtrId"):
                    self.cospfshamlinknbrrtrid = value
                    self.cospfshamlinknbrrtrid.value_namespace = name_space
                    self.cospfshamlinknbrrtrid.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinkNbrState"):
                    self.cospfshamlinknbrstate = value
                    self.cospfshamlinknbrstate.value_namespace = name_space
                    self.cospfshamlinknbrstate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cospfshamlinknbrentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cospfshamlinknbrentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cospfShamLinkNbrTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-OSPF-MIB:CISCO-OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cospfShamLinkNbrEntry"):
                for c in self.cospfshamlinknbrentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoOspfMib.Cospfshamlinknbrtable.Cospfshamlinknbrentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cospfshamlinknbrentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cospfShamLinkNbrEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cospfshamlinkstable(Entity):
        """
        Information about this router's sham links.
        
        .. attribute:: cospfshamlinksentry
        
        	Information about a single sham link
        	**type**\: list of    :py:class:`Cospfshamlinksentry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfshamlinkstable.Cospfshamlinksentry>`
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            super(CiscoOspfMib.Cospfshamlinkstable, self).__init__()

            self.yang_name = "cospfShamLinksTable"
            self.yang_parent_name = "CISCO-OSPF-MIB"

            self.cospfshamlinksentry = YList(self)

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
                        super(CiscoOspfMib.Cospfshamlinkstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoOspfMib.Cospfshamlinkstable, self).__setattr__(name, value)


        class Cospfshamlinksentry(Entity):
            """
            Information about a single sham link.
            
            .. attribute:: cospfshamlinksareaid  <key>
            
            	The area that this sham link is part of
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfshamlinkslocalipaddrtype  <key>
            
            	The type of internet address of this sham link's local IP address
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cospfshamlinkslocalipaddr  <key>
            
            	The Local IP address of the sham link
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cospfshamlinksremoteipaddrtype  <key>
            
            	The type of internet address of this sham link's remote IP address
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cospfshamlinksremoteipaddr  <key>
            
            	The IP address of the other end router of the sham link
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cospfshamlinksevents
            
            	The number of state changes or error events on this sham link
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfshamlinkshellointerval
            
            	The length of time, in  seconds,  between  the Hello  packets that the router sends on the sham link
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: cospfshamlinksmetric
            
            	The Metric to be advertised
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cospfshamlinksretransinterval
            
            	The number of seconds between  link\-state  advertisement retransmissions, for adjacencies belonging to this link. This value is also used when retransmitting database  description and link\-state request packets. This value should be well over the expected round trip time
            	**type**\:  int
            
            	**range:** 0..3600
            
            .. attribute:: cospfshamlinksrtrdeadinterval
            
            	The number of seconds that  a  router's  Hello packets  have  not been seen before it's neighbors declare the router down.  This  should  be some  multiple  of  the  Hello  interval
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cospfshamlinksstate
            
            	OSPF sham link states
            	**type**\:   :py:class:`Cospfshamlinksstate <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CiscoOspfMib.Cospfshamlinkstable.Cospfshamlinksentry.Cospfshamlinksstate>`
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                super(CiscoOspfMib.Cospfshamlinkstable.Cospfshamlinksentry, self).__init__()

                self.yang_name = "cospfShamLinksEntry"
                self.yang_parent_name = "cospfShamLinksTable"

                self.cospfshamlinksareaid = YLeaf(YType.str, "cospfShamLinksAreaId")

                self.cospfshamlinkslocalipaddrtype = YLeaf(YType.enumeration, "cospfShamLinksLocalIpAddrType")

                self.cospfshamlinkslocalipaddr = YLeaf(YType.str, "cospfShamLinksLocalIpAddr")

                self.cospfshamlinksremoteipaddrtype = YLeaf(YType.enumeration, "cospfShamLinksRemoteIpAddrType")

                self.cospfshamlinksremoteipaddr = YLeaf(YType.str, "cospfShamLinksRemoteIpAddr")

                self.cospfshamlinksevents = YLeaf(YType.uint32, "cospfShamLinksEvents")

                self.cospfshamlinkshellointerval = YLeaf(YType.int32, "cospfShamLinksHelloInterval")

                self.cospfshamlinksmetric = YLeaf(YType.int32, "cospfShamLinksMetric")

                self.cospfshamlinksretransinterval = YLeaf(YType.int32, "cospfShamLinksRetransInterval")

                self.cospfshamlinksrtrdeadinterval = YLeaf(YType.int32, "cospfShamLinksRtrDeadInterval")

                self.cospfshamlinksstate = YLeaf(YType.enumeration, "cospfShamLinksState")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cospfshamlinksareaid",
                                "cospfshamlinkslocalipaddrtype",
                                "cospfshamlinkslocalipaddr",
                                "cospfshamlinksremoteipaddrtype",
                                "cospfshamlinksremoteipaddr",
                                "cospfshamlinksevents",
                                "cospfshamlinkshellointerval",
                                "cospfshamlinksmetric",
                                "cospfshamlinksretransinterval",
                                "cospfshamlinksrtrdeadinterval",
                                "cospfshamlinksstate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoOspfMib.Cospfshamlinkstable.Cospfshamlinksentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoOspfMib.Cospfshamlinkstable.Cospfshamlinksentry, self).__setattr__(name, value)

            class Cospfshamlinksstate(Enum):
                """
                Cospfshamlinksstate

                OSPF sham link states.

                .. data:: down = 1

                .. data:: pointToPoint = 4

                """

                down = Enum.YLeaf(1, "down")

                pointToPoint = Enum.YLeaf(4, "pointToPoint")


            def has_data(self):
                return (
                    self.cospfshamlinksareaid.is_set or
                    self.cospfshamlinkslocalipaddrtype.is_set or
                    self.cospfshamlinkslocalipaddr.is_set or
                    self.cospfshamlinksremoteipaddrtype.is_set or
                    self.cospfshamlinksremoteipaddr.is_set or
                    self.cospfshamlinksevents.is_set or
                    self.cospfshamlinkshellointerval.is_set or
                    self.cospfshamlinksmetric.is_set or
                    self.cospfshamlinksretransinterval.is_set or
                    self.cospfshamlinksrtrdeadinterval.is_set or
                    self.cospfshamlinksstate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cospfshamlinksareaid.yfilter != YFilter.not_set or
                    self.cospfshamlinkslocalipaddrtype.yfilter != YFilter.not_set or
                    self.cospfshamlinkslocalipaddr.yfilter != YFilter.not_set or
                    self.cospfshamlinksremoteipaddrtype.yfilter != YFilter.not_set or
                    self.cospfshamlinksremoteipaddr.yfilter != YFilter.not_set or
                    self.cospfshamlinksevents.yfilter != YFilter.not_set or
                    self.cospfshamlinkshellointerval.yfilter != YFilter.not_set or
                    self.cospfshamlinksmetric.yfilter != YFilter.not_set or
                    self.cospfshamlinksretransinterval.yfilter != YFilter.not_set or
                    self.cospfshamlinksrtrdeadinterval.yfilter != YFilter.not_set or
                    self.cospfshamlinksstate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cospfShamLinksEntry" + "[cospfShamLinksAreaId='" + self.cospfshamlinksareaid.get() + "']" + "[cospfShamLinksLocalIpAddrType='" + self.cospfshamlinkslocalipaddrtype.get() + "']" + "[cospfShamLinksLocalIpAddr='" + self.cospfshamlinkslocalipaddr.get() + "']" + "[cospfShamLinksRemoteIpAddrType='" + self.cospfshamlinksremoteipaddrtype.get() + "']" + "[cospfShamLinksRemoteIpAddr='" + self.cospfshamlinksremoteipaddr.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-OSPF-MIB:CISCO-OSPF-MIB/cospfShamLinksTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cospfshamlinksareaid.is_set or self.cospfshamlinksareaid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinksareaid.get_name_leafdata())
                if (self.cospfshamlinkslocalipaddrtype.is_set or self.cospfshamlinkslocalipaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinkslocalipaddrtype.get_name_leafdata())
                if (self.cospfshamlinkslocalipaddr.is_set or self.cospfshamlinkslocalipaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinkslocalipaddr.get_name_leafdata())
                if (self.cospfshamlinksremoteipaddrtype.is_set or self.cospfshamlinksremoteipaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinksremoteipaddrtype.get_name_leafdata())
                if (self.cospfshamlinksremoteipaddr.is_set or self.cospfshamlinksremoteipaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinksremoteipaddr.get_name_leafdata())
                if (self.cospfshamlinksevents.is_set or self.cospfshamlinksevents.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinksevents.get_name_leafdata())
                if (self.cospfshamlinkshellointerval.is_set or self.cospfshamlinkshellointerval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinkshellointerval.get_name_leafdata())
                if (self.cospfshamlinksmetric.is_set or self.cospfshamlinksmetric.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinksmetric.get_name_leafdata())
                if (self.cospfshamlinksretransinterval.is_set or self.cospfshamlinksretransinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinksretransinterval.get_name_leafdata())
                if (self.cospfshamlinksrtrdeadinterval.is_set or self.cospfshamlinksrtrdeadinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinksrtrdeadinterval.get_name_leafdata())
                if (self.cospfshamlinksstate.is_set or self.cospfshamlinksstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cospfshamlinksstate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cospfShamLinksAreaId" or name == "cospfShamLinksLocalIpAddrType" or name == "cospfShamLinksLocalIpAddr" or name == "cospfShamLinksRemoteIpAddrType" or name == "cospfShamLinksRemoteIpAddr" or name == "cospfShamLinksEvents" or name == "cospfShamLinksHelloInterval" or name == "cospfShamLinksMetric" or name == "cospfShamLinksRetransInterval" or name == "cospfShamLinksRtrDeadInterval" or name == "cospfShamLinksState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cospfShamLinksAreaId"):
                    self.cospfshamlinksareaid = value
                    self.cospfshamlinksareaid.value_namespace = name_space
                    self.cospfshamlinksareaid.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinksLocalIpAddrType"):
                    self.cospfshamlinkslocalipaddrtype = value
                    self.cospfshamlinkslocalipaddrtype.value_namespace = name_space
                    self.cospfshamlinkslocalipaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinksLocalIpAddr"):
                    self.cospfshamlinkslocalipaddr = value
                    self.cospfshamlinkslocalipaddr.value_namespace = name_space
                    self.cospfshamlinkslocalipaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinksRemoteIpAddrType"):
                    self.cospfshamlinksremoteipaddrtype = value
                    self.cospfshamlinksremoteipaddrtype.value_namespace = name_space
                    self.cospfshamlinksremoteipaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinksRemoteIpAddr"):
                    self.cospfshamlinksremoteipaddr = value
                    self.cospfshamlinksremoteipaddr.value_namespace = name_space
                    self.cospfshamlinksremoteipaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinksEvents"):
                    self.cospfshamlinksevents = value
                    self.cospfshamlinksevents.value_namespace = name_space
                    self.cospfshamlinksevents.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinksHelloInterval"):
                    self.cospfshamlinkshellointerval = value
                    self.cospfshamlinkshellointerval.value_namespace = name_space
                    self.cospfshamlinkshellointerval.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinksMetric"):
                    self.cospfshamlinksmetric = value
                    self.cospfshamlinksmetric.value_namespace = name_space
                    self.cospfshamlinksmetric.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinksRetransInterval"):
                    self.cospfshamlinksretransinterval = value
                    self.cospfshamlinksretransinterval.value_namespace = name_space
                    self.cospfshamlinksretransinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinksRtrDeadInterval"):
                    self.cospfshamlinksrtrdeadinterval = value
                    self.cospfshamlinksrtrdeadinterval.value_namespace = name_space
                    self.cospfshamlinksrtrdeadinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cospfShamLinksState"):
                    self.cospfshamlinksstate = value
                    self.cospfshamlinksstate.value_namespace = name_space
                    self.cospfshamlinksstate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cospfshamlinksentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cospfshamlinksentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cospfShamLinksTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-OSPF-MIB:CISCO-OSPF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cospfShamLinksEntry"):
                for c in self.cospfshamlinksentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoOspfMib.Cospfshamlinkstable.Cospfshamlinksentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cospfshamlinksentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cospfShamLinksEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cospfgeneralgroup is not None and self.cospfgeneralgroup.has_data()) or
            (self.cospflocallsdbtable is not None and self.cospflocallsdbtable.has_data()) or
            (self.cospflsdbtable is not None and self.cospflsdbtable.has_data()) or
            (self.cospfshamlinknbrtable is not None and self.cospfshamlinknbrtable.has_data()) or
            (self.cospfshamlinkstable is not None and self.cospfshamlinkstable.has_data()) or
            (self.cospfshamlinktable is not None and self.cospfshamlinktable.has_data()) or
            (self.cospfvirtlocallsdbtable is not None and self.cospfvirtlocallsdbtable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cospfgeneralgroup is not None and self.cospfgeneralgroup.has_operation()) or
            (self.cospflocallsdbtable is not None and self.cospflocallsdbtable.has_operation()) or
            (self.cospflsdbtable is not None and self.cospflsdbtable.has_operation()) or
            (self.cospfshamlinknbrtable is not None and self.cospfshamlinknbrtable.has_operation()) or
            (self.cospfshamlinkstable is not None and self.cospfshamlinkstable.has_operation()) or
            (self.cospfshamlinktable is not None and self.cospfshamlinktable.has_operation()) or
            (self.cospfvirtlocallsdbtable is not None and self.cospfvirtlocallsdbtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-OSPF-MIB:CISCO-OSPF-MIB" + path_buffer

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

        if (child_yang_name == "cospfGeneralGroup"):
            if (self.cospfgeneralgroup is None):
                self.cospfgeneralgroup = CiscoOspfMib.Cospfgeneralgroup()
                self.cospfgeneralgroup.parent = self
                self._children_name_map["cospfgeneralgroup"] = "cospfGeneralGroup"
            return self.cospfgeneralgroup

        if (child_yang_name == "cospfLocalLsdbTable"):
            if (self.cospflocallsdbtable is None):
                self.cospflocallsdbtable = CiscoOspfMib.Cospflocallsdbtable()
                self.cospflocallsdbtable.parent = self
                self._children_name_map["cospflocallsdbtable"] = "cospfLocalLsdbTable"
            return self.cospflocallsdbtable

        if (child_yang_name == "cospfLsdbTable"):
            if (self.cospflsdbtable is None):
                self.cospflsdbtable = CiscoOspfMib.Cospflsdbtable()
                self.cospflsdbtable.parent = self
                self._children_name_map["cospflsdbtable"] = "cospfLsdbTable"
            return self.cospflsdbtable

        if (child_yang_name == "cospfShamLinkNbrTable"):
            if (self.cospfshamlinknbrtable is None):
                self.cospfshamlinknbrtable = CiscoOspfMib.Cospfshamlinknbrtable()
                self.cospfshamlinknbrtable.parent = self
                self._children_name_map["cospfshamlinknbrtable"] = "cospfShamLinkNbrTable"
            return self.cospfshamlinknbrtable

        if (child_yang_name == "cospfShamLinksTable"):
            if (self.cospfshamlinkstable is None):
                self.cospfshamlinkstable = CiscoOspfMib.Cospfshamlinkstable()
                self.cospfshamlinkstable.parent = self
                self._children_name_map["cospfshamlinkstable"] = "cospfShamLinksTable"
            return self.cospfshamlinkstable

        if (child_yang_name == "cospfShamLinkTable"):
            if (self.cospfshamlinktable is None):
                self.cospfshamlinktable = CiscoOspfMib.Cospfshamlinktable()
                self.cospfshamlinktable.parent = self
                self._children_name_map["cospfshamlinktable"] = "cospfShamLinkTable"
            return self.cospfshamlinktable

        if (child_yang_name == "cospfVirtLocalLsdbTable"):
            if (self.cospfvirtlocallsdbtable is None):
                self.cospfvirtlocallsdbtable = CiscoOspfMib.Cospfvirtlocallsdbtable()
                self.cospfvirtlocallsdbtable.parent = self
                self._children_name_map["cospfvirtlocallsdbtable"] = "cospfVirtLocalLsdbTable"
            return self.cospfvirtlocallsdbtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cospfGeneralGroup" or name == "cospfLocalLsdbTable" or name == "cospfLsdbTable" or name == "cospfShamLinkNbrTable" or name == "cospfShamLinksTable" or name == "cospfShamLinkTable" or name == "cospfVirtLocalLsdbTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoOspfMib()
        return self._top_entity


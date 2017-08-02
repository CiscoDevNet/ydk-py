""" SNMPv2_MIB 

The MIB module for SNMP entities.

Copyright (C) The Internet Society (2002). This
version of this MIB module is part of RFC 3418;
see the RFC itself for full legal notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Snmpv2Mib(Entity):
    """
    
    
    .. attribute:: snmp
    
    	
    	**type**\:   :py:class:`Snmp <ydk.models.cisco_ios_xe.SNMPv2_MIB.Snmpv2Mib.Snmp>`
    
    .. attribute:: snmpset
    
    	
    	**type**\:   :py:class:`Snmpset <ydk.models.cisco_ios_xe.SNMPv2_MIB.Snmpv2Mib.Snmpset>`
    
    .. attribute:: sysortable
    
    	The (conceptual) table listing the capabilities of the local SNMP application acting as a command responder with respect to various MIB modules. SNMP entities having dynamically\-configurable support of MIB modules will have a dynamically\-varying number of conceptual rows
    	**type**\:   :py:class:`Sysortable <ydk.models.cisco_ios_xe.SNMPv2_MIB.Snmpv2Mib.Sysortable>`
    
    .. attribute:: system
    
    	
    	**type**\:   :py:class:`System <ydk.models.cisco_ios_xe.SNMPv2_MIB.Snmpv2Mib.System>`
    
    

    """

    _prefix = 'SNMPv2-MIB'
    _revision = '2002-10-16'

    def __init__(self):
        super(Snmpv2Mib, self).__init__()
        self._top_entity = None

        self.yang_name = "SNMPv2-MIB"
        self.yang_parent_name = "SNMPv2-MIB"

        self.snmp = Snmpv2Mib.Snmp()
        self.snmp.parent = self
        self._children_name_map["snmp"] = "snmp"
        self._children_yang_names.add("snmp")

        self.snmpset = Snmpv2Mib.Snmpset()
        self.snmpset.parent = self
        self._children_name_map["snmpset"] = "snmpSet"
        self._children_yang_names.add("snmpSet")

        self.sysortable = Snmpv2Mib.Sysortable()
        self.sysortable.parent = self
        self._children_name_map["sysortable"] = "sysORTable"
        self._children_yang_names.add("sysORTable")

        self.system = Snmpv2Mib.System()
        self.system.parent = self
        self._children_name_map["system"] = "system"
        self._children_yang_names.add("system")


    class System(Entity):
        """
        
        
        .. attribute:: syscontact
        
        	The textual identification of the contact person for this managed node, together with information on how to contact this person.  If no contact information is known, the value is the zero\-length string
        	**type**\:  str
        
        	**length:** 0..255
        
        .. attribute:: sysdescr
        
        	A textual description of the entity.  This value should include the full name and version identification of the system's hardware type, software operating\-system, and networking software
        	**type**\:  str
        
        	**length:** 0..255
        
        .. attribute:: syslocation
        
        	The physical location of this node (e.g., 'telephone closet, 3rd floor').  If the location is unknown, the value is the zero\-length string
        	**type**\:  str
        
        	**length:** 0..255
        
        .. attribute:: sysname
        
        	An administratively\-assigned name for this managed node.  By convention, this is the node's fully\-qualified domain name.  If the name is unknown, the value is the zero\-length string
        	**type**\:  str
        
        	**length:** 0..255
        
        .. attribute:: sysobjectid
        
        	The vendor's authoritative identification of the network management subsystem contained in the entity. This value is allocated within the SMI enterprises subtree (1.3.6.1.4.1) and provides an easy and unambiguous means for determining `what kind of box' is being managed.  For example, if vendor `Flintstones, Inc.' was assigned the subtree 1.3.6.1.4.1.424242, it could assign the identifier 1.3.6.1.4.1.424242.1.1 to its `Fred Router'
        	**type**\:  str
        
        	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
        
        .. attribute:: sysorlastchange
        
        	The value of sysUpTime at the time of the most recent change in state or value of any instance of sysORID
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: sysservices
        
        	A value which indicates the set of services that this entity may potentially offer.  The value is a sum. This sum initially takes the value zero. Then, for each layer, L, in the range 1 through 7, that this node performs transactions for, 2 raised to (L \- 1) is added to the sum.  For example, a node which performs only routing functions would have a value of 4 (2^(3\-1)). In contrast, a node which is a host offering application services would have a value of 72 (2^(4\-1) + 2^(7\-1)). Note that in the context of the Internet suite of protocols, values should be calculated accordingly\:       layer      functionality        1        physical (e.g., repeaters)        2        datalink/subnetwork (e.g., bridges)        3        internet (e.g., supports the IP)        4        end\-to\-end  (e.g., supports the TCP)        7        applications (e.g., supports the SMTP)  For systems including OSI protocols, layers 5 and 6 may also be counted
        	**type**\:  int
        
        	**range:** 0..127
        
        .. attribute:: sysuptime
        
        	The time (in hundredths of a second) since the network management portion of the system was last re\-initialized
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'SNMPv2-MIB'
        _revision = '2002-10-16'

        def __init__(self):
            super(Snmpv2Mib.System, self).__init__()

            self.yang_name = "system"
            self.yang_parent_name = "SNMPv2-MIB"

            self.syscontact = YLeaf(YType.str, "sysContact")

            self.sysdescr = YLeaf(YType.str, "sysDescr")

            self.syslocation = YLeaf(YType.str, "sysLocation")

            self.sysname = YLeaf(YType.str, "sysName")

            self.sysobjectid = YLeaf(YType.str, "sysObjectID")

            self.sysorlastchange = YLeaf(YType.uint32, "sysORLastChange")

            self.sysservices = YLeaf(YType.int32, "sysServices")

            self.sysuptime = YLeaf(YType.uint32, "sysUpTime")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("syscontact",
                            "sysdescr",
                            "syslocation",
                            "sysname",
                            "sysobjectid",
                            "sysorlastchange",
                            "sysservices",
                            "sysuptime") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Snmpv2Mib.System, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Snmpv2Mib.System, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.syscontact.is_set or
                self.sysdescr.is_set or
                self.syslocation.is_set or
                self.sysname.is_set or
                self.sysobjectid.is_set or
                self.sysorlastchange.is_set or
                self.sysservices.is_set or
                self.sysuptime.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.syscontact.yfilter != YFilter.not_set or
                self.sysdescr.yfilter != YFilter.not_set or
                self.syslocation.yfilter != YFilter.not_set or
                self.sysname.yfilter != YFilter.not_set or
                self.sysobjectid.yfilter != YFilter.not_set or
                self.sysorlastchange.yfilter != YFilter.not_set or
                self.sysservices.yfilter != YFilter.not_set or
                self.sysuptime.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "system" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SNMPv2-MIB:SNMPv2-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.syscontact.is_set or self.syscontact.yfilter != YFilter.not_set):
                leaf_name_data.append(self.syscontact.get_name_leafdata())
            if (self.sysdescr.is_set or self.sysdescr.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sysdescr.get_name_leafdata())
            if (self.syslocation.is_set or self.syslocation.yfilter != YFilter.not_set):
                leaf_name_data.append(self.syslocation.get_name_leafdata())
            if (self.sysname.is_set or self.sysname.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sysname.get_name_leafdata())
            if (self.sysobjectid.is_set or self.sysobjectid.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sysobjectid.get_name_leafdata())
            if (self.sysorlastchange.is_set or self.sysorlastchange.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sysorlastchange.get_name_leafdata())
            if (self.sysservices.is_set or self.sysservices.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sysservices.get_name_leafdata())
            if (self.sysuptime.is_set or self.sysuptime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sysuptime.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sysContact" or name == "sysDescr" or name == "sysLocation" or name == "sysName" or name == "sysObjectID" or name == "sysORLastChange" or name == "sysServices" or name == "sysUpTime"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "sysContact"):
                self.syscontact = value
                self.syscontact.value_namespace = name_space
                self.syscontact.value_namespace_prefix = name_space_prefix
            if(value_path == "sysDescr"):
                self.sysdescr = value
                self.sysdescr.value_namespace = name_space
                self.sysdescr.value_namespace_prefix = name_space_prefix
            if(value_path == "sysLocation"):
                self.syslocation = value
                self.syslocation.value_namespace = name_space
                self.syslocation.value_namespace_prefix = name_space_prefix
            if(value_path == "sysName"):
                self.sysname = value
                self.sysname.value_namespace = name_space
                self.sysname.value_namespace_prefix = name_space_prefix
            if(value_path == "sysObjectID"):
                self.sysobjectid = value
                self.sysobjectid.value_namespace = name_space
                self.sysobjectid.value_namespace_prefix = name_space_prefix
            if(value_path == "sysORLastChange"):
                self.sysorlastchange = value
                self.sysorlastchange.value_namespace = name_space
                self.sysorlastchange.value_namespace_prefix = name_space_prefix
            if(value_path == "sysServices"):
                self.sysservices = value
                self.sysservices.value_namespace = name_space
                self.sysservices.value_namespace_prefix = name_space_prefix
            if(value_path == "sysUpTime"):
                self.sysuptime = value
                self.sysuptime.value_namespace = name_space
                self.sysuptime.value_namespace_prefix = name_space_prefix


    class Snmp(Entity):
        """
        
        
        .. attribute:: snmpenableauthentraps
        
        	Indicates whether the SNMP entity is permitted to generate authenticationFailure traps.  The value of this object overrides any configuration information; as such, it provides a means whereby all authenticationFailure traps may be disabled.  Note that it is strongly recommended that this object be stored in non\-volatile memory so that it remains constant across re\-initializations of the network management system
        	**type**\:   :py:class:`Snmpenableauthentraps <ydk.models.cisco_ios_xe.SNMPv2_MIB.Snmpv2Mib.Snmp.Snmpenableauthentraps>`
        
        .. attribute:: snmpinasnparseerrs
        
        	The total number of ASN.1 or BER errors encountered by the SNMP entity when decoding received SNMP messages
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinbadcommunitynames
        
        	The total number of community\-based SNMP messages (for example,  SNMPv1) delivered to the SNMP entity which used an SNMP community name not known to said entity. Also, implementations which authenticate community\-based SNMP messages using check(s) in addition to matching the community name (for example, by also checking whether the message originated from a transport address allowed to use a specified community name) MAY include in this value the number of messages which failed the additional check(s).  It is strongly RECOMMENDED that the documentation for any security model which is used to authenticate community\-based SNMP messages specify the precise conditions that contribute to this value
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinbadcommunityuses
        
        	The total number of community\-based SNMP messages (for example, SNMPv1) delivered to the SNMP entity which represented an SNMP operation that was not allowed for the SNMP community named in the message.  The precise conditions under which this counter is incremented (if at all) depend on how the SNMP entity implements its access control mechanism and how its applications interact with that access control mechanism.  It is strongly RECOMMENDED that the documentation for any access control mechanism which is used to control access to and visibility of MIB instrumentation specify the precise conditions that contribute to this value
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinbadvalues
        
        	The total number of SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field was `badValue'
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpinbadversions
        
        	The total number of SNMP messages which were delivered to the SNMP entity and were for an unsupported SNMP version
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpingenerrs
        
        	The total number of SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field was `genErr'
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpingetnexts
        
        	The total number of SNMP Get\-Next PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpingetrequests
        
        	The total number of SNMP Get\-Request PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpingetresponses
        
        	The total number of SNMP Get\-Response PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpinnosuchnames
        
        	The total number of SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field was `noSuchName'
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpinpkts
        
        	The total number of messages delivered to the SNMP entity from the transport service
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinreadonlys
        
        	The total number valid SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field was `readOnly'.  It should be noted that it is a protocol error to generate an SNMP PDU which contains the value `readOnly' in the error\-status field, as such this object is provided as a means of detecting incorrect implementations of the SNMP
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpinsetrequests
        
        	The total number of SNMP Set\-Request PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpintoobigs
        
        	The total number of SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field was `tooBig'
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpintotalreqvars
        
        	The total number of MIB objects which have been retrieved successfully by the SNMP protocol entity as the result of receiving valid SNMP Get\-Request and Get\-Next PDUs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpintotalsetvars
        
        	The total number of MIB objects which have been altered successfully by the SNMP protocol entity as the result of receiving valid SNMP Set\-Request PDUs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpintraps
        
        	The total number of SNMP Trap PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpoutbadvalues
        
        	The total number of SNMP PDUs which were generated by the SNMP protocol entity and for which the value of the error\-status field was `badValue'
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpoutgenerrs
        
        	The total number of SNMP PDUs which were generated by the SNMP protocol entity and for which the value of the error\-status field was `genErr'
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpoutgetnexts
        
        	The total number of SNMP Get\-Next PDUs which have been generated by the SNMP protocol entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpoutgetrequests
        
        	The total number of SNMP Get\-Request PDUs which have been generated by the SNMP protocol entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpoutgetresponses
        
        	The total number of SNMP Get\-Response PDUs which have been generated by the SNMP protocol entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpoutnosuchnames
        
        	The total number of SNMP PDUs which were generated by the SNMP protocol entity and for which the value of the error\-status was `noSuchName'
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpoutpkts
        
        	The total number of SNMP Messages which were passed from the SNMP protocol entity to the transport service
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpoutsetrequests
        
        	The total number of SNMP Set\-Request PDUs which have been generated by the SNMP protocol entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpouttoobigs
        
        	The total number of SNMP PDUs which were generated by the SNMP protocol entity and for which the value of the error\-status field was `tooBig.'
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpouttraps
        
        	The total number of SNMP Trap PDUs which have been generated by the SNMP protocol entity
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpproxydrops
        
        	The total number of Confirmed Class PDUs (such as GetRequest\-PDUs, GetNextRequest\-PDUs, GetBulkRequest\-PDUs, SetRequest\-PDUs, and InformRequest\-PDUs) delivered to the SNMP entity which were silently dropped because the transmission of the (possibly translated) message to a proxy target failed in a manner (other than a time\-out) such that no Response Class PDU (such as a Response\-PDU) could be returned
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpsilentdrops
        
        	The total number of Confirmed Class PDUs (such as GetRequest\-PDUs, GetNextRequest\-PDUs, GetBulkRequest\-PDUs, SetRequest\-PDUs, and InformRequest\-PDUs) delivered to the SNMP entity which were silently dropped because the size of a reply containing an alternate Response Class PDU (such as a Response\-PDU) with an empty variable\-bindings field was greater than either a local constraint or the maximum message size associated with the originator of the request
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'SNMPv2-MIB'
        _revision = '2002-10-16'

        def __init__(self):
            super(Snmpv2Mib.Snmp, self).__init__()

            self.yang_name = "snmp"
            self.yang_parent_name = "SNMPv2-MIB"

            self.snmpenableauthentraps = YLeaf(YType.enumeration, "snmpEnableAuthenTraps")

            self.snmpinasnparseerrs = YLeaf(YType.uint32, "snmpInASNParseErrs")

            self.snmpinbadcommunitynames = YLeaf(YType.uint32, "snmpInBadCommunityNames")

            self.snmpinbadcommunityuses = YLeaf(YType.uint32, "snmpInBadCommunityUses")

            self.snmpinbadvalues = YLeaf(YType.uint32, "snmpInBadValues")

            self.snmpinbadversions = YLeaf(YType.uint32, "snmpInBadVersions")

            self.snmpingenerrs = YLeaf(YType.uint32, "snmpInGenErrs")

            self.snmpingetnexts = YLeaf(YType.uint32, "snmpInGetNexts")

            self.snmpingetrequests = YLeaf(YType.uint32, "snmpInGetRequests")

            self.snmpingetresponses = YLeaf(YType.uint32, "snmpInGetResponses")

            self.snmpinnosuchnames = YLeaf(YType.uint32, "snmpInNoSuchNames")

            self.snmpinpkts = YLeaf(YType.uint32, "snmpInPkts")

            self.snmpinreadonlys = YLeaf(YType.uint32, "snmpInReadOnlys")

            self.snmpinsetrequests = YLeaf(YType.uint32, "snmpInSetRequests")

            self.snmpintoobigs = YLeaf(YType.uint32, "snmpInTooBigs")

            self.snmpintotalreqvars = YLeaf(YType.uint32, "snmpInTotalReqVars")

            self.snmpintotalsetvars = YLeaf(YType.uint32, "snmpInTotalSetVars")

            self.snmpintraps = YLeaf(YType.uint32, "snmpInTraps")

            self.snmpoutbadvalues = YLeaf(YType.uint32, "snmpOutBadValues")

            self.snmpoutgenerrs = YLeaf(YType.uint32, "snmpOutGenErrs")

            self.snmpoutgetnexts = YLeaf(YType.uint32, "snmpOutGetNexts")

            self.snmpoutgetrequests = YLeaf(YType.uint32, "snmpOutGetRequests")

            self.snmpoutgetresponses = YLeaf(YType.uint32, "snmpOutGetResponses")

            self.snmpoutnosuchnames = YLeaf(YType.uint32, "snmpOutNoSuchNames")

            self.snmpoutpkts = YLeaf(YType.uint32, "snmpOutPkts")

            self.snmpoutsetrequests = YLeaf(YType.uint32, "snmpOutSetRequests")

            self.snmpouttoobigs = YLeaf(YType.uint32, "snmpOutTooBigs")

            self.snmpouttraps = YLeaf(YType.uint32, "snmpOutTraps")

            self.snmpproxydrops = YLeaf(YType.uint32, "snmpProxyDrops")

            self.snmpsilentdrops = YLeaf(YType.uint32, "snmpSilentDrops")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("snmpenableauthentraps",
                            "snmpinasnparseerrs",
                            "snmpinbadcommunitynames",
                            "snmpinbadcommunityuses",
                            "snmpinbadvalues",
                            "snmpinbadversions",
                            "snmpingenerrs",
                            "snmpingetnexts",
                            "snmpingetrequests",
                            "snmpingetresponses",
                            "snmpinnosuchnames",
                            "snmpinpkts",
                            "snmpinreadonlys",
                            "snmpinsetrequests",
                            "snmpintoobigs",
                            "snmpintotalreqvars",
                            "snmpintotalsetvars",
                            "snmpintraps",
                            "snmpoutbadvalues",
                            "snmpoutgenerrs",
                            "snmpoutgetnexts",
                            "snmpoutgetrequests",
                            "snmpoutgetresponses",
                            "snmpoutnosuchnames",
                            "snmpoutpkts",
                            "snmpoutsetrequests",
                            "snmpouttoobigs",
                            "snmpouttraps",
                            "snmpproxydrops",
                            "snmpsilentdrops") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Snmpv2Mib.Snmp, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Snmpv2Mib.Snmp, self).__setattr__(name, value)

        class Snmpenableauthentraps(Enum):
            """
            Snmpenableauthentraps

            Indicates whether the SNMP entity is permitted to

            generate authenticationFailure traps.  The value of this

            object overrides any configuration information; as such,

            it provides a means whereby all authenticationFailure

            traps may be disabled.

            Note that it is strongly recommended that this object

            be stored in non\-volatile memory so that it remains

            constant across re\-initializations of the network

            management system.

            .. data:: enabled = 1

            .. data:: disabled = 2

            """

            enabled = Enum.YLeaf(1, "enabled")

            disabled = Enum.YLeaf(2, "disabled")


        def has_data(self):
            return (
                self.snmpenableauthentraps.is_set or
                self.snmpinasnparseerrs.is_set or
                self.snmpinbadcommunitynames.is_set or
                self.snmpinbadcommunityuses.is_set or
                self.snmpinbadvalues.is_set or
                self.snmpinbadversions.is_set or
                self.snmpingenerrs.is_set or
                self.snmpingetnexts.is_set or
                self.snmpingetrequests.is_set or
                self.snmpingetresponses.is_set or
                self.snmpinnosuchnames.is_set or
                self.snmpinpkts.is_set or
                self.snmpinreadonlys.is_set or
                self.snmpinsetrequests.is_set or
                self.snmpintoobigs.is_set or
                self.snmpintotalreqvars.is_set or
                self.snmpintotalsetvars.is_set or
                self.snmpintraps.is_set or
                self.snmpoutbadvalues.is_set or
                self.snmpoutgenerrs.is_set or
                self.snmpoutgetnexts.is_set or
                self.snmpoutgetrequests.is_set or
                self.snmpoutgetresponses.is_set or
                self.snmpoutnosuchnames.is_set or
                self.snmpoutpkts.is_set or
                self.snmpoutsetrequests.is_set or
                self.snmpouttoobigs.is_set or
                self.snmpouttraps.is_set or
                self.snmpproxydrops.is_set or
                self.snmpsilentdrops.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.snmpenableauthentraps.yfilter != YFilter.not_set or
                self.snmpinasnparseerrs.yfilter != YFilter.not_set or
                self.snmpinbadcommunitynames.yfilter != YFilter.not_set or
                self.snmpinbadcommunityuses.yfilter != YFilter.not_set or
                self.snmpinbadvalues.yfilter != YFilter.not_set or
                self.snmpinbadversions.yfilter != YFilter.not_set or
                self.snmpingenerrs.yfilter != YFilter.not_set or
                self.snmpingetnexts.yfilter != YFilter.not_set or
                self.snmpingetrequests.yfilter != YFilter.not_set or
                self.snmpingetresponses.yfilter != YFilter.not_set or
                self.snmpinnosuchnames.yfilter != YFilter.not_set or
                self.snmpinpkts.yfilter != YFilter.not_set or
                self.snmpinreadonlys.yfilter != YFilter.not_set or
                self.snmpinsetrequests.yfilter != YFilter.not_set or
                self.snmpintoobigs.yfilter != YFilter.not_set or
                self.snmpintotalreqvars.yfilter != YFilter.not_set or
                self.snmpintotalsetvars.yfilter != YFilter.not_set or
                self.snmpintraps.yfilter != YFilter.not_set or
                self.snmpoutbadvalues.yfilter != YFilter.not_set or
                self.snmpoutgenerrs.yfilter != YFilter.not_set or
                self.snmpoutgetnexts.yfilter != YFilter.not_set or
                self.snmpoutgetrequests.yfilter != YFilter.not_set or
                self.snmpoutgetresponses.yfilter != YFilter.not_set or
                self.snmpoutnosuchnames.yfilter != YFilter.not_set or
                self.snmpoutpkts.yfilter != YFilter.not_set or
                self.snmpoutsetrequests.yfilter != YFilter.not_set or
                self.snmpouttoobigs.yfilter != YFilter.not_set or
                self.snmpouttraps.yfilter != YFilter.not_set or
                self.snmpproxydrops.yfilter != YFilter.not_set or
                self.snmpsilentdrops.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "snmp" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SNMPv2-MIB:SNMPv2-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.snmpenableauthentraps.is_set or self.snmpenableauthentraps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpenableauthentraps.get_name_leafdata())
            if (self.snmpinasnparseerrs.is_set or self.snmpinasnparseerrs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpinasnparseerrs.get_name_leafdata())
            if (self.snmpinbadcommunitynames.is_set or self.snmpinbadcommunitynames.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpinbadcommunitynames.get_name_leafdata())
            if (self.snmpinbadcommunityuses.is_set or self.snmpinbadcommunityuses.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpinbadcommunityuses.get_name_leafdata())
            if (self.snmpinbadvalues.is_set or self.snmpinbadvalues.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpinbadvalues.get_name_leafdata())
            if (self.snmpinbadversions.is_set or self.snmpinbadversions.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpinbadversions.get_name_leafdata())
            if (self.snmpingenerrs.is_set or self.snmpingenerrs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpingenerrs.get_name_leafdata())
            if (self.snmpingetnexts.is_set or self.snmpingetnexts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpingetnexts.get_name_leafdata())
            if (self.snmpingetrequests.is_set or self.snmpingetrequests.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpingetrequests.get_name_leafdata())
            if (self.snmpingetresponses.is_set or self.snmpingetresponses.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpingetresponses.get_name_leafdata())
            if (self.snmpinnosuchnames.is_set or self.snmpinnosuchnames.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpinnosuchnames.get_name_leafdata())
            if (self.snmpinpkts.is_set or self.snmpinpkts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpinpkts.get_name_leafdata())
            if (self.snmpinreadonlys.is_set or self.snmpinreadonlys.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpinreadonlys.get_name_leafdata())
            if (self.snmpinsetrequests.is_set or self.snmpinsetrequests.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpinsetrequests.get_name_leafdata())
            if (self.snmpintoobigs.is_set or self.snmpintoobigs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpintoobigs.get_name_leafdata())
            if (self.snmpintotalreqvars.is_set or self.snmpintotalreqvars.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpintotalreqvars.get_name_leafdata())
            if (self.snmpintotalsetvars.is_set or self.snmpintotalsetvars.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpintotalsetvars.get_name_leafdata())
            if (self.snmpintraps.is_set or self.snmpintraps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpintraps.get_name_leafdata())
            if (self.snmpoutbadvalues.is_set or self.snmpoutbadvalues.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpoutbadvalues.get_name_leafdata())
            if (self.snmpoutgenerrs.is_set or self.snmpoutgenerrs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpoutgenerrs.get_name_leafdata())
            if (self.snmpoutgetnexts.is_set or self.snmpoutgetnexts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpoutgetnexts.get_name_leafdata())
            if (self.snmpoutgetrequests.is_set or self.snmpoutgetrequests.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpoutgetrequests.get_name_leafdata())
            if (self.snmpoutgetresponses.is_set or self.snmpoutgetresponses.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpoutgetresponses.get_name_leafdata())
            if (self.snmpoutnosuchnames.is_set or self.snmpoutnosuchnames.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpoutnosuchnames.get_name_leafdata())
            if (self.snmpoutpkts.is_set or self.snmpoutpkts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpoutpkts.get_name_leafdata())
            if (self.snmpoutsetrequests.is_set or self.snmpoutsetrequests.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpoutsetrequests.get_name_leafdata())
            if (self.snmpouttoobigs.is_set or self.snmpouttoobigs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpouttoobigs.get_name_leafdata())
            if (self.snmpouttraps.is_set or self.snmpouttraps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpouttraps.get_name_leafdata())
            if (self.snmpproxydrops.is_set or self.snmpproxydrops.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpproxydrops.get_name_leafdata())
            if (self.snmpsilentdrops.is_set or self.snmpsilentdrops.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpsilentdrops.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "snmpEnableAuthenTraps" or name == "snmpInASNParseErrs" or name == "snmpInBadCommunityNames" or name == "snmpInBadCommunityUses" or name == "snmpInBadValues" or name == "snmpInBadVersions" or name == "snmpInGenErrs" or name == "snmpInGetNexts" or name == "snmpInGetRequests" or name == "snmpInGetResponses" or name == "snmpInNoSuchNames" or name == "snmpInPkts" or name == "snmpInReadOnlys" or name == "snmpInSetRequests" or name == "snmpInTooBigs" or name == "snmpInTotalReqVars" or name == "snmpInTotalSetVars" or name == "snmpInTraps" or name == "snmpOutBadValues" or name == "snmpOutGenErrs" or name == "snmpOutGetNexts" or name == "snmpOutGetRequests" or name == "snmpOutGetResponses" or name == "snmpOutNoSuchNames" or name == "snmpOutPkts" or name == "snmpOutSetRequests" or name == "snmpOutTooBigs" or name == "snmpOutTraps" or name == "snmpProxyDrops" or name == "snmpSilentDrops"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "snmpEnableAuthenTraps"):
                self.snmpenableauthentraps = value
                self.snmpenableauthentraps.value_namespace = name_space
                self.snmpenableauthentraps.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInASNParseErrs"):
                self.snmpinasnparseerrs = value
                self.snmpinasnparseerrs.value_namespace = name_space
                self.snmpinasnparseerrs.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInBadCommunityNames"):
                self.snmpinbadcommunitynames = value
                self.snmpinbadcommunitynames.value_namespace = name_space
                self.snmpinbadcommunitynames.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInBadCommunityUses"):
                self.snmpinbadcommunityuses = value
                self.snmpinbadcommunityuses.value_namespace = name_space
                self.snmpinbadcommunityuses.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInBadValues"):
                self.snmpinbadvalues = value
                self.snmpinbadvalues.value_namespace = name_space
                self.snmpinbadvalues.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInBadVersions"):
                self.snmpinbadversions = value
                self.snmpinbadversions.value_namespace = name_space
                self.snmpinbadversions.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInGenErrs"):
                self.snmpingenerrs = value
                self.snmpingenerrs.value_namespace = name_space
                self.snmpingenerrs.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInGetNexts"):
                self.snmpingetnexts = value
                self.snmpingetnexts.value_namespace = name_space
                self.snmpingetnexts.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInGetRequests"):
                self.snmpingetrequests = value
                self.snmpingetrequests.value_namespace = name_space
                self.snmpingetrequests.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInGetResponses"):
                self.snmpingetresponses = value
                self.snmpingetresponses.value_namespace = name_space
                self.snmpingetresponses.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInNoSuchNames"):
                self.snmpinnosuchnames = value
                self.snmpinnosuchnames.value_namespace = name_space
                self.snmpinnosuchnames.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInPkts"):
                self.snmpinpkts = value
                self.snmpinpkts.value_namespace = name_space
                self.snmpinpkts.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInReadOnlys"):
                self.snmpinreadonlys = value
                self.snmpinreadonlys.value_namespace = name_space
                self.snmpinreadonlys.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInSetRequests"):
                self.snmpinsetrequests = value
                self.snmpinsetrequests.value_namespace = name_space
                self.snmpinsetrequests.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInTooBigs"):
                self.snmpintoobigs = value
                self.snmpintoobigs.value_namespace = name_space
                self.snmpintoobigs.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInTotalReqVars"):
                self.snmpintotalreqvars = value
                self.snmpintotalreqvars.value_namespace = name_space
                self.snmpintotalreqvars.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInTotalSetVars"):
                self.snmpintotalsetvars = value
                self.snmpintotalsetvars.value_namespace = name_space
                self.snmpintotalsetvars.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpInTraps"):
                self.snmpintraps = value
                self.snmpintraps.value_namespace = name_space
                self.snmpintraps.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpOutBadValues"):
                self.snmpoutbadvalues = value
                self.snmpoutbadvalues.value_namespace = name_space
                self.snmpoutbadvalues.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpOutGenErrs"):
                self.snmpoutgenerrs = value
                self.snmpoutgenerrs.value_namespace = name_space
                self.snmpoutgenerrs.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpOutGetNexts"):
                self.snmpoutgetnexts = value
                self.snmpoutgetnexts.value_namespace = name_space
                self.snmpoutgetnexts.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpOutGetRequests"):
                self.snmpoutgetrequests = value
                self.snmpoutgetrequests.value_namespace = name_space
                self.snmpoutgetrequests.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpOutGetResponses"):
                self.snmpoutgetresponses = value
                self.snmpoutgetresponses.value_namespace = name_space
                self.snmpoutgetresponses.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpOutNoSuchNames"):
                self.snmpoutnosuchnames = value
                self.snmpoutnosuchnames.value_namespace = name_space
                self.snmpoutnosuchnames.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpOutPkts"):
                self.snmpoutpkts = value
                self.snmpoutpkts.value_namespace = name_space
                self.snmpoutpkts.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpOutSetRequests"):
                self.snmpoutsetrequests = value
                self.snmpoutsetrequests.value_namespace = name_space
                self.snmpoutsetrequests.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpOutTooBigs"):
                self.snmpouttoobigs = value
                self.snmpouttoobigs.value_namespace = name_space
                self.snmpouttoobigs.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpOutTraps"):
                self.snmpouttraps = value
                self.snmpouttraps.value_namespace = name_space
                self.snmpouttraps.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpProxyDrops"):
                self.snmpproxydrops = value
                self.snmpproxydrops.value_namespace = name_space
                self.snmpproxydrops.value_namespace_prefix = name_space_prefix
            if(value_path == "snmpSilentDrops"):
                self.snmpsilentdrops = value
                self.snmpsilentdrops.value_namespace = name_space
                self.snmpsilentdrops.value_namespace_prefix = name_space_prefix


    class Snmpset(Entity):
        """
        
        
        .. attribute:: snmpsetserialno
        
        	An advisory lock used to allow several cooperating command generator applications to coordinate their use of the SNMP set operation.  This object is used for coarse\-grain coordination. To achieve fine\-grain coordination, one or more similar objects might be defined within each MIB group, as appropriate
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'SNMPv2-MIB'
        _revision = '2002-10-16'

        def __init__(self):
            super(Snmpv2Mib.Snmpset, self).__init__()

            self.yang_name = "snmpSet"
            self.yang_parent_name = "SNMPv2-MIB"

            self.snmpsetserialno = YLeaf(YType.int32, "snmpSetSerialNo")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("snmpsetserialno") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Snmpv2Mib.Snmpset, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Snmpv2Mib.Snmpset, self).__setattr__(name, value)

        def has_data(self):
            return self.snmpsetserialno.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.snmpsetserialno.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "snmpSet" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SNMPv2-MIB:SNMPv2-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.snmpsetserialno.is_set or self.snmpsetserialno.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snmpsetserialno.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "snmpSetSerialNo"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "snmpSetSerialNo"):
                self.snmpsetserialno = value
                self.snmpsetserialno.value_namespace = name_space
                self.snmpsetserialno.value_namespace_prefix = name_space_prefix


    class Sysortable(Entity):
        """
        The (conceptual) table listing the capabilities of
        the local SNMP application acting as a command
        responder with respect to various MIB modules.
        SNMP entities having dynamically\-configurable support
        of MIB modules will have a dynamically\-varying number
        of conceptual rows.
        
        .. attribute:: sysorentry
        
        	An entry (conceptual row) in the sysORTable
        	**type**\: list of    :py:class:`Sysorentry <ydk.models.cisco_ios_xe.SNMPv2_MIB.Snmpv2Mib.Sysortable.Sysorentry>`
        
        

        """

        _prefix = 'SNMPv2-MIB'
        _revision = '2002-10-16'

        def __init__(self):
            super(Snmpv2Mib.Sysortable, self).__init__()

            self.yang_name = "sysORTable"
            self.yang_parent_name = "SNMPv2-MIB"

            self.sysorentry = YList(self)

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
                        super(Snmpv2Mib.Sysortable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Snmpv2Mib.Sysortable, self).__setattr__(name, value)


        class Sysorentry(Entity):
            """
            An entry (conceptual row) in the sysORTable.
            
            .. attribute:: sysorindex  <key>
            
            	The auxiliary variable used for identifying instances of the columnar objects in the sysORTable
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: sysordescr
            
            	A textual description of the capabilities identified by the corresponding instance of sysORID
            	**type**\:  str
            
            .. attribute:: sysorid
            
            	An authoritative identification of a capabilities statement with respect to various MIB modules supported by the local SNMP application acting as a command responder
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: sysoruptime
            
            	The value of sysUpTime at the time this conceptual row was last instantiated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'SNMPv2-MIB'
            _revision = '2002-10-16'

            def __init__(self):
                super(Snmpv2Mib.Sysortable.Sysorentry, self).__init__()

                self.yang_name = "sysOREntry"
                self.yang_parent_name = "sysORTable"

                self.sysorindex = YLeaf(YType.int32, "sysORIndex")

                self.sysordescr = YLeaf(YType.str, "sysORDescr")

                self.sysorid = YLeaf(YType.str, "sysORID")

                self.sysoruptime = YLeaf(YType.uint32, "sysORUpTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("sysorindex",
                                "sysordescr",
                                "sysorid",
                                "sysoruptime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Snmpv2Mib.Sysortable.Sysorentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Snmpv2Mib.Sysortable.Sysorentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.sysorindex.is_set or
                    self.sysordescr.is_set or
                    self.sysorid.is_set or
                    self.sysoruptime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.sysorindex.yfilter != YFilter.not_set or
                    self.sysordescr.yfilter != YFilter.not_set or
                    self.sysorid.yfilter != YFilter.not_set or
                    self.sysoruptime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sysOREntry" + "[sysORIndex='" + self.sysorindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "SNMPv2-MIB:SNMPv2-MIB/sysORTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.sysorindex.is_set or self.sysorindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sysorindex.get_name_leafdata())
                if (self.sysordescr.is_set or self.sysordescr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sysordescr.get_name_leafdata())
                if (self.sysorid.is_set or self.sysorid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sysorid.get_name_leafdata())
                if (self.sysoruptime.is_set or self.sysoruptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sysoruptime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "sysORIndex" or name == "sysORDescr" or name == "sysORID" or name == "sysORUpTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "sysORIndex"):
                    self.sysorindex = value
                    self.sysorindex.value_namespace = name_space
                    self.sysorindex.value_namespace_prefix = name_space_prefix
                if(value_path == "sysORDescr"):
                    self.sysordescr = value
                    self.sysordescr.value_namespace = name_space
                    self.sysordescr.value_namespace_prefix = name_space_prefix
                if(value_path == "sysORID"):
                    self.sysorid = value
                    self.sysorid.value_namespace = name_space
                    self.sysorid.value_namespace_prefix = name_space_prefix
                if(value_path == "sysORUpTime"):
                    self.sysoruptime = value
                    self.sysoruptime.value_namespace = name_space
                    self.sysoruptime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.sysorentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.sysorentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sysORTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "SNMPv2-MIB:SNMPv2-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "sysOREntry"):
                for c in self.sysorentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Snmpv2Mib.Sysortable.Sysorentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.sysorentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sysOREntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.snmp is not None and self.snmp.has_data()) or
            (self.snmpset is not None and self.snmpset.has_data()) or
            (self.sysortable is not None and self.sysortable.has_data()) or
            (self.system is not None and self.system.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.snmp is not None and self.snmp.has_operation()) or
            (self.snmpset is not None and self.snmpset.has_operation()) or
            (self.sysortable is not None and self.sysortable.has_operation()) or
            (self.system is not None and self.system.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "SNMPv2-MIB:SNMPv2-MIB" + path_buffer

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

        if (child_yang_name == "snmp"):
            if (self.snmp is None):
                self.snmp = Snmpv2Mib.Snmp()
                self.snmp.parent = self
                self._children_name_map["snmp"] = "snmp"
            return self.snmp

        if (child_yang_name == "snmpSet"):
            if (self.snmpset is None):
                self.snmpset = Snmpv2Mib.Snmpset()
                self.snmpset.parent = self
                self._children_name_map["snmpset"] = "snmpSet"
            return self.snmpset

        if (child_yang_name == "sysORTable"):
            if (self.sysortable is None):
                self.sysortable = Snmpv2Mib.Sysortable()
                self.sysortable.parent = self
                self._children_name_map["sysortable"] = "sysORTable"
            return self.sysortable

        if (child_yang_name == "system"):
            if (self.system is None):
                self.system = Snmpv2Mib.System()
                self.system.parent = self
                self._children_name_map["system"] = "system"
            return self.system

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "snmp" or name == "snmpSet" or name == "sysORTable" or name == "system"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Snmpv2Mib()
        return self._top_entity


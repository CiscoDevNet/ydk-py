""" SNMPv2_MIB 

The MIB module for SNMP entities.

Copyright (C) The Internet Society (2002). This
version of this MIB module is part of RFC 3418;
see the RFC itself for full legal notices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SNMPv2MIB(Entity):
    """
    
    
    .. attribute:: system
    
    	
    	**type**\:  :py:class:`System <ydk.models.cisco_ios_xe.SNMPv2_MIB.SNMPv2MIB.System>`
    
    .. attribute:: snmp
    
    	
    	**type**\:  :py:class:`Snmp <ydk.models.cisco_ios_xe.SNMPv2_MIB.SNMPv2MIB.Snmp>`
    
    .. attribute:: snmpset
    
    	
    	**type**\:  :py:class:`Snmpset <ydk.models.cisco_ios_xe.SNMPv2_MIB.SNMPv2MIB.Snmpset>`
    
    .. attribute:: sysortable
    
    	The (conceptual) table listing the capabilities of the local SNMP application acting as a command responder with respect to various MIB modules. SNMP entities having dynamically\-configurable support of MIB modules will have a dynamically\-varying number of conceptual rows
    	**type**\:  :py:class:`Sysortable <ydk.models.cisco_ios_xe.SNMPv2_MIB.SNMPv2MIB.Sysortable>`
    
    

    """

    _prefix = 'SNMPv2-MIB'
    _revision = '2002-10-16'

    def __init__(self):
        super(SNMPv2MIB, self).__init__()
        self._top_entity = None

        self.yang_name = "SNMPv2-MIB"
        self.yang_parent_name = "SNMPv2-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("system", ("system", SNMPv2MIB.System)), ("snmp", ("snmp", SNMPv2MIB.Snmp)), ("snmpSet", ("snmpset", SNMPv2MIB.Snmpset)), ("sysORTable", ("sysortable", SNMPv2MIB.Sysortable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.system = SNMPv2MIB.System()
        self.system.parent = self
        self._children_name_map["system"] = "system"
        self._children_yang_names.add("system")

        self.snmp = SNMPv2MIB.Snmp()
        self.snmp.parent = self
        self._children_name_map["snmp"] = "snmp"
        self._children_yang_names.add("snmp")

        self.snmpset = SNMPv2MIB.Snmpset()
        self.snmpset.parent = self
        self._children_name_map["snmpset"] = "snmpSet"
        self._children_yang_names.add("snmpSet")

        self.sysortable = SNMPv2MIB.Sysortable()
        self.sysortable.parent = self
        self._children_name_map["sysortable"] = "sysORTable"
        self._children_yang_names.add("sysORTable")
        self._segment_path = lambda: "SNMPv2-MIB:SNMPv2-MIB"


    class System(Entity):
        """
        
        
        .. attribute:: sysdescr
        
        	A textual description of the entity.  This value should include the full name and version identification of the system's hardware type, software operating\-system, and networking software
        	**type**\: str
        
        	**length:** 0..255
        
        .. attribute:: sysobjectid
        
        	The vendor's authoritative identification of the network management subsystem contained in the entity. This value is allocated within the SMI enterprises subtree (1.3.6.1.4.1) and provides an easy and unambiguous means for determining `what kind of box' is being managed.  For example, if vendor `Flintstones, Inc.' was assigned the subtree 1.3.6.1.4.1.424242, it could assign the identifier 1.3.6.1.4.1.424242.1.1 to its `Fred Router'
        	**type**\: str
        
        	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
        
        .. attribute:: sysuptime
        
        	The time (in hundredths of a second) since the network management portion of the system was last re\-initialized
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: syscontact
        
        	The textual identification of the contact person for this managed node, together with information on how to contact this person.  If no contact information is known, the value is the zero\-length string
        	**type**\: str
        
        	**length:** 0..255
        
        .. attribute:: sysname
        
        	An administratively\-assigned name for this managed node.  By convention, this is the node's fully\-qualified domain name.  If the name is unknown, the value is the zero\-length string
        	**type**\: str
        
        	**length:** 0..255
        
        .. attribute:: syslocation
        
        	The physical location of this node (e.g., 'telephone closet, 3rd floor').  If the location is unknown, the value is the zero\-length string
        	**type**\: str
        
        	**length:** 0..255
        
        .. attribute:: sysservices
        
        	A value which indicates the set of services that this entity may potentially offer.  The value is a sum. This sum initially takes the value zero. Then, for each layer, L, in the range 1 through 7, that this node performs transactions for, 2 raised to (L \- 1) is added to the sum.  For example, a node which performs only routing functions would have a value of 4 (2^(3\-1)). In contrast, a node which is a host offering application services would have a value of 72 (2^(4\-1) + 2^(7\-1)). Note that in the context of the Internet suite of protocols, values should be calculated accordingly\:       layer      functionality        1        physical (e.g., repeaters)        2        datalink/subnetwork (e.g., bridges)        3        internet (e.g., supports the IP)        4        end\-to\-end  (e.g., supports the TCP)        7        applications (e.g., supports the SMTP)  For systems including OSI protocols, layers 5 and 6 may also be counted
        	**type**\: int
        
        	**range:** 0..127
        
        .. attribute:: sysorlastchange
        
        	The value of sysUpTime at the time of the most recent change in state or value of any instance of sysORID
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'SNMPv2-MIB'
        _revision = '2002-10-16'

        def __init__(self):
            super(SNMPv2MIB.System, self).__init__()

            self.yang_name = "system"
            self.yang_parent_name = "SNMPv2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('sysdescr', YLeaf(YType.str, 'sysDescr')),
                ('sysobjectid', YLeaf(YType.str, 'sysObjectID')),
                ('sysuptime', YLeaf(YType.uint32, 'sysUpTime')),
                ('syscontact', YLeaf(YType.str, 'sysContact')),
                ('sysname', YLeaf(YType.str, 'sysName')),
                ('syslocation', YLeaf(YType.str, 'sysLocation')),
                ('sysservices', YLeaf(YType.int32, 'sysServices')),
                ('sysorlastchange', YLeaf(YType.uint32, 'sysORLastChange')),
            ])
            self.sysdescr = None
            self.sysobjectid = None
            self.sysuptime = None
            self.syscontact = None
            self.sysname = None
            self.syslocation = None
            self.sysservices = None
            self.sysorlastchange = None
            self._segment_path = lambda: "system"
            self._absolute_path = lambda: "SNMPv2-MIB:SNMPv2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPv2MIB.System, ['sysdescr', 'sysobjectid', 'sysuptime', 'syscontact', 'sysname', 'syslocation', 'sysservices', 'sysorlastchange'], name, value)


    class Snmp(Entity):
        """
        
        
        .. attribute:: snmpinpkts
        
        	The total number of messages delivered to the SNMP entity from the transport service
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpoutpkts
        
        	The total number of SNMP Messages which were passed from the SNMP protocol entity to the transport service
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpinbadversions
        
        	The total number of SNMP messages which were delivered to the SNMP entity and were for an unsupported SNMP version
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinbadcommunitynames
        
        	The total number of community\-based SNMP messages (for example,  SNMPv1) delivered to the SNMP entity which used an SNMP community name not known to said entity. Also, implementations which authenticate community\-based SNMP messages using check(s) in addition to matching the community name (for example, by also checking whether the message originated from a transport address allowed to use a specified community name) MAY include in this value the number of messages which failed the additional check(s).  It is strongly RECOMMENDED that the documentation for any security model which is used to authenticate community\-based SNMP messages specify the precise conditions that contribute to this value
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinbadcommunityuses
        
        	The total number of community\-based SNMP messages (for example, SNMPv1) delivered to the SNMP entity which represented an SNMP operation that was not allowed for the SNMP community named in the message.  The precise conditions under which this counter is incremented (if at all) depend on how the SNMP entity implements its access control mechanism and how its applications interact with that access control mechanism.  It is strongly RECOMMENDED that the documentation for any access control mechanism which is used to control access to and visibility of MIB instrumentation specify the precise conditions that contribute to this value
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpinasnparseerrs
        
        	The total number of ASN.1 or BER errors encountered by the SNMP entity when decoding received SNMP messages
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpintoobigs
        
        	The total number of SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field was `tooBig'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpinnosuchnames
        
        	The total number of SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field was `noSuchName'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpinbadvalues
        
        	The total number of SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field was `badValue'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpinreadonlys
        
        	The total number valid SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field was `readOnly'.  It should be noted that it is a protocol error to generate an SNMP PDU which contains the value `readOnly' in the error\-status field, as such this object is provided as a means of detecting incorrect implementations of the SNMP
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpingenerrs
        
        	The total number of SNMP PDUs which were delivered to the SNMP protocol entity and for which the value of the error\-status field was `genErr'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpintotalreqvars
        
        	The total number of MIB objects which have been retrieved successfully by the SNMP protocol entity as the result of receiving valid SNMP Get\-Request and Get\-Next PDUs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpintotalsetvars
        
        	The total number of MIB objects which have been altered successfully by the SNMP protocol entity as the result of receiving valid SNMP Set\-Request PDUs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpingetrequests
        
        	The total number of SNMP Get\-Request PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpingetnexts
        
        	The total number of SNMP Get\-Next PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpinsetrequests
        
        	The total number of SNMP Set\-Request PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpingetresponses
        
        	The total number of SNMP Get\-Response PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpintraps
        
        	The total number of SNMP Trap PDUs which have been accepted and processed by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpouttoobigs
        
        	The total number of SNMP PDUs which were generated by the SNMP protocol entity and for which the value of the error\-status field was `tooBig.'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpoutnosuchnames
        
        	The total number of SNMP PDUs which were generated by the SNMP protocol entity and for which the value of the error\-status was `noSuchName'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpoutbadvalues
        
        	The total number of SNMP PDUs which were generated by the SNMP protocol entity and for which the value of the error\-status field was `badValue'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpoutgenerrs
        
        	The total number of SNMP PDUs which were generated by the SNMP protocol entity and for which the value of the error\-status field was `genErr'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpoutgetrequests
        
        	The total number of SNMP Get\-Request PDUs which have been generated by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpoutgetnexts
        
        	The total number of SNMP Get\-Next PDUs which have been generated by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpoutsetrequests
        
        	The total number of SNMP Set\-Request PDUs which have been generated by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpoutgetresponses
        
        	The total number of SNMP Get\-Response PDUs which have been generated by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpouttraps
        
        	The total number of SNMP Trap PDUs which have been generated by the SNMP protocol entity
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: obsolete
        
        .. attribute:: snmpenableauthentraps
        
        	Indicates whether the SNMP entity is permitted to generate authenticationFailure traps.  The value of this object overrides any configuration information; as such, it provides a means whereby all authenticationFailure traps may be disabled.  Note that it is strongly recommended that this object be stored in non\-volatile memory so that it remains constant across re\-initializations of the network management system
        	**type**\:  :py:class:`Snmpenableauthentraps <ydk.models.cisco_ios_xe.SNMPv2_MIB.SNMPv2MIB.Snmp.Snmpenableauthentraps>`
        
        .. attribute:: snmpsilentdrops
        
        	The total number of Confirmed Class PDUs (such as GetRequest\-PDUs, GetNextRequest\-PDUs, GetBulkRequest\-PDUs, SetRequest\-PDUs, and InformRequest\-PDUs) delivered to the SNMP entity which were silently dropped because the size of a reply containing an alternate Response Class PDU (such as a Response\-PDU) with an empty variable\-bindings field was greater than either a local constraint or the maximum message size associated with the originator of the request
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: snmpproxydrops
        
        	The total number of Confirmed Class PDUs (such as GetRequest\-PDUs, GetNextRequest\-PDUs, GetBulkRequest\-PDUs, SetRequest\-PDUs, and InformRequest\-PDUs) delivered to the SNMP entity which were silently dropped because the transmission of the (possibly translated) message to a proxy target failed in a manner (other than a time\-out) such that no Response Class PDU (such as a Response\-PDU) could be returned
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'SNMPv2-MIB'
        _revision = '2002-10-16'

        def __init__(self):
            super(SNMPv2MIB.Snmp, self).__init__()

            self.yang_name = "snmp"
            self.yang_parent_name = "SNMPv2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('snmpinpkts', YLeaf(YType.uint32, 'snmpInPkts')),
                ('snmpoutpkts', YLeaf(YType.uint32, 'snmpOutPkts')),
                ('snmpinbadversions', YLeaf(YType.uint32, 'snmpInBadVersions')),
                ('snmpinbadcommunitynames', YLeaf(YType.uint32, 'snmpInBadCommunityNames')),
                ('snmpinbadcommunityuses', YLeaf(YType.uint32, 'snmpInBadCommunityUses')),
                ('snmpinasnparseerrs', YLeaf(YType.uint32, 'snmpInASNParseErrs')),
                ('snmpintoobigs', YLeaf(YType.uint32, 'snmpInTooBigs')),
                ('snmpinnosuchnames', YLeaf(YType.uint32, 'snmpInNoSuchNames')),
                ('snmpinbadvalues', YLeaf(YType.uint32, 'snmpInBadValues')),
                ('snmpinreadonlys', YLeaf(YType.uint32, 'snmpInReadOnlys')),
                ('snmpingenerrs', YLeaf(YType.uint32, 'snmpInGenErrs')),
                ('snmpintotalreqvars', YLeaf(YType.uint32, 'snmpInTotalReqVars')),
                ('snmpintotalsetvars', YLeaf(YType.uint32, 'snmpInTotalSetVars')),
                ('snmpingetrequests', YLeaf(YType.uint32, 'snmpInGetRequests')),
                ('snmpingetnexts', YLeaf(YType.uint32, 'snmpInGetNexts')),
                ('snmpinsetrequests', YLeaf(YType.uint32, 'snmpInSetRequests')),
                ('snmpingetresponses', YLeaf(YType.uint32, 'snmpInGetResponses')),
                ('snmpintraps', YLeaf(YType.uint32, 'snmpInTraps')),
                ('snmpouttoobigs', YLeaf(YType.uint32, 'snmpOutTooBigs')),
                ('snmpoutnosuchnames', YLeaf(YType.uint32, 'snmpOutNoSuchNames')),
                ('snmpoutbadvalues', YLeaf(YType.uint32, 'snmpOutBadValues')),
                ('snmpoutgenerrs', YLeaf(YType.uint32, 'snmpOutGenErrs')),
                ('snmpoutgetrequests', YLeaf(YType.uint32, 'snmpOutGetRequests')),
                ('snmpoutgetnexts', YLeaf(YType.uint32, 'snmpOutGetNexts')),
                ('snmpoutsetrequests', YLeaf(YType.uint32, 'snmpOutSetRequests')),
                ('snmpoutgetresponses', YLeaf(YType.uint32, 'snmpOutGetResponses')),
                ('snmpouttraps', YLeaf(YType.uint32, 'snmpOutTraps')),
                ('snmpenableauthentraps', YLeaf(YType.enumeration, 'snmpEnableAuthenTraps')),
                ('snmpsilentdrops', YLeaf(YType.uint32, 'snmpSilentDrops')),
                ('snmpproxydrops', YLeaf(YType.uint32, 'snmpProxyDrops')),
            ])
            self.snmpinpkts = None
            self.snmpoutpkts = None
            self.snmpinbadversions = None
            self.snmpinbadcommunitynames = None
            self.snmpinbadcommunityuses = None
            self.snmpinasnparseerrs = None
            self.snmpintoobigs = None
            self.snmpinnosuchnames = None
            self.snmpinbadvalues = None
            self.snmpinreadonlys = None
            self.snmpingenerrs = None
            self.snmpintotalreqvars = None
            self.snmpintotalsetvars = None
            self.snmpingetrequests = None
            self.snmpingetnexts = None
            self.snmpinsetrequests = None
            self.snmpingetresponses = None
            self.snmpintraps = None
            self.snmpouttoobigs = None
            self.snmpoutnosuchnames = None
            self.snmpoutbadvalues = None
            self.snmpoutgenerrs = None
            self.snmpoutgetrequests = None
            self.snmpoutgetnexts = None
            self.snmpoutsetrequests = None
            self.snmpoutgetresponses = None
            self.snmpouttraps = None
            self.snmpenableauthentraps = None
            self.snmpsilentdrops = None
            self.snmpproxydrops = None
            self._segment_path = lambda: "snmp"
            self._absolute_path = lambda: "SNMPv2-MIB:SNMPv2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPv2MIB.Snmp, ['snmpinpkts', 'snmpoutpkts', 'snmpinbadversions', 'snmpinbadcommunitynames', 'snmpinbadcommunityuses', 'snmpinasnparseerrs', 'snmpintoobigs', 'snmpinnosuchnames', 'snmpinbadvalues', 'snmpinreadonlys', 'snmpingenerrs', 'snmpintotalreqvars', 'snmpintotalsetvars', 'snmpingetrequests', 'snmpingetnexts', 'snmpinsetrequests', 'snmpingetresponses', 'snmpintraps', 'snmpouttoobigs', 'snmpoutnosuchnames', 'snmpoutbadvalues', 'snmpoutgenerrs', 'snmpoutgetrequests', 'snmpoutgetnexts', 'snmpoutsetrequests', 'snmpoutgetresponses', 'snmpouttraps', 'snmpenableauthentraps', 'snmpsilentdrops', 'snmpproxydrops'], name, value)

        class Snmpenableauthentraps(Enum):
            """
            Snmpenableauthentraps (Enum Class)

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



    class Snmpset(Entity):
        """
        
        
        .. attribute:: snmpsetserialno
        
        	An advisory lock used to allow several cooperating command generator applications to coordinate their use of the SNMP set operation.  This object is used for coarse\-grain coordination. To achieve fine\-grain coordination, one or more similar objects might be defined within each MIB group, as appropriate
        	**type**\: int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'SNMPv2-MIB'
        _revision = '2002-10-16'

        def __init__(self):
            super(SNMPv2MIB.Snmpset, self).__init__()

            self.yang_name = "snmpSet"
            self.yang_parent_name = "SNMPv2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('snmpsetserialno', YLeaf(YType.int32, 'snmpSetSerialNo')),
            ])
            self.snmpsetserialno = None
            self._segment_path = lambda: "snmpSet"
            self._absolute_path = lambda: "SNMPv2-MIB:SNMPv2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPv2MIB.Snmpset, ['snmpsetserialno'], name, value)


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
        	**type**\: list of  		 :py:class:`Sysorentry <ydk.models.cisco_ios_xe.SNMPv2_MIB.SNMPv2MIB.Sysortable.Sysorentry>`
        
        

        """

        _prefix = 'SNMPv2-MIB'
        _revision = '2002-10-16'

        def __init__(self):
            super(SNMPv2MIB.Sysortable, self).__init__()

            self.yang_name = "sysORTable"
            self.yang_parent_name = "SNMPv2-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("sysOREntry", ("sysorentry", SNMPv2MIB.Sysortable.Sysorentry))])
            self._leafs = OrderedDict()

            self.sysorentry = YList(self)
            self._segment_path = lambda: "sysORTable"
            self._absolute_path = lambda: "SNMPv2-MIB:SNMPv2-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SNMPv2MIB.Sysortable, [], name, value)


        class Sysorentry(Entity):
            """
            An entry (conceptual row) in the sysORTable.
            
            .. attribute:: sysorindex  (key)
            
            	The auxiliary variable used for identifying instances of the columnar objects in the sysORTable
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: sysorid
            
            	An authoritative identification of a capabilities statement with respect to various MIB modules supported by the local SNMP application acting as a command responder
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: sysordescr
            
            	A textual description of the capabilities identified by the corresponding instance of sysORID
            	**type**\: str
            
            .. attribute:: sysoruptime
            
            	The value of sysUpTime at the time this conceptual row was last instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'SNMPv2-MIB'
            _revision = '2002-10-16'

            def __init__(self):
                super(SNMPv2MIB.Sysortable.Sysorentry, self).__init__()

                self.yang_name = "sysOREntry"
                self.yang_parent_name = "sysORTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['sysorindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('sysorindex', YLeaf(YType.int32, 'sysORIndex')),
                    ('sysorid', YLeaf(YType.str, 'sysORID')),
                    ('sysordescr', YLeaf(YType.str, 'sysORDescr')),
                    ('sysoruptime', YLeaf(YType.uint32, 'sysORUpTime')),
                ])
                self.sysorindex = None
                self.sysorid = None
                self.sysordescr = None
                self.sysoruptime = None
                self._segment_path = lambda: "sysOREntry" + "[sysORIndex='" + str(self.sysorindex) + "']"
                self._absolute_path = lambda: "SNMPv2-MIB:SNMPv2-MIB/sysORTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SNMPv2MIB.Sysortable.Sysorentry, ['sysorindex', 'sysorid', 'sysordescr', 'sysoruptime'], name, value)

    def clone_ptr(self):
        self._top_entity = SNMPv2MIB()
        return self._top_entity


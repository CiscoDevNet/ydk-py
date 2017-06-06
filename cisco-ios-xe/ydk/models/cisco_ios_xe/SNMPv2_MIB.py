""" SNMPv2_MIB 

The MIB module for SNMP entities.

Copyright (C) The Internet Society (2002). This
version of this MIB module is part of RFC 3418;
see the RFC itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Snmpv2Mib(object):
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
        self.snmp = Snmpv2Mib.Snmp()
        self.snmp.parent = self
        self.snmpset = Snmpv2Mib.Snmpset()
        self.snmpset.parent = self
        self.sysortable = Snmpv2Mib.Sysortable()
        self.sysortable.parent = self
        self.system = Snmpv2Mib.System()
        self.system.parent = self


    class System(object):
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
            self.parent = None
            self.syscontact = None
            self.sysdescr = None
            self.syslocation = None
            self.sysname = None
            self.sysobjectid = None
            self.sysorlastchange = None
            self.sysservices = None
            self.sysuptime = None

        @property
        def _common_path(self):

            return '/SNMPv2-MIB:SNMPv2-MIB/SNMPv2-MIB:system'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.syscontact is not None:
                return True

            if self.sysdescr is not None:
                return True

            if self.syslocation is not None:
                return True

            if self.sysname is not None:
                return True

            if self.sysobjectid is not None:
                return True

            if self.sysorlastchange is not None:
                return True

            if self.sysservices is not None:
                return True

            if self.sysuptime is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _SNMPv2_MIB as meta
            return meta._meta_table['Snmpv2Mib.System']['meta_info']


    class Snmp(object):
        """
        
        
        .. attribute:: snmpenableauthentraps
        
        	Indicates whether the SNMP entity is permitted to generate authenticationFailure traps.  The value of this object overrides any configuration information; as such, it provides a means whereby all authenticationFailure traps may be disabled.  Note that it is strongly recommended that this object be stored in non\-volatile memory so that it remains constant across re\-initializations of the network management system
        	**type**\:   :py:class:`SnmpenableauthentrapsEnum <ydk.models.cisco_ios_xe.SNMPv2_MIB.Snmpv2Mib.Snmp.SnmpenableauthentrapsEnum>`
        
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
            self.parent = None
            self.snmpenableauthentraps = None
            self.snmpinasnparseerrs = None
            self.snmpinbadcommunitynames = None
            self.snmpinbadcommunityuses = None
            self.snmpinbadvalues = None
            self.snmpinbadversions = None
            self.snmpingenerrs = None
            self.snmpingetnexts = None
            self.snmpingetrequests = None
            self.snmpingetresponses = None
            self.snmpinnosuchnames = None
            self.snmpinpkts = None
            self.snmpinreadonlys = None
            self.snmpinsetrequests = None
            self.snmpintoobigs = None
            self.snmpintotalreqvars = None
            self.snmpintotalsetvars = None
            self.snmpintraps = None
            self.snmpoutbadvalues = None
            self.snmpoutgenerrs = None
            self.snmpoutgetnexts = None
            self.snmpoutgetrequests = None
            self.snmpoutgetresponses = None
            self.snmpoutnosuchnames = None
            self.snmpoutpkts = None
            self.snmpoutsetrequests = None
            self.snmpouttoobigs = None
            self.snmpouttraps = None
            self.snmpproxydrops = None
            self.snmpsilentdrops = None

        class SnmpenableauthentrapsEnum(Enum):
            """
            SnmpenableauthentrapsEnum

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

            enabled = 1

            disabled = 2


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _SNMPv2_MIB as meta
                return meta._meta_table['Snmpv2Mib.Snmp.SnmpenableauthentrapsEnum']


        @property
        def _common_path(self):

            return '/SNMPv2-MIB:SNMPv2-MIB/SNMPv2-MIB:snmp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.snmpenableauthentraps is not None:
                return True

            if self.snmpinasnparseerrs is not None:
                return True

            if self.snmpinbadcommunitynames is not None:
                return True

            if self.snmpinbadcommunityuses is not None:
                return True

            if self.snmpinbadvalues is not None:
                return True

            if self.snmpinbadversions is not None:
                return True

            if self.snmpingenerrs is not None:
                return True

            if self.snmpingetnexts is not None:
                return True

            if self.snmpingetrequests is not None:
                return True

            if self.snmpingetresponses is not None:
                return True

            if self.snmpinnosuchnames is not None:
                return True

            if self.snmpinpkts is not None:
                return True

            if self.snmpinreadonlys is not None:
                return True

            if self.snmpinsetrequests is not None:
                return True

            if self.snmpintoobigs is not None:
                return True

            if self.snmpintotalreqvars is not None:
                return True

            if self.snmpintotalsetvars is not None:
                return True

            if self.snmpintraps is not None:
                return True

            if self.snmpoutbadvalues is not None:
                return True

            if self.snmpoutgenerrs is not None:
                return True

            if self.snmpoutgetnexts is not None:
                return True

            if self.snmpoutgetrequests is not None:
                return True

            if self.snmpoutgetresponses is not None:
                return True

            if self.snmpoutnosuchnames is not None:
                return True

            if self.snmpoutpkts is not None:
                return True

            if self.snmpoutsetrequests is not None:
                return True

            if self.snmpouttoobigs is not None:
                return True

            if self.snmpouttraps is not None:
                return True

            if self.snmpproxydrops is not None:
                return True

            if self.snmpsilentdrops is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _SNMPv2_MIB as meta
            return meta._meta_table['Snmpv2Mib.Snmp']['meta_info']


    class Snmpset(object):
        """
        
        
        .. attribute:: snmpsetserialno
        
        	An advisory lock used to allow several cooperating command generator applications to coordinate their use of the SNMP set operation.  This object is used for coarse\-grain coordination. To achieve fine\-grain coordination, one or more similar objects might be defined within each MIB group, as appropriate
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'SNMPv2-MIB'
        _revision = '2002-10-16'

        def __init__(self):
            self.parent = None
            self.snmpsetserialno = None

        @property
        def _common_path(self):

            return '/SNMPv2-MIB:SNMPv2-MIB/SNMPv2-MIB:snmpSet'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.snmpsetserialno is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _SNMPv2_MIB as meta
            return meta._meta_table['Snmpv2Mib.Snmpset']['meta_info']


    class Sysortable(object):
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
            self.parent = None
            self.sysorentry = YList()
            self.sysorentry.parent = self
            self.sysorentry.name = 'sysorentry'


        class Sysorentry(object):
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
                self.parent = None
                self.sysorindex = None
                self.sysordescr = None
                self.sysorid = None
                self.sysoruptime = None

            @property
            def _common_path(self):
                if self.sysorindex is None:
                    raise YPYModelError('Key property sysorindex is None')

                return '/SNMPv2-MIB:SNMPv2-MIB/SNMPv2-MIB:sysORTable/SNMPv2-MIB:sysOREntry[SNMPv2-MIB:sysORIndex = ' + str(self.sysorindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.sysorindex is not None:
                    return True

                if self.sysordescr is not None:
                    return True

                if self.sysorid is not None:
                    return True

                if self.sysoruptime is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _SNMPv2_MIB as meta
                return meta._meta_table['Snmpv2Mib.Sysortable.Sysorentry']['meta_info']

        @property
        def _common_path(self):

            return '/SNMPv2-MIB:SNMPv2-MIB/SNMPv2-MIB:sysORTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.sysorentry is not None:
                for child_ref in self.sysorentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _SNMPv2_MIB as meta
            return meta._meta_table['Snmpv2Mib.Sysortable']['meta_info']

    @property
    def _common_path(self):

        return '/SNMPv2-MIB:SNMPv2-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.snmp is not None and self.snmp._has_data():
            return True

        if self.snmpset is not None and self.snmpset._has_data():
            return True

        if self.sysortable is not None and self.sysortable._has_data():
            return True

        if self.system is not None and self.system._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _SNMPv2_MIB as meta
        return meta._meta_table['Snmpv2Mib']['meta_info']



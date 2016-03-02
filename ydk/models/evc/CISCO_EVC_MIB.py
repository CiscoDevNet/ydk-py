""" CISCO_EVC_MIB 

Metro Ethernet services can support a wide range of
applications and subscriber needs easily, efficiently
and cost\-effectively.  Using standard Ethernet interfaces, 
subscribers can set up secure, private Ethernet Virtual 
Connections, to connect their sites together and connect 
to business partners, suppliers and the Internet.

This MIB module defines the managed objects and notifications
describing Ethernet Virtual Connections.

Ethernet Virtual Connections (EVC), are defined by the Metro
Ethernet Forum (MEF), as an association between two or more
UNIs.  Frames within an EVC can only be exchanged among the
associated UNIs.  Frames sent into the MEN via a particular
UNI must not be delivered back to the UNI from which it 
originated.  

Along an EVC path, there are demarcation flow points on 
associated ingress and egress interface, of every device, 
through which the EVC passes.  A service instance represents
these flow points where a service passes through an interface.  

From an operational perspective, a service instance serves 
three purposes\: 
    1.  Defines the instance of a particular EVC service on
        a specific interface and identifies all frames that
        belongs to that particular service/flow.
    2.  To provide the capability of applying the configured 
        features to those frames belonging to the service.
    3.  To optionally define how to forward those frames in
        the data\-path.  

The association of a service instance to an EVC depicts
an instance of an Ethernet flow on a particular interface
for an end\-to\-end (UNI\-to\-UNI) Ethernet service for a 
subscriber.

The following diagram illustrates the association of
EVC, UNIs and service instances.  UNI physical ports
are depicted as 'U', and service instances as 'x'.

    CE             MEN            MEN            CE
  \-\-\-\-\-\-\-        \-\-\-\-\-\-\-        \-\-\-\-\-\-\-        \-\-\-\-\-\-\-
  \|     \|        \|     \|   ()   \|     \|        \|     \|
  \|     \|\-\-\-\-\-\-\-\-Ux   x\|\-\-(  )\-\-\|x   xU\-\-\-\-\-\-\-\-\|     \|
  \|     \|        \|     \|   ()   \|     \|        \|     \|
  \-\-\-\-\-\-\-        \-\-\-\-\-\-\-        \-\-\-\-\-\-\-        \-\-\-\-\-\-\-
                 ^                    ^
                 \|                    \|
                 \-\-\-\-\-\-\-\- EVC \-\-\-\-\-\-\-\-\-

This MIB module addresses the functional areas of network
management for EVC, including\:

    The operational mode for interfaces that are providing
    Ethernet service(s).

    The service attributes regarding an interface behaving
    as UNI, such as CE\-VLAN mapping and layer 2 control 
    protocol (eg. stp, vtp, cdp) processing.

    The provisioning of service instances to define flow 
    points for an Ethernet service.

    The operational status of EVCs for notifications
    of status changes, and EVC creation and deletion.

Definition of terms and acronyms\:

    B\-Tag\: Backbone Tag field in Ethernet 802.1ah frame

    CE\: Customer Edge

    CE\-VLAN\: Customer Edge VLAN

    CoS\: Class Of Service

    EVC\: Ethernet Virtual Connection

    I\-SID\: Service Instance Identifier field in Ethernet 
    802.1ah frame

    MAC\: Media Access Control

    MEN\: Metro Ethernet Network 

    NNI\: Network to Network Interface

    OAM\: Operations Administration and Management

    PPPoE\: Point\-to\-Point Protocol over Ethernet

    Service frame\: An Ethernet frame transmitted across the 
    UNI toward the service provider or an Ethernet frame 
    transmitted across the UNI toward the Subscriber.

    Service Instance\: A flow point of an Ethernet service

    Service provider\: The organization providing Ethernet
    service(s).

    Subscriber\: The organization purchasing and/or using 
    Ethernet service(s).

    UNI\: User Network Interface
         The physical demarcation point between the 
         responsibility of the service provider and 
         the responsibility of the Subscriber.

    UNI\-C\: User Network Interface, subscriber side

    UNI\-N\: User Network Interface, service provider side

    VLAN\: Virtual Local Area Network

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum
from ydk.models.snmpv2.SNMPv2_TC import StorageType_Enum
from ydk.models.tc.CISCO_TC import CiscoCosList_Bits

class CevcL2ControlProtocolType_Enum(Enum):
    """
    CevcL2ControlProtocolType_Enum

    Defines the different types of layer 2 control protocols\:
    
    
    'other'
        None of the following.
    
    
    'cdp' 
        Cisco Discovery Protocol.
    
    
    'dtp'
        Dynamic Trunking Protocol.
    
    
    'pagp'
        Port Aggregration Protocol.
    
    
    'udld'
        UniDirectional Link Detection.
    
    
    'vtp' 
        Vlan Trunking Protocol.
    
    
    'lacp'
        Link Aggregation Control Protocol.
    
    
    'dot1x'
        IEEE 802.1x
    
    
    'stp'
        Spanning Tree Protocol.

    """

    OTHER = 1

    CDP = 2

    DTP = 3

    PAGP = 4

    UDLD = 5

    VTP = 6

    LACP = 7

    DOT1X = 8

    STP = 9


    @staticmethod
    def _meta_info():
        from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
        return meta._meta_table['CevcL2ControlProtocolType_Enum']


class CevcMacSecurityViolationCauseType_Enum(Enum):
    """
    CevcMacSecurityViolationCauseType_Enum

    An integer value which identifies the cause for the MAC
    Security Violation.
    
    If the system MAC Address limit is exceeded, the
    cevcMacSecurityViolationCauseType will contain 
    'exceedSystemLimit' value.
    
    If the Bridge domain limit is exceeded, the
    cevcMacSecurityViolationCauseType will contain 
    'exceedBdLimit' value.
    
    If the Service Instance limit is exceeded, the
    cevcMacSecurityViolationCauseType will contain 
    'exceedSILimit' value.
    
    If the MAC address is present in the Black list
    then cevcMacSecurityViolationCauseType will contain 
    'blackListDeny' value.

    """

    EXCEEDSYSTEMLIMIT = 1

    EXCEEDBDLIMIT = 2

    EXCEEDSILIMIT = 3

    BLACKLISTDENY = 4


    @staticmethod
    def _meta_info():
        from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
        return meta._meta_table['CevcMacSecurityViolationCauseType_Enum']


class ServiceInstanceTargetType_Enum(Enum):
    """
    ServiceInstanceTargetType_Enum

    Defines the type of interface/media to which a service instance
    is attached.
    
        'other'
            None of the following.  This value MUST be used if the
            value of the corresponding ServiceInstanceTarget
            object is a zero\-length string.
    
        'interface'
            Service instance is attached to the the interface
            defined by ServiceInstanceInterface textual
            convention.
    
    Each definition of a concrete ServiceInstanceTargetType value
    must be accompanied by a definition of a textual convention for
    use with that ServiceInstanceTargetType.
    
    To support future extensions, the ServiceInstanceTargetType
    textual convention SHOULD NOT be sub\-typed in object type
    definitions.  It MAY be sub\-typed in compliance statements in
    order to require only a subset of these target types for a
    compliant implementation.
    
    Implementations must ensure that ServiceInstanceTargetType
    objects and any dependent objects (e.g. ServiceInstanceTarget
    objects) are consistent.  An inconsistentValue error must be
    generated if an attempt to change an ServiceInstanceTargetType
    object would, for example, lead to an undefined
    ServiceInstanceTarget value.  In particular,
    ServiceInstanceTargetType/ServiceInstanceTarget pairs must be
    changed together if the service instance taget type changes.

    """

    OTHER = 1

    INTERFACE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
        return meta._meta_table['ServiceInstanceTargetType_Enum']



class CISCOEVCMIB(object):
    """
    
    
    .. attribute:: cevcevcnotificationconfig
    
    	
    	**type**\: :py:class:`CevcEvcNotificationConfig <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcEvcNotificationConfig>`
    
    .. attribute:: cevcevcstatetable
    
    	This table lists statical/status data of the EVC.  This table has an one\-to\-one dependent relationship on the cevcEvcTable, containing a row for each EVC
    	**type**\: :py:class:`CevcEvcStateTable <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcEvcStateTable>`
    
    .. attribute:: cevcevctable
    
    	This table contains a list of EVCs and their service attributes
    	**type**\: :py:class:`CevcEvcTable <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcEvcTable>`
    
    .. attribute:: cevcevcunitable
    
    	This table contains a list of UNI's for each EVC configured on the device.  The UNIs can be  local (i.e. physically  located on the system) or remote (i.e. not physically located on the device).  For local UNIs, the UNI Id is the same as  denoted by cevcUniIdentifier with the same ifIndex value as  cevcEvcLocalUniIfIndex.  For remote UNIs, the underlying OAM  protocol, if capable, provides the UNI Id via its protocol  messages.  This table has an expansion dependent relationship on the cevcEvcTable, containing a row for each UNI that is in the EVC
    	**type**\: :py:class:`CevcEvcUniTable <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcEvcUniTable>`
    
    .. attribute:: cevcmacsecurityviolation
    
    	
    	**type**\: :py:class:`CevcMacSecurityViolation <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcMacSecurityViolation>`
    
    .. attribute:: cevcportl2controlprotocoltable
    
    	This table lists the layer 2 control protocol processing attributes at UNI ports.    This table has an expansion dependent relationship on the  cevcUniTable, containing zero or more rows for each UNI
    	**type**\: :py:class:`CevcPortL2ControlProtocolTable <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcPortL2ControlProtocolTable>`
    
    .. attribute:: cevcporttable
    
    	This table provides the operational mode and configuration limitations of the physical interfaces (ports) that provide Ethernet services for the MEN.   This table has a sparse depedent relationship on the ifTable,  containing a row for each ifEntry having an ifType of  'ethernetCsmacd' capable of supporting Ethernet services
    	**type**\: :py:class:`CevcPortTable <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcPortTable>`
    
    .. attribute:: cevcsicevlantable
    
    	This table contains the CE\-VLAN map list for each Service Instance.  This table has an expansion dependent relationship on the cevcSITable, containing a row for each CE\-VLAN or a range of CE\-VLANs that are mapped to a service instance
    	**type**\: :py:class:`CevcSICEVlanTable <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSICEVlanTable>`
    
    .. attribute:: cevcsiforwardbdtable
    
    	This table contains the forwarding bridge domain information for each service instance.  This table has a sparse dependent relationship on the  cevcSITable, containing a row for each service instance having  a cevcSIForwardingType of 'bridgeDomain'
    	**type**\: :py:class:`CevcSIForwardBdTable <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIForwardBdTable>`
    
    .. attribute:: cevcsil2controlprotocoltable
    
    	This table lists the layer 2 control protocol processing attributes at service instances.    This table has an expansion dependent relationship on the  cevcSITable, containing a row for each layer 2  control protocol disposition at each service instance
    	**type**\: :py:class:`CevcSIL2ControlProtocolTable <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIL2ControlProtocolTable>`
    
    .. attribute:: cevcsimatchcriteriatable
    
    	This table contains the match criteria for each Service Instance.  This table has an expansion dependent relationship on the cevcSITable, containing a row for each group of  match criteria of each service instance
    	**type**\: :py:class:`CevcSIMatchCriteriaTable <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIMatchCriteriaTable>`
    
    .. attribute:: cevcsimatchencaptable
    
    	This table contains the encapsulation based match criteria for each service instance.    This table has a sparse dependent relationship on the  cevcSIMatchCriteriaTable, containing a row for each match  criteria having one of the following values for  cevcSIMatchCriteriaType\:      \- 'dot1q'     \- 'dot1ad'     \- 'untaggedAndDot1q'     \- 'untaggedAndDot1ad'     \- 'priorityTagged'
    	**type**\: :py:class:`CevcSIMatchEncapTable <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIMatchEncapTable>`
    
    .. attribute:: cevcsiprimaryvlantable
    
    	This table contains the primary VLAN ID list for each Service Instance.  This table has an expansion dependent relationship on the  cevcSIMatchEncapTable, containing zero or more rows for each  encapsulation match criteria
    	**type**\: :py:class:`CevcSIPrimaryVlanTable <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIPrimaryVlanTable>`
    
    .. attribute:: cevcsisecondaryvlantable
    
    	This table contains the seconadary VLAN ID list for each service instance.  This table has an expansion dependent relationship on the  cevcSIMatchEncapTable, containing zero or more rows for each  encapsulation match criteria
    	**type**\: :py:class:`CevcSISecondaryVlanTable <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSISecondaryVlanTable>`
    
    .. attribute:: cevcsistatetable
    
    	This table lists statical status data of the service instance.  This table has an one\-to\-one dependent relationship on the cevcSITable, containing a row for each service instance
    	**type**\: :py:class:`CevcSIStateTable <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIStateTable>`
    
    .. attribute:: cevcsitable
    
    	This table lists each service instance and its service attributes
    	**type**\: :py:class:`CevcSITable <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSITable>`
    
    .. attribute:: cevcsivlanrewritetable
    
    	This table lists the rewrite adjustments of the service frame's VLAN tags for service instances.  This table has an expansion dependent relationship on the cevcSITable, containing a row for a VLAN adjustment for ingress and egress frames at each service instance
    	**type**\: :py:class:`CevcSIVlanRewriteTable <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIVlanRewriteTable>`
    
    .. attribute:: cevcsystem
    
    	
    	**type**\: :py:class:`CevcSystem <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSystem>`
    
    .. attribute:: cevcunicevlanevctable
    
    	This table contains for each UNI, a list of EVCs and the association of CE\-VLANs to the EVC.  The CE\-VLAN mapping is  locally significant to the UNI.  This table has an expansion dependent relationship on the  cevcUniTable, containing zero or more rows for each UNI
    	**type**\: :py:class:`CevcUniCEVlanEvcTable <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcUniCEVlanEvcTable>`
    
    .. attribute:: cevcunitable
    
    	This table contains a list of UNIs locally configured on the system.  This table has a sparse dependent relationship on the  cevcPortTable, containing a row for each cevcPortEntry having a cevcPortMode column value 'uni'
    	**type**\: :py:class:`CevcUniTable <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcUniTable>`
    
    

    """

    _prefix = 'cisco-evc'
    _revision = '2012-05-21'

    def __init__(self):
        self.cevcevcnotificationconfig = CISCOEVCMIB.CevcEvcNotificationConfig()
        self.cevcevcnotificationconfig.parent = self
        self.cevcevcstatetable = CISCOEVCMIB.CevcEvcStateTable()
        self.cevcevcstatetable.parent = self
        self.cevcevctable = CISCOEVCMIB.CevcEvcTable()
        self.cevcevctable.parent = self
        self.cevcevcunitable = CISCOEVCMIB.CevcEvcUniTable()
        self.cevcevcunitable.parent = self
        self.cevcmacsecurityviolation = CISCOEVCMIB.CevcMacSecurityViolation()
        self.cevcmacsecurityviolation.parent = self
        self.cevcportl2controlprotocoltable = CISCOEVCMIB.CevcPortL2ControlProtocolTable()
        self.cevcportl2controlprotocoltable.parent = self
        self.cevcporttable = CISCOEVCMIB.CevcPortTable()
        self.cevcporttable.parent = self
        self.cevcsicevlantable = CISCOEVCMIB.CevcSICEVlanTable()
        self.cevcsicevlantable.parent = self
        self.cevcsiforwardbdtable = CISCOEVCMIB.CevcSIForwardBdTable()
        self.cevcsiforwardbdtable.parent = self
        self.cevcsil2controlprotocoltable = CISCOEVCMIB.CevcSIL2ControlProtocolTable()
        self.cevcsil2controlprotocoltable.parent = self
        self.cevcsimatchcriteriatable = CISCOEVCMIB.CevcSIMatchCriteriaTable()
        self.cevcsimatchcriteriatable.parent = self
        self.cevcsimatchencaptable = CISCOEVCMIB.CevcSIMatchEncapTable()
        self.cevcsimatchencaptable.parent = self
        self.cevcsiprimaryvlantable = CISCOEVCMIB.CevcSIPrimaryVlanTable()
        self.cevcsiprimaryvlantable.parent = self
        self.cevcsisecondaryvlantable = CISCOEVCMIB.CevcSISecondaryVlanTable()
        self.cevcsisecondaryvlantable.parent = self
        self.cevcsistatetable = CISCOEVCMIB.CevcSIStateTable()
        self.cevcsistatetable.parent = self
        self.cevcsitable = CISCOEVCMIB.CevcSITable()
        self.cevcsitable.parent = self
        self.cevcsivlanrewritetable = CISCOEVCMIB.CevcSIVlanRewriteTable()
        self.cevcsivlanrewritetable.parent = self
        self.cevcsystem = CISCOEVCMIB.CevcSystem()
        self.cevcsystem.parent = self
        self.cevcunicevlanevctable = CISCOEVCMIB.CevcUniCEVlanEvcTable()
        self.cevcunicevlanevctable.parent = self
        self.cevcunitable = CISCOEVCMIB.CevcUniTable()
        self.cevcunitable.parent = self


    class CevcEvcNotificationConfig(object):
        """
        
        
        .. attribute:: cevcevcnotifyenabled
        
        	This object specifies the system generation of notification, including\:      'status'         This bit set to '1' specifies the system          generation of cevcEvcStatusChangedNotification.       'creation'         This bit set to '1' specifies the system        generation of cevcEvcCreationNotification.       'deletion'         This bit set to '1' specifices the system         generation of cevcEvcDeletionNotification.              'macSecurityViolation'       This bit set to '1' specifies the system        generation of cevcMacSecurityViolation
        	**type**\: :py:class:`CevcEvcNotifyEnabled_Bits <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcEvcNotificationConfig.CevcEvcNotifyEnabled_Bits>`
        
        

        """

        _prefix = 'cisco-evc'
        _revision = '2012-05-21'

        def __init__(self):
            self.parent = None
            self.cevcevcnotifyenabled = CISCOEVCMIB.CevcEvcNotificationConfig.CevcEvcNotifyEnabled_Bits()

        class CevcEvcNotifyEnabled_Bits(FixedBitsDict):
            """
            CevcEvcNotifyEnabled_Bits

            This object specifies the system generation of notification,
            including\:
            
                'status'
                    This bit set to '1' specifies the system 
                    generation of cevcEvcStatusChangedNotification.
            
            
                'creation'
                    This bit set to '1' specifies the system
                   generation of cevcEvcCreationNotification.
            
            
                'deletion'
                    This bit set to '1' specifices the system
                    generation of cevcEvcDeletionNotification.
                    
                'macSecurityViolation'
                  This bit set to '1' specifies the system 
                  generation of cevcMacSecurityViolation.
            Keys are:- status , creation , macSecurityViolation , deletion

            """

            def __init__(self):
                self._dictionary = { 
                    'status':False,
                    'creation':False,
                    'macSecurityViolation':False,
                    'deletion':False,
                }
                self._pos_map = { 
                    'status':0,
                    'creation':1,
                    'macSecurityViolation':3,
                    'deletion':2,
                }

        @property
        def _common_path(self):

            return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcEvcNotificationConfig'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cevcevcnotifyenabled is not None:
                if self.cevcevcnotifyenabled._has_data():
                    return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
            return meta._meta_table['CISCOEVCMIB.CevcEvcNotificationConfig']['meta_info']


    class CevcEvcStateTable(object):
        """
        This table lists statical/status data of the EVC.
        
        This table has an one\-to\-one dependent relationship on the
        cevcEvcTable, containing a row for each EVC.
        
        .. attribute:: cevcevcstateentry
        
        	This entry represents status atrributes of an EVC.  The system automatically creates an entry when the system or the EMS/NMS creates a row in the cevcEvcTable.  Likewise, the system automatically destroys an entry when the system or the EMS/NMS destroys the corresponding row in the cevcEvcTable
        	**type**\: list of :py:class:`CevcEvcStateEntry <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcEvcStateTable.CevcEvcStateEntry>`
        
        

        """

        _prefix = 'cisco-evc'
        _revision = '2012-05-21'

        def __init__(self):
            self.parent = None
            self.cevcevcstateentry = YList()
            self.cevcevcstateentry.parent = self
            self.cevcevcstateentry.name = 'cevcevcstateentry'


        class CevcEvcStateEntry(object):
            """
            This entry represents status atrributes of an EVC.
            
            The system automatically creates an entry when the system or
            the EMS/NMS creates a row in the cevcEvcTable.  Likewise, the
            system automatically destroys an entry when the system or the
            EMS/NMS destroys the corresponding row in the cevcEvcTable.
            
            .. attribute:: cevcevcindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cevcevcactiveunis
            
            	This object indicates the number of active UNIs for the EVC in the MEN.  This value is derived from data gathered by  underlying OAM Protocol
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cevcevcoperstatus
            
            	This object specifies the operational status of the EVC\:   'unknown'     Not enough information available regarding the EVC to     determine the operational status at this time or EVC      operational status is undefined.  'active'     Fully operational between the UNIs in the EVC.     'partiallyActive'     Capable of transferring traffic among some but not all     of the UNIs in the EVC.  This operational status is     applicable only for Multipoint\-to\-Multipoint EVCs.   'inactive'     Not capable of transferring traffic among any of the     UNIs in the EVC.    This value is derived from data gathered by underlying OAM protocol
            	**type**\: :py:class:`CevcEvcOperStatus_Enum <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcEvcStateTable.CevcEvcStateEntry.CevcEvcOperStatus_Enum>`
            
            

            """

            _prefix = 'cisco-evc'
            _revision = '2012-05-21'

            def __init__(self):
                self.parent = None
                self.cevcevcindex = None
                self.cevcevcactiveunis = None
                self.cevcevcoperstatus = None

            class CevcEvcOperStatus_Enum(Enum):
                """
                CevcEvcOperStatus_Enum

                This object specifies the operational status of the EVC\:
                
                
                'unknown'
                    Not enough information available regarding the EVC to
                    determine the operational status at this time or EVC 
                    operational status is undefined.
                
                'active'
                    Fully operational between the UNIs in the EVC.  
                
                
                'partiallyActive'
                    Capable of transferring traffic among some but not all
                    of the UNIs in the EVC.  This operational status is
                    applicable only for Multipoint\-to\-Multipoint EVCs.
                
                
                'inactive'
                    Not capable of transferring traffic among any of the
                    UNIs in the EVC.  
                
                This value is derived from data gathered by underlying OAM
                protocol.

                """

                UNKNOWN = 1

                ACTIVE = 2

                PARTIALLYACTIVE = 3

                INACTIVE = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                    return meta._meta_table['CISCOEVCMIB.CevcEvcStateTable.CevcEvcStateEntry.CevcEvcOperStatus_Enum']


            @property
            def _common_path(self):
                if self.cevcevcindex is None:
                    raise YPYDataValidationError('Key property cevcevcindex is None')

                return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcEvcStateTable/CISCO-EVC-MIB:cevcEvcStateEntry[CISCO-EVC-MIB:cevcEvcIndex = ' + str(self.cevcevcindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cevcevcindex is not None:
                    return True

                if self.cevcevcactiveunis is not None:
                    return True

                if self.cevcevcoperstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                return meta._meta_table['CISCOEVCMIB.CevcEvcStateTable.CevcEvcStateEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcEvcStateTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cevcevcstateentry is not None:
                for child_ref in self.cevcevcstateentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
            return meta._meta_table['CISCOEVCMIB.CevcEvcStateTable']['meta_info']


    class CevcEvcTable(object):
        """
        This table contains a list of EVCs and their service
        attributes.
        
        .. attribute:: cevcevcentry
        
        	This entry represents the EVC configured on the system and its service atrributes.  Entries in this table may be created and deleted via the cevcEvcRowStatus object or the management console on the system.  Using SNMP, rows are created by a SET request setting the value of cevcEvcRowStatus column to 'createAndGo'or 'createAndWait'.  Rows are deleted by a SET request setting the value of cevcEvcRowStatus column to 'destroy'
        	**type**\: list of :py:class:`CevcEvcEntry <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcEvcTable.CevcEvcEntry>`
        
        

        """

        _prefix = 'cisco-evc'
        _revision = '2012-05-21'

        def __init__(self):
            self.parent = None
            self.cevcevcentry = YList()
            self.cevcevcentry.parent = self
            self.cevcevcentry.name = 'cevcevcentry'


        class CevcEvcEntry(object):
            """
            This entry represents the EVC configured on the system and
            its service atrributes.
            
            Entries in this table may be created and deleted via the
            cevcEvcRowStatus object or the management console on the
            system.
            
            Using SNMP, rows are created by a SET request setting the value
            of cevcEvcRowStatus column to 'createAndGo'or 'createAndWait'. 
            Rows are deleted by a SET request setting the value of
            cevcEvcRowStatus column to 'destroy'.
            
            .. attribute:: cevcevcindex
            
            	This object indicates an arbitrary integer\-value that uniquely identifies the EVC
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cevcevccfgunis
            
            	This object specifies the number of UNIs expected to be configured for the EVC in the MEN.  The underlying OAM protocol can use this value of UNIs to determine the EVC operational status, cevcEvcOperStatus.  For a  Multipoint\-to\-Multipoint EVC the minimum number of Uni's would be two
            	**type**\: int
            
            	**range:** 2..4294967295
            
            .. attribute:: cevcevcidentifier
            
            	This object specifies a string\-value identifying the EVC. This value should be unique across the MEN
            	**type**\: str
            
            	**range:** 1..100
            
            .. attribute:: cevcevcrowstatus
            
            	This object enables a SNMP peer to create, modify, and delete rows in the cevcEvcTable.   cevcEvcIdentifier column must have a valid value before a  row can be set to 'active'.  Writable objects in this table can be modified while the value of cevcEvcRowStatus column is 'active'.  An entry cannot be deleted if there exists a service instance which is referring to the cevcEvcEntry i.e. cevcSIEvcIndex in the cevcSITable has the same value as cevcEvcIndex being deleted
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: cevcevcstoragetype
            
            	This object specifies how the SNMP entity stores the data contained by the corresponding conceptual row.  This object can be set to either 'volatile' or 'nonVolatile'. Other values are not applicable for this conceptual row and are not supported
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: cevcevctype
            
            	This object specifies the type of EVC\:   'pointToPoint'      Exactly two UNIs are associated with one another.  An     ingress service frame at one UNI must not result in an     egress service frame at a UNI other than the other UNI     in the EVC.   'multipointToMultipoint'     Two or more UNIs are associated with one another.  An     ingress service frame at one UNI must not result in an     egress service frame at a UNI that is not in the EVC
            	**type**\: :py:class:`CevcEvcType_Enum <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcEvcTable.CevcEvcEntry.CevcEvcType_Enum>`
            
            

            """

            _prefix = 'cisco-evc'
            _revision = '2012-05-21'

            def __init__(self):
                self.parent = None
                self.cevcevcindex = None
                self.cevcevccfgunis = None
                self.cevcevcidentifier = None
                self.cevcevcrowstatus = None
                self.cevcevcstoragetype = None
                self.cevcevctype = None

            class CevcEvcType_Enum(Enum):
                """
                CevcEvcType_Enum

                This object specifies the type of EVC\:
                
                
                'pointToPoint' 
                    Exactly two UNIs are associated with one another.  An
                    ingress service frame at one UNI must not result in an
                    egress service frame at a UNI other than the other UNI
                    in the EVC.
                
                
                'multipointToMultipoint'
                    Two or more UNIs are associated with one another.  An
                    ingress service frame at one UNI must not result in an
                    egress service frame at a UNI that is not in the EVC.

                """

                POINTTOPOINT = 1

                MULTIPOINTTOMULTIPOINT = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                    return meta._meta_table['CISCOEVCMIB.CevcEvcTable.CevcEvcEntry.CevcEvcType_Enum']


            @property
            def _common_path(self):
                if self.cevcevcindex is None:
                    raise YPYDataValidationError('Key property cevcevcindex is None')

                return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcEvcTable/CISCO-EVC-MIB:cevcEvcEntry[CISCO-EVC-MIB:cevcEvcIndex = ' + str(self.cevcevcindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cevcevcindex is not None:
                    return True

                if self.cevcevccfgunis is not None:
                    return True

                if self.cevcevcidentifier is not None:
                    return True

                if self.cevcevcrowstatus is not None:
                    return True

                if self.cevcevcstoragetype is not None:
                    return True

                if self.cevcevctype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                return meta._meta_table['CISCOEVCMIB.CevcEvcTable.CevcEvcEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcEvcTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cevcevcentry is not None:
                for child_ref in self.cevcevcentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
            return meta._meta_table['CISCOEVCMIB.CevcEvcTable']['meta_info']


    class CevcEvcUniTable(object):
        """
        This table contains a list of UNI's for each EVC configured
        on the device.  The UNIs can be  local (i.e. physically 
        located on the system) or remote (i.e. not physically located
        on the device).  For local UNIs, the UNI Id is the same as 
        denoted by cevcUniIdentifier with the same ifIndex value as 
        cevcEvcLocalUniIfIndex.  For remote UNIs, the underlying OAM 
        protocol, if capable, provides the UNI Id via its protocol 
        messages.
        
        This table has an expansion dependent relationship on the
        cevcEvcTable, containing a row for each UNI that is in
        the EVC.
        
        .. attribute:: cevcevcunientry
        
        	This entry represents a UNI, either local or remote, in the EVC.  The system automatically creates an entry, when an UNI is attached to the EVC.  Entries are automatically destroyed when the system or the EMS/NMS destroys the corresponding  row in the cevcEvcTable or when an UNI is removed from the EVC
        	**type**\: list of :py:class:`CevcEvcUniEntry <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcEvcUniTable.CevcEvcUniEntry>`
        
        

        """

        _prefix = 'cisco-evc'
        _revision = '2012-05-21'

        def __init__(self):
            self.parent = None
            self.cevcevcunientry = YList()
            self.cevcevcunientry.parent = self
            self.cevcevcunientry.name = 'cevcevcunientry'


        class CevcEvcUniEntry(object):
            """
            This entry represents a UNI, either local or remote, in the
            EVC.
            
            The system automatically creates an entry, when an UNI is
            attached to the EVC.  Entries are automatically destroyed
            when the system or the EMS/NMS destroys the corresponding 
            row in the cevcEvcTable or when an UNI is removed from the
            EVC.
            
            .. attribute:: cevcevcindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cevcevcuniindex
            
            	This object indicates an arbitrary integer\-value that uniquely  identifies the UNI in an EVC
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cevcevclocaluniifindex
            
            	When the UNI is local on the system, this object specifies the ifIndex of the UNI.  The value '0' of this column indicates remote UNI
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cevcevcuniid
            
            	This object indicates the string\-value identifying the UNI that is in the EVC.  For UNI that is local, this value is the same as cevcUniIdentifier for the same ifIndex value as  cevcEvcLocalUniIfIndex.  For UNI that is not on the system,  this value may be derived from the underlying OAM protocol.  If the UNI identifier value is not specified for the UNI or it is unknown, the value of the cevcEvcUniId column is a zero\-length string
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: cevcevcunioperstatus
            
            	This object indicates the operational status derived from data gathered by the OAM protocol for an UNI.       'unknown'          Status is not known; possible reason could be caused         by the OAM protocol has not provided information         regarding the UNI.       'notReachable'         UNI is not reachable; possible reason could be caused         by the OAM protocol messages having not been received         for an excessive length of time.       'up'         UNI is active, up, and able to pass traffic.       'down'         UNI is down and not passing traffic.       'adminDown'         UNI has been administratively put in down state.       'localExcessiveError'         UNI has experienced excessive number of invalid frames         on the local end of the physical link between UNI\-C          and UNI\-N.       'remoteExcessiveError'         UNI has experienced excessive number of invalid frames         on the remote side of the physical connection between         UNI\-C and UNI\-N.       'localInLoopback'         UNI is loopback on the local end of the physical link         between UNI\-C and UNI\-N.       'remoteInLoopback'         UNI is looped back on the remote end of the link          between UNI\-C and UNI\-N.       'localOutLoopback'         UNI just transitioned out of loopback on the local end         of the physcial link between UNI\-C and UNI\-N.      'remoteOutLoopback'         UNI just transitioned out of loopback on the remote          end of the physcial link between UNI\-C and UNI\-N
            	**type**\: :py:class:`CevcEvcUniOperStatus_Enum <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcEvcUniTable.CevcEvcUniEntry.CevcEvcUniOperStatus_Enum>`
            
            

            """

            _prefix = 'cisco-evc'
            _revision = '2012-05-21'

            def __init__(self):
                self.parent = None
                self.cevcevcindex = None
                self.cevcevcuniindex = None
                self.cevcevclocaluniifindex = None
                self.cevcevcuniid = None
                self.cevcevcunioperstatus = None

            class CevcEvcUniOperStatus_Enum(Enum):
                """
                CevcEvcUniOperStatus_Enum

                This object indicates the operational status derived from data
                gathered by the OAM protocol for an UNI.
                
                
                    'unknown' 
                        Status is not known; possible reason could be caused
                        by the OAM protocol has not provided information
                        regarding the UNI.
                
                
                    'notReachable'
                        UNI is not reachable; possible reason could be caused
                        by the OAM protocol messages having not been received
                        for an excessive length of time.
                
                
                    'up'
                        UNI is active, up, and able to pass traffic.
                
                
                    'down'
                        UNI is down and not passing traffic.
                
                
                    'adminDown'
                        UNI has been administratively put in down state.
                
                
                    'localExcessiveError'
                        UNI has experienced excessive number of invalid frames
                        on the local end of the physical link between UNI\-C 
                        and UNI\-N.
                
                
                    'remoteExcessiveError'
                        UNI has experienced excessive number of invalid frames
                        on the remote side of the physical connection between
                        UNI\-C and UNI\-N.
                
                
                    'localInLoopback'
                        UNI is loopback on the local end of the physical link
                        between UNI\-C and UNI\-N.
                
                
                    'remoteInLoopback'
                        UNI is looped back on the remote end of the link 
                        between UNI\-C and UNI\-N.
                
                
                    'localOutLoopback'
                        UNI just transitioned out of loopback on the local end
                        of the physcial link between UNI\-C and UNI\-N.
                
                    'remoteOutLoopback'
                        UNI just transitioned out of loopback on the remote 
                        end of the physcial link between UNI\-C and UNI\-N.

                """

                UNKNOWN = 1

                NOTREACHABLE = 2

                UP = 3

                DOWN = 4

                ADMINDOWN = 5

                LOCALEXCESSIVEERROR = 6

                REMOTEEXCESSIVEERROR = 7

                LOCALINLOOPBACK = 8

                REMOTEINLOOPBACK = 9

                LOCALOUTLOOPBACK = 10

                REMOTEOUTLOOPBACK = 11


                @staticmethod
                def _meta_info():
                    from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                    return meta._meta_table['CISCOEVCMIB.CevcEvcUniTable.CevcEvcUniEntry.CevcEvcUniOperStatus_Enum']


            @property
            def _common_path(self):
                if self.cevcevcindex is None:
                    raise YPYDataValidationError('Key property cevcevcindex is None')
                if self.cevcevcuniindex is None:
                    raise YPYDataValidationError('Key property cevcevcuniindex is None')

                return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcEvcUniTable/CISCO-EVC-MIB:cevcEvcUniEntry[CISCO-EVC-MIB:cevcEvcIndex = ' + str(self.cevcevcindex) + '][CISCO-EVC-MIB:cevcEvcUniIndex = ' + str(self.cevcevcuniindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cevcevcindex is not None:
                    return True

                if self.cevcevcuniindex is not None:
                    return True

                if self.cevcevclocaluniifindex is not None:
                    return True

                if self.cevcevcuniid is not None:
                    return True

                if self.cevcevcunioperstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                return meta._meta_table['CISCOEVCMIB.CevcEvcUniTable.CevcEvcUniEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcEvcUniTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cevcevcunientry is not None:
                for child_ref in self.cevcevcunientry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
            return meta._meta_table['CISCOEVCMIB.CevcEvcUniTable']['meta_info']


    class CevcMacSecurityViolation(object):
        """
        
        
        .. attribute:: cevcmacaddress
        
        	This object indicates the MAC Address which has violated the Mac security rules
        	**type**\: str
        
        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
        
        .. attribute:: cevcmaxmacconfiglimit
        
        	This object specifies the maximum MAC configuration limit. This is also sent as a part of MAC security violation notification. Every platform has their own forwarding table limitation. User  can also set the maximum MAC configuration limit and if the  limit set by user is not supported by platform then the object returns error
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cevcsiid
        
        	This object indicates the service instance ID for the MAC security violation notification
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: cevcviolationcause
        
        	This object indicates the MAC security violation cause.  When the system MAC Address limit is exceeded, the cevcMacSecurityViolationCause will contain 'exceedSystemLimit' value.  When the Bridge domain limit is exceeded, the cevcMacSecurityViolationCause will contain 'exceedBdLimit' value.  When the Service Instance limit is exceeded, the cevcMacSecurityViolationCause will contain 'exceedSILimit' value.  If the MAC address is present in the Black list then cevcMacSecurityViolationCause will contain 'blackListDeny' value
        	**type**\: :py:class:`CevcMacSecurityViolationCauseType_Enum <ydk.models.evc.CISCO_EVC_MIB.CevcMacSecurityViolationCauseType_Enum>`
        
        

        """

        _prefix = 'cisco-evc'
        _revision = '2012-05-21'

        def __init__(self):
            self.parent = None
            self.cevcmacaddress = None
            self.cevcmaxmacconfiglimit = None
            self.cevcsiid = None
            self.cevcviolationcause = None

        @property
        def _common_path(self):

            return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcMacSecurityViolation'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cevcmacaddress is not None:
                return True

            if self.cevcmaxmacconfiglimit is not None:
                return True

            if self.cevcsiid is not None:
                return True

            if self.cevcviolationcause is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
            return meta._meta_table['CISCOEVCMIB.CevcMacSecurityViolation']['meta_info']


    class CevcPortL2ControlProtocolTable(object):
        """
        This table lists the layer 2 control protocol processing
        attributes at UNI ports.  
        
        This table has an expansion dependent relationship on the 
        cevcUniTable, containing zero or more rows for each UNI.
        
        .. attribute:: cevcportl2controlprotocolentry
        
        	This entry represents the layer 2 control protocol processing at the UNI.  The system automatically creates an entry for each layer 2 control protocol type when an entry is created in the cevcUniTable, and entries are automatically destroyed when the system destroys the corresponding row in the cevcUniTable
        	**type**\: list of :py:class:`CevcPortL2ControlProtocolEntry <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcPortL2ControlProtocolTable.CevcPortL2ControlProtocolEntry>`
        
        

        """

        _prefix = 'cisco-evc'
        _revision = '2012-05-21'

        def __init__(self):
            self.parent = None
            self.cevcportl2controlprotocolentry = YList()
            self.cevcportl2controlprotocolentry.parent = self
            self.cevcportl2controlprotocolentry.name = 'cevcportl2controlprotocolentry'


        class CevcPortL2ControlProtocolEntry(object):
            """
            This entry represents the layer 2 control protocol processing
            at the UNI.
            
            The system automatically creates an entry for each layer 2
            control protocol type when an entry is created in the
            cevcUniTable, and entries are automatically destroyed when the
            system destroys the corresponding row in the cevcUniTable.
            
            .. attribute:: cevcportl2controlprotocoltype
            
            	This object indicates the type of layer 2 control protocol service frame as denoted by the value of  cevcPortL2ControlProtocolAction column
            	**type**\: :py:class:`CevcL2ControlProtocolType_Enum <ydk.models.evc.CISCO_EVC_MIB.CevcL2ControlProtocolType_Enum>`
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cevcportl2controlprotocolaction
            
            	This object specifies the action to be taken for the given layer 2 control protocol service frames which matches the  cevcPortL2ControlProtocolType, including\:       'discard'          The port must discard all ingress service frames         carrying the layer 2 control protocol service         frames and the port must not generate any egress         service frames carrying the layer 2 control protocol         service frames.  When this action is set at the port,         an EVC cannot process the layer 2 control protocol         service frames.       'peer'          The port must act as a peer, meaning it actively         participates with the Customer Equipment, in the         operation of the layer 2 control protocol service         frames.  An example of this is port authentication         service at the UNI with 802.1x or enhanced link OAM         functionality by peering at the UNI with link OAM         (IEEE 802.3ah).  When this action is set at the port,         an EVC cannot process the layer 2 control protocol         service frames.       'passToEvc'         The disposition of the service frames which are layer 2         control protocol service frames must be determined by         the layer 2 control protocol action attribute of the         EVC, (see cevcSIL2ControlProtocolAction for further         details).       'peerAndPassToEvc'          The layer 2 control protocol service frames will be         peered at the port and also passed to one or more EVCs         for tunneling.  An example of this possibility is where         an 802.1x authentication frame is peered at the UNI for         UNI\-based authentication, but also passed to a given         EVC for customer end\-to\-end authentication
            	**type**\: :py:class:`CevcPortL2ControlProtocolAction_Enum <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcPortL2ControlProtocolTable.CevcPortL2ControlProtocolEntry.CevcPortL2ControlProtocolAction_Enum>`
            
            

            """

            _prefix = 'cisco-evc'
            _revision = '2012-05-21'

            def __init__(self):
                self.parent = None
                self.cevcportl2controlprotocoltype = None
                self.ifindex = None
                self.cevcportl2controlprotocolaction = None

            class CevcPortL2ControlProtocolAction_Enum(Enum):
                """
                CevcPortL2ControlProtocolAction_Enum

                This object specifies the action to be taken for the given
                layer 2 control protocol service frames which matches the 
                cevcPortL2ControlProtocolType, including\:
                
                
                    'discard' 
                        The port must discard all ingress service frames
                        carrying the layer 2 control protocol service
                        frames and the port must not generate any egress
                        service frames carrying the layer 2 control protocol
                        service frames.  When this action is set at the port,
                        an EVC cannot process the layer 2 control protocol
                        service frames.
                
                
                    'peer' 
                        The port must act as a peer, meaning it actively
                        participates with the Customer Equipment, in the
                        operation of the layer 2 control protocol service
                        frames.  An example of this is port authentication
                        service at the UNI with 802.1x or enhanced link OAM
                        functionality by peering at the UNI with link OAM
                        (IEEE 802.3ah).  When this action is set at the port,
                        an EVC cannot process the layer 2 control protocol
                        service frames.
                
                
                    'passToEvc'
                        The disposition of the service frames which are layer 2
                        control protocol service frames must be determined by
                        the layer 2 control protocol action attribute of the
                        EVC, (see cevcSIL2ControlProtocolAction for further
                        details).
                
                
                    'peerAndPassToEvc' 
                        The layer 2 control protocol service frames will be
                        peered at the port and also passed to one or more EVCs
                        for tunneling.  An example of this possibility is where
                        an 802.1x authentication frame is peered at the UNI for
                        UNI\-based authentication, but also passed to a given
                        EVC for customer end\-to\-end authentication.

                """

                DISCARD = 1

                PEER = 2

                PASSTOEVC = 3

                PEERANDPASSTOEVC = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                    return meta._meta_table['CISCOEVCMIB.CevcPortL2ControlProtocolTable.CevcPortL2ControlProtocolEntry.CevcPortL2ControlProtocolAction_Enum']


            @property
            def _common_path(self):
                if self.cevcportl2controlprotocoltype is None:
                    raise YPYDataValidationError('Key property cevcportl2controlprotocoltype is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcPortL2ControlProtocolTable/CISCO-EVC-MIB:cevcPortL2ControlProtocolEntry[CISCO-EVC-MIB:cevcPortL2ControlProtocolType = ' + str(self.cevcportl2controlprotocoltype) + '][CISCO-EVC-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cevcportl2controlprotocoltype is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.cevcportl2controlprotocolaction is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                return meta._meta_table['CISCOEVCMIB.CevcPortL2ControlProtocolTable.CevcPortL2ControlProtocolEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcPortL2ControlProtocolTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cevcportl2controlprotocolentry is not None:
                for child_ref in self.cevcportl2controlprotocolentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
            return meta._meta_table['CISCOEVCMIB.CevcPortL2ControlProtocolTable']['meta_info']


    class CevcPortTable(object):
        """
        This table provides the operational mode and configuration
        limitations of the physical interfaces (ports) that provide
        Ethernet services for the MEN. 
        
        This table has a sparse depedent relationship on the ifTable, 
        containing a row for each ifEntry having an ifType of 
        'ethernetCsmacd' capable of supporting Ethernet services.
        
        .. attribute:: cevcportentry
        
        	This entry represents a port, a physical point, at which signals can enter or leave the network en route to or from another network to provide Ethernet services for the MEN.  The system automatically creates an entry for each ifEntry in the ifTable having an ifType of 'ethernetCsmacd' capable of supporting Ethernet services and entries are automatically destroyed when the corresponding row in the ifTable is destroyed
        	**type**\: list of :py:class:`CevcPortEntry <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcPortTable.CevcPortEntry>`
        
        

        """

        _prefix = 'cisco-evc'
        _revision = '2012-05-21'

        def __init__(self):
            self.parent = None
            self.cevcportentry = YList()
            self.cevcportentry.parent = self
            self.cevcportentry.name = 'cevcportentry'


        class CevcPortEntry(object):
            """
            This entry represents a port, a physical point, at which
            signals can enter or leave the network en route to or from
            another network to provide Ethernet services for the MEN.
            
            The system automatically creates an entry for each ifEntry in
            the ifTable having an ifType of 'ethernetCsmacd' capable of
            supporting Ethernet services and entries are automatically
            destroyed when the corresponding row in the ifTable is
            destroyed.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cevcportmaxnumevcs
            
            	This object indicates the maximum number of EVCs that the interface can support
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cevcportmaxnumserviceinstances
            
            	This object indicates the maximum number of service instances that the interface can support
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cevcportmode
            
            	Port denotes the physcial interface which can provide Ethernet services.  This object indicates the mode of the port and its operational behaviour in the MEN.       'uni'        User Network Interface        The port resides on the interface between the end user        and the network.  Additional information related        to the UNI is included in cevcUniTable.       'nni'         Network to Network Interface.  The port resides on the         interface between two networks
            	**type**\: :py:class:`CevcPortMode_Enum <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcPortTable.CevcPortEntry.CevcPortMode_Enum>`
            
            

            """

            _prefix = 'cisco-evc'
            _revision = '2012-05-21'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cevcportmaxnumevcs = None
                self.cevcportmaxnumserviceinstances = None
                self.cevcportmode = None

            class CevcPortMode_Enum(Enum):
                """
                CevcPortMode_Enum

                Port denotes the physcial interface which can provide
                Ethernet services.  This object indicates the mode of the
                port and its operational behaviour in the MEN. 
                
                
                   'uni'
                       User Network Interface
                       The port resides on the interface between the end user
                       and the network.  Additional information related
                       to the UNI is included in cevcUniTable.
                
                
                    'nni'
                        Network to Network Interface.  The port resides on the
                        interface between two networks.

                """

                UNI = 1

                NNI = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                    return meta._meta_table['CISCOEVCMIB.CevcPortTable.CevcPortEntry.CevcPortMode_Enum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcPortTable/CISCO-EVC-MIB:cevcPortEntry[CISCO-EVC-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.cevcportmaxnumevcs is not None:
                    return True

                if self.cevcportmaxnumserviceinstances is not None:
                    return True

                if self.cevcportmode is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                return meta._meta_table['CISCOEVCMIB.CevcPortTable.CevcPortEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcPortTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cevcportentry is not None:
                for child_ref in self.cevcportentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
            return meta._meta_table['CISCOEVCMIB.CevcPortTable']['meta_info']


    class CevcSICEVlanTable(object):
        """
        This table contains the CE\-VLAN map list for each Service
        Instance.
        
        This table has an expansion dependent relationship on the
        cevcSITable, containing a row for each CE\-VLAN or a range of
        CE\-VLANs that are mapped to a service instance.
        
        .. attribute:: cevcsicevlanentry
        
        	This entry contains the CE\-VLANs that are mapped at a Service Instance.  Entries in this table may be created and deleted via the cevcSICEVlanRowStatus object or the management console on the system.  Using SNMP, rows are created by a SET request setting the value of cevcSICEVlanRowStatus column to 'createAndGo' or 'createAndWait'.  Rows are deleted by a SET request setting the value of cevcSICEVlanRowStatus column to 'destroy'
        	**type**\: list of :py:class:`CevcSICEVlanEntry <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSICEVlanTable.CevcSICEVlanEntry>`
        
        

        """

        _prefix = 'cisco-evc'
        _revision = '2012-05-21'

        def __init__(self):
            self.parent = None
            self.cevcsicevlanentry = YList()
            self.cevcsicevlanentry.parent = self
            self.cevcsicevlanentry.name = 'cevcsicevlanentry'


        class CevcSICEVlanEntry(object):
            """
            This entry contains the CE\-VLANs that are mapped at a Service
            Instance.
            
            Entries in this table may be created and deleted via the
            cevcSICEVlanRowStatus object or the management console on the
            system.
            
            Using SNMP, rows are created by a SET request setting the value
            of cevcSICEVlanRowStatus column to 'createAndGo' or
            'createAndWait'.  Rows are deleted by a SET request setting the
            value of cevcSICEVlanRowStatus column to 'destroy'.
            
            .. attribute:: cevcsicevlanbeginningvlan
            
            	If cevcSICEVlanEndingVlan is '0', then this object indicates a single VLAN in the list.  If cevcSICEVlanEndingVlan is not '0', then this object indicates the first VLAN in a range of VLANs
            	**type**\: int
            
            	**range:** 1..4094
            
            .. attribute:: cevcsiindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cevcsicevlanendingvlan
            
            	This object indicates the last VLAN in a range of VLANs.  If the row does not describe a range, then the value of this column must be '0'
            	**type**\: int
            
            	**range:** 0..4094
            
            .. attribute:: cevcsicevlanrowstatus
            
            	This object enables a SNMP peer to create, modify, and delete rows in the cevcSICEVlanTable.  This object cannot be set to 'active' until all objects have  been assigned valid values.  Writable objects in this table can be modified while the value of the cevcSICEVlanRowStatus column is 'active'
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: cevcsicevlanstoragetype
            
            	This object specifies how the SNMP entity stores the data contained by the corresponding conceptual row.  This object can be set to either 'volatile' or 'nonVolatile'. Other values are not applicable for this conceptual row and are not supported
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'cisco-evc'
            _revision = '2012-05-21'

            def __init__(self):
                self.parent = None
                self.cevcsicevlanbeginningvlan = None
                self.cevcsiindex = None
                self.cevcsicevlanendingvlan = None
                self.cevcsicevlanrowstatus = None
                self.cevcsicevlanstoragetype = None

            @property
            def _common_path(self):
                if self.cevcsicevlanbeginningvlan is None:
                    raise YPYDataValidationError('Key property cevcsicevlanbeginningvlan is None')
                if self.cevcsiindex is None:
                    raise YPYDataValidationError('Key property cevcsiindex is None')

                return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcSICEVlanTable/CISCO-EVC-MIB:cevcSICEVlanEntry[CISCO-EVC-MIB:cevcSICEVlanBeginningVlan = ' + str(self.cevcsicevlanbeginningvlan) + '][CISCO-EVC-MIB:cevcSIIndex = ' + str(self.cevcsiindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cevcsicevlanbeginningvlan is not None:
                    return True

                if self.cevcsiindex is not None:
                    return True

                if self.cevcsicevlanendingvlan is not None:
                    return True

                if self.cevcsicevlanrowstatus is not None:
                    return True

                if self.cevcsicevlanstoragetype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                return meta._meta_table['CISCOEVCMIB.CevcSICEVlanTable.CevcSICEVlanEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcSICEVlanTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cevcsicevlanentry is not None:
                for child_ref in self.cevcsicevlanentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
            return meta._meta_table['CISCOEVCMIB.CevcSICEVlanTable']['meta_info']


    class CevcSIForwardBdTable(object):
        """
        This table contains the forwarding bridge domain information
        for each service instance.
        
        This table has a sparse dependent relationship on the 
        cevcSITable, containing a row for each service instance having 
        a cevcSIForwardingType of 'bridgeDomain'.
        
        .. attribute:: cevcsiforwardbdentry
        
        	This entry represents an bridged domain used to forward service frames by the service instance.  Entries in this table may be created and deleted via the cevcSIForwardBdRowStatus object or the management console on the system.  Using SNMP, rows are created by a SET request setting the value of the cevcSIForwardBdRowStatus column to 'createAndGo' or 'createAndWait'.  Rows are deleted by a SET request setting the value of the cevcSIForwardBdRowStatus column to 'destroy'
        	**type**\: list of :py:class:`CevcSIForwardBdEntry <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIForwardBdTable.CevcSIForwardBdEntry>`
        
        

        """

        _prefix = 'cisco-evc'
        _revision = '2012-05-21'

        def __init__(self):
            self.parent = None
            self.cevcsiforwardbdentry = YList()
            self.cevcsiforwardbdentry.parent = self
            self.cevcsiforwardbdentry.name = 'cevcsiforwardbdentry'


        class CevcSIForwardBdEntry(object):
            """
            This entry represents an bridged domain used to forward service
            frames by the service instance.
            
            Entries in this table may be created and deleted via the
            cevcSIForwardBdRowStatus object or the management console
            on the system.
            
            Using SNMP, rows are created by a SET request setting the value
            of the cevcSIForwardBdRowStatus column to 'createAndGo' or
            'createAndWait'.  Rows are deleted by a SET request setting the
            value of the cevcSIForwardBdRowStatus column to 'destroy'.
            
            .. attribute:: cevcsiindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cevcsiforwardbdnumber
            
            	The bridge domain identifier that is associated with the service instance.  A bridge domain refers to a layer 2 broadcast domain spanning a set of physical or virtual ports.  Frames are switched  Multicast and unknown destination unicast frames are flooded within the confines of the bridge domain
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cevcsiforwardbdnumber1kbitmap
            
            	This object specifies a string of octets containing one bit  per Bridge domain per service instance(generally we have one bridge domain per nontrunk service instance but can have more than one bridge configured with a trunk service instance). The first octet corresponds to Bridge domains with  Bridge domain ID values of 0 through 7; the second octet to Bridge domains 8 through 15; etc. Thus, this 128\-octet bitmap represents bridge domain ID value 0~1023.  For each Bridge domain configured, the bit corresponding to that bridge domain is set to '1'. SNMP Administrator uses cevcSIForwardBdNumberBase + (position of the set bit in  bitmap)to calculate BD number of a service instance.  Note that if the length of this string is less than 128 octets,  any 'missing' octets are assumed to contain the value zero. An  NMS may omit any zero\-valued octets from the end of this string  in order to reduce SetPDU size, and the agent may also omit  zero\-valued trailing octets, to reduce the size of GetResponse  PDUs
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: cevcsiforwardbdnumber2kbitmap
            
            	This object specifies a string of octets containing one bit  per Bridge domain per service instance(generally we have one bridge domain per nontrunk service instance but can have more than one bridge configured with a trunk service instance). The first octet corresponds to Bridge domains with  Bridge domain ID values of 1024 through 1031; the second  octet to Bridge domains 1032 through 1039; etc. Thus, this  128\-octet bitmap represents bridge domain ID value 1024~2047.  For each Bridge domain configured, the bit corresponding to that bridge domain is set to 1. SNMP Administrator uses cevcSIForwardBdNumberBase + (position of the set bit in  bitmap)to calculate BD number of a service instance.    Note that if the length of this string is less than 128 octets,  any 'missing' octets are assumed to contain the value zero. An  NMS may omit any zero\-valued octets from the end of this string  in order to reduce SetPDU size, and the agent may also omit  zero\-valued trailing octets, to reduce the size of GetResponse  PDUs
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: cevcsiforwardbdnumber3kbitmap
            
            	This object specifies a string of octets containing one bit per Bridge domain per service instance(generally we have one bridge domain per non\-trunk service instance but can have more than one bridge configured with a trunk service instance). The first octet corresponds to Bridge domains with Bridgedomain ID values of 2048 through 2055; the second octet to Bridge  domains 2056 through 2063; etc. Thus, this 128\-octet bitmap represents bridge domain ID value 2048~3071.  For each Bridge domain configured, the bit corresponding to that bridge domain is set to 1. SNMP Administrator uses cevcSIForwardBdNumberBase + (position of the set bit in  bitmap)to calculate BD number of a service instance.    Note that if the length of this string is less than 128 octets,  any 'missing' octets are assumed to contain the value zero. An  NMS may omit any zero\-valued octets from the end of this string  in order to reduce SetPDU size, and the agent may also omit  zero\-valued trailing octets, to reduce the size of GetResponse  PDUs
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: cevcsiforwardbdnumber4kbitmap
            
            	This object specifies a string of octets containing one bit  per Bridge domain per service instance(generally we have one bridge domain per non\-trunk service instance but can have more than one bridge configured with a trunk service instance). The first octet corresponds to Bridge domains with  Bridgedomain ID values of 3078 through 3085; the second octet  to Bridge domains 3086 through 3093; etc. Thus, this 128\-octet  bitmap represents bridge domain ID value 3072~4095.  For each Bridge domain configured, the bit corresponding to that bridge domain is set to 1. SNMP Administrator uses cevcSIForwardBdNumberBase + (position of the set bit in  bitmap)to calculate BD number of a service instance.    Note that if the length of this string is less than 128 octets,  any 'missing' octets are assumed to contain the value zero. An  NMS may omit any zero\-valued octets from the end of this string  in order to reduce SetPDU size, and the agent may also omit  zero\-valued trailing octets, to reduce the size of GetResponse  PDUs
            	**type**\: str
            
            	**range:** 0..128
            
            .. attribute:: cevcsiforwardbdnumberbase
            
            	This object specifies the base of bridge domain. The bridge domain range is 1~16k, cevcSIForwardBdNumberBase is to track what is the base of each 4k bitmap. In this way we can specify all the  16k bridge domains using four 1k bitmaps and having the base which describes that is the base of each 4k bitmap. The four 1k bitmaps, cevcSIForwardBdNumber1kBitmap represents 0~1023, cevcSIForwardBdNumber2kBitmap represents 1024~2047, cevcSIForwardBdNumber3kBitmap represents 2048~3071, cevcSIForwardBdNumber4kBitmap represents 3072~4095 And cevcSIForwardBdNumberBase is one of 0, 4096, 8192, 12288,  16384. SNMP Administrator can use cevcSIForwardBdNumberBase + (position  of the set bit in four 1k bitmaps) to get BD number of a  service instance
            	**type**\: :py:class:`CevcSIForwardBdNumberBase_Enum <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIForwardBdTable.CevcSIForwardBdEntry.CevcSIForwardBdNumberBase_Enum>`
            
            .. attribute:: cevcsiforwardbdrowstatus
            
            	This object enables a SNMP peer to create, modify, and delete rows in the cevcSIForwardBdTable.  This column can not be set to 'active' until all objects have  been assigned valid values.  Writable objects in this table can be modified while the value of the cevcSIForwardBdRowStatus column is 'active'
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: cevcsiforwardbdstoragetype
            
            	This object specifies how the SNMP entity stores the data contained by the corresponding conceptual row.  This object can be set to either 'volatile' or 'nonVolatile'. Other values are not applicable for this conceptual row and are not supported
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'cisco-evc'
            _revision = '2012-05-21'

            def __init__(self):
                self.parent = None
                self.cevcsiindex = None
                self.cevcsiforwardbdnumber = None
                self.cevcsiforwardbdnumber1kbitmap = None
                self.cevcsiforwardbdnumber2kbitmap = None
                self.cevcsiforwardbdnumber3kbitmap = None
                self.cevcsiforwardbdnumber4kbitmap = None
                self.cevcsiforwardbdnumberbase = None
                self.cevcsiforwardbdrowstatus = None
                self.cevcsiforwardbdstoragetype = None

            class CevcSIForwardBdNumberBase_Enum(Enum):
                """
                CevcSIForwardBdNumberBase_Enum

                This object specifies the base of bridge domain. The bridge
                domain range is 1~16k, cevcSIForwardBdNumberBase is to track what
                is the base of each 4k bitmap. In this way we can specify all the 
                16k bridge domains using four 1k bitmaps and having the base which
                describes that is the base of each 4k bitmap. The four 1k bitmaps,
                cevcSIForwardBdNumber1kBitmap represents 0~1023,
                cevcSIForwardBdNumber2kBitmap represents 1024~2047,
                cevcSIForwardBdNumber3kBitmap represents 2048~3071,
                cevcSIForwardBdNumber4kBitmap represents 3072~4095
                And cevcSIForwardBdNumberBase is one of 0, 4096, 8192, 12288, 
                16384.
                SNMP Administrator can use cevcSIForwardBdNumberBase + (position 
                of the set bit in four 1k bitmaps) to get BD number of a 
                service instance.

                """

                BDNUMBASE0 = 0

                BDNUMBASE4096 = 4096

                BDNUMBASE8192 = 8192

                BDNUMBASE12288 = 12288

                BDNUMBASE16384 = 16384


                @staticmethod
                def _meta_info():
                    from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                    return meta._meta_table['CISCOEVCMIB.CevcSIForwardBdTable.CevcSIForwardBdEntry.CevcSIForwardBdNumberBase_Enum']


            @property
            def _common_path(self):
                if self.cevcsiindex is None:
                    raise YPYDataValidationError('Key property cevcsiindex is None')

                return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcSIForwardBdTable/CISCO-EVC-MIB:cevcSIForwardBdEntry[CISCO-EVC-MIB:cevcSIIndex = ' + str(self.cevcsiindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cevcsiindex is not None:
                    return True

                if self.cevcsiforwardbdnumber is not None:
                    return True

                if self.cevcsiforwardbdnumber1kbitmap is not None:
                    return True

                if self.cevcsiforwardbdnumber2kbitmap is not None:
                    return True

                if self.cevcsiforwardbdnumber3kbitmap is not None:
                    return True

                if self.cevcsiforwardbdnumber4kbitmap is not None:
                    return True

                if self.cevcsiforwardbdnumberbase is not None:
                    return True

                if self.cevcsiforwardbdrowstatus is not None:
                    return True

                if self.cevcsiforwardbdstoragetype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                return meta._meta_table['CISCOEVCMIB.CevcSIForwardBdTable.CevcSIForwardBdEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcSIForwardBdTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cevcsiforwardbdentry is not None:
                for child_ref in self.cevcsiforwardbdentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
            return meta._meta_table['CISCOEVCMIB.CevcSIForwardBdTable']['meta_info']


    class CevcSIL2ControlProtocolTable(object):
        """
        This table lists the layer 2 control protocol processing
        attributes at service instances.  
        
        This table has an expansion dependent relationship on the 
        cevcSITable, containing a row for each layer 2 
        control protocol disposition at each service instance.
        
        .. attribute:: cevcsil2controlprotocolentry
        
        	This entry represents the layer 2 control protocol processing at a service instance.  The system automatically creates an entry for each layer 2 control protocol type when an entry is created in the cevcSITable, and entries are automatically destroyed when the system destroys the corresponding row in the cevcSITable
        	**type**\: list of :py:class:`CevcSIL2ControlProtocolEntry <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIL2ControlProtocolTable.CevcSIL2ControlProtocolEntry>`
        
        

        """

        _prefix = 'cisco-evc'
        _revision = '2012-05-21'

        def __init__(self):
            self.parent = None
            self.cevcsil2controlprotocolentry = YList()
            self.cevcsil2controlprotocolentry.parent = self
            self.cevcsil2controlprotocolentry.name = 'cevcsil2controlprotocolentry'


        class CevcSIL2ControlProtocolEntry(object):
            """
            This entry represents the layer 2 control protocol processing
            at a service instance.
            
            The system automatically creates an entry for each layer 2
            control protocol type when an entry is created in the
            cevcSITable, and entries are automatically destroyed when the
            system destroys the corresponding row in the cevcSITable.
            
            .. attribute:: cevcsiindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cevcsil2controlprotocoltype
            
            	The layer 2 control protocol service frame that the service instance is to process as defined by object cevcSIL2ControlProtocolAction
            	**type**\: :py:class:`CevcL2ControlProtocolType_Enum <ydk.models.evc.CISCO_EVC_MIB.CevcL2ControlProtocolType_Enum>`
            
            .. attribute:: cevcsil2controlprotocolaction
            
            	The actions to be taken for a given layer 2 control protocol service frames that matches cevcSIL2ControlProtocolType,  including\:       'discard'         The MEN must discard all ingress service frames          carrying the layer 2 control protocol service frames         on the EVC and the MEN must not generate any egress         service frames carrying the layer 2 control protocol         frames on the EVC.       'tunnel'         Forward the layer 2 control protocol service frames          with the MAC address changed as defined by the         individual layer 2 control protocol.  The EVC does not         process the layer 2 protocol service frames.  If a          layer 2 control protocol service frame is to be         tunneled, all the UNIs in the EVC must be configured to         pass the layer 2 control protocol service frames to the         EVC, cevcPortL2ControlProtocolAction column has the         value of 'passToEvc' or 'peerAndPassToEvc'.       'forward'         Forward the layer 2 conrol protocol service frames as         data; similar to tunnel but layer 2 control protocol         service frames are forwarded without changing the MAC         address
            	**type**\: :py:class:`CevcSIL2ControlProtocolAction_Enum <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIL2ControlProtocolTable.CevcSIL2ControlProtocolEntry.CevcSIL2ControlProtocolAction_Enum>`
            
            

            """

            _prefix = 'cisco-evc'
            _revision = '2012-05-21'

            def __init__(self):
                self.parent = None
                self.cevcsiindex = None
                self.cevcsil2controlprotocoltype = None
                self.cevcsil2controlprotocolaction = None

            class CevcSIL2ControlProtocolAction_Enum(Enum):
                """
                CevcSIL2ControlProtocolAction_Enum

                The actions to be taken for a given layer 2 control protocol
                service frames that matches cevcSIL2ControlProtocolType, 
                including\:
                
                
                    'discard'
                        The MEN must discard all ingress service frames 
                        carrying the layer 2 control protocol service frames
                        on the EVC and the MEN must not generate any egress
                        service frames carrying the layer 2 control protocol
                        frames on the EVC.
                
                
                    'tunnel'
                        Forward the layer 2 control protocol service frames 
                        with the MAC address changed as defined by the
                        individual layer 2 control protocol.  The EVC does not
                        process the layer 2 protocol service frames.  If a 
                        layer 2 control protocol service frame is to be
                        tunneled, all the UNIs in the EVC must be configured to
                        pass the layer 2 control protocol service frames to the
                        EVC, cevcPortL2ControlProtocolAction column has the
                        value of 'passToEvc' or 'peerAndPassToEvc'.
                
                
                    'forward'
                        Forward the layer 2 conrol protocol service frames as
                        data; similar to tunnel but layer 2 control protocol
                        service frames are forwarded without changing the MAC
                        address.

                """

                DISCARD = 1

                TUNNEL = 2

                FORWARD = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                    return meta._meta_table['CISCOEVCMIB.CevcSIL2ControlProtocolTable.CevcSIL2ControlProtocolEntry.CevcSIL2ControlProtocolAction_Enum']


            @property
            def _common_path(self):
                if self.cevcsiindex is None:
                    raise YPYDataValidationError('Key property cevcsiindex is None')
                if self.cevcsil2controlprotocoltype is None:
                    raise YPYDataValidationError('Key property cevcsil2controlprotocoltype is None')

                return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcSIL2ControlProtocolTable/CISCO-EVC-MIB:cevcSIL2ControlProtocolEntry[CISCO-EVC-MIB:cevcSIIndex = ' + str(self.cevcsiindex) + '][CISCO-EVC-MIB:cevcSIL2ControlProtocolType = ' + str(self.cevcsil2controlprotocoltype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cevcsiindex is not None:
                    return True

                if self.cevcsil2controlprotocoltype is not None:
                    return True

                if self.cevcsil2controlprotocolaction is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                return meta._meta_table['CISCOEVCMIB.CevcSIL2ControlProtocolTable.CevcSIL2ControlProtocolEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcSIL2ControlProtocolTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cevcsil2controlprotocolentry is not None:
                for child_ref in self.cevcsil2controlprotocolentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
            return meta._meta_table['CISCOEVCMIB.CevcSIL2ControlProtocolTable']['meta_info']


    class CevcSIMatchCriteriaTable(object):
        """
        This table contains the match criteria for each Service
        Instance.
        
        This table has an expansion dependent relationship on the
        cevcSITable, containing a row for each group of  match
        criteria of each service instance.
        
        .. attribute:: cevcsimatchcriteriaentry
        
        	This entry represents a group of match criteria for a service instance.  Each entry in the table with the same cevcSIIndex and different cevcSIMatchCriteriaIndex represents an OR operation of the match criteria for the service instance.  Entries in this table may be created and deleted via the cevcSIMatchRowStatus object or the management console on the system.  Using SNMP, rows are created by a SET request setting the value of cevcSIMatchRowStatus column to 'createAndGo' or 'createAndWait'.  Rows are deleted by a SET request setting the value of cevcSIMatchRowStatus column to 'destroy'
        	**type**\: list of :py:class:`CevcSIMatchCriteriaEntry <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIMatchCriteriaTable.CevcSIMatchCriteriaEntry>`
        
        

        """

        _prefix = 'cisco-evc'
        _revision = '2012-05-21'

        def __init__(self):
            self.parent = None
            self.cevcsimatchcriteriaentry = YList()
            self.cevcsimatchcriteriaentry.parent = self
            self.cevcsimatchcriteriaentry.name = 'cevcsimatchcriteriaentry'


        class CevcSIMatchCriteriaEntry(object):
            """
            This entry represents a group of match criteria for a service
            instance.  Each entry in the table with the same cevcSIIndex and
            different cevcSIMatchCriteriaIndex represents an OR operation of
            the match criteria for the service instance.
            
            Entries in this table may be created and deleted via the
            cevcSIMatchRowStatus object or the management console on the
            system.
            
            Using SNMP, rows are created by a SET request setting the value
            of cevcSIMatchRowStatus column to 'createAndGo' or
            'createAndWait'.  Rows are deleted by a SET request setting the
            value of cevcSIMatchRowStatus column to 'destroy'.
            
            .. attribute:: cevcsiindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cevcsimatchcriteriaindex
            
            	This object indicates an arbitrary integer\-value that uniquely identifies a match criteria for a service instance
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cevcsimatchcriteriatype
            
            	This object specifies the criteria used to match a service instance.      'unknown'         Match criteria for the service instance is not         defined or unknown.       'dot1q'         The IEEE 802.1q encapsulation is used as a match         criteria for the service instance.  The ether type         value of the IEEE 802.1q tag is specified by the         object cevcSIEncapEncapsulation with the same          index value of cevcSIIndex and         cevcSIMatchCreriaIndex.       'dot1ad'         The IEEE 802.1ad encapsulation is used as a match         criteria for the service instance.  The ether type         value of the IEEE 802.1ad tag is specified by the         cevcSIEncapEncapsulation column with the same index         value of cevcSIIndex and cevcSIMatchCreriaIndex.      'untagged'         Service instance processes untagged service frames.         Only one service instance on the interface/media         type can use untagged frames as a match criteria.       'untaggedAndDot1q'         Both untagged frames and the IEEE 802.1q encapsulation         are used as a match criteria for the service instance.         Only one service instance on the interface/media         type can use untagged frames as a match criteria.         The ether type value of the IEEE 802.1q tag is         specified by the cevcSIEncapEncapsulation column         with the same index value of cevcSIIndex and         cevcSIMatchCreriaIndex.      'untaggedAndDot1ad'         Both untagged frames and the IEEE 802.1ad encapsulation         are used as a match criteria for the service instance.         Only one service instance on the interface/media         type can use untagged frames as a match criteria.         The ether type value of the IEEE 802.1ad tag is         specified by the cevcSIEncapEncapsulation column         with the same index value of cevcSIIndex and         cevcSIMatchCreriaIndex.       'priorityTagged'         Service instance processes priority tagged frames.         Only one service instance on the interface/media         type can use priority tagged frames as a match          criteria.       'defaultTagged'         Service instance is a default service instance.  The         default service instance processes frames with VLANs         that do not match to any other service instances         configured on the interface/media type.  Only one         service instance on the interface/media type can be         the default service instance
            	**type**\: :py:class:`CevcSIMatchCriteriaType_Enum <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIMatchCriteriaTable.CevcSIMatchCriteriaEntry.CevcSIMatchCriteriaType_Enum>`
            
            .. attribute:: cevcsimatchrowstatus
            
            	This object enables a SNMP peer to create, modify, and delete rows in the cevcSIMatchCriteriaTable.  If the value of cevcSIMatchCriteriaType column is 'dot1q(1)' or 'dot1ad(2)' or 'untaggedAndDot1q' or 'untaggedAndDot1ad, then cevcSIMatchCriteriaRowStatus can not be set to 'active' until there exist an active row in the cevcSIMatchEncapTable with the same index value for cevcSIIndex and cevcSIMatchCriteriaIndex.  Writable objects in this table can be modified while the value of the cevcSIMatchRowStatus column is 'active'
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: cevcsimatchstoragetype
            
            	This object specifies how the SNMP entity stores the data contained by the corresponding conceptual row.  This object can be set to either 'volatile' or 'nonVolatile'. Other values are not applicable for this conceptual row and are not supported
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'cisco-evc'
            _revision = '2012-05-21'

            def __init__(self):
                self.parent = None
                self.cevcsiindex = None
                self.cevcsimatchcriteriaindex = None
                self.cevcsimatchcriteriatype = None
                self.cevcsimatchrowstatus = None
                self.cevcsimatchstoragetype = None

            class CevcSIMatchCriteriaType_Enum(Enum):
                """
                CevcSIMatchCriteriaType_Enum

                This object specifies the criteria used to match a service
                instance.
                
                    'unknown'
                        Match criteria for the service instance is not
                        defined or unknown.
                
                
                    'dot1q'
                        The IEEE 802.1q encapsulation is used as a match
                        criteria for the service instance.  The ether type
                        value of the IEEE 802.1q tag is specified by the
                        object cevcSIEncapEncapsulation with the same 
                        index value of cevcSIIndex and
                        cevcSIMatchCreriaIndex.
                
                
                    'dot1ad'
                        The IEEE 802.1ad encapsulation is used as a match
                        criteria for the service instance.  The ether type
                        value of the IEEE 802.1ad tag is specified by the
                        cevcSIEncapEncapsulation column with the same index
                        value of cevcSIIndex and cevcSIMatchCreriaIndex.
                
                    'untagged'
                        Service instance processes untagged service frames.
                        Only one service instance on the interface/media
                        type can use untagged frames as a match criteria.
                
                
                    'untaggedAndDot1q'
                        Both untagged frames and the IEEE 802.1q encapsulation
                        are used as a match criteria for the service instance.
                        Only one service instance on the interface/media
                        type can use untagged frames as a match criteria.
                        The ether type value of the IEEE 802.1q tag is
                        specified by the cevcSIEncapEncapsulation column
                        with the same index value of cevcSIIndex and
                        cevcSIMatchCreriaIndex.
                
                    'untaggedAndDot1ad'
                        Both untagged frames and the IEEE 802.1ad encapsulation
                        are used as a match criteria for the service instance.
                        Only one service instance on the interface/media
                        type can use untagged frames as a match criteria.
                        The ether type value of the IEEE 802.1ad tag is
                        specified by the cevcSIEncapEncapsulation column
                        with the same index value of cevcSIIndex and
                        cevcSIMatchCreriaIndex.
                
                
                    'priorityTagged'
                        Service instance processes priority tagged frames.
                        Only one service instance on the interface/media
                        type can use priority tagged frames as a match 
                        criteria.
                
                
                    'defaultTagged'
                        Service instance is a default service instance.  The
                        default service instance processes frames with VLANs
                        that do not match to any other service instances
                        configured on the interface/media type.  Only one
                        service instance on the interface/media type can be
                        the default service instance.

                """

                UNKNOWN = 1

                DOT1Q = 2

                DOT1AD = 3

                UNTAGGED = 4

                UNTAGGEDANDDOT1Q = 5

                UNTAGGEDANDDOT1AD = 6

                PRIORITYTAGGED = 7

                DEFAULTTAGGED = 8


                @staticmethod
                def _meta_info():
                    from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                    return meta._meta_table['CISCOEVCMIB.CevcSIMatchCriteriaTable.CevcSIMatchCriteriaEntry.CevcSIMatchCriteriaType_Enum']


            @property
            def _common_path(self):
                if self.cevcsiindex is None:
                    raise YPYDataValidationError('Key property cevcsiindex is None')
                if self.cevcsimatchcriteriaindex is None:
                    raise YPYDataValidationError('Key property cevcsimatchcriteriaindex is None')

                return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcSIMatchCriteriaTable/CISCO-EVC-MIB:cevcSIMatchCriteriaEntry[CISCO-EVC-MIB:cevcSIIndex = ' + str(self.cevcsiindex) + '][CISCO-EVC-MIB:cevcSIMatchCriteriaIndex = ' + str(self.cevcsimatchcriteriaindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cevcsiindex is not None:
                    return True

                if self.cevcsimatchcriteriaindex is not None:
                    return True

                if self.cevcsimatchcriteriatype is not None:
                    return True

                if self.cevcsimatchrowstatus is not None:
                    return True

                if self.cevcsimatchstoragetype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                return meta._meta_table['CISCOEVCMIB.CevcSIMatchCriteriaTable.CevcSIMatchCriteriaEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcSIMatchCriteriaTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cevcsimatchcriteriaentry is not None:
                for child_ref in self.cevcsimatchcriteriaentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
            return meta._meta_table['CISCOEVCMIB.CevcSIMatchCriteriaTable']['meta_info']


    class CevcSIMatchEncapTable(object):
        """
        This table contains the encapsulation based match criteria for
        each service instance.  
        
        This table has a sparse dependent relationship on the 
        cevcSIMatchCriteriaTable, containing a row for each match 
        criteria having one of the following values for 
        cevcSIMatchCriteriaType\:
        
            \- 'dot1q'
            \- 'dot1ad'
            \- 'untaggedAndDot1q'
            \- 'untaggedAndDot1ad'
            \- 'priorityTagged'
        
        .. attribute:: cevcsimatchencapentry
        
        	This entry represents a group of encapulation match criteria for a service instance.  Entries in this table may be created and deleted via the cevcSIMatchEncapRowStatus object or the management console on the system.  Using SNMP, rows are created by a SET request setting the value of cevcSIMatchEncapRowStatus column to 'createAndGo' or 'createAndWait'.  Rows are deleted by a SET request setting the value of cevcSIMatchEncapRowStatus column to 'destroy'
        	**type**\: list of :py:class:`CevcSIMatchEncapEntry <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIMatchEncapTable.CevcSIMatchEncapEntry>`
        
        

        """

        _prefix = 'cisco-evc'
        _revision = '2012-05-21'

        def __init__(self):
            self.parent = None
            self.cevcsimatchencapentry = YList()
            self.cevcsimatchencapentry.parent = self
            self.cevcsimatchencapentry.name = 'cevcsimatchencapentry'


        class CevcSIMatchEncapEntry(object):
            """
            This entry represents a group of encapulation match criteria
            for a service instance.
            
            Entries in this table may be created and deleted via the
            cevcSIMatchEncapRowStatus object or the management console
            on the system.
            
            Using SNMP, rows are created by a SET request setting the value
            of cevcSIMatchEncapRowStatus column to 'createAndGo' or
            'createAndWait'.  Rows are deleted by a SET request setting the
            value of cevcSIMatchEncapRowStatus column to 'destroy'.
            
            .. attribute:: cevcsiindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cevcsimatchcriteriaindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cevcsimatchencapencapsulation
            
            	This object specifies the encapsulation type used as service match criteria.  The object also specifies the Ethertype for egress packets on the service instance.       'dot1qEthertype0x8100'         The IEEE 801.1q encapsulation with ether type value         0x8100.       'dot1qEthertype0x9100'         The IEEE 801.1q encapsulation with ether type value         0x9100.       'dot1qEthertype0x9200'         The IEEE 801.1q encapsulation with ether type value         0x9200.       'dot1qEthertype0x88A8'          The IEEE 801.1q encapsulation with ether type value          0x88A8.       'dot1adEthertype0x88A8'         The IEEE 801.1ad encapsulation with ether type value         0x88A8.       'dot1ahEthertype0x88A8'         The IEEE 801.1ah encapsulation with ether type value         0x88A8
            	**type**\: :py:class:`CevcSIMatchEncapEncapsulation_Enum <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIMatchEncapTable.CevcSIMatchEncapEntry.CevcSIMatchEncapEncapsulation_Enum>`
            
            .. attribute:: cevcsimatchencappayloadtype
            
            	This object specifies the PayloadType(etype/protocol type) values that the service instance uses as a service match criteria.  This object is required when the forwarding of layer\-2 ethernet packet is done through the payloadType i.e IP etc.       'other'         None of the following.       'payloadType0x0800ip'         Payload type value for IP is 0x0800.   This object is valid only when 'payloadType' bit is set to '1' in corresponding instance of the object  cevcSIMatchEncapValid.  This object is deprecated by cevcSIMatchEncapPayloadTypes
            	**type**\: :py:class:`CevcSIMatchEncapPayloadType_Enum <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIMatchEncapTable.CevcSIMatchEncapEntry.CevcSIMatchEncapPayloadType_Enum>`
            
            .. attribute:: cevcsimatchencappayloadtypes
            
            	This object specifies the etype/protocol type values that service instance uses as a service match criteria.  This object is required when the forwarding of layer\-2 ethernet packet is done through the payload ether type i.e IP etc.       'payloadTypeIPv4'         Ethernet payload type value for IPv4 protocol.       'payloadTypeIPv6'         Ethernet payload type value for IPv6 protocol.       'payloadTypePPPoEDiscovery'         Ethernet payload type value for PPPoE discovery         stage.       'payloadTypePPPoESession'         Ethernet payload type value for PPPoE session         stage.       'payloadTypePPPoEAll'         All ethernet payload type values for PPPoE protocol.  This object is valid only when 'payloadTypes' bit is set to '1' in corresponding instance of the object cevcSIMatchEncapValid.  This object deprecates cevcSIMatchEncapPayloadType
            	**type**\: :py:class:`CevcSIMatchEncapPayloadTypes_Bits <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIMatchEncapTable.CevcSIMatchEncapEntry.CevcSIMatchEncapPayloadTypes_Bits>`
            
            .. attribute:: cevcsimatchencapprimarycos
            
            	This object specifies the CoS values which the Service Instance uses as service match criteria.  This object is valid only when 'primaryVlans' and 'primaryCos' bits are set to '1' in corresponding instance of the object cevcSIMatchEncapValid
            	**type**\: :py:class:`CiscoCosList_Bits <ydk.models.tc.CISCO_TC.CiscoCosList_Bits>`
            
            .. attribute:: cevcsimatchencapprioritycos
            
            	This object specifies the priority CoS values which the service instance uses as service match criteria.  This  object is valid only when 'priorityCos' bit is set to '1' in corresponding instance of the object cevcSIMatchEncapValid
            	**type**\: :py:class:`CiscoCosList_Bits <ydk.models.tc.CISCO_TC.CiscoCosList_Bits>`
            
            .. attribute:: cevcsimatchencaprowstatus
            
            	This object enables a SNMP peer to create, modify, and delete rows in the cevcSIMatchEncapTable.  This object cannot be set to 'active' until cevcSIEncapEncapsulation and objects referred by  cevcSIMatchEncapValid have been assigned their respective valid values.  Writable objects in this table can be modified while the value of the cevcSIEncapMatchRowStatus column is 'active'
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: cevcsimatchencapsecondarycos
            
            	This object specifies the CoS values which the Service Instance uses as service match criteria.  This object is valid only when 'secondaryVlans' and 'secondaryCos' bits are set to '1' in corresponding instance of the object cevcSIMatchEncapValid
            	**type**\: :py:class:`CiscoCosList_Bits <ydk.models.tc.CISCO_TC.CiscoCosList_Bits>`
            
            .. attribute:: cevcsimatchencapstoragetype
            
            	This object specifies how the SNMP entity stores the data contained by the corresponding conceptual row.  This object can be set to either 'volatile' or 'nonVolatile'. Other values are not applicable for this conceptual row and are not supported
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: cevcsimatchencapvalid
            
            	This object specifies the encapsulation criteria used to match a service instance.       'primaryCos'         The 'primaryCos' bit set to '1' specifies the         Class of Service is used as service match criteria for         the service instance.  When this bit is set to '1'         there must exist aleast one active rows in the         cevcSIPrimaryVlanTable which has the same index values         of cevcSIIndex and cevcSIMatchCriteriaIndex.  When         'primaryCos' bit is '1', the cevcSIPrimaryCos column         indicates the CoS value(s).      'secondaryCos'         The 'secondaryCos' bit set to '1' specifies the         Class of Service is used as service match criteria for         the service instance.  When this bit is set to '1'         there must exist aleast one active rows in the         cevcSISecondaryVlanTable which has the same index         values of cevcSIIndex and cevcSIMatchCriteriaIndex.         When 'secondaryCos' bit is '1', the         cevcSISecondaryCos column indicates the CoS          value(s).       'payloadType'         This bit set to '1' specifies that the value of         corresponding instance of cevcSIMatchEncapPayloadType         is used as service match criteria for the service         instance.       'payloadTypes'         This bit set to '1' specifies that the value of         corresponding instance of cevcSIMatchEncapPayloadTypes         is used as service match criteria for the service         instance.       'priorityCos'         This bit set to '1' specifies that the value of         corresponding instance of cevcSIMatchEncapPriorityCos         is used as service match criteria for the service         instance.       'dot1qNativeVlan'         This bit set to '1' specifies that the IEEE 802.1q         tag with native vlan is used as service match          criteria for the service instance.       'dot1adNativeVlan'         This bit set to '1' specifies that the IEEE 802.1ad         tag with native vlan is used as service match          criteria for the service instance.       'encapExact'         This bit set to '1' specifies that a service frame is         mapped to the service instance only if it matches         exactly to the encapsulation specified by the service         instance
            	**type**\: :py:class:`CevcSIMatchEncapValid_Bits <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIMatchEncapTable.CevcSIMatchEncapEntry.CevcSIMatchEncapValid_Bits>`
            
            

            """

            _prefix = 'cisco-evc'
            _revision = '2012-05-21'

            def __init__(self):
                self.parent = None
                self.cevcsiindex = None
                self.cevcsimatchcriteriaindex = None
                self.cevcsimatchencapencapsulation = None
                self.cevcsimatchencappayloadtype = None
                self.cevcsimatchencappayloadtypes = CISCOEVCMIB.CevcSIMatchEncapTable.CevcSIMatchEncapEntry.CevcSIMatchEncapPayloadTypes_Bits()
                self.cevcsimatchencapprimarycos = CiscoCosList_Bits()
                self.cevcsimatchencapprioritycos = CiscoCosList_Bits()
                self.cevcsimatchencaprowstatus = None
                self.cevcsimatchencapsecondarycos = CiscoCosList_Bits()
                self.cevcsimatchencapstoragetype = None
                self.cevcsimatchencapvalid = CISCOEVCMIB.CevcSIMatchEncapTable.CevcSIMatchEncapEntry.CevcSIMatchEncapValid_Bits()

            class CevcSIMatchEncapEncapsulation_Enum(Enum):
                """
                CevcSIMatchEncapEncapsulation_Enum

                This object specifies the encapsulation type used as service
                match criteria.  The object also specifies the Ethertype for
                egress packets on the service instance.
                
                
                    'dot1qEthertype0x8100'
                        The IEEE 801.1q encapsulation with ether type value
                        0x8100.
                
                
                    'dot1qEthertype0x9100'
                        The IEEE 801.1q encapsulation with ether type value
                        0x9100.
                
                
                    'dot1qEthertype0x9200'
                        The IEEE 801.1q encapsulation with ether type value
                        0x9200.
                
                
                    'dot1qEthertype0x88A8'
                         The IEEE 801.1q encapsulation with ether type value
                         0x88A8.
                
                
                    'dot1adEthertype0x88A8'
                        The IEEE 801.1ad encapsulation with ether type value
                        0x88A8.
                
                
                    'dot1ahEthertype0x88A8'
                        The IEEE 801.1ah encapsulation with ether type value
                        0x88A8.

                """

                DOT1QETHERTYPE0X8100 = 1

                DOT1QETHERTYPE0X9100 = 2

                DOT1QETHERTYPE0X9200 = 3

                DOT1QETHERTYPE0X88A8 = 4

                DOT1ADETHERTYPE0X88A8 = 5

                DOT1AHETHERTYPE0X88A8 = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                    return meta._meta_table['CISCOEVCMIB.CevcSIMatchEncapTable.CevcSIMatchEncapEntry.CevcSIMatchEncapEncapsulation_Enum']


            class CevcSIMatchEncapPayloadType_Enum(Enum):
                """
                CevcSIMatchEncapPayloadType_Enum

                This object specifies the PayloadType(etype/protocol type)
                values that the service instance uses as a service match
                criteria.  This object is required when the forwarding of
                layer\-2 ethernet packet is done through the payloadType i.e IP
                etc.
                
                
                    'other'
                        None of the following.
                
                
                    'payloadType0x0800ip'
                        Payload type value for IP is 0x0800.
                
                
                This object is valid only when 'payloadType' bit is set to '1'
                in corresponding instance of the object 
                cevcSIMatchEncapValid.
                
                This object is deprecated by cevcSIMatchEncapPayloadTypes.

                """

                OTHER = 1

                PAYLOADTYPE0X0800IP = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                    return meta._meta_table['CISCOEVCMIB.CevcSIMatchEncapTable.CevcSIMatchEncapEntry.CevcSIMatchEncapPayloadType_Enum']


            class CevcSIMatchEncapPayloadTypes_Bits(FixedBitsDict):
                """
                CevcSIMatchEncapPayloadTypes_Bits

                This object specifies the etype/protocol type values that
                service instance uses as a service match criteria.  This
                object is required when the forwarding of layer\-2 ethernet
                packet is done through the payload ether type i.e IP etc.
                
                
                    'payloadTypeIPv4'
                        Ethernet payload type value for IPv4 protocol.
                
                
                    'payloadTypeIPv6'
                        Ethernet payload type value for IPv6 protocol.
                
                
                    'payloadTypePPPoEDiscovery'
                        Ethernet payload type value for PPPoE discovery
                        stage.
                
                
                    'payloadTypePPPoESession'
                        Ethernet payload type value for PPPoE session
                        stage.
                
                
                    'payloadTypePPPoEAll'
                        All ethernet payload type values for PPPoE protocol.
                
                This object is valid only when 'payloadTypes' bit is set to
                '1' in corresponding instance of the object
                cevcSIMatchEncapValid.
                
                This object deprecates cevcSIMatchEncapPayloadType.
                Keys are:- payloadTypeIPv4 , payloadTypePPPoEDiscovery , payloadTypeIPv6 , payloadTypePPPoEAll , payloadTypePPPoESession

                """

                def __init__(self):
                    self._dictionary = { 
                        'payloadTypeIPv4':False,
                        'payloadTypePPPoEDiscovery':False,
                        'payloadTypeIPv6':False,
                        'payloadTypePPPoEAll':False,
                        'payloadTypePPPoESession':False,
                    }
                    self._pos_map = { 
                        'payloadTypeIPv4':0,
                        'payloadTypePPPoEDiscovery':2,
                        'payloadTypeIPv6':1,
                        'payloadTypePPPoEAll':4,
                        'payloadTypePPPoESession':3,
                    }

            class CevcSIMatchEncapValid_Bits(FixedBitsDict):
                """
                CevcSIMatchEncapValid_Bits

                This object specifies the encapsulation criteria used to match
                a service instance.
                
                
                    'primaryCos'
                        The 'primaryCos' bit set to '1' specifies the
                        Class of Service is used as service match criteria for
                        the service instance.  When this bit is set to '1'
                        there must exist aleast one active rows in the
                        cevcSIPrimaryVlanTable which has the same index values
                        of cevcSIIndex and cevcSIMatchCriteriaIndex.  When
                        'primaryCos' bit is '1', the cevcSIPrimaryCos column
                        indicates the CoS value(s).
                
                    'secondaryCos'
                        The 'secondaryCos' bit set to '1' specifies the
                        Class of Service is used as service match criteria for
                        the service instance.  When this bit is set to '1'
                        there must exist aleast one active rows in the
                        cevcSISecondaryVlanTable which has the same index
                        values of cevcSIIndex and cevcSIMatchCriteriaIndex.
                        When 'secondaryCos' bit is '1', the
                        cevcSISecondaryCos column indicates the CoS 
                        value(s).
                
                
                    'payloadType'
                        This bit set to '1' specifies that the value of
                        corresponding instance of cevcSIMatchEncapPayloadType
                        is used as service match criteria for the service
                        instance.
                
                
                    'payloadTypes'
                        This bit set to '1' specifies that the value of
                        corresponding instance of cevcSIMatchEncapPayloadTypes
                        is used as service match criteria for the service
                        instance.
                
                
                    'priorityCos'
                        This bit set to '1' specifies that the value of
                        corresponding instance of cevcSIMatchEncapPriorityCos
                        is used as service match criteria for the service
                        instance.
                
                
                    'dot1qNativeVlan'
                        This bit set to '1' specifies that the IEEE 802.1q
                        tag with native vlan is used as service match 
                        criteria for the service instance.
                
                
                    'dot1adNativeVlan'
                        This bit set to '1' specifies that the IEEE 802.1ad
                        tag with native vlan is used as service match 
                        criteria for the service instance.
                
                
                    'encapExact'
                        This bit set to '1' specifies that a service frame is
                        mapped to the service instance only if it matches
                        exactly to the encapsulation specified by the service
                        instance.
                Keys are:- dot1adNativeVlan , payloadType , primaryCos , payloadTypes , priorityCos , dot1qNativeVlan , encapExact , secondaryCos

                """

                def __init__(self):
                    self._dictionary = { 
                        'dot1adNativeVlan':False,
                        'payloadType':False,
                        'primaryCos':False,
                        'payloadTypes':False,
                        'priorityCos':False,
                        'dot1qNativeVlan':False,
                        'encapExact':False,
                        'secondaryCos':False,
                    }
                    self._pos_map = { 
                        'dot1adNativeVlan':6,
                        'payloadType':2,
                        'primaryCos':0,
                        'payloadTypes':3,
                        'priorityCos':4,
                        'dot1qNativeVlan':5,
                        'encapExact':7,
                        'secondaryCos':1,
                    }

            @property
            def _common_path(self):
                if self.cevcsiindex is None:
                    raise YPYDataValidationError('Key property cevcsiindex is None')
                if self.cevcsimatchcriteriaindex is None:
                    raise YPYDataValidationError('Key property cevcsimatchcriteriaindex is None')

                return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcSIMatchEncapTable/CISCO-EVC-MIB:cevcSIMatchEncapEntry[CISCO-EVC-MIB:cevcSIIndex = ' + str(self.cevcsiindex) + '][CISCO-EVC-MIB:cevcSIMatchCriteriaIndex = ' + str(self.cevcsimatchcriteriaindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cevcsiindex is not None:
                    return True

                if self.cevcsimatchcriteriaindex is not None:
                    return True

                if self.cevcsimatchencapencapsulation is not None:
                    return True

                if self.cevcsimatchencappayloadtype is not None:
                    return True

                if self.cevcsimatchencappayloadtypes is not None:
                    if self.cevcsimatchencappayloadtypes._has_data():
                        return True

                if self.cevcsimatchencapprimarycos is not None:
                    if self.cevcsimatchencapprimarycos._has_data():
                        return True

                if self.cevcsimatchencapprioritycos is not None:
                    if self.cevcsimatchencapprioritycos._has_data():
                        return True

                if self.cevcsimatchencaprowstatus is not None:
                    return True

                if self.cevcsimatchencapsecondarycos is not None:
                    if self.cevcsimatchencapsecondarycos._has_data():
                        return True

                if self.cevcsimatchencapstoragetype is not None:
                    return True

                if self.cevcsimatchencapvalid is not None:
                    if self.cevcsimatchencapvalid._has_data():
                        return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                return meta._meta_table['CISCOEVCMIB.CevcSIMatchEncapTable.CevcSIMatchEncapEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcSIMatchEncapTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cevcsimatchencapentry is not None:
                for child_ref in self.cevcsimatchencapentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
            return meta._meta_table['CISCOEVCMIB.CevcSIMatchEncapTable']['meta_info']


    class CevcSIPrimaryVlanTable(object):
        """
        This table contains the primary VLAN ID list for each Service
        Instance.
        
        This table has an expansion dependent relationship on the 
        cevcSIMatchEncapTable, containing zero or more rows for each 
        encapsulation match criteria.
        
        .. attribute:: cevcsiprimaryvlanentry
        
        	This entry specifies a single VLAN or a range of VLANs contained in the primary VLAN list that's part of the  encapsulation match criteria.  Entries in this table may be created and deleted via the cevcSIPrimaryVlanRowStatus object or the management console on the system.  Using SNMP, rows are created by a SET request setting the value of the cevcSIPrimaryVlanRowStatus column to 'createAndGo' or 'createAndWait'.  Rows are deleted by a SET request setting the value of the cevcSIPrimaryVlanRowStatus column to 'destroy'
        	**type**\: list of :py:class:`CevcSIPrimaryVlanEntry <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIPrimaryVlanTable.CevcSIPrimaryVlanEntry>`
        
        

        """

        _prefix = 'cisco-evc'
        _revision = '2012-05-21'

        def __init__(self):
            self.parent = None
            self.cevcsiprimaryvlanentry = YList()
            self.cevcsiprimaryvlanentry.parent = self
            self.cevcsiprimaryvlanentry.name = 'cevcsiprimaryvlanentry'


        class CevcSIPrimaryVlanEntry(object):
            """
            This entry specifies a single VLAN or a range of VLANs
            contained in the primary VLAN list that's part of the 
            encapsulation match criteria.
            
            Entries in this table may be created and deleted via the
            cevcSIPrimaryVlanRowStatus object or the management console
            on the system.
            
            Using SNMP, rows are created by a SET request setting the value
            of the cevcSIPrimaryVlanRowStatus column to 'createAndGo' or
            'createAndWait'.  Rows are deleted by a SET request setting the
            value of the cevcSIPrimaryVlanRowStatus column to 'destroy'.
            
            .. attribute:: cevcsiindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cevcsimatchcriteriaindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cevcsiprimaryvlanbeginningvlan
            
            	If cevcSIPrimaryVlanEndingVlan is '0', then this object indicates a single VLAN in the list.  If cevcSIPrimaryVlanEndingVlan is not '0', then this object indicates the first VLAN in a range of VLANs
            	**type**\: int
            
            	**range:** 1..4094
            
            .. attribute:: cevcsiprimaryvlanendingvlan
            
            	This object indicates the last VLAN in a range of VLANs.  If the row does not describe a range, then the value of this column must be '0'
            	**type**\: int
            
            	**range:** 0..4094
            
            .. attribute:: cevcsiprimaryvlanrowstatus
            
            	This object enables a SNMP peer to create, modify, and delete rows in the cevcSIPrimaryVlanTable.  This column cannot be set to 'active' until all objects have  been assigned valid values.  Writable objects in this table can be modified while the value of the cevcSIPrimaryVlanRowStatus column is 'active'
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: cevcsiprimaryvlanstoragetype
            
            	This object specifies how the SNMP entity stores the data contained by the corresponding conceptual row.  This object can be set to either 'volatile' or 'nonVolatile'. Other values are not applicable for this conceptual row and are not supported
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'cisco-evc'
            _revision = '2012-05-21'

            def __init__(self):
                self.parent = None
                self.cevcsiindex = None
                self.cevcsimatchcriteriaindex = None
                self.cevcsiprimaryvlanbeginningvlan = None
                self.cevcsiprimaryvlanendingvlan = None
                self.cevcsiprimaryvlanrowstatus = None
                self.cevcsiprimaryvlanstoragetype = None

            @property
            def _common_path(self):
                if self.cevcsiindex is None:
                    raise YPYDataValidationError('Key property cevcsiindex is None')
                if self.cevcsimatchcriteriaindex is None:
                    raise YPYDataValidationError('Key property cevcsimatchcriteriaindex is None')
                if self.cevcsiprimaryvlanbeginningvlan is None:
                    raise YPYDataValidationError('Key property cevcsiprimaryvlanbeginningvlan is None')

                return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcSIPrimaryVlanTable/CISCO-EVC-MIB:cevcSIPrimaryVlanEntry[CISCO-EVC-MIB:cevcSIIndex = ' + str(self.cevcsiindex) + '][CISCO-EVC-MIB:cevcSIMatchCriteriaIndex = ' + str(self.cevcsimatchcriteriaindex) + '][CISCO-EVC-MIB:cevcSIPrimaryVlanBeginningVlan = ' + str(self.cevcsiprimaryvlanbeginningvlan) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cevcsiindex is not None:
                    return True

                if self.cevcsimatchcriteriaindex is not None:
                    return True

                if self.cevcsiprimaryvlanbeginningvlan is not None:
                    return True

                if self.cevcsiprimaryvlanendingvlan is not None:
                    return True

                if self.cevcsiprimaryvlanrowstatus is not None:
                    return True

                if self.cevcsiprimaryvlanstoragetype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                return meta._meta_table['CISCOEVCMIB.CevcSIPrimaryVlanTable.CevcSIPrimaryVlanEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcSIPrimaryVlanTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cevcsiprimaryvlanentry is not None:
                for child_ref in self.cevcsiprimaryvlanentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
            return meta._meta_table['CISCOEVCMIB.CevcSIPrimaryVlanTable']['meta_info']


    class CevcSISecondaryVlanTable(object):
        """
        This table contains the seconadary VLAN ID list for each
        service instance.
        
        This table has an expansion dependent relationship on the 
        cevcSIMatchEncapTable, containing zero or more rows for each 
        encapsulation match criteria.
        
        .. attribute:: cevcsisecondaryvlanentry
        
        	This entry specifies a single VLAN or a range of VLANs contained in the secondary VLAN list that's part of the  encapsulation match criteria.  Entries in this table may be created and deleted via the cevcSISecondaryVlanRowStatus object or the management console on the system.  Using SNMP, rows are created by a SET request setting the value of the cevcSISecondaryVlanRowStatus column to 'createAndGo' or 'createAndWait'.  Rows are deleted by a SET request setting the value of the cevcSISecondaryVlanRowStatus column to 'destroy'
        	**type**\: list of :py:class:`CevcSISecondaryVlanEntry <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSISecondaryVlanTable.CevcSISecondaryVlanEntry>`
        
        

        """

        _prefix = 'cisco-evc'
        _revision = '2012-05-21'

        def __init__(self):
            self.parent = None
            self.cevcsisecondaryvlanentry = YList()
            self.cevcsisecondaryvlanentry.parent = self
            self.cevcsisecondaryvlanentry.name = 'cevcsisecondaryvlanentry'


        class CevcSISecondaryVlanEntry(object):
            """
            This entry specifies a single VLAN or a range of VLANs
            contained in the secondary VLAN list that's part of the 
            encapsulation match criteria.
            
            Entries in this table may be created and deleted via the
            cevcSISecondaryVlanRowStatus object or the management console
            on the system.
            
            Using SNMP, rows are created by a SET request setting the value
            of the cevcSISecondaryVlanRowStatus column to 'createAndGo' or
            'createAndWait'.  Rows are deleted by a SET request setting the
            value of the cevcSISecondaryVlanRowStatus column to 'destroy'.
            
            .. attribute:: cevcsiindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cevcsimatchcriteriaindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cevcsisecondaryvlanbeginningvlan
            
            	If cevcSISecondaryVlanEndingVlan is '0', then this object indicates a single VLAN in the list.  If cevcSISecondaryVlanEndingVlan is not '0', then this object indicates the first VLAN in a range of VLANs
            	**type**\: int
            
            	**range:** 1..4094
            
            .. attribute:: cevcsisecondaryvlanendingvlan
            
            	This object indicates the last VLAN in a range of VLANs.  If the row does not describe a range, then the value of this column must be '0'
            	**type**\: int
            
            	**range:** 0..4094
            
            .. attribute:: cevcsisecondaryvlanrowstatus
            
            	This object enables a SNMP peer to create, modify, and delete rows in the cevcSISecondaryVlanTable.  This column can not be set to 'active' until all objects have  been assigned valid values.  Writable objects in this table can be modified while the value of cevcSISecondaryVlanRowStatus column is 'active'
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: cevcsisecondaryvlanstoragetype
            
            	This object specifies how the SNMP entity stores the data contained by the corresponding conceptual row.  This object can be set to either 'volatile' or 'nonVolatile'. Other values are not applicable for this conceptual row and are not supported
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'cisco-evc'
            _revision = '2012-05-21'

            def __init__(self):
                self.parent = None
                self.cevcsiindex = None
                self.cevcsimatchcriteriaindex = None
                self.cevcsisecondaryvlanbeginningvlan = None
                self.cevcsisecondaryvlanendingvlan = None
                self.cevcsisecondaryvlanrowstatus = None
                self.cevcsisecondaryvlanstoragetype = None

            @property
            def _common_path(self):
                if self.cevcsiindex is None:
                    raise YPYDataValidationError('Key property cevcsiindex is None')
                if self.cevcsimatchcriteriaindex is None:
                    raise YPYDataValidationError('Key property cevcsimatchcriteriaindex is None')
                if self.cevcsisecondaryvlanbeginningvlan is None:
                    raise YPYDataValidationError('Key property cevcsisecondaryvlanbeginningvlan is None')

                return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcSISecondaryVlanTable/CISCO-EVC-MIB:cevcSISecondaryVlanEntry[CISCO-EVC-MIB:cevcSIIndex = ' + str(self.cevcsiindex) + '][CISCO-EVC-MIB:cevcSIMatchCriteriaIndex = ' + str(self.cevcsimatchcriteriaindex) + '][CISCO-EVC-MIB:cevcSISecondaryVlanBeginningVlan = ' + str(self.cevcsisecondaryvlanbeginningvlan) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cevcsiindex is not None:
                    return True

                if self.cevcsimatchcriteriaindex is not None:
                    return True

                if self.cevcsisecondaryvlanbeginningvlan is not None:
                    return True

                if self.cevcsisecondaryvlanendingvlan is not None:
                    return True

                if self.cevcsisecondaryvlanrowstatus is not None:
                    return True

                if self.cevcsisecondaryvlanstoragetype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                return meta._meta_table['CISCOEVCMIB.CevcSISecondaryVlanTable.CevcSISecondaryVlanEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcSISecondaryVlanTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cevcsisecondaryvlanentry is not None:
                for child_ref in self.cevcsisecondaryvlanentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
            return meta._meta_table['CISCOEVCMIB.CevcSISecondaryVlanTable']['meta_info']


    class CevcSIStateTable(object):
        """
        This table lists statical status data of the service instance.
        
        This table has an one\-to\-one dependent relationship on the
        cevcSITable, containing a row for each service instance.
        
        .. attribute:: cevcsistateentry
        
        	This entry represents operational status of a service instance.  The system automatically creates an entry when the system or the EMS NMS creates a row in the cevcSITable.  Likewise, the system automatically destroys an entry when the system or the EMS NMS destroys the corresponding row in the cevcSITable
        	**type**\: list of :py:class:`CevcSIStateEntry <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIStateTable.CevcSIStateEntry>`
        
        

        """

        _prefix = 'cisco-evc'
        _revision = '2012-05-21'

        def __init__(self):
            self.parent = None
            self.cevcsistateentry = YList()
            self.cevcsistateentry.parent = self
            self.cevcsistateentry.name = 'cevcsistateentry'


        class CevcSIStateEntry(object):
            """
            This entry represents operational status of a service instance.
            
            The system automatically creates an entry when the system or
            the EMS NMS creates a row in the cevcSITable.  Likewise, the
            system automatically destroys an entry when the system or the
            EMS NMS destroys the corresponding row in the cevcSITable.
            
            .. attribute:: cevcsiindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cevcsioperstatus
            
            	This object indicates the operational status of the Service Instance.       'up'          Service instance is fully operational and able to         transfer traffic.       'down'         Service instance is down and not capable of         transferring traffic, and is not administratively         configured to be down by management system.        'adminDown'         Service instance has been explicitly configured to         administratively down by a management system and is not         capable of transferring traffic.       'deleted'         Service instance has been deleted.       'errorDisabled'         Service instance has been shut down due to MAC          security violations.        'unknown'         Operational status of service instance is unknown or         undefined
            	**type**\: :py:class:`CevcSIOperStatus_Enum <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIStateTable.CevcSIStateEntry.CevcSIOperStatus_Enum>`
            
            

            """

            _prefix = 'cisco-evc'
            _revision = '2012-05-21'

            def __init__(self):
                self.parent = None
                self.cevcsiindex = None
                self.cevcsioperstatus = None

            class CevcSIOperStatus_Enum(Enum):
                """
                CevcSIOperStatus_Enum

                This object indicates the operational status of the Service
                Instance.
                
                
                    'up' 
                        Service instance is fully operational and able to
                        transfer traffic.
                
                
                    'down'
                        Service instance is down and not capable of
                        transferring traffic, and is not administratively
                        configured to be down by management system. 
                
                
                    'adminDown'
                        Service instance has been explicitly configured to
                        administratively down by a management system and is not
                        capable of transferring traffic.
                
                
                    'deleted'
                        Service instance has been deleted.
                
                
                    'errorDisabled'
                        Service instance has been shut down due to MAC 
                        security violations. 
                
                
                    'unknown'
                        Operational status of service instance is unknown or
                        undefined.

                """

                UP = 1

                DOWN = 2

                ADMINDOWN = 3

                DELETED = 4

                ERRORDISABLED = 5

                UNKNOWN = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                    return meta._meta_table['CISCOEVCMIB.CevcSIStateTable.CevcSIStateEntry.CevcSIOperStatus_Enum']


            @property
            def _common_path(self):
                if self.cevcsiindex is None:
                    raise YPYDataValidationError('Key property cevcsiindex is None')

                return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcSIStateTable/CISCO-EVC-MIB:cevcSIStateEntry[CISCO-EVC-MIB:cevcSIIndex = ' + str(self.cevcsiindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cevcsiindex is not None:
                    return True

                if self.cevcsioperstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                return meta._meta_table['CISCOEVCMIB.CevcSIStateTable.CevcSIStateEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcSIStateTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cevcsistateentry is not None:
                for child_ref in self.cevcsistateentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
            return meta._meta_table['CISCOEVCMIB.CevcSIStateTable']['meta_info']


    class CevcSITable(object):
        """
        This table lists each service instance and its service
        attributes.
        
        .. attribute:: cevcsientry
        
        	This entry represents a service instance configured on the system and its service attributes.  Entries in this table may be created and deleted via the cevcSIRowStatus object or the management console on the system.  Using SNMP, rows are created by a SET request setting the value of cevcSIRowStatus column to 'createAndGo'or 'createAndWait'.  Rows are deleted by a SET request setting the value of cevcSIRowStatus column to 'destroy'
        	**type**\: list of :py:class:`CevcSIEntry <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSITable.CevcSIEntry>`
        
        

        """

        _prefix = 'cisco-evc'
        _revision = '2012-05-21'

        def __init__(self):
            self.parent = None
            self.cevcsientry = YList()
            self.cevcsientry.parent = self
            self.cevcsientry.name = 'cevcsientry'


        class CevcSIEntry(object):
            """
            This entry represents a service instance configured on the
            system and its service attributes.
            
            Entries in this table may be created and deleted via the
            cevcSIRowStatus object or the management console on the
            system.
            
            Using SNMP, rows are created by a SET request setting the value
            of cevcSIRowStatus column to 'createAndGo'or 'createAndWait'. 
            Rows are deleted by a SET request setting the value of
            cevcSIRowStatus column to 'destroy'.
            
            .. attribute:: cevcsiindex
            
            	This object indicates an arbitrary integer\-value that uniquely identifies a service instance.  An implementation MAY assign an ifIndex\-value assigned to the service instance to cevcSIIndex
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cevcsiadminstatus
            
            	This object specifies the desired state of the Service Instance.         'up'         Ready to transfer traffic.  When a system initializes,         all service instances start with this state.         'down'         The service instance is administratively down and is         not capable of transferring traffic
            	**type**\: :py:class:`CevcSIAdminStatus_Enum <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSITable.CevcSIEntry.CevcSIAdminStatus_Enum>`
            
            .. attribute:: cevcsicreationtype
            
            	This object specifies whether the service instance created is statically configured by the user or is dynamically created.        'static'           If the service instance is configured manually this             object is set to static(1).        'dynamic'           If the service instance is created dynamically            by the first sign of life of an Ethernet frame,             then this object is set to dynamic(2) for              the service instance
            	**type**\: :py:class:`CevcSICreationType_Enum <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSITable.CevcSIEntry.CevcSICreationType_Enum>`
            
            .. attribute:: cevcsievcindex
            
            	This object specifies the EVC Index that the service instance is associated.  The value of '0' this column indicates that the service instance is not associated to an EVC.  If the value of cevcSIEvcIndex column is not '0', there must exist an active row in the cevcEvcTable with the same index value for cevcEvcIndex
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cevcsiforwardingtype
            
            	This object indicates technique used by a service instance to forward service frames.      'other'         If the forwarding behavior of a service instance is         not defined or unknown, this object is set to other(0).       'bridgeDomain'         Bridge domain is used to forward service frames by a         service instance.  If cevcSIForwardingType is          'bridgeDomain(1)', there must exist an active         row in the cevcSIForwardBdTable with the same         index value of cevcSIIndex.  The object         cevcSIForwardBdNumber indicates the identifier of         the bridge domain component being used
            	**type**\: :py:class:`CevcSIForwardingType_Enum <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSITable.CevcSIEntry.CevcSIForwardingType_Enum>`
            
            .. attribute:: cevcsiname
            
            	The textual name of the service instance.  The value of this column should be the name of the component as assigned by the local interface/media type and should be be suitable for use in commands entered at the device's 'console'.  This might be text name, such as 'si1' or a simple service instance number,  such as '1', depending on the interface naming syntax of the device.  If there is no local name or this object is otherwise not applicable, then this object contains a zero\-length string
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cevcsirowstatus
            
            	This object enables a SNMP peer to create, modify, and delete rows in the cevcSITable.  This object cannot be set to 'active' until following corresponding objects are assigned to valid values\:     \- cevcSITargetType    \- cevcSITarget    \- cevcSIName    \- cevcSIType  Following writable objects in this table cannot be modified while the value of cevcSIRowStatus is 'active'\:     \- cevcSITargetType    \- cevcSITarget    \- cevcSIName    \- cevcSIType  Objects in this table and all other tables that have the same cevcSIIndex value as an index disappear when cevcSIRowStatus is set to 'destroy'
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: cevcsistoragetype
            
            	This object specifies how the SNMP entity stores the data contained by the corresponding conceptual row.  This object can be set to either 'volatile' or 'nonVolatile'. Other values are not applicable for this conceptual row and are not supported
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: cevcsitarget
            
            	This object indicates the target to which a service instance has an attachment.  If the target is unknown, the value of the cevcSITarget column is a zero\-length string
            	**type**\: str
            
            	**range:** 0..40
            
            .. attribute:: cevcsitargettype
            
            	This object indicates the type of interface/media to which a service instance has an attachment
            	**type**\: :py:class:`ServiceInstanceTargetType_Enum <ydk.models.evc.CISCO_EVC_MIB.ServiceInstanceTargetType_Enum>`
            
            .. attribute:: cevcsitype
            
            	This object specifies the type of the service instance. It mentions if the service instance is either a regular or trunk or l2context service instance.          'regular'               If a service instance is configured without                 any type specified, then it is a regular service                instance.                         'trunk'               If the service instance is configured               with trunk type, then it is a trunk service               instance. For a trunk service instance,               its Bridge domain IDs are derived from                encapsulation VLAN plus an optional offset                (refer cevcSIForwardBdNumberBase object).                          'l2context'               If the service instance is configured                with dynamic type, then it is a L2 context                service instance. The Ethernet L2 Context               is a statically configured service instance               which contains the Ethernet Initiator               for attracting the first sign of life. In other               words, Ethernet L2 Context service instance is               used for catching the first sign of life of                Ethernet frames to create dynamic Ethernet                sessions service instances
            	**type**\: :py:class:`CevcSIType_Enum <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSITable.CevcSIEntry.CevcSIType_Enum>`
            
            

            """

            _prefix = 'cisco-evc'
            _revision = '2012-05-21'

            def __init__(self):
                self.parent = None
                self.cevcsiindex = None
                self.cevcsiadminstatus = None
                self.cevcsicreationtype = None
                self.cevcsievcindex = None
                self.cevcsiforwardingtype = None
                self.cevcsiname = None
                self.cevcsirowstatus = None
                self.cevcsistoragetype = None
                self.cevcsitarget = None
                self.cevcsitargettype = None
                self.cevcsitype = None

            class CevcSIAdminStatus_Enum(Enum):
                """
                CevcSIAdminStatus_Enum

                This object specifies the desired state of the Service
                Instance.  
                
                
                    'up'
                        Ready to transfer traffic.  When a system initializes,
                        all service instances start with this state.  
                
                
                    'down'
                        The service instance is administratively down and is
                        not capable of transferring traffic.

                """

                UP = 1

                DOWN = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                    return meta._meta_table['CISCOEVCMIB.CevcSITable.CevcSIEntry.CevcSIAdminStatus_Enum']


            class CevcSICreationType_Enum(Enum):
                """
                CevcSICreationType_Enum

                This object specifies whether the service instance created
                is statically configured by the user or is dynamically created.
                
                      'static'
                          If the service instance is configured manually this  
                          object is set to static(1).
                
                      'dynamic'
                          If the service instance is created dynamically
                           by the first sign of life of an Ethernet frame,
                            then this object is set to dynamic(2) for 
                            the service instance.

                """

                STATIC = 1

                DYNAMIC = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                    return meta._meta_table['CISCOEVCMIB.CevcSITable.CevcSIEntry.CevcSICreationType_Enum']


            class CevcSIForwardingType_Enum(Enum):
                """
                CevcSIForwardingType_Enum

                This object indicates technique used by a service instance to
                forward service frames.
                
                    'other'
                        If the forwarding behavior of a service instance is
                        not defined or unknown, this object is set to other(0).
                
                
                    'bridgeDomain'
                        Bridge domain is used to forward service frames by a
                        service instance.  If cevcSIForwardingType is 
                        'bridgeDomain(1)', there must exist an active
                        row in the cevcSIForwardBdTable with the same
                        index value of cevcSIIndex.  The object
                        cevcSIForwardBdNumber indicates the identifier of
                        the bridge domain component being used.

                """

                OTHER = 0

                BRIDGEDOMAIN = 1


                @staticmethod
                def _meta_info():
                    from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                    return meta._meta_table['CISCOEVCMIB.CevcSITable.CevcSIEntry.CevcSIForwardingType_Enum']


            class CevcSIType_Enum(Enum):
                """
                CevcSIType_Enum

                This object specifies the type of the service instance. It
                mentions if the service instance is either a regular or trunk
                or l2context service instance.
                
                        'regular'
                              If a service instance is configured without  
                              any type specified, then it is a regular service 
                              instance.
                              
                
                        'trunk'
                              If the service instance is configured
                              with trunk type, then it is a trunk service
                              instance. For a trunk service instance,
                              its Bridge domain IDs are derived from 
                              encapsulation VLAN plus an optional offset
                               (refer cevcSIForwardBdNumberBase object).
                             
                
                          'l2context'
                              If the service instance is configured 
                              with dynamic type, then it is a L2 context 
                              service instance. The Ethernet L2 Context
                              is a statically configured service instance
                              which contains the Ethernet Initiator
                              for attracting the first sign of life. In other
                              words, Ethernet L2 Context service instance is
                              used for catching the first sign of life of 
                              Ethernet frames to create dynamic Ethernet 
                              sessions service instances.

                """

                REGULAR = 1

                TRUNK = 2

                L2CONTEXT = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                    return meta._meta_table['CISCOEVCMIB.CevcSITable.CevcSIEntry.CevcSIType_Enum']


            @property
            def _common_path(self):
                if self.cevcsiindex is None:
                    raise YPYDataValidationError('Key property cevcsiindex is None')

                return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcSITable/CISCO-EVC-MIB:cevcSIEntry[CISCO-EVC-MIB:cevcSIIndex = ' + str(self.cevcsiindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cevcsiindex is not None:
                    return True

                if self.cevcsiadminstatus is not None:
                    return True

                if self.cevcsicreationtype is not None:
                    return True

                if self.cevcsievcindex is not None:
                    return True

                if self.cevcsiforwardingtype is not None:
                    return True

                if self.cevcsiname is not None:
                    return True

                if self.cevcsirowstatus is not None:
                    return True

                if self.cevcsistoragetype is not None:
                    return True

                if self.cevcsitarget is not None:
                    return True

                if self.cevcsitargettype is not None:
                    return True

                if self.cevcsitype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                return meta._meta_table['CISCOEVCMIB.CevcSITable.CevcSIEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcSITable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cevcsientry is not None:
                for child_ref in self.cevcsientry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
            return meta._meta_table['CISCOEVCMIB.CevcSITable']['meta_info']


    class CevcSIVlanRewriteTable(object):
        """
        This table lists the rewrite adjustments of the service
        frame's VLAN tags for service instances.
        
        This table has an expansion dependent relationship on the
        cevcSITable, containing a row for a VLAN adjustment
        for ingress and egress frames at each service instance.
        
        .. attribute:: cevcsivlanrewriteentry
        
        	Each entry represents the VLAN adjustment for a Service Instance
        	**type**\: list of :py:class:`CevcSIVlanRewriteEntry <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIVlanRewriteTable.CevcSIVlanRewriteEntry>`
        
        

        """

        _prefix = 'cisco-evc'
        _revision = '2012-05-21'

        def __init__(self):
            self.parent = None
            self.cevcsivlanrewriteentry = YList()
            self.cevcsivlanrewriteentry.parent = self
            self.cevcsivlanrewriteentry.name = 'cevcsivlanrewriteentry'


        class CevcSIVlanRewriteEntry(object):
            """
            Each entry represents the VLAN adjustment for a Service
            Instance.
            
            .. attribute:: cevcsiindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cevcsivlanrewritedirection
            
            	This object specifies the VLAN adjustment for 'ingress' frames or 'egress' frames on the service instance
            	**type**\: :py:class:`CevcSIVlanRewriteDirection_Enum <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIVlanRewriteTable.CevcSIVlanRewriteEntry.CevcSIVlanRewriteDirection_Enum>`
            
            .. attribute:: cevcsivlanrewriteaction
            
            	This object specifies the rewrite action the device performs for the service instance, including\:      'push1'         Add cevcSIVlanRewriteVlan1 as the VLAN tag to the         service frame.       'push2'         Add cevcSIVlanRewriteVlan1 as the outer VLAN tag          and cevcSIVlanRewriteVlan2 as the inner VLAN tag of         the service frame.       'pop1'         Remove the outermost VLAN tag from the service frame.       'pop2'         Remove the two outermost VLAN tags from the service         frame.       'translate1To1'         Replace the outermost VLAN tag with the          cevcSIVlanRewriteVlan1 tag.      'translate1To2'        Replace the outermost VLAN tag with        cevcSIVlanRewriteVlan1 and add cevcSIVlanRewriteVlan2        to the second VLAN tag of the service frame.       'translate2To1'         Remove the outermost VLAN tag and replace the second         VLAN tag with cevcSIVlanVlanRewriteVlan1.      'translate2To2'        Replace the outermost VLAN tag with        cevcSIVlanRewriteVlan1 and the second VLAN tag with        cevcSIVlanRewriteVlan2
            	**type**\: :py:class:`CevcSIVlanRewriteAction_Enum <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIVlanRewriteTable.CevcSIVlanRewriteEntry.CevcSIVlanRewriteAction_Enum>`
            
            .. attribute:: cevcsivlanrewriteencapsulation
            
            	This object specifies the encapsulation type to process for the service instance.       'dot1q'         The IEEE 802.1q encapsulation.       'dot1ad'         The IEEE 802.1ad encapsulation
            	**type**\: :py:class:`CevcSIVlanRewriteEncapsulation_Enum <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcSIVlanRewriteTable.CevcSIVlanRewriteEntry.CevcSIVlanRewriteEncapsulation_Enum>`
            
            .. attribute:: cevcsivlanrewriterowstatus
            
            	This object enables a SNMP peer to create, modify, and delete rows in the cevcSIVlanRewriteTable.  cevcSIVlanRewriteAction and cevcSIVlanRewriteEncapsulation must have valid values before this object can be set to 'active'.  Writable objects in this table can be modified while the value of cevcSIVlanRewriteRowStatus column is 'active'
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: cevcsivlanrewritestoragetype
            
            	This object specifies how the SNMP entity stores the data contained by the corresponding conceptual row.  This object can be set to either 'volatile' or 'nonVolatile'. Other values are not applicable for this conceptual row and are not supported
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: cevcsivlanrewritesymmetric
            
            	This object is valid only when cevcSIVlanRewriteDirection is 'ingress'.  The value 'true' of this column specifies that egress packets are tagged with a VLAN specified by an active row in cevcSIPrimaryVlanTable.  There could only be one VLAN value assigned in the  cevcSIPrimaryVlanTable, i.e. only one 'active' entry that has the same index value of cevcSIIndex column and corresponding instance of cevcSIPrimaryVlanEndingVlan column has value '0'
            	**type**\: bool
            
            .. attribute:: cevcsivlanrewritevlan1
            
            	This object specifies the outermost VLAN ID tag of the frame for the service instance.  This object is valid  only when cevcSIVlanRewriteAction is 'push1', 'push2', 'translate1To1', 'translate1To2', 'translate2To1', or  'translate2To2'
            	**type**\: int
            
            	**range:** 1..4094
            
            .. attribute:: cevcsivlanrewritevlan2
            
            	This object specifies the second VLAN ID tag of the frame for the service instance.  This object is valid  only when cevcSIVlanRewriteAction is 'push2', 'translate1To2', or 'translate2To2'
            	**type**\: int
            
            	**range:** 1..4094
            
            

            """

            _prefix = 'cisco-evc'
            _revision = '2012-05-21'

            def __init__(self):
                self.parent = None
                self.cevcsiindex = None
                self.cevcsivlanrewritedirection = None
                self.cevcsivlanrewriteaction = None
                self.cevcsivlanrewriteencapsulation = None
                self.cevcsivlanrewriterowstatus = None
                self.cevcsivlanrewritestoragetype = None
                self.cevcsivlanrewritesymmetric = None
                self.cevcsivlanrewritevlan1 = None
                self.cevcsivlanrewritevlan2 = None

            class CevcSIVlanRewriteAction_Enum(Enum):
                """
                CevcSIVlanRewriteAction_Enum

                This object specifies the rewrite action the device performs
                for the service instance, including\:
                
                    'push1'
                        Add cevcSIVlanRewriteVlan1 as the VLAN tag to the
                        service frame.
                
                
                    'push2'
                        Add cevcSIVlanRewriteVlan1 as the outer VLAN tag 
                        and cevcSIVlanRewriteVlan2 as the inner VLAN tag of
                        the service frame.
                
                
                    'pop1'
                        Remove the outermost VLAN tag from the service frame.
                
                
                    'pop2'
                        Remove the two outermost VLAN tags from the service
                        frame.
                
                
                    'translate1To1'
                        Replace the outermost VLAN tag with the 
                        cevcSIVlanRewriteVlan1 tag.
                
                
                   'translate1To2'
                       Replace the outermost VLAN tag with
                       cevcSIVlanRewriteVlan1 and add cevcSIVlanRewriteVlan2
                       to the second VLAN tag of the service frame.
                
                
                    'translate2To1'
                        Remove the outermost VLAN tag and replace the second
                        VLAN tag with cevcSIVlanVlanRewriteVlan1.
                
                
                   'translate2To2'
                       Replace the outermost VLAN tag with
                       cevcSIVlanRewriteVlan1 and the second VLAN tag with
                       cevcSIVlanRewriteVlan2.

                """

                PUSH1 = 1

                PUSH2 = 2

                POP1 = 3

                POP2 = 4

                TRANSLATE1TO1 = 5

                TRANSLATE1TO2 = 6

                TRANSLATE2TO1 = 7

                TRANSLATE2TO2 = 8


                @staticmethod
                def _meta_info():
                    from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                    return meta._meta_table['CISCOEVCMIB.CevcSIVlanRewriteTable.CevcSIVlanRewriteEntry.CevcSIVlanRewriteAction_Enum']


            class CevcSIVlanRewriteDirection_Enum(Enum):
                """
                CevcSIVlanRewriteDirection_Enum

                This object specifies the VLAN adjustment for 'ingress'
                frames or 'egress' frames on the service instance.

                """

                INGRESS = 1

                EGRESS = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                    return meta._meta_table['CISCOEVCMIB.CevcSIVlanRewriteTable.CevcSIVlanRewriteEntry.CevcSIVlanRewriteDirection_Enum']


            class CevcSIVlanRewriteEncapsulation_Enum(Enum):
                """
                CevcSIVlanRewriteEncapsulation_Enum

                This object specifies the encapsulation type to
                process for the service instance.
                
                
                    'dot1q'
                        The IEEE 802.1q encapsulation.
                
                
                    'dot1ad'
                        The IEEE 802.1ad encapsulation.

                """

                DOT1Q = 1

                DOT1AD = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                    return meta._meta_table['CISCOEVCMIB.CevcSIVlanRewriteTable.CevcSIVlanRewriteEntry.CevcSIVlanRewriteEncapsulation_Enum']


            @property
            def _common_path(self):
                if self.cevcsiindex is None:
                    raise YPYDataValidationError('Key property cevcsiindex is None')
                if self.cevcsivlanrewritedirection is None:
                    raise YPYDataValidationError('Key property cevcsivlanrewritedirection is None')

                return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcSIVlanRewriteTable/CISCO-EVC-MIB:cevcSIVlanRewriteEntry[CISCO-EVC-MIB:cevcSIIndex = ' + str(self.cevcsiindex) + '][CISCO-EVC-MIB:cevcSIVlanRewriteDirection = ' + str(self.cevcsivlanrewritedirection) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cevcsiindex is not None:
                    return True

                if self.cevcsivlanrewritedirection is not None:
                    return True

                if self.cevcsivlanrewriteaction is not None:
                    return True

                if self.cevcsivlanrewriteencapsulation is not None:
                    return True

                if self.cevcsivlanrewriterowstatus is not None:
                    return True

                if self.cevcsivlanrewritestoragetype is not None:
                    return True

                if self.cevcsivlanrewritesymmetric is not None:
                    return True

                if self.cevcsivlanrewritevlan1 is not None:
                    return True

                if self.cevcsivlanrewritevlan2 is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                return meta._meta_table['CISCOEVCMIB.CevcSIVlanRewriteTable.CevcSIVlanRewriteEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcSIVlanRewriteTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cevcsivlanrewriteentry is not None:
                for child_ref in self.cevcsivlanrewriteentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
            return meta._meta_table['CISCOEVCMIB.CevcSIVlanRewriteTable']['meta_info']


    class CevcSystem(object):
        """
        
        
        .. attribute:: cevcmaxnumevcs
        
        	This object indicates the maximum number of EVCs that the system supports
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cevcnumcfgevcs
        
        	This object indicates the actual number of EVCs currently configured on the system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-evc'
        _revision = '2012-05-21'

        def __init__(self):
            self.parent = None
            self.cevcmaxnumevcs = None
            self.cevcnumcfgevcs = None

        @property
        def _common_path(self):

            return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcSystem'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cevcmaxnumevcs is not None:
                return True

            if self.cevcnumcfgevcs is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
            return meta._meta_table['CISCOEVCMIB.CevcSystem']['meta_info']


    class CevcUniCEVlanEvcTable(object):
        """
        This table contains for each UNI, a list of EVCs and the
        association of CE\-VLANs to the EVC.  The CE\-VLAN mapping is 
        locally significant to the UNI.
        
        This table has an expansion dependent relationship on the 
        cevcUniTable, containing zero or more rows for each UNI.
        
        .. attribute:: cevcunicevlanevcentry
        
        	This entry represents an EVC and the CE\-VLANs that are mapped to it at an UNI.  For example, if CE\-VLANs 10, 20\-30, 40 are mapped to an EVC indicated by  cevcUniEvcIndex = 1, at an UNI with ifIndex = 2, this table will contain following rows to represent above CE\-VLAN map\:    cevcUniCEVlanEvcEndingVlan.2.1.10 = 0   cevcUniCEVlanEvcEndingVlan.2.1.20 = 30   cevcUniCEVlanEvcEndingVlan.2.1.40 = 0  The system automatically creates an entry when the system creates an entry in the cevcUniTable and an entry is created in cevcSICEVlanTable for a service instance which is attached to an EVC on this UNI.  Likewise, the system automatically destroys an entry when the system or the EMS/NMS destroys the corresponding row in the cevcUniTable or in the cevcSICEVlanTable
        	**type**\: list of :py:class:`CevcUniCEVlanEvcEntry <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcUniCEVlanEvcTable.CevcUniCEVlanEvcEntry>`
        
        

        """

        _prefix = 'cisco-evc'
        _revision = '2012-05-21'

        def __init__(self):
            self.parent = None
            self.cevcunicevlanevcentry = YList()
            self.cevcunicevlanevcentry.parent = self
            self.cevcunicevlanevcentry.name = 'cevcunicevlanevcentry'


        class CevcUniCEVlanEvcEntry(object):
            """
            This entry represents an EVC and the CE\-VLANs that are mapped
            to it at an UNI.
            
            For example, if CE\-VLANs 10, 20\-30, 40 are mapped to an EVC
            indicated by  cevcUniEvcIndex = 1, at an UNI with ifIndex = 2,
            this table will contain following rows to represent above
            CE\-VLAN map\:
            
              cevcUniCEVlanEvcEndingVlan.2.1.10 = 0
              cevcUniCEVlanEvcEndingVlan.2.1.20 = 30
              cevcUniCEVlanEvcEndingVlan.2.1.40 = 0
            
            The system automatically creates an entry when the system
            creates an entry in the cevcUniTable and an entry is created in
            cevcSICEVlanTable for a service instance which is attached to
            an EVC on this UNI.  Likewise, the system automatically destroys
            an entry when the system or the EMS/NMS destroys the
            corresponding row in the cevcUniTable or in the
            cevcSICEVlanTable.
            
            .. attribute:: cevcunicevlanevcbeginningvlan
            
            	If cevcUniCEVlanEvcEndingVlan is '0', then this object indicates a single VLAN in the list.  If cevcUniCEVlanEvcEndingVlan is not '0', then this object indicates the first VLAN in a range of VLANs
            	**type**\: int
            
            	**range:** 1..4094
            
            .. attribute:: cevcunievcindex
            
            	This object indicates an arbitrary integer\-value that uniquely identifies the EVC attached at an UNI
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cevcunicevlanevcendingvlan
            
            	This object indicates the last VLAN in a range of VLANs.  If the row does not describe a range, then the value of this column must be '0'
            	**type**\: int
            
            	**range:** 0..4094
            
            

            """

            _prefix = 'cisco-evc'
            _revision = '2012-05-21'

            def __init__(self):
                self.parent = None
                self.cevcunicevlanevcbeginningvlan = None
                self.cevcunievcindex = None
                self.ifindex = None
                self.cevcunicevlanevcendingvlan = None

            @property
            def _common_path(self):
                if self.cevcunicevlanevcbeginningvlan is None:
                    raise YPYDataValidationError('Key property cevcunicevlanevcbeginningvlan is None')
                if self.cevcunievcindex is None:
                    raise YPYDataValidationError('Key property cevcunievcindex is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcUniCEVlanEvcTable/CISCO-EVC-MIB:cevcUniCEVlanEvcEntry[CISCO-EVC-MIB:cevcUniCEVlanEvcBeginningVlan = ' + str(self.cevcunicevlanevcbeginningvlan) + '][CISCO-EVC-MIB:cevcUniEvcIndex = ' + str(self.cevcunievcindex) + '][CISCO-EVC-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cevcunicevlanevcbeginningvlan is not None:
                    return True

                if self.cevcunievcindex is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.cevcunicevlanevcendingvlan is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                return meta._meta_table['CISCOEVCMIB.CevcUniCEVlanEvcTable.CevcUniCEVlanEvcEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcUniCEVlanEvcTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cevcunicevlanevcentry is not None:
                for child_ref in self.cevcunicevlanevcentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
            return meta._meta_table['CISCOEVCMIB.CevcUniCEVlanEvcTable']['meta_info']


    class CevcUniTable(object):
        """
        This table contains a list of UNIs locally configured on the
        system.
        
        This table has a sparse dependent relationship on the 
        cevcPortTable, containing a row for each cevcPortEntry
        having a cevcPortMode column value 'uni'.
        
        .. attribute:: cevcunientry
        
        	This entry represents an UNI and its service attributes.  The system automatically creates an entry when the system or the EMS/NMS creates a row in the cevcPortTable with a  cevcPortMode of 'uni'.  Likewise, the system automatically destroys an entry when the system or the EMS/NMS destroys the corresponding row in the cevcPortTable
        	**type**\: list of :py:class:`CevcUniEntry <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcUniTable.CevcUniEntry>`
        
        

        """

        _prefix = 'cisco-evc'
        _revision = '2012-05-21'

        def __init__(self):
            self.parent = None
            self.cevcunientry = YList()
            self.cevcunientry.parent = self
            self.cevcunientry.name = 'cevcunientry'


        class CevcUniEntry(object):
            """
            This entry represents an UNI and its service attributes.
            
            The system automatically creates an entry when the system or
            the EMS/NMS creates a row in the cevcPortTable with a 
            cevcPortMode of 'uni'.  Likewise, the system automatically
            destroys an entry when the system or the EMS/NMS destroys the
            corresponding row in the cevcPortTable.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cevcuniidentifier
            
            	This object specifies a string\-value assigned to a UNI for identification.  When the UNI identifier is configured by the system or the EMS/NMS, it should be unique among all UNIs for the MEN.  If the UNI identifier value is not specified, the value of the cevcUniIdentifier column is a zero\-length string
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: cevcuniporttype
            
            	This object specifies the UNI port type.   'dot1q'     The UNI port is an IEEE 802.1q port.      'dot1ad'     The UNI port is an IEEE 802.1ad port
            	**type**\: :py:class:`CevcUniPortType_Enum <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcUniTable.CevcUniEntry.CevcUniPortType_Enum>`
            
            .. attribute:: cevcuniserviceattributes
            
            	This object specifies the UNI service attributes.   'serviceMultiplexing'     This bit specifies whether the UNI supports multiple     EVCs.  Point\-to\-Point EVCs and Multipoint\-to\-Multipoint     EVCs may be multiplexed in any combination at the UNI      if this bit is set to '1'.   'bundling'     This bit specifies whether the UNI has the bundling     attribute configured.  If this bit is set to '1', more     than one CE\-VLAN ID can map to a particular EVC at the     UNI.    'allToOneBundling'     This bit specifies whether the UNI has the all to one     bundling attribute.  If this bit is set to '1', all     CE\-VLAN IDs map to a single EVC at the UNI.  To summarize the valid combinations of serviceMultiplexing(0), bundling(1) and allToOneBundling(2) bits for an UNI, consider  the following diagram\:             VALID COMBINATIONS +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+  \|UNI ATTRIBUTES \|   1   \|   2   \|   3   \|   4   \|   5   \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+ \|Service        \|       \|       \|       \|       \|       \| \|Multiplexing   \|       \|   Y   \|   Y   \|       \|       \| \|               \|       \|       \|       \|       \|       \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+ \|               \|       \|       \|       \|       \|       \| \|Bundling       \|       \|       \|   Y   \|   Y   \|       \| \|               \|       \|       \|       \|       \|       \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+ \|All to One     \|       \|       \|       \|       \|       \| \|Bundling       \|       \|       \|       \|       \|   Y   \| \|               \|       \|       \|       \|       \|       \| +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\- +\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+
            	**type**\: :py:class:`CevcUniServiceAttributes_Bits <ydk.models.evc.CISCO_EVC_MIB.CISCOEVCMIB.CevcUniTable.CevcUniEntry.CevcUniServiceAttributes_Bits>`
            
            

            """

            _prefix = 'cisco-evc'
            _revision = '2012-05-21'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.cevcuniidentifier = None
                self.cevcuniporttype = None
                self.cevcuniserviceattributes = CISCOEVCMIB.CevcUniTable.CevcUniEntry.CevcUniServiceAttributes_Bits()

            class CevcUniPortType_Enum(Enum):
                """
                CevcUniPortType_Enum

                This object specifies the UNI port type.
                
                
                'dot1q'
                    The UNI port is an IEEE 802.1q port.   
                
                
                'dot1ad'
                    The UNI port is an IEEE 802.1ad port.

                """

                DOT1Q = 1

                DOT1AD = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                    return meta._meta_table['CISCOEVCMIB.CevcUniTable.CevcUniEntry.CevcUniPortType_Enum']


            class CevcUniServiceAttributes_Bits(FixedBitsDict):
                """
                CevcUniServiceAttributes_Bits

                This object specifies the UNI service attributes.
                
                
                'serviceMultiplexing'
                    This bit specifies whether the UNI supports multiple
                    EVCs.  Point\-to\-Point EVCs and Multipoint\-to\-Multipoint
                    EVCs may be multiplexed in any combination at the UNI 
                    if this bit is set to '1'.
                
                
                'bundling'
                    This bit specifies whether the UNI has the bundling
                    attribute configured.  If this bit is set to '1', more
                    than one CE\-VLAN ID can map to a particular EVC at the
                    UNI. 
                
                
                'allToOneBundling'
                    This bit specifies whether the UNI has the all to one
                    bundling attribute.  If this bit is set to '1', all
                    CE\-VLAN IDs map to a single EVC at the UNI.
                
                To summarize the valid combinations of serviceMultiplexing(0),
                bundling(1) and allToOneBundling(2) bits for an UNI, consider 
                the following diagram\:
                
                           VALID COMBINATIONS
                +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+ 
                \|UNI ATTRIBUTES \|   1   \|   2   \|   3   \|   4   \|   5   \|
                +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-+\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+
                \|Service        \|       \|       \|       \|       \|       \|
                \|Multiplexing   \|       \|   Y   \|   Y   \|       \|       \|
                \|               \|       \|       \|       \|       \|       \|
                +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+
                \|               \|       \|       \|       \|       \|       \|
                \|Bundling       \|       \|       \|   Y   \|   Y   \|       \|
                \|               \|       \|       \|       \|       \|       \|
                +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+
                \|All to One     \|       \|       \|       \|       \|       \|
                \|Bundling       \|       \|       \|       \|       \|   Y   \|
                \|               \|       \|       \|       \|       \|       \|
                +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+\-\-\-\-\-\- +\-\-\-\-\-\-\-+\-\-\-\-\-\-\-+
                Keys are:- bundling , serviceMultiplexing , allToOneBundling

                """

                def __init__(self):
                    self._dictionary = { 
                        'bundling':False,
                        'serviceMultiplexing':False,
                        'allToOneBundling':False,
                    }
                    self._pos_map = { 
                        'bundling':1,
                        'serviceMultiplexing':0,
                        'allToOneBundling':2,
                    }

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcUniTable/CISCO-EVC-MIB:cevcUniEntry[CISCO-EVC-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.cevcuniidentifier is not None:
                    return True

                if self.cevcuniporttype is not None:
                    return True

                if self.cevcuniserviceattributes is not None:
                    if self.cevcuniserviceattributes._has_data():
                        return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
                return meta._meta_table['CISCOEVCMIB.CevcUniTable.CevcUniEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-EVC-MIB:CISCO-EVC-MIB/CISCO-EVC-MIB:cevcUniTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cevcunientry is not None:
                for child_ref in self.cevcunientry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
            return meta._meta_table['CISCOEVCMIB.CevcUniTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-EVC-MIB:CISCO-EVC-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cevcevcnotificationconfig is not None and self.cevcevcnotificationconfig._has_data():
            return True

        if self.cevcevcnotificationconfig is not None and self.cevcevcnotificationconfig.is_presence():
            return True

        if self.cevcevcstatetable is not None and self.cevcevcstatetable._has_data():
            return True

        if self.cevcevcstatetable is not None and self.cevcevcstatetable.is_presence():
            return True

        if self.cevcevctable is not None and self.cevcevctable._has_data():
            return True

        if self.cevcevctable is not None and self.cevcevctable.is_presence():
            return True

        if self.cevcevcunitable is not None and self.cevcevcunitable._has_data():
            return True

        if self.cevcevcunitable is not None and self.cevcevcunitable.is_presence():
            return True

        if self.cevcmacsecurityviolation is not None and self.cevcmacsecurityviolation._has_data():
            return True

        if self.cevcmacsecurityviolation is not None and self.cevcmacsecurityviolation.is_presence():
            return True

        if self.cevcportl2controlprotocoltable is not None and self.cevcportl2controlprotocoltable._has_data():
            return True

        if self.cevcportl2controlprotocoltable is not None and self.cevcportl2controlprotocoltable.is_presence():
            return True

        if self.cevcporttable is not None and self.cevcporttable._has_data():
            return True

        if self.cevcporttable is not None and self.cevcporttable.is_presence():
            return True

        if self.cevcsicevlantable is not None and self.cevcsicevlantable._has_data():
            return True

        if self.cevcsicevlantable is not None and self.cevcsicevlantable.is_presence():
            return True

        if self.cevcsiforwardbdtable is not None and self.cevcsiforwardbdtable._has_data():
            return True

        if self.cevcsiforwardbdtable is not None and self.cevcsiforwardbdtable.is_presence():
            return True

        if self.cevcsil2controlprotocoltable is not None and self.cevcsil2controlprotocoltable._has_data():
            return True

        if self.cevcsil2controlprotocoltable is not None and self.cevcsil2controlprotocoltable.is_presence():
            return True

        if self.cevcsimatchcriteriatable is not None and self.cevcsimatchcriteriatable._has_data():
            return True

        if self.cevcsimatchcriteriatable is not None and self.cevcsimatchcriteriatable.is_presence():
            return True

        if self.cevcsimatchencaptable is not None and self.cevcsimatchencaptable._has_data():
            return True

        if self.cevcsimatchencaptable is not None and self.cevcsimatchencaptable.is_presence():
            return True

        if self.cevcsiprimaryvlantable is not None and self.cevcsiprimaryvlantable._has_data():
            return True

        if self.cevcsiprimaryvlantable is not None and self.cevcsiprimaryvlantable.is_presence():
            return True

        if self.cevcsisecondaryvlantable is not None and self.cevcsisecondaryvlantable._has_data():
            return True

        if self.cevcsisecondaryvlantable is not None and self.cevcsisecondaryvlantable.is_presence():
            return True

        if self.cevcsistatetable is not None and self.cevcsistatetable._has_data():
            return True

        if self.cevcsistatetable is not None and self.cevcsistatetable.is_presence():
            return True

        if self.cevcsitable is not None and self.cevcsitable._has_data():
            return True

        if self.cevcsitable is not None and self.cevcsitable.is_presence():
            return True

        if self.cevcsivlanrewritetable is not None and self.cevcsivlanrewritetable._has_data():
            return True

        if self.cevcsivlanrewritetable is not None and self.cevcsivlanrewritetable.is_presence():
            return True

        if self.cevcsystem is not None and self.cevcsystem._has_data():
            return True

        if self.cevcsystem is not None and self.cevcsystem.is_presence():
            return True

        if self.cevcunicevlanevctable is not None and self.cevcunicevlanevctable._has_data():
            return True

        if self.cevcunicevlanevctable is not None and self.cevcunicevlanevctable.is_presence():
            return True

        if self.cevcunitable is not None and self.cevcunitable._has_data():
            return True

        if self.cevcunitable is not None and self.cevcunitable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.evc._meta import _CISCO_EVC_MIB as meta
        return meta._meta_table['CISCOEVCMIB']['meta_info']



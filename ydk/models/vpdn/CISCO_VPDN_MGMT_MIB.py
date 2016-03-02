""" CISCO_VPDN_MGMT_MIB 

The MIB module for VPDN.

Overview of VPDN MIB

MIB description

This MIB is to support the Virtual Private Dialup Network (VPDN)
feature of Cisco IOS.  VPDN handles the forwarding of PPP links
from an Internet Provider (ISP) to a Home Gateway.

The VPDN MIB provides the operational information on Cisco's
VPDN tunnelling implementation.  The following entities are
managed\:
1) Global VPDN information
2) VPDN tunnel information
3) VPDN tunnel's user information
4) Failure history per user

The following example configuration shows how the VPDN MIB
returns VPDN information, from either CISCO A \- Network Access
Server (NAS) or CISCO B \- Tunnel Server (TS).  The User call is
projected by either domain name or Dialed Number Identification
Service (DNIS).

The terms NAS and TS are generic terms refering to the VPDN
systems.

The following table shows the corresponding technology\-specific
terms.

      Network Access Server            Tunnel Server
      \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-   \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-
L2F   Network Access Server    (NAS)   Home Gateway (HGW)
L2TP  L2TP Access Concentrator (LAC)   L2TP Network Server (LNS)
PPTP  PPTP Access Concentrator (PAC)   PPTP Network Server (PNS)

           (NAS)                          (TS)
User ===== Cisco A ===== IP Network ===== Cisco B ===== Server
                \|                          \|
                +========== VPDN ==========+

1) The VPDN global entry identifies the system wide VPDN
   information.
2) The VPDN tunnel table identifies the active VPDN tunnels on
   Cisco A and Cisco B.  The table contains an entry for each
   active tunnel on the system.
3) The VPDN tunnel user table identifies the active users for
   each active tunnel on each system and provides relevant
   information for each user.
4) The VPDN failure history table identifies the last failure
   recorded per user and provides relevant information.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.inet.INET_ADDRESS_MIB import InetAddressType_Enum

class EndpointClass_Enum(Enum):
    """
    EndpointClass_Enum

    The endpoint discriminator class supplied by the remote peer in
    a PPP Multilink bundle.
    
    RFC 1990 defines the following classes\:
    
    none\:        Class 0 \- Null Class.  No endpoint discriminator
                 is being used.  The endpoint discriminator should
                 contain a SnmpAdminString (SIZE (0)) value.
    
    local\:       Class 1 \- Locally Assigned Address.  This class is
                 defined to permit a local assignment in the case
                 where use of one of the globally unique classes is
                 not possible.  The endpoint discriminator should
                 contain a SnmpAdminString (SIZE(1..20)) value.
    
    ipV4Address\: Class 2 \- Internet Protocol (IP) Address.  An
                 address in this class contains an IP host address.
                 The endpoint discriminator should contain a
                 InetAddressIPv4 value.
    
    macAddress\:  Class 3 \- IEEE 802.1 Globally Assigned MAC
                 Address.  An address in this class contains an
                 IEEE 802.1 MAC address in canonical (802.3)
                 format.  The endpoint discriminator should contain
                 a MacAddress value.
    
    magicNumber\: Class 4 \- PPP Magic\-Number Block.  This is not an
                 address but a block of 1 to 5 concatenated 32 bit
                 PPP Magic\-Numbers.  The endpoint discriminator
                 should contain an OCTET STRING (SIZE (4\|8\|12\|16\|
                 20)) value.
    
    phone\:       Class 5 \- Public Switched Network Directory 
                 Number.  An address in this class contains an
                 octet sequence as defined by I.331 (E.164)
                 representing an international telephone directory
                 number suitable for use to access the endpoint via
                 the public switched telephone network.  The
                 endpoint discriminator should contain a
                 SnmpAdminString (SIZE(1..15)) value.

    """

    NONE = 1

    LOCAL = 2

    IPV4ADDRESS = 3

    MACADDRESS = 4

    MAGICNUMBER = 5

    PHONE = 6


    @staticmethod
    def _meta_info():
        from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
        return meta._meta_table['EndpointClass_Enum']


class TunnelType_Enum(Enum):
    """
    TunnelType_Enum

    The tunnel type.  This is the tunnel protocol of a VPDN
    tunnel.

    """

    L2F = 1

    L2TP = 2

    PPTP = 3


    @staticmethod
    def _meta_info():
        from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
        return meta._meta_table['TunnelType_Enum']



class CISCOVPDNMGMTMIB(object):
    """
    
    
    .. attribute:: ciscovpdnmgmtmibnotifs
    
    	
    	**type**\: :py:class:`CiscoVpdnMgmtMIBNotifs <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CiscoVpdnMgmtMIBNotifs>`
    
    .. attribute:: cvpdnbundlechildtable
    
    	A table that exposes the containment relationship between a multilink PPP bundle and a VPDN tunnel
    	**type**\: :py:class:`CvpdnBundleChildTable <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnBundleChildTable>`
    
    .. attribute:: cvpdnbundletable
    
    	Table that describes the multilink PPP attributes of the active VPDN sessions
    	**type**\: :py:class:`CvpdnBundleTable <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnBundleTable>`
    
    .. attribute:: cvpdnmultilinkinfo
    
    	
    	**type**\: :py:class:`CvpdnMultilinkInfo <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnMultilinkInfo>`
    
    .. attribute:: cvpdnsessionattrtable
    
    	Table of information about individual sessions within the active tunnels.  An entry is added to the table when a new session is initiated and removed from the table when the session is terminated
    	**type**\: :py:class:`CvpdnSessionAttrTable <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnSessionAttrTable>`
    
    .. attribute:: cvpdnsysteminfo
    
    	
    	**type**\: :py:class:`CvpdnSystemInfo <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnSystemInfo>`
    
    .. attribute:: cvpdnsystemtable
    
    	Table of information about the VPDN system for all tunnel types
    	**type**\: :py:class:`CvpdnSystemTable <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnSystemTable>`
    
    .. attribute:: cvpdntemplatetable
    
    	Table of information about the VPDN templates.  The VPDN template is a grouping mechanism that allows configuration settings to be shared among multiple VPDN groups.  One such setting is a limit on the number of active sessions across all VPDN groups associated with the template.  The template table allows customers to monitor template\-wide information such as tracking the allocation of sessions across templates
    	**type**\: :py:class:`CvpdnTemplateTable <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTemplateTable>`
    
    .. attribute:: cvpdntunnelattrtable
    
    	Table of information about the active VPDN tunnels.  An entry is added to the table when a new tunnel is initiated and removed from the table when the tunnel is terminated
    	**type**\: :py:class:`CvpdnTunnelAttrTable <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable>`
    
    .. attribute:: cvpdntunnelsessiontable
    
    	Table of information about individual user sessions within the active tunnels.  Entry is added to the table when new user session is initiated and be removed from the table when the user session is terminated
    	**type**\: :py:class:`CvpdnTunnelSessionTable <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelSessionTable>`
    
    .. attribute:: cvpdntunneltable
    
    	Table of information about the active VPDN tunnels
    	**type**\: :py:class:`CvpdnTunnelTable <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelTable>`
    
    .. attribute:: cvpdnusertofailhistinfotable
    
    	Table of the record of failure objects which can be referenced by an user name.  Only a name that has a valid item in the Cisco IOS VPDN failure history table will yield a valid entry in this table.  The table has a maximum size of 50 entries.  Only the newest 50 entries will be kept in the table
    	**type**\: :py:class:`CvpdnUserToFailHistInfoTable <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnUserToFailHistInfoTable>`
    
    

    """

    _prefix = 'cisco-vpdn'
    _revision = '2009-06-16'

    def __init__(self):
        self.ciscovpdnmgmtmibnotifs = CISCOVPDNMGMTMIB.CiscoVpdnMgmtMIBNotifs()
        self.ciscovpdnmgmtmibnotifs.parent = self
        self.cvpdnbundlechildtable = CISCOVPDNMGMTMIB.CvpdnBundleChildTable()
        self.cvpdnbundlechildtable.parent = self
        self.cvpdnbundletable = CISCOVPDNMGMTMIB.CvpdnBundleTable()
        self.cvpdnbundletable.parent = self
        self.cvpdnmultilinkinfo = CISCOVPDNMGMTMIB.CvpdnMultilinkInfo()
        self.cvpdnmultilinkinfo.parent = self
        self.cvpdnsessionattrtable = CISCOVPDNMGMTMIB.CvpdnSessionAttrTable()
        self.cvpdnsessionattrtable.parent = self
        self.cvpdnsysteminfo = CISCOVPDNMGMTMIB.CvpdnSystemInfo()
        self.cvpdnsysteminfo.parent = self
        self.cvpdnsystemtable = CISCOVPDNMGMTMIB.CvpdnSystemTable()
        self.cvpdnsystemtable.parent = self
        self.cvpdntemplatetable = CISCOVPDNMGMTMIB.CvpdnTemplateTable()
        self.cvpdntemplatetable.parent = self
        self.cvpdntunnelattrtable = CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable()
        self.cvpdntunnelattrtable.parent = self
        self.cvpdntunnelsessiontable = CISCOVPDNMGMTMIB.CvpdnTunnelSessionTable()
        self.cvpdntunnelsessiontable.parent = self
        self.cvpdntunneltable = CISCOVPDNMGMTMIB.CvpdnTunnelTable()
        self.cvpdntunneltable.parent = self
        self.cvpdnusertofailhistinfotable = CISCOVPDNMGMTMIB.CvpdnUserToFailHistInfoTable()
        self.cvpdnusertofailhistinfotable.parent = self


    class CiscoVpdnMgmtMIBNotifs(object):
        """
        
        
        .. attribute:: cvpdnnotifsessionevent
        
        	Indicates the event that generated the L2X session notification.  The events are represented as follows\:  up\:     Session has come up.  down\:   Session has gone down.  pwUp\:   Pseudowire associated with this          session has come up.  pwDown\: Pseudowire associated with this          session has gone down
        	**type**\: :py:class:`CvpdnNotifSessionEvent_Enum <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CiscoVpdnMgmtMIBNotifs.CvpdnNotifSessionEvent_Enum>`
        
        .. attribute:: cvpdnnotifsessionid
        
        	This object contains the local session ID of the L2X session for which this notification has been generated
        	**type**\: int
        
        	**range:** 0..65535
        
        

        """

        _prefix = 'cisco-vpdn'
        _revision = '2009-06-16'

        def __init__(self):
            self.parent = None
            self.cvpdnnotifsessionevent = None
            self.cvpdnnotifsessionid = None

        class CvpdnNotifSessionEvent_Enum(Enum):
            """
            CvpdnNotifSessionEvent_Enum

            Indicates the event that generated the L2X session
            notification.
            
            The events are represented as follows\:
            
            up\:     Session has come up.
            
            down\:   Session has gone down.
            
            pwUp\:   Pseudowire associated with this 
                    session has come up.
            
            pwDown\: Pseudowire associated with this 
                    session has gone down.

            """

            UP = 1

            DOWN = 2

            PWUP = 3

            PWDOWN = 4


            @staticmethod
            def _meta_info():
                from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
                return meta._meta_table['CISCOVPDNMGMTMIB.CiscoVpdnMgmtMIBNotifs.CvpdnNotifSessionEvent_Enum']


        @property
        def _common_path(self):

            return '/CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/CISCO-VPDN-MGMT-MIB:ciscoVpdnMgmtMIBNotifs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvpdnnotifsessionevent is not None:
                return True

            if self.cvpdnnotifsessionid is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
            return meta._meta_table['CISCOVPDNMGMTMIB.CiscoVpdnMgmtMIBNotifs']['meta_info']


    class CvpdnBundleChildTable(object):
        """
        A table that exposes the containment relationship between a
        multilink PPP bundle and a VPDN tunnel.
        
        .. attribute:: cvpdnbundlechildentry
        
        	An entry in this table represents a session that belongs to a VPDN tunnel and to a multilink PPP bundle
        	**type**\: list of :py:class:`CvpdnBundleChildEntry <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnBundleChildTable.CvpdnBundleChildEntry>`
        
        

        """

        _prefix = 'cisco-vpdn'
        _revision = '2009-06-16'

        def __init__(self):
            self.parent = None
            self.cvpdnbundlechildentry = YList()
            self.cvpdnbundlechildentry.parent = self
            self.cvpdnbundlechildentry.name = 'cvpdnbundlechildentry'


        class CvpdnBundleChildEntry(object):
            """
            An entry in this table represents a session that belongs to
            a VPDN tunnel and to a multilink PPP bundle.
            
            .. attribute:: cvpdnbundlechildsessionid
            
            	The ID of an active VPDN session that is associated with a multilink PPP bundle
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnbundlechildtunnelid
            
            	The Tunnel ID of an active VPDN session that is associated with a multilink PPP bundle
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnbundlechildtunneltype
            
            	The tunnel type.  This is the tunnel protocol of an active VPDN session that is associated with a multilink PPP bundle
            	**type**\: :py:class:`TunnelType_Enum <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.TunnelType_Enum>`
            
            .. attribute:: cvpdnbundlename
            
            	
            	**type**\: str
            
            	**range:** 1..64
            
            

            """

            _prefix = 'cisco-vpdn'
            _revision = '2009-06-16'

            def __init__(self):
                self.parent = None
                self.cvpdnbundlechildsessionid = None
                self.cvpdnbundlechildtunnelid = None
                self.cvpdnbundlechildtunneltype = None
                self.cvpdnbundlename = None

            @property
            def _common_path(self):
                if self.cvpdnbundlechildsessionid is None:
                    raise YPYDataValidationError('Key property cvpdnbundlechildsessionid is None')
                if self.cvpdnbundlechildtunnelid is None:
                    raise YPYDataValidationError('Key property cvpdnbundlechildtunnelid is None')
                if self.cvpdnbundlechildtunneltype is None:
                    raise YPYDataValidationError('Key property cvpdnbundlechildtunneltype is None')
                if self.cvpdnbundlename is None:
                    raise YPYDataValidationError('Key property cvpdnbundlename is None')

                return '/CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/CISCO-VPDN-MGMT-MIB:cvpdnBundleChildTable/CISCO-VPDN-MGMT-MIB:cvpdnBundleChildEntry[CISCO-VPDN-MGMT-MIB:cvpdnBundleChildSessionId = ' + str(self.cvpdnbundlechildsessionid) + '][CISCO-VPDN-MGMT-MIB:cvpdnBundleChildTunnelId = ' + str(self.cvpdnbundlechildtunnelid) + '][CISCO-VPDN-MGMT-MIB:cvpdnBundleChildTunnelType = ' + str(self.cvpdnbundlechildtunneltype) + '][CISCO-VPDN-MGMT-MIB:cvpdnBundleName = ' + str(self.cvpdnbundlename) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cvpdnbundlechildsessionid is not None:
                    return True

                if self.cvpdnbundlechildtunnelid is not None:
                    return True

                if self.cvpdnbundlechildtunneltype is not None:
                    return True

                if self.cvpdnbundlename is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
                return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnBundleChildTable.CvpdnBundleChildEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/CISCO-VPDN-MGMT-MIB:cvpdnBundleChildTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvpdnbundlechildentry is not None:
                for child_ref in self.cvpdnbundlechildentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
            return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnBundleChildTable']['meta_info']


    class CvpdnBundleTable(object):
        """
        Table that describes the multilink PPP attributes of the
        active VPDN sessions.
        
        .. attribute:: cvpdnbundleentry
        
        	An entry in this table represents an active multilink PPP bundle that belongs to a VPDN tunnel
        	**type**\: list of :py:class:`CvpdnBundleEntry <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnBundleTable.CvpdnBundleEntry>`
        
        

        """

        _prefix = 'cisco-vpdn'
        _revision = '2009-06-16'

        def __init__(self):
            self.parent = None
            self.cvpdnbundleentry = YList()
            self.cvpdnbundleentry.parent = self
            self.cvpdnbundleentry.name = 'cvpdnbundleentry'


        class CvpdnBundleEntry(object):
            """
            An entry in this table represents an active multilink PPP
            bundle that belongs to a VPDN tunnel.
            
            .. attribute:: cvpdnbundlename
            
            	The name of the multilink PPP bundle associated with a VPDN tunnel
            	**type**\: str
            
            	**range:** 1..64
            
            .. attribute:: cvpdnbundleendpoint
            
            	Indicates the discriminator used in this bundle that is associated with a VPDN tunnel
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cvpdnbundleendpointclass
            
            	The multilink PPP bundle discriminator class associated with a VPDN tunnel.  The value of this object represents the type of discriminator used in cvpdnBundleEndpoint
            	**type**\: :py:class:`EndpointClass_Enum <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.EndpointClass_Enum>`
            
            .. attribute:: cvpdnbundleendpointtype
            
            	The multilink PPP bundle discriminator type associated with a VPDN tunnel.  The value of this object represents the type of discriminator used in cvpdnBundleEndpoint.      none\:        No endpoint discriminator was supplied, the                  default value is being used.      hostname\:    The router's hostname is being used as                  discriminator.      string\:      User specified string is being used as                  discriminator.      macAddress\:  A MAC address as defined by the MacAddress                  textual convention is being used as                  discriminator.      ipV4Address\: An IP address as defined by the                  InetAddressIPv4 textual convention is being                  used as discriminator.      ipV6Address\: An IP address as defined by the                  InetAddressIPv6 textual convention is being                  used as discriminator.      phone\:       The PSTN phone number is being used as                  discriminator.      magicNumber\: A magic number is being used as                  discriminator
            	**type**\: :py:class:`CvpdnBundleEndpointType_Enum <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnBundleTable.CvpdnBundleEntry.CvpdnBundleEndpointType_Enum>`
            
            .. attribute:: cvpdnbundlelinkcount
            
            	The total number of active links in a multilink PPP bundle associated with a VPDN tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnbundlepeeripaddr
            
            	The IP address of the multilink PPP peer in a VPDN tunnel
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cvpdnbundlepeeripaddrtype
            
            	Indicates the type of address contained in cvpdnBundlePeerIpAddr
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            

            """

            _prefix = 'cisco-vpdn'
            _revision = '2009-06-16'

            def __init__(self):
                self.parent = None
                self.cvpdnbundlename = None
                self.cvpdnbundleendpoint = None
                self.cvpdnbundleendpointclass = None
                self.cvpdnbundleendpointtype = None
                self.cvpdnbundlelinkcount = None
                self.cvpdnbundlepeeripaddr = None
                self.cvpdnbundlepeeripaddrtype = None

            class CvpdnBundleEndpointType_Enum(Enum):
                """
                CvpdnBundleEndpointType_Enum

                The multilink PPP bundle discriminator type associated with
                a VPDN tunnel.  The value of this object represents the type
                of discriminator used in cvpdnBundleEndpoint.
                
                    none\:        No endpoint discriminator was supplied, the
                                 default value is being used.
                
                    hostname\:    The router's hostname is being used as
                                 discriminator.
                
                    string\:      User specified string is being used as
                                 discriminator.
                
                    macAddress\:  A MAC address as defined by the MacAddress
                                 textual convention is being used as
                                 discriminator.
                
                    ipV4Address\: An IP address as defined by the
                                 InetAddressIPv4 textual convention is being
                                 used as discriminator.
                
                    ipV6Address\: An IP address as defined by the
                                 InetAddressIPv6 textual convention is being
                                 used as discriminator.
                
                    phone\:       The PSTN phone number is being used as
                                 discriminator.
                
                    magicNumber\: A magic number is being used as
                                 discriminator.

                """

                NONE = 1

                HOSTNAME = 2

                STRING = 3

                MACADDRESS = 4

                IPV4ADDRESS = 5

                IPV6ADDRESS = 6

                PHONE = 7

                MAGICNUMBER = 8


                @staticmethod
                def _meta_info():
                    from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
                    return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnBundleTable.CvpdnBundleEntry.CvpdnBundleEndpointType_Enum']


            @property
            def _common_path(self):
                if self.cvpdnbundlename is None:
                    raise YPYDataValidationError('Key property cvpdnbundlename is None')

                return '/CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/CISCO-VPDN-MGMT-MIB:cvpdnBundleTable/CISCO-VPDN-MGMT-MIB:cvpdnBundleEntry[CISCO-VPDN-MGMT-MIB:cvpdnBundleName = ' + str(self.cvpdnbundlename) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cvpdnbundlename is not None:
                    return True

                if self.cvpdnbundleendpoint is not None:
                    return True

                if self.cvpdnbundleendpointclass is not None:
                    return True

                if self.cvpdnbundleendpointtype is not None:
                    return True

                if self.cvpdnbundlelinkcount is not None:
                    return True

                if self.cvpdnbundlepeeripaddr is not None:
                    return True

                if self.cvpdnbundlepeeripaddrtype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
                return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnBundleTable.CvpdnBundleEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/CISCO-VPDN-MGMT-MIB:cvpdnBundleTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvpdnbundleentry is not None:
                for child_ref in self.cvpdnbundleentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
            return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnBundleTable']['meta_info']


    class CvpdnMultilinkInfo(object):
        """
        
        
        .. attribute:: cvpdnbundlelastchanged
        
        	The value of the sysUpTime object when the contents of cvpdnBundleTable last changed
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cvpdnbundleswithmorethantwolinks
        
        	The total number of bundles comprised of more than two links
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cvpdnbundleswithonelink
        
        	The total number of bundles comprised of a single link
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cvpdnbundleswithtwolinks
        
        	The total number of bundles comprised of two links
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-vpdn'
        _revision = '2009-06-16'

        def __init__(self):
            self.parent = None
            self.cvpdnbundlelastchanged = None
            self.cvpdnbundleswithmorethantwolinks = None
            self.cvpdnbundleswithonelink = None
            self.cvpdnbundleswithtwolinks = None

        @property
        def _common_path(self):

            return '/CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/CISCO-VPDN-MGMT-MIB:cvpdnMultilinkInfo'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvpdnbundlelastchanged is not None:
                return True

            if self.cvpdnbundleswithmorethantwolinks is not None:
                return True

            if self.cvpdnbundleswithonelink is not None:
                return True

            if self.cvpdnbundleswithtwolinks is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
            return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnMultilinkInfo']['meta_info']


    class CvpdnSessionAttrTable(object):
        """
        Table of information about individual sessions within the
        active tunnels.  An entry is added to the table when a new
        session is initiated and removed from the table when the
        session is terminated.
        
        .. attribute:: cvpdnsessionattrentry
        
        	An entry in the table, containing information about a single session within the tunnel
        	**type**\: list of :py:class:`CvpdnSessionAttrEntry <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnSessionAttrTable.CvpdnSessionAttrEntry>`
        
        

        """

        _prefix = 'cisco-vpdn'
        _revision = '2009-06-16'

        def __init__(self):
            self.parent = None
            self.cvpdnsessionattrentry = YList()
            self.cvpdnsessionattrentry.parent = self
            self.cvpdnsessionattrentry.name = 'cvpdnsessionattrentry'


        class CvpdnSessionAttrEntry(object):
            """
            An entry in the table, containing information about a
            single session within the tunnel.
            
            .. attribute:: cvpdnsessionattrsessionid
            
            	The ID of an active VPDN session
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cvpdnsystemtunneltype
            
            	
            	**type**\: :py:class:`TunnelType_Enum <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.TunnelType_Enum>`
            
            .. attribute:: cvpdntunnelattrtunnelid
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cvpdnsessionattrbytesin
            
            	The total number of input bytes through this active session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrbytesout
            
            	The total number of output bytes through this active session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrcallduration
            
            	This object specifies the call duration of the current active session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrdevicecallerid
            
            	The incoming caller identification of the user.  It is the originating number that called into the device that initiates the session.  This object can be empty since not all dial devices can provide caller ID information
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cvpdnsessionattrdevicephyid
            
            	The device ID of the physical interface for the session. The object is the the interface index which points to the ifTable.  For virtual interfaces that are not in the ifTable, the value will be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cvpdnsessionattrdevicetype
            
            	The type of physical devices that this session is attached to for the local end of the tunnel.  The meaning of each device type is explained below\:      other\:              Any device that has not been                         defined.      asyncInternalModem\: Modem Pool device of an access                         server.      async\:              A regular asynchronous serial                         interface.      sync\:               A regular synchronous serial                         interface.      bchan\:              An ISDN call.      xdsl\:               xDSL interface.      cable\:              cable modem interface
            	**type**\: :py:class:`CvpdnSessionAttrDeviceType_Enum <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnSessionAttrTable.CvpdnSessionAttrEntry.CvpdnSessionAttrDeviceType_Enum>`
            
            .. attribute:: cvpdnsessionattrds1channelindex
            
            	The DS1 database channel index if it is associated with this session.  Only a session over a device of type 'asyncInternalModem' will have a valid value for this object; otherwise it is not instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrds1portindex
            
            	The DS1 database port index if it is associated with this session.  Only a session with a device of type 'asyncInternalModem' will have a valid value for this object; otherwise it is not instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrds1slotindex
            
            	The DS1 database slot index if it is associated with this session.  Only a session with a device of type 'asyncInternalModem' will have a valid value for this object; otherwise it is not instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrmodemcallstartindex
            
            	Arbitrary small integer to distinguish modem calls that occurred at the same time tick.  Only session over device 'asyncInternalModem' will have a valid value for this object; otherwise, it is not instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrmodemcallstarttime
            
            	The start time of the current modem call.  Only a session with a device of type 'asyncInternalModem' will have a valid value for this object; otherwise, it is not instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrmodemportindex
            
            	The Modem Pool database port index if it is associated with this session.  Only a session with a device of type 'asyncInternalModem' will have a valid value for this object; otherwise, it is not instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrmodemslotindex
            
            	The Modem Pool database slot index if it is associated with this session.  Only a session with device of type 'asyncInternalModem' will have a valid value for this object; otherwise, it is not instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrmultilink
            
            	This object indicates whether the session is part of a multilink PPP bundle, even if there is only one link or session in the bundle.  If it is multilink PPP, the value is true
            	**type**\: bool
            
            .. attribute:: cvpdnsessionattrmultilinkbundle
            
            	This object specifies the name of the multilink bundle to which this session belongs.  The value of this object is only valid when the value of cvpdnSessionAttrMultilink is 'true'.  If the value of cvpdnSessionAttrMultilink is 'false', then the value of this object will be the empty string
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cvpdnsessionattrmultilinkifindex
            
            	This object specifies the ifIndex of the multilink bundle to which this session belongs.  The value of this object is only valid when the value of cvpdnSessionAttrMultilink is 'true'.  If the value of cvpdnSessionAttrMultilink is 'false', then the value of this object will be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cvpdnsessionattrpacketsin
            
            	The total number of input packets through this active session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrpacketsout
            
            	The total number of output packets through this active session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrrecvpktsdropped
            
            	The total number of dropped packets that were received from this active session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrsentpktsdropped
            
            	The total number of dropped packets that could not be sent into this active session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrstate
            
            	The current state of a tunnel session. L2F tunnel sessions will have states with the 'l2f' prefix. L2TP tunnel sessions will have states with the 'l2tp' prefix.  Each state code is explained below\:      unknown\:             The current state of the tunnel's                          session is unknown.      l2fOpening\:          The session has just been                          initiated through a tunnel and is                          pending for the remote end reply                          to complete the process.      l2fOpen\:             The session is active.      l2fCloseWait\:        The session has just been closed                          and is pending for the remote end                          reply to complete the process.      l2fWaitingForTunnel\: The session is in this state when                          the tunnel which this session is                          going through is still in CLOSED                          state.  It waits for the tunnel to                          become OPEN before the session is                          allowed to be fully established.      l2tpIdle\:            No session is initiated yet.      l2tpWaitingTunnel\:   The session is waiting for the                          tunnel to be established.      l2tpWaitReply\:       The session has been initiated and                          is pending for the remote end                          reply to complete the process.      l2tpWaitConnect\:     This end has acknowledged a                          connection request and is waiting                          for the remote end to connect.      l2tpEstablished\:     The session is active.      l2tpShuttingDown\:    The session is in progress of                          shutting down.      pptpWaitVAccess\:     The session is waiting for the                          creation of a virtual access                          interface.      pptpPacEstablished\:  The session is active.      pptpWaitTunnel\:      The session is waiting for the                          tunnel to be established.      pptpWaitOCRP\:        The session has been initiated and                          is pending for the remote end                          reply to complete the process.      pptpPnsEstablished\:  The session is active.      pptpWaitCallDisc\:    Session shutdown is in progress
            	**type**\: :py:class:`CvpdnSessionAttrState_Enum <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnSessionAttrTable.CvpdnSessionAttrEntry.CvpdnSessionAttrState_Enum>`
            
            .. attribute:: cvpdnsessionattrusername
            
            	The name of the user of the session
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cvpdnsessionattrvirtualcircuitid
            
            	The virtual circuit ID of an active Layer 2 VPN session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-vpdn'
            _revision = '2009-06-16'

            def __init__(self):
                self.parent = None
                self.cvpdnsessionattrsessionid = None
                self.cvpdnsystemtunneltype = None
                self.cvpdntunnelattrtunnelid = None
                self.cvpdnsessionattrbytesin = None
                self.cvpdnsessionattrbytesout = None
                self.cvpdnsessionattrcallduration = None
                self.cvpdnsessionattrdevicecallerid = None
                self.cvpdnsessionattrdevicephyid = None
                self.cvpdnsessionattrdevicetype = None
                self.cvpdnsessionattrds1channelindex = None
                self.cvpdnsessionattrds1portindex = None
                self.cvpdnsessionattrds1slotindex = None
                self.cvpdnsessionattrmodemcallstartindex = None
                self.cvpdnsessionattrmodemcallstarttime = None
                self.cvpdnsessionattrmodemportindex = None
                self.cvpdnsessionattrmodemslotindex = None
                self.cvpdnsessionattrmultilink = None
                self.cvpdnsessionattrmultilinkbundle = None
                self.cvpdnsessionattrmultilinkifindex = None
                self.cvpdnsessionattrpacketsin = None
                self.cvpdnsessionattrpacketsout = None
                self.cvpdnsessionattrrecvpktsdropped = None
                self.cvpdnsessionattrsentpktsdropped = None
                self.cvpdnsessionattrstate = None
                self.cvpdnsessionattrusername = None
                self.cvpdnsessionattrvirtualcircuitid = None

            class CvpdnSessionAttrDeviceType_Enum(Enum):
                """
                CvpdnSessionAttrDeviceType_Enum

                The type of physical devices that this session is attached
                to for the local end of the tunnel.  The meaning of each
                device type is explained below\:
                
                    other\:              Any device that has not been
                                        defined.
                
                    asyncInternalModem\: Modem Pool device of an access
                                        server.
                
                    async\:              A regular asynchronous serial
                                        interface.
                
                    sync\:               A regular synchronous serial
                                        interface.
                
                    bchan\:              An ISDN call.
                
                    xdsl\:               xDSL interface.
                
                    cable\:              cable modem interface.

                """

                OTHER = 1

                ASYNCINTERNALMODEM = 2

                ASYNC = 3

                BCHAN = 4

                SYNC = 5

                VIRTUALACCESS = 6

                XDSL = 7

                CABLE = 8


                @staticmethod
                def _meta_info():
                    from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
                    return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnSessionAttrTable.CvpdnSessionAttrEntry.CvpdnSessionAttrDeviceType_Enum']


            class CvpdnSessionAttrState_Enum(Enum):
                """
                CvpdnSessionAttrState_Enum

                The current state of a tunnel session.
                L2F tunnel sessions will have states with the 'l2f' prefix.
                L2TP tunnel sessions will have states with the 'l2tp'
                prefix.
                
                Each state code is explained below\:
                
                    unknown\:             The current state of the tunnel's
                                         session is unknown.
                
                    l2fOpening\:          The session has just been
                                         initiated through a tunnel and is
                                         pending for the remote end reply
                                         to complete the process.
                
                    l2fOpen\:             The session is active.
                
                    l2fCloseWait\:        The session has just been closed
                                         and is pending for the remote end
                                         reply to complete the process.
                
                    l2fWaitingForTunnel\: The session is in this state when
                                         the tunnel which this session is
                                         going through is still in CLOSED
                                         state.  It waits for the tunnel to
                                         become OPEN before the session is
                                         allowed to be fully established.
                
                    l2tpIdle\:            No session is initiated yet.
                
                    l2tpWaitingTunnel\:   The session is waiting for the
                                         tunnel to be established.
                
                    l2tpWaitReply\:       The session has been initiated and
                                         is pending for the remote end
                                         reply to complete the process.
                
                    l2tpWaitConnect\:     This end has acknowledged a
                                         connection request and is waiting
                                         for the remote end to connect.
                
                    l2tpEstablished\:     The session is active.
                
                    l2tpShuttingDown\:    The session is in progress of
                                         shutting down.
                
                    pptpWaitVAccess\:     The session is waiting for the
                                         creation of a virtual access
                                         interface.
                
                    pptpPacEstablished\:  The session is active.
                
                    pptpWaitTunnel\:      The session is waiting for the
                                         tunnel to be established.
                
                    pptpWaitOCRP\:        The session has been initiated and
                                         is pending for the remote end
                                         reply to complete the process.
                
                    pptpPnsEstablished\:  The session is active.
                
                    pptpWaitCallDisc\:    Session shutdown is in progress.

                """

                UNKNOWN = 1

                L2FOPENING = 2

                L2FOPEN = 3

                L2FCLOSEWAIT = 4

                L2FWAITINGFORTUNNEL = 5

                L2TPIDLE = 6

                L2TPWAITINGTUNNEL = 7

                L2TPWAITREPLY = 8

                L2TPWAITCONNECT = 9

                L2TPESTABLISHED = 10

                L2TPSHUTTINGDOWN = 11

                PPTPWAITVACCESS = 12

                PPTPPACESTABLISHED = 13

                PPTPWAITTUNNEL = 14

                PPTPWAITOCRP = 15

                PPTPPNSESTABLISHED = 16

                PPTPWAITCALLDISC = 17

                PPTPTERMINAL = 18


                @staticmethod
                def _meta_info():
                    from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
                    return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnSessionAttrTable.CvpdnSessionAttrEntry.CvpdnSessionAttrState_Enum']


            @property
            def _common_path(self):
                if self.cvpdnsessionattrsessionid is None:
                    raise YPYDataValidationError('Key property cvpdnsessionattrsessionid is None')
                if self.cvpdnsystemtunneltype is None:
                    raise YPYDataValidationError('Key property cvpdnsystemtunneltype is None')
                if self.cvpdntunnelattrtunnelid is None:
                    raise YPYDataValidationError('Key property cvpdntunnelattrtunnelid is None')

                return '/CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/CISCO-VPDN-MGMT-MIB:cvpdnSessionAttrTable/CISCO-VPDN-MGMT-MIB:cvpdnSessionAttrEntry[CISCO-VPDN-MGMT-MIB:cvpdnSessionAttrSessionId = ' + str(self.cvpdnsessionattrsessionid) + '][CISCO-VPDN-MGMT-MIB:cvpdnSystemTunnelType = ' + str(self.cvpdnsystemtunneltype) + '][CISCO-VPDN-MGMT-MIB:cvpdnTunnelAttrTunnelId = ' + str(self.cvpdntunnelattrtunnelid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cvpdnsessionattrsessionid is not None:
                    return True

                if self.cvpdnsystemtunneltype is not None:
                    return True

                if self.cvpdntunnelattrtunnelid is not None:
                    return True

                if self.cvpdnsessionattrbytesin is not None:
                    return True

                if self.cvpdnsessionattrbytesout is not None:
                    return True

                if self.cvpdnsessionattrcallduration is not None:
                    return True

                if self.cvpdnsessionattrdevicecallerid is not None:
                    return True

                if self.cvpdnsessionattrdevicephyid is not None:
                    return True

                if self.cvpdnsessionattrdevicetype is not None:
                    return True

                if self.cvpdnsessionattrds1channelindex is not None:
                    return True

                if self.cvpdnsessionattrds1portindex is not None:
                    return True

                if self.cvpdnsessionattrds1slotindex is not None:
                    return True

                if self.cvpdnsessionattrmodemcallstartindex is not None:
                    return True

                if self.cvpdnsessionattrmodemcallstarttime is not None:
                    return True

                if self.cvpdnsessionattrmodemportindex is not None:
                    return True

                if self.cvpdnsessionattrmodemslotindex is not None:
                    return True

                if self.cvpdnsessionattrmultilink is not None:
                    return True

                if self.cvpdnsessionattrmultilinkbundle is not None:
                    return True

                if self.cvpdnsessionattrmultilinkifindex is not None:
                    return True

                if self.cvpdnsessionattrpacketsin is not None:
                    return True

                if self.cvpdnsessionattrpacketsout is not None:
                    return True

                if self.cvpdnsessionattrrecvpktsdropped is not None:
                    return True

                if self.cvpdnsessionattrsentpktsdropped is not None:
                    return True

                if self.cvpdnsessionattrstate is not None:
                    return True

                if self.cvpdnsessionattrusername is not None:
                    return True

                if self.cvpdnsessionattrvirtualcircuitid is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
                return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnSessionAttrTable.CvpdnSessionAttrEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/CISCO-VPDN-MGMT-MIB:cvpdnSessionAttrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvpdnsessionattrentry is not None:
                for child_ref in self.cvpdnsessionattrentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
            return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnSessionAttrTable']['meta_info']


    class CvpdnSystemInfo(object):
        """
        
        
        .. attribute:: cvpdndenieduserstotal
        
        	The total number of denied user attempts to all the active VPDN tunnels within this system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cvpdnsessiontotal
        
        	The total number of active users in all the active VPDN tunnels within this system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cvpdnsystemclearsessions
        
        	Clears all the sessions in a given tunnel type.  When reading this object, the value of 'none' will always be returned.  When setting these values, the following operations will be performed\:      none\: no operation.      all\:  clears all the sessions in all the tunnels.      l2f\:  clears all the L2F sessions.      l2tp\: clears all the L2TP sessions.      pptp\: clears all the PPTP sessions
        	**type**\: :py:class:`CvpdnSystemClearSessions_Enum <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnSystemInfo.CvpdnSystemClearSessions_Enum>`
        
        .. attribute:: cvpdnsystemnotifsessionenabled
        
        	Indicates whether Layer 2 VPN session notifications are enabled
        	**type**\: bool
        
        .. attribute:: cvpdntunneltotal
        
        	The total number of VPDN tunnels that are currently active within this system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-vpdn'
        _revision = '2009-06-16'

        def __init__(self):
            self.parent = None
            self.cvpdndenieduserstotal = None
            self.cvpdnsessiontotal = None
            self.cvpdnsystemclearsessions = None
            self.cvpdnsystemnotifsessionenabled = None
            self.cvpdntunneltotal = None

        class CvpdnSystemClearSessions_Enum(Enum):
            """
            CvpdnSystemClearSessions_Enum

            Clears all the sessions in a given tunnel type.  When
            reading this object, the value of 'none' will always be
            returned.
            
            When setting these values, the following operations will be
            performed\:
            
                none\: no operation.
            
                all\:  clears all the sessions in all the tunnels.
            
                l2f\:  clears all the L2F sessions.
            
                l2tp\: clears all the L2TP sessions.
            
                pptp\: clears all the PPTP sessions.

            """

            NONE = 1

            ALL = 2

            L2F = 3

            L2TP = 4

            PPTP = 5


            @staticmethod
            def _meta_info():
                from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
                return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnSystemInfo.CvpdnSystemClearSessions_Enum']


        @property
        def _common_path(self):

            return '/CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/CISCO-VPDN-MGMT-MIB:cvpdnSystemInfo'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvpdndenieduserstotal is not None:
                return True

            if self.cvpdnsessiontotal is not None:
                return True

            if self.cvpdnsystemclearsessions is not None:
                return True

            if self.cvpdnsystemnotifsessionenabled is not None:
                return True

            if self.cvpdntunneltotal is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
            return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnSystemInfo']['meta_info']


    class CvpdnSystemTable(object):
        """
        Table of information about the VPDN system for all tunnel
        types.
        
        .. attribute:: cvpdnsystementry
        
        	An entry in the table, containing information about a single type of VPDN tunnel
        	**type**\: list of :py:class:`CvpdnSystemEntry <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnSystemTable.CvpdnSystemEntry>`
        
        

        """

        _prefix = 'cisco-vpdn'
        _revision = '2009-06-16'

        def __init__(self):
            self.parent = None
            self.cvpdnsystementry = YList()
            self.cvpdnsystementry.parent = self
            self.cvpdnsystementry.name = 'cvpdnsystementry'


        class CvpdnSystemEntry(object):
            """
            An entry in the table, containing information about a
            single type of VPDN tunnel.
            
            .. attribute:: cvpdnsystemtunneltype
            
            	The tunnel type.  This is the tunnel protocol
            	**type**\: :py:class:`TunnelType_Enum <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.TunnelType_Enum>`
            
            .. attribute:: cvpdnsystemdenieduserstotal
            
            	The total number of denied user attempts to all the VPDN tunnels of this tunnel type since last system re\-initialization
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsystemfailedconnreq
            
            	The total number tunnel Failed connection attempts in VPDN tunnels of this tunnel type since last system re\-initialization
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsysteminitialconnreq
            
            	The total number tunnel connection attempts on all the VPDN tunnels of this tunnel type since last system re\-initialization
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsystemsessiontotal
            
            	The total number of active sessions in all the active VPDN tunnels of this tunnel type
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsystemsuccessconnreq
            
            	The total number tunnel Successful connection attempts in VPDN tunnels of this tunnel type since last system re\-initialization
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsystemtunneltotal
            
            	The total number of VPDN tunnels that are currently active of this tunnel type
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-vpdn'
            _revision = '2009-06-16'

            def __init__(self):
                self.parent = None
                self.cvpdnsystemtunneltype = None
                self.cvpdnsystemdenieduserstotal = None
                self.cvpdnsystemfailedconnreq = None
                self.cvpdnsysteminitialconnreq = None
                self.cvpdnsystemsessiontotal = None
                self.cvpdnsystemsuccessconnreq = None
                self.cvpdnsystemtunneltotal = None

            @property
            def _common_path(self):
                if self.cvpdnsystemtunneltype is None:
                    raise YPYDataValidationError('Key property cvpdnsystemtunneltype is None')

                return '/CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/CISCO-VPDN-MGMT-MIB:cvpdnSystemTable/CISCO-VPDN-MGMT-MIB:cvpdnSystemEntry[CISCO-VPDN-MGMT-MIB:cvpdnSystemTunnelType = ' + str(self.cvpdnsystemtunneltype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cvpdnsystemtunneltype is not None:
                    return True

                if self.cvpdnsystemdenieduserstotal is not None:
                    return True

                if self.cvpdnsystemfailedconnreq is not None:
                    return True

                if self.cvpdnsysteminitialconnreq is not None:
                    return True

                if self.cvpdnsystemsessiontotal is not None:
                    return True

                if self.cvpdnsystemsuccessconnreq is not None:
                    return True

                if self.cvpdnsystemtunneltotal is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
                return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnSystemTable.CvpdnSystemEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/CISCO-VPDN-MGMT-MIB:cvpdnSystemTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvpdnsystementry is not None:
                for child_ref in self.cvpdnsystementry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
            return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnSystemTable']['meta_info']


    class CvpdnTemplateTable(object):
        """
        Table of information about the VPDN templates.  The
        VPDN template is a grouping mechanism that allows
        configuration settings to be shared among multiple VPDN
        groups.  One such setting is a limit on the number of
        active sessions across all VPDN groups associated with
        the template.  The template table allows customers to
        monitor template\-wide information such as tracking the
        allocation of sessions across templates.
        
        .. attribute:: cvpdntemplateentry
        
        	An entry in the table, containing information about a single VPDN template
        	**type**\: list of :py:class:`CvpdnTemplateEntry <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTemplateTable.CvpdnTemplateEntry>`
        
        

        """

        _prefix = 'cisco-vpdn'
        _revision = '2009-06-16'

        def __init__(self):
            self.parent = None
            self.cvpdntemplateentry = YList()
            self.cvpdntemplateentry.parent = self
            self.cvpdntemplateentry.name = 'cvpdntemplateentry'


        class CvpdnTemplateEntry(object):
            """
            An entry in the table, containing information about a
            single VPDN template.
            
            .. attribute:: cvpdntemplatename
            
            	The name of the VPDN template
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cvpdntemplateactivesessions
            
            	The total number of active session in all groups associated with the template
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-vpdn'
            _revision = '2009-06-16'

            def __init__(self):
                self.parent = None
                self.cvpdntemplatename = None
                self.cvpdntemplateactivesessions = None

            @property
            def _common_path(self):
                if self.cvpdntemplatename is None:
                    raise YPYDataValidationError('Key property cvpdntemplatename is None')

                return '/CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/CISCO-VPDN-MGMT-MIB:cvpdnTemplateTable/CISCO-VPDN-MGMT-MIB:cvpdnTemplateEntry[CISCO-VPDN-MGMT-MIB:cvpdnTemplateName = ' + str(self.cvpdntemplatename) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cvpdntemplatename is not None:
                    return True

                if self.cvpdntemplateactivesessions is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
                return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnTemplateTable.CvpdnTemplateEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/CISCO-VPDN-MGMT-MIB:cvpdnTemplateTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvpdntemplateentry is not None:
                for child_ref in self.cvpdntemplateentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
            return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnTemplateTable']['meta_info']


    class CvpdnTunnelAttrTable(object):
        """
        Table of information about the active VPDN tunnels.  An
        entry is added to the table when a new tunnel is initiated
        and removed from the table when the tunnel is terminated.
        
        .. attribute:: cvpdntunnelattrentry
        
        	An entry in the table, containing information about a single active VPDN tunnel
        	**type**\: list of :py:class:`CvpdnTunnelAttrEntry <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable.CvpdnTunnelAttrEntry>`
        
        

        """

        _prefix = 'cisco-vpdn'
        _revision = '2009-06-16'

        def __init__(self):
            self.parent = None
            self.cvpdntunnelattrentry = YList()
            self.cvpdntunnelattrentry.parent = self
            self.cvpdntunnelattrentry.name = 'cvpdntunnelattrentry'


        class CvpdnTunnelAttrEntry(object):
            """
            An entry in the table, containing information about a
            single active VPDN tunnel.
            
            .. attribute:: cvpdnsystemtunneltype
            
            	
            	**type**\: :py:class:`TunnelType_Enum <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.TunnelType_Enum>`
            
            .. attribute:: cvpdntunnelattrtunnelid
            
            	The Tunnel ID of an active VPDN tunnel.  If this end is the instigator of the tunnel, the ID is the TS tunnel ID, otherwise it is the NAS tunnel ID.  Two distinct tunnels with the same tunnel ID may exist, but with different tunnel types
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cvpdntunnelattractivesessions
            
            	The total number of active session currently in the tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdntunnelattrdeniedusers
            
            	A count of the accumulated total of denied users for the tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdntunnelattrlocalinetaddress
            
            	The local IP address of the tunnel.  This IP address is that of the interface at the local end of the tunnel. The type of this address is determined by the value of  cvpdnTunnelAttrLocalInetAddressType
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cvpdntunnelattrlocalinetaddresstype
            
            	Indicates the type of address contained in cvpdnTunnelAttrLocalInetAddress
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cvpdntunnelattrlocalinitconnection
            
            	This object indicates whether the tunnel was originated locally or not.  If it's true, the tunnel was originated locally
            	**type**\: bool
            
            .. attribute:: cvpdntunnelattrlocalipaddress
            
            	The local IP address of the tunnel.  This IP address is that of the interface at the local end of the tunnel
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cvpdntunnelattrlocalname
            
            	The local name of an active VPDN tunnel.  It will be the NAS name of the tunnel if the system serves as the NAS, or the TS name of the tunnel if the system serves as the tunnel server.  Typically, the local name is the configured host name of the system
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cvpdntunnelattrnetworkservicetype
            
            	The type of network service used in the active tunnel
            	**type**\: :py:class:`CvpdnTunnelAttrNetworkServiceType_Enum <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable.CvpdnTunnelAttrEntry.CvpdnTunnelAttrNetworkServiceType_Enum>`
            
            .. attribute:: cvpdntunnelattrorigcause
            
            	The cause which originated an active VPDN tunnel.  The tunnel can be projected via domain name, DNIS, stack group, or L2 Xconnect
            	**type**\: :py:class:`CvpdnTunnelAttrOrigCause_Enum <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable.CvpdnTunnelAttrEntry.CvpdnTunnelAttrOrigCause_Enum>`
            
            .. attribute:: cvpdntunnelattrremoteendpointname
            
            	The remote end point name of an active VPDN tunnel.  This name is either the domain name or the DNIS that this tunnel is projected with
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cvpdntunnelattrremoteinetaddress
            
            	The remote IP address of the tunnel.  This IP address is that of the interface at the remote end of the tunnel. The type of this address is determined by the value of  cvpdnTunnelAttrRemoteInetAddressType
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cvpdntunnelattrremoteinetaddresstype
            
            	Indicates the type of address contained in cvpdnTunnelAttrRemoteInetAddress
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cvpdntunnelattrremoteipaddress
            
            	The remote IP address of the tunnel.  This IP address is that of the interface at the remote end of the tunnel
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cvpdntunnelattrremotename
            
            	The remote name of an active VPDN tunnel.  It will be the tunnel server name of the tunnel if the system is a NAS, or the NAS name of the tunnel if the system serves as the tunnel server
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cvpdntunnelattrremotetunnelid
            
            	The remote Tunnel ID of an active VPDN tunnel.  If this end is the instigator of the tunnel, the ID is the NAS tunnel ID, otherwise it is the TS tunnel ID
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cvpdntunnelattrsoftshut
            
            	A VPDN tunnel can be put into a soft shut state to prevent any new session to be added.  This object specifies whether this tunnel has been soft shut.  If its true, it has been soft shut
            	**type**\: bool
            
            .. attribute:: cvpdntunnelattrsourceinetaddress
            
            	The source IP address of the tunnel.  This IP address is the user configurable IP address for Stack Group Biding Protocol.  The type of this address is determined by the  value of cvpdnTunnelAttrSourceInetAddressType
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cvpdntunnelattrsourceinetaddresstype
            
            	Indicates the type of address contained in cvpdnTunnelAttrSourceInetAddress
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cvpdntunnelattrsourceipaddress
            
            	The source IP address of the tunnel.  This IP address is the user configurable IP address for Stack Group Biding Protocol
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cvpdntunnelattrstate
            
            	The current state of an active VPDN tunnel. Tunnels of type l2f will have states with the 'l2f' prefix. Tunnels of type l2tp will have states with the 'l2tp' prefix. Tunnels of type pptp will have states with the 'pptp' prefix.  Each state code is explained below\:      unknown\:            The current state of the tunnel is                         unknown.      l2fOpening\:         The tunnel has just been initiated                         and is pending for a remote end                         reply to complete the process.      l2fOpenWait\:        This end received a tunnel open                         request from the remote end and is                         waiting for the tunnel to be                         established.      l2fOpen\:            The tunnel is active.      l2fClosing\:         This end received a tunnel close                         request.      l2fCloseWait\:       The tunnel has just been shut down                         and is pending for the remote end                         to reply to complete the process.      l2tpIdle\:           No tunnel is initiated yet.      l2tpWaitCtlReply\:   The tunnel has been initiated and                         is pending for a remote end reply                         to complete the process.      l2tpEstablished\:    The tunnel is active.      l2tpShuttingDown\:   The tunnel is in progress of                         shutting down.      l2tpNoSessionLeft\:  There is no session left in the                         tunnel.      pptpIdle\:           No tunnel is initiated yet.      pptpWaitConnect\:    The tunnel is waiting for a TCP                         connection.      pptpWaitCtlRequest\: The tunnel has been initiated and                         is pending for a remote end                         request.      pptpWaitCtlReply\:   The tunnel has been initiated and                         is pending for a remote end reply.      pptpEstablished\:    The tunnel is active.      pptpWaitStopReply\:  The tunnel is being shut down and                         is pending for a remote end reply.      pptpTerminal\:       The tunnel has been shut down
            	**type**\: :py:class:`CvpdnTunnelAttrState_Enum <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable.CvpdnTunnelAttrEntry.CvpdnTunnelAttrState_Enum>`
            
            

            """

            _prefix = 'cisco-vpdn'
            _revision = '2009-06-16'

            def __init__(self):
                self.parent = None
                self.cvpdnsystemtunneltype = None
                self.cvpdntunnelattrtunnelid = None
                self.cvpdntunnelattractivesessions = None
                self.cvpdntunnelattrdeniedusers = None
                self.cvpdntunnelattrlocalinetaddress = None
                self.cvpdntunnelattrlocalinetaddresstype = None
                self.cvpdntunnelattrlocalinitconnection = None
                self.cvpdntunnelattrlocalipaddress = None
                self.cvpdntunnelattrlocalname = None
                self.cvpdntunnelattrnetworkservicetype = None
                self.cvpdntunnelattrorigcause = None
                self.cvpdntunnelattrremoteendpointname = None
                self.cvpdntunnelattrremoteinetaddress = None
                self.cvpdntunnelattrremoteinetaddresstype = None
                self.cvpdntunnelattrremoteipaddress = None
                self.cvpdntunnelattrremotename = None
                self.cvpdntunnelattrremotetunnelid = None
                self.cvpdntunnelattrsoftshut = None
                self.cvpdntunnelattrsourceinetaddress = None
                self.cvpdntunnelattrsourceinetaddresstype = None
                self.cvpdntunnelattrsourceipaddress = None
                self.cvpdntunnelattrstate = None

            class CvpdnTunnelAttrNetworkServiceType_Enum(Enum):
                """
                CvpdnTunnelAttrNetworkServiceType_Enum

                The type of network service used in the active tunnel.

                """

                IP = 1


                @staticmethod
                def _meta_info():
                    from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
                    return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable.CvpdnTunnelAttrEntry.CvpdnTunnelAttrNetworkServiceType_Enum']


            class CvpdnTunnelAttrOrigCause_Enum(Enum):
                """
                CvpdnTunnelAttrOrigCause_Enum

                The cause which originated an active VPDN tunnel.  The
                tunnel can be projected via domain name, DNIS, stack group,
                or L2 Xconnect.

                """

                DOMAIN = 1

                DNIS = 2

                STACK = 3

                XCONNECT = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
                    return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable.CvpdnTunnelAttrEntry.CvpdnTunnelAttrOrigCause_Enum']


            class CvpdnTunnelAttrState_Enum(Enum):
                """
                CvpdnTunnelAttrState_Enum

                The current state of an active VPDN tunnel.
                Tunnels of type l2f will have states with the 'l2f' prefix.
                Tunnels of type l2tp will have states with the 'l2tp'
                prefix.
                Tunnels of type pptp will have states with the 'pptp'
                prefix.
                
                Each state code is explained below\:
                
                    unknown\:            The current state of the tunnel is
                                        unknown.
                
                    l2fOpening\:         The tunnel has just been initiated
                                        and is pending for a remote end
                                        reply to complete the process.
                
                    l2fOpenWait\:        This end received a tunnel open
                                        request from the remote end and is
                                        waiting for the tunnel to be
                                        established.
                
                    l2fOpen\:            The tunnel is active.
                
                    l2fClosing\:         This end received a tunnel close
                                        request.
                
                    l2fCloseWait\:       The tunnel has just been shut down
                                        and is pending for the remote end
                                        to reply to complete the process.
                
                    l2tpIdle\:           No tunnel is initiated yet.
                
                    l2tpWaitCtlReply\:   The tunnel has been initiated and
                                        is pending for a remote end reply
                                        to complete the process.
                
                    l2tpEstablished\:    The tunnel is active.
                
                    l2tpShuttingDown\:   The tunnel is in progress of
                                        shutting down.
                
                    l2tpNoSessionLeft\:  There is no session left in the
                                        tunnel.
                
                    pptpIdle\:           No tunnel is initiated yet.
                
                    pptpWaitConnect\:    The tunnel is waiting for a TCP
                                        connection.
                
                    pptpWaitCtlRequest\: The tunnel has been initiated and
                                        is pending for a remote end
                                        request.
                
                    pptpWaitCtlReply\:   The tunnel has been initiated and
                                        is pending for a remote end reply.
                
                    pptpEstablished\:    The tunnel is active.
                
                    pptpWaitStopReply\:  The tunnel is being shut down and
                                        is pending for a remote end reply.
                
                    pptpTerminal\:       The tunnel has been shut down.

                """

                UNKNOWN = 1

                L2FOPENING = 2

                L2FOPENWAIT = 3

                L2FOPEN = 4

                L2FCLOSING = 5

                L2FCLOSEWAIT = 6

                L2TPIDLE = 7

                L2TPWAITCTLREPLY = 8

                L2TPESTABLISHED = 9

                L2TPSHUTTINGDOWN = 10

                L2TPNOSESSIONLEFT = 11

                PPTPIDLE = 12

                PPTPWAITCONNECT = 13

                PPTPWAITCTLREQUEST = 14

                PPTPWAITCTLREPLY = 15

                PPTPESTABLISHED = 16

                PPTPWAITSTOPREPLY = 17

                PPTPTERMINAL = 18


                @staticmethod
                def _meta_info():
                    from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
                    return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable.CvpdnTunnelAttrEntry.CvpdnTunnelAttrState_Enum']


            @property
            def _common_path(self):
                if self.cvpdnsystemtunneltype is None:
                    raise YPYDataValidationError('Key property cvpdnsystemtunneltype is None')
                if self.cvpdntunnelattrtunnelid is None:
                    raise YPYDataValidationError('Key property cvpdntunnelattrtunnelid is None')

                return '/CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/CISCO-VPDN-MGMT-MIB:cvpdnTunnelAttrTable/CISCO-VPDN-MGMT-MIB:cvpdnTunnelAttrEntry[CISCO-VPDN-MGMT-MIB:cvpdnSystemTunnelType = ' + str(self.cvpdnsystemtunneltype) + '][CISCO-VPDN-MGMT-MIB:cvpdnTunnelAttrTunnelId = ' + str(self.cvpdntunnelattrtunnelid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cvpdnsystemtunneltype is not None:
                    return True

                if self.cvpdntunnelattrtunnelid is not None:
                    return True

                if self.cvpdntunnelattractivesessions is not None:
                    return True

                if self.cvpdntunnelattrdeniedusers is not None:
                    return True

                if self.cvpdntunnelattrlocalinetaddress is not None:
                    return True

                if self.cvpdntunnelattrlocalinetaddresstype is not None:
                    return True

                if self.cvpdntunnelattrlocalinitconnection is not None:
                    return True

                if self.cvpdntunnelattrlocalipaddress is not None:
                    return True

                if self.cvpdntunnelattrlocalname is not None:
                    return True

                if self.cvpdntunnelattrnetworkservicetype is not None:
                    return True

                if self.cvpdntunnelattrorigcause is not None:
                    return True

                if self.cvpdntunnelattrremoteendpointname is not None:
                    return True

                if self.cvpdntunnelattrremoteinetaddress is not None:
                    return True

                if self.cvpdntunnelattrremoteinetaddresstype is not None:
                    return True

                if self.cvpdntunnelattrremoteipaddress is not None:
                    return True

                if self.cvpdntunnelattrremotename is not None:
                    return True

                if self.cvpdntunnelattrremotetunnelid is not None:
                    return True

                if self.cvpdntunnelattrsoftshut is not None:
                    return True

                if self.cvpdntunnelattrsourceinetaddress is not None:
                    return True

                if self.cvpdntunnelattrsourceinetaddresstype is not None:
                    return True

                if self.cvpdntunnelattrsourceipaddress is not None:
                    return True

                if self.cvpdntunnelattrstate is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
                return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable.CvpdnTunnelAttrEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/CISCO-VPDN-MGMT-MIB:cvpdnTunnelAttrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvpdntunnelattrentry is not None:
                for child_ref in self.cvpdntunnelattrentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
            return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable']['meta_info']


    class CvpdnTunnelSessionTable(object):
        """
        Table of information about individual user sessions
        within the active tunnels.  Entry is added to the table
        when new user session is initiated and be removed from
        the table when the user session is terminated.
        
        .. attribute:: cvpdntunnelsessionentry
        
        	An entry in the table, containing information about a single user session within the tunnel
        	**type**\: list of :py:class:`CvpdnTunnelSessionEntry <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelSessionTable.CvpdnTunnelSessionEntry>`
        
        

        """

        _prefix = 'cisco-vpdn'
        _revision = '2009-06-16'

        def __init__(self):
            self.parent = None
            self.cvpdntunnelsessionentry = YList()
            self.cvpdntunnelsessionentry.parent = self
            self.cvpdntunnelsessionentry.name = 'cvpdntunnelsessionentry'


        class CvpdnTunnelSessionEntry(object):
            """
            An entry in the table, containing information about a
            single user session within the tunnel.
            
            .. attribute:: cvpdntunnelsessionid
            
            	The ID of an active VPDN tunnel user session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdntunneltunnelid
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdntunnelsessionbytesin
            
            	The total number of input bytes through this active user session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdntunnelsessionbytesout
            
            	The total number of output bytes through this active user session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdntunnelsessioncallduration
            
            	This object specifies the call duration of the current active user session in value of system uptime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdntunnelsessiondevicecallerid
            
            	The incoming caller identification of the user.  It is the originating number that called into the device that initiates the user session.  This object can be empty since not all dial device can provide caller ID information
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cvpdntunnelsessiondevicephyid
            
            	The device ID of the physical interface for the user session.  The object is the the interface index which points to the ifTable.  For virtual interface that is not in the ifTable, it will have zero value
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cvpdntunnelsessiondevicetype
            
            	The type of physical devices that this user session is attached to for the local end of the tunnel.  The meaning of each device type is explained below\:      other\:              Any device that has not been                         defined.      asyncInternalModem\: Modem Pool device of an access                         server.      async\:              A regular asynchronous serial                         interface.      sync\:               A regular synchronous serial                         interface.      bchan\:              An ISDN call.      xdsl\:               Future application with xDSL                         devices.      cable\:              Future application with Cable                         modem devices
            	**type**\: :py:class:`CvpdnTunnelSessionDeviceType_Enum <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelSessionTable.CvpdnTunnelSessionEntry.CvpdnTunnelSessionDeviceType_Enum>`
            
            .. attribute:: cvpdntunnelsessionds1channelindex
            
            	The DS1 database channel index if it is associated with this user session.  Only a session over a device of type asyncInternalModem will have a valid value for this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdntunnelsessionds1portindex
            
            	The DS1 database port index if it is associated with this user session.  Only a session with a device of type asyncInternalModem will have a a valid value for this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdntunnelsessionds1slotindex
            
            	The DS1 database slot index if it is associated with this user session.  Only a session with a device of type asyncInternalModem will have a valid value for this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdntunnelsessionmodemcallstartindex
            
            	Arbitrary small integer to distinguish modem calls that occurred at the same time tick.  Only session over device asyncInternalModem will have a valid value for this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdntunnelsessionmodemcallstarttime
            
            	The start time of the current modem call.  Only a session with a  device of type asyncInternalModem will have a valid value for this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdntunnelsessionmodemportindex
            
            	The Modem Pool database port index if it is associated with this user session.  Only a session with a device of type asyncInternalModem will have a valid value for this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdntunnelsessionmodemslotindex
            
            	The Modem Pool database slot index if it is associated with this user session.  Only a session with device of type asyncInternalModem will have a valid value for this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdntunnelsessionmultilink
            
            	This object indicates whether the session is part of a multilink or not
            	**type**\: bool
            
            .. attribute:: cvpdntunnelsessionpacketsin
            
            	The total number of input packets through this active user session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdntunnelsessionpacketsout
            
            	The total number of output packets through this active user session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdntunnelsessionstate
            
            	The current state of an active user session.  Each state code is explained below\:      unknown\:          The current state of the tunnel's                       session is unknown.      opening\:          The user session has just been                       initiated through a tunnel and is                       pending for the remote end reply                       to complete the process.      open\:             The user session is active.      closing\:          The user session has just been                       closed and is pending for the                       remote end reply to complete the                       process.      waitingForTunnel\: The user session is in this state                       when the tunnel which this session                       is going through is still in                       CLOSED state.  It waits for the                       tunnel to become OPEN before the                       session is allow to be fully                       established
            	**type**\: :py:class:`CvpdnTunnelSessionState_Enum <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelSessionTable.CvpdnTunnelSessionEntry.CvpdnTunnelSessionState_Enum>`
            
            .. attribute:: cvpdntunnelsessionusername
            
            	The name of the user of the user session
            	**type**\: str
            
            	**range:** 1..255
            
            

            """

            _prefix = 'cisco-vpdn'
            _revision = '2009-06-16'

            def __init__(self):
                self.parent = None
                self.cvpdntunnelsessionid = None
                self.cvpdntunneltunnelid = None
                self.cvpdntunnelsessionbytesin = None
                self.cvpdntunnelsessionbytesout = None
                self.cvpdntunnelsessioncallduration = None
                self.cvpdntunnelsessiondevicecallerid = None
                self.cvpdntunnelsessiondevicephyid = None
                self.cvpdntunnelsessiondevicetype = None
                self.cvpdntunnelsessionds1channelindex = None
                self.cvpdntunnelsessionds1portindex = None
                self.cvpdntunnelsessionds1slotindex = None
                self.cvpdntunnelsessionmodemcallstartindex = None
                self.cvpdntunnelsessionmodemcallstarttime = None
                self.cvpdntunnelsessionmodemportindex = None
                self.cvpdntunnelsessionmodemslotindex = None
                self.cvpdntunnelsessionmultilink = None
                self.cvpdntunnelsessionpacketsin = None
                self.cvpdntunnelsessionpacketsout = None
                self.cvpdntunnelsessionstate = None
                self.cvpdntunnelsessionusername = None

            class CvpdnTunnelSessionDeviceType_Enum(Enum):
                """
                CvpdnTunnelSessionDeviceType_Enum

                The type of physical devices that this user session
                is attached to for the local end of the tunnel.  The
                meaning of each device type is explained below\:
                
                    other\:              Any device that has not been
                                        defined.
                
                    asyncInternalModem\: Modem Pool device of an access
                                        server.
                
                    async\:              A regular asynchronous serial
                                        interface.
                
                    sync\:               A regular synchronous serial
                                        interface.
                
                    bchan\:              An ISDN call.
                
                    xdsl\:               Future application with xDSL
                                        devices.
                
                    cable\:              Future application with Cable
                                        modem devices.

                """

                OTHER = 1

                ASYNCINTERNALMODEM = 2

                ASYNC = 3

                BCHAN = 4

                SYNC = 5

                VIRTUALACCESS = 6

                XDSL = 7

                CABLE = 8


                @staticmethod
                def _meta_info():
                    from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
                    return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnTunnelSessionTable.CvpdnTunnelSessionEntry.CvpdnTunnelSessionDeviceType_Enum']


            class CvpdnTunnelSessionState_Enum(Enum):
                """
                CvpdnTunnelSessionState_Enum

                The current state of an active user session.  Each state
                code is explained below\:
                
                    unknown\:          The current state of the tunnel's
                                      session is unknown.
                
                    opening\:          The user session has just been
                                      initiated through a tunnel and is
                                      pending for the remote end reply
                                      to complete the process.
                
                    open\:             The user session is active.
                
                    closing\:          The user session has just been
                                      closed and is pending for the
                                      remote end reply to complete the
                                      process.
                
                    waitingForTunnel\: The user session is in this state
                                      when the tunnel which this session
                                      is going through is still in
                                      CLOSED state.  It waits for the
                                      tunnel to become OPEN before the
                                      session is allow to be fully
                                      established.

                """

                UNKNOWN = 1

                OPENING = 2

                OPEN = 3

                CLOSING = 4

                WAITINGFORTUNNEL = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
                    return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnTunnelSessionTable.CvpdnTunnelSessionEntry.CvpdnTunnelSessionState_Enum']


            @property
            def _common_path(self):
                if self.cvpdntunnelsessionid is None:
                    raise YPYDataValidationError('Key property cvpdntunnelsessionid is None')
                if self.cvpdntunneltunnelid is None:
                    raise YPYDataValidationError('Key property cvpdntunneltunnelid is None')

                return '/CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/CISCO-VPDN-MGMT-MIB:cvpdnTunnelSessionTable/CISCO-VPDN-MGMT-MIB:cvpdnTunnelSessionEntry[CISCO-VPDN-MGMT-MIB:cvpdnTunnelSessionId = ' + str(self.cvpdntunnelsessionid) + '][CISCO-VPDN-MGMT-MIB:cvpdnTunnelTunnelId = ' + str(self.cvpdntunneltunnelid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cvpdntunnelsessionid is not None:
                    return True

                if self.cvpdntunneltunnelid is not None:
                    return True

                if self.cvpdntunnelsessionbytesin is not None:
                    return True

                if self.cvpdntunnelsessionbytesout is not None:
                    return True

                if self.cvpdntunnelsessioncallduration is not None:
                    return True

                if self.cvpdntunnelsessiondevicecallerid is not None:
                    return True

                if self.cvpdntunnelsessiondevicephyid is not None:
                    return True

                if self.cvpdntunnelsessiondevicetype is not None:
                    return True

                if self.cvpdntunnelsessionds1channelindex is not None:
                    return True

                if self.cvpdntunnelsessionds1portindex is not None:
                    return True

                if self.cvpdntunnelsessionds1slotindex is not None:
                    return True

                if self.cvpdntunnelsessionmodemcallstartindex is not None:
                    return True

                if self.cvpdntunnelsessionmodemcallstarttime is not None:
                    return True

                if self.cvpdntunnelsessionmodemportindex is not None:
                    return True

                if self.cvpdntunnelsessionmodemslotindex is not None:
                    return True

                if self.cvpdntunnelsessionmultilink is not None:
                    return True

                if self.cvpdntunnelsessionpacketsin is not None:
                    return True

                if self.cvpdntunnelsessionpacketsout is not None:
                    return True

                if self.cvpdntunnelsessionstate is not None:
                    return True

                if self.cvpdntunnelsessionusername is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
                return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnTunnelSessionTable.CvpdnTunnelSessionEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/CISCO-VPDN-MGMT-MIB:cvpdnTunnelSessionTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvpdntunnelsessionentry is not None:
                for child_ref in self.cvpdntunnelsessionentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
            return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnTunnelSessionTable']['meta_info']


    class CvpdnTunnelTable(object):
        """
        Table of information about the active VPDN tunnels.
        
        .. attribute:: cvpdntunnelentry
        
        	An entry in the table, containing information about a single active VPDN tunnel
        	**type**\: list of :py:class:`CvpdnTunnelEntry <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelTable.CvpdnTunnelEntry>`
        
        

        """

        _prefix = 'cisco-vpdn'
        _revision = '2009-06-16'

        def __init__(self):
            self.parent = None
            self.cvpdntunnelentry = YList()
            self.cvpdntunnelentry.parent = self
            self.cvpdntunnelentry.name = 'cvpdntunnelentry'


        class CvpdnTunnelEntry(object):
            """
            An entry in the table, containing information about a
            single active VPDN tunnel.
            
            .. attribute:: cvpdntunneltunnelid
            
            	The Tunnel ID of an active VPDN tunnel.  If it is the instigator of the tunnel, the ID is the HGW/LNS tunnel ID, otherwise it is the NAS/LAC tunnel ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdntunnelactivesessions
            
            	The total number of active session currently in the tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdntunneldeniedusers
            
            	A count of the accumulated total of denied users for the tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdntunnellocalinitconnection
            
            	This object indicates whether the tunnel was generated locally or not
            	**type**\: bool
            
            .. attribute:: cvpdntunnellocalipaddress
            
            	The local IP address of the tunnel.  This IP address is that of the interface at the local end of the tunnel
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cvpdntunnellocalname
            
            	The local name of an active VPDN tunnel.  It will be the NAS/LAC name of the tunnel if the router serves as the NAS/LAC, or the HGW/LNS name of the tunnel if the system serves as the home gateway.  Typically, the local name is the configured host name of the router
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cvpdntunnelnetworkservicetype
            
            	The type of network service used in the active tunnel. For now it is IP only
            	**type**\: :py:class:`CvpdnTunnelNetworkServiceType_Enum <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelTable.CvpdnTunnelEntry.CvpdnTunnelNetworkServiceType_Enum>`
            
            .. attribute:: cvpdntunnelorigcause
            
            	The cause which originated an active VPDN tunnel.  The tunnel can be projected via domain name, DNIS or a stack group (SGBP)
            	**type**\: :py:class:`CvpdnTunnelOrigCause_Enum <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelTable.CvpdnTunnelEntry.CvpdnTunnelOrigCause_Enum>`
            
            .. attribute:: cvpdntunnelremoteendpointname
            
            	The remote end point name of an active VPDN tunnel. This name is either the domain name or the DNIS that this tunnel is projected with
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cvpdntunnelremoteipaddress
            
            	The remote IP address of the tunnel.  This IP address is that of the interface at the remote end of the tunnel
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cvpdntunnelremotename
            
            	The remote name of an active VPDN tunnel.  It will be the home gateway name of the tunnel if the system is a NAS/LAC, or the NAS/LAC name of the tunnel if the system serves as the home gateway
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cvpdntunnelremotetunnelid
            
            	The remote Tunnel ID of an active VPDN tunnel.  If it is the instigator of the tunnel, the ID is the NAS/LAC tunnel ID, otherwise it is the HGW/LNS tunnel ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdntunnelsoftshut
            
            	A VPDN tunnel can be put into a soft shut state to prevent any new user session to be added.  This object specifies whether this tunnel has been soft shut
            	**type**\: bool
            
            .. attribute:: cvpdntunnelsourceipaddress
            
            	The source IP address of the tunnel.  This IP address is the user configurable IP address for Stack Group Biding Protocol (SGBP) via the CLI command\: vpdn source\-ip
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cvpdntunnelstate
            
            	The current state of an active VPDN tunnel.  Each state code is explained below\:         unknown\: The current state of the tunnel is                 unknown.         opening\: The tunnel has just been instigated and                 is pending for a remote end reply to                 complete the process.         open\:    The tunnel is active.         closing\: The tunnel has just been shut down and                 is pending for the remote end to reply                 to complete the process
            	**type**\: :py:class:`CvpdnTunnelState_Enum <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelTable.CvpdnTunnelEntry.CvpdnTunnelState_Enum>`
            
            

            """

            _prefix = 'cisco-vpdn'
            _revision = '2009-06-16'

            def __init__(self):
                self.parent = None
                self.cvpdntunneltunnelid = None
                self.cvpdntunnelactivesessions = None
                self.cvpdntunneldeniedusers = None
                self.cvpdntunnellocalinitconnection = None
                self.cvpdntunnellocalipaddress = None
                self.cvpdntunnellocalname = None
                self.cvpdntunnelnetworkservicetype = None
                self.cvpdntunnelorigcause = None
                self.cvpdntunnelremoteendpointname = None
                self.cvpdntunnelremoteipaddress = None
                self.cvpdntunnelremotename = None
                self.cvpdntunnelremotetunnelid = None
                self.cvpdntunnelsoftshut = None
                self.cvpdntunnelsourceipaddress = None
                self.cvpdntunnelstate = None

            class CvpdnTunnelNetworkServiceType_Enum(Enum):
                """
                CvpdnTunnelNetworkServiceType_Enum

                The type of network service used in the active tunnel.
                For now it is IP only.

                """

                IP = 1


                @staticmethod
                def _meta_info():
                    from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
                    return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnTunnelTable.CvpdnTunnelEntry.CvpdnTunnelNetworkServiceType_Enum']


            class CvpdnTunnelOrigCause_Enum(Enum):
                """
                CvpdnTunnelOrigCause_Enum

                The cause which originated an active VPDN tunnel.  The
                tunnel can be projected via domain name, DNIS or a
                stack group (SGBP).

                """

                DOMAIN = 1

                DNIS = 2

                STACK = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
                    return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnTunnelTable.CvpdnTunnelEntry.CvpdnTunnelOrigCause_Enum']


            class CvpdnTunnelState_Enum(Enum):
                """
                CvpdnTunnelState_Enum

                The current state of an active VPDN tunnel.  Each state
                code is explained below\:
                
                       unknown\: The current state of the tunnel is
                                unknown.
                
                       opening\: The tunnel has just been instigated and
                                is pending for a remote end reply to
                                complete the process.
                
                       open\:    The tunnel is active.
                
                       closing\: The tunnel has just been shut down and
                                is pending for the remote end to reply
                                to complete the process.

                """

                UNKNOWN = 1

                OPENING = 2

                OPEN = 3

                CLOSING = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
                    return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnTunnelTable.CvpdnTunnelEntry.CvpdnTunnelState_Enum']


            @property
            def _common_path(self):
                if self.cvpdntunneltunnelid is None:
                    raise YPYDataValidationError('Key property cvpdntunneltunnelid is None')

                return '/CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/CISCO-VPDN-MGMT-MIB:cvpdnTunnelTable/CISCO-VPDN-MGMT-MIB:cvpdnTunnelEntry[CISCO-VPDN-MGMT-MIB:cvpdnTunnelTunnelId = ' + str(self.cvpdntunneltunnelid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cvpdntunneltunnelid is not None:
                    return True

                if self.cvpdntunnelactivesessions is not None:
                    return True

                if self.cvpdntunneldeniedusers is not None:
                    return True

                if self.cvpdntunnellocalinitconnection is not None:
                    return True

                if self.cvpdntunnellocalipaddress is not None:
                    return True

                if self.cvpdntunnellocalname is not None:
                    return True

                if self.cvpdntunnelnetworkservicetype is not None:
                    return True

                if self.cvpdntunnelorigcause is not None:
                    return True

                if self.cvpdntunnelremoteendpointname is not None:
                    return True

                if self.cvpdntunnelremoteipaddress is not None:
                    return True

                if self.cvpdntunnelremotename is not None:
                    return True

                if self.cvpdntunnelremotetunnelid is not None:
                    return True

                if self.cvpdntunnelsoftshut is not None:
                    return True

                if self.cvpdntunnelsourceipaddress is not None:
                    return True

                if self.cvpdntunnelstate is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
                return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnTunnelTable.CvpdnTunnelEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/CISCO-VPDN-MGMT-MIB:cvpdnTunnelTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvpdntunnelentry is not None:
                for child_ref in self.cvpdntunnelentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
            return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnTunnelTable']['meta_info']


    class CvpdnUserToFailHistInfoTable(object):
        """
        Table of the record of failure objects which can be
        referenced by an user name.  Only a name that has a
        valid item in the Cisco IOS VPDN failure history table
        will yield a valid entry in this table.  The table has
        a maximum size of 50 entries.  Only the newest 50
        entries will be kept in the table.
        
        .. attribute:: cvpdnusertofailhistinfoentry
        
        	An entry in the table, containing failure history relevant to an user name
        	**type**\: list of :py:class:`CvpdnUserToFailHistInfoEntry <ydk.models.vpdn.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnUserToFailHistInfoTable.CvpdnUserToFailHistInfoEntry>`
        
        

        """

        _prefix = 'cisco-vpdn'
        _revision = '2009-06-16'

        def __init__(self):
            self.parent = None
            self.cvpdnusertofailhistinfoentry = YList()
            self.cvpdnusertofailhistinfoentry.parent = self
            self.cvpdnusertofailhistinfoentry.name = 'cvpdnusertofailhistinfoentry'


        class CvpdnUserToFailHistInfoEntry(object):
            """
            An entry in the table, containing failure history
            relevant to an user name.
            
            .. attribute:: cvpdnunametofailhisttunnelid
            
            	The Tunnel ID for this failure entry.  If it is the instigator of the tunnel, the ID is the TS tunnel ID, otherwise it is the NAS tunnel ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnunametofailhistuname
            
            	The user name for this failure entry
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cvpdnunametofailhistcount
            
            	This object is incremented when multiple failures has been experienced by this user on this tunnel.  Seeing a delta of >1 is an indication that the current failure record is the latest of a series of failures that has been recorded
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnunametofailhistdestinetaddr
            
            	The destination IP address of the tunnel in which the failure occurred.  This IP address is that of the interface at the receiver end of the tunnel.  The type  of this address is determined by the value of  cvpdnUnameToFailHistDestInetType
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cvpdnunametofailhistdestinettype
            
            	Indicates the type of address contained in cvpdnUnameToFailHistDestInetAddr
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cvpdnunametofailhistdestip
            
            	The destination IP address of the tunnel in which the failure occurred.  This IP address is that of the interface at the receiver end of the tunnel
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cvpdnunametofailhistfailreason
            
            	The reason of failure for the current failure record
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cvpdnunametofailhistfailtime
            
            	This object specifies the time when the failure is occurred
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnunametofailhistfailtype
            
            	The type of failure for the current failure record.  It comes in a form of a an ASCII string which describes the type of failure
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: cvpdnunametofailhistlocalinitconn
            
            	This object indicates whether the tunnel in which the failure occurred was generated locally or not
            	**type**\: bool
            
            .. attribute:: cvpdnunametofailhistlocalname
            
            	The local name of the VPDN tunnel in which the failure occurred.  It will be the NAS name of the tunnel if the system serves as the NAS, or the TS name of the tunnel if the system serves as the tunnel server.  The local name is the configured host name of the system.  This object can be empty if the failure occurred prior to successful tunnel projection, thus no source name will be available
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cvpdnunametofailhistremotename
            
            	The remote name of the VPDN tunnel in which the failure occurred.  It will be the tunnel server name of the tunnel if the system is a NAS, or the NAS name of the tunnel if the system serves as the tunnel server.  This object can be empty if the failure occurred prior to successful tunnel projection, thus no source name will be available
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cvpdnunametofailhistsourceinetaddr
            
            	The source IP address of the tunnel in which the failure occurred.  This IP address is that of the interface at the instigator end of the tunnel.  The instigator end is the peer which initiates the tunnel estalishment.  The type of this address is determined by the value of cvpdnUnameToFailHistSourceInetType
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cvpdnunametofailhistsourceinettype
            
            	Indicates the type of address contained in cvpdnUnameToFailHistSourceInetAddr
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cvpdnunametofailhistsourceip
            
            	The source IP address of the tunnel in which the failure occurred.  This IP address is that of the interface at the instigator end of the tunnel
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cvpdnunametofailhistuserid
            
            	The user ID of this failure entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-vpdn'
            _revision = '2009-06-16'

            def __init__(self):
                self.parent = None
                self.cvpdnunametofailhisttunnelid = None
                self.cvpdnunametofailhistuname = None
                self.cvpdnunametofailhistcount = None
                self.cvpdnunametofailhistdestinetaddr = None
                self.cvpdnunametofailhistdestinettype = None
                self.cvpdnunametofailhistdestip = None
                self.cvpdnunametofailhistfailreason = None
                self.cvpdnunametofailhistfailtime = None
                self.cvpdnunametofailhistfailtype = None
                self.cvpdnunametofailhistlocalinitconn = None
                self.cvpdnunametofailhistlocalname = None
                self.cvpdnunametofailhistremotename = None
                self.cvpdnunametofailhistsourceinetaddr = None
                self.cvpdnunametofailhistsourceinettype = None
                self.cvpdnunametofailhistsourceip = None
                self.cvpdnunametofailhistuserid = None

            @property
            def _common_path(self):
                if self.cvpdnunametofailhisttunnelid is None:
                    raise YPYDataValidationError('Key property cvpdnunametofailhisttunnelid is None')
                if self.cvpdnunametofailhistuname is None:
                    raise YPYDataValidationError('Key property cvpdnunametofailhistuname is None')

                return '/CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/CISCO-VPDN-MGMT-MIB:cvpdnUserToFailHistInfoTable/CISCO-VPDN-MGMT-MIB:cvpdnUserToFailHistInfoEntry[CISCO-VPDN-MGMT-MIB:cvpdnUnameToFailHistTunnelId = ' + str(self.cvpdnunametofailhisttunnelid) + '][CISCO-VPDN-MGMT-MIB:cvpdnUnameToFailHistUname = ' + str(self.cvpdnunametofailhistuname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cvpdnunametofailhisttunnelid is not None:
                    return True

                if self.cvpdnunametofailhistuname is not None:
                    return True

                if self.cvpdnunametofailhistcount is not None:
                    return True

                if self.cvpdnunametofailhistdestinetaddr is not None:
                    return True

                if self.cvpdnunametofailhistdestinettype is not None:
                    return True

                if self.cvpdnunametofailhistdestip is not None:
                    return True

                if self.cvpdnunametofailhistfailreason is not None:
                    return True

                if self.cvpdnunametofailhistfailtime is not None:
                    return True

                if self.cvpdnunametofailhistfailtype is not None:
                    return True

                if self.cvpdnunametofailhistlocalinitconn is not None:
                    return True

                if self.cvpdnunametofailhistlocalname is not None:
                    return True

                if self.cvpdnunametofailhistremotename is not None:
                    return True

                if self.cvpdnunametofailhistsourceinetaddr is not None:
                    return True

                if self.cvpdnunametofailhistsourceinettype is not None:
                    return True

                if self.cvpdnunametofailhistsourceip is not None:
                    return True

                if self.cvpdnunametofailhistuserid is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
                return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnUserToFailHistInfoTable.CvpdnUserToFailHistInfoEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/CISCO-VPDN-MGMT-MIB:cvpdnUserToFailHistInfoTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cvpdnusertofailhistinfoentry is not None:
                for child_ref in self.cvpdnusertofailhistinfoentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
            return meta._meta_table['CISCOVPDNMGMTMIB.CvpdnUserToFailHistInfoTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.ciscovpdnmgmtmibnotifs is not None and self.ciscovpdnmgmtmibnotifs._has_data():
            return True

        if self.ciscovpdnmgmtmibnotifs is not None and self.ciscovpdnmgmtmibnotifs.is_presence():
            return True

        if self.cvpdnbundlechildtable is not None and self.cvpdnbundlechildtable._has_data():
            return True

        if self.cvpdnbundlechildtable is not None and self.cvpdnbundlechildtable.is_presence():
            return True

        if self.cvpdnbundletable is not None and self.cvpdnbundletable._has_data():
            return True

        if self.cvpdnbundletable is not None and self.cvpdnbundletable.is_presence():
            return True

        if self.cvpdnmultilinkinfo is not None and self.cvpdnmultilinkinfo._has_data():
            return True

        if self.cvpdnmultilinkinfo is not None and self.cvpdnmultilinkinfo.is_presence():
            return True

        if self.cvpdnsessionattrtable is not None and self.cvpdnsessionattrtable._has_data():
            return True

        if self.cvpdnsessionattrtable is not None and self.cvpdnsessionattrtable.is_presence():
            return True

        if self.cvpdnsysteminfo is not None and self.cvpdnsysteminfo._has_data():
            return True

        if self.cvpdnsysteminfo is not None and self.cvpdnsysteminfo.is_presence():
            return True

        if self.cvpdnsystemtable is not None and self.cvpdnsystemtable._has_data():
            return True

        if self.cvpdnsystemtable is not None and self.cvpdnsystemtable.is_presence():
            return True

        if self.cvpdntemplatetable is not None and self.cvpdntemplatetable._has_data():
            return True

        if self.cvpdntemplatetable is not None and self.cvpdntemplatetable.is_presence():
            return True

        if self.cvpdntunnelattrtable is not None and self.cvpdntunnelattrtable._has_data():
            return True

        if self.cvpdntunnelattrtable is not None and self.cvpdntunnelattrtable.is_presence():
            return True

        if self.cvpdntunnelsessiontable is not None and self.cvpdntunnelsessiontable._has_data():
            return True

        if self.cvpdntunnelsessiontable is not None and self.cvpdntunnelsessiontable.is_presence():
            return True

        if self.cvpdntunneltable is not None and self.cvpdntunneltable._has_data():
            return True

        if self.cvpdntunneltable is not None and self.cvpdntunneltable.is_presence():
            return True

        if self.cvpdnusertofailhistinfotable is not None and self.cvpdnusertofailhistinfotable._has_data():
            return True

        if self.cvpdnusertofailhistinfotable is not None and self.cvpdnusertofailhistinfotable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.vpdn._meta import _CISCO_VPDN_MGMT_MIB as meta
        return meta._meta_table['CISCOVPDNMGMTMIB']['meta_info']



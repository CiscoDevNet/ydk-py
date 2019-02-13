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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class EndpointClass(Enum):
    """
    EndpointClass (Enum Class)

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

    .. data:: none = 1

    .. data:: local = 2

    .. data:: ipV4Address = 3

    .. data:: macAddress = 4

    .. data:: magicNumber = 5

    .. data:: phone = 6

    """

    none = Enum.YLeaf(1, "none")

    local = Enum.YLeaf(2, "local")

    ipV4Address = Enum.YLeaf(3, "ipV4Address")

    macAddress = Enum.YLeaf(4, "macAddress")

    magicNumber = Enum.YLeaf(5, "magicNumber")

    phone = Enum.YLeaf(6, "phone")


class TunnelType(Enum):
    """
    TunnelType (Enum Class)

    The tunnel type.  This is the tunnel protocol of a VPDN

    tunnel.

    .. data:: l2f = 1

    .. data:: l2tp = 2

    .. data:: pptp = 3

    """

    l2f = Enum.YLeaf(1, "l2f")

    l2tp = Enum.YLeaf(2, "l2tp")

    pptp = Enum.YLeaf(3, "pptp")



class CISCOVPDNMGMTMIB(Entity):
    """
    
    
    .. attribute:: ciscovpdnmgmtmibnotifs
    
    	
    	**type**\:  :py:class:`CiscoVpdnMgmtMIBNotifs <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CiscoVpdnMgmtMIBNotifs>`
    
    	**config**\: False
    
    .. attribute:: cvpdnsysteminfo
    
    	
    	**type**\:  :py:class:`CvpdnSystemInfo <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnSystemInfo>`
    
    	**config**\: False
    
    .. attribute:: cvpdnmultilinkinfo
    
    	
    	**type**\:  :py:class:`CvpdnMultilinkInfo <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnMultilinkInfo>`
    
    	**config**\: False
    
    .. attribute:: cvpdnsystemtable
    
    	Table of information about the VPDN system for all tunnel types
    	**type**\:  :py:class:`CvpdnSystemTable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnSystemTable>`
    
    	**config**\: False
    
    .. attribute:: cvpdntunneltable
    
    	Table of information about the active VPDN tunnels
    	**type**\:  :py:class:`CvpdnTunnelTable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelTable>`
    
    	**config**\: False
    
    	**status**\: obsolete
    
    .. attribute:: cvpdntunnelattrtable
    
    	Table of information about the active VPDN tunnels.  An entry is added to the table when a new tunnel is initiated and removed from the table when the tunnel is terminated
    	**type**\:  :py:class:`CvpdnTunnelAttrTable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable>`
    
    	**config**\: False
    
    .. attribute:: cvpdntunnelsessiontable
    
    	Table of information about individual user sessions within the active tunnels.  Entry is added to the table when new user session is initiated and be removed from the table when the user session is terminated
    	**type**\:  :py:class:`CvpdnTunnelSessionTable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelSessionTable>`
    
    	**config**\: False
    
    	**status**\: obsolete
    
    .. attribute:: cvpdnsessionattrtable
    
    	Table of information about individual sessions within the active tunnels.  An entry is added to the table when a new session is initiated and removed from the table when the session is terminated
    	**type**\:  :py:class:`CvpdnSessionAttrTable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnSessionAttrTable>`
    
    	**config**\: False
    
    .. attribute:: cvpdnusertofailhistinfotable
    
    	Table of the record of failure objects which can be referenced by an user name.  Only a name that has a valid item in the Cisco IOS VPDN failure history table will yield a valid entry in this table.  The table has a maximum size of 50 entries.  Only the newest 50 entries will be kept in the table
    	**type**\:  :py:class:`CvpdnUserToFailHistInfoTable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnUserToFailHistInfoTable>`
    
    	**config**\: False
    
    .. attribute:: cvpdntemplatetable
    
    	Table of information about the VPDN templates.  The VPDN template is a grouping mechanism that allows configuration settings to be shared among multiple VPDN groups.  One such setting is a limit on the number of active sessions across all VPDN groups associated with the template.  The template table allows customers to monitor template\-wide information such as tracking the allocation of sessions across templates
    	**type**\:  :py:class:`CvpdnTemplateTable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTemplateTable>`
    
    	**config**\: False
    
    .. attribute:: cvpdnbundletable
    
    	Table that describes the multilink PPP attributes of the active VPDN sessions
    	**type**\:  :py:class:`CvpdnBundleTable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnBundleTable>`
    
    	**config**\: False
    
    .. attribute:: cvpdnbundlechildtable
    
    	A table that exposes the containment relationship between a multilink PPP bundle and a VPDN tunnel
    	**type**\:  :py:class:`CvpdnBundleChildTable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnBundleChildTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-VPDN-MGMT-MIB'
    _revision = '2009-06-16'

    def __init__(self):
        super(CISCOVPDNMGMTMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-VPDN-MGMT-MIB"
        self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ciscoVpdnMgmtMIBNotifs", ("ciscovpdnmgmtmibnotifs", CISCOVPDNMGMTMIB.CiscoVpdnMgmtMIBNotifs)), ("cvpdnSystemInfo", ("cvpdnsysteminfo", CISCOVPDNMGMTMIB.CvpdnSystemInfo)), ("cvpdnMultilinkInfo", ("cvpdnmultilinkinfo", CISCOVPDNMGMTMIB.CvpdnMultilinkInfo)), ("cvpdnSystemTable", ("cvpdnsystemtable", CISCOVPDNMGMTMIB.CvpdnSystemTable)), ("cvpdnTunnelTable", ("cvpdntunneltable", CISCOVPDNMGMTMIB.CvpdnTunnelTable)), ("cvpdnTunnelAttrTable", ("cvpdntunnelattrtable", CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable)), ("cvpdnTunnelSessionTable", ("cvpdntunnelsessiontable", CISCOVPDNMGMTMIB.CvpdnTunnelSessionTable)), ("cvpdnSessionAttrTable", ("cvpdnsessionattrtable", CISCOVPDNMGMTMIB.CvpdnSessionAttrTable)), ("cvpdnUserToFailHistInfoTable", ("cvpdnusertofailhistinfotable", CISCOVPDNMGMTMIB.CvpdnUserToFailHistInfoTable)), ("cvpdnTemplateTable", ("cvpdntemplatetable", CISCOVPDNMGMTMIB.CvpdnTemplateTable)), ("cvpdnBundleTable", ("cvpdnbundletable", CISCOVPDNMGMTMIB.CvpdnBundleTable)), ("cvpdnBundleChildTable", ("cvpdnbundlechildtable", CISCOVPDNMGMTMIB.CvpdnBundleChildTable))])
        self._leafs = OrderedDict()

        self.ciscovpdnmgmtmibnotifs = CISCOVPDNMGMTMIB.CiscoVpdnMgmtMIBNotifs()
        self.ciscovpdnmgmtmibnotifs.parent = self
        self._children_name_map["ciscovpdnmgmtmibnotifs"] = "ciscoVpdnMgmtMIBNotifs"

        self.cvpdnsysteminfo = CISCOVPDNMGMTMIB.CvpdnSystemInfo()
        self.cvpdnsysteminfo.parent = self
        self._children_name_map["cvpdnsysteminfo"] = "cvpdnSystemInfo"

        self.cvpdnmultilinkinfo = CISCOVPDNMGMTMIB.CvpdnMultilinkInfo()
        self.cvpdnmultilinkinfo.parent = self
        self._children_name_map["cvpdnmultilinkinfo"] = "cvpdnMultilinkInfo"

        self.cvpdnsystemtable = CISCOVPDNMGMTMIB.CvpdnSystemTable()
        self.cvpdnsystemtable.parent = self
        self._children_name_map["cvpdnsystemtable"] = "cvpdnSystemTable"

        self.cvpdntunneltable = CISCOVPDNMGMTMIB.CvpdnTunnelTable()
        self.cvpdntunneltable.parent = self
        self._children_name_map["cvpdntunneltable"] = "cvpdnTunnelTable"

        self.cvpdntunnelattrtable = CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable()
        self.cvpdntunnelattrtable.parent = self
        self._children_name_map["cvpdntunnelattrtable"] = "cvpdnTunnelAttrTable"

        self.cvpdntunnelsessiontable = CISCOVPDNMGMTMIB.CvpdnTunnelSessionTable()
        self.cvpdntunnelsessiontable.parent = self
        self._children_name_map["cvpdntunnelsessiontable"] = "cvpdnTunnelSessionTable"

        self.cvpdnsessionattrtable = CISCOVPDNMGMTMIB.CvpdnSessionAttrTable()
        self.cvpdnsessionattrtable.parent = self
        self._children_name_map["cvpdnsessionattrtable"] = "cvpdnSessionAttrTable"

        self.cvpdnusertofailhistinfotable = CISCOVPDNMGMTMIB.CvpdnUserToFailHistInfoTable()
        self.cvpdnusertofailhistinfotable.parent = self
        self._children_name_map["cvpdnusertofailhistinfotable"] = "cvpdnUserToFailHistInfoTable"

        self.cvpdntemplatetable = CISCOVPDNMGMTMIB.CvpdnTemplateTable()
        self.cvpdntemplatetable.parent = self
        self._children_name_map["cvpdntemplatetable"] = "cvpdnTemplateTable"

        self.cvpdnbundletable = CISCOVPDNMGMTMIB.CvpdnBundleTable()
        self.cvpdnbundletable.parent = self
        self._children_name_map["cvpdnbundletable"] = "cvpdnBundleTable"

        self.cvpdnbundlechildtable = CISCOVPDNMGMTMIB.CvpdnBundleChildTable()
        self.cvpdnbundlechildtable.parent = self
        self._children_name_map["cvpdnbundlechildtable"] = "cvpdnBundleChildTable"
        self._segment_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOVPDNMGMTMIB, [], name, value)


    class CiscoVpdnMgmtMIBNotifs(Entity):
        """
        
        
        .. attribute:: cvpdnnotifsessionid
        
        	This object contains the local session ID of the L2X session for which this notification has been generated
        	**type**\: int
        
        	**range:** 0..65535
        
        	**config**\: False
        
        .. attribute:: cvpdnnotifsessionevent
        
        	Indicates the event that generated the L2X session notification.  The events are represented as follows\:  up\:     Session has come up.  down\:   Session has gone down.  pwUp\:   Pseudowire associated with this          session has come up.  pwDown\: Pseudowire associated with this          session has gone down
        	**type**\:  :py:class:`CvpdnNotifSessionEvent <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CiscoVpdnMgmtMIBNotifs.CvpdnNotifSessionEvent>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.CiscoVpdnMgmtMIBNotifs, self).__init__()

            self.yang_name = "ciscoVpdnMgmtMIBNotifs"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cvpdnnotifsessionid', (YLeaf(YType.int32, 'cvpdnNotifSessionID'), ['int'])),
                ('cvpdnnotifsessionevent', (YLeaf(YType.enumeration, 'cvpdnNotifSessionEvent'), [('ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CISCOVPDNMGMTMIB', 'CiscoVpdnMgmtMIBNotifs.CvpdnNotifSessionEvent')])),
            ])
            self.cvpdnnotifsessionid = None
            self.cvpdnnotifsessionevent = None
            self._segment_path = lambda: "ciscoVpdnMgmtMIBNotifs"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.CiscoVpdnMgmtMIBNotifs, ['cvpdnnotifsessionid', 'cvpdnnotifsessionevent'], name, value)

        class CvpdnNotifSessionEvent(Enum):
            """
            CvpdnNotifSessionEvent (Enum Class)

            Indicates the event that generated the L2X session

            notification.

            The events are represented as follows\:

            up\:     Session has come up.

            down\:   Session has gone down.

            pwUp\:   Pseudowire associated with this 

                    session has come up.

            pwDown\: Pseudowire associated with this 

                    session has gone down.

            .. data:: up = 1

            .. data:: down = 2

            .. data:: pwUp = 3

            .. data:: pwDown = 4

            """

            up = Enum.YLeaf(1, "up")

            down = Enum.YLeaf(2, "down")

            pwUp = Enum.YLeaf(3, "pwUp")

            pwDown = Enum.YLeaf(4, "pwDown")




    class CvpdnSystemInfo(Entity):
        """
        
        
        .. attribute:: cvpdntunneltotal
        
        	The total number of VPDN tunnels that are currently active within this system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: tunnels
        
        	**status**\: obsolete
        
        .. attribute:: cvpdnsessiontotal
        
        	The total number of active users in all the active VPDN tunnels within this system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: users
        
        	**status**\: obsolete
        
        .. attribute:: cvpdndenieduserstotal
        
        	The total number of denied user attempts to all the active VPDN tunnels within this system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: attempts
        
        	**status**\: obsolete
        
        .. attribute:: cvpdnsystemnotifsessionenabled
        
        	Indicates whether Layer 2 VPN session notifications are enabled
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: cvpdnsystemclearsessions
        
        	Clears all the sessions in a given tunnel type.  When reading this object, the value of 'none' will always be returned.  When setting these values, the following operations will be performed\:      none\: no operation.      all\:  clears all the sessions in all the tunnels.      l2f\:  clears all the L2F sessions.      l2tp\: clears all the L2TP sessions.      pptp\: clears all the PPTP sessions
        	**type**\:  :py:class:`CvpdnSystemClearSessions <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnSystemInfo.CvpdnSystemClearSessions>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.CvpdnSystemInfo, self).__init__()

            self.yang_name = "cvpdnSystemInfo"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cvpdntunneltotal', (YLeaf(YType.uint32, 'cvpdnTunnelTotal'), ['int'])),
                ('cvpdnsessiontotal', (YLeaf(YType.uint32, 'cvpdnSessionTotal'), ['int'])),
                ('cvpdndenieduserstotal', (YLeaf(YType.uint32, 'cvpdnDeniedUsersTotal'), ['int'])),
                ('cvpdnsystemnotifsessionenabled', (YLeaf(YType.boolean, 'cvpdnSystemNotifSessionEnabled'), ['bool'])),
                ('cvpdnsystemclearsessions', (YLeaf(YType.enumeration, 'cvpdnSystemClearSessions'), [('ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CISCOVPDNMGMTMIB', 'CvpdnSystemInfo.CvpdnSystemClearSessions')])),
            ])
            self.cvpdntunneltotal = None
            self.cvpdnsessiontotal = None
            self.cvpdndenieduserstotal = None
            self.cvpdnsystemnotifsessionenabled = None
            self.cvpdnsystemclearsessions = None
            self._segment_path = lambda: "cvpdnSystemInfo"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.CvpdnSystemInfo, ['cvpdntunneltotal', 'cvpdnsessiontotal', 'cvpdndenieduserstotal', 'cvpdnsystemnotifsessionenabled', 'cvpdnsystemclearsessions'], name, value)

        class CvpdnSystemClearSessions(Enum):
            """
            CvpdnSystemClearSessions (Enum Class)

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

            .. data:: none = 1

            .. data:: all = 2

            .. data:: l2f = 3

            .. data:: l2tp = 4

            .. data:: pptp = 5

            """

            none = Enum.YLeaf(1, "none")

            all = Enum.YLeaf(2, "all")

            l2f = Enum.YLeaf(3, "l2f")

            l2tp = Enum.YLeaf(4, "l2tp")

            pptp = Enum.YLeaf(5, "pptp")




    class CvpdnMultilinkInfo(Entity):
        """
        
        
        .. attribute:: cvpdnbundleswithonelink
        
        	The total number of bundles comprised of a single link
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: cvpdnbundleswithtwolinks
        
        	The total number of bundles comprised of two links
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: cvpdnbundleswithmorethantwolinks
        
        	The total number of bundles comprised of more than two links
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: cvpdnbundlelastchanged
        
        	The value of the sysUpTime object when the contents of cvpdnBundleTable last changed
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.CvpdnMultilinkInfo, self).__init__()

            self.yang_name = "cvpdnMultilinkInfo"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cvpdnbundleswithonelink', (YLeaf(YType.uint32, 'cvpdnBundlesWithOneLink'), ['int'])),
                ('cvpdnbundleswithtwolinks', (YLeaf(YType.uint32, 'cvpdnBundlesWithTwoLinks'), ['int'])),
                ('cvpdnbundleswithmorethantwolinks', (YLeaf(YType.uint32, 'cvpdnBundlesWithMoreThanTwoLinks'), ['int'])),
                ('cvpdnbundlelastchanged', (YLeaf(YType.uint32, 'cvpdnBundleLastChanged'), ['int'])),
            ])
            self.cvpdnbundleswithonelink = None
            self.cvpdnbundleswithtwolinks = None
            self.cvpdnbundleswithmorethantwolinks = None
            self.cvpdnbundlelastchanged = None
            self._segment_path = lambda: "cvpdnMultilinkInfo"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.CvpdnMultilinkInfo, ['cvpdnbundleswithonelink', 'cvpdnbundleswithtwolinks', 'cvpdnbundleswithmorethantwolinks', 'cvpdnbundlelastchanged'], name, value)



    class CvpdnSystemTable(Entity):
        """
        Table of information about the VPDN system for all tunnel
        types.
        
        .. attribute:: cvpdnsystementry
        
        	An entry in the table, containing information about a single type of VPDN tunnel
        	**type**\: list of  		 :py:class:`CvpdnSystemEntry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnSystemTable.CvpdnSystemEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.CvpdnSystemTable, self).__init__()

            self.yang_name = "cvpdnSystemTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cvpdnSystemEntry", ("cvpdnsystementry", CISCOVPDNMGMTMIB.CvpdnSystemTable.CvpdnSystemEntry))])
            self._leafs = OrderedDict()

            self.cvpdnsystementry = YList(self)
            self._segment_path = lambda: "cvpdnSystemTable"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.CvpdnSystemTable, [], name, value)


        class CvpdnSystemEntry(Entity):
            """
            An entry in the table, containing information about a
            single type of VPDN tunnel.
            
            .. attribute:: cvpdnsystemtunneltype  (key)
            
            	The tunnel type.  This is the tunnel protocol
            	**type**\:  :py:class:`TunnelType <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.TunnelType>`
            
            	**config**\: False
            
            .. attribute:: cvpdnsystemtunneltotal
            
            	The total number of VPDN tunnels that are currently active of this tunnel type
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: tunnels
            
            .. attribute:: cvpdnsystemsessiontotal
            
            	The total number of active sessions in all the active VPDN tunnels of this tunnel type
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: cvpdnsystemdenieduserstotal
            
            	The total number of denied user attempts to all the VPDN tunnels of this tunnel type since last system re\-initialization
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: attempts
            
            .. attribute:: cvpdnsysteminitialconnreq
            
            	The total number tunnel connection attempts on all the VPDN tunnels of this tunnel type since last system re\-initialization
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: attempts
            
            .. attribute:: cvpdnsystemsuccessconnreq
            
            	The total number tunnel Successful connection attempts in VPDN tunnels of this tunnel type since last system re\-initialization
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: attempts
            
            .. attribute:: cvpdnsystemfailedconnreq
            
            	The total number tunnel Failed connection attempts in VPDN tunnels of this tunnel type since last system re\-initialization
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: attempts
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CISCOVPDNMGMTMIB.CvpdnSystemTable.CvpdnSystemEntry, self).__init__()

                self.yang_name = "cvpdnSystemEntry"
                self.yang_parent_name = "cvpdnSystemTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvpdnsystemtunneltype']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvpdnsystemtunneltype', (YLeaf(YType.enumeration, 'cvpdnSystemTunnelType'), [('ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'TunnelType', '')])),
                    ('cvpdnsystemtunneltotal', (YLeaf(YType.uint32, 'cvpdnSystemTunnelTotal'), ['int'])),
                    ('cvpdnsystemsessiontotal', (YLeaf(YType.uint32, 'cvpdnSystemSessionTotal'), ['int'])),
                    ('cvpdnsystemdenieduserstotal', (YLeaf(YType.uint32, 'cvpdnSystemDeniedUsersTotal'), ['int'])),
                    ('cvpdnsysteminitialconnreq', (YLeaf(YType.uint32, 'cvpdnSystemInitialConnReq'), ['int'])),
                    ('cvpdnsystemsuccessconnreq', (YLeaf(YType.uint32, 'cvpdnSystemSuccessConnReq'), ['int'])),
                    ('cvpdnsystemfailedconnreq', (YLeaf(YType.uint32, 'cvpdnSystemFailedConnReq'), ['int'])),
                ])
                self.cvpdnsystemtunneltype = None
                self.cvpdnsystemtunneltotal = None
                self.cvpdnsystemsessiontotal = None
                self.cvpdnsystemdenieduserstotal = None
                self.cvpdnsysteminitialconnreq = None
                self.cvpdnsystemsuccessconnreq = None
                self.cvpdnsystemfailedconnreq = None
                self._segment_path = lambda: "cvpdnSystemEntry" + "[cvpdnSystemTunnelType='" + str(self.cvpdnsystemtunneltype) + "']"
                self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/cvpdnSystemTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVPDNMGMTMIB.CvpdnSystemTable.CvpdnSystemEntry, ['cvpdnsystemtunneltype', 'cvpdnsystemtunneltotal', 'cvpdnsystemsessiontotal', 'cvpdnsystemdenieduserstotal', 'cvpdnsysteminitialconnreq', 'cvpdnsystemsuccessconnreq', 'cvpdnsystemfailedconnreq'], name, value)




    class CvpdnTunnelTable(Entity):
        """
        Table of information about the active VPDN tunnels.
        
        .. attribute:: cvpdntunnelentry
        
        	An entry in the table, containing information about a single active VPDN tunnel
        	**type**\: list of  		 :py:class:`CvpdnTunnelEntry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelTable.CvpdnTunnelEntry>`
        
        	**config**\: False
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.CvpdnTunnelTable, self).__init__()

            self.yang_name = "cvpdnTunnelTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cvpdnTunnelEntry", ("cvpdntunnelentry", CISCOVPDNMGMTMIB.CvpdnTunnelTable.CvpdnTunnelEntry))])
            self._leafs = OrderedDict()

            self.cvpdntunnelentry = YList(self)
            self._segment_path = lambda: "cvpdnTunnelTable"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.CvpdnTunnelTable, [], name, value)


        class CvpdnTunnelEntry(Entity):
            """
            An entry in the table, containing information about a
            single active VPDN tunnel.
            
            .. attribute:: cvpdntunneltunnelid  (key)
            
            	The Tunnel ID of an active VPDN tunnel.  If it is the instigator of the tunnel, the ID is the HGW/LNS tunnel ID, otherwise it is the NAS/LAC tunnel ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelremotetunnelid
            
            	The remote Tunnel ID of an active VPDN tunnel.  If it is the instigator of the tunnel, the ID is the NAS/LAC tunnel ID, otherwise it is the HGW/LNS tunnel ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnellocalname
            
            	The local name of an active VPDN tunnel.  It will be the NAS/LAC name of the tunnel if the router serves as the NAS/LAC, or the HGW/LNS name of the tunnel if the system serves as the home gateway.  Typically, the local name is the configured host name of the router
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelremotename
            
            	The remote name of an active VPDN tunnel.  It will be the home gateway name of the tunnel if the system is a NAS/LAC, or the NAS/LAC name of the tunnel if the system serves as the home gateway
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelremoteendpointname
            
            	The remote end point name of an active VPDN tunnel. This name is either the domain name or the DNIS that this tunnel is projected with
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnellocalinitconnection
            
            	This object indicates whether the tunnel was generated locally or not
            	**type**\: bool
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelorigcause
            
            	The cause which originated an active VPDN tunnel.  The tunnel can be projected via domain name, DNIS or a stack group (SGBP)
            	**type**\:  :py:class:`CvpdnTunnelOrigCause <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelTable.CvpdnTunnelEntry.CvpdnTunnelOrigCause>`
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelstate
            
            	The current state of an active VPDN tunnel.  Each state code is explained below\:         unknown\: The current state of the tunnel is                 unknown.         opening\: The tunnel has just been instigated and                 is pending for a remote end reply to                 complete the process.         open\:    The tunnel is active.         closing\: The tunnel has just been shut down and                 is pending for the remote end to reply                 to complete the process
            	**type**\:  :py:class:`CvpdnTunnelState <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelTable.CvpdnTunnelEntry.CvpdnTunnelState>`
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelactivesessions
            
            	The total number of active session currently in the tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunneldeniedusers
            
            	A count of the accumulated total of denied users for the tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: calls
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsoftshut
            
            	A VPDN tunnel can be put into a soft shut state to prevent any new user session to be added.  This object specifies whether this tunnel has been soft shut
            	**type**\: bool
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelnetworkservicetype
            
            	The type of network service used in the active tunnel. For now it is IP only
            	**type**\:  :py:class:`CvpdnTunnelNetworkServiceType <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelTable.CvpdnTunnelEntry.CvpdnTunnelNetworkServiceType>`
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnellocalipaddress
            
            	The local IP address of the tunnel.  This IP address is that of the interface at the local end of the tunnel
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsourceipaddress
            
            	The source IP address of the tunnel.  This IP address is the user configurable IP address for Stack Group Biding Protocol (SGBP) via the CLI command\: vpdn source\-ip
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelremoteipaddress
            
            	The remote IP address of the tunnel.  This IP address is that of the interface at the remote end of the tunnel
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CISCOVPDNMGMTMIB.CvpdnTunnelTable.CvpdnTunnelEntry, self).__init__()

                self.yang_name = "cvpdnTunnelEntry"
                self.yang_parent_name = "cvpdnTunnelTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvpdntunneltunnelid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvpdntunneltunnelid', (YLeaf(YType.uint32, 'cvpdnTunnelTunnelId'), ['int'])),
                    ('cvpdntunnelremotetunnelid', (YLeaf(YType.uint32, 'cvpdnTunnelRemoteTunnelId'), ['int'])),
                    ('cvpdntunnellocalname', (YLeaf(YType.str, 'cvpdnTunnelLocalName'), ['str'])),
                    ('cvpdntunnelremotename', (YLeaf(YType.str, 'cvpdnTunnelRemoteName'), ['str'])),
                    ('cvpdntunnelremoteendpointname', (YLeaf(YType.str, 'cvpdnTunnelRemoteEndpointName'), ['str'])),
                    ('cvpdntunnellocalinitconnection', (YLeaf(YType.boolean, 'cvpdnTunnelLocalInitConnection'), ['bool'])),
                    ('cvpdntunnelorigcause', (YLeaf(YType.enumeration, 'cvpdnTunnelOrigCause'), [('ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CISCOVPDNMGMTMIB', 'CvpdnTunnelTable.CvpdnTunnelEntry.CvpdnTunnelOrigCause')])),
                    ('cvpdntunnelstate', (YLeaf(YType.enumeration, 'cvpdnTunnelState'), [('ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CISCOVPDNMGMTMIB', 'CvpdnTunnelTable.CvpdnTunnelEntry.CvpdnTunnelState')])),
                    ('cvpdntunnelactivesessions', (YLeaf(YType.uint32, 'cvpdnTunnelActiveSessions'), ['int'])),
                    ('cvpdntunneldeniedusers', (YLeaf(YType.uint32, 'cvpdnTunnelDeniedUsers'), ['int'])),
                    ('cvpdntunnelsoftshut', (YLeaf(YType.boolean, 'cvpdnTunnelSoftshut'), ['bool'])),
                    ('cvpdntunnelnetworkservicetype', (YLeaf(YType.enumeration, 'cvpdnTunnelNetworkServiceType'), [('ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CISCOVPDNMGMTMIB', 'CvpdnTunnelTable.CvpdnTunnelEntry.CvpdnTunnelNetworkServiceType')])),
                    ('cvpdntunnellocalipaddress', (YLeaf(YType.str, 'cvpdnTunnelLocalIpAddress'), ['str'])),
                    ('cvpdntunnelsourceipaddress', (YLeaf(YType.str, 'cvpdnTunnelSourceIpAddress'), ['str'])),
                    ('cvpdntunnelremoteipaddress', (YLeaf(YType.str, 'cvpdnTunnelRemoteIpAddress'), ['str'])),
                ])
                self.cvpdntunneltunnelid = None
                self.cvpdntunnelremotetunnelid = None
                self.cvpdntunnellocalname = None
                self.cvpdntunnelremotename = None
                self.cvpdntunnelremoteendpointname = None
                self.cvpdntunnellocalinitconnection = None
                self.cvpdntunnelorigcause = None
                self.cvpdntunnelstate = None
                self.cvpdntunnelactivesessions = None
                self.cvpdntunneldeniedusers = None
                self.cvpdntunnelsoftshut = None
                self.cvpdntunnelnetworkservicetype = None
                self.cvpdntunnellocalipaddress = None
                self.cvpdntunnelsourceipaddress = None
                self.cvpdntunnelremoteipaddress = None
                self._segment_path = lambda: "cvpdnTunnelEntry" + "[cvpdnTunnelTunnelId='" + str(self.cvpdntunneltunnelid) + "']"
                self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/cvpdnTunnelTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVPDNMGMTMIB.CvpdnTunnelTable.CvpdnTunnelEntry, ['cvpdntunneltunnelid', 'cvpdntunnelremotetunnelid', 'cvpdntunnellocalname', 'cvpdntunnelremotename', 'cvpdntunnelremoteendpointname', 'cvpdntunnellocalinitconnection', 'cvpdntunnelorigcause', 'cvpdntunnelstate', 'cvpdntunnelactivesessions', 'cvpdntunneldeniedusers', 'cvpdntunnelsoftshut', 'cvpdntunnelnetworkservicetype', 'cvpdntunnellocalipaddress', 'cvpdntunnelsourceipaddress', 'cvpdntunnelremoteipaddress'], name, value)

            class CvpdnTunnelNetworkServiceType(Enum):
                """
                CvpdnTunnelNetworkServiceType (Enum Class)

                The type of network service used in the active tunnel.

                For now it is IP only.

                .. data:: ip = 1

                """

                ip = Enum.YLeaf(1, "ip")


            class CvpdnTunnelOrigCause(Enum):
                """
                CvpdnTunnelOrigCause (Enum Class)

                The cause which originated an active VPDN tunnel.  The

                tunnel can be projected via domain name, DNIS or a

                stack group (SGBP).

                .. data:: domain = 1

                .. data:: dnis = 2

                .. data:: stack = 3

                """

                domain = Enum.YLeaf(1, "domain")

                dnis = Enum.YLeaf(2, "dnis")

                stack = Enum.YLeaf(3, "stack")


            class CvpdnTunnelState(Enum):
                """
                CvpdnTunnelState (Enum Class)

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

                .. data:: unknown = 1

                .. data:: opening = 2

                .. data:: open = 3

                .. data:: closing = 4

                """

                unknown = Enum.YLeaf(1, "unknown")

                opening = Enum.YLeaf(2, "opening")

                open = Enum.YLeaf(3, "open")

                closing = Enum.YLeaf(4, "closing")





    class CvpdnTunnelAttrTable(Entity):
        """
        Table of information about the active VPDN tunnels.  An
        entry is added to the table when a new tunnel is initiated
        and removed from the table when the tunnel is terminated.
        
        .. attribute:: cvpdntunnelattrentry
        
        	An entry in the table, containing information about a single active VPDN tunnel
        	**type**\: list of  		 :py:class:`CvpdnTunnelAttrEntry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable.CvpdnTunnelAttrEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable, self).__init__()

            self.yang_name = "cvpdnTunnelAttrTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cvpdnTunnelAttrEntry", ("cvpdntunnelattrentry", CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable.CvpdnTunnelAttrEntry))])
            self._leafs = OrderedDict()

            self.cvpdntunnelattrentry = YList(self)
            self._segment_path = lambda: "cvpdnTunnelAttrTable"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable, [], name, value)


        class CvpdnTunnelAttrEntry(Entity):
            """
            An entry in the table, containing information about a
            single active VPDN tunnel.
            
            .. attribute:: cvpdnsystemtunneltype  (key)
            
            	
            	**type**\:  :py:class:`TunnelType <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.TunnelType>`
            
            	**config**\: False
            
            .. attribute:: cvpdntunnelattrtunnelid  (key)
            
            	The Tunnel ID of an active VPDN tunnel.  If this end is the instigator of the tunnel, the ID is the TS tunnel ID, otherwise it is the NAS tunnel ID.  Two distinct tunnels with the same tunnel ID may exist, but with different tunnel types
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: cvpdntunnelattrremotetunnelid
            
            	The remote Tunnel ID of an active VPDN tunnel.  If this end is the instigator of the tunnel, the ID is the NAS tunnel ID, otherwise it is the TS tunnel ID
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: cvpdntunnelattrlocalname
            
            	The local name of an active VPDN tunnel.  It will be the NAS name of the tunnel if the system serves as the NAS, or the TS name of the tunnel if the system serves as the tunnel server.  Typically, the local name is the configured host name of the system
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            .. attribute:: cvpdntunnelattrremotename
            
            	The remote name of an active VPDN tunnel.  It will be the tunnel server name of the tunnel if the system is a NAS, or the NAS name of the tunnel if the system serves as the tunnel server
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            .. attribute:: cvpdntunnelattrremoteendpointname
            
            	The remote end point name of an active VPDN tunnel.  This name is either the domain name or the DNIS that this tunnel is projected with
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            .. attribute:: cvpdntunnelattrlocalinitconnection
            
            	This object indicates whether the tunnel was originated locally or not.  If it's true, the tunnel was originated locally
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cvpdntunnelattrorigcause
            
            	The cause which originated an active VPDN tunnel.  The tunnel can be projected via domain name, DNIS, stack group, or L2 Xconnect
            	**type**\:  :py:class:`CvpdnTunnelAttrOrigCause <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable.CvpdnTunnelAttrEntry.CvpdnTunnelAttrOrigCause>`
            
            	**config**\: False
            
            .. attribute:: cvpdntunnelattrstate
            
            	The current state of an active VPDN tunnel. Tunnels of type l2f will have states with the 'l2f' prefix. Tunnels of type l2tp will have states with the 'l2tp' prefix. Tunnels of type pptp will have states with the 'pptp' prefix.  Each state code is explained below\:      unknown\:            The current state of the tunnel is                         unknown.      l2fOpening\:         The tunnel has just been initiated                         and is pending for a remote end                         reply to complete the process.      l2fOpenWait\:        This end received a tunnel open                         request from the remote end and is                         waiting for the tunnel to be                         established.      l2fOpen\:            The tunnel is active.      l2fClosing\:         This end received a tunnel close                         request.      l2fCloseWait\:       The tunnel has just been shut down                         and is pending for the remote end                         to reply to complete the process.      l2tpIdle\:           No tunnel is initiated yet.      l2tpWaitCtlReply\:   The tunnel has been initiated and                         is pending for a remote end reply                         to complete the process.      l2tpEstablished\:    The tunnel is active.      l2tpShuttingDown\:   The tunnel is in progress of                         shutting down.      l2tpNoSessionLeft\:  There is no session left in the                         tunnel.      pptpIdle\:           No tunnel is initiated yet.      pptpWaitConnect\:    The tunnel is waiting for a TCP                         connection.      pptpWaitCtlRequest\: The tunnel has been initiated and                         is pending for a remote end                         request.      pptpWaitCtlReply\:   The tunnel has been initiated and                         is pending for a remote end reply.      pptpEstablished\:    The tunnel is active.      pptpWaitStopReply\:  The tunnel is being shut down and                         is pending for a remote end reply.      pptpTerminal\:       The tunnel has been shut down
            	**type**\:  :py:class:`CvpdnTunnelAttrState <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable.CvpdnTunnelAttrEntry.CvpdnTunnelAttrState>`
            
            	**config**\: False
            
            .. attribute:: cvpdntunnelattractivesessions
            
            	The total number of active session currently in the tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: cvpdntunnelattrdeniedusers
            
            	A count of the accumulated total of denied users for the tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: calls
            
            .. attribute:: cvpdntunnelattrsoftshut
            
            	A VPDN tunnel can be put into a soft shut state to prevent any new session to be added.  This object specifies whether this tunnel has been soft shut.  If its true, it has been soft shut
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cvpdntunnelattrnetworkservicetype
            
            	The type of network service used in the active tunnel
            	**type**\:  :py:class:`CvpdnTunnelAttrNetworkServiceType <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable.CvpdnTunnelAttrEntry.CvpdnTunnelAttrNetworkServiceType>`
            
            	**config**\: False
            
            .. attribute:: cvpdntunnelattrlocalipaddress
            
            	The local IP address of the tunnel.  This IP address is that of the interface at the local end of the tunnel
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: cvpdntunnelattrsourceipaddress
            
            	The source IP address of the tunnel.  This IP address is the user configurable IP address for Stack Group Biding Protocol
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: cvpdntunnelattrremoteipaddress
            
            	The remote IP address of the tunnel.  This IP address is that of the interface at the remote end of the tunnel
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: cvpdntunnelattrlocalinetaddresstype
            
            	Indicates the type of address contained in cvpdnTunnelAttrLocalInetAddress
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cvpdntunnelattrlocalinetaddress
            
            	The local IP address of the tunnel.  This IP address is that of the interface at the local end of the tunnel. The type of this address is determined by the value of  cvpdnTunnelAttrLocalInetAddressType
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cvpdntunnelattrsourceinetaddresstype
            
            	Indicates the type of address contained in cvpdnTunnelAttrSourceInetAddress
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cvpdntunnelattrsourceinetaddress
            
            	The source IP address of the tunnel.  This IP address is the user configurable IP address for Stack Group Biding Protocol.  The type of this address is determined by the  value of cvpdnTunnelAttrSourceInetAddressType
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cvpdntunnelattrremoteinetaddresstype
            
            	Indicates the type of address contained in cvpdnTunnelAttrRemoteInetAddress
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cvpdntunnelattrremoteinetaddress
            
            	The remote IP address of the tunnel.  This IP address is that of the interface at the remote end of the tunnel. The type of this address is determined by the value of  cvpdnTunnelAttrRemoteInetAddressType
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable.CvpdnTunnelAttrEntry, self).__init__()

                self.yang_name = "cvpdnTunnelAttrEntry"
                self.yang_parent_name = "cvpdnTunnelAttrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvpdnsystemtunneltype','cvpdntunnelattrtunnelid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvpdnsystemtunneltype', (YLeaf(YType.enumeration, 'cvpdnSystemTunnelType'), [('ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'TunnelType', '')])),
                    ('cvpdntunnelattrtunnelid', (YLeaf(YType.int32, 'cvpdnTunnelAttrTunnelId'), ['int'])),
                    ('cvpdntunnelattrremotetunnelid', (YLeaf(YType.int32, 'cvpdnTunnelAttrRemoteTunnelId'), ['int'])),
                    ('cvpdntunnelattrlocalname', (YLeaf(YType.str, 'cvpdnTunnelAttrLocalName'), ['str'])),
                    ('cvpdntunnelattrremotename', (YLeaf(YType.str, 'cvpdnTunnelAttrRemoteName'), ['str'])),
                    ('cvpdntunnelattrremoteendpointname', (YLeaf(YType.str, 'cvpdnTunnelAttrRemoteEndpointName'), ['str'])),
                    ('cvpdntunnelattrlocalinitconnection', (YLeaf(YType.boolean, 'cvpdnTunnelAttrLocalInitConnection'), ['bool'])),
                    ('cvpdntunnelattrorigcause', (YLeaf(YType.enumeration, 'cvpdnTunnelAttrOrigCause'), [('ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CISCOVPDNMGMTMIB', 'CvpdnTunnelAttrTable.CvpdnTunnelAttrEntry.CvpdnTunnelAttrOrigCause')])),
                    ('cvpdntunnelattrstate', (YLeaf(YType.enumeration, 'cvpdnTunnelAttrState'), [('ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CISCOVPDNMGMTMIB', 'CvpdnTunnelAttrTable.CvpdnTunnelAttrEntry.CvpdnTunnelAttrState')])),
                    ('cvpdntunnelattractivesessions', (YLeaf(YType.uint32, 'cvpdnTunnelAttrActiveSessions'), ['int'])),
                    ('cvpdntunnelattrdeniedusers', (YLeaf(YType.uint32, 'cvpdnTunnelAttrDeniedUsers'), ['int'])),
                    ('cvpdntunnelattrsoftshut', (YLeaf(YType.boolean, 'cvpdnTunnelAttrSoftshut'), ['bool'])),
                    ('cvpdntunnelattrnetworkservicetype', (YLeaf(YType.enumeration, 'cvpdnTunnelAttrNetworkServiceType'), [('ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CISCOVPDNMGMTMIB', 'CvpdnTunnelAttrTable.CvpdnTunnelAttrEntry.CvpdnTunnelAttrNetworkServiceType')])),
                    ('cvpdntunnelattrlocalipaddress', (YLeaf(YType.str, 'cvpdnTunnelAttrLocalIpAddress'), ['str'])),
                    ('cvpdntunnelattrsourceipaddress', (YLeaf(YType.str, 'cvpdnTunnelAttrSourceIpAddress'), ['str'])),
                    ('cvpdntunnelattrremoteipaddress', (YLeaf(YType.str, 'cvpdnTunnelAttrRemoteIpAddress'), ['str'])),
                    ('cvpdntunnelattrlocalinetaddresstype', (YLeaf(YType.enumeration, 'cvpdnTunnelAttrLocalInetAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cvpdntunnelattrlocalinetaddress', (YLeaf(YType.str, 'cvpdnTunnelAttrLocalInetAddress'), ['str'])),
                    ('cvpdntunnelattrsourceinetaddresstype', (YLeaf(YType.enumeration, 'cvpdnTunnelAttrSourceInetAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cvpdntunnelattrsourceinetaddress', (YLeaf(YType.str, 'cvpdnTunnelAttrSourceInetAddress'), ['str'])),
                    ('cvpdntunnelattrremoteinetaddresstype', (YLeaf(YType.enumeration, 'cvpdnTunnelAttrRemoteInetAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cvpdntunnelattrremoteinetaddress', (YLeaf(YType.str, 'cvpdnTunnelAttrRemoteInetAddress'), ['str'])),
                ])
                self.cvpdnsystemtunneltype = None
                self.cvpdntunnelattrtunnelid = None
                self.cvpdntunnelattrremotetunnelid = None
                self.cvpdntunnelattrlocalname = None
                self.cvpdntunnelattrremotename = None
                self.cvpdntunnelattrremoteendpointname = None
                self.cvpdntunnelattrlocalinitconnection = None
                self.cvpdntunnelattrorigcause = None
                self.cvpdntunnelattrstate = None
                self.cvpdntunnelattractivesessions = None
                self.cvpdntunnelattrdeniedusers = None
                self.cvpdntunnelattrsoftshut = None
                self.cvpdntunnelattrnetworkservicetype = None
                self.cvpdntunnelattrlocalipaddress = None
                self.cvpdntunnelattrsourceipaddress = None
                self.cvpdntunnelattrremoteipaddress = None
                self.cvpdntunnelattrlocalinetaddresstype = None
                self.cvpdntunnelattrlocalinetaddress = None
                self.cvpdntunnelattrsourceinetaddresstype = None
                self.cvpdntunnelattrsourceinetaddress = None
                self.cvpdntunnelattrremoteinetaddresstype = None
                self.cvpdntunnelattrremoteinetaddress = None
                self._segment_path = lambda: "cvpdnTunnelAttrEntry" + "[cvpdnSystemTunnelType='" + str(self.cvpdnsystemtunneltype) + "']" + "[cvpdnTunnelAttrTunnelId='" + str(self.cvpdntunnelattrtunnelid) + "']"
                self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/cvpdnTunnelAttrTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable.CvpdnTunnelAttrEntry, ['cvpdnsystemtunneltype', 'cvpdntunnelattrtunnelid', 'cvpdntunnelattrremotetunnelid', 'cvpdntunnelattrlocalname', 'cvpdntunnelattrremotename', 'cvpdntunnelattrremoteendpointname', 'cvpdntunnelattrlocalinitconnection', 'cvpdntunnelattrorigcause', 'cvpdntunnelattrstate', 'cvpdntunnelattractivesessions', 'cvpdntunnelattrdeniedusers', 'cvpdntunnelattrsoftshut', 'cvpdntunnelattrnetworkservicetype', 'cvpdntunnelattrlocalipaddress', 'cvpdntunnelattrsourceipaddress', 'cvpdntunnelattrremoteipaddress', 'cvpdntunnelattrlocalinetaddresstype', 'cvpdntunnelattrlocalinetaddress', 'cvpdntunnelattrsourceinetaddresstype', 'cvpdntunnelattrsourceinetaddress', 'cvpdntunnelattrremoteinetaddresstype', 'cvpdntunnelattrremoteinetaddress'], name, value)

            class CvpdnTunnelAttrNetworkServiceType(Enum):
                """
                CvpdnTunnelAttrNetworkServiceType (Enum Class)

                The type of network service used in the active tunnel.

                .. data:: ip = 1

                """

                ip = Enum.YLeaf(1, "ip")


            class CvpdnTunnelAttrOrigCause(Enum):
                """
                CvpdnTunnelAttrOrigCause (Enum Class)

                The cause which originated an active VPDN tunnel.  The

                tunnel can be projected via domain name, DNIS, stack group,

                or L2 Xconnect.

                .. data:: domain = 1

                .. data:: dnis = 2

                .. data:: stack = 3

                .. data:: xconnect = 4

                """

                domain = Enum.YLeaf(1, "domain")

                dnis = Enum.YLeaf(2, "dnis")

                stack = Enum.YLeaf(3, "stack")

                xconnect = Enum.YLeaf(4, "xconnect")


            class CvpdnTunnelAttrState(Enum):
                """
                CvpdnTunnelAttrState (Enum Class)

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

                .. data:: unknown = 1

                .. data:: l2fOpening = 2

                .. data:: l2fOpenWait = 3

                .. data:: l2fOpen = 4

                .. data:: l2fClosing = 5

                .. data:: l2fCloseWait = 6

                .. data:: l2tpIdle = 7

                .. data:: l2tpWaitCtlReply = 8

                .. data:: l2tpEstablished = 9

                .. data:: l2tpShuttingDown = 10

                .. data:: l2tpNoSessionLeft = 11

                .. data:: pptpIdle = 12

                .. data:: pptpWaitConnect = 13

                .. data:: pptpWaitCtlRequest = 14

                .. data:: pptpWaitCtlReply = 15

                .. data:: pptpEstablished = 16

                .. data:: pptpWaitStopReply = 17

                .. data:: pptpTerminal = 18

                """

                unknown = Enum.YLeaf(1, "unknown")

                l2fOpening = Enum.YLeaf(2, "l2fOpening")

                l2fOpenWait = Enum.YLeaf(3, "l2fOpenWait")

                l2fOpen = Enum.YLeaf(4, "l2fOpen")

                l2fClosing = Enum.YLeaf(5, "l2fClosing")

                l2fCloseWait = Enum.YLeaf(6, "l2fCloseWait")

                l2tpIdle = Enum.YLeaf(7, "l2tpIdle")

                l2tpWaitCtlReply = Enum.YLeaf(8, "l2tpWaitCtlReply")

                l2tpEstablished = Enum.YLeaf(9, "l2tpEstablished")

                l2tpShuttingDown = Enum.YLeaf(10, "l2tpShuttingDown")

                l2tpNoSessionLeft = Enum.YLeaf(11, "l2tpNoSessionLeft")

                pptpIdle = Enum.YLeaf(12, "pptpIdle")

                pptpWaitConnect = Enum.YLeaf(13, "pptpWaitConnect")

                pptpWaitCtlRequest = Enum.YLeaf(14, "pptpWaitCtlRequest")

                pptpWaitCtlReply = Enum.YLeaf(15, "pptpWaitCtlReply")

                pptpEstablished = Enum.YLeaf(16, "pptpEstablished")

                pptpWaitStopReply = Enum.YLeaf(17, "pptpWaitStopReply")

                pptpTerminal = Enum.YLeaf(18, "pptpTerminal")





    class CvpdnTunnelSessionTable(Entity):
        """
        Table of information about individual user sessions
        within the active tunnels.  Entry is added to the table
        when new user session is initiated and be removed from
        the table when the user session is terminated.
        
        .. attribute:: cvpdntunnelsessionentry
        
        	An entry in the table, containing information about a single user session within the tunnel
        	**type**\: list of  		 :py:class:`CvpdnTunnelSessionEntry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelSessionTable.CvpdnTunnelSessionEntry>`
        
        	**config**\: False
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.CvpdnTunnelSessionTable, self).__init__()

            self.yang_name = "cvpdnTunnelSessionTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cvpdnTunnelSessionEntry", ("cvpdntunnelsessionentry", CISCOVPDNMGMTMIB.CvpdnTunnelSessionTable.CvpdnTunnelSessionEntry))])
            self._leafs = OrderedDict()

            self.cvpdntunnelsessionentry = YList(self)
            self._segment_path = lambda: "cvpdnTunnelSessionTable"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.CvpdnTunnelSessionTable, [], name, value)


        class CvpdnTunnelSessionEntry(Entity):
            """
            An entry in the table, containing information about a
            single user session within the tunnel.
            
            .. attribute:: cvpdntunneltunnelid  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cvpdntunneltunnelid <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelTable.CvpdnTunnelEntry>`
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionid  (key)
            
            	The ID of an active VPDN tunnel user session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionusername
            
            	The name of the user of the user session
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionstate
            
            	The current state of an active user session.  Each state code is explained below\:      unknown\:          The current state of the tunnel's                       session is unknown.      opening\:          The user session has just been                       initiated through a tunnel and is                       pending for the remote end reply                       to complete the process.      open\:             The user session is active.      closing\:          The user session has just been                       closed and is pending for the                       remote end reply to complete the                       process.      waitingForTunnel\: The user session is in this state                       when the tunnel which this session                       is going through is still in                       CLOSED state.  It waits for the                       tunnel to become OPEN before the                       session is allow to be fully                       established
            	**type**\:  :py:class:`CvpdnTunnelSessionState <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelSessionTable.CvpdnTunnelSessionEntry.CvpdnTunnelSessionState>`
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessioncallduration
            
            	This object specifies the call duration of the current active user session in value of system uptime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionpacketsout
            
            	The total number of output packets through this active user session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: packets
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionbytesout
            
            	The total number of output bytes through this active user session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionpacketsin
            
            	The total number of input packets through this active user session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: packets
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionbytesin
            
            	The total number of input bytes through this active user session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessiondevicetype
            
            	The type of physical devices that this user session is attached to for the local end of the tunnel.  The meaning of each device type is explained below\:      other\:              Any device that has not been                         defined.      asyncInternalModem\: Modem Pool device of an access                         server.      async\:              A regular asynchronous serial                         interface.      sync\:               A regular synchronous serial                         interface.      bchan\:              An ISDN call.      xdsl\:               Future application with xDSL                         devices.      cable\:              Future application with Cable                         modem devices
            	**type**\:  :py:class:`CvpdnTunnelSessionDeviceType <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelSessionTable.CvpdnTunnelSessionEntry.CvpdnTunnelSessionDeviceType>`
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessiondevicecallerid
            
            	The incoming caller identification of the user.  It is the originating number that called into the device that initiates the user session.  This object can be empty since not all dial device can provide caller ID information
            	**type**\: str
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessiondevicephyid
            
            	The device ID of the physical interface for the user session.  The object is the the interface index which points to the ifTable.  For virtual interface that is not in the ifTable, it will have zero value
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionmultilink
            
            	This object indicates whether the session is part of a multilink or not
            	**type**\: bool
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionmodemslotindex
            
            	The Modem Pool database slot index if it is associated with this user session.  Only a session with device of type asyncInternalModem will have a valid value for this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionmodemportindex
            
            	The Modem Pool database port index if it is associated with this user session.  Only a session with a device of type asyncInternalModem will have a valid value for this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionds1slotindex
            
            	The DS1 database slot index if it is associated with this user session.  Only a session with a device of type asyncInternalModem will have a valid value for this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionds1portindex
            
            	The DS1 database port index if it is associated with this user session.  Only a session with a device of type asyncInternalModem will have a a valid value for this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionds1channelindex
            
            	The DS1 database channel index if it is associated with this user session.  Only a session over a device of type asyncInternalModem will have a valid value for this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionmodemcallstarttime
            
            	The start time of the current modem call.  Only a session with a  device of type asyncInternalModem will have a valid value for this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionmodemcallstartindex
            
            	Arbitrary small integer to distinguish modem calls that occurred at the same time tick.  Only session over device asyncInternalModem will have a valid value for this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CISCOVPDNMGMTMIB.CvpdnTunnelSessionTable.CvpdnTunnelSessionEntry, self).__init__()

                self.yang_name = "cvpdnTunnelSessionEntry"
                self.yang_parent_name = "cvpdnTunnelSessionTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvpdntunneltunnelid','cvpdntunnelsessionid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvpdntunneltunnelid', (YLeaf(YType.str, 'cvpdnTunnelTunnelId'), ['int'])),
                    ('cvpdntunnelsessionid', (YLeaf(YType.uint32, 'cvpdnTunnelSessionId'), ['int'])),
                    ('cvpdntunnelsessionusername', (YLeaf(YType.str, 'cvpdnTunnelSessionUserName'), ['str'])),
                    ('cvpdntunnelsessionstate', (YLeaf(YType.enumeration, 'cvpdnTunnelSessionState'), [('ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CISCOVPDNMGMTMIB', 'CvpdnTunnelSessionTable.CvpdnTunnelSessionEntry.CvpdnTunnelSessionState')])),
                    ('cvpdntunnelsessioncallduration', (YLeaf(YType.uint32, 'cvpdnTunnelSessionCallDuration'), ['int'])),
                    ('cvpdntunnelsessionpacketsout', (YLeaf(YType.uint32, 'cvpdnTunnelSessionPacketsOut'), ['int'])),
                    ('cvpdntunnelsessionbytesout', (YLeaf(YType.uint32, 'cvpdnTunnelSessionBytesOut'), ['int'])),
                    ('cvpdntunnelsessionpacketsin', (YLeaf(YType.uint32, 'cvpdnTunnelSessionPacketsIn'), ['int'])),
                    ('cvpdntunnelsessionbytesin', (YLeaf(YType.uint32, 'cvpdnTunnelSessionBytesIn'), ['int'])),
                    ('cvpdntunnelsessiondevicetype', (YLeaf(YType.enumeration, 'cvpdnTunnelSessionDeviceType'), [('ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CISCOVPDNMGMTMIB', 'CvpdnTunnelSessionTable.CvpdnTunnelSessionEntry.CvpdnTunnelSessionDeviceType')])),
                    ('cvpdntunnelsessiondevicecallerid', (YLeaf(YType.str, 'cvpdnTunnelSessionDeviceCallerId'), ['str'])),
                    ('cvpdntunnelsessiondevicephyid', (YLeaf(YType.int32, 'cvpdnTunnelSessionDevicePhyId'), ['int'])),
                    ('cvpdntunnelsessionmultilink', (YLeaf(YType.boolean, 'cvpdnTunnelSessionMultilink'), ['bool'])),
                    ('cvpdntunnelsessionmodemslotindex', (YLeaf(YType.uint32, 'cvpdnTunnelSessionModemSlotIndex'), ['int'])),
                    ('cvpdntunnelsessionmodemportindex', (YLeaf(YType.uint32, 'cvpdnTunnelSessionModemPortIndex'), ['int'])),
                    ('cvpdntunnelsessionds1slotindex', (YLeaf(YType.uint32, 'cvpdnTunnelSessionDS1SlotIndex'), ['int'])),
                    ('cvpdntunnelsessionds1portindex', (YLeaf(YType.uint32, 'cvpdnTunnelSessionDS1PortIndex'), ['int'])),
                    ('cvpdntunnelsessionds1channelindex', (YLeaf(YType.uint32, 'cvpdnTunnelSessionDS1ChannelIndex'), ['int'])),
                    ('cvpdntunnelsessionmodemcallstarttime', (YLeaf(YType.uint32, 'cvpdnTunnelSessionModemCallStartTime'), ['int'])),
                    ('cvpdntunnelsessionmodemcallstartindex', (YLeaf(YType.uint32, 'cvpdnTunnelSessionModemCallStartIndex'), ['int'])),
                ])
                self.cvpdntunneltunnelid = None
                self.cvpdntunnelsessionid = None
                self.cvpdntunnelsessionusername = None
                self.cvpdntunnelsessionstate = None
                self.cvpdntunnelsessioncallduration = None
                self.cvpdntunnelsessionpacketsout = None
                self.cvpdntunnelsessionbytesout = None
                self.cvpdntunnelsessionpacketsin = None
                self.cvpdntunnelsessionbytesin = None
                self.cvpdntunnelsessiondevicetype = None
                self.cvpdntunnelsessiondevicecallerid = None
                self.cvpdntunnelsessiondevicephyid = None
                self.cvpdntunnelsessionmultilink = None
                self.cvpdntunnelsessionmodemslotindex = None
                self.cvpdntunnelsessionmodemportindex = None
                self.cvpdntunnelsessionds1slotindex = None
                self.cvpdntunnelsessionds1portindex = None
                self.cvpdntunnelsessionds1channelindex = None
                self.cvpdntunnelsessionmodemcallstarttime = None
                self.cvpdntunnelsessionmodemcallstartindex = None
                self._segment_path = lambda: "cvpdnTunnelSessionEntry" + "[cvpdnTunnelTunnelId='" + str(self.cvpdntunneltunnelid) + "']" + "[cvpdnTunnelSessionId='" + str(self.cvpdntunnelsessionid) + "']"
                self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/cvpdnTunnelSessionTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVPDNMGMTMIB.CvpdnTunnelSessionTable.CvpdnTunnelSessionEntry, ['cvpdntunneltunnelid', 'cvpdntunnelsessionid', 'cvpdntunnelsessionusername', 'cvpdntunnelsessionstate', 'cvpdntunnelsessioncallduration', 'cvpdntunnelsessionpacketsout', 'cvpdntunnelsessionbytesout', 'cvpdntunnelsessionpacketsin', 'cvpdntunnelsessionbytesin', 'cvpdntunnelsessiondevicetype', 'cvpdntunnelsessiondevicecallerid', 'cvpdntunnelsessiondevicephyid', 'cvpdntunnelsessionmultilink', 'cvpdntunnelsessionmodemslotindex', 'cvpdntunnelsessionmodemportindex', 'cvpdntunnelsessionds1slotindex', 'cvpdntunnelsessionds1portindex', 'cvpdntunnelsessionds1channelindex', 'cvpdntunnelsessionmodemcallstarttime', 'cvpdntunnelsessionmodemcallstartindex'], name, value)

            class CvpdnTunnelSessionDeviceType(Enum):
                """
                CvpdnTunnelSessionDeviceType (Enum Class)

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

                .. data:: other = 1

                .. data:: asyncInternalModem = 2

                .. data:: async = 3

                .. data:: bchan = 4

                .. data:: sync = 5

                .. data:: virtualAccess = 6

                .. data:: xdsl = 7

                .. data:: cable = 8

                """

                other = Enum.YLeaf(1, "other")

                asyncInternalModem = Enum.YLeaf(2, "asyncInternalModem")

                async = Enum.YLeaf(3, "async")

                bchan = Enum.YLeaf(4, "bchan")

                sync = Enum.YLeaf(5, "sync")

                virtualAccess = Enum.YLeaf(6, "virtualAccess")

                xdsl = Enum.YLeaf(7, "xdsl")

                cable = Enum.YLeaf(8, "cable")


            class CvpdnTunnelSessionState(Enum):
                """
                CvpdnTunnelSessionState (Enum Class)

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

                .. data:: unknown = 1

                .. data:: opening = 2

                .. data:: open = 3

                .. data:: closing = 4

                .. data:: waitingForTunnel = 5

                """

                unknown = Enum.YLeaf(1, "unknown")

                opening = Enum.YLeaf(2, "opening")

                open = Enum.YLeaf(3, "open")

                closing = Enum.YLeaf(4, "closing")

                waitingForTunnel = Enum.YLeaf(5, "waitingForTunnel")





    class CvpdnSessionAttrTable(Entity):
        """
        Table of information about individual sessions within the
        active tunnels.  An entry is added to the table when a new
        session is initiated and removed from the table when the
        session is terminated.
        
        .. attribute:: cvpdnsessionattrentry
        
        	An entry in the table, containing information about a single session within the tunnel
        	**type**\: list of  		 :py:class:`CvpdnSessionAttrEntry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnSessionAttrTable.CvpdnSessionAttrEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.CvpdnSessionAttrTable, self).__init__()

            self.yang_name = "cvpdnSessionAttrTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cvpdnSessionAttrEntry", ("cvpdnsessionattrentry", CISCOVPDNMGMTMIB.CvpdnSessionAttrTable.CvpdnSessionAttrEntry))])
            self._leafs = OrderedDict()

            self.cvpdnsessionattrentry = YList(self)
            self._segment_path = lambda: "cvpdnSessionAttrTable"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.CvpdnSessionAttrTable, [], name, value)


        class CvpdnSessionAttrEntry(Entity):
            """
            An entry in the table, containing information about a
            single session within the tunnel.
            
            .. attribute:: cvpdnsystemtunneltype  (key)
            
            	
            	**type**\:  :py:class:`TunnelType <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.TunnelType>`
            
            	**config**\: False
            
            .. attribute:: cvpdntunnelattrtunnelid  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`cvpdntunnelattrtunnelid <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTunnelAttrTable.CvpdnTunnelAttrEntry>`
            
            	**config**\: False
            
            .. attribute:: cvpdnsessionattrsessionid  (key)
            
            	The ID of an active VPDN session
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: cvpdnsessionattrusername
            
            	The name of the user of the session
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            .. attribute:: cvpdnsessionattrstate
            
            	The current state of a tunnel session. L2F tunnel sessions will have states with the 'l2f' prefix. L2TP tunnel sessions will have states with the 'l2tp' prefix.  Each state code is explained below\:      unknown\:             The current state of the tunnel's                          session is unknown.      l2fOpening\:          The session has just been                          initiated through a tunnel and is                          pending for the remote end reply                          to complete the process.      l2fOpen\:             The session is active.      l2fCloseWait\:        The session has just been closed                          and is pending for the remote end                          reply to complete the process.      l2fWaitingForTunnel\: The session is in this state when                          the tunnel which this session is                          going through is still in CLOSED                          state.  It waits for the tunnel to                          become OPEN before the session is                          allowed to be fully established.      l2tpIdle\:            No session is initiated yet.      l2tpWaitingTunnel\:   The session is waiting for the                          tunnel to be established.      l2tpWaitReply\:       The session has been initiated and                          is pending for the remote end                          reply to complete the process.      l2tpWaitConnect\:     This end has acknowledged a                          connection request and is waiting                          for the remote end to connect.      l2tpEstablished\:     The session is active.      l2tpShuttingDown\:    The session is in progress of                          shutting down.      pptpWaitVAccess\:     The session is waiting for the                          creation of a virtual access                          interface.      pptpPacEstablished\:  The session is active.      pptpWaitTunnel\:      The session is waiting for the                          tunnel to be established.      pptpWaitOCRP\:        The session has been initiated and                          is pending for the remote end                          reply to complete the process.      pptpPnsEstablished\:  The session is active.      pptpWaitCallDisc\:    Session shutdown is in progress
            	**type**\:  :py:class:`CvpdnSessionAttrState <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnSessionAttrTable.CvpdnSessionAttrEntry.CvpdnSessionAttrState>`
            
            	**config**\: False
            
            .. attribute:: cvpdnsessionattrcallduration
            
            	This object specifies the call duration of the current active session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cvpdnsessionattrpacketsout
            
            	The total number of output packets through this active session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cvpdnsessionattrbytesout
            
            	The total number of output bytes through this active session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cvpdnsessionattrpacketsin
            
            	The total number of input packets through this active session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cvpdnsessionattrbytesin
            
            	The total number of input bytes through this active session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cvpdnsessionattrdevicetype
            
            	The type of physical devices that this session is attached to for the local end of the tunnel.  The meaning of each device type is explained below\:      other\:              Any device that has not been                         defined.      asyncInternalModem\: Modem Pool device of an access                         server.      async\:              A regular asynchronous serial                         interface.      sync\:               A regular synchronous serial                         interface.      bchan\:              An ISDN call.      xdsl\:               xDSL interface.      cable\:              cable modem interface
            	**type**\:  :py:class:`CvpdnSessionAttrDeviceType <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnSessionAttrTable.CvpdnSessionAttrEntry.CvpdnSessionAttrDeviceType>`
            
            	**config**\: False
            
            .. attribute:: cvpdnsessionattrdevicecallerid
            
            	The incoming caller identification of the user.  It is the originating number that called into the device that initiates the session.  This object can be empty since not all dial devices can provide caller ID information
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cvpdnsessionattrdevicephyid
            
            	The device ID of the physical interface for the session. The object is the the interface index which points to the ifTable.  For virtual interfaces that are not in the ifTable, the value will be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cvpdnsessionattrmultilink
            
            	This object indicates whether the session is part of a multilink PPP bundle, even if there is only one link or session in the bundle.  If it is multilink PPP, the value is true
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cvpdnsessionattrmodemslotindex
            
            	The Modem Pool database slot index if it is associated with this session.  Only a session with device of type 'asyncInternalModem' will have a valid value for this object; otherwise, it is not instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cvpdnsessionattrmodemportindex
            
            	The Modem Pool database port index if it is associated with this session.  Only a session with a device of type 'asyncInternalModem' will have a valid value for this object; otherwise, it is not instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cvpdnsessionattrds1slotindex
            
            	The DS1 database slot index if it is associated with this session.  Only a session with a device of type 'asyncInternalModem' will have a valid value for this object; otherwise it is not instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cvpdnsessionattrds1portindex
            
            	The DS1 database port index if it is associated with this session.  Only a session with a device of type 'asyncInternalModem' will have a valid value for this object; otherwise it is not instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cvpdnsessionattrds1channelindex
            
            	The DS1 database channel index if it is associated with this session.  Only a session over a device of type 'asyncInternalModem' will have a valid value for this object; otherwise it is not instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cvpdnsessionattrmodemcallstarttime
            
            	The start time of the current modem call.  Only a session with a device of type 'asyncInternalModem' will have a valid value for this object; otherwise, it is not instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cvpdnsessionattrmodemcallstartindex
            
            	Arbitrary small integer to distinguish modem calls that occurred at the same time tick.  Only session over device 'asyncInternalModem' will have a valid value for this object; otherwise, it is not instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cvpdnsessionattrvirtualcircuitid
            
            	The virtual circuit ID of an active Layer 2 VPN session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cvpdnsessionattrsentpktsdropped
            
            	The total number of dropped packets that could not be sent into this active session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cvpdnsessionattrrecvpktsdropped
            
            	The total number of dropped packets that were received from this active session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cvpdnsessionattrmultilinkbundle
            
            	This object specifies the name of the multilink bundle to which this session belongs.  The value of this object is only valid when the value of cvpdnSessionAttrMultilink is 'true'.  If the value of cvpdnSessionAttrMultilink is 'false', then the value of this object will be the empty string
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cvpdnsessionattrmultilinkifindex
            
            	This object specifies the ifIndex of the multilink bundle to which this session belongs.  The value of this object is only valid when the value of cvpdnSessionAttrMultilink is 'true'.  If the value of cvpdnSessionAttrMultilink is 'false', then the value of this object will be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CISCOVPDNMGMTMIB.CvpdnSessionAttrTable.CvpdnSessionAttrEntry, self).__init__()

                self.yang_name = "cvpdnSessionAttrEntry"
                self.yang_parent_name = "cvpdnSessionAttrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvpdnsystemtunneltype','cvpdntunnelattrtunnelid','cvpdnsessionattrsessionid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvpdnsystemtunneltype', (YLeaf(YType.enumeration, 'cvpdnSystemTunnelType'), [('ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'TunnelType', '')])),
                    ('cvpdntunnelattrtunnelid', (YLeaf(YType.str, 'cvpdnTunnelAttrTunnelId'), ['int'])),
                    ('cvpdnsessionattrsessionid', (YLeaf(YType.int32, 'cvpdnSessionAttrSessionId'), ['int'])),
                    ('cvpdnsessionattrusername', (YLeaf(YType.str, 'cvpdnSessionAttrUserName'), ['str'])),
                    ('cvpdnsessionattrstate', (YLeaf(YType.enumeration, 'cvpdnSessionAttrState'), [('ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CISCOVPDNMGMTMIB', 'CvpdnSessionAttrTable.CvpdnSessionAttrEntry.CvpdnSessionAttrState')])),
                    ('cvpdnsessionattrcallduration', (YLeaf(YType.uint32, 'cvpdnSessionAttrCallDuration'), ['int'])),
                    ('cvpdnsessionattrpacketsout', (YLeaf(YType.uint32, 'cvpdnSessionAttrPacketsOut'), ['int'])),
                    ('cvpdnsessionattrbytesout', (YLeaf(YType.uint32, 'cvpdnSessionAttrBytesOut'), ['int'])),
                    ('cvpdnsessionattrpacketsin', (YLeaf(YType.uint32, 'cvpdnSessionAttrPacketsIn'), ['int'])),
                    ('cvpdnsessionattrbytesin', (YLeaf(YType.uint32, 'cvpdnSessionAttrBytesIn'), ['int'])),
                    ('cvpdnsessionattrdevicetype', (YLeaf(YType.enumeration, 'cvpdnSessionAttrDeviceType'), [('ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CISCOVPDNMGMTMIB', 'CvpdnSessionAttrTable.CvpdnSessionAttrEntry.CvpdnSessionAttrDeviceType')])),
                    ('cvpdnsessionattrdevicecallerid', (YLeaf(YType.str, 'cvpdnSessionAttrDeviceCallerId'), ['str'])),
                    ('cvpdnsessionattrdevicephyid', (YLeaf(YType.int32, 'cvpdnSessionAttrDevicePhyId'), ['int'])),
                    ('cvpdnsessionattrmultilink', (YLeaf(YType.boolean, 'cvpdnSessionAttrMultilink'), ['bool'])),
                    ('cvpdnsessionattrmodemslotindex', (YLeaf(YType.uint32, 'cvpdnSessionAttrModemSlotIndex'), ['int'])),
                    ('cvpdnsessionattrmodemportindex', (YLeaf(YType.uint32, 'cvpdnSessionAttrModemPortIndex'), ['int'])),
                    ('cvpdnsessionattrds1slotindex', (YLeaf(YType.uint32, 'cvpdnSessionAttrDS1SlotIndex'), ['int'])),
                    ('cvpdnsessionattrds1portindex', (YLeaf(YType.uint32, 'cvpdnSessionAttrDS1PortIndex'), ['int'])),
                    ('cvpdnsessionattrds1channelindex', (YLeaf(YType.uint32, 'cvpdnSessionAttrDS1ChannelIndex'), ['int'])),
                    ('cvpdnsessionattrmodemcallstarttime', (YLeaf(YType.uint32, 'cvpdnSessionAttrModemCallStartTime'), ['int'])),
                    ('cvpdnsessionattrmodemcallstartindex', (YLeaf(YType.uint32, 'cvpdnSessionAttrModemCallStartIndex'), ['int'])),
                    ('cvpdnsessionattrvirtualcircuitid', (YLeaf(YType.uint32, 'cvpdnSessionAttrVirtualCircuitID'), ['int'])),
                    ('cvpdnsessionattrsentpktsdropped', (YLeaf(YType.uint32, 'cvpdnSessionAttrSentPktsDropped'), ['int'])),
                    ('cvpdnsessionattrrecvpktsdropped', (YLeaf(YType.uint32, 'cvpdnSessionAttrRecvPktsDropped'), ['int'])),
                    ('cvpdnsessionattrmultilinkbundle', (YLeaf(YType.str, 'cvpdnSessionAttrMultilinkBundle'), ['str'])),
                    ('cvpdnsessionattrmultilinkifindex', (YLeaf(YType.int32, 'cvpdnSessionAttrMultilinkIfIndex'), ['int'])),
                ])
                self.cvpdnsystemtunneltype = None
                self.cvpdntunnelattrtunnelid = None
                self.cvpdnsessionattrsessionid = None
                self.cvpdnsessionattrusername = None
                self.cvpdnsessionattrstate = None
                self.cvpdnsessionattrcallduration = None
                self.cvpdnsessionattrpacketsout = None
                self.cvpdnsessionattrbytesout = None
                self.cvpdnsessionattrpacketsin = None
                self.cvpdnsessionattrbytesin = None
                self.cvpdnsessionattrdevicetype = None
                self.cvpdnsessionattrdevicecallerid = None
                self.cvpdnsessionattrdevicephyid = None
                self.cvpdnsessionattrmultilink = None
                self.cvpdnsessionattrmodemslotindex = None
                self.cvpdnsessionattrmodemportindex = None
                self.cvpdnsessionattrds1slotindex = None
                self.cvpdnsessionattrds1portindex = None
                self.cvpdnsessionattrds1channelindex = None
                self.cvpdnsessionattrmodemcallstarttime = None
                self.cvpdnsessionattrmodemcallstartindex = None
                self.cvpdnsessionattrvirtualcircuitid = None
                self.cvpdnsessionattrsentpktsdropped = None
                self.cvpdnsessionattrrecvpktsdropped = None
                self.cvpdnsessionattrmultilinkbundle = None
                self.cvpdnsessionattrmultilinkifindex = None
                self._segment_path = lambda: "cvpdnSessionAttrEntry" + "[cvpdnSystemTunnelType='" + str(self.cvpdnsystemtunneltype) + "']" + "[cvpdnTunnelAttrTunnelId='" + str(self.cvpdntunnelattrtunnelid) + "']" + "[cvpdnSessionAttrSessionId='" + str(self.cvpdnsessionattrsessionid) + "']"
                self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/cvpdnSessionAttrTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVPDNMGMTMIB.CvpdnSessionAttrTable.CvpdnSessionAttrEntry, ['cvpdnsystemtunneltype', 'cvpdntunnelattrtunnelid', 'cvpdnsessionattrsessionid', 'cvpdnsessionattrusername', 'cvpdnsessionattrstate', 'cvpdnsessionattrcallduration', 'cvpdnsessionattrpacketsout', 'cvpdnsessionattrbytesout', 'cvpdnsessionattrpacketsin', 'cvpdnsessionattrbytesin', 'cvpdnsessionattrdevicetype', 'cvpdnsessionattrdevicecallerid', 'cvpdnsessionattrdevicephyid', 'cvpdnsessionattrmultilink', 'cvpdnsessionattrmodemslotindex', 'cvpdnsessionattrmodemportindex', 'cvpdnsessionattrds1slotindex', 'cvpdnsessionattrds1portindex', 'cvpdnsessionattrds1channelindex', 'cvpdnsessionattrmodemcallstarttime', 'cvpdnsessionattrmodemcallstartindex', 'cvpdnsessionattrvirtualcircuitid', 'cvpdnsessionattrsentpktsdropped', 'cvpdnsessionattrrecvpktsdropped', 'cvpdnsessionattrmultilinkbundle', 'cvpdnsessionattrmultilinkifindex'], name, value)

            class CvpdnSessionAttrDeviceType(Enum):
                """
                CvpdnSessionAttrDeviceType (Enum Class)

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

                .. data:: other = 1

                .. data:: asyncInternalModem = 2

                .. data:: async = 3

                .. data:: bchan = 4

                .. data:: sync = 5

                .. data:: virtualAccess = 6

                .. data:: xdsl = 7

                .. data:: cable = 8

                """

                other = Enum.YLeaf(1, "other")

                asyncInternalModem = Enum.YLeaf(2, "asyncInternalModem")

                async = Enum.YLeaf(3, "async")

                bchan = Enum.YLeaf(4, "bchan")

                sync = Enum.YLeaf(5, "sync")

                virtualAccess = Enum.YLeaf(6, "virtualAccess")

                xdsl = Enum.YLeaf(7, "xdsl")

                cable = Enum.YLeaf(8, "cable")


            class CvpdnSessionAttrState(Enum):
                """
                CvpdnSessionAttrState (Enum Class)

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

                .. data:: unknown = 1

                .. data:: l2fOpening = 2

                .. data:: l2fOpen = 3

                .. data:: l2fCloseWait = 4

                .. data:: l2fWaitingForTunnel = 5

                .. data:: l2tpIdle = 6

                .. data:: l2tpWaitingTunnel = 7

                .. data:: l2tpWaitReply = 8

                .. data:: l2tpWaitConnect = 9

                .. data:: l2tpEstablished = 10

                .. data:: l2tpShuttingDown = 11

                .. data:: pptpWaitVAccess = 12

                .. data:: pptpPacEstablished = 13

                .. data:: pptpWaitTunnel = 14

                .. data:: pptpWaitOCRP = 15

                .. data:: pptpPnsEstablished = 16

                .. data:: pptpWaitCallDisc = 17

                .. data:: pptpTerminal = 18

                """

                unknown = Enum.YLeaf(1, "unknown")

                l2fOpening = Enum.YLeaf(2, "l2fOpening")

                l2fOpen = Enum.YLeaf(3, "l2fOpen")

                l2fCloseWait = Enum.YLeaf(4, "l2fCloseWait")

                l2fWaitingForTunnel = Enum.YLeaf(5, "l2fWaitingForTunnel")

                l2tpIdle = Enum.YLeaf(6, "l2tpIdle")

                l2tpWaitingTunnel = Enum.YLeaf(7, "l2tpWaitingTunnel")

                l2tpWaitReply = Enum.YLeaf(8, "l2tpWaitReply")

                l2tpWaitConnect = Enum.YLeaf(9, "l2tpWaitConnect")

                l2tpEstablished = Enum.YLeaf(10, "l2tpEstablished")

                l2tpShuttingDown = Enum.YLeaf(11, "l2tpShuttingDown")

                pptpWaitVAccess = Enum.YLeaf(12, "pptpWaitVAccess")

                pptpPacEstablished = Enum.YLeaf(13, "pptpPacEstablished")

                pptpWaitTunnel = Enum.YLeaf(14, "pptpWaitTunnel")

                pptpWaitOCRP = Enum.YLeaf(15, "pptpWaitOCRP")

                pptpPnsEstablished = Enum.YLeaf(16, "pptpPnsEstablished")

                pptpWaitCallDisc = Enum.YLeaf(17, "pptpWaitCallDisc")

                pptpTerminal = Enum.YLeaf(18, "pptpTerminal")





    class CvpdnUserToFailHistInfoTable(Entity):
        """
        Table of the record of failure objects which can be
        referenced by an user name.  Only a name that has a
        valid item in the Cisco IOS VPDN failure history table
        will yield a valid entry in this table.  The table has
        a maximum size of 50 entries.  Only the newest 50
        entries will be kept in the table.
        
        .. attribute:: cvpdnusertofailhistinfoentry
        
        	An entry in the table, containing failure history relevant to an user name
        	**type**\: list of  		 :py:class:`CvpdnUserToFailHistInfoEntry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnUserToFailHistInfoTable.CvpdnUserToFailHistInfoEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.CvpdnUserToFailHistInfoTable, self).__init__()

            self.yang_name = "cvpdnUserToFailHistInfoTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cvpdnUserToFailHistInfoEntry", ("cvpdnusertofailhistinfoentry", CISCOVPDNMGMTMIB.CvpdnUserToFailHistInfoTable.CvpdnUserToFailHistInfoEntry))])
            self._leafs = OrderedDict()

            self.cvpdnusertofailhistinfoentry = YList(self)
            self._segment_path = lambda: "cvpdnUserToFailHistInfoTable"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.CvpdnUserToFailHistInfoTable, [], name, value)


        class CvpdnUserToFailHistInfoEntry(Entity):
            """
            An entry in the table, containing failure history
            relevant to an user name.
            
            .. attribute:: cvpdnunametofailhistuname  (key)
            
            	The user name for this failure entry
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            .. attribute:: cvpdnunametofailhisttunnelid  (key)
            
            	The Tunnel ID for this failure entry.  If it is the instigator of the tunnel, the ID is the TS tunnel ID, otherwise it is the NAS tunnel ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cvpdnunametofailhistuserid
            
            	The user ID of this failure entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cvpdnunametofailhistlocalinitconn
            
            	This object indicates whether the tunnel in which the failure occurred was generated locally or not
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cvpdnunametofailhistlocalname
            
            	The local name of the VPDN tunnel in which the failure occurred.  It will be the NAS name of the tunnel if the system serves as the NAS, or the TS name of the tunnel if the system serves as the tunnel server.  The local name is the configured host name of the system.  This object can be empty if the failure occurred prior to successful tunnel projection, thus no source name will be available
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cvpdnunametofailhistremotename
            
            	The remote name of the VPDN tunnel in which the failure occurred.  It will be the tunnel server name of the tunnel if the system is a NAS, or the NAS name of the tunnel if the system serves as the tunnel server.  This object can be empty if the failure occurred prior to successful tunnel projection, thus no source name will be available
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cvpdnunametofailhistsourceip
            
            	The source IP address of the tunnel in which the failure occurred.  This IP address is that of the interface at the instigator end of the tunnel
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: cvpdnunametofailhistdestip
            
            	The destination IP address of the tunnel in which the failure occurred.  This IP address is that of the interface at the receiver end of the tunnel
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: cvpdnunametofailhistcount
            
            	This object is incremented when multiple failures has been experienced by this user on this tunnel.  Seeing a delta of >1 is an indication that the current failure record is the latest of a series of failures that has been recorded
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: failures
            
            .. attribute:: cvpdnunametofailhistfailtime
            
            	This object specifies the time when the failure is occurred
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cvpdnunametofailhistfailtype
            
            	The type of failure for the current failure record.  It comes in a form of a an ASCII string which describes the type of failure
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            .. attribute:: cvpdnunametofailhistfailreason
            
            	The reason of failure for the current failure record
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            .. attribute:: cvpdnunametofailhistsourceinettype
            
            	Indicates the type of address contained in cvpdnUnameToFailHistSourceInetAddr
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cvpdnunametofailhistsourceinetaddr
            
            	The source IP address of the tunnel in which the failure occurred.  This IP address is that of the interface at the instigator end of the tunnel.  The instigator end is the peer which initiates the tunnel estalishment.  The type of this address is determined by the value of cvpdnUnameToFailHistSourceInetType
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cvpdnunametofailhistdestinettype
            
            	Indicates the type of address contained in cvpdnUnameToFailHistDestInetAddr
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cvpdnunametofailhistdestinetaddr
            
            	The destination IP address of the tunnel in which the failure occurred.  This IP address is that of the interface at the receiver end of the tunnel.  The type  of this address is determined by the value of  cvpdnUnameToFailHistDestInetType
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CISCOVPDNMGMTMIB.CvpdnUserToFailHistInfoTable.CvpdnUserToFailHistInfoEntry, self).__init__()

                self.yang_name = "cvpdnUserToFailHistInfoEntry"
                self.yang_parent_name = "cvpdnUserToFailHistInfoTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvpdnunametofailhistuname','cvpdnunametofailhisttunnelid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvpdnunametofailhistuname', (YLeaf(YType.str, 'cvpdnUnameToFailHistUname'), ['str'])),
                    ('cvpdnunametofailhisttunnelid', (YLeaf(YType.uint32, 'cvpdnUnameToFailHistTunnelId'), ['int'])),
                    ('cvpdnunametofailhistuserid', (YLeaf(YType.uint32, 'cvpdnUnameToFailHistUserId'), ['int'])),
                    ('cvpdnunametofailhistlocalinitconn', (YLeaf(YType.boolean, 'cvpdnUnameToFailHistLocalInitConn'), ['bool'])),
                    ('cvpdnunametofailhistlocalname', (YLeaf(YType.str, 'cvpdnUnameToFailHistLocalName'), ['str'])),
                    ('cvpdnunametofailhistremotename', (YLeaf(YType.str, 'cvpdnUnameToFailHistRemoteName'), ['str'])),
                    ('cvpdnunametofailhistsourceip', (YLeaf(YType.str, 'cvpdnUnameToFailHistSourceIp'), ['str'])),
                    ('cvpdnunametofailhistdestip', (YLeaf(YType.str, 'cvpdnUnameToFailHistDestIp'), ['str'])),
                    ('cvpdnunametofailhistcount', (YLeaf(YType.uint32, 'cvpdnUnameToFailHistCount'), ['int'])),
                    ('cvpdnunametofailhistfailtime', (YLeaf(YType.uint32, 'cvpdnUnameToFailHistFailTime'), ['int'])),
                    ('cvpdnunametofailhistfailtype', (YLeaf(YType.str, 'cvpdnUnameToFailHistFailType'), ['str'])),
                    ('cvpdnunametofailhistfailreason', (YLeaf(YType.str, 'cvpdnUnameToFailHistFailReason'), ['str'])),
                    ('cvpdnunametofailhistsourceinettype', (YLeaf(YType.enumeration, 'cvpdnUnameToFailHistSourceInetType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cvpdnunametofailhistsourceinetaddr', (YLeaf(YType.str, 'cvpdnUnameToFailHistSourceInetAddr'), ['str'])),
                    ('cvpdnunametofailhistdestinettype', (YLeaf(YType.enumeration, 'cvpdnUnameToFailHistDestInetType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cvpdnunametofailhistdestinetaddr', (YLeaf(YType.str, 'cvpdnUnameToFailHistDestInetAddr'), ['str'])),
                ])
                self.cvpdnunametofailhistuname = None
                self.cvpdnunametofailhisttunnelid = None
                self.cvpdnunametofailhistuserid = None
                self.cvpdnunametofailhistlocalinitconn = None
                self.cvpdnunametofailhistlocalname = None
                self.cvpdnunametofailhistremotename = None
                self.cvpdnunametofailhistsourceip = None
                self.cvpdnunametofailhistdestip = None
                self.cvpdnunametofailhistcount = None
                self.cvpdnunametofailhistfailtime = None
                self.cvpdnunametofailhistfailtype = None
                self.cvpdnunametofailhistfailreason = None
                self.cvpdnunametofailhistsourceinettype = None
                self.cvpdnunametofailhistsourceinetaddr = None
                self.cvpdnunametofailhistdestinettype = None
                self.cvpdnunametofailhistdestinetaddr = None
                self._segment_path = lambda: "cvpdnUserToFailHistInfoEntry" + "[cvpdnUnameToFailHistUname='" + str(self.cvpdnunametofailhistuname) + "']" + "[cvpdnUnameToFailHistTunnelId='" + str(self.cvpdnunametofailhisttunnelid) + "']"
                self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/cvpdnUserToFailHistInfoTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVPDNMGMTMIB.CvpdnUserToFailHistInfoTable.CvpdnUserToFailHistInfoEntry, ['cvpdnunametofailhistuname', 'cvpdnunametofailhisttunnelid', 'cvpdnunametofailhistuserid', 'cvpdnunametofailhistlocalinitconn', 'cvpdnunametofailhistlocalname', 'cvpdnunametofailhistremotename', 'cvpdnunametofailhistsourceip', 'cvpdnunametofailhistdestip', 'cvpdnunametofailhistcount', 'cvpdnunametofailhistfailtime', 'cvpdnunametofailhistfailtype', 'cvpdnunametofailhistfailreason', 'cvpdnunametofailhistsourceinettype', 'cvpdnunametofailhistsourceinetaddr', 'cvpdnunametofailhistdestinettype', 'cvpdnunametofailhistdestinetaddr'], name, value)




    class CvpdnTemplateTable(Entity):
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
        	**type**\: list of  		 :py:class:`CvpdnTemplateEntry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnTemplateTable.CvpdnTemplateEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.CvpdnTemplateTable, self).__init__()

            self.yang_name = "cvpdnTemplateTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cvpdnTemplateEntry", ("cvpdntemplateentry", CISCOVPDNMGMTMIB.CvpdnTemplateTable.CvpdnTemplateEntry))])
            self._leafs = OrderedDict()

            self.cvpdntemplateentry = YList(self)
            self._segment_path = lambda: "cvpdnTemplateTable"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.CvpdnTemplateTable, [], name, value)


        class CvpdnTemplateEntry(Entity):
            """
            An entry in the table, containing information about a
            single VPDN template.
            
            .. attribute:: cvpdntemplatename  (key)
            
            	The name of the VPDN template
            	**type**\: str
            
            	**length:** 1..255
            
            	**config**\: False
            
            .. attribute:: cvpdntemplateactivesessions
            
            	The total number of active session in all groups associated with the template
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CISCOVPDNMGMTMIB.CvpdnTemplateTable.CvpdnTemplateEntry, self).__init__()

                self.yang_name = "cvpdnTemplateEntry"
                self.yang_parent_name = "cvpdnTemplateTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvpdntemplatename']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvpdntemplatename', (YLeaf(YType.str, 'cvpdnTemplateName'), ['str'])),
                    ('cvpdntemplateactivesessions', (YLeaf(YType.uint32, 'cvpdnTemplateActiveSessions'), ['int'])),
                ])
                self.cvpdntemplatename = None
                self.cvpdntemplateactivesessions = None
                self._segment_path = lambda: "cvpdnTemplateEntry" + "[cvpdnTemplateName='" + str(self.cvpdntemplatename) + "']"
                self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/cvpdnTemplateTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVPDNMGMTMIB.CvpdnTemplateTable.CvpdnTemplateEntry, ['cvpdntemplatename', 'cvpdntemplateactivesessions'], name, value)




    class CvpdnBundleTable(Entity):
        """
        Table that describes the multilink PPP attributes of the
        active VPDN sessions.
        
        .. attribute:: cvpdnbundleentry
        
        	An entry in this table represents an active multilink PPP bundle that belongs to a VPDN tunnel
        	**type**\: list of  		 :py:class:`CvpdnBundleEntry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnBundleTable.CvpdnBundleEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.CvpdnBundleTable, self).__init__()

            self.yang_name = "cvpdnBundleTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cvpdnBundleEntry", ("cvpdnbundleentry", CISCOVPDNMGMTMIB.CvpdnBundleTable.CvpdnBundleEntry))])
            self._leafs = OrderedDict()

            self.cvpdnbundleentry = YList(self)
            self._segment_path = lambda: "cvpdnBundleTable"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.CvpdnBundleTable, [], name, value)


        class CvpdnBundleEntry(Entity):
            """
            An entry in this table represents an active multilink PPP
            bundle that belongs to a VPDN tunnel.
            
            .. attribute:: cvpdnbundlename  (key)
            
            	The name of the multilink PPP bundle associated with a VPDN tunnel
            	**type**\: str
            
            	**length:** 1..64
            
            	**config**\: False
            
            .. attribute:: cvpdnbundlelinkcount
            
            	The total number of active links in a multilink PPP bundle associated with a VPDN tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: links
            
            .. attribute:: cvpdnbundleendpointtype
            
            	The multilink PPP bundle discriminator type associated with a VPDN tunnel.  The value of this object represents the type of discriminator used in cvpdnBundleEndpoint.      none\:        No endpoint discriminator was supplied, the                  default value is being used.      hostname\:    The router's hostname is being used as                  discriminator.      string\:      User specified string is being used as                  discriminator.      macAddress\:  A MAC address as defined by the MacAddress                  textual convention is being used as                  discriminator.      ipV4Address\: An IP address as defined by the                  InetAddressIPv4 textual convention is being                  used as discriminator.      ipV6Address\: An IP address as defined by the                  InetAddressIPv6 textual convention is being                  used as discriminator.      phone\:       The PSTN phone number is being used as                  discriminator.      magicNumber\: A magic number is being used as                  discriminator
            	**type**\:  :py:class:`CvpdnBundleEndpointType <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnBundleTable.CvpdnBundleEntry.CvpdnBundleEndpointType>`
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: cvpdnbundleendpoint
            
            	Indicates the discriminator used in this bundle that is associated with a VPDN tunnel
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cvpdnbundlepeeripaddrtype
            
            	Indicates the type of address contained in cvpdnBundlePeerIpAddr
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cvpdnbundlepeeripaddr
            
            	The IP address of the multilink PPP peer in a VPDN tunnel
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cvpdnbundleendpointclass
            
            	The multilink PPP bundle discriminator class associated with a VPDN tunnel.  The value of this object represents the type of discriminator used in cvpdnBundleEndpoint
            	**type**\:  :py:class:`EndpointClass <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.EndpointClass>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CISCOVPDNMGMTMIB.CvpdnBundleTable.CvpdnBundleEntry, self).__init__()

                self.yang_name = "cvpdnBundleEntry"
                self.yang_parent_name = "cvpdnBundleTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvpdnbundlename']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvpdnbundlename', (YLeaf(YType.str, 'cvpdnBundleName'), ['str'])),
                    ('cvpdnbundlelinkcount', (YLeaf(YType.uint32, 'cvpdnBundleLinkCount'), ['int'])),
                    ('cvpdnbundleendpointtype', (YLeaf(YType.enumeration, 'cvpdnBundleEndpointType'), [('ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'CISCOVPDNMGMTMIB', 'CvpdnBundleTable.CvpdnBundleEntry.CvpdnBundleEndpointType')])),
                    ('cvpdnbundleendpoint', (YLeaf(YType.str, 'cvpdnBundleEndpoint'), ['str'])),
                    ('cvpdnbundlepeeripaddrtype', (YLeaf(YType.enumeration, 'cvpdnBundlePeerIpAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cvpdnbundlepeeripaddr', (YLeaf(YType.str, 'cvpdnBundlePeerIpAddr'), ['str'])),
                    ('cvpdnbundleendpointclass', (YLeaf(YType.enumeration, 'cvpdnBundleEndpointClass'), [('ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'EndpointClass', '')])),
                ])
                self.cvpdnbundlename = None
                self.cvpdnbundlelinkcount = None
                self.cvpdnbundleendpointtype = None
                self.cvpdnbundleendpoint = None
                self.cvpdnbundlepeeripaddrtype = None
                self.cvpdnbundlepeeripaddr = None
                self.cvpdnbundleendpointclass = None
                self._segment_path = lambda: "cvpdnBundleEntry" + "[cvpdnBundleName='" + str(self.cvpdnbundlename) + "']"
                self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/cvpdnBundleTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVPDNMGMTMIB.CvpdnBundleTable.CvpdnBundleEntry, ['cvpdnbundlename', 'cvpdnbundlelinkcount', 'cvpdnbundleendpointtype', 'cvpdnbundleendpoint', 'cvpdnbundlepeeripaddrtype', 'cvpdnbundlepeeripaddr', 'cvpdnbundleendpointclass'], name, value)

            class CvpdnBundleEndpointType(Enum):
                """
                CvpdnBundleEndpointType (Enum Class)

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

                .. data:: none = 1

                .. data:: hostname = 2

                .. data:: string = 3

                .. data:: macAddress = 4

                .. data:: ipV4Address = 5

                .. data:: ipV6Address = 6

                .. data:: phone = 7

                .. data:: magicNumber = 8

                """

                none = Enum.YLeaf(1, "none")

                hostname = Enum.YLeaf(2, "hostname")

                string = Enum.YLeaf(3, "string")

                macAddress = Enum.YLeaf(4, "macAddress")

                ipV4Address = Enum.YLeaf(5, "ipV4Address")

                ipV6Address = Enum.YLeaf(6, "ipV6Address")

                phone = Enum.YLeaf(7, "phone")

                magicNumber = Enum.YLeaf(8, "magicNumber")





    class CvpdnBundleChildTable(Entity):
        """
        A table that exposes the containment relationship between a
        multilink PPP bundle and a VPDN tunnel.
        
        .. attribute:: cvpdnbundlechildentry
        
        	An entry in this table represents a session that belongs to a VPDN tunnel and to a multilink PPP bundle
        	**type**\: list of  		 :py:class:`CvpdnBundleChildEntry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnBundleChildTable.CvpdnBundleChildEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.CvpdnBundleChildTable, self).__init__()

            self.yang_name = "cvpdnBundleChildTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cvpdnBundleChildEntry", ("cvpdnbundlechildentry", CISCOVPDNMGMTMIB.CvpdnBundleChildTable.CvpdnBundleChildEntry))])
            self._leafs = OrderedDict()

            self.cvpdnbundlechildentry = YList(self)
            self._segment_path = lambda: "cvpdnBundleChildTable"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.CvpdnBundleChildTable, [], name, value)


        class CvpdnBundleChildEntry(Entity):
            """
            An entry in this table represents a session that belongs to
            a VPDN tunnel and to a multilink PPP bundle.
            
            .. attribute:: cvpdnbundlename  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..64
            
            	**refers to**\:  :py:class:`cvpdnbundlename <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.CvpdnBundleTable.CvpdnBundleEntry>`
            
            	**config**\: False
            
            .. attribute:: cvpdnbundlechildtunneltype  (key)
            
            	The tunnel type.  This is the tunnel protocol of an active VPDN session that is associated with a multilink PPP bundle
            	**type**\:  :py:class:`TunnelType <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.TunnelType>`
            
            	**config**\: False
            
            .. attribute:: cvpdnbundlechildtunnelid  (key)
            
            	The Tunnel ID of an active VPDN session that is associated with a multilink PPP bundle
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cvpdnbundlechildsessionid  (key)
            
            	The ID of an active VPDN session that is associated with a multilink PPP bundle
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CISCOVPDNMGMTMIB.CvpdnBundleChildTable.CvpdnBundleChildEntry, self).__init__()

                self.yang_name = "cvpdnBundleChildEntry"
                self.yang_parent_name = "cvpdnBundleChildTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvpdnbundlename','cvpdnbundlechildtunneltype','cvpdnbundlechildtunnelid','cvpdnbundlechildsessionid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvpdnbundlename', (YLeaf(YType.str, 'cvpdnBundleName'), ['str'])),
                    ('cvpdnbundlechildtunneltype', (YLeaf(YType.enumeration, 'cvpdnBundleChildTunnelType'), [('ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB', 'TunnelType', '')])),
                    ('cvpdnbundlechildtunnelid', (YLeaf(YType.uint32, 'cvpdnBundleChildTunnelId'), ['int'])),
                    ('cvpdnbundlechildsessionid', (YLeaf(YType.uint32, 'cvpdnBundleChildSessionId'), ['int'])),
                ])
                self.cvpdnbundlename = None
                self.cvpdnbundlechildtunneltype = None
                self.cvpdnbundlechildtunnelid = None
                self.cvpdnbundlechildsessionid = None
                self._segment_path = lambda: "cvpdnBundleChildEntry" + "[cvpdnBundleName='" + str(self.cvpdnbundlename) + "']" + "[cvpdnBundleChildTunnelType='" + str(self.cvpdnbundlechildtunneltype) + "']" + "[cvpdnBundleChildTunnelId='" + str(self.cvpdnbundlechildtunnelid) + "']" + "[cvpdnBundleChildSessionId='" + str(self.cvpdnbundlechildsessionid) + "']"
                self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/cvpdnBundleChildTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVPDNMGMTMIB.CvpdnBundleChildTable.CvpdnBundleChildEntry, ['cvpdnbundlename', 'cvpdnbundlechildtunneltype', 'cvpdnbundlechildtunnelid', 'cvpdnbundlechildsessionid'], name, value)



    def clone_ptr(self):
        self._top_entity = CISCOVPDNMGMTMIB()
        return self._top_entity




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
    
    	
    	**type**\:  :py:class:`Ciscovpdnmgmtmibnotifs <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Ciscovpdnmgmtmibnotifs>`
    
    .. attribute:: cvpdnsysteminfo
    
    	
    	**type**\:  :py:class:`Cvpdnsysteminfo <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdnsysteminfo>`
    
    .. attribute:: cvpdnmultilinkinfo
    
    	
    	**type**\:  :py:class:`Cvpdnmultilinkinfo <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdnmultilinkinfo>`
    
    .. attribute:: cvpdnsystemtable
    
    	Table of information about the VPDN system for all tunnel types
    	**type**\:  :py:class:`Cvpdnsystemtable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdnsystemtable>`
    
    .. attribute:: cvpdntunneltable
    
    	Table of information about the active VPDN tunnels
    	**type**\:  :py:class:`Cvpdntunneltable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdntunneltable>`
    
    	**status**\: obsolete
    
    .. attribute:: cvpdntunnelattrtable
    
    	Table of information about the active VPDN tunnels.  An entry is added to the table when a new tunnel is initiated and removed from the table when the tunnel is terminated
    	**type**\:  :py:class:`Cvpdntunnelattrtable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdntunnelattrtable>`
    
    .. attribute:: cvpdntunnelsessiontable
    
    	Table of information about individual user sessions within the active tunnels.  Entry is added to the table when new user session is initiated and be removed from the table when the user session is terminated
    	**type**\:  :py:class:`Cvpdntunnelsessiontable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdntunnelsessiontable>`
    
    	**status**\: obsolete
    
    .. attribute:: cvpdnsessionattrtable
    
    	Table of information about individual sessions within the active tunnels.  An entry is added to the table when a new session is initiated and removed from the table when the session is terminated
    	**type**\:  :py:class:`Cvpdnsessionattrtable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdnsessionattrtable>`
    
    .. attribute:: cvpdnusertofailhistinfotable
    
    	Table of the record of failure objects which can be referenced by an user name.  Only a name that has a valid item in the Cisco IOS VPDN failure history table will yield a valid entry in this table.  The table has a maximum size of 50 entries.  Only the newest 50 entries will be kept in the table
    	**type**\:  :py:class:`Cvpdnusertofailhistinfotable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdnusertofailhistinfotable>`
    
    .. attribute:: cvpdntemplatetable
    
    	Table of information about the VPDN templates.  The VPDN template is a grouping mechanism that allows configuration settings to be shared among multiple VPDN groups.  One such setting is a limit on the number of active sessions across all VPDN groups associated with the template.  The template table allows customers to monitor template\-wide information such as tracking the allocation of sessions across templates
    	**type**\:  :py:class:`Cvpdntemplatetable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdntemplatetable>`
    
    .. attribute:: cvpdnbundletable
    
    	Table that describes the multilink PPP attributes of the active VPDN sessions
    	**type**\:  :py:class:`Cvpdnbundletable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdnbundletable>`
    
    .. attribute:: cvpdnbundlechildtable
    
    	A table that exposes the containment relationship between a multilink PPP bundle and a VPDN tunnel
    	**type**\:  :py:class:`Cvpdnbundlechildtable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdnbundlechildtable>`
    
    

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
        self._child_container_classes = OrderedDict([("ciscoVpdnMgmtMIBNotifs", ("ciscovpdnmgmtmibnotifs", CISCOVPDNMGMTMIB.Ciscovpdnmgmtmibnotifs)), ("cvpdnSystemInfo", ("cvpdnsysteminfo", CISCOVPDNMGMTMIB.Cvpdnsysteminfo)), ("cvpdnMultilinkInfo", ("cvpdnmultilinkinfo", CISCOVPDNMGMTMIB.Cvpdnmultilinkinfo)), ("cvpdnSystemTable", ("cvpdnsystemtable", CISCOVPDNMGMTMIB.Cvpdnsystemtable)), ("cvpdnTunnelTable", ("cvpdntunneltable", CISCOVPDNMGMTMIB.Cvpdntunneltable)), ("cvpdnTunnelAttrTable", ("cvpdntunnelattrtable", CISCOVPDNMGMTMIB.Cvpdntunnelattrtable)), ("cvpdnTunnelSessionTable", ("cvpdntunnelsessiontable", CISCOVPDNMGMTMIB.Cvpdntunnelsessiontable)), ("cvpdnSessionAttrTable", ("cvpdnsessionattrtable", CISCOVPDNMGMTMIB.Cvpdnsessionattrtable)), ("cvpdnUserToFailHistInfoTable", ("cvpdnusertofailhistinfotable", CISCOVPDNMGMTMIB.Cvpdnusertofailhistinfotable)), ("cvpdnTemplateTable", ("cvpdntemplatetable", CISCOVPDNMGMTMIB.Cvpdntemplatetable)), ("cvpdnBundleTable", ("cvpdnbundletable", CISCOVPDNMGMTMIB.Cvpdnbundletable)), ("cvpdnBundleChildTable", ("cvpdnbundlechildtable", CISCOVPDNMGMTMIB.Cvpdnbundlechildtable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.ciscovpdnmgmtmibnotifs = CISCOVPDNMGMTMIB.Ciscovpdnmgmtmibnotifs()
        self.ciscovpdnmgmtmibnotifs.parent = self
        self._children_name_map["ciscovpdnmgmtmibnotifs"] = "ciscoVpdnMgmtMIBNotifs"
        self._children_yang_names.add("ciscoVpdnMgmtMIBNotifs")

        self.cvpdnsysteminfo = CISCOVPDNMGMTMIB.Cvpdnsysteminfo()
        self.cvpdnsysteminfo.parent = self
        self._children_name_map["cvpdnsysteminfo"] = "cvpdnSystemInfo"
        self._children_yang_names.add("cvpdnSystemInfo")

        self.cvpdnmultilinkinfo = CISCOVPDNMGMTMIB.Cvpdnmultilinkinfo()
        self.cvpdnmultilinkinfo.parent = self
        self._children_name_map["cvpdnmultilinkinfo"] = "cvpdnMultilinkInfo"
        self._children_yang_names.add("cvpdnMultilinkInfo")

        self.cvpdnsystemtable = CISCOVPDNMGMTMIB.Cvpdnsystemtable()
        self.cvpdnsystemtable.parent = self
        self._children_name_map["cvpdnsystemtable"] = "cvpdnSystemTable"
        self._children_yang_names.add("cvpdnSystemTable")

        self.cvpdntunneltable = CISCOVPDNMGMTMIB.Cvpdntunneltable()
        self.cvpdntunneltable.parent = self
        self._children_name_map["cvpdntunneltable"] = "cvpdnTunnelTable"
        self._children_yang_names.add("cvpdnTunnelTable")

        self.cvpdntunnelattrtable = CISCOVPDNMGMTMIB.Cvpdntunnelattrtable()
        self.cvpdntunnelattrtable.parent = self
        self._children_name_map["cvpdntunnelattrtable"] = "cvpdnTunnelAttrTable"
        self._children_yang_names.add("cvpdnTunnelAttrTable")

        self.cvpdntunnelsessiontable = CISCOVPDNMGMTMIB.Cvpdntunnelsessiontable()
        self.cvpdntunnelsessiontable.parent = self
        self._children_name_map["cvpdntunnelsessiontable"] = "cvpdnTunnelSessionTable"
        self._children_yang_names.add("cvpdnTunnelSessionTable")

        self.cvpdnsessionattrtable = CISCOVPDNMGMTMIB.Cvpdnsessionattrtable()
        self.cvpdnsessionattrtable.parent = self
        self._children_name_map["cvpdnsessionattrtable"] = "cvpdnSessionAttrTable"
        self._children_yang_names.add("cvpdnSessionAttrTable")

        self.cvpdnusertofailhistinfotable = CISCOVPDNMGMTMIB.Cvpdnusertofailhistinfotable()
        self.cvpdnusertofailhistinfotable.parent = self
        self._children_name_map["cvpdnusertofailhistinfotable"] = "cvpdnUserToFailHistInfoTable"
        self._children_yang_names.add("cvpdnUserToFailHistInfoTable")

        self.cvpdntemplatetable = CISCOVPDNMGMTMIB.Cvpdntemplatetable()
        self.cvpdntemplatetable.parent = self
        self._children_name_map["cvpdntemplatetable"] = "cvpdnTemplateTable"
        self._children_yang_names.add("cvpdnTemplateTable")

        self.cvpdnbundletable = CISCOVPDNMGMTMIB.Cvpdnbundletable()
        self.cvpdnbundletable.parent = self
        self._children_name_map["cvpdnbundletable"] = "cvpdnBundleTable"
        self._children_yang_names.add("cvpdnBundleTable")

        self.cvpdnbundlechildtable = CISCOVPDNMGMTMIB.Cvpdnbundlechildtable()
        self.cvpdnbundlechildtable.parent = self
        self._children_name_map["cvpdnbundlechildtable"] = "cvpdnBundleChildTable"
        self._children_yang_names.add("cvpdnBundleChildTable")
        self._segment_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB"


    class Ciscovpdnmgmtmibnotifs(Entity):
        """
        
        
        .. attribute:: cvpdnnotifsessionid
        
        	This object contains the local session ID of the L2X session for which this notification has been generated
        	**type**\: int
        
        	**range:** 0..65535
        
        .. attribute:: cvpdnnotifsessionevent
        
        	Indicates the event that generated the L2X session notification.  The events are represented as follows\:  up\:     Session has come up.  down\:   Session has gone down.  pwUp\:   Pseudowire associated with this          session has come up.  pwDown\: Pseudowire associated with this          session has gone down
        	**type**\:  :py:class:`Cvpdnnotifsessionevent <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Ciscovpdnmgmtmibnotifs.Cvpdnnotifsessionevent>`
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.Ciscovpdnmgmtmibnotifs, self).__init__()

            self.yang_name = "ciscoVpdnMgmtMIBNotifs"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cvpdnnotifsessionid', YLeaf(YType.int32, 'cvpdnNotifSessionID')),
                ('cvpdnnotifsessionevent', YLeaf(YType.enumeration, 'cvpdnNotifSessionEvent')),
            ])
            self.cvpdnnotifsessionid = None
            self.cvpdnnotifsessionevent = None
            self._segment_path = lambda: "ciscoVpdnMgmtMIBNotifs"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.Ciscovpdnmgmtmibnotifs, ['cvpdnnotifsessionid', 'cvpdnnotifsessionevent'], name, value)

        class Cvpdnnotifsessionevent(Enum):
            """
            Cvpdnnotifsessionevent (Enum Class)

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



    class Cvpdnsysteminfo(Entity):
        """
        
        
        .. attribute:: cvpdntunneltotal
        
        	The total number of VPDN tunnels that are currently active within this system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: tunnels
        
        	**status**\: obsolete
        
        .. attribute:: cvpdnsessiontotal
        
        	The total number of active users in all the active VPDN tunnels within this system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: users
        
        	**status**\: obsolete
        
        .. attribute:: cvpdndenieduserstotal
        
        	The total number of denied user attempts to all the active VPDN tunnels within this system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**units**\: attempts
        
        	**status**\: obsolete
        
        .. attribute:: cvpdnsystemnotifsessionenabled
        
        	Indicates whether Layer 2 VPN session notifications are enabled
        	**type**\: bool
        
        .. attribute:: cvpdnsystemclearsessions
        
        	Clears all the sessions in a given tunnel type.  When reading this object, the value of 'none' will always be returned.  When setting these values, the following operations will be performed\:      none\: no operation.      all\:  clears all the sessions in all the tunnels.      l2f\:  clears all the L2F sessions.      l2tp\: clears all the L2TP sessions.      pptp\: clears all the PPTP sessions
        	**type**\:  :py:class:`Cvpdnsystemclearsessions <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdnsysteminfo.Cvpdnsystemclearsessions>`
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.Cvpdnsysteminfo, self).__init__()

            self.yang_name = "cvpdnSystemInfo"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cvpdntunneltotal', YLeaf(YType.uint32, 'cvpdnTunnelTotal')),
                ('cvpdnsessiontotal', YLeaf(YType.uint32, 'cvpdnSessionTotal')),
                ('cvpdndenieduserstotal', YLeaf(YType.uint32, 'cvpdnDeniedUsersTotal')),
                ('cvpdnsystemnotifsessionenabled', YLeaf(YType.boolean, 'cvpdnSystemNotifSessionEnabled')),
                ('cvpdnsystemclearsessions', YLeaf(YType.enumeration, 'cvpdnSystemClearSessions')),
            ])
            self.cvpdntunneltotal = None
            self.cvpdnsessiontotal = None
            self.cvpdndenieduserstotal = None
            self.cvpdnsystemnotifsessionenabled = None
            self.cvpdnsystemclearsessions = None
            self._segment_path = lambda: "cvpdnSystemInfo"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.Cvpdnsysteminfo, ['cvpdntunneltotal', 'cvpdnsessiontotal', 'cvpdndenieduserstotal', 'cvpdnsystemnotifsessionenabled', 'cvpdnsystemclearsessions'], name, value)

        class Cvpdnsystemclearsessions(Enum):
            """
            Cvpdnsystemclearsessions (Enum Class)

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



    class Cvpdnmultilinkinfo(Entity):
        """
        
        
        .. attribute:: cvpdnbundleswithonelink
        
        	The total number of bundles comprised of a single link
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cvpdnbundleswithtwolinks
        
        	The total number of bundles comprised of two links
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cvpdnbundleswithmorethantwolinks
        
        	The total number of bundles comprised of more than two links
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cvpdnbundlelastchanged
        
        	The value of the sysUpTime object when the contents of cvpdnBundleTable last changed
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.Cvpdnmultilinkinfo, self).__init__()

            self.yang_name = "cvpdnMultilinkInfo"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cvpdnbundleswithonelink', YLeaf(YType.uint32, 'cvpdnBundlesWithOneLink')),
                ('cvpdnbundleswithtwolinks', YLeaf(YType.uint32, 'cvpdnBundlesWithTwoLinks')),
                ('cvpdnbundleswithmorethantwolinks', YLeaf(YType.uint32, 'cvpdnBundlesWithMoreThanTwoLinks')),
                ('cvpdnbundlelastchanged', YLeaf(YType.uint32, 'cvpdnBundleLastChanged')),
            ])
            self.cvpdnbundleswithonelink = None
            self.cvpdnbundleswithtwolinks = None
            self.cvpdnbundleswithmorethantwolinks = None
            self.cvpdnbundlelastchanged = None
            self._segment_path = lambda: "cvpdnMultilinkInfo"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.Cvpdnmultilinkinfo, ['cvpdnbundleswithonelink', 'cvpdnbundleswithtwolinks', 'cvpdnbundleswithmorethantwolinks', 'cvpdnbundlelastchanged'], name, value)


    class Cvpdnsystemtable(Entity):
        """
        Table of information about the VPDN system for all tunnel
        types.
        
        .. attribute:: cvpdnsystementry
        
        	An entry in the table, containing information about a single type of VPDN tunnel
        	**type**\: list of  		 :py:class:`Cvpdnsystementry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdnsystemtable.Cvpdnsystementry>`
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.Cvpdnsystemtable, self).__init__()

            self.yang_name = "cvpdnSystemTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvpdnSystemEntry", ("cvpdnsystementry", CISCOVPDNMGMTMIB.Cvpdnsystemtable.Cvpdnsystementry))])
            self._leafs = OrderedDict()

            self.cvpdnsystementry = YList(self)
            self._segment_path = lambda: "cvpdnSystemTable"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.Cvpdnsystemtable, [], name, value)


        class Cvpdnsystementry(Entity):
            """
            An entry in the table, containing information about a
            single type of VPDN tunnel.
            
            .. attribute:: cvpdnsystemtunneltype  (key)
            
            	The tunnel type.  This is the tunnel protocol
            	**type**\:  :py:class:`TunnelType <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.TunnelType>`
            
            .. attribute:: cvpdnsystemtunneltotal
            
            	The total number of VPDN tunnels that are currently active of this tunnel type
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: tunnels
            
            .. attribute:: cvpdnsystemsessiontotal
            
            	The total number of active sessions in all the active VPDN tunnels of this tunnel type
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: cvpdnsystemdenieduserstotal
            
            	The total number of denied user attempts to all the VPDN tunnels of this tunnel type since last system re\-initialization
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: attempts
            
            .. attribute:: cvpdnsysteminitialconnreq
            
            	The total number tunnel connection attempts on all the VPDN tunnels of this tunnel type since last system re\-initialization
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: attempts
            
            .. attribute:: cvpdnsystemsuccessconnreq
            
            	The total number tunnel Successful connection attempts in VPDN tunnels of this tunnel type since last system re\-initialization
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: attempts
            
            .. attribute:: cvpdnsystemfailedconnreq
            
            	The total number tunnel Failed connection attempts in VPDN tunnels of this tunnel type since last system re\-initialization
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: attempts
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CISCOVPDNMGMTMIB.Cvpdnsystemtable.Cvpdnsystementry, self).__init__()

                self.yang_name = "cvpdnSystemEntry"
                self.yang_parent_name = "cvpdnSystemTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvpdnsystemtunneltype']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvpdnsystemtunneltype', YLeaf(YType.enumeration, 'cvpdnSystemTunnelType')),
                    ('cvpdnsystemtunneltotal', YLeaf(YType.uint32, 'cvpdnSystemTunnelTotal')),
                    ('cvpdnsystemsessiontotal', YLeaf(YType.uint32, 'cvpdnSystemSessionTotal')),
                    ('cvpdnsystemdenieduserstotal', YLeaf(YType.uint32, 'cvpdnSystemDeniedUsersTotal')),
                    ('cvpdnsysteminitialconnreq', YLeaf(YType.uint32, 'cvpdnSystemInitialConnReq')),
                    ('cvpdnsystemsuccessconnreq', YLeaf(YType.uint32, 'cvpdnSystemSuccessConnReq')),
                    ('cvpdnsystemfailedconnreq', YLeaf(YType.uint32, 'cvpdnSystemFailedConnReq')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVPDNMGMTMIB.Cvpdnsystemtable.Cvpdnsystementry, ['cvpdnsystemtunneltype', 'cvpdnsystemtunneltotal', 'cvpdnsystemsessiontotal', 'cvpdnsystemdenieduserstotal', 'cvpdnsysteminitialconnreq', 'cvpdnsystemsuccessconnreq', 'cvpdnsystemfailedconnreq'], name, value)


    class Cvpdntunneltable(Entity):
        """
        Table of information about the active VPDN tunnels.
        
        .. attribute:: cvpdntunnelentry
        
        	An entry in the table, containing information about a single active VPDN tunnel
        	**type**\: list of  		 :py:class:`Cvpdntunnelentry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdntunneltable.Cvpdntunnelentry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.Cvpdntunneltable, self).__init__()

            self.yang_name = "cvpdnTunnelTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvpdnTunnelEntry", ("cvpdntunnelentry", CISCOVPDNMGMTMIB.Cvpdntunneltable.Cvpdntunnelentry))])
            self._leafs = OrderedDict()

            self.cvpdntunnelentry = YList(self)
            self._segment_path = lambda: "cvpdnTunnelTable"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.Cvpdntunneltable, [], name, value)


        class Cvpdntunnelentry(Entity):
            """
            An entry in the table, containing information about a
            single active VPDN tunnel.
            
            .. attribute:: cvpdntunneltunnelid  (key)
            
            	The Tunnel ID of an active VPDN tunnel.  If it is the instigator of the tunnel, the ID is the HGW/LNS tunnel ID, otherwise it is the NAS/LAC tunnel ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelremotetunnelid
            
            	The remote Tunnel ID of an active VPDN tunnel.  If it is the instigator of the tunnel, the ID is the NAS/LAC tunnel ID, otherwise it is the HGW/LNS tunnel ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnellocalname
            
            	The local name of an active VPDN tunnel.  It will be the NAS/LAC name of the tunnel if the router serves as the NAS/LAC, or the HGW/LNS name of the tunnel if the system serves as the home gateway.  Typically, the local name is the configured host name of the router
            	**type**\: str
            
            	**length:** 1..255
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelremotename
            
            	The remote name of an active VPDN tunnel.  It will be the home gateway name of the tunnel if the system is a NAS/LAC, or the NAS/LAC name of the tunnel if the system serves as the home gateway
            	**type**\: str
            
            	**length:** 1..255
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelremoteendpointname
            
            	The remote end point name of an active VPDN tunnel. This name is either the domain name or the DNIS that this tunnel is projected with
            	**type**\: str
            
            	**length:** 1..255
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnellocalinitconnection
            
            	This object indicates whether the tunnel was generated locally or not
            	**type**\: bool
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelorigcause
            
            	The cause which originated an active VPDN tunnel.  The tunnel can be projected via domain name, DNIS or a stack group (SGBP)
            	**type**\:  :py:class:`Cvpdntunnelorigcause <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdntunneltable.Cvpdntunnelentry.Cvpdntunnelorigcause>`
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelstate
            
            	The current state of an active VPDN tunnel.  Each state code is explained below\:         unknown\: The current state of the tunnel is                 unknown.         opening\: The tunnel has just been instigated and                 is pending for a remote end reply to                 complete the process.         open\:    The tunnel is active.         closing\: The tunnel has just been shut down and                 is pending for the remote end to reply                 to complete the process
            	**type**\:  :py:class:`Cvpdntunnelstate <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdntunneltable.Cvpdntunnelentry.Cvpdntunnelstate>`
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelactivesessions
            
            	The total number of active session currently in the tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunneldeniedusers
            
            	A count of the accumulated total of denied users for the tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsoftshut
            
            	A VPDN tunnel can be put into a soft shut state to prevent any new user session to be added.  This object specifies whether this tunnel has been soft shut
            	**type**\: bool
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelnetworkservicetype
            
            	The type of network service used in the active tunnel. For now it is IP only
            	**type**\:  :py:class:`Cvpdntunnelnetworkservicetype <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdntunneltable.Cvpdntunnelentry.Cvpdntunnelnetworkservicetype>`
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnellocalipaddress
            
            	The local IP address of the tunnel.  This IP address is that of the interface at the local end of the tunnel
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsourceipaddress
            
            	The source IP address of the tunnel.  This IP address is the user configurable IP address for Stack Group Biding Protocol (SGBP) via the CLI command\: vpdn source\-ip
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelremoteipaddress
            
            	The remote IP address of the tunnel.  This IP address is that of the interface at the remote end of the tunnel
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CISCOVPDNMGMTMIB.Cvpdntunneltable.Cvpdntunnelentry, self).__init__()

                self.yang_name = "cvpdnTunnelEntry"
                self.yang_parent_name = "cvpdnTunnelTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvpdntunneltunnelid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvpdntunneltunnelid', YLeaf(YType.uint32, 'cvpdnTunnelTunnelId')),
                    ('cvpdntunnelremotetunnelid', YLeaf(YType.uint32, 'cvpdnTunnelRemoteTunnelId')),
                    ('cvpdntunnellocalname', YLeaf(YType.str, 'cvpdnTunnelLocalName')),
                    ('cvpdntunnelremotename', YLeaf(YType.str, 'cvpdnTunnelRemoteName')),
                    ('cvpdntunnelremoteendpointname', YLeaf(YType.str, 'cvpdnTunnelRemoteEndpointName')),
                    ('cvpdntunnellocalinitconnection', YLeaf(YType.boolean, 'cvpdnTunnelLocalInitConnection')),
                    ('cvpdntunnelorigcause', YLeaf(YType.enumeration, 'cvpdnTunnelOrigCause')),
                    ('cvpdntunnelstate', YLeaf(YType.enumeration, 'cvpdnTunnelState')),
                    ('cvpdntunnelactivesessions', YLeaf(YType.uint32, 'cvpdnTunnelActiveSessions')),
                    ('cvpdntunneldeniedusers', YLeaf(YType.uint32, 'cvpdnTunnelDeniedUsers')),
                    ('cvpdntunnelsoftshut', YLeaf(YType.boolean, 'cvpdnTunnelSoftshut')),
                    ('cvpdntunnelnetworkservicetype', YLeaf(YType.enumeration, 'cvpdnTunnelNetworkServiceType')),
                    ('cvpdntunnellocalipaddress', YLeaf(YType.str, 'cvpdnTunnelLocalIpAddress')),
                    ('cvpdntunnelsourceipaddress', YLeaf(YType.str, 'cvpdnTunnelSourceIpAddress')),
                    ('cvpdntunnelremoteipaddress', YLeaf(YType.str, 'cvpdnTunnelRemoteIpAddress')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVPDNMGMTMIB.Cvpdntunneltable.Cvpdntunnelentry, ['cvpdntunneltunnelid', 'cvpdntunnelremotetunnelid', 'cvpdntunnellocalname', 'cvpdntunnelremotename', 'cvpdntunnelremoteendpointname', 'cvpdntunnellocalinitconnection', 'cvpdntunnelorigcause', 'cvpdntunnelstate', 'cvpdntunnelactivesessions', 'cvpdntunneldeniedusers', 'cvpdntunnelsoftshut', 'cvpdntunnelnetworkservicetype', 'cvpdntunnellocalipaddress', 'cvpdntunnelsourceipaddress', 'cvpdntunnelremoteipaddress'], name, value)

            class Cvpdntunnelnetworkservicetype(Enum):
                """
                Cvpdntunnelnetworkservicetype (Enum Class)

                The type of network service used in the active tunnel.

                For now it is IP only.

                .. data:: ip = 1

                """

                ip = Enum.YLeaf(1, "ip")


            class Cvpdntunnelorigcause(Enum):
                """
                Cvpdntunnelorigcause (Enum Class)

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


            class Cvpdntunnelstate(Enum):
                """
                Cvpdntunnelstate (Enum Class)

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



    class Cvpdntunnelattrtable(Entity):
        """
        Table of information about the active VPDN tunnels.  An
        entry is added to the table when a new tunnel is initiated
        and removed from the table when the tunnel is terminated.
        
        .. attribute:: cvpdntunnelattrentry
        
        	An entry in the table, containing information about a single active VPDN tunnel
        	**type**\: list of  		 :py:class:`Cvpdntunnelattrentry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdntunnelattrtable.Cvpdntunnelattrentry>`
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.Cvpdntunnelattrtable, self).__init__()

            self.yang_name = "cvpdnTunnelAttrTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvpdnTunnelAttrEntry", ("cvpdntunnelattrentry", CISCOVPDNMGMTMIB.Cvpdntunnelattrtable.Cvpdntunnelattrentry))])
            self._leafs = OrderedDict()

            self.cvpdntunnelattrentry = YList(self)
            self._segment_path = lambda: "cvpdnTunnelAttrTable"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.Cvpdntunnelattrtable, [], name, value)


        class Cvpdntunnelattrentry(Entity):
            """
            An entry in the table, containing information about a
            single active VPDN tunnel.
            
            .. attribute:: cvpdnsystemtunneltype  (key)
            
            	
            	**type**\:  :py:class:`TunnelType <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.TunnelType>`
            
            .. attribute:: cvpdntunnelattrtunnelid  (key)
            
            	The Tunnel ID of an active VPDN tunnel.  If this end is the instigator of the tunnel, the ID is the TS tunnel ID, otherwise it is the NAS tunnel ID.  Two distinct tunnels with the same tunnel ID may exist, but with different tunnel types
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cvpdntunnelattrremotetunnelid
            
            	The remote Tunnel ID of an active VPDN tunnel.  If this end is the instigator of the tunnel, the ID is the NAS tunnel ID, otherwise it is the TS tunnel ID
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cvpdntunnelattrlocalname
            
            	The local name of an active VPDN tunnel.  It will be the NAS name of the tunnel if the system serves as the NAS, or the TS name of the tunnel if the system serves as the tunnel server.  Typically, the local name is the configured host name of the system
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: cvpdntunnelattrremotename
            
            	The remote name of an active VPDN tunnel.  It will be the tunnel server name of the tunnel if the system is a NAS, or the NAS name of the tunnel if the system serves as the tunnel server
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: cvpdntunnelattrremoteendpointname
            
            	The remote end point name of an active VPDN tunnel.  This name is either the domain name or the DNIS that this tunnel is projected with
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: cvpdntunnelattrlocalinitconnection
            
            	This object indicates whether the tunnel was originated locally or not.  If it's true, the tunnel was originated locally
            	**type**\: bool
            
            .. attribute:: cvpdntunnelattrorigcause
            
            	The cause which originated an active VPDN tunnel.  The tunnel can be projected via domain name, DNIS, stack group, or L2 Xconnect
            	**type**\:  :py:class:`Cvpdntunnelattrorigcause <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdntunnelattrtable.Cvpdntunnelattrentry.Cvpdntunnelattrorigcause>`
            
            .. attribute:: cvpdntunnelattrstate
            
            	The current state of an active VPDN tunnel. Tunnels of type l2f will have states with the 'l2f' prefix. Tunnels of type l2tp will have states with the 'l2tp' prefix. Tunnels of type pptp will have states with the 'pptp' prefix.  Each state code is explained below\:      unknown\:            The current state of the tunnel is                         unknown.      l2fOpening\:         The tunnel has just been initiated                         and is pending for a remote end                         reply to complete the process.      l2fOpenWait\:        This end received a tunnel open                         request from the remote end and is                         waiting for the tunnel to be                         established.      l2fOpen\:            The tunnel is active.      l2fClosing\:         This end received a tunnel close                         request.      l2fCloseWait\:       The tunnel has just been shut down                         and is pending for the remote end                         to reply to complete the process.      l2tpIdle\:           No tunnel is initiated yet.      l2tpWaitCtlReply\:   The tunnel has been initiated and                         is pending for a remote end reply                         to complete the process.      l2tpEstablished\:    The tunnel is active.      l2tpShuttingDown\:   The tunnel is in progress of                         shutting down.      l2tpNoSessionLeft\:  There is no session left in the                         tunnel.      pptpIdle\:           No tunnel is initiated yet.      pptpWaitConnect\:    The tunnel is waiting for a TCP                         connection.      pptpWaitCtlRequest\: The tunnel has been initiated and                         is pending for a remote end                         request.      pptpWaitCtlReply\:   The tunnel has been initiated and                         is pending for a remote end reply.      pptpEstablished\:    The tunnel is active.      pptpWaitStopReply\:  The tunnel is being shut down and                         is pending for a remote end reply.      pptpTerminal\:       The tunnel has been shut down
            	**type**\:  :py:class:`Cvpdntunnelattrstate <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdntunnelattrtable.Cvpdntunnelattrentry.Cvpdntunnelattrstate>`
            
            .. attribute:: cvpdntunnelattractivesessions
            
            	The total number of active session currently in the tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: cvpdntunnelattrdeniedusers
            
            	A count of the accumulated total of denied users for the tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: cvpdntunnelattrsoftshut
            
            	A VPDN tunnel can be put into a soft shut state to prevent any new session to be added.  This object specifies whether this tunnel has been soft shut.  If its true, it has been soft shut
            	**type**\: bool
            
            .. attribute:: cvpdntunnelattrnetworkservicetype
            
            	The type of network service used in the active tunnel
            	**type**\:  :py:class:`Cvpdntunnelattrnetworkservicetype <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdntunnelattrtable.Cvpdntunnelattrentry.Cvpdntunnelattrnetworkservicetype>`
            
            .. attribute:: cvpdntunnelattrlocalipaddress
            
            	The local IP address of the tunnel.  This IP address is that of the interface at the local end of the tunnel
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cvpdntunnelattrsourceipaddress
            
            	The source IP address of the tunnel.  This IP address is the user configurable IP address for Stack Group Biding Protocol
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cvpdntunnelattrremoteipaddress
            
            	The remote IP address of the tunnel.  This IP address is that of the interface at the remote end of the tunnel
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cvpdntunnelattrlocalinetaddresstype
            
            	Indicates the type of address contained in cvpdnTunnelAttrLocalInetAddress
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cvpdntunnelattrlocalinetaddress
            
            	The local IP address of the tunnel.  This IP address is that of the interface at the local end of the tunnel. The type of this address is determined by the value of  cvpdnTunnelAttrLocalInetAddressType
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cvpdntunnelattrsourceinetaddresstype
            
            	Indicates the type of address contained in cvpdnTunnelAttrSourceInetAddress
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cvpdntunnelattrsourceinetaddress
            
            	The source IP address of the tunnel.  This IP address is the user configurable IP address for Stack Group Biding Protocol.  The type of this address is determined by the  value of cvpdnTunnelAttrSourceInetAddressType
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cvpdntunnelattrremoteinetaddresstype
            
            	Indicates the type of address contained in cvpdnTunnelAttrRemoteInetAddress
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cvpdntunnelattrremoteinetaddress
            
            	The remote IP address of the tunnel.  This IP address is that of the interface at the remote end of the tunnel. The type of this address is determined by the value of  cvpdnTunnelAttrRemoteInetAddressType
            	**type**\: str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CISCOVPDNMGMTMIB.Cvpdntunnelattrtable.Cvpdntunnelattrentry, self).__init__()

                self.yang_name = "cvpdnTunnelAttrEntry"
                self.yang_parent_name = "cvpdnTunnelAttrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvpdnsystemtunneltype','cvpdntunnelattrtunnelid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvpdnsystemtunneltype', YLeaf(YType.enumeration, 'cvpdnSystemTunnelType')),
                    ('cvpdntunnelattrtunnelid', YLeaf(YType.int32, 'cvpdnTunnelAttrTunnelId')),
                    ('cvpdntunnelattrremotetunnelid', YLeaf(YType.int32, 'cvpdnTunnelAttrRemoteTunnelId')),
                    ('cvpdntunnelattrlocalname', YLeaf(YType.str, 'cvpdnTunnelAttrLocalName')),
                    ('cvpdntunnelattrremotename', YLeaf(YType.str, 'cvpdnTunnelAttrRemoteName')),
                    ('cvpdntunnelattrremoteendpointname', YLeaf(YType.str, 'cvpdnTunnelAttrRemoteEndpointName')),
                    ('cvpdntunnelattrlocalinitconnection', YLeaf(YType.boolean, 'cvpdnTunnelAttrLocalInitConnection')),
                    ('cvpdntunnelattrorigcause', YLeaf(YType.enumeration, 'cvpdnTunnelAttrOrigCause')),
                    ('cvpdntunnelattrstate', YLeaf(YType.enumeration, 'cvpdnTunnelAttrState')),
                    ('cvpdntunnelattractivesessions', YLeaf(YType.uint32, 'cvpdnTunnelAttrActiveSessions')),
                    ('cvpdntunnelattrdeniedusers', YLeaf(YType.uint32, 'cvpdnTunnelAttrDeniedUsers')),
                    ('cvpdntunnelattrsoftshut', YLeaf(YType.boolean, 'cvpdnTunnelAttrSoftshut')),
                    ('cvpdntunnelattrnetworkservicetype', YLeaf(YType.enumeration, 'cvpdnTunnelAttrNetworkServiceType')),
                    ('cvpdntunnelattrlocalipaddress', YLeaf(YType.str, 'cvpdnTunnelAttrLocalIpAddress')),
                    ('cvpdntunnelattrsourceipaddress', YLeaf(YType.str, 'cvpdnTunnelAttrSourceIpAddress')),
                    ('cvpdntunnelattrremoteipaddress', YLeaf(YType.str, 'cvpdnTunnelAttrRemoteIpAddress')),
                    ('cvpdntunnelattrlocalinetaddresstype', YLeaf(YType.enumeration, 'cvpdnTunnelAttrLocalInetAddressType')),
                    ('cvpdntunnelattrlocalinetaddress', YLeaf(YType.str, 'cvpdnTunnelAttrLocalInetAddress')),
                    ('cvpdntunnelattrsourceinetaddresstype', YLeaf(YType.enumeration, 'cvpdnTunnelAttrSourceInetAddressType')),
                    ('cvpdntunnelattrsourceinetaddress', YLeaf(YType.str, 'cvpdnTunnelAttrSourceInetAddress')),
                    ('cvpdntunnelattrremoteinetaddresstype', YLeaf(YType.enumeration, 'cvpdnTunnelAttrRemoteInetAddressType')),
                    ('cvpdntunnelattrremoteinetaddress', YLeaf(YType.str, 'cvpdnTunnelAttrRemoteInetAddress')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVPDNMGMTMIB.Cvpdntunnelattrtable.Cvpdntunnelattrentry, ['cvpdnsystemtunneltype', 'cvpdntunnelattrtunnelid', 'cvpdntunnelattrremotetunnelid', 'cvpdntunnelattrlocalname', 'cvpdntunnelattrremotename', 'cvpdntunnelattrremoteendpointname', 'cvpdntunnelattrlocalinitconnection', 'cvpdntunnelattrorigcause', 'cvpdntunnelattrstate', 'cvpdntunnelattractivesessions', 'cvpdntunnelattrdeniedusers', 'cvpdntunnelattrsoftshut', 'cvpdntunnelattrnetworkservicetype', 'cvpdntunnelattrlocalipaddress', 'cvpdntunnelattrsourceipaddress', 'cvpdntunnelattrremoteipaddress', 'cvpdntunnelattrlocalinetaddresstype', 'cvpdntunnelattrlocalinetaddress', 'cvpdntunnelattrsourceinetaddresstype', 'cvpdntunnelattrsourceinetaddress', 'cvpdntunnelattrremoteinetaddresstype', 'cvpdntunnelattrremoteinetaddress'], name, value)

            class Cvpdntunnelattrnetworkservicetype(Enum):
                """
                Cvpdntunnelattrnetworkservicetype (Enum Class)

                The type of network service used in the active tunnel.

                .. data:: ip = 1

                """

                ip = Enum.YLeaf(1, "ip")


            class Cvpdntunnelattrorigcause(Enum):
                """
                Cvpdntunnelattrorigcause (Enum Class)

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


            class Cvpdntunnelattrstate(Enum):
                """
                Cvpdntunnelattrstate (Enum Class)

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



    class Cvpdntunnelsessiontable(Entity):
        """
        Table of information about individual user sessions
        within the active tunnels.  Entry is added to the table
        when new user session is initiated and be removed from
        the table when the user session is terminated.
        
        .. attribute:: cvpdntunnelsessionentry
        
        	An entry in the table, containing information about a single user session within the tunnel
        	**type**\: list of  		 :py:class:`Cvpdntunnelsessionentry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdntunnelsessiontable.Cvpdntunnelsessionentry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.Cvpdntunnelsessiontable, self).__init__()

            self.yang_name = "cvpdnTunnelSessionTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvpdnTunnelSessionEntry", ("cvpdntunnelsessionentry", CISCOVPDNMGMTMIB.Cvpdntunnelsessiontable.Cvpdntunnelsessionentry))])
            self._leafs = OrderedDict()

            self.cvpdntunnelsessionentry = YList(self)
            self._segment_path = lambda: "cvpdnTunnelSessionTable"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.Cvpdntunnelsessiontable, [], name, value)


        class Cvpdntunnelsessionentry(Entity):
            """
            An entry in the table, containing information about a
            single user session within the tunnel.
            
            .. attribute:: cvpdntunneltunnelid  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cvpdntunneltunnelid <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdntunneltable.Cvpdntunnelentry>`
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionid  (key)
            
            	The ID of an active VPDN tunnel user session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionusername
            
            	The name of the user of the user session
            	**type**\: str
            
            	**length:** 1..255
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionstate
            
            	The current state of an active user session.  Each state code is explained below\:      unknown\:          The current state of the tunnel's                       session is unknown.      opening\:          The user session has just been                       initiated through a tunnel and is                       pending for the remote end reply                       to complete the process.      open\:             The user session is active.      closing\:          The user session has just been                       closed and is pending for the                       remote end reply to complete the                       process.      waitingForTunnel\: The user session is in this state                       when the tunnel which this session                       is going through is still in                       CLOSED state.  It waits for the                       tunnel to become OPEN before the                       session is allow to be fully                       established
            	**type**\:  :py:class:`Cvpdntunnelsessionstate <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdntunnelsessiontable.Cvpdntunnelsessionentry.Cvpdntunnelsessionstate>`
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessioncallduration
            
            	This object specifies the call duration of the current active user session in value of system uptime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionpacketsout
            
            	The total number of output packets through this active user session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionbytesout
            
            	The total number of output bytes through this active user session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionpacketsin
            
            	The total number of input packets through this active user session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionbytesin
            
            	The total number of input bytes through this active user session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessiondevicetype
            
            	The type of physical devices that this user session is attached to for the local end of the tunnel.  The meaning of each device type is explained below\:      other\:              Any device that has not been                         defined.      asyncInternalModem\: Modem Pool device of an access                         server.      async\:              A regular asynchronous serial                         interface.      sync\:               A regular synchronous serial                         interface.      bchan\:              An ISDN call.      xdsl\:               Future application with xDSL                         devices.      cable\:              Future application with Cable                         modem devices
            	**type**\:  :py:class:`Cvpdntunnelsessiondevicetype <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdntunnelsessiontable.Cvpdntunnelsessionentry.Cvpdntunnelsessiondevicetype>`
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessiondevicecallerid
            
            	The incoming caller identification of the user.  It is the originating number that called into the device that initiates the user session.  This object can be empty since not all dial device can provide caller ID information
            	**type**\: str
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessiondevicephyid
            
            	The device ID of the physical interface for the user session.  The object is the the interface index which points to the ifTable.  For virtual interface that is not in the ifTable, it will have zero value
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionmultilink
            
            	This object indicates whether the session is part of a multilink or not
            	**type**\: bool
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionmodemslotindex
            
            	The Modem Pool database slot index if it is associated with this user session.  Only a session with device of type asyncInternalModem will have a valid value for this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionmodemportindex
            
            	The Modem Pool database port index if it is associated with this user session.  Only a session with a device of type asyncInternalModem will have a valid value for this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionds1slotindex
            
            	The DS1 database slot index if it is associated with this user session.  Only a session with a device of type asyncInternalModem will have a valid value for this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionds1portindex
            
            	The DS1 database port index if it is associated with this user session.  Only a session with a device of type asyncInternalModem will have a a valid value for this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionds1channelindex
            
            	The DS1 database channel index if it is associated with this user session.  Only a session over a device of type asyncInternalModem will have a valid value for this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionmodemcallstarttime
            
            	The start time of the current modem call.  Only a session with a  device of type asyncInternalModem will have a valid value for this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionmodemcallstartindex
            
            	Arbitrary small integer to distinguish modem calls that occurred at the same time tick.  Only session over device asyncInternalModem will have a valid value for this object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CISCOVPDNMGMTMIB.Cvpdntunnelsessiontable.Cvpdntunnelsessionentry, self).__init__()

                self.yang_name = "cvpdnTunnelSessionEntry"
                self.yang_parent_name = "cvpdnTunnelSessionTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvpdntunneltunnelid','cvpdntunnelsessionid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvpdntunneltunnelid', YLeaf(YType.str, 'cvpdnTunnelTunnelId')),
                    ('cvpdntunnelsessionid', YLeaf(YType.uint32, 'cvpdnTunnelSessionId')),
                    ('cvpdntunnelsessionusername', YLeaf(YType.str, 'cvpdnTunnelSessionUserName')),
                    ('cvpdntunnelsessionstate', YLeaf(YType.enumeration, 'cvpdnTunnelSessionState')),
                    ('cvpdntunnelsessioncallduration', YLeaf(YType.uint32, 'cvpdnTunnelSessionCallDuration')),
                    ('cvpdntunnelsessionpacketsout', YLeaf(YType.uint32, 'cvpdnTunnelSessionPacketsOut')),
                    ('cvpdntunnelsessionbytesout', YLeaf(YType.uint32, 'cvpdnTunnelSessionBytesOut')),
                    ('cvpdntunnelsessionpacketsin', YLeaf(YType.uint32, 'cvpdnTunnelSessionPacketsIn')),
                    ('cvpdntunnelsessionbytesin', YLeaf(YType.uint32, 'cvpdnTunnelSessionBytesIn')),
                    ('cvpdntunnelsessiondevicetype', YLeaf(YType.enumeration, 'cvpdnTunnelSessionDeviceType')),
                    ('cvpdntunnelsessiondevicecallerid', YLeaf(YType.str, 'cvpdnTunnelSessionDeviceCallerId')),
                    ('cvpdntunnelsessiondevicephyid', YLeaf(YType.int32, 'cvpdnTunnelSessionDevicePhyId')),
                    ('cvpdntunnelsessionmultilink', YLeaf(YType.boolean, 'cvpdnTunnelSessionMultilink')),
                    ('cvpdntunnelsessionmodemslotindex', YLeaf(YType.uint32, 'cvpdnTunnelSessionModemSlotIndex')),
                    ('cvpdntunnelsessionmodemportindex', YLeaf(YType.uint32, 'cvpdnTunnelSessionModemPortIndex')),
                    ('cvpdntunnelsessionds1slotindex', YLeaf(YType.uint32, 'cvpdnTunnelSessionDS1SlotIndex')),
                    ('cvpdntunnelsessionds1portindex', YLeaf(YType.uint32, 'cvpdnTunnelSessionDS1PortIndex')),
                    ('cvpdntunnelsessionds1channelindex', YLeaf(YType.uint32, 'cvpdnTunnelSessionDS1ChannelIndex')),
                    ('cvpdntunnelsessionmodemcallstarttime', YLeaf(YType.uint32, 'cvpdnTunnelSessionModemCallStartTime')),
                    ('cvpdntunnelsessionmodemcallstartindex', YLeaf(YType.uint32, 'cvpdnTunnelSessionModemCallStartIndex')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVPDNMGMTMIB.Cvpdntunnelsessiontable.Cvpdntunnelsessionentry, ['cvpdntunneltunnelid', 'cvpdntunnelsessionid', 'cvpdntunnelsessionusername', 'cvpdntunnelsessionstate', 'cvpdntunnelsessioncallduration', 'cvpdntunnelsessionpacketsout', 'cvpdntunnelsessionbytesout', 'cvpdntunnelsessionpacketsin', 'cvpdntunnelsessionbytesin', 'cvpdntunnelsessiondevicetype', 'cvpdntunnelsessiondevicecallerid', 'cvpdntunnelsessiondevicephyid', 'cvpdntunnelsessionmultilink', 'cvpdntunnelsessionmodemslotindex', 'cvpdntunnelsessionmodemportindex', 'cvpdntunnelsessionds1slotindex', 'cvpdntunnelsessionds1portindex', 'cvpdntunnelsessionds1channelindex', 'cvpdntunnelsessionmodemcallstarttime', 'cvpdntunnelsessionmodemcallstartindex'], name, value)

            class Cvpdntunnelsessiondevicetype(Enum):
                """
                Cvpdntunnelsessiondevicetype (Enum Class)

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


            class Cvpdntunnelsessionstate(Enum):
                """
                Cvpdntunnelsessionstate (Enum Class)

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



    class Cvpdnsessionattrtable(Entity):
        """
        Table of information about individual sessions within the
        active tunnels.  An entry is added to the table when a new
        session is initiated and removed from the table when the
        session is terminated.
        
        .. attribute:: cvpdnsessionattrentry
        
        	An entry in the table, containing information about a single session within the tunnel
        	**type**\: list of  		 :py:class:`Cvpdnsessionattrentry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdnsessionattrtable.Cvpdnsessionattrentry>`
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.Cvpdnsessionattrtable, self).__init__()

            self.yang_name = "cvpdnSessionAttrTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvpdnSessionAttrEntry", ("cvpdnsessionattrentry", CISCOVPDNMGMTMIB.Cvpdnsessionattrtable.Cvpdnsessionattrentry))])
            self._leafs = OrderedDict()

            self.cvpdnsessionattrentry = YList(self)
            self._segment_path = lambda: "cvpdnSessionAttrTable"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.Cvpdnsessionattrtable, [], name, value)


        class Cvpdnsessionattrentry(Entity):
            """
            An entry in the table, containing information about a
            single session within the tunnel.
            
            .. attribute:: cvpdnsystemtunneltype  (key)
            
            	
            	**type**\:  :py:class:`TunnelType <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.TunnelType>`
            
            .. attribute:: cvpdntunnelattrtunnelid  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`cvpdntunnelattrtunnelid <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdntunnelattrtable.Cvpdntunnelattrentry>`
            
            .. attribute:: cvpdnsessionattrsessionid  (key)
            
            	The ID of an active VPDN session
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cvpdnsessionattrusername
            
            	The name of the user of the session
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: cvpdnsessionattrstate
            
            	The current state of a tunnel session. L2F tunnel sessions will have states with the 'l2f' prefix. L2TP tunnel sessions will have states with the 'l2tp' prefix.  Each state code is explained below\:      unknown\:             The current state of the tunnel's                          session is unknown.      l2fOpening\:          The session has just been                          initiated through a tunnel and is                          pending for the remote end reply                          to complete the process.      l2fOpen\:             The session is active.      l2fCloseWait\:        The session has just been closed                          and is pending for the remote end                          reply to complete the process.      l2fWaitingForTunnel\: The session is in this state when                          the tunnel which this session is                          going through is still in CLOSED                          state.  It waits for the tunnel to                          become OPEN before the session is                          allowed to be fully established.      l2tpIdle\:            No session is initiated yet.      l2tpWaitingTunnel\:   The session is waiting for the                          tunnel to be established.      l2tpWaitReply\:       The session has been initiated and                          is pending for the remote end                          reply to complete the process.      l2tpWaitConnect\:     This end has acknowledged a                          connection request and is waiting                          for the remote end to connect.      l2tpEstablished\:     The session is active.      l2tpShuttingDown\:    The session is in progress of                          shutting down.      pptpWaitVAccess\:     The session is waiting for the                          creation of a virtual access                          interface.      pptpPacEstablished\:  The session is active.      pptpWaitTunnel\:      The session is waiting for the                          tunnel to be established.      pptpWaitOCRP\:        The session has been initiated and                          is pending for the remote end                          reply to complete the process.      pptpPnsEstablished\:  The session is active.      pptpWaitCallDisc\:    Session shutdown is in progress
            	**type**\:  :py:class:`Cvpdnsessionattrstate <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdnsessionattrtable.Cvpdnsessionattrentry.Cvpdnsessionattrstate>`
            
            .. attribute:: cvpdnsessionattrcallduration
            
            	This object specifies the call duration of the current active session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrpacketsout
            
            	The total number of output packets through this active session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cvpdnsessionattrbytesout
            
            	The total number of output bytes through this active session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cvpdnsessionattrpacketsin
            
            	The total number of input packets through this active session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cvpdnsessionattrbytesin
            
            	The total number of input bytes through this active session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cvpdnsessionattrdevicetype
            
            	The type of physical devices that this session is attached to for the local end of the tunnel.  The meaning of each device type is explained below\:      other\:              Any device that has not been                         defined.      asyncInternalModem\: Modem Pool device of an access                         server.      async\:              A regular asynchronous serial                         interface.      sync\:               A regular synchronous serial                         interface.      bchan\:              An ISDN call.      xdsl\:               xDSL interface.      cable\:              cable modem interface
            	**type**\:  :py:class:`Cvpdnsessionattrdevicetype <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdnsessionattrtable.Cvpdnsessionattrentry.Cvpdnsessionattrdevicetype>`
            
            .. attribute:: cvpdnsessionattrdevicecallerid
            
            	The incoming caller identification of the user.  It is the originating number that called into the device that initiates the session.  This object can be empty since not all dial devices can provide caller ID information
            	**type**\: str
            
            .. attribute:: cvpdnsessionattrdevicephyid
            
            	The device ID of the physical interface for the session. The object is the the interface index which points to the ifTable.  For virtual interfaces that are not in the ifTable, the value will be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cvpdnsessionattrmultilink
            
            	This object indicates whether the session is part of a multilink PPP bundle, even if there is only one link or session in the bundle.  If it is multilink PPP, the value is true
            	**type**\: bool
            
            .. attribute:: cvpdnsessionattrmodemslotindex
            
            	The Modem Pool database slot index if it is associated with this session.  Only a session with device of type 'asyncInternalModem' will have a valid value for this object; otherwise, it is not instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrmodemportindex
            
            	The Modem Pool database port index if it is associated with this session.  Only a session with a device of type 'asyncInternalModem' will have a valid value for this object; otherwise, it is not instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrds1slotindex
            
            	The DS1 database slot index if it is associated with this session.  Only a session with a device of type 'asyncInternalModem' will have a valid value for this object; otherwise it is not instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrds1portindex
            
            	The DS1 database port index if it is associated with this session.  Only a session with a device of type 'asyncInternalModem' will have a valid value for this object; otherwise it is not instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrds1channelindex
            
            	The DS1 database channel index if it is associated with this session.  Only a session over a device of type 'asyncInternalModem' will have a valid value for this object; otherwise it is not instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrmodemcallstarttime
            
            	The start time of the current modem call.  Only a session with a device of type 'asyncInternalModem' will have a valid value for this object; otherwise, it is not instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrmodemcallstartindex
            
            	Arbitrary small integer to distinguish modem calls that occurred at the same time tick.  Only session over device 'asyncInternalModem' will have a valid value for this object; otherwise, it is not instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrvirtualcircuitid
            
            	The virtual circuit ID of an active Layer 2 VPN session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrsentpktsdropped
            
            	The total number of dropped packets that could not be sent into this active session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cvpdnsessionattrrecvpktsdropped
            
            	The total number of dropped packets that were received from this active session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cvpdnsessionattrmultilinkbundle
            
            	This object specifies the name of the multilink bundle to which this session belongs.  The value of this object is only valid when the value of cvpdnSessionAttrMultilink is 'true'.  If the value of cvpdnSessionAttrMultilink is 'false', then the value of this object will be the empty string
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cvpdnsessionattrmultilinkifindex
            
            	This object specifies the ifIndex of the multilink bundle to which this session belongs.  The value of this object is only valid when the value of cvpdnSessionAttrMultilink is 'true'.  If the value of cvpdnSessionAttrMultilink is 'false', then the value of this object will be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CISCOVPDNMGMTMIB.Cvpdnsessionattrtable.Cvpdnsessionattrentry, self).__init__()

                self.yang_name = "cvpdnSessionAttrEntry"
                self.yang_parent_name = "cvpdnSessionAttrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvpdnsystemtunneltype','cvpdntunnelattrtunnelid','cvpdnsessionattrsessionid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvpdnsystemtunneltype', YLeaf(YType.enumeration, 'cvpdnSystemTunnelType')),
                    ('cvpdntunnelattrtunnelid', YLeaf(YType.str, 'cvpdnTunnelAttrTunnelId')),
                    ('cvpdnsessionattrsessionid', YLeaf(YType.int32, 'cvpdnSessionAttrSessionId')),
                    ('cvpdnsessionattrusername', YLeaf(YType.str, 'cvpdnSessionAttrUserName')),
                    ('cvpdnsessionattrstate', YLeaf(YType.enumeration, 'cvpdnSessionAttrState')),
                    ('cvpdnsessionattrcallduration', YLeaf(YType.uint32, 'cvpdnSessionAttrCallDuration')),
                    ('cvpdnsessionattrpacketsout', YLeaf(YType.uint32, 'cvpdnSessionAttrPacketsOut')),
                    ('cvpdnsessionattrbytesout', YLeaf(YType.uint32, 'cvpdnSessionAttrBytesOut')),
                    ('cvpdnsessionattrpacketsin', YLeaf(YType.uint32, 'cvpdnSessionAttrPacketsIn')),
                    ('cvpdnsessionattrbytesin', YLeaf(YType.uint32, 'cvpdnSessionAttrBytesIn')),
                    ('cvpdnsessionattrdevicetype', YLeaf(YType.enumeration, 'cvpdnSessionAttrDeviceType')),
                    ('cvpdnsessionattrdevicecallerid', YLeaf(YType.str, 'cvpdnSessionAttrDeviceCallerId')),
                    ('cvpdnsessionattrdevicephyid', YLeaf(YType.int32, 'cvpdnSessionAttrDevicePhyId')),
                    ('cvpdnsessionattrmultilink', YLeaf(YType.boolean, 'cvpdnSessionAttrMultilink')),
                    ('cvpdnsessionattrmodemslotindex', YLeaf(YType.uint32, 'cvpdnSessionAttrModemSlotIndex')),
                    ('cvpdnsessionattrmodemportindex', YLeaf(YType.uint32, 'cvpdnSessionAttrModemPortIndex')),
                    ('cvpdnsessionattrds1slotindex', YLeaf(YType.uint32, 'cvpdnSessionAttrDS1SlotIndex')),
                    ('cvpdnsessionattrds1portindex', YLeaf(YType.uint32, 'cvpdnSessionAttrDS1PortIndex')),
                    ('cvpdnsessionattrds1channelindex', YLeaf(YType.uint32, 'cvpdnSessionAttrDS1ChannelIndex')),
                    ('cvpdnsessionattrmodemcallstarttime', YLeaf(YType.uint32, 'cvpdnSessionAttrModemCallStartTime')),
                    ('cvpdnsessionattrmodemcallstartindex', YLeaf(YType.uint32, 'cvpdnSessionAttrModemCallStartIndex')),
                    ('cvpdnsessionattrvirtualcircuitid', YLeaf(YType.uint32, 'cvpdnSessionAttrVirtualCircuitID')),
                    ('cvpdnsessionattrsentpktsdropped', YLeaf(YType.uint32, 'cvpdnSessionAttrSentPktsDropped')),
                    ('cvpdnsessionattrrecvpktsdropped', YLeaf(YType.uint32, 'cvpdnSessionAttrRecvPktsDropped')),
                    ('cvpdnsessionattrmultilinkbundle', YLeaf(YType.str, 'cvpdnSessionAttrMultilinkBundle')),
                    ('cvpdnsessionattrmultilinkifindex', YLeaf(YType.int32, 'cvpdnSessionAttrMultilinkIfIndex')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVPDNMGMTMIB.Cvpdnsessionattrtable.Cvpdnsessionattrentry, ['cvpdnsystemtunneltype', 'cvpdntunnelattrtunnelid', 'cvpdnsessionattrsessionid', 'cvpdnsessionattrusername', 'cvpdnsessionattrstate', 'cvpdnsessionattrcallduration', 'cvpdnsessionattrpacketsout', 'cvpdnsessionattrbytesout', 'cvpdnsessionattrpacketsin', 'cvpdnsessionattrbytesin', 'cvpdnsessionattrdevicetype', 'cvpdnsessionattrdevicecallerid', 'cvpdnsessionattrdevicephyid', 'cvpdnsessionattrmultilink', 'cvpdnsessionattrmodemslotindex', 'cvpdnsessionattrmodemportindex', 'cvpdnsessionattrds1slotindex', 'cvpdnsessionattrds1portindex', 'cvpdnsessionattrds1channelindex', 'cvpdnsessionattrmodemcallstarttime', 'cvpdnsessionattrmodemcallstartindex', 'cvpdnsessionattrvirtualcircuitid', 'cvpdnsessionattrsentpktsdropped', 'cvpdnsessionattrrecvpktsdropped', 'cvpdnsessionattrmultilinkbundle', 'cvpdnsessionattrmultilinkifindex'], name, value)

            class Cvpdnsessionattrdevicetype(Enum):
                """
                Cvpdnsessionattrdevicetype (Enum Class)

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


            class Cvpdnsessionattrstate(Enum):
                """
                Cvpdnsessionattrstate (Enum Class)

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



    class Cvpdnusertofailhistinfotable(Entity):
        """
        Table of the record of failure objects which can be
        referenced by an user name.  Only a name that has a
        valid item in the Cisco IOS VPDN failure history table
        will yield a valid entry in this table.  The table has
        a maximum size of 50 entries.  Only the newest 50
        entries will be kept in the table.
        
        .. attribute:: cvpdnusertofailhistinfoentry
        
        	An entry in the table, containing failure history relevant to an user name
        	**type**\: list of  		 :py:class:`Cvpdnusertofailhistinfoentry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdnusertofailhistinfotable.Cvpdnusertofailhistinfoentry>`
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.Cvpdnusertofailhistinfotable, self).__init__()

            self.yang_name = "cvpdnUserToFailHistInfoTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvpdnUserToFailHistInfoEntry", ("cvpdnusertofailhistinfoentry", CISCOVPDNMGMTMIB.Cvpdnusertofailhistinfotable.Cvpdnusertofailhistinfoentry))])
            self._leafs = OrderedDict()

            self.cvpdnusertofailhistinfoentry = YList(self)
            self._segment_path = lambda: "cvpdnUserToFailHistInfoTable"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.Cvpdnusertofailhistinfotable, [], name, value)


        class Cvpdnusertofailhistinfoentry(Entity):
            """
            An entry in the table, containing failure history
            relevant to an user name.
            
            .. attribute:: cvpdnunametofailhistuname  (key)
            
            	The user name for this failure entry
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: cvpdnunametofailhisttunnelid  (key)
            
            	The Tunnel ID for this failure entry.  If it is the instigator of the tunnel, the ID is the TS tunnel ID, otherwise it is the NAS tunnel ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnunametofailhistuserid
            
            	The user ID of this failure entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnunametofailhistlocalinitconn
            
            	This object indicates whether the tunnel in which the failure occurred was generated locally or not
            	**type**\: bool
            
            .. attribute:: cvpdnunametofailhistlocalname
            
            	The local name of the VPDN tunnel in which the failure occurred.  It will be the NAS name of the tunnel if the system serves as the NAS, or the TS name of the tunnel if the system serves as the tunnel server.  The local name is the configured host name of the system.  This object can be empty if the failure occurred prior to successful tunnel projection, thus no source name will be available
            	**type**\: str
            
            .. attribute:: cvpdnunametofailhistremotename
            
            	The remote name of the VPDN tunnel in which the failure occurred.  It will be the tunnel server name of the tunnel if the system is a NAS, or the NAS name of the tunnel if the system serves as the tunnel server.  This object can be empty if the failure occurred prior to successful tunnel projection, thus no source name will be available
            	**type**\: str
            
            .. attribute:: cvpdnunametofailhistsourceip
            
            	The source IP address of the tunnel in which the failure occurred.  This IP address is that of the interface at the instigator end of the tunnel
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cvpdnunametofailhistdestip
            
            	The destination IP address of the tunnel in which the failure occurred.  This IP address is that of the interface at the receiver end of the tunnel
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cvpdnunametofailhistcount
            
            	This object is incremented when multiple failures has been experienced by this user on this tunnel.  Seeing a delta of >1 is an indication that the current failure record is the latest of a series of failures that has been recorded
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: failures
            
            .. attribute:: cvpdnunametofailhistfailtime
            
            	This object specifies the time when the failure is occurred
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnunametofailhistfailtype
            
            	The type of failure for the current failure record.  It comes in a form of a an ASCII string which describes the type of failure
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: cvpdnunametofailhistfailreason
            
            	The reason of failure for the current failure record
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: cvpdnunametofailhistsourceinettype
            
            	Indicates the type of address contained in cvpdnUnameToFailHistSourceInetAddr
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cvpdnunametofailhistsourceinetaddr
            
            	The source IP address of the tunnel in which the failure occurred.  This IP address is that of the interface at the instigator end of the tunnel.  The instigator end is the peer which initiates the tunnel estalishment.  The type of this address is determined by the value of cvpdnUnameToFailHistSourceInetType
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cvpdnunametofailhistdestinettype
            
            	Indicates the type of address contained in cvpdnUnameToFailHistDestInetAddr
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cvpdnunametofailhistdestinetaddr
            
            	The destination IP address of the tunnel in which the failure occurred.  This IP address is that of the interface at the receiver end of the tunnel.  The type  of this address is determined by the value of  cvpdnUnameToFailHistDestInetType
            	**type**\: str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CISCOVPDNMGMTMIB.Cvpdnusertofailhistinfotable.Cvpdnusertofailhistinfoentry, self).__init__()

                self.yang_name = "cvpdnUserToFailHistInfoEntry"
                self.yang_parent_name = "cvpdnUserToFailHistInfoTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvpdnunametofailhistuname','cvpdnunametofailhisttunnelid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvpdnunametofailhistuname', YLeaf(YType.str, 'cvpdnUnameToFailHistUname')),
                    ('cvpdnunametofailhisttunnelid', YLeaf(YType.uint32, 'cvpdnUnameToFailHistTunnelId')),
                    ('cvpdnunametofailhistuserid', YLeaf(YType.uint32, 'cvpdnUnameToFailHistUserId')),
                    ('cvpdnunametofailhistlocalinitconn', YLeaf(YType.boolean, 'cvpdnUnameToFailHistLocalInitConn')),
                    ('cvpdnunametofailhistlocalname', YLeaf(YType.str, 'cvpdnUnameToFailHistLocalName')),
                    ('cvpdnunametofailhistremotename', YLeaf(YType.str, 'cvpdnUnameToFailHistRemoteName')),
                    ('cvpdnunametofailhistsourceip', YLeaf(YType.str, 'cvpdnUnameToFailHistSourceIp')),
                    ('cvpdnunametofailhistdestip', YLeaf(YType.str, 'cvpdnUnameToFailHistDestIp')),
                    ('cvpdnunametofailhistcount', YLeaf(YType.uint32, 'cvpdnUnameToFailHistCount')),
                    ('cvpdnunametofailhistfailtime', YLeaf(YType.uint32, 'cvpdnUnameToFailHistFailTime')),
                    ('cvpdnunametofailhistfailtype', YLeaf(YType.str, 'cvpdnUnameToFailHistFailType')),
                    ('cvpdnunametofailhistfailreason', YLeaf(YType.str, 'cvpdnUnameToFailHistFailReason')),
                    ('cvpdnunametofailhistsourceinettype', YLeaf(YType.enumeration, 'cvpdnUnameToFailHistSourceInetType')),
                    ('cvpdnunametofailhistsourceinetaddr', YLeaf(YType.str, 'cvpdnUnameToFailHistSourceInetAddr')),
                    ('cvpdnunametofailhistdestinettype', YLeaf(YType.enumeration, 'cvpdnUnameToFailHistDestInetType')),
                    ('cvpdnunametofailhistdestinetaddr', YLeaf(YType.str, 'cvpdnUnameToFailHistDestInetAddr')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVPDNMGMTMIB.Cvpdnusertofailhistinfotable.Cvpdnusertofailhistinfoentry, ['cvpdnunametofailhistuname', 'cvpdnunametofailhisttunnelid', 'cvpdnunametofailhistuserid', 'cvpdnunametofailhistlocalinitconn', 'cvpdnunametofailhistlocalname', 'cvpdnunametofailhistremotename', 'cvpdnunametofailhistsourceip', 'cvpdnunametofailhistdestip', 'cvpdnunametofailhistcount', 'cvpdnunametofailhistfailtime', 'cvpdnunametofailhistfailtype', 'cvpdnunametofailhistfailreason', 'cvpdnunametofailhistsourceinettype', 'cvpdnunametofailhistsourceinetaddr', 'cvpdnunametofailhistdestinettype', 'cvpdnunametofailhistdestinetaddr'], name, value)


    class Cvpdntemplatetable(Entity):
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
        	**type**\: list of  		 :py:class:`Cvpdntemplateentry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdntemplatetable.Cvpdntemplateentry>`
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.Cvpdntemplatetable, self).__init__()

            self.yang_name = "cvpdnTemplateTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvpdnTemplateEntry", ("cvpdntemplateentry", CISCOVPDNMGMTMIB.Cvpdntemplatetable.Cvpdntemplateentry))])
            self._leafs = OrderedDict()

            self.cvpdntemplateentry = YList(self)
            self._segment_path = lambda: "cvpdnTemplateTable"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.Cvpdntemplatetable, [], name, value)


        class Cvpdntemplateentry(Entity):
            """
            An entry in the table, containing information about a
            single VPDN template.
            
            .. attribute:: cvpdntemplatename  (key)
            
            	The name of the VPDN template
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: cvpdntemplateactivesessions
            
            	The total number of active session in all groups associated with the template
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CISCOVPDNMGMTMIB.Cvpdntemplatetable.Cvpdntemplateentry, self).__init__()

                self.yang_name = "cvpdnTemplateEntry"
                self.yang_parent_name = "cvpdnTemplateTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvpdntemplatename']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvpdntemplatename', YLeaf(YType.str, 'cvpdnTemplateName')),
                    ('cvpdntemplateactivesessions', YLeaf(YType.uint32, 'cvpdnTemplateActiveSessions')),
                ])
                self.cvpdntemplatename = None
                self.cvpdntemplateactivesessions = None
                self._segment_path = lambda: "cvpdnTemplateEntry" + "[cvpdnTemplateName='" + str(self.cvpdntemplatename) + "']"
                self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/cvpdnTemplateTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVPDNMGMTMIB.Cvpdntemplatetable.Cvpdntemplateentry, ['cvpdntemplatename', 'cvpdntemplateactivesessions'], name, value)


    class Cvpdnbundletable(Entity):
        """
        Table that describes the multilink PPP attributes of the
        active VPDN sessions.
        
        .. attribute:: cvpdnbundleentry
        
        	An entry in this table represents an active multilink PPP bundle that belongs to a VPDN tunnel
        	**type**\: list of  		 :py:class:`Cvpdnbundleentry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdnbundletable.Cvpdnbundleentry>`
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.Cvpdnbundletable, self).__init__()

            self.yang_name = "cvpdnBundleTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvpdnBundleEntry", ("cvpdnbundleentry", CISCOVPDNMGMTMIB.Cvpdnbundletable.Cvpdnbundleentry))])
            self._leafs = OrderedDict()

            self.cvpdnbundleentry = YList(self)
            self._segment_path = lambda: "cvpdnBundleTable"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.Cvpdnbundletable, [], name, value)


        class Cvpdnbundleentry(Entity):
            """
            An entry in this table represents an active multilink PPP
            bundle that belongs to a VPDN tunnel.
            
            .. attribute:: cvpdnbundlename  (key)
            
            	The name of the multilink PPP bundle associated with a VPDN tunnel
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: cvpdnbundlelinkcount
            
            	The total number of active links in a multilink PPP bundle associated with a VPDN tunnel
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: links
            
            .. attribute:: cvpdnbundleendpointtype
            
            	The multilink PPP bundle discriminator type associated with a VPDN tunnel.  The value of this object represents the type of discriminator used in cvpdnBundleEndpoint.      none\:        No endpoint discriminator was supplied, the                  default value is being used.      hostname\:    The router's hostname is being used as                  discriminator.      string\:      User specified string is being used as                  discriminator.      macAddress\:  A MAC address as defined by the MacAddress                  textual convention is being used as                  discriminator.      ipV4Address\: An IP address as defined by the                  InetAddressIPv4 textual convention is being                  used as discriminator.      ipV6Address\: An IP address as defined by the                  InetAddressIPv6 textual convention is being                  used as discriminator.      phone\:       The PSTN phone number is being used as                  discriminator.      magicNumber\: A magic number is being used as                  discriminator
            	**type**\:  :py:class:`Cvpdnbundleendpointtype <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdnbundletable.Cvpdnbundleentry.Cvpdnbundleendpointtype>`
            
            	**status**\: deprecated
            
            .. attribute:: cvpdnbundleendpoint
            
            	Indicates the discriminator used in this bundle that is associated with a VPDN tunnel
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cvpdnbundlepeeripaddrtype
            
            	Indicates the type of address contained in cvpdnBundlePeerIpAddr
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cvpdnbundlepeeripaddr
            
            	The IP address of the multilink PPP peer in a VPDN tunnel
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cvpdnbundleendpointclass
            
            	The multilink PPP bundle discriminator class associated with a VPDN tunnel.  The value of this object represents the type of discriminator used in cvpdnBundleEndpoint
            	**type**\:  :py:class:`EndpointClass <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.EndpointClass>`
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CISCOVPDNMGMTMIB.Cvpdnbundletable.Cvpdnbundleentry, self).__init__()

                self.yang_name = "cvpdnBundleEntry"
                self.yang_parent_name = "cvpdnBundleTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvpdnbundlename']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvpdnbundlename', YLeaf(YType.str, 'cvpdnBundleName')),
                    ('cvpdnbundlelinkcount', YLeaf(YType.uint32, 'cvpdnBundleLinkCount')),
                    ('cvpdnbundleendpointtype', YLeaf(YType.enumeration, 'cvpdnBundleEndpointType')),
                    ('cvpdnbundleendpoint', YLeaf(YType.str, 'cvpdnBundleEndpoint')),
                    ('cvpdnbundlepeeripaddrtype', YLeaf(YType.enumeration, 'cvpdnBundlePeerIpAddrType')),
                    ('cvpdnbundlepeeripaddr', YLeaf(YType.str, 'cvpdnBundlePeerIpAddr')),
                    ('cvpdnbundleendpointclass', YLeaf(YType.enumeration, 'cvpdnBundleEndpointClass')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVPDNMGMTMIB.Cvpdnbundletable.Cvpdnbundleentry, ['cvpdnbundlename', 'cvpdnbundlelinkcount', 'cvpdnbundleendpointtype', 'cvpdnbundleendpoint', 'cvpdnbundlepeeripaddrtype', 'cvpdnbundlepeeripaddr', 'cvpdnbundleendpointclass'], name, value)

            class Cvpdnbundleendpointtype(Enum):
                """
                Cvpdnbundleendpointtype (Enum Class)

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



    class Cvpdnbundlechildtable(Entity):
        """
        A table that exposes the containment relationship between a
        multilink PPP bundle and a VPDN tunnel.
        
        .. attribute:: cvpdnbundlechildentry
        
        	An entry in this table represents a session that belongs to a VPDN tunnel and to a multilink PPP bundle
        	**type**\: list of  		 :py:class:`Cvpdnbundlechildentry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdnbundlechildtable.Cvpdnbundlechildentry>`
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CISCOVPDNMGMTMIB.Cvpdnbundlechildtable, self).__init__()

            self.yang_name = "cvpdnBundleChildTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cvpdnBundleChildEntry", ("cvpdnbundlechildentry", CISCOVPDNMGMTMIB.Cvpdnbundlechildtable.Cvpdnbundlechildentry))])
            self._leafs = OrderedDict()

            self.cvpdnbundlechildentry = YList(self)
            self._segment_path = lambda: "cvpdnBundleChildTable"
            self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOVPDNMGMTMIB.Cvpdnbundlechildtable, [], name, value)


        class Cvpdnbundlechildentry(Entity):
            """
            An entry in this table represents a session that belongs to
            a VPDN tunnel and to a multilink PPP bundle.
            
            .. attribute:: cvpdnbundlename  (key)
            
            	
            	**type**\: str
            
            	**length:** 1..64
            
            	**refers to**\:  :py:class:`cvpdnbundlename <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CISCOVPDNMGMTMIB.Cvpdnbundletable.Cvpdnbundleentry>`
            
            .. attribute:: cvpdnbundlechildtunneltype  (key)
            
            	The tunnel type.  This is the tunnel protocol of an active VPDN session that is associated with a multilink PPP bundle
            	**type**\:  :py:class:`TunnelType <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.TunnelType>`
            
            .. attribute:: cvpdnbundlechildtunnelid  (key)
            
            	The Tunnel ID of an active VPDN session that is associated with a multilink PPP bundle
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnbundlechildsessionid  (key)
            
            	The ID of an active VPDN session that is associated with a multilink PPP bundle
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CISCOVPDNMGMTMIB.Cvpdnbundlechildtable.Cvpdnbundlechildentry, self).__init__()

                self.yang_name = "cvpdnBundleChildEntry"
                self.yang_parent_name = "cvpdnBundleChildTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cvpdnbundlename','cvpdnbundlechildtunneltype','cvpdnbundlechildtunnelid','cvpdnbundlechildsessionid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cvpdnbundlename', YLeaf(YType.str, 'cvpdnBundleName')),
                    ('cvpdnbundlechildtunneltype', YLeaf(YType.enumeration, 'cvpdnBundleChildTunnelType')),
                    ('cvpdnbundlechildtunnelid', YLeaf(YType.uint32, 'cvpdnBundleChildTunnelId')),
                    ('cvpdnbundlechildsessionid', YLeaf(YType.uint32, 'cvpdnBundleChildSessionId')),
                ])
                self.cvpdnbundlename = None
                self.cvpdnbundlechildtunneltype = None
                self.cvpdnbundlechildtunnelid = None
                self.cvpdnbundlechildsessionid = None
                self._segment_path = lambda: "cvpdnBundleChildEntry" + "[cvpdnBundleName='" + str(self.cvpdnbundlename) + "']" + "[cvpdnBundleChildTunnelType='" + str(self.cvpdnbundlechildtunneltype) + "']" + "[cvpdnBundleChildTunnelId='" + str(self.cvpdnbundlechildtunnelid) + "']" + "[cvpdnBundleChildSessionId='" + str(self.cvpdnbundlechildsessionid) + "']"
                self._absolute_path = lambda: "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/cvpdnBundleChildTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOVPDNMGMTMIB.Cvpdnbundlechildtable.Cvpdnbundlechildentry, ['cvpdnbundlename', 'cvpdnbundlechildtunneltype', 'cvpdnbundlechildtunnelid', 'cvpdnbundlechildsessionid'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOVPDNMGMTMIB()
        return self._top_entity


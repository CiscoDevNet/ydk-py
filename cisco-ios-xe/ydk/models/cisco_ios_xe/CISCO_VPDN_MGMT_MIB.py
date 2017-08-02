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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Endpointclass(Enum):
    """
    Endpointclass

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


class Tunneltype(Enum):
    """
    Tunneltype

    The tunnel type.  This is the tunnel protocol of a VPDN

    tunnel.

    .. data:: l2f = 1

    .. data:: l2tp = 2

    .. data:: pptp = 3

    """

    l2f = Enum.YLeaf(1, "l2f")

    l2tp = Enum.YLeaf(2, "l2tp")

    pptp = Enum.YLeaf(3, "pptp")



class CiscoVpdnMgmtMib(Entity):
    """
    
    
    .. attribute:: ciscovpdnmgmtmibnotifs
    
    	
    	**type**\:   :py:class:`Ciscovpdnmgmtmibnotifs <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Ciscovpdnmgmtmibnotifs>`
    
    .. attribute:: cvpdnbundlechildtable
    
    	A table that exposes the containment relationship between a multilink PPP bundle and a VPDN tunnel
    	**type**\:   :py:class:`Cvpdnbundlechildtable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdnbundlechildtable>`
    
    .. attribute:: cvpdnbundletable
    
    	Table that describes the multilink PPP attributes of the active VPDN sessions
    	**type**\:   :py:class:`Cvpdnbundletable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdnbundletable>`
    
    .. attribute:: cvpdnmultilinkinfo
    
    	
    	**type**\:   :py:class:`Cvpdnmultilinkinfo <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdnmultilinkinfo>`
    
    .. attribute:: cvpdnsessionattrtable
    
    	Table of information about individual sessions within the active tunnels.  An entry is added to the table when a new session is initiated and removed from the table when the session is terminated
    	**type**\:   :py:class:`Cvpdnsessionattrtable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdnsessionattrtable>`
    
    .. attribute:: cvpdnsysteminfo
    
    	
    	**type**\:   :py:class:`Cvpdnsysteminfo <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdnsysteminfo>`
    
    .. attribute:: cvpdnsystemtable
    
    	Table of information about the VPDN system for all tunnel types
    	**type**\:   :py:class:`Cvpdnsystemtable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdnsystemtable>`
    
    .. attribute:: cvpdntemplatetable
    
    	Table of information about the VPDN templates.  The VPDN template is a grouping mechanism that allows configuration settings to be shared among multiple VPDN groups.  One such setting is a limit on the number of active sessions across all VPDN groups associated with the template.  The template table allows customers to monitor template\-wide information such as tracking the allocation of sessions across templates
    	**type**\:   :py:class:`Cvpdntemplatetable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdntemplatetable>`
    
    .. attribute:: cvpdntunnelattrtable
    
    	Table of information about the active VPDN tunnels.  An entry is added to the table when a new tunnel is initiated and removed from the table when the tunnel is terminated
    	**type**\:   :py:class:`Cvpdntunnelattrtable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdntunnelattrtable>`
    
    .. attribute:: cvpdntunnelsessiontable
    
    	Table of information about individual user sessions within the active tunnels.  Entry is added to the table when new user session is initiated and be removed from the table when the user session is terminated
    	**type**\:   :py:class:`Cvpdntunnelsessiontable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdntunnelsessiontable>`
    
    	**status**\: obsolete
    
    .. attribute:: cvpdntunneltable
    
    	Table of information about the active VPDN tunnels
    	**type**\:   :py:class:`Cvpdntunneltable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdntunneltable>`
    
    	**status**\: obsolete
    
    .. attribute:: cvpdnusertofailhistinfotable
    
    	Table of the record of failure objects which can be referenced by an user name.  Only a name that has a valid item in the Cisco IOS VPDN failure history table will yield a valid entry in this table.  The table has a maximum size of 50 entries.  Only the newest 50 entries will be kept in the table
    	**type**\:   :py:class:`Cvpdnusertofailhistinfotable <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdnusertofailhistinfotable>`
    
    

    """

    _prefix = 'CISCO-VPDN-MGMT-MIB'
    _revision = '2009-06-16'

    def __init__(self):
        super(CiscoVpdnMgmtMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-VPDN-MGMT-MIB"
        self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"

        self.ciscovpdnmgmtmibnotifs = CiscoVpdnMgmtMib.Ciscovpdnmgmtmibnotifs()
        self.ciscovpdnmgmtmibnotifs.parent = self
        self._children_name_map["ciscovpdnmgmtmibnotifs"] = "ciscoVpdnMgmtMIBNotifs"
        self._children_yang_names.add("ciscoVpdnMgmtMIBNotifs")

        self.cvpdnbundlechildtable = CiscoVpdnMgmtMib.Cvpdnbundlechildtable()
        self.cvpdnbundlechildtable.parent = self
        self._children_name_map["cvpdnbundlechildtable"] = "cvpdnBundleChildTable"
        self._children_yang_names.add("cvpdnBundleChildTable")

        self.cvpdnbundletable = CiscoVpdnMgmtMib.Cvpdnbundletable()
        self.cvpdnbundletable.parent = self
        self._children_name_map["cvpdnbundletable"] = "cvpdnBundleTable"
        self._children_yang_names.add("cvpdnBundleTable")

        self.cvpdnmultilinkinfo = CiscoVpdnMgmtMib.Cvpdnmultilinkinfo()
        self.cvpdnmultilinkinfo.parent = self
        self._children_name_map["cvpdnmultilinkinfo"] = "cvpdnMultilinkInfo"
        self._children_yang_names.add("cvpdnMultilinkInfo")

        self.cvpdnsessionattrtable = CiscoVpdnMgmtMib.Cvpdnsessionattrtable()
        self.cvpdnsessionattrtable.parent = self
        self._children_name_map["cvpdnsessionattrtable"] = "cvpdnSessionAttrTable"
        self._children_yang_names.add("cvpdnSessionAttrTable")

        self.cvpdnsysteminfo = CiscoVpdnMgmtMib.Cvpdnsysteminfo()
        self.cvpdnsysteminfo.parent = self
        self._children_name_map["cvpdnsysteminfo"] = "cvpdnSystemInfo"
        self._children_yang_names.add("cvpdnSystemInfo")

        self.cvpdnsystemtable = CiscoVpdnMgmtMib.Cvpdnsystemtable()
        self.cvpdnsystemtable.parent = self
        self._children_name_map["cvpdnsystemtable"] = "cvpdnSystemTable"
        self._children_yang_names.add("cvpdnSystemTable")

        self.cvpdntemplatetable = CiscoVpdnMgmtMib.Cvpdntemplatetable()
        self.cvpdntemplatetable.parent = self
        self._children_name_map["cvpdntemplatetable"] = "cvpdnTemplateTable"
        self._children_yang_names.add("cvpdnTemplateTable")

        self.cvpdntunnelattrtable = CiscoVpdnMgmtMib.Cvpdntunnelattrtable()
        self.cvpdntunnelattrtable.parent = self
        self._children_name_map["cvpdntunnelattrtable"] = "cvpdnTunnelAttrTable"
        self._children_yang_names.add("cvpdnTunnelAttrTable")

        self.cvpdntunnelsessiontable = CiscoVpdnMgmtMib.Cvpdntunnelsessiontable()
        self.cvpdntunnelsessiontable.parent = self
        self._children_name_map["cvpdntunnelsessiontable"] = "cvpdnTunnelSessionTable"
        self._children_yang_names.add("cvpdnTunnelSessionTable")

        self.cvpdntunneltable = CiscoVpdnMgmtMib.Cvpdntunneltable()
        self.cvpdntunneltable.parent = self
        self._children_name_map["cvpdntunneltable"] = "cvpdnTunnelTable"
        self._children_yang_names.add("cvpdnTunnelTable")

        self.cvpdnusertofailhistinfotable = CiscoVpdnMgmtMib.Cvpdnusertofailhistinfotable()
        self.cvpdnusertofailhistinfotable.parent = self
        self._children_name_map["cvpdnusertofailhistinfotable"] = "cvpdnUserToFailHistInfoTable"
        self._children_yang_names.add("cvpdnUserToFailHistInfoTable")


    class Ciscovpdnmgmtmibnotifs(Entity):
        """
        
        
        .. attribute:: cvpdnnotifsessionevent
        
        	Indicates the event that generated the L2X session notification.  The events are represented as follows\:  up\:     Session has come up.  down\:   Session has gone down.  pwUp\:   Pseudowire associated with this          session has come up.  pwDown\: Pseudowire associated with this          session has gone down
        	**type**\:   :py:class:`Cvpdnnotifsessionevent <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Ciscovpdnmgmtmibnotifs.Cvpdnnotifsessionevent>`
        
        .. attribute:: cvpdnnotifsessionid
        
        	This object contains the local session ID of the L2X session for which this notification has been generated
        	**type**\:  int
        
        	**range:** 0..65535
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CiscoVpdnMgmtMib.Ciscovpdnmgmtmibnotifs, self).__init__()

            self.yang_name = "ciscoVpdnMgmtMIBNotifs"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"

            self.cvpdnnotifsessionevent = YLeaf(YType.enumeration, "cvpdnNotifSessionEvent")

            self.cvpdnnotifsessionid = YLeaf(YType.int32, "cvpdnNotifSessionID")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cvpdnnotifsessionevent",
                            "cvpdnnotifsessionid") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoVpdnMgmtMib.Ciscovpdnmgmtmibnotifs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVpdnMgmtMib.Ciscovpdnmgmtmibnotifs, self).__setattr__(name, value)

        class Cvpdnnotifsessionevent(Enum):
            """
            Cvpdnnotifsessionevent

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


        def has_data(self):
            return (
                self.cvpdnnotifsessionevent.is_set or
                self.cvpdnnotifsessionid.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cvpdnnotifsessionevent.yfilter != YFilter.not_set or
                self.cvpdnnotifsessionid.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoVpdnMgmtMIBNotifs" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cvpdnnotifsessionevent.is_set or self.cvpdnnotifsessionevent.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvpdnnotifsessionevent.get_name_leafdata())
            if (self.cvpdnnotifsessionid.is_set or self.cvpdnnotifsessionid.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvpdnnotifsessionid.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvpdnNotifSessionEvent" or name == "cvpdnNotifSessionID"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cvpdnNotifSessionEvent"):
                self.cvpdnnotifsessionevent = value
                self.cvpdnnotifsessionevent.value_namespace = name_space
                self.cvpdnnotifsessionevent.value_namespace_prefix = name_space_prefix
            if(value_path == "cvpdnNotifSessionID"):
                self.cvpdnnotifsessionid = value
                self.cvpdnnotifsessionid.value_namespace = name_space
                self.cvpdnnotifsessionid.value_namespace_prefix = name_space_prefix


    class Cvpdnsysteminfo(Entity):
        """
        
        
        .. attribute:: cvpdndenieduserstotal
        
        	The total number of denied user attempts to all the active VPDN tunnels within this system
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: attempts
        
        	**status**\: obsolete
        
        .. attribute:: cvpdnsessiontotal
        
        	The total number of active users in all the active VPDN tunnels within this system
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: users
        
        	**status**\: obsolete
        
        .. attribute:: cvpdnsystemclearsessions
        
        	Clears all the sessions in a given tunnel type.  When reading this object, the value of 'none' will always be returned.  When setting these values, the following operations will be performed\:      none\: no operation.      all\:  clears all the sessions in all the tunnels.      l2f\:  clears all the L2F sessions.      l2tp\: clears all the L2TP sessions.      pptp\: clears all the PPTP sessions
        	**type**\:   :py:class:`Cvpdnsystemclearsessions <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdnsysteminfo.Cvpdnsystemclearsessions>`
        
        .. attribute:: cvpdnsystemnotifsessionenabled
        
        	Indicates whether Layer 2 VPN session notifications are enabled
        	**type**\:  bool
        
        .. attribute:: cvpdntunneltotal
        
        	The total number of VPDN tunnels that are currently active within this system
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: tunnels
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CiscoVpdnMgmtMib.Cvpdnsysteminfo, self).__init__()

            self.yang_name = "cvpdnSystemInfo"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"

            self.cvpdndenieduserstotal = YLeaf(YType.uint32, "cvpdnDeniedUsersTotal")

            self.cvpdnsessiontotal = YLeaf(YType.uint32, "cvpdnSessionTotal")

            self.cvpdnsystemclearsessions = YLeaf(YType.enumeration, "cvpdnSystemClearSessions")

            self.cvpdnsystemnotifsessionenabled = YLeaf(YType.boolean, "cvpdnSystemNotifSessionEnabled")

            self.cvpdntunneltotal = YLeaf(YType.uint32, "cvpdnTunnelTotal")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cvpdndenieduserstotal",
                            "cvpdnsessiontotal",
                            "cvpdnsystemclearsessions",
                            "cvpdnsystemnotifsessionenabled",
                            "cvpdntunneltotal") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoVpdnMgmtMib.Cvpdnsysteminfo, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVpdnMgmtMib.Cvpdnsysteminfo, self).__setattr__(name, value)

        class Cvpdnsystemclearsessions(Enum):
            """
            Cvpdnsystemclearsessions

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


        def has_data(self):
            return (
                self.cvpdndenieduserstotal.is_set or
                self.cvpdnsessiontotal.is_set or
                self.cvpdnsystemclearsessions.is_set or
                self.cvpdnsystemnotifsessionenabled.is_set or
                self.cvpdntunneltotal.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cvpdndenieduserstotal.yfilter != YFilter.not_set or
                self.cvpdnsessiontotal.yfilter != YFilter.not_set or
                self.cvpdnsystemclearsessions.yfilter != YFilter.not_set or
                self.cvpdnsystemnotifsessionenabled.yfilter != YFilter.not_set or
                self.cvpdntunneltotal.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvpdnSystemInfo" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cvpdndenieduserstotal.is_set or self.cvpdndenieduserstotal.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvpdndenieduserstotal.get_name_leafdata())
            if (self.cvpdnsessiontotal.is_set or self.cvpdnsessiontotal.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvpdnsessiontotal.get_name_leafdata())
            if (self.cvpdnsystemclearsessions.is_set or self.cvpdnsystemclearsessions.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvpdnsystemclearsessions.get_name_leafdata())
            if (self.cvpdnsystemnotifsessionenabled.is_set or self.cvpdnsystemnotifsessionenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvpdnsystemnotifsessionenabled.get_name_leafdata())
            if (self.cvpdntunneltotal.is_set or self.cvpdntunneltotal.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvpdntunneltotal.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvpdnDeniedUsersTotal" or name == "cvpdnSessionTotal" or name == "cvpdnSystemClearSessions" or name == "cvpdnSystemNotifSessionEnabled" or name == "cvpdnTunnelTotal"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cvpdnDeniedUsersTotal"):
                self.cvpdndenieduserstotal = value
                self.cvpdndenieduserstotal.value_namespace = name_space
                self.cvpdndenieduserstotal.value_namespace_prefix = name_space_prefix
            if(value_path == "cvpdnSessionTotal"):
                self.cvpdnsessiontotal = value
                self.cvpdnsessiontotal.value_namespace = name_space
                self.cvpdnsessiontotal.value_namespace_prefix = name_space_prefix
            if(value_path == "cvpdnSystemClearSessions"):
                self.cvpdnsystemclearsessions = value
                self.cvpdnsystemclearsessions.value_namespace = name_space
                self.cvpdnsystemclearsessions.value_namespace_prefix = name_space_prefix
            if(value_path == "cvpdnSystemNotifSessionEnabled"):
                self.cvpdnsystemnotifsessionenabled = value
                self.cvpdnsystemnotifsessionenabled.value_namespace = name_space
                self.cvpdnsystemnotifsessionenabled.value_namespace_prefix = name_space_prefix
            if(value_path == "cvpdnTunnelTotal"):
                self.cvpdntunneltotal = value
                self.cvpdntunneltotal.value_namespace = name_space
                self.cvpdntunneltotal.value_namespace_prefix = name_space_prefix


    class Cvpdnmultilinkinfo(Entity):
        """
        
        
        .. attribute:: cvpdnbundlelastchanged
        
        	The value of the sysUpTime object when the contents of cvpdnBundleTable last changed
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cvpdnbundleswithmorethantwolinks
        
        	The total number of bundles comprised of more than two links
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cvpdnbundleswithonelink
        
        	The total number of bundles comprised of a single link
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cvpdnbundleswithtwolinks
        
        	The total number of bundles comprised of two links
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CiscoVpdnMgmtMib.Cvpdnmultilinkinfo, self).__init__()

            self.yang_name = "cvpdnMultilinkInfo"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"

            self.cvpdnbundlelastchanged = YLeaf(YType.uint32, "cvpdnBundleLastChanged")

            self.cvpdnbundleswithmorethantwolinks = YLeaf(YType.uint32, "cvpdnBundlesWithMoreThanTwoLinks")

            self.cvpdnbundleswithonelink = YLeaf(YType.uint32, "cvpdnBundlesWithOneLink")

            self.cvpdnbundleswithtwolinks = YLeaf(YType.uint32, "cvpdnBundlesWithTwoLinks")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cvpdnbundlelastchanged",
                            "cvpdnbundleswithmorethantwolinks",
                            "cvpdnbundleswithonelink",
                            "cvpdnbundleswithtwolinks") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoVpdnMgmtMib.Cvpdnmultilinkinfo, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVpdnMgmtMib.Cvpdnmultilinkinfo, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cvpdnbundlelastchanged.is_set or
                self.cvpdnbundleswithmorethantwolinks.is_set or
                self.cvpdnbundleswithonelink.is_set or
                self.cvpdnbundleswithtwolinks.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cvpdnbundlelastchanged.yfilter != YFilter.not_set or
                self.cvpdnbundleswithmorethantwolinks.yfilter != YFilter.not_set or
                self.cvpdnbundleswithonelink.yfilter != YFilter.not_set or
                self.cvpdnbundleswithtwolinks.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvpdnMultilinkInfo" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cvpdnbundlelastchanged.is_set or self.cvpdnbundlelastchanged.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvpdnbundlelastchanged.get_name_leafdata())
            if (self.cvpdnbundleswithmorethantwolinks.is_set or self.cvpdnbundleswithmorethantwolinks.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvpdnbundleswithmorethantwolinks.get_name_leafdata())
            if (self.cvpdnbundleswithonelink.is_set or self.cvpdnbundleswithonelink.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvpdnbundleswithonelink.get_name_leafdata())
            if (self.cvpdnbundleswithtwolinks.is_set or self.cvpdnbundleswithtwolinks.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cvpdnbundleswithtwolinks.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvpdnBundleLastChanged" or name == "cvpdnBundlesWithMoreThanTwoLinks" or name == "cvpdnBundlesWithOneLink" or name == "cvpdnBundlesWithTwoLinks"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cvpdnBundleLastChanged"):
                self.cvpdnbundlelastchanged = value
                self.cvpdnbundlelastchanged.value_namespace = name_space
                self.cvpdnbundlelastchanged.value_namespace_prefix = name_space_prefix
            if(value_path == "cvpdnBundlesWithMoreThanTwoLinks"):
                self.cvpdnbundleswithmorethantwolinks = value
                self.cvpdnbundleswithmorethantwolinks.value_namespace = name_space
                self.cvpdnbundleswithmorethantwolinks.value_namespace_prefix = name_space_prefix
            if(value_path == "cvpdnBundlesWithOneLink"):
                self.cvpdnbundleswithonelink = value
                self.cvpdnbundleswithonelink.value_namespace = name_space
                self.cvpdnbundleswithonelink.value_namespace_prefix = name_space_prefix
            if(value_path == "cvpdnBundlesWithTwoLinks"):
                self.cvpdnbundleswithtwolinks = value
                self.cvpdnbundleswithtwolinks.value_namespace = name_space
                self.cvpdnbundleswithtwolinks.value_namespace_prefix = name_space_prefix


    class Cvpdnsystemtable(Entity):
        """
        Table of information about the VPDN system for all tunnel
        types.
        
        .. attribute:: cvpdnsystementry
        
        	An entry in the table, containing information about a single type of VPDN tunnel
        	**type**\: list of    :py:class:`Cvpdnsystementry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdnsystemtable.Cvpdnsystementry>`
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CiscoVpdnMgmtMib.Cvpdnsystemtable, self).__init__()

            self.yang_name = "cvpdnSystemTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"

            self.cvpdnsystementry = YList(self)

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
                        super(CiscoVpdnMgmtMib.Cvpdnsystemtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVpdnMgmtMib.Cvpdnsystemtable, self).__setattr__(name, value)


        class Cvpdnsystementry(Entity):
            """
            An entry in the table, containing information about a
            single type of VPDN tunnel.
            
            .. attribute:: cvpdnsystemtunneltype  <key>
            
            	The tunnel type.  This is the tunnel protocol
            	**type**\:   :py:class:`Tunneltype <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.Tunneltype>`
            
            .. attribute:: cvpdnsystemdenieduserstotal
            
            	The total number of denied user attempts to all the VPDN tunnels of this tunnel type since last system re\-initialization
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: attempts
            
            .. attribute:: cvpdnsystemfailedconnreq
            
            	The total number tunnel Failed connection attempts in VPDN tunnels of this tunnel type since last system re\-initialization
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: attempts
            
            .. attribute:: cvpdnsysteminitialconnreq
            
            	The total number tunnel connection attempts on all the VPDN tunnels of this tunnel type since last system re\-initialization
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: attempts
            
            .. attribute:: cvpdnsystemsessiontotal
            
            	The total number of active sessions in all the active VPDN tunnels of this tunnel type
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: cvpdnsystemsuccessconnreq
            
            	The total number tunnel Successful connection attempts in VPDN tunnels of this tunnel type since last system re\-initialization
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: attempts
            
            .. attribute:: cvpdnsystemtunneltotal
            
            	The total number of VPDN tunnels that are currently active of this tunnel type
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: tunnels
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CiscoVpdnMgmtMib.Cvpdnsystemtable.Cvpdnsystementry, self).__init__()

                self.yang_name = "cvpdnSystemEntry"
                self.yang_parent_name = "cvpdnSystemTable"

                self.cvpdnsystemtunneltype = YLeaf(YType.enumeration, "cvpdnSystemTunnelType")

                self.cvpdnsystemdenieduserstotal = YLeaf(YType.uint32, "cvpdnSystemDeniedUsersTotal")

                self.cvpdnsystemfailedconnreq = YLeaf(YType.uint32, "cvpdnSystemFailedConnReq")

                self.cvpdnsysteminitialconnreq = YLeaf(YType.uint32, "cvpdnSystemInitialConnReq")

                self.cvpdnsystemsessiontotal = YLeaf(YType.uint32, "cvpdnSystemSessionTotal")

                self.cvpdnsystemsuccessconnreq = YLeaf(YType.uint32, "cvpdnSystemSuccessConnReq")

                self.cvpdnsystemtunneltotal = YLeaf(YType.uint32, "cvpdnSystemTunnelTotal")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cvpdnsystemtunneltype",
                                "cvpdnsystemdenieduserstotal",
                                "cvpdnsystemfailedconnreq",
                                "cvpdnsysteminitialconnreq",
                                "cvpdnsystemsessiontotal",
                                "cvpdnsystemsuccessconnreq",
                                "cvpdnsystemtunneltotal") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVpdnMgmtMib.Cvpdnsystemtable.Cvpdnsystementry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVpdnMgmtMib.Cvpdnsystemtable.Cvpdnsystementry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cvpdnsystemtunneltype.is_set or
                    self.cvpdnsystemdenieduserstotal.is_set or
                    self.cvpdnsystemfailedconnreq.is_set or
                    self.cvpdnsysteminitialconnreq.is_set or
                    self.cvpdnsystemsessiontotal.is_set or
                    self.cvpdnsystemsuccessconnreq.is_set or
                    self.cvpdnsystemtunneltotal.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cvpdnsystemtunneltype.yfilter != YFilter.not_set or
                    self.cvpdnsystemdenieduserstotal.yfilter != YFilter.not_set or
                    self.cvpdnsystemfailedconnreq.yfilter != YFilter.not_set or
                    self.cvpdnsysteminitialconnreq.yfilter != YFilter.not_set or
                    self.cvpdnsystemsessiontotal.yfilter != YFilter.not_set or
                    self.cvpdnsystemsuccessconnreq.yfilter != YFilter.not_set or
                    self.cvpdnsystemtunneltotal.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvpdnSystemEntry" + "[cvpdnSystemTunnelType='" + self.cvpdnsystemtunneltype.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/cvpdnSystemTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cvpdnsystemtunneltype.is_set or self.cvpdnsystemtunneltype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsystemtunneltype.get_name_leafdata())
                if (self.cvpdnsystemdenieduserstotal.is_set or self.cvpdnsystemdenieduserstotal.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsystemdenieduserstotal.get_name_leafdata())
                if (self.cvpdnsystemfailedconnreq.is_set or self.cvpdnsystemfailedconnreq.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsystemfailedconnreq.get_name_leafdata())
                if (self.cvpdnsysteminitialconnreq.is_set or self.cvpdnsysteminitialconnreq.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsysteminitialconnreq.get_name_leafdata())
                if (self.cvpdnsystemsessiontotal.is_set or self.cvpdnsystemsessiontotal.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsystemsessiontotal.get_name_leafdata())
                if (self.cvpdnsystemsuccessconnreq.is_set or self.cvpdnsystemsuccessconnreq.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsystemsuccessconnreq.get_name_leafdata())
                if (self.cvpdnsystemtunneltotal.is_set or self.cvpdnsystemtunneltotal.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsystemtunneltotal.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cvpdnSystemTunnelType" or name == "cvpdnSystemDeniedUsersTotal" or name == "cvpdnSystemFailedConnReq" or name == "cvpdnSystemInitialConnReq" or name == "cvpdnSystemSessionTotal" or name == "cvpdnSystemSuccessConnReq" or name == "cvpdnSystemTunnelTotal"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cvpdnSystemTunnelType"):
                    self.cvpdnsystemtunneltype = value
                    self.cvpdnsystemtunneltype.value_namespace = name_space
                    self.cvpdnsystemtunneltype.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSystemDeniedUsersTotal"):
                    self.cvpdnsystemdenieduserstotal = value
                    self.cvpdnsystemdenieduserstotal.value_namespace = name_space
                    self.cvpdnsystemdenieduserstotal.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSystemFailedConnReq"):
                    self.cvpdnsystemfailedconnreq = value
                    self.cvpdnsystemfailedconnreq.value_namespace = name_space
                    self.cvpdnsystemfailedconnreq.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSystemInitialConnReq"):
                    self.cvpdnsysteminitialconnreq = value
                    self.cvpdnsysteminitialconnreq.value_namespace = name_space
                    self.cvpdnsysteminitialconnreq.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSystemSessionTotal"):
                    self.cvpdnsystemsessiontotal = value
                    self.cvpdnsystemsessiontotal.value_namespace = name_space
                    self.cvpdnsystemsessiontotal.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSystemSuccessConnReq"):
                    self.cvpdnsystemsuccessconnreq = value
                    self.cvpdnsystemsuccessconnreq.value_namespace = name_space
                    self.cvpdnsystemsuccessconnreq.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSystemTunnelTotal"):
                    self.cvpdnsystemtunneltotal = value
                    self.cvpdnsystemtunneltotal.value_namespace = name_space
                    self.cvpdnsystemtunneltotal.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvpdnsystementry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvpdnsystementry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvpdnSystemTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvpdnSystemEntry"):
                for c in self.cvpdnsystementry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVpdnMgmtMib.Cvpdnsystemtable.Cvpdnsystementry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvpdnsystementry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvpdnSystemEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvpdntunneltable(Entity):
        """
        Table of information about the active VPDN tunnels.
        
        .. attribute:: cvpdntunnelentry
        
        	An entry in the table, containing information about a single active VPDN tunnel
        	**type**\: list of    :py:class:`Cvpdntunnelentry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdntunneltable.Cvpdntunnelentry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CiscoVpdnMgmtMib.Cvpdntunneltable, self).__init__()

            self.yang_name = "cvpdnTunnelTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"

            self.cvpdntunnelentry = YList(self)

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
                        super(CiscoVpdnMgmtMib.Cvpdntunneltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVpdnMgmtMib.Cvpdntunneltable, self).__setattr__(name, value)


        class Cvpdntunnelentry(Entity):
            """
            An entry in the table, containing information about a
            single active VPDN tunnel.
            
            .. attribute:: cvpdntunneltunnelid  <key>
            
            	The Tunnel ID of an active VPDN tunnel.  If it is the instigator of the tunnel, the ID is the HGW/LNS tunnel ID, otherwise it is the NAS/LAC tunnel ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelactivesessions
            
            	The total number of active session currently in the tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunneldeniedusers
            
            	A count of the accumulated total of denied users for the tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnellocalinitconnection
            
            	This object indicates whether the tunnel was generated locally or not
            	**type**\:  bool
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnellocalipaddress
            
            	The local IP address of the tunnel.  This IP address is that of the interface at the local end of the tunnel
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnellocalname
            
            	The local name of an active VPDN tunnel.  It will be the NAS/LAC name of the tunnel if the router serves as the NAS/LAC, or the HGW/LNS name of the tunnel if the system serves as the home gateway.  Typically, the local name is the configured host name of the router
            	**type**\:  str
            
            	**length:** 1..255
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelnetworkservicetype
            
            	The type of network service used in the active tunnel. For now it is IP only
            	**type**\:   :py:class:`Cvpdntunnelnetworkservicetype <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdntunneltable.Cvpdntunnelentry.Cvpdntunnelnetworkservicetype>`
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelorigcause
            
            	The cause which originated an active VPDN tunnel.  The tunnel can be projected via domain name, DNIS or a stack group (SGBP)
            	**type**\:   :py:class:`Cvpdntunnelorigcause <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdntunneltable.Cvpdntunnelentry.Cvpdntunnelorigcause>`
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelremoteendpointname
            
            	The remote end point name of an active VPDN tunnel. This name is either the domain name or the DNIS that this tunnel is projected with
            	**type**\:  str
            
            	**length:** 1..255
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelremoteipaddress
            
            	The remote IP address of the tunnel.  This IP address is that of the interface at the remote end of the tunnel
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelremotename
            
            	The remote name of an active VPDN tunnel.  It will be the home gateway name of the tunnel if the system is a NAS/LAC, or the NAS/LAC name of the tunnel if the system serves as the home gateway
            	**type**\:  str
            
            	**length:** 1..255
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelremotetunnelid
            
            	The remote Tunnel ID of an active VPDN tunnel.  If it is the instigator of the tunnel, the ID is the NAS/LAC tunnel ID, otherwise it is the HGW/LNS tunnel ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsoftshut
            
            	A VPDN tunnel can be put into a soft shut state to prevent any new user session to be added.  This object specifies whether this tunnel has been soft shut
            	**type**\:  bool
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsourceipaddress
            
            	The source IP address of the tunnel.  This IP address is the user configurable IP address for Stack Group Biding Protocol (SGBP) via the CLI command\: vpdn source\-ip
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelstate
            
            	The current state of an active VPDN tunnel.  Each state code is explained below\:         unknown\: The current state of the tunnel is                 unknown.         opening\: The tunnel has just been instigated and                 is pending for a remote end reply to                 complete the process.         open\:    The tunnel is active.         closing\: The tunnel has just been shut down and                 is pending for the remote end to reply                 to complete the process
            	**type**\:   :py:class:`Cvpdntunnelstate <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdntunneltable.Cvpdntunnelentry.Cvpdntunnelstate>`
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CiscoVpdnMgmtMib.Cvpdntunneltable.Cvpdntunnelentry, self).__init__()

                self.yang_name = "cvpdnTunnelEntry"
                self.yang_parent_name = "cvpdnTunnelTable"

                self.cvpdntunneltunnelid = YLeaf(YType.uint32, "cvpdnTunnelTunnelId")

                self.cvpdntunnelactivesessions = YLeaf(YType.uint32, "cvpdnTunnelActiveSessions")

                self.cvpdntunneldeniedusers = YLeaf(YType.uint32, "cvpdnTunnelDeniedUsers")

                self.cvpdntunnellocalinitconnection = YLeaf(YType.boolean, "cvpdnTunnelLocalInitConnection")

                self.cvpdntunnellocalipaddress = YLeaf(YType.str, "cvpdnTunnelLocalIpAddress")

                self.cvpdntunnellocalname = YLeaf(YType.str, "cvpdnTunnelLocalName")

                self.cvpdntunnelnetworkservicetype = YLeaf(YType.enumeration, "cvpdnTunnelNetworkServiceType")

                self.cvpdntunnelorigcause = YLeaf(YType.enumeration, "cvpdnTunnelOrigCause")

                self.cvpdntunnelremoteendpointname = YLeaf(YType.str, "cvpdnTunnelRemoteEndpointName")

                self.cvpdntunnelremoteipaddress = YLeaf(YType.str, "cvpdnTunnelRemoteIpAddress")

                self.cvpdntunnelremotename = YLeaf(YType.str, "cvpdnTunnelRemoteName")

                self.cvpdntunnelremotetunnelid = YLeaf(YType.uint32, "cvpdnTunnelRemoteTunnelId")

                self.cvpdntunnelsoftshut = YLeaf(YType.boolean, "cvpdnTunnelSoftshut")

                self.cvpdntunnelsourceipaddress = YLeaf(YType.str, "cvpdnTunnelSourceIpAddress")

                self.cvpdntunnelstate = YLeaf(YType.enumeration, "cvpdnTunnelState")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cvpdntunneltunnelid",
                                "cvpdntunnelactivesessions",
                                "cvpdntunneldeniedusers",
                                "cvpdntunnellocalinitconnection",
                                "cvpdntunnellocalipaddress",
                                "cvpdntunnellocalname",
                                "cvpdntunnelnetworkservicetype",
                                "cvpdntunnelorigcause",
                                "cvpdntunnelremoteendpointname",
                                "cvpdntunnelremoteipaddress",
                                "cvpdntunnelremotename",
                                "cvpdntunnelremotetunnelid",
                                "cvpdntunnelsoftshut",
                                "cvpdntunnelsourceipaddress",
                                "cvpdntunnelstate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVpdnMgmtMib.Cvpdntunneltable.Cvpdntunnelentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVpdnMgmtMib.Cvpdntunneltable.Cvpdntunnelentry, self).__setattr__(name, value)

            class Cvpdntunnelnetworkservicetype(Enum):
                """
                Cvpdntunnelnetworkservicetype

                The type of network service used in the active tunnel.

                For now it is IP only.

                .. data:: ip = 1

                """

                ip = Enum.YLeaf(1, "ip")


            class Cvpdntunnelorigcause(Enum):
                """
                Cvpdntunnelorigcause

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
                Cvpdntunnelstate

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


            def has_data(self):
                return (
                    self.cvpdntunneltunnelid.is_set or
                    self.cvpdntunnelactivesessions.is_set or
                    self.cvpdntunneldeniedusers.is_set or
                    self.cvpdntunnellocalinitconnection.is_set or
                    self.cvpdntunnellocalipaddress.is_set or
                    self.cvpdntunnellocalname.is_set or
                    self.cvpdntunnelnetworkservicetype.is_set or
                    self.cvpdntunnelorigcause.is_set or
                    self.cvpdntunnelremoteendpointname.is_set or
                    self.cvpdntunnelremoteipaddress.is_set or
                    self.cvpdntunnelremotename.is_set or
                    self.cvpdntunnelremotetunnelid.is_set or
                    self.cvpdntunnelsoftshut.is_set or
                    self.cvpdntunnelsourceipaddress.is_set or
                    self.cvpdntunnelstate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cvpdntunneltunnelid.yfilter != YFilter.not_set or
                    self.cvpdntunnelactivesessions.yfilter != YFilter.not_set or
                    self.cvpdntunneldeniedusers.yfilter != YFilter.not_set or
                    self.cvpdntunnellocalinitconnection.yfilter != YFilter.not_set or
                    self.cvpdntunnellocalipaddress.yfilter != YFilter.not_set or
                    self.cvpdntunnellocalname.yfilter != YFilter.not_set or
                    self.cvpdntunnelnetworkservicetype.yfilter != YFilter.not_set or
                    self.cvpdntunnelorigcause.yfilter != YFilter.not_set or
                    self.cvpdntunnelremoteendpointname.yfilter != YFilter.not_set or
                    self.cvpdntunnelremoteipaddress.yfilter != YFilter.not_set or
                    self.cvpdntunnelremotename.yfilter != YFilter.not_set or
                    self.cvpdntunnelremotetunnelid.yfilter != YFilter.not_set or
                    self.cvpdntunnelsoftshut.yfilter != YFilter.not_set or
                    self.cvpdntunnelsourceipaddress.yfilter != YFilter.not_set or
                    self.cvpdntunnelstate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvpdnTunnelEntry" + "[cvpdnTunnelTunnelId='" + self.cvpdntunneltunnelid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/cvpdnTunnelTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cvpdntunneltunnelid.is_set or self.cvpdntunneltunnelid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunneltunnelid.get_name_leafdata())
                if (self.cvpdntunnelactivesessions.is_set or self.cvpdntunnelactivesessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelactivesessions.get_name_leafdata())
                if (self.cvpdntunneldeniedusers.is_set or self.cvpdntunneldeniedusers.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunneldeniedusers.get_name_leafdata())
                if (self.cvpdntunnellocalinitconnection.is_set or self.cvpdntunnellocalinitconnection.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnellocalinitconnection.get_name_leafdata())
                if (self.cvpdntunnellocalipaddress.is_set or self.cvpdntunnellocalipaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnellocalipaddress.get_name_leafdata())
                if (self.cvpdntunnellocalname.is_set or self.cvpdntunnellocalname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnellocalname.get_name_leafdata())
                if (self.cvpdntunnelnetworkservicetype.is_set or self.cvpdntunnelnetworkservicetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelnetworkservicetype.get_name_leafdata())
                if (self.cvpdntunnelorigcause.is_set or self.cvpdntunnelorigcause.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelorigcause.get_name_leafdata())
                if (self.cvpdntunnelremoteendpointname.is_set or self.cvpdntunnelremoteendpointname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelremoteendpointname.get_name_leafdata())
                if (self.cvpdntunnelremoteipaddress.is_set or self.cvpdntunnelremoteipaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelremoteipaddress.get_name_leafdata())
                if (self.cvpdntunnelremotename.is_set or self.cvpdntunnelremotename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelremotename.get_name_leafdata())
                if (self.cvpdntunnelremotetunnelid.is_set or self.cvpdntunnelremotetunnelid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelremotetunnelid.get_name_leafdata())
                if (self.cvpdntunnelsoftshut.is_set or self.cvpdntunnelsoftshut.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelsoftshut.get_name_leafdata())
                if (self.cvpdntunnelsourceipaddress.is_set or self.cvpdntunnelsourceipaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelsourceipaddress.get_name_leafdata())
                if (self.cvpdntunnelstate.is_set or self.cvpdntunnelstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelstate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cvpdnTunnelTunnelId" or name == "cvpdnTunnelActiveSessions" or name == "cvpdnTunnelDeniedUsers" or name == "cvpdnTunnelLocalInitConnection" or name == "cvpdnTunnelLocalIpAddress" or name == "cvpdnTunnelLocalName" or name == "cvpdnTunnelNetworkServiceType" or name == "cvpdnTunnelOrigCause" or name == "cvpdnTunnelRemoteEndpointName" or name == "cvpdnTunnelRemoteIpAddress" or name == "cvpdnTunnelRemoteName" or name == "cvpdnTunnelRemoteTunnelId" or name == "cvpdnTunnelSoftshut" or name == "cvpdnTunnelSourceIpAddress" or name == "cvpdnTunnelState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cvpdnTunnelTunnelId"):
                    self.cvpdntunneltunnelid = value
                    self.cvpdntunneltunnelid.value_namespace = name_space
                    self.cvpdntunneltunnelid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelActiveSessions"):
                    self.cvpdntunnelactivesessions = value
                    self.cvpdntunnelactivesessions.value_namespace = name_space
                    self.cvpdntunnelactivesessions.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelDeniedUsers"):
                    self.cvpdntunneldeniedusers = value
                    self.cvpdntunneldeniedusers.value_namespace = name_space
                    self.cvpdntunneldeniedusers.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelLocalInitConnection"):
                    self.cvpdntunnellocalinitconnection = value
                    self.cvpdntunnellocalinitconnection.value_namespace = name_space
                    self.cvpdntunnellocalinitconnection.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelLocalIpAddress"):
                    self.cvpdntunnellocalipaddress = value
                    self.cvpdntunnellocalipaddress.value_namespace = name_space
                    self.cvpdntunnellocalipaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelLocalName"):
                    self.cvpdntunnellocalname = value
                    self.cvpdntunnellocalname.value_namespace = name_space
                    self.cvpdntunnellocalname.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelNetworkServiceType"):
                    self.cvpdntunnelnetworkservicetype = value
                    self.cvpdntunnelnetworkservicetype.value_namespace = name_space
                    self.cvpdntunnelnetworkservicetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelOrigCause"):
                    self.cvpdntunnelorigcause = value
                    self.cvpdntunnelorigcause.value_namespace = name_space
                    self.cvpdntunnelorigcause.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelRemoteEndpointName"):
                    self.cvpdntunnelremoteendpointname = value
                    self.cvpdntunnelremoteendpointname.value_namespace = name_space
                    self.cvpdntunnelremoteendpointname.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelRemoteIpAddress"):
                    self.cvpdntunnelremoteipaddress = value
                    self.cvpdntunnelremoteipaddress.value_namespace = name_space
                    self.cvpdntunnelremoteipaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelRemoteName"):
                    self.cvpdntunnelremotename = value
                    self.cvpdntunnelremotename.value_namespace = name_space
                    self.cvpdntunnelremotename.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelRemoteTunnelId"):
                    self.cvpdntunnelremotetunnelid = value
                    self.cvpdntunnelremotetunnelid.value_namespace = name_space
                    self.cvpdntunnelremotetunnelid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelSoftshut"):
                    self.cvpdntunnelsoftshut = value
                    self.cvpdntunnelsoftshut.value_namespace = name_space
                    self.cvpdntunnelsoftshut.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelSourceIpAddress"):
                    self.cvpdntunnelsourceipaddress = value
                    self.cvpdntunnelsourceipaddress.value_namespace = name_space
                    self.cvpdntunnelsourceipaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelState"):
                    self.cvpdntunnelstate = value
                    self.cvpdntunnelstate.value_namespace = name_space
                    self.cvpdntunnelstate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvpdntunnelentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvpdntunnelentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvpdnTunnelTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvpdnTunnelEntry"):
                for c in self.cvpdntunnelentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVpdnMgmtMib.Cvpdntunneltable.Cvpdntunnelentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvpdntunnelentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvpdnTunnelEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvpdntunnelattrtable(Entity):
        """
        Table of information about the active VPDN tunnels.  An
        entry is added to the table when a new tunnel is initiated
        and removed from the table when the tunnel is terminated.
        
        .. attribute:: cvpdntunnelattrentry
        
        	An entry in the table, containing information about a single active VPDN tunnel
        	**type**\: list of    :py:class:`Cvpdntunnelattrentry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdntunnelattrtable.Cvpdntunnelattrentry>`
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CiscoVpdnMgmtMib.Cvpdntunnelattrtable, self).__init__()

            self.yang_name = "cvpdnTunnelAttrTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"

            self.cvpdntunnelattrentry = YList(self)

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
                        super(CiscoVpdnMgmtMib.Cvpdntunnelattrtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVpdnMgmtMib.Cvpdntunnelattrtable, self).__setattr__(name, value)


        class Cvpdntunnelattrentry(Entity):
            """
            An entry in the table, containing information about a
            single active VPDN tunnel.
            
            .. attribute:: cvpdnsystemtunneltype  <key>
            
            	
            	**type**\:   :py:class:`Tunneltype <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.Tunneltype>`
            
            .. attribute:: cvpdntunnelattrtunnelid  <key>
            
            	The Tunnel ID of an active VPDN tunnel.  If this end is the instigator of the tunnel, the ID is the TS tunnel ID, otherwise it is the NAS tunnel ID.  Two distinct tunnels with the same tunnel ID may exist, but with different tunnel types
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cvpdntunnelattractivesessions
            
            	The total number of active session currently in the tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: cvpdntunnelattrdeniedusers
            
            	A count of the accumulated total of denied users for the tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: calls
            
            .. attribute:: cvpdntunnelattrlocalinetaddress
            
            	The local IP address of the tunnel.  This IP address is that of the interface at the local end of the tunnel. The type of this address is determined by the value of  cvpdnTunnelAttrLocalInetAddressType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cvpdntunnelattrlocalinetaddresstype
            
            	Indicates the type of address contained in cvpdnTunnelAttrLocalInetAddress
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cvpdntunnelattrlocalinitconnection
            
            	This object indicates whether the tunnel was originated locally or not.  If it's true, the tunnel was originated locally
            	**type**\:  bool
            
            .. attribute:: cvpdntunnelattrlocalipaddress
            
            	The local IP address of the tunnel.  This IP address is that of the interface at the local end of the tunnel
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cvpdntunnelattrlocalname
            
            	The local name of an active VPDN tunnel.  It will be the NAS name of the tunnel if the system serves as the NAS, or the TS name of the tunnel if the system serves as the tunnel server.  Typically, the local name is the configured host name of the system
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cvpdntunnelattrnetworkservicetype
            
            	The type of network service used in the active tunnel
            	**type**\:   :py:class:`Cvpdntunnelattrnetworkservicetype <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdntunnelattrtable.Cvpdntunnelattrentry.Cvpdntunnelattrnetworkservicetype>`
            
            .. attribute:: cvpdntunnelattrorigcause
            
            	The cause which originated an active VPDN tunnel.  The tunnel can be projected via domain name, DNIS, stack group, or L2 Xconnect
            	**type**\:   :py:class:`Cvpdntunnelattrorigcause <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdntunnelattrtable.Cvpdntunnelattrentry.Cvpdntunnelattrorigcause>`
            
            .. attribute:: cvpdntunnelattrremoteendpointname
            
            	The remote end point name of an active VPDN tunnel.  This name is either the domain name or the DNIS that this tunnel is projected with
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cvpdntunnelattrremoteinetaddress
            
            	The remote IP address of the tunnel.  This IP address is that of the interface at the remote end of the tunnel. The type of this address is determined by the value of  cvpdnTunnelAttrRemoteInetAddressType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cvpdntunnelattrremoteinetaddresstype
            
            	Indicates the type of address contained in cvpdnTunnelAttrRemoteInetAddress
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cvpdntunnelattrremoteipaddress
            
            	The remote IP address of the tunnel.  This IP address is that of the interface at the remote end of the tunnel
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cvpdntunnelattrremotename
            
            	The remote name of an active VPDN tunnel.  It will be the tunnel server name of the tunnel if the system is a NAS, or the NAS name of the tunnel if the system serves as the tunnel server
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cvpdntunnelattrremotetunnelid
            
            	The remote Tunnel ID of an active VPDN tunnel.  If this end is the instigator of the tunnel, the ID is the NAS tunnel ID, otherwise it is the TS tunnel ID
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cvpdntunnelattrsoftshut
            
            	A VPDN tunnel can be put into a soft shut state to prevent any new session to be added.  This object specifies whether this tunnel has been soft shut.  If its true, it has been soft shut
            	**type**\:  bool
            
            .. attribute:: cvpdntunnelattrsourceinetaddress
            
            	The source IP address of the tunnel.  This IP address is the user configurable IP address for Stack Group Biding Protocol.  The type of this address is determined by the  value of cvpdnTunnelAttrSourceInetAddressType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cvpdntunnelattrsourceinetaddresstype
            
            	Indicates the type of address contained in cvpdnTunnelAttrSourceInetAddress
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cvpdntunnelattrsourceipaddress
            
            	The source IP address of the tunnel.  This IP address is the user configurable IP address for Stack Group Biding Protocol
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cvpdntunnelattrstate
            
            	The current state of an active VPDN tunnel. Tunnels of type l2f will have states with the 'l2f' prefix. Tunnels of type l2tp will have states with the 'l2tp' prefix. Tunnels of type pptp will have states with the 'pptp' prefix.  Each state code is explained below\:      unknown\:            The current state of the tunnel is                         unknown.      l2fOpening\:         The tunnel has just been initiated                         and is pending for a remote end                         reply to complete the process.      l2fOpenWait\:        This end received a tunnel open                         request from the remote end and is                         waiting for the tunnel to be                         established.      l2fOpen\:            The tunnel is active.      l2fClosing\:         This end received a tunnel close                         request.      l2fCloseWait\:       The tunnel has just been shut down                         and is pending for the remote end                         to reply to complete the process.      l2tpIdle\:           No tunnel is initiated yet.      l2tpWaitCtlReply\:   The tunnel has been initiated and                         is pending for a remote end reply                         to complete the process.      l2tpEstablished\:    The tunnel is active.      l2tpShuttingDown\:   The tunnel is in progress of                         shutting down.      l2tpNoSessionLeft\:  There is no session left in the                         tunnel.      pptpIdle\:           No tunnel is initiated yet.      pptpWaitConnect\:    The tunnel is waiting for a TCP                         connection.      pptpWaitCtlRequest\: The tunnel has been initiated and                         is pending for a remote end                         request.      pptpWaitCtlReply\:   The tunnel has been initiated and                         is pending for a remote end reply.      pptpEstablished\:    The tunnel is active.      pptpWaitStopReply\:  The tunnel is being shut down and                         is pending for a remote end reply.      pptpTerminal\:       The tunnel has been shut down
            	**type**\:   :py:class:`Cvpdntunnelattrstate <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdntunnelattrtable.Cvpdntunnelattrentry.Cvpdntunnelattrstate>`
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CiscoVpdnMgmtMib.Cvpdntunnelattrtable.Cvpdntunnelattrentry, self).__init__()

                self.yang_name = "cvpdnTunnelAttrEntry"
                self.yang_parent_name = "cvpdnTunnelAttrTable"

                self.cvpdnsystemtunneltype = YLeaf(YType.enumeration, "cvpdnSystemTunnelType")

                self.cvpdntunnelattrtunnelid = YLeaf(YType.int32, "cvpdnTunnelAttrTunnelId")

                self.cvpdntunnelattractivesessions = YLeaf(YType.uint32, "cvpdnTunnelAttrActiveSessions")

                self.cvpdntunnelattrdeniedusers = YLeaf(YType.uint32, "cvpdnTunnelAttrDeniedUsers")

                self.cvpdntunnelattrlocalinetaddress = YLeaf(YType.str, "cvpdnTunnelAttrLocalInetAddress")

                self.cvpdntunnelattrlocalinetaddresstype = YLeaf(YType.enumeration, "cvpdnTunnelAttrLocalInetAddressType")

                self.cvpdntunnelattrlocalinitconnection = YLeaf(YType.boolean, "cvpdnTunnelAttrLocalInitConnection")

                self.cvpdntunnelattrlocalipaddress = YLeaf(YType.str, "cvpdnTunnelAttrLocalIpAddress")

                self.cvpdntunnelattrlocalname = YLeaf(YType.str, "cvpdnTunnelAttrLocalName")

                self.cvpdntunnelattrnetworkservicetype = YLeaf(YType.enumeration, "cvpdnTunnelAttrNetworkServiceType")

                self.cvpdntunnelattrorigcause = YLeaf(YType.enumeration, "cvpdnTunnelAttrOrigCause")

                self.cvpdntunnelattrremoteendpointname = YLeaf(YType.str, "cvpdnTunnelAttrRemoteEndpointName")

                self.cvpdntunnelattrremoteinetaddress = YLeaf(YType.str, "cvpdnTunnelAttrRemoteInetAddress")

                self.cvpdntunnelattrremoteinetaddresstype = YLeaf(YType.enumeration, "cvpdnTunnelAttrRemoteInetAddressType")

                self.cvpdntunnelattrremoteipaddress = YLeaf(YType.str, "cvpdnTunnelAttrRemoteIpAddress")

                self.cvpdntunnelattrremotename = YLeaf(YType.str, "cvpdnTunnelAttrRemoteName")

                self.cvpdntunnelattrremotetunnelid = YLeaf(YType.int32, "cvpdnTunnelAttrRemoteTunnelId")

                self.cvpdntunnelattrsoftshut = YLeaf(YType.boolean, "cvpdnTunnelAttrSoftshut")

                self.cvpdntunnelattrsourceinetaddress = YLeaf(YType.str, "cvpdnTunnelAttrSourceInetAddress")

                self.cvpdntunnelattrsourceinetaddresstype = YLeaf(YType.enumeration, "cvpdnTunnelAttrSourceInetAddressType")

                self.cvpdntunnelattrsourceipaddress = YLeaf(YType.str, "cvpdnTunnelAttrSourceIpAddress")

                self.cvpdntunnelattrstate = YLeaf(YType.enumeration, "cvpdnTunnelAttrState")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cvpdnsystemtunneltype",
                                "cvpdntunnelattrtunnelid",
                                "cvpdntunnelattractivesessions",
                                "cvpdntunnelattrdeniedusers",
                                "cvpdntunnelattrlocalinetaddress",
                                "cvpdntunnelattrlocalinetaddresstype",
                                "cvpdntunnelattrlocalinitconnection",
                                "cvpdntunnelattrlocalipaddress",
                                "cvpdntunnelattrlocalname",
                                "cvpdntunnelattrnetworkservicetype",
                                "cvpdntunnelattrorigcause",
                                "cvpdntunnelattrremoteendpointname",
                                "cvpdntunnelattrremoteinetaddress",
                                "cvpdntunnelattrremoteinetaddresstype",
                                "cvpdntunnelattrremoteipaddress",
                                "cvpdntunnelattrremotename",
                                "cvpdntunnelattrremotetunnelid",
                                "cvpdntunnelattrsoftshut",
                                "cvpdntunnelattrsourceinetaddress",
                                "cvpdntunnelattrsourceinetaddresstype",
                                "cvpdntunnelattrsourceipaddress",
                                "cvpdntunnelattrstate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVpdnMgmtMib.Cvpdntunnelattrtable.Cvpdntunnelattrentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVpdnMgmtMib.Cvpdntunnelattrtable.Cvpdntunnelattrentry, self).__setattr__(name, value)

            class Cvpdntunnelattrnetworkservicetype(Enum):
                """
                Cvpdntunnelattrnetworkservicetype

                The type of network service used in the active tunnel.

                .. data:: ip = 1

                """

                ip = Enum.YLeaf(1, "ip")


            class Cvpdntunnelattrorigcause(Enum):
                """
                Cvpdntunnelattrorigcause

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
                Cvpdntunnelattrstate

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


            def has_data(self):
                return (
                    self.cvpdnsystemtunneltype.is_set or
                    self.cvpdntunnelattrtunnelid.is_set or
                    self.cvpdntunnelattractivesessions.is_set or
                    self.cvpdntunnelattrdeniedusers.is_set or
                    self.cvpdntunnelattrlocalinetaddress.is_set or
                    self.cvpdntunnelattrlocalinetaddresstype.is_set or
                    self.cvpdntunnelattrlocalinitconnection.is_set or
                    self.cvpdntunnelattrlocalipaddress.is_set or
                    self.cvpdntunnelattrlocalname.is_set or
                    self.cvpdntunnelattrnetworkservicetype.is_set or
                    self.cvpdntunnelattrorigcause.is_set or
                    self.cvpdntunnelattrremoteendpointname.is_set or
                    self.cvpdntunnelattrremoteinetaddress.is_set or
                    self.cvpdntunnelattrremoteinetaddresstype.is_set or
                    self.cvpdntunnelattrremoteipaddress.is_set or
                    self.cvpdntunnelattrremotename.is_set or
                    self.cvpdntunnelattrremotetunnelid.is_set or
                    self.cvpdntunnelattrsoftshut.is_set or
                    self.cvpdntunnelattrsourceinetaddress.is_set or
                    self.cvpdntunnelattrsourceinetaddresstype.is_set or
                    self.cvpdntunnelattrsourceipaddress.is_set or
                    self.cvpdntunnelattrstate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cvpdnsystemtunneltype.yfilter != YFilter.not_set or
                    self.cvpdntunnelattrtunnelid.yfilter != YFilter.not_set or
                    self.cvpdntunnelattractivesessions.yfilter != YFilter.not_set or
                    self.cvpdntunnelattrdeniedusers.yfilter != YFilter.not_set or
                    self.cvpdntunnelattrlocalinetaddress.yfilter != YFilter.not_set or
                    self.cvpdntunnelattrlocalinetaddresstype.yfilter != YFilter.not_set or
                    self.cvpdntunnelattrlocalinitconnection.yfilter != YFilter.not_set or
                    self.cvpdntunnelattrlocalipaddress.yfilter != YFilter.not_set or
                    self.cvpdntunnelattrlocalname.yfilter != YFilter.not_set or
                    self.cvpdntunnelattrnetworkservicetype.yfilter != YFilter.not_set or
                    self.cvpdntunnelattrorigcause.yfilter != YFilter.not_set or
                    self.cvpdntunnelattrremoteendpointname.yfilter != YFilter.not_set or
                    self.cvpdntunnelattrremoteinetaddress.yfilter != YFilter.not_set or
                    self.cvpdntunnelattrremoteinetaddresstype.yfilter != YFilter.not_set or
                    self.cvpdntunnelattrremoteipaddress.yfilter != YFilter.not_set or
                    self.cvpdntunnelattrremotename.yfilter != YFilter.not_set or
                    self.cvpdntunnelattrremotetunnelid.yfilter != YFilter.not_set or
                    self.cvpdntunnelattrsoftshut.yfilter != YFilter.not_set or
                    self.cvpdntunnelattrsourceinetaddress.yfilter != YFilter.not_set or
                    self.cvpdntunnelattrsourceinetaddresstype.yfilter != YFilter.not_set or
                    self.cvpdntunnelattrsourceipaddress.yfilter != YFilter.not_set or
                    self.cvpdntunnelattrstate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvpdnTunnelAttrEntry" + "[cvpdnSystemTunnelType='" + self.cvpdnsystemtunneltype.get() + "']" + "[cvpdnTunnelAttrTunnelId='" + self.cvpdntunnelattrtunnelid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/cvpdnTunnelAttrTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cvpdnsystemtunneltype.is_set or self.cvpdnsystemtunneltype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsystemtunneltype.get_name_leafdata())
                if (self.cvpdntunnelattrtunnelid.is_set or self.cvpdntunnelattrtunnelid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelattrtunnelid.get_name_leafdata())
                if (self.cvpdntunnelattractivesessions.is_set or self.cvpdntunnelattractivesessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelattractivesessions.get_name_leafdata())
                if (self.cvpdntunnelattrdeniedusers.is_set or self.cvpdntunnelattrdeniedusers.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelattrdeniedusers.get_name_leafdata())
                if (self.cvpdntunnelattrlocalinetaddress.is_set or self.cvpdntunnelattrlocalinetaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelattrlocalinetaddress.get_name_leafdata())
                if (self.cvpdntunnelattrlocalinetaddresstype.is_set or self.cvpdntunnelattrlocalinetaddresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelattrlocalinetaddresstype.get_name_leafdata())
                if (self.cvpdntunnelattrlocalinitconnection.is_set or self.cvpdntunnelattrlocalinitconnection.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelattrlocalinitconnection.get_name_leafdata())
                if (self.cvpdntunnelattrlocalipaddress.is_set or self.cvpdntunnelattrlocalipaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelattrlocalipaddress.get_name_leafdata())
                if (self.cvpdntunnelattrlocalname.is_set or self.cvpdntunnelattrlocalname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelattrlocalname.get_name_leafdata())
                if (self.cvpdntunnelattrnetworkservicetype.is_set or self.cvpdntunnelattrnetworkservicetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelattrnetworkservicetype.get_name_leafdata())
                if (self.cvpdntunnelattrorigcause.is_set or self.cvpdntunnelattrorigcause.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelattrorigcause.get_name_leafdata())
                if (self.cvpdntunnelattrremoteendpointname.is_set or self.cvpdntunnelattrremoteendpointname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelattrremoteendpointname.get_name_leafdata())
                if (self.cvpdntunnelattrremoteinetaddress.is_set or self.cvpdntunnelattrremoteinetaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelattrremoteinetaddress.get_name_leafdata())
                if (self.cvpdntunnelattrremoteinetaddresstype.is_set or self.cvpdntunnelattrremoteinetaddresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelattrremoteinetaddresstype.get_name_leafdata())
                if (self.cvpdntunnelattrremoteipaddress.is_set or self.cvpdntunnelattrremoteipaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelattrremoteipaddress.get_name_leafdata())
                if (self.cvpdntunnelattrremotename.is_set or self.cvpdntunnelattrremotename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelattrremotename.get_name_leafdata())
                if (self.cvpdntunnelattrremotetunnelid.is_set or self.cvpdntunnelattrremotetunnelid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelattrremotetunnelid.get_name_leafdata())
                if (self.cvpdntunnelattrsoftshut.is_set or self.cvpdntunnelattrsoftshut.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelattrsoftshut.get_name_leafdata())
                if (self.cvpdntunnelattrsourceinetaddress.is_set or self.cvpdntunnelattrsourceinetaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelattrsourceinetaddress.get_name_leafdata())
                if (self.cvpdntunnelattrsourceinetaddresstype.is_set or self.cvpdntunnelattrsourceinetaddresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelattrsourceinetaddresstype.get_name_leafdata())
                if (self.cvpdntunnelattrsourceipaddress.is_set or self.cvpdntunnelattrsourceipaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelattrsourceipaddress.get_name_leafdata())
                if (self.cvpdntunnelattrstate.is_set or self.cvpdntunnelattrstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelattrstate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cvpdnSystemTunnelType" or name == "cvpdnTunnelAttrTunnelId" or name == "cvpdnTunnelAttrActiveSessions" or name == "cvpdnTunnelAttrDeniedUsers" or name == "cvpdnTunnelAttrLocalInetAddress" or name == "cvpdnTunnelAttrLocalInetAddressType" or name == "cvpdnTunnelAttrLocalInitConnection" or name == "cvpdnTunnelAttrLocalIpAddress" or name == "cvpdnTunnelAttrLocalName" or name == "cvpdnTunnelAttrNetworkServiceType" or name == "cvpdnTunnelAttrOrigCause" or name == "cvpdnTunnelAttrRemoteEndpointName" or name == "cvpdnTunnelAttrRemoteInetAddress" or name == "cvpdnTunnelAttrRemoteInetAddressType" or name == "cvpdnTunnelAttrRemoteIpAddress" or name == "cvpdnTunnelAttrRemoteName" or name == "cvpdnTunnelAttrRemoteTunnelId" or name == "cvpdnTunnelAttrSoftshut" or name == "cvpdnTunnelAttrSourceInetAddress" or name == "cvpdnTunnelAttrSourceInetAddressType" or name == "cvpdnTunnelAttrSourceIpAddress" or name == "cvpdnTunnelAttrState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cvpdnSystemTunnelType"):
                    self.cvpdnsystemtunneltype = value
                    self.cvpdnsystemtunneltype.value_namespace = name_space
                    self.cvpdnsystemtunneltype.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelAttrTunnelId"):
                    self.cvpdntunnelattrtunnelid = value
                    self.cvpdntunnelattrtunnelid.value_namespace = name_space
                    self.cvpdntunnelattrtunnelid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelAttrActiveSessions"):
                    self.cvpdntunnelattractivesessions = value
                    self.cvpdntunnelattractivesessions.value_namespace = name_space
                    self.cvpdntunnelattractivesessions.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelAttrDeniedUsers"):
                    self.cvpdntunnelattrdeniedusers = value
                    self.cvpdntunnelattrdeniedusers.value_namespace = name_space
                    self.cvpdntunnelattrdeniedusers.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelAttrLocalInetAddress"):
                    self.cvpdntunnelattrlocalinetaddress = value
                    self.cvpdntunnelattrlocalinetaddress.value_namespace = name_space
                    self.cvpdntunnelattrlocalinetaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelAttrLocalInetAddressType"):
                    self.cvpdntunnelattrlocalinetaddresstype = value
                    self.cvpdntunnelattrlocalinetaddresstype.value_namespace = name_space
                    self.cvpdntunnelattrlocalinetaddresstype.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelAttrLocalInitConnection"):
                    self.cvpdntunnelattrlocalinitconnection = value
                    self.cvpdntunnelattrlocalinitconnection.value_namespace = name_space
                    self.cvpdntunnelattrlocalinitconnection.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelAttrLocalIpAddress"):
                    self.cvpdntunnelattrlocalipaddress = value
                    self.cvpdntunnelattrlocalipaddress.value_namespace = name_space
                    self.cvpdntunnelattrlocalipaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelAttrLocalName"):
                    self.cvpdntunnelattrlocalname = value
                    self.cvpdntunnelattrlocalname.value_namespace = name_space
                    self.cvpdntunnelattrlocalname.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelAttrNetworkServiceType"):
                    self.cvpdntunnelattrnetworkservicetype = value
                    self.cvpdntunnelattrnetworkservicetype.value_namespace = name_space
                    self.cvpdntunnelattrnetworkservicetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelAttrOrigCause"):
                    self.cvpdntunnelattrorigcause = value
                    self.cvpdntunnelattrorigcause.value_namespace = name_space
                    self.cvpdntunnelattrorigcause.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelAttrRemoteEndpointName"):
                    self.cvpdntunnelattrremoteendpointname = value
                    self.cvpdntunnelattrremoteendpointname.value_namespace = name_space
                    self.cvpdntunnelattrremoteendpointname.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelAttrRemoteInetAddress"):
                    self.cvpdntunnelattrremoteinetaddress = value
                    self.cvpdntunnelattrremoteinetaddress.value_namespace = name_space
                    self.cvpdntunnelattrremoteinetaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelAttrRemoteInetAddressType"):
                    self.cvpdntunnelattrremoteinetaddresstype = value
                    self.cvpdntunnelattrremoteinetaddresstype.value_namespace = name_space
                    self.cvpdntunnelattrremoteinetaddresstype.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelAttrRemoteIpAddress"):
                    self.cvpdntunnelattrremoteipaddress = value
                    self.cvpdntunnelattrremoteipaddress.value_namespace = name_space
                    self.cvpdntunnelattrremoteipaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelAttrRemoteName"):
                    self.cvpdntunnelattrremotename = value
                    self.cvpdntunnelattrremotename.value_namespace = name_space
                    self.cvpdntunnelattrremotename.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelAttrRemoteTunnelId"):
                    self.cvpdntunnelattrremotetunnelid = value
                    self.cvpdntunnelattrremotetunnelid.value_namespace = name_space
                    self.cvpdntunnelattrremotetunnelid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelAttrSoftshut"):
                    self.cvpdntunnelattrsoftshut = value
                    self.cvpdntunnelattrsoftshut.value_namespace = name_space
                    self.cvpdntunnelattrsoftshut.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelAttrSourceInetAddress"):
                    self.cvpdntunnelattrsourceinetaddress = value
                    self.cvpdntunnelattrsourceinetaddress.value_namespace = name_space
                    self.cvpdntunnelattrsourceinetaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelAttrSourceInetAddressType"):
                    self.cvpdntunnelattrsourceinetaddresstype = value
                    self.cvpdntunnelattrsourceinetaddresstype.value_namespace = name_space
                    self.cvpdntunnelattrsourceinetaddresstype.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelAttrSourceIpAddress"):
                    self.cvpdntunnelattrsourceipaddress = value
                    self.cvpdntunnelattrsourceipaddress.value_namespace = name_space
                    self.cvpdntunnelattrsourceipaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelAttrState"):
                    self.cvpdntunnelattrstate = value
                    self.cvpdntunnelattrstate.value_namespace = name_space
                    self.cvpdntunnelattrstate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvpdntunnelattrentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvpdntunnelattrentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvpdnTunnelAttrTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvpdnTunnelAttrEntry"):
                for c in self.cvpdntunnelattrentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVpdnMgmtMib.Cvpdntunnelattrtable.Cvpdntunnelattrentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvpdntunnelattrentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvpdnTunnelAttrEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvpdntunnelsessiontable(Entity):
        """
        Table of information about individual user sessions
        within the active tunnels.  Entry is added to the table
        when new user session is initiated and be removed from
        the table when the user session is terminated.
        
        .. attribute:: cvpdntunnelsessionentry
        
        	An entry in the table, containing information about a single user session within the tunnel
        	**type**\: list of    :py:class:`Cvpdntunnelsessionentry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdntunnelsessiontable.Cvpdntunnelsessionentry>`
        
        	**status**\: obsolete
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CiscoVpdnMgmtMib.Cvpdntunnelsessiontable, self).__init__()

            self.yang_name = "cvpdnTunnelSessionTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"

            self.cvpdntunnelsessionentry = YList(self)

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
                        super(CiscoVpdnMgmtMib.Cvpdntunnelsessiontable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVpdnMgmtMib.Cvpdntunnelsessiontable, self).__setattr__(name, value)


        class Cvpdntunnelsessionentry(Entity):
            """
            An entry in the table, containing information about a
            single user session within the tunnel.
            
            .. attribute:: cvpdntunneltunnelid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cvpdntunneltunnelid <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdntunneltable.Cvpdntunnelentry>`
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionid  <key>
            
            	The ID of an active VPDN tunnel user session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionbytesin
            
            	The total number of input bytes through this active user session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionbytesout
            
            	The total number of output bytes through this active user session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessioncallduration
            
            	This object specifies the call duration of the current active user session in value of system uptime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessiondevicecallerid
            
            	The incoming caller identification of the user.  It is the originating number that called into the device that initiates the user session.  This object can be empty since not all dial device can provide caller ID information
            	**type**\:  str
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessiondevicephyid
            
            	The device ID of the physical interface for the user session.  The object is the the interface index which points to the ifTable.  For virtual interface that is not in the ifTable, it will have zero value
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessiondevicetype
            
            	The type of physical devices that this user session is attached to for the local end of the tunnel.  The meaning of each device type is explained below\:      other\:              Any device that has not been                         defined.      asyncInternalModem\: Modem Pool device of an access                         server.      async\:              A regular asynchronous serial                         interface.      sync\:               A regular synchronous serial                         interface.      bchan\:              An ISDN call.      xdsl\:               Future application with xDSL                         devices.      cable\:              Future application with Cable                         modem devices
            	**type**\:   :py:class:`Cvpdntunnelsessiondevicetype <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdntunnelsessiontable.Cvpdntunnelsessionentry.Cvpdntunnelsessiondevicetype>`
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionds1channelindex
            
            	The DS1 database channel index if it is associated with this user session.  Only a session over a device of type asyncInternalModem will have a valid value for this object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionds1portindex
            
            	The DS1 database port index if it is associated with this user session.  Only a session with a device of type asyncInternalModem will have a a valid value for this object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionds1slotindex
            
            	The DS1 database slot index if it is associated with this user session.  Only a session with a device of type asyncInternalModem will have a valid value for this object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionmodemcallstartindex
            
            	Arbitrary small integer to distinguish modem calls that occurred at the same time tick.  Only session over device asyncInternalModem will have a valid value for this object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionmodemcallstarttime
            
            	The start time of the current modem call.  Only a session with a  device of type asyncInternalModem will have a valid value for this object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionmodemportindex
            
            	The Modem Pool database port index if it is associated with this user session.  Only a session with a device of type asyncInternalModem will have a valid value for this object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionmodemslotindex
            
            	The Modem Pool database slot index if it is associated with this user session.  Only a session with device of type asyncInternalModem will have a valid value for this object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionmultilink
            
            	This object indicates whether the session is part of a multilink or not
            	**type**\:  bool
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionpacketsin
            
            	The total number of input packets through this active user session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionpacketsout
            
            	The total number of output packets through this active user session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionstate
            
            	The current state of an active user session.  Each state code is explained below\:      unknown\:          The current state of the tunnel's                       session is unknown.      opening\:          The user session has just been                       initiated through a tunnel and is                       pending for the remote end reply                       to complete the process.      open\:             The user session is active.      closing\:          The user session has just been                       closed and is pending for the                       remote end reply to complete the                       process.      waitingForTunnel\: The user session is in this state                       when the tunnel which this session                       is going through is still in                       CLOSED state.  It waits for the                       tunnel to become OPEN before the                       session is allow to be fully                       established
            	**type**\:   :py:class:`Cvpdntunnelsessionstate <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdntunnelsessiontable.Cvpdntunnelsessionentry.Cvpdntunnelsessionstate>`
            
            	**status**\: obsolete
            
            .. attribute:: cvpdntunnelsessionusername
            
            	The name of the user of the user session
            	**type**\:  str
            
            	**length:** 1..255
            
            	**status**\: obsolete
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CiscoVpdnMgmtMib.Cvpdntunnelsessiontable.Cvpdntunnelsessionentry, self).__init__()

                self.yang_name = "cvpdnTunnelSessionEntry"
                self.yang_parent_name = "cvpdnTunnelSessionTable"

                self.cvpdntunneltunnelid = YLeaf(YType.str, "cvpdnTunnelTunnelId")

                self.cvpdntunnelsessionid = YLeaf(YType.uint32, "cvpdnTunnelSessionId")

                self.cvpdntunnelsessionbytesin = YLeaf(YType.uint32, "cvpdnTunnelSessionBytesIn")

                self.cvpdntunnelsessionbytesout = YLeaf(YType.uint32, "cvpdnTunnelSessionBytesOut")

                self.cvpdntunnelsessioncallduration = YLeaf(YType.uint32, "cvpdnTunnelSessionCallDuration")

                self.cvpdntunnelsessiondevicecallerid = YLeaf(YType.str, "cvpdnTunnelSessionDeviceCallerId")

                self.cvpdntunnelsessiondevicephyid = YLeaf(YType.int32, "cvpdnTunnelSessionDevicePhyId")

                self.cvpdntunnelsessiondevicetype = YLeaf(YType.enumeration, "cvpdnTunnelSessionDeviceType")

                self.cvpdntunnelsessionds1channelindex = YLeaf(YType.uint32, "cvpdnTunnelSessionDS1ChannelIndex")

                self.cvpdntunnelsessionds1portindex = YLeaf(YType.uint32, "cvpdnTunnelSessionDS1PortIndex")

                self.cvpdntunnelsessionds1slotindex = YLeaf(YType.uint32, "cvpdnTunnelSessionDS1SlotIndex")

                self.cvpdntunnelsessionmodemcallstartindex = YLeaf(YType.uint32, "cvpdnTunnelSessionModemCallStartIndex")

                self.cvpdntunnelsessionmodemcallstarttime = YLeaf(YType.uint32, "cvpdnTunnelSessionModemCallStartTime")

                self.cvpdntunnelsessionmodemportindex = YLeaf(YType.uint32, "cvpdnTunnelSessionModemPortIndex")

                self.cvpdntunnelsessionmodemslotindex = YLeaf(YType.uint32, "cvpdnTunnelSessionModemSlotIndex")

                self.cvpdntunnelsessionmultilink = YLeaf(YType.boolean, "cvpdnTunnelSessionMultilink")

                self.cvpdntunnelsessionpacketsin = YLeaf(YType.uint32, "cvpdnTunnelSessionPacketsIn")

                self.cvpdntunnelsessionpacketsout = YLeaf(YType.uint32, "cvpdnTunnelSessionPacketsOut")

                self.cvpdntunnelsessionstate = YLeaf(YType.enumeration, "cvpdnTunnelSessionState")

                self.cvpdntunnelsessionusername = YLeaf(YType.str, "cvpdnTunnelSessionUserName")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cvpdntunneltunnelid",
                                "cvpdntunnelsessionid",
                                "cvpdntunnelsessionbytesin",
                                "cvpdntunnelsessionbytesout",
                                "cvpdntunnelsessioncallduration",
                                "cvpdntunnelsessiondevicecallerid",
                                "cvpdntunnelsessiondevicephyid",
                                "cvpdntunnelsessiondevicetype",
                                "cvpdntunnelsessionds1channelindex",
                                "cvpdntunnelsessionds1portindex",
                                "cvpdntunnelsessionds1slotindex",
                                "cvpdntunnelsessionmodemcallstartindex",
                                "cvpdntunnelsessionmodemcallstarttime",
                                "cvpdntunnelsessionmodemportindex",
                                "cvpdntunnelsessionmodemslotindex",
                                "cvpdntunnelsessionmultilink",
                                "cvpdntunnelsessionpacketsin",
                                "cvpdntunnelsessionpacketsout",
                                "cvpdntunnelsessionstate",
                                "cvpdntunnelsessionusername") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVpdnMgmtMib.Cvpdntunnelsessiontable.Cvpdntunnelsessionentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVpdnMgmtMib.Cvpdntunnelsessiontable.Cvpdntunnelsessionentry, self).__setattr__(name, value)

            class Cvpdntunnelsessiondevicetype(Enum):
                """
                Cvpdntunnelsessiondevicetype

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
                Cvpdntunnelsessionstate

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


            def has_data(self):
                return (
                    self.cvpdntunneltunnelid.is_set or
                    self.cvpdntunnelsessionid.is_set or
                    self.cvpdntunnelsessionbytesin.is_set or
                    self.cvpdntunnelsessionbytesout.is_set or
                    self.cvpdntunnelsessioncallduration.is_set or
                    self.cvpdntunnelsessiondevicecallerid.is_set or
                    self.cvpdntunnelsessiondevicephyid.is_set or
                    self.cvpdntunnelsessiondevicetype.is_set or
                    self.cvpdntunnelsessionds1channelindex.is_set or
                    self.cvpdntunnelsessionds1portindex.is_set or
                    self.cvpdntunnelsessionds1slotindex.is_set or
                    self.cvpdntunnelsessionmodemcallstartindex.is_set or
                    self.cvpdntunnelsessionmodemcallstarttime.is_set or
                    self.cvpdntunnelsessionmodemportindex.is_set or
                    self.cvpdntunnelsessionmodemslotindex.is_set or
                    self.cvpdntunnelsessionmultilink.is_set or
                    self.cvpdntunnelsessionpacketsin.is_set or
                    self.cvpdntunnelsessionpacketsout.is_set or
                    self.cvpdntunnelsessionstate.is_set or
                    self.cvpdntunnelsessionusername.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cvpdntunneltunnelid.yfilter != YFilter.not_set or
                    self.cvpdntunnelsessionid.yfilter != YFilter.not_set or
                    self.cvpdntunnelsessionbytesin.yfilter != YFilter.not_set or
                    self.cvpdntunnelsessionbytesout.yfilter != YFilter.not_set or
                    self.cvpdntunnelsessioncallduration.yfilter != YFilter.not_set or
                    self.cvpdntunnelsessiondevicecallerid.yfilter != YFilter.not_set or
                    self.cvpdntunnelsessiondevicephyid.yfilter != YFilter.not_set or
                    self.cvpdntunnelsessiondevicetype.yfilter != YFilter.not_set or
                    self.cvpdntunnelsessionds1channelindex.yfilter != YFilter.not_set or
                    self.cvpdntunnelsessionds1portindex.yfilter != YFilter.not_set or
                    self.cvpdntunnelsessionds1slotindex.yfilter != YFilter.not_set or
                    self.cvpdntunnelsessionmodemcallstartindex.yfilter != YFilter.not_set or
                    self.cvpdntunnelsessionmodemcallstarttime.yfilter != YFilter.not_set or
                    self.cvpdntunnelsessionmodemportindex.yfilter != YFilter.not_set or
                    self.cvpdntunnelsessionmodemslotindex.yfilter != YFilter.not_set or
                    self.cvpdntunnelsessionmultilink.yfilter != YFilter.not_set or
                    self.cvpdntunnelsessionpacketsin.yfilter != YFilter.not_set or
                    self.cvpdntunnelsessionpacketsout.yfilter != YFilter.not_set or
                    self.cvpdntunnelsessionstate.yfilter != YFilter.not_set or
                    self.cvpdntunnelsessionusername.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvpdnTunnelSessionEntry" + "[cvpdnTunnelTunnelId='" + self.cvpdntunneltunnelid.get() + "']" + "[cvpdnTunnelSessionId='" + self.cvpdntunnelsessionid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/cvpdnTunnelSessionTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cvpdntunneltunnelid.is_set or self.cvpdntunneltunnelid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunneltunnelid.get_name_leafdata())
                if (self.cvpdntunnelsessionid.is_set or self.cvpdntunnelsessionid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelsessionid.get_name_leafdata())
                if (self.cvpdntunnelsessionbytesin.is_set or self.cvpdntunnelsessionbytesin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelsessionbytesin.get_name_leafdata())
                if (self.cvpdntunnelsessionbytesout.is_set or self.cvpdntunnelsessionbytesout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelsessionbytesout.get_name_leafdata())
                if (self.cvpdntunnelsessioncallduration.is_set or self.cvpdntunnelsessioncallduration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelsessioncallduration.get_name_leafdata())
                if (self.cvpdntunnelsessiondevicecallerid.is_set or self.cvpdntunnelsessiondevicecallerid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelsessiondevicecallerid.get_name_leafdata())
                if (self.cvpdntunnelsessiondevicephyid.is_set or self.cvpdntunnelsessiondevicephyid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelsessiondevicephyid.get_name_leafdata())
                if (self.cvpdntunnelsessiondevicetype.is_set or self.cvpdntunnelsessiondevicetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelsessiondevicetype.get_name_leafdata())
                if (self.cvpdntunnelsessionds1channelindex.is_set or self.cvpdntunnelsessionds1channelindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelsessionds1channelindex.get_name_leafdata())
                if (self.cvpdntunnelsessionds1portindex.is_set or self.cvpdntunnelsessionds1portindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelsessionds1portindex.get_name_leafdata())
                if (self.cvpdntunnelsessionds1slotindex.is_set or self.cvpdntunnelsessionds1slotindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelsessionds1slotindex.get_name_leafdata())
                if (self.cvpdntunnelsessionmodemcallstartindex.is_set or self.cvpdntunnelsessionmodemcallstartindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelsessionmodemcallstartindex.get_name_leafdata())
                if (self.cvpdntunnelsessionmodemcallstarttime.is_set or self.cvpdntunnelsessionmodemcallstarttime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelsessionmodemcallstarttime.get_name_leafdata())
                if (self.cvpdntunnelsessionmodemportindex.is_set or self.cvpdntunnelsessionmodemportindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelsessionmodemportindex.get_name_leafdata())
                if (self.cvpdntunnelsessionmodemslotindex.is_set or self.cvpdntunnelsessionmodemslotindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelsessionmodemslotindex.get_name_leafdata())
                if (self.cvpdntunnelsessionmultilink.is_set or self.cvpdntunnelsessionmultilink.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelsessionmultilink.get_name_leafdata())
                if (self.cvpdntunnelsessionpacketsin.is_set or self.cvpdntunnelsessionpacketsin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelsessionpacketsin.get_name_leafdata())
                if (self.cvpdntunnelsessionpacketsout.is_set or self.cvpdntunnelsessionpacketsout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelsessionpacketsout.get_name_leafdata())
                if (self.cvpdntunnelsessionstate.is_set or self.cvpdntunnelsessionstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelsessionstate.get_name_leafdata())
                if (self.cvpdntunnelsessionusername.is_set or self.cvpdntunnelsessionusername.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelsessionusername.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cvpdnTunnelTunnelId" or name == "cvpdnTunnelSessionId" or name == "cvpdnTunnelSessionBytesIn" or name == "cvpdnTunnelSessionBytesOut" or name == "cvpdnTunnelSessionCallDuration" or name == "cvpdnTunnelSessionDeviceCallerId" or name == "cvpdnTunnelSessionDevicePhyId" or name == "cvpdnTunnelSessionDeviceType" or name == "cvpdnTunnelSessionDS1ChannelIndex" or name == "cvpdnTunnelSessionDS1PortIndex" or name == "cvpdnTunnelSessionDS1SlotIndex" or name == "cvpdnTunnelSessionModemCallStartIndex" or name == "cvpdnTunnelSessionModemCallStartTime" or name == "cvpdnTunnelSessionModemPortIndex" or name == "cvpdnTunnelSessionModemSlotIndex" or name == "cvpdnTunnelSessionMultilink" or name == "cvpdnTunnelSessionPacketsIn" or name == "cvpdnTunnelSessionPacketsOut" or name == "cvpdnTunnelSessionState" or name == "cvpdnTunnelSessionUserName"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cvpdnTunnelTunnelId"):
                    self.cvpdntunneltunnelid = value
                    self.cvpdntunneltunnelid.value_namespace = name_space
                    self.cvpdntunneltunnelid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelSessionId"):
                    self.cvpdntunnelsessionid = value
                    self.cvpdntunnelsessionid.value_namespace = name_space
                    self.cvpdntunnelsessionid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelSessionBytesIn"):
                    self.cvpdntunnelsessionbytesin = value
                    self.cvpdntunnelsessionbytesin.value_namespace = name_space
                    self.cvpdntunnelsessionbytesin.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelSessionBytesOut"):
                    self.cvpdntunnelsessionbytesout = value
                    self.cvpdntunnelsessionbytesout.value_namespace = name_space
                    self.cvpdntunnelsessionbytesout.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelSessionCallDuration"):
                    self.cvpdntunnelsessioncallduration = value
                    self.cvpdntunnelsessioncallduration.value_namespace = name_space
                    self.cvpdntunnelsessioncallduration.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelSessionDeviceCallerId"):
                    self.cvpdntunnelsessiondevicecallerid = value
                    self.cvpdntunnelsessiondevicecallerid.value_namespace = name_space
                    self.cvpdntunnelsessiondevicecallerid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelSessionDevicePhyId"):
                    self.cvpdntunnelsessiondevicephyid = value
                    self.cvpdntunnelsessiondevicephyid.value_namespace = name_space
                    self.cvpdntunnelsessiondevicephyid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelSessionDeviceType"):
                    self.cvpdntunnelsessiondevicetype = value
                    self.cvpdntunnelsessiondevicetype.value_namespace = name_space
                    self.cvpdntunnelsessiondevicetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelSessionDS1ChannelIndex"):
                    self.cvpdntunnelsessionds1channelindex = value
                    self.cvpdntunnelsessionds1channelindex.value_namespace = name_space
                    self.cvpdntunnelsessionds1channelindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelSessionDS1PortIndex"):
                    self.cvpdntunnelsessionds1portindex = value
                    self.cvpdntunnelsessionds1portindex.value_namespace = name_space
                    self.cvpdntunnelsessionds1portindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelSessionDS1SlotIndex"):
                    self.cvpdntunnelsessionds1slotindex = value
                    self.cvpdntunnelsessionds1slotindex.value_namespace = name_space
                    self.cvpdntunnelsessionds1slotindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelSessionModemCallStartIndex"):
                    self.cvpdntunnelsessionmodemcallstartindex = value
                    self.cvpdntunnelsessionmodemcallstartindex.value_namespace = name_space
                    self.cvpdntunnelsessionmodemcallstartindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelSessionModemCallStartTime"):
                    self.cvpdntunnelsessionmodemcallstarttime = value
                    self.cvpdntunnelsessionmodemcallstarttime.value_namespace = name_space
                    self.cvpdntunnelsessionmodemcallstarttime.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelSessionModemPortIndex"):
                    self.cvpdntunnelsessionmodemportindex = value
                    self.cvpdntunnelsessionmodemportindex.value_namespace = name_space
                    self.cvpdntunnelsessionmodemportindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelSessionModemSlotIndex"):
                    self.cvpdntunnelsessionmodemslotindex = value
                    self.cvpdntunnelsessionmodemslotindex.value_namespace = name_space
                    self.cvpdntunnelsessionmodemslotindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelSessionMultilink"):
                    self.cvpdntunnelsessionmultilink = value
                    self.cvpdntunnelsessionmultilink.value_namespace = name_space
                    self.cvpdntunnelsessionmultilink.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelSessionPacketsIn"):
                    self.cvpdntunnelsessionpacketsin = value
                    self.cvpdntunnelsessionpacketsin.value_namespace = name_space
                    self.cvpdntunnelsessionpacketsin.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelSessionPacketsOut"):
                    self.cvpdntunnelsessionpacketsout = value
                    self.cvpdntunnelsessionpacketsout.value_namespace = name_space
                    self.cvpdntunnelsessionpacketsout.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelSessionState"):
                    self.cvpdntunnelsessionstate = value
                    self.cvpdntunnelsessionstate.value_namespace = name_space
                    self.cvpdntunnelsessionstate.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelSessionUserName"):
                    self.cvpdntunnelsessionusername = value
                    self.cvpdntunnelsessionusername.value_namespace = name_space
                    self.cvpdntunnelsessionusername.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvpdntunnelsessionentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvpdntunnelsessionentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvpdnTunnelSessionTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvpdnTunnelSessionEntry"):
                for c in self.cvpdntunnelsessionentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVpdnMgmtMib.Cvpdntunnelsessiontable.Cvpdntunnelsessionentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvpdntunnelsessionentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvpdnTunnelSessionEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvpdnsessionattrtable(Entity):
        """
        Table of information about individual sessions within the
        active tunnels.  An entry is added to the table when a new
        session is initiated and removed from the table when the
        session is terminated.
        
        .. attribute:: cvpdnsessionattrentry
        
        	An entry in the table, containing information about a single session within the tunnel
        	**type**\: list of    :py:class:`Cvpdnsessionattrentry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdnsessionattrtable.Cvpdnsessionattrentry>`
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CiscoVpdnMgmtMib.Cvpdnsessionattrtable, self).__init__()

            self.yang_name = "cvpdnSessionAttrTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"

            self.cvpdnsessionattrentry = YList(self)

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
                        super(CiscoVpdnMgmtMib.Cvpdnsessionattrtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVpdnMgmtMib.Cvpdnsessionattrtable, self).__setattr__(name, value)


        class Cvpdnsessionattrentry(Entity):
            """
            An entry in the table, containing information about a
            single session within the tunnel.
            
            .. attribute:: cvpdnsystemtunneltype  <key>
            
            	
            	**type**\:   :py:class:`Tunneltype <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.Tunneltype>`
            
            .. attribute:: cvpdntunnelattrtunnelid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`cvpdntunnelattrtunnelid <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdntunnelattrtable.Cvpdntunnelattrentry>`
            
            .. attribute:: cvpdnsessionattrsessionid  <key>
            
            	The ID of an active VPDN session
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cvpdnsessionattrbytesin
            
            	The total number of input bytes through this active session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cvpdnsessionattrbytesout
            
            	The total number of output bytes through this active session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cvpdnsessionattrcallduration
            
            	This object specifies the call duration of the current active session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrdevicecallerid
            
            	The incoming caller identification of the user.  It is the originating number that called into the device that initiates the session.  This object can be empty since not all dial devices can provide caller ID information
            	**type**\:  str
            
            .. attribute:: cvpdnsessionattrdevicephyid
            
            	The device ID of the physical interface for the session. The object is the the interface index which points to the ifTable.  For virtual interfaces that are not in the ifTable, the value will be zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cvpdnsessionattrdevicetype
            
            	The type of physical devices that this session is attached to for the local end of the tunnel.  The meaning of each device type is explained below\:      other\:              Any device that has not been                         defined.      asyncInternalModem\: Modem Pool device of an access                         server.      async\:              A regular asynchronous serial                         interface.      sync\:               A regular synchronous serial                         interface.      bchan\:              An ISDN call.      xdsl\:               xDSL interface.      cable\:              cable modem interface
            	**type**\:   :py:class:`Cvpdnsessionattrdevicetype <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdnsessionattrtable.Cvpdnsessionattrentry.Cvpdnsessionattrdevicetype>`
            
            .. attribute:: cvpdnsessionattrds1channelindex
            
            	The DS1 database channel index if it is associated with this session.  Only a session over a device of type 'asyncInternalModem' will have a valid value for this object; otherwise it is not instantiated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrds1portindex
            
            	The DS1 database port index if it is associated with this session.  Only a session with a device of type 'asyncInternalModem' will have a valid value for this object; otherwise it is not instantiated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrds1slotindex
            
            	The DS1 database slot index if it is associated with this session.  Only a session with a device of type 'asyncInternalModem' will have a valid value for this object; otherwise it is not instantiated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrmodemcallstartindex
            
            	Arbitrary small integer to distinguish modem calls that occurred at the same time tick.  Only session over device 'asyncInternalModem' will have a valid value for this object; otherwise, it is not instantiated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrmodemcallstarttime
            
            	The start time of the current modem call.  Only a session with a device of type 'asyncInternalModem' will have a valid value for this object; otherwise, it is not instantiated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrmodemportindex
            
            	The Modem Pool database port index if it is associated with this session.  Only a session with a device of type 'asyncInternalModem' will have a valid value for this object; otherwise, it is not instantiated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrmodemslotindex
            
            	The Modem Pool database slot index if it is associated with this session.  Only a session with device of type 'asyncInternalModem' will have a valid value for this object; otherwise, it is not instantiated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnsessionattrmultilink
            
            	This object indicates whether the session is part of a multilink PPP bundle, even if there is only one link or session in the bundle.  If it is multilink PPP, the value is true
            	**type**\:  bool
            
            .. attribute:: cvpdnsessionattrmultilinkbundle
            
            	This object specifies the name of the multilink bundle to which this session belongs.  The value of this object is only valid when the value of cvpdnSessionAttrMultilink is 'true'.  If the value of cvpdnSessionAttrMultilink is 'false', then the value of this object will be the empty string
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cvpdnsessionattrmultilinkifindex
            
            	This object specifies the ifIndex of the multilink bundle to which this session belongs.  The value of this object is only valid when the value of cvpdnSessionAttrMultilink is 'true'.  If the value of cvpdnSessionAttrMultilink is 'false', then the value of this object will be zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cvpdnsessionattrpacketsin
            
            	The total number of input packets through this active session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cvpdnsessionattrpacketsout
            
            	The total number of output packets through this active session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cvpdnsessionattrrecvpktsdropped
            
            	The total number of dropped packets that were received from this active session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cvpdnsessionattrsentpktsdropped
            
            	The total number of dropped packets that could not be sent into this active session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cvpdnsessionattrstate
            
            	The current state of a tunnel session. L2F tunnel sessions will have states with the 'l2f' prefix. L2TP tunnel sessions will have states with the 'l2tp' prefix.  Each state code is explained below\:      unknown\:             The current state of the tunnel's                          session is unknown.      l2fOpening\:          The session has just been                          initiated through a tunnel and is                          pending for the remote end reply                          to complete the process.      l2fOpen\:             The session is active.      l2fCloseWait\:        The session has just been closed                          and is pending for the remote end                          reply to complete the process.      l2fWaitingForTunnel\: The session is in this state when                          the tunnel which this session is                          going through is still in CLOSED                          state.  It waits for the tunnel to                          become OPEN before the session is                          allowed to be fully established.      l2tpIdle\:            No session is initiated yet.      l2tpWaitingTunnel\:   The session is waiting for the                          tunnel to be established.      l2tpWaitReply\:       The session has been initiated and                          is pending for the remote end                          reply to complete the process.      l2tpWaitConnect\:     This end has acknowledged a                          connection request and is waiting                          for the remote end to connect.      l2tpEstablished\:     The session is active.      l2tpShuttingDown\:    The session is in progress of                          shutting down.      pptpWaitVAccess\:     The session is waiting for the                          creation of a virtual access                          interface.      pptpPacEstablished\:  The session is active.      pptpWaitTunnel\:      The session is waiting for the                          tunnel to be established.      pptpWaitOCRP\:        The session has been initiated and                          is pending for the remote end                          reply to complete the process.      pptpPnsEstablished\:  The session is active.      pptpWaitCallDisc\:    Session shutdown is in progress
            	**type**\:   :py:class:`Cvpdnsessionattrstate <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdnsessionattrtable.Cvpdnsessionattrentry.Cvpdnsessionattrstate>`
            
            .. attribute:: cvpdnsessionattrusername
            
            	The name of the user of the session
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cvpdnsessionattrvirtualcircuitid
            
            	The virtual circuit ID of an active Layer 2 VPN session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CiscoVpdnMgmtMib.Cvpdnsessionattrtable.Cvpdnsessionattrentry, self).__init__()

                self.yang_name = "cvpdnSessionAttrEntry"
                self.yang_parent_name = "cvpdnSessionAttrTable"

                self.cvpdnsystemtunneltype = YLeaf(YType.enumeration, "cvpdnSystemTunnelType")

                self.cvpdntunnelattrtunnelid = YLeaf(YType.str, "cvpdnTunnelAttrTunnelId")

                self.cvpdnsessionattrsessionid = YLeaf(YType.int32, "cvpdnSessionAttrSessionId")

                self.cvpdnsessionattrbytesin = YLeaf(YType.uint32, "cvpdnSessionAttrBytesIn")

                self.cvpdnsessionattrbytesout = YLeaf(YType.uint32, "cvpdnSessionAttrBytesOut")

                self.cvpdnsessionattrcallduration = YLeaf(YType.uint32, "cvpdnSessionAttrCallDuration")

                self.cvpdnsessionattrdevicecallerid = YLeaf(YType.str, "cvpdnSessionAttrDeviceCallerId")

                self.cvpdnsessionattrdevicephyid = YLeaf(YType.int32, "cvpdnSessionAttrDevicePhyId")

                self.cvpdnsessionattrdevicetype = YLeaf(YType.enumeration, "cvpdnSessionAttrDeviceType")

                self.cvpdnsessionattrds1channelindex = YLeaf(YType.uint32, "cvpdnSessionAttrDS1ChannelIndex")

                self.cvpdnsessionattrds1portindex = YLeaf(YType.uint32, "cvpdnSessionAttrDS1PortIndex")

                self.cvpdnsessionattrds1slotindex = YLeaf(YType.uint32, "cvpdnSessionAttrDS1SlotIndex")

                self.cvpdnsessionattrmodemcallstartindex = YLeaf(YType.uint32, "cvpdnSessionAttrModemCallStartIndex")

                self.cvpdnsessionattrmodemcallstarttime = YLeaf(YType.uint32, "cvpdnSessionAttrModemCallStartTime")

                self.cvpdnsessionattrmodemportindex = YLeaf(YType.uint32, "cvpdnSessionAttrModemPortIndex")

                self.cvpdnsessionattrmodemslotindex = YLeaf(YType.uint32, "cvpdnSessionAttrModemSlotIndex")

                self.cvpdnsessionattrmultilink = YLeaf(YType.boolean, "cvpdnSessionAttrMultilink")

                self.cvpdnsessionattrmultilinkbundle = YLeaf(YType.str, "cvpdnSessionAttrMultilinkBundle")

                self.cvpdnsessionattrmultilinkifindex = YLeaf(YType.int32, "cvpdnSessionAttrMultilinkIfIndex")

                self.cvpdnsessionattrpacketsin = YLeaf(YType.uint32, "cvpdnSessionAttrPacketsIn")

                self.cvpdnsessionattrpacketsout = YLeaf(YType.uint32, "cvpdnSessionAttrPacketsOut")

                self.cvpdnsessionattrrecvpktsdropped = YLeaf(YType.uint32, "cvpdnSessionAttrRecvPktsDropped")

                self.cvpdnsessionattrsentpktsdropped = YLeaf(YType.uint32, "cvpdnSessionAttrSentPktsDropped")

                self.cvpdnsessionattrstate = YLeaf(YType.enumeration, "cvpdnSessionAttrState")

                self.cvpdnsessionattrusername = YLeaf(YType.str, "cvpdnSessionAttrUserName")

                self.cvpdnsessionattrvirtualcircuitid = YLeaf(YType.uint32, "cvpdnSessionAttrVirtualCircuitID")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cvpdnsystemtunneltype",
                                "cvpdntunnelattrtunnelid",
                                "cvpdnsessionattrsessionid",
                                "cvpdnsessionattrbytesin",
                                "cvpdnsessionattrbytesout",
                                "cvpdnsessionattrcallduration",
                                "cvpdnsessionattrdevicecallerid",
                                "cvpdnsessionattrdevicephyid",
                                "cvpdnsessionattrdevicetype",
                                "cvpdnsessionattrds1channelindex",
                                "cvpdnsessionattrds1portindex",
                                "cvpdnsessionattrds1slotindex",
                                "cvpdnsessionattrmodemcallstartindex",
                                "cvpdnsessionattrmodemcallstarttime",
                                "cvpdnsessionattrmodemportindex",
                                "cvpdnsessionattrmodemslotindex",
                                "cvpdnsessionattrmultilink",
                                "cvpdnsessionattrmultilinkbundle",
                                "cvpdnsessionattrmultilinkifindex",
                                "cvpdnsessionattrpacketsin",
                                "cvpdnsessionattrpacketsout",
                                "cvpdnsessionattrrecvpktsdropped",
                                "cvpdnsessionattrsentpktsdropped",
                                "cvpdnsessionattrstate",
                                "cvpdnsessionattrusername",
                                "cvpdnsessionattrvirtualcircuitid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVpdnMgmtMib.Cvpdnsessionattrtable.Cvpdnsessionattrentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVpdnMgmtMib.Cvpdnsessionattrtable.Cvpdnsessionattrentry, self).__setattr__(name, value)

            class Cvpdnsessionattrdevicetype(Enum):
                """
                Cvpdnsessionattrdevicetype

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
                Cvpdnsessionattrstate

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


            def has_data(self):
                return (
                    self.cvpdnsystemtunneltype.is_set or
                    self.cvpdntunnelattrtunnelid.is_set or
                    self.cvpdnsessionattrsessionid.is_set or
                    self.cvpdnsessionattrbytesin.is_set or
                    self.cvpdnsessionattrbytesout.is_set or
                    self.cvpdnsessionattrcallduration.is_set or
                    self.cvpdnsessionattrdevicecallerid.is_set or
                    self.cvpdnsessionattrdevicephyid.is_set or
                    self.cvpdnsessionattrdevicetype.is_set or
                    self.cvpdnsessionattrds1channelindex.is_set or
                    self.cvpdnsessionattrds1portindex.is_set or
                    self.cvpdnsessionattrds1slotindex.is_set or
                    self.cvpdnsessionattrmodemcallstartindex.is_set or
                    self.cvpdnsessionattrmodemcallstarttime.is_set or
                    self.cvpdnsessionattrmodemportindex.is_set or
                    self.cvpdnsessionattrmodemslotindex.is_set or
                    self.cvpdnsessionattrmultilink.is_set or
                    self.cvpdnsessionattrmultilinkbundle.is_set or
                    self.cvpdnsessionattrmultilinkifindex.is_set or
                    self.cvpdnsessionattrpacketsin.is_set or
                    self.cvpdnsessionattrpacketsout.is_set or
                    self.cvpdnsessionattrrecvpktsdropped.is_set or
                    self.cvpdnsessionattrsentpktsdropped.is_set or
                    self.cvpdnsessionattrstate.is_set or
                    self.cvpdnsessionattrusername.is_set or
                    self.cvpdnsessionattrvirtualcircuitid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cvpdnsystemtunneltype.yfilter != YFilter.not_set or
                    self.cvpdntunnelattrtunnelid.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrsessionid.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrbytesin.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrbytesout.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrcallduration.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrdevicecallerid.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrdevicephyid.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrdevicetype.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrds1channelindex.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrds1portindex.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrds1slotindex.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrmodemcallstartindex.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrmodemcallstarttime.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrmodemportindex.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrmodemslotindex.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrmultilink.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrmultilinkbundle.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrmultilinkifindex.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrpacketsin.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrpacketsout.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrrecvpktsdropped.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrsentpktsdropped.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrstate.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrusername.yfilter != YFilter.not_set or
                    self.cvpdnsessionattrvirtualcircuitid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvpdnSessionAttrEntry" + "[cvpdnSystemTunnelType='" + self.cvpdnsystemtunneltype.get() + "']" + "[cvpdnTunnelAttrTunnelId='" + self.cvpdntunnelattrtunnelid.get() + "']" + "[cvpdnSessionAttrSessionId='" + self.cvpdnsessionattrsessionid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/cvpdnSessionAttrTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cvpdnsystemtunneltype.is_set or self.cvpdnsystemtunneltype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsystemtunneltype.get_name_leafdata())
                if (self.cvpdntunnelattrtunnelid.is_set or self.cvpdntunnelattrtunnelid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntunnelattrtunnelid.get_name_leafdata())
                if (self.cvpdnsessionattrsessionid.is_set or self.cvpdnsessionattrsessionid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrsessionid.get_name_leafdata())
                if (self.cvpdnsessionattrbytesin.is_set or self.cvpdnsessionattrbytesin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrbytesin.get_name_leafdata())
                if (self.cvpdnsessionattrbytesout.is_set or self.cvpdnsessionattrbytesout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrbytesout.get_name_leafdata())
                if (self.cvpdnsessionattrcallduration.is_set or self.cvpdnsessionattrcallduration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrcallduration.get_name_leafdata())
                if (self.cvpdnsessionattrdevicecallerid.is_set or self.cvpdnsessionattrdevicecallerid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrdevicecallerid.get_name_leafdata())
                if (self.cvpdnsessionattrdevicephyid.is_set or self.cvpdnsessionattrdevicephyid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrdevicephyid.get_name_leafdata())
                if (self.cvpdnsessionattrdevicetype.is_set or self.cvpdnsessionattrdevicetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrdevicetype.get_name_leafdata())
                if (self.cvpdnsessionattrds1channelindex.is_set or self.cvpdnsessionattrds1channelindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrds1channelindex.get_name_leafdata())
                if (self.cvpdnsessionattrds1portindex.is_set or self.cvpdnsessionattrds1portindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrds1portindex.get_name_leafdata())
                if (self.cvpdnsessionattrds1slotindex.is_set or self.cvpdnsessionattrds1slotindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrds1slotindex.get_name_leafdata())
                if (self.cvpdnsessionattrmodemcallstartindex.is_set or self.cvpdnsessionattrmodemcallstartindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrmodemcallstartindex.get_name_leafdata())
                if (self.cvpdnsessionattrmodemcallstarttime.is_set or self.cvpdnsessionattrmodemcallstarttime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrmodemcallstarttime.get_name_leafdata())
                if (self.cvpdnsessionattrmodemportindex.is_set or self.cvpdnsessionattrmodemportindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrmodemportindex.get_name_leafdata())
                if (self.cvpdnsessionattrmodemslotindex.is_set or self.cvpdnsessionattrmodemslotindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrmodemslotindex.get_name_leafdata())
                if (self.cvpdnsessionattrmultilink.is_set or self.cvpdnsessionattrmultilink.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrmultilink.get_name_leafdata())
                if (self.cvpdnsessionattrmultilinkbundle.is_set or self.cvpdnsessionattrmultilinkbundle.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrmultilinkbundle.get_name_leafdata())
                if (self.cvpdnsessionattrmultilinkifindex.is_set or self.cvpdnsessionattrmultilinkifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrmultilinkifindex.get_name_leafdata())
                if (self.cvpdnsessionattrpacketsin.is_set or self.cvpdnsessionattrpacketsin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrpacketsin.get_name_leafdata())
                if (self.cvpdnsessionattrpacketsout.is_set or self.cvpdnsessionattrpacketsout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrpacketsout.get_name_leafdata())
                if (self.cvpdnsessionattrrecvpktsdropped.is_set or self.cvpdnsessionattrrecvpktsdropped.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrrecvpktsdropped.get_name_leafdata())
                if (self.cvpdnsessionattrsentpktsdropped.is_set or self.cvpdnsessionattrsentpktsdropped.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrsentpktsdropped.get_name_leafdata())
                if (self.cvpdnsessionattrstate.is_set or self.cvpdnsessionattrstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrstate.get_name_leafdata())
                if (self.cvpdnsessionattrusername.is_set or self.cvpdnsessionattrusername.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrusername.get_name_leafdata())
                if (self.cvpdnsessionattrvirtualcircuitid.is_set or self.cvpdnsessionattrvirtualcircuitid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnsessionattrvirtualcircuitid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cvpdnSystemTunnelType" or name == "cvpdnTunnelAttrTunnelId" or name == "cvpdnSessionAttrSessionId" or name == "cvpdnSessionAttrBytesIn" or name == "cvpdnSessionAttrBytesOut" or name == "cvpdnSessionAttrCallDuration" or name == "cvpdnSessionAttrDeviceCallerId" or name == "cvpdnSessionAttrDevicePhyId" or name == "cvpdnSessionAttrDeviceType" or name == "cvpdnSessionAttrDS1ChannelIndex" or name == "cvpdnSessionAttrDS1PortIndex" or name == "cvpdnSessionAttrDS1SlotIndex" or name == "cvpdnSessionAttrModemCallStartIndex" or name == "cvpdnSessionAttrModemCallStartTime" or name == "cvpdnSessionAttrModemPortIndex" or name == "cvpdnSessionAttrModemSlotIndex" or name == "cvpdnSessionAttrMultilink" or name == "cvpdnSessionAttrMultilinkBundle" or name == "cvpdnSessionAttrMultilinkIfIndex" or name == "cvpdnSessionAttrPacketsIn" or name == "cvpdnSessionAttrPacketsOut" or name == "cvpdnSessionAttrRecvPktsDropped" or name == "cvpdnSessionAttrSentPktsDropped" or name == "cvpdnSessionAttrState" or name == "cvpdnSessionAttrUserName" or name == "cvpdnSessionAttrVirtualCircuitID"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cvpdnSystemTunnelType"):
                    self.cvpdnsystemtunneltype = value
                    self.cvpdnsystemtunneltype.value_namespace = name_space
                    self.cvpdnsystemtunneltype.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTunnelAttrTunnelId"):
                    self.cvpdntunnelattrtunnelid = value
                    self.cvpdntunnelattrtunnelid.value_namespace = name_space
                    self.cvpdntunnelattrtunnelid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrSessionId"):
                    self.cvpdnsessionattrsessionid = value
                    self.cvpdnsessionattrsessionid.value_namespace = name_space
                    self.cvpdnsessionattrsessionid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrBytesIn"):
                    self.cvpdnsessionattrbytesin = value
                    self.cvpdnsessionattrbytesin.value_namespace = name_space
                    self.cvpdnsessionattrbytesin.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrBytesOut"):
                    self.cvpdnsessionattrbytesout = value
                    self.cvpdnsessionattrbytesout.value_namespace = name_space
                    self.cvpdnsessionattrbytesout.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrCallDuration"):
                    self.cvpdnsessionattrcallduration = value
                    self.cvpdnsessionattrcallduration.value_namespace = name_space
                    self.cvpdnsessionattrcallduration.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrDeviceCallerId"):
                    self.cvpdnsessionattrdevicecallerid = value
                    self.cvpdnsessionattrdevicecallerid.value_namespace = name_space
                    self.cvpdnsessionattrdevicecallerid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrDevicePhyId"):
                    self.cvpdnsessionattrdevicephyid = value
                    self.cvpdnsessionattrdevicephyid.value_namespace = name_space
                    self.cvpdnsessionattrdevicephyid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrDeviceType"):
                    self.cvpdnsessionattrdevicetype = value
                    self.cvpdnsessionattrdevicetype.value_namespace = name_space
                    self.cvpdnsessionattrdevicetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrDS1ChannelIndex"):
                    self.cvpdnsessionattrds1channelindex = value
                    self.cvpdnsessionattrds1channelindex.value_namespace = name_space
                    self.cvpdnsessionattrds1channelindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrDS1PortIndex"):
                    self.cvpdnsessionattrds1portindex = value
                    self.cvpdnsessionattrds1portindex.value_namespace = name_space
                    self.cvpdnsessionattrds1portindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrDS1SlotIndex"):
                    self.cvpdnsessionattrds1slotindex = value
                    self.cvpdnsessionattrds1slotindex.value_namespace = name_space
                    self.cvpdnsessionattrds1slotindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrModemCallStartIndex"):
                    self.cvpdnsessionattrmodemcallstartindex = value
                    self.cvpdnsessionattrmodemcallstartindex.value_namespace = name_space
                    self.cvpdnsessionattrmodemcallstartindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrModemCallStartTime"):
                    self.cvpdnsessionattrmodemcallstarttime = value
                    self.cvpdnsessionattrmodemcallstarttime.value_namespace = name_space
                    self.cvpdnsessionattrmodemcallstarttime.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrModemPortIndex"):
                    self.cvpdnsessionattrmodemportindex = value
                    self.cvpdnsessionattrmodemportindex.value_namespace = name_space
                    self.cvpdnsessionattrmodemportindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrModemSlotIndex"):
                    self.cvpdnsessionattrmodemslotindex = value
                    self.cvpdnsessionattrmodemslotindex.value_namespace = name_space
                    self.cvpdnsessionattrmodemslotindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrMultilink"):
                    self.cvpdnsessionattrmultilink = value
                    self.cvpdnsessionattrmultilink.value_namespace = name_space
                    self.cvpdnsessionattrmultilink.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrMultilinkBundle"):
                    self.cvpdnsessionattrmultilinkbundle = value
                    self.cvpdnsessionattrmultilinkbundle.value_namespace = name_space
                    self.cvpdnsessionattrmultilinkbundle.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrMultilinkIfIndex"):
                    self.cvpdnsessionattrmultilinkifindex = value
                    self.cvpdnsessionattrmultilinkifindex.value_namespace = name_space
                    self.cvpdnsessionattrmultilinkifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrPacketsIn"):
                    self.cvpdnsessionattrpacketsin = value
                    self.cvpdnsessionattrpacketsin.value_namespace = name_space
                    self.cvpdnsessionattrpacketsin.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrPacketsOut"):
                    self.cvpdnsessionattrpacketsout = value
                    self.cvpdnsessionattrpacketsout.value_namespace = name_space
                    self.cvpdnsessionattrpacketsout.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrRecvPktsDropped"):
                    self.cvpdnsessionattrrecvpktsdropped = value
                    self.cvpdnsessionattrrecvpktsdropped.value_namespace = name_space
                    self.cvpdnsessionattrrecvpktsdropped.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrSentPktsDropped"):
                    self.cvpdnsessionattrsentpktsdropped = value
                    self.cvpdnsessionattrsentpktsdropped.value_namespace = name_space
                    self.cvpdnsessionattrsentpktsdropped.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrState"):
                    self.cvpdnsessionattrstate = value
                    self.cvpdnsessionattrstate.value_namespace = name_space
                    self.cvpdnsessionattrstate.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrUserName"):
                    self.cvpdnsessionattrusername = value
                    self.cvpdnsessionattrusername.value_namespace = name_space
                    self.cvpdnsessionattrusername.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnSessionAttrVirtualCircuitID"):
                    self.cvpdnsessionattrvirtualcircuitid = value
                    self.cvpdnsessionattrvirtualcircuitid.value_namespace = name_space
                    self.cvpdnsessionattrvirtualcircuitid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvpdnsessionattrentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvpdnsessionattrentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvpdnSessionAttrTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvpdnSessionAttrEntry"):
                for c in self.cvpdnsessionattrentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVpdnMgmtMib.Cvpdnsessionattrtable.Cvpdnsessionattrentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvpdnsessionattrentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvpdnSessionAttrEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cvpdnusertofailhistinfoentry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdnusertofailhistinfotable.Cvpdnusertofailhistinfoentry>`
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CiscoVpdnMgmtMib.Cvpdnusertofailhistinfotable, self).__init__()

            self.yang_name = "cvpdnUserToFailHistInfoTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"

            self.cvpdnusertofailhistinfoentry = YList(self)

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
                        super(CiscoVpdnMgmtMib.Cvpdnusertofailhistinfotable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVpdnMgmtMib.Cvpdnusertofailhistinfotable, self).__setattr__(name, value)


        class Cvpdnusertofailhistinfoentry(Entity):
            """
            An entry in the table, containing failure history
            relevant to an user name.
            
            .. attribute:: cvpdnunametofailhistuname  <key>
            
            	The user name for this failure entry
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cvpdnunametofailhisttunnelid  <key>
            
            	The Tunnel ID for this failure entry.  If it is the instigator of the tunnel, the ID is the TS tunnel ID, otherwise it is the NAS tunnel ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnunametofailhistcount
            
            	This object is incremented when multiple failures has been experienced by this user on this tunnel.  Seeing a delta of >1 is an indication that the current failure record is the latest of a series of failures that has been recorded
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: failures
            
            .. attribute:: cvpdnunametofailhistdestinetaddr
            
            	The destination IP address of the tunnel in which the failure occurred.  This IP address is that of the interface at the receiver end of the tunnel.  The type  of this address is determined by the value of  cvpdnUnameToFailHistDestInetType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cvpdnunametofailhistdestinettype
            
            	Indicates the type of address contained in cvpdnUnameToFailHistDestInetAddr
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cvpdnunametofailhistdestip
            
            	The destination IP address of the tunnel in which the failure occurred.  This IP address is that of the interface at the receiver end of the tunnel
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cvpdnunametofailhistfailreason
            
            	The reason of failure for the current failure record
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cvpdnunametofailhistfailtime
            
            	This object specifies the time when the failure is occurred
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnunametofailhistfailtype
            
            	The type of failure for the current failure record.  It comes in a form of a an ASCII string which describes the type of failure
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cvpdnunametofailhistlocalinitconn
            
            	This object indicates whether the tunnel in which the failure occurred was generated locally or not
            	**type**\:  bool
            
            .. attribute:: cvpdnunametofailhistlocalname
            
            	The local name of the VPDN tunnel in which the failure occurred.  It will be the NAS name of the tunnel if the system serves as the NAS, or the TS name of the tunnel if the system serves as the tunnel server.  The local name is the configured host name of the system.  This object can be empty if the failure occurred prior to successful tunnel projection, thus no source name will be available
            	**type**\:  str
            
            .. attribute:: cvpdnunametofailhistremotename
            
            	The remote name of the VPDN tunnel in which the failure occurred.  It will be the tunnel server name of the tunnel if the system is a NAS, or the NAS name of the tunnel if the system serves as the tunnel server.  This object can be empty if the failure occurred prior to successful tunnel projection, thus no source name will be available
            	**type**\:  str
            
            .. attribute:: cvpdnunametofailhistsourceinetaddr
            
            	The source IP address of the tunnel in which the failure occurred.  This IP address is that of the interface at the instigator end of the tunnel.  The instigator end is the peer which initiates the tunnel estalishment.  The type of this address is determined by the value of cvpdnUnameToFailHistSourceInetType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cvpdnunametofailhistsourceinettype
            
            	Indicates the type of address contained in cvpdnUnameToFailHistSourceInetAddr
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cvpdnunametofailhistsourceip
            
            	The source IP address of the tunnel in which the failure occurred.  This IP address is that of the interface at the instigator end of the tunnel
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cvpdnunametofailhistuserid
            
            	The user ID of this failure entry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CiscoVpdnMgmtMib.Cvpdnusertofailhistinfotable.Cvpdnusertofailhistinfoentry, self).__init__()

                self.yang_name = "cvpdnUserToFailHistInfoEntry"
                self.yang_parent_name = "cvpdnUserToFailHistInfoTable"

                self.cvpdnunametofailhistuname = YLeaf(YType.str, "cvpdnUnameToFailHistUname")

                self.cvpdnunametofailhisttunnelid = YLeaf(YType.uint32, "cvpdnUnameToFailHistTunnelId")

                self.cvpdnunametofailhistcount = YLeaf(YType.uint32, "cvpdnUnameToFailHistCount")

                self.cvpdnunametofailhistdestinetaddr = YLeaf(YType.str, "cvpdnUnameToFailHistDestInetAddr")

                self.cvpdnunametofailhistdestinettype = YLeaf(YType.enumeration, "cvpdnUnameToFailHistDestInetType")

                self.cvpdnunametofailhistdestip = YLeaf(YType.str, "cvpdnUnameToFailHistDestIp")

                self.cvpdnunametofailhistfailreason = YLeaf(YType.str, "cvpdnUnameToFailHistFailReason")

                self.cvpdnunametofailhistfailtime = YLeaf(YType.uint32, "cvpdnUnameToFailHistFailTime")

                self.cvpdnunametofailhistfailtype = YLeaf(YType.str, "cvpdnUnameToFailHistFailType")

                self.cvpdnunametofailhistlocalinitconn = YLeaf(YType.boolean, "cvpdnUnameToFailHistLocalInitConn")

                self.cvpdnunametofailhistlocalname = YLeaf(YType.str, "cvpdnUnameToFailHistLocalName")

                self.cvpdnunametofailhistremotename = YLeaf(YType.str, "cvpdnUnameToFailHistRemoteName")

                self.cvpdnunametofailhistsourceinetaddr = YLeaf(YType.str, "cvpdnUnameToFailHistSourceInetAddr")

                self.cvpdnunametofailhistsourceinettype = YLeaf(YType.enumeration, "cvpdnUnameToFailHistSourceInetType")

                self.cvpdnunametofailhistsourceip = YLeaf(YType.str, "cvpdnUnameToFailHistSourceIp")

                self.cvpdnunametofailhistuserid = YLeaf(YType.uint32, "cvpdnUnameToFailHistUserId")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cvpdnunametofailhistuname",
                                "cvpdnunametofailhisttunnelid",
                                "cvpdnunametofailhistcount",
                                "cvpdnunametofailhistdestinetaddr",
                                "cvpdnunametofailhistdestinettype",
                                "cvpdnunametofailhistdestip",
                                "cvpdnunametofailhistfailreason",
                                "cvpdnunametofailhistfailtime",
                                "cvpdnunametofailhistfailtype",
                                "cvpdnunametofailhistlocalinitconn",
                                "cvpdnunametofailhistlocalname",
                                "cvpdnunametofailhistremotename",
                                "cvpdnunametofailhistsourceinetaddr",
                                "cvpdnunametofailhistsourceinettype",
                                "cvpdnunametofailhistsourceip",
                                "cvpdnunametofailhistuserid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVpdnMgmtMib.Cvpdnusertofailhistinfotable.Cvpdnusertofailhistinfoentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVpdnMgmtMib.Cvpdnusertofailhistinfotable.Cvpdnusertofailhistinfoentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cvpdnunametofailhistuname.is_set or
                    self.cvpdnunametofailhisttunnelid.is_set or
                    self.cvpdnunametofailhistcount.is_set or
                    self.cvpdnunametofailhistdestinetaddr.is_set or
                    self.cvpdnunametofailhistdestinettype.is_set or
                    self.cvpdnunametofailhistdestip.is_set or
                    self.cvpdnunametofailhistfailreason.is_set or
                    self.cvpdnunametofailhistfailtime.is_set or
                    self.cvpdnunametofailhistfailtype.is_set or
                    self.cvpdnunametofailhistlocalinitconn.is_set or
                    self.cvpdnunametofailhistlocalname.is_set or
                    self.cvpdnunametofailhistremotename.is_set or
                    self.cvpdnunametofailhistsourceinetaddr.is_set or
                    self.cvpdnunametofailhistsourceinettype.is_set or
                    self.cvpdnunametofailhistsourceip.is_set or
                    self.cvpdnunametofailhistuserid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cvpdnunametofailhistuname.yfilter != YFilter.not_set or
                    self.cvpdnunametofailhisttunnelid.yfilter != YFilter.not_set or
                    self.cvpdnunametofailhistcount.yfilter != YFilter.not_set or
                    self.cvpdnunametofailhistdestinetaddr.yfilter != YFilter.not_set or
                    self.cvpdnunametofailhistdestinettype.yfilter != YFilter.not_set or
                    self.cvpdnunametofailhistdestip.yfilter != YFilter.not_set or
                    self.cvpdnunametofailhistfailreason.yfilter != YFilter.not_set or
                    self.cvpdnunametofailhistfailtime.yfilter != YFilter.not_set or
                    self.cvpdnunametofailhistfailtype.yfilter != YFilter.not_set or
                    self.cvpdnunametofailhistlocalinitconn.yfilter != YFilter.not_set or
                    self.cvpdnunametofailhistlocalname.yfilter != YFilter.not_set or
                    self.cvpdnunametofailhistremotename.yfilter != YFilter.not_set or
                    self.cvpdnunametofailhistsourceinetaddr.yfilter != YFilter.not_set or
                    self.cvpdnunametofailhistsourceinettype.yfilter != YFilter.not_set or
                    self.cvpdnunametofailhistsourceip.yfilter != YFilter.not_set or
                    self.cvpdnunametofailhistuserid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvpdnUserToFailHistInfoEntry" + "[cvpdnUnameToFailHistUname='" + self.cvpdnunametofailhistuname.get() + "']" + "[cvpdnUnameToFailHistTunnelId='" + self.cvpdnunametofailhisttunnelid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/cvpdnUserToFailHistInfoTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cvpdnunametofailhistuname.is_set or self.cvpdnunametofailhistuname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnunametofailhistuname.get_name_leafdata())
                if (self.cvpdnunametofailhisttunnelid.is_set or self.cvpdnunametofailhisttunnelid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnunametofailhisttunnelid.get_name_leafdata())
                if (self.cvpdnunametofailhistcount.is_set or self.cvpdnunametofailhistcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnunametofailhistcount.get_name_leafdata())
                if (self.cvpdnunametofailhistdestinetaddr.is_set or self.cvpdnunametofailhistdestinetaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnunametofailhistdestinetaddr.get_name_leafdata())
                if (self.cvpdnunametofailhistdestinettype.is_set or self.cvpdnunametofailhistdestinettype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnunametofailhistdestinettype.get_name_leafdata())
                if (self.cvpdnunametofailhistdestip.is_set or self.cvpdnunametofailhistdestip.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnunametofailhistdestip.get_name_leafdata())
                if (self.cvpdnunametofailhistfailreason.is_set or self.cvpdnunametofailhistfailreason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnunametofailhistfailreason.get_name_leafdata())
                if (self.cvpdnunametofailhistfailtime.is_set or self.cvpdnunametofailhistfailtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnunametofailhistfailtime.get_name_leafdata())
                if (self.cvpdnunametofailhistfailtype.is_set or self.cvpdnunametofailhistfailtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnunametofailhistfailtype.get_name_leafdata())
                if (self.cvpdnunametofailhistlocalinitconn.is_set or self.cvpdnunametofailhistlocalinitconn.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnunametofailhistlocalinitconn.get_name_leafdata())
                if (self.cvpdnunametofailhistlocalname.is_set or self.cvpdnunametofailhistlocalname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnunametofailhistlocalname.get_name_leafdata())
                if (self.cvpdnunametofailhistremotename.is_set or self.cvpdnunametofailhistremotename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnunametofailhistremotename.get_name_leafdata())
                if (self.cvpdnunametofailhistsourceinetaddr.is_set or self.cvpdnunametofailhistsourceinetaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnunametofailhistsourceinetaddr.get_name_leafdata())
                if (self.cvpdnunametofailhistsourceinettype.is_set or self.cvpdnunametofailhistsourceinettype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnunametofailhistsourceinettype.get_name_leafdata())
                if (self.cvpdnunametofailhistsourceip.is_set or self.cvpdnunametofailhistsourceip.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnunametofailhistsourceip.get_name_leafdata())
                if (self.cvpdnunametofailhistuserid.is_set or self.cvpdnunametofailhistuserid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnunametofailhistuserid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cvpdnUnameToFailHistUname" or name == "cvpdnUnameToFailHistTunnelId" or name == "cvpdnUnameToFailHistCount" or name == "cvpdnUnameToFailHistDestInetAddr" or name == "cvpdnUnameToFailHistDestInetType" or name == "cvpdnUnameToFailHistDestIp" or name == "cvpdnUnameToFailHistFailReason" or name == "cvpdnUnameToFailHistFailTime" or name == "cvpdnUnameToFailHistFailType" or name == "cvpdnUnameToFailHistLocalInitConn" or name == "cvpdnUnameToFailHistLocalName" or name == "cvpdnUnameToFailHistRemoteName" or name == "cvpdnUnameToFailHistSourceInetAddr" or name == "cvpdnUnameToFailHistSourceInetType" or name == "cvpdnUnameToFailHistSourceIp" or name == "cvpdnUnameToFailHistUserId"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cvpdnUnameToFailHistUname"):
                    self.cvpdnunametofailhistuname = value
                    self.cvpdnunametofailhistuname.value_namespace = name_space
                    self.cvpdnunametofailhistuname.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnUnameToFailHistTunnelId"):
                    self.cvpdnunametofailhisttunnelid = value
                    self.cvpdnunametofailhisttunnelid.value_namespace = name_space
                    self.cvpdnunametofailhisttunnelid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnUnameToFailHistCount"):
                    self.cvpdnunametofailhistcount = value
                    self.cvpdnunametofailhistcount.value_namespace = name_space
                    self.cvpdnunametofailhistcount.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnUnameToFailHistDestInetAddr"):
                    self.cvpdnunametofailhistdestinetaddr = value
                    self.cvpdnunametofailhistdestinetaddr.value_namespace = name_space
                    self.cvpdnunametofailhistdestinetaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnUnameToFailHistDestInetType"):
                    self.cvpdnunametofailhistdestinettype = value
                    self.cvpdnunametofailhistdestinettype.value_namespace = name_space
                    self.cvpdnunametofailhistdestinettype.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnUnameToFailHistDestIp"):
                    self.cvpdnunametofailhistdestip = value
                    self.cvpdnunametofailhistdestip.value_namespace = name_space
                    self.cvpdnunametofailhistdestip.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnUnameToFailHistFailReason"):
                    self.cvpdnunametofailhistfailreason = value
                    self.cvpdnunametofailhistfailreason.value_namespace = name_space
                    self.cvpdnunametofailhistfailreason.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnUnameToFailHistFailTime"):
                    self.cvpdnunametofailhistfailtime = value
                    self.cvpdnunametofailhistfailtime.value_namespace = name_space
                    self.cvpdnunametofailhistfailtime.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnUnameToFailHistFailType"):
                    self.cvpdnunametofailhistfailtype = value
                    self.cvpdnunametofailhistfailtype.value_namespace = name_space
                    self.cvpdnunametofailhistfailtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnUnameToFailHistLocalInitConn"):
                    self.cvpdnunametofailhistlocalinitconn = value
                    self.cvpdnunametofailhistlocalinitconn.value_namespace = name_space
                    self.cvpdnunametofailhistlocalinitconn.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnUnameToFailHistLocalName"):
                    self.cvpdnunametofailhistlocalname = value
                    self.cvpdnunametofailhistlocalname.value_namespace = name_space
                    self.cvpdnunametofailhistlocalname.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnUnameToFailHistRemoteName"):
                    self.cvpdnunametofailhistremotename = value
                    self.cvpdnunametofailhistremotename.value_namespace = name_space
                    self.cvpdnunametofailhistremotename.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnUnameToFailHistSourceInetAddr"):
                    self.cvpdnunametofailhistsourceinetaddr = value
                    self.cvpdnunametofailhistsourceinetaddr.value_namespace = name_space
                    self.cvpdnunametofailhistsourceinetaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnUnameToFailHistSourceInetType"):
                    self.cvpdnunametofailhistsourceinettype = value
                    self.cvpdnunametofailhistsourceinettype.value_namespace = name_space
                    self.cvpdnunametofailhistsourceinettype.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnUnameToFailHistSourceIp"):
                    self.cvpdnunametofailhistsourceip = value
                    self.cvpdnunametofailhistsourceip.value_namespace = name_space
                    self.cvpdnunametofailhistsourceip.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnUnameToFailHistUserId"):
                    self.cvpdnunametofailhistuserid = value
                    self.cvpdnunametofailhistuserid.value_namespace = name_space
                    self.cvpdnunametofailhistuserid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvpdnusertofailhistinfoentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvpdnusertofailhistinfoentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvpdnUserToFailHistInfoTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvpdnUserToFailHistInfoEntry"):
                for c in self.cvpdnusertofailhistinfoentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVpdnMgmtMib.Cvpdnusertofailhistinfotable.Cvpdnusertofailhistinfoentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvpdnusertofailhistinfoentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvpdnUserToFailHistInfoEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cvpdntemplateentry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdntemplatetable.Cvpdntemplateentry>`
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CiscoVpdnMgmtMib.Cvpdntemplatetable, self).__init__()

            self.yang_name = "cvpdnTemplateTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"

            self.cvpdntemplateentry = YList(self)

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
                        super(CiscoVpdnMgmtMib.Cvpdntemplatetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVpdnMgmtMib.Cvpdntemplatetable, self).__setattr__(name, value)


        class Cvpdntemplateentry(Entity):
            """
            An entry in the table, containing information about a
            single VPDN template.
            
            .. attribute:: cvpdntemplatename  <key>
            
            	The name of the VPDN template
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: cvpdntemplateactivesessions
            
            	The total number of active session in all groups associated with the template
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CiscoVpdnMgmtMib.Cvpdntemplatetable.Cvpdntemplateentry, self).__init__()

                self.yang_name = "cvpdnTemplateEntry"
                self.yang_parent_name = "cvpdnTemplateTable"

                self.cvpdntemplatename = YLeaf(YType.str, "cvpdnTemplateName")

                self.cvpdntemplateactivesessions = YLeaf(YType.uint32, "cvpdnTemplateActiveSessions")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cvpdntemplatename",
                                "cvpdntemplateactivesessions") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVpdnMgmtMib.Cvpdntemplatetable.Cvpdntemplateentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVpdnMgmtMib.Cvpdntemplatetable.Cvpdntemplateentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cvpdntemplatename.is_set or
                    self.cvpdntemplateactivesessions.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cvpdntemplatename.yfilter != YFilter.not_set or
                    self.cvpdntemplateactivesessions.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvpdnTemplateEntry" + "[cvpdnTemplateName='" + self.cvpdntemplatename.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/cvpdnTemplateTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cvpdntemplatename.is_set or self.cvpdntemplatename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntemplatename.get_name_leafdata())
                if (self.cvpdntemplateactivesessions.is_set or self.cvpdntemplateactivesessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdntemplateactivesessions.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cvpdnTemplateName" or name == "cvpdnTemplateActiveSessions"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cvpdnTemplateName"):
                    self.cvpdntemplatename = value
                    self.cvpdntemplatename.value_namespace = name_space
                    self.cvpdntemplatename.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnTemplateActiveSessions"):
                    self.cvpdntemplateactivesessions = value
                    self.cvpdntemplateactivesessions.value_namespace = name_space
                    self.cvpdntemplateactivesessions.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvpdntemplateentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvpdntemplateentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvpdnTemplateTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvpdnTemplateEntry"):
                for c in self.cvpdntemplateentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVpdnMgmtMib.Cvpdntemplatetable.Cvpdntemplateentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvpdntemplateentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvpdnTemplateEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvpdnbundletable(Entity):
        """
        Table that describes the multilink PPP attributes of the
        active VPDN sessions.
        
        .. attribute:: cvpdnbundleentry
        
        	An entry in this table represents an active multilink PPP bundle that belongs to a VPDN tunnel
        	**type**\: list of    :py:class:`Cvpdnbundleentry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdnbundletable.Cvpdnbundleentry>`
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CiscoVpdnMgmtMib.Cvpdnbundletable, self).__init__()

            self.yang_name = "cvpdnBundleTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"

            self.cvpdnbundleentry = YList(self)

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
                        super(CiscoVpdnMgmtMib.Cvpdnbundletable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVpdnMgmtMib.Cvpdnbundletable, self).__setattr__(name, value)


        class Cvpdnbundleentry(Entity):
            """
            An entry in this table represents an active multilink PPP
            bundle that belongs to a VPDN tunnel.
            
            .. attribute:: cvpdnbundlename  <key>
            
            	The name of the multilink PPP bundle associated with a VPDN tunnel
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cvpdnbundleendpoint
            
            	Indicates the discriminator used in this bundle that is associated with a VPDN tunnel
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cvpdnbundleendpointclass
            
            	The multilink PPP bundle discriminator class associated with a VPDN tunnel.  The value of this object represents the type of discriminator used in cvpdnBundleEndpoint
            	**type**\:   :py:class:`Endpointclass <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.Endpointclass>`
            
            .. attribute:: cvpdnbundleendpointtype
            
            	The multilink PPP bundle discriminator type associated with a VPDN tunnel.  The value of this object represents the type of discriminator used in cvpdnBundleEndpoint.      none\:        No endpoint discriminator was supplied, the                  default value is being used.      hostname\:    The router's hostname is being used as                  discriminator.      string\:      User specified string is being used as                  discriminator.      macAddress\:  A MAC address as defined by the MacAddress                  textual convention is being used as                  discriminator.      ipV4Address\: An IP address as defined by the                  InetAddressIPv4 textual convention is being                  used as discriminator.      ipV6Address\: An IP address as defined by the                  InetAddressIPv6 textual convention is being                  used as discriminator.      phone\:       The PSTN phone number is being used as                  discriminator.      magicNumber\: A magic number is being used as                  discriminator
            	**type**\:   :py:class:`Cvpdnbundleendpointtype <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdnbundletable.Cvpdnbundleentry.Cvpdnbundleendpointtype>`
            
            	**status**\: deprecated
            
            .. attribute:: cvpdnbundlelinkcount
            
            	The total number of active links in a multilink PPP bundle associated with a VPDN tunnel
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: links
            
            .. attribute:: cvpdnbundlepeeripaddr
            
            	The IP address of the multilink PPP peer in a VPDN tunnel
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cvpdnbundlepeeripaddrtype
            
            	Indicates the type of address contained in cvpdnBundlePeerIpAddr
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CiscoVpdnMgmtMib.Cvpdnbundletable.Cvpdnbundleentry, self).__init__()

                self.yang_name = "cvpdnBundleEntry"
                self.yang_parent_name = "cvpdnBundleTable"

                self.cvpdnbundlename = YLeaf(YType.str, "cvpdnBundleName")

                self.cvpdnbundleendpoint = YLeaf(YType.str, "cvpdnBundleEndpoint")

                self.cvpdnbundleendpointclass = YLeaf(YType.enumeration, "cvpdnBundleEndpointClass")

                self.cvpdnbundleendpointtype = YLeaf(YType.enumeration, "cvpdnBundleEndpointType")

                self.cvpdnbundlelinkcount = YLeaf(YType.uint32, "cvpdnBundleLinkCount")

                self.cvpdnbundlepeeripaddr = YLeaf(YType.str, "cvpdnBundlePeerIpAddr")

                self.cvpdnbundlepeeripaddrtype = YLeaf(YType.enumeration, "cvpdnBundlePeerIpAddrType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cvpdnbundlename",
                                "cvpdnbundleendpoint",
                                "cvpdnbundleendpointclass",
                                "cvpdnbundleendpointtype",
                                "cvpdnbundlelinkcount",
                                "cvpdnbundlepeeripaddr",
                                "cvpdnbundlepeeripaddrtype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVpdnMgmtMib.Cvpdnbundletable.Cvpdnbundleentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVpdnMgmtMib.Cvpdnbundletable.Cvpdnbundleentry, self).__setattr__(name, value)

            class Cvpdnbundleendpointtype(Enum):
                """
                Cvpdnbundleendpointtype

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


            def has_data(self):
                return (
                    self.cvpdnbundlename.is_set or
                    self.cvpdnbundleendpoint.is_set or
                    self.cvpdnbundleendpointclass.is_set or
                    self.cvpdnbundleendpointtype.is_set or
                    self.cvpdnbundlelinkcount.is_set or
                    self.cvpdnbundlepeeripaddr.is_set or
                    self.cvpdnbundlepeeripaddrtype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cvpdnbundlename.yfilter != YFilter.not_set or
                    self.cvpdnbundleendpoint.yfilter != YFilter.not_set or
                    self.cvpdnbundleendpointclass.yfilter != YFilter.not_set or
                    self.cvpdnbundleendpointtype.yfilter != YFilter.not_set or
                    self.cvpdnbundlelinkcount.yfilter != YFilter.not_set or
                    self.cvpdnbundlepeeripaddr.yfilter != YFilter.not_set or
                    self.cvpdnbundlepeeripaddrtype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvpdnBundleEntry" + "[cvpdnBundleName='" + self.cvpdnbundlename.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/cvpdnBundleTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cvpdnbundlename.is_set or self.cvpdnbundlename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnbundlename.get_name_leafdata())
                if (self.cvpdnbundleendpoint.is_set or self.cvpdnbundleendpoint.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnbundleendpoint.get_name_leafdata())
                if (self.cvpdnbundleendpointclass.is_set or self.cvpdnbundleendpointclass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnbundleendpointclass.get_name_leafdata())
                if (self.cvpdnbundleendpointtype.is_set or self.cvpdnbundleendpointtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnbundleendpointtype.get_name_leafdata())
                if (self.cvpdnbundlelinkcount.is_set or self.cvpdnbundlelinkcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnbundlelinkcount.get_name_leafdata())
                if (self.cvpdnbundlepeeripaddr.is_set or self.cvpdnbundlepeeripaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnbundlepeeripaddr.get_name_leafdata())
                if (self.cvpdnbundlepeeripaddrtype.is_set or self.cvpdnbundlepeeripaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnbundlepeeripaddrtype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cvpdnBundleName" or name == "cvpdnBundleEndpoint" or name == "cvpdnBundleEndpointClass" or name == "cvpdnBundleEndpointType" or name == "cvpdnBundleLinkCount" or name == "cvpdnBundlePeerIpAddr" or name == "cvpdnBundlePeerIpAddrType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cvpdnBundleName"):
                    self.cvpdnbundlename = value
                    self.cvpdnbundlename.value_namespace = name_space
                    self.cvpdnbundlename.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnBundleEndpoint"):
                    self.cvpdnbundleendpoint = value
                    self.cvpdnbundleendpoint.value_namespace = name_space
                    self.cvpdnbundleendpoint.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnBundleEndpointClass"):
                    self.cvpdnbundleendpointclass = value
                    self.cvpdnbundleendpointclass.value_namespace = name_space
                    self.cvpdnbundleendpointclass.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnBundleEndpointType"):
                    self.cvpdnbundleendpointtype = value
                    self.cvpdnbundleendpointtype.value_namespace = name_space
                    self.cvpdnbundleendpointtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnBundleLinkCount"):
                    self.cvpdnbundlelinkcount = value
                    self.cvpdnbundlelinkcount.value_namespace = name_space
                    self.cvpdnbundlelinkcount.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnBundlePeerIpAddr"):
                    self.cvpdnbundlepeeripaddr = value
                    self.cvpdnbundlepeeripaddr.value_namespace = name_space
                    self.cvpdnbundlepeeripaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnBundlePeerIpAddrType"):
                    self.cvpdnbundlepeeripaddrtype = value
                    self.cvpdnbundlepeeripaddrtype.value_namespace = name_space
                    self.cvpdnbundlepeeripaddrtype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvpdnbundleentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvpdnbundleentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvpdnBundleTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvpdnBundleEntry"):
                for c in self.cvpdnbundleentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVpdnMgmtMib.Cvpdnbundletable.Cvpdnbundleentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvpdnbundleentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvpdnBundleEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cvpdnbundlechildtable(Entity):
        """
        A table that exposes the containment relationship between a
        multilink PPP bundle and a VPDN tunnel.
        
        .. attribute:: cvpdnbundlechildentry
        
        	An entry in this table represents a session that belongs to a VPDN tunnel and to a multilink PPP bundle
        	**type**\: list of    :py:class:`Cvpdnbundlechildentry <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdnbundlechildtable.Cvpdnbundlechildentry>`
        
        

        """

        _prefix = 'CISCO-VPDN-MGMT-MIB'
        _revision = '2009-06-16'

        def __init__(self):
            super(CiscoVpdnMgmtMib.Cvpdnbundlechildtable, self).__init__()

            self.yang_name = "cvpdnBundleChildTable"
            self.yang_parent_name = "CISCO-VPDN-MGMT-MIB"

            self.cvpdnbundlechildentry = YList(self)

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
                        super(CiscoVpdnMgmtMib.Cvpdnbundlechildtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoVpdnMgmtMib.Cvpdnbundlechildtable, self).__setattr__(name, value)


        class Cvpdnbundlechildentry(Entity):
            """
            An entry in this table represents a session that belongs to
            a VPDN tunnel and to a multilink PPP bundle.
            
            .. attribute:: cvpdnbundlename  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..64
            
            	**refers to**\:  :py:class:`cvpdnbundlename <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.CiscoVpdnMgmtMib.Cvpdnbundletable.Cvpdnbundleentry>`
            
            .. attribute:: cvpdnbundlechildtunneltype  <key>
            
            	The tunnel type.  This is the tunnel protocol of an active VPDN session that is associated with a multilink PPP bundle
            	**type**\:   :py:class:`Tunneltype <ydk.models.cisco_ios_xe.CISCO_VPDN_MGMT_MIB.Tunneltype>`
            
            .. attribute:: cvpdnbundlechildtunnelid  <key>
            
            	The Tunnel ID of an active VPDN session that is associated with a multilink PPP bundle
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cvpdnbundlechildsessionid  <key>
            
            	The ID of an active VPDN session that is associated with a multilink PPP bundle
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-VPDN-MGMT-MIB'
            _revision = '2009-06-16'

            def __init__(self):
                super(CiscoVpdnMgmtMib.Cvpdnbundlechildtable.Cvpdnbundlechildentry, self).__init__()

                self.yang_name = "cvpdnBundleChildEntry"
                self.yang_parent_name = "cvpdnBundleChildTable"

                self.cvpdnbundlename = YLeaf(YType.str, "cvpdnBundleName")

                self.cvpdnbundlechildtunneltype = YLeaf(YType.enumeration, "cvpdnBundleChildTunnelType")

                self.cvpdnbundlechildtunnelid = YLeaf(YType.uint32, "cvpdnBundleChildTunnelId")

                self.cvpdnbundlechildsessionid = YLeaf(YType.uint32, "cvpdnBundleChildSessionId")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cvpdnbundlename",
                                "cvpdnbundlechildtunneltype",
                                "cvpdnbundlechildtunnelid",
                                "cvpdnbundlechildsessionid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoVpdnMgmtMib.Cvpdnbundlechildtable.Cvpdnbundlechildentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoVpdnMgmtMib.Cvpdnbundlechildtable.Cvpdnbundlechildentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cvpdnbundlename.is_set or
                    self.cvpdnbundlechildtunneltype.is_set or
                    self.cvpdnbundlechildtunnelid.is_set or
                    self.cvpdnbundlechildsessionid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cvpdnbundlename.yfilter != YFilter.not_set or
                    self.cvpdnbundlechildtunneltype.yfilter != YFilter.not_set or
                    self.cvpdnbundlechildtunnelid.yfilter != YFilter.not_set or
                    self.cvpdnbundlechildsessionid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cvpdnBundleChildEntry" + "[cvpdnBundleName='" + self.cvpdnbundlename.get() + "']" + "[cvpdnBundleChildTunnelType='" + self.cvpdnbundlechildtunneltype.get() + "']" + "[cvpdnBundleChildTunnelId='" + self.cvpdnbundlechildtunnelid.get() + "']" + "[cvpdnBundleChildSessionId='" + self.cvpdnbundlechildsessionid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/cvpdnBundleChildTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cvpdnbundlename.is_set or self.cvpdnbundlename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnbundlename.get_name_leafdata())
                if (self.cvpdnbundlechildtunneltype.is_set or self.cvpdnbundlechildtunneltype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnbundlechildtunneltype.get_name_leafdata())
                if (self.cvpdnbundlechildtunnelid.is_set or self.cvpdnbundlechildtunnelid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnbundlechildtunnelid.get_name_leafdata())
                if (self.cvpdnbundlechildsessionid.is_set or self.cvpdnbundlechildsessionid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cvpdnbundlechildsessionid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cvpdnBundleName" or name == "cvpdnBundleChildTunnelType" or name == "cvpdnBundleChildTunnelId" or name == "cvpdnBundleChildSessionId"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cvpdnBundleName"):
                    self.cvpdnbundlename = value
                    self.cvpdnbundlename.value_namespace = name_space
                    self.cvpdnbundlename.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnBundleChildTunnelType"):
                    self.cvpdnbundlechildtunneltype = value
                    self.cvpdnbundlechildtunneltype.value_namespace = name_space
                    self.cvpdnbundlechildtunneltype.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnBundleChildTunnelId"):
                    self.cvpdnbundlechildtunnelid = value
                    self.cvpdnbundlechildtunnelid.value_namespace = name_space
                    self.cvpdnbundlechildtunnelid.value_namespace_prefix = name_space_prefix
                if(value_path == "cvpdnBundleChildSessionId"):
                    self.cvpdnbundlechildsessionid = value
                    self.cvpdnbundlechildsessionid.value_namespace = name_space
                    self.cvpdnbundlechildsessionid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cvpdnbundlechildentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cvpdnbundlechildentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cvpdnBundleChildTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cvpdnBundleChildEntry"):
                for c in self.cvpdnbundlechildentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoVpdnMgmtMib.Cvpdnbundlechildtable.Cvpdnbundlechildentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cvpdnbundlechildentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cvpdnBundleChildEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ciscovpdnmgmtmibnotifs is not None and self.ciscovpdnmgmtmibnotifs.has_data()) or
            (self.cvpdnbundlechildtable is not None and self.cvpdnbundlechildtable.has_data()) or
            (self.cvpdnbundletable is not None and self.cvpdnbundletable.has_data()) or
            (self.cvpdnmultilinkinfo is not None and self.cvpdnmultilinkinfo.has_data()) or
            (self.cvpdnsessionattrtable is not None and self.cvpdnsessionattrtable.has_data()) or
            (self.cvpdnsysteminfo is not None and self.cvpdnsysteminfo.has_data()) or
            (self.cvpdnsystemtable is not None and self.cvpdnsystemtable.has_data()) or
            (self.cvpdntemplatetable is not None and self.cvpdntemplatetable.has_data()) or
            (self.cvpdntunnelattrtable is not None and self.cvpdntunnelattrtable.has_data()) or
            (self.cvpdntunnelsessiontable is not None and self.cvpdntunnelsessiontable.has_data()) or
            (self.cvpdntunneltable is not None and self.cvpdntunneltable.has_data()) or
            (self.cvpdnusertofailhistinfotable is not None and self.cvpdnusertofailhistinfotable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ciscovpdnmgmtmibnotifs is not None and self.ciscovpdnmgmtmibnotifs.has_operation()) or
            (self.cvpdnbundlechildtable is not None and self.cvpdnbundlechildtable.has_operation()) or
            (self.cvpdnbundletable is not None and self.cvpdnbundletable.has_operation()) or
            (self.cvpdnmultilinkinfo is not None and self.cvpdnmultilinkinfo.has_operation()) or
            (self.cvpdnsessionattrtable is not None and self.cvpdnsessionattrtable.has_operation()) or
            (self.cvpdnsysteminfo is not None and self.cvpdnsysteminfo.has_operation()) or
            (self.cvpdnsystemtable is not None and self.cvpdnsystemtable.has_operation()) or
            (self.cvpdntemplatetable is not None and self.cvpdntemplatetable.has_operation()) or
            (self.cvpdntunnelattrtable is not None and self.cvpdntunnelattrtable.has_operation()) or
            (self.cvpdntunnelsessiontable is not None and self.cvpdntunnelsessiontable.has_operation()) or
            (self.cvpdntunneltable is not None and self.cvpdntunneltable.has_operation()) or
            (self.cvpdnusertofailhistinfotable is not None and self.cvpdnusertofailhistinfotable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-VPDN-MGMT-MIB:CISCO-VPDN-MGMT-MIB" + path_buffer

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

        if (child_yang_name == "ciscoVpdnMgmtMIBNotifs"):
            if (self.ciscovpdnmgmtmibnotifs is None):
                self.ciscovpdnmgmtmibnotifs = CiscoVpdnMgmtMib.Ciscovpdnmgmtmibnotifs()
                self.ciscovpdnmgmtmibnotifs.parent = self
                self._children_name_map["ciscovpdnmgmtmibnotifs"] = "ciscoVpdnMgmtMIBNotifs"
            return self.ciscovpdnmgmtmibnotifs

        if (child_yang_name == "cvpdnBundleChildTable"):
            if (self.cvpdnbundlechildtable is None):
                self.cvpdnbundlechildtable = CiscoVpdnMgmtMib.Cvpdnbundlechildtable()
                self.cvpdnbundlechildtable.parent = self
                self._children_name_map["cvpdnbundlechildtable"] = "cvpdnBundleChildTable"
            return self.cvpdnbundlechildtable

        if (child_yang_name == "cvpdnBundleTable"):
            if (self.cvpdnbundletable is None):
                self.cvpdnbundletable = CiscoVpdnMgmtMib.Cvpdnbundletable()
                self.cvpdnbundletable.parent = self
                self._children_name_map["cvpdnbundletable"] = "cvpdnBundleTable"
            return self.cvpdnbundletable

        if (child_yang_name == "cvpdnMultilinkInfo"):
            if (self.cvpdnmultilinkinfo is None):
                self.cvpdnmultilinkinfo = CiscoVpdnMgmtMib.Cvpdnmultilinkinfo()
                self.cvpdnmultilinkinfo.parent = self
                self._children_name_map["cvpdnmultilinkinfo"] = "cvpdnMultilinkInfo"
            return self.cvpdnmultilinkinfo

        if (child_yang_name == "cvpdnSessionAttrTable"):
            if (self.cvpdnsessionattrtable is None):
                self.cvpdnsessionattrtable = CiscoVpdnMgmtMib.Cvpdnsessionattrtable()
                self.cvpdnsessionattrtable.parent = self
                self._children_name_map["cvpdnsessionattrtable"] = "cvpdnSessionAttrTable"
            return self.cvpdnsessionattrtable

        if (child_yang_name == "cvpdnSystemInfo"):
            if (self.cvpdnsysteminfo is None):
                self.cvpdnsysteminfo = CiscoVpdnMgmtMib.Cvpdnsysteminfo()
                self.cvpdnsysteminfo.parent = self
                self._children_name_map["cvpdnsysteminfo"] = "cvpdnSystemInfo"
            return self.cvpdnsysteminfo

        if (child_yang_name == "cvpdnSystemTable"):
            if (self.cvpdnsystemtable is None):
                self.cvpdnsystemtable = CiscoVpdnMgmtMib.Cvpdnsystemtable()
                self.cvpdnsystemtable.parent = self
                self._children_name_map["cvpdnsystemtable"] = "cvpdnSystemTable"
            return self.cvpdnsystemtable

        if (child_yang_name == "cvpdnTemplateTable"):
            if (self.cvpdntemplatetable is None):
                self.cvpdntemplatetable = CiscoVpdnMgmtMib.Cvpdntemplatetable()
                self.cvpdntemplatetable.parent = self
                self._children_name_map["cvpdntemplatetable"] = "cvpdnTemplateTable"
            return self.cvpdntemplatetable

        if (child_yang_name == "cvpdnTunnelAttrTable"):
            if (self.cvpdntunnelattrtable is None):
                self.cvpdntunnelattrtable = CiscoVpdnMgmtMib.Cvpdntunnelattrtable()
                self.cvpdntunnelattrtable.parent = self
                self._children_name_map["cvpdntunnelattrtable"] = "cvpdnTunnelAttrTable"
            return self.cvpdntunnelattrtable

        if (child_yang_name == "cvpdnTunnelSessionTable"):
            if (self.cvpdntunnelsessiontable is None):
                self.cvpdntunnelsessiontable = CiscoVpdnMgmtMib.Cvpdntunnelsessiontable()
                self.cvpdntunnelsessiontable.parent = self
                self._children_name_map["cvpdntunnelsessiontable"] = "cvpdnTunnelSessionTable"
            return self.cvpdntunnelsessiontable

        if (child_yang_name == "cvpdnTunnelTable"):
            if (self.cvpdntunneltable is None):
                self.cvpdntunneltable = CiscoVpdnMgmtMib.Cvpdntunneltable()
                self.cvpdntunneltable.parent = self
                self._children_name_map["cvpdntunneltable"] = "cvpdnTunnelTable"
            return self.cvpdntunneltable

        if (child_yang_name == "cvpdnUserToFailHistInfoTable"):
            if (self.cvpdnusertofailhistinfotable is None):
                self.cvpdnusertofailhistinfotable = CiscoVpdnMgmtMib.Cvpdnusertofailhistinfotable()
                self.cvpdnusertofailhistinfotable.parent = self
                self._children_name_map["cvpdnusertofailhistinfotable"] = "cvpdnUserToFailHistInfoTable"
            return self.cvpdnusertofailhistinfotable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ciscoVpdnMgmtMIBNotifs" or name == "cvpdnBundleChildTable" or name == "cvpdnBundleTable" or name == "cvpdnMultilinkInfo" or name == "cvpdnSessionAttrTable" or name == "cvpdnSystemInfo" or name == "cvpdnSystemTable" or name == "cvpdnTemplateTable" or name == "cvpdnTunnelAttrTable" or name == "cvpdnTunnelSessionTable" or name == "cvpdnTunnelTable" or name == "cvpdnUserToFailHistInfoTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoVpdnMgmtMib()
        return self._top_entity


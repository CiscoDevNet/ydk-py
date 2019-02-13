""" TUNNEL_MIB 

The MIB module for management of IP Tunnels,
independent of the specific encapsulation scheme in
use.

Copyright (C) The Internet Society (2005).  This
version of this MIB module is part of RFC 4087;  see
the RFC itself for full legal notices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class TUNNELMIB(Entity):
    """
    
    
    .. attribute:: tunneliftable
    
    	The (conceptual) table containing information on configured tunnels
    	**type**\:  :py:class:`TunnelIfTable <ydk.models.cisco_ios_xe.TUNNEL_MIB.TUNNELMIB.TunnelIfTable>`
    
    	**config**\: False
    
    .. attribute:: tunnelconfigtable
    
    	The (conceptual) table containing information on configured tunnels.  This table can be used to map a set of tunnel endpoints to the associated ifIndex value.  It can also be used for row creation.  Note that every row in the tunnelIfTable with a fixed IPv4 destination address should have a corresponding row in the tunnelConfigTable, regardless of whether it was created via SNMP.  Since this table does not support IPv6, it is deprecated in favor of tunnelInetConfigTable
    	**type**\:  :py:class:`TunnelConfigTable <ydk.models.cisco_ios_xe.TUNNEL_MIB.TUNNELMIB.TunnelConfigTable>`
    
    	**config**\: False
    
    	**status**\: deprecated
    
    .. attribute:: tunnelinetconfigtable
    
    	The (conceptual) table containing information on configured tunnels.  This table can be used to map a set of tunnel endpoints to the associated ifIndex value.  It can also be used for row creation.  Note that every row in the tunnelIfTable with a fixed destination address should have a corresponding row in the tunnelInetConfigTable, regardless of whether it was created via SNMP
    	**type**\:  :py:class:`TunnelInetConfigTable <ydk.models.cisco_ios_xe.TUNNEL_MIB.TUNNELMIB.TunnelInetConfigTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'TUNNEL-MIB'
    _revision = '2005-05-16'

    def __init__(self):
        super(TUNNELMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "TUNNEL-MIB"
        self.yang_parent_name = "TUNNEL-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("tunnelIfTable", ("tunneliftable", TUNNELMIB.TunnelIfTable)), ("tunnelConfigTable", ("tunnelconfigtable", TUNNELMIB.TunnelConfigTable)), ("tunnelInetConfigTable", ("tunnelinetconfigtable", TUNNELMIB.TunnelInetConfigTable))])
        self._leafs = OrderedDict()

        self.tunneliftable = TUNNELMIB.TunnelIfTable()
        self.tunneliftable.parent = self
        self._children_name_map["tunneliftable"] = "tunnelIfTable"

        self.tunnelconfigtable = TUNNELMIB.TunnelConfigTable()
        self.tunnelconfigtable.parent = self
        self._children_name_map["tunnelconfigtable"] = "tunnelConfigTable"

        self.tunnelinetconfigtable = TUNNELMIB.TunnelInetConfigTable()
        self.tunnelinetconfigtable.parent = self
        self._children_name_map["tunnelinetconfigtable"] = "tunnelInetConfigTable"
        self._segment_path = lambda: "TUNNEL-MIB:TUNNEL-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(TUNNELMIB, [], name, value)


    class TunnelIfTable(Entity):
        """
        The (conceptual) table containing information on
        configured tunnels.
        
        .. attribute:: tunnelifentry
        
        	An entry (conceptual row) containing the information on a particular configured tunnel
        	**type**\: list of  		 :py:class:`TunnelIfEntry <ydk.models.cisco_ios_xe.TUNNEL_MIB.TUNNELMIB.TunnelIfTable.TunnelIfEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'TUNNEL-MIB'
        _revision = '2005-05-16'

        def __init__(self):
            super(TUNNELMIB.TunnelIfTable, self).__init__()

            self.yang_name = "tunnelIfTable"
            self.yang_parent_name = "TUNNEL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tunnelIfEntry", ("tunnelifentry", TUNNELMIB.TunnelIfTable.TunnelIfEntry))])
            self._leafs = OrderedDict()

            self.tunnelifentry = YList(self)
            self._segment_path = lambda: "tunnelIfTable"
            self._absolute_path = lambda: "TUNNEL-MIB:TUNNEL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TUNNELMIB.TunnelIfTable, [], name, value)


        class TunnelIfEntry(Entity):
            """
            An entry (conceptual row) containing the information
            on a particular configured tunnel.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: tunneliflocaladdress
            
            	The address of the local endpoint of the tunnel (i.e., the source address used in the outer IP header), or 0.0.0.0 if unknown or if the tunnel is over IPv6.  Since this object does not support IPv6, it is deprecated in favor of tunnelIfLocalInetAddress
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: tunnelifremoteaddress
            
            	The address of the remote endpoint of the tunnel (i.e., the destination address used in the outer IP header), or 0.0.0.0 if unknown, or an IPv6 address, or  the tunnel is not a point\-to\-point link (e.g., if it is a 6to4 tunnel).  Since this object does not support IPv6, it is deprecated in favor of tunnelIfRemoteInetAddress
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: tunnelifencapsmethod
            
            	The encapsulation method used by the tunnel
            	**type**\:  :py:class:`IANAtunnelType <ydk.models.cisco_ios_xe.IANAifType_MIB.IANAtunnelType>`
            
            	**config**\: False
            
            .. attribute:: tunnelifhoplimit
            
            	The IPv4 TTL or IPv6 Hop Limit to use in the outer IP header.  A value of 0 indicates that the value is copied from the payload's header
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: tunnelifsecurity
            
            	The method used by the tunnel to secure the outer IP header.  The value ipsec indicates that IPsec is used between the tunnel endpoints for authentication or encryption or both.  More specific security\-related information may be available in a MIB module for the security protocol in use
            	**type**\:  :py:class:`TunnelIfSecurity <ydk.models.cisco_ios_xe.TUNNEL_MIB.TUNNELMIB.TunnelIfTable.TunnelIfEntry.TunnelIfSecurity>`
            
            	**config**\: False
            
            .. attribute:: tunneliftos
            
            	The method used to set the high 6 bits (the  differentiated services codepoint) of the IPv4 TOS or IPv6 Traffic Class in the outer IP header.  A value of \-1 indicates that the bits are copied from the payload's header.  A value of \-2 indicates that a traffic conditioner is invoked and more information may be available in a traffic conditioner MIB module. A value between 0 and 63 inclusive indicates that the bit field is set to the indicated value.  Note\: instead of the name tunnelIfTOS, a better name would have been tunnelIfDSCPMethod, but the existing name appeared in RFC 2667 and existing objects cannot be renamed
            	**type**\: int
            
            	**range:** \-2..63
            
            	**config**\: False
            
            .. attribute:: tunnelifflowlabel
            
            	The method used to set the IPv6 Flow Label value. This object need not be present in rows where tunnelIfAddressType indicates the tunnel is not over IPv6.  A value of \-1 indicates that a traffic conditioner is invoked and more information may be available in a traffic conditioner MIB.  Any other value indicates that the Flow Label field is set to the indicated value
            	**type**\: int
            
            	**range:** \-1..100
            
            	**config**\: False
            
            .. attribute:: tunnelifaddresstype
            
            	The type of address in the corresponding tunnelIfLocalInetAddress and tunnelIfRemoteInetAddress objects
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: tunneliflocalinetaddress
            
            	The address of the local endpoint of the tunnel (i.e., the source address used in the outer IP header).  If the address is unknown, the value is  0.0.0.0 for IPv4 or \:\: for IPv6.  The type of this object is given by tunnelIfAddressType
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: tunnelifremoteinetaddress
            
            	The address of the remote endpoint of the tunnel (i.e., the destination address used in the outer IP header).  If the address is unknown or the tunnel is not a point\-to\-point link (e.g., if it is a 6to4 tunnel), the value is 0.0.0.0 for tunnels over IPv4 or \:\: for tunnels over IPv6.  The type of this object is given by tunnelIfAddressType
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: tunnelifencapslimit
            
            	The maximum number of additional encapsulations permitted for packets undergoing encapsulation at this node.  A value of \-1 indicates that no limit is present (except as a result of the packet size)
            	**type**\: int
            
            	**range:** \-1..255
            
            	**config**\: False
            
            

            """

            _prefix = 'TUNNEL-MIB'
            _revision = '2005-05-16'

            def __init__(self):
                super(TUNNELMIB.TunnelIfTable.TunnelIfEntry, self).__init__()

                self.yang_name = "tunnelIfEntry"
                self.yang_parent_name = "tunnelIfTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('tunneliflocaladdress', (YLeaf(YType.str, 'tunnelIfLocalAddress'), ['str'])),
                    ('tunnelifremoteaddress', (YLeaf(YType.str, 'tunnelIfRemoteAddress'), ['str'])),
                    ('tunnelifencapsmethod', (YLeaf(YType.enumeration, 'tunnelIfEncapsMethod'), [('ydk.models.cisco_ios_xe.IANAifType_MIB', 'IANAtunnelType', '')])),
                    ('tunnelifhoplimit', (YLeaf(YType.int32, 'tunnelIfHopLimit'), ['int'])),
                    ('tunnelifsecurity', (YLeaf(YType.enumeration, 'tunnelIfSecurity'), [('ydk.models.cisco_ios_xe.TUNNEL_MIB', 'TUNNELMIB', 'TunnelIfTable.TunnelIfEntry.TunnelIfSecurity')])),
                    ('tunneliftos', (YLeaf(YType.int32, 'tunnelIfTOS'), ['int'])),
                    ('tunnelifflowlabel', (YLeaf(YType.int32, 'tunnelIfFlowLabel'), ['int'])),
                    ('tunnelifaddresstype', (YLeaf(YType.enumeration, 'tunnelIfAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('tunneliflocalinetaddress', (YLeaf(YType.str, 'tunnelIfLocalInetAddress'), ['str'])),
                    ('tunnelifremoteinetaddress', (YLeaf(YType.str, 'tunnelIfRemoteInetAddress'), ['str'])),
                    ('tunnelifencapslimit', (YLeaf(YType.int32, 'tunnelIfEncapsLimit'), ['int'])),
                ])
                self.ifindex = None
                self.tunneliflocaladdress = None
                self.tunnelifremoteaddress = None
                self.tunnelifencapsmethod = None
                self.tunnelifhoplimit = None
                self.tunnelifsecurity = None
                self.tunneliftos = None
                self.tunnelifflowlabel = None
                self.tunnelifaddresstype = None
                self.tunneliflocalinetaddress = None
                self.tunnelifremoteinetaddress = None
                self.tunnelifencapslimit = None
                self._segment_path = lambda: "tunnelIfEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "TUNNEL-MIB:TUNNEL-MIB/tunnelIfTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TUNNELMIB.TunnelIfTable.TunnelIfEntry, ['ifindex', 'tunneliflocaladdress', 'tunnelifremoteaddress', 'tunnelifencapsmethod', 'tunnelifhoplimit', 'tunnelifsecurity', 'tunneliftos', 'tunnelifflowlabel', 'tunnelifaddresstype', 'tunneliflocalinetaddress', 'tunnelifremoteinetaddress', 'tunnelifencapslimit'], name, value)

            class TunnelIfSecurity(Enum):
                """
                TunnelIfSecurity (Enum Class)

                The method used by the tunnel to secure the outer IP

                header.  The value ipsec indicates that IPsec is used

                between the tunnel endpoints for authentication or

                encryption or both.  More specific security\-related

                information may be available in a MIB module for the

                security protocol in use.

                .. data:: none = 1

                .. data:: ipsec = 2

                .. data:: other = 3

                """

                none = Enum.YLeaf(1, "none")

                ipsec = Enum.YLeaf(2, "ipsec")

                other = Enum.YLeaf(3, "other")





    class TunnelConfigTable(Entity):
        """
        The (conceptual) table containing information on
        configured tunnels.  This table can be used to map a
        set of tunnel endpoints to the associated ifIndex
        value.  It can also be used for row creation.  Note
        that every row in the tunnelIfTable with a fixed IPv4
        destination address should have a corresponding row in
        the tunnelConfigTable, regardless of whether it was
        created via SNMP.
        
        Since this table does not support IPv6, it is
        deprecated in favor of tunnelInetConfigTable.
        
        .. attribute:: tunnelconfigentry
        
        	An entry (conceptual row) containing the information on a particular configured tunnel.  Since this entry does not support IPv6, it is deprecated in favor of tunnelInetConfigEntry
        	**type**\: list of  		 :py:class:`TunnelConfigEntry <ydk.models.cisco_ios_xe.TUNNEL_MIB.TUNNELMIB.TunnelConfigTable.TunnelConfigEntry>`
        
        	**config**\: False
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'TUNNEL-MIB'
        _revision = '2005-05-16'

        def __init__(self):
            super(TUNNELMIB.TunnelConfigTable, self).__init__()

            self.yang_name = "tunnelConfigTable"
            self.yang_parent_name = "TUNNEL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tunnelConfigEntry", ("tunnelconfigentry", TUNNELMIB.TunnelConfigTable.TunnelConfigEntry))])
            self._leafs = OrderedDict()

            self.tunnelconfigentry = YList(self)
            self._segment_path = lambda: "tunnelConfigTable"
            self._absolute_path = lambda: "TUNNEL-MIB:TUNNEL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TUNNELMIB.TunnelConfigTable, [], name, value)


        class TunnelConfigEntry(Entity):
            """
            An entry (conceptual row) containing the information
            on a particular configured tunnel.
            
            Since this entry does not support IPv6, it is
            deprecated in favor of tunnelInetConfigEntry.
            
            .. attribute:: tunnelconfiglocaladdress  (key)
            
            	The address of the local endpoint of the tunnel, or 0.0.0.0 if the device is free to choose any of its addresses at tunnel establishment time.  Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigLocalAddress
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: tunnelconfigremoteaddress  (key)
            
            	The address of the remote endpoint of the tunnel.  Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigRemoteAddress
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: tunnelconfigencapsmethod  (key)
            
            	The encapsulation method used by the tunnel.  Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigEncapsMethod
            	**type**\:  :py:class:`IANAtunnelType <ydk.models.cisco_ios_xe.IANAifType_MIB.IANAtunnelType>`
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: tunnelconfigid  (key)
            
            	An identifier used to distinguish between multiple tunnels of the same encapsulation method, with the same endpoints.  If the encapsulation protocol only allows one tunnel per set of endpoint addresses (such as for GRE or IP\-in\-IP), the value of this object is 1.  For encapsulation methods (such as L2F) which allow multiple parallel tunnels, the manager is responsible for choosing any ID which does not conflict with an existing row, such as choosing a random number.  Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigID
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: tunnelconfigifindex
            
            	If the value of tunnelConfigStatus for this row is active, then this object contains the value of ifIndex corresponding to the tunnel interface.  A value of 0 is not legal in the active state, and means that the interface index has not yet been assigned.  Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigIfIndex
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: tunnelconfigstatus
            
            	The status of this row, by which new entries may be created, or old entries deleted from this table.  The agent need not support setting this object to createAndWait or notInService since there are no other writable objects in this table, and writable objects in rows of corresponding tables such as the tunnelIfTable may be modified while this row is active.  To create a row in this table for an encapsulation method which does not support multiple parallel tunnels with the same endpoints, the management station should simply use a tunnelConfigID of 1, and set tunnelConfigStatus to createAndGo.  For encapsulation methods such as L2F which allow multiple parallel tunnels, the management station may select a pseudo\-random number to use as the tunnelConfigID and set tunnelConfigStatus to createAndGo.  In the event that this ID is already in use and an inconsistentValue is returned in response to the set operation, the management station should simply select a new pseudo\-random number and retry the operation.  Creating a row in this table will cause an interface index to be assigned by the agent in an implementation\-dependent manner, and corresponding rows will be instantiated in the ifTable and the tunnelIfTable.  The status of this row will become active as soon as the agent assigns the interface index, regardless of whether the interface is operationally up.  Deleting a row in this table will likewise delete the corresponding row in the ifTable and in the tunnelIfTable.  Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigStatus
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'TUNNEL-MIB'
            _revision = '2005-05-16'

            def __init__(self):
                super(TUNNELMIB.TunnelConfigTable.TunnelConfigEntry, self).__init__()

                self.yang_name = "tunnelConfigEntry"
                self.yang_parent_name = "tunnelConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['tunnelconfiglocaladdress','tunnelconfigremoteaddress','tunnelconfigencapsmethod','tunnelconfigid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('tunnelconfiglocaladdress', (YLeaf(YType.str, 'tunnelConfigLocalAddress'), ['str'])),
                    ('tunnelconfigremoteaddress', (YLeaf(YType.str, 'tunnelConfigRemoteAddress'), ['str'])),
                    ('tunnelconfigencapsmethod', (YLeaf(YType.enumeration, 'tunnelConfigEncapsMethod'), [('ydk.models.cisco_ios_xe.IANAifType_MIB', 'IANAtunnelType', '')])),
                    ('tunnelconfigid', (YLeaf(YType.int32, 'tunnelConfigID'), ['int'])),
                    ('tunnelconfigifindex', (YLeaf(YType.int32, 'tunnelConfigIfIndex'), ['int'])),
                    ('tunnelconfigstatus', (YLeaf(YType.enumeration, 'tunnelConfigStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.tunnelconfiglocaladdress = None
                self.tunnelconfigremoteaddress = None
                self.tunnelconfigencapsmethod = None
                self.tunnelconfigid = None
                self.tunnelconfigifindex = None
                self.tunnelconfigstatus = None
                self._segment_path = lambda: "tunnelConfigEntry" + "[tunnelConfigLocalAddress='" + str(self.tunnelconfiglocaladdress) + "']" + "[tunnelConfigRemoteAddress='" + str(self.tunnelconfigremoteaddress) + "']" + "[tunnelConfigEncapsMethod='" + str(self.tunnelconfigencapsmethod) + "']" + "[tunnelConfigID='" + str(self.tunnelconfigid) + "']"
                self._absolute_path = lambda: "TUNNEL-MIB:TUNNEL-MIB/tunnelConfigTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TUNNELMIB.TunnelConfigTable.TunnelConfigEntry, ['tunnelconfiglocaladdress', 'tunnelconfigremoteaddress', 'tunnelconfigencapsmethod', 'tunnelconfigid', 'tunnelconfigifindex', 'tunnelconfigstatus'], name, value)




    class TunnelInetConfigTable(Entity):
        """
        The (conceptual) table containing information on
        configured tunnels.  This table can be used to map a
        set of tunnel endpoints to the associated ifIndex
        value.  It can also be used for row creation.  Note
        that every row in the tunnelIfTable with a fixed
        destination address should have a corresponding row in
        the tunnelInetConfigTable, regardless of whether it
        was created via SNMP.
        
        .. attribute:: tunnelinetconfigentry
        
        	An entry (conceptual row) containing the information on a particular configured tunnel.  Note that there is a 128 subid maximum for object OIDs.  Implementers need to be aware that if the total number of octets in tunnelInetConfigLocalAddress and tunnelInetConfigRemoteAddress exceeds 110 then OIDs of column instances in this table will have more than 128 sub\-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3.  In practice this is not expected to be a problem since IPv4 and IPv6 addresses will not cause the limit to be reached, but if other types are supported by an agent, care must be taken to ensure that the sum of the lengths do not cause the limit to be exceeded
        	**type**\: list of  		 :py:class:`TunnelInetConfigEntry <ydk.models.cisco_ios_xe.TUNNEL_MIB.TUNNELMIB.TunnelInetConfigTable.TunnelInetConfigEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'TUNNEL-MIB'
        _revision = '2005-05-16'

        def __init__(self):
            super(TUNNELMIB.TunnelInetConfigTable, self).__init__()

            self.yang_name = "tunnelInetConfigTable"
            self.yang_parent_name = "TUNNEL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tunnelInetConfigEntry", ("tunnelinetconfigentry", TUNNELMIB.TunnelInetConfigTable.TunnelInetConfigEntry))])
            self._leafs = OrderedDict()

            self.tunnelinetconfigentry = YList(self)
            self._segment_path = lambda: "tunnelInetConfigTable"
            self._absolute_path = lambda: "TUNNEL-MIB:TUNNEL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TUNNELMIB.TunnelInetConfigTable, [], name, value)


        class TunnelInetConfigEntry(Entity):
            """
            An entry (conceptual row) containing the information
            on a particular configured tunnel.  Note that there is
            a 128 subid maximum for object OIDs.  Implementers
            need to be aware that if the total number of octets in
            tunnelInetConfigLocalAddress and
            tunnelInetConfigRemoteAddress exceeds 110 then OIDs of
            column instances in this table will have more than 128
            sub\-identifiers and cannot be accessed using SNMPv1,
            SNMPv2c, or SNMPv3.  In practice this is not expected
            to be a problem since IPv4 and IPv6 addresses will not
            cause the limit to be reached, but if other types are
            supported by an agent, care must be taken to ensure
            that the sum of the lengths do not cause the limit to
            be exceeded.
            
            .. attribute:: tunnelinetconfigaddresstype  (key)
            
            	The address type over which the tunnel encapsulates packets
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: tunnelinetconfiglocaladdress  (key)
            
            	The address of the local endpoint of the tunnel, or 0.0.0.0 (for IPv4) or \:\: (for IPv6) if the device is free to choose any of its addresses at tunnel establishment time
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: tunnelinetconfigremoteaddress  (key)
            
            	The address of the remote endpoint of the tunnel
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: tunnelinetconfigencapsmethod  (key)
            
            	The encapsulation method used by the tunnel
            	**type**\:  :py:class:`IANAtunnelType <ydk.models.cisco_ios_xe.IANAifType_MIB.IANAtunnelType>`
            
            	**config**\: False
            
            .. attribute:: tunnelinetconfigid  (key)
            
            	An identifier used to distinguish between multiple tunnels of the same encapsulation method, with the same endpoints.  If the encapsulation protocol only allows one tunnel per set of endpoint addresses (such as for GRE or IP\-in\-IP), the value of this object is 1.  For encapsulation methods (such as L2F) which allow multiple parallel tunnels, the manager is responsible for choosing any ID which does not  conflict with an existing row, such as choosing a random number
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: tunnelinetconfigifindex
            
            	If the value of tunnelInetConfigStatus for this row is active, then this object contains the value of ifIndex corresponding to the tunnel interface.  A value of 0 is not legal in the active state, and means that the interface index has not yet been assigned
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: tunnelinetconfigstatus
            
            	The status of this row, by which new entries may be created, or old entries deleted from this table.  The agent need not support setting this object to createAndWait or notInService since there are no other writable objects in this table, and writable objects in rows of corresponding tables such as the tunnelIfTable may be modified while this row is active.  To create a row in this table for an encapsulation method which does not support multiple parallel tunnels with the same endpoints, the management station should simply use a tunnelInetConfigID of 1, and set tunnelInetConfigStatus to createAndGo.  For encapsulation methods such as L2F which allow multiple parallel tunnels, the management station may select a pseudo\-random number to use as the tunnelInetConfigID and set tunnelInetConfigStatus to createAndGo.  In the event that this ID is already in use and an inconsistentValue is returned in response to the set operation, the management station should simply select a new pseudo\-random number and retry the operation.  Creating a row in this table will cause an interface index to be assigned by the agent in an implementation\-dependent manner, and corresponding rows will be instantiated in the ifTable and the  tunnelIfTable.  The status of this row will become active as soon as the agent assigns the interface index, regardless of whether the interface is operationally up.  Deleting a row in this table will likewise delete the corresponding row in the ifTable and in the tunnelIfTable
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: tunnelinetconfigstoragetype
            
            	The storage type of this row.  If the row is permanent(4), no objects in the row need be writable
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            	**config**\: False
            
            

            """

            _prefix = 'TUNNEL-MIB'
            _revision = '2005-05-16'

            def __init__(self):
                super(TUNNELMIB.TunnelInetConfigTable.TunnelInetConfigEntry, self).__init__()

                self.yang_name = "tunnelInetConfigEntry"
                self.yang_parent_name = "tunnelInetConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['tunnelinetconfigaddresstype','tunnelinetconfiglocaladdress','tunnelinetconfigremoteaddress','tunnelinetconfigencapsmethod','tunnelinetconfigid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('tunnelinetconfigaddresstype', (YLeaf(YType.enumeration, 'tunnelInetConfigAddressType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('tunnelinetconfiglocaladdress', (YLeaf(YType.str, 'tunnelInetConfigLocalAddress'), ['str'])),
                    ('tunnelinetconfigremoteaddress', (YLeaf(YType.str, 'tunnelInetConfigRemoteAddress'), ['str'])),
                    ('tunnelinetconfigencapsmethod', (YLeaf(YType.enumeration, 'tunnelInetConfigEncapsMethod'), [('ydk.models.cisco_ios_xe.IANAifType_MIB', 'IANAtunnelType', '')])),
                    ('tunnelinetconfigid', (YLeaf(YType.int32, 'tunnelInetConfigID'), ['int'])),
                    ('tunnelinetconfigifindex', (YLeaf(YType.int32, 'tunnelInetConfigIfIndex'), ['int'])),
                    ('tunnelinetconfigstatus', (YLeaf(YType.enumeration, 'tunnelInetConfigStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('tunnelinetconfigstoragetype', (YLeaf(YType.enumeration, 'tunnelInetConfigStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                ])
                self.tunnelinetconfigaddresstype = None
                self.tunnelinetconfiglocaladdress = None
                self.tunnelinetconfigremoteaddress = None
                self.tunnelinetconfigencapsmethod = None
                self.tunnelinetconfigid = None
                self.tunnelinetconfigifindex = None
                self.tunnelinetconfigstatus = None
                self.tunnelinetconfigstoragetype = None
                self._segment_path = lambda: "tunnelInetConfigEntry" + "[tunnelInetConfigAddressType='" + str(self.tunnelinetconfigaddresstype) + "']" + "[tunnelInetConfigLocalAddress='" + str(self.tunnelinetconfiglocaladdress) + "']" + "[tunnelInetConfigRemoteAddress='" + str(self.tunnelinetconfigremoteaddress) + "']" + "[tunnelInetConfigEncapsMethod='" + str(self.tunnelinetconfigencapsmethod) + "']" + "[tunnelInetConfigID='" + str(self.tunnelinetconfigid) + "']"
                self._absolute_path = lambda: "TUNNEL-MIB:TUNNEL-MIB/tunnelInetConfigTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TUNNELMIB.TunnelInetConfigTable.TunnelInetConfigEntry, ['tunnelinetconfigaddresstype', 'tunnelinetconfiglocaladdress', 'tunnelinetconfigremoteaddress', 'tunnelinetconfigencapsmethod', 'tunnelinetconfigid', 'tunnelinetconfigifindex', 'tunnelinetconfigstatus', 'tunnelinetconfigstoragetype'], name, value)



    def clone_ptr(self):
        self._top_entity = TUNNELMIB()
        return self._top_entity



